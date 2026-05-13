# SE(3)-Hyena Operator for Scalable Equivariant Learning

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Modeling global geometric context while maintaining equivariance is crucial for accurate predictions in many fields such as biology, chemistry, or vision. Yet, this is challenging due to the computational demands of processing high-dimensional data at scale. Existing approaches such as equivariant self-attention or distance-based message passing, suffer from quadratic complexity with respect to sequence length, while localized methods sacrifice global information. Inspired by the recent success of state-space and long-convolutional models, in this work, we introduce SE(3)-Hyena operator, an equivariant long-convolutional model based on the Hyena operator. The SE(3)-Hyena captures global geometric context at sub-quadratic complexity while maintaining equivariance to rotations and translations. Evaluated on equivariant associative recall and n-body modeling, SE(3)-Hyena matches or outperforms equivariant self-attention while requiring significantly less memory and computational resources for long sequences. Our model processes the geometric context of $20k$ tokens $\times3.5$ faster than the equivariant transformer and allows $\times175$ longer a context within the same memory budget

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the SE(3)-Hyena operator, the first equivariant long-convolutional model with sub-quadratic complexity for global geometric context.  Importantly, authors claim their framework is flexible and can accommodate any equivariant network as the projection function.

### Strengths
The idea of using global information to improve the model is very natural, and the convolution simplification of the cross product is very elegant.

### Weaknesses
 > **W1. Lack of discussion on related work.**

There are many works that use global features to improve equivariance. Although this paper's work is obviously different from them, it is recommended to add a discussion on these works (e.g. FastEGNN [a], Neural P^3M [b]).

> **W2. The motivation for operator design is unclear.**

Why is the motivation for using the cross product not well explained? As we all know, the cross product is the Hodge star dual of the outer product. Can it be explained from this perspective? In addition, the introduction of the cross product actually produces pseudovectors, which also leads to the fact that this paper is only SE(3) equivariant rather than E(3) equivariant. Is such an introduction really reasonable?

> **W3. Results on N-body lack the latest baseline.**

Some of the latest results are not shown (e.g. 0.0043 of SEGNN [c], 0.0039 of CGENN [d]). Compared with these works, the results of this work seem to be insufficient.

> **W4. The significance of associative recall experiments is unclear.**

The current experiment cannot illustrate the "contextual learning capabilities of sequence models" that the authors want to claim. First, the model lacks more baselines (e.g. LEFTNet [e], MACE [f], EquiformerV2 [g], SO3krates [h]). It is more like explaining that in this setting, equivariant models are better than models without built-in symmetry priors. Secondly, this experiment lacks practical application significance. I can't seem to find a corresponding task in real life. I hope the authors can give further explanation.

> **W5. Lack of baseline in RNA dataset.** 

The baseline is also missing, and the baseline mentioned in W1 and W4 should be supplemented.

> **W6. Lack of expansion on other models.**

Authors claim their framework is flexible and can accommodate any equivariant network as the projection function. Is it possible to extend several common models (e.g. SchNet [i], EGNN [j], MACE [f], HEGNN [k])?

> **W7. Others (Some typos)**

- Line 144: where is the function $\Psi$, or the hat $\hat{\mathbf{x}_i}, \hat{\mathbf{f}_i}$ are the outputs?
- Line 231: in calculation of $\alpha_3$, it should be $\mathbf{r}_1^\top\mathbf{r}_2$
- Line 242: feature tuples $f_i$, LaTeX misses underscore
- Line 817: "hiddent dimension" should be "hidden dimension"
- Others: the logarithmic symbol should be $\log$ instead of $log$, and why is there a base sometimes without and sometimes with 2?

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the SE(3)-Hyena operator to capture global geometric information while preserving equivariant constraints. It aims to address the computational limitations of existing methods, such as self-attention and local processing techniques. The proposed model is evaluated on dynamical system modeling and RNA property prediction tasks, and the authors introduce an "equivariant associative recall" task to assess contextual learning abilities.

### Strengths
Applying deep learning to problems that involve modeling geometric context, as done in this paper, is a valuable direction in the field. Performance improvements in this area often depend on architectural advances, which is also good to see.

### Weaknesses
 - The experiments in the paper are not comprehensive enough to clearly demonstrate the advantages of the proposed method over existing ones. For example, baselines used in the paper -- SchNet, EGNN, and SE(3)-Transformer -- have been evaluated on the QM9 dataset in their original papers. It would be more convincing if the authors included results on QM9 as well.

- Several state-of-the-art baselines for dynamical system modeling are missing, making the performance of the proposed model not convincing enough. Examples include SEGNN [1], SAKE [2], SEGNO [3], and GeoMFormer [4].

### Questions
Since the work focuses on "scalable" equivariant learning, could the authors provide results on larger-scale datasets to further demonstrate the model's effectiveness?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors proposed SE(3)-Hyena operator for modeling global interaction of atomistic systems. Unlike naive SE(3)-equivariant attention, the SE(3)-equivariant operator does not require quadratic computational complexity due to the usage of FFT. The reduced complexity is well-benchmarked on toy examples.

### Strengths
1. Using a sub-quadratic operator for global context in 3D atomistic modeling can be potentially a good idea.

### Weaknesses
1. The writing should be greatly improved. See Questions below for more details.
2. Experiments in the paper are very limited. The first two experiments basically tell little about how effective a network architecture can be. The third one does not show the benefit of SE(3)-Hyena except that the proposed method takes less memory.
3. Lack of comparisons to previous works on other better-benchmarked datasets such as MD17, QM9 and so on. Overall, how effective modeling global context is remains unclear.
4. The exact proposed architecture is missing or very hard to understand. I think a better visualization covering all the details in a high-level manner can be helpful.
5. The proposed architecture only uses type-0 and type-1 vectors and can only use 1 channel for type-1 vectors. These significantly limit applying the network to slightly larger datasets.

### Questions
> Writing
1. Line 19: Give one or two sentences about long convolutions. Otherwise, it is hard to tell the difference from message passing.
2. Line 22: Give the name of datasets you tested so that people can better judge the scale of experiments at the beginning.
3. Line 32 -- 38: Give one or two sentences about equivariance.
4. Figure 1: I cannot tell any difference from typical self-attention, and thus the complexity O(N log N) is unclear.
5. Figure 2: The figure is too simplified without giving any detail. You should include more details about projection, geometric long convolution and gating and make them consistent with the context.
6. Line 144 -- 145: Add equation number. Also I think $\hat{x}_i$ is not defined here.
7. Line 169 -- 170: typo: "To this end,"
8. Line 191 -- 192: I don't think $F^H$ is defined.
9. Line 237 -- 239: Spherical harmonics with type-0 and type-1 vectors are the same as the representation in Cartesian space.
10. Section 3 should be reflected in figures.

---

> Experiments

1. Figure 5: Why is SE(3)-Hyena better than SE(3)-Transformer? I think some explanations would be great.
2. Line 463: Why using just 2 layers? In such small models, global context probably does not exist, resulting a potentially unfair comparison.
3. Line 473 -- 474: You can train a smaller SE(3)-Transformer to fit on GPU?
4. Please compare the proposed network with other previous works on QM9 and MD17 datasets.

---

> Reproducibility

Please submit the code when the work is under review instead of releasing upon acceptance, especially when parts of the paper are unclear and experiments are not well verified.

--- 

> Question

1. Is the memory complexity still $O(N^2)$? If not, please give a very short introduction to this in the paper (either in the main text or appendix).
2. Line 294 -- Line 302: The weighting factor depends on the index of input tokens. How is the permutation of tokens handled?
3. Line 269: You still use typical message passing (EGNN layer) to encode the context. Would this be the memory bottleneck instead of SE(3)-Hyena operator? If yes, I think other equivariant networks share the same memory and compute bottleneck as this work.

### Soundness
1

### Presentation
1

### Contribution
2
