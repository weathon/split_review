# Metamizer: A Versatile Neural Optimizer for Fast and Accurate Physics Simulations

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 3, 8, 5

## Abstract
\iffalse
Efficient physics simulations are essential for countless applications, ranging from cloth animations or smoke effects in video games, to analyzing pollutant dispersion in environmental sciences, to calculating vehicle drag coefficients in engineering applications. 
Unfortunately, analytical solutions to the underlying physical equations are rarely available, and numerical solutions require high computational resources. %enormous => high
Latest developments in the field of physics-based Deep Learning have led to promising efficiency gains for physics simulations but still suffer from limited generalization capabilities and low accuracy compared to numerical solvers. % (especially for generalization or when no ground truth data was available during training)

Here, we present a novel neural optimizer that iteratively solves a wide range of physical systems with high accuracy by minimizing a physics-based loss function. To this end, we introduce a scale invariant architecture that proposes improved gradient descent update steps to accelerate convergence.
Since the neural network itself acts as an optimizer, training this neural optimizer falls into the category of meta-optimization approaches. 

The very same network was trained on the Laplace, Advection-Diffusion, incompressible Navier-Stokes as well as on cloth simulations % very same network unklar hier => vllt besser this neural optimizer und dann noch sagen, dass man den optimizer nicht retrainen musste und dass es sogar auf die Burgers und Wave equation generalisiert hat oder so...
and achieved unprecedented accuracy for deep learning based approaches on several PDEs - in some cases coming close to machine precision. Furthermore, we show that the trained model also generalizes to PDEs that were not covered during training such as the Poisson, wave and Burgers equation.
We believe that our method could have a profound impact on future numerical solvers, paving the way for fast and accurate neural physics simulations without the need for retraining.


\fi

Efficient physics simulations are essential for numerous applications, ranging from realistic cloth animations or smoke effects in video games, to analyzing pollutant dispersion in environmental sciences, to calculating vehicle drag coefficients in engineering applications. Unfortunately, analytical solutions to the underlying physical equations are rarely available, and numerical solutions require high computational resources. Latest developments in the field of physics-based Deep Learning have led to promising efficiency improvements but still suffer from limited generalization capabilities and low accuracy compared to numerical solvers.

In this work, we introduce Metamizer, a novel neural optimizer that iteratively solves a wide range of physical systems with high accuracy by minimizing a physics-based loss function. To this end, our approach leverages a scale-invariant architecture that enhances gradient descent updates to accelerate convergence. Since the neural network itself acts as an optimizer, training this neural optimizer falls into the category of meta-optimization approaches.

We demonstrate that Metamizer achieves unprecedented accuracy for deep learning based approaches - sometimes approaching machine precision - across multiple PDEs after training on the Laplace, advection-diffusion and incompressible Navier-Stokes equation as well as on cloth simulations. Remarkably, the model also generalizes to PDEs that were not covered during training such as the Poisson, wave and Burgers equation.

Our results suggest that Metamizer could have a profound impact on future numerical solvers, paving the way for fast and accurate neural physics simulations without the need for retraining.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a meta-optimization technique for solving physics simulation problems, including linear and nonlinear PDE problems.  The proposed Metamizer framework is an iterative optimizer that uses a scale-invariant architecture to improve gradient descent updates to accelerate convergence.

### Strengths
1. A nice advantage of Metamizer is that it's able to be applied to PDEs that weren't seen during training.  I don't know if there are other state-of-the-art methods like that, but I appreciated that feature.

2. Metamizer appears to be scale-invariant and to not need retraining for different PDEs, which again, is quite useful from a practical perspective.

3. Metamizer seems like a simple idea with a relatively straightforward architecture, which means that future research in this direction should be possible to build upon the present work.

### Weaknesses
1. "However, to the best of our knowledge, L2O has not yet been applied in the context of physics simulations"
Unfortunately, I must inform the authors that L2O has absolutely been applied in the context of physics simulations.  Please see for example the works "A deep conjugate direction method for iteratively solving linear systems" (ICML 2023) and "A Neural-Preconditioned Poisson Solver for Mixed Dirichlet and Neumann Boundary Conditions" (ICML 2024) and the references / related work discussions in there. These works demonstrate the use of learned preconditioners within iterative solvers, achieving significant residual reduction, and should be acknowledged. The authors should also note that these methods are capable of reaching arbitrarily low tolerances, just like a standard CG solver, and are not limited to the 4-6 orders of magnitude reduction mentioned in the response.

2. "Data-driven Deep Learning approaches"
The authors may be interested recent works like "Toward Improving Boussinesq Flow Simulations by Learning with Compressible Flow" (PASC 2024), which show that the addition of a neural surrogate can produce results that are more accurate than what is possible with a classical numerical solver - because a solver may be using a less accurate physical model.  This is an important point to be aware of or mention, since many deep learning approaches overlook the fact that one way to improve efficiency and accuracy is to simulate things with a cheaper model and then use learning models trained on more accurate models.

2. "Unfortunately, the learned implicit representations need to be retrained for every physical simulation and thus are not real-time capable."
This criticism of PINNs does not make sense to me.  When you train a PINN, you can evaluate is very quickly.  The fact that PINNs are best when trained on a specific physics problem, does not seem correlated to the performance of evaluating (performing inference on) a neural network like a PINN.  I suggest the authors remove this criticism or clarify what they mean.

3. (Minor) In the section "Time-Integration Schemes," it is likely worth tossing in a reference to a textbook or some similar resource that discusses additional common time integration schemes like RK4 - just to avoid giving the impression that the three schemes mentioned are the only ones.

4. It is interesting the authors' technique seems to essentially just be a U-net with carefully-chosen features (Fig. 3).  With physics problems, solutions are often smooth/continuous, so practitioners often use CNNs or perhaps mix convolutional layers with U-nets.  There is no discussion of why a plain U-net architecture was chosen, and adding something like that would be helpful for readers to gain intuition into the method.

5. There's not much that can be gleaned from Figs. 7 or 8 without quantitative metrics or labeled error/scale bars.

6. L757 "This is because Metamizer can be effectively parallelized on a GPU." Sparse iterative linear solvers can be effectively parallelized on a GPU - in fact, this is one of the things GPUs are best at.  This statement makes me believe the authors are using CPU or perhaps even serial implementations of things like CG or MINRES, which is a severely (10x+) unfair comparison. It is crucial to compare against optimized GPU implementations of these methods to provide a fair assessment of Metamizer's performance. Additionally, the comparison of a GPU implementation of Metamizer against a CPU implementation of other solvers is not a useful comparison.

Minor:

7. L245 you call it a CNN but it's specifically a U-Net?

8. L264 You say you use gradient descent but in parentheses you say Adam - do the authors understand these are distinct numerical methods?

9. L268 "ca 6 hours" should just be "about 6 hours," or even better, just specify the time more precisely, e.g., "6 hours and 15 minutes"

10. The abstract is a little long and split into a few paragraphs; I would recommend condensing things a bit.

11. Formatting mistakes like not doing LaTeX quotes properly - the authors should know better than this in a venue like ICLR

12. L235 citation not formatted right (\citet not \citep)

13. L277-281 (for instance - there are other places for this) Put commas after e.g., this is a grammar thing

14. L434 probably a typo in the table here

### Questions
1. The authors criticize gradient descent-like methods like AdaGrad and Adam, yet their method is based on improving gradient descent.  Can the authors speculate on how their ideas could work if based on other techniques like Adam?

2. L251-254 The authors describe how they want to use one network for all PDEs but then describe how different PDEs require different numbers of channels.  This sounds like different networks need to be trained depending on how many variables are in the problem (e.g., you'd have a 1-variable network, a 3-variable network, etc.).  Can the authors clarify this?

3. Figure 6 and the discussion around it doesn't say what equation and what boundary conditions are being solved here.  If this is Laplace/Poisson (at least without all-Neumann boundary conditions) - I don't really believe the results, because this should be a symmetric positive-definite sparse linear system that conjugate gradients should perform quite well on (and certainly better than GMRES and other slower/more general Krylov solvers).

4. With regards to the Figure 6 results, it's a little unfair to compare against constant-learning-rate variants of the other methods shown.  Of course things like SGD can't converge to 1e-33 precision with a learning rate of 0.01 - it is probably doing a very good job but the learning rate is so large that it literally cannot land on the minimum.  And it's not a mystery how to choose step sizes that enable convergence - e.g., for gradient descent, the Wolfe conditions (for instance) can inform what step size you should take at each step.

5. These results are further unfair because Metamizer - along with any other L2O methods used for these types of problems, see for instance the discussion in Kaneda et al. 2023 - are effectively acting as preconditioned solvers.  In Metamizer's case you're preconditioning gradient descent by using data about PDE losses.  So it would be fairer to compare against preconditioned CG, MINRES, GMRES, etc.  Unfortunately, the timings and iteration counts are so close that I bet if you used even just a Jacobi/diagonal preconditioner on those methods, they would all be outperforming Metamizer.

6. Figure 4 indicates that Metamizer-produced solutions may not enforce much smoothness (e.g., there is some rough noise around 20 iterations, where solutions are still not in the regime of double precision limits).  As mentioned earlier, I might venture a guess that this is due to the U-Net architecture chosen.  However, I am curious for the authors' thoughts?  This may be a useful thing to discuss in the paper, too.

Although my score leans somewhat negative (I would prefer to mark this as a 4, but it's not an option), it is mostly due to the evaluation and presentation, and I believe this is a worthwhile idea that could be published in an appropriate venue and with suitable manuscript improvements.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a neural-network-based meta-optimizer, Metamizer, designed to minimize the residuals of physical systems, especially partial differential equations (PDEs), in pixel space. The authors conduct experiments comparing the performance of Metamizer to both gradient-base optimzers and linear system solvers. Metamizer is evaluated on different PDEs and the results presented.

### Strengths
The problem the paper tries to address is of interest and has wide applicability.

### Weaknesses
 The paper has 3 main weaknesses:
- **MW1**: Lack of quantitative evaluation. Only qualitative images and residuals are presented, making it difficult to assess the method's performance objectively. This issue affects all the experiments. The chaotic nature of some of the PDEs does not justify the absence of a comparison with a baseline, such as MSE to a ground truth solution. While chaos develops over time, there is an initial period where trajectories are similar, and this period can be used for comparison. This is standard practice in both Neural Operator (NO) and autoregressive models (AR) literature. Furthermore, the residual alone is insufficient to assess solution quality, as methods like PINNs can achieve small residuals but produce poor solutions. Residuals are also problem-dependent, making comparisons without a reference solution difficult. While a ground truth is provided for the Laplace equation, this does not extend to other experiments, limiting the assessment of the method's general performance.
- **MW2**:  No baseline comparisons with other Learning to Optimize (L2O) methods, classical numerical solvers, or neural PDE methods. While the authors compare against linear solvers for a linear system built in pixel space, this is insufficient. Standard methods like FEM and FVM are routinely used to solve non-linear equations, and the paper claims Metamizer will outperform solvers on these equations as well. The lack of comparison to these methods, and to other L2O methods, makes it impossible to judge the relative performance of Metamizer. The claim that L2O has not been applied to PDEs does not justify not comparing against them, as these methods are general and can be applied to PDE-based losses. Without such comparisons, it is impossible to assess Metamizer's performance against existing L2O approaches.
- **MW3**:  Limited experimental scope. Experiments use only fixed-size grids, 100x100 (331) and 400x400 (775), which restricts generalizability and does not test varying resolutions, where new dynamics may arise, especially in the Navier-Stokes equation. The claim that the PDE can be scaled to fit the network resolution is not sufficient, as the discretization will have a finite resolution, and the solutions can vary dramatically depending on that resolution. The method's performance at a given resolution does not guarantee generalization to different resolutions, especially when new dynamics emerge. The lack of comparisons to proven solvers under such conditions further limits the validation of the solution quality.


## Main weaknesses

The proposed method can be viewed as a meta-learning method, a PDE solver, or an emulator but it lacks comparisons with other methods from these fields. Ideally, the method would be compared against methods from each of these fields. I acknowledge that such an exhaustive comparison involves a considerable effort, but the paper omits even a basic evaluation against standard methods in these areas.

The authors assert that L2O has not been applied to physics (99) but fail to demonstrate how Metamizer performs in the physics context against other L2O methods. Furthermore, the paper’s accuracy claims lack quantitative evidence, as it provides only qualitative images and residuals. This is inadequate for judging solution quality, especially when standard neural PDE literature benchmarks against ground truth obtained from numerical methods. Moreover, the lack of comparison to classical numerical methods is striking, since a comparison is performed against linear solvers for a linear system built in pixel space. Effectively, the paper is comparing against different linear solvers for the finite element method.

In short, the experimental evidence does not convincingly support the method's efficacy or comparative performance and extensive existing literature has not been engaged with.

## Additional Weaknesses

**W1**: The claim that no hyperparameters are used (68-69) is inaccurate, as $s_0$ is a hyperparameter (238).

**W2**: The claim on (332-333) is misleading. In the deep learning literature, accuracy typically reflects error metrics like MSE between the ground truth and the prediction. In this paper, accuracy has a different meaning (value of the residual) so it is not directly comparable. This is related to **MW1-2**.

**W2**: The accuracy claim on (332-333) is misleading; in deep learning, accuracy typically reflects error metrics like MSE. It is not possible to directly compare it to the claimed MSR.

**W3**: Misleading claim about linear solvers and their usage. In Fig. 6 Metamizer is compared to linear solvers, and in (327) it is claimed that linear solvers are limited to linear PDEs. This is only true in pixel space. Most PDE-solving techniques, such as the FEM, rely on solving a linear system derived from the equation through linearization [1]. Related to **MW2**.

**W4**: The caption of Fig. 8 claims that Metamizer can simulate a wide range of Reynolds numbers and shows snapshots for $Re=1$, $Re=50$ and $Re=200$. This range is insufficient compared to the typical Reynolds number range (1 to millions) in fluid dynamics, missing the complex behaviors at higher Reynolds numbers [2].

**W5**: No limitations whatsoever are discussed or acknowledged.

### Questions
## Missing details/questions

**Q1**: Insufficient details on residual computation (148-154, 175), specifically handling spatial resolution and Navier-Stokes pressure. More information should be provided in the appendix (related to **MW3**).

**Q2**: In (198-211) you say that the main problem with directly optimizing the gradient is the scaling, therefore you introduce a scale-invariant optimizer. What about local minima? The solution of the physical problem is the global minimum of the problem, so getting stuck in a local minimum is a potential issue that is not necessarily solved by scale invariance.

**Q3**: Is there no cold start issue? In the **Training** paragraph (256-269) it is stated that the training pool is initialized with randomized solutions. How exactly?. Fig. 6 shows that the gradient-based optimizers (Adam, SGD, etc) fail to converge. If the gradient signal is so poor how can the UNet learn from it? How does this relate to the scale vs local minima issues from Q1? Can Metamizer, once trained, minimize for randomized solutions drawn from a different distribution than the one it was trained on?

**Q4**: I appreciate the wall time and GPU usage training information (269). How many update steps were performed on the model? How many data samples did it see (presumably the number of update steps * batch size)?

**Q5** I find the description of the time integration and how it is used in the context of Metamizer unclear. Is the integration scheme used to define the discretization used of the time derivative? E.g. for forward Euler it would be approximated as $u_t' = \frac{u_{t+1} - u_{t}}{\Delta t}$ 

**Q6** Why is time integration needed at all? Can the residual computed on the full trajectory not be minimized for all the states at once?


## Things to improve the paper that did **not** impact the score:

Abstracts usually have a single paragraph.

Space before comma on line 93.


## Refrences

1) Brenner, S. C., & Scott, L. R. (2008). The Mathematical Theory of Finite Element Methods. In Texts in Applied Mathematics. Springer New York. https://doi.org/10.1007/978-0-387-75934-0 
2) Chassaing, P. (2022). Fundamentals of Fluid Mechanics. Springer International Publishing. https://doi.org/10.1007/978-3-031-10086-4


## Edit history
1. Confidence reduced from 4 to 3 in light of the discussion with the authors.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper targets an optimizer for training deep neural networks for improving the solving of tasks related to PDE solving. The goal if scale invariance is identified as a central challenge for physics-related learning tasks. The paper then proposes a U-net that is employed to infer the scaling of an update in order to improve conditioning of the neural network update.

The importance of scale invariance has been studied before for physics problems, e.g. in Holl et al., Scale-invariant learning by physics inversion, NeurIPS 2022. I just double checked , and e..g fig 1 there and figure 2 here are actually have a lot in common. This previous paper in the end takes a different approach, so I think it's no direction competition, but the unclear parts of the current submission definitely lead to a few questions.

The paper evaluates this idea for several canonical PDEs (Poisson & Laplace, advection-diffusion), as well as more complicated ones (waves, Navier-Stokes). Interestingly, cloth dynamics are included as well. While the rang of experiments is very nice, the motivation in terms of theory behind the approach remains unclear. Nonetheless, I think it’s an interesting and novel direction. So I liked the paper and its direction, but several unclear topics remain, which I hope the authors can address during the rebuttal phase.

### Strengths
The central goal of addressing "scale invariance" is not new, but the proposed learning of scale invariance is new if I understood the approach correctly.

The breadth of results is also great to see.

### Weaknesses
One central part that was unclear to me was how the scale factors for learning are actually precomputed. Is this simply a scaling of the reference solutions from the solver? As this is the central component that is supposed to make the method work, I think it would be important to be clear where this comes from. Correspondingly, I was missing an evaluation in terms of how well the network actually learned to predict these scaling factors. The results seem to only show the loss in terms of the state.

The Holl'22 paper above also provides some theory on how updates from scale invariant solvers improve learning. Unfortunately the submission here does not take up on these topics, and focuses on experiments.

The appendix is also very brief on how the different learning tasks were actually set up.

### Questions
Closely related to the topics above, can the authors shed light on the following topics?

- How does the approach differ from the scale-invariant learning proposed in the NeurIPS'22 paper above?

- Does the theory there affect or relate to the current submission? 

- How are the scaling factors s_i computed, and how accurately are they inferred?

- Have the authors considered Newton methods, that approximate the inverse Hessian for "scale invariance"? I think this would also be worth a discussion, at least.

- The paper focuses on solving optimization problems in terms of PDE states. How would this extend to a second neural network, i.e. backpropagating further than just the u?

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
The paper studies solving partial differential equations (PDEs) numerically. The proposed framework builds upon a finite-difference spatial discretization of the unknown fields on a regular grid. Next, it minimizes a residual loss similar to that in the physics-informed neural network (PINN) via gradient-based optimization. The new idea comes in a neural network that predicts the update rule (scaling factor and direction) used in each step of the gradient-based optimization. The paper demonstrates this idea on several linear and nonlinear PDE problems.

### Strengths
- The idea of applying meta-optimizers to learning-based PDE solvers looks new to me. I think this is an interesting thought worth further discussion and exploration.
- The technical method is simple, straightforward, and easy to implement.
- The paper writing is good; it articulates its technical details very well.
- The paper considers a diverse set of PDE problems, including N-S equations and 3D cloth simulation (albeit with limited features).

### Weaknesses
 **Introduction/Related Work**
- The paper claims numerical methods for solving PDEs “are computationally
expensive”/“are still relatively expensive to compute”/“require high computational resources.” This argument is generally valid for large-scale problems. However, for the small-sized problems demonstrated in this work (400 x 400), Chances are that numerical methods are not as expensive as the paper indicates and may be faster than Metamizer (See Poisson/Laplacian problem below). I suggest the paper evaluate its method on problems of much larger sizes, e.g., on >=1024^2 (2D) or >=64^3 (3D) grids.

**Foundations**
- Equations 3 and 4 are not new and should cite the original PINN paper. It is probably also worth mentioning that minimizing Equation 3 may get stuck in a local minimum (grad L = 0, but L is nonzero), which is not a solution to the original PDE. For several problems (linear second-order PDEs) demonstrated in the experiments, a variational loss from the PDE’s weak form is a standard and a naturally better candidate for the loss design. The incremental potential in Eqn. 12 is one such example that highlights this point.
- The issue in Fig. 2 and the main intuition for taking gradients from previous steps into account have been extensively studied in numerical optimization methods. The former is typically handled with (exact) line searches, and the latter is discussed in (nonlinear) CG, L-BFGS, etc. (“Numerical Optimization” by Nocedal & Wright.) It is still very interesting to contemplate the possibility of training a neural network to exploit gradients from previous steps, but the paper should discuss its relation to these classic numerical optimization methods and compare them in an experiment.

**Experiments**
- The Poisson/Laplacian example has the most complete analysis, but the main results in Fig. 6 look dubious for several reasons:
1) It looks like Metamizer has used an Nvidia RTX 4090 GPU (line 330 and Appendix B), so it should be compared with linear solvers implemented on the same GPU. However, I don’t recall scipy having a GPU implementation of them. Please correct me if I am wrong.
2) The state-of-the-art GPU implementation of a Krylov subspace solver (CG, GMRES, etc.) is likely to be better than both the scipy baselines and Metamizer reported in Fig. 6 and Appendix B. Back in 2005, deploying a standard CG algorithm on a GPU could solve wave/Poisson equations on a 1024^2 grid at a rate of 10-30 fps (Chapter 44 in “GPU Gems 2” edited by Pharr & Fernando and the referenced papers), already arguably faster than the speed of Metamizer reported in the much smaller 400^2 problem. I feel this paper didn’t identify the right baseline for comparison.

- The wave equation example does not compare Metamizer’s performance with a baseline. I suggest comparing it with the CG-GPU baseline mentioned above.

- Eqn. 12 in the cloth example is not new and should cite its original source, e.g., Stotko 2024. This equation can be traced back to at least “Optimization Integrator for Large Time Steps” by Gast et al. in 2015, if not earlier.

- “Note that L can take negative values and cannot be interpreted as easily as the mean squared residuals of the previous PDEs. Thus we omitted L in Table 1 for our cloth simulations.” In this case, grad L = 0 is the right indicator for successfully solving the PDE. There should be a table reporting grad L after certain iterations.

- On the algorithmic side, I feel some classic approaches for exploiting gradients from past iterations should be considered for comparison to establish the advantage of the network module in Fig. 3a. Two candidates are nonlinear CG and L-BFGS (with history size = 2). These methods do not require training and can be directly used to minimize Eqns. 3 and 4.

### Questions
- Does CG fail to converge in Fig. 6? Is the matrix not symmetric positive definite?

### Soundness
2

### Presentation
3

### Contribution
2
