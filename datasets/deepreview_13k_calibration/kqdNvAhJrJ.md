# AC-PKAN: Attention-Enhanced and Chebyshev Polynomial-Based Physics-Informed Kolmogorov–Arnold Networks

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
This paper introduces AC-PKAN, an advanced framework for Physics-Informed Neural Networks (PINNs) that integrates Kolmogorov–Arnold Networks (KANs) with Chebyshev Type-I polynomials and incorporates both internal and external attention mechanisms. Traditional PINNs based on Multilayer Perceptrons (MLPs) encounter challenges when handling complex partial differential equations (PDEs) due to vanishing gradients, limited interpretability, and computational inefficiency. To address these issues, we enhance the model from both external and internal perspectives. Externally, we propose a novel Residual Gradient Attention (RGA) mechanism that dynamically adjusts loss term weights based on gradient norms and residuals, thereby mitigating gradient stiffness and residual imbalance. Internally, AC-PKAN employs point-wise Chebyshev polynomial-based KANs, wavelet-activated MLPs with learnable parameters, and internal attention mechanisms. These integrated components improve both training efficiency and prediction accuracy. We provide mathematical proofs demonstrating that AC-PKAN can theoretically solve any finite-order PDE. Experimental results from five benchmark tasks across three domains show that AC-PKAN consistently outperforms or matches state-of-the-art models such as PINNsFormer, establishing it as a highly effective tool for solving complex real-world engineering problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new architecture, the AC-PKAN, which improves on previous variation of Kolmogorov-Arnold Neural Networks thanks to its replacement of the traditional B-spline layers with the novel Chebyshev type-1 polynomial layers. It also introduces an external mechanism, the RGA (residual and gradient based attention), which allows an adaptive reweighting of the various loss components considered and ensures an efficient optimization. The performance of the model is evaluated for various function and PDE solution approximation cases, and an ablation study is proposed.

### Strengths
- This contribution innovates by proposing a novel architecture based on the Chebyshev type 1 polynomials to replace the traditional B-splines, as well as an adaptive reweighting technique to control the physics loss
- The newly proposed layer has non-zero derivatives of all orders, a property backed  by a theoretical proof
- The benchmarks show that AC-PKAN offers state-of-the-art (or close to) performance on all cases studied, which include complex PDEs and non-trivial domains
- An ablation study showcases the importance of all the modules introduced in this new architecture, including the RGA

### Weaknesses
While the claims are solidly backed by theory and numerical results, the paper sometimes lacks descriptions to aid reader comprehension.
The contribution could provide more explanations for the reason why certain architectural choices are utilized. The role of  the wavelet activation function is one of them.
The paper could be more clear and provide at least some intuition of the explanation for why the Chebyshev type 1 polynomials lead to an increased performance and lower memory cost in comparison to the B-spline.

### Questions
Could you provide a more in depth explanation (even intuitive) about (see weaknesses):
- the role of the wavelet activation function and how it helps with performance
- the reason why Chebyshev type 1 polynomials improve upon B-splines

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
The paper introduces several new mechanisms to address the failure of PINNs and difficulties of PINNs to extend to higher complexities.The paper proposes the residual gradient attention mechanism to dynamically adjust the loss coefficients of residuals and gradient norms.   It also improves the Kolmogorov-Arnold Networks with enhanced attention and a learnable Wavelet function. The paper showcases that AC-PKAN improves over KANN and PINN on complex function interpolation. It also achieves comparable and superior results to SOTA PINN variants in solving PDEs. The authors show the effectiveness of AC-PKAN components by a series of ablation studies.

### Strengths
(1) The paper is written with a logical flow and clear exposition, and the authors provide several algorithm pseudocodes that make the algorithm easy to understand.

(2) The empirical performance of AC-PKAN is promising, demonstrating improvements across a range of benchmark tests and scenarios where traditional approaches like PINNs and KANs face challenges.  

(3) The authors have proposed several novel modifications to both PINNs and KANs,  to addresses several limitations inherent to PINNs and KANs, such as scalability with respect to equation complexity, convergence stability, and generalizability across various domains.

(4) The authors provide the mean values of GRA weights and RBA weights over epochs in the experiment section. The increase of the GRA weights and significant difference between GRA and RBA justifies the authors' claim that balanced attention will resolve the gradient stiffness problem.

(5) The Loss Landscape Analysis, illustrations of fitting complex functions and plots of loss of PDE fitting are useful to understand how AC-PKAN performs in various setting. 

(6) The authors provide a detailed experiment setting and model parameter analysis, allowing for replicating the paper findings.

### Weaknesses
 (1) While the memory is discussed within the appendix, the paper fails to discuss the running time of each algorithm to fit the PDEs and complex functions in the experiments. It’s unclear to the readers how much different architectures such as KAN, Cheby2KAN, MLP and transformer trades off time with accuracy and efficiency.

(2) The ablation study only discusses the drop of algorithm effectiveness by removing the key components of the AC-PKAN. However, many of the design choices can be adapted to other algorithms, for example, the RGA/RBA attention updates can work with MLP PINNs and First-kind Chebyshev KAN Layer could also work seamlessly with the PINN objective. Without analysis on each individual component, it is hard to see how each component could improve the algorithm performance.

(3) Proposition 1 is a bit vague, it is hard to know what "positive integer N" means in the theorem without having to look at the detailed proofs in the appendix.

(4) Moreoever, while the authors claim that AC-PKAN is able to approximate the PDEs with higher orders and higher dimensionality, there is lack of experiment showing such effect.

(5) For the total loss under the RGA mechanism in Equation 8. The authors state that they would set the scaling factors to 1. However, the scaling factor could be set to larger number, and the authors could remove the logarithmic transformation in the loss function. It may be better to demonstrate the effect of scales vesus setting log transformation to justify the design choices.

### Questions
(1) In Algorithm 1, the compute gradients and modify parameters uses single SGD, could we apply the RGA Mechanism with other gradient update techniques such as Adam or AdamW?

(2) PINN suffers from the curse of dimensionality of high-dimensional spaces, does AC-PKAN resolve such issues on multi-dimensional PDE equations? The current experiment focuses all on 1-D PDEs and complex equations.

(3) Proposition 1 states that the attention mechanism and wavelet activations in AC-PKAN ensure the output function has non-zero derivatives of all orders. Can a simpler architecture, like an MLP with sinusoidal activations, also guarantee non-zero derivatives in its output?

(4) The ablation study reveals that removing the linear layer has the most significant impact on AC-PKAN’s performance. Could the authors clarify why this occurs? Why does the linear layer play such a crucial role in AC-PKAN, while other PINN methods do not require similar linear projections?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces AC-PKAN, an advanced Physics-Informed Neural Networks (PINNs) framework that integrates Residual Gradient Attention (RGA) and point-wise Chebyshev polynomial-based (KANsCheby1KAN) to address the limitations of traditional PINNs in solving complex partial differential equations. Experimental results demonstrate that AC-PKAN consistently outperforms or matches state-of-the-art models, establishing it as a highly effective tool for engineering applications

### Strengths
1. This article conducts quite a few experiments to demonstrate the method's effectiveness compared to other KAN and MLP.
2. This paper's presentation is very clear, and the main idea and proposed optimization are easily understood.

### Weaknesses
1. In my opinion, RGA and Cheby1KAN seem to be separated from each other, and there is a feeling that two methods were found to sew the optimized PINN and KAN respectively. It is necessary to explain whether Cheby1KAN is more effective for your proposed RGA compared with other network layers through theory.
2. In the experiment part, only the comparison of different KAN and MLP used by PINN, more comparisons should be added such as FNO-related methods.

### Questions
1. Is the dataset trained in different batches, if there is, how can we calculate the maximum Loss of the entire training data in Equation 4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces AC-PKAN to fit functions and solve PDEs. The proposed AC-PKAN method employs a Residual Gradient Attention (RGA) mechanism to dynamically adjusts loss term weights, wavelet-activated MLPs with learnable parameters, and Chebyshev polynomial
Based KANs to improve training efficiency and prediction accuracy. The paper is well-written. The method is effective compared to existing methods on five benchmarks.

### Strengths
1. The method AC-RKAN is original. Ablation studies show the necessity of each module of AC-RKAN.
2. The paper is well-written. The theoretical insight is interesting and the experiments are rich, demonstrating the effective of the method.
3. The AC-RKAN method can make a timely contribution to the community of physics-informed machine learning.

### Weaknesses
1.The experiments and the comparisons are not challenging. For the 1D-wave case, the author claimed PINNsFormer has a relative l2 norm 0.32 in Table 2, but Wang 2022 (fig.6 of their paper) has trained PINN for this case to achieve a relative l2 norm 1.7e-3, which is the same order to AC-KAN. The other PDEs are also simple 2d Poisson eq. Although with Heterogeneous Problem and Complex Geometry, the solution is smooth, and are easy to solve by simple traditional numerical methods such as finite element methods. Challenging PINN problems Wang 2023 such as the Kuramoto–Sivashinsky equation with chaotic behavior，Lid-driven cavity flow (Re=3200)， Navier–Stokes flow in a torus or around a cylinder, are not reported in the paper.

[a]Wang S, Yu X, Perdikaris P. When and why PINNs fail to train: A neural tangent kernel perspective[J]. Journal of Computational Physics, 2022, 449: 110768.
[b]Wang S, Sankaran S, Wang H, et al. An expert's guide to training physics-informed neural networks[J]. arXiv preprint arXiv:2308.08468, 2023.

2.The method introduction is expatiatory, from page3-7. A concentration of the method introduction is recommended and more theoretical insights and experiments can be discussed in the main text.

### Questions
See in the weakness

### Soundness
2

### Presentation
3

### Contribution
2
