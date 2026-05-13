# Neural Electrostatics: A 3D Physics-Informed Boundary Element Poisson Equation Solver

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Electrostatics solvers relate an imposed voltage to a
corresponding charge density. Current classical methods require fine
discretization and scale poorly due to the construction of a large linear system
of equations. We recast the problem using neural networks and introduce
neural electrostatics, a hybrid 3D boundary element method (BEM). By using the
boundary element form, we are able to overcome many shortcomings of previous
neural solvers, such as learning trivial solutions and balancing loss terms
between the domain and boundary, at the cost of introducing a large integral
containing a singular kernel. We handle this singularity by locally
transforming the integral into polar coordinates and applying a numerical
quadrature. We also show that previous neural solver sampling methods are unable
to minimize the PDE residual, and propose a variational adaptive sampling
method. This technique is able to reduce mean absolute error by 5 times, while
keeping training time constant. Extensive scaling and ablation studies are
performed to justify our method. Results show that our method learns a charge
distribution within 1.2 $pC/m^2$ of mean absolute error from a classical BEM
solver, while using 25 times fewer rectangular elements.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a neural solver for eletrostatics problems (Poisson's equation) where the loss function is inspired by the boundary element methods. Using this formulation, both the domain and the boundary integrals feature in the residual together, and therefore, no special weighing of domain and boundary terms is needed. A singularity appears in the boundary integrals, and the authors use a change of coordinate system for the boundary integral to handle this. The authors present their results on one particular example, and provide ablation studies on various test functions, loss functions and integration techniques.

### Strengths
The paper is well written.

I like how the $ i^{th} $ residual (Eq 5) is a linear combination of a domain integral ($ \textlangle v, \phi \textrangle $), and another term that contains a boundary integral. This means, the residual for each test function has a naturally formulated contribution from the domain and the boundary. Therefore, no extra weighing is needed between the boundary and the domain terms.

In scaling study, it is interesting to see that the method is largely independent of the size of the network (among the sizes tested).

### Weaknesses
A lot of the details are unclear. How does the mapping look like? Does the network take in the coordinate of a point as input, and return both $ \phi $ and $ \rho $? The mapping detail, and the architecture should be made more precise. A flow-chart / picture might help.

Only one simple problem is considered in the results section.

Minor:

A lot of abbreviations used without explanation.

Sec 2 header: "work"

line 134: vein instead of vain

### Questions
Please specify ''rectangular test function'' precisely.

Fig 2: why are the errors for 225 test functions higher than both 25 and 100 test functions?

Please state the boundary conditions for the example considered in Sec 5.

The authors use the so-called "fundamental solution'' as Green's function in this paper. The fundamental solution pertains to the PDE solved on $ R^n $ with no boundary condition. But the considered example is a finite domain with some boundary conditions (though the boundary conditions are never stated). Does the Green's function remain the same as the fundamental solution in this case? Could the authors please explain this in detail?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work applies PINN in a boundary element form to solve electrostatics problems. The singularity issue is handled by locally transforming the integral into polar coordinates. A variational adaptive sampling method is also introduced to improve the solving efficiency. Experimental results show the proposed method can obtain results similar to a traditional BEM solver while using 25 times fewer elements.

### Strengths
- The idea of this work is reasonable in principle.
- The writing is overall clear and detailed.

### Weaknesses
 - This paper limits itself to solving electrostatics problems. On the other hand, it can be easily extended to a wider range of scenarios in the computational mathematics sense, so that it will be more appealing to a much wider audience of ICLR.
- Combining PINN and the boundary integral equation has been investigated by a few previous works, e.g., [1]. However, there are no analytical or experimental comparisons provided in this paper.
- The experiment is overall too simple and not very convincing. The provided test case is just 1 specific example, which is not very difficult in scale and in smoothness. Also, there lacks comparison to previous works, for example PINN variants designed for BEM.

### Questions
/

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposed a novel electrostatic solver by combining an adapted physics-informed neural network (PINN), and a 3D boundary element method (BEM). With special techniques, the solver can simplify the original 3D problems into 2D problems, and solve them more effectively. The results are demonstrated on an experiment of a flat plate with constant charge, and with different test function configurations.

### Strengths
- The paper is easy to follow, well conveyed, and I appreciate that.
- The proposed 3D boundary element solver is able to combine domain and boundary losses into a single loss.
- By transforming the integral equations into polar coordinates, the solver can remove singularity.
- A variational sampling techniques is introduced to improve accuracy of the solver.

### Weaknesses
 - I did not see any demonstration of the neural network architecture. A diagram would help. Implementation details such as training data size are also missing.
- I expect more contents in the result section. More experiments are needed to evaluate the neural network model. For example, different geometry domains, different scale, etc.

### Questions
- Is the neural solver able to generalize to different domains, ie, different shape or size?
- To judge the practicality of the solver, do you have inference time recorded? Is it faster than the classical method?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims at finding the density field in 3D electrostatic problems. This is done by modelling the density with a neural network, which is learnt in PINN fashion. Instead of solving the problem in its 3D original setting, the authors use known results from the literature that relate the solution in 3D to the solution at the 2D boundary, which is called boundary element method. This approach is known in the literature of PINNs but present some shortcomings. The contribution of the authors is to formulate the problem in spherical coordinates to avoid the singularity in the fundamental solution and to use a resampling scheme to improve the results.

### Strengths
- the idea of exploiting boundary elements method is indeed interesting both from a computational and conceptual point of view, even though it is not new in the literature
- the paper is easy to read

### Weaknesses
 - the contribution of the paper is limited to the choice of spherical coordinates and of resampling test functions (which is however borrowed from PINNs trained with collocation points).
- I have the impression a classical numerical solver would anyway be preferable, especially in the simple (and only) setting used for evaluation.
- the paper is missing some important references to other PINN approaches that exploit the idea behind boundary element methods [1,2,3]. In particular, all papers study the Poisson equation, which is the focus of the present paper as well.


### Questions
1. As argued in the paper, the proposed approach has the benefit of decoupling base functions from test functions with respect to classical numerical solvers. However, in the paper I did not find any strong reasons or discussion why PINNs should be used instead of the numerical solver. What is the main argument why the proposed approach should be preferable than the standard numerical solver? Is there any experiment where you show that for the same accuracy you require significantly less computational resources?
2. Did you actually mean that training time for the proposed method is orders of magnitude "longer" than classical numerical methods or did you mean "shorter"? line 535: "Training time of the technique is orders of magnitude longer than the BEM solver, as it uses highly optimized linear algebra solvers". This would make the BEM solver significantly more preferable than the proposed method.
3. The only experiment shown is very simple and by itself does not justify the use of the proposed approach. I believe that the paper would greatly benefit from further experiments and evaluation, possibly in less trivial settings 
4. Furthermore, the comparison with PINNs would require some more in-depth analysis. I would expect that when many collocation points are used (as many as they can fit in the GPU) a somewhat reasonable solution is learnt. Do you observe this? if so, it would be interesting to see a comparison as a function of the collocation points used. Recent work RAD [4] improves on RAR and would be a relevant comparison for the present method.
5. I am a bit confused about the singularity argument in Equation (7). If I understand correctly, with spherical coordinates the singularity in the denominator is absorbed in the singularity of the coordinate system, so one can compute the integral without worrying about it. However, doesn't this hold only for point sources?
6. I also have a broader question concerning the boundary element method for Equation (1). Isn't the dimensionality reduction from 3D to 2D only possible for point sources? or anyways for sources that allow to compute the source integral easily?

I found the following typos in the paper:
- 88 "decision decisions"
- 182 "v_i, ..., v_N" --> should be "v_1, ..., v_N"
- 202 "Singularity in 12"  --> I guess you meant 2 and I would add "Eqaution" as you did throughout the paper
- 203 "simultaneous" --> "simultaneously"
- 338 I would suggest to use another notation since epsilon was already used in Equation 8
- 431 "test function" --> "test functions"
- 445 Figure 4 does not have a caption saying that it is Figure 4

[4] Wu et al., A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks, Computer Methods in Applied Mechanics and Engineering, 2022.

### Soundness
2

### Presentation
2

### Contribution
1
