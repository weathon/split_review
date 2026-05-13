# AlphaDou: High-Performance End-to-End Doudizhu AI Integrating Bidding

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Artificial intelligence for card games has long been a popular topic in AI research. In recent years, complex card games like Mahjong and Texas Hold'em have been solved, with corresponding AI programs reaching the level of human experts. However, the game of Doudizhu presents significant challenges due to its vast state/action space and unique characteristics involving reasoning about competition and cooperation, making the game extremely difficult to solve.The RL model Douzero, trained using the Deep Monte Carlo algorithm framework, has shown excellent performance in Doudizhu. However, there are differences between its simplified game environment and the actual Doudizhu environment, and its performance is still a considerable distance from that of human experts. This paper modifies the Deep Monte Carlo algorithm framework by using reinforcement learning to obtain a neural network that simultaneously estimates win rates and expectations. The action space is pruned using expectations, and strategies are generated based on win rates.  The modified algorithm enables the AI to perform the full range of tasks in the Doudizhu game, including bidding and cardplay. The model was trained in a actual Doudizhu environment and achieved state-of-the-art performance among publicly available models. We hope that this new framework will provide valuable insights for AI development in other bidding-based games.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper improves the Deep Monte Carlo for the Doudizhu Game and evaluates it by incorporating the effects of bidding(not random), which were not incorporated in the previous study Douzero.

### Strengths
- The effects of bidding were incorporated, and improvements were made to Deep Montecaro.

### Weaknesses
 - This can be accomplished with existing methods, and this paper represents only a partial enhancement. Additionally, it has not undergone theoretical evaluation. There is few development of the architecture from the previous study DouZero.

### Questions
- Are there any architectural innovations in deep learning? 
- Can it be compared to the Transformer base apporoach[1].

[1] Amortized Planning with Large-Scale Transformers: A Case Study on Chess, NeurIPS2024.

### Soundness
2

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
This paper developes a new Doudizhu AI, which modifies the Deep Monte Carlo algorithm framework (i.e. DouZero) by using reinforcement
learning to obtain a neural network that simultaneously estimates win rates and expectations. Stronger performance is achieved against DouZero.

### Strengths
Stronger performance is achieved against DouZero and its variants.

### Weaknesses
 - Weak experiments. More recent SOTA Doudizhu AIs should be included as the baseline methods.
- The reason why the proposed method AlphaDou is better than DouZero is unclear.  
- The improvements (both in terms of methodology and experimental results) of the proposed method AlphaDou over DouZero seem marginal.

Minor:
- Section 2, The game of Doudizhu, is suggested to be moved to the appendix. 
- The end of Introduction. The training code for AlphaDou is available. Please attach the code link if you claim it available. 
- Missing previous related work on Doudizhu AI. e.g., Zhang, Yunsheng, et al. "Combining Tree Search and Action Prediction for State-of-the-Art Performance in DouDiZhu." IJCAI. 2021.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces AlphaDou, an end-to-end trained reinforcement learning (RL) agent that plays the game of Doudizhu. AlphaDou consists of a bid model and a card model that handles the bidding and playing phases separately. Central to the technique of AlphaDou are Deep Monte Carlo (DMC), value factorization and action pruning. The experiments demonstrate that AlphaDou achieves a higher win rate and average point difference against previous models, especially after incorporating the bid model.

### Strengths
- The AlphaDou framework is straightforward and likely easy to implement.
- The bid model is a novel artifact responsible for improving the overall playing strength of AlphaDou.
- AlphaDou appears to be a more powerful agent than the previous DouZero agent in terms of winning rate and point difference.

### Weaknesses
 - The contribution of AlphaDou requires more explanation. Except for the bid model, it directly combines two ideas already explored -- Deep Monte Carlo and value factorization, leaving the contribution of this work unclear.
- The paper does not have a background section, leaving several notations undefined. The authors should not assume that all readers have the necessary background in RL or understand the notations without proper definitions. In addition, the equation numbers are missing.
- Some claims made by the authors are merely speculations without evidence. For instance, "when opponents bid low, the Bid Model may bid high even if the player’s  hand is not exceptionally good but relatively better than the opponents’ hands."
- The improvement of AlphaDou over previous baselines is marginal and lacks an ablation study.

Some minor issues:
> ... complex card games like Mahjong and Texas Hold’em have been solved

I believe we say a game is solved when we at least discover the game-theoretic outcome when all players play optimally. Under this definition, Mahjong and Texas Hold'em are not solved games.

### Questions
- Since $p_w(s, a)$ models the winning probability, the cross entropy loss is a natural choice. Why did you choose the mean square error over the cross entropy loss?
- What is your justification for the action pruning method? Do you have experiments demonstrating its effectiveness?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduce AlphaDou, an end-to-end DouDiZhu AI system that integrates bidding. This model is capable of perceiving bidding outcomes and dynamically adjusting its move strategy accordingly. Compared to previous algorithms for DouDiZhu, AlphaDou demonstrates enhanced capabilities in the experiments.

### Strengths
1. This paper provides a comprehensive summary of the related work on AI for DouDiZhu.
2. This paper is a good AI project implementation in the application of DouDiZhu.

### Weaknesses
1. The clarity of the paper's writing is insufficient; please refer to the Question.
2. The experimental validation is not sufficiently robust.
3. The input of the model includes the number of bombs played in the game, and I think this point involves the use of expert knowledge. An algorithm is end-to-end if only the direct observation is used as the input with post-processing.

### Questions
1. To what extent does considering bidding affect the complexity of the game of DouDizhu?
2. You should directly competing AlphaDou with RARSMSDou since RARSMSDou is the strongest publicly available Doudizhu model. Different models employ distinct strategies. A higher win rate against the same benchmark by one model does not necessarily imply that it can defeat another model.
3. In line 152, I am not entirely clear on why "i" can equal 4. Since each card has a maximum count of 4, it is impossible for the count of cards to be greater than i=4.
4. In line 389, it seems that the reported results in the column of the 1st position is worse than the results in the column of the 2nd position, is it correct?

### Soundness
2

### Presentation
2

### Contribution
2
