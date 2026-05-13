# Human-Aligned Chess With a Bit of Search

- Decision: Accept
- Scores: 8, 8, 6, 6, 6

## Abstract
Chess has long been a testbed for AI's quest to match human intelligence, and in recent years, chess AI systems have surpassed the strongest humans at the game.
However, these systems are \textit{not human-aligned}; they are unable to match the skill levels of all human partners or model human-like behaviors beyond piece movement.
In this paper, we introduce \Allie, a chess-playing AI designed to bridge the gap between artificial and human intelligence in this classic game.
\Allie is trained on log sequences of real chess games to model the behaviors of human chess players across the skill spectrum, including non-move behaviors such as pondering times and resignations
In offline evaluations, we find that \Allie exhibits humanlike behavior: it outperforms the existing state-of-the-art in human chess move prediction and ``ponders'' at critical positions.
The model learns to reliably assign reward at each game state, which can be used at inference as a reward function in a novel {\em time-adaptive} Monte-Carlo tree search (MCTS) procedure, where the amount of search depends on how long humans would think in the same positions.
Adaptive search enables remarkable {\em skill calibration}; in a large-scale online evaluation against players with ratings from 1000 to 2600 Elo, our adaptive search method leads to a skill gap of only 49 Elo on average, substantially outperforming search-free and standard MCTS baselines.
Against grandmaster-level (2500 Elo) opponents, \Allie with adaptive search exhibits the strength of a fellow grandmaster, all while learning {\em exclusively from humans}.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents Allie, a chess-playing AI model designed to imitate human behavior across a spectrum of skill levels. Allie is a transformer-based model trained on human games from Lichess that, given a board position and the Elo strength of the two players, predicts the next move the player will play (policy head), the think time, and the game outcome (value head). During inference time, Allie uses these prediction heads to add some MCTS search, where the search rollouts are guided by the (human-like) policy and value heads and the number of rollouts is proportional to the (human-like) think time. The main prior work in this area is the Maia project by McIlroy-Young et al., which also trained on human games to create models at different skill levels (KDD '20) and at the individual level (NeurIPS '21, KDD '22). Allie differs from Maia in three main ways: (1) it is a larger, transformer-based model that represents chess positions as a sequence of move tokens; (2) it models think time and resignation; and (3) it adds MCTS search during inference based on the human-like predictions.

Allie achieves ~4% higher move-matching accuracy on average than Maia (a much smaller model) and ~2% higher accuracy than GPT 3.5 (a much bigger model). More importantly, it exhibits better skill calibration across a wide range of Elo ratings (1000 - 2600), as verified by a human study of 7,483 games which shows that Allie incurs a skill gap of only 49 Elo points on average (provided adaptive search is used). Notably, Allie can play at a grandmaster level (2500 Elo) and still retain human-like qualities.

### Strengths
There are several aspects of Allie's methodology and results that I find compelling and believe advance the state of the art.

Allie models human chess playing more holistically by also predicting think time and special decisions such as resignation, which were not modeled in prior chess-playing agents work. Granted, these are just additional metadata recorded with Lichess games that prior methods could also train on, but what I found compelling is the authors' observation that these prediction outputs can be used to parameterize an MCTS search. This time-adaptive search proves to be crucial for closing the skill gap between Allie and the human opponent, as shown in the human study the authors conducted.

Allie achieves good move-matching accuracy across a wider range of Elo ratings (Fig. 2), as well as closer skill calibration to human players (Fig. 5), than prior work. In particular, the Maia models achieve good move-matching accuracy (so they feel human-like) but are not as well calibrated to the Elo of human opponents. Additionally, the fact that Allie can play at a grandmaster level (2500 Elo) is an impressive achievement given that behavior cloning on human data typically yields sub-expert policies.

I like that the authors include GPT 3.5 as a challenging baseline. GPT 3.5's move-matching accuracy is remarkable, given that it wasn't necessarily intended to play chess. Allie's performance is still slightly better, but its main advantage is in enabling search (and requiring much fewer parameters). 

Allie's architecture is quite sensibly designed. The use of move tokens and history is a natural way of representing a board position for a transformer model, and avoids the need for a visual representation (as used in AlphaZero, Maia, etc.) -- though it is an interesting question if adding such a visual representation would help, given how visually humans process a chess board. I liked the use of "soft tokens" to encode each player's Elo ratings, allowing Allie to condition its output on skill level. I also liked the design of taking the final decoder layer output and parameterizing each prediction using separate linear layers. 

The user study was a nice addition to the paper, as it demonstrated Allie's skill calibration in real human games and also allowed the authors to collect survey results on how enjoyable and human-like Allie (and the other baselines) felt.

### Weaknesses
There a several things that concern me about the paper's presentation and claims, which I hope can be clarified through the rebuttal. 

First, the discussion of Maia in the introduction and related work seems lacking/misleading to me. I don't think it's fair to say that existing systems are not "human-aligned" -- this was precisely the goal of Maia and they did create both skill-level and individual-level (KDD '22) models using the same basic approach (behavior cloning on human data). The individual-level models improve move-matching accuracy over Maia by a similar margin to your improvement over Maia. McIlroy-Young et al. also did some work on style identification (stylometry) that achieved very high accuracy (NeurIPS '21). I suggest citing and mentioning the NeurIPS '21 and KDD '22 papers.

The fact that the published Maia models do not include think time, resignation, or history does not seem that fundamental to me -- there are archived submissions on OpenReview that extend Maia in some of these ways, e.g., deepening the model and achieving move-matching accuracy similar to Allie's. One of these submissions was recently accepted to NeurIPS '24 and should be discussed in this paper: "Maia-2: A Unified Model for Human-AI Alignment in Chess", which presents a unified version of Maia that conditions on the player's Elo rating and achieves better calibration across skill levels. It is worth noting that Allie's architecture, at 355M parameters, is more than an order of magnitude bigger than these Maia models -- you point out size difference as a reason the comparison to GPT 3.5 is unfair, but you do not point out the size difference between Allie and Maia. 

Instead of focusing on the above differences, I think a better framing of this paper is to focus on how predicting human-like outputs (including think time) enables you to augment a behavior-cloned model with search, closing the gap between Allie and human players, particularly stronger ones.

It is important to note that adding MCTS search introduces a non-human-like element to your approach. There is not enough evidence to suggest that humans search the game tree in an MCTS-like manner, and in general our understanding of how humans balance board state evaluation with search (calculation) is quite poor. Thus, I would tone down the claims about only relying on human data, since a search algorithm applied to a game tree implicitly encodes non-human information. One recent piece of work that supports your use of think time to limit MCTS is the paper by Russek et al. called "Time spent thinking in online chess reflects the value of computation". It would be helpful if you could report move-matching accuracy as a function of search time; is it the case that when you do more search, move-matching accuracy decreases? Also, how did you choose the constant 'c' in the number of rollouts function? It would be useful to see how sensitive your results (move-matching accuracy, Elo calibration) are to the choice of c.

Related to the above, it's not clear to me why you would expect Allie's value estimates to match those of Stockfish (Fig. 4). Isn't Allie's value head predicting the outcome a *human* would experience if they continued from that board position? I agree that in many situations this would align with Stockfish's assessment (e.g., if the human is up a lot of material, or if it's close to the end game), but it seems more sensible to me to compare Allie's value estimate to the actual outcome of the game, not what Stockfish thinks the outcome should be.

How is it that adaptive search does better than non-adaptive (AlphaZero-like MCTS) search against 2500 Elo players? Is the non-adaptive search time bounded, in addition to being the same for each move?
 
You observe that using discrete tokens for Elo would be too sparse, but your soft tokens also interpolate between Elos and are represented as tokens. Isn't this representation also sparse, i.e., won't it suffer from a lack of examples associated with each value, or are you representing them differently internally? 

The loss function you use doesn't mention normalization or weights to balance the different loss terms. Is this a potential issue, given that these terms capture very different things (e.g., log-likelihood of next move vs. MSA of think time prediction)?

### Questions
My questions and suggestions are interspersed in the comments above. I summarize them here for convenience:  

1. There is some missing related work. I realize you may not have seen some of these papers in time, but hope they are helpful in revising your paper.  
2. The size difference between Allie and Maia's architectures (and its connection to increased move-matching accuracy).
3. The non-human-like aspects of MCTS search. Can you report move-matching accuracy as a function of search time?
4. How sensitive are your results (e.g., move-matching accuracy) to the constant 'c' in the rollouts function?
5. The difference between Allie's value head and Stockfish's evaluation. How accurately does Allie's value head predict game outcomes?
6. Explain why Allie with adaptive search does better than AlphaZero-like MCTS search against 2500 Elo opponents.
7. Are soft tokens encoded in a way that also suffers from sparsity? 
8. Any normalization/weighting applied to the loss function terms?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new human-like chess model that exceeds the current SOTA while adding ponder. The authors look at the model compared to the previous SOTA tests and add some new ones, along with user studies to strongly argue for their model's performance.

### Strengths
I think this is a good paper presenting an original approach to human-like play modeling and it answered most of my questions in the text.

# originality

The idea of using a transformer to solve chess predates the current LLM craze (I can find a cite if needed), but this the most successful one so far and shows a real improvement compared to the current slate of LLMs for chess papers. Adding the ponder time is an obvious step from a FEN based dataset, but again is done very well. So while most of the ideas are not novel the combination and execution are.

# quality

The experiments look to be done well and the paper flows well. Adding the human studies was good move to really show it's an improvement over Maia.

# clarity

I found figure 3 difficult to read, the median is almost impossible to see. I also don't know what the squares in figure 1b mean from the caption, is it supposed to be a chess board?

# significance

Chess AI has had a resurgence in the last few years and this could aid that work, it also shows a path for many other turned based games. So I think this has a chance of being significant.

### Weaknesses
I don't think the term _human-aligned_ is good in this paper. An aligned AI system is already implicitly aligned to humans, but the term does not mean that it acts like a human, just that it works in the best interest of humans. I think a different term should be used for this concept to prevent it from being interpreted in the more common AI alignment sense.

I'm not clear how the <resign> token can be used in practice, even with a false positive rate of 0.1%, that would be ~2% over 20 moves, and only takes one bad resign to distribute a game. Was the resign prediction used in testing the models in the user studies? And how does it look in a real gameplay scenario, not just against single game states?

The lack of code right now is also concerning, my rating is contingent on the authors fulfilling their promises in the text.

### Questions
See the Weaknesses section

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on proposing a chess-playing AI (called ALLIE) that is aligned to human gameplay. It does so by training a Transformer-based network on a dataset of human games, taking into account metadata such as the player's skills (Elo score) and their pondering time. By assuming players ponder on critical situations, the authors propose to add a MCTS-based search component proportional to the pondering time. ALLIE's skill level is estimated against numerous human players, and is shown to have an average skill gap of 49 Elo.

### Strengths
- Shows strong and accurate performance across a wide range of Elo scores
- Strong performance compared to Maia, which is also human aligned
- Thorough analysis on different aspects of the algorithm (accuracy of move prediction, accuracy of pondering times, accuracy of value estimate)
- Extensive human study

### Weaknesses
 - Entirely based on offline data, based of recording of human gameplays. This limits the scope of this method for human-aligned AI. Moreover, large parts of the data have been removed for training (downsampling low-Elo games, removing transitions under time pressure), so it seems training ALLIE-like agents require a specific training regimen.
- There does not seem to be any related work on skill calibration. Although I am not an expert in that area, I would be curious about what works have been done in that regard.
- I find the claim that ALLIE has a "reliable board value estimate" a bit misleading. Fig3 (with a Pearson's $r=0.697$) is already quite noisy, and the vast majority of Fig4 is below that number (around 5+ moves from terminal), with 30+ moves from terminal having a weakly correlated $r<0.3$. What would these values be in terms of mean absolute error?
- GPT3.5 has a comparative move-matching accuracy as ALLIE on higher-Elo games, despite having not been explicitly trained for chess. Although I do not expect it to be included in the human evaluation, it would have been interesting to provide a more in-depth comparison between GPT3.5 and ALLIE. Would a fine-tuned GPT3.5 on the same dataset as ALLIE (but in PGN format) result in a human-aligned agent?

### Questions
- ALLIE has been trained exclusively on Blitz games. How does this impact the importance of search compared to standard games? I would expect that Blitz players play mostly instinctively. Blitz might thus be enough to train an agent solely on a human dataset of gameplays, but this might be insufficient for standard games. Do you have any insights as to the types of changes that would be required to scale ALLIE to standard games?
- Related to the previous question, the authors mention the need to generalize to out-of-distribution positions. How well would ALLIE (trained on Blitz) perform in standard games?
- Is the Elo score used throughout this paper specific for Blitz? Or is it the player's global Elo score? I would assume the former, but one survey respondent (Table 9, second row) has an Elo of 1940 and mentions he or she "doesn't really play Blitz so I can't imagine I'm very good".
- Since ALLIE is trained on a fixed dataset of different levels of experts, this would be suited to an offline reinforcement learning (RL) setting. More specifically, ALLIE use a GPT-2 like architecture, making it related to Decision Transformers (DT) [1] (execpt of course the search component). Offline RL approaches provide performance and out-of-distribution gains compared to the behavior-cloning-based approach taken by ALLIE. Are there any reasons why the authors chose to behavior cloning?


[1] Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A., Laskin, M., ... & Mordatch, I. (2021). Decision transformer: Reinforcement learning via sequence modeling. Advances in neural information processing systems, 34, 15084-15097.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ALLIE, a chess AI trained exclusively in human chess games with the goal of creating a skill-calibrated and human-aligned chess AI. If the policy is solely employed for matches with humans, the AI struggles to align with human players of corresponding Elo ratings. To address this challenge, ALLIE takes into account the pondering time of each move recorded in human games and proposes a time-adaptive Monte Carlo tree search to mitigate the skill gap, which outperforms search-free and standard MCTS baselines. Furthermore, ALLIE also considers human resignation behavior; analyses show that ALLIE achieves an 86.4% true positive rate, indicating that it demonstrates more human-like behavior.

### Strengths
This work proposes some novel ideas for developing human-like agents by considering not only move accuracy but also non-move behaviors of human players, such as pondering time and when to resign. It helps bridge the gap in developing human-aligned AIs, as strong AI agents may exhibit non-interpretable behaviors. Additionally, it compares favorably with state-of-the-art agents, MAIA and GPT-3.5, achieving better results.

### Weaknesses
## Major Comments:
First, the novelty of this paper is very limited. Specifically, it directly applies the transformer architecture to chess games. The only novel thing is that the approach introduces some new outputs, such as predicting pondering time or resignation. Moreover, for the network architecture, the reason why the transformer architecture is better than MAIA, which uses residual networks, is not explicitly explained. For example, if the parameter size is much larger than MAIA, the inference time might be also much longer, and the fairness of the experiments should be reconsidered. It is better to compare the inference time and the number of parameters under the same hardware.

Second, the evaluation set excludes moves made under time pressure (when the remaining time is less than 30 seconds) to avoid situations where players tend to make random moves. However, these blitz moves under time pressure might reflect human intuitions. Although MAIA’s evaluation also excludes these moves, but since this paper aims to create human-like AIs, it is recommended to include these moves in the evaluation, as they might yield interesting and more convincing results. Furthermore, while non-move behaviors consider the pondering time for each move, human players often decide the thinking time for the next move according to the remaining time. How about incorporating the remaining time as input to models? By doing this, the method might not need to exclude moves made under time pressure in the evaluation set.

Third, for the generality of the proposed method, the experiment in this paper is only applied to chess, it is not sure whether this method can be generalized to other games. The author should include other games to demonstrate the effectiveness of their approach.

## Minor Comments:
- In abstract, “... resignations In offline evaluations,” -> “... resignations in offline evaluations,” 
- The time spent for each move should be recorded in the game history, but not explicitly stated in the main text, please address it.

### Questions
1. Please address the issues mentioned in the Weakness, especially major comments.
2. Why do transformer-based models perform better than MAIA? Is this due to the architecture itself or the parameter size? Does the transformer-based model in ALLIE have a longer inference time than MAIA*?
3. Can this method be applied to other games or domains? Any further experiments on other games?
4. Do you enable resignation for ALLIE as mentioned in Section 5.2 for the LARGE-SCALE HUMAN STUDY?
5. Do ALLIE-SEARCH and ALLIE-ADAPTIVE-SEARCH use the softmax function for final move decisions, as ALLIE-policy does? If not, the experiment may be unfair.
6. Is the bin range in Figure 5 set to 200? The datasets are separated every 100 Elo ratings. Why does the bin range differ?
7. In section 4.3, it claims "Due to dependency on the textual PGN notation, this approach
is not compatible with OpenAI’s latest chat-based LLMs (e.g., GPT-4)". However, the explanation of why we cannot use GPT-4 for evaluation is unclear.
8. Could you incorporate the remaining time as input to the model? Maybe it might make the agent more human-like.
9. How to determine the constant c in the time-adaptive MCTS procedure? It seems it is not explicitly stated in the main text.
10. For the resignation conditions, you consider both the resignation token and values. What if it only thinks of resign tokens? Would the result be better or worse than TPR of 86.4%?
11. In Maia’s paper, they state that MCTS tends to degrade move prediction performance in their setting. Why does MCTS improve move accuracy, especially in expert-level human games in this work?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents ALLIE, a skill-calibrated and human-aligned chess AI trained purely from human games. ALLIE uses the transformer architecture for sequence modelling to predict the distribution of the next move, the pondering time humans spend at the current position, and the winner of the game. Through a test against a database of human games and an online user study, the authors find ALLIE better at predicting human moves than its counterparts. They also propose an adaptive Monte Carlo Tree Search (MCTS) mechanism at inference time, leveraging the predicted pondering time to model human behaviours better and calibrate the skill.

### Strengths
- The objectives of the paper are clearly defined, and the paper sticks close to these objectives.
- The writing and presentation of the paper are clear and of good quality. I do not spot any visible typos in the main text.
- Though I am not entirely sure, I believe modelling the pondering time and resignation and utilizing the time prediction for adaptive MCTS are novel ideas in this line of work. In addition, the invention of soft tokens for strength conditioning is a fresh idea.
- The presented evaluation methods and metrics seem rigorous. Furthermore, this work complements the offline human alignment evaluation with surveys consisting of quantitative and qualitative feedback from online users.

### Weaknesses
 - The design of ALLIE is akin to AlphaGo [1] without the self-play phase. Therefore, I do not view training the neural networks entirely on human data and applying MCTS for policy improvement as an algorithmic advancement.
- The authors stress the necessity of adaptive search in skill calibration. However, failure to match the grandmaster level can be interpreted merely as a lack of strength, and incorporating a planning phase improves ALLIE's strength to close that gap. The authors do not explain why adaptive search attains a better skill calibration error even against mid-level opponents. Furthermore, it is unclear if the adaptive search is truly necessary for skill calibration, or if the improved performance is simply due to the increased search depth, which would naturally lead to stronger play.
- As the authors point out, the users knew they were playing against an AI before they filled out the survey. Therefore, the human alignment result from the user study might not be as objective as if they conducted a Turing test.
- It would better support the superiority of adaptive search in skill calibration if ALLIE with adaptive search were compared against an AlphaZero-like agent, where the skill level is adjusted using a temperature parameter. It is not clear if the adaptive search mechanism provides a unique advantage over simply adjusting the exploration-exploitation balance in a standard MCTS.

### Questions
- I wonder how the hyperparameter $c$ for deciding $N_{sim}$ was selected. Was it determined via trial and error?
- Could you explain why the move-matching accuracy is a good metric for human alignment evaluation? For instance, I can imagine that amateur players can make blunder moves in many different ways given the same board position. Thus, ALLIE may get a low move-matching accuracy even with strength conditioning, while the human player feels their opponent is human-like. Continuing with this point, I believe chess beginners are less likely to tell if their opponent is a human simply because they see fewer games and don't have the same level of experience. Therefore, I believe it would be interesting to report the human alignment survey grouped by Elo ratings.

### Soundness
3

### Presentation
3

### Contribution
2
