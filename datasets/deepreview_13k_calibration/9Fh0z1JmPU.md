# Progressively Refined Differentiable Physics

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
The physics solvers employed for neural network training are primarily iterative, and hence, differentiating through them introduces a severe computational burden as iterations grow large. Inspired by works in bilevel optimization, we show that full accuracy of the network is achievable through physics significantly coarser than fully converged solvers. We propose *progressively refined differentiable physics* (PRDP), an approach that identifies the level of physics refinement sufficient for full training accuracy. By beginning with coarse physics, adaptively refining it during training, and stopping refinement at the level adequate for training, it enables significant compute savings without sacrificing network accuracy. Our focus is on differentiating iterative linear solvers for sparsely discretized differential operators, which are fundamental to scientific computing. PRDP is applicable to both unrolled and implicit differentiation. We validate its performance on a variety of learning scenarios involving differentiable physics solvers such as inverse problems, autoregressive neural emulators, and correction-based neural-hybrid solvers. In the challenging example of emulating the Navier-Stokes equations, we reduce training time by 62%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This article presents a method to reduce the computational costs of end-to-end training with a linear PDE solver in the pipeline. In particular, the scope of this article is about linear solves that are big enough to require an iterative solver. It posits that the level of accuracy, that is needed of the forward model evaluation and its gradient, increases during training. The PRDP borrows inspiration from bi-level optimization schemes: the method starts with an inaccurate linear solver (where the number of iterations is stopped too early) and progressively increases the accuracy (or number of iterations in the solver) as the training starts to plateau. The authors provide an algorithm to schedule the number of iteration in function of the validation loss. The authors show computational savings from two major mechanisms: the progressive refinements (the early gradient updates in the training cost less iterations of the solver) and incomplete convergence (where the iterative solver reaches the desired accuracy without needed to train until the number of iterations is sufficient). The computational savings are up to 86% (case of the 2D heat equation if I understand correctly 72% (IC) + 14% (PR) = 86%, but the text only reports 81%), for more complicated examples, the savings go down to 59%.

### Strengths
This article is clearly written and introduces a promising solution to computational costs of training campaigns that include a linear PDE solver, end to end.
The main result, that progressively increasing the accuracy of the solver in end-to-end training converges to similar performance as a fully converged solver while substantially reducing computing costs, is original.
The benefit from incomplete convergence is very interesting. Although unexpected, the computational experiments show that they originate most of the computational savings.
It is interesting to see that the computational saving are larger for the 2D heat equations than for the 1D heat equation.
It is an interesting finding that unrolled differentiation which inefficiently accurately differentiate a sequence of iterative approximation performs similarly to the smarter implicit differentiation.

### Weaknesses
The paper suffer weak baselines. The main use case of the method is for iterative solvers of large linear models, however, the authors use 1D and 2D examples which would likely be solved efficiently by a direct solver. The authors should at least provide one 3D example with the simple heat equation. The heat equation itself is also a weak baseline, more complex linear models such as Helmholtz equation could be considered.

It is worrying that the benefit of the method diminish as the problem get harder as in the nonlinear neural emulator learning. Some discussion is needed about the potential harmful mechanisms that limited the computational savings in that case.

### Questions
Please add a computational experiment that scales where an iterative solver is necessary (e.g. 3D heat equation).
Please consider harder baselines for the linear emulator learning, such as Helmholtz equation.
Please add a discussion about potential mechanisms specific to nonlinear neural emulator learning that would explain the reduced computational savings.

Minor:
If needed, please correct the reported saving of the 2D heat equation to 72%+14%=86% as well as the maximum saving in the conclusion.

### Soundness
3

### Presentation
4

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
This paper introduces a framework to progressively refine the resolution of physics solvers during neural network training. The authors demonstrate that training a neural network with a physics solver scheduled to increase in iterations $K$ over training can significantly reduce computational costs, especially by using fewer iterations in the early training phases (*progressive refinement* savings). Additionally, they observe that a neural network can be effectively trained even when the physics solver has not fully converged, eliminating the need for an extensive number of solver steps to achieve high accuracy (*incomplete convergence* savings). To automate this process and determine optimal parameters for these refinements, the authors propose an algorithm that monitors validation set metrics, incrementally increasing solver refinement when performance plateaus. The framework is validated across four use cases: a linear inverse solver, linear neural emulator learning, nonlinear neural emulator learning, and a neural-hybrid emulator.

### Strengths
* The paper is well-written, with clear explanations of the intuitions and motivations behind the method.
* The algorithm is straightforward and effectively delivers the intended results, as seen in the reduction of validation loss with the progressive refinement of the physics solver, particularly notable in Figure 4 for the 2D Heat and 2D Navier-Stokes cases.
* The savings in training time and computational resources are substantial.
* The appendix is thorough and well-organized, with especially valuable details on iterative linear solvers and detailed derivations for each problem.

### Weaknesses
 * Overall, the technical contribution of the paper is somewhat limited, with the main novelty being the proposed algorithm for iterative refinements.
* All physics solvers employed rely on iterative linear solvers. It would have been interesting to see if the method also applies with other physics solvers, particularly those involving explicit time-stepping schemes where no linear solve is required, and the 'resolution' is determined by the spatial and temporal discretization.
* With the exception of the final example (the neural-hybrid approach), the other examples appear to be simplified or illustrative cases without clear, concrete applications. The chosen examples, while useful for demonstrating the core mechanism, do not fully explore the method's potential in more complex, real-world scenarios, such as those involving complex boundary conditions or irregular meshes.


### Questions
* How sensitive are the parameters of PRDP? Did you experiment with many different parameters for each problem before achieving the results, or was it relatively straightforward?
* Do you expect the method to achieve similar savings in training time for domains with complex boundary conditions and irregular meshing?
* Do you think your method could work where the physics solver contains incomplete physics (e.g., the parameters are not perfectly calibrated, and some terms of the equations could be missing)?
* How would the method be affected by noise in the observations?
* How well do you think this could help reduce the training time of neural GCMs [1]?

[1] Kochkov et al. Neural general circulation models for weather and climate. Nature, 2024.

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
2

### Summary
This paper proposes to use progressively refined differentiable physics, termed as PRDP, to increase the training efficiency while not harnessing the accuracy. The key finding lies in the fact that the full accuracy of the neural network is achievable through insufficiently converged solvers. Several experiments are conducted to validate the effectiveness of PRDP in reducing training time.

### Strengths
The topic this paper wants to tackle seems interesting. It seems intuitive that, considering the noiseness of neural network training and approximative nature of deep models, the physics solver does not need to fully converge for the network to achieve maximum possible accuracy. This paper proposes to use an adaptive strategy to progressively refine the physics solver and thus improve the training efficiency. Several experiments are conducted to verify the efficacy of the proposed method.

### Weaknesses
 - This paper should provide more background information about *differentiable physics* to make readers better understand the core contribution of the proposed method. I am not an expert of this field, and I find this paper a little bit hard to follow, and also unaware of the broader context this paper lies in.
- The experiment settings in this paper are not clearly presented. Considering that this is paper submitted to ICLR, I want to know what is the role of the neural networks in each experiment.

### Questions
The experiments report the improved efficiency by adopting progressive refinement and incomplete convergence. Does these strategies influence the accuracy?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
PRDP proposes an algorithm to reduce computational cost of training neural networks when a nested optimization problem is required during training. The authors first exhibit source of savings (IC and PR), before introducing their method. Specifically, this method consists in considering partially solving the inner problem in for the firsts steps of training and then refining this inner solution to more precise one as the training goes through. Moreover, the method considers not fully solving linear systems, since it may not greatly improve the performances. Finally, they evaluate their method on several PDE problems and instances.

### Strengths
- The paper is very complete. 
- Several experiments are proposed and isolate and illustrate well the 2 kinds of cost reduction proposed. 
- The proposed algorithm is easy to understand and well described. 
- A lot of details about training and the physical systems studied are proposed in the appendices. 
- The authors discuss impact and limitations of their work

### Weaknesses
 - The paper is very technical and I think pseudo code or a scheme would help in the comprehension of the method. For example, it is unclear to me where is the neural network used in the global framework/experiments, what are inner/outer optimization problems in the examples... Despite understanding the overall idea and performances of the proposed algorithm, I think more explicit and easy-to-understand notations would help the comprehension. A more detailed example would help for a precise comprehension of the framework proposed (see questions section).

 - The paper lacks a clear presentation of the training time required for the experiments. Given that the main claim is computation savings, this is a critical omission. The authors should provide a comparison of training times with and without PRDP, and ideally compare against standard methods to quantify the actual speedup achieved.

 - The choice of validation loss as the metric for the PRDP algorithm is not fully justified. While the authors mention it avoids issues with training loss, a more detailed explanation is needed. An ablation study comparing the use of training loss versus validation loss would strengthen this choice and address potential concerns about the validation set's representativeness. Moreover, it is unclear how the method would behave if the validation loss plateaus and then decreases again, a common scenario in neural network training with learning rate schedulers.

 - The paper does not adequately compare its results with existing methods, specifically the work of Um et al., despite using a similar setting for the Navier-Stokes experiment. A direct comparison of both performance and training times with Um et al. and other relevant methods cited in the related work section is necessary to properly evaluate the benefits of the proposed approach. The current lack of comparison makes it difficult to assess the novelty and impact of the method.

### Questions
-	Is this method only applicable in the context of Physical systems? It seems to me that this method could be more general and this being used in a broader range of applications, as soon as an iterative process incurs in the forward pass?  
-	Could the author also provide a comparison of the differences of performances w/ and w/o PRDP? (see for example Fig 1 where it looks like there is a very little difference in performances, thus making me wondering how much is this loss)
-	Why is the algorithm based on validation losses? In what does these losses consist in? At inference, these validation values are not available? 
-	What are the applications at inference? Once trained, what would be some application of NNs? Could this method be applied on new physical systems/PDEs/boundary or initial conditions/discretization? 
-	In section 2, what does the subscript h stands for? Are the parameters $\theta$ the neural network parameters to be optimized through training? 
-	On page 2, last paragraph it is stated that experiments are conducted on real world application, is the Navier-Stokes this example? These are synthetic data; in which sense do you consider this example as “real-world application”? 
-	In example 2.2, are the $\theta$ parameters optimized with the outer step? This means that one wants to optimize the forcing terms? The application would be to find the forcing term associated to a recorded and given trajectory? 
-	For the IC savings, I was wondering if the authors have tried to experiment if without NN, the performances would be better? My guess is that the introduction of a NN in the framework prevent the performances from being optimal, thus allowing for IC savings. What if the neural network size increases/its expressiveness improves? Are the performances better? 
-	The main claim of the paper is computation savings. Could the author provide training times for their experiments? And a comparison of this solving time with standard methods? 
-	What happen on cases where the losses plateau then decreases again? This situation could arise in some training of neural networks especially, when using a learning rate scheduler. How would behave the method in this context? 
-	In section 4.4 why don’t you compare your results (performances, training times) with the method from Um et al.? Since the setting is the same and your method is supposed to improve training times, it would be interesting to evaluate the benefit with other methods existing. Moreover, in the related work several methods are cited, and could be used as a comparison.

### Soundness
3

### Presentation
3

### Contribution
3
