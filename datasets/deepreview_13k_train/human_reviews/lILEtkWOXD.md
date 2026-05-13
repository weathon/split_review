# Contractive Dynamical Imitation Policies for Efficient Out-of-Sample Recovery

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Imitation learning is a data-driven approach to learning policies from expert behavior, but it is prone to unreliable outcomes in out-of-sample (\oos{}) regions. While previous research relying on stable dynamical systems guarantees convergence to a desired state, it often overlooks transient behavior. We propose a framework for learning policies using modeled by contractive dynamical systems, ensuring that all policy rollouts converge regardless of perturbations, and in turn, enable efficient \oos{} recovery. By leveraging recurrent equilibrium networks and coupling layers, the policy structure guarantees contractivity for any parameter choice, which facilitates unconstrained optimization. Furthermore, we provide theoretical upper bounds for worst-case and expected loss terms, rigorously establishing the reliability of our method in deployment. Empirically, we demonstrate substantial \oos{} performance improvements in robotics manipulation and navigation tasks in simulation.
\let\thefootnote\relax\footnotetext{Corresponding author: \texttt{amin.abyaneh@mail.mcgill.ca}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses limitations in traditional imitation learning (IL) by introducing a framework based on contractive dynamical systems. The goal is to create imitation policies that reliably generalize to out-of-sample (OOS) states and remain stable under environmental perturbations. The approach leverages recurrent equilibrium networks (RENs) and coupling layers to ensure contractivity across all parameter values. By formulating the imitation problem as a differentiable ODE, the authors achieve efficient training with unconstrained optimization. The framework is demonstrated on robotics tasks, with improved OOS performance compared to existing methods.

### Strengths
- The paper introduces a novel approach to imitation learning by employing contractive dynamical systems, going beyond traditional stability guarantees to enhance policy reliability in out-of-sample (OOS) regions and under perturbations.

- The authors provide theoretical bounds for loss term.

- The idea of integrating recurrent equilibrium networks (RENs) and coupling layers to ensure that the policy is contractive regardless of parameter choices seems interesting. This idea enables efficient training with unconstrained optimization and simplifying policy deployment.

- Experimental results on LASA and Robomimic datasets demonstrate improvements in OOS recovery and imitation accuracy over baselines.

- I appreciate that the authors provided code base for reproducibility. Also, the paper is well-written.

### Weaknesses
 - No comparison of computational complexity along with wall clock time against the baselines is provided.

- In the policy representation, the usage of RENs and coupling layers adds complexity. I am expecting a discussion around this as well as the complexity of the baselines.

- While I appreciate that the authors provided bounds on the loss term, the result is too simple, I was expecting some sort of sample complexity result to actually see the sample requirements for their method.

- SNDS paper also includes discussion on high-dimensional Snake demonstrations. I don't see experiments on such data in this work.

- I have some questions that I would like to get answers to in the Questions section.

### Questions
- The paper assumes that there is a given final state and that the initial states may be perturbed. However, how to deal with the cases where the target state is not fixed? For example, in the MuJoCo environments, the only requirement is to have the robot work successfully for 1000 steps and there is no constraint on final state as such. How to deal with this case?

- The above also brings me to the question that if for every expert trajectory in the dataset, the final state changes. Will your method work in this case? If not, how would you address that? Currently, I see that the number of steps in each trajectory can be different but the final state is still the same.

- How much is the algorithm sensitive to the quality of expert demonstration? If the data comes from a suboptimal policy, what should one expect would happen in this framework?

- Maybe I missed this but does the method do interaction with the environment during learning? If yes, then some comparison of number of interactions made by different algorithms is needed.

- The model’s performance is sensitive to the contraction rate, as mentioned by the author, I am curious how critical this is when we have to run the algorithm on some new task.

### Soundness
3

### Presentation
3

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
This paper proposes a method for learning an autonomous dynamical system model from data. Specifically, the data is assumed to be in the form of recorded state trajectories from a dynamical system controlled by an "expert" policy. The proposed model is "contractive" by construction; that is, all solutions of initial value problems (IVPs) using this model exponentially converge towards each other.

The paper claims that using a contractive model improves robustness of the learned model to out-of-sample (OOS) states. Specifically, if the model and expert-controlled systems are initialized at a state in a bounded region near those in the expert-demonstration data, then the error between the model and expert-controlled rolled-out state trajectories differs from the empirical loss by at most a constant. This claim is accompanied by theoretical and simulated experiment results.

### Strengths
The paper shows a good effort put into communicating concepts from contraction theory and dynamical systems in an imitation learning context. The simulation experiments encompass a variety of systems that make them potentially compelling, in particular to the robot learning community. The choice of loss term weights in Equation (9) is, to the best of my knowledge, novel; moreover, their use in establishing the bound in Theorem 4.1 is neat.

### Weaknesses
My primary issue with this paper is its misuse of the term "policy", and its presentation as a paper that supposedly does policy learning. As mentioned in my summary of this paper, the proposed method learns a model of an _autonomous dynamical system_, i.e., one that is uncontrolled or has a fixed controller. In other words, given a system described by the ODE $\dot{x} = f(x)$, or $\dot{x} = f(x, u) = f(x, \pi(x)) \eqqcolon f_\pi(x)$ with fixed controller $u = \pi(x)$, the method in this paper learns an approximate model $\hat{f}$ for $f$ or $f_\pi$. This is not policy learning, which would instead attempt to explicitly learn a controller $\pi$. Specifically, in an imitation learning context, policy learning would involve trying to learn whatever "expert policy" $\pi$ gives rise to the data in the expert demonstration set.

This is an important distinction to make, particularly for the robot learning community that this paper seems to target. Learning an imitating policy would allow a user to then deploy the policy on the actual robot to autonomously recreate expert demonstrations (within some error). However, just learning a model for the closed-loop "dynamical system + expert policy" does not enable this. This diminishes the proposed contribution.

There are also a couple of mathematical issues (although they may be remediable):
- In the linear projection $P_\theta z$ with $P_\theta \in \mathbb{R}^{N_y \times N_z}$, from the paper and the accompanying code, the authors seem to use a much larger latent dimension $N_z$ than robot state dimension $N_y$. However, $P_\theta$ then cannot be injective (i.e., have full column rank), and so the left inverse $P_\theta^\dagger$ does not exist in general (even if it may still be computable without errors on a computer using floating point arithmetic).
- Each reciprocal in the _harmonic_ mean (not geometric mean as incorrectly mentioned in the appendix on page 16) in Equation (9) is only defined when the initial condition does not match any of the expert trajectories (otherwise you get 1 / 0). However, having the same reciprocal in the numerator may make the limit tend to 1 (since $\lim_{a \to 0^+} (1/a) / (1/a + 1/b) = \lim_{a \to 0^+} 1 / (1 + a/b) = 1)$, although this should be clarified in the paper. More importantly, the submitted code does not seem to use these weights at all and instead just uses the regular mean (see `loss = criterion(out, expert_trajectory).mean()` on line 83 in `ren_trainer.py`).

### Questions
- Please clarify whether the work does or does not learn an implementable controller / policy for the system (e.g., robot). In the case of the latter, are there "real-world scenarios" (page 6, line 293) where this might be useful, particularly for the robot learning community? Describing these would be crucial to better establishing the proposed contribution.

- Can you remedy the issue of non-injective $P_\theta$ in Equation (7)? Since there are multiple possible $z_0 \in \mathbb{R}^{N_z}$ corresponding to a given $\hat{y}_0 \in \mathbb{R}^{N_y}$ when $N_z > N_y$, is there a way to make a "best" choice?

- Please clarify where the submitted experiment code actually uses the weights $ \lambda_m(\hat{y}_0) $. Do they make a difference in the results when compared to just using the standard mean?

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
3

### Summary
The paper proposes a method (SCDS) for imitating trajectories by learning a contractive latent dynamical systems. Contractivity means, that the resulting (latent) trajectories of any two initial states exponentially converge to the same trajectory with contractivity rate $\gamma$. By enforcing contractivity, the paper aims to put more focus on approaching the goal in the same way as the demonstrations.

For modeling the latent dynamical system, SCDS uses a recurrent equilibrium network (REN, Martinelli et al., 2023), which already enforces contractivity by design. The latent state is mapped to the observed state by linearly projecting it to the desired dimension and then applying a learned bijection. The parameters of the REN, the projection and the bijection are learned end-to-end by minimizing a weighted MSE between the generated trajectory and the different demonstrations, where the trajectories are generated by first obtaining the latent initial state (by applying the inversed bijection of the observed initial state followed by a pseudo-inverse of the linear projection), and then integrating the latent dynamical system using a neural ODE. For computing the MSE between trajectories of potentially different length, SCDS applies dynamic time warping; the weights for the weighted MLE are computed such that the closest demonstrations obtain the largest weights.

Apart from presenting this architecture, the paper shows a lower bound on this weighted MLE for any initial states within a certain region of the demonstrated initial states, and compares the method with baselines on simulated robot environments.

### Strengths
The presentation of the method is very clear. Figure 1 illustrates the problem setting quite well, and Figure 2 gives a good overview of the pipeline.

The experimental results are good, and show that the reproduced trajectories behave similar to the demonstration, for initial states that are close to the demonstrated initial states.

The proposed pipeline is novel.

The claims seem to be correct, although the discussion of the experimental results need to be toned down, as the benefits are often not significant (e.g. in Table 1).

### Weaknesses
__Relevance__

The proposed method has several limitations:
- First of all, it is to note that the problem setting only involves imitating state trajectories, without accounting for the robot dynamics and therefore the feasibility of the planned motions. This is a significant simplification, as the feasibility of a trajectory is crucial for real-world robotic applications.
- The methods assumes that all demonstrations end in the same state, which is rarely the case for practical problems where demonstrations might have slight variations in their final states due to noise or different environmental conditions.
- By applying DTW, the method is not able to imitate velocity profiles. While DTW is useful for aligning trajectories, it inherently discards the temporal information, making it impossible to learn the velocity profiles of the demonstrations.

__Soundness__

- The weighting for the MLE loss (Eq. 9) is not derived from first-order principles. The rationale behind the specific weighting scheme is not clearly justified, and it is unclear how this weighting affects the overall optimization landscape.

- Assumption 4.1 seems to be overly strong, as it assumes that *all* (rather than any) demonstrated initial states are close to $\hat{\mathbf{y}}\_0$. This assumption might not hold in many practical scenarios, especially when dealing with a diverse set of demonstrations.

- The mapping from latent state to observed state is not invertible and therefore requires the use of a pseudo-inverse. As a consequence, the generated trajectory might not start at the correct initial state, which can lead to deviations from the desired behavior, especially at the beginning of the trajectory.

- Although the experiments involve settings with multi-modal initial state distributions, it seems like such settings are not compatible with the aim of learning a dynamical system where all trajectories converge to the same one. I assume that approaching a goal from very directions would only be possible with loose contraction rates, which would defeat the main motivation of the paper. The inherent conflict between contractivity and multi-modality needs to be addressed more thoroughly.

__Experiments__

- The presentation of the experiments in Table 1 highlight the best mean MSEs, although the confidence intervals are quite large, which is a bit misleading. A more appropriate presentation would involve statistical tests to determine if the observed differences are statistically significant.

- The "OOD" initial states are still rather close to the initial states of the demonstrations. It would be interesting to evaluate the different methods for more distant initial states. It would also be interesting to evaluate the demonstrations at states that appeared during the end of a demonstration, to assess the method's ability to generalize to different parts of the demonstrated trajectories.

- Qualitatively, the generated demonstrations tend to collapse to the same trajectory, which is not surprising given the objective. However, oftentimes, we are also interested in capturing the variance of the demonstration, which can be important for variable stiffness control. In that respect, the baseline SDS-EF yields arguably a better imitation. The paper should discuss the trade-off between contractivity and the ability to capture the variance of the demonstrations.

### Questions
- Were the metrics in Table 1 computed by weighting the demonstrations using Eq. 9? Wouldn't this bias the results in favor of the proposed method?

- Why isn't the contractivity in conflict with multimodal trajectory distributions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies how to learn a policy with contractive guarantee for out-of-sample recovery on a dynamical system. Remarkably, The paper 1) instantiates their DS policy through contractive REN, bijective transformation and neural ODE solver, with careful considerations of their each feature and applicability; and 2) provides thorough mathematical analysis on contractivity of the  proposed methods and an upper-bound of the loss when initial states locate in a multi-focal ellipse region. Finally, the authors provide empirical results on 2 datasets and a simulated environment, demonstrating the favorable performance of their methods.

### Strengths
## originality:
The paper creatively integrates several interesting techniques, i.e. contractive REN, neural ODE and coupling layers into their methods, resulting in a successful and analyzable performance. To my knowledge, the method is both novel and effective, with a clean and elegant design.

## quality:
Some mathematical analysis are performed on the contractivity of the proposed method, SCDS. Notably, an upper-bound of the true loss $\mathcal{L}(\rho_0; \theta)$ is derived and provides much insights.

## clarity:
The paper is well written with clean words and appealing figures. It is easy to read and comprehend.

## significance:
Under the condition considered (the initial state locates in a multi-focal ellipse of in-data samples), the method proposed offers rigorous guarantee of contractivity and favorable  performance, which is illustrated by numerical and visual results in experiment section.

### Weaknesses
I have 2 major concerns of this work:

1.  the lack of consideration of  control input $u$, and the system dynamics with it, $\dot{s} = f(s, u)$. Together with the ignorance of first-derivative of the system state. The author's  problem formulation reduces to how to generate state-only trajectory to meet the desired system requirement. Unfortunately, in my opinion, this approach of system modeling and problem formulation doesn't tackle the difficulty we usually meet in Robotics: 1) the real-world robotic system always has dynamics capacity and not every planned trajectory is equally executable hence the real-world impact of SCDS remains unknown; 2) Without the consideration of system dynamics in terms of control input, it's hard to assess the significance of the proposed method. Actually, under this simplified situation, the theoretical derivations and contractivity guarantees seem to be an over-kill.  One could simply generate trajectory interpolating towards the nearest in-sample point then exactly follow its trajectory.

2. the overly-simplified experiment settings. Besides the simplification in problem formulation, the experiment settings are also too narrow. There are 2 settings of the initial states in the experiments: 1) the initial states are sampled directly from the dataset; and 2) the initial states are sampled from a multi-focal ellipse of the in-dataset samples, with a radius of 0.1 of its norm. I think this experiment setting is neither challenging nor fitting for the real-world cases where OOS recovery is in great need.

### Questions
for concern 1,

1. could you provide papers/references to showcase how your problem formulation could lead to  methods with successful real-world deployments/applications on robotic system? 
2. could you provide analysis on the realizability of the trajectory generated by your methods? i.e. does it always generate trajectory that is executable for the underlying robotic system? if not, could you provide analysis or experiments on the performance of your method under this situation? 

for concern 2,

1. In your experiments, could you set the initial states to be in some regions where state visitation density is low and show its performance? 
2. could you try training a diffusion model based policy (with treating the problem as future state generation conditioned on current state and train it with a data augmentation that adds the same level of ellipse noise to conditioned input state) and evaluating it in your experiments? I suspect this would already generate a decent performance on the experiments you conducted.

### Soundness
2

### Presentation
3

### Contribution
2
