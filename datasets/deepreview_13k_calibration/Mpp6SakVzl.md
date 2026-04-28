# DiLQR: Differentiable Iterative Linear Quadratic Regulator

- Decision: Reject
- Avg Score: 3.33
- Scores: 6, 1, 3

## Abstract
Differentiable control promises end-to-end differentiability and adaptability, effectively combining the advantages of both model-free and model-based control
approaches. However, the iterative Linear Quadratic Regulator (iLQR), despite
being a powerful nonlinear controller, still lacks differentiable capabilities. The
scalability of differentiating through extended iterations and horizons poses signifi
cant challenges, hindering iLQR from being an effective differentiable controller.
This paper introduces a framework that facilitates differentiation through iLQR,
allowing it to serve as a trainable and differentiable module, either as or within
a neural network. for control purposes. A novel aspect of this framework is the
analytical solution that it provides for the gradient of an iLQR controller through
implicit differentiation, which ensures a constant backward cost regardless of iteration, while producing an accurate gradient. We evaluate our framework on
imitation tasks on famous control benchmarks. Our analytical method demonstrates superior computational performance, achieving up to $\mathbf{128x}$ speedup and
a minimum of $\mathbf{21x}$ speedup compared to automatic differentiation. Our method
also demonstrates superior learning performance ($\mathbf{10^6}$x) compared to traditional
neural network policies and better model loss with differentiable controllers that
lack exact analytical gradients. Furthermore, we integrate our module into a
larger network with visual inputs to demonstrate the capacity of our method for
high-dimensional, fully end-to-end tasks. Codes can be found on the project
homepage https://sites.google.com/view/dilqr/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper proposes a method for calculating the analytical gradient of iLQR by leveraging implicit differentiation at the fixed point to enhance the learning and optimization of control algorithms using iterative Linear Quadratic Regulators (iLQR). The method also introduces a forward approach that reuses computations from each time step to accelerate the next step, along with parallelization techniques to further improve efficiency. The proposed approach significantly reduces computational costs and enables accurate and scalable gradient calculations compared to conventional automatic differentiation methods. Additionally, the integration of iLQR as a module within neural networks demonstrated the feasibility of end-to-end learning for high-dimensional tasks involving visual inputs.

### Strengths
- The paper is well-written overall, with the proposed method's theoretical foundation clearly explained. Additionally, the positioning and differences from existing research are clearly demonstrated.
- The proposed method significantly reduces computational costs compared to conventional methods using automatic differentiation, achieving improved scalability. To the best of my knowledge, this approach is novel and highly useful, as it is applicable to large-scale control problems and tasks with long horizons. Furthermore, the integration of iLQR as a module within neural networks for end-to-end learning has been demonstrated, suggesting potential applications to more complex tasks.

### Weaknesses
 - The proposed method improves gradient accuracy through analytical implicit differentiation at the fixed point and further enhances speed by introducing a forward method for differentiation concerning nonlinear dynamics parameters of linear dynamics, as well as implementing parallelization. However, the results only evaluate the final method that combines these improvements, making it unclear how much each specific enhancement contributed to the overall speed improvement. The authors should clarify through experiments how much each component contributed to the speed and performance outcomes.
- While the paper is well-written overall, the explanation of the proposed method could be further improved. For instance, due to the parallel presentation of Sections 4.1 to 4.6, understanding the complete picture was challenging, and it was difficult to grasp how each element fit into the overall method. Including an overview at the beginning of Section 4 or presenting the entire computation as an algorithm would make the method easier to understand. Additionally, while reading the paper, I found it confusing that both $D_\theta$​ (meaning $D_\theta X=\partial X / \partial \theta$) and $D_t$​ (meaning $D_t=\left[A_t, B_t\right]$) were represented by the same symbol $D$. Using different notations or adding a note for clarification would help avoid confusion.

### Questions
- To clarify the proposed method's effectiveness, I would like you to improve the points I have raised in the above weaknesses.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper studies derivatives through an iLQR-based controller, which are given by implicit differentiation in Prop 1. The experimental setting in section 5 compare this method's runtime to the unrolled derivatives (Fig 2), and then go onto imitation/inverse control settings on the pendulum and cartpole (Fig 3), and finally to a pixel-based control setting.

### Strengths
Understanding controller derivatives is an important topic, and the paper investigates efficient ways of doing this.

### Weaknesses
While the overall direction of the paper is okay, it is not ready for publication. My biggest concern is that there are at least two crucial pieces of related work that need to be discussed and compared against: [Differentiable Optimal Control via Differential Dynamic Programming](https://arxiv.org/abs/2209.01117) and [Leveraging Proximal Optimization for Differentiating Optimal Control Solvers](https://hal.science/hal-03786820v1/document). This abstract of the submitted paper claims "the iterative Linear Quadratic Regulator (iLQR) [...] still lacks differentiable capabilities." However, both of these papers focus on this setting. Section A of [Differentiable Optimal Control via Differential Dynamic Programming](https://arxiv.org/abs/2209.01117) states that they use "any method (including either iLQR or DDP) for solving optimal control problems" while using the second-order terms from DDP in only the implicit derivative computation. I believe it's possible the derivatives between the submitted paper and this one are very similar, if not identical, and a discussion and direct comparison here is necessary.  Furthermore, [Leveraging Proximal Optimization for Differentiating Optimal Control Solvers](https://hal.science/hal-03786820v1/document) can also solve the OC problem with iLQR and then proposes a proximal optimization way of computing the implicit derivatives. 

I have a few other minor concerns with the paper: 1) Figures 1 and 2 compare autodiff through the unrolled LQR iterates to the proposed method. This is slightly misleading as it ignores the related work and alternative approaches that are not based on unrolling. 2) The experimental results on imitating the pendulum and cartpole are relatively small-scale. I would find it significantly more convincing to use the larger experimental settings from these other differentiable control papers.

### Questions
I do not have any further specific questions. I am very open to discussing the weaknesses above

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an efficient O(1) iterative Linear Quadratic Regulator (iLQR) based-method to analytically compute the trajectory gradients for optimal control problem with constrained first-order difference equations. The forward differentiation method outlines impressive speedups compared to standard automatic differentiation tools. The method is evaluated on tasks from inverted pendulum to vision-based cartpoles, consistently displaying outstanding scaling and learning performance over neural network policies.

### Strengths
The paper has a careful presentation and illustration of existing work, and how its approach differs from the rest. It carefully distinshuisiung between the various notions of forward and backward passes it introduces. The results are interesting, especially on computational performance and imitation learning, as they indicate near constant scaling with the number of iLQR iteration and remarkably low losses.

### Weaknesses
The paper suffers from a number of weaknesses, listed below using the same references as in the main paper:
1) The contribution is somewhat limited. As you point out in section 4.7, the most important related work (Amos et al. 2018) differs from the current because it assumes independent fixed points. You combine this with the idea of analytically deriving derivatives for a fixed-point wrt to parameters $\theta$. This has been done very well before, notably in (Bai et al. 2019) as you point out. I think better contextualization of your contribution and acknowledgements of these two pieces of work is important. Specifically, the novelty of applying fixed-point differentiation to iLQR is not clearly articulated, and the connection to prior work on implicit differentiation of fixed points is downplayed. The paper needs to more clearly delineate what is novel in their approach beyond a specific application of a known technique.
2) Since the main contribution of this work is theoretical with the aim of outperforming auto-differentiation, I believe the comparison shouldn't be limited to Pytorch's implementation. Other frameworks like JAX could provide invaluable insights. Specifically, the use of JAX's `jaxopt` library, which has built-in support for implicit differentiation, could provide a more robust comparison. The current comparison only shows an advantage over PyTorch's standard autograd, which is not sufficient to claim superiority over all autodiff approaches.
3) The visual control task is interesting, but it lacks substantial results, analysis, and discussion. The only results available are qualitative. More generally, the work is not compared to more established methods on advanced tasks, and it suggests potential for SOTA performance. The work mentions other works that only consider toy examples, but those have various strengths that the current doesn't have, particularly in their exposition and strong theoretical guarantees (e.g. Xu et al. 2024a, Amos et al. 2018). The lack of quantitative metrics and comparisons to established baselines makes it difficult to assess the true performance of the proposed method. The claim of potential SOTA performance is not supported by sufficient evidence.
4) The presentation suffers from inconsistent notations, and the limitations of the work are absent. Specifically, the paper should clearly state the assumptions of the method, such as the requirement for a fixed point in iLQR and the need for first and second-order derivatives of the dynamics. These limitations should be explicitly discussed to provide a complete picture of the method's applicability.

### Questions
1) I am confused about section 4.4. Is the $L$ referenced there sill referring to the loss function from line 208 ? Also, is the binary loss approach described in that section **approximate** ? If so, then it might be worth clarifying that the gradients mentioned in the main contribution are equally approximate (line 094). 
2) I'm not sure about the first paragraph in section 4.6. In PyTorch's `torch.autograd.jacobian` documentation, I believe the flag `create_graph` which would in turn raise `retain_graph` should allow gradient information to flow through time steps. I couldn't figure that out from the code you attached. Can you please clarify whether this feature is what you addressed, or not ?
3) In line 312, you refer to $\frac{\partial D_t}{\partial \theta}$ from Eq. 9, but that term doesn't appear in Eq. 9. Did you mean Eq. 13 instead ? (It makes it hard to understand Eq. 14 and 15.)

### Soundness
1

### Presentation
2

### Contribution
2
