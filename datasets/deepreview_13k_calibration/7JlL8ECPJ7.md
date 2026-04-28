# Kernel Banzhaf: A Fast and Robust Estimator for Banzhaf Values

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Banzhaf values offer a simple and interpretable alternative to the widely-used Shapley values. We introduce Kernel Banzhaf, a novel algorithm inspired by KernelSHAP, that leverages an elegant connection between Banzhaf values and linear regression. Through extensive experiments on feature attribution tasks, we demonstrate that Kernel Banzhaf substantially outperforms other algorithms for estimating Banzhaf values in both sample efficiency and robustness to noise. Furthermore, we prove theoretical guarantees on the algorithm's performance, establishing Kernel Banzhaf as a valuable tool for interpretable machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Inspired by KernelSHAP, the paper introduces a method named "Kernel Banzhaf" that connects Banzhaf values to linear regression, leveraging "leverage score sampling" and "paired sampling" to approximate the Banzhaf values. The authors provide theoretical guarantees for the algorithm's performance and showcase its advantages in sample efficiency and robustness to noise through experiments on feature attribution tasks across eight datasets, outperforming existing estimators such as MC and MSR.

### Strengths
1. The paper is well-organized and clearly explains theoretical results and algorithms. In particular, I like that the authors kept the main paper simple while postponing the heavy theories and additional experiments and their analysis to the appendices. 
2. Kernel Banzhaf addresses a gap in the computation of Banzhaf values for arbitrary set functions, an area with limited prior research compared to Shapley values.
3. The algorithm has solid theoretical support, as demonstrated by Theorem 3.2, Theorem 3.3, and Corollary 3.4, which ensure statistical accuracy and confidence and explain the connection to regression tasks. The authors also claimed that these results are "nearly optimal."

### Weaknesses
1. While the paper introduces a practical and efficient method for estimating Banzhaf values, much of its foundation relies on adapting existing techniques developed for Shapley values and generic regression problems.  
2. Kernel Banzhaf demonstrates accuracy in Banzhaf value estimation, yet its broader implications for data valuation and generative AI tasks have not been explored. In particular, the authors consider that being inapplicable to generative AI is a limitation of MSR.
3. Robustness is primarily demonstrated through empirical evaluations, such as the $\ell_2$-norm error under varying noise levels (e.g., Figure 3). The paper does not explicitly incorporate noise-level assumptions and parameters into its theoretical guarantees (e.g., results in Section 3.3).

### Questions
1. As "Banzhaf values are often considered more intuitive for AI applications," is there a reason most existing studies focus on Shapley values?
2. How does Kernel Banzhaf perform under structured noise patterns, such as adversarial perturbations?

### Soundness
3

### Presentation
3

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
This work applies ideas proven effective for estimating Shapley values to Banzhaf values, introducing Kernel Banzhaf, a regression-based approximation algorithm for estimating Banzhaf values of general set functions. The authors demonstrate through extensive experiments that Kernel Banzhaf has significant advantages in sample efficiency and noise robustness. Additionally, they provide theoretical guarantees for the algorithm's performance.

### Strengths
1. Few algorithms have been proposed to compute Banzhaf values for arbitrary set functions. This paper addresses this gap by introducing an algorithm that overcomes this limitation, representing a significant improvement. It also experimentally evaluates the estimator in relation to the true Banzhaf values,rather than relying just on convergence metrics.

2. Theorem 3.2 states that the Banzhaf values are the solution to the linear regression problem defined by matrix A and vector b. Theorem 3.3 is a standard guarantee for leverage score sampling. Corollary 3.4 Kernel Banzhaf can recover a solution  that has near optimal objective value but is far from the optimal solution .

3. This work compared the Kernel Banzhaf with state-of-the-art estimators across eight popular datasets, and the results confirmed the superior performance of the Kernel Banzhaf.

### Weaknesses
1.While the theoretical underpinnings are well-developed, the paper may not provide a comprehensive assessment of the computational efficiency and practicality of the proposed method in real-world applications. Like the computational complexity analysis or empirical time/memory cost.

2.The study demonstrates the robustness of the Kernel Banzhaf algorithm primarily through relevant experiments. Figure 4 shows the horizontal line representing Kernel Banzhaf, which remains unchanged as noise levels increase.Previous studies, such as Data Banzhaf[1], have provided theoretical proof of robustness using the Safety Margin. This study may need to supplement related theoretical proofs.

### Questions
1.Broader baselines and empirical settings. For example, the settings for “Noisy” are kind of simple. What’s the variance of the added noise? The study claims to evaluate the Banzhaf values of general set functions and suggests expanding the dataset range to explore more scenarios, such as MNIST, FMNIST, and CIFAR-10.

Minor:
line106： What does  mean, and is it consistent with Data Banzhaf[1] ? Does it represent -approximation in -norm.

Ref. 
[1]Jiachen T. Wang and Ruoxi Jia. Data banzhaf: A robust data valuation framework for machine learning. In AISTAT,  2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors proposed an efficient method for approximating the Banzhaf value. The Banzhaf value, similar to the Shapley value, is a measure used in cooperative game theory. Unlike the Shapley value, however, the Banzhaf value assigns equal weights to all subsets. The authors showed that the Banzhaf value can be represented as the solution to a least squares problem, and they propose a sampling-based approach to approximate this least squares solution. Through experiments, the authors demonstrated that their method achieves higher accuracy than other existing methods for approximating the Banzhaf value.

### Strengths
A key strength of this research is the simplicity of the proposed estimator for the Banzhaf value. The method involves simply sampling subsets and solving a least squares problem, making the computation highly straightforward. Additionally, the theoretical complexity of the sampling process is studied. While an exact calculation requires all the $2^n$ subsets, the proposed approach reduces this to approximately $O(n \log n / \delta)$. This ease of implementation, along with the theoretical guarantees, gives the study valuable for applications involving the Banzhaf value.

The discussion in Appendix H regarding the (un)necessity of efficiency axiom is particularly interesting. I think the efficiency axiom is not necessary within the context of feature attribution. Therefore, this discussion supporting the usefulness of the Banzhaf value is especially important.

### Weaknesses
There are no obvious weaknesses I found in this paper. If I have to mention a potential drawback, it might be that the Banzhaf value is less well-known compared to the Shapley value. However, as the authors discuss in Appendix H, the Banzhaf value can serve as a viable alternative to the Shapley value, and it would be ideal to see it become more widely studied alongside the Shapley value in the future.

### Questions
It is generally possible to achieve variance reduction by combining multiple estimators. 
Would it be possible to create an estimator with lower variance by mixing the proposed method with MC and MSR estimators using appropriate weights?
If further variance reduction can be achieved, it would be highly useful for practical applications.

### Soundness
4

### Presentation
4

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
This paper proposes a new estimator for Banzhaf, which can be used to derive feature importance for general ML models. Theoretical analysis provides control over the error of the estimator.

### Strengths
* The proposed estimator seems to be more precise than current practice and hold theoretical guarantees.
* Experiments show that Kernel Banzhaf empirically has better sample complexity on eight tabular datasets.

### Weaknesses
 * While the authors show that their approach achieves good sample complexity, it is unclear how meaningful that improvement is in practice from the current manuscript. I would make two suggestions: (1) can you use the proposed method to analyze datasets of large sizes in which MC and MSR fail to produce meaningful results but Kernel Banzhaf succeeds? (2) For the datasets you analyze, can you show that Kernel Banzhaf recovers feature ranking (overall and among the top-k features), or a similar quantity the practitioners would typically be interested in?
* This work is similar to Musco & Witter, and while there are differences (Banzhaf instead of Shapley, and the theoretical analysis required different techniques), the level of novelty in this work is not very high. The core idea of using leverage score sampling for a regression formulation is not new, and the adaptation to Banzhaf values, while requiring some technical work, does not represent a major conceptual leap. The regression formulation of Shapley values has been known for a long time, and while the authors claim the analogous connection for Banzhaf values was only known for a special kind of set function, the practical implications of this distinction are not fully clear. The theoretical guarantees, while present, do not seem to offer a significant advantage over existing methods in practical scenarios, and the experimental results, while showing some improvement, do not demonstrate a substantial practical impact.

### Questions
* The MSR estimator should obtain sample complexity that is comparable to proposer method under the classification setting. How you explain the fact Kernel Benzhaf obtains better results in the experiments for the classification datasets? Is that true in general or not?
* Can't the theoretical results of Wang & Jia be extended to regression by normalizing the responses? 
* In the contribution you write: "We argue that, up to log factors and the dependence on ϵ, our analysis is the best possible". What you mean by best? Do you mean tight? Or do you mean it is the best possible estimator for Banzhaf values?

### Soundness
3

### Presentation
3

### Contribution
2
