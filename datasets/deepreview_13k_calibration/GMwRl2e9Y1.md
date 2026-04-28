# Restructuring Vector Quantization with the Rotation Trick

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Vector Quantized Variational AutoEncoders (VQ-VAEs) are designed to compress a continuous input to a discrete latent space and reconstruct it with minimal distortion. 
They operate by maintaining a set of vectors---often referred to as the codebook---and quantizing each encoder output to the nearest vector in the codebook. 
However, as vector quantization is non-differentiable, the gradient to the encoder flows \textit{around} the vector quantization layer rather than \textit{through} it in a straight-through approximation.
This approximation may be undesirable as all information from the vector quantization operation is lost. 
In this work, we propose a way to propagate gradients through the vector quantization layer of VQ-VAEs. 
We smoothly transform each encoder output into its corresponding codebook vector via a rotation and rescaling linear transformation that is treated as a constant during backpropagation. 
As a result, the relative magnitude and angle between encoder output and codebook vector becomes encoded into the gradient as it propagates through the vector quantization layer and back to the encoder.
Across 11 different VQ-VAE training paradigms, we find this restructuring improves reconstruction metrics, codebook utilization, and quantization error.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an improvement to the STE method for training VQ-VAE. While STE copies the gradient from the quantizer output to input, this paper proposes the rotation trick, which uses a rotated and scaled gradient according to the value of the quantizer input. This enables the gradient to depend on the value of the quantizer input, whereas in STE it is the same for all inputs that get mapped to the same codebook vector. Experimental results demonstrate superior reconstruction performance and codebook usage across a variety of tasks using VQ-VAE methods.

### Strengths
- The method is principled, and I think it is a good and simple idea to improve some of the issues of STE
- The paper motivates the issues with STE well, as well as the rotation trick itself. The explanations with figures are helpful to understand the intuition of the method. 
- Experimental results are fairly extensive, encompassing many different scenarios where VQ-based models are used, each showing the superiority of the rotation trick over STE.

### Weaknesses
 - I have some trouble understanding why the Hessian idea is not good. The explanations provided in the paper are that it is similar to a vanilla auto encoder training, with no quantization. However, this seems only applicable to the "exact gradient" idea and not the Hessian idea. It seems the Hessian idea sets the gradient at e to the gradient at q (what STE does), plus the additional curvature term. Whereas the rotation trick multiplies the gradient at q by the scaled rotation matrix. So it seems that both capture the location of e.
- Moreover, I wonder if the analysis in section 4.3 could be extended to the Hessian idea. It seems the Hessian idea also gets the benefits that Section 4.3 argues in favor of the rotation trick. There seems to be some disconnect between this and the experimental results where it was shown the Hessian idea does not perform well. If a stronger explanation is provided, that would be helpful to understand.
- While the experimental settings are fairly extensive, they primarily demonstrate how the rotation trick is superior to STE. I think some other baseline methods that improve upon STE are also necessary for comparison. Namely, those mentioned in Section 2, such as Huh et al 2023, Gautam et al, 2023, and Takida et al, 2022. This would provide comparison between the rotation trick and other methods that go beyond STE.

### Questions
Please see the weaknesses above.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors address the training instability of the straight-through estimator by proposing the rotation trick for vector quantization (VQ), i.e. rotating the gradient $\nabla_q\mathcal{L}$ at the codebook vector $q$ to become the gradient $\nabla_e\mathcal{L}$ at the encoder output $e$ such that the angle between $q$ and $\nabla_q\mathcal{L}$ after the VQ equals the angle between $e$ and $\nabla_e\mathcal{L}$. The rotation trick significantly improves the image reconstruction quality across 11 VQ(-VAE|GAN) training paradigms.

### Strengths
1. The rotation trick is novel, intuitive, and mathematically principled
1. Applying two Householder reflectors is computationally efficient, and incurs no additional training cost
1. Strong empirical success across various VQ(-VAE|GAN) training paradigms

### Weaknesses
1. The method, i.e. how to achieve the rotation, is not explained clearly in the title or main text. It's probably a good idea to move Appendix A.4 into the main text. In fact, consider renaming this paper to "Restructuring Vector Quantization with the *Reflection* Trick", because the rotation $R$ is really two Householder reflectors chained together (maybe we can get away with one reflection? see below).
2. Appendix A.4 appears to be incorrect: in Remark 3, I think the final reflection/rotation matrix should be $(I-2cc^T)(I-2aa^T)$, or equivalently $(I-2bb^T)(I-2cc^T)$, but not $(I-cc^T)(I-bb^T)$. To make this part easier to understand, perhaps you should re-use the $e, q, r$ notation instead of introducing new symbols $a, b, c$, and include a detailed derivation of why $R = (I-2cc^T)(I-2aa^T) = (I-2bb^T)(I-2cc^T) = I - 2rr^T + 2qe^T$. The lack of clarity in the derivation makes it difficult to verify the correctness of the proposed rotation.
3. The effect of the rotation trick is only verified on a high level by codebook usage and quantization error. In particular, Figure 4 is only a diagram ("how we think it works"), not generated from an actual numerical simulation ("how it really works"). Moreover, Figure 4 only shows one gradient update step, and it's unclear how the rotation trick affect the codebook in the long run. It would be beneficial to see a more comprehensive analysis of the gradient dynamics over multiple steps, and how the codebook vectors evolve with the proposed method.
4. The notations are a little confusing. For example, Section 4.3 allows $\tilde{\theta}$ to be negative or exceed $\pi$, but the angle between two vectors is typically defined within $[0, \pi]$. The top panel in Figure 5 also defines $\tilde{\theta}$ in a nonstandard way (when $q$ and $\nabla_q\mathcal{L}$ points at opposite directions, $\tilde{\theta} = 0$ according to the diagram, but normally we say $\tilde{\theta} = \pi$ for this case). In addition, renaming $\tilde{\theta}$ to $\phi$ might avoid some misread. The current notation makes it hard to understand the geometric interpretation of the method.
5. There is an extra "a" on line 113.

### Questions
1. What if we just do one Householder reflection, i.e. $R = I - 2rr^T$? It still preserves the angle ($\tilde{\theta} \in [0, \pi]$), but the "push" effect in Section 4.3 becomes "pull", and vice versa. However, as you pointed out, both push and pull are beneficial, so the result should still be good. The mirror symmetry makes me think this will be as effective as $R = I - 2rr^T + 2qe^T$, and it would be great if you could verify this hypothesis experimentally.
1. The rotation/reflection transformation depends on the location of a center, which you implicitly choose to be the origin. Do you need to shift the $q$ and $e$ such that their center/mean is the origin, or does the rotation trick work even if all $q$ and $e$ fall on one side of the origin (e.g. imagine Figure 4, but on a shifted coordinates system $x' = x + 10, y' = y + 10$, such that the coordinate of all points are positive)?

### Soundness
4

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
3

### Summary
The authors propose an alternative to using straight-through estimation for the gradients of a vector-quantized variational autoencoder (VQ-VAE) to stabilize training and improve codebook usage.

VQ-VAEs are a popular model for data compression and generation, consisting of an encoder and a decoder network. However, instead of passing the encoder output directly to the decoder, the output is first quantized to some codebook vector; these vectors are also learnt during training. However, vector quantization (VQ) is a non-differentiable operation; thus, practitioners usually ignore the quantization operation in the backward pass to enable gradient back-propagation; this is called straight-through estimation (STE). More formally, given some encoder output $e$ and its vector quantized version $q$, STE "sets" the Jacobian $\frac{\partial q}{\partial e} = I$, where $I$ is the identity matrix instead of the all-zero matrix (almost everywhere) as would be dictated by the standard rules of calculus.

In this paper, the authors identify some important shortcomings of using STE in practice, such as training instability and codebook collapse. Based on their observations, they instead suggest "setting" the Jacobian $\frac{\partial q}{\partial e} = \frac{\lVert q \rVert}{\lVert e \rVert} \cdot R$, where $R$ is an orthogonal matrix depending on $e$ such that $q = \frac{\partial q}{\partial e} \times e$.

The authors argue and demonstrate empirically across several experiments that this pick significantly improves codebook utilization, reconstruction loss, and reconstruction quality.

### Strengths
The paper's core idea to set the Jacobian to the quantity suggested by the authors is reasonably well-motivated. It can be considered a natural dual to STE, as it uses the multiplicative/polar structure over Euclidean space as opposed to the additive structure used by STE.

The core idea in the paper is neat and simple, and the experimental verification appears reasonably extensive and rigorous.

The paper is well-written, with very nice illustrative figures.

### Weaknesses
While I do not think the paper suffers from any major weakness, there are two aspects in which it could be strengthened:
1. The authors do not discuss the limitations of their proposed method. While they present good arguments for when their proposed rotation trick is preferable to STE, have they considered the scenarios in which it might be undesirable? For instance, under what conditions might the rotation trick lead to unstable training or suboptimal performance compared to STE? Specifically, are there situations where the assumption that the gradient at the quantized vector $q$ is a good proxy for the gradient at the encoder output $e$ breaks down when using the rotation trick? This could be due to the rotation matrix $R$ being ill-conditioned or the scaling factor $\frac{\lVert q \rVert}{\lVert e \rVert}$ becoming unstable.
2. The theoretical motivation for the rotation trick is unclear, other than the fact that it is the natural "multiplicative counterpart" to STE. While I really like the "post hoc" argument that the rotation trick results in a non-constant Jacobian, which might help improve codebook usage, I do not see a good mathematical reason for ensuring that the angles between the vectors and their gradients are preserved, which is better than magnitude and direction. For example, one could argue that an advantage of the identity Jacobian is that it does not shrink or expand space since its determinant is one. This could be solved by combining the STE and the rotation trick by setting (in the authors' notation) $\tilde{q} = R e + (q - R e)$ for an appropriate rotation matrix $R$ and using an appropriate stop-gradient; this would now preserve both magnitude and angle as I understand. In fact, we can even create an entire two-parameter family of gradient approximations by setting (in the authors' notation) $\tilde{q} = \lambda^\alpha R_{\alpha, \beta} e + \beta (q - R_{\alpha, \beta} e)$. Have the authors considered such a solution? If not, could the authors run some small-scale experiments at least to check its performance?

Minor:
 - Fig 2: Increase the tick and axis label font size to match the font size of the caption, as the text is illegible at 100% zoom right now.

### Questions
- Suggestion: Figure 2 beautifully illustrates the difference between the original and the STE gradient. To make it even nicer, I think the authors should consider adding the "rotation trick" gradient field as well!
 - Recently, the STE was connected to the deeper theory of numerical integration in [1]. Could the authors comment on whether their method might also have such an interpretation?

## References
[1] Liu, L., Dong, C., Liu, X., Yu, B., & Gao, J. (2024). Bridging discrete and back-propagation: Straight-through and beyond. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method, reffered to as the "rotation trick", to propagate approximated gradients through the vector quantization layer of VQ-VAEs.
The proposed method addresses the issue of a "straight-through estimator (STE)," which loses information about the positions of encoder outputs relative to codebook vectors.
The capability of the method to increase information capacity and reduce distortion in vector quantization is illustrated with examples and explanation of the "push-pull effect".
The authors conduct experiments across 11 VQ-VAE training settings to demonstrate that the proposed method improves reconstruction performance compared to baseline methods.

### Strengths
This paper is well-written and well-motivated. Its review of VQ-VAE, STE, and related work is concise and easy to follow, providing a clear motivation for the study.
The algorithm for the rotation trick is clearly formulated.
The explanation of the effects of the rotation trick, supported by figures, is illustrative.
The effectiveness of the proposed method is investigated through experiments in 11 different settings, which can be considered sufficient.

### Weaknesses
Overall, this paper is well-motivated and well-structured, but I would like to raise a point that requires clarification.

The algorithm is designed to preserves the angle between a vector and a gradient, which leads to the push-pull effect described in Section 4.3. However, it appears that using only a rotation, $\frac{\partial \tilde{q}}{\partial e} = R$, satisfies this requirement, and rescaling with $\frac{||q||}{||e||}$ is not necessary for the gradient approximation. (I understand that rescaling is necessary for transforming $e$ into $q$.) 
Additionally, it seems that rescaling of gradients may hinder the propagation of gradients when $||q||$ is close to zero.
Providing an explanation for why the rescaling factor $\frac{||q||}{||e||}$ is used for the gradient approximation would clarify the motivation behind this algorithm's design.

### Questions
* Why is the rescaling factor $||q|| / ||e||$ used for the gradient approximation? How does it affect training of the encoder and the codebook?
* Minor comment: In Definition 1 (Householder Reflection Matrix), isn't it required that $||a|| = 1$?
* Minor comment: there is a typo: "a a convex combination'" in p3 L6.

### Soundness
4

### Presentation
4

### Contribution
3
