# Which Algorithms Have Tight Generalization Bounds?

- Decision: Reject
- Avg Score: 5.00
- Scores: 1, 5, 6, 8

## Abstract
We study which machine learning algorithms have tight generalization bounds. First, we present conditions that preclude the existence of tight generalization bounds. Specifically, we show that algorithms that have certain inductive biases that cause them to be unstable do not admit tight generalization bounds. Next, we show that algorithms that are sufficiently stable do have tight generalization bounds.  We conclude with a simple characterization that relates the existence of tight generalization bounds to the conditional variance of the algorithm's loss.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This work examines the conditions under which learning algorithms achieve tight bounds. To this end, the authors introduce a new definition of stability and explore its implications.

### Strengths
The paper is well-written.

### Weaknesses
 - There are various mathematical models for over-parameterization in the literature. However, the authors do not mention related work on generalization error analysis within the over-parameterization regime. For instance, generalization error has been studied in frameworks such as the NTK [1] or Mean-field approaches [2,3,4]. In these studies, the authors do not assume zero training loss (or empirical risk) for all learning algorithms. Given that the primary claim of this paper concerns results for deep learning models, I believe the authors should compare their results to these works to better position their paper. Additionally, the authors refer to Appendix D of [6], which is incomplete.
- The current theoretical results are restrictive and apply only to binary classification. The core of the theoretical contribution seems to be negative results, which are derived for binary classification. It is unclear how these results extend to more general settings such as multi-class classification or regression, which are more common in practical applications of deep learning.
- The experiments are insufficient and require further exploration. Moreover, some experimental details are missing. For instance, what are the loss functions used in the experiments? The experimental section lacks sufficient detail to reproduce the results. Furthermore, the experiments should explore a wider range of hyperparameter settings and network architectures to support the theoretical claims.


### Questions
- Suppose someone extended the leave-one-out stability definition in [5] to a leave-k-out notion. What would be the specific difference between your stability notion and the leave-k-out notion?
- Could you provide a connection between your stability definition and the generalization error? For example, see Lemma 7 in [5].
- Why, in Definition 3.1, do you assume that $A$ is a mapping to $\\{\pm1\\}$?
- Why did the authors choose the neural network with 512 hidden neurons in the experiments? Why not 256 or fewer? Is there a particular reason?
- The authors define Definition 4.1 for the over-parameterized setting. Where is this used?

---

My current evaluation is strong reject. However, I am interested in reading authors's response.


---
**References:**

- [1]:Zixiang Chen, Yuan Cao, Quanquan Gu, and Tong Zhang. A generalized neural tangent kernel analysis for two-layer neural networks. Advances in Neural Information Processing Systems, 33: 13363–13373, 2020.
- [2]: Naoki Nishikawa, Taiji Suzuki, Atsushi Nitanda, and Denny Wu. Two-layer neural network on infinite dimensional data: global optimization guarantee in the mean-field regime. In Advances in Neural Information Processing Systems, 2022
- [3]: Atsushi Nitanda, Denny Wu, and Taiji Suzuki. Particle dual averaging: Optimization of mean field neural network with global convergence rate analysis. Advances in Neural Information Processing Systems, 34:19608–19621, 2021.
- [4]: Aminian, Gholamali, Samuel N. Cohen, and Łukasz Szpruch. "Mean-field Analysis of Generalization Errors." arXiv preprint arXiv:2306.11623 (2023).
- [5]: Bousquet, O., & Elisseeff, A. (2002). Stability and generalization. The Journal of Machine Learning Research, 2, 499–526. 
- [6]: Gastpar, M., Nachum, I., Shafer, J., & Weinberger, T. (2024). Fantastic generalization measures are nowhere to be found. The 12th International Conference on Learning Representations, ICLR 2024.

### Soundness
2

### Presentation
1

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
The paper investigates the conditions under which machine learning algorithms exhibit tight generalization bounds through the concept of estimability (Definition 1.2). By first providing illustrative examples, the authors introduce estimability as a framework for understanding generalization. The paper establishes that certain inductive biases, which lead to algorithmic instability, can prevent the existence of uniformly tight generalization bounds. Conversely, stable algorithms are more likely to achieve tight bounds, highlighting stability as a favorable trait for reliable generalization. Finally, the paper introduces a novel characterization that connects tight generalization bounds to the conditional variance of an algorithm's loss.

### Strengths
The paper provides clear examples in Section 1.2 that illustrate the relationship between learnability, estimability, and good learning algorithms.

### Weaknesses
The paper is difficult to follow, primarily due to its reliance on concepts introduced in previous work. For example, footnote 3 does little to clarify the concept of overparameterization, and I found it necessary to refer back to Gastpar et al. (2024) to grasp these foundational ideas.

Additionally, immediately following Definition 1.10, the authors specify that only deterministic algorithms are considered in the paper. This limitation raises questions about the applicability of the theoretical framework to practical settings, where randomized algorithm often plays a role. Incorporating expectations across this “channel” of randomness, as done in information-theoretic bounds, would seem a complex but necessary extension to make the framework more practically relevant.

### Questions
Can the proposed framework be extended to handle randomized algorithms? If not, what challenges prevent this extension?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper builds on the concept of the "Overparameterized setting" as defined in previous work (Gastpar et al., 2024), employing the recent notion of estimability to investigate conditions for the existence of tight generalization bounds for a given learning algorithm and distribution collection. The authors begin by showing that algorithms with certain inductive biases that lead to instability do not admit tight generalization bounds. Specifically, they demonstrate that when the amount of training data is significantly smaller than the hypothesis class’s VC dimension, it precludes worst-case estimability (Theorem 2.1).  Additionally, they establish inestimability for any algorithm with an inductive bias toward a class of nearly-orthogonal functions (Theorem 2.2).

Furthermore, they show that stability is a sufficient—but not necessary—condition for estimability. Notably, the paper's definition of stability differs from traditional leave-one-out algorithm stability (Bousquet and Elisseeff (2002)). They go on to prove that algorithms that are sufficiently stable do indeed possess tight generalization bounds (Theorem 3.3). Finally, they explain that whether an algorithm is estimable with respect to a set of distributions can be assessed by examining the conditional variance of the algorithm's loss, thereby relating the existence of tight generalization bounds to this conditional variance.

### Strengths
1. This paper addresses an often-overlooked issue in statistical learning theory: the concept of uniformly tight generalization bounds. By following the approach in Gastpar et al. (2024), the authors provide a particularly interesting perspective on the theoretical underpinnings of generalization error.

2. The detailed motivation and references regarding the definition of the overparameterized setting are invaluable for readers, especially as this overparameterized setting diverges from the more commonly understood notion of overparameterization (where the parameter count exceeds the sample size). Its purpose leans more towards serving as a definition for theoretical analysis.

3. The formal results and proofs appear sound and reasonably well-articulated, despite the fact that I have not verified every line of the proof.

4. Section 1.3 is particularly well-written, helping readers to quickly understand the paper’s theoretical results.

5. The paper’s approach of linking uniformly tight generalization bounds with estimability and traditional concepts like VC dimension and stability adds significant value, rendering the conclusions more intuitive and enhancing their relevance to established statistical learning theory.

### Weaknesses
1. The paper's title and abstract may give readers the impression that it explores which machine learning algorithms have tight generalization bounds in a broad context. However, the paper primarily focuses on the Overparameterized setting as defined within this work. While I acknowledge that the Overparameterized setting is prevalent in the deep learning community and holds significant theoretical value, there are models in deep learning that are not overparameterized, especially in resource-constrained scenarios or specific tasks, such as lightweight models designed to reduce parameter count and computational requirements. It would be beneficial for the authors to clarify in the abstract that their analysis is specific to the Overparameterized setting.

2. Adding more comparisons with Gastpar et al., 2024 could help to better delineate this paper’s contributions, as much of its setting and methodology are derived from that work. In fact, the central question of this paper—"Which machine learning algorithms have tight generalization bounds?"—originates from Question 2 in Gastpar et al., 2024: “For which algorithms does there exist a generalization bound that is tight for all population distributions in every overparameterized setting?” Therefore, a more detailed comparison with the conclusions of Gastpar et al., 2024, such as highlighting the additional insights provided by Theorem 2.1 in contrast to Theorem 2 in Gastpar et al., would enhance readers’ understanding of this paper’s contributions.

3. The statement in the related work section, “Our definition of an estimator EEE formalizes algorithm-dependent generalization bounds,” may be misleading, as the concept of estimability is derived from Gastpar et al., 2024, rather than being an original contribution of this paper.

4. The Introduction could benefit from a clearer summary of the main contributions. Additionally, the contributions of this paper appear somewhat limited, given that they build upon an already comprehensive theoretical framework established by Gastpar et al., 2024.

### Questions
The paper links the existence of tight generalization bounds to the conditional variance of the algorithm’s loss. How feasible is it to measure or approximate this conditional variance in practice, particularly for complex models like deep neural networks?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In prior work, it was established that it is not possible for generalization bounds to be tight uniformly across distributions if it does not explicitly incorporate the learning algorithm or data distribution. Building on this, the present paper studies conditions under which specific algorithms allow for tight generalization bounds, in the sense that they are close to the population loss for a family of distributions. Conditions are established for when this is possible (e.g., overparameterization and inductive bias) and when it is possible (a type of stability).

### Strengths
The contribution of the paper is significant in the sense that it formalizes and studies several notions related to generalization that are often discussed in loose terms. Taking a foundational approach like this to specify what goals we actually aim for, and conditions under which they are attainable, is important for the wider community. The presentation of the paper is overall clear and nicely written.

### Weaknesses
Some kind of small ablation in terms of model architecture could perhaps be interesting for the numerical experiments. At least something to indicate how the conclusions change with the scale of the model.

In some places, explicitly defining notation (even if it is standard) could be useful, e.g. $U(S)$ for uniform distribution on $S$.

This paper only considers deterministic algorithms. Are the general conclusions expected to hold for randomized ones? How would this differ?

Can you comment on any connection to stability-focused works in the information-theoretic gen. bound literature, such as “Sample-Conditioned Hypothesis Stability Sharpens Information-Theoretic Generalization Bounds” by Wang and Mao? Is this aligned with the notions of stability you consider?

### Questions
— This paper only considers deterministic algorithms. Are the general conclusions expected to hold for randomized ones? How would this differ?

— Can you comment on any connection to stability-focused works in the information-theoretic gen. bound literature, such as “Sample-Conditioned Hypothesis Stability Sharpens Information-Theoretic Generalization Bounds” by Wang and Mao? Is this aligned with the notions of stability you consider?

### Soundness
4

### Presentation
4

### Contribution
3
