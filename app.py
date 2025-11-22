import random
import numpy as np
from numpy.linalg import norm
import spacy
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from mahjong_kb import KNOWLEDGE_BASE


# 1. UTILITY FUNCTIONS
# handle vector math and text preparation.

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    """
    Calculates cosine similarity between two vectors (a and b).
    Used for comparing query vectors with knowledge base vectors.
    """
    if a is None or b is None:
        return 0.0
    na = norm(a)
    nb = norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))


def build_doc_text(entry, lang: str = "en") -> str:
    """
    Combines all text fields of a rule entry into a single string, then turned into a vector for semantic search.
    """
    info = entry[lang]
    text = " ".join([
        info.get("title", ""),
        " ".join(info.get("question_examples", [])),
        info.get("definition", ""),
        info.get("when_it_happens", ""),
        info.get("examples", ""),
        info.get("newbie_tip", ""),
    ])
    return text


def build_kb_vectors_en(kb, nlp_en):
    """
    Pre-computes vectors for all English rules using spaCy.
    Returns:
      - vectors: numpy array of shape (N_rules, vector_dim)
    """
    vectors = []
    for entry in kb:
        doc_text = build_doc_text(entry, lang="en")
        doc = nlp_en(doc_text)
        vectors.append(doc.vector)
    return np.vstack(vectors)


def build_tfidf_zh(kb):
    """
    Builds a TF-IDF model for Chinese rules.
    use character-level n-grams (2-4 chars) to capture meaning.
    Returns:
      - vectorizer: The fitted TF-IDF object
      - doc_matrix: The sparse matrix of rule vectors
    """
    corpus = []
    for entry in kb:
        doc_text = build_doc_text(entry, lang="zh")
        corpus.append(doc_text)

    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
    doc_matrix = vectorizer.fit_transform(corpus)
    return vectorizer, doc_matrix


# 2. encapsulate the search logic for each language.

class SpacyEnglishMahjongQA:
    """
    English QA Engine using spaCy embeddings.
    Matches user queries to rules based on semantic meaning.
    """
    def __init__(self, kb, nlp_en, kb_vecs_en):
        self.kb = kb
        self.nlp_en = nlp_en
        self.kb_vecs_en = kb_vecs_en

    def retrieve(self, query: str, top_k: int = 3):
        # Convert user query to vector
        doc = self.nlp_en(query)
        q_vec = doc.vector

        # Compare against all rule vectors
        sims = []
        for vec in self.kb_vecs_en:
            sims.append(cosine_sim(q_vec, vec))
        sims = np.array(sims)

        # Sort by similarity (descending)
        top_idx = np.argsort(sims)[::-1][:top_k]
        
        # Format results
        results = []
        for idx in top_idx:
            entry = self.kb[idx]
            score = float(sims[idx])
            results.append({
                "id": entry["id"],
                "score": score,
                "content": entry["en"]
            })
        return results


class TfidfChineseMahjongQA:
    """
    Chinese QA Engine using TF-IDF + Cosine Similarity.
    Matches user queries based on keyword overlap and n-gram features.
    """
    def __init__(self, kb, vectorizer_zh, doc_matrix_zh):
        self.kb = kb
        self.vectorizer_zh = vectorizer_zh
        self.doc_matrix_zh = doc_matrix_zh

    def retrieve(self, query: str, top_k: int = 3):
        # Convert user query to TF-IDF vector
        q_vec = self.vectorizer_zh.transform([query])
        # Compute similarity against all rules
        sims = cosine_similarity(q_vec, self.doc_matrix_zh)[0]

        # Sort by similarity
        top_idx = np.argsort(sims)[::-1][:top_k]
        
        results = []
        for idx in top_idx:
            entry = self.kb[idx]
            score = float(sims[idx])
            results.append({
                "id": entry["id"],
                "score": score,
                "content": entry["zh"]
            })
        return results


# 3. initialization

@st.cache_resource
def load_models():
    nlp_en = spacy.load("en_core_web_sm")
    kb_vecs_en = build_kb_vectors_en(KNOWLEDGE_BASE, nlp_en)
    qa_en = SpacyEnglishMahjongQA(KNOWLEDGE_BASE, nlp_en, kb_vecs_en)

    vectorizer_zh, doc_matrix_zh = build_tfidf_zh(KNOWLEDGE_BASE)
    qa_zh = TfidfChineseMahjongQA(KNOWLEDGE_BASE, vectorizer_zh, doc_matrix_zh)

    return qa_en, qa_zh

qa_en, qa_zh = load_models()


# 4. STREAMLIT UI

st.set_page_config(
    page_title="Sichuan Mahjong Assistant",
    page_icon="🀄",
    layout="centered"
)

st.markdown("""
<style>
    /* Global Settings */
    html, body, [class*="css"] {
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
        background-color: #f7f9f5; 
        color: #2f3e2f;            
    }
    
    /* Headers */
    h1 {
        font-weight: 700 !important;
        color: #3a5a40; 
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
    }
    h2, h3, h4 {
        font-weight: 600 !important;
        color: #588157; 
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #eff3ee; 
        border-right: 1px solid #dbe4d8;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #3a5a40;
    }

    /* Primary Action Button */
    .stButton > button {
        width: 100%;
        border-radius: 4px;
        background-color: #588157; 
        color: #fff;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #3a5a40; 
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        color: #fff;
    }

    /* Input Fields */
    .stTextInput > div > div > input {
        border-radius: 4px;
        padding: 0.5rem 1rem;
        border: 1px solid #a3b18a; 
        background-color: #ffffff;
    }
    
    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        border-bottom: 1px solid #dbe4d8;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        background-color: transparent;
        border-radius: 0;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #588157;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: transparent;
        color: #3a5a40;
        font-weight: 600;
    }

    /* Alerts/Warnings */
    .stAlert {
        border-radius: 4px;
        background-color: #e9edc9; 
        border: 1px solid #ccd5ae;
        color: #2f3e2f;
    }
</style>
""", unsafe_allow_html=True)


# 5. SIDEBAR & HEADER

with st.sidebar:
    st.header("Settings / 设置")
    lang = st.radio("Language / 语言", ["English", "中文"], index=0)

    st.subheader("About / 关于")
    if lang == "English":
        st.write(
            "This assistant connects your questions to the "
            "**Sichuan Mahjong rule**, explaining what it means and how beginners should react."
        )
    else:
        st.write(
            "这个小助手会把你的问题对应到 **四川麻将规则**，"
            "说明它的含义以及新手该怎么应对。"
        )

# Main Title area
if lang == "English":
    st.title("Sichuan Mahjong Assistant")
    st.write("Type any question about **Sichuan Mahjong rules**.")
else:
    st.title("四川麻将小助手")
    st.write("用中文输入任何你听不懂的 **川麻规则相关问题**。")


# 6. RANDOM QUESTIONS

sample_questions_en = [
    "What is hua zhu?",
    "What does ding que mean?",
    "Why do we keep playing after someone wins?",
    "What is the rule where we exchange tiles at the beginning?"
]
sample_questions_zh = [
    "为什么要换三张？",
    "定缺是什么？",
    "什么是花猪？",
    "胡了之后为什么还要继续打？",
]

question_key = "question_input"
question_lang_key = "question_lang"
sample_pool = sample_questions_en if lang == "English" else sample_questions_zh

# Initialize session state if needed
if question_lang_key not in st.session_state:
    st.session_state[question_lang_key] = lang
if question_key not in st.session_state:
    st.session_state[question_key] = random.choice(sample_pool)

# If language changed, pick a new random question from the new pool
if st.session_state[question_lang_key] != lang:
    st.session_state[question_lang_key] = lang
    st.session_state[question_key] = random.choice(sample_pool)


# 7. INPUT FORM & EXAMPLES

with st.container():
    if lang == "English":
        user_question = st.text_input(
            "Your question:",
            placeholder="e.g., What is hua zhu?",
            key=question_key,
            label_visibility="collapsed"
        )
        st.write("") # Spacer
        ask_button = st.button("Ask the assistant", type="primary")
        
        # Show static examples in a styled box
        st.markdown("#### Examples")
        st.markdown(
            """
            <div style="background-color: #f1f4f0; padding: 15px; border-radius: 6px; font-size: 0.9rem; color: #2f3e2f;">
            • What is hua zhu?<br>
            • What does ding que mean?<br>
            • Why do we keep playing after someone wins?<br>
            </div>
            """, 
            unsafe_allow_html=True
        )

    else:
        user_question = st.text_input(
            "请输入你想问的问题：",
            placeholder="例如：为什么要换三张？",
            key=question_key,
            label_visibility="collapsed"
        )
        st.write("")
        ask_button = st.button("向小助手提问", type="primary")

        st.markdown("#### 示例问题")
        st.markdown(
            """
            <div style="background-color: #f1f4f0; padding: 15px; border-radius: 6px; font-size: 0.9rem; color: #2f3e2f;">
            • 为什么要换三张？<br>
            • 定缺是什么？<br>
            • 什么是花猪？<br>
            • 胡了之后为什么还要继续打？<br>
            </div>
            """,
            unsafe_allow_html=True
        )


# 8. ANSWER & EXPLANATION LOGIC

st.markdown("---")
with st.container():
    if ask_button:
        # 1. Validate Input
        if not user_question.strip():
            if lang == "English":
                st.warning("Please enter a question first.")
            else:
                st.warning("请先输入一个问题。")
        else:
            # 2. Perform Search (Retrieve Top 3)
            with st.spinner("Thinking..." if lang == "English" else "思考中..."):
                if lang == "English":
                    results = qa_en.retrieve(user_question, top_k=3)
                else:
                    results = qa_zh.retrieve(user_question, top_k=3)

            # 3. Handle No Results
            if not results:
                if lang == "English":
                    st.warning("No matching rules were found.")
                else:
                    st.warning("没有找到匹配的规则。")
                st.stop()

            # 4. Determine Confidence Level of Best Match
            best = results[0]
            score = best["score"]

            # 5. Render Results in Tabs
            if lang == "English":
                st.subheader("Explanation")
                tab_labels = [
                    f"Top {i+1}: {r['content'].get('title', 'Unknown Rule')}"
                    for i, r in enumerate(results)
                ]
            else:
                st.subheader("规则解释")
                tab_labels = [
                    f"第{i+1}条：{r['content'].get('title', '未知规则')}"
                    for i, r in enumerate(results)
                ]

            tabs = st.tabs(tab_labels)

            for idx, tab in enumerate(tabs):
                r = results[idx]
                content = r["content"]
                with tab:
                    # Header color now uses the deep green
                    st.markdown(f"""
                    <h3 style="margin-top: 10px; color: #3a5a40; margin-bottom: 5px;">{content.get('title', 'Unknown Rule')}</h3>
                    """, unsafe_allow_html=True)

                    st.markdown(f"<span style='color: #588157; font-size: 0.9rem;'>Similarity score: {r['score']:.2f}</span>", unsafe_allow_html=True)

                    # Content blocks styled with the new palette (Sage bg, Dark Green accent)
                    block_style = "background-color: #f1f4f0; padding: 15px; border-radius: 6px; color: #2f3e2f; border-left: 4px solid #588157; margin-top: 15px; line-height: 1.6;"

                    if lang == "English":
                        st.markdown(f"""
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">Definition</strong>
                            {content.get('definition', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">When it happens</strong>
                            {content.get('when_it_happens', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">Example</strong>
                            {content.get('examples', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">Tip</strong>
                            <em style="color: #556b2f;">{content.get('newbie_tip', '')}</em>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">定义</strong>
                            {content.get('definition', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">什么时候会发生？</strong>
                            {content.get('when_it_happens', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">举个例子</strong>
                            {content.get('examples', '')}
                        </div>
                        <div style="{block_style}">
                            <strong style="color: #3a5a40; display: block; margin-bottom: 6px;">小提示</strong>
                            <em style="color: #556b2f;">{content.get('newbie_tip', '')}</em>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        # Only show help text if no interaction yet
        help_box_style = (
            "background-color: #e9edc9;"
            "border: 1px solid #ccd5ae;"
            "border-radius: 6px;"
            "padding: 12px;"
            "color: #2f3e2f;"
            "font-size: 0.95rem;"
        )
        if lang == "English":
            st.markdown(
                f"<div style='{help_box_style}'>👆 Type a question above and click "
                "<strong>Ask the assistant</strong>.</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='{help_box_style}'>👆 在上面输入你的问题，然后点击 "
                "<strong>向小助手提问</strong>。</div>",
                unsafe_allow_html=True
            )
