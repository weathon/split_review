# A New, Physics-Based Continuous-Time Reinforcement Learning Algorithm with Performance Guarantees

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
We introduce a new, physics-based continuous-time reinforcement learning (CT-RL) algorithm for control of affine nonlinear systems, an area that enables a plethora of well-motivated applications. Based on fundamental input/output control mechanisms, our approach uses reference command input (RCI) as probing noise in learning. With known physical dynamics of the environment, and by leveraging on the Kleinman algorithm structure, our RCI-based CT-RL algorithm not only provides theoretical guarantees such as learning convergence, solution optimality, and closed-loop stability, but also well-behaved dynamic system responses with data efficiency during learning. Our results are therefore an advance from the two currently available classes of approaches to CT-RL. The first school of adaptive dynamic programming (ADP) methods features elegant theoretical results stemming from adaptive and optimal control. Yet, they have not been shown effectively synthesizing meaningful controllers. The second school of fitted value iteration (FVI) methods, also the state-of-the-art (SOTA) deep RL (DRL) design, has shown impressive learning solutions, yet theoretical guarantees are still to be developed. We provide several evaluations to demonstrate that our RCI-based design leads to new, SOTA CT-RL results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a new method exclusively for solving LQR problems (restricted to Q-R cost functionals without cross terms) by leveraging input/output insights and the underlying control problem structure. This enables the proposed method to have theoretical foundation which is currently lacking in more general purpose methods including ADP and DeepRL. In several benchmark tasks, the proposed method outperforms or matches existing practice.

### Strengths
The authors specifically studied an important class of control problem, namely the affine nonlinear LQR problem, in continuous time. By leveraging the linear-quadratic property of the underlying problem structure, and utilizing Kleinman's method, the authors arrived at a theoretical guarantee unsurprisingly. The proposed method indeed outperform in tasks where underlying dynamics are known and deterministic.

### Weaknesses
The study of linear-quadratic problems has formed a long list, while the manuscript only mentioned a few general-purpose methods such as ADP and FVI. The weakness of this work hence can be summarized as follows.

1. This work failed to mention other similar works in continuous-time LQR setting where different exploitation of the same linear-quadratic structure (as Kleinman's method) leads to different theoretical guarantees and efficient algorithms. The authors may want to conduct a thorough survey on existing works and compare their approaches with other model-based continuous-time LQR methods. A few examples can be found like:

[1] Jeongho Kim, Jaeuk Shin, and Insoon Yang. Hamilton-jacobi deep q-learning for deterministic continuous-time systems with lipschitz continuous controls. The Journal of Machine Learning Research, 22(1):9363–9396, 2021.

[2] Haoran Wang, Thaleia Zariphopoulou, and Xun Yu Zhou. Reinforcement learning in continuous time and space: A stochastic control approach. The Journal of Machine Learning Research, 21(1): 8145–8178, 2020.

2. It is questionable if the method in this work can be fairly compared to other general purpose RL methods or ADP methods, since the latter typically won't consider the specific underlying structure of the control problem. The authors may want to proceed more carefully when utilizing FVI as the benchmark and perform comparison for tasks like pendulum for which model-based LQR-type algorithm can easily excel.

### Questions
The experiment provided in the work is only restricted to very low-dimensional control problem, i.e., pendulum. Since this work has exploited the underlying linear-quadratic structure to a great extent, it is more worth looking at the capacity and efficiency of the algorithm on high-dimensional tasks, with both state and action space in large dimensions. Otherwise, the contribution is limited.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces physics-based CT-RL algorithm for affine systems using reference command input.  It aims at providing theoretical guarantees while showing good performance.

### Strengths
1. Careful comparisons and evaluations (if the presentations become better, those should become clearer)

Theorem 2.1 could be a potential strength; but I could not quite follow the details here.
To be honest, it was very hard to parse the overall algorithm.
Why for nonlinear systems the policy K is introduced in the algorithm?  The author also mention mu as a policy.
Proposition A.1 is referred at several places but without clear connections.
For nonlinear systems, the results should only be satisfied locally?
I may be missing something here, but I believe improving presentations should largely help clarifying the strength of the theoretical statements.

### Weaknesses
1. From the cost 2, the system must stabilizes on a zero cost point and stays there without control input so that the cost exists: Although there is a comparison to other methods, I honestly think this is a strong assumption for practical purposes that this work claims to target. The requirement that the system must stabilize to a zero-cost point without control input for the cost to be finite is a significant limitation. This implies that the system's natural dynamics must inherently lead to a stable equilibrium at the desired state, which is not generally true for many real-world systems. This assumption severely restricts the applicability of the proposed method, as it cannot handle systems that require continuous control to maintain stability or track a desired trajectory.
2. The presentation is not well structured; perhaps it is better to present a conceptual procedures first with figures, pseudo algorithm etc., and then go into the details.  The authors also use some notations and concepts and describe them later; which make it harder to track; those should be mentioned at the conceptual presentation stage. Also for experimental sections, I guess it is because of page limit, it is a bit hard to parse what is going on (no indent, no new line...). The lack of a clear conceptual overview with figures and pseudo-code makes it difficult to grasp the algorithm's core mechanics. Introducing notations and concepts before explaining them creates confusion and hinders understanding. The experimental section's presentation is also problematic, lacking proper formatting and making it difficult to interpret the results. For instance, the absence of indentation and new lines makes it hard to follow the experimental setup and results.
3. More explanations around A, B (nominal linearization terms that are known) are needed. The paper does not adequately explain the origin and role of the nominal linearization terms A and B. It is unclear how these terms are obtained and what assumptions are made about their accuracy. This lack of clarity makes it difficult to assess the method's robustness to model uncertainties.
4. Table 2 is hard to parse.  Table 4 could be improved to show which case works better for RCI. The tables, particularly Table 2, are poorly formatted and difficult to interpret. Table 4 could be improved by explicitly stating which cases show the benefits of using RCI, making it easier to understand the experimental results.
5. For all of the tables (and some figures) in the appendix, they should have more descriptions in the captions and they could be improved so that it becomes easier to get the ideas. The tables and figures in the appendix lack sufficient descriptions in their captions, hindering the reader's ability to understand the presented information. The figures and tables should be self-contained and easily interpretable without referring back to the main text.

### Questions
1. I don’t get what “Thus, RCI can improve learning of existing CT-RL algorithms” mean from the paragraph.  Can you elaborate on this?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new continuous-time reinforcement learning (CTRL) algorithm for control of affine nonlinear systems. The key idea is to use reference command input (RCI) as probing noise in learning. The simulations show RCI leads to better results than fitted value iteration.

### Strengths
This paper has a good review of the existing ADP methods.

### Weaknesses
1. The methodology introduced in this paper is an extension of the RADP method, with the primary modification being the linearization of the nonlinear system. However, the implications of such linearization are not distinctly outlined, nor is there a clear comparative analysis with the traditional RADP method. The absence of a detailed examination of the linearization's impact raises questions about the method's efficacy and novelty. Specifically, the paper does not address how the linearization affects the approximation of the value function, nor does it discuss the limitations imposed by this approximation, such as potential instability or divergence in regions far from the linearization point. A more rigorous analysis of the error introduced by linearization is needed.

2. The authors suggest that the rationale behind employing the RCI framework is its potential to enhance the PE condition. Nevertheless, the explanation as to why this approach is effective is insufficiently substantiated. Furthermore, the connection between the RCI and the employed linearization technique is ambiguous, resulting in a fragmented logical flow in the methodology's presentation. The paper lacks a clear explanation of how the RCI specifically excites the system's modes to ensure persistent excitation, and how this excitation interacts with the linearized dynamics. A more detailed explanation of the mechanism through which RCI achieves PE and its relationship to the linearized system is needed.

3. The proposed methodology presupposes a comprehensive understanding of system dynamics. However, with known system dynamics, one could conduct policy iteration directly using a "differential" formulation as opposed to the "integral" formulation, which seems unnecessarily convoluted. For instance, a comparison could be made with the "Relaxed Actor-Critic" method detailed in [1], which offers a solution to the HJB equation through policy iteration in the context of fully understood system dynamics. The paper does not explore the potential benefits of using differential forms of the Bellman equation, which can offer more direct and stable solutions when system dynamics are known. The authors should justify why an integral approach is preferred over a differential one given their assumption of known system dynamics.

4. Unfortunately, the link provided for the open-source code corresponding to the paper's methodology is inaccessible, which hinders peer verification and replicability of the results presented. This lack of accessibility prevents the community from validating the claims made in the paper and reproducing the experimental results, which is a crucial aspect of scientific research.

5. The proof presented for Theorem 2.1 is unconvincing. It employs the Closed-Loop Stability attribute of Kleinman’s Algorithm, but the narrative fails to clarify why this particular inference is applicable to nonlinear systems as well. The proof lacks a thorough explanation, making the applicability of Kleinman’s Algorithm to nonlinear systems questionable. The authors need to provide a more detailed and rigorous proof that explicitly addresses the challenges of applying a linear stability result to a nonlinear system, and clarify the conditions under which the stability of the linearized system implies the stability of the original nonlinear system.

### Questions
Why use the proposed method using linearization? What is the intuition behind it?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
