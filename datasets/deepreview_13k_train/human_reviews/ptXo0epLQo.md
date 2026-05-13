# $\alpha$TC-VAE: On the relationship between Disentanglement and Diversity

- Decision: Accept
- Scores: 8, 5, 5

## Abstract
Understanding and developing optimal representations has long been foundational in machine learning (ML). While disentangled representations have shown promise in generative modeling and representation learning, their downstream usefulness remains debated. Recent studies re-defined disentanglement through a formal connection to symmetries, emphasizing the ability to reduce latent domains (i.e., ML problem spaces) and consequently enhance data efficiency and generative capabilities. However, from an information theory viewpoint, assigning a complex attribute (i.e., features) to a specific latent variable may be infeasible, limiting the applicability of disentangled representations to simple datasets. In this work, we introduce $\alpha$-TCVAE, a variational autoencoder optimized using a novel total correlation (TC) lower bound that maximizes disentanglement and latent variables informativeness. The proposed TC bound is grounded in information theory constructs, generalizes the $\beta$-VAE lower bound, and can be reduced to a convex combination of the known variational information bottleneck (VIB) and conditional entropy bottleneck (CEB) terms. Moreover, we present quantitative analyses and correlation studies that support the idea that smaller latent domains (i.e., disentangled representations) lead to better generative capabilities and diversity. Additionally, we perform downstream task experiments from both representation and RL domains to assess our questions from a broader ML perspective. Our results demonstrate that $\alpha$-TCVAE consistently learns more disentangled representations than baselines and generates more diverse observations without sacrificing visual fidelity. Notably, $\alpha$-TCVAE exhibits marked improvements on MPI3D-Real, the most realistic disentangled dataset in our study,  confirming its ability to represent complex datasets when maximizing the informativeness of individual variables. Finally, testing the proposed model off-the-shelf on a state-of-the-art model-based RL agent, Director, significantly shows $\alpha$-TCVAE downstream usefulness on the loconav Ant Maze task. Implementation available at https://github.com/Cmeo97/Alpha-TCVAE

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method for learning disentangled representations, alpha-TCVAE. 
It is based on a new lower bound for TC loss, that convexly combines VIB and CEB terms.
For alpha = 0, the alpha-TCVAE reduces to beta-VAE.
Experiments show that alpha-TCVAE brings some improvement in disentanglement quality measures and diversity of generated samples. 
Comparisons with beta-TCVAE, beta-TCVAE, FactorVAE, beta-VAE+HFS, VAE and StyleGAN are provided.
An additional experiment shows usefullness of alpha-TCVAE for reinforcement learning.

### Strengths
1. A new approximation to the TC loss is provided.
2. In Appendix E, authors show that α-TCVAE can learn and represent generative factors that are not present in the ground-truth dataset. This is a very surprising observation, probably authors shoud consider making it more visible by moving it to the main part of the manuscript.
3. Have you used augmentations during training? Because new factors of variations (like camera elevation) mights be side effect of some augmentations like crop. 
4. A comparison with the recent model β-VAE+HFS is provided.
5. The paper contains interesting insights about connections between disentanglement and diversity.
6. An application to RL is provided.
7. The paper is well written and easy to follow, the language is fine.

### Weaknesses
1. The improvements over other VAE-based methods are very moderate, sometimes lower than std.
2. The popular dSprites dataset is missing; also popular measures like MIG, DCI-C, DCI-I are missing.
3. The term Iθ(z, x) is not defined in Section 3.
4. The experimental setting, when a diversity is evaluated by doing traversals by +-6,8,10 std. looks strange for me.
Such points will be never sampled from the noise. 
5. Where did hyperparameters from Appendix B come from? For example, Roth et al, 2023 provided a grid search for them. As far as rival methods are concerned, you can take hyperparameters from original papers (but in this case original training pipeline and architectures must be also used). If the hyperparameters for rival methods are selected arbitrary, experimental results are not valid!
6. Figure 1 is not convincing. For example, row 3 for alpha-TCVAE, contains an image with a defect: non-round violet border. 
High diversity obviously can be achieved by generating wrong images.

### Questions
1. In Figure 2, what does green horizontal line mean?
2. In Figure 3, you write that "The scores for the images of our model, α-TCVAE, are consistently better than baseline VAE models (lower FID is better), and only slightly worse than StyleGAN."
But from Figure 3, I see that blue circles (sampling from "noise") for all VAE-based models have significantly higher FID than StyleGAN. 
Probably, you compare traversal from VAE and "noise" samples from StyleGAN, but it seems not fair to me.
3. How the matrix for the Vendi score is formed?
4. FID from "traversals" image generation is much lower than from straightforward generation from noise. Do you have an explanation?
Also, it is interesting to compare VAE models via Precision/Recall (Kynkäänniemi, T., Karras, T., Laine, S., Lehtinen, J., & Aila, T. (2019). Improved precision and recall metric for assessing generative models. Advances in Neural Information Processing Systems, 32.)

**post rebuttal**. Most of my questions have been addressed, authors even did some additional computations. So, I am raising my score.

### Soundness
2 fair

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
In this paper, the author introduce α-TCVAE, a variational autoencoder optimized using a new total correlation (TC) lower bound that both maximizes disentanglement and latent variables informativeness. The new TC bound is grounded in information theory and can be reduced to a convex combination of the known VIB and CEB terms. Moreover, the paper also presents quantitative analyses and correlation studies which support the idea that smaller latent domains lead to better generative capabilities and diversity.

### Strengths
- The total correlation between x and z has not been previously used in disentangled representation learning, although similar concepts exist, such as mutual information in InfoGAN.
- The paper  first paper propose to discuss diversity in the context of disentangled representation learning, drawing from previous research in GANs (e.g., FID).
- The paper considers reinforcement learning as a downstream task for disentangled representations.

### Weaknesses
 - The paper proposes maximizing an upper bound of the correlation between x and z for disentanglement, but β-TCVAE penalizes total correlation between different z's. The connection between these two approaches is unclear, and the use of α-TCVAE may be misleading. If there is a connection, it should be further clarified. Specifically, the paper needs to clarify how maximizing the total correlation between x and z, as opposed to minimizing the total correlation between latent dimensions, leads to disentanglement. The current explanation is insufficient to justify this approach.
- The authors should explain why maximizing the upper bound of the correlation between x and z promotes disentanglement, and why increasing variable informativeness enhances diversity. The paper lacks a clear theoretical justification for these claims. The connection between the proposed objective function and the desired properties of disentanglement and diversity needs to be rigorously established, potentially through information-theoretic arguments.
- The traversal results shown in Appendix Figure 12 are poor in terms of both disentanglement and generation quality. Additionally, the paper lacks traversal images results for real world natural images (not MPI3D-real), such as CelebA. The absence of results on standard datasets like CelebA limits the generalizability of the findings. The quality of the traversals on MPI3D-real is also concerning, suggesting potential issues with the model's ability to learn disentangled representations.
- The paper should provide an analysis of the sensitivity of the $\alpha$ parameter. Without this analysis, it is difficult to understand how the performance of the model is affected by the choice of this hyperparameter. The lack of sensitivity analysis makes it difficult to assess the robustness of the proposed method.
- If the answer to weakness 1 is the latter, it seems that this work is relatively incremental, as it only adds a conditional TC term to the β-TCVAE. Considering this point, the authors should clarify it in the rebuttal stage. If the core contribution is simply adding a conditional total correlation term, the novelty of the work is questionable, and this should be explicitly addressed.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
From the perspective of information theory, this paper decomposes the Total Correlation term into two distinct bounds: the information bottleneck and the conditional entropy bottleneck. It assigns specific weights to these bounds to balance their influence. Furthermore, the authors evaluate their learning objective across multiple datasets.

### Strengths
- From an information theory perspective, the authors derive a lower bound of total correlation. They simultaneously address both the disentanglement and informativeness of the latent variable.
- The writing throughout the paper is lucid and well-structured, making it accessible for readers.
- The research showcases effectiveness by employing diverse evaluation metrics and testing their approach across various datasets.

### Weaknesses
 - The novelty is limited. Earlier research, referenced by the authors, already explored the decomposition of Total Correlation. The primary contribution seems to be the weighted combination of these two decompositions, which might appear incremental.
- They claim that the VIB term promotes compression of the latent representation, and the CEB term promotes balance between the information contained in each latent dimension. However, the paper lacks a clear illustration of:
  - How the information bottleneck correlates with disentanglement.
  - The connection between diversity and the conditional entropy bottleneck.
- A more profound point of contention is the origin of the VIB and the CEB terms. Both terms are derived from the same TC term, yet they supposedly represent different characteristics. The paper doesn't sufficiently elucidate why this is the case, which could have made for a compelling discussion.

### Questions
- How does the parameter alpha influence the results?
- What about the traversal outcomes for the CelebA dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
