# L-PINN: A Langevin Dynamics Approach with Balanced Sampling to Improve Learning Stability in Physics-Informed Neural Networks

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Physics-informed neural networks (PINNs) have emerged as a promising technique solving partial differential equations (PDEs). However, PINNs face challenges in resource efficiency (e.g., repeatedly sampling of collocation points) and achieving fast convergence to accurate solutions. To address these issues, adaptive sampling methods that focus on collocation points with high residual values have been proposed, enhancing both resource efficiency and solution accuracy. While these high residual-based sampling methods have demonstrated exceptional performance in solving certain stiff PDEs, their potential drawbacks, particularly the relative neglect of points with medium and low residuals, remain under-explored. In this paper, we investigate the limitations of high residual-based methods concerning learning stability as model complexity increases. We provide a theoretical analysis demonstrating that high residual-based methods require tighter upper bound on the learning rate to maintain stability. To overcome this limitation, we present a novel Langevin dynamics-based PINN (L-PINN) framework for adaptive sampling of collocation points, which is designed to improve learning stability and convergence speed. To validate the effectiveness, we evaluated the L-PINN framework against existing adaptive sampling approaches for PINNs. Our results indicate that the L-PINN framework achieves superior relative $L^{2}$ error performance in solutions while demonstrating faster or comparable convergence stability. Furthermore, we showed that our framework maintains robust performance across varying model complexities, suggesting its potential for compatibility with larger, more complex neural network architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a method to adaptively select the collocation points for solving partial differential equations (PDEs) through physics-informed neural networks (PINNs). In PINNs, the selection of the number and location of collocation points impacts the model training and is a well-known issue in the literature. Various methods have already been proposed in the literature, some of which have been compared in this paper. The paper presents a novel method for selecting the collocation points through empirical results and theory. The method named Langevin PINNs aims to focus not only on high-residual-based locations, but also proposes to balance it with selecting locations with low or medium residual values. Overall, the paper's motivation aligns with improving PINNs for simulating PDEs, showcasing its effectiveness on canonical examples.

### Strengths
The paper is easy to follow for non-theory parts and presents a concise overview of the literature in this domain.

The choice of PDEs is diverse and incorporates diverse challenges observed while training PINNs for simulating PDEs.

Sample trajectory plots help observe the method's performance.

### Weaknesses
The rationale for showcasing the method's performance on deep networks is unclear. The advantage gained by the algorithm with a deep neural network is unclear. From Table 1, it seems like the baselines achieve a similar result even with a small network, so why would one opt for a further deep network which is even harder to optimize?

The method is not clearly explained, and it is unclear how to implement the proposed method. It would be appreciated if the authors could provide a more detailed explanation of the method and implementation. 

The discussion on the computational complexity of the baseline methods is presented. However, the manuscript does not compare the proposed method's computational cost with the baselines. Can the authors provide such a comparison of the computational cost? It would help the readers analyze the advantages of the proposed method in terms of computational cost.

Although compared with similar methods, can the authors compare their method with RAR-D presented in [1] or justify why the comparison is/should not be performed?

It is difficult to understand what Fig. 5 shows. It seems like the performance of the proposed method is completely off for a deeper network, contrary to the text in the article.

Although a sensitivity analysis of the proposed method is carried out with different learning rates, the range seems limited. How do the methods perform when trained at an even smaller learning rate?

Limitations:

The proposed method is presented for low-dimensional problems, and validating its performance on high-dimensional problems is not performed. The selection of collocation points in higher dimensions is also a complex problem. The paper does not discuss how the method scales with the rise in dimensionality.

Along similar lines, the method is not performed for multiscale systems of PDEs, which have challenges in choosing the right collocation points.

### Questions
Included along with weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper investigates the limitations of high residual-based methods concerning learning stability as model complexity increases. The authors claim two questions which remain unclear: lack of theoretical analysis of the balancing effect and potential risks of the high residual method. They provide a theoretical analysis and propose Langevin dynamics-based PINN (L-PINN) framework for adaptive sampling of collocation points. The paper also compares the performance between L-PINN and other adaptive sampling methods.

### Strengths
- This paper investigates the limitations of high residual-based methods concerning learning stability as model complexity increases.

- This work provides a theoretical analysis and propose Langevin dynamics-based PINN (L-PINN) framework for adaptive sampling of collocation points.

- The paper is well-written and easy to follow.

- The figures and tables are clear.

### Weaknesses
 - The other adaptive sampling methods (baselines) compared in the paper have some important hyperparameters which could significantly affect the performance. For example, in RAD, $k$ and $c$ are important and improper values of them will fail the method. I cannot find any description about the hyperparameters of the baseline methods. I am concerned about if the baselines are well-trained.

- It is true that applicability to large models is important for these methods. However, Applying simple 1-D PDEs to deep MLPs may not be a good choice.
  - These PDEs do not need such deep MLPs at all. Two or three hidden layers are enough for training the model. 
  - Increasing the depth of MLPs will make the training unstable. 
  - On the other hand, increasing width will also increase the size of the MLPs and will not make the MLPs unstable. The paper could do a comparison on this.
  - It might be more meaningful to adopt other multiple layers like attention layers and Fourier layers instead of deep MLPs. I am concerned about whether L-PINN can be applied to the scenarios that really need large models and still be robust.

- “Adaptive sampling based on residual distribution” is introduced at first and then the “Adaptive sampling focused on high residuals”. Why do the authors claim the latter method is used to address convergence issues of the former method? Actually, RAR can be regarded as a special case of RAD or RAR-D. The RAD method is used to address the issue of RAR focusing too much on high residuals. RAD has less convergence issues than RAR.

- RAD methods have experimentally discussed the “Unresolved questions 2, Potential risks of the high residual method” (lines 136-139). I admit this paper discusses this problem from a different aspect. But I would like to see what is unclarified or unsolved of RAD with respect to “Unresolved questions 2”.

- A period is missing in line 148.

- In figure 4, I suggest adding standard deviations. For figure 4b, it seems L-PINN only performs better when the learning rate is 0.003. This might result from randomness. I would like to see more cases when the learning rate is between 0.002 and 0.004.

### Questions
- “Adaptive sampling based on residual distribution” is introduced at first and then the “Adaptive sampling focused on high residuals”. Why do the authors claim the latter method is used to address convergence issues of the former method? Actually, RAR can be regarded as a special case of RAD or RAR-D. The RAD method is used to address the issue of RAR focusing too much on high residuals. RAD has less convergence issues than RAR.

- RAD methods have experimentally discussed the “Unresolved questions 2, Potential risks of the high residual method” (lines 136-139). I admit this paper discusses this problem from a different aspect. But I would like to see what is unclarified or unsolved of RAD with respect to “Unresolved questions 2”.

- A period is missing in line 148.

- In figure 4, I suggest adding standard deviations. For figure 4b, it seems L-PINN only performs better when the learning rate is 0.003. This might result from randomness. I would like to see more cases when the learning rate is between 0.002 and 0.004.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the relationship between sampling strategies and learning stability in PINNs. The authors provide theoretical analysis showing that sampling methods focused on high-residual points require stricter learning rate constraints for stability, especially with increased model complexity. They present a Langevin dynamics-based PINN (L-PINN) framework that implements balanced sampling proportional to PDE residuals. They vaildate the effectiveness of the proposed sampling method across multiple PDEs, showing that  L-PINN achieves comparable or better relative L2 error performance while maintaining stability across different model complexities and learning rates compared to existing methods.

### Strengths
1.  The proposed method is novel and provides rigorous theoretical analysis of stability issues in high-residual sampling methods. The authors establish clear mathematical connections between sampling strategies and learning rate constraints, backing their theoretical claims with detailed proofs. This helps explain the stability challenges that emerge as model complexity increases.

2. Another strength is the paper's thorough empirical validation. The experiments span multiple representative PDEs (Burgers', Convection, Allen-Cahn). The authors carefully compare their approach against various sampling methods, with comprehensive ablation studies on learning rates and network depth.

### Weaknesses
1.  The assumption 3.1 seems to be too strong for nonlinear PDEs. But I think it is ok for linear PDEs. 

2. Section 5.2's experimental results are dense and difficult to follow - this content could be better organized with supporting details moved to the appendix. 

3.  The authors overlook relevant prior work, particularly PirateNet [1], which addresses similar scaling challenges in training deep PINN models through adaptive skip connections.

### Questions
1. What exactly are the feature vectors being visualized in Figure 6? The paper relies on Assumption 3.1 to express PDE residuals as linear combinations of feature-mapped vectors, but does not clearly define how these feature vectors ϕ(x) are obtained for nonlinear PDEs. Are these simply outputs from hidden layers, or do they incorporate PDE residual information? The authors should provide precise mathematical expressions for the visualized quantities.

2.  If these feature vectors are merely hidden layer outputs without considering PDE residuals, there appears to be a significant gap in the paper's logic. How do these empirical visualizations justify Assumption 3.2 about heavy-tailed distributions of feature vectors that appear in Eq 3.1?  This disconnect between the theoretical framework and empirical validation needs to be addressed.

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
3

### Summary
In this paper the authors highlight some potential shortcomings of residual-based methods for training PINNs and the lack of theoretical understanding thereof. In particular, the authors show theoretically that convergence requires a tighter upper bound on the learning rate. Furthermore, the authors propose a novel algorithm to train PINNs that exploits Langevin dynamics. The main idea is, instead of resampling the collocation points at each iteration (proportionally to the residual loss), to update existing sample position based on residual loss gradient.

### Strengths
- the paper is clearly written and easy to read.
- the idea of using Langevin dynamics to update sample points instead of resampling is elegant.

### Weaknesses
 - while the theoretical contribution on the learning rate is interesting, it seems to be not very useful in practice. Based on the ablation study in Figure 3a and 4a it seems like that the steepness changes only slightly and that picking a smaller learning rate would already help convergence of current methods.
- furthermore, as the authors highlighted in the paper, Langevin dynamics comes at the price of two new additional parameters, which need to be fine tuned. As the authors themselves note, experiments in Appendix E suggest that the choice of these two parameters highly influence the performance of the proposed method.

- Theorem 4.1 relies on an asymptotic limit for reaching collocation sample population. Therefore, I expected that performance would improve as the number of Langevin steps increases. Based on the results in Appendix E, it is hard to see a clear improvement when $l_L$ is increased, and this behavior is particularly true for small $eta$. These results seem to imply that reaching the collocation sample population is not particularly useful in practice.
- It would be interesting to see quantitatively how much the choice of the step size $	au$ in L-PINN affects convergence. It might be useful to have a comparison along the lines of the evaluation in Appendix E for $eta$ and $l_L$, but in this case as $	au$ varies. The current analysis lacks a systematic study of the sensitivity of the method to this parameter.
- Instead of sampling new collocation points to find high-residuals, the proposed approach updates points according to the residual gradient. Intuitively, this seems to be more intense computationally, since sampling can usually be done rather cheaply. The paper lacks a detailed analysis of the computational cost of the proposed approach compared to standard re-sampling methods.
- I find Figure 5 a bit confusing. Could you clarify whether you are showing the error with respect to the solution or the solution itself?

Some minor typos:
- line 88: I would add $R_	heta(x)$ after "residual" such that it is clear what $R_	heta(x)$ is
- line 105: should use a comma instead of a point before "i.e."
- line 148: missing a point before "Additionally"
- line 430: for L-PINN, RAD, R3 and L* "exact solution" should be "predicted solution"
- line 460-466: results fro the Burgers' equation with 8 layers for Random-R and R3 should also be in boldface

### Questions
- Theorem 4.1 relies on an asymptotic limit for reaching collocation sample population. Therefore, I expected that performance would improve as the number of Langevin steps increases. Can you elaborate on why this is not the case based on the results in Appendix E? (the authors note that this behaviour is particularly true for small $\beta$ but also in the other cases it is hard to see an improvement if $l_L$ is increased). Somehow these results seem to imply that reaching collocation sample population is not useful in practice.
- It would be interesting to see quantitatively how much the choice of the step size $\tau$ in L-PINN affects convergence. It might be useful to have a comparison along the lines of the evaluation in Appendix E for $\beta$ and $l_L$, but in this case as $\tau$ varies.
- Instead of sampling new collocation points to find high-residuals, the proposed approach updates points according to the residual gradient. Intuitively, this seems to be more intense computationally, since sampling can usually be done rather cheaply. Did you run any experiments in this direction? 
- I find Figure 5 a bit confusing. Could you clarify whether you are showing the error with respect to the solution or the solution itself?

Some minor typos:
- line 88: I would add $R_\theta(x)$ after "residual" such that it is clear what $R_\theta(x)$ is
- line 105: should use a comma instead of a point before "i.e."
- line 148: missing a point before "Additionally"
- line 430: for L-PINN, RAD, R3 and L* "exact solution" should be "predicted solution"
- line 460-466: results fro the Burgers' equation with 8 layers for Random-R and R3 should also be in boldface

### Soundness
2

### Presentation
3

### Contribution
2
