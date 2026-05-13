# Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Conditional Flow Matching (CFM), a simulation-free method for training continuous normalizing flows, provides an efficient alternative to diffusion models for key tasks like image and video generation. The performance of CFM in solving these tasks depends on the way data is coupled with noise. A recent approach uses minibatch optimal transport (OT) to reassign noise-data pairs in each training step to streamline sampling trajectories and thus accelerate inference. However, its optimization is restricted to individual minibatches, limiting its effectiveness on large datasets. To address this shortcoming, we introduce LOOM-CFM (Looking Out Of Minibatch-CFM), a novel method to extend the scope of minibatch OT by preserving and optimizing these assignments across minibatches over training time. Our approach demonstrates consistent improvements in the sampling speed-quality trade-off across multiple datasets. LOOM-CFM also enhances distillation initialization and supports high-resolution synthesis in latent space training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work investigates coupling methods for drawing paired samples of data and noise to during the training of Conditional Flow Matching (CFM) models to improve model performance. In particular, well-chosen coupling during training can make sampling paths straighter at inference time so that generation requires fewer model evaluations. Methods for achieving such a coupling are known but prohibitively expensive for large training datasets. Prior work performed the coupling only within a minibatch for Gaussian noise drawn at each step. This work improves upon this idea by using persistent noise samples whose pairings with data are gradually refined. Initially, one noise sample is drawn for each data sample at random. In each minibatch, noise and data are drawn together, and data-noise pairs are reassigned according to an efficient optimal pairing algorithm acting on the small minibatch. These new pairs are used to update the model, after which the pairs are stored until the data sample is revisited and pairings recomputed within the new batch. Multiple noise caches are used for small-scale datasets to prevent overfitting. Experimental results show significant improvement over the baseline independent coupling method and superior performance to other coupling methods, especially in the low-step regime.

### Strengths
* This paper has a clear focus and motivation. Coupling methods with little computational cost that can improve the performance of CFMs, especially in the low-step regime, have the potential to become widely adopted. The proposed method is scalable and the extra I/O cost seems reasonable.
* The method is clearly presented and natural. While the method remains unable to guarantee an optimal pairing (a fact which holds for any method which does not scan the entire dataset at once), it provides a richer pairing mechanism than previous minibatch approaches and remains low cost.
* The experimental results show significant improvement over the original coupling, along with strong performance relative to other few-step generation methods, and in particular among other coupling approaches.

### Weaknesses
 * It seems somewhat limited to use only a fixed set of pre-sampled noise to train the model, in contrast to the typical approach of drawing fresh noise at every iteration. I would guess that the need for using caching for small datasets is related to the fact that the noise is not refreshed, leaving the method with a bit of a loose end. The work claims that in practice this is not an issue for large enough datasets. Nonetheless, I am curious if it is possible to define a variant of the method where noise is refreshed, eliminating the need for caches for smaller datasets.
* While the work maintains a strong focus on an important problem, actual method is fairly straightforward and heavily influence by prior work. This is not a major drawback in my view as long as the benefits that are presented in the experimental section are accurate and reproducible, because the proposed method is very easy to adopt.

### Questions
* How scalable is this approach? Could it be used datasets much larger than ImageNet, such as LAION-5B?
* Is the use of fixed noise an issue? Could there be a benefit from gradually refreshing the noise?

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
This paper introduced LOOM-CFM to extend the scope of minibatch OT by proposing a novel iterative algorithm to optimize the global data-noise assignments of minibatch OT. This method has consistent improvements in the sampling speed-quality trade-off and also helps enhance distillation initialization of rectified flow and supports high-resolution synthesis in latent space training.

### Strengths
This paper introduces an iterative approach to more accurately approximate the global optimal assignment between noise and data samples, resulting in a more precise estimation of the global OT plan compared to minibatch-CFM. It also present a convergence analysis of LOOM-CFM.

### Weaknesses
1. The paper lacks an analysis of the training time overhead and convergence rate of LOOM-CFM compared to minibatch-CFM. Additionally, while finite convergence is intuitive, providing a detailed analysis of the convergence rate is crucial—especially to understand the scalability of this method for large-scale text-to-image (T2I) and text-to-video (T2V) diffusion model training. The current analysis does not sufficiently address the practical implications of the iterative optimization, particularly concerning the computational cost associated with recomputing and applying the assignments across multiple epochs. A more thorough investigation into how the overhead scales with dataset size and dimensionality is needed, as the reported 24% increase in training time on CIFAR-10 may become a more significant bottleneck for larger, more complex datasets.

2. While the use of multiple noise caches empirically helps reduce overfitting, the one-to-many correspondence may affect the properties of probability flow. It would be valuable if the authors could provide further explanation or analysis on how multiple noise caches might or might not influence the probability flow. Specifically, the paper should explore whether the duplication of data points through multiple noise caches introduces any bias in the learned vector field, and how this might impact the quality of the generated samples. It is also unclear if this approach maintains the desired properties of the optimal transport plan, and a more rigorous analysis is needed to justify this design choice.

### Questions
See weakness

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
This paper proposes an improved method (LOOM) for computing the minibatch optimal transport coupling used to train conditional flow matching models. Unlike previous OT-CFM approaches which throw away the minibatch OT coupling after each neural net update, LOOM uses minibatch OT coupling to update the global coupling between training datasets.

### Strengths
**Originality** : this paper introduces an alternative (LOOM) to the Hungarian algorithm or Sinkhorn for approximating the OT coupling between two empirical measures. LOOM is suitable for conditional flow matching / minibatch flow matching in the sense that it uses local OT coupling to improve the global OT coupling.

**Clarity** : method and experiment results are clearly presented. I had no problem following the writing.

**Quality** : proposed method is supported with both theory and experiments on CIFAR10, ImageNet-32&64, and FFHQ 256x256. The experiment results support the authors' claim that conditional flow matching with LOOM yields faster flow models.

**Significance** : the paper takes a step towards scaling up OT minibatch flow matching.

### Weaknesses
 **Weak Performance** : the only weakness of the paper stopping me from giving Accept is the weak empirical performance of the proposed method compared to relevant baselines such as [1] and [2] (which also happen to be missing from Section 4). For instance, [1] achieves 1.97 FID on CIFAR10 with 35 NFEs, whereas LOOM achieves 4.41 FID with 134 NFEs. On ImageNet-64, [2] achieves around 1.4 FID with 63 NFEs while LOOM yields 2.75 FID with 133 NFEs. The performance gap is significant, especially considering the higher number of NFEs required by LOOM to achieve these results. This suggests that while LOOM might offer a novel approach to minibatch optimal transport, it does not yet translate to state-of-the-art performance in terms of sample quality or computational efficiency. The substantial difference in FID scores and NFE counts raises concerns about the practical applicability of the method in its current form. The lack of a direct comparison in Section 4 with these specific baselines further obscures the relative strengths and weaknesses of LOOM.

### Questions
**Q1** : to what degree does LOOM accelerate convergence (in terms of number of model updates) compared to, e.g., independent coupling, Hungarian OT coupling, or Sinkhorn OT coupling?

### Soundness
3

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
4

### Summary
The paper proposes a novel method for reassigning noise-data, which overcomes the limitations of minibatch OT reassigning. This method allows noise-data pairing beyond the confines of minibatch, reducing the curvature of the sampling trajectory and thereby accelerating the adoption process.

### Strengths
The paper presents a novel approach that overcomes the limitations of minibatch optimal transport (OT) by retaining coupling information within minibatches, thus facilitating the transfer of coupling information across minibatches. This advancement enables the construction of noise-data pairings that are more closely aligned with the global optimal transport framework. The proposed LOOM-CFM offers a new solution for developing superior noise-data couplings in the training of continuous flow models (CFMs). This work contributes to the application of computationally complex OT calculations in high-dimensional spaces within generative models, providing insights and references for future research in this area. Besides, the paper is well-written.

### Weaknesses
While LOOM-CFM demonstrates superior performance in unconditional image generation tasks compared to methods like minibatch OT, its approach of updating global pairings through optimal pairings within minibatches may not be very efficient. There exists a vast solution space for potential noise-data pairings, which poses a significant challenge. For instance, in the CIFAR-10 dataset, even when using just one cache, there are around $50000!$ possible noise-data pairing configurations. However, with a batch size of 128, each minibatch can explore a maximum of only $128!$ coupling configurations at a time. Consequently, the number of training steps required to identify the optimal pairing becomes substantially large. Furthermore, the method's reliance on local minibatch optimizations to approximate a global optimal transport plan could lead to suboptimal solutions, particularly when the underlying data manifold is complex or highly non-convex. The iterative refinement process, while improving upon minibatch OT, may still converge to a local minimum far from the true global optimum, especially given the high dimensionality of the noise and data spaces.

### Questions
1. From the comparison of results between LOOM-CFM with 4 caches + reflow and LOOM-CFM with 4 caches, it can be observed that there are still many intersections in the noise-data coupling generated by LOOM-CFM. This indirectly reflects the low efficiency of the algorithm mentioned in the weaknesses. Therefore, does the issue of low efficiency in continuously exploring the global optimal pairing using minibatches impose demanding requirements on the number of training steps and training time? Could you provide the time required for training the model?
2. The meaning of the subscript $j$ in Equation 9 does not seem very clear. Could you please provide a clearer explanation?

### Soundness
3

### Presentation
3

### Contribution
3
