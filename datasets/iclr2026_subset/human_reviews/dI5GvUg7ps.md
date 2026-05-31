## Human Reviewer 1

### Summary
The paper introduces RewardRank, a framework for optimizing so-called counterfactual utility in learning-to-rank (LTR) systems. The authors argue that RewardRank addresses the limitation of traditional LTR methods by first training a reward model from logged data to predict the utility of various rankings and then optimizes a ranker to maximize this predicted utility using a differentiable soft permutation operator. They propose two evaluation protocols: Parametric Oracle Evaluation (PO-Eval) and LLM-As-User Evaluation (LAU-Eval) to benchmark their approach against existing methods.

### Strengths
1. Overall, the design of the method is reasonable. Particularly, borrowing the idea from offline reinforcement learning to mitigate utility noise is interesting.
2. The idea of using LLM-as-users to evaluate recommendation rankings is interesting, though some design rationale need more justification (as described below)

### Weaknesses
1. The novelty of the paper is limited. The idea of training a utility model from logs is not new, and the proposed training process is a direct application of Softsort.
2. This paper ignores a huge amount of relevant works on unbiased LTR and reinforced LTR. For example, counterfactual LTR is often closely discussed with Unbiased LTR [1], and, according to [2], the state-of-the-art ULTR methods are already much better than standard LTR and the proposed method in this paper on BaiduULTR. As for utility-based optimization, this has long been recognized as an advantages of reinforced LTR methods, and recent RLTR methods have already achieved the state-of-the-art performance only based on utility-based training (i.e., listwise reward, no pointwise annotations or labels)[4]. It’s not clear what’s the main novelty of this paper without detail comparison and discussion of ULTR and RLTR methods.  Also, transformer-based ranker has been proposed for a while, and it would be better to add proper references.
3. The proposed evaluation protocols are not well justified. BaiduULTR already has real clicks, and previous studies on ULTR have already build comprehensive simulation experiment frameworks[3]. It’s not clear to me what is exactly new in PO-Eval. While the LLM-as-user paradigm is interesting, whether it can reflect user behaviors in real scenarios is not well justified.

[1] Ai, Q., Yang, T., Wang, H. and Mao, J., 2021. Unbiased learning to rank: online or offline?. *ACM Transactions on Information Systems (TOIS)*, *39*(2), pp.1-29.

[2] Zechun Niu, Lang Mei, Chong Chen, and Jiaxin Mao. 2025. Distributionally Robust Optimization for Unbiased Learning to Rank. In Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '25). 

[3] Niu, Z., Zhang, Z., Mao, J., Ai, Q. and Wen, J.R., 2025, July. Investigating the Robustness of Counterfactual Learning to Rank Models: A Reproducibility Study. In *Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval* (pp. 3265-3275).

[4] Tu, Y., Xu, Z., Yang, T., Su, W., Zhou, Y., Liu, Y., Lin, F., Liu, Q. and Ai, Q., 2022. Reinforcement Learning to Rank Using Coarse-grained Rewards. *arXiv e-prints*, pp.arXiv-2208.

### Questions
- Why we need to build an “oracle IPS” model on BaiduULTR for evaluation? BaiduULTR already has real clicks (I noticed that the authors have already done experiments with them), and if you believe that using the real clicks is not convenient for controlled studied, previous ULTR papers have already developed quite comprehensive simulation experiment pipeline for different scenarios [3].
- Have you conducted any experiments validating the reliability of LLM-as-users?

### Soundness
1

### Presentation
3

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper introduces RewardRank, a novel data-driven Learning-to-Rank (LTR) framework designed to directly optimize true counterfactual user utility instead of relying on traditional offline proxy objectives (like NDCG) that fail to capture complex, list-level user biases and behaviors (such as position bias, diversity, and similarity aversion). RewardRank operates in two phases: Reward Model, A permutation-aware Transformer encoder is trained to predict the scalar utility (e.g., click/purchase probability) for any given ranking permutation, modeling list-level preferences, and Ranker Optimization, A ranker is trained to maximize the predicted utility using the SoftSort operator for end-to-end differentiable optimization over the permutation space. A Reward Correction Term is introduced to mitigate the risk of reward model misspecification. The framework achieved state-of-the-art results on two novel, automated counterfactual evaluation protocols (PO-Eval and LAU-Eval) and demonstrated significant improvements on human-labeled relevance metrics using the Baidu-ULTR dataset.

### Strengths
1. Addresses the fundamental limitation of traditional LTR by directly optimizing for complex, list-level user utility, bypassing simplified proxy objectives and effectively capturing permutation-aware behavioral biases.

2. Introduction of PO-Eval and LAU-Eval (LLM-As-User) provides standardized, scalable, and automated benchmarks for counterfactual LTR assessment.

### Weaknesses
1. The permutation-aware RewardRank framework, particularly the Reward Model and SoftSort operator, requires significant computational resources. Scalability remains a challenge for very large datasets or long item permutations.

2. Despite the goal of optimizing true utility, the paper lacks crucial real-world A/B test results to directly verify performance gains over baselines, confining its claims to offline/counterfactual assessment.

3. It appears to be missing comparisons against the latest generator-evaluator-based reranking schemes, which are designed to handle list-level preferences and counterfactual exploration, such as PIER，GFN4Rec，NAR4Rec，MG-E. (See Questions for moree details)

### Questions
1. The paper reports SOTA results but primarily compares against traditional LTR and earlier counterfactual methods. It appears to be missing comparisons against the latest generator-evaluator-based reranking schemes, which are designed to handle list-level preferences and counterfactual exploration. Why were the following related, modern reranking works not included for comparison?

* Permutation-Level Interest-Based End-to-End Re-ranking Framework in E-commerce (PIER )
* Generative Flow Network for Listwise Recommendation (GFN4Rec) 
* Non-autoregressive Generative Models for Reranking Recommendation (NAR4Rec)
* Additionally, the related work Comprehensive list generation for multi-generator reranking (MG-E) was not cited. 

Can the authors comment on how RewardRank's approach theoretically or empirically differs from these generator-evaluator/reranking architectures?

2. The entire framework's success hinges on the Reward Model (RM) accurately learning and generalizing true user utility to the unseen counterfactual space. While the reward correction term is introduced, what is the sensitivity of the final ranking performance to a poorly trained or highly misspecified RM? Has the stability of the final ranker been tested under various levels of RM noise or error?

3. Can the authors provide a more rigorous theoretical derivation or a clearer explanation of the optimization goal achieved by the proposed reward correction term? Specifically, how does this term ensure robustness in the context of the highly non-linear and combinatorial ranking problem, and what are the theoretical boundaries on its effective strength ($\lambda$)?

4. The use of the SoftSort operator introduces a relaxation into the optimization process. The paper is highly empirical; can the authors provide any theoretical analysis or proof of convergence for the ranker optimization step when using SoftSort in this specific maximum-utility objective? How close is the relaxed solution to the true discrete global optimum?

5. Given the reliance on a complex Transformer-based Reward Model that is queried during the ranker's optimization/inference, what are the anticipated real-world latency implications of deploying RewardRank in a production environment? Was any pilot A/B test conducted, and if so, what were the results regarding business metrics (e.g., revenue, user retention) and serving latency compared to the production baseline?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper proposes RewardRank, a two-stage counterfactual learning-to-rank framework that explicitly optimizes true list-level utility rather than traditional heuristic relevance metrics. A reward model predicts engagement-related utility over full permutations, and a ranker is trained to maximize this reward with a differentiable sorting operator (SoftSort). To address the lack of benchmarks, the authors introduce two evaluation suites: PO-Eval using a parametric click model on Baidu-ULTR data, and LAU-Eval, where an LLM simulates user preferences on a modified Amazon KDD-Cup dataset. The method reports state-of-the-art counterfactual utility and outperforms baselines on standard relevance metrics as well.

### Strengths
1. The studied problem is well-motivated. Utility optimization is meaningful in many realistic scenarios.
2. Differentiable permutation modeling with SoftSort is nicely integrated and technically sound.
3. The attempt to create a reproducible counterfactual evaluation is valuable for the community.
4. The writing and presentation are good.

### Weaknesses
1. The problem formulation and proposed approach have limited novelty. Training a reward model to estimate the reward of a ranking list in both search and recommendation is common, such as:
* "Model-based unbiased learning to rank. D Luo, L Zou, Q Ai, Z Chen, D Yin, BD Davison".  Optimizing towards an overall metric, given a list rather than pointwise evaluation of each result, has also been studied. 
* "Reinforcement Learning to Rank Using Coarse-grained Rewards." Tu, Yiteng; Xu, Zhichao; Yang, Tao; Su, Weihang; Zhou, Yujia; Liu, Yiqun; Lin, Fen; Liu, Qin; Ai, Qingyao. 
* Unbiased learning to rank regarding position bias in real-world click data, etc., that also works on the BaiduLTR dataset: 

2. Some important baselines are missing (e.g., on tackling position bias in real-world click data, or context-aware is missing).
* "Unbiased Learning to Rank with Query-Level Click Propensity Estimation: Beyond Pointwise Observation and Relevance. Lulu Yu, Keping Bi, Jiafeng Guo, Shihao Liu, Dawei Yin, Xueqi Cheng". In TheWebConf 2025.
* "Unbiased Learning-to-Rank Needs Unconfounded Propensity Estimation." Dan Luo, Lixin Zou, Qingyao Ai, Zhiyu Chen, Chenliang Li, Dawei Yin, and Brian D Davison. In SIGIR 2024.
* “Towards disentangling relevance and bias in unbiased learning to rank." Yunan Zhang, Le Yan, Zhen Qin, Honglei Zhuang, Jiaming Shen, Xuanhui Wang, Michael Bendersky, and Marc Najork. 2023.  In SIGKDD’23. 
* "Adapting interactional observation embedding for counterfactual learning to rank." Mouxiang Chen, Chenghao Liu, Jianling Sun, and Steven CH Hoi. In SIGIR 2021. 

3. A large body of related works is missing, some of which are listed above. 

4. The evaluation is not very solid: The original ESCI human annotations are not used. Instead, LLM judgments are leveraged. 
* a. Using LLM-simulated human-like decisions (e.g., color/brand bias) lacks validation against real user studies, risking overfitting to synthetic patterns. 
* b. Baidu-ULTR experiment setting does not match the problem definition. There is no counterfactual utility in Baidu clicks; evaluation is on human-assigned relevance labels.

### Questions
1. Which dataset do the results in Table 1 report? I cannot find it anywhere in the paper. 
2. In Line 142, it mentions that reranking methods rely on a strong base ranker for comparison. The proposed method does not rely on a base ranker? I'm a bit confused.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper studies a reward model to estimate the utility of ranking, taking the interaction among items (positions) into account. Specifically, by utilizing the transformer architecture, the reward model can encode linear interaction among items in ranking, taking diversity or positional effect into account. The proposed method also tries to maximize the pessimistic estimate of the policy performance by penalizing the uncertainty in the prediction. The experiment on two datasets demonstrates that the proposed method works well on the expected reward metric by taking the item-item interactions into account, while baselines focus on the relevance scores, such as NDCG.

### Strengths
- The proposed approach can consider the interaction among items (positions) by using the attention mechanism of the reward model (although only encoding linear interactions).

- The two benchmark setups used in the experiment should be useful for other ranking papers and the community, too. Especially, demonstrating that the metrics of expected reward and NDCG may be different can be a useful takeaway. The results also show that the proposed method works well on these benchmarks.

- The related work mentions representative ranking papers.

### Weaknesses
- The main concern I have is whether the proposed ranker loss adequately addresses the distribution shift issue. In my understanding, the discounting weight ($|u_i - \hat{u}_i|$) is calculated on the observed samples, regardless of the results of the soft-ranked results (i.e., choice of the optimized model). Moreover, downweighting the uncertain sample seems to work well when the logging data contains a high reward value, like an imitation learning. Clarification on this point should be useful.

- Regarding the above point, how does the proposed method work compared with a simple imitation learning or off-policy learning baseline, such as Chen et al., 19. I wonder if the improvement of performance comes from the good performance of the data collection policy or the actual effects of the algorithm.

- Initially, I'm a bit confused about what parameters $\phi$ and $\theta$ refer to. After carefully re-reading the paper, I found that probably the attention matrices (e.g., $v$) are $\phi$ and $\Pi$ are $\theta$, but additional clarification is needed for this part.

Chen et al., 19. Top-K Off-Policy Correction for a REINFORCE Recommender System. https://arxiv.org/abs/1812.02353

### Questions
- How does the proposed method address the distribution shifts?

- How does the proposed method work compared with imitation learning?

- Nits: The parentheses are corrupt in Eq (13).

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3