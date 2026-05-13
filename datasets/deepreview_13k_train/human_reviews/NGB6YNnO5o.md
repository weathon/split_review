# Generalization in VAE and Diffusion Models: A Unified Information-Theoretic Analysis

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
Despite the empirical success of Diffusion Models (DMs) and Variational Autoencoders (VAEs), their generalization performance remains theoretically underexplored, particularly lacking a full consideration of the shared encoder-generator structure. Leveraging recent information-theoretic tools, we propose a unified theoretical framework that guarantees the generalization of both the encoder and generator by treating them as randomized mappings. This framework further enables (1) a refined analysis for VAEs, accounting for the generator's generalization, which was previously overlooked; (2) illustrating an explicit trade-off in generalization terms for DMs that depends on the diffusion time $T$; and (3) providing estimable bounds for DMs based solely on the training data, allowing the selection of the optimal $T$ and the integration of such bounds into the optimization process to improve model performance. Empirical results on both synthetic and real datasets illustrate the validity of the proposed theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a information-theoretic framework of generalization theory for variational auto-encoders and diffusion models. Authors consider generalization properities for both the encoder and the generator in VAEs. Their generalization bounds can be estimated using only training data, providing a practical guidance for hyperparameter selection.

### Strengths
- The authors address the critical topic of generalization in generative models, and provide estimable bounds for both the encoder and the generator in VAEs. 
- Bounds for VAEs avoid Wasserstein distance and impose milder assumptions (bounded to sub-Gaussian). 
- Bounds for DMs overcome the challenges associated with KL-divergence's non-satisfaction of the triangle inequality, and contribute to a clearer understanding of diffusion time’s role in generalization and model performance.

### Weaknesses
- In line 98, the paper asserts that the bounds for the encoder are tighter, yet this claim lacks sufficient detail. Although some comparisons to previous bounds are made in line 324, there remains a need for a more explicit, quantitative analysis to illustrate the improvements over existing bounds. Specifically, the paper should provide a comparative analysis against the PAC-Bayes bound, as described in "User-friendly introduction to PAC-Bayes bounds" [1], and the mutual information bound from "Statistical guarantees for variational autoencoders using pac-bayesian theory" [2]. Adding a direct comparison or detailed quantitative analysis, potentially through visual aids like those used for evaluating lossy compression rates of deep generative models as in "Evaluating lossy compression rates of deep generative models" [7], would make the claim more substantiated and provide clearer evidence of the improvement.
- The proposed generalization bounds do not clearly indicate a dependency on the number of samples, $m$, limiting their practical applicability. While the bounds are presented in an algorithm-dependent and data-dependent manner, the sample complexity is crucial for understanding their effectiveness. To make the bounds more actionable, it would be helpful if the authors explicitly stated the sample complexity (e.g., $O(1/ m)$ or $O(1/\sqrt{m})$) within the main theorems or discussed the bounds’ scaling with respect to $m$. Furthermore, the authors should clarify how the sample-wise mutual information term scales with $m$, given that it often exhibits sublinear behavior. This addition could guide readers in understanding the bounds’ robustness and sample efficiency, similar to the analysis provided in "On the quantitative analysis of decoder-based generative models" [5].
- The paper suggests a theoretical trade-off for diffusion models based on diffusion time, but this trade-off is not consistently reflected in the experimental results, as KL and BPD metrics do not show this effect, especially in high-dimensional, few-shot settings. The authors could address this discrepancy by either providing a potential explanation for the divergence between the theoretical and experimental findings or suggesting additional experiments that might better capture the trade-off. For instance, conducting experiments with varying dataset sizes and dimensionalities could illuminate the conditions under which the trade-off becomes apparent. Revisiting this section would enhance clarity and ensure its alignment with the paper’s core contributions. Additionally, the authors should consider discussing the challenges associated with estimating KL divergence and log density in high-dimensional spaces, as highlighted in "A note on the evaluation of generative models" [6].

### Questions
- The generalization bounds resemble Theorem 4.1, which primarily links encoder mappings' complexity to the gap between empirical generalization and expected generalization. But this should also affects empirical generalization. Can you provide a theorem telling how this two terms together affects expected generalization? 
- As far as I know, in practical works of generative models, the target distribution is always unknown, which means the empirical generalization error is always unknown. Could the authors elaborate on the practical benefits of bounding the gap between expected and empirical generalization error, particularly when the empirical error itself may not be measurable? 
- As mentioned in line 350, generalization bounds are computable, can you explain how to compute term $\hat{L}_{ESM}$ among upper bounds in Theorem 6.2?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper derives generalization bounds for encoder-generator-based generative models, considering both the encoder and generator components. The analysis is specifically applied to Variational Autoencoders (VAEs) and Diffusion Models (DMs), with tailored generalization bounds presented for each. Notably, a novel trade-off relationship is introduced for DMs. The theoretical results are supported by numerical experiments, demonstrating that the derived bounds offer practical utility, particularly in capturing the trade-offs in generalization.

### Strengths
- This paper derives a generalization bound for encoder-generator architectures under the relatively mild assumption of sub-Gaussian loss functions. As noted in lines 286-291, the paper provides an intuitive explanation of these bounds and a convincing discussion of the trade-offs involved.
- Corollaries 4.2 and 4.3 extend the analysis to evaluate the Wasserstein distance and KL divergence between the generative model's distribution and the data distribution, offering valuable tools for the theoretical analysis of a wide range of generative models.
- For VAEs, the paper presents a bound that applies to arbitrary generators, distinguishing it from existing research.
- In the case of DMs, a new trade-off relationship is derived. Under certain reasonable assumptions, the generalization bound involving mutual information of $G^{θ}$ is established concerning sample size, score function bounds, and time $T$. This leads to a tighter $ m^{-1/2}$ bound.
- The results are further substantiated by numerical experiments that validate the theoretical trade-offs observed in the upper bound.

### Weaknesses
While the results are significant in terms of learning theory by considering the effects of both the encoder and generator, some areas could be further improved:
- Although challenging, the analysis does not incorporate the complexity of the learning models. Including bounds related to the complexity of simple neural networks or linear models could strengthen the work. Specifically, the current bounds do not explicitly account for the number of parameters or the depth of the networks used in the encoder and generator, which are crucial factors in determining the generalization ability of deep learning models. Analyzing how the bounds scale with network size would provide a more complete picture.
- Aside from the theoretical analysis provided by the generalization bound, it would be beneficial to relate these results to those from sharp theoretical analyses in proportional limit settings. For example, in denoising encoders [1], autoencoders [2], or variational autoencoders [3, 4], the generalization error has been sharply evaluated by fixing the ratio $\alpha = n/d = \Theta(1)$, where $n \to \infty$ is the number of data points and $d \to \infty$ is the data dimension. Including such discussions in the related work section would provide a more comprehensive view of the literature. The current analysis would benefit from a discussion of how its bounds compare to these asymptotic results, particularly in terms of their tightness and applicability in different regimes.
- It would be interesting to see the results of training on the complete datasets of MNIST and CIFAR-10 rather than in a few-shot setting. The few-shot setting, while useful for demonstrating the trade-offs, may not fully reflect the behavior of these models in more typical training scenarios with larger datasets. Evaluating the bounds on full datasets would provide a more robust assessment of their practical relevance.
- The paper refers to the claime by Thesis et al. (2015) that "accurately estimating the KL divergence and Bits-Per-Dimension (BPD) for high-dimensional data distributions with limited data is challenging". However, this could be addressed using population MCMC or other Markov chain Monte Carlo methods. Investigating whether the trade-offs as in the upper bound remain evident in such scenarios would be intriguing. The current analysis relies on potentially inaccurate estimates of KL divergence and BPD, especially in the few-shot setting, and exploring more robust estimation techniques would strengthen the empirical validation.

### Questions
- The paper recommends adding terms for the generalization of $G$ to provide insights and practical guidance for VAEs. However, estimating these terms is generally considered difficult. Are there any methodologies that could facilitate this estimation?
- The few-shot setting with $m=16$ is mentioned in the experiments on real data. Could you provide more details on this experimental setup? Does it involve generating new data with a pre-trained model in a few-shot learning manner, or is it simply trained with limited data?
- What is the definition of $g$ in line 209?
- How would the generalization bounds change if the data were assumed to lie on a low dimensional manifold? What predictions can be made regarding such cases?

### Soundness
3

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
4

### Summary
In this paper, the authors explore the theoretical generalization behaviour for both variational autoencoders (VAEs) and diffusion models (DMs), noting that a DM can be seen as an infinite-layered hierarchical VAE. For both models, the behaviour of both the encoder and decoder in the VAE, and forward and reverse diffusion steps in the DM are analyzed. The authors then provide a theoretical upper bound for DMs with respect to the number of diffusion steps and then empirically verify it on several datasets, both synthetic and real (MNIST and CIFAR10), demonstrating its validity and usefulness in training optimal DMs.

### Strengths
This paper provides a very detailed and comprehensive information-theoretic analysis of generalization in VAEs and DMs along with experiments that empirically validate it. In particular, the incorporation of encoder-decoder / forward-reverse process into the analysis provides a novel view into their impact on the generative models' generalization behaviour, such as the finding that longer diffusion steps do not necessarily result in better estimates in DMs.

### Weaknesses
The paper's writing made it difficult to process the main contributions to the paper for two main reasons:

(1) Despite the abstract suggesting that the VAE's generalization behaviour is studied, much of the paper's focus is on analyzing DM behaviour.

(2) There is notably no experiments that validate VAE behaviour, which suggests that the VAE is studied here as a precursor to understanding the generalization behaviour of DMs.

### Questions
I suggest the authors make the writing more clear by including a separate background section on the relationship between VAEs and diffusion models; this will make it clear that the main contribution is providing a theoretical upper-bound for diffusion models as aided by the analysis of VAE generalization. A good place to start is the Variational Diffusion Models paper [1] that explicitly makes this connection by formulating the diffusion learning algorithm in terms of a variational lower bound.

References
[1] Diederik P. Kingma, Tim Salimans, Ben Poole, & Jonathan Ho. (2023). Variational Diffusion Models.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work puts a bound on the generalization gap for generative models relying on an encoder-decoder architecture. 
Using this, they introduce bounds on 
 - the wasserstein distance between the data distribution and generated distribution for variational autoencoders (VAEs),
 - the KL-divergence between the data distribution and generated distribution for diffusion models. 

They run experiments on a score based diffusion model using data from "Swiss Roll", MNIST and CIFAR-10.

### Strengths
S1: VAEs and diffusion models are widely used, so theoretical work on them is very relevant. 

S2: The bounds introduced in the work are new. 

S3: The story of the article is easy to follow.

### Weaknesses
The weaknesses relate to the experimental part of the paper.

W1: For both experiments you are using a fixed number of steps for generation while changing T.
	This means that for varying T, you are also varying the step-size, which can have a large effect
	on generation (See e.g. Zhang and Chen 2023 "Fast Sampling of Diffusion Models with Exponential Integrator").
	It is not clear to me whether this also affects your experiment in other ways (you should check this),
	but if you want to say something about sample quality, my suggested solution is to choose a step size, e.g. 1/1000,
	and also generate images with varying T, but fixed step-size.

W2: Figure 3 b) and c) do not support your claim. You say that the discrepancy comes from using too few samples
	to get a reliable estimation of KL divergence. My suggested solution is to do the experiment with enough samples
	to get a reliable estimation. Since your result is about KL-Divergence and not sample quality, it is not enough to
	look at sample quality for verification. Especially since since performance in one is not directly linked to
	performance in the other. This observation is also made in Theis et al. 2015 "A note on the evaluation of generative models"
	which you also cite yourselves.

### Questions
Q1: Do you have a theoretical reason (or at least an intuition) for why the mutual information should follow 
the upper bound in theorem 6.3?

Q2: At the end of section 6.1, you write "$T_3$, which characterizes the generalization of generator $G_T$ , will
remain non-zero for a small sample size". How small does the sample size need to be? And if you use enough samples in your 
MNIST and CIFAR-10 experiments to get a good estimation of KL-Divergence, will that make the contribution of $T_3$
very small? 

Q3: Could you add the next steps in your proof in appendix 1.C? As it is now, I don't see the final claim of the theorem 
in the last lines of the proof.

### Soundness
2

### Presentation
3

### Contribution
3
