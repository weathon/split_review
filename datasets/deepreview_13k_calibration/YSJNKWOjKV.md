# Inverse Flow and Consistency Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
Inverse generation problems, such as denoising without ground truth observations, is a critical challenge in many scientific inquiries and real-world applications. While recent advances in generative models like diffusion models, conditional flow matching, and consistency models achieved impressive results by casting generation as denoising problems, they cannot be directly used for inverse generation without access to clean data. Here we introduce Inverse Flow (IF), a novel framework that enables using these generative models for inverse generation problems including denoising without ground truth. Inverse Flow can be flexibly applied to nearly any continuous noise distribution and allows complex dependencies. We propose two algorithms for learning Inverse Flows, Inverse Flow Matching (IFM) and Inverse Consistency Model (ICM). Notably, to derive the computationally efficient, simulation-free inverse consistency model objective, we generalized consistency training to any forward diffusion processes or conditional flows, which have applications beyond denoising. We demonstrate the effectiveness of IF on synthetic and real datasets, outperforming prior approaches while enabling noise distributions that previous methods cannot support. Finally, we showcase applications of our techniques to fluorescence microscopy and single-cell genomics data, highlighting IF's utility in scientific problems. This work opens up the use of powerful generative models for denoising.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers the problem of denoising noisy observations $x_1$ without access to ground truth observations $x_0$. This work proposes two methods to solve this problem: 
1. Inverse Flow Matching (IFM) training: The inverse flow matching loss is similar to the regular flow matching loss with two key differences: As $x_0$ is not accessible, ODE is simulated from $x_1$ to $x_0$ to approximate $x_0$. The conditional vector field used is the standard conditional optimal transport flow. 
2. Inverse Consistency Model (ICM) training: This is the inverse counterpart of the standard consistency distillation. The model is trained to predict $x_0$ given $x_t$ where $t \in [0, 1]$.  This predicted $x_0$ is used to predict $x_{t+1}$ and $x_{t}$ (by applying one step of Euler ODE solver). The loss between 
Both the proposed methods have been tested on a combination of standard image datasets such as BSDS500, Kodak, Set12, scientific datasets like microscopy dataset and genomics data, as well as synthetic datasets such as Navier-Stokes, gaussian datasets.

### Strengths
- Inverse consistency model (ICM) training is simulation-free. It also gives good qualitative results in gray scale as shown in the appendix, and quantitative results as shown in Table 1 compared to prior baselines.
- The proposed method works better compared to prior methods on complex noise such as correlated noise and on data transformed with Jacobi process. 
- The proposed methods are easy to understand as these are simple modifications of existing methods.

### Weaknesses
 - Inverse Flow Matching training requires simulating the ODE which can be slow. 
- The proposed methods are simple modifications of existing methods such as consistency distillation/training and flow matching and there seems to be limited novelty.
    - Generalized Consistency Training: The core idea is same as consistency distillation. This work rewrites consistency distillation loss with a general ODE instead of Probability Flow ODE (PF-ODE).  Instead of assuming a pretrained diffusion model, GCT assumes that the vector field is user-specified (which is equivalent to having a pretrained teacher model).

- More experiments are needed, especially to measure robustness of the proposed method.
    - Different levels of noise (for eg. in case of Gaussian noise, consider different values of variance - both low and high)
    - Different combinations of noise - What happens if we have multiple types of noise being applied simultaneously in the observed image? Prior works also consider more types of noise: Noise2Score (Xie et al. 2023) presents results on both additive gaussian noise and multiplicative noise such as gamma noise, poisson noise and rayleigh noise. Please refer to Table 1 in this paper for a more extensive list of all different types of noise the authors consider (around 16 types).
- More experiments on colored datasets. Prior works consider results on extensively colored datasets such as ImageNet 256X256 (used by Noise2Same), CBSD68 dataset (Noise2Score). However, this work only shows qualitative results on fluorescence microscopy images which doesn’t have lot of color. Kodak and BSDS500 are all colored but qualitative results shown are in gray scale (Figure 5,6,7).
- More experimental details are needed. For instance, the paper should mention the architecture used to train these models on each of the datasets. Various hyperparameter values for training on real-world datasets should be included,

### Questions
1. Kodak and BSDS500 datasets are colored - why weren't colored images included in qualitative results? Were the models trained on grayscale images?
2. I think Noise2Score (Kim & Ye, 2021) should be included as a baseline. It seems to outperform other baselines considered in this work; though it is unclear if it will perform well with the types of noise considered in this work.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper is on the topic of learning generative models from corrupted data. The degradation operator is known but not invertible. To tackle this problem, the authors propose a new framework, called Inverse Flow Matching (IFM), and its computationally tractable version Inverse Consistency Models (ICM). In their training objective, the authors replace the (non-available) clean data with the ODE solution (simulated by a neural network) that arises when the deterministic sampling is initialized with the available corrupted samples. The authors test their method in synthetic, semi-synthetic and real datasets and show that the proposed framework outperforms Noise2X-type baselines.

### Strengths
1) The problem of learning generative models from corrupted data is very interesting and it has broad scientific applications.
2) The proposed framework is very general: it can handle arbitrary corruption as long as the distribution is identifiable from the measurements and the corruption model is known.
3) The proposed algorithm borrows ideas from the consistency models literature and extends them in a novel way to learn without access to uncorrupted samples. 
4) The proposed method clearly outperforms the considered baselines.

### Weaknesses
While I strongly believe that this paper has some very interesting aspects, I think there are also several important weaknesses.

1) I believe the presentation of the paper should be improved. In the background Section 2.1.1. there are several undefined symbols. For example, $u_t(x)$ is defined in (1) as the vector field of the ODE. However, in (2) a conditional form of this vector field is used, without defining what this conditional form means and how it relates with the vector field in (1). Specifically, the notation $u_t(x | x_0, x_1)$ is introduced without explanation, making it unclear how this conditional vector field is derived or what its precise role is within the proposed framework. This lack of clarity extends to the subsequent equations, hindering a clear understanding of the core methodology. There are also several typos throughout the paper, for example, there is a parenthesis missing in line 103.

   I also do not understand the point of lines 178-179. I would think that if you have managed to learn the prior $p_0(x_0)$ and the corruption model is known, then posterior sampling can be performed, so I do not understand why this is a strength of this particular method. The proof of Theorem 1 seems also unnecessarily convoluted. If I understand correctly the steps are: 1) show that minimizing the loss guarantees that $p_1=q_1$, 2) write the marginal expression for $q_1$, and 3) use the assumption to show that 1), 2) imply $p_0=q_0$. I think that step 1 needs more clarity. I don't understand from what's written how this follows from the minimization of the objective. Steps 2) and 3) are more straightforward and I believe that the paper would benefit by presenting them as such. Finally, I believe that it is very hard for someone not familiar with FMD and Single Cell Genomics Data to understand what's happening in section 4.3. The authors should include more details so that the authors/reviewers can appreciate the significance of the contribution, especially for Section 4.3.2.

2) The position related to prior work is weak. The authors mention that Ambient Diffusion and G-SURE-diffusion are only useful for generation and not for denoising. I respectfully disagree with this statement. In fact, there are results in the papers for solving inverse problems. The authors also miss prior work, including 1) the [Ambient Diffusion Posterior Sampling](https://arxiv.org/abs/2403.08728) paper, 2) the [Consistent Diffusion Meets Tweedie](https://arxiv.org/abs/2404.10177) paper, 3) works on learning diffusion models from corrupted data based on EM, e.g. [this work](https://arxiv.org/abs/2405.13712). Particularly 2) seems connected to the IFM objective. Overall, there are no comparisons at all with existing methods for training generative models from corrupted data. I understand the point of the authors that their technique is more general and can handle arbitrary corruptions but still, it would be very beneficial for the work to show how the method performs for corruptions that prior work can handle (such as additive Gaussian noise and masking). The authors only compare with restoration baselines (variants of the Noise2Noise framework) and they do not compare with any other generative modeling approach.

3) The experimental evaluation is limited. I believe comparisons with other generative modeling-based approaches for learning with corrupted data should be included, in the setting tested by prior work. For the experiments with natural images, the authors could have included more extensive baselines (colorized images in standard datasets such as CIFAR-10, CelebA, FFHQ, ImageNet). I also believe that the authors should spend more time explaining in the paper how Noise2Self and Noise2Void work since these are the main baselines. Finally, I firmly believe that the authors should also provide generation results (e.g. FID scores) for their trained models to understand the capacity of the method for training generative models from corrupted data.


--- 

**Update**: During the authors-reviewers discussion period, the authors confirmed that the trivial solution of always predicting 0 minimizes their objective. Even though this does not happen in practice, the theoretical validity of the proposed method is severely weakened. This also raises very important concerns regarding the correctness of the proposed theorems. For these reasons, I am lowering my score to 3 and I am recommending reject.

### Questions
See also the weaknesses above.

1) Could the authors provide connections and missing comparisons with prior work in the space of learning generative models from corrupted data?

2) Could the authors provide unconditional generation results for their method?

3) Could the authors demonstrate that their generalized consistency is useful beyond the setting of learning from corrupted data? Is this currently ablated somewhere?

4) Could the authors include experimental results in widely used datasets such as CIFAR-10, FFHQ, ImageNet?

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
4

### Summary
This paper presents a new framework, Inverse Flow (IF), designed to extend generative modeling to inverse generation tasks, such as denoising data without access to clean reference data. Traditionally, generative models like diffusion and flow-based models have relied on access to clean data to learn mappings between noisy and noise-free distributions. Generating clean data directly from noisy inputs in cases where clean data is not available is an important application of relevance in multiple areas, particularly scientific discovery, and I am glad that the authors are tackling this problem. 

The framework introduces two main algorithms: Inverse Flow Matching (IFM) and Inverse Consistency Model (ICM). IFM is an approach based on solving a reverse flow via an Ordinary Differential Equation (ODE) to gradually map noisy data back to a clean state, while ICM takes a more efficient approach by using a consistency function to produce clean data without requiring iterative ODE solutions.

The authors validate IFM by testing it on both synthetic datasets and real-world applications, such as fluorescence microscopy and single-cell genomics, where it demonstrates improved performance over traditional denoising methods that require ground truth. Authors show in all examples that their IFM does better than the baselines.

### Strengths
+ **Originality**: The paper introduces a fresh perspective on handling inverse generation problems by leveraging continuous-time generative models without the need for clean data, which addresses a significant gap in denoising research.

+ **Quality, Clarity and Presentation**: The paper is thorough in presenting both theoretical and empirical support for its claims. Proofs for the effectiveness of IFM and ICM are detailed, and experiments are extensive, covering synthetic benchmarks and practical applications. The methods, particularly the differences between IFM and ICM, are presented clearly, with diagrams and mathematical derivations that aid understanding. The paper is accessible to readers familiar with generative models and denoising literature. That said, I do believe that the paper can benefit from a bit more explanation. I found myself re-reading Section 2.1.1, 2.1.2 and 3 a couple of times until I understood all details - explaining what was happening with an example would reduce the burden on readers. 

+ **Significance**: The flexibility of IFM and ICM for a wide range of noise distributions and its applicability in denoising tasks without ground truth data offer potential advancements in fields requiring clean data from noisy measurements, such as biomedical imaging and genomics as demonstrated. Overall, the improvements in denoising performance achieved is significant, and I believe that method would foster more research in unsupervised denoising.

### Weaknesses
 + **Assumption on Noise Distribution**: As also noted by the authors, the methods reliance on prior knowledge of the noise distribution is a limitation, as it may restrict the method’s generalizability in scenarios where noise characteristics are unknown or complex. Given this, I would really like to understand to what extend the noise distribution should be known for the method to work well. Authors could do experiments using approximate noise distributions and see the implications on performance. 

+ **How much data is required?** We know that diffusion models are generally data hungry, and particularly in scientific discovery, the amount of data available is very limited. For eg. in a typical [electron microscopy denoising](https://arxiv.org/abs/2010.12970) problem, there are only 40 frames of real data available. How does the method work when the amount of noisy data is limited? 

+ **Inadequate comparison**. Can you compare with [Noise2Same](https://arxiv.org/abs/2010.11971) and [Neighbor2Neighbor](https://arxiv.org/abs/2101.02824)which doesn't make assumption on J-invariance, or justify why this comparison is not needed? This would also serve as good baselines for the experiment suggested above. 

+ **The Navier-Stokes example seem a bit oversold**. In lines 317-319 the authors say that this is particularly helpful in understanding turbulent flows but the example in Fig 2 seems a bit too simple without any turbulence. The example would be much more compelling if authors apply it to an actual turbulent flow and the algorithm is able to recover the GT. Authors may find relevant dataset [here](https://turbulence.pha.jhu.edu)

### Questions
+ **Typo:** In equation 42, the derivate has V instead of $v$

+ **Comparative Baselines**:  Can authors include a supervised baseline in the examples to see what is performance gap with a supervised system? 

+ **Is ICM training stable?** Since ICM relies on enforcing self-consistency across noise levels, it may be prone to issues with training stability or convergence in some noise settings. Clarification on the strategies used to stabilize the model (e.g., gradient clipping, regularization methods) could give further insight into ensuring training robustness.

### Soundness
3

### Presentation
3

### Contribution
3
