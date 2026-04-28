# Optimizing Learning for Robust Hyperbolic Deep Learning in Computer Vision

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 3, 5, 6, 5

## Abstract
Hyperbolic deep learning has become a growing research direction in computer vision for the unique properties afforded by the alternate embedding space. The negative curvature and exponentially growing distance metric provide a natural framework for capturing hierarchical relationships between datapoints and allowing for finer separability between their embeddings. However, these methods are still computationally expensive and prone to instability, especially when attempting to learn the negative curvature that best suits the task and the data. Current Riemannian optimizers do not account for changes in the manifold which greatly harms performance and forces lower learning rates to minimize projection errors. Our paper focuses on curvature learning by introducing an improved schema for popular learning algorithms and providing a novel normalization approach to constrain embeddings within the variable representative radius of the manifold. Additionally, we introduce a novel formulation for Riemannian AdamW, and alternative hybrid encoder techniques and foundational formulations for current convolutional hyperbolic operations, greatly reducing the computational penalty of the hyperbolic embedding space. Our approach demonstrates consistent performance improvements across both direct classification and hierarchical metric learning tasks while allowing for larger hyperbolic models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose several methods to improve learning in hyperbolic space: a more principled way to learn the curvature as a parameter, a Riemannian version of AdamW, a maximum distance rescaling function that allows the usage of fp16 precision, and a more efficient hyperbolic convolutional layer. Experiments are conducted on the hierarchical metric learning problem, image classification, and image generation with a VAE architecture.

### Strengths
Proposes a variety of new techniques to improve hyperbolic learning, including a Riemannian version of AdamW, a more principled curvature learning algorithm, a max rescaling algorithm for better numerical stability, and new efficient hyperbolic convolution.

### Weaknesses
The use of the proposed Riemannian AdamW algorithm is not well-supported, as it is only used in the hierarchical metric learning experiment, there is no ablation on using Riemannian AdamW, and there is no theoretical justification.

It isn't clear whether the proposed Lorentz-Core Bottleneck Block was used for any of the experiments and no ablation study is done on this component. 

Improvements using this method either barely improves is comparable, or is slightly worse than the proposed baselines in hierarchical metric learning task and classification tasks (Tables 1, 2, 3). 

Minor point: In Table 1, some of the numbers for the proposed method (LHIER) are bolded despite not being better than the baseline numbers.

### Questions
1. Which experiments was the Lorentz-Core Bottleneck Block used in? And are there ablations showing the effectiveness of the proposed block?
2. Is it possible to compare Riemannian AdamW to Riemannian Adam or Riemannian SGD?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper extends the AdamW optimizer to Riemannian manifolds and proposes a method for curvature optimization and a Riemannian convolutional layer. Despite extensive experiments, the approach lacks theoretical insights, such as the rationality of the proposed several blocks.

### Strengths
1. Extension of several existing Lorentz blocks to Riemannian Setting.

### Weaknesses
1. Generalizing Adam into AdamW is straightforward. This can be readily done by the Riemannian operators at hand.

2. In Riemannian optimization, usually use retractions and vector transport instead of exp and Levi-Civita transport. This has become a common technique. The reason why the authors focus on the expensive exp and LC trans is not clear.

3. As for the mentioned Kim et al. (2023), it is more generally called trivilization. One of the biggest benefits is the direct application of Euclidean optimizer. So, the missing trivialized AdamW makes this work incomplete.

4. The key ingredients in L170-185 for the curvature optimization are confusing. We can post-optimize K and transport every data into the new space via tangent space. so, why can we not do prior-optimize K and post-transport similarly, by tangent space? A more important question is why should we bother to transport data, esp manifold data. Why can we not view the manifold data unchanged? As doing the transformation by single tangent space is clearly just an expedient, just as no transformation. if the authors want to show the benefits of post-K-and-transformation, the authors should show some theoretical analysis of which properties have been maintained or respected by the proposed methods.

5. The motivation and benefits of the convolutional layer are unclear. Except for ensuring the output as the L space, which geometric properties does the convolutional layer respect? Does the proposed conv layer have properties such as equivariance [2]?

6. Experiments should be done on large datasets, as the proposed method is targeted to the CV and most of the experiments are on small datasets.

7. Finally, does the proposed RAdamW and curvature optimization have a better theoretical guarantee than the existing ones?

Other minor comments:
Some notations lack clarity or rigorousness and expressions lack motivation:

- $v_i$​​ in L centroid should lie in simplex
- L 216-219,  what does the L case mean? does it mean the centroid between $\theta ^{t-1}$ and $\bar{0}$​​? why is it formulated in this way is not clear.
- $x_t$ in L 129.
- the notation for the Stiefel manifold is quite exclusive.
- what is LorentzBoost in Eq. (5)
- why centroid is $(\sqrt{K}, 0)$. Does it come from the hom space or mimicking some aspect of the Euc space?

### Questions
1. in the experiments, is the K identical across layers or different depending on the layer?



1. Trivializations for Gradient-Based Optimization on Manifolds
2. ManifoldNet: A Deep Neural Network for Manifold-Valued Data With Applications

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper enhances hyperbolic deep learning for computer vision by introducing new methods to improve curvature learning and computational efficiency. Key contributions include a schema for Riemannian optimizers that handle manifold changes, a Riemannian AdamW optimizer, and a maximum distance rescaling function for stability. It also presents an efficient convolutional layer to reduce memory and runtime costs. These innovations boost performance in hierarchical metric learning and classification tasks, showing robustness even with lower precision.

### Strengths
The paper is original, introducing innovative methods like the Riemannian AdamW optimizer and distance rescaling for better curvature learning in hyperbolic deep learning. The quality is strong, backed by comprehensive experiments that show improved performance. It is clear, with structured explanations and detailed algorithms. Its significance lies in enhancing the stability and efficiency of hyperbolic models, making them more practical for computer vision.

### Weaknesses
The atuhor failed to provide the results in lartge dataset, like ImageNet 1000 or 100. It will hinder the generosity of the proposed method. The implementation details is too little, like the hyperparameters.

### Questions
Could the author explain why only run small datasets, is the computational cost too high for large datasets?

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
This paper introduces a new method for properly learning the curvature in a hyperbolic learning setting. Previous approaches simply update the curvature of the manifold(s) containing parameters without changing the parameters. This paper rescales the parameters according to the updated curvature of the manifold. Besides this contribution, the paper introduces a hyperbolic version of the AdamW optimizer, a maximum distance rescaling function and a more efficient convolutional layer. The effect of these new proposals is shown through a number of experiments on hierarchical metric learning, image classification, VAE image generation and a number of ablations.

### Strengths
The paper addresses an important issue, namely the fact that all previous hyperbolic learning methods that use a learnable curvature ignore the parameters when performing the curvature update, potentially leading to numerical instability. The proposed approach for dealing with this issue seems straightforward and effective. The other contributions are also quite interesting and together form a nice contribution to hyperbolic learning.

The experiments show that the proposed methods indeed lead to a fairly significant improvement compared to existing methods.

### Weaknesses
While the ideas behind the paper are great, the presentation of some of these is currently rather unclear. There are also many notational inconsistencies, typos and missing details, which together make the paper (especially the method) difficult to follow and probably impossible to reproduce. Some of the contributions are also missing sufficient motivation in my opinion. Therefore, I think the paper needs some significant revisions before it can be accepted. I will list some of my main concerns here:

Optimizers for learned curvatures:
1. Algorithm 1 is a bit cluttered, making it hard to read. It might be better to just mention the expmap, logmap and PT without giving the full formulations. The formulations of these mappings are already given in the background, so they can easily be substituted if needed.

Maximum distance scaling:
1. For $||x_s|| \gg K$, $x_t \approx ||x_s||$ and the approximation error for float64 is less than $5 * 10^{-9}$. Why can we not simply ignore this rounding error? Why does it lead to problems?
2. Commonly used libraries such as geoopt already perform projection onto the Poincaré ball and hyperboloid after many operations. Why is this projection not enough for numerical stability?
3. I understand that the operation is mapping the input to the tangent space, scaling and mapping back onto the manifold. However, I do not precisely understand where the scaling term is coming from. What exactly is it supposed to achieve? The motivation appears to be coming from the limit that is given after equation 3. However, it is unclear to me how this limit is solved. I think that a visualization of the operations in terms of $|\mathbf{x}||$ versus $|\mathbf{x}_{rescaled}||$ could be a useful aid to help explain this.
4. There are some notational inconsistencies and typos in this section:
    - $D(x, \mathbf{\overline{0}})_{max}^K$ is introduced which hints at a dependency on $x$, but it is not clear what $x$ is in this context. Is this term not a constant? If it is, would it not be better to simply write $D\_{max}^K$?
    - There appear to be some $k$'s that should be $K$'s.
    - Later on a $D\_{0_{max}}^K$ appears, which I am guessing is denoting the same as the earlier $D(x, \mathbf{\overline{0}})_{max}^K$.
    - I guess it should be $||z\_{rescaled}||$ instead of $||z||\_{rescaled}$.
    - Some more small things.

Lorentz convolutional layer:
1. This section introduces a lot of technical stuff without really discussing or motivating it.
2. Lorentz transformations are not discussed in the background, but this section assumes the reader to be familiar with the details of both Lorentz boosts and rotations. The background should include a discussion on these transformations as well, since anyone not familiar with the Lorentz model will almost certainly not be familiar with Lorentz transformations.
3. A stiefel manifold requires $n' \leq n$ (with the notation of the paper). It is an empty set when this is not the case, so maybe it is best to focus on what the goal of the mapping is and not necessarily go into Stiefel manifolds.
4. It is unclear to me what the exact contributions are in this section and which parts are taken from other papers. I am also unsure about the advantages of this convolutional layer with respect to other convolutional layers. Were they originally not compatible with existing 2D convolution implementations? If so, why?
5. Some Caley transform is mentioned with a reference to a paper. As far as I know, within the context of matrices, a Cayley transform is a transformation of the form $Q = (I - A)(I + A)^{-1}$, where $A$ is some skew-symmetric matrix, which leads to a special orthogonal matrix $Q$. However, it is not explained how the skew-symmetric matrix $A$ is obtained, so it is unclear to me how the transform is being used. Additional details seem important for applying the method.

Experiments:
1. What are HECNN and HCNN? This should be clear from the text.
2. What is the curvature fixed to in the fixed curvature ablation?

I do believe that the proposed methods, especially the method for optimizing the curvature, are very interesting ideas that should be shared. Therefore, if the authors address most of these issues by rewriting the method section to be more coherent, consistent and complete, then I am certainly willing to increase my score.

Some more small notes:
1. There's a mistake in the definition of $\mathcal{L}^n$. I think the squared Lorentzian norms should be equal to $-K$.
2. Equation 4 is missing brackets.
3. Text below equation 5 mentions 2 and 2, which should refer to equation 2 and algorithm 2, respectively, I think.

### Questions
Aside from my concerns listed above, I have several questions regarding additional experiments. I think that answering these could be beneficial to the paper, although in my opinion not strictly necessary.
1. If I understand correctly, then the encoder and the decoder each have their own learnable curvature currently. What happens if each layer is given its own learnable curvature? Does performance stay approximately similar or does it increase? Do the layers learn significantly different curvatures?
2. How expensive is the moving of the parameters that is performed in algorithm 1 compared to the usual parameter update that occurs? 
3. What happens when the curvature scheme is replaced by simply clipping the parameters to be within the representation radius of the new manifold?
4. In my experience, a learnable curvature is often helpful in stabilizing the loss a bit during training. Do the authors find this as well? If so, it might be nice to add a visualization of training curves somewhere (maybe the appendix).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a set of methods aimed at enhancing hyperbolic deep learning within the context of computer vision. The authors propose improvements to the current hyperbolic learning paradigms, such as introducing a novel Riemannian AdamW optimizer, a bounding method for stable hyperbolic optimization, and an efficient convolutional layer that minimizes computational overhead. The paper demonstrates empirical improvements on tasks including hierarchical metric learning and image classification and demonstrates the improved results after applying their improvements.

### Strengths
The introduced components to hyperbolic deep learning are indeed novel, and some of the contributions have some clever ways to work around difficulties in the Riemannian setting, such as the centroid trick for AdamW. The empirical evaluation is extensive and compares against a good number of baselines. It is also nice, especially in the Riemannian optimization community, to see that the authors also consider computational challenges and propose solutions that are efficient and work well with modern hardware.

### Weaknesses
 (roughly ordered by importance)

- **Insufficient analysis of AdamW in Riemannian context.** The paper draws analogies to AdamW in the Riemannian optimization context, and while the adaptation is interesting, it is fundamentally different than a direct Riemannian AdamW. The adaptation involves changes that are not fully explored or justified, and it remains unclear how closely the benefits of AdamW translate to hyperbolic settings. Specifically, the paper does not delve into the implications of using a centroid-based update for the momentum and variance terms, which deviates from the standard Riemannian Adam approach that would involve parallel transport of these terms. This raises questions about the convergence properties and stability of the proposed method, and how it compares to a true Riemannian AdamW implementation. A more detailed analysis, perhaps including a comparison to a more direct Riemannian adaptation of AdamW, is necessary to fully validate this approach.

- **Marginal experimental improvements.** The reported improvements in performance across different tasks are generally quite marginal. In most settings, the proposed approaches show only slight gains over existing methods, which raises questions regarding the significance of these contributions. For example, the gains in image classification are not substantial enough to justify the added complexity of the proposed methods. The self-ablations also show very marginal improvements with each other, not giving insight into the individual role of each component. This makes it difficult to assess the practical value of each individual modification and whether the overall performance gain is worth the additional computational overhead.

- **Lack of theoretical insights.** The paper largely presents itself as an empirical collection of modifications to existing hyperbolic optimization methods. However, there is a lack of rigorous theoretical backing for these modifications. For instance, the proposed bounding method lacks a theoretical justification for its effectiveness, and it's unclear how it affects the optimization landscape. Without theoretical insights, it is difficult to understand the underlying mechanisms that drive the observed improvements and to generalize these methods to other settings. A more detailed theoretical analysis is needed to provide a solid foundation for the proposed modifications and to guide future research in this area.

### Questions
1. Are there any theorems about any of the proposed modifications that the authors could provide and give a proof sketch for, that highlight the true value of the improvements?

2. How does the proposed maximum distance rescaling function compare against simpler solutions, such as gradient clipping or norm bounding, in terms of both stability and performance? What drove you all to your particular design choices?

3. Can the authors discuss the practical scenarios where these improvements might be crucial (rather than incremental changes), and how these methods contribute significantly beyond existing alternatives?

### Soundness
3

### Presentation
3

### Contribution
2
