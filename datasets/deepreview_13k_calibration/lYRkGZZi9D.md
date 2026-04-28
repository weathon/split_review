# Analysis of Linear Mode Connectivity via Permutation-Based Weight Matching: With Insights into Other Permutation Search Methods

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Recently, Ainsworth et al. (2023) showed that using weight matching (WM) to minimize the $L_2$ distance in a permutation search of model parameters effectively identifies permutations that satisfy linear mode connectivity (LMC), where the loss along a linear path between two independently trained models with different seeds remains nearly constant. This paper analyzes LMC using WM, which is useful for understanding stochastic gradient descent's effectiveness and its application in areas like model merging. We first empirically show that permutations found by WM do not significantly reduce the $L_2$ distance between two models, and the occurrence of LMC is not merely due to distance reduction by WM itself. We then demonstrate that permutations can change the directions of the singular vectors, but not the singular values, of the weight matrices in each layer. This finding shows that permutations found by WM primarily align the directions of singular vectors associated with large singular values across models. This alignment brings the singular vectors with large singular values, which determine the model's functionality, closer between the original and merged models, allowing the merged model to retain functionality similar to the original models, thereby satisfying LMC. This paper also analyzes activation matching (AM) in terms of singular vectors and finds that the principle of AM is likely the same as that of WM. Finally, we analyze the difference between WM and the straight-through estimator (STE), a dataset-dependent permutation search method, and show that WM can be more advantageous than STE in achieving LMC among three or more models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyses the the weight matching algorithm through singular value decomposition. 

Paper starts with the observation that algorithms like weight matching do not significantly reduce the  l2 distance. Followed by this observation, authors empirically verify that weight matching algorithm does not bring the models close enough such that the error barrier can be calculated by a second order Taylor approximation. 

Authors then made the observation that minimizing the l2 distance wrt permutations is equivalent to maximizing the inner product wrt permutations. Using this relationship authors show that weight matching indeed matches the singular values of the layer-wise weight matrices. 

Authors empirically validate that weight-matching and activation matching align the singular vectors however STE does not match the STE. 

Authors empirically show that aligning via SVD can lead to better alignment for 3 models.

### Strengths
- Analysis of the weight matching via SVD of layerwise weight matrices is interesting.
- I find the observation that weight alignment leads to linear connectivity of more that 2 models also interesting

### Weaknesses
 - I would suggest authors to keep the vectorized notation instead of summations to make the paper an easier read.
- Observation that minimizing the l2 distance is equivalent to  maximizing the inner product is pretty well know. [1] also leverages this observation to implement the weight matching algorithm. I found those contributions incremental.

### Questions
- What explains that permutations found by activation matching are much different from weight matching? Can we use SVD to analyze the qualitative / quantitative differences between the two methods that ostensibly minimize a similar objectives, i.e. matching the singular values.
- In [2], authors also analyzed linear connectivity of more than 3 models for checking strong linear connectivity where it is found that as width of the model increases, weight matching allows strong linear connectivity. Are there any insights we can gain from SVD when it studying strong linear connectivity.

[2] Sharma, E., Kwok D., Denton T., Roy DM, Rolnick D., and  Dziugaite G.K.: Simultaneous linear connectivity of neural networks modulo permutation. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (2024).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents a novel analysis of weight matching (WM) for model merging, with comparisons to AM and STE. The authors demonstrate that permutations found by WM may not reduce the L2 distance between 2 models, albeit LMC is satisfied. Instead they show that the singular vectors are aligned. They also demonstrate that STE merging does not align singular vectors.

### Strengths
- This work covers a very important topic likely to have a broad impact in understanding learning and combining in deep neural networks. 
- Paper is very well written; notation is clear and consistent, the problem is motivated, contributions are clear. 
- The Taylor approximation to estimate the barrier for merging models provides a clear intuition for their approach, and demonstrate that WM permutations may not result in the best merge. Results in Table 1 provide good evidence for this stance (though perhaps too many unnecessary significant figures are given and appear arbitrary as a result). 
- Results overall support the paper claims and demonstrate the different merging means for WM, STE, and AM.

### Weaknesses
 - Table 1 (and others) could be improved through highlighting sections to support the conclusion, e.g., where some solutions violate the nearness assumption and the Taylor approx. is not good. Many values presented are overlapping with over values and it is not immediately clear which are significant different vs not. 
- Figures are small and difficult to read. For the distribution plots (Fig. 1, 4), perhaps a logscale on the y axis would allow the reader to better evaluate the claims. 
- "the barrier between πb(θb) and πc(θc) is smaller with WM than with STE. This means that there is a significant difference between the principles of permutations obtained by WM and STE." (line 519) is difficult to evaluate by eye in Figure 6 and not particularly convincing. 
- The statement "suggesting that the reason AM achieves LMC is likely the same as for WM" (line 458) seems overly confident given the evidence presented. Are there other explanations for the similar results?

### Questions
- Connecting it back to the idea in the intro about SGD and the loss landscape, do the authors have any thoughts on how their findings relate to the efficacy of SGD?
- How well does this analysis scale beyond 2 or 3 models? "Therefore, WM is likely to be more advantageous, especially for merging three or more models" (line 522), is there additional proof of this?

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
This paper analyses the linear mode connectivity (LMC) using weight matching (WM), activation matching (AM), and straight-through estimator (STE), with a primary focus on WM. The authors propose that, even though WM does not significantly decrease the $L_2$ distance of the weights between two independently trained models, it still establishes LMC by aligning the singular vectors of each layer associated with the largest singular values. Empirically, the paper demonstrates that two models with a large $L_2$ weight distance after WM can nonetheless produce similar outputs, and empirical results support that singular vectors with largest singular values across the layers are aligned with WM process. Furthermore, it has been demonstrated that AM process exhibits a similar effect, while STE behaves differently. The theoretical analysis leverages SVD on layer weights, and numerical experiments using VGG, ResNet, and MLP on MNIST, CIFAR10, and ImageNet support the claims.

### Strengths
* The paper is clearly written and easy to follow. 

* I have checked the proofs of the theorems presented in the main paper, and they appear correct and clearly articulated.

* The observation that $L_2$ distance reduction via WM is not the sole cause of LMC is interesting. This observation is supported with numerical experiments.

* The theoretical analysis is clearly explained when the underlying assumptions hold (though I have questions about the assumptions' validity; see the Weaknesses section).

* The appendix provides a good amount of detail for reproducing experiments, although the code itself is not shared.

### Weaknesses
 * In line 70, the sentence "... this intuition is inaccurate ..." raises a concern. I think the intuition presented above this sentence is correct, i.e., if $\theta_a \approx \pi (\theta_b)$ then it is reasonable to think that the interpolated model will produce similar outputs. I believe the main narrative of the paper appears to be that even when $\theta_a \not\approx \pi (\theta_b)$, where $\pi$ is found by WM, the interpolated model can produce approximately equal outputs. 

* In line 211, the phrase "... algorithm similar to the backpropagation method to efficiently compute $\mu^T H$ ..." would benefit from further clarification in the appendix. I couldn’t locate a section elaborating on this point. What specifically do the authors mean by "similar algorithm to backprop"? It would be helpful to specify the exact method or provide a reference to a well-established technique for computing the Hessian-vector product efficiently, as this is a non-trivial computation.

* Regarding the sentence in line 261 "... we can find permutation matrices such that the left and right singular vectors of the two models match ...": it seems unlikely that all singular vectors can be matched purely through permutation in all scenarios. This claim needs more rigorous justification, as the singular vectors are generally not permutable without affecting the underlying linear transformation. The authors should clarify under what conditions this assumption holds, or provide a more nuanced explanation.

* In line 286 "distributions of the singular values of the weights ... almost equal": This seems like a strong claim to me. The paper presents results with common datasets like MNIST and CIFAR10 using MLP, VGG, and ResNet. I think the conclusion requires further evidence or a more theoretical foundation. The appendix H.1 discusses this in a more detailed manner, and Figure 7 indicates that output layers' singular value distribution have variability. For this case, the paper suggests that the singular values are approximately a constant multiple across the two models. Even though the output layers' singular value distributions seem correlated, the "constant multiple" assumption seems like a strong one to me as there are contradicting examples in Figure 7 (e.g. Figure 7(a) light blue curve and red curve). The paper should provide a more in-depth analysis of the conditions under which this approximation holds, and acknowledge the limitations of this assumption.

* The assumption that the input vector's direction aligns with the singular vectors associated with large singular values also seems like a strong claim. Analysis in Appendix H.8 with ResNet50 on ImageNet shows that this assumption does not always hold. The paper needs to address this discrepancy more directly and discuss the implications of this assumption not holding for all layers or architectures. It would be beneficial to provide a more detailed analysis of when this assumption is valid and when it is not, and how this affects the overall conclusions of the paper.

* The abbreviation "layer-wise model compression (LMC)" in line 890 conflicts with the abbreviation for linear mode connectivity, and I believe layer-wise model compression does not need an abbreviation.

### Questions
* For the sentence in line 139 "Entezari et al. (2022) conjectured that for SGD solutions ...": is this still a conjecture, or has a more solid theoretical foundation been established?

* In line 122, why is $W_{\ell + 1}' = W_{\ell + 1} P^{T}$ while $W_\ell' = P W_\ell$? I thought it should be $W_{\ell + 1}' = P W_{l+1} $

### Soundness
3

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
4

### Summary
This paper analyzes the algorithms for enforcing linear mode connectivity (LMC) as discussed in Ainsworth et al. (2023). The central question addressed is the underlying mechanisms that lead to the removal of barriers when applying weight matching (WM), activation matching (AM), or the straight-through estimator (STE). The authors argue that the primary reason WM and AM achieve linear connectivity between models is the alignment of the eigenvectors corresponding to large eigenvalues of the weights. Theoretically, they demonstrate that similar eigenvectors lead to similar outputs at the layer level, and that minimizing the L_2 distance between weights is equivalent to aligning these eigenvectors. Furthermore, the paper suggests that STE operates through a different mechanism to achieve low-barrier perturbations.

### Strengths
The study offers a valuable perspective on analyzing LMC, a phenomenon that characterizes the properties of loss surfaces and solutions discovered by stochastic gradient descent (SGD) and its analogs. The results are presented clearly and are substantiated both empirically and, in part, theoretically.

### Weaknesses
A key weakness is the lack of significant novelty in the paper's primary insights. Similar observations have been made in previous works, such as [1] and [2]. These papers also explore Hessian-based barrier approximations and spectral analysis to explain LMC. Although this does not undermine the findings of the current paper, these existing works should be cited and discussed.

Another concern is the transition to per-layer analysis in the discussion of WM. The authors claim that eigenvector alignment results in aligned representations, but this can be challenged. Firstly, the use of the Lipschitz constant in the analysis limits the result to essentially one activation only. When multiple layers are involved, the Lipschitz constant becomes excessively large. Secondly, [3] show that there are often no barriers at the layer level (even when barriers exist at the full network level). Although this could still be explained by eigenvectors, it weakens the connection between similar activations on the level of one layer and the lack of barriers at the full-model level.

The analysis of STE seems rather straightforward, given that this algorithm is designed solely to minimize loss at a single point (the midpoint on the linear path). Unlike WM or AM, it does not aim to identify fully "matching" models. The numerical results in Table 4 are also not fully convincing, as the difference between the barriers found using WM and STE is minimal. The comparison is further weakened by the fact that the initial barriers for STE are much higher than those for WM, making the relative reduction less significant.

Additionally, the paper claims that models trained in the same manner exhibit higher barriers at the midpoint between them. However, in the experiments of [3], it is shown that when one model generalizes better than another, the higher barrier shifts. Therefore, the assumptions in Section 3.2 require further clarification.

Minor Comments:

1 - In Section 4.4, please specify that the results in Appendix H3 and H4 are empirical.

2 - I suggest replacing Figure 6 with Table 4, as low-dimensional visualizations provide an imprecise representation of loss surface properties.

### Questions
1 - Both WM and AM are iterative algorithms. How does the L_2 distance evolve with an increasing number of iterations? It is surprising that the distance shrinkage is nearly identical between WM and AM, given that AM corresponds to layer-wise feature matching, which is closely linked to reduced distances between models.

2 - While the experimental results indicate that the Taylor approximation is imprecise for estimating the barrier, could it be that the models are still relatively close? Since L_2 distance is difficult to interpret in high-dimensional spaces, do you think that including the third term of the Taylor decomposition might help, or that a more precise analysis of the barrier (not just at the midpoint) could yield better insights?

3 - How does your analysis account for the necessity of post-matching fine-tuning, which is particularly critical for networks with batch normalization layers (e.g., Jordan et al., Repair: Renormalizing Permuted Activations for Interpolation Repair)?

### Soundness
3

### Presentation
4

### Contribution
2
