# Learning HJB Viscosity Solutions with PINNs for Continuous-Time Reinforcement Learning

- Decision: Reject
- Scores: 8, 5, 3, 5

## Abstract
Despite recent advances in Reinforcement Learning (RL), the Markov Decision
Processes are not always the best choice to model complex dynamical systems
requiring interactions at high frequency. Being able to work with arbitrary time
intervals, Continuous Time Reinforcement Learning (CTRL) is more suitable for
those problems. Instead of the Bellman equation operating in discrete time, it
is the Hamiltonian Jacobi Bellman (HJB) equation that describes value function
evolution in CTRL. Even though the value function is a solution of the HJB
equation, it may not be its unique solution. To distinguish the value function
from other solutions, it is important to look for the viscosity solutions of the HJB
equation. The viscosity solutions constitute a special class of solutions that possess
uniqueness and stability properties. This paper proposes a novel approach to
approximate the value function by training a Physics Informed Neural Network
(PINN) through a speciﬁc $\epsilon$-scheduling iterative process constraining the PINN
to converge towards the viscosity solution and shows experimental results with
classical control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new way of solving Hamilton-Jacobi-Bellman (HJB) equation using the framework of Physics Informed Neural Network (PINN). To find the viscous solution, which is the optimal value function, this paper proposes an iterative algorithm to gradually decrease the epsilon for approximation.
The proposed algorithm works well in the pendulum task, but a problem in applying the method for higher dimension systems was identified.

### Strengths
This paper nicely reviews the concept of the viscous solution of HJB equation and presents a novel way of obtaining the solution by PINN, which utilized the automatic differentiation capability of recent deep learning tools.

### Weaknesses
Although the title is "reinforcement learning," this method requires an analytic model of the system dynamics and the cost/reward function to apply PINN, and the states are sampled uniformly randomly in the state space. It may be better called optimal control rather than reinforcement learning, which usually assumes that the agent explore the environment by its own policy without explicit prior knowledge of the environment.

In Figure 1, why are the solutions have a dip at the origin, where the value function should be maximum. Is there any issue with dealing with the terminal cost/reward?

For people new to PINN, isn't it better to include the network architecture diagram with inputs, outputs, and how derivatives are combined for the objective function?

### Questions
In Figure 1, why are the solutions have a dip at the origin, where the value function should be maximum. Is there any issue with dealing with the terminal cost/reward?
For people new to PINN, isn't it better to include the network architecture diagram with inputs, outputs, and how derivatives are combined for the objective function?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed and testes a neural network based method for solving a deterministic Hamilton-Jacobi-Bellman (HJB) equation. The method utilizes the stability of viscosity sub(super)solution of HJB equation, and solves a sequence of PDEs to approximate the solution to HJB. Each PDE is solved by PINN method. Numerical experiments show that the proposed method outperforms PPO and A2C, but not the dynamic programming when it can be applied.

### Strengths
A new method for solving deterministic HJB, showing success in limited numerical experiments.

### Weaknesses
Generally, there lacks theoretical study for numerical solutions to a PDE. To ensure the necessary convergence, the conditions of Lemma 3.1 have to be verified, most importantly $W^\epsilon$ converges to $W$ uniformly. What presented in the subsection of $\epsilon$-schedulers is not adequate for this purpose. The $\epsilon$-scheduler, as described, does not provide a rigorous guarantee of uniform convergence of the approximate solutions $W^\epsilon$ to the true solution $W$. The adaptive scheduler aims to ensure that $\delta(\epsilon, \theta)$ converges to zero, but this is a convergence of the residual, not necessarily the solutions themselves. The uniform convergence of the solutions is a much stronger requirement and is not addressed by the proposed scheduling. The regularization loss in Eq. 10, while helpful, does not guarantee uniform convergence either, as it only encourages solutions to stay close to previous ones, but does not ensure convergence to the true solution. 

There are also several families of numerical methods for solving HJB, not limited to the ones that the authors listed (FD,FEM) and can be easily found in literature(such as level set , the method proposed here need to be compared to them for effective and accuracy. The authors should provide a more comprehensive comparison with existing numerical methods for solving HJB equations, including level set methods. The argument that level set methods are limited by domain discretization and are more suitable for finite-horizon problems is not entirely convincing, as many HJB problems can be reformulated or approximated in a finite-horizon setting. A more detailed discussion of the limitations and advantages of different methods is needed.

The numerical experiments are limited to a few small scale problems, some large scale, high dimensional examples can certainly improve the quality of the paper.

### Questions
Several key parameters given between equation (12) and (13) are not presented precisely, for example how to pick $k_\epsilon$ exactly for a given problem and the definition of $N_S$.   

Could numerical methods for HJB be more thoroughly surveyed and compared? See e.g. Falcone, M., Ferretti, R.: Numerical methods for Hamilton-Jacobi type equations. Handb. Numer. Anal., Elsevier/North-Holland, Amsterdam,17, 603–626 (2016).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduced a numerical method for solving continuous time HJB equations in a deterministic control and reward setting. The method depends on convergence theory of viscosity solutions to value function, a core Lemma that the authors elaborated in a very clear and accessible way. With three different types of decaying schemes for a core parameter $\epsilon$, the authors used PINN/PDE solvers to solve a sequence of PDEs that approximate the interested optimal control problems. Numerical experiments demonstrate the introduced method is effective on some of the classic control tasks, although there are challenges to be addressed in the continuous time setting.

### Strengths
The authors give a very detailed and clear introduction of optimal control problems in continuous time and the necessity of involving viscosity solutions. This (and the Appendices) makes the manuscript very easy to understand for non-experts in control theory. The authors also provide plentiful details on the numerical experiments, such as how to blend different $\epsilon$ decaying schemes, what types of NN are more suitable for learning viscosity solution, etc. Numerical experiments, although for simple classic tasks, demonstrate acceptable improvements over other SOTA RL/optimal control methods.

### Weaknesses
The main weakness of this manuscript is its novelty and magnitude of its contributions in terms of both theoretical and experimental aspects. The details are listed below:

1. The main theoretical foundation is Lemma 3.1, which is a well-known results in optimal control community. For clarity, the authors have to spend more than half of the main context introduce this Lemma. This left the only novelty in the algorithm design where the authors introduced three $\epsilon$ decay schemes and the PDE solver (the latter of which has also been widely studied by PDE people). The overall significance of this work is therefore limited.

2. If the authors want to enhance the theoretical contribution of this work, I would prefer to see how they would address the convergence in more details. Lemma 3.1 is a general result, but in the PINN setting, what conditions on the NN can guarantee convergence and how to characterize approximation error or convergence speed, etc. These are challenging theoretical questions if the authors want to go multiple steps further than just citing Lemma 3.1 as the foundation of their method.

3. If the authors want to focus on the experimental aspect of their approach, I believe high dimensional control tasks may be the right playground for PINNs. The purpose of introducing NN in PDE community is for solving large dimensional problems. The value of PINN for optimal control problems are likely to be similar. Otherwise, with known dynamics and easily observable rewards (as in this work), it is relatively easy to come up with efficient functional forms to approximate value functions without PINNs.

### Questions
My suggestions for a more in-depth analysis from either theoretical or experimental perspective are in the above section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a training scheme for neural networks to approximate
viscosity solutions of HJB equations. This presents a principled
approach to optimal control in continuous-time deterministic RL
settings, overcoming the curse of dimensionality incurred by existing
viscosity solution methods that rely on space
discretization. Experiments on classical control environments with
small timesteps are conducted, and the authors both demonstrate
desirable performance of their proposed method and identify the
remaining challenges.

### Strengths
I found the approach presented in the paper to be interesting. While
it is based on an existing approximation scheme for viscosity
solutions, I have never seen this applied to RL or general function
approximation methods for solving HJB equations. The approach is
sensible, and highlights an alternative paradigm to value learning
that replaces bootstrapping with PDE solving (using something like a
collocation method, as I understand it). I really appreciate how the
authors identified the remaining challenges surrounding their
approach, which seems to provide nice motivation and direction for
future work. I generally enjoyed learning about the proposed method,
and found the scheduling and regularization technique interesting.

### Weaknesses
The most major issues for me are:
1. The PINN method does not perform as well as existing DTRL methods
   (or at least PPO) in settings that require function
   approximation. While I appreciate that the authors give some
   insight about why that may be the case (and ideas for future
   research towards bridging the gap), I wish there was more
   motivating results: even if the highlighted issues with the
   approach are solved, what benefits should we expect to see relative
   to DTRL algorithms? Particularly, it would have been nice to see
   some results from the PINN method trained on much more data (i.e.,
   to overcome the uniform sampling issue), to visualize the benefits
   we can expect if we eventually find a more efficient training
   scheme.
2. While the $\epsilon$ schedules that are presented seem intuitively
   reasonable, it would have been nice to see more discussion and/or
   analysis about those in the paper. I understand that space is
   limited, but 5 pages are spent before the method is even
   presented. Is there a theoretically principled way to choose the
   $\epsilon$ schedule, or is there a principled way to quantitatively
   compare them?

When referring to the HJ-DQN algorithm (Kim et. al, 2021), it says
"this approach is limited to Lipschitz continuous control". I am
familiar with this paper so I know what this means, but I definitely
think it is worth clarifying further, since "Lipschitz continuous
control" can be interpreted in at least a few different ways. On this
note, is this really a limitation? Controls that vary smoothly in time
are often desirable.

Citations for Definition 3.1 and Lemma 3.1 should be given.

It should be made more clear why you call some HJB solutions "bad" vs
"good".

### Questions
The paper says that the work of Darbon et. al 2023 "work with min-plus
algebra", what does that mean? What types of optimal control problems
is it not suitable for?

In equation 7, what is $\nabla^2_x$? Is that the Laplacian? Likewise,
just below, what is $\nabla^2_{xx}$? What is the significance of the
RHS in equation 7, can we choose other "perturbations" instead? How
can you know if the RHS in equation 7 converges to 0 when
$\epsilon\to 0$?

At the bottom of page 5, it says "dynamic programming approaches are
able to find the solutions of the HJB equation that are intrinsically
viscosity solutions" -- what does "intrinsically viscosity solutions" mean?

Why does PPO seemingly scale better than the PINNs method? Is this
just because PPO is specializing to regions of the state space visited
by nearly optimal policies, whereas the PINNs method has to train on
the whole space? How do the methods based on the Pontryagin maximum
principle that were mentioned in the related work compare?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
