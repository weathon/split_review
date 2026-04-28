# Doubly Robust Instance-Reweighted Adversarial Training

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Assigning importance weights to adversarial data has achieved great success in training adversarially robust networks under limited model capacity. However, existing instance-reweighted adversarial training (AT) methods heavily depend on heuristics and/or geometric interpretations to determine those importance weights, making these algorithms lack rigorous theoretical justification/guarantee. Moreover, recent research has shown that adversarial training suffers from a severe non-uniform robust performance across the training distribution, e.g., data points belonging to some classes can be much more vulnerable to adversarial attacks than others. To address both issues, in this paper, we propose a novel doubly-robust instance reweighted AT framework, which allows to obtain the importance weights via exploring distributionally robust optimization (DRO) techniques, and at the same time boosts the robustness on the most vulnerable examples. In particular, our importance weights are obtained by optimizing the KL-divergence regularized loss function, which allows us to devise new algorithms with a theoretical convergence guarantee. 
Experiments on standard classification datasets demonstrate that our proposed approach outperforms related state-of-the-art baseline methods in terms of average robust performance, and at the same time improves the robustness against attacks on the weakest data points. Codes will be available soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a instance reweighting based adversarial training (AT) framework. Consequently, the authors follow the setting of Zhang et al. 2022  (bilevel optimization formulation for AT) and add the instance reweighting mechanism into it. Moreover, the authors seek to  build a model in the outer level problem that is robust not only to the adversarial examples but also to the worst-case attack distribution.  Compared with the exisiting instance reweighting AT methods, the proposed method  obtain the importance weights by distributionally robust optimization (DRO). The DRO is a more sophisticated choice than the heuristic/geometric schemes of instance rewweighting. Furthermore, the authors propose an equivalent compositional optimization problem (Eq. (6)) and adopt the log-barrier penalty function to drop the challenging $\ell_{\infty}$ norm constraint. The final optimization problem is Eq. (7) and the authors modify SCGD into the compositional implicit differentiation (CID) algorithm to solve it. With some common used assumptions, the authors establish the convegence result for CID. 
In the experimental studies, the authors compare three instance re-weighted adversarial training methods with the proposed method on four small-scale datasets. The proposed method show promising improvement on RA-PGD, RA-Tail-30 and RA-AA metric.

### Strengths
1. The paper is well-written and easy to follow. 
2. The motivation is clear and the equivalent compositional optimization problem is reasonable. 
3. The proposed CID method has convergence guarantee.

### Weaknesses
1. The empirical studies is not sufficient. Only small-scale datasets is adopted in the experiment. The lack of experiments on larger, more complex datasets limits the generalizability of the findings. It is unclear if the observed improvements would hold on datasets with higher dimensionality or more intricate data distributions.
2. The computational analysis is missing. The paper lacks a thorough analysis of the computational cost associated with the proposed method. Specifically, there is no discussion of the time and memory requirements, which are crucial for assessing the practical applicability of the approach. A comparison with the computational demands of existing adversarial training methods would be beneficial.
3. The justifiability of the assumptions is not discussed. While the authors mention that Assumptions 1-3 are standard, they do not provide a detailed discussion on whether these assumptions are reasonable in the context of adversarial training. The validity of these assumptions should be carefully examined, as they directly impact the convergence guarantees of the proposed algorithm.
4. The SA performance is a weakness of the proposed method. The paper acknowledges that the proposed method does not improve standard accuracy (SA). It is important to provide a more in-depth analysis of why this limitation exists and how it could potentially be addressed. The trade-off between robust accuracy and standard accuracy needs to be explored further.

### Questions
1. In Eq. (7)，is the constraint $\delta\in\mathcal{C}_i$ correct? The author claim that "Note that now the constraint $\{\delta\in\mathcal{C}_i\}$ is never binding in Equation (7), because the log-barrier penalty forces the minimizer of $\ell^{bar}_{i}$ to be strictly inside the constraint set." Moreover, in Algorithm 1 Line 5-7, why need the projected operator to keep $\delta_{i,t}^{k}$ in $\mathcal{C}$?

2. It is better to discuss the justifiability  of Assumption 1-3 for AT problem. 

3. The SA performance is a weaknness of the proposed method. It is better to explain this limitation. 

4. It is better to add some statistical analyses like  P-values, CIs, effect sizes, and so on.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addressed the challenge of adversarial robustness on most vulnerable samples. The existing approaches adopt a instance-reweighted strategy towards improving the worse case robustness. However, there is no principled way to estimate the per-sample weight. This work combines instance-reweighting with bi-level optimization for adversarial robustness. The min-max problem for instance-reweighting optimization was solve with a equivalent compositional bilevel optimization problem.

### Strengths
Strength:

1. The mathematical formulation of instance-reweighted bilevel optimization is solved in an elegant manner.

2. The evaluation on imbalanced dataset suggest the worst case adversarial robustness can be improved.

### Weaknesses
Weakenss:

1. The improvements on PGD and AutoAttack seem to be less significant. The more significant improvements are observed from RA-Tail-30. Therefore, it is necessary to provide more details of the evaluation protocol for RA-Tail-30. Specifically, the paper should clarify how the 30% most vulnerable classes are determined and if this selection process is consistent across different experimental runs. It is also important to understand the variance in the RA-Tail-30 metric, as a small number of classes can greatly influence this metric, making it sensitive to minor changes in the training process.

2. Since the advantage is mainly demonstrated at the imbalanced dataset, the current evaluations on Imbalanced datasets (CIFAR10 and SVHN imbalanced) are not enough for analyzing the performance breakpoint. The paper needs to explore a wider range of imbalance ratios and provide a more granular analysis of how performance degrades as the imbalance becomes more severe. Furthermore, the specific method used to create the imbalanced datasets (e.g., class subsampling) should be detailed, as this can significantly impact the observed results.

3. Comparisons with more recent adversarial training methods are missing. The absence of comparisons with state-of-the-art adversarial training techniques makes it difficult to assess the true contribution of the proposed method. It is crucial to benchmark against the latest methods to demonstrate that the proposed approach offers a genuine improvement over the current best practices.

### Questions
It is encouraged to make comparisons with more recent adversarial training methods.

Experiments on more diverse imbalance degrees are necessary for more comprehensive evaluation.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel framework called Doubly Robust Instance-Reweighted Adversarial Training to address the issues of heuristics and non-uniform robust performance in adversarial training. The approach utilizes distributionally robust optimization techniques to obtain importance weights and boost robustness on vulnerable examples. The experiments show that the proposed method outperforms state-of-the-arts on standard classification datasets.

### Strengths
1. The proposed framework addresses the issues of heuristics and non-uniform robust performance in adversarial training. The authors use a doubly robust optimization (DRO) approach that is theoretically grounded. It provides a principled way to reweight the training examples based on their vulnerability to adversarial attacks. 

2. Even the algorithm falls under the category of iteratively-reweighted adversarial attack, this paper has a more principled optimization formulation than previous works because its DRO approach combines two different models to estimate the importance weights of each training example, and to estimate the importance weights, which is more robust to model misspecification and can handle a wider range of distributional shifts compared to traditional optimization methods. The obtained weights are optimal for the DRO optimization problem defined in Eq. 5 (with the closed-form exact solution for the weights), rather than being ad-hoc picked. This is the most important difference form previous instance-wise or iterative attacks.

3. The bilevel optimization formulation of AT gives one the flexibility to separately design the inner and outer level objectives. This enables the authors to independently construct a new outer level objective that also solves for the instance weights w, and an inner level objective for regularized attack. This flexibility allows for a more generic and powerful framework than the traditional AT formulation, which is limited to a single objective function.

4. The proposed method outperforms several state-of-the-art baselines on standard classification datasets, in terms of robustness against multiple adversarial attacks. They also show that their method can improve the robustness of the weakest (worst-case) data points, which is an important property for real-world applications.

### Weaknesses
Since the algorithm requires computing Jacobian inner products to perform parameter updates in the bi-level optimization, could the authors comment on the incurred time complexity? I am wondering if the algorithm runs much slower than vanilla AT (but only improves the robust accuracy moderately).

In their experiments, the authors have compared with AutoAttack which is good, but not with other SOTA methods such as TRADES or Diffusion-based Defense (ICML 2023). Adding some more comparison method would be good.

### Questions
See the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
