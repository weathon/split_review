# Supervised Contrastive Block Disentanglement

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Real-world datasets often combine data collected under different experimental conditions. Although this yields larger datasets, it also introduces spurious correlations that make it difficult to accurately model the phenomena of interest. We address this by learning two blocks of latent variables to independently represent the phenomena of interest and the spurious correlations. The former are correlated with the target variable $y$ and invariant to the environment variable $e$, while the latter depend on $e$. The invariance of the phenomena of interest to $e$ is highly sought-after but difficult to achieve on real-world datasets. Our primary contribution is an algorithm called Supervised Contrastive Block Disentanglement (SCBD) that is highly effective at enforcing this invariance. It is based purely on supervised contrastive learning, and scales to real-world data better than existing approaches. We empirically validate SCBD on two challenging problems. The first is domain generalization, where we achieve strong performance on a synthetic dataset, as well as on Camelyon17-WILDS. SCBD introduces a single hyperparameter $\alpha$ that controls the degree of invariance to $e$. When we increase $\alpha$ to strengthen the degree of invariance, there is a monotonic improvement in out-of-distribution performance at the expense of in-distribution performance. The second is a scientific problem of batch correction. Here, we demonstrate the utility of SCBD by learning representations of single-cell perturbations from 26 million Optical Pooled Screening images that are nearly free of technical artifacts induced by the variation across wells.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method, named SCBD, for improving domain generalization and reducing spurious correlations and so-called batch effect among data collected in different environments, an common issue in datasets from experimental biology and clinical data. The proposed method mainly involves modeling the spurious correlation and true signal with two latent vectors and optimizing an objective involving four different parts: one for signals induced from the target labels, one for signals induced from the environment, one for the invariance amongst the environment, one for making the learning invariant to the environment, and a regularization loss on the generation. Empirically, the experiments were done on both small Colored MNIST and Camelyon17-WILDS. The results show their method is able to tune a parameter that exhibits a tradeoff between in-domain generalization and out-domain generalization.

### Strengths
The research problem of domain generalization is well-motivated. The introduction stating the issues with current methods for domain generalization/adaptation is clear, such as the batch effect issues in experimental biology. The writing of how the method works is straightforward to understand. In terms of novelty, the proposed method demonstrate that their method shows a monotonic trade-off between validation and test accuracy.  Their experiments also demonstrate their method can achieve the desired U-shape curved. Their method is also applied to biology-related datasets, which the authors have fairly introduced the datasets, making the problem well-contained. Overall, the problem is significant and very relevant to today’s research landscape.

### Weaknesses
The weaknesses are the following: 

1. The novelty of the work seems limited.  There already exist works that model signals from environment and target variables with two latent factors [1]. The paper also proposed a modification to iVAE, but as the authors mentioned, it was challenging to learn and the experiments do not yield significant improvements from other baselines. The core idea of disentangling environment-specific and environment-invariant features using latent variables is not new, and the specific implementation using supervised contrastive learning, while potentially effective, does not represent a fundamental shift in approach. The use of dot products for predicting environment labels, while clever, is an incremental improvement rather than a groundbreaking innovation. The method's reliance on a specific contrastive learning framework also limits its generalizability to other representation learning techniques.
2. While the experiment settings are well-design, each with a clear point that it is trying to demonstrate, having only one synthetic and one real-world dataset is not convincing enough that this method will work on most cases. And this is especially important, if the authors are trying to claim that their method can show a trade-off between validation and test accuracy in any general case. The authors also mentioned related works on domain generalization, but do not have any comparisons against state-of-the-art methods without block disentanglement or baseline against methods that do not handle out-of-distribution methods. The limited number of datasets, particularly the lack of diverse real-world datasets, makes it difficult to assess the robustness of the proposed method. The claim of a general trade-off between validation and test accuracy needs to be supported by more extensive empirical evidence across a wider range of datasets and problem settings. The absence of comparisons against strong baselines in domain generalization further weakens the empirical validation.
3. The visualizations of the experiment results are quite hard to compare. For example, in Figure 3 and 4, instead of having three separate plots, they could be one single plot, where different methods correspond to different colors, with SCBD being a range of colors (such as a rainbow spectrum). The way it’s currently presented, with the tick-labels being on different scales, makes it difficult if not impossible to compare. The use of separate plots with different scales hinders the ability to make direct comparisons between the performance of different methods. This makes it difficult to visually assess the claimed trade-off and the overall effectiveness of the proposed approach.
4. There is also a lack of ablation study. In particular, it seems the choice of dimension is important when learning latent factors but a study on how that affects learning and performance is not in the paper. The effects of batch size, learning rate, and regularization is also not shown. The absence of a systematic ablation study makes it difficult to understand the sensitivity of the method to different hyperparameters and design choices. The impact of the latent space dimensionality, batch size, learning rate, and regularization parameters on the performance of the model is not clear, which limits the reproducibility and practical applicability of the method.
5. (Minor) Typos on L781 “lossesl”

### Questions
1. Is there a difference between domain generalization and batch correction? It seems batch effect is just a case of domain generalization, but the paper is written right now that they are two issues.  
2. The trade-off between the validation and test accuracy is clear to me if there are only two environments. What is the intuition if there are more than two environments? Would there be multiple validation and test accuracy trade-off?

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
4

### Summary
This paper adapts & modifies the Supervised Contrast Learning algorithm (SCL; Khosla et al 2020) to solve domain generalization tasks. They use a loss that leverages similar ideas to SCL to block disentangle the representation into "content" and "style" blocks capturing the respective parts of the signal that are invariant and vary across domains. They have an explicit regularization term that encourages invariance across domains, and they show experimentally that increasing this hyperparameter leads to improved test set performance on the downstream tasks.

### Strengths
* I thought it was a very clearly written paper - the various terms in the loss function are well motivated from a probabilistic perspective, and clearly explained.
* I liked that it was a pragmatic take on an area that has a lot of nice theory but relatively little practical success, suggesting a focus on algorithms is important.
* The empirical results clearly demonstrate the role that the invariance loss plays.

### Weaknesses
 * Given that this is primarily a methods paper that is supported by empirical evidence, it would have been nice to see the empirical results replicated across all of WILDS. Aside from the compute requirements, I don't see what's stopping that?
* It seems likely that the paper could have been supported with theory that shows that the optimizer of the loss separates the representations (analogous to [Von Kügelgen et al., 2021]). It not essential, but it would have strengthened the paper.
* While I totally agree on the importance of having a well-defined validation set metric to optimize for, I wasn't convinced by the argument that you could simply maximize invariance subject to some constraint on accuracy loss (see questions below for why).

### Questions
- How do you choose the accuracy loss threshold? Surely both the rate of accuracy loss and the necessary invariance is domain specific? I.e. on some domains, you need a larger validation accuracy in order to get good test performance?
 - Could the same accuracy trade-off procedure not be applied to any domain generalization method with an invariance penalty? What is specific about this paper?
 - What is preventing you running this on all of WILDS?

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
3

### Summary
The paper proposes Supervised Contrastive Block Disentanglement (SCBD), using supervised contrastive learning to separate target phenomena from spurious correlations in data collected under different experimental conditions. The method introduces a single hyperparameter α to control invariance, and is evaluated on domain generalization and biological batch correction tasks.

The paper presents a novel approach to an important problem with promising results, particularly in biological applications. While the theoretical foundations could be stronger and there are some practical limitations, the method makes a clear contribution with its clean formulation and demonstrated utility on real-world data. The limitations around environment labels and decoder training are acknowledged by the authors and provide clear directions for future work. Thus, I recommend marginal acceptance.

### Strengths
- Novel application of supervised contrastive learning for disentanglement
- Clean formulation with interpretable hyperparameter
- Thorough experimental evaluation of the proposed method including relevant competing methods
- Convincing empirical results on biological batch correction applications

### Weaknesses
 - Limited theoretical analysis
    - No formal guarantees for disentanglement
    - Lacks justification for why contrastive learning should work better than alternatives
- Practical limitations (as also acknowledged by the authors)
    - Method requires known environment labels e, limiting broader applicability.
    - Poor reconstruction quality due to separate decoder training.
    - Worse CORUM results compared to iVAE with conditioning.

### Questions
1. How does computational cost compare to competing approaches?
2. Are there any failure modes of the method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes a new disentanglement method that is able to learn predictors (e.g., inferring a disease from histology images) that are invariant to spurious correlations arising from different environments in which the training was collected (e.g., histology images coming from different hospitals). The ansatz is most closely related to adversarial approaches in which representations are learnt that are invariant to the environment. Instead of an adversarial objective, however, this paper introduces an easier-to-optimise contrastive objective.

### Strengths
- Provides an interesting new ansatz to domain generalisation which might be easier to optimise than adversarial approaches to domain generalisation.
- It's encouraging to see that the regularisation parameter induces a clear trade-off between validation and test performance.
- The problem is still highly relevant, in particular in data-constrained settings.

### Weaknesses
 - The central weakness of the work is the experimental validation: the proposed method sits squarely in a long line of work on domain generalisation. However, the related benchmarks (e.g, DomainBed) are only mentioned, but there is almost no comparison to existing methods.
- The paper introduces it's own baseline based on variational approaches, but it's not clear to me why we would expect this baseline to learn invariances against the environment. The argument in lines 210 - 213 does not hold up because it's unclear why q_\phi(z_c | x) wouldn't learn to use environmental features in order to infer y (which it should to match p_\theta(z_c | y)). Specifically, the variational autoencoder (VAE) objective encourages the latent representation z_c to capture information relevant to reconstructing the input x. In the presence of spurious correlations, the most efficient way for the VAE to reconstruct x might be to encode environment-specific features into z_c, especially if these features are highly predictive of the input. The decoder, p_\theta(x | z_c, z_s), would then learn to rely on these spurious correlations, undermining the goal of learning environment-invariant representations.
- The relation to identifiability (lines 490 - 496) is not correct: identifiability doesn't make a causal argument as to how a feature y is extracted from the data - it's generally only applicable IID and to probe causality or feature reliance, one would need to probe OOD which identifiability (usually) says nothing about. The concept of identifiability, as typically used in the context of independent component analysis (ICA) or similar methods, focuses on whether the underlying latent factors can be uniquely recovered from the observed data under certain assumptions. However, this is a different question from whether these latent factors are causally related to the target variable y or are invariant to changes in the environment. Identifiability alone does not guarantee that the learned representations will generalize to out-of-distribution data. The paper seems to conflate identifiability with the ability to learn causal or invariant features, which is not correct.
- I found the theoretical outline in chapter 2 rather convoluted.

### Questions
- Why are you not following the typical protocol for evaluating domain generalization methods?
- Why do you create your own baseline VAE instead of comparing against the many existing works in domain generalisation?
- Why does the proposed VAE approach is expected to learn invariances against the environment?

### Soundness
2

### Presentation
3

### Contribution
2
