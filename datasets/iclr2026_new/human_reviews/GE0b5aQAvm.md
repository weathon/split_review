## Human Reviewer 1

### Summary
This paper studies the suboptimality of nonlinear and ensemble policies in continuous control problems. The authors formulate their analysis in the context of linear systems with quadratic costs and compare the performance of nonlinear neural policies and ensembles of neural policies against linear policies and linear ensembles. They define a nonlinearity measure quantifying the deviation of a function from being affine and show that, for linear-quadratic systems, any nonlinear (or non-affine) policy must be suboptimal relative to the optimal linear policy. Theorem 1 and Theorem 2 establish that nonlinear policies cannot be globally optimal, and Theorem 3 extends this argument to ensemble policies, suggesting that non-convex mixtures of policies are also suboptimal compared to convex-mixing policy ensembles. Empirical evaluations are conducted on synthetic linear control systems, comparing the performance of linear, nonlinear, and ensemble policies. The results show that neural policy ensembles perform worse than linear policies and ensembles.

### Strengths
- The paper tackles a clear and well-posed theoretical question: under what conditions are neural or nonlinear ensembles suboptimal compared to linear policies? This is question, I believe, is of theoretical interest.
- The mathematical results are formally presented with explicit assumptions and definitions (e.g., the "nonlinearity measure" and the LQR cosntraints). The formalism appears internally consistent and logically valid given the assumptions.
- The paper attempts to connect classical control theory insights (LQR optimality) with modern neural network and ensemble formulations, a potentially valuable contribution.

### Weaknesses
**Presentation**:

- I found the paper extremely difficult to parse, both linguistically and conceptually. The writing is often ambiguous, and key terms are not defined well. For example, the opening statement of the abstract ("neural policy ensembles are sub-optimal with respect to linear policy ensembles") is already unclear and leaves the reader guessing what kind of optimality this is referring to. 
- The central theoretical claim almost seems self-referential given the assumptions. Since the problem setup is fully linear with quadratic costs, and the class of linear policies already contains the global optimum, it follows by construction that any non-linear function cannot be better. If I understood correctly, this result is highly unsurprising and, arguably, trivial within the stated framework of linear problems with quadratic costs. 
- The authors seem to assume that neural policies are nonlinear by construction and therefore suboptimal. However, this neglects the fact that, by the universal approximation theorem, a neural network with ReLU activations can represent a linear function exactly. In other words, a neural policy can approximate the optimal linear controller arbitrarily well. The suboptimality is in my view a statement about nonlinear functions in general, not necessarily about neural policies.
- In the treatment of ensembles, the authors reference, for example, Burke et al. for non-convex mixing with neural networks, but these works consider state-dependent mixtures. In the author's notation, the weights $w_i$ seem to be static rather than state-dependent. As before, the authors exclude the probability simples from the support of non-convex mixing by construction.

### Questions
- What motivates the focus on linear dynamics and quadratic costs for the theoretical exposition? It seems clear that LQRs solve these optimally. 
- In Theorem 3, how are mixture weights $w_i$ defined as statis scalars or as state-dependent functions? The notation suggests static weights, but the text refers to neural mixing networks.
- How does this result translate to systems that are not linear?

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper presents a theoretical study that argues that non-linear neural policy ensembles are sub-optimal and less stable compared to linear policy ensembles in Linear Quadratic Systems in optimal control. It also presents a theoretical result that shows non-convex policy mixing is sup-optimal to convex mixing of policies. The theoretical results are verified in a control environments which demonstrate that even well-tuned neural ensembles can underperform by 2 orders of magnitude compared to equivalent linear ensembles in Linear Quadratic Systems.  


**Recommendation:**\
The content of this paper falls quite far outside my area of expertise, as I am an expert in neural ensembles in deep reinforcement learning, not in control systems. However, from my perspective, I recommend to reject this paper, as it seems to lack in the following areas: overly general claims and statements, and a general lack of clarity.

### Strengths
- The question of whether neural policy ensembles exhibit the same benefits as previously found for ensemble classifiers is very relevant. 
- The theoretical results are interesting.

### Weaknesses
- The paper overclaims its contributions. The abstract and introduction have no mention of the assumptions made in both the theoretical and empirical studies. 
	- For example, the abstract states: _"We develop a theoretical framework to formally prove that (non-linear) neural policy ensembles are sub-optimal with respect to linear policy ensembles."_ However, from different parts of the text I have pieced together that this results only holds for: a Lipschitz continuous transition function, deterministic polices, in a linear quadratic system, and doesn't hold for neural policies in general, but instead for policies with an additional assumption of a minimum level of non-stationarity of each individual ensemble member (neural networks are universal function approximators, so they can also learn linear policies). Furthermore, the result seems to only guarantee the existence of one state for which the non-linear neural ensemble is suboptimal, which might not be encountered by the controller from the given starting state, which would make it irrelevant for its performance.
- The theoretical results are difficult to follow. The theorems are stated rather clinically, and are lacking in clear structure regarding assumptions, how they are proven, and what they imply.

### Questions
- The paper claims that (non-linear) neural policy ensembles are inherently suboptimal compared to the individual policies. How do you square this claim with the studies that show improved performance of policy ensembles compared to single policies in RL (some examples, [1,2,3,4])?
- Line 39: _"In contrast, nonlinear policy ensembles face temporal coupling: the ensemble’s actions affect future states, creating feedback loops that may amplify rather than cancel errors. The temporal dependence breaks the mathematical foundation of ensemble methods."_
	- Which part of the results or experiments in this paper explain or verify this intuition?
- Section 3.3: There seems to be a one-to-one correspondence implied between neural ensembles and non-convex mixing. Why could a neural network not produce a convex mixing function? 


**References:**\
[1] SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning. (Lee et al. 2021)\
[2] Swarm Behavior Cloning. (Nüsslein et al. 2024)\
[3] Why Generalization in RL is Difficult: Epistemic POMDPs and Implicit Partial Observability. (Ghosh et al. 2021)\
[4] How Ensembles of Distilled Policies Improve Generalisation in Reinforcement Learning. (Weltevrede et al. 2025)

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
2

---

## Human Reviewer 3

### Summary
The paper studies the ensembling of policies where each sub-policy is solving a different LQR problem. The authors provide several results that highlight the fact that ensembling of non-linear policies might be sub-optimal and unstable. Specifically, the authors show that given a set of tasks (defined by different reward functions), ensembling non-linear controllers learned on each task is worse than ensembling the best linear controllers for each task, that the resulting ensemble of non-linear controller might be unstable even when each individual controller is stable and that a non-convex averaging of the linear controllers is always worse than the convex averaging of linear controller with the same weight as the weight averaging the reward functions. The authors then provide a set of experiments that illustrate each of their theoretical findings.

### Strengths
The paper might provide interesting theoretical results on ensembling of non-linear policies for LQR problems.

### Weaknesses
- There is a clear mismatch between the claims and the theoretical results. The introduction and related work cite deep RL methods using ensembling of policies (notably the work of Yang et al. 2022) in a completely different way than what the theoretical results consider. Introduction mentions that their theory would explain why ensembling of neural policies is doomed to be sub-optimal because of temporal coupling and non i.i.d setting compared to standard classification but the theoretical results show none of that. Instead all the theory is built around ensembling non-linear policies that are solving distinct control problems and then averaging them with no further learning. However, taking a quick look at the paper of Yang et al. 2022, there are large difference in the setting, as in the latter work every sub-policy is solving the same task, and the ensemble policy is also optimized using what they call an ensemble aware loss. Can the author clarify the relation between their theoretical results and the setting of Yang et al. 2022, or any other deep RL setting using ensembles of neural policies? 

-  Theorem statements, assumptions and proofs lack clarity. In the main theorem, it is not clear how the non-linear policies are obtained. The optimal policy is linear for each LQR sub-problem, but by the assumption in line 140, the neural policies are forced to be non-linear and thus these policies are sub-optimal by design. It is then not surprising then that the ensembling of these policies is also sub-optimal. Studying problems where linear policies are optimal and making the assumption that neural policies cannot be optimal is in my opinion not a setting reflective of practical applications that use neural policies. Moreover, the proof could also gain some clarity: where do equation 21 and 22 come from? What even is $R$ in these equations, do you perhaps mean $R_{\text{ens}}$? Is $\lambda_{\min}$ the smallest eigenvalue? For the proof of Theorem 3, could you please provide a reference to the claim that $K_\lambda$ is optimal? As it does not seem trivial to me from the equations since there doesn't seem to be a linear relation between gain matrices and cost matrices. Thank you.

### Questions
Please see the questions in the weakness section.

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
2