# Implicit Bias in Matrix Factorization and its Explicit Realization in a new Architecture

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 3, 5, 3

## Abstract
Gradient descent for matrix factorization is known to exhibit an implicit bias toward approximately low-rank solutions. While existing theories often assume the boundedness of iterates, empirically the bias persists even with unbounded sequences. We thus hypothesize that implicit bias is driven by divergent dynamics markedly different from the convergent dynamics for data fitting. Using this perspective, we introduce a new factorization model: $X\approx UDV^\top$, where $U$ and $V$ are constrained within norm balls, while $D$ is a diagonal factor allowing the model to span the entire search space. Our experiments reveal that this model exhibits a strong implicit bias regardless of initialization and step size, yielding truly (rather than approximately) low-rank solutions. Furthermore, drawing parallels between matrix factorization and neural networks, we propose a novel neural network model featuring constrained layers and diagonal components. This model achieves strong performance across various regression and classification tasks while finding low-rank solutions, resulting in efficient and lightweight networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the use of a three-factor decomposition X=UDV^T of weight matrices along with a strong weight decay penalty during the training of neural networks. It also includes numerical demonstrations of this method's effectiveness on a small dataset.

### Strengths
The paper is generally well-written and pleasant to read. The three-factor decomposition appears to be effective.

### Weaknesses
 **Limited Novelty:** The reasoning behind the improved compression achieved by three-factor decomposition with weight decay has been previously presented in Proposition 4.2 of [1] and this explanation holds for algorithms including gradient descent. While the original proposition does not enforce a diagonal constraint on D, its proof generalizes to the diagonal case. Could the authors clarify how their approach advances beyond the method proposed in [1]? Notably, [1] utilizes a Frobenius norm penalty rather than a constraint—could the authors discuss the potential benefits of using a Frobenius norm constraint over a penalty if any, considering that the latter might simplify implementation?

**Issues with the Formulation:** The reparameterization approach raises concerns due to its reliance on the constraint ∣∣U∣∣_F≤α, which appears redundant. This constraint can be met by scaling down U and scaling up D, so it does not affect the solution set for the optimization problem. Consequently, optimization problem (4) is not well-defined. If this constraint is intended to influence the solution during the gradient descent update, this section would benefit from revision to avoid presenting (4) with a potentially redundant constraint. 

**Lack of Theoretical Insight**: Since the paper focuses on studying the three-factor reparameterization of a single network layer without nonlinear activation, restricted to gradient descent updates, theoretical insights would be highly expected. Prior work in similar settings with two-factor reparameterization has provided theoretical analysis, which suggests that this problem is amenable to theoretical investigation. Given the existing literature, the paper’s empirical results without theoretical support limit its contribution. Could the authors provide some theoretical analysis on aspects such as convergence rates, optimality conditions, or guarantees on the rank of the solution for their proposed method? How does the theoretical behavior of the three-factor decomposition compare to that of two-factor methods in previous work?

**Limited Numerical Experiments:** The experiments conducted in the paper are limited in scope. Could the authors include comparisons with other state-of-the-art compression methods? Additionally, extending the experiments to larger, more challenging datasets like CIFAR-10 or ImageNet would provide a more comprehensive evaluation of the method's effectiveness and scalability.

### Questions
Please refer to the weaknesses above. I would consider raising the score if these concerns are adequately addressed

### Soundness
2

### Presentation
3

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
The paper looks at the low rank bias of matrix factorization and how to improve upon it. They propose to use a different decomposition of the target matrix and appropriate constraints. The constraints are enforced using a projection. The benefit of the reformulation is shown on a synthetic problem in the paper and additional experiments are provided in the appendix. Moreover, the idea is extended to feedforward neural networks. The paper illustrates using transfer learning that the method is well equipped to prune neurons.

### Strengths
The paper is clear in convening the main idea. The idea of the reformulation is to the best of my knowledge novel (although it is directly based on SVD and projected gradient descent). In addition, the extension to neural networks is new. The method outperforms the BM algorithm on several tasks.

### Weaknesses
As mentioned by the authors deeper matrix factorization has a lower rank bias. The experiment in appendix B5 shows that just the depth can not explain the bias. This shows the importance of the constraints introduced which act as explicit regularization. Thus, comparing it with explicit regularization such as weight decay is needed. For example, a comparison with weight decay on $U$ and $V$ for the formulation $UV$ which also has been proposed as a pruning strategy in:

https://openreview.net/forum?id=880tEHqxzg

Furthermore, there is no theoretical analysis of the formulation. For neural networks, an unconstrained optimization problem would get worse results on a metric than a constrained one based on that metric. Similarly, which of the constrained formulations leads to the best (convex) domain? In appendix A1 it is seen that the BM algorithm gets lower residual than the proposed method at the cost of a higher rank. This suggests that the constrained loss landscape is excluding good minimizers. Therefore, looking at the loss landscape might be a needed addition.

The neural network experiments are of small scale. To show that the reformulation can be used as a pruning method it has to work for larger scale experiments as well. Note that there are multiple pruning methods to compare with:

https://arxiv.org/abs/2002.03231

https://arxiv.org/abs/2402.19262

### Questions
- Could you please compare with weight decay?
- Provide large scale experiments and comparison to pruning benchmarks.
- Motivate the use of particular constraints by theory or loss landscapes.
- Explain the worse performance of the method than the BM algorithm in A1.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this work the authors introduces a matrix factorization model UDU as an improvement over the traditional BM factorization. The authors claim that while BM factorization find approximate low rank solutions depending on small initialization and lr, the UDU model can find exact low rank solutions independent on initialization scale or stable lr. Then, the authors use this factorization on classification and regression tasks and compare with the two layer UV model.

### Strengths
The introduction and the setting of the paper is well established. The proposed method following the lines of past works are clearly written.

### Weaknesses
There are several weaknesses in the technical and novelty section of the paper which is highlighted:

*Formulation is not novel enough*

The authors claim that the proposed UDV model leads to faster convergence to low rank solutions irrespective of lr or initialization. However due to lack of analysis, the authors might have missed the fact the model is a mere extension of deep matrix with depth=3 with additional constraints. It is well known that with increasing depth, the solution recovered becomes more low rank. In other words, the residual singular values of the product matrix gets suppresed by the power of depth leading to attenuation of residual singular values, hence stronger low rank. This has been studied in great detail in https://arxiv.org/abs/1905.13655 and followed up in several papers such as https://arxiv.org/abs/2011.13772 and https://arxiv.org/abs/2406.04112. The current model UDV is a depth-3 model with spectral normalization on U and V and diagonal constraint on D. The lack of comparisons or even mention of larger depth models raises question on the novelty of the formulation. 

*Unclear contributions*

The authors mention the dynamics is divergent but in their experiments they show no experiments where this is the case. The paper they cite https://arxiv.org/pdf/2005.06398 only shows divergent behaviours for matrix completion and not for matrix sensing problems. Furthermore, the arcthitecture proposed is just a 3 layer network with spectral normalization on the first, last layer and diagonal contraint on the middle one. There seems to be nothing new about this contribution.

*Lack of analysis and insights into the model*

As stated earlier, the slight advatange the UDV model seems to exhibit is most probably due to the effect of depth which promotes increased attenuation of singular values. Even applying SVT (singular value thresholding) post training to higher depth factors seems to give quite good compression rate https://openreview.net/pdf?id=1KCrVMJoJ9. The lack of any analysis for gradient flow on this model prevents from understanding why this model has slight advantage over BM factorization.

### Questions
The primary question is how is the proposed model any different from a deep matrix facrtorization setup with depth>3. There are no experiments comparing higher depth. Is there any difference, if so, can the authors compare and provide analysis and insight for gradient flow?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The main contribution of this work is a novel formulation of the matrix factorization, namely the UDV factorization. The authors conduct a series of numerical experiments to reveal that the proposed formulation has a stronger implicit bias towards low-rank solution than the common factorization $X = UV^T$, which then inspires a structure of neural networks that has the potential to be lightweight by pruning.

### Strengths
Overall, this paper is well-written and clearly organized. The idea is simple and straightforward as reflected in Eq. (4). The effect of the proposed formulation is also promising: it clearly exhibits a favor of the low-rank solution, e.g., the singular values decay very fast in Fig. 1. The phenomena observed in this paper definitely give rise to many follow-up questions, e.g., why gradient descent exhibits such a strong preference for low-rank solution compared to other forms of factorization.

### Weaknesses
My major concerns are in three aspects.

1. The underlying mechanism of the effectiveness of the proposed formulation is completely absent in the current version of this paper. As there is not a clear and compelling motivation for why the formulation proposed in this paper is highly effective for gradient descent to obtain a low-rank solution, I think it is crucial to give a corresponding comprehensive explanation or discussion regarding the effectiveness of the UDV decomposition, including the roles of all the explicit constraints. Even an informal explanation would be helpful for understanding the idea behind the formulation, e.g., why impose these explicit constraints and why they are helpful for finding low-rank solutions? Specifically, the authors should provide a theoretical justification for why these constraints lead to low-rank solutions, rather than simply observing the phenomenon in experiments. The current explanation lacks a rigorous analysis of how the constraints interact with the gradient descent dynamics to promote low-rank solutions. It is not sufficient to state that the constraints shrink non-dominant directions; a deeper analysis of the underlying optimization landscape is required.

2. The authors do not carefully discuss the related work Li et al., 2020. Li et al., 2020 clearly showed that gradient flow (GF) prefers low-rank solution by connecting the GF dynamics with Greedy Low Rank Learning (GLRL). In particular, GF implicitly prefers low-rank solution even when $r = d $ for the factorization $X = UU^T, U \in R^{d \times r}$. 

The lack of a comparison between this work and Li et al., 2020 will induce several key questions. Can the theory in Li et al., 2020 be applied to explain results in this paper as UDV decomposition can be viewed as a three-layer GLRL? What will happen in the UDV decomposition if $r = d$? Does it still exhibit a stronger preference of low-rank solution compared to $UU^T$? What will happen if the constraints on the norms are relaxed, e.g., by assuming a large $\alpha$? The authors need to clarify whether the observed low-rank bias is a direct consequence of the constraints or if it arises from the underlying optimization dynamics, as suggested by Li et al., 2020. The paper should also explore the behavior of the UDV decomposition when the constraints are relaxed, to understand the extent to which they contribute to the low-rank bias.

3. The comparison between the proposed formulation and other related factorizations is absent. There are already a variety of formulations for matrix factorization. In particular, if the UDV decomposition can still be applied in the case with $r = d$, then what are the differences between the UDV decomposition and other ones, say LDLT decomposition, and what are advantages and disadvantages of UDV? More specifically, when will UDV decomposition be a better choice than other decompositions? The authors should provide a comprehensive comparison with other matrix factorization techniques, such as LDLT decomposition, and discuss the specific scenarios where UDV is advantageous. The paper should also address the computational complexity of UDV compared to other methods.

Minor comments:

How does the rank of $X$ affect qualities of the recovered solutions for different factorizations? For example, in Fig. 1, if $r$ varies from 3 to 20 ($r = 3$ in Fig. 1), does UDV decomposition still find better solution?

### Questions
1. Why is it crucial to impose explicit constraints on norms and why they are helpful for finding low-rank solutions?

2. Can depth-3 GLRL in Li et al., 2020 explain the proposed formulation in this work? If this is not the case, then what will happen in the UDV decomposition if $r = d$ and does it still exhibits a stronger preference of low-rank solution over $UU^T$? 

3. What are the differences between the UDV decomposition and LDLT decomposition?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Motivated by the literature on the implicit bias towards low rank in matrix factorization, proposes the $UDV^\top$ (and symmetric $UDU^\top$) factorization, which consists of two norm constrained matrices and a diagonal component. Then, empirically shows that this parameterization enjoys a stronger implicit bias towards low-rank solutions, with a weaker dependence on the learning rate and initialization size. Based on the results for matrix factorization, the proposed factorization is evaluated in the context of transfer learning, where it is used to parameterize the linear head of a non-linear neural network base.

### Strengths
For standard matrix factorization, the implicit bias towards low rank usually requires a small initialization. Since the origin is a saddle point, this leads to a tradeoff between optimization time and generalization. I find it interesting that the proposed $UDV^\top$ factorization is demonstrated empirically to enjoy an implicit bias towards low rank even for relatively large initializations (and learning rates). This observation can motivate theoretically studying properties of the $UDV^\top$ factorization.

### Weaknesses
1. The paper does not provide insight, whether theoretical or empirical, as to why the proposed matrix factorization enjoys a stronger low rank bias that depends less on learning rate and initialization, compared to other matrix factorizations.

2. Given the above, the significance of the contributions hinges on the applicability of the factorization and its empirical evaluation. However, the empirical evaluation is limited. Specifically, the considered datasets are non-standard and outdated (MNIST and a couple of tabular regression datasets), and the results do not seem to suggest that the proposed $UDV^\top$ factorization brings any advantage compared to a standard matrix factorization or a simple two-layer ReLU network head, in the considered transfer learning setting.

3. The novelty of reducing network size with SVD-based pruning is limited. Prior work has already suggested compressing neural networks through low rank matrix (and tensor) decompositions (e.g. [1,2,3]). Furthermore, there is no comparison to these or other alternative network pruning and compression techniques, and the utility of the method proposed in this paper is unclear since it only pertains to the last linear classifier head, leaving the base of the network uncompressed.

### Questions
--

### Soundness
3

### Presentation
2

### Contribution
2
