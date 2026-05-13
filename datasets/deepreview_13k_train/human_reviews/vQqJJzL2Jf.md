# Understanding and Mitigating Extrapolation Failures in Physics-Informed Neural Networks

- Decision: Reject
- Scores: 6, 8, 5, 5

## Abstract
Physics-informed Neural Networks (PINNs) have recently gained popularity in the scientific community due to their effective approximation of partial differential equations (PDEs) using deep neural networks. However, their application has been generally limited to interpolation scenarios, where predictions rely on inputs within the support of the training set. In real-world applications, extrapolation is often required, but the out of domain behavior of PINNs is understudied. In this paper, we provide a detailed investigation of PINNs' extrapolation behavior and provide evidence against several previously held assumptions: we study the effects of different model choices on extrapolation and find that once the model can achieve zero interpolation error, further increases in architecture size or in the number of points sampled have no effect on extrapolation behavior. We also show that for some PDEs, PINNs perform nearly as well in extrapolation as in interpolation. By analyzing the Fourier spectra of the solution functions, we characterize the PDEs that yield favorable extrapolation behavior, and show that the presence of high frequencies in the solution function is not to blame for poor extrapolation behavior. Finally, we propose a transfer learning-based strategy based on our Fourier results, which decreases extrapolation errors in PINNs by up to $82 \%$.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper debunks the idea that the poor extrapolation performance of PINNs are due to the presence of high frequency components. The paper demonstrates the poor extrapolation performance is due to a shift in the support of the Fourier spectrum, which they refer to as the spectral shift. The paper introduces a metric to quantify this shift using Weighted Wasserstein Fourier distance (WWF). The paper finally shows that a transfer-learning based technique which trains a multi-headed PINN can be effective in providing better extrapolation performances.

### Strengths
1. The paper is overall well-written and easy to follow.
2. Analyzing the poor extrapolation performance using spectral shifts is novel and interesting.
3. The proposed WWF metric can be a good evaluation tool to visualize the spectral shifts.

### Weaknesses
1. Although the paper provides some empirical evidence of correlations of spectral shifts and poor extrapolation performance, the paper lacks a theoretical understanding of why the hypothesized Spectral Shift is the root cause of extrapolation error. Specifically, the paper does not provide a mechanistic explanation of how the shift in the Fourier spectrum directly leads to the observed degradation in extrapolation accuracy. A more rigorous analysis, perhaps involving perturbation theory or a stability analysis of the underlying PDE, would be necessary to solidify this claim.
2. The motivation behind the proposed transfer learning approach is not clear. It is not immediately obvious why pre-training on a related PDE would mitigate the spectral shift. The authors should provide a more detailed explanation of how the shared feature space learned during transfer learning is able to capture and correct for the spectral shift phenomenon. A clear connection between the spectral shift and the inductive biases learned through transfer learning is missing.
3. The empirical results for improved extrapolation performance are not convincing. While the transfer learning approach shows some improvement, the L2 Extrapolation Error on the Schrodinger Equation (imag) for the proposed method is still quite poor (290%), which is still quite unusable from a practical stand-point. The authors should acknowledge that the improvement is marginal and that further work is needed to achieve practically useful extrapolation performance. The results lack a comparison with other state-of-the-art extrapolation techniques, making it difficult to assess the true value of the proposed method.

### Questions
**Comments/Questions:**
1. I understand the space constraints but figures 7a and b are quite important to demonstrate the results shown in Section 3.1.
2. The placement of Figure 1 can be improved. It is referenced in Page 6 while the Figure is present in page 1. Changing the location of the figure to a more appropriate location can improve the readability of the paper.
3. In my opinion, transfer Learning on the full domain is an unfair comparison, as the PDEs with a similar set of coefficients were already trained on the entire domain. 

**Minor comments:** 
The authors use a different citation format than the standard ICLR format. Using the original citation format would result in overflow of the text outside the page limit since they are considerably longer.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript looks at extrapolation capabilities of the PINN solutions for multipl. The authors introduce a concept of spectral shifts that can be used to predict the PINN extrapolation performance. 

The spectral shifts are used to analyse what features are not affecting the extrapolation performance using a set of seven different PDEs. Their results indicate that the number of layers, number of neurons , activation function, number of samples or training do not contribute.

To remedy the extrapolation challenge, the authors find that  transfer learning using similar PDEs, decreases significantly the extrapolation errors.

### Strengths
A significant analysis on the extrapolation capability of the  PINN in its basic structure.
Introduction of the weighted Wasserstein-Fourier distance as a measure.
Excellent and clear presentation of the results.

### Weaknesses
One may assume that extrapolation will be successful when the training data contains the types of behaviour that will occur in the extrapolated portion of the time domain. This would explain how the PINN solutions of PDEs without or with small spectral shift are viable for extrapolation. If the characteristics of the PDE solutions change drastically after some time scale i.e. have a large spectral shift.

I am missing an analysis where the a particular differential equation have short time behaviour which is spectrally "stable" and long term behaviour, where the spectral shift emerges.  Hence, the difference in the PDE behaviour may also come from how long a certain trajectory is followed, not intrinsically from what kind of equation it is. Then, a user of the method may feel safe to extrapolate a given PDF that has seemed to be "safe" but enter in the dangerous domain without warning.

It seems that safe way would be to use an alternative method to check the accuracy of the solution always, which makes the extrapolation capability less useful.

### Questions
Please, consider the possible issue I raised in the weaknesses part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces extrapolation failures of PINNs, which studies the out-of-domain behavior of PINNs. The paper then analyzes the extrapolation failures in the scope of Weighted Wasserstein-Fourier Distance and spectral bias, showing the PDEs with blockwise WWFs tend to have extrapolation failures, and when extrapolation happens, the prediction spectral shifts from the true solution.

The paper then proposes a transfer learning strategy that effectively mitigates extrapolation failures.

### Strengths
1. The paper introduces extrapolation failures of PINNs, which studies the out-of-domain behavior of PINNs and seems to be a novel and promising research topic.
2. The paper leverages a novel scope, Weighted Wasserstein-Fourier Distance, to analyze spectral shifts for extrapolation failures. The analysis shows that (1) PDEs with blockwise WWFs tend to have extrapolation failures and (2) when extrapolation happens, the prediction spectral shifts from the true solution.
3. The paper proposes a transfer learning strategy that mitigates extrapolation failures.

### Weaknesses
1. The theory of this paper is not solidly developed enough. The conclusion of the paper, says spectral shift, is drawn from observations of several specific types of PDEs, can be empiricism, and may not be generalizable enough for other PDEs. In addition, justifying whether a PDE will suffer from an extrapolation failure using WWF can be difficult in practice. To examine whether the WWF is blockwise or not, it requires true $f_s$ for $s\in I$ and $f_t$ for $t\in E$, while $f_s$ and $f_t$ are not available for most practical cases. The paper does not provide a clear theoretical framework for how the blockwise nature of the WWF directly leads to extrapolation failures, making the connection somewhat speculative. Furthermore, the practical challenge of obtaining the true solutions to assess the blockwise nature of the WWF significantly limits the applicability of this analysis.

2. Leveraging the concept of spectral bias for extrapolation as a hypothesis is problematic. The spectral bias states that NN tends to learn low-frequency components more easily and faster than high-dimensional components during training [1]. While extrapolation is a validation/testing process. Thus, one should not explain a phenomenon in testing with a theory for training, or use it as a hypothesis (despite that the paper beats the hypothesis to the end). The hypothesis reference paper [2] does not make any statement on extrapolation with spectral bias either, they only assert PINNs fail to train when the training time window becomes large, possibly due to spectral bias. The paper's reliance on spectral bias, a concept primarily related to training dynamics, to explain extrapolation behavior is a significant weakness. The paper does not adequately address the fundamental differences between the training and testing phases. While spectral bias might influence the learned representation, it does not necessarily dictate how the model will perform on out-of-domain data. The link between spectral bias and extrapolation error needs more rigorous justification.

3. The presentation of the paper can be improved, say most figures can be denser to save space, and most tables can have nicer borders, etc.

### Questions
1. For the proposed transfer learning method, what is the benefit of transfer learning rather than directly learning new PINNs over the full domain?  As shown by massive previous works, PINNs can easily learn accurate solutions for Burger's equation, as showcased in this work.

2. Could the author explain why (or what does it mean) for a constant WWF distance of the true solutions for diffusion/reaction-diffusion equation in Figures 15 & 16?

3. Could the author explain why diffusion and reaction-diffusion (Figures 15 & 16) show similar WWF distance differences between true solutions and predictions as Burger's and Allen-Cahn (Figures 13 & 14), but the first two do not show significant extrapolation failure, while the latter two show significant extrapolation failures (Figure 7)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the extrapolation of PINNs based on the Fourier spectrum shifts.

### Strengths
The author analyzes the extrapolation performance of PINNs based on the Weighted Wasserstein-Fourier distance (WWF) in different time domains during training and testing.

### Weaknesses
The extrapolation problem of PINN is not a significant problem, as we can always finetune the PINN if long-time prediction is needed, or we can train a new PINN on the new domain.

In the context of domain adaptation and domain generalization in computer vision, the conclusion of this paper does not seem to be novel. The distance between Fourier components during train & test domains is just like the concept of distribution shift in computer vision, where people use the KL divergence and other metrics to quantify the representation distribution between train and test to predict the out-of-domain  /out-of-distribution generalization performance.

From this viewpoint, we can also reinterpret the authors' conclusion: We find that failure to extrapolate is not caused by high frequencies in the solution function, but rather by shifts in the support of the Fourier spectrum over time.

The so-called "shifts in the support of the Fourier spectrum over time" is just the distribution shift in computer vision.

And one can actually derive a rigorous mathematical bound for the out-of-domain PINN error.

### Questions
Please justify the importance of PINN's extrapolation: why don't we just train a new model/finetune?
Please explain your novelty over the concept of domain adaptation and domain generalization in computer vision.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
