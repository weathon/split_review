# PDE-constrained Learning with Multi-time-stepping for Accelerated Fluid Simulation

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6, 3, 8, 6

## Abstract
Solving partial differential equations (PDEs) by numerical methods meet computational cost challenge for getting the accurate solution since fine grids and small time steps are required. Machine learning can accelerate this process, but struggle with weak generalizability, interpretability, and data dependency, as well as suffer in long-term prediction. To this end, we propose a PDE-embedded network with multiscale time stepping (MultiPDENet), which fuses the scheme of numerical methods and machine learning, for accelerated simulation of fluid flows. In particular, we design a convolutional filter based on the structure of finite difference stencils with a small number of parameters to optimize, which estimates the equivalent form of spatial derivative on a coarse grid to minimize the equation's residual. A physics block with a 4th-order Runge-Kutta integrator at the fine time scale is established that embeds the structure of PDEs to guide the prediction. To alleviate the curse of temporal error accumulation in long-term prediction, we introduce a multiscale time integration approach, where a neural network is used to correct the prediction error at a coarse time scale. Experiments across various PDE systems, including the Navier-Stokes equations, demonstrate that MultiPDENet can accurately predict long-term spatiotemporal dynamics, even given small and incomplete training data, e.g., spatiotemporally down-sampled datasets. MultiPDENet achieves the state-of-the-art performance compared with other baseline models, with over 5$\times$ speedup compared to classical numerical methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose to learn fluid simulation with multi-step predictions.

### Strengths
- Using numerical integrator with neural networks is an interesting approach.
- The reported experimental results show improvement over the reported baselines.

### Weaknesses
 - The multi-step prediction naturally makes the network to be much deeper. For example, the computation will go through at least 4x layers with 4 micro step prediction, albeit the weight sharing. However, the benchmarked baselines are only single networks which are not as deep. It has been shown that using more stacks of shared-weight networks can greatly increase the performance [1, 2]. Given the big improvement in the reported metrics, the authors need to compare their methods with stronger baselines with more layers. Specifically, the comparison should involve baselines with a similar number of effective layers, even if the weights are shared, to isolate the impact of the multi-step prediction approach.

 - Another related point is regarding the numerical integration. The numerical integration is naturally similar to the simple residual network. The authors need to benchmark the proposed solution with a network with the same amount of network blocks but without using the RK4 integration, e.g., by stacking them or using the simple residual connections. This comparison should control for the number of layers and the overall network depth, to determine if the performance gains are due to the specific numerical integration scheme or simply the increased depth of the model. It is crucial to understand if the observed improvements are a result of the RK4 integration itself or merely an effect of the increased computational steps.

 - Since the paper focuses on flow problem, it can benefit from testing larger flow benchmarks, such as PDEArena [3]. The current benchmarks are relatively small and may not fully demonstrate the scalability and robustness of the proposed method. Testing on more complex and larger-scale flow problems would provide a more comprehensive evaluation of the method's capabilities.

### Questions
- For Eq. 3, does it mean that inside each PDE block there will be multiple network evaluation to perform the RK4 integration? E.g., there will be multiple steps for each micro step.

- For Eq. 2, how are the derivative quantities also predicted by the network at the coarser grid? Where is the poisson block defined in Eq. 2?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes an interesting hybrid neural learner for fluid problems. The neural network builds the PDE in the pipeline, instead of using it as a loss function. A time-stepping scheme is applied explicitly instead of applying the NN directly in an autoregressive fashion.

### Strengths
The method proposed is pretty straightforward to implement and uses the physics (PDE) in a good way, not just simply throwing the PDE residual into a loss function and calling it for a day. The numerics are competitive among end-to-end models.

### Weaknesses
 - The writings are pretty bad, there are many typos, e.g., "spatialemporal". The word choices and phrasing definitely read pretty weird at places, for example, the term "promotion" in Table 2. I felt that this paper could really use proof-reading from a native speaker.
- As someone from a background of many years of training in numerical analysis, I would not name the NN in consideration a "PDE-constrained" NN. The reason is that in traditional numerical methods, when talking about "constraint", it refers to the fact that the method of interest imposes the constraint ***exactly*** up to the machine eps. For example, the divergence-free constraint in NS.
- These micro and macro blocks $M_iNN$ and $M_aNN$ are not properly defined. After digging into the figures (S1 to be specific) and Section 3.2.4, I still do not know what their exact architectures are. For example, what hyperparams are used in the FNO and UNet? Why not use UNet as $M_iNN$ and FNO as $M_aNN$?
- $\mathcal{B}$ is not clearly defined either. Given the form of (S8), one would guess it is $\mathcal{F}$ plus the external forcing but (S6) states otherwise.
- The Poisson block is essentially a pressure projection scheme, which is nothing new and has been introduced back by Chorin in 1967 and by Shen later in 1980s. 
- The ablation lacks some in-depth studies, examples include: 
  - in theory, making the FD operator as learnable filters sounds pretty good, but do the learned parameters actually replicate the FD operator and have a truncation error of four-order accuracy?
  - instead of simply removing different components of the model in 4.6, I think it is better to compare the RK4 used with another time stepping scheme (with a less truncation error order) to test whether it is the RK4 adopted really works, or the pipeline is really robust with respect to any time-stepping schemes.
- Some missing references on making the FD stencil learnable as a convolution filter, e.g., a paper by Kossaczká-Ehrhardt-Günther and arXiv:2201.01854. There is also arXiv:2003.09573 on using NN as correction to a time stepping scheme.

### Questions
I don't understand "FD method can yield inaccurate derivatives on sparse grids." What does "sparse grids" mean here?

### Soundness
3

### Presentation
2

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
This paper presents MultiPDENet, a physics-constrained neural network framework developed to accelerate the simulation of complex spatiotemporal dynamical systems, particularly for fluid dynamics applications. The paper addresses two key challenges: long-horizon prediction and generalization. To tackle these issues, MultiPDENet combines numerical schemes with deep learning through a multiscale time-stepping approach, which includes both fine-scale and coarse-scale predictions, effectively mitigating temporal error accumulation in long-term forecasting.

[-] Claims on Spatial Derivative Accuracy (Abstract, line 019): The authors state that MultiPDENet "enables accurate estimation of spatial derivatives on coarse grids." However, there is no theoretical analysis or empirical evidence provided in the main text or experiments to support this claim. Additional analysis or experimental validation is needed to substantiate this assertion. Actually, this claim appears many times in the paper.

[-] Oversimplification of Method Section (Section 3.2): The method description in Section 3.2 is oversimplified, with essential details, including the Poisson and correction blocks, relegated to the appendix. These blocks are central to the model's architecture and should be introduced in the main text to improve readability and clarity. Readers currently need to constantly refer to the appendix for critical information about the methodology.

[-] Computational and Memory Cost Analysis: Since the network architecture includes the computation of partial derivatives (especially second-order derivatives), this likely increases computational complexity and memory requirements. To provide a more comprehensive evaluation, the authors should compare the time and memory costs of MultiPDENet with those of other baseline models, during both training and testing. Additionally, reporting the parameter count for each method would help control variables, clarifying whether the performance gains result from the proposed architecture or from increased computational resources and model size.


[-] Framework Independence and Network Architecture Variability: Given that the proposed framework is architecture-agnostic, it would be beneficial for the authors to demonstrate that MultiPDENet performs well with different backbone architectures (such as FNO, UNet, or Transformers). This would further validate the framework's flexibility and effectiveness across architectures. As operator learning progresses rapidly, incorporating more recent models, such as transformer-based operators, as baselines would strengthen the paper's relevance and rigor.

### Strengths
See above

### Weaknesses
[-] Claims on Spatial Derivative Accuracy (Abstract, line 019): The authors state that MultiPDENet "enables accurate estimation of spatial derivatives on coarse grids." However, there is no theoretical analysis or empirical evidence provided in the main text or experiments to support this claim. Additional analysis or experimental validation is needed to substantiate this assertion. Actually, this claim appears many times in the paper.

[-] Oversimplification of Method Section (Section 3.2): The method description in Section 3.2 is oversimplified, with essential details, including the Poisson and correction blocks, relegated to the appendix. These blocks are central to the model's architecture and should be introduced in the main text to improve readability and clarity. Readers currently need to constantly refer to the appendix for critical information about the methodology.

[-] Computational and Memory Cost Analysis: Since the network architecture includes the computation of partial derivatives (especially second-order derivatives), this likely increases computational complexity and memory requirements. To provide a more comprehensive evaluation, the authors should compare the time and memory costs of MultiPDENet with those of other baseline models, during both training and testing. Additionally, reporting the parameter count for each method would help control variables, clarifying whether the performance gains result from the proposed architecture or from increased computational resources and model size.


[-] Framework Independence and Network Architecture Variability: Given that the proposed framework is architecture-agnostic, it would be beneficial for the authors to demonstrate that MultiPDENet performs well with different backbone architectures (such as FNO, UNet, or Transformers). This would further validate the framework's flexibility and effectiveness across architectures. As operator learning progresses rapidly, incorporating more recent models, such as transformer-based operators, as baselines would strengthen the paper's relevance and rigor.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a hybrid method for solving PDEs, combining elements of classical numerical methods with learnable parameters.  Elements of classical numerical methods include an RK4 time integrator, finite-difference derivatives, and a Poisson solver for pressure.  The learned correction block uses a Fourier Neural operator. The problem is tested on 1D and 2D PDEs with periodic boundary conditions.  The authors claim that using a learned correction at a coarse time scale improves the prediction error and provides "53x speedup" compared to classical numerical methods.

### Strengths
This paper proposes an architecture to solve PDEs. Overall I cannot rate this paper strongly and am unable to offer a view of strengths because I find much of the presentation unclear.

### Weaknesses
The approach here is similar to other hybrid classical+learned approaches.  The presentation of the work is rather unclear in my view.  It is not explained in detail what the micro (MiNN) and macro (MaNN) blocks do exactly and what the difference is between them.  The authors refer to "sparse grids" on occasion, and it is unclear what is meant because the authors also use the separate term "coarse grid".

The claim that this method offers a 53x speedup compared to traditional numerical methods is not backed up by evidence, nor details of how it is measured.  Overall, what is here is not sufficiently convincing or compelling.

### Questions
Please provide details of how the speedup compared to traditional numerical methods is obtained.  Are the same resolutions being used for both?  Is the same type of device being used, or does this a comparison where one simulation is on CPU and another on GPU?  Is accuracy being checked at all for this comparison?  Please see https://www.nature.com/articles/s42256-024-00897-5.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MultiPDENet, a novel neural network architecture designed to accelerate simulations of fluid dynamics by integrating machine learning with partial differential equation (PDE) constraints. The architecture uses a multi-scale time-stepping approach and a learnable convolutional filter that embeds physical equations directly into the network, enhancing both accuracy and computational efficiency. The numerical findings of MultiPDENet demonstrate the accuracy and generalizability across different initial conditions, Reynolds numbers, and external forces. The inclusion of correction blocks enhances its long-term stability and robustness. An ablation study validates the effectiveness of the model’s components, highlighting its potential as a powerful tool for fluid simulations and complex PDE-constrained problems. Overall, this paper is well-written and could be a significant algorithmic contribution. I am willing to recommend accept. However, there are still some comments and questions need to be clarified or further discussion,  see the weakness and questions.

### Strengths
1. Originality: the paper introduces an innovative approach by integrating a physics-informed neural network (PINN) with a multi-scale time-stepping mechanism and a learnable filter, making it distinct from traditional numerical methods and existing data-driven models. This combination of deep learning and PDE constraints is a novel contribution that enhances the model's interpretability and applicability in fluid dynamics simulations.
2. Quality: this work is thorough, with comprehensive experiments demonstrating MultiPDENet’s performance across various PDE systems. The detailed ablation study provides strong evidence that each component of the model contributes meaningfully to its success. The results are rigorously compared against baseline methods, showcasing significant improvements in accuracy and computational efficiency.
3. Clarity: the paper is well-structured, providing clear explanations of the methodology, architecture, and experimental setup. The figures and tables are informative and support the textual content effectively. The presentation of the multi-scale time-stepping framework and the incorporation of physics into the network are clear.
4. Significance: the findings of the paper have potential implications in the field of computational fluid dynamics and PDE-constrained modeling.

### Weaknesses
1. The model is limited to regular grids due to the use of convolutional operations. This restricts its applicability in cases involving irregular or adaptive grids. The reliance on structured grids inherently limits the model's ability to handle complex geometries or simulations where mesh refinement is necessary to capture localized phenomena accurately. For example, simulating flow around complex objects or within intricate porous media would be challenging without the flexibility of unstructured meshes.
2. The current study only addresses 1D and 2D problems, which limits its applicability to more complex 3D simulations. Examples of 3D fluid simulations are more convincing. The extension to 3D is not trivial, as it introduces challenges related to computational cost and memory requirements, especially when dealing with high-resolution simulations. The paper lacks a discussion on how the model would scale with the increased dimensionality and the associated computational burden.
3. Although it is mentioned that the method works with sparse data, the paper could elaborate more on the data requirements for practical cases with very noisy or incomplete data. The paper does not provide a clear analysis of the model's performance under varying degrees of data sparsity or noise levels. This is crucial for real-world applications where data is often imperfect. A more detailed study on the model's robustness to noisy or incomplete data is needed.
4. The inclusion of multi-scale architectures, learnable filters, and correction blocks adds complexity to the model. This could impact the ease of implementation and adoption by other researchers or practitioners, especially when compared to more straightforward neural network models. The author should address this and provide open-source code for reproducibility. The complexity of the model architecture, with its multiple components, may hinder its adoption by researchers and practitioners who prefer simpler and more easily implementable models. The lack of publicly available code further exacerbates this issue.

### Questions
1. On page 5 line 233, "e divide the neural network..." what is statement? 
2. On page 9 line 478, "This demonstrates our model..." this claim is questionable. The current test has Re = 4000. To demonstrate the capability of this approach for high Re turbulence, a 3D flow with Re of at least 10^4 would be necessary to substantiate this claim.
3. The training data collected are from uniform timestep (\Delta t). However, many fluid simulations have non-uniform timestep. How does the model react to these scenarios?
4. The paper mentions future work involving graph neural networks for irregular grids. How feasible is this adaptation, and what challenges might arise in integrating GNNs with the current architecture?
5. Are there foreseeable issues when extending the current approach to higher dimensions?
6. How sensitive is the model’s performance to hyperparameters, such as the choice of kernel size for the learnable filter or the learning rate for training?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce MultiPDENet. The goal is to accelerate the solution of time-dependent PDEs using deep learning. MultiPDENet has a learnable multiscale timestepper, inspired by Runge-Kutta updates. It also has some interesting inductive biases, such as symmetry constraints on layers that mimic the operation of finite difference stencils. The results show impressive gains over standard neural PDE surrogates from the literature in terms of long term rollout accuracy and stability.

### Strengths
**Novelty**

There are several novel aspects of MultiPDENet
- The schematic diagram of how everything fits together is unique
- While learning a timestepper is not unique, I have not since it in the context of PDEs, only ODEs.
- While placing constraints on learnable derivative filters is not unique e.g. **Learning data driven discretizations for partial differential equations** Bar Sinai et al. (2018), the symmetry constraints of the MultiPDENet is unique

**Quality**

The results are really good! This is probably because of the sensible use of inductive bias in the learned solver structure. I think this is the highlight of the paper. In particular:
- The high correlation time plots in Figure 3 b/e/h are highly motivating
- The results in Table 2 show some massive performance improvements over baselines
- The results in Section 4.2 show large improvements over baselines even outside the ICs of the training range, demonstrating robustness to distribution shift
- I found the ablation in Table 3 very informative. This will also be important for anyone wishing to build on this work

**Significance**

For the field of ML4PDEs, any model that can push the envelope of performance forward is significant, and in this sense, MultiPDENet is significant.

### Weaknesses
 **Clarity**

I found it hard to follow the mathematical description of the model, since many of the terms are not laid out in the main text. I had to refer to the diagrams to understand the general gist of how everything fits together. Please see my questions below for further requests for clarification. I found I was able to understand, at a gut-feeling level, why main design choices were made, but because of the ambiguity in the exact model design I am not sure whether my reading is correct. The clarity is the part of the paper I would implore the authors to focus on most.

**Quality**

One subtle, but very important weakness of the paper is the very small number of training data used. The number of snapshots per equation are as follows:
- KdV: 3000 snapshots
- Burgers: 700 snapshots
- Gray-Scott: 540 snapshots
- Navier-Stokes: 24000 snapshots
For deep learning applications this is extremely small and could explain, to a large degree, just why the performance of MultiPDENet is just so good when compared with the other models, which exhibit much less inductive bias. As is well known, inductive bias helps in the low data regime, such as this. Indeed this could become the angle that this paper takes, but unless I missed it, there is no data ablation in the paper, which would have been a useful comparison

### Questions
- Line 55: In what way are PiNNs data-drive? I think the claim that PiNNs are “data-driven”, at least in their vanilla form, is contentious. If you consider collocation points as data then this is somewhat true, but there are no ground-truth targets fed to PiNNs, which would render them data-free. 
- Line 103: One the citations reads “_Transformers Cao (2021)_”. I think this should read “_Cao (2021)_”.
- Equation 1: Please explain all the mathematical terms in full.
  - What is $\tilde{\textbf{x}}$?
  - Why is $\tau$ a dummy variable in the integral, but also found outside the integral?
  - Is $\Delta$ a difference operator or a Laplacian?
  - What is $\mu$
  - What do $i$ and $j$ correspond to? If timestep indices, how are they different from $k$?
  - Referring back to Figure 1.b), please explain what $k+\delta$ means? Is $\delta$ a fractional time index? What values does $\delta$ take?
- Equation 3:
  - What is $\lambda$?
  - What values can $m$ take on? Does this imply that Equation 3 is an $m$-step block? How does it correspond to Figure 1a)? Is Figure 1a) the Runge-Kutta style discretization of the integral?
  - In Equation 1 $\mathcal{P}$ accepts argument $\textbf{u}$, but in Equation 3 it also includes $\Delta \textbf{u}$ and $\lambda$.
  - What is the significance of square brackets?
- Figure 2: Please expand on the symmetry constraints for the central difference stencils. We see even symmetry in the vertical direction and odd/even symmetry in the horizontal direction. If you are working in 2 dimensions, what does the mixed derivative operator $\partial_{xy}$ looks like?
- Line 233: e -> We
- Line 269: What is $T$? Is it time? How is $T$ different from $t$?
- Figure 3: b)e)h).
  - Between each plot the colors of the curves per model change, please fix this.
  - In e) you write "Ours"; whereas, in b) and h) you write "MultiPDENet". Please choose one.

### Soundness
2

### Presentation
2

### Contribution
3
