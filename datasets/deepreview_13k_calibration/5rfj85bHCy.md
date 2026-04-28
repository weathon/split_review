# HyResPINNs: Adaptive Hybrid Residual Networks for Learning Optimal Combinations of Neural and RBF Components for Physics-Informed Modeling

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Physics-informed neural networks (PINNs) are an increasingly popular class of techniques for the numerical solution of partial differential equations (PDEs), where neural networks are trained using loss functions regularized by relevant PDE terms to enforce physical constraints. 
We present a new class of PINNs called HyResPINNs, which augment traditional PINNs with adaptive hybrid residual blocks that combine the outputs of a standard neural network and a radial basis function (RBF) network. 
A key feature of our method is the inclusion of adaptive combination parameters within each residual block, which dynamically learn to weigh the contributions of the neural network and RBF network outputs. 
Additionally, adaptive connections between residual blocks allow for flexible information flow throughout the network. 
We show that HyResPINNs are more robust to training point locations and neural network architectures than traditional PINNs. 
Moreover, HyResPINNs offer orders of magnitude greater accuracy than competing methods on certain problems, with only modest increases in training costs. 
We demonstrate the strengths of our approach on challenging PDEs, including the Allen-Cahn equation and the Darcy-Flow equation. Our results suggest that HyResPINNs effectively bridge the gap between traditional numerical methods and modern machine learning-based solvers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This contribution proposes a method based on residual blocks of hybrid RBF networks and standard MLPs. The method follows the general approach of PirateNets and Stacked networks in that residual blocks are used, but here it appears that there are no gating mechanisms to allow the model to start from a small configuration and progressively add more blocks during training, as in PirateNets.

### Strengths
The method is part of a recent trend in using stacked networks/multifidelity approaches, which appear to improve the accuracy of PINNs.

The contribution of the RBF-NN and MLP is adaptively learned in each block.

The paper is generally well written, with the presence of a small number of typos.

### Weaknesses
There is no discussion of the computational complexity of the proposed approach. Nothing is said about training and inference time in comparison with baseline approaches.

Only two benchmark PDEs are used in the experiments, which is not enough to evaluate the effectiveness of the proposed approach. The chosen PDEs, while relevant, do not fully explore the range of challenges that PINNs face, such as high-dimensional problems or those with highly oscillatory solutions.

It is claimed that the RBF-NN can improve the approximation of sharp transitions in the solution, but no detailed plots or discussion is given in support of that. In particular,  Figure 3 seems to contradict this claim, as the kernels look very smooth.

### Questions
Are the centers and coefficients trained in each RBF-NN?

A few typos need to be corrected:

Eq (4), script D should be script F.

Bottom of page 7: repetition of "smaller".

Appendix A has broken references.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel architecture for Physics Informed Neural Networks (PINNs), combining elements from both deep learning and kernel modeling. Specifically, their architecture, named HyResPINNs implement blocks where a dense layer and a RBF kernel regression are computed in parallel, then combined by an adjustable weighted average. The network also implements trainable residual connections between blocks to help train deeper architectures.

After providing a thorough literature review, the authors formally describe their method, highlighting how the mixed Neural Network/RBF components help the network learn combinations of smooth and high-frequency components of the target function, leveraging the advantages of each method. Their training method also includes a regularization term, penalizing higher contributions of the RBF components in order to limit overfitting to very high-frequency functions. Finally, the authors evaluate their method against several competitive baselines on two PDEs: the Allen-Cahn equation, and the Darcy Flow. Their experiments show HyResPINNs consistently outperforming other methods on these benchmarks.

The authors conclude by summarizing their work, highlighting how their method is able to capture sharp solutions at a manageable computational cost.

### Strengths
### Originality
To the best of my knowledge, this work appears to present novel and interesting ideas. By using a very local RBF kernel in order to assist (but not completely replace) traditional neural network solvers for PINNs, their work aims to help address the well-known spectral bias problem for learning highly oscillatory functions.


### Quality
The paper presents a very interesting idea, and details the HyResPINN architecture in an effective manner. Their experiments are grounded and well-executed, and they compare their method against several competitive baselines. The authors also do a good job of summarizing existing work and highlighting the differences between different methods. I also like their idea of regularizing the weight of the RBF contribution of each block to stabilize the training process.


### Clarity
The paper is overall very well written and clear in its explanations. The literature review at the introduction is thorough, and the required information is presented in a clear and concise manner. The figures are informative and capture the author's arguments well. I particularly like figure 3, where they show kernels learned in HyResPINN are more local than ones from RBFPINNs.

### Weaknesses
### Limited Experiments
In my view, the biggest setback of this paper is the limited range of PDEs considered in the experiments section. The authors do a good job of executing the experiments included in the paper, but only consider the Allen-Cahn equation and the Darcy Flow problem (under different conditions). It is great to see their method work well in these cases, but I believe the paper would greatly benefit from additional experiments using other PDEs, specially ones that challenge existing PINNs architectures. Examples of PDEs that could be considered, in order of difficulty, include: 1) the Poisson equation with different forcing functions (depending on the forcing function this can become a harder problem); 2) Burger's equation, 3) the advection equation; 4) the Kuramoto–Sivashinsky equation, 5) problems using the Navier-Stokes equation, such as lid-driven cavity flow (even with low Reynolds number). Although not all of these PDEs need to be considered, including at least one or two of them (or other suitable problems) could make for a stronger paper.

### Flawed Notion of Training Set Size in PINNs
Another critique I have is on the experiments/plots where they examine the performance of different architectures using different training set sizes (e.g.: figures 7 and 8). Under the Physics Informed framework, although the target function is in principle unknown, we can query the differential operator $\mathcal{F}$ from equation (1) on any point of the input domain using automatic differentiation. This means that it is possible to sample collocation points at will at any given point in the domain, as the authors mention themselves in line 147. In fact, it is always recommended to sample points randomly and independently across the entire input space at each iteration of the training algorithm, effectively meaning that there is unlimited "training data" available for PINN problems. Not only is this approach (independent random collocation points at each iteration) more theoretically grounded by taking advantage of the mesh-less nature of PINNs, it often leads to more accurate and robust performance. This renders the comparison of different "training sizes" meaningless, as it is always possible (and encouraged) to sample new points.


### Other comments/typos that did not affect my score:
- [line 140] In equation (4) the $\mathcal{D}$ should be $\mathcal{F}$ instead, in order to be consistent with equation (1).
- [Figure 1] There is a typo in the diagram. According to the formula from equation (10) and regularization shown in equation (11), it should be $\phi(\alpha^{(l)})$ multiplying $F_R^{(l)}(x)$ and $(1-\phi(\alpha^{(l)}))$ multiplying $F_N^{(l)}(x)$, not the other way around, as it is currently shown.
- [line 215] In equation (10), the activation $\sigma$ is shown to be part of the function $H^{(l)}$, while in the diagram of Figure 1 the $\sigma$ is shown outside of the function $H$. One of these should be changed for the sake of consistency.
- [line 303] There is a mention of an "input block" that lifts the original input to a higher dimension in the diagram, but Figure 2 does not include this block, only the "output block".
- [line 362] Given the initial conditions, the boundary conditions are not satisfied at $t=0$, making this problem ill-posed as it is (you can check that $u_x(0,-1)=2$, while $u_x(0,1)=-2$). This is, unfortunately, a very common mistake in the PINNs community, as this specific benchmark has now become standard. Instead, a very similar solution is given by assuming zero Dirichlet boundary conditions on $x=\pm1$, which makes the problem well-posed and has also been studied in a couple papers. It likely won't make much of a difference in the results, but if possible I would encourage the authors to run this benchmark with Dirichlet boundary, or at the very least add a remark/footnote about the ill-posed nature of the problem.
- [lines 710 + 712] There seems to be a bad reference pointer in the LaTeX file.

### Questions
I list below my questions/suggestions to the authors, in order of how influential they would be towards increasing my score of their submission.

- [**Including More PDEs In Experiments**] As mentioned above, I believe including more experiments with other PDEs would make for a stronger paper. Suggestions for which PDEs to use are detailed in the previous section. I would be open to increasing my score if more experiments are conducted, even if HyResPINNs don't necessarily beat all other baselines on them.

- [**Reconsidering Notion of "training size" For PINNs + Randomly Sampling Collocation Points**] As mentioned in the previous section, I would urge the authors to move away from the notion of "training size" for PINNs, and train networks with freshly-sampled random collocation points at each iteration.

- [**Clarity on Formulation of Residual Connections**] The adaptive residual connections are implicitly defined in line 234, but it would be good do add an extra formula detailing it. Are the $\beta^{(l)}$ parameters constrained in any way, or is it left for the sigmoid function $\phi$ to make the residual connection in the $(0,1)$ interval? If so, initializing the $\beta^{(l)}$ to be 1, as indicated in line 237, leads the residual connection to have strength $\phi(1) \approx 0.73$. Is there a particular meaning over this choice? In a related issue, initializing the $\alpha^{(l)}$ to be 0.5 means that $\phi(0.5)\approx 0.62$, which is not an equal contribution, as mentioned in line 237. Did you mean to say the $\alpha^{(l)}$ are initialized to be 0?

- [**Other RBF Kernel Possibilities**] The choice of using the Wendland kernel seems well motivated to me, and overall a good choice, but it would be great to see the effect of using other kernels in the RBF blocks of HyResPINNs. This could be a valuable ablation to include, either in the main text, or the appendix. Such an ablation could be done for a single PDE, if testing for all problems is too troublesome/time-consuming.

- [**Reporting Computation Time + Hardware**] The authors highlight that HyResPINNs offer significant gains over plain MLPs, with little extra computational cost, but the training time for each method is not reported, to the best of my knowledge. It would also be good to specify the hardware used to run the experiments.

- [**Lack of Code As Supplementary Material**] In order to get a better understanding of the method and evaluate the execution of experiments, it would be good to provide representative code for running experiments as part of the supplementary material, which is currently missing.

- [**References for RBF Networks**] Overall, the authors do a good job at highlighting existing work and providing a careful perspective of current PINNs research. However, there are no references given for RBF networks, either in the introduction or in section 2.2.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work proposes an architecture with the adaptive residual connection between a regular neural network and a Radial bias network. They also demonstrated the effect of the residual connection and adaptivity of the residual connection. The designed architecture has been shown to outperform baselines on Allen-Cahn and Darcy flow.

### Strengths
The authors tackle a significant issue in scientific computation. The architecture they propose is clearly explained in the paper. The authors conducted ablation studies to illustrate the importance of the proposed components. The proposed model demonstrates superior performance compared to baseline models.

### Weaknesses
1. The motivation of the work was “While these deep residual-based approaches show much promise, the increased architectural complexity leads to higher computational costs both in terms of memory and training time—requiring careful selection of training routines to prevent instabilities or poor convergence” - however, authors do not report computation cost and memory requirement for the baselines. Also, from Figure 6, we notice that PirateNet and the proposed model are rather close when compared to training time. The lack of reported computational costs for baseline models makes it difficult to assess the practical advantages of the proposed method, especially given the stated motivation regarding computational efficiency. The similarity in training time between PirateNet and the proposed model, as observed in Figure 6, further undermines the claim of reduced computational overhead.

2. To prove the model's superiority, other PDEs, such as the Navier–Stokes equation, the Grey-Scott equation, the Ginzburg-Landau equation, the Korteweg–De Vries equation, etc., should be used as the baseline. The current evaluation is limited to Allen-Cahn and Darcy flow, which may not fully capture the model's performance across a broader range of PDE characteristics. The absence of more complex PDEs, such as those with turbulent or chaotic solutions, raises concerns about the generalizability of the proposed method.

3. The work replaces the residual connection by the RBF network in PiretNet. This limits the technical novelty of the work. The core architecture appears to be a direct substitution of the residual connection with an RBF network, which does not represent a significant departure from existing methods. The incremental change raises questions about the novelty and impact of this work.

### Questions
1. $\alpha$ in Eq. 10 does not depend on the input, right? Will it be useful if $\alpha$ also depends on the input?

2. Line 217: both sigmoid and RBF functions are denoted by $\phi$. Authors should consider renaming to avoid confusion

3. why the RBF kernel is chosen to be the Wendland C4 kernel? At this point, it seems that the choice is arbitrary.

### Soundness
3

### Presentation
3

### Contribution
2
