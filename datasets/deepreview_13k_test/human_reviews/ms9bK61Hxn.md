# Similarity Group Equivariant Convolutional Networks

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
We introduce similarity group equivariant convolutional networks (SECNNs), designed to achieve continuous translation, rotation and scale equivariance, or discrete similarity group equivariance that involves discrete Dihedral group. The networks are implemented as steerable CNNs by employing a steerable and approximately shiftable and scalable basis for continuous translating, rotating and scaling convolution kernels within a five-dimensional position-orientation-scale-reflection space. 
Our results demonstrate that SECNNs attain state-of-the-art results on translated, rotated and scaled MNIST datasets. SECNNs also achieve the accuracy of other leading group equivariant networks on CIFAR10/100,
while being equivariant to the full range of the similarity group in comparison to existing state of the art, which is equivariant to only sub-groups of the similarity group.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper describes a group convolution architecture that is equivariant to the similarity group. It is based one expanding the convolution kernels into a (Fourier-Melin) basis that is steerable w.r.t. to the rotation, scale and reflection action. The method is evaluated on a variation of MNIST and on CIFAR10.

### Strengths
## Strengths
1. The paper presents what appears to be the first rotation-scale equivariant group convolution architecture utilizing this particular steerable approach. While previous work [Sosnovik et al. 2020] implemented steerable scale-equivariant G-CNNs, they employed a different definition of steerability.
2. The paper provides a thorough construction of the steerable basis, building upon the foundation established in [Zhang and Williams 2022].

### Weaknesses
## Areas for Improvement and Suggestions

### Historical Context and Novelty Claims
The paper's claim of being the first to implement SIM(2) equivariant networks (emphasized in the abstract's first line) would benefit from more precise positioning within the literature. [Knigge et al. 2022] previously proposed this using the regular group convolution paradigm, with arguably more efficient implementation due to its separable nature. Additionally, the relationship to [Zhang and Williams 2022] could be more clearly articulated, as they also address similarity equivariant networks.

### Technical Contributions
The extension from [Zhang and Williams 2022] appears primarily focused on the addition of reflection. It would be helpful to clarify the significance of this contribution, particularly regarding the SECNN 3D and 4D implementations shown in the tables (presumably versions without flips). It seems that in Zhang and Williams the theory is already presented, and if the only contribution is the flips (which is trivial), and even more if they are not used in the experiments, I don't really see any contribution.

### Experimental Validation
The practical advantages of the method could be more thoroughly demonstrated. While showing improved performance on transformed MNIST, the method's performance on CIFAR falls below other baselines. Given the increased computational complexity, a more detailed discussion of the method's optimal use cases would be valuable.

### Technical Clarifications Needed

1. Terminology: The distinction between shiftable, steerable, and scalable would benefit from more precise definitions, particularly regarding the specific group representations involved. That is, in my point of view these terms are collectively referred to as steerable, but then one can define steerability w.r.t. different groups and different group representations.

2. Implementation Details:
   - Line 64: Please specify the axes of the 5D space
   - Line 214: Consider providing interpretations for variables $\omega_\phi$, $\alpha_\rho$, and $\omega_\rho$
   - The nature of the "approximate" steerability requires clarification. Approximate is mentioned various time but it is never explain in what sense there is an approximation.
   - Equations 6 and 14 appear to have inconsistencies regarding position dependence in $M{g}$. Equation 6 seems that M{g} provides the frequencies, but equation 14 also shows a dependency on positions.

3. Theoretical Framework:
   - The paper appears to generate steerable feature fields through basis function convolution, placing it within the steerable group convolutions framework (cf. [Weiler and Cesa 2019])
   - The 5x5 grid implementation raises questions about effectively modeling scale variations. That is, it is reasonable to assume that sensible scale variations can be modeled on a small 5x5 grid? How are other scale equivariant methods handling this?
   - Line 330's equation setting $x_0, x_1$ equal to $\phi, \rho$ is not quite correct. It is not an equality but rather equivalence (reparametrization). I mean $x_0$ is not equal to $\phi$.
   - I do not understand the logic in line 341: " As the factor ..."

### Additional Literature
Consider incorporating discussion of:
- [Marcos et al. 2018]'s work on scale equivariance too when citing Marcos et al.'s work on rotation equivariance.
- [Knigge et al. 2022] in the introduction and Table 1
- The scale equivariant Lie group method [Bekkers 2019] in Table 1.

### Technical Details Requiring Clarification
1. Equation 14: Please clarify the distinction between $f$ and $f'$, what does the prime indicate?
2. Line 402's observation about frequency domain implementation is great and it aligns with [Cesa and Weiler 2019]'s findings. It also seems to motive more recent works like [Bekkers et al. 2024] to completely avoid Fourier based steerable methods.
3. Line 426: Please specify which axes of the 5D space constitute the "4D nature"
4. Table 2: The terms 3D, 4D, and mixed need explicit definition regarding symmetries
5. Line 498: The SECNN-Mix weight blending process requires elaboration, what is meant here?

### Experimental Evaluation
Consider including comparisons based on equal channel counts, even if this results in different parameter counts, to provide additional insight into the method's efficiency. That is, I don't believe matching parameters is necessarily a fair thing to do.

## References

Bekkers, E. J., Vadgama, S., Hesselink, R., Van der Linden, P. A., & Romero, D. W. (2024). Fast, Expressive SE(n) Equivariant Networks through Weight-Sharing in Position-Orientation Space. In The Twelfth International Conference on Learning Representations.

Knigge, D. M., Romero, D. W., & Bekkers, E. J. (2022, June). Exploiting redundancy: Separable group convolutional networks on lie groups. In International Conference on Machine Learning (pp. 11359-11386). PMLR.

Marcos, D., Kellenberger, B., Lobry, S., & Tuia, D. (2018). Scale equivariance in CNNs with vector fields. arXiv preprint arXiv:1807.11783.

Sosnovik, I., Szmaja, M., & Smeulders, A. (2020). Scale-Equivariant Steerable Networks. In International Conference on Learning Representations.

Weiler, M., & Cesa, G. (2019). General e(2)-equivariant steerable CNNs. Advances in Neural Information Processing Systems, 32.

Zhang, X., & Williams, L. R. (2022). Similarity equivariant linear transformation of joint orientation-scale space representations. arXiv preprint arXiv:2203.06786.

### Questions
see above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents SECNNs, a family of neural networks equivariant to continuous translation, rotation and scale, or to discrete similarity groups. Their implementation encompasses the use of steerable, approx. shiftable and scalable basis for the convolutional kernels. In their evaluation, authors show remarkable experimental results for SECNNs.

**Important.** The authors claim to be first in achieving these equivariances, but this is not true. There is in fact a work from ICML 2022 that already provided it (in fact it can achieve equivariance to Sim(2) without the constraints (continuous vs. discrete) of this work) [1] .

### Strengths
- The method presented here is novel, with multiple important contributions. I believe it has tons of potential for the field, both for future research and practical applications.

- Despite having multiple theoretical contributions, the paper is very easy to follow. It is clearly written and well-structured. I enjoyed reading the paper very much!

### Weaknesses
- I did not observe any strong weaknesses in this paper. However, there is one important point that must be addressed / modified in the paper.

  In particular, the paper claims that it is the first method ever to achieve equivariance to Sim(2). However, there have been previous works that tackle (and provide practical implementations to this equivariance) [1]. Now, that does not demerit the contributions of this paper, as the approaches are quite different and the results are very positive, but it definitely calls for modifications in the paper positioning. I encourage the authors to do this during the rebuttal. Add proper comparisons, differences, etc. I trust that the authors will do so, and as of now, I will not let this affect my score.

- In addition, it seems that the proposed method  is not really able to achieve equivariance to the whole of the Sim(2) group –please correct me if I am wrong–. This should be stated clearly in the paper.

- Finally, as expected, the main limitation of the paper is related to memory consumption and speed. However, the authors do not provide any analysis / comparison in this aspect. It would be very helpful to provide such analyses such that the community can understand what the current cost is, e.g., in comparison to E2 nets and [1]’s method. It also would be helpful to have ablation analyses that study how the number of basis functions used affects accuracy, runtime and memory consumption.

### Questions
### Questions / Additional comments

- The authors do not explicitly define what seccn3D secnn4d and secnnmix are in Table 2.

- Line 317. “... allows us to precompute the basis with large enough spatial frequencies, for instance 1024x1024.” -> I am not sure I understand this. Could you please explain what you mean by this? How big will be the precomputed kernels in spatial dimensions?

- Line 355. Footnotes should go at the end of sentences after the point. 

- For the Fourier Transform, it is known that its complexity grows as N log N, where N is the length of the sequence. What is the complexity / cost of going back and forth all the time from the spatial to the frequency space? 

- Line 445-449. Is this inducing separability on the kernels? If so, it would be worth noting that [1] also exploits this to scale to Sim(2). 

### Other comments

- The authors mention how the inherent 4D nature of the kernels leads to very large parameter consumption. I believe that using CKConvs [2] –or subsequent parameterizations., e.g., [3, 4] – to parameterize the kernels, akin to [1] could be used to mitigate this issue. Using this parameterization could provide more flexibility / parameter efficiency, and, perhaps, leads to better results. 

- [5] uses CKConvs and masking strategies to learn the level of equivariances (as opposed to E2CNNs) –Line 422. I wonder whether this approach could be used to extend [5] to truly large groups.

- Under the assumption that the scaling of the method is similar to that of the Fourier transform, e.g., NlogN, then the method's complexity would not be dependent of the kernel size. If this happens to be the case, it would be interesting to look at long context. This has gained much attention in recent years [2, 3, 4, 5, 6, 7, 8].

### Conclusion

In summary, I consider this a well-rounded paper with interesting contributions and potential impact to the field. Provided that the points related to [1] are included, I believe this paper deserves a clear acceptance. I, therefore, recommend this paper be accepted. 


### References

[1] Knigge, D.M., Romero, D.W. and Bekkers, E.J., 2022, June. Exploiting redundancy: Separable group convolutional networks on lie groups. In International Conference on Machine Learning (pp. 11359-11386). PMLR. 

[2] Romero, D.W., Kuzina, A., Bekkers, E.J., Tomczak, J.M. and Hoogendoorn, M., 2021. Ckconv: Continuous kernel convolution for sequential data. arXiv preprint arXiv:2102.02611.

[3] Romero, D.W., Bruintjes, R.J., Tomczak, J.M., Bekkers, E.J., Hoogendoorn, M. and van Gemert, J.C., 2021. Flexconv: Continuous kernel convolutions with differentiable kernel sizes. arXiv preprint arXiv:2110.08059.

[4] Knigge, D.M., Romero, D.W., Gu, A., Gavves, E., Bekkers, E.J., Tomczak, J.M., Hoogendoorn, M. and Sonke, J.J., 2023. Modelling Long Range Dependencies in $ N $ D: From Task-Specific to a General Purpose CNN. arXiv preprint arXiv:2301.10540.

[5] Romero, David W., and Suhas Lohit. "Learning partial equivariances from data." arXiv preprint arXiv:2110.10211 (2021).

[6]  Gu, A., Goel, K. and Ré, C., 2021. Efficiently modeling long sequences with structured state spaces. arXiv preprint arXiv:2111.00396.

[7] Poli, M., Massaroli, S., Nguyen, E., Fu, D.Y., Dao, T., Baccus, S., Bengio, Y., Ermon, S. and Ré, C., 2023, July. Hyena hierarchy: Towards larger convolutional language models. In International Conference on Machine Learning (pp. 28043-28078). PMLR.

[8] Moskalev, A., Prakash, M., Liao, R. and Mansi, T., 2024. SE (3)-Hyena Operator for Scalable Equivariant Learning. arXiv preprint arXiv:2407.01049.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents SEC-NN, Similarity group equivariant convolutional networks for continuous translation, rotation, and scale equivariance. This is achieved by using an approximate translation and scale basis in the Joint-orientation Scale Space proposed by Zhang et al. The empirical experiments are conducted on MNIST, CIFAR10/CIFAR100 datasets and the work contains several design choices for the proposed method.

### Strengths
1. The paper presents a relevant related work section, motivating the area of research as well as building upon existing works. 
2. The ablations provided for SECNNs in the paper and appendix is very thorough.

### Weaknesses
1. The writing of the paper can be improved as it lacks clarity on the work actually done creating difficulty in distinguishing it from existing work, especially in building simConv using shiftable steerable and scalable filters.  
2. Existing methods is literature like Group convolution methods like [1] have steerable kernels, [2] present convolution kernels through weight sharing in position orientation space missing in the experiments comparison. 
3.  [3] presents similar group equivariant convolutions using AFMT in join orientation-scale space. Given this, as far as I understand the proposed method, SECNNs use the same basis as [3] and provide a different implementation for similarity group convolutions and ablations for the same through different modeling choices. 



[1] Implicit Convolutional Kernels for Steerable CNNs, Zhdanov et al
[2]Fast, Expressive Equivariant Networks through Weight-Sharing in Position-Orientation Space, Bekkers et al
[3] Similarity Equivariant Linear Transformation of Joint Orientation-Scale Space Representations, Zhang et al

### Questions
1. Could you clarify their contribution especially distinguishing from the work of Zhang et al. ?
2. Does the Fourier transform approach of the AFMT basis functions scale well? Are there other advantages of working in this representation scheme? The experiments presented are on MNIST and CIFAR10/CIFAR100 datasets, but would this approach be more useful in non-image domains?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper constructs similarity group equivariant convolutional networks by utilizing steerable, (approximately) shiftable and scalable kernels. The authors demonstrate how to improve computational efficiency and present some design choices. They implement SECNNs that are equivariant to a continuous subgroup and a discrete version of the similarity group, and evaluate them on transformed MNIST and CIFAR10/100, with results demonstrating improved empirical performance.

### Strengths
1. The paper constructs equivariant networks, called SECNNs, for the full similarity group using shiftable, steerable, and scalable filters. This achieves equivariance with respect to continuous translation (often ignored in prior work), rotation, scale, and reflection.
2. The paper improves the computational efficiency of SECNNs with multidimensional kernels through measures including a cropped Fourier series of the steerable and scalable basis.
3. The paper provides comprehensive details on the model and experimental setup, ensuring a fair evaluation of the proposed approach.

### Weaknesses
1. While SECNN extends Zhang & Williams (2022) to include reflection, this extension alone may not constitute a substantial advancement for the field. A more detailed and explicit discussion on the limitations of Zhang & Williams (2022), the specific advantages of SECNN, and the technical challenges involved in achieving these improvements would enhance the paper.
2. Existing methods achieving affine or general Lie group equivariance [1-3] are not adequately compared, leaving a gap in understanding how SECNN competes with these models. Similarity equivariance might also be achievable through these alternatives.
3. One of the paper's key contributions is achieving equivariance for the full similarity group, including reflection. However, the implementation and experiments do not cover the full similarity group with both reflection and continuous rotation.
4. RST-CNN and SREN, which offer rotation, translation, and scale equivariance, would serve as more relevant baselines than the chosen ones (SESN and E2CNN). Including comparisons with RST-CNN or/and SREN could be more convincing.


References

[1] Lachlan E MacDonald, Sameera Ramasinghe, and Simon Lucey. Enabling equivariance for arbitrary Lie groups. CVPR 2022.

[2] Mircea Mironenco and Patrick Forre ́. Lie group decompositions for equivariant neural networks. ICLR 2024.

[3] Yikang Li, Yeqing Qiu, Yuxuan Chen, Lingshen He, and Zhouchen Lin. Affine equivariant networks based on differential invariants. CVPR 2024.

### Questions
1. It could be important to provide a comprehensive discussion on the limitations of Zhang & Williams (2022) and improvements of this paper.
2. A comparison with existing methods that achieve affine or general Lie group equivariance is necessary (see Weakness 2). As these methods can also attain similarity group equivariance, what distinct advantages does SECNN offer?
3. Experiments on the full similarity group would strengthen the paper. Minimally, it should encompass a brief discussion on the practicality of implementing the full similarity group, along with rationale and insights on selecting different groups to maintain equivariance for different tasks.
4. Comparisons with RST-CNN and/or SREN in the experimental section would offer a more convincing evaluation than the current baselines.
5. Could you further explain how making filters “shiftable, steerable and scalable” in this paper contributes to the achievement of equivariance?
6. Providing examples of promising applications for similarity group equivariant convolutional networks would be both valuable and intriguing.
7. On line 358, 2D images are modeled as functions $\mathbb{Z}^2 \rightarrow \mathbb{R}$. But defining similarity transformations on functions defined over $\mathbb{Z}^2$ is impractical, which hinders the discussion of similarity equivariance. It may be more reasonable to regard 2D images as functions $\mathbb{R}^2 \rightarrow \mathbb{R}$.
8. For natural image classification, the paper employs an orientation histogram approach to convert equivariant feature maps into non-invariant representations. In this context, what role does the equivariance of features play?
9. In Table 2, it is somewhat unexpected that SESN performs worse on Scaled MNIST compared to CNN and E2CNN. Is there an explanation for this?

### Soundness
3

### Presentation
3

### Contribution
2
