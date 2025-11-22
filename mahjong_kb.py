KNOWLEDGE_BASE = [
    {
        "id": "exchange_three",
        "zh": {
            "title": "换三张",
            "question_examples": ["为什么要换三张？", "换三张怎么换？", "是不是必须换三张？"],
            "definition": "川麻开局前的固定规则，玩家必须从手牌中选出三张相同花色的牌，按方向交换给其他玩家。",
            "when_it_happens": "起牌后正式打牌之前进行，所有玩家同时选牌并交换。",
            "examples": "如果你手上条子比较少，例如只有 3 张条，可以选择交换给别人，让你的牌更容易打缺。",
            "newbie_tip": "选出你最不想要的花色的三张牌，可以增加胡牌率。"
        },
        "en": {
            "title": "Exchange Three Tiles",
            "question_examples": [
                "Why do we exchange three tiles?",
                "How do I choose which tiles to exchange?",
                "Do I have to exchange three tiles?"
            ],
            "definition": "Before the round officially begins, each player must select three tiles of the same suit and exchange them with another player in a fixed direction.",
            "when_it_happens": "Immediately after drawing the starting hand and before normal play begins.",
            "examples": "If you only have three tiles in the bamboo suit, you can exchange those to make it easier to choose bamboo as your missing suit later.",
            "newbie_tip": "Pick three tiles from the suit you dislike the most — it increases your chance of forming a cleaner hand."
        }
    },
    {
        "id": "missing_suit",
        "zh": {
            "title": "定缺",
            "question_examples": ["定缺是什么？", "为什么要选一个不要的花色？", "定缺怎么决定？"],
            "definition": "玩家必须选择一种花色作为整局都不能保留的牌，称为“缺一门”。",
            "when_it_happens": "换三张之后，正式开局前进行。",
            "examples": "如果你手牌里几乎没有条子，就可以选择“缺条”，并尽快把条子打掉。",
            "newbie_tip": "选你手上数量最少的花色，会最容易完成定缺要求。"
        },
        "en": {
            "title": "Missing Suit (Ding Que)",
            "question_examples": [
                "What is ding que?",
                "How do I pick my missing suit?",
                "Why must I choose a suit I can't keep?"
            ],
            "definition": "Each player must choose one suit that they cannot keep for the entire round. This is called the missing suit.",
            "when_it_happens": "Right after exchanging three tiles and before normal play begins.",
            "examples": "If you barely have any bamboo tiles, choose bamboo as your missing suit and discard them quickly.",
            "newbie_tip": "Pick the suit with the fewest tiles in your hand — it will be easier to clear."
        }
    },
    {
        "id": "blood_battle",
        "zh": {
            "title": "血战到底",
            "question_examples": ["血战到底是什么意思？", "有人胡牌了还要继续吗？"],
            "definition": "川麻特有规则。有人胡牌后，剩下的玩家继续打，直到场上只剩下一家未胡。",
            "when_it_happens": "第一家胡牌之后，仍未胡的玩家继续游戏。",
            "examples": "A 玩家胡牌后，B、C、D 仍继续打，直到只剩一人未胡为止。",
            "newbie_tip": "你胡了之后还可以继续观察局势和结算。"
        },
        "en": {
            "title": "Blood Battle to the End",
            "question_examples": [
                "What does 'blood battle' mean?",
                "Why do we keep playing after someone wins?",
                "Does the round stop after the first win?"
            ],
            "definition": "A special Sichuan Mahjong rule: when one player wins, the remaining players continue playing until only one player has not won.",
            "when_it_happens": "After the first player wins.",
            "examples": "If Player A wins first, Players B, C, and D keep playing until only one player has not won.",
            "newbie_tip": "Even after winning, keep watching the game — scoring continues until all but one player have won."
        }
    },
    {
        "id": "flower_pig",
        "zh": {
            "title": "花猪",
            "question_examples": ["花猪是什么？", "为什么会变成花猪？", "花猪要赔多少钱？"],
            "definition": "定缺之后，玩家应该优先打掉自己缺的那一门的牌。之后每一轮打牌，如果你在出牌结束时手里还留着缺门的牌（比如摸到缺门的牌却一直不打），就会被视为“花猪”，在结算时要额外赔付。",
            "when_it_happens": "从定缺完成开始到整局结束，都在持续生效；只要在自己的回合结束时还留着缺门的牌，就算花猪。",
            "examples": "你选择缺条，正常应该逐轮优先把条子打光。如果中途摸到条子却一直舍不得打，手里还留着条子，就会被算作花猪，在最后结算时要额外赔分。",
            "newbie_tip": "定缺之后，每一轮出牌都先检查自己手里有没有缺门的牌：有就先打掉。"
        },
        "en": {
            "title": "Penalty Pig (Hua Zhu)",
            "question_examples": [
                "What is a hua zhu?",
                "Why do players become a hua zhu?",
                "What happens if I keep tiles from my missing suit?"
            ],
            "definition": "After choosing your missing suit, you must prioritize discarding tiles from that suit. If at the end of any of your turns you still keep tiles from your missing suit — such as drawing one and refusing to discard it — you count as being in a 'hua zhu' state and will be heavily penalized when the round ends.",
            "when_it_happens": "From the moment ding que is decided until the end of the round. If you end any turn while still holding tiles from your missing suit, you are considered a hua zhu.",
            "examples": "If you choose bamboo as your missing suit but keep a bamboo tile after finishing your turn, you will be counted as a hua zhu at final scoring.",
            "newbie_tip": "After choosing your missing suit, check your hand every turn — if tiles from that suit remain, discard them immediately."
        }
    },
    {
        "id": "ready_punish",
        "zh": {
            "title": "查叫",
            "question_examples": ["查叫是什么意思？", "没下叫为什么要赔？", "川麻每家都要下叫吗？"],
            "definition": "牌局结束时，未下叫的玩家需要向所有下叫玩家额外赔分。",
            "when_it_happens": "血战到底结束时结算。",
            "examples": "A、B 已下叫，C 没下叫，C 就要赔给 A 和 B。",
            "newbie_tip": "后期尽量保持下叫状态，否则查叫的赔付可能更高。"
        },
        "en": {
            "title": "Penalty for Not Ready (Cha Jiao)",
            "question_examples": [
                "What is cha jiao?",
                "Why do I need to pay when I’m not ready?",
                "Does everyone need to be in ready hand?"
            ],
            "definition": "At the end of the round, players who are not in ready hand must pay additional points to all players who are already in ready hand.",
            "when_it_happens": "During final scoring at the end of the blood-battle phase.",
            "examples": "If A and B are in ready hand while C is not, C must pay both A and B.",
            "newbie_tip": "Near the end of the round, try to reach a ready hand — the penalty for not doing so can be large."
        }
    },
    {
        "id": "pong",
        "zh": {
            "title": "碰",
            "question_examples": ["什么时候可以碰？", "碰了之后可以胡吗？", "碰是不是会暴露自己的牌？"],
            "definition": "当你手上还有两张相同牌，别人打出与你手牌相同的牌时，你就可以碰组成刻子。",
            "when_it_happens": "任何玩家出牌后",
            "examples": "你手上有两张五万，别人打出一张五万，你可以碰。",
            "newbie_tip": "可以先观察一下，再决定是否碰。"
        },
        "en": {
            "title": "Pong (Pung)",
            "question_examples": [
                "When can I pong?",
                "Does pong reveal my hand?",
                "Is pong always a good move?"
            ],
            "definition": "If another player discards a tile and you have two identical tiles, you may claim it to form a triplet.",
            "when_it_happens": "Immediately after another player discards a tile.",
            "examples": "If you have two 5-characters and someone discards a third, you can pong.",
            "newbie_tip": "Pong reveals part of your hand — beginners should use it thoughtfully."
        }
    },
    {
        "id": "kong",
        "zh": {
            "title": "杠",
            "question_examples": ["杠是不是一定要亮出来？", "暗杠和明杠有什么区别？", "杠了是不是要摸牌？"],
            "definition": "四张相同的牌组成杠，分为暗杠、明杠、补杠。",
            "when_it_happens": "只要你凑齐四张相同的牌即可杠。",
            "examples": "手里有三张，摸到第四张，就可以暗杠；手里有三张，别人打出第四张一样的，就可以明杠；碰完别人打出的牌后，自己再摸到第四张可以补杠。",
            "newbie_tip": "川麻中杠通常会多翻倍，遇到机会不要忘记杠。"
        },
        "en": {
            "title": "Kong (Gang)",
            "question_examples": [
                "Do I have to show my tiles when I kong?",
                "What’s the difference between concealed and exposed kong?",
                "Do I draw a tile after kong?"
            ],
            "definition": "Four identical tiles form a kong. It may be concealed, exposed, or added onto an existing pong.",
            "when_it_happens": "Whenever you obtain four of the same tile.",
            "examples": "If you have three of a tile and draw the fourth, you can make a concealed kong; if another player discards the fourth, you can make an exposed kong.",
            "newbie_tip": "Kongs often lead to bonus scoring in Sichuan Mahjong — don’t overlook them."
        }
    },
    {
        "id": "ready_hand",
        "zh": {
            "title": "下叫",
            "question_examples": ["下叫是什么意思？", "怎么判断自己下没下叫？", "下叫要不要亮牌？"],
            "definition": "只差一张牌即可胡牌，称为下叫。",
            "when_it_happens": "任意牌局阶段，只要你的牌型只差一张即可。",
            "examples": "你手上的牌型只差一张三条即可胡，那你就在下叫三条。",
            "newbie_tip": "川麻查大叫会处罚未下叫玩家，后期能下叫就尽量下叫。"
        },
        "en": {
            "title": "Ready Hand (Ting Pai)",
            "question_examples": [
                "What does ready hand mean?",
                "How do I know if I’m in ready state?",
                "Do I need to reveal my hand when I’m ready?"
            ],
            "definition": "You are in ready hand when your tiles are only one tile away from forming a legal winning hand.",
            "when_it_happens": "Whenever your hand structure lacks only one tile to complete.",
            "examples": "If your hand needs just a 3-bamboo to win, you are in ready hand for 3-bamboo.",
            "newbie_tip": "Being in ready hand avoids heavy penalties during final scoring."
        }
    },
    {
        "id": "win",
        "zh": {
            "title": "胡牌",
            "question_examples": ["胡牌的基本条件是什么？", "哪些牌型可以胡？", "自摸和点炮的区别是什么？"],
            "definition": "玩家满足基本牌型组合要求，并获得最后一张牌，即可胡牌。",
            "when_it_happens": "摸牌或别人打牌后，只要补上最后一张牌即可。",
            "examples": "最常见的基本牌型为 4 个顺子或刻子 + 1 对将。",
            "newbie_tip": "川麻的胡牌条件相对简单，先学会认出 4 个顺子或刻子 + 1 对将的结构。"
        },
        "en": {
            "title": "Winning Hand (Hu)",
            "question_examples": [
                "What are the basic requirements to win?",
                "Which patterns can win in Sichuan Mahjong?",
                "What’s the difference between self-draw and discard win?"
            ],
            "definition": "You win when your tiles form a legal hand and you obtain the final tile needed to complete it.",
            "when_it_happens": "Either when you draw the winning tile yourself or another player discards it.",
            "examples": "The most common winning pattern is four melds plus one pair.",
            "newbie_tip": "Learn to recognize the basic “four melds + one pair” structure first."
        }
    },
    {
        "id": "self_draw",
        "zh": {
            "title": "自摸",
            "question_examples": ["自摸是不是最赚？", "自摸怎么结算？", "川麻自摸是不是每家都要赔？"],
            "definition": "玩家自己摸到胡牌所需的最后一张牌，称为自摸。",
            "when_it_happens": "在自己的摸牌阶段摸到胡牌牌。",
            "examples": "你下叫三条，自己摸到三条就是自摸。",
            "newbie_tip": "自摸在川麻中通常得分更高，多留意自己摸进来的牌。"
        },
        "en": {
            "title": "Self-Draw Win (Zi Mo)",
            "question_examples": [
                "Is self-draw worth more?",
                "How is self-draw scored?",
                "Do all players pay when I self-draw?"
            ],
            "definition": "You win by drawing the winning tile yourself during your own turn.",
            "when_it_happens": "During your personal draw phase.",
            "examples": "If you are waiting for a 3-dots tile and draw it yourself, that is a self-draw win.",
            "newbie_tip": "Self-draw often yields higher points — pay attention to your draws."
        }
    },
    {
        "id": "discard_win",
        "zh": {
            "title": "点炮",
            "question_examples": ["点炮是谁赔？", "川麻点炮是不是一家赔？", "点炮了是不是不能继续打？"],
            "definition": "你打出的牌刚好被别人用来胡牌，称为点炮。",
            "when_it_happens": "你打出的每一张牌都有可能点炮。",
            "examples": "你打出三条，而别人刚好下叫三条，就点炮了。",
            "newbie_tip": "川麻点炮通常是一家赔，不是大家都赔，打牌时要注意别人可能在下叫的牌。"
        },
        "en": {
            "title": "Discard Win (Dian Pao)",
            "question_examples": [
                "Who pays when another player wins off my discard?",
                "Does only one player pay?",
                "Can I still continue playing after causing a discard win?"
            ],
            "definition": "If another player wins using a tile you discard, you are responsible for the payment.",
            "when_it_happens": "Any time you discard a tile that another player may be waiting for.",
            "examples": "If you discard 3-bamboo and another player was waiting for 3-bamboo, you triggered a discard win.",
            "newbie_tip": "Towards the end of the round, be extra cautious — many players are already in ready hand."
        }
    },
    {
        "id": "pair",
        "zh": {
            "title": "将牌（对子）",
            "question_examples": ["将是什么？", "是不是必须有一对？", "眼位是什么意思？"],
            "definition": "组成两张一样的牌，称为将。",
            "when_it_happens": "胡牌前的最终结构中必须存在一对。",
            "examples": "两张九条就是一对将。",
            "newbie_tip": "做牌时可以先找出可能当将的一对，会更利于规划牌型。"
        },
        "en": {
            "title": "Pair / Eye (Jiang)",
            "question_examples": [
                "What is a pair in Mahjong?",
                "Do all hands require a pair?",
                "Why is the eye important?"
            ],
            "definition": "A pair consists of two identical tiles and is required in most standard winning hands.",
            "when_it_happens": "In the final structure of a legal winning hand.",
            "examples": "Two 9-bamboos form a pair that can serve as the eye.",
            "newbie_tip": "Identify potential pairs early — it helps you plan your overall hand."
        }
    },
    {
        "id": "meld",
        "zh": {
            "title": "顺子和刻子",
            "question_examples": ["顺子怎么算？", "刻子和碰是不是一个意思？", "顺子能吃别人的吗？"],
            "definition": "顺子：同花色连续三张。刻子：三张一模一样的牌。",
            "when_it_happens": "任意阶段形成的基本面子。",
            "examples": "3-4-5 万是顺子；三个七饼是刻子。",
            "newbie_tip": "可以多留意各类排列组合的可能性。"
        },
        "en": {
            "title": "Sequences and Triplets",
            "question_examples": [
                "How do I form a sequence?",
                "Is a triplet the same as pong?",
                "Can I form a sequence using another player’s discard?"
            ],
            "definition": "A sequence is three consecutive tiles in the same suit; a triplet is three identical tiles.",
            "when_it_happens": "They can be formed naturally or when claiming another player’s discard.",
            "examples": "3-4-5 of characters is a sequence; three 7-dots is a triplet.",
            "newbie_tip": "Watch for possible combinations — sequences appear very often in Sichuan Mahjong."
        }
    },
    {
        "id": "seven_pairs",
        "zh": {
            "title": "七对",
            "question_examples": ["七对算胡吗？", "七对在川麻能胡吗？"],
            "definition": "由七个对子组成的特殊牌型，在川麻中可以胡。",
            "when_it_happens": "只要你手里有七个对子且结构合法，就可以胡七对。",
            "examples": "2 万 x2，5 条 x2，7 筒 x2 等凑齐七个对子。",
            "newbie_tip": "如果你一开始对子特别多，不要随意拆对，可能有机会做七对。"
        },
        "en": {
            "title": "Seven Pairs",
            "question_examples": [
                "Can I win with seven pairs?",
                "What is the seven-pairs hand?"
            ],
            "definition": "A special winning pattern made of seven distinct pairs.",
            "when_it_happens": "Whenever your hand can be arranged into seven legal pairs.",
            "examples": "Two 2-characters, two 5-bamboos, two 7-dots, etc., forming seven pairs.",
            "newbie_tip": "If your starting hand has many pairs, avoid breaking them — seven pairs might be easier than a normal hand."
        }
    },
    {
        "id": "kong_flower",
        "zh": {
            "title": "杠上花",
            "question_examples": ["杠上花是不是加倍？", "杠上花怎么算？"],
            "definition": "玩家杠后补牌，补到胡牌所需的最后一张牌，称为杠上花。",
            "when_it_happens": "宣布杠之后，补牌时摸到胡牌牌。",
            "examples": "你补一张三筒，如果刚好胡，就是杠上花。",
            "newbie_tip": "杠上花通常有额外加分，但是很看运气。"
        },
        "en": {
            "title": "Win After Kong (Kong Flower)",
            "question_examples": [
                "Is winning after kong worth more?",
                "How does kong-flower scoring work?"
            ],
            "definition": "After declaring a kong, if the supplement tile you draw completes your hand, it is called a kong-flower win.",
            "when_it_happens": "Immediately after drawing the supplement tile from a kong.",
            "examples": "If you kong and draw the exact tile you need, you win with kong-flower.",
            "newbie_tip": "Kong-flower wins often include bonus points — they're exciting but rely heavily on luck."
        }
    },
]