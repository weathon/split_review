# Symmetrization of Loss Functions for Robust Training of Neural Networks in the Presence of Noisy Labels

- Decision: Reject
- Scores: 6, 5, 3, 5, 5

## Abstract
Labeling a training set is not only often expensive but also susceptible to errors. Consequently, the development of robust loss functions to handle label noise has emerged as a problem of great importance. The symmetry condition provides theoretical guarantees for robustness to such noise. In this work, we investigate a symmetrization method that arises from the unique decomposition of any multi-class loss function into a sum of a symmetric loss function and a class-insensitive term. Notably, the special case of symmetrizing the cross-entropy loss leads to a multi-class extension of the unhinged loss function. This loss function is linear, but unlike in the binary case, it must have specific coefficients in order to satisfy the symmetry condition. Under appropriate assumptions, we demonstrate that this multi-class unhinged loss function is the unique convex multi-class symmetric loss function. It holds a significant role among multi-class symmetric loss functions since the linear approximation of any symmetric loss function around points with equal components must be equivalent to the multi-class unhinged. Furthermore, we introduce SGCE and α-MAE, two novel loss functions that smoothly transition between the multi-class unhinged loss and the Mean Absolute Error (MAE). Our experiments demonstrate superior performance over previous state-of-the-art robust loss functions on standard benchmarks, highlighting the effectiveness of our approach in handling label noise.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
he paper introduces a new approach for designing robust loss functions for neural network training in the presence of label noise. It proposes a symmetrization method to create symmetric loss functions, yielding novel loss functions such as SGCE and α-MAE. These loss functions demonstrate competitive robustness across various noisy label scenarios, performing well on standard benchmarks.

### Strengths
1- Provides a comprehensive theoretical foundation for the symmetrization method, demonstrating its potential robustness in noisy label environments.

2- Introduces two novel loss functions, SGCE and α-MAE, with empirical validation across multiple datasets and noise types, showing competitive or superior performance.

3- Addresses a key problem in deep learning, where noisy labels can lead to model memorization, with a focus on both theoretical and practical robustness.

4- The introduction of SGCE and α-MAE loss functions showcases a balance between robustness (inspired by the MAE) and performance (closer to Cross-Entropy). This aligns well with existing literature that often emphasizes a trade-off between robustness (e.g., using MAE or its variants) and fitting capacity (e.g., Cross-Entropy), as seen in works by Zhang and Sabuncu (2018) and Wang et al. (2019). However, SGCE and α-MAE offer smooth interpolations between these behaviors with fewer tuning parameters. By allowing practitioners to adjust robustness dynamically, these losses contribute an innovative middle ground not fully achieved by either purely robust or purely performance-driven loss functions in prior research.

### Weaknesses
1- Ambiguity in Theorem 5.1's Uniqueness Proof for Multi-Class Symmetric Loss Functions
The paper claims the uniqueness of the multi-class unhinged loss as the sole convex, non-trivial, non-increasing multi-class symmetric loss function. However, the proof relies heavily on the assumption of "invariance to permutations" without exploring whether alternative symmetry constraints might yield other valid loss functions. Additional exploration into the necessity and sufficiency of this invariance condition could strengthen the claim.

The uniqueness result is also tied to specific choices of additive and multiplicative constants, which can limit generalization. The paper could benefit from detailing if the uniqueness result holds when different constants are applied or providing a clearer justification for these choices.  If invariance to permutations is essential to achieve the robustness and symmetry desired, the authors should provide a more detailed justification. They could demonstrate why this particular form of symmetry best aligns with robustness under label noise or show through theoretical or empirical comparisons that other symmetry constraints yield suboptimal results.

2- Over-Reliance on Assumptions in Proposition 5.2
Proposition 5.2 requires the loss function to be both non-increasing and symmetric with respect to permutations at specific points. This assumption is restrictive and could limit the practical applicability of the result, especially when the conditions on gradients may not hold in practical, noisy scenarios. It may be beneficial to relax these assumptions or provide an empirical analysis of their validity in real-world applications.

The discussion around local symmetry might also benefit from examining cases where symmetry does not hold uniformly across the input space. Providing examples or simulations where these assumptions are invalidated would help to contextualize the limitations of the theorem.

3- While the linear approximation of the cross-entropy loss around specific points is theoretically compelling, there is limited empirical evidence provided to demonstrate the robustness of this approximation in practice. Testing how this approximation affects model behavior under various noise conditions could clarify its practical utility and limitations. 
The authors could empirically test the linear approximation under different noise settings. including but not limited to:
Uniform noise,
Class-conditional noise,
Asymmetric noise,
For each noise type, it would be useful to assess metrics like the model’s convergence rate, generalization on clean data, and stability over training epochs. This analysis would give a more concrete understanding of how the linear approximation affects learning dynamics in noisy settings.

4-The introduction of β-smoothness in Proposition 5.3, which bounds the size of the linear approximation's remainder, lacks a clear justification regarding how this affects overall model performance and robustness. Furthermore, the relationship between β-smoothness and generalization to unseen data remains unexplored. Further discussion on the implications of β-smoothness and empirical verification could substantiate the proposition.
Additionally, the selection of β and its sensitivity to model hyperparameters (e.g., regularization strength, learning rate) could impact the robustness claim, an area not thoroughly investigated.

5- The interpretation of the unhinged multi-class data centroid as a kernel learning component is intriguing but underdeveloped. The appendix briefly introduces this concept without exploring its potential applications in kernel-based methods or examining how the centroid relates to noise robustness.
The explanation could be made clearer by providing more context or examples of how this centroid could be leveraged in practical kernel learning setups. Additionally, the generalization to non-linear hypothesis spaces could be further clarified.
The relationship between the centroid and noise robustness should be elaborated. For instance, if the centroid can help in characterizing the loss landscape under noisy conditions, this could provide a basis for developing noise-resilient learning frameworks. An empirical investigation showing the impact of varying centroid values on robustness would also be informative.

Comparing this approach with other centroid-based noise-robust methods, such as loss decomposition and centroid estimation (Ding et al., 2022), would help in positioning the proposed method within the broader context of robust learning.

6-Proposition 4.1 introduces a decomposition method to achieve a symmetric loss function. However, the paper does not thoroughly address potential limitations or boundary cases where this decomposition might fail or yield unintended behavior, such as in highly imbalanced datasets.
While the uniqueness claim in the decomposition is theoretically interesting, the paper does not fully explore alternative decomposition approaches that might yield other symmetric loss functions. Additional comparative analysis on the benefits of this specific decomposition relative to others could enhance understanding.

7- The symmetric noise condition discussed in Appendix A, while foundational, could benefit from more discussion about its limitations. Real-world noise distributions are rarely perfectly symmetric, and a broader exploration of how deviations from symmetry impact the loss function's robustness would add practical relevance.
The appendix could also benefit from incorporating empirical data on how well this assumption holds in real-world datasets or from proposing adjustments to handle non-symmetric noise more effectively.

8- In Appendix G, the implementation details, particularly regarding Euclidean normalization and batch normalization for stability, hint at potential computational overhead. However, the appendix lacks an in-depth analysis of these computational costs, especially for large-scale datasets or real-time applications.
Additional experimentation showing the computational impact of these normalization techniques and alternative methods for improving numerical stability would be valuable.

9- In Appendix B, Proposition B.1's explanation of binary symmetric loss decomposition is somewhat unclear, especially regarding the relationship between odd and even Taylor series coefficients. More detailed explanations and illustrative examples would make this complex derivation more accessible.
Furthermore, extending this analysis to illustrate how the concept translates (or fails to translate) to the multi-class case would enhance understanding and show the limitations of applying binary assumptions to multi-class problems.

### Questions
1- How does the proposed symmetrization method compare with other noise-tolerant loss functions in terms of theoretical robustness and generalization?
Given the vast literature on noise-tolerant loss functions, comparing symmetrization with other loss correction approaches, such as the active-passive loss framework or transition matrix estimation, could provide insights into when and why this method might outperform or underperform. How does symmetrization fare in scenarios with non-uniform or class-conditional noise, which are common in real-world datasets?

2- What is the impact of the proposed loss functions on generalization performance under non-ideal noise conditions?
The paper’s symmetrization method assumes uniform noise distribution. However, real-world datasets often exhibit more complex noise patterns (e.g., class-conditional or asymmetric noise). Can the authors empirically or theoretically verify the method’s robustness and generalization capabilities under such more complex noise settings? How might the proposed loss functions be modified to account for non-uniform noise?

3- Could alternative constraints besides “invariance to permutations” produce comparable or even superior symmetric loss functions?
The uniqueness of the multi-class unhinged loss relies on the specific constraint of invariance to permutations, yet other forms of symmetry might yield alternative robust loss functions. For instance, can partial or relaxed symmetry conditions, such as those used in semi-supervised learning, yield alternative loss functions that retain noise robustness? Is there theoretical or empirical evidence that such alternatives might be beneficial?

4- How sensitive are SGCE and α-MAE to variations in hyperparameters across diverse model architectures and datasets?
Robustness in noisy label settings often depends on careful tuning of hyperparameters, and the success of SGCE and α-MAE could vary across different architectures (e.g., convolutional neural networks vs. transformers) or task-specific datasets. What guidelines or empirical evidence can the authors provide for tuning these parameters effectively across different architectures? Is there a general heuristic or principle to guide practitioners in tuning α for α-MAE?

5- What insights do the linear approximation and β-smoothness properties provide for real-world optimization stability and convergence?
β-smoothness in Proposition 5.3 is noted to bound the approximation’s remainder, but the implications for optimization stability, convergence speed, and computational efficiency remain unclear. Are there insights from optimization theory or empirical results that can validate these assumptions? Specifically, does β-smoothness impact the rate of convergence in practice, and does it allow for more stable training trajectories in noisy settings?

6 - How does the unhinged multi-class data centroid introduced in Appendix C compare with centroids used in clustering algorithms or kernel-based methods?
The multi-class unhinged data centroid shares conceptual similarities with centroids in clustering algorithms or kernel learning. Could a comparison be drawn here, especially in terms of interpretability and robustness to outliers? Additionally, would this centroid calculation be feasible in settings with limited computation resources, or could it be approximated?

7 - Can symmetrization be extended or adjusted to support the robust training of imbalanced datasets?
Many practical datasets contain imbalances across classes, which can exacerbate the effects of noise. Could the symmetrization method accommodate such scenarios, possibly by adjusting for class frequencies or by incorporating additional regularization terms?  How does the multi-class unhinged loss perform under varying levels of class imbalance, and are there empirical or theoretical justifications for any observed effects?

8- How does the proposed symmetrization framework align with recent advances in self-supervised or unsupervised learning under label noise?
With recent progress in self-supervised learning, particularly for handling label noise by avoiding reliance on labels entirely, it would be valuable to contextualize this symmetrization approach. Are there synergies between the proposed loss functions and self-supervised frameworks? Could the symmetrization approach be adapted or serve as a regularization term within self-supervised pretraining paradigms?

9- What are the theoretical implications of Proposition B.1’s Taylor series-based decomposition for the binary case, especially regarding generalization to non-linear classifiers?
Proposition B.1’s odd/even decomposition for the binary case through Taylor expansion is interesting but highly idealized. How does this decomposition behave in settings where non-linear classifiers (e.g., deep networks) introduce significant non-linearity? Could this decomposition help develop a more general approach for generating symmetric loss functions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript proposes an novel symmetrization method for robust learning in the presence of label, derived from the decomposition of any multi-class loss function into a sum of a symmetric loss function and a class-insensitive term. The authors introduce the SGCE and $\alpha$-MAE functions, which provide a smooth interpolation between the multi-class unhinged loss and the Mean Absolute Error (MAE). Overall, the paper presents a straightforward and effective method for symmetrizing any loss functions, contributing both interesting theoretical insights and experimental validation of the proposed method. However, I feel that significant writing issues detract from the clarity and accessibility of the content. Reorganizing the presentation of results could enhance the paper’s readability and overall acceptability.

### Strengths
- This paper presents a simple and efficient method for symmetrizing loss functions to handle label noise.
- The experimental results are comprehensive and support for the proposed method.

### Weaknesses
- The writing quality is insufficient and may not meet the standards required for acceptance.
- The authors should give the definition of $\tau(y)$ for $y\in\{1,...,C\}$ in Definition 3.2, as $y$ does not have $C$ elements.
- A definition of one-hot vector $e_y$ is missing in Lines 224-225.
- The authors’ statement in Lines 238-241, claiming that “the unhinged loss function is robust by maintaining larger gradients for correctly classified examples, while MAE is robust by reducing the gradient of incorrectly classified examples,” requires further clarification. Both methods, in fact, focus on increasing  $z_y$  while reducing $z_k$ for $k\neq y$., so an explanation for this distinction is warranted.
- The symmetrization of the cosine similarity loss could be interpreted as an equivalent form of MAE when the softmax layer is replaced by an $\ell_2$-normalization layer.
- “The unhinged” should likely be revised to “The unhinged loss” in Lines 248-249 and Lines 250-251.
- Why using $s(z)-y$ in Lines 277-278 instead of $s(z)-e_y$?

### Questions
Some questions relating to the weaknesses:
- How does the symmetrization method handle cases where class imbalances may impact the performance of the symmetric loss function?
- Could the authors elaborate on the decision to use SGCE and $\alpha$-MAE specifically for interpolation between multi-class unhinged loss and MAE? Are there alternative interpolative methods that could be considered?
- How does this approach compare in terms of computational complexity to existing symmetrization techniques for multi-class loss functions?
- In practical applications, how sensitive is the proposed symmetrization method to the choice of hyperparameters, and are there any guidelines for optimal tuning?
- Could the theoretical results be more clearly linked to the observed experimental outcomes to strengthen the argument for the method's effectiveness?

### Soundness
2

### Presentation
1

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
This paper proposes a symmetrization method for multi-class loss functions, which can decompose a loss function into a sum of a symmetric loss function and a class-insensitive term. Based on this method, new robust loss functions (SGCE, $\alpha$-MAE) are proposed. The authors also provide theoretical analyses of multi-class unhinged loss. To verify the effectiveness of the proposed loss functions, the authors conduct experiments on several benchmark datasets (CIFAR-10, CIFAR-100, and WebVision).

### Strengths
1. The research topic, training neural networks in the presence of noisy labels, is interesting.
2. The author conducted sufficient experiments to verify the effectiveness of the proposed method.

### Weaknesses
1. Some definitions of crucial concepts are important for this paper, such as symmetry condition (proposed in [1]). The authors did not define them clearly in the paper.
2. A claim is wrong in Lines (184-185). The standard cross-entropy loss is not permutation-invariant. For example, the predition of network is $z=[0.2,0.5,0.3]$, the one-hot target is $y=[0,1,0]$, the corresponding cross-entropy loss is $L(z,y)=-\log(z_2)=-\log(0.5)$. Now, applying the permutation $\tau(1)=3,\tau(2)=1,\tau(3)=2$. The permuted predition is $\tau(z)=[z_3,z_1,z_2]=[0.3,0.2,0.5]$, the permuted target is $\tau(y)=[1,0,0]$, the cross-entropy loss after permutation is $L(z,y)=-\log(\tau(z)_1)=-\log(0.3)$. Obviously, $-\log(0.3)\neq-\log(0.5)$. Similarly, the linear loss: $L(z,y)=-z_y$ is not permutation-invariant.
3. The proposed method in Proposition 4.1 changes the original loss: $L^{sym}(z,y):=L(z,y)-\frac{1}{C}\sum_{k=1}^CL(z,k)$. Can the author prove whether the minimizer of $L^{sym}(z,y)$ is the same as that of $L(z,y)$?
4. The theoretical analyses in Section 5 are about the multi-class unhinged loss. The readers could be more interested in the properties of the loss $L^{sym}(z,y)$.
5. The writing and organization of this paper are poor. For example, the introduction lacks sufficient detail, and the related work is overly detailed and lengthy.
6. The location of the experiment results (Tables 1-4) is inappropriate. These tables should be in the experiment section or in the front of the experiment section.

**References**

[1] Ghosh, Aritra, Himanshu Kumar, and P. Shanti Sastry. "Robust loss functions under label noise for deep neural networks." *Proceedings of the AAAI conference on artificial intelligence*. Vol. 31. No. 1. 2017.

### Questions
Please see the Weaknesses.

### Soundness
2

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
5

### Summary
This paper focuses on the robust loss functions in noisy label learning. Since the symmetric loss is proved to be robust to noisy labels, the authors propose a method to symmetrize the loss function. The corresponding theoretical analysis is provided, including a proof that the multi-class unhinged loss is the only convex multi-class symmetric loss. The authors use three loss functions, and evaluate on CIFAR-10, CIFAR-100 and WebVision.

### Strengths
1. The authors use a  clever way to achieve symmetric condition.
2. This paper provides a reasonable theoretical analysis.
3. The authors make comparisons on different noises, including symmetric noise, asymmetric noise, human-annotated noise, and real world noise.
4. Three new robust loss functions are proposed.

### Weaknesses
1. The fonts used don't seem to conform to the ICLR format. Futhermore, I think the symbol definitions are confusing. The lowercase characters in the paper can represent both vectors and constants, as well as elements of vectors. A clearer distinction would have been better.
2. Although the authors' method implements the symmetric condition, I noticed that in the actual experiment the authors used a lot of tricks, including Euclidean normalization and batch normalization for $z$, and weight decay adjustment. However, baselines[1, 2] do not need to use these tricks.
3. The authors did not perform experiments according to the uniform experimental setting of baselines[1, 2]. Instead, they search for optimal parameters and optimal weight decay for their own method, but only for weight decay without optimal hyperparameters for baselines. A fairer way to experiment is to refer to [3], or to use the uniform experimental setting of baselines[1, 2].
4. No code is provided for this work. It would be better to provide code about Euclidean normalized and batch normalized multi-class unhinged loss, etc.

### Questions
1. The author mainly analyzes multi-class unhinged loss in theory, but uses Euclidean normalized and batch normalized multi-class unhinged loss in practice. After using normalization, does the proposed theory still hold？ 
2. Is there any corresponding theoretical analysis about the use of  Euclidean normalization and batch normalization？
3. Since the unhinged loss is already symmetric and convex, why is there a trade-off between it and MAE? Why does such an operation improve performance? Is there any theoretical analysis？
4. Since SGCE and $\alpha$-MAE are both a trade-off between unhinged and MAE, is there a theoretical explanation for why $\alpha$-MAE performs better in most cases?
5. Can you provide the results in the same experimental setting as baselines [1, 2] ?

[1] Normalized Loss Functions for Deep Learning with Noisy Labels, ICML 2020.

[2] Asymmetric Loss Functions for Learning with Noisy Labels, ICML 2021.

[3] Generalized Jensen-Shannon Divergence Loss for Learning with Noisy Labels, NeurIPS 2021.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper,  a symmetrization method for designing robust loss functions to handle label noise is proposed as mainly illustrated in Section 4. this loss function.  This may be regarded as a good extension of the binary unhinged loss in the multi-class case. The symmetrization of the generalized crossentropy loss (SGCE) and the  alpha-MAE  are introduced with some experimental validation.

### Strengths
1. The paper introduced  a symmetrization method for designing robust loss functions to handle label noise in the multi-class setting.  It is a good extension of the unhinged loss in binary case to multi-class cases. 

2. Various properties of the multi-class unhinged loss are discussed.

### Weaknesses
1. Many of the properties of the multi-class unhinged loss function seem to be straightforward and may not offer substantial novelty.  I have not checked very step of the proofs and was not able to judge how significant the proof techniques are. 

2. While the introduction of the symmetrization method for designing robust loss functions in the multi-class setting is intriguing, the results feel somewhat incremental and lack sufficient depth. For instance, in the binary case, there are established results in binary classification that show how the design of robust loss functions to handle label noise relates to statistical consistency. I would encourage the authors to exploring this connection explicitly which will increase the impact and significance of the paper. 

3. The presentation could be improved. For example, immediately after Definition 3.1, the authors mention that the form of symmetry between classes differs from the notion of symmetry related to noise robustness. However, in Section 4, the paper states, "to decompose a loss function into a sum of a symmetric loss function and a class-insensitive term," yet the definition of a symmetric loss function has not been provided.  I would suggest the authors to clearly define the symmetric loss function before Section 4.   

The writing seems to assume that readers already know very well the literature on robust (symmetric) loss functions for handling label noise. For instance, there are various key terms such as robust loss functions based on the symmetry condition, symmetric loss function, symmetrization of the cross-entropy loss, unhinged loss.  It would be beneficial to the readers to properly define and introduce them in a more logical order before mentioning them.

### Questions
See the weakness part

### Soundness
2

### Presentation
3

### Contribution
2
