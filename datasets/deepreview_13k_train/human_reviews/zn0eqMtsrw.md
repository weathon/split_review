# GUD: Generation with Unified Diffusion

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Diffusion generative models transform noise into data by inverting a process that progressively adds noise to data samples. Inspired by concepts from the renormalization group in physics, which analyzes systems across different scales, we revisit diffusion models by exploring three key design aspects: 1) the choice of representation in which the diffusion process operates (e.g. pixel-, PCA-, Fourier-,\linebreak or wavelet-basis), 2) the prior distribution that data is transformed into during diffusion (e.g. Gaussian with covariance $\Sigma$), and 3) the scheduling of noise levels applied separately to different parts of the data, captured by a component-wise noise schedule.
Incorporating the flexibility in these choices, we develop a unified framework for diffusion generative models with greatly enhanced design freedom. In particular, we introduce soft-conditioning models that smoothly interpolate between standard diffusion models and autoregressive models (in any basis), conceptually bridging these two approaches.
Our framework opens up a wide design space which may lead to more efficient training and data generation, and paves the way to novel architectures integrating different generative approaches and generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors describe diffusion models with a under class of dynamics and marginals than the typical scaled Ornstein Uhlenbeck or Brownian motion reference processes used in the vast majority of diffusion model papers. In particular, the authors consider a linear transformation to perform the diffusion under a change of basis; varying the variance of the prior  Gaussian marginal  to match the data distribution; considering time dependent diffusion scale terms which can lead to auto-regressive-like dynamics.

### Strengths
The paper is well explained. 

The authors bring attention to the flexibility in the diffusion model paradigm, though as discussed below this has been discussed in many prior papers.

The authors introduce what I believe to be a novel interpretation and use case for time-varying diffusion scale timers, leading to an autoregressive type forward process, applying noise to separate components independently. A similar procedure was used for diffusion in frequency space by applying different diffusion noise scales per frequency level [1] but these were not set to 0 as described here.


[1] Blurring diffusion models, Hoogeboom et al 2022

### Weaknesses
## Weakness 1
While the authors attempt to unify the design of dynamics for references; two of the three ideas proposed are not novel so it is unclear what the main contributions of the paper are.

1) Using a change of basis
Applying diffusion in a transformed space / change of basis has been done before. Although [1] focuses on  change of basis to frequency basis, section 4.1 of [1] explicitly explains how any other change of basis can be performed.  I do not see any compelling evidence to suggest one basis over another in this submission. The authors do not provide any theoretical justification or empirical evidence to support the claim that a specific basis is advantageous for the proposed method. The lack of a clear rationale for choosing a particular basis undermines the novelty of this aspect.

2) Prior distribution
Discussion of variance of prior distribution was first discussed in [3], and referred to as Technique 1. This is still using diagonal covariance. It is not clear how scalable learning the covariance matrix for a full high dimensional data distribution would be or if it would even be beneficial. The authors do not address the computational cost of estimating or using a full covariance matrix, nor do they provide any analysis of the potential benefits of a non-diagonal covariance structure. This raises concerns about the practical applicability of this approach.

The time-dependent diffusion scale term has not been investigated in much detail as far as I am aware and I believe this should be the main focus of the paper or at least more attention.

## Weakness 2
The second major weakness is in limited numerical evaluation. The FID scores shown for CIFAR10 are >20; significantly far from standard diffusion model performance of <3. It is not possible to evaluate whether there any benefit to generative modelling for the proposed methods without compelling numerical support. The lack of competitive FID scores makes it difficult to assess the practical value of the proposed techniques. The authors should provide more extensive experimental results on standard benchmarks to demonstrate the effectiveness of their approach.

Whilst I am not particularly interested in SOTA generative models FID <2, for toy datasets like CIFAR10 I would expect at least FID<4 given the abundance of code available for this and the limited novelty for 2/3 methods.

## Weakness 3
It is not clear to me the theoretical soundness of using the autoregressive approach for extending existing images i.e. changing dimension from previously trained model. It seems the generative process is no longer related to the time reversal of an SDE given the dimension changes. Can this be formalised? The authors do not provide a rigorous theoretical framework for the autoregressive image extension process. The lack of a formal connection to the reverse-time SDE raises concerns about the validity of this approach. The authors need to clarify how the generative process remains consistent with the underlying diffusion model when the dimensionality changes.

Minor
- Blurring diffusion models [2] was a follow up to inverse Heat Dissipation Generative Model [1]. This should be cited and discussed as it was a pioneering paper in this area.

### Questions
See weaknesses.

The time-dependent diffusion scale term has not been investigated in much detail as far as I am aware and I believe this should be the main focus of the paper or at least more attention. What are the benefits of this compared to cascading diffusion, can cascading be seen as a case of this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces the Generative Unified Diffusion (GUD) model, a framework that expands the flexibility of diffusion-based generative models by enabling diverse configurations in basis representation, noise scheduling, and prior distributions. Standard diffusion models transform noise into data through a learned reverse process. Here, GUD leverages concepts from physics, specifically renormalization group flows, allowing distinct configurations in the process, such as using Fourier, PCA, or wavelet bases, and implementing component-wise noise schedules to tune noise levels for different data parts.

The GUD framework unifies diffusion and autoregressive models, bridging differences between simultaneous and sequential generation. It introduces soft-conditioning, where the model can conditionally generate components based on previously generated data, enabling partial dependency across features. The approach supports more efficient training, flexible architectural designs, and tasks requiring conditional generation, inpainting, or sequential extensions.

A key technical innovation is in the model’s flexibility of noise schedules and priors. GUD models allow each component a unique noise schedule, enabling a range of generation hierarchies from purely autoregressive (extreme component-wise scheduling) to standard diffusion. Additionally, a whitening transformation using PCA stabilizes the variance, simplifying the denoising process.

Experiments demonstrate the framework's adaptability across various data representations, including PCA, Fourier, and wavelet bases. By controlling softness and hierarchical order in noise schedules, GUD supports both hierarchical and spatially sequential generation, showing improved performance on benchmark image generation tasks, like CIFAR-10.

### Strengths
The Generative Unified Diffusion (GUD) model provides a novel unification of diffusion and autoregressive generative approaches, allowing a flexible transition between simultaneous and sequential generation processes. This ability to bridge methods expands the framework’s application to a broad spectrum of tasks, from inpainting and sequential data extension to standard generative modeling. By creating a model that can interpolate between different generative styles, GUD allows developers to tailor the generation process to specific needs, enhancing control over the structure and dependencies of generated data.

One of GUD’s most notable strengths is its capacity for component-wise noise scheduling, which enables a hierarchical and selective approach to noising different parts of the data. This flexibility allows the model to prioritize important features by applying noise schedules tailored to specific components, leading to a more efficient and accurate generative process. Combined with its support for multiple basis representations—such as pixel, PCA, Fourier, and wavelet bases—GUD is adaptable to various data types and structures, making it particularly suitable for applications that benefit from multi-scale or hierarchical data representations.

Additionally, GUD’s design includes a whitening process, which aligns the data and noise distributions, providing better variance control throughout the generative process. This feature simplifies denoising and increases model stability, potentially reducing training time by minimizing noise-related artifacts. By supporting flexible basis selection, component-wise noise control, and variance alignment, GUD allows for refined generative modeling that can adapt to diverse tasks and applications, offering a powerful tool for high-quality, customizable data generation.

### Weaknesses
The GUD framework is flexible, and consequently introduces significant computational complexity. Each configuration, such as basis choice (PCA, Fourier, wavelet) and component-wise noise scheduling, requires tuning, making the model resource-intensive. This complexity can hinder scalability, especially in high-dimensional data applications where each choice impacts the computational load. The authors do not provide a clear methodology for selecting optimal configurations, which is a significant drawback given the vast parameter space. For instance, the choice of basis representation and the specific noise schedule for each component are not trivial and can drastically affect performance. Without a systematic approach, users may struggle to effectively leverage the model's flexibility. 

Architecturally, GUD’s design adds complexity by requiring modifications like cross-attention mechanisms for conditioning on component-wise noise states. These additions complicate the implementation and increase the risk of instability during training, as standard architectures like U-Nets are not inherently optimized for GUD’s intricate conditioning needs. The paper does not fully explore the implications of these architectural modifications on training stability and convergence. The need for custom layers and conditioning mechanisms adds to the implementation overhead and makes it harder to adopt the framework using existing deep learning libraries.

Finally, I think the authors could have expanded the comparison with  related works. As (non exhaustive) examples, non isotropic noise perturbation has been considered in [1] and optimal steady state covariance wrt the data distribution has been investigated [2]. The current discussion does not adequately position the GUD framework within the broader landscape of diffusion models, particularly those exploring alternative noise structures and optimization strategies. A more thorough comparison would help clarify the unique contributions and limitations of the proposed approach.

### Questions
Could the authors explain how to select in the large design space the various parameters/hyperparameters?

Can the authors briefly position wrt the works like the ones cited in the weaknesses section?

Minor:  Figure 7 is qualitatively difficult to interpret from someone not specialized in the field. I suggest the authors to either add some extra comments or produce a similar image for a dataset which is more understandable for a generic reader.

### Soundness
3

### Presentation
3

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
This paper proposes Generative Unified Diffusion (GUD), an extension of standard diffusion models based on the Ornstein-Uhlenbeck process. By defining appropriate orthogonal transformations, the authors introduce novel analyses and designs within the GUD framework, including SNR analysis, soft-conditioning, whitening, and orthogonal transformations. The authors conclude with experiments that validate these designs, showcasing GUD's potential in various applications.

### Strengths
1. The paper addresses limitations in standard diffusion models by proposing an interesting and innovative Generative Unified Diffusion (GUD) model.
2. The theoretical foundation of the paper is solid, and the presentation is clear.
3. The analyses and designs within the GUD framework are novel and potentially valuable across multiple applications.

### Weaknesses
1. **Limited empirical evaluation:** The experiments primarily serve to validate the proposed designs (pixel/PCA/FFT). While these results offer some insights, the evaluation lacks depth, particularly in quantifying each design’s impact on GUD's performance. More comprehensive quantitative and qualitative results would better demonstrate the effectiveness of each design. For instance, the paper does not provide a clear comparison of FID scores or other relevant metrics across different basis choices and schedules, making it difficult to assess the practical benefits of GUD. The experiments should also include a more diverse set of datasets to demonstrate the generalizability of the proposed method.

2. **Limited practical application contribution:** Although the paper suggests various potential applications, it appears these may not be fully viable in practice. The paper lacks concrete examples of how GUD could be applied to solve real-world problems, and the potential benefits over existing methods are not clearly articulated. Providing further insights into real-world application strategies, such as specific use cases with detailed implementation considerations, would enhance the paper's practical relevance.

3. **Missing discussion of related work:** One significant application of GUD is the component-wise scheduling for different states used in sequential generation (as outlined in Sec. 5.2). As a comparison, [1,2] also propose distinct schedules for different components. Could the authors discuss these related works or provide a comparative analysis within the GUD framework?

### Questions
Could the authors summarize the experimental results from Sec. 5.1, particularly regarding how the choice of basis, prior, and noising schedule contributes to performance compared with standard diffusion models?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a unified framework for diffusion generative models, inspired by renormalization concepts from physics, allowing for flexible design choices in representation, prior distribution, and noise scheduling. The framework introduces soft-conditioning models that blend diffusion and autoregressive approaches, potentially enabling more efficient training and versatile generative architectures.

### Strengths
1. **Unified Framework**: The authors present a cohesive framework for diffusion generative models, broadening design options.

2. **Structured Components**: The framework is well-organized around the Ornstein-Uhlenbeck process, prior distribution choice, and component-wise noise scheduling, enhancing its theoretical foundation.

3. **Diverse Design Examples**: The paper includes examples of various diffusion designs, demonstrating the framework’s flexibility and applicability.

### Weaknesses
1. **Limited Experimental Scope**: The experiments are primarily conducted on CIFAR-10, a relatively small dataset. The use of a single, small dataset limits the ability to assess the framework's scalability and robustness.  Datasets with larger, more complex images, such as ImageNet or even higher-resolution datasets like CelebA-HQ, would be necessary to validate the findings and demonstrate the framework’s effectiveness in diverse settings, particularly its ability to handle high-dimensional data and complex dependencies. The current experiments do not provide sufficient evidence that the proposed framework is competitive with state-of-the-art diffusion models on more challenging benchmarks.

2. **Insufficient Explanation of Unified Diffusion and Autoregressive Generation**: The explanation on how the framework unifies standard diffusion and autoregressive generation remains unclear. While the concept of component-wise noise scheduling is introduced, the paper lacks a concrete, step-by-step example that would illustrate how this scheduling can smoothly transition between a standard diffusion process and an autoregressive generation scheme. A more detailed explanation, perhaps with a specific example using a toy dataset, would be beneficial to clarify the practical implications of this unification. The current explanation leaves the reader with an abstract understanding without a clear grasp of the implementation details.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
4
