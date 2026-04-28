# DiSK: Differentially Private Optimizer with Simplified Kalman Filter for Noise Reduction

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Differential privacy (DP) offers a robust framework for safeguarding individual data privacy. To utilize DP in training modern machine learning models, differentially private optimizers have been widely used in recent years. A popular approach to privatize an optimizer is to clip the individual gradients and add sufficiently large noise to the clipped gradient. This approach led to the development of DP optimizers that have comparable performance with their non-private counterparts in fine-tuning tasks or in tasks with a small number of training parameters. However, a significant performance drop is observed when these optimizers are applied to large-scale training. This degradation stems from the substantial noise injection required to maintain DP, which disrupts the optimizer's dynamics.
This paper introduces \algname, a novel framework designed to significantly enhance the performance of DP optimizers. \algname \ employs Kalman filtering, a technique drawn from control and signal processing, to effectively denoise privatized gradients and generate progressively refined gradient estimations. To ensure practicality for large-scale training, we simplify the Kalman filtering process, minimizing its memory and computational demands.
We establish theoretical privacy-utility trade-off guarantees for \algname and demonstrate provable improvements over standard DP optimizers like DPSGD in terms of iteration complexity upper-bound.
Extensive experiments across diverse tasks, including vision tasks such as CIFAR-100 and ImageNet-1k and language fine-tuning tasks such as GLUE, E2E, and DART, validate the effectiveness of \algname.  The results showcase its ability to significantly improve the performance of DP optimizers, surpassing state-of-the-art results under the same privacy constraints on several benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces DiSK, a novel framework for enhancing differentially private (DP) optimizers by applying Kalman filtering to denoise privatized gradients, producing refined gradient estimates with reduced noise interference. By simplifying Kalman filtering for large-scale tasks, DiSK maintains efficiency and improves privacy-utility trade-offs, achieving significant performance gains over standard DP optimizers like DPSGD. Experimental results on vision and language tasks demonstrate DiSK's superiority under equivalent privacy constraints, achieving state-of-the-art performance across multiple benchmarks.

### Strengths
Empirical results are very strong and very significant. Computational costs (e.g. time/memory/parallelizability) of the method are quite good too. You mention this in theory, it may be good to make even a small empirical statement about this as well.

### Weaknesses
Why don’t people use Kalman filters for non-DP optimization? I don’t see why the same tricks you employed to not incur d^6 computational costs are not applicable to other non-private settings. 
This feels like an important consideration to understand for contextualizing the empirical claims made in this work

### Questions
I’m very impressed with these results and somewhat surprised about why they work so much better than existing methods. In developing new methods, or building on top of this, what parts of this method can be extended - what are they key things that differentiate this from existing methods that don’t work as well. This may seem a bit naive, but my question is effectively - based on how big of an improvement this algorithm produces, what should next steps focus on?

Comment: I did not go through the utility proofs in great detail and could have missed something there.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to use the Kalman filter for denoising gradient computation in differentially private optimization. Specifically, the Kalman filter views the gradient vector as the state and derives the system update equation based on the Taylor expansion of the gradient. The observation is then written as Gaussian perturbation of the gradient. However, naive incorporation of the Kalman filter involves computing the Hessian matrix, which is computationally infeasible for large models under DP constraints. To address the computational challenge, the authors proposed to use a simplified Kalman filter with noisy input, multiplicative observation noise, and diagonal covariance matrix. Theoretical analysis shows that the proposed algorithm satisfies $O\left(\sqrt{d/T}\right)$ convergence rate for smooth loss function with bounded per-sample gradient and bounded per-sample gradient variance, which has a constant factor improvement over DP-SGD under certain assumptions. Experiments validate the improvement of the proposed algorithm compared to DP-SGD and DP-Adam over a variety of DP vision and language tasks.

### Strengths
- The paper proposed an interesting way of viewing gradient update in differentially private training as a linear dynamics system. The proposed algorithm provides a novel and computationally efficient way of (approximately) incorporating the Kalman filter into DP training for denoising gradient.
- Extensive numerical experiments that validate the effectiveness of the proposed method.

### Weaknesses
 - The reason for the gain of the proposed denoising algorithm is not perfectly clear from the presentation -- could the authors elaborate more on (1) why does the Kalman filter (as described in Algorithm 2) effectively denoise the gradient observation? (E.g., what is the minimized objective under denoising), (2) what are the assumptions for the simplifications made in Algorithm 3 and why are the assumptions meaningful?
- The authors mention that the algorithm performs better than all SOTA methods, including the DP-FTRL algorithm. However, DP-FTRL is also effectively a gradient denoising method that is proved optimal in terms of l2 error for releasing linear queries (gradient estimation in the context). Consequently, it is not very clear why the proposed Kalman filter method would be beneficial compared to another denoising method, and how much the improvement is.
- In Algorithm 2, are $\mathbb{E}[C]$ and $H_t$ data-dependent? If so, does Algorithm 2 satisfy differential privacy?
- In Figure 2 (b), both the proposed algorithm KL-DPAdam and the baseline DP-Adam seem to achieve lower test accuracy than the SOTA results in De et al. 2022 Figure 1 (a). Does this contradict the claim that the proposed algorithm enables improvement compared to SOTA?

### Questions
1. In Algorithm 2, are $\mathbb{E}[C]$ and $H_t$ data-dependent? If so, does Algorithm 2 satisfy differential privacy?

2. In Figure 2 (b), both the proposed algorithm KL-DPAdam and the baseline DP-Adam seem to achieve lower test accuracy than the SOTA results in De et al. 2022 Figure 1 (a). Does this contradict the claim that the proposed algorithm enables improvement compared to SOTA?

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
2

### Summary
This paper proposes using a Kalman filter to enhance the privacy-accuracy trade-off of DP optimizers. While traditional Kalman filtering introduces significant computational and memory demands, the authors provide a simplified approach that reduces these costs while retaining its advantages. Theoretically, they show that their method achieves better iteration complexity than DP-SGD by a constant factor. Experimentally, their method outperforms DP-SGD on various datasets.

### Strengths
- This paper effectively applies Kalman filtering from control theory to improve DP optimization algorithms, presenting an interesting connection between DP optimization and control theory. 
- The algorithm improves upon the traditional Kalman filter and requires only a constant factor more space and computation than DP-SGD. 
- The method is versatile and can be integrated with various DP optimization techniques, not just DP-SGD.

### Weaknesses
 - The privacy analysis of algorithm 3 is not clear to me. Is it possible to express $\sigma_{DP}$ explicitly in terms of other variables? 

- While the conditions in Theorem 2 and Figure 8 offer some guidance on hyperparameter selection, the interactions between different hyperparameters ($\gamma, \epsilon$ and $\kappa$) remain complex and unclear, making practical hyperparameter tuning challenging.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes DiSK. DiSK is inspired by an application of a Kalman filter to the DP-SGD process. While the Kalman filter includes computationally intensive steps and requires knowledge of some unknown matrices, the simplification steps result in DP-SGD with two seemingly small changes. The first is that the clipped gradient is computed from an average of the gradient at two carefully chosen nearby points. The second is a momentum applied to the clipped gradient before being passed into an optimizer.

With these changes, the authors prove an upper bound on convergence rate. The provable constant in the upper bound for DiSK is smaller than the provable constant in the upper bound for vanilla SGD. Although this does not mean that the paper proved that DiSK has faster convergence (a claim that should be fixed), it does suggest that DiSK would converge faster. The analysis suggests that the pre-clipping averaging step may be the more important of the differences between DiSK and DP-SGD.

The paper also performs extensive experiments to compare against prior work to establish SOTA. It is not clear that the experiments match the deltas of the prior SOTA. I wasn't able to match the reported SOTA numbers to the papers that I checked, and some SOTA numbers are missing.

### Strengths
The paper reads very nicely. The authors take the reader through a tour of their intuition when explaining the algorithm. The theoretical results are also discussed nicely. Most papers simply present a Big-O result and switch topics. This paper explained the significance of the theorem conclusion.

I like the fact that the resulting algorithm is simple, increasing the chance of it being widely adopted.

The theoretical analysis is nice (theorem 2 and corollary 1) and shows that the provable convergence upper bound can be improved by a constant factor that depends on the model and data. It is not the same as claiming that faster convergence has been proved (Line 419, but that claim can be reworded to be accurate)

The model technique achieves state of the art in many settings (there is a small asterisk because I am not fully convinced yet, see below)..

### Weaknesses
There is a lot of ambiguity in the paper. Critical details are not discussed to ensure comparisons are apples to apples (see below).

There are discrepancies in the experiments and comparisons to prior SOTA (see below)

# Questions about ambiguity
- The way neighbors are defined has been left ambiguous. Are two datasets neighbors if adding/removing a record turns one into the other? Are two datasets neighbors if modifying one record turns one into another? The choice can result in significant differences in sensitivity and applicability of subsampling amplification results.

- What form of subsampling was used for the creation of minibatches. Simple random sample with a fixed size? Poisson sampling?

- What privacy accountant was used?

- Algorithms 1,2,3 should use parentheses to more clearly resolve the ambiguity of whether the noise term belongs
in the summation or outside.


# Experimental questions
- Did you match neighbor definitions in the comparisons to prior SOTA?

- Have you tried any of the privacy auditing frameworks (e.g., relatively recent NeurIPS papers) to check for possible errors? For example, depending on when you add noise and when you average over a batch, an error could easily appear to be SOTA and this is not uncommon in DP-SGD.

- The algorithms is 2 changes away from vanilla DP-SGD. The paper has hyperparmaeter tuning studies that are named ablation studies, but it does not have true ablation studies. There are 4 possible comparisons that can shed light on what is responsible for most of the apparent performance improvements. (1) vanilla dp-SGD (k=1, gamma=0); (2) weighted average before clipping, but no momentum on the gradient after clipping; (3) only momentum in the gradient and no pre-clipping averaging (gamma=0), (4) DiSK. 
    - Corollary 1 implies that gamma may be the more important parameter.

- The paper does not explain how hyperparameters were selected. Were they chosen based on validation data (good) or testing data (thus favoring any approach that has more hyperparameters).

- I tried to match up some of the SOTA numbers in the appendix as a spot check. 
    - Specifically, I looked at De et al. because they have a few prior SOTA numbers in the same place. I couldn't match their Imagenet numbers (32.4% top-1 accuracy to the 36.5 written in Appendix C5). 
   - I also noticed that some of the high CIFAR-10 training from scratch numbers in De et al. are completely missing from the Appendix.
   - It is not clear to me whether DiSK is appropriately compared to the prior SOTA. Do you match deltas? Do you match neighbor definitions and batch subsampling? Do you match privacy accountants?
   - Delta is a big difference maker, so you should put its numerical value(s) in every table.
   - Table 6 does not match imagenet for table 2.

# Other questions/comments
- What is that wacky green line in Figure 1?
- The paper uses C for too many different purposes. In some cases it is a clipping threshold, other times a constant in theoretical bounds, and other times a constant on properties of the data. This can get confusing even with subscripts.
- Line 121: where is the delta < 0.05 restriction coming from? If I am not mistaken, Definition 2 is all Balle & Wang and does not use the results from Dwork and Roth.
-Line 086-089: such comparisons are incomplete without specifying privacy parameters and adding citations.

### Questions
My initial rating is a weak reject that I am willing to raise with good responses to these questions.

# Questions about ambiguity
- The way neighbors are defined has been left ambiguous. Are two datasets neighbors if adding/removing a record turns one into the other? Are two datasets neighbors if modifying one record turns one into another? The choice can result in significant differences in sensitivity and applicability of subsampling amplification results.

- What form of subsampling was used for the creation of minibatches. Simple random sample with a fixed size? Poisson sampling?

- What privacy accountant was used?

- Algorithms 1,2,3 should use parentheses to more clearly resolve the ambiguity of whether the noise term belongs
in the summation or outside.


# Experimental questions
- Did you match neighbor definitions in the comparisons to prior SOTA?

- Have you tried any of the privacy auditing frameworks (e.g., relatively recent NeurIPS papers) to check for possible errors? For example, depending on when you add noise and when you average over a batch, an error could easily appear to be SOTA and this is not uncommon in DP-SGD.

- The algorithms is 2 changes away from vanilla DP-SGD. The paper has hyperparmaeter tuning studies that are named ablation studies, but it does not have true ablation studies. There are 4 possible comparisons that can shed light on what is responsible for most of the apparent performance improvements. (1) vanilla dp-SGD (k=1, gamma=0); (2) weighted average before clipping, but no momentum on the gradient after clipping; (3) only momentum in the gradient and no pre-clipping averaging (gamma=0), (4) DiSK. 
    - Corollary 1 implies that gamma may be the more important parameter.

- The paper does not explain how hyperparameters were selected. Were they chosen based on validation data (good) or testing data (thus favoring any approach that has more hyperparameters).

- I tried to match up some of the SOTA numbers in the appendix as a spot check. 
    - Specifically, I looked at De et al. because they have a few prior SOTA numbers in the same place. I couldn't match their Imagenet numbers (32.4% top-1 accuracy to the 36.5 written in Appendix C5). 
   - I also noticed that some of the high CIFAR-10 training from scratch numbers in De et al. are completely missing from the Appendix.
   - It is not clear to me whether DiSK is appropriately compared to the prior SOTA. Do you match deltas? Do you match neighbor definitions and batch subsampling? Do you match privacy accountants?
   - Delta is a big difference maker, so you should put its numerical value(s) in every table.
   - Table 6 does not match imagenet for table 2.

# Other questions/comments
- What is that wacky green line in Figure 1?
- The paper uses C for too many different purposes. In some cases it is a clipping threshold, other times a constant in theoretical bounds, and other times a constant on properties of the data. This can get confusing even with subscripts.
- Line 121: where is the delta < 0.05 restriction coming from? If I am not mistaken, Definition 2 is all Balle & Wang and does not use the results from Dwork and Roth.
-Line 086-089: such comparisons are incomplete without specifying privacy parameters and adding citations.

### Soundness
3

### Presentation
4

### Contribution
3
