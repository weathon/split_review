# Dynamic Elimination For PAC Optimal Item Selection From Relative Feedback

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
We study the problem of best-item identification from relative feedback where a learner adaptively plays subsets of items and receives stochastic feedback in the form of the best item in the set. We propose an algorithm - Dynamic Elimination (DE) - that dynamically prunes sub-optimal items from contention to efficiently identify the best item and show a strong sample complexity upper bound for it. We further formalize the notion of inferred updates to obtain estimates on item win rates without directly playing them by leveraging item correlation information. We propose the Dynamic Elimination by Correlation (DEBC) algorithm as an extension to DE with inferred updates. We show through extensive experiments that DE and DEBC significantly outperform all existing baselines across multiple datasets in various settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work addresses the problem of identifying the best item from a set of items based on relative feedback, specifically using a method called Dynamic Elimination (DE). DE efficiently prunes sub-optimal items as it progresses, improving sample complexity compared to existing algorithms. The authors also propose an extension, Dynamic Elimination by Correlation (DEBC), which incorporates inferred updates based on item correlations. DEBC significantly outperforms DE in settings where item correlation is strong, reducing sample complexity further. Extensive experiments demonstrate that both DE and DEBC outperform existing state-of-the-art (SOTA) methods in terms of sample complexity across multiple datasets and settings. Additionally, the paper explores future directions for improving sample complexity bounds and extending the methods to partial/full rankings.

### Strengths
1. DE and its extension, DEBC, significantly improve sample complexity for identifying the best item compared to existing algorithms, reducing the number of subset plays needed.

2. The incorporation of inferred updates through item correlation in DEBC provides a robust mechanism to handle correlated item structures, leading to superior performance in certain datasets.

3. The paper extensively evaluates DE and DEBC across various synthetic and real-world datasets, demonstrating their practical effectiveness and robustness across different settings.

### Weaknesses
The algorithmic contribution of this looks narrow. The core idea of DE is flexibly eliminating items once they are deemed suboptimal. This idea is old in the bandit literature. The authors can refer to Chapter 6 of [3] for some reference.  Also, a simple google search would gives you a number of work on elimination algorithms. The core idea of DEBC is exploiting the generalized linear structure on the correlation among arms. This idea is also not new since linear structure has been extensively studied in linear bandits, reinforcement learning. Please refer to Part V of [3] from some details.

The proof techniques of this paper are not new, most of them are drawn from literature. Thus, this paper does not contribute to new proof techniques.  To me more specific, compared to [1,2], I do not see enough new ideas in the proof.  For example, the analysis of concentration, probability of event, etc., looks very normal. Could the author elaborate on the novelty of the proof?

The theoretical improvement over SOTA techniques is not clear. The improvement on the sample complexity compared with SOTA works is not stated.  How does it improve the sample complexity upper bound?

The second paragraph of the related work overstated the limitations of previous works without any supporting evidence. Previous algorithms may require up to millions of samples to rank only a few items, but this possibility depends on the setting of the problem. It should not be stated as a general claim. Furthermore, this paragraph is not precise. What do you mean by often? Could you quantify it?

Lemma 1 is confusing. It is highlighted as a lower bound, but the sample complexity is stated using the big O notation.

### Questions
How can the sample complexity bounds be further improved to match the practical performance observed in experiments, and is there potential for achieving instance-optimal sample complexity in the PAC best-item setting?

Could the proposed DE and DEBC algorithms be adapted or extended to work with partial or full rankings instead of just identifying the best item, and what challenges might arise in such extensions?

How would the algorithms perform in settings where item correlations are dynamic or evolve over time, and what adjustments to DE/DEBC might be necessary to handle such changes effectively?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors have introduced a dynamic elimination method for item selection based on relative feedback. They propose two distinct algorithms: one that implements the fundamental dynamic elimination approach and another that incorporates item correlations into the elimination process. The paper provides theoretical analysis on both the sample complexities and the correctness of the proposed methods. Furthermore, the authors demonstrate the proposed methods' ability in terms of reducing sample complexities when compared to several baseline approaches.

### Strengths
S1: The proposed methods enhance existing approaches by dynamically eliminating suboptimal items, significantly reducing the algorithm's complexity.

S2: By incorporating correlations between items, the proposed methods extend their applicability to items initially absent from the played set.

S3: The authors offer theoretical assurances regarding the sample complexity of DE and DEBC. They also demonstrate that the sample mean of an inferred update sequence serves as an unbiased estimator.

### Weaknesses
The significance of this paper's results is questionable. For the best item identification, the sample complexity (worst-case) is O(n*\epsilon^{-2} *\log(n*n_s^{-1}*\delta^{-1})). However, in a previous paper [1], when n_s = 2 (i.e., pairwise comparisons), the sample complexity (expected) for best item identification is O(n*\epsilon^{-2} *\log\delta^{-1})) (Theorem 5 of [1]), which is log(n) better than the proposed algorithm. When n_s is large enough like \Omega(n), the sample complexity of the proposed in this paper will become the same as that in [1]. Hence, the proposed algorithm does not show superiority compared to existing algorithms, or at least be as good as existing ones. Although its sample complexity is worst case instead of in expectation, but this difference is not large enough to support the significance of the new results. 

Besides, the winning chance estimation and the sample complexity of best item identification seem not to be correlated enough to be put in the same paper. Putting them in one paper makes the paper's scope to be ambiguous. If the winning chance estimate is significant enough, it is better to be placed in another paper focusing on a more related topic.

### Questions
Q1: It would be appreciated if the authors could include additional experiments conducted in real-world scenarios. These experiments should aim to demonstrate the effectiveness of the proposed methods in best item identification. Additionally, it is recommended that results be presented using widely accepted metrics such as accuracy, AUC, F1, precision, and recall. 
Q2: The authors might consider providing a more precise and explicit formulation of the item selection problem in Section 3. Furthermore, it would be valuable to discuss in greater detail how DE and DEBC can be applied in practical, real-world contexts.

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
3

### Summary
This paper studies the problem of best-item identification from relative feedback in the setting where a learner adaptively plays subsets of items and receives stochastic feedback in the form of the best item in the set. An algorithm named Dynamic Elimination (DE) is proposed, which dynamically prunes sub-optimal items from contention to efficiently identify the best item. Then the model is extended to capture the generalized linear correlation of items. An algorithm named DEBC, an extension of DE is proposed to handle this extension. The core idea is leveraging the generalized linear correlation to obtain estimates on item win rates without directly playing them by leveraging item correlation information. Extensive experiments are conducted to validate the empirical performance of the proposed algorithm.

### Strengths
This paper studies an important problem.  

The proposed algorithm is complemented with theoretical analysis as well as extensive experiments.

### Weaknesses
The algorithmic contribution of this looks narrow. The core idea of DE is flexibly eliminating items once they are deemed suboptimal. This idea is old in the bandit literature. The authors can refer to Chapter 6 of [3] for some reference.  Also, a simple google search would gives you a number of work on elimination algorithms. The core idea of DEBC is exploiting the generalized linear structure on the correlation among arms. This idea is also not new since linear structure has been extensively studied in linear bandits, reinforcement learning. Please refer to Part V of [3] from some details.  

The proof techniques of this paper are not new, most of them are drawn from literature. Thus, this paper does not contribute to new proof techniques.  To me more specific, compared to [1,2], I do not see enough new ideas in the proof.  For example, the analysis of concentration, probability of event, etc., looks very normal. Could the author elaborate on the novelty of the proof? 

The theoretical improvement over SOTA techniques is not clear. The improvement on the sample complexity compared with SOTA works is not stated.  How does it improve the sample complexity upper bound? 

The second paragraph of the related work overstated the limitations of previous works without any supporting evidence. Previous algorithms may require up to millions of samples to rank only a few items, but this possibility depends on the setting of the problem. It should not be stated as a general claim. Furthermore, this paragraph is not precise. What do you mean by often? Could you quantify it? 

Lemma 1 is confusing. It is highlighted as a lower bound, but the sample complexity is stated using the big O notation.  

[1] Yisong Yue, et al. The K-armed Dueling Bandits Problem, Journal of Computer and System Sciences, 78(5): 1538–1556.

[2] Björn Haddenhorst. Identification of the Generalized Condorcet Winner in Multi-dueling Bandits, NeurIPS, 2021

[3] Tor Lattimore, et al. Bandit Algorithms. Cambridge press.

### Questions
See weakness part.

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
4

### Summary
This paper studies the best item selection problem from noisy multi-wise comparisons. There are totally n items, and at each round the agent can select n_s items to compare, and the comparison will return one item as the winner according to the PL model. The better item will have a higher chance to win the comparison. The problem is to find the best item with 1-\delta confidence with the least amount of comparisons. 

The authors propose a new algorithm for best item selection from multi-wise comparisons and give the worst-case, best-case, and expected sample complexity. The authors further propose a method to estimate the winning probabilities between two items without directly comparing these two items.

### Strengths
This paper proposes new algorithms for best item identification and winning rate estimation. These algorithms do have some novelty and are inspiring.

### Weaknesses
The significance of this paper's results is questionable. For the best item identification, the sample complexity (worst-case) is O(n*\epsilon^{-2} *\log(n*n_s^{-1}*\delta^{-1})). However, in a previous paper [1], when n_s = 2 (i.e., pairwise comparisons), the sample complexity (expected) for best item identification is O(n*\epsilon^{-2} *\log\delta^{-1})) (Theorem 5 of [1]), which is log(n) better than the proposed algorithm. When n_s is large enough like \Omega(n), the sample complexity of the proposed in this paper will become the same as that in [1]. Hence, the proposed algorithm does not show superiority compared to existing algorithms, or at least be as good as existing ones. Although its sample complexity is worst case instead of in expectation, but this difference is not large enough to support the significance of the new results. 

Besides, the winning chance estimation and the sample complexity of best item identification seem not to be correlated enough to be put in the same paper. Putting them in one paper makes the paper's scope to be ambiguous. If the winning chance estimate is significant enough, it is better to be placed in another paper focusing on a more related topic.

[1] Ren, W., Liu, J., & Shroff, N. (2020, November). The Sample Complexity of Best-$ k $ Items Selection from Pairwise Comparisons. In International Conference on Machine Learning (pp. 8051-8072). PMLR.

### Questions
It will help if the authors can have more evidence to demonstrate this paper's results' significance. 
Or if I perceive this paper wrongly, please let me know.

### Soundness
3

### Presentation
3

### Contribution
2
