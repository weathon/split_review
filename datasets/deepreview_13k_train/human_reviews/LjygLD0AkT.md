# Rethinking Test-time Likelihood: The Likelihood Path Principle and Its Application to OOD Detection

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
While likelihood is attractive in theory, its estimates by deep generative models (DGMs) are often broken in practice, and perform poorly for out of distribution (OOD) Detection.
    Various recent works started to consider alternative scores and achieved better performances.
    However, such recipes do not come with provable guarantees, nor is it clear that their choices extract sufficient information.
    
    We attempt to change this by conducting a case study on variational autoencoders (VAEs).
    First, we introduce the \textit{likelihood path (LPath) principle}, generalizing the likelihood principle. This narrows the search for informative summary statistics down to the \textit{minimal sufficient statistics} of VAEs' conditional likelihoods.
    Second, introducing new theoretic tools such as \textit{nearly essential support}, \textit{essential distance} and \textit{co-Lipschitzness}, 
    we obtain non-asymptotic provable OOD detection guarantees for certain distillation of the minimal sufficient statistics.} with poor likelihood estimates.
    To our best knowledge, this is the first provable unsupervised OOD method that delivers excellent empirical results, better than any other VAEs based techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper develops a generalization of Likelihood principle that comes with provable guarantees for OOD detection in deep generative models. Applying this new principle to VAEs, the authors propose using minimal sufficient statistics for OOD detection with non asymptotic guarantees. Empirical results show the suggested approach can outperform or perform on par with other OOD detection methods in an unsupervised setting.

### Strengths
- The paper analyzes different types of OOD samples and the reason behind the difficulty of some of OOD cases in a principled way. 
- It provides a theory and a simple computational approach for identifying OODs.

### Weaknesses
 - The intuition behind the theorem and the illustration in Figure 1 can be further improved. As the main figure of the paper which is introducing the idea, Figure 1 is not easy to follow. You need to read the paper all the way to the end of page 7 so you can understand the 4 cases and their connection to the idea presented in the paper. 
- As the authors have mentioned, Equation 10 is non-trivial to compute and an approximation is provided. The effect of the error of this approximation on the performance of the algorithm can be further studied in synthetic cases. Specifically, the approximation in Equation 13 and 14, while justified, needs further analysis regarding its impact on the final OOD detection performance. It's unclear how sensitive the method is to the approximation error, and under what conditions this error becomes significant. A synthetic case study would help to quantify this.
- Setting the decision criteria in the proposed algorithm is non-trivial and can be further studied in the paper. The paper does not clearly define the decision criteria for classifying OOD samples. While the AUROC is used as an evaluation metric, the actual thresholding or decision rule based on the computed score is not explicitly stated, making it difficult to understand how the method would be used in practice. This lack of clarity also makes it hard to assess the robustness of the method to different decision thresholds.
- The fact that the method outperforms other VAE baselines but doesn’t perform as well as more sophisticated baselines makes the practical usage of the method in safety critical domains less feasible. The performance gap between the proposed method and more advanced OOD detection techniques, especially on challenging datasets like SVHN vs CIFAR, raises concerns about its applicability in real-world safety-critical scenarios. While the theoretical guarantees are valuable, the empirical performance needs to be more competitive to justify its use in such domains.

### Questions
- Minor: Fix the references to Equations 19 and 18 in section 3.2. 
- Fix “∥x_OOD − x_OOD∥_2 is large” on page 7
- How does the approximation error of Equation 12 affect the performance?
- The motivation behind the paired VAE idea in section 4 is unclear. The idea has been introduced in few lines and the reasoning behind it is deferred to the appendix. Can you either expand the motivation in the main text or move these few lines to the appendix?
- What are the hyperparameters that are needed for the OOD decision rule? 
- Minor: I think the citations for DDPM and LMD are flipped

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission #8717  presents a new perspective on out-of-distribution detection with the introduction of the "Likelihood Path Principle". The principle is based on the observation that traditional likelihood measures can be ineffective for OOD detection due to their reliance on static data snapshots. The authors suggest a dynamic path-wise likelihood integration method to capture the evolving nature of data distributions. 

The paper asserts that this method more accurately differentiates between in-distribution (ID) and OOD samples by considering the trajectory of the likelihood as data moves from ID to OOD. To substantiate their claims, the authors provide experimental results that demonstrate an improvement over existing methods such as ODIN across several benchmarks. Additionally, they offer theoretical insights into why considering the path of likelihood can be beneficial for OOD detection.

### Strengths
- The paper introduces new theoretical tools (section 2, section3) that provide a solid foundation for their proposed LPath principle and OOD detection approach. Unlike some previous work, the proposed method comes with non-asymptotic provable guarantees for OOD detection.

- The paper claims state-of-the-art empirical results, suggesting a significant advancement over existing methods.

### Weaknesses
 - *Complexity of implementation*. While not explicitly mentioned, the introduction of new theoretical concepts might imply a more complex implementation and understanding, potentially limiting accessibility for practitioners. The author has not provided any valid implementations for reviewing.

- *Dependence on VAEs*. The method's effectiveness may be highly dependent on the performance and tuning of the underlying VAEs, which can be sensitive to hyperparameters and data quality. Specifically, the reliance on VAEs introduces a potential bottleneck, as the quality of the OOD detection is now indirectly tied to the VAE's ability to accurately model the in-distribution data. This dependence could lead to suboptimal performance if the VAE struggles with complex or high-dimensional data, or if the chosen VAE architecture is not well-suited for the specific dataset.

- *Presentation*. I feel that the presentation quality of the manuscript could still be improved, especially some illustrations/figures are difficult to read.

Additionally, please refer to the ‘Questions’ section for my other potential concerns.

### Questions
- What is the computational overhead introduced by the path-wise likelihood calculation, and how does it scale with the complexity of the model and the size of the dataset?

- Continuing above, in high-dimensional spaces, traditional likelihood methods often struggle due to the curse of dimensionality. How does the Likelihood Path Principle mitigate these issues, and is there a threshold where the method becomes computationally infeasible?

- How does the LPath algorithm perform under different types of data distributions and noise levels? How does the method handle cases where the OOD data is deliberately designed to mimic ID data, as in adversarial attacks?

- Can the principles introduced in the paper be extended to other types of generative models beyond VAEs? Also, is there potential for the Likelihood Path Principle to be integrated into a wider array of model architectures beyond those tested, including unsupervised and semi-supervised learning scenarios?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel approach to out-of-distribution (OOD) detection in Variational Autoencoders (VAEs) by leveraging minimal sufficient statistics within the encoder and decoder. This method differs from Morningstar et al. (2022) by focusing on the mean and variance of $q(z|x)$ instead of the posterior entropy and KL divergence for the latent variable $z$. Theoretical guarantee is derived by assuming there is essential separation between in distribution and OOD samples w.r.t. the $L_2$ norm, and the encoder/decoder in VAEs are Lipschitz. But in practice the assumptions are not always realistic. The experiment results are sometimes surpass SOTA and sometimes perform worse when the assumptions broke. 
1. **Proposed Methodology**:
  - The paper suggests the utilization of the minimal sufficient statistics in both the encoder and decoder of the VAE for OOD detection.
  - The work is reminiscent of Morningstar et al. (2022), but distinguishes itself by emphasizing the mean and variance of $q(z∣x)$ and derive theoretical guarantee of OOD under assumptions.
2. **Assumptions and Implications**:
  - Essential separation of in-distribution (ID) and OOD data based on L2 norm distance is assumed.
  - The encoder and decoder must satisfy Lipschitz type conditions.
  - Under these conditions, detection using reconstruction error or L2 norm distance in the latent space between a sample and ID samples is reliable with high probability.
    - Practical implementation does not calculate distance by sampling IID samples. Instead, it is approximated using $\mid || \mu_{{z}}\left({x}_{\mathrm{OOD}}\right) \|-r_0 \mid$.
3. **Experimental Outcomes**:
  - The method proves effective when the assumption on essential separation is likely met.
  - On datasets with minor separations, like horizontally and vertically flipped variants, the technique is less effective compared to some state-of-the-art (SOTA) methods.

### Strengths
- The proposed sufficient statistics used for OOD detection are different from Morningstar et al. (2022) by focusing on the mean and variance of $q(z|x)$ instead of the posterior entropy and KL divergence for the latent variable $z$.

### Weaknesses
 - The utilization of  $\mid || \mu_{z} (x_{{OOD}}) \|-r_0 \mid$ to approximate the distance between test and ID samples is questioned for its lack of a principled basis. If ID samples have a wide spread in $μ(x_{IID})$ in the latent space, the absence of a singular reference point makes the approximation meaningless. The reliance on VAEs' regularization of the posterior on $z$ towards a Gaussian (typically zero mean) implies the technique may not be generalizable to other generative models with distinct latent variable regularization.

- The assumptions for essential separation and Lipschitz conditions are too strong. The separation (defined by the $L_2$ norm)  may not hold for real world problems. The Lipschitz conditions are not enforced during training of VAEs (or in other generative models) as well.

- The idea of using reconstruction error for OOD detection was proposed in [1]. It is worth discussing the difference and what are the new interpretations. 

- The paper's presentation quality needs improvements.
    
  - Some concepts are articulated in an imprecise, non-rigorous manner. For example, the phrase “break in the right way” from Section 2 lacks clarity.
  - Several explanations are relegated to appendices, compromising the fluidity and comprehension of the main text. Definitions, like B.6 and B.7, are cited without main text elaboration.
  - The excessive use of bold text and protracted informal subtitles detract the reader.

### Questions
- When the assumptions will hold and measure it empirically if possible to validate?
- Explain the use of $\mid || \mu_{z} (x_{{OOD}}) \|-r_0 \mid$, when does this serve as a good approximate? Is this limited to methods like VAE that regularize posterior distribution of $z$?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the OOD detection problem, where likelihood and scores either performs poorly or lack of provable guarantees. Under the VAE setup, the authors introduce the likelihood path (LPath) principle, suggesting that minimal sufficient statistics of VAEs’ conditional likelihoods are enough for OOD detection. Under several assumptions, the authors prove OOD detection guarantees for the chosen minimal sufficient statistics. Empirical results are also provided, suggesting the applicability of the proposed LPath principle.

### Strengths
The authors give a provable unsupervised OOD detection method that achieves good empirical performance, showing their work's high originality and significance. They also introduce several new concepts to facilitate the theoretical analysis.

### Weaknesses
1. I have the concern of whether the assumptions (essential separation concepts) are too strong, so that they can easily imply the theoretical guarantee. Specifically, the notion of 'essential separation' seems to require a very structured difference between in-distribution and out-of-distribution data in the latent space, which might not hold in practice. For instance, if the latent representations of in-distribution and out-of-distribution data are not neatly clustered but instead form complex, intertwined manifolds, the assumption of a clear separation with a specified probability might be overly optimistic. Also, I am not sure whether these "separations" are reasonable in realistic dataset. 

2. The writing is unclear in the sense that some notation seems not to be defined, such as $p_{\theta}$, $\mu_z$. This makes me sometimes a little bit confusing. Furthermore, the connection between the likelihood path (LPath) principle and the chosen minimal sufficient statistics is not clearly established. It's not immediately obvious why these specific statistics are sufficient for OOD detection based on the LPath principle. The paper would benefit from a more detailed explanation of how these concepts are linked.

### Questions
I am wondering whether the Definitions can be interpreted in a more standard way using conventional languages such as total variation distance (or some other distances) between OOD and IID distributions is large?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
