# Dataset Condensation with Sharpness-Aware Trajectory Matching

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 5, 5, 6

## Abstract
Dataset condensation aims to synthesise datasets with a few representative samples that can effectively represent the original datasets. This enables efficient training and produces models with performance close to those trained on the original sets. Most existing dataset condensation methods conduct dataset learning under the bilevel (inner and outer loop) based optimisation. However, due to its notoriously complicated loss landscape and expensive time-space complexity, the preceding methods either develop advanced training protocols so that the learned datasets generalise to unseen tasks or reduce the inner loop learning cost increasing proportionally to the unrolling steps. This phenomenon deteriorates when the datasets are learned via matching the trajectories of networks trained on the real and synthetic datasets with a long horizon inner loop. To address these issues, we introduce Sharpness-Aware Trajectory Matching (SATM), which enhances the generalisation capability of learned synthetic datasets by minimising sharpness in the outer loop of bilevel optimisation. Moreover, our approach is coupled with an efficient hypergradient approximation that is mathematically well-supported and straightforward to implement along with controllable computational overhead. Empirical evaluations of SATM demonstrate its effectiveness across various applications, including standard in-domain benchmarks and out-of-domain settings. Moreover, its easy-to-implement properties afford flexibility, allowing it to integrate with other advanced sharpness-aware minimisers. We will release our code on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper enhances the generalization capability of dataset condensation by minimizing sharpness in the outer loop of bilevel optimization. Specifically, it introduces Sharpness-Aware Trajectory Matching (SATM), a variant of trajectory matching. SATM jointly minimizes the sharpness and the distance between training trajectories with a tailored loss landscape smoothing strategy. This paper also introduces some techniques to tackle the problems of using SATM, such as the computational overhead, redundancy of the (hyper) gradient calculation, and hyperparameter tuning.
According to the experiments, it achieves the best results in the conventional dataset condensation setting and also shows impressive results in the OOD setting, demonstrating great generalization capability.

### Strengths
1. Generalization capability is a good research topic in dataset condensation, and a few papers study it.
2. The overall writing and presentation are satisfactory. 
3. SATM and some techniques to tackle the problems when using SATM are novel.

### Weaknesses
Missing comparisons with SOTA methods, such as DATM, RDED, and CUDD.
Towards Lossless Dataset Distillation via Difficulty-Aligned Trajectory Matching
On the Diversity and Realism of Distilled Dataset: An Efficient Dataset Distillation Paradigm
Curriculum Dataset Distillation

### Questions
How about the results on ResNet-101 and ImageNet-1K.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Sharpness-Aware Trajectory Matching (SATM) as an approach to improve dataset condensation. The goal is to synthesize representative samples from large datasets, reducing both computational costs and training time. SATM enhances generalization by minimizing the sharpness in the outer loop of bilevel optimization and uses efficient hypergradient approximation techniques to control memory and computational costs. The method outperforms existing condensation approaches across in-domain and out-of-domain benchmarks, particularly when used in conjunction with sharpness-aware minimization methods.

### Strengths
1. SATM’s use of sharpness-aware trajectory matching addresses generalization issues in previous dataset condensation methods and introduces a theoretically sound approach to managing computational complexity.

2. The proposed hypergradient approximation strategies reduce computational overhead, making SATM adaptable and efficient.
3. SATM demonstrates robust performance gains over other state-of-the-art methods across various benchmarks and settings.
4. SATM is compatible with other sharpness-aware optimizers, making it adaptable to a wide range of machine-learning tasks.

### Weaknesses
1. **Proposition 3.1**: Could the authors clarify whether $\alpha J$ is greater than or less than 1? If $\alpha J > 1$, the inequality appears incorrect since the norm cannot be bounded by a negative value on the right-hand side. If $\alpha J < 1$, a smaller $\iota$ would yield a tighter bound. Therefore, a discussion on the trade-off between the number of truncated steps and performance is needed. An ablation study on this trade-off would add valuable insights.

2. **Theorem 3.2**: $\theta$ should be treated as a vector, so $\Delta \theta_\tau$ is also a vector, not a scalar. Additionally, the bound on $|\|\Delta \theta_\tau\||$ makes more sense to me, and the upper bound of $\Delta \theta_\tau$ does not necessarily imply that $\theta_\tau$ is close to $\hat{\theta}_\tau$. 

3. **Sharpness-Aware Minimization**: Sharpness-aware minimization is known to impose a significant computational burden. The authors argue that minimizing sharpness enhances generalization, but could they elaborate on why sharpness minimization is particularly beneficial in the context of dataset condensation? Further insights on this aspect would strengthen the motivation behind using sharpness-aware methods here.

4. **Formatting Issues**: Ensure there is a space between "min" and $\mathcal{L}$; additionally, Figure 1 currently displays an incomplete label for "training iteration."

### Questions
See weakness

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This article mainly builds on the MTT method, which aims to make a network mimic the training patterns of real data by ensuring that the paths (or parameter trajectories) created with synthetic data align with those from real data. The improvement here is adding a "sharpness-smoothing" strategy with Bayesian Optimization (BO) to approximate sharpness, plus a few other gradient tweaks.

### Strengths
This article does a solid job of exploring optimization theory, with most of the formula derivations being accurate. The experimental setup is also fairly thorough.

### Weaknesses
This article seems like a patchwork of various innovative points. The main concern is that the baseline experimental data is identical to that in the reference paper, Minimizing the Accumulated Trajectory Error to Improve Dataset Distillation. While it's understandable for the data to be similar, it raises the question: was the author involved in the previous paper? If so, please clarify this connection.

This article does a solid job of exploring optimization theory, with most of the formula derivations being accurate. The experimental setup is also fairly thorough. However, the innovation in the method isn't major. It mostly combines BO with MTT. There's no new data compression method, just some changes to the optimization steps. For improving data compression, the focus should be on synthesizing effective datasets to cut down the need for lots of data, not on cutting the cost of loop optimization. Also, for experiments with DC, DM, MMT, etc., the results are the same as those in the paper "Minimizing the Accumulated Trajectory Error to Improve Dataset Distillation." Please list specific settings like the learning rate.

### Questions
1. The innovation in the method isnt major. It mostly combines BO with MTT. There's no new data compression method, just some changes to the optimization steps.
2. For improving data compression, the focus should be on synthesizing effective datasets to cut down the need for lots of data, not on cutting the cost of loop optimization.
3.Also, for experiments with DC, DM, MMT, etc., the results are the same as those in the paper "Minimizing the Accumulated Trajectory Error to Improve Dataset Distillation." Please list specific settings like the learning rate.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a new approach of the Dataset Distillation method with Sharpness-Aware Minimisation (SAM).

### Strengths
The theoretical analysis and proofs are sufficient. The authors detailed the approach of Matching Training Trajectory (MTT) with SAM. The proof of the theorem is provided and technically sound. 

The manuscript is well-structured.

### Weaknesses
Though the proposed approach is technically sound, my main concern is that the experiments can’t support the claims of the proposed model. Specifically,

1. The proposed method claims to reduce the computation overhead and the time complexity of the MTT. However, the method doesn’t provide a computational cost comparison with the current methods.

2. The proposed method claims that the memory cost is also reduced. Given that the baseline Tesla [1] mentioned in the manuscript already reduces the memory cost so that the distillation of ImageNet-1K becomes available, evaluating the effectiveness of the proposed method on ImageNet would be beneficial. 

[1] Justin Cui, Ruochen Wang, Si Si, Cho-Jui Hsieh. “Scaling Up Dataset Distillation to ImageNet-1K with Constant Memory,” NeurIPS 2022.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to improve the performance of trajectory-matching based dataset distillation method by using sharpness-aware minimiser (SAM) to flatten the trajectory used for matching.
Also, to mitigate the additional budget introduced by SAM, several tricks including truncate unrolling hypergradient and trajectory resuing are proposed.

### Strengths
1. Good writing, easy to follow.
2. The author gives comprehensive math proof of how to efficiently integrate SAM into trajectory matching-based distillation method, improving this paper's soundness.

### Weaknesses
1. Missing comparison with SOTA methods such as DATM [1] in Table 2.

2. Only one ablation study (on sharpness-aware optimization method) is conducted. Authors should also conduct ablation studies on the proposed trajectory resuing and hyper-gradient truncating methods to prove their effectiveness.

3. Poor performance. Compared with FTD [2], which also proposes to use SAM, the performance improvement brought by SATM becomes marginal as IPC increases (less than 0.2% on CIFAR, IPC50). Is this method only effective in low IPC cases?

4. The distillation cost is only calculated in theory. Comparisons of the distillation cost in practice should be included.

5. The evaluation setting is not introduced clearly, whether the zca whitening, EMA, and DSA augment are used?

### Questions
Please see weakness

### Soundness
3

### Presentation
3

### Contribution
2
