# Probing the Latent Hierarchical Structure of Data via Diffusion Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
\looseness=-1 High-dimensional data must be highly structured to be learnable. Although the compositional and hierarchical nature of data is often put forward to explain learnability, quantitative measurements establishing these properties are scarce. Likewise, accessing the latent variables underlying such a data structure remains a challenge. 
    In this work, we show that forward-backward experiments in diffusion-based models, where data is noised and then denoised to generate new samples, are a promising tool to probe the latent structure of data.
    We predict in simple hierarchical models that, in this process, changes in data occur by correlated chunks, with a length scale that diverges at a noise level where a phase transition is known to take place. Remarkably, we confirm this prediction in both text and image datasets using state-of-the-art diffusion models. 
    Our results show how latent variable changes manifest in the data and establish how to measure these effects in real data using diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper examines the hierarchical correlation structures among input tokens using a dynamic correlation function and dynamical susceptibility within a forward-backward experimental framework. These variables reveal how two input tokens respond to perturbations when attempting to recover data from noisy inputs. Analyzing diffusion and language models, the study demonstrates an anticipated correlation aligned with spatial structures.

### Strengths
(1) The paper introduces novel approaches for analyzing the structure of inputs using pretrained diffusion and language models.

(2) The authors offer a thorough analysis and derivation, with experimental results closely aligning with theoretical expectations.

(3) Multiple schematic diagrams and data visualizations are included, providing valuable insights into the methods.

### Weaknesses
 (1) The paper’s presentation could be improved. While there are numerous figures to aid understanding, the main text is somewhat challenging to follow.

(2) Why is the σ in Equation 3 binary? Wouldn’t a continuous measurement be more appropriate? For instance, a small difference in pixel values might not alter the semantic structure of the images, but it would be captured by binary measurement.

(3) Shouldn’t the spatial correlation structures be content-dependent? For example, if the bird and the laptop in Figure 5 were moved slightly farther from the camera, would this change affect the result shown in Figure 2?

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to understand diffusion models through a hierarchical latent variable model. Through this framework, this paper demonstrates the connection between the noise level and the hierarchical levels, as evidenced by a transition phrase. This paper builds on the tools from physics and illustrate their theoretical model with empirical results on practical models.

### Strengths
1. The hierarchical perspective provides novel insights into the diffusion model's mechanism and the application of physics is also refreshing. I feel that the community can benefit from these insights, which may give rise to empirical advancements.
2. The paper is well written and clearly communicates the main ideas.
3. The experiments on natural data (image/text) support the theoretical claims.

### Weaknesses
1. It'd be great to see attempts at utilizing the theoretical/empirical observations to advance practical model design. Some discussions along this direction would also be appreciated.
2. The tree model seems overly simplified for real-world data like images and languages. For example, one would imagine two high-level variables could become co-parents for some low-level variables, thus breaking the tree structure. I would appreciate a discussion on this limitation and the applicability of the theoretical framework to more general latent models.

### Questions
Please refer to the weaknesses section.

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
2

### Summary
In this paper, the authors examine the hierarchical structure in high-dimensional data by conducting forward-backward experiments within diffusion-based models. They employ a Random Hierarchy Model (RHM) for the data where the tokens of data are generated from a tree structure of latent, they also use Belief Propagation (BP) as the score function to denoise samples.

The authors focus on the phase transition of the average belief $p_L$ of the RHM's root node by analyzing an iterative mapping (Equation 7) and identifying a critical noise level $\epsilon^*$ at which the transition occurs. Based on that, they also compute the minimum layers $\tilde {l}$ needed for the transition, beyond which $p_l$ would collapse to trivial fixed points $\{1/v,1\}$, indicating either a complete reconstruction or randomization of upper latent variables. At this specific noise level, BP can modify the deepest latent layer $\tilde {l}$, yielding the maximum correlation length (i.e. big "chunks" of data token), which is the distance over which token changes remain correlated.

To characterize this effect, the authors introduce **dynamical susceptibility** which exhibits a first increase then decrease curve as expected. They further demonstrate that the dynamical susceptibility curve has the same trend for forward-backward experiments with diffusion models and synthetic RHM experiments.

### Strengths
1. The authors aim to capture hidden hierarchical structures within discrete data using the RHM model, with their RHM+BP framework supporting both discrete and continuous diffusion processes.

2. By applying BP for denoising, the authors rigorously analyze phase transitions in the denoising results and identify the critical noise level needed to induce a change in the data class (or low-level feature).

### Weaknesses
1. The paper is somewhat disorganized and hard to follow, as definitions, derivations, and experimental results are heavily interwoven. To improve clarity, consider using theorems or structured definitions to better organize the content (e.g. by moving some derivations, such as Equations 8 and 9 to appendix and summarizing them as a main theorem).

2. In practice, people use real data + score-based denoising; however, the authors use RHM data + BP denoising instead. This discrepancy is insufficiently justified, making the claim that real-world data shares the same hierarchy as RHM unconvincing. While the authors show a similar phase transition phenomenon between the RHM case and real-world diffusion case, they do not rigorously establish a connection between them. Verification by testing real-world diffusion on RHM data may strengthen this claim.

3. The results are somewhat vague and lack practical insights, as it appears that neither the RHM setup nor the forward-backward experiment has direct practical applications. Although the authors mention interpreting the "chunks" that emerge during the forward-backward experiments, they do not provide further discussion or related work on that.

### Questions
1. From the analysis, BP denoising appears to be a one-step method that directly samples $\hat{x_0}$ from the noisy observation $x_t$, differing from typical diffusion denoising that iteratively samples $x_{t-1}$ from $x_t$ throughout the process. Does this discrepancy exist, or are the authors also using a denoising schedule similar to real diffusion models?

2. Can we interpret the maximal correlated length achieved at an intermediate noise level (time step) as the model generating class information or lower-level features? If so, this would contrast with existing observations that diffusion processes follow a coarse-to-fine generation pattern (e.g., https://arxiv.org/abs/2303.02490), where lower-level features are generated at the beginning, not in the middle.

3. Figure 4(a) is somewhat unclear. Combined with (c), it seems the authors are suggesting that the largest correlated changing chunk appears at a masking fraction $t/T \in [0.5, 0.7]$. However, this is not immediately evident from (a) alone.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper suggests that forward-backward diffusion experiments can be helpful in uncovering hierachical structure in data. They first study a synthetic Random Hierarchical Model and show that a peak of the dynamical susceptibility (related to correlations between blocks of tokens) occurs at a noise level where a phase transition is known to occur in the RHM (i.e. the latent class at the root changes). They then show peaks in the susceptibility in text and image experiments.

### Strengths
The paper is clearly written and the RHM model is nicely studied. The text and image experiments are well-designed (although I still have some questions, below, about how well the conclusions from RHM transfer to real data). I appreciate the application of ideas from Physics to ML problems.

### Weaknesses
L57: Does such a divergence definitely indicate a hierarchical structure or are there other ways/reasons divergence could occur? i.e. is this divergence a “proof” of (or very strong evidence for) hierarchy? It's not clear if the observed divergence is unique to hierarchical models or if other non-hierarchical models could also exhibit similar behavior under specific conditions. The paper needs to more clearly address the specificity of this divergence as a signature of hierarchy.

L210: Clarification: so, the epsilon-process is itself a mean-field approximation of the discrete diffusion process, but then you use another mean-field on top of that to compute the correlation? The description of the mean-field approximations is somewhat unclear. It would be helpful to have a more detailed explanation of how these approximations are derived and what assumptions they entail. Specifically, the relationship between the epsilon-process and the discrete diffusion process needs further elaboration.

L356: Can you elaborate on why a susceptibility peak is a ‘smoking gun’ for hierarchy? Just because one nonhierarchical example doesn’t have a susceptibility peak doesn’t mean there might not be others that do? The argument that a susceptibility peak is a 'smoking gun' for hierarchy is not entirely convincing. The paper only shows that one specific non-hierarchical model doesn't exhibit this peak, but this doesn't preclude the possibility that other non-hierarchical models might. A more rigorous justification is needed to support this claim.

L511: How (or does) this relate to the diffusion-as-spectral-autoregression point of view? Also there is a typo, 'trough'. The connection to the diffusion-as-spectral-autoregression perspective is not clear. The paper should discuss how the observed phenomena relate to this alternative viewpoint. Additionally, the typo should be corrected.

General:

Does the susceptibility divergence tell us anything about how many levels of hierarchy are likely present? Or just that there is at least one level? The paper does not adequately address whether the susceptibility divergence can provide information about the depth of the hierarchy, or if it simply indicates the presence of at least one level. This is a crucial point that needs further discussion.

The RHM is discrete, and discrete vs continuous diffusion are rather different; can you justify why RHM should be a good model for continuous data/diffusion as well? The justification for using the discrete RHM as a model for continuous data and diffusion is weak. The paper needs to provide a more compelling argument for why the RHM is a suitable model for continuous data, given the fundamental differences between discrete and continuous diffusion processes.

Do the MDLM and ImageNet expts actually confirm that a phase transition occurs? Or do we just observe the susceptibility peak and infer a phase transition by analogy to RHM? In particular, it seems that for ImageNet it might actually be possible to run a classifier to determine whether the class changed. It's not clear if the experiments on MDLM and ImageNet actually demonstrate a phase transition, or if the authors are just inferring it based on the susceptibility peak. The paper should provide more direct evidence for a phase transition, especially for ImageNet where a classifier could be used to verify class changes.

### Questions
L57: Does such a divergence definitely indicate a hierarchical structure or are there other ways/reasons divergence could occur? i.e. is this divergence a “proof” of (or very strong evidence for) hierarchy?

L210: Clarification: so, the epsilon-process is itself a mean-field approximation of the discrete diffusion process, but then you use another mean-field on top of that to compute the correlation?

L356: Can you elaborate on why a susceptibility peak is a ‘smoking gun’ for hierarchy? Just because one nonhierarchical example doesn’t have a susceptibility peak doesn’t mean there might not be others that do?

L511: How (or does) this relate to the diffusion-as-spectral-autoregression point of view? Also there is a typo, 'trough'.

General: 

Does the susceptibility divergence tell us anything about how many levels of hierarchy are likely present? Or just that there is at least one level?

The RHM is discrete, and discrete vs continuous diffusion are rather different; can you justify why RHM should be a good model for continuous data/diffusion as well?

Do the MDLM and ImageNet expts actually confirm that a phase transition occurs? Or do we just observe the susceptibility peak and infer a phase transition by analogy to RHM? In particular, it seems that for ImageNet it might actually be possible to run a classifier to determine whether the class changed.

### Soundness
4

### Presentation
3

### Contribution
3
