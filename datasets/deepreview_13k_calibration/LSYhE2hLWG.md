# SineNet: Learning Temporal Dynamics in Time-Dependent Partial Differential Equations

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We consider using deep neural networks to solve time-dependent partial differential equations (PDEs), where multi-scale processing is crucial for modeling complex, time-evolving dynamics. 
While the U-Net architecture with skip connections is commonly used by prior studies to enable multi-scale processing, our analysis shows that the need for features to evolve across layers results in temporally misaligned features in skip connections, which limits the model's performance.
To address this limitation, we propose SineNet, consisting of multiple sequentially connected U-shaped network blocks, referred to as waves. % , dubbed waves. 
In SineNet, high-resolution features are evolved progressively through multiple stages, thereby reducing the amount of misalignment within each stage.
We furthermore analyze the role of skip connections in enabling both parallel and sequential processing of multi-scale information.
Our method is rigorously tested on multiple PDE datasets, including the Navier-Stokes equations and shallow water equations, showcasing the advantages of our proposed approach over conventional U-Nets with a comparable parameter budget. We further demonstrate that increasing the number of waves in SineNet while maintaining the same number of parameters leads to a monotonically improved performance. The results highlight the effectiveness of SineNet and the potential of our approach in advancing the state-of-the-art in neural PDE solver design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
SineNet, a sequential U-Net with comparably small channel depths, is introduced to model the temporal evolution of 2D PDEs. By design, SineNet mitigates the spatial misalignment between skip connections in the traditional U-Net by subdividing the task of spatial propagation over multiple small U-Nets, referred to as waves. Experiments on multiple benchmarks demonstrate the superiority of SineNet against state-of-the-art methods.

### Strengths
_Originality:_ of spatial information misalignment between different hierarchies in the U-Net is an elemental observation and finding. Related work is exhaustive and cited adequately.

_Quality:_ All claims are well supported by appropriate visualizations and experiments.

_Clarity:_ The manuscript is mostly clear, well organized and written in approachable language. One point remained unclear to me and should be clarified upon publication (see question below).

_Significance:_ Solving the spatial misalignment problem with the proposed method has a potentially large impact on time-series forecasting with U-Nets and will advance the field. The ML community that is interested in simulating spatiotemporal dynamics (which also relates to video prediction) will likely benefit from the observations presented in this manuscript.

_Further comments_:
- The demonstration of spatially misaligned features in Figure 1 is very indicative and comprehensive.
- I like the neat property to have adaptive $\delta_k$ per wave to adequately model velocities of different speeds.
- Great to have runtime analysis and memory footprint of all models provided in Table 4 of Appendix C!

### Weaknesses
1. Unclear what limitations the method bears. Under what circumstances do you expect SineNet to break and fail? Specifically, it is not clear how the method would perform on PDEs with highly chaotic or turbulent behavior, where the temporal dynamics are less predictable. Furthermore, the reliance on a fixed number of waves might limit its ability to adapt to PDEs with varying degrees of temporal complexity. It would also be beneficial to understand how the model's performance scales with increasing spatial resolution and longer time horizons, as these are common challenges in PDE modeling.
2. Why does Dil-ResNet which you benchmark against only have 4.2M parameters (compared to 35M in your model)? This is a fairly critical point, since neither the inference time nor the required memory in Table 4 seem to justify such a small parameter count for Dil-ResNet. Indeed, I was curious to see how vanilla ResNet would perform and like that you have included Dil-ResNet. This actually forced me to only rate your submission as "marginally above threshold" instead of voting for a clear accept. The discrepancy in parameter count raises concerns about the fairness of the comparison. A more detailed analysis of the computational cost and performance trade-offs between the models is needed, including a breakdown of the parameter count for each layer in both SineNet and Dil-ResNet.

### Questions
1. In Section 3.4, does $L=4$ mean that four downsampling plus convolution combinations followed by four upsampling plus convolution combinations are employed? That is, $x=f_l(d(x))$ (encoding) followed by $x=g_l(v(x))$ (decoding) for $l\in[0, 1, 2, 3]$? Or do you employ only two downsampling and upsampling operations, as visualized in Figure 1? Maybe you can clarify right after Equation (7). 
2. Have you tried to set $\delta_k$ as learnable parameter, or is the tuning of the time-subscale subject to the practitioner and model designer?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the misalignment problem caused by the U-Net architecture in the context of PDE simulations and proposes multi-stage modeling of temporal dynamics with SineNet. SineNet consists of multiple sequentially connected U-shaped network blocks, which the authors call waves. High-resolution features evolve progressively through multiple stages, and contains misalignment within each stage. The method is evaluated on typical problems where multi-scalability can be seen, and its effectiveness are shown compared to representative baselines.

### Strengths
The paper points out an interesting problem that happens when employing the U-Net architecture to simulate spatiotemporal dynamics. The paper is well-organized and is generally easy to follow. The idea of the proposed model is simple and the choice of the architecture is based on reasonable analyzation of existing works. Wide range of ablation study is conducted and the proposed method outperforms strong baselines in rollout experiments.

### Weaknesses
I still do not fully understand what the authors mean by misalignment, since the metric for misalignment does not look properly introduced. Although the loss $a_{t+\Delta l}$ is introduced in the Appendix A.1, the loss does not seem to serve as the metric because it (and the experiment in Appendix A.1) looks more like for the robustness against noise injected. Thus, it is also still unclear if the improvement in the rollout result reported in Table 1 and Table 2 is achieved by the reduction of misalignment.


Some ablation study is missing. For example, what about if we replace each $V_{k}$ with standard U-Net with the equations (2) and (3)? Can the authors also provide visualization on this ablation version of the model in a way similar to Figure 5?
 

 
**Minor comments**

Typo Section 3.3: … benefits of the U-Net architecture, we contruct the ….

### Questions
See the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
When applying U-Net architectures with skip connections to dynamical problems, the features do not evolve across layers, thus limiting the efficiency of these methods for predicting dynamical systems. The method proposed in the article tries to overcome this challenge by having features across layers that evolve with the time. More precisely, the architecture is an encode-process-decode architecture consisting of several U-Net architectures stacked together with convolutions to encode and decode the solutions. Each U-Net, or wave, predicts the latent solution at a small time step instead of at the final time step, thus allowing evolving features. In addition to this global architecture, the downsampling and upsampling operations include residual blocks from the input, thus connecting the evolution of the features directly with the input. The architecture is tested on fluid mechanics problems, namely incompressible Navier-Stokes, compressible Navier-Stokes and Shallow Water equations. The experiments consist in forecasting these dynamical systems.

### Strengths
- The method solves a common problems when directly applying U-Net architectures to dynamical systems.

- The paper is well written and the justifications of the architecture are documented.
 
- The performances of the method seem to be competitive with several baselines.

### Weaknesses
 - Stacked U-net have already been developed  for different tasks as detailed in the article (section Stacked U-Nets in the related work). The implementation here differs in some minor points and thus is more effective for PDE prediction but this is a marginal improvement over the previous works.
- The experiments are not extensive. First, more baselines should be used, with at least DeepONet [1], MP-PDE ([2], cited but not implemented) or Neural ODE [3], which closely resembles the formulation of SineNet. Second, the evolution of the error with the time is not shown, only at a given number of rollout steps for each datasets, thus limiting the impact of the results. Third, no ablation on the influence of the number of historical time steps is performed.
- As other U-Net architectures, SineNet cannot handle irregular grids or grids of different sizes, which are very common in various dynamics resolution problems. This limits the applicability of this line of methods to more practical problems.
- This is more minor. As with other auto-regressive architectures, the forecasting process is done at regular steps, so the architecture cannot produce values at any time $t$, but only at multiples of $\Delta t$.

### Questions
- Have you tried with a high number of rollout steps ? It would be interesting to see how stable the method is when pushed to its limits.
- In Figure 3, the error seems to keep decreasing with the number of waves. Have you tested with more waves? This would be interesting to see when the error arrives at a plateau and this could help improve the performances of the model if the error keeps decreasing with the number of waves.
- Have you tried using noise to improve the rollout stability? (as has been done for instance in [4])
- In the experiments, null Dirichlet and Neumann boundary conditions were chosen. What happens if different values for these conditions are chosen? Will zero padding still be effective? 

[4]: Stachenfeld, K., Fielding, D. B., Kochkov, D., Cranmer, M., Pfaff, T., Godwin, J., ..., Sanchez-Gonzalez, A. (2021). Learned coarse models for efficient turbulence simulation. arXiv preprint arXiv:2112.15275.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces SineNet as sequential / multi-stage UNet which improves temporal modeling for time-dependent partial differential equation (PDE) surrogates. This is motivated by misalignment in UNet architectures between downsampling and upsampling paths. The misalignment is caused by the temporal update of the underlying PDE which is in stark contrast to segmentation tasks for which the U-Net was initially introduced. SineNet architectures consist of multiple waves which are individual small UNet components, and thus, enable a smooth transfer between input timesteps and predicted timestep. SineNet models are testes against Factorized Fourier Neural Operators, Dilated ResNets, and various U-Net variants on 2D benchmarks of compressible / incompressible Navier-Stokes equations and shallow water equations.

### Strengths
- The paper is well motivated. It presents an intriguing observation on temporal PDE modeling for U-Nets. Whereas U-Nets are ideally suited for e.g. segmentation tasks (U-Nets extract information on various scales hierarchically before invoking a symmetric upsampling path), for PDE modeling this symmetric upsampling is broken since the time evolution of the system is incorrectly modeled. The visualizations help a lot understanding this problematic.
- The architecture design is novel and thought-through.
- Experimental results are strong and ablations are convincing, personally I like Figure 3 a lot!  
- The code is clean and easy to follow.

### Weaknesses
 - As clearly stated in the paper, U-Nets in this setting only work for fixed grid resolutions. There are however already works which design operators for different grids - see e.g.,  Raonic et al. Would it be possible to extend the experiments to some "super-resolution" experiments (i.e., evaluating at a different (higher) resolution than the one used during training)? I am pretty convinced SineNets are doing great there as well.
- One advantage U-Nets have is that they are storage efficient since the highest resolution is only used in the first and last block. I am not sure how SineNets handle this - probably through P and Q networks? It would be great to have some information on this. Toward this end I am wondering if the number of waves is increasing the memory footprint and by how much?

### Questions
- The iterative refinement process is conceptually similar to PDE Refiner (Lippe et al.) - with some major differences to my understanding. SineNets iteratively refines the temporal update in an one end-to-end approach whereas PDE Refiner looks at the input several times and refines different frequency components. It might be interesting to contrast those two approaches in the discussion.
- The paper strongly references the original paper of Gupta & Brandstetter. This paper put some emphasis on conditioning on equation parameters as well as flexible lead time predictions. It would be interesting to have statements / experiments on this as well. Similar FiLM like encodings would work for SineNet I suppose?  
- The misalignment made me realize why ViTs or Swin Transformers might be better fit for PDE modeling compared to standard U-Nets. Can you comment on this?  

I am happy to raise my score if weaknesses and questions are addressed properly.




Lippe, P., Veeling, B. S., Perdikaris, P., Turner, R. E., & Brandstetter, J. (2023). Pde-refiner: Achieving accurate long rollouts with neural pde solvers. arXiv preprint arXiv:2308.05732.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
