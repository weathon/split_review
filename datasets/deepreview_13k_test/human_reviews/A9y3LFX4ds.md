# Implicit Search via Discrete Diffusion: A Study on Chess

- Decision: Accept
- Scores: 3, 6, 5, 6

## Abstract
In the post-AlphaGo era, there has been a resurgence of interest in search techniques like Monte Carlo Tree Search (MCTS) within the realm of Large Language Models (LLMs). This renewed attention is driven by the recognition that current next-token prediction models often lack the ability for long-term planning. Is it possible to instill search-like abilities within the models to enhance their planning abilities without relying on explicit search? We propose DiffuSearch, a model that does implicit search by looking into the future world via discrete diffusion modeling. We instantiate DiffuSearch on a classical board game, Chess, where explicit search is known to be essential. Through extensive controlled experiments, we show DiffuSearch outperforms both the searchless and explicit search-enhanced policies. Specifically, DiffuSearch outperforms the one-step policy by 19.2\% and the MCTS-enhanced policy by 14\% on action accuracy. Furthermore, DiffuSearch demonstrates a notable 30\% enhancement in puzzle-solving abilities compared to explicit search, along with a significant 540 Elo increase in game-playing strength assessment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes to address Chess playing with an implicit search using diffusion modeling. The paper is compared to Transformers networks and MCTS. It reaches an Elo of 1728 when trained on data from Stockfish.

### Strengths
The paper compares the proposed approach to other approaches

### Weaknesses
The resulting Chess program is very weak compared to the current state of the art. Lc0 or Stoofvless use MCTS and deep neural networks and have a Elo greater than 3500 according to the Swedish Rating List. This is far above the 1728 Elo of DiffuSearch.

### Questions
What would you propose to improve the Elo of your program?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work aims to explore the possibility of planning using LLM without explicit search (e.g., MCTS), i.e., employing implicit search. Specifically, this paper proposes a method named DiffuSearch that looks into the future world by diffusion modeling. DiffuSearch considers the bidirectional self-attention  architecture and the multi-step diffusion generative process. This work focuses on a study of a specific board game--chess. The numerical experiments demonstrate the efficacy of the proposed DiffuSearch approach.

### Strengths
Overall, the idea of this work is novel and intuitive.

The paper is well-written and easy-to-follow.

The technical contents like the theorems as well as proofs are well-organized and sound.

The experimental setup is detailed and clear. The empirical results substantiate that DiffuSearch outperforms the existing baselines.

The demonstration plots like Figures 4 and 5 are very clear and intuitive.

### Weaknesses
Line 83. The link of source code is invalid. I hope to see the code during the rebuttal. The authors may consider submitting via a zip file or providing a valid link to an anonymous repo.


I would expect more detailed explanation of Figure 1 in both the main texts and the caption of Figure 1. As the comparison between the explicit and implicit searches is the main idea of this work. For example, the authors could explain the difference of explicit and implicit searches by describing Figure 1 more carefully. The discussion of the structures in Figure 1 is not enough. I felt that the difference between the explicit and implicit that authors mentioned in the texts is not well-connected to Figure 1.

The authors should provide a brief explanation of each input parameter and its role in Algorithm 1. For instance, what is \lambda_t? And a curiosity question: can you use other random sampling methods to draw t in line 169? Like Gaussian? Will different sampling methods affect the algorithm's performance?


In Figures 3(a) and (b), why DiffuSearch only runs around 7 depths? Are there any technical limitations that might prevent running DiffuSearch at greater depths? If it is feasible, I would like to see if it converges when you run the same depth as the baseline method, i.e., depth = 24 or 25.


I noticed that the demonstration plots like Figures 4 and 5 are limited to the comparison between DiffuSearch and Transformer (S-A). Can the authors explain the possible reasons? What about DiffuSearch against Transformer (S-V), against Transformer (SA-V), and Transformer (100 MCTS simulations)? If it is feasible, the authors may show at least one scenario for all of these three baseline comparisons. If not feasible, can the authors provide some explanations/reasons?

### Questions
Please refer to the "Weaknesses" section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper trains a transformer to imitate actions from a chess engine, while using discrete diffusion modeling to incentivize a form of implicit search during action selection. The diffusion modeling distills forward and backward prediction into the policy network, whereas the baseline transformer with MCTS involves only forward prediction. The paper includes several comparisons and ablations, and claims that diffusion modeling improves performance.

### Strengths
The paper investigates whether diffusion modeling can be helpful for emulating search using a feedforward network. This is an interesting question, as transformers have generally struggled thus far to solve problems requiring search. Normally, the solution is to add explicit search in the form of MCTS using the outputs of the transformer. This paper tries to improve the policy network instead, and indeed provides some evidence that transformers can simulate search using search with a single forward pass.

### Weaknesses
1. I wish it were more clear what exactly the paper is arguing. The paper seems to provide evidence for the following claim: "If we must use transformers in tasks that require search, it is more efficient and effective to train them via diffusion to do implicit search than it is to add explicit search via MCTS." However, it seems as though the paper is instead arguing that implicit search is better than explicit search. There doesn't seem to be evidence for this, as the method still relies on a dataset that comes from a Stockfish oracle that uses explicit search (and which vastly outperforms the diffusion model). If the paper is arguing for the former, weaker claim, then I think it does an fine job of this, provided the intro/discussion/etc. are updated to make this more clear.

2. I would have liked to see much more detail on the MCTS baseline. I couldn't tell whether it uses a perfect world model or a learned one, and if the world model is learned, I couldn't find information on how it is trained. These details are crucial for understanding exactly what method diffusion is improving on. How does the paper combine the policy model with MCTS to do search for each different "future paradigm"? Furthermore, the future paradigms in section 3.1 include s-arsar, which seems to be different from s-avsav, and while these names provide an intuition about what's going on, it's still unclear precisely what either of these mean.

3. The text is often rather imprecise, and in some places even a bit misleading. For instance:
    1. AlphaGo pre-dates the transformer, but the abstract makes it seem like people were working on LLMs prior to AlphaGo.
    2. Heuristic search existed long before the deep learning revolution, but the intro makes it sound like NNs introduced the idea of more efficient search.
    3. The intro (line 044) references three papers, all of which discuss model-based RL and the compounding error problem, but presents them as evidence that such errors occur due to recursive invocation of the *value* function, rather than the world model.
    4. The problem setting defines the value function with respect to a single policy, despite the fact that the players generally have different policies.
    5. In Sec 4.5 (line 288), S-AVAV does not lead to a significant performance improvement, though S-ASS does.
    6. It is unclear what the names in Table 4 actually mean. The process is described rather vaugely in the adjacent paragraph.
    7. The scaling trends in lines 411-418 are presented as scaling "laws", but it is far from clear that these results will have that level of robustness beyond that single experiment in this paper.
    8. Line 429 suggests that the method correctly values "the long-term positional benefits of opening lines for its rooks." However, the model is playing as white, has only one rook, and sacrifices it in the first turn, preventing any such long-term benefits.
    9. Section 5.2 (line 468), suggests that diffusion models might be "a way to substitute for conventional handcrafted search algorithms," but offers no evidence of this claim, since the oracle that provides the training data for the model uses exactly that sort of conventional handcrafted search algorithm.

### Questions
1. Can you provide more detail on precisely how MCTS is being combined with the policy network?

2. The Best $a_i$ and Match $a_{i-1}-s_i$ lines in Fig. 2 (left) are not discussed in the text. It seems like the model is terribly inaccurate for the actions it actually takes. How does it do so well?

3. In Table 8 (Appendix B), if $s'$ matches $f(s,a)$ with 99% accuracy, why does Best $a_i$ accuracy drop by ~1/3 after each step?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
DiffuSearch is a novel approach to enhancing the planning abilities of Large Language Models (LLMs) without relying on explicit search techniques like Monte Carlo Tree Search (MCTS). Developed in response to the limitations of current next-token prediction models in long-term planning, DiffuSearch uses discrete diffusion modeling to perform implicit search by predicting and utilizing future states. The method is implemented and tested on the game of chess, where explicit search has traditionally been essential. In extensive experiments, DiffuSearch outperforms both searchless and explicit search-enhanced policies, demonstrating a 19.2% improvement over one-step policies and a 14% improvement over MCTS-enhanced policies in action accuracy. Additionally, it shows a 30% enhancement in puzzle-solving abilities and a significant 540 Elo increase in game-playing strength compared to explicit search methods. These results suggest that DiffuSearch’s approach of internalizing a world model within the policy, without intermediate components, could be a promising alternative to traditional explicit search techniques in AI problem-solving.

### Strengths
1. Superior performance: DiffuSearch significantly outperforms baseline models, as evidenced in Table 2. It demonstrates a substantial improvement over both searchless and explicit search-enhanced policies, showing the potential of using diffusion as a model for search in chess.
2. Novel methodology: DiffuSearch incorporates future states and actions through discrete diffusion modeling, enabling it to leverage future information for improved next action prediction without relying on explicit search. This approach offers a new perspective on implicit search in AI.
3. Sample efficiency: Despite using 20 times fewer data records than some baseline models (e.g., SA-V), DiffuSearch demonstrates superior performance with approximately 10% higher action accuracy.

### Weaknesses
1. Declining prediction accuracy: As shown in Figure 2 (left), the accuracy of predicted future states and actions declines significantly for steps further into the future. For a strong world model in chess, the lookahead should ideally be accurate for about 7 steps, similar to top engines like Stockfish.
2. Training complexity: The paper doesn't provide a clear comparison of the computational requirements (e.g., FLOPs) for training DiffuSearch versus traditional transformer models. This makes it difficult to assess the scalability and efficiency of the diffusion process compared to other approaches.
3. Limited comparison to state-of-the-art: The paper doesn't compare DiffuSearch to more recent advancements in chess AI [1] that achieved a 2299 Elo rating using transformers. This omission makes it challenging to contextualize DiffuSearch's performance within the current state-of-the-art in chess AI.
[1] Ruoss, A., Delétang, G., Medapati, S., Grau-Moya, J., Wenliang, L. K., Catt, E., ... & Genewein, T. (2024). Grandmaster-level chess without search. arXiv preprint arXiv:2402.04494.

### Questions
Line 060: It is unclear if the Ha & Schmidhuber citation is correct or necessary here. Work has existed prior to this paper[2] and there are many more works that use it. This is a fundamental concept and probably does not need a citation unless it is citing a textbook. It should be removed.

Is the performance conditioned on the amount of train time and test time compute? What is the trade-off in FLOPs at train time versus test time?

Line 083: Code link is broken. Make sure to correct this for publication.


[2] Triggs, B., and Cameron, S. (1991). ““The Oxford robot world model,”,” in Expert systems and robotics (Springer Berlin Heidelberg), 275–284.

### Soundness
4

### Presentation
3

### Contribution
3
