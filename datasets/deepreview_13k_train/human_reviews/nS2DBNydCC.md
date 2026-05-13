# Vector Quantization By Distribution Matching

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
The success of autoregressive models largely depends on the effectiveness of vector quantization, a technique that compresses and discretizes continuous features by mapping them to the nearest code vectors within a learnable codebook. Two critical issues in existing vector quantization methods are training instability and codebook collapse. Training instability arises from the gradient gap during both forward and backward gradient propagation, especially in the presence of significant quantization errors, while codebook collapse occurs when only a small subset of code vectors are utilized during training.
A closer examination of these issues reveals that they are primarily driven by a mismatch between the distributions of the features and code vectors, leading to unrepresentative code vectors and significant data information loss during compression. To address this, we employ the Wasserstein distance to align these two distributions, achieving near 100\% codebook utilization and significantly reducing the quantization error. Both empirical and theoretical analyses validate the effectiveness of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the training instability and codebook collapse in vector quantization, the authors align the distribution of features and code vectors by including an additional quadratic Wasserstein distance term which regularizes their disparity under a Gaussian assumption. This method leads to 100% codebook utilization and better image reconstruction/generation quality.

### Strengths
1. The Wasserstein VQ algorithm is efficient and has a mathematical foundation
1. Empirical experiments indicate improvement in reconstruction quality

### Weaknesses
### weaknesses:
 1. The presentation is not clear enough. See the questions below, some of which are crucial.
1. The improvement in reconstruction quality is marginal. The authors also didn't explain how they picked the additional hyperparameter $\alpha_3$, which can raise suspicion of $p$-hacking. The authors should provide a detailed explanation of the selection process for this parameter, including the criteria used for choosing its value. It is important to clarify whether this value was determined through a principled approach or if it was the result of empirical tuning. If the latter, the authors should detail the range of values explored and the performance at each value to mitigate concerns of overfitting to the specific dataset.
1. Insufficient ablation experiments. The authors should study how the choice of distance measure (Wasserstein vs KL divergence), $\alpha_3$, and other knobs affect the performance of the proposed method. Specifically, an ablation study on the distance measure should compare the performance of the model using the quadratic Wasserstein distance versus the KL divergence, as mentioned on Wikipedia. This comparison is crucial to justify the choice of the quadratic Wasserstein distance. Additionally, a sensitivity analysis on $\alpha_3$ should be conducted to understand its impact on model performance across a range of values. This would help in understanding the robustness of the model to changes in this hyperparameter.
1. Editorial:
    1. On line 93, it's inaccurate to say "codeword IDs $r \in \mathbb{R}^{h \times w}$", because the components in $r$ are discrete.
    1. When presenting the experiment in Figure 3, the authors should point the reader to Appendix E.1, which includes details of the experimental setting.
    1. On line 280, consider calling the optimal set of code vectors $\{e_K^*\}_{k=1}^K$ to avoid confusion.
    1. There is an extra "Then" in Lemma 3 on line 310.
    1. In Section 4.1 on line 370, it's clearer to use the existing notations $z_i$ and $e_i$, instead of defining new ones $z_e$ and $z_q$.
    1. In Section 4.2 on line 418, the footnote $ ^3$ looks like a cubic power notation.
    1. In Section 6 on line 534, there is a typo in "alignment".

### Questions
1. The authors mentioned training instability on line 107, but it's unclear to me how Wasserstein VQ can help stabilize the learning. Is the argument that a smaller VQ reconstruction error makes $z_i$ and $e_i$ closer in expectation, and thus corresponds to better learning stability?
1. For "Criterion 2 (Codebook Utilization Rate)" defined on line 156, how does it depend on $N$?
1. For "Criterion 3 (Codebook Perplexity)" defined on line 180, do we want a high codebook perplexity? I am a little confused because in language modeling we want the "perplexity" to be low.
1. The interpretation of Figure 3 in lines 203 through 213 is not deep enough. In particular, why do $\mathcal{E}$, $\mathcal{U}$, and $\mathcal{C}$ exhibit different behavior when the feature covers the codebook vs vice versa?
1. In Section 2.4, the theorems all require bounded support, but Section 3.1 has the Gaussian assumption, while Gaussian does not have a bounded support. It's fine to use the theorems as an intuitive argument, but the authors should at least explain why their theoretical results "somehow" apply to Gaussian when the assumption is violated.
1. What's the motivation for the Gaussian assumption in Section 3.1? What's the real distribution of the features and code vectors in the experiments?
1. On line 307, it is claimed that KL divergence between Gaussian distributions has no analytical formula, but there is one on [Wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Multivariate_normal_distributions). It would be great if the authors can check if that is correct and explain why the quadratic Wasserstein distance is a better measure than the KL divergence.
1. In Section 3.2 and Figure 5, it is unclear what "training steps" mean. By inspection, we can see Equation (3) has an optimal solution at $\hat{\mu}_2^* = \hat{\mu}_1$ and $\hat{\Sigma}_2^* = \hat{\Sigma}_1$. We can then transform the code vectors such that $\hat{\mu}_2 = \hat{\mu}_2^*$ and $\hat{\Sigma}_2 = \hat{\Sigma}_2^*$ with a linear transformation. I don't think there is anything to be trained.
1. In Section 3.2 on line 346, what's the motivation for sampling the code vectors such that $\hat{\mu}_2 \ne \hat{\mu}_1$, which is clearly suboptimal? Moreover, how does Wasserstein VQ compare against other methods when $\hat{\mu}_2 = \hat{\mu}_1$ at initialization?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper tackles key issues in vector quantization (VQ) within autoregressive models, specifically addressing training instability and codebook collapse. The authors identify these issues as a mismatch between the distributions of features and code vectors, leading to significant information loss during compression. They propose aligning the codebook distribution with the feature distribution using quadratic Wasserstein distance to improve three criteria they introduce—Quantization Error, Codebook Utilization Rate, and Codebook Perplexity. The paper validates the effectiveness of these metrics through empirical analysis and further substitutes vanilla VQ with a multi-scale VQ structure. Experimental results demonstrate near 100% codebook utilization, reduced quantization error, and performance improvements.

### Strengths
1. The paper thoroughly analyzes the issues with VQ, particularly the training instability due to gradient discontinuities (addressed via the Straight-Through Estimator, though still prone to instability), and the low codebook utilization due to limited active code vectors.
2. The introduction of three specific criteria—Quantization Error, Codebook Utilization Rate, and Codebook Perplexity—adds quantifiable methods for assessing VQ performance and measuring improvements objectively.
3. The alignment of the feature distribution with the codebook distribution via quadratic Wasserstein distance is well-motivated theoretically and effectively addresses the identified issues.
4. The paper validates its proposed approach through experiments, showing substantial improvements in codebook utilization (nearly 100%) and other metrics, supporting the contributions' significance.
5. The multi-scale VQ approach, combined with Wasserstein distance loss, shows promise for practical applications, especially in visual generative tasks.

### Weaknesses
1. While Gaussian sampling effectively validates the proposed metrics, testing on a broader range of data distributions would enhance the generalizability of the findings, particularly for distributions commonly encountered in autoregressive models or visual tasks. Notably, VQ-VAE does not assume a Gaussian distribution in its latent space, making evaluating performance across diverse data types essential to reflect real-world applications better. The reliance on a Gaussian assumption, while simplifying analysis, may not accurately reflect the complex, non-Gaussian distributions often observed in the latent spaces of autoregressive models or in the feature spaces of visual data. This limitation raises concerns about the practical applicability of the proposed metrics and the Wasserstein alignment method in more realistic scenarios.
2. Although the metrics (Quantization Error, Codebook Utilization Rate, and Codebook Perplexity) are proposed and demonstrated through Gaussian sampling, the paper lacks validation on diverse and realistic data, especially those commonly used in autoregressive and generative tasks. The reliance on Gaussian sampling limits the generalizability and applicability of the metrics, making it uncertain how they would perform in varied contexts. The metrics, while well-defined, need to be tested on more complex datasets, such as those used in image or audio generation, to ensure they remain meaningful and effective beyond the simplified Gaussian setting. Without such validation, the practical utility of these metrics remains questionable.
3. The paper's focus on aligning feature and codebook distributions with Wasserstein distance for improved quantization seems limited in scope and impact. The primary advantage is codebook utilization. However, the broader implications or potential applications in complex or large-scale generative tasks (e.g., real-world autoregressive models) are not clearly demonstrated. While achieving high codebook utilization is a positive step, the paper does not sufficiently explore how this translates to improved performance in downstream tasks or more complex generative models. The practical benefits of this alignment, beyond the immediate metric improvements, are not well-established.
4. While the paper achieves nearly 100% codebook utilization, the practical significance of this improvement remains unclear. It's difficult to determine if the proposed method advances the field without a comprehensive comparison to other quantization methods that might achieve similar outcomes or more straightforward approaches to training stabilization. The paper needs to demonstrate that the near-perfect codebook utilization leads to tangible benefits, such as improved reconstruction quality or faster convergence, compared to existing methods. Without such comparisons, the practical value of this achievement is difficult to assess.
5. While multi-scale VQ improves vanilla VQ, the paper lacks detailed theoretical grounding or motivation for why a multi-scale approach is advantageous, specifically in Wasserstein distance. The paper should provide a more in-depth explanation of why a multi-scale approach is beneficial in the context of Wasserstein distance alignment, including any theoretical justifications or empirical evidence supporting this choice. The current motivation is insufficient to justify the added complexity of the multi-scale structure.

### Questions
1. Could you clarify the theoretical motivation behind using multi-scale VQ over vanilla VQ and its role in improving Wasserstein alignment?
2. Have you tested your metrics on real-world datasets beyond Gaussian sampling to validate their general applicability?
3. Can you clarify the practical implications of 100% codebook utilization, especially when compared to alternative methods in vector quantization?

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
Existing vector quantization methods in autoregressive models suffer from training instability and codebook collapse due to a mismatch between feature and code vector distributions, causing significant data loss. To address the problem, the authors propose to use the Wasserstein distance to align these distributions, achieving high codebook utilization and reduced quantization error.

### Strengths
The Gaussian modeling-based distribution matching is proposed to enhance the codebook utilization rate, then improving the VQ performance.

### Weaknesses
As discussed in the paper, several methods have been introduced to enhance the codebook utilization rate. The paper's contribution appears to be more incremental than highly innovative. Additionally, the proposed distribution matching method simply assumes that all feature vectors adhere to a Gaussian distribution. This assumption may not be perfect for feature vectors of various patterns.

There are simpler methods for matching  distributions, like the k-means, which does not require prior assumptions about the data distribution. This raises the question of whether  the Gaussian modeling-based distribution matching is  necessary, especially given its higher complexity.

Is Criterion 2 (Codebook utilization rate) necessary for optimization?  This criterion seems to be well satisfied if Criterion 3 (Codebook perplexity ) is satisfied.

The paper devotes considerable effort (in sections 2.3 and 2.4) to demonstrating the advantage of distribution matching (between feature vectors and code vectors) in enhancing quantization accuracy. This relationship is straightforward and readily understandable. However, the authors are encouraged to provide a more detailed examination of the convergence properties of the proposed three criteria.

Does the multi-scale VQ cost (namely Eq. (5)) really work?  By 4.2, it is easy to derive that $z_q=z_1+(\hat{z}_T-z_T)$, implying that the features we adopt for codebook optimization essentially share the same resolution  with  $ z_T$, rather than multi-scale. For the operation on $z_i$, ($1<i<T$), the method implicitly assume that the feature vectors nearby in space are similar to each other, and then share the same quantization values (code vectors). However, this assumption is not appropriate for the low-resolution features with high variance.

In Figures 2 and 6, the sub-figures about  ${e_k}$  and ${\gamma}$ should be put in the rectangle of “vector quantizer”.

### Questions
1) There are simpler methods for matching  distributions, like the k-means, which does not require prior assumptions about the data distribution. This raises the question of whether  the Gaussian modeling-based distribution matching is  necessary, especially given its higher complexity.


2) Is Criterion 2 (Codebook utilization rate) necessary for optimization?  This criterion seems to be well satisfied if Criterion 3 (Codebook perplexity ) is satisfied.

3) The paper devotes considerable effort (in sections 2.3 and 2.4) to demonstrating the advantage of distribution matching (between feature vectors and code vectors) in enhancing quantization accuracy. This relationship is straightforward and readily understandable. However, the authors are encouraged to provide a more detailed examination of the convergence properties of the proposed three criteria.


4)  Does the multi-scale VQ cost (namely Eq. (5)) really work?  By 4.2, it is easy to derive that $z_q=z_1+(\hat{z}_T-z_T)$, implying that the features we adopt for codebook optimization essentially share the same resolution  with  $ z_T$, rather than multi-scale. For the operation on $z_i$, ($1<i<T$), the method implicitly assume that the feature vectors nearby in space are similar to each other, and then share the same quantization values (code vectors). However, this assumption is not appropriate for the low-resolution features with high variance.


5) In Figures 2 and 6, the sub-figures about  ${e_k}$  and ${\gamma}$ should be put in the rectangle of “vector quantizer”.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In the paper, the authors highlighted that a low utilization rate of the codebook will impair the training stability  of Vector Quantization (VQ), and subsequently proposed to enhance this utilization rate by aligning the distributions of feature vectors with those of the codebook.

### Strengths
1) To enhance the utilization rate of codebook, this paper proposed to align the distributions of feature vectors with those of the codebook.

2) Gaussian distributions are adopted  to model the feature and code vectors.

 3) Wasserstein  distance is used d to measure the distance between distributions.

### Weaknesses
1) Using Gaussian distributions to model the feature and code vectors is not reasonable, as these vectors typically belong to diverse classes with more intricate distributions. From a statistical perspective, modeling the data with Gaussian mixtures is more appropriate. Consequently, it is reasonable to raise doubts regarding the effectiveness of the proposed distribution matching method.

2) Improving the utilization rate of  code vectors in a  codebook (or called dictionary) is not a novel problem, which has been early studied in dictionary learning.

3) The authors claim that their major contribution is providing an optimal VQ strategy for the machine learning community. However, numerous studies have delved into this issue, particularly in the context of signal processing and information theory. These studies have investigated the optimal VQ issue from the traditional rate-distortion perspective, offering a more comprehensive and in-depth analysis compared to the theorems presented in the paper. This suggests that the innovation in this paper is quite limited.

### Questions
1) Is the low utilization rate of code vectors a result of the gradient backpropagation problem (as argued by the authors in line 049), or is it due to the insufficient diversity of training samples relative to the large size of the codebook? I lean towards the latter explanation, and therefore consider the low utilization rate is *not* a pivotal issue that significantly impacts the final performance of vector quantization.

2) In Lines 062-068, the authors should  delve into the reasons behind the low code vector utilization rate observed in existing methods. For instance, in my view, the codebook initialization with k-means (Zhu et al. 2024) should work well in distribution matching, but performed worse in the paper. Could this be attributed to the issue of codebook utilization rate, or other factors, such as differences in network structures?

3) A codebook with a high utilization rate should closely match the distribution of feature vectors. Therefore, is it necessary to incorporate an additional distribution matching approach based on the Wasserstein distance?

4) As previously mentioned, modeling the entire set of feature vectors using a single Gaussian distribution is not reasonable. Instead, Gaussian mixtures are recommended as a more suitable alternative.

### Soundness
2

### Presentation
2

### Contribution
2
