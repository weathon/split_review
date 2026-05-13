# Strength Estimation and Human-Like Strength Adjustment in Games

- Decision: Accept
- Scores: 5, 3, 6, 6

## Abstract
Strength estimation and adjustment are crucial in designing human-AI interactions, particularly in games where AI surpasses human players.
This paper introduces a novel strength system, including a strength estimator (SE) and an SE-based Monte Carlo tree search, denoted as SE-MCTS, which predicts strengths from games and offers different playing strengths with human styles.
The strength estimator calculates strength scores and predicts ranks from games without direct human interaction.
SE-MCTS utilizes the strength scores in a Monte Carlo tree search to adjust playing strength and style.
We first conduct experiments in Go, a challenging board game with a wide range of ranks.
Our strength estimator significantly achieves over 80\% accuracy in predicting ranks by observing 15 games only, whereas the previous method reached 49\% accuracy for 100 games.
For strength adjustment, SE-MCTS successfully adjusts to designated ranks while achieving a 51.33\% accuracy in aligning to human actions, outperforming a previous state-of-the-art, with only 42.56\% accuracy.
To demonstrate the generality of our strength system, we further apply SE and SE-MCTS to chess and obtain consistent results.
These results show a promising approach to strength estimation and adjustment, enhancing human-AI interactions in games.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a strength estimation method that predicts rough player strength in go with only a few games. They use this as a method for running MCTS showing that it can be leveraged to approximate human-like play in go (and chess).

### Strengths
I think this is an interesting approach to modeling players in games and I like that the authors introduce a new metric for looking at player skill, but I am not fully convinced by the results.

# originality

This is a new approach to modeling humans and is breath of fresh air compared to the maximizing win rate approaches most other models use. I also like that this can be used for insight into players (as the authors note) and think this is a good new area of research.

# quality

The writing is OK, but I think the presentation needs another pass. The plots are difficult to read, I'm not clear how the confidence intervals are calculated, and the colours make telling lines apart difficult (figure 4 also has colour issues), consider some tables, log axis, larger lines/dots, smoothed lines, and fewer data points.

# clarity

I also found the paper not easy to follow the model labels aren't intuitive and are not defined in one place so it took some time to figure out what is meant by SE±1 vs SE_\inf±1 for example. I'm also not fully clear how the training and testing were done, which the lack of code exacerbates. 

 # significance

I like the idea and this could be a significant new direction in the area, but the numerous issues with the paper limit it.

### Weaknesses
What is the training/testing split? I feel like I missed the section on how the dataset is constructed as I could only find a short discussion in section 4.1. I'm very concerned that there is some data leakage in how the experiments were run, specifically that the authors did not partition by players between training and testing. This would mean that the models can simply learn the preferred openings of each player and use that to predict skill. The numbers they get are about the same for a player identifier in chess [1].

The lack of baseline or consideration of alternative skill estimators I also find concerning as it makes evaluating the number much more difficult. Can the authors compare their results to the raw Elo estimates given by the 100/15 games (using the opponents known Elo) or better yet compare to some simple classifier.

I am also concerned by lack of code release as that is an important part of the final paper.

### Questions
+ Why did the authors not compare their results to any of the models of human-like play in chess or go?
+ I'm unclear on the reasoning for the claim on line 534 "However, this issue could potentially be addressed by using all models trained by AlphaZero, which", how would that work? Elo is a relative measure (expected winrate vs the community), how would AlphaZero's Elo be relevant for humans without human games?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper derives a strength estimator network from human game-plays labeled with rating data and then use the SE network to inform MCTS such that the policy plays at a specific rank in a human-like fashion. The strength estimator is learned with a loss function derived from a Bradley-Terry model.

### Strengths
I find the application of a SE network applied to adjusting the strength of game playing agents an interesting application with practical utility. The loss function derived from the Bradley-Terry model for learning the SE network is novel and with generalisation to more than two player settings.

### Weaknesses
I have several concerns with the proposed approach in this paper. First, the Bradley-Terry model represents each candidates with a scalar score (e.g. Elo score), which has many well-documented limitations [1-4]. A salient limitation is its inability to capture intransitivity, which would become a limitation factor for the SE network as it assumes that game plays by a player at rank $r' > r$ would win against game play by a player at rank $r$ when the lower ranked play may have played an effective exploiter strategy. Perhaps the scope of the method should be limited to perfect-information games? Second, the authors have not discussed the issue of reach-probability of states in defining the loss function to the SE network. For a state-action pair (s, a), the output of SE(s, a) is most heavily influenced by the player rank that most often visit state $s$, yet this does not seem to be accounted for in the method presented. While the issue of state coverage came up, it's not clear that adding randomised exploration policies would offset the influence of different state reach probability. Finally, the notion of "strength" features heavily in writing, however, I find it difficult to pin down exactly what "strength" means as it should depend on both the player and its opponent's strategies. The distribution over strategies seem implicit and dependent on the empirical game play data.

### Questions
1. L53: "..., with higher scores indicating stronger actions": could you clarify what stronger implies here? Is it actions that lead to expected win-rates? If so, what is the expectation over? 
2. L58: "... correspond to a given targeted strength score": am I right in thinking that the quality of the strength adjustment of SE-MCTS in state s relies heavily on the quality of SE(s, a)? If so, could it be the case that players at a certain rank would rarely reach state s in the first place and lead to inaccurate prediction by SE-MCTS? 
3. L173: "... aggregating using the geometric mean": it would help readers if the use of the geometric mean can be better motivated. Is it because of how it works out in Eq (3) for comparing a rank to multiple other ranks? It could be helpful to state this explicitly. 
4. L238: "we sequentially perform the softmax loss...", typo? minimise the softmax loss? 
5. an intuitive baseline, given that the authors have access to ranked game play, would be to optimise a rank-conditioned policy network $\pi(\cdot | s, r)$ with $r$ the set of player ranks. If I understood correctly, methods such as SA-MCTS does not require ranked game-play data whereas the proposed methods do.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a strength estimator to estimate the strength of GO and chess players. Additionally, a modification of the MCTS algorithm based on the strength estimator is introduced, to make it possible to adjust the playing strength of the MCTS agent to certain levels. The data for training the strength estimator is collected from FoxWeiqi, the largest online GO platform, and models are trained to estimate the gameplay levels from 3-5kyu to 9 dan, which covers most of the meaningful strength levels of human players. The experiments show the strength estimator significantly outperforms traditional supervised learning approaches, and the gameplay strength of $\text{SE}_\infty$-MCTS agent appears to be correlated to the target strength.

### Strengths
This paper presents the proposed methods clearly with sufficient details. The proposed methods are described with proper motivations. According to experiment results, the proposed strength estimator shows significant improvement compared to the traditional supervised learning algorithms. The results also show the proposed method can adjust the playing strength to some extent.

### Weaknesses
To my understanding, the strength estimator method is relevant to learning to rank [1], [2]. I believe there is some novelty, but some related background could be discussed to make the novelty more clear. Specifically, the paper does not adequately address how the proposed strength estimator differs from existing ranking methods in the context of game playing agents. The current discussion does not delve into the nuances of how the aggregation of rankings across multiple game states is handled, nor does it discuss the potential impact of different aggregation strategies on the final strength estimation. A more detailed comparison with established learning-to-rank techniques, highlighting the unique challenges and solutions in the game-playing domain, would be beneficial.

I believe there are some ways to improve the clarity and soundness of experiment parts. For Figure 4, I would like to recommend authors expand each column to a 2D map (except for MCTS). That means comparing SA-MCTS, SE-MCTS, and $\text{SE}_\infty$-MCTS for all combinations of ranks, instead of comparing all ranks with only $r_5$. I understand there is a page limit but such figures can be included in the appendix. The current experimental setup, which compares all methods against a single baseline rank ($r_5$), does not provide a comprehensive view of the relative performance of each method across different strength levels. This makes it difficult to assess the robustness and generalizability of the proposed strength adjustment methods. A more thorough evaluation would involve a full round-robin tournament, where each method is tested against all other methods at various rank settings. This would provide a more complete picture of the strengths and weaknesses of each approach.

Some more concerns about the experiment are listed in my Questions and can be addressed by updating the paper.

### Questions
1.	Is it possible to train and test SE-MCTS on Chess like on GO? I believe no matter whether the results are good or bad, adding such results will always strengthen the paper.
2.	What is the exact value of $z$ for each rank?
3.	Which strength estimator is used in Figure 3?
4.	What does the strength score of vanilla MCTS and SA-MCTS look like? I am interested in the strength score curves (Figure 3) of vanilla MCTS and SA-MCTS (with varied strength index/rank settings).
5.	Which paper is the reference for SA-MCTS? I understand it is referred to in subsection 2.3, but there are multiple citations in 2.3, and am not sure which one proposed SA-MCTS.

### Soundness
2

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
This paper introduces a dedicated strength estimator and an SE-based Monte Carlo tree search,  which predicts strengths from games
and offers different playing strengths with human styles. A large amount of expert data with different playing level is used for training, and the learned strength is empoyed to adjust the prior policy in MCTS. Starting from the Bradley-Terry model, a new loss function is proposed. The experimental results demonstrate that the model can effectively predict the level of actions and guide MCTS in making decisions at various levels in both Go and Chess.

### Strengths
1. This paper is well-written with a clear and easily understandable structure.

2. This paper is highly motivated and the novelty is good.

3. The experiments are comprehensive, with cross-validation conducted using two applications.

### Weaknesses
 1. SE-MCTS adjusts the prior probabilities by the strength level $\hat{\delta}$  to influence the decision-making level of MCTS, and the number of simulations has not been reduced. It seems that SA-MCTS can give actions with $k$ different strength level by setting different $z$ for just one search process, but SE-MCTS need $k$ searches for $k$ different strength level actions. Besides aligning more closely with the desired strength rank, what are the more advantages of modifying the search process compared with performing on the final action decision? Specifically, the paper does not clearly articulate why modifying the prior probabilities during the search is superior to adjusting the final action selection based on the estimated strength. The computational overhead of performing multiple searches for different strength levels with SE-MCTS is a significant concern that needs to be addressed more thoroughly.

2. SE-MCTS achieves different levels of actions by modifying prior probabilities. However, as mentioned in the paper, with an increase in the number of simulations, the decision-making gradually shifts towards relying on Q-values. Does this imply that with a sufficient number of simulations, SE-MCTS might become ineffective, generatinig the same action with different $\hat{\delta}$? Can you provide a ablation study of SE-MCTS under different numbers of MCTS simulations? The paper should include a detailed analysis of how the effectiveness of SE-MCTS changes with varying simulation counts, and whether the strength-based prior modification remains relevant as the search converges towards optimal Q-values. This analysis is crucial to understand the practical limitations of the proposed approach.

3.  In Figure 4, why the win rate of SE-MCTS so low? The explanation provided in the paper regarding the exploration of low-probability moves is not entirely convincing. It would be beneficial to have a more detailed analysis of why SE-MCTS underperforms in this specific scenario, potentially including a breakdown of the types of moves where it struggles and a comparison with the performance of other MCTS variants.

4. Because different players have different strategies, Player A's defeat Player B does not necessarily indicate that A is stronger than B. It may simply mean that A's policy happened to exploit a weakness in B's policy. You can have pairwise matches between SE-MCTS, SA-MCTS, and MCTS with different levels, then rank them using Elo rating system, which would be more convincing. The current evaluation method based on win rates is insufficient to establish a robust ranking of different playing strengths. A more rigorous evaluation using an Elo rating system would provide a more reliable measure of the relative strengths of different MCTS variants and their ability to play at different levels.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
