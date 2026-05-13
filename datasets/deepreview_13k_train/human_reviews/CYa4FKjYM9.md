# Enhancing Optimizer Stability: Momentum Adaptation of NGN Step-size

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Modern optimization algorithms that incorporate momentum and adaptive step-size offer improved performance in various challenging Deep Learning tasks. However, their effectiveness is often highly sensitive to the choice of hyper-parameters, especially the learning rate.  Tuning these parameters is often difficult, resource-intensive, and time-consuming. State-of-the-art optimization algorithms incorporating momentum and adaptive step size are the algorithms of choice in several challenging Deep Learning domains. However, their effectiveness is frequently dependent on selecting the right hyper-parameters, especially the learning rate. Therefore, recent efforts have been directed toward enhancing the stability of optimizers across a wide range of hyper-parameter choices (Schaipp et al., 2024). In this paper, we introduce an algorithm that matches the performance of state-of-the-art optimizers while improving stability through a novel adaptation of the NGN step-size method (Orvieto & Xiao, 2024). Specifically, we propose a momentum-based version (NGN-M) that attains the standard convergence rate of $\mathcal{O}(1/\sqrt{K})$ under common assumptions, without the need for interpolation condition or assumptions of bounded stochastic gradients or iterates, in contrast to previous approaches. Additionally, we empirically demonstrate that the combination of the NGN step-size with momentum results in high robustness while delivering performance that is comparable to or surpasses other state-of-the-art optimizers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new optimization algorithm, NGN-M, which combines the NGN step size with momentum and develops NGN-MD, a coordinate-wise diagonal preconditioner version. The work aims to improve robustness in hyperparameter selection while maintaining state-of-the-art performance. The authors provide both theoretical and empirical evidence supporting the algorithm’s stability and convergence。

### Strengths
1. It is a natural and reasonable idea to extend the NGN method to the momentum setting. The authors achieved good empirical results and provided theoretical convergence guarantees.
2. The authors also introduced a diagonal step-size version, enriching the paper's content. The comparative experiments are comprehensive which improves over previous work.

### Weaknesses
1. Since the authors claim that the NGN-M algorithm can achieve better stability with larger step sizes, I would expect that the effective step size $\gamma_k$ during training dynamics would maintain a larger value, not just that the step size hyperparameter can be set larger. If it is merely the latter, wouldn't this imply a false sense of stability? In Figures 4 and 5, I do not see NGN-M demonstrating a consistently larger effective learning rate during training. If the observed stability is merely due to using a smaller effective step size relative to the hyperparameter, what is the practical significance of this stability?

2. I find the argument presented in Section 5.5 lacking rigor. The authors state, "Increasing the stepsize hyper-parameter of NGN-M leads to...," but this explanation is imprecise and somewhat misleading. The phenomenon of increasing the step size hyperparameter leading to convergence to flatter minima (i.e., with smaller eigenvalues of the loss Hessian) has already been explained by the EOS literature (see https://arxiv.org/abs/2103.00065). This body of work indicates that increasing the step size within a reasonable range generally leads to lower sharpness (i.e., reduced top eigenvalue) during neural network training. It is unclear if the authors' claim aligns with this well-known phenomenon, and they should reconsider this explanation.	

Minor issues: I noticed that some notations are not precise.
1.	Ver.1 in Section 3.1 appears to have a typo. The term $\gamma^k$ in the lines 179 of the formula should be removed.
2.	I suggest the authors align the notation for iteration indices. Are the $\gamma$ values in lines 179 and 180 referring to the same iteration?

### Questions
1.	In addition to the questions posed in the Weaknesses1, I find that the comparison between NGN-MD and methods using a constant step size may not be entirely fair. Although the authors include a learning rate schedule in the comparative experiments after Section 5.3, it is evident that in Section 5.3, as shown in Figures 3 and 4, the advantage of NGN-MD becomes less pronounced compared to earlier experiments. I would be interested in seeing the stability comparisons in Sections 5.1 and 5.2 against classical optimizers that use warmup or learning rate schedules.

2.	Figure 16 is hard to understand. Does the loss along the top 2 eigenvectors truly represent the landscape along the update directions (such as negative gradient or various momentum directions)? And would a comparison under the same effective learning rate

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
3

### Summary
This paper builds upon a variant of the Polyak step-size called NGN (Non-negative Gauss-Newton) and offers two main variants.

The first algorithm combines NGN with momentum, resulting in the NGN-M algorithm. The authors theoretically prove that NGN-M achieves a convergence rate of $O(1/\sqrt{K})$ in the convex setting, without requiring assumptions of bounded gradients or interpolation.

The second variant is inspired by prevalent coordinate-wise adaptive optimization methods like Adam for training neural networks and introduces an NGN for coordinate-wise step-size configuration in the NGN-D algorithm. The authors show that NGN-D converges with a rate of $O(1/\sqrt{K})$ for convex and smooth functions with bounded noise variance. They use this coordinate-wise variant, NGN-D, with momentum to create the NGN-MD algorithm. When used with RMSprop preconditioning, they refer to it as NGN-MDv1, otherwise NGN-MDv2.

Empirically, NGN-M and NGN-MD achieve comparable performance with baselines and demonstrate enhanced robustness to step-size selection in experiments on CIFAR10, CIFAR100, ResNet18, and ViT.

### Strengths
Developing new adaptive optimization methods that match Adam’s performance while providing additional stability and convergence guarantees for certain problem classes represents a significant contribution to the current deep learning literature.

### Weaknesses
These are relatively minor issues. Overall, I believe the paper would benefit from an additional pass for writing clarity.

- The difference between NGN-MDv1 and NGN-MDv2 is not explained in text, and it is confusing. I would generally prefer if you treated NGN-MDv1 and NGN-MDv2 similarly to how you approached ver1 and ver2 of NGN-M: by experimenting to determine which performs better and then using that version consistently throughout the paper. 

- The organization of the NGN-D section in Section 3.3, along with Algorithm 2, could be improved. For example, in Equation 3, you already have $\gamma_k$ multiplied by $\Sigma$, and then you choose $\Sigma^{-1}_j = \gamma^j$, which results in a squared $\gamma_k$ as the step-size. Based on Algorithm 2, I don’t think this is what you intended. The description of how the coordinate-wise step-size is derived and applied is unclear, making it difficult to understand the precise update rule for NGN-D and its relation to NGN-MDv2.

- Figure 5 could also be improved: please add method names more clearly. Could you also compare the effective step-size of Adam? I would be more interested in that comparison than in one with MoMo, as MoMo is not shown in the ViT experiments. In that experiment, you compare MoMo-Adam, Adam, and NGN-MDv1, so it would make more sense to focus on those methods.

### Questions
- Is it obvious that all NGN-based methods perform better than SPS (stochastic Polyak step-size)? If not, did you consider adding it to the baselines for the NGN-M algorithm?

- Your analysis of NGN-M in Theorem 1 notably avoids the need for the interpolation condition, which is often a key assumption for proving convergence in stochastic Polyak step-size methods. Given that interpolation occurs in overparameterized neural networks, I found it a reasonable assumption. Could you elaborate on the specific mechanisms that enable the proof of convergence rates without relying on the interpolation condition?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces NGN-M, an optimizer that combines NGN step-size with momentum, achieving robust, state-of-the-art performance with less sensitivity to step-size tuning. Theoretical analysis shows convergence comparable to SGDM in convex settings, and experiments on CIFAR and ImageNet validate its effectiveness and stability across varying hyperparameters. Two additional variants, NGN-D and NGN-MD, further extend its adaptability, making NGN-M a promising approach for stable, efficient optimization in deep learning.

### Strengths
1. **Enhanced Stability**: NGN-M addresses a key limitation in adaptive optimizers—sensitivity to learning rates—by combining momentum and NGN step-size. This stability improvement is backed by both theoretical and empirical results.
  
2. **Theoretical Contributions**: The authors provide rigorous theoretical analysis showing that NGN-M’s convergence rate matches that of SGDM in convex settings. This is a notable achievement since it removes the bounded gradients constraint common in other optimizers.

3. **Extensive Empirical Validation**: Results on diverse tasks, including ResNet and Vision Transformers on CIFAR datasets and ImageNet, demonstrate NGN-M’s robustness and competitive performance. Additionally, the optimizer performs well even at larger step sizes, which is uncommon among traditional optimizers.

### Weaknesses
1. **Limited Non-Convex Analysis**: While the authors focus on convex settings, optimizers like Adam are widely used in non-convex scenarios, such as deep networks. Addressing NGN-M’s performance under non-convex conditions would strengthen its applicability. Specifically, the paper could benefit from an analysis of convergence rates and stability guarantees when applied to problems exhibiting saddle points or local minima. Investigating the behavior of NGN-M in such scenarios, potentially through empirical studies on benchmark non-convex functions, would provide a more comprehensive understanding of its practical utility.

2. **Complexity of the NGN-MD Variant**: NGN-MD, which uses both momentum and diagonal preconditioning, can be computationally intensive due to additional matrix operations. In practice, this may pose challenges for large-scale applications, especially in memory-constrained environments. The concern is particularly relevant when considering the computation of the inverse of the diagonal preconditioner matrix and its multiplication with the gradient vector. A detailed complexity analysis comparing the per-iteration cost of NGN-MD against standard Adam, including memory footprint and computational overhead, would be highly beneficial.

3. **Lack of Comparison on NLP Tasks**: Although NGN-M shows promise in vision tasks, the paper could benefit from an expanded evaluation on NLP tasks, where optimizers like Adam and AdamW are dominant. The unique challenges posed by sequential data and the prevalence of coordinate-wise adaptive methods in NLP make this a crucial area for evaluation. Including experiments on tasks such as language modeling, machine translation, or text classification using benchmark datasets would provide valuable insights into NGN-M's broader applicability.

### Questions
As above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper’s main contribution is the development of an adaptive algorithm for the NGN step size, termed NGN-M, incorporating momentum to improve robustness in hyper-parameter selection. NGN-M addresses the sensitivity issues in hyper-parameter choices (specifically step-size). The authors provide a theoretical analysis, ensuring that the new adaptive momentum-based NGN (NGN-M) achieves a convergence rate of $O(1/\sqrt(K))$ under convex settings, and mention that this rate even without common assumptions like interpolation or bounded gradients. The authors not only propose the NGN-M but also introduce two variants—NGN-MD targeted at enhancing robustness in step size through a diagonal adaptation approach.

### Strengths
The robustness of the proposed NGN-M and NGN-MD, in dealing with a wide range of step sizes is a major strength. This is a practical advantage, as it reduces the need for extensive hyperparameter tuning. They compared their method clearly with other related methods in the literature in Table 1. They provided theorems that clearly state assumptions and convergence rates for their method. They justify that their assumption for theorem 1 is commonly made in the literature. They support their theoretical findings with experimental results(e.g., image and language models) highlighting NGN-M's performance's applicability and potential as a general-purpose optimizer.

### Weaknesses
There is a bounded variance assumption in Theorem 2 which may limit practical applicability in cases where these conditions do not hold (e.g. RL setting). 
However, I have not seen significant weaknesses in this paper. I should mention that I have not read the proofs in the appendix.

### Questions
Have you done any further exploration of the non-convex settings and NGN’s potential there?

### Soundness
3

### Presentation
3

### Contribution
3
