## Human Reviewer 1

### Summary
This paper introduces the Noise-to-Process (N2P) framework, transforming a sample from a base-noise process (Z) into a single trajectory (X) that remains consistent with observed data, supported by substantial theoretical development. Building on this, the authors propose a Deconvolution-Based Process Transformation (DBPT) implementation, which shows improvements over existing baselines on the MNIST and CIFAR datasets.

### Strengths
* **Thorough literature review**: Clearly situates the paper within prior work and explains both its positioning and novelty.


* **Sound theoretical development**: Provides extensive theory development to justify the method design.

### Weaknesses
*  The biggest concern is that the empirical performance seems weak. The proposed method shows superior results on MNIST/CIFAR at (32x32), but performs worse than WGP on the BIA and PDB benchmarks. The baselines and datasets are also kind of weak: the paper should at least test at (64x64), and more challenging datasets would be welcome. Most baselines are pre-2018, with only one (Bartosh et al., 2025) that is recent, including more recent baselines will strengthen the experiment part.

* Line 96: the proof of Proposition 2 is referred to Proposition 10, but no proof is provided for Proposition 10. 

* The discussion of “Prior-driven Approaches” is not accurate. Line 222 states, “Despite these advances, learning remains anchored to a predefined prior scaffold,” This is a strong claim, and the prior over stochastic processes can be learned directly from data via flow/diffusion models (e.g., Shi et al., 2025), which enables exact (or principled) posterior sampling.  Reference: Shi et al., Stochastic Process Learning via Operator Flow Matching, 2025.

* The paper introduces a theoretically index-agnostic paradigm but instantiates it with a specific, practical architecture (DBPT) that is, by its deconvolutional nature, tied to a discrete (regular) grid and its specific training resolution. The authors should explicitly acknowledge the gap between the theoretical advantages of the paradigm and the practical limitations of the implementation.

* Super-resolution experiments are missing. While the DBPT design seems applicable for super-resolution, its convolutional constraints likely limit evaluation to the specific training resolution. In contrast, general NP or operator-learning–based models often enable zero-shot evaluation at different resolutions (e.g., train on 64x64, evaluate on 128x128 or higher) without retraining. 

*  The ablation study in Appendix J is confusing. The Transformer-based model seems to perform very poorly , while the deconvolution architecture is significantly better. This large performance gap raises suspicion that the Transformer model may not be correctly implemented or tuned. Given that numerous state-of-the-art models in computer vision and generative modeling use Transformers as backbones and consistently show advantages over convolution-based models, I strongly suggest the authors detail the settings for this part and consider trying either a standard ViT (Vision Transformer) or a (multi-layer) cross-attention architecture

* Typos :  
1) Line 269. “Figure 2 present” should be “presents” 
2) Line 292,  “GP demonstrate” should be “demonstrates”. 
3) Line 302, “The synthetic experiment demonstrate” should be “experiments” 
4) Line 1063, “rising from !1 min” check the typo

### Questions
See weaknesses. I’m inclined to raise my score if those concerns are resolved.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes a “Noise-to-Process (N2P)” framework, claiming to model stochastic processes from a single trajectory via a generative mapping (X = G_\theta(Z)) from a shared noise process. A specific instantiation, Deconvolution-Based Process Transformation (DBPT), is introduced and trained using a masked mean squared error (MSE) objective. The authors argue that this approach enables process-level uncertainty modeling under weak priors without requiring multiple trajectories, in contrast to Neural Processes (NP) or Gaussian Process (GP) models.

### Strengths
1.The paper is clearly written and attempts to unify process modeling ideas (GP, NP, neural SDEs) under a shared noise-to-function framework.

2.The experimental results cover diverse tasks (synthetic, time series, image completion) and demonstrate reasonable reconstruction quality.

### Weaknesses
The proposed N2P framework largely restates existing ideas found in Variational Implicit Processes, Normalizing Flow GPs, or Neural SDEs. The notion of generating a stochastic process via a measurable transformation of a base noise process (e.g., a Gaussian or Wiener process) is well established in prior literature. The contribution here is mainly terminological (“weak prior paradigm”) rather than methodological.

Despite the stochastic notation, the training objective reduces to a deterministic regression with noise regularization:
$$
L = E_Z[\frac{1}{\tau_o}|R_{\tau_o}(G_\theta(Z)) - O|_F^2].
$$
There is no explicit likelihood, no KL regularization, and no posterior inference—thus no genuine process-level probabilistic learning. In effect, the method behaves like a conditional generator (akin to a GAN without a discriminator) trained purely with an MSE loss.

The comparison with Neural Processes (NP) is also misleading. The claim that NP “requires multiple trajectories” is not accurate; NP frameworks can, in principle, operate on single trajectories, though with limited generalization. More importantly, NP remains a proper probabilistic model with explicit latent variables and variational inference, whereas N2P collapses to deterministic regression. The distinction the paper emphasizes (task-level z vs noise process Z) is not substantial.

The experimental evaluation is limited. Reported improvements over baselines are modest and could easily result from architectural capacity or convolutional inductive biases. There is no ablation study to isolate the effect of the proposed “noise process” component, and the claims of “single-trajectory learning” are not convincingly demonstrated—the model still relies on dense sampling along one trajectory, which effectively provides many supervision points.

The paper does not compare against recent and strong baselines in process learning and uncertainty-aware meta-learning, such as Attentive Neural Processes (Kim et al., 2019), Convolutional Conditional Neural Processes (Gordon et al., 2019), Transformer Neural Processes (Nguyen & Grover, 2022), and Neural Diffusion Processes (Dutordoir et al., 2023).

It also fails to cite or discuss several directly relevant works. Most notably, Variational Implicit Processes (Garnelo et al., ICML 2019) and “Functional Variational Inference based on Stochastic Process Generators” (Chao Ma, NeurIPS 2021) already introduced the same “noise-to-function” formulation with proper probabilistic objectives. Similarly, the idea of mapping base noise to structured samples has long existed in GANs and Normalizing Flow models. By omitting these foundational references and not clarifying its novelty relative to them, the submission overstates its originality and misrepresents its contribution.

The experimental validation is limited in both scale and diversity. Most experiments are confined to small, overused datasets such as MNIST and CIFAR-10. These benchmarks are no longer considered sufficient for demonstrating generalization or scalability in the ICLR community, as their challenges have been largely saturated. The paper does not evaluate on larger, more complex datasets or real-world continuous process data, making it difficult to assess whether the proposed framework meaningfully improves process-level modeling beyond toy examples.

While the paper’s narrative is appealing—“learning stochastic processes from a single trajectory under weak priors”—the technical substance does not support this claim. The approach amounts to deterministic regression with injected noise and lacks both probabilistic rigor and meaningful novelty. The comparison with Neural Processes is conceptually misleading, and the theoretical contributions are largely decorative. 

Additionally, several presentation and technical issues reduce the clarity of the paper. Many equations appear without numbering, making it difficult to reference them in the text. In addition, some lemmas and corollaries are stated without proof or with only vague intuitive arguments. For a paper that emphasizes theoretical grounding, the absence of formal derivations undermines the claimed rigor and makes it hard to verify correctness.

### Questions
1. The paper claims to enable single-trajectory stochastic process learning, yet the training still relies on densely sampled points from the same trajectory. How does the method behave under sparse or partially observed data? Is there any theoretical or empirical analysis of sample complexity?

2. The notion of a “weak prior” is central to the paper’s narrative. Could the authors formally define what constitutes a “weak” prior in this context and explain how it differs quantitatively from priors in GP or Neural SDE models?

3. The training loss is a plain MSE （page 4） with Monte Carlo noise resampling. How does this loss capture process-level uncertainty rather than simple reconstruction accuracy? Have the authors considered using an explicit likelihood-based or probabilistic objective instead?

4. Compared with *Variational Implicit Processes* (VIP) (Garnelo et al., ICML 2019), the proposed method removes the variational posterior and KL term. What is the theoretical justification for this simplification? Does this mean the model is optimized purely under empirical risk minimization without probabilistic inference semantics?

5. Theoretical elements such as Kolmogorov consistency and measurability are presented at length. Do these properties impose any actual constraints or provide practical benefits for model training and inference, or are they purely formal?

6. The experiments omit comparisons with recent state-of-the-art Neural Process and process-learning models (e.g., Attentive NP, Transformer NP, Neural Diffusion Processes). Were these baselines tested, and if not, how do the authors justify the fairness of their empirical evaluation?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a ``noise-to-process'' (N2P) paradigm for learning stochastic processes from a single, sparsely observed trajectory. The key idea is to learn a single, parameterized generator $G_{\theta}$  that maps a shared base-noise process $Z$ to a full trajectory $\bar{X} = G_{\theta}(Z)$. This design ensures projective consistency by construction, as all finite-dimensional marginals are projections of the same joint sample. The authors instantiate this paradigm with Deconvolution-Based Process Transformation (DBPT), which uses a noise encoder and a multi-scale deconvolutional decoder to capture inter-temporal dependencies. DBPT is evaluated on synthetic data, financial time series, image completion, and black-box optimization, comparing against prior-driven (e.g., GPs, SDEs) and data-driven (e.g., CNPs) baselines.

### Strengths
* The general idea of the paper is easy to follow. 

* The `noise-to-process' paradigm, in its abstract form, bears a conceptual resemblance to frameworks like transformed GPs that map a base process through a nonlinear function. However, the significant novelty of this work lies in its concrete formulation for the single-trajectory regime and the introduction of the DBPT architecture, which uses a shared noise process and a deconvolutional decoder to explicitly enforce projective consistency and capture long-range dependencies.

### Weaknesses
Some limitations in my eyes are as follows:

* **Writting**. The writting and organization of the paper can be improved. For example, the citation commands (e.g., \citet vs. \citep) appear to be used wrongly and inconsistently, which affects the flow of the narrative. Several acronyms are introduced without full definitions at first use.  

*  The experiment section can be better explained. For example, in terms of time-series MSE, what is the MSE here? Prediction or imputation?

*   **Limitation of Discrete Index Sets:** The entire framework is built upon a discretized index set $\mathcal{T}$. While Corollary 13 states that the model is *compatible* with Kolmogorov extension to a continuum, this is an existence result. In practice, the trained DBPT model is fixed to its training grid. Making predictions at arbitrary, new time points not in $\mathcal{T}$ would require re-discretization and potentially retraining, which is a significant limitation compared to native continuous-time models like GPs or Neural SDEs. The method lacks **native continuous-index inference**.

*   **Dependence on Generator and Noise Specifications:** The quality of the learned stochastic process is entirely dependent on the representational capacity of  $G_{\theta}$ and the characteristics of the base noise $Z $. While the deconvolution decoder is a good choice, the framework is susceptible to issues common in generative models, such as potential **mode collapse** or failure to capture the full complexity of the target process's randomness, especially if the architecture or noise dimension is poorly chosen. 

*   **Scalability and Computational Cost:** The claim of ``lightweight computation'' (Appendix E) is supported for the presented tasks, but this may not scale well. Generating the *entire trajectory* in one forward pass means that for very high-resolution index sets (e.g., megapixel images or extremely long sequences), the memory and computation cost of the deconvolutional decoder could become prohibitive. A more nuanced discussion of the **computational complexity in  $|\mathcal{T}|$** and its scaling limits would be helpful.

*   **Depth of Comparison with State-of-the-Art:** The baseline selection is relatively dated (except SDE matching); a comparison with more recent and powerful sequence models, such as single-sequence diffusion models (see question section) or Gaussian process state-space models, would strengthen the evaluation.

### Questions
1. The theoretical guarantee of projective consistency is a key advantage. Could you design a simple quantitative experiment to empirically verify this property on a held-out test? For example, by showing that the marginal distribution at a point  $t$, computed from different higher-dimensional joint distributions that includet, remains consistent, which might not be the case for a method like CNP.

2. The masked MSE objective is simple, but it only supervises the mean (implicitly). While uncertainty emerges from noise resampling, the training signal doesn’t directly optimize calibration (e.g., via NLL or CRPS). Maybe it should note that this is a pragmatic choice, but may limit distributional fidelity compared to likelihood-based methods.  And also, in terms of performance metrics, including CRPS and other uncertainty quantification metrics would be beneficial. 

3. In sparse data regimes, I suspect that overfitting can be an issue. At least, training the network here seems not data-efficient to me. Can the authors explain more about this, particularly compared to GP+DKL?

4. The paper shows an ablation on the decoder architecture. Could you provide more analysis on the sensitivity to the dimension and distribution of the base noise $Z$? What happens if  $d_z $ is too small or too large? Are there guidelines for choosing $Z$ for a new problem?

5. There are a series of papers about ``Diffusion Generative Models in Infinite Dimensions'' and ``Score-based Diffusion Models in Function Space'', which also transform the noise into a random process. There was a lack of discussion of comparisons in the paper. In my opinion, this paper should also compare to the Transformed Gaussian Processes (TGP) using Normalizing Flow, since TGP is also strongly related to this paper.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The work proposed a noise to stochastic process (N2P) framework that consists of two parts, a shared base process and a shared generator to transform the base process to observable trajectories. The work aims at solving the prior constraints of existing approaches like SDE-based approaches or structured GP-based approaches. The work further proposed an instantiation of the N2P framework called deconvolution based process transformation (DBPT) where the base process are IID Gaussians on a finite discrete time grid and the common generator is a deconvolution network. The work evaluate the proposed DBPT on both time-series modelling and image completion tasks and conducted ablation study on

### Strengths
1. The experiment section of the work considers a divers set of tasks including time series modeling, image modeling and black-box optimization.
2. The presentation is well structured with a general N2P framework followed by DBPT as the the concrete instantiation of the N2P framework and the technical details. The work makes a clear distinction between N2P as the theoretical framework and DBPT as a methodological contribution.
3. The work also studies different architecture choice for DBPT to justify the choice of a deconvolution architecture.

### Weaknesses
1. In Section 2.1, the work grounds the theoretical results on the basis of finite or countable time grid T. First, I can not see how a generator $G_\theta$ take an infinite number of $Z_t$s as inputs. Considering the actual DBPT model operates on a predefined, finite, discrete grid, the actual instantiation of the N2P framework is underwhelming and makes the grandiose theoretical result of Section 2.2 which invokes the Kolmogorov Extension Theory unnecessary.
2. The experiment results on finance related data is very weak. 
3. The work compares against conditional neural processes and SDE matching as baselines from the SDE-based approaches and neural process families. More recent and stronger baselines like latent SDE [1, 2], attentive and transformer neural processes[3, 4], gaussian neural processes [5, 6] should be compared against.

References:

[1] Li, Xuechen, et al. "Scalable gradients for stochastic differential equations." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.

[2] Deng, Ruizhi, et al. "Continuous latent process flows." Advances in Neural Information Processing Systems 34 (2021): 5162-5173

[3] Kim, Hyunjik, et al. "Attentive neural processes." arXiv preprint arXiv:1901.05761 (2019).

[4] Nguyen, Tung, and Aditya Grover. "Transformer neural processes: Uncertainty-aware meta learning via sequence modeling." arXiv preprint arXiv:2207.04179 (2022).

[5] Bruinsma, Wessel P., et al. "The Gaussian neural process." arXiv preprint arXiv:2101.03606 (2021).

[6] Markou, Stratis, et al. "Practical conditional neural processes via tractable dependent predictions." arXiv preprint arXiv:2203.08775 (2022).

### Questions
1. If we restrict the setup to a finite, discrete, and pre-defined time grid, is there any fundamental difference between the proposed N2P framework and the existing neural processes framework?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
2