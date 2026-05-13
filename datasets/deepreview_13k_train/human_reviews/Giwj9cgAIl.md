# Mechanistic Neural Networks

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
We present Mechanistic Neural Networks, a new neural module that represent the evolution of its input data in the form of differential explicit equations.
Similar to regular neural networks, Mechanistic Neural Networks $\mathcal{}F(x)$ receive as input system observations $x$, \emph{e.g.} $n$-body trajectories or fluid dynamics recordings.
However, unlike regular neural network modules that return vector-valued outputs, mechanistic neural networks output (the parameters of) a \emph{mechanism} $\mathcal{U}_x=F(x)$ in the form of an explicit symbolic ordinary differential equation $\mathcal{U}_x$ (and not the numerical solution of the differential equation), that can be solved in the forward pass to solve arbitrary tasks, supervised and unsupervised. Providing explicit equations as part of multi-layer architectures, they differ from Neural ODEs, UDEs and symbolic regression methods like SINDy. 
To learn explicit differential equations as representations, Mechanistic Neural Networks employ a new parallel and differentiable ODE solver design that (i) is able to solve large batches of independent ODEs in parallel on GPU and (ii) do so for hundreds of steps at once (iii) with \emph{learnable} step sizes.
The new solver overcomes the limitations of traditional ODE solvers that proceed sequentially and do not scale for large numbers of independent ODEs.
Mechanistic Neural Networks can be employed in diverse settings including governing equation discovery, prediction for dynamical systems, PDE solving and yield competitive or state-of-the-art results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors introduce a methodology wherein they learn a neural network to output the coefficients of an ODE instead of the solution in itself, hence making the output of the neural network more interpretable. 

The key idea is that for the ODE written in the form of equation 2 in the paper (which is a general form that should comprise of both linear, nonlinear and time-varying PDEs), the authors propose to learn a neural network that outputs the coefficients of the ODE. The authors also point to the fact that their method can also be used to infer the (temporal) discretization of the ODE from observation data as well. 

The learning of the neural networks approximating the ODE coefficients is done by solving a system of equations subject to quadratic constraints. The number of parameter that the network needs to approximate are determined by the number of time-grids and the order of the ODE.

### Strengths
The work provides a very interesting methodology a single governing equation of a linear/nonlinear system in an interpretable manner. 

The authors show through their experiments that they are able to learn nonlinear ODEs (unlike previous work like SINDy). 

The methodology also enables the authors to infer quantities like the temporal discretization and also the initial conditions gives a set of trajectories which is quite useful/interesting.

### Weaknesses
While the methodolgy is pretty interesting, I wonder how it scales with the number of dimensions in the input data, and for more complex systems like Navier-Stokes. Some discussion related to it would be useful! 

The results on PDEs like Darcy Flow show that the network is not as much better (at least in performance) as compared to FNO baseline. It is not clear if the method offers a significant advantage over existing methods in terms of predictive accuracy, especially when considering the computational overhead of solving the constrained optimization problem. The performance gains, if any, need to be more clearly highlighted and quantified in comparison to other methods.


### Questions
- I am a bit unclear about how the authors are able to parallelize in terms of the sequences, I understand the parallel batchwise training aspect of the training. Is is that since we have ground truth training data, and the we can write down the forward and backward Taylor approximations, we get different sets of equations that are solved in parallel?
- It seems that the authors are solving a relatively complex system of equations stemming from the discretization of the ODEs. Are there any set of equations that may not be solvable due to the given methodology.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Mechanistic Neural Networks (MNNs), a neural module that represents the evolution of its input data in the form of differential explicit equations. Unlike some traditional neural networks that return vector-valued outputs, MNNs output the parameters of a mechanism in the form of an explicit symbolic ordinary differential equation. MNNs employ a new parallel and differentiable ODE solver design that can solve large batches of independent ODEs in parallel on GPU.

### Strengths
The introduction of Mechanistic Neural Networks provides a new approach to learning differential equations from the evolution of data.

### Weaknesses
1. The paper's clarity is wanting. For example, around eq(2), there's an inconsistency in notation with both $c_i(t;x)$ and $c_i(t)$ being used. Which of these is the intended notation? Additionally, there's no explicit description or definition of $b(t;x)$.
2. On page 2, the statement "In general, one ODE is generated for a single data example $x$ and a different example $x'$ would lead to a different ODE" is made. Could the authors elucidate why this is a characteristic of the modeling approach presented in eq(2)? Specifically, how does the architecture ensure that each input $x$ maps to a unique ODE, and what are the implications for generalization?
3. If a new instance $x'$ necessitates retraining the model, wouldn't it be more streamlined to directly learn a neural ODE through parameter optimization, bypassing the need for coefficients as functions of $x$? The current approach seems to add complexity without clear benefit if retraining is always needed for new data instances.
4. The paper's approach to solving any nonlinear ODEs using equality-constrained quadratic programming must have gaps. These gaps aren't clearly addressed. Relying on such an algorithm to solve any ODE without theoretical guarantees is precarious. A more transparent discussion on potential limitations is needed, including an analysis of the types of ODEs for which this method is expected to fail or perform poorly. For instance, what are the stability properties of this solver, and how does it handle stiff ODEs?
5. The methodology for handling nonlinear ODEs, as presented on page 4, lacks clarity and could benefit from a more detailed exposition. The description of how the non-linearity is incorporated into the QP solver and the loss function is vague. A concrete example of a non-linear ODE and its corresponding implementation details would greatly enhance understanding.
6. The literature review in section 4 seems outdated, with the most recent references dating back to 2020. A comprehensive literature survey, including more recent and relevant baselines, would strengthen the paper's context. For example for the ODE modelling, [1][2] may be included.
7. The term $\Theta \xi$ on page 6 is introduced without clear definition or context. Could the authors provide clarity on this? A proper definition of both $\Theta$ and $\xi$, as well as their role in the overall framework is needed.
8. The paper delineates two primary components: the learning of the ODE and its subsequent solving. However, the experimental section seems to lack comprehensive ablation studies that convincingly demonstrate the efficacy of each individual component. It is unclear how much each component contributes to the overall performance, and whether the proposed method is truly superior to simpler alternatives.

### Questions
Please clarify the issues raised in the weaknesses section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes mechanistic neural networks, a framework to learn differential equations. Given an input, these networks output (the parameters of) a differential equation. To solve the differential equations and backprogate through the solution, the authors first leverage old work from the 1960s, which frames numerically solving ODEs as a quadratic optimization problem. Then, they leverage more recent work allowing to solve and backpropagate through the solution of quadratic optimization problems given by neural networks. This way of solving and backpropagating through ODEs is more amenable to parallelization in a GPU than other methods used in neural ODEs. Finally, the authors perform a large amount of qualitative comparisons to show the effectiveness of their method.

Before starting my review, I do want to highlight that I am not an expert in differential equations nor in neural ODEs. While I found the high-level idea of the paper to be understandable, the details were very confusing. Notation is poorly chosen and the paper reads like a rushed submission. This opinion might nonetheless be a consequence of my own lack of expertise in the topic, so I will happily change my opinion on this if other reviewers who are more knowledgeable in the area disagree.

### Strengths
1. I believe the authors are tackling a highly relevant problem, which can be of interest not only to the machine learning community itself, but to physicists and scientists in general who are interested in using machine learning.

2. Improving the computational efficiency of ODE solvers with neural networks in mind is also a relevant problem, and the proposed method seems to perform well.

### Weaknesses
3. The notation is quite confusing, and I think the authors use the same symbols to denote different objects in different sections. For example, in section 2, $x$ is the input to the neural network, and $c$, $g$, and $b$ define the differential equation (eq 2). In section 3, $x$ is the variable being optimized over, $c$ is part of the objective, $b$ provides a constraint, and the matrix $G$ is a multiple of the identity that has nothing to do with the $g$ scalars defined in the previous section. The notation used by the authors is highly suggestive of a connection between $x$, $b$, $c$, $g$, and $G$ in these two sections, but unless I hugely misunderstood, there is no connection other than the quantities in section 2 characterize the optimization problem in eq 5.

4. I also found eqs 8 and 9 to not be clear, could you please further explain their role and how they are obtained?

5. The paper emphasizes throughout how it is fundamentally different than neural ODEs, making it sound like neural ODEs cannot be used to solve tasks that mechanistic neural networks can be used for. Yet, most of the empirical comparisons are carried out against neural ODEs.

5. Other than table 1, which compares exclusively solvers, the paper presents no quantitative comparisons against its baselines, only plots qualitatively comparing trajectories.

Finally, I have many minor comments:

- The line after eq 2 has $u^{(k)}$, should this be $u^{(i)}$?

- The line after eq 3 says $c_{d, t}$ and $c_d$, should these be $c_{i, t}$ and $c_i$, respectively?

- Using the same symbol for transpose than for time indexing is also confusing, I'd recommend using ^\top.

- \citep and \citet are used exchangeably throughout the manuscript, please use each one when appropriate only.

- In the abstract, lists are numbered as (i), (ii); whereas throughout the manuscript as (1), (2).

- Missing parenthesis above eq 4.

- Bottom of page 6: "not enough represent" -> "not enough to represent".

- "Planar and Lorenz System" paragraph: "represent" -> "represented"

- The phrasing "where we must classify per particles which class out of two it belongs too" is awkward.

- "a wing on gives rise" -> "a wing gives rise"

- "only and to predicting" -> "only and to predict"

- Period missing after the first sentence in sec 5.4.

### Questions
What is $\hat{r}$ in 5.4?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
