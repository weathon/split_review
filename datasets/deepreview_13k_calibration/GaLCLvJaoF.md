# Robust Model Based Reinforcement Learning Using $\mathcal{L}_1$ Adaptive Control

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We introduce $\mathcal{L}_1$-MBRL, a control-theoretic augmentation scheme for Model-Based Reinforcement Learning (MBRL) algorithms. Unlike model-free approaches, MBRL algorithms learn a model of the transition function using data and use it to design a control input. Our approach generates a series of approximate control-affine models of the learned transition function according to the proposed \textit{switching law}. Using the approximate model, control input produced by the underlying MBRL is perturbed by the \ellone adaptive control, which is designed to enhance the robustness of the system against uncertainties. Importantly, this approach is agnostic to the choice of MBRL algorithm,  enabling the use of the scheme with various MBRL algorithms. MBRL algorithms with \ellone augmentation exhibit enhanced performance and sample efficiency across multiple MuJoCo environments, outperforming the original MBRL algorithms, both with and without system noise.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a control-theoretic augmentation scheme for Model-Based Reinforcement Learning (MBRL) algorithms. This method is designed to enhance the robustness of the MBRL system against uncertainties, using MBRL perturbed by the L1 adaptive control.

### Strengths
The paper attempts to balance theory and empirical validation. It aims to integrate Model-Based Reinforcement Learning with control.

### Weaknesses
The paper has flaws both with theory and experiment.

  1. In theory, there is so much technically that is incorrect.  Some issues are highlighted below.

  2. The evaluation does not compare the proposed method with recent competitors, such as:

Annaswamy, A. M., Guha, A., Cui, Y., Tang, S., Fisher, P. A., & Gaudio, J. E. (2023). Integration of adaptive control and reinforcement learning for real-time control and learning. IEEE Transactions on Automatic Control.

Kim, J. W., Park, B. J., Yoo, H., Oh, T. H., Lee, J. H., & Lee, J. M. (2020). A model-based deep reinforcement learning method applied to finite-horizon optimal control of nonlinear control-affine system. Journal of Process Control, 87, 166-178.

The paper is littered with inconsistencies and half-truths that make it difficult to follow.

A. The paper has serious misunderstandings concerning the relationships among non-linear or affine models and switching. The paper makes claims that mis-represent the following:

1. In control theory, using a switching law is independent of whether the system is non-linear or affine.
2. An affine model can be tuned to be a close approximation to a non-linear model.
3. A well-tuned affine model can be compatible with the underlying MBRL algorithm.

The text around eq. 10-11 is standard control theory: we tune an affine model for a set of operating conditions, and have a switching function that switches to the best-approximation affine model as appropriate.

It is confusing to try to follow the logic of p. 5, starting with "Although using the above naive control-affine model can be convenient, it must trade in the capabilities of the underlying MBRL algorithm."

There are many overblown claims. such as:

  (i) "Classical control tools rely on extensively modeled dynamics that are gain scheduled, linear, and/or true up to parametric uncertainties. An example is prohibitively expensive wind-tunnel modeling for designing flight control systems (Neal et al., 2004; Nichols et al., 1993)."

This is not true. Many modern approaches use nonlinear methods. Your example makes no sense.

  (ii) "MBRL algorithms often use highly nonlinear models (often NNs) that do not have true parameters corresponding to the ground truth dynamics, only optimal from a predictive sense, which makes consolidating MBRL with control theoretic tools challenging."

The following is over 10 years old and covers many topics in (ii):

Wang, X., & Hovakimyan, N. (2012). L1 adaptive controller for nonlinear time-varying reference systems. Systems & Control Letters, 61(4), 455-463.

p.4: "it is necessary to represent the nominal model in the control-affine form."

It is not required to have affine form, even for NNs:

Padhi, R., Unnikrishnan, N., & Balakrishnan, S. N. (2007). Model-following neuro-adaptive control design for non-square, non-affine nonlinear systems. IET Control Theory & Applications, 1(6), 1650-1661.

### Questions
1. What is the extension over:

Annaswamy, A. M., Guha, A., Cui, Y., Tang, S., Fisher, P. A., & Gaudio, J. E. (2023). Integration of adaptive control and reinforcement learning for real-time control and learning. IEEE Transactions on Automatic Control.

2. Please carefully show differences with the following paper. There also seems to be a big overlap with:

Kim, J. W., Park, B. J., Yoo, H., Oh, T. H., Lee, J. H., & Lee, J. M. (2020). A model-based deep reinforcement learning method applied to finite-horizon optimal control of nonlinear control-affine system. Journal of Process Control, 87, 166-178.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an improvement to existing model based RL algorithms where an approximate dynamics model is used in an L1 adaptive control scheme to contribute to the robustness of the algorithms. By relying on an "affinized" a trained nonlinear model using the switching rule, L1 adaptive control can be used in tandem with MBRL algorithms. This method is shown to improve both the sample efficiency and robustness of MBRL algorithms.

### Strengths
1. The statement of contributions is nice for understanding which parts of the proposed work are original and which already exist.
2. There is a nice literature review in the related work and preliminaries sections to introduce L1 adaptive control to people less familiar with it. 
3. The approach was shown to work well on a wide variety of control tasks.

### Weaknesses
1. Without a solid adaptive control background, I found this paper very hard to follow. 
2. Some of the figure captions weren't descriptive enough, more detail would be helpful. 
3. This paper seemed to be very heavy on math in place it made it hard to follow.

### Questions
Why L1 adaptive control? What were some of the other options from the adaptive control community considered in this work?

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
The paper proposes robust control method combining existing MBRL algorithms and $\mathcal{L}_1$ adaptive control method. MBRL algorithm provides the reference control and $\mathcal{L}_1$ adaptive control is applied to reject the uncertainty.
 
The difficulty in combining MBRL and adpative control method is how to represent the model. The authors have chosen control-affine dynamics using Taylor approximation and switching law, and it seems to work well.

### Strengths
- The idea to use MBRL as reference control and then applying $\mathcal{L}_1$ adaptive control seems to straightforward and clear. The presentation is clear and well-organized.

- The method is applicable to wide range of MBRL algorithms.

- The experimental results show the effectiveness of the proposed method.

### Weaknesses
 - Using output of the RL algorithm as reference input for $\mathcal{L}_1$ adaptive control has been explored in Cheng et al., therefore the proposed method does not seem to be novel.

- Since the suggested method is an augmentation framework, the performnace of the method highly depends on existing MBRL algorithms. 

- Since the true model is assumed to be deterministic, it highly restricts the range of application.

- Comparison with existing uncertainty dealing methods seems to insufficient. I would expect several more explanations and experiments comparing with probabilistic models as in Section D.4.

### Questions
- What is the importance of Theorem 1 or what does it have to do with MBRL? What is the difference with the existing stability result in $\mathcal{L}_1$-adaptive control theory?

- In equation (9), how is $\nabla_u \hat{f}_{\theta}(x_t,u)$ implemented?

- What does it mean to skip the update in non-differentiable points? Then should the update is over when it the agorihm meets the non-differntiable point?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose an $\mathcal{L}_1$ adaptive control "add-on" that can be applied to existing model-based RL algorithms in order to improve robustness to model uncertainties. This scheme is agnostic to the choice of model-based RL algorithm; it transforms/filters said algorithm's control outputs before they are input to the dynamical system or simulator. The authors provide some theory behind this approach as well as experimental validation in MuJoCo environments.

### Strengths
- The paper is written very well, which is rarely a given.
- The authors spend an appropriate amount of space on each section of the paper and do not belabor introductory material or time over-explaining things.
- The (meta-)algorithm is a nice idea that can be tested fairly easily.
- Code to replicate experiments was provided, which is rarely a given.

### Weaknesses
Some presentation issues:
- The single-column "wrapped" figures are awkward, especially on pg. 6.
- Tables (esp. numbers) should have larger fonts--shouldn't be below footnote size.
- In Table 1 and Fig. 3, what the bounds/error bars represent isn't stated.
#
- I would have liked to see on-off comparisons for more model-based RL algorithms as in Figure 3 (especially in the main body of the paper), as it's one of the paper's main selling points.
- While I appreciate the installation README, having one of the steps being "go get a MuJoCo license" isn't very user-friendly (not sure why it couldn't have been included?).

### Questions
As a sanity check, how does this perform on linear systems?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
