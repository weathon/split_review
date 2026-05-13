# Enhancing Learning with Label Differential Privacy by Vector Approximation

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Label differential privacy (DP) is a framework that protects the privacy of labels in training datasets, while the feature vectors are public. Existing approaches protect the privacy of labels by flipping them randomly, and then train a model to make the output approximate the privatized label. However, as the number of classes $K$ increases, stronger randomization is needed, thus the performances of these methods become significantly worse. In this paper, we propose a vector approximation approach, which is easy to implement and introduces little additional computational overhead. Instead of flipping each label into a single scalar, our method converts each label into a random vector with $K$ components, whose expectations reflect class conditional probabilities. Intuitively, vector approximation retains more information than scalar labels. A brief theoretical analysis shows that the performance of our method only decays slightly with $K$. Finally, we conduct experiments on both synthesized and real datasets, which validate our theoretical analysis as well as the practical performance of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper consider the problem of supervised multi-class learning problem under the setting of "label differential privacy" (LDP). This is a setting that is well-studied in recent literature, where the input features are considered public, and only the label is considered sensitive and needs to be protected by differential privacy.

This paper proposes a new randomizing mechanism that satisfies LDP, and outperforms prior methods studied in literature. The new method is as follows: Suppose there are $K$ possible labels. Given any label $y \in [K]$, construct the $K$-dimensional one-hot encoding of $y$ and apply the (binary) Randomized Response mechanism on each bit of the one-hot encoding, flipping each bit with probability $\frac{1}{1 + e^{\epsilon/2}}$.

A theoretical analysis is done for the k-nearest neighbor learning rule showing that the excess risk grows as $\sim \sqrt{\ln K}$ with increasing $K$ (keeping other parameter fixed).

Experimental results show that this approach outperforms prior methods studied in literature on a synthetic dataset (mixture of Gaussians data with centers around a circle) as well as real data (MNIST, CIFAR).

### Strengths
The paper proposes a simple method and shows that it outperforms prior methods proposed in literature of LP-MST (Label Privacy Multi Stage Training [[Ghazi et al. '21](https://arxiv.org/abs/2102.06062)]) and ALIBI [[Malek et al. '21](https://arxiv.org/abs/2106.03408)].

The method is also simple to implement with minimal computational overhead relative to prior methods.

The paper is well written and easy to follow.

### Weaknesses
I feel there is rooom for making the paper stronger on the theoretical side.

I feel the analysis of k-NN is a bit incomplete (Appendix B.1) and doesn't highlight the complete picture. What I would have liked to see is how the excess risk decreases as $N \to \infty$ (see more details about this under "Questions").

Nevertheless, I find it quite interesting that such a simple method shows a clear improvement over prior methods in the experiments, and so I don't think of the above as a significant weakness, since the theoretical analysis is not critical for the experimental results.

### Questions
In particular, [Ghazi et al. '21](https://arxiv.org/abs/2102.06062) have an analysis in Appendix F where they show that the excess risk of learning with stochastic gradient descent is $K / \sqrt{N}$ for pure-DP and $\sqrt{K / N}$ for approximate-DP. A subsequent paper by [Ghazi et al. '24](https://arxiv.org/abs/2406.19040) provides a more complex method that can theoretically achieve a excess empirical error rate of $\sqrt{(\log K) / N}$.

But I think the $\sim \sqrt{(\log K) / k}$ scaling does not exactly say how the excess error scales with $N$. I would imagine that as $N \to \infty$, the optimal learning rule would also be scaling $k$ in some way, and not keep it fixed. I think this analysis might bring in dimensionality factors into the picture, which are necessary for understanding the precise scaling of excess risk with $N$.

---

On the experimental side, I am wondering if the authors have also considered datasets with non-uniform distribution over labels. For example, one could consider MNIST or CIFAR datasets by additional duplicates of certain labels to make the distribution of labels to be biased. How does the proposed method perform against prior methods, especially methods that use prior information (such as RRWithPrior or LP-MST)?

### Soundness
4

### Presentation
3

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
This paper introduces a new approach to local label differential privacy, transforming each label into a K-dimensional vector, where each component is independently randomized with a RAPPOR-like mechanism. This vector-based approach preserves more information than scalar label transformations while maintaining ε-local differential privacy. The authors provide theoretical analysis showing that their method's performance only degrades slightly with increasing number of classes K. They empirically validate their approach using both synthetic data and standard benchmark datasets (MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100), demonstrating that their method significantly outperforms existing approaches, especially when the number of classes is large and the privacy requirements are strict (small ε). Notably, proposed method outperforms a similar approach proposed by Malek Esmaeili et al. (2021), also relying on expanding a label to a vector of probabilities and adding noise to the vector.

### Strengths
1. The paper studies an important and well defined problem of label DP, which however does not get as much attention in the literature as traditional DP, while being relevant for many practical applications
2. The paper proposes a novel method to provide local label-only DP guarantees, and thoroughly explores it. The proposed method provides better utility (at the same privacy budget) compared to the prior methods on standard benchmarks. The paper provides necessary proofs of privacy guarantees, as well as general intuition behind the method.
3. The paper does a good job of putting this work in the context of the overall field, providing important details of prior works (notably, by Malek Esmaeili et al. (2021) as it shares the most similarities with the current paper)
4. The evaluation protocol looks solid and follows standard practices and baselines, including what is typically used by prior works.
5. The proposed practical implementation is quite neat, making the implementation of the method computationally efficient.

### Weaknesses
At it's core, the proposed method can be summarised as applying technique from RAPPOR (Erlingsson et al. (2014)) to the "soft label" approach to label DP introduced by ALIBI (Malek Esmaeili et al. (2021)). Both techniques are properly acknowledged by the authors, and combining two existing techniques in a novel way is not a weakness by itself. Especially given the strong empirical results and accompanying theoretical analysis. 

However, I believe this should affect the focus of the analysis. In particular, the main focus area for the theoretical part of the paper is answering the question "how does the excess risk grow with the number of classes K", implicitly comparing it with the randomized response and RRWithPrior (Ghazi et al. (2021)), which are known to degrade in utility with growing K. Given strong conceptual similarities between ALIBI and the method proposed here, as well as the fact that the former is the current state-of-the-art for label DP task, I would have expected the theoretical analysis to focus on comparing the two methods. Specifically, a more in-depth analysis of how the proposed method's error bounds compare to those of ALIBI would be beneficial. It's not clear if the analysis of $\Delta(x)$ is directly relevant for comparison with ALIBI, and if it is, this needs to be explicitly shown. The current analysis focuses on the dependence on K, but a comparison with the error bounds of ALIBI, which also uses a vector representation of labels, would provide a more direct and relevant comparison.

Additionally, citing computational efficiency ($O(K^2$) vs $O(K$)) when comparing the new approach with ALIBI (Malek Esmaeili et al. (2021)) looks misplaced, when in any practical ML application the cost of training would dominate over the computational cost of flipping labels. While the computational cost of label transformation might be relevant in some niche scenarios, in the context of the presented experiments, the training time is the dominant factor, making this comparison less meaningful.

### Questions
1. Can you elaborate your reasoning on the line 107: "However, ALIBI generates outputs using Bayesian inference and normalizes them to 1 using a softmax operation. Intuitively, such normalization causes bias"?
2. In section 4.3 Practical Implementation, how does changing the activation function of the last layer affects the model performance? Do you use this in the experiments chapter and if yes, how do you modify the training process?
3. To be pedantic, line 87 should say "Malek Esmaeili et al. (2021) proposes PATE-FM". Original PATE was introduced by [Papernot et al., 2016](https://arxiv.org/abs/1610.05755), and is not specific to label DP.

### Soundness
4

### Presentation
4

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
This paper introduces a new (?) approach for local label differential privacy (LDP) in machine learning, presenting both the theoretical framework and a numerical evaluation of the proposed method’s effectiveness. This method is based on a component-wise randomised response mechanism on the one-hot encoding of the class.

### Strengths
- The paper is well-organized and easy to follow, helping readers grasp the main ideas and methodology.
- The authors provide a numerical evaluation of the proposed methods, which helps to demonstrate its performance in practice.
- The authors provide a semi formal justification of the performance of the proposed method

### Weaknesses
 - The focus on local differential privacy is not clear from the title and abstract, which could be misleading for readers. Revising these sections to clearly indicate this focus would improve accessibility and transparency.
- The methods mentioned in the “Others” section of the related work could be discussed in more detail to give readers a clearer understanding of the techniques used in prior studies.
- The practical applicability of the method is limited, as it requires training a separate discriminant for each class, which could be cumbersome or impractical for larger or more complex tasks. Specifically, the need to train K separate classifiers, where K is the number of classes, introduces a significant computational overhead, especially when K is large. This approach contrasts with methods that learn a single classifier, making it less scalable to datasets with a high number of classes.
- The novelty of the proposed method is questionable, as noted by the authors themselves in lines 232-233, where they acknowledge its prior use in the literature. While the application of RAPPOR to label differential privacy is a specific use case, the core mechanism is not new, which raises concerns about the contribution.
- The authors claim that their method achieves better results by encoding more information in a vector rather than a scalar, but it remains unclear if this added information genuinely benefits the privacy-utility tradeoff. It would be valuable to see a theoretical result similar to Theorem 2 applied to the randomized response mechanism over the simplex to support a comparative analysis. The claim that vector encoding is superior to scalar encoding needs more rigorous justification, especially considering the increased dimensionality of the output space.

### Questions
Could the authors provide justifications or address the weaknesses mentioned above, especially regarding the novelty of the method and the theoretical basis of the claimed improvements? If these concerns are adequately addressed, I would be open to revising my rating and overall assessment of the paper.

### Soundness
3

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
4

### Summary
This paper introduces a vector approximation method aimed at improving label differential privacy (label DP) for large multi-class datasets. By encoding labels as vectors rather than scalars, the authors argue that this approach retains more class information, enabling better performance in high-class settings where traditional label DP methods degrade significantly. They present both theoretical analysis and empirical validation on synthesized and benchmark datasets, demonstrating superior accuracy, especially as the number of classes $K$ grows.

### Strengths
- The paper addresses a meaningful problem: label LDP learning with a large number of label classes. This has important practical relevance, particularly in applications with long-tailed data distributions.
- The paper proposes a simple yet effective technique to tackle this issue.
- The theoretical results are adaptable and could be extended to various scenarios under specific assumptions (e.g., smooth regression functions).
- The experimental results demonstrate significant improvements over previous methods.

### Weaknesses
 - The theoretical results provide only an upper bound for the proposed method. I suggest including additional comparisons and discussions between this bound and existing results. Additionally, could the authors establish any lower bounds for previous methods that use scalar labels alone (and possibly find the phase transition between $\log K$ and $K$ dependence)? Such bounds would clearly demonstrate the necessity of the proposed method. 
- The experiments were conducted on standard datasets. It would be valuable for the authors to conduct experiments on datasets with long-tailed distributions to highlight the method's practical relevance. Furthermore, it would be interesting to discuss how a long-tail distribution or class imbalance might impact the theoretical guarantees of the algorithm.
- The paper is somewhat repetitive and could benefit from further editing for conciseness.

### Questions
- What is the purpose of the footnote in Table 3?

Also, see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
