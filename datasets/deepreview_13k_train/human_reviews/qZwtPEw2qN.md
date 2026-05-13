# How Much is a  Noisy Image Worth? Data Scaling Laws for Ambient Diffusion.

- Decision: Accept
- Scores: 6, 6, 8, 8, 6

## Abstract
The quality of generative models depends on the quality of the data they are trained on. Creating large-scale, high-quality datasets is often expensive and sometimes impossible, e.g.~in certain scientific applications where there is no access to clean data due to physical or instrumentation constraints. Ambient Diffusion and related frameworks train diffusion models with solely corrupted data (which are usually cheaper to acquire) but ambient models significantly underperform models trained on clean data. We study this phenomenon at scale by training more than $80$ models on data with different corruption levels across three datasets ranging from $30,000$ to $\approx 1.3$M samples. We show that it is impossible, at these sample sizes, to match the performance of models trained on clean data when only training on noisy data. Yet, a combination of a small set of clean data (e.g.~$10\%$ of the total dataset) and a large set of highly noisy data suffices to reach the performance of models trained solely on similar-size datasets of clean data, and in particular to achieve near state-of-the-art performance. We provide theoretical evidence for our findings by developing novel sample complexity bounds for learning from Gaussian Mixtures with heterogeneous variances. Our theoretical model suggests that, for large enough datasets, the effective marginal utility of a noisy sample is exponentially worse that of a clean sample. Providing a small set of clean samples can significantly reduce the sample size requirements for noisy data, as we also observe in our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the impact of noisy data on (ambient) diffusion models. The paper shows that noisy data can be leveraged to improve the performance of diffusion models. In addition they provide the data regime where the noisy data are useful.

### Strengths
- the paper is well written
- the tackled problem is very interesting
- experiments are exhaustive and convincing (Figure 1 shows the regime of interest for using noisy data)

### Weaknesses
 - I am not familiar with proof techniques for the mixture of Gaussian sample complexity, but I am not sure I understood the goal/take-away of Theorems 4.2-4.4. IMO much more discussion is needed here. Specifically, the connection between the theoretical results and the practical implications for diffusion models is not clear. The theorems seem to focus on sample complexity bounds for Gaussian mixture models, but it is not clear how these bounds translate to the performance of diffusion models trained with noisy data. The discussion should elaborate on how the theoretical results inform the design choices for using noisy data in diffusion models.
- Lack of motivation: the tackled problem is overall very interesting, but I am not sure that the authors provided a concrete application where such new noisy data are available, and known as such. It would be helpful to have a more compelling real-world scenario where the proposed approach would be particularly beneficial. The current examples are somewhat abstract and do not fully justify the need for the proposed method. A concrete application with specific data characteristics would strengthen the motivation.



### Questions
- ¨For example, a blurry image might get dismissed from the filtering pipeline¨ Can authors provide a real example of such a filtering, i.e., a real filter used and a real discarded image?
- "For realistic sample sizes" Do you have an order of magnitude of "realistic sample size" in your context?
- Figure 1: in addition to training on noisy data, are other data augmentation techniques used? if not, do you know how new noisy data would compare against already existing standard data augmentation?


- The heteroscedastic model: I do not understand how the proposed model in Definition 4.1 is a heteroscedastic mixture of Gaussian. As currently written in the paper, it feels that all the points of the distribution are convolved with the Gaussian noise (which is coherent with the proposed setting). Following Shah (2023), shouldn't a heteroscedastic mixture of Gaussian write $X_i \sim \\mathcal{N}(\mu_i, \sigma_i)$.
In other words, IMO maths matches the setting, but I am not sure of the ¨heteroscedastic mixture of Gaussian¨ terminology.

- Regarding the cost of the augmentation, are all models trained with the augmentation, do you confirm that all models are trained with the same budget? (i.e., with the same number of images seen, since the datasets are different) I guess yes since EDM code takes ¨million number of images¨ as input


Theorem 4.2:
- what are $c_1$ and $c_2$? Absolute constants as defined in Vershynin (2018)?
- "Discussion" I did not understand the discussion after Theorem 4.2, could you elaborate on the "error in estimating the low-dimensional sub-space" and the "low-dimensional estimation procedures"
- "Then, there is a procedure which when given n independent ...." could you give a word on the procedure?

- Algorithm 1: is the noise level of each sample require in Algorithm 1?

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
2

### Summary
This paper studies data scaling laws for ambient diffusion. The authors find that training on a small set of clean data and a large set of noisy data significantly outperforms training solely on either one of these sets. The paper provides both theoretical analysis and empirical results to verify their findings.

### Strengths
1. The studied problem is interesting and important.
2. The authors provide theoretical results to support their findings.

### Weaknesses
1. I'm a bit confused about the relationship between thm 4.2 and alg 1. The thm 4.2 states that there exists a procedure which can return a good estimate of D. Is Algorithm 1 the procedure referenced in this theorem?
2. Alg 1 need to know whether each data is clean or noisy. Is it possible to generalize the proposed algorithm to handle cases where clean and noisy data are mixed? Specifically, what if the algorithm is provided with a dataset where the clean/noisy labels are not available, and the proportion of clean to noisy data is unknown?
3. In the experiments, The paper only presents the empirical results of the proposed method and does not compare it with previous work. (Daras et al., 2024; 2023b).

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Quick summary: This paper studies the performance of the diffusion model in the ambient diffusion scenario. Previous work shows that the diffusion model trained by noisy data is inferior to the model trained on clean data, and the consistent diffusion model requires the noisy samples to be infinity from the asymptotic view. This paper proposes to use the mixture of clean data (high-frequency feature) and corrupted data (low-frequency feature) to assist the ambient diffusion model to obtain a very close performance to the state-of-the-art and provide the theoretic analysis to support the experiment and evaluate the corresponding value of noise image using the inspiring sampling bounds from the theoretical results.
Quality: The paper is well-written and well-motivated, and the proposed method is good with a theoretical foundation albeit a bit simple.
Originality: The theoretical analysis of the two sampling bounds is inspiring with practical meaning. 
Significance: This is an important research direction because noise data is common in the real world.
Pros: * Important problem * theoretical foundation * nice results and sufficient experiments
Cons: * The solution is a bit simple and kind of engineering consideration.   
Summary: This is a nice paper that gives a simple solution to the ambient diffusion models with theoretic analysis and while not groundbreaking, certainly merits a publication.

### Strengths
The theoretical analysis of the two sampling bounds is inspiring with practical meaning.

### Weaknesses
The solution is a bit simple and kind of engineering consideration.

### Questions
What's the exact number of samples or dimensions in your settings in line 93, page 2?

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
First, the paper empirically shows that training on entire noisy data will lead to bad performance, but as long as a few clean data (~10%) are available, models trained by the proposed algorithm are comparable to models trained on clean data. Second, the paper derives minimax optimal estimation bounds to explain the phenomenon. Third, the paper pinpoints the price of noisy images for different datasets and noise levels, which has practical implications.

### Strengths
1. The paper is written clearly.
2. In practice, we have small sets of clean data and large sets of noisy data, so the paper considers an important setting.
3. The experiments on different realistic image datasets are sufficient to support the claim in the paper.
4. The established estimation bounds are minimax optimal and discussed clearly. 
5. The price of noisy images is interesting.

### Weaknesses
1. The obtained $\hat{D}$ is the ERM result for the Wasserstein distance loss, which is mismatched with the loss of diffusion models. Specifically, while the Wasserstein distance provides a measure of distributional similarity, the diffusion model objective is based on denoising score matching, which doesn't directly minimize the Wasserstein distance. The paper needs to address this gap by either showing a tighter connection between the two losses or by modifying the theoretical framework to better align with the diffusion training objective. This mismatch raises concerns about the direct applicability of the theoretical results to diffusion models.
2. The proposed algorithm and proof technique are mainly based on existing works, which may decrease the novelty of this paper. The core idea of using a small clean dataset to guide the learning from noisy data is not entirely new. The paper should clearly articulate the novel aspects of the algorithm and the proof technique, highlighting the specific modifications and extensions that differentiate it from prior work. Without a clear explanation of the novelty, the contribution of the paper is limited.

### Questions
1. How can we know the value $\sigma_{t_n}$ in the inputs of Algorithm 1?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles a critical issue in training diffusion models with corrupted data when clean data is scarce or costly. The authors explore the effectiveness of a combination of a small clean dataset and a large noisy dataset, demonstrating that this approach can yield performance close to models trained solely on clean data. Theoretical analysis based on Gaussian Mixture Models (GMMs) with heterogeneous variances and experimental validation across multiple datasets support these claims. Additionally, the paper proposes a budget allocation mechanism for more efficient dataset curation by balancing the use of noisy and clean data.

### Strengths
* The paper is well-written and logically structured, making the content easy to follow.
* The theoretical analysis is rigorous and provides good intuition behind the proposed methods. The experiments are thorough, involving the training of more than 80 models across various datasets and noise levels.
* The paper’s conclusions offer significant practical value for dataset curation and budget allocation strategies in real-world applications, where collecting clean data can be expensive.

### Weaknesses
 * The analysis is limited to Gaussian noise corruption and discrete distributions with finite support. Expanding this framework to continuous distributions and non-Gaussian noise would increase its impact. Specifically, the current analysis does not address scenarios where the noise distribution is heavy-tailed or multimodal, which are common in real-world data corruption. Furthermore, the restriction to discrete distributions with finite support limits the applicability of the theoretical results to many practical cases involving continuous data.
* The proposed method assumes that the noise level is known in advance, which may not be the case in real-world scenarios. Incorporating techniques and analysis to handle unknown noise levels would make the approach more practical. The assumption of known noise variance is a significant limitation, as in many real-world scenarios, the noise characteristics are either unknown or vary across the dataset. This requires additional pre-processing steps to estimate the noise level, which introduces additional uncertainty and potential for error. 
* It remains unclear why an exponentially larger amount of corrupted data is necessary to compensate for the lack of clean data. The paper does not provide a clear explanation of the underlying information theoretic reasons for this exponential relationship. A more detailed analysis of how the information content of noisy samples degrades with increasing noise levels would be beneficial.

### Questions
It remains unclear why an exponentially larger amount of corrupted data is necessary to compensate for the lack of clean data. Can the authors provide more clarification for this point?

### Soundness
3

### Presentation
4

### Contribution
3
