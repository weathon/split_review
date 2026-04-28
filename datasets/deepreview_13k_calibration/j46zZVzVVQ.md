# Customizing Reinforcement Learning Agent with Multi-Objective Preference Control

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Practical reinforcement learning (RL) usually requires agents to be optimized for multiple potentially conflicting criteria, e.g. speed vs. safety. 
Although Multi-Objective RL (MORL) algorithms have been studied in previous works, their trained agents often lack precise controllability of the delicate trade-off among multiple objectives. Hence, the resulting agent is not versatile in aligning with customized requests from different users. 
To bridge the gap, we develop ``Preference control (PC) RL'', which aims to train a meta-policy that takes user preference as input controlling the generation of a trajectory on the Pareto frontier adhering to the preference. To this end, we train a preference-conditioned meta-policy by our proposed preference-regularized MORL algorithm. The achieved meta-policy performs as a multi-objective optimizer that can produce user-desired solutions on the Pareto frontier. The proposed algorithm is analyzed and its convergence and controllability are theoretically justified. 
Experiments from discrete toy examples to higher-dimension robotic control tasks and experiments with more than two objectives are conducted to show its performance.  In these experiments, PCRL-trained policies show significantly better controllability than existing approaches and can generate Pareto optimal solutions with better diversity and utilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new multi-objective algorithm, PreCo, which aligns with preferences. Additionally, this work introduces a new similarity function as a regularizer for policy updates. Empirically, it demonstrates improved hypervolume (HV) scores across multiple multi-objective environments, showing the effectiveness of preference alignment.

### Strengths
+  This work provides comprehensive theoretical analysis for the convergence of Pareto stationary points.

+  Extensive experiments are conducted in both discrete and continuous state-action environments.

### Weaknesses
 - There is a lack of a formal definition for the policy-level gradient, $\nabla_{\pi_p}v^{\pi_p}$, especially in continuous state-action spaces. Additionally, a major concern is the efficiency of computing the policy-level gradient in continuous state-action spaces. Recent RL works often use more expressive models as the policy network, such as diffusion models [1, 2] or normalizing flows [3]. It remains unclear how to compute the policy-level gradient for such generative models.

- The training time is not reported, which makes the claim of computational efficiency for solving the min-norm problem (Equation 6) in Section 3 unconvincing..

- The evaluation metrics are limited. The experiments mainly focus on hypervolume (HV) and cosine similarity between preferences and value functions. The similarity metric is designed to demonstrate the effectiveness of the proposed similarity function $\mathcal{\Psi}(\cdot, \cdot)$. Consequently, HV remains the sole evaluation metric for assessing the quality of the Pareto front. However, HV may increase due to improvement in only one of the objectives. In Figures 5(d) and 6(d), the authors provide visualizations of the Pareto front, which show only marginal improvements over EPO. Several other evaluation metrics could be used to assess the quality of results: Overall Non-dominated Vector Generation Ratio [4], Error Ratio [4], and Sparsity [5].

- Comparisons could be made more extensive. There exists a state-of-the-art preference-driven multi-objective RL algorithm [5].

- The authors may also wish to compare their approach with another baseline that incorporates preferences as input [6].

- Additionally, this work references SDMGrad [7] and aims to address a similar min-norm problem (Equation 6 in this work, Equation 8 in SDMGrad), yet experimental results from SDMGrad are missing. It would be valuable to observe the effectiveness of the similarity function based on a comparison between this work and SDMGrad.

### Questions
- Are there other similarity functions that can be used in Equation (6), or what properties should these similarity functions have?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents Multi-objective Preference Control RL, an approach for multi-objective RL, which trains a meta-policy that takes user preference as input controlling the generated trajectories within the preference region on the Pareto frontier. They show that their meta-policy performs as
a multi-objective optimizer that can directly generate user-desired Pareto solutions. They theoretically analyze the convergence and controllability of the MORL objectives, and perform experiments on challenging robotics tasks.

### Strengths
The approach for employing preference control for MORL, by controlling generates trajectories is interesting and novel. 

The paper performs detailed theoretical analysis and discusses convergence and controllability of the learnt policies, which is impressive.

The authors perform experiments and show impressive performance on challenging robotics tasks.

### Weaknesses
The paper method would benefit by adding a detailed algorithm explaining the method. The paper could benefit from the addition of pseudocode for the key steps of preference-conditioned policy training, and additional details on how the preference regularization is implemented algorithmically. 

Extensive experimental and implementation details are missing, which would make the results hard to reproduce. Addition of information on hyperparameters, network architectures, training procedures, or environment specifications needed to reproduce the results will greatly help increase paper reproducibility.

I am currently recommending a weak reject, but will accordingly update the score based on the discussion and ratings by other reviewers.

### Questions
None.

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
4

### Summary
The paper provides a method for optimizing multi-objective RL problems such that the obtained policy lies on the Pareto frontier. Instead of relying on scalarization of the objective, like standard MORL methods do, the proposed method instead optimized for a similarity metric between the preference vector and the value function. The paper provides a theoretical convergence analysis and compares with a number of adequate baselines on multiple environments.

### Strengths
The paper provides a novel and reasonable approach for finding pareto-optimal policies. This is non-trivial, most existing methods rely on scalarization and fall short, or require costly and complex constrained optimization methods. This paper instead provides a simpler updating scheme applicable in both discrete and continuous action-space MDPs. Good, adequate baseline comparison.

### Weaknesses
Clarity: Method section is hard to follow. In order to understand fully why the method converges to pareto-optimal policies, I'd appreciate if the authors could provide additional intuition (one or two sentences) for step 3 in section 3.2. Specifically, the connection between minimizing the norm of d* and achieving Pareto optimality is not immediately clear. It would be beneficial to elaborate on why driving this norm to zero implies that the policy is non-dominated. The current explanation lacks a clear link between the optimization objective and the desired outcome of Pareto optimality.

Experiments & reproducibility: While the paper provides a number of experiments, it does not seem like results were averaged across multiple random seeds, maybe I missed it? This is crucial though, because RL methods depend strongly on the seed. I strongly feel like the authors should report statistics across multiple seeds, otherwise it is very hard to say if the results are reproducible and significant. Reporting only the mean performance without standard deviations or confidence intervals makes it difficult to assess the robustness of the proposed method. The lack of this information significantly weakens the experimental validation.

Meta-RL: It is not clear to me why the authors learn a preference conditioned meta policy. Is this a requirement of the learning algorithm or is this solely done to have access to multiple policies at inference time? Does the method rely on training with uniformly sampled preference vectors or can it also optimize and find the pareto-optimal policy for a single preference, without uniformly sampling from the preference space during training at random? The paper does not clearly explain whether the preference conditioning is integral to the algorithm's convergence or merely a design choice for practical purposes. This distinction is important for understanding the core contribution of the method.

### Questions
See the points under weaknesses. I think this is a good approach but also believe that the current version of the manuscript has some limitations that need to accounted for (or the clarity needs to improved) to justify a higher score.

### Soundness
3

### Presentation
2

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
This paper studies multi-objective reinforcement learning (MORL) algorithms that can be controlled to produce policies with different trade-offs between conflicting objectives. In particular, the paper tackles the case in which the policy is conditioned on a preference vector $p$ that controls the desired trade-offs. The paper introduces a novel method, named Preference Control RL (PreCo), which learns a policy that encourages the preference vector $p$ to have high similarity with the value vector of the corresponding policy. Experiments were performed in discrete toy domains as well as in multi-objective versions of the Mujoco benchmark to assess the properties of the method proposed.

### Strengths
- The problem of designing MORL algorithms with better controllability is of high relevance in the RL community, and the idea of using a similarity function to achieve that is novel to the best of my knowledge.
- The experiments consider many different MORL problems with diverse characteristics and complexities.

### Weaknesses
 - The paper has a significant problem of clarity, to the point of being very difficult to follow what is being proposed in terms of theory, mathematical notation, and algorithms. I discuss this in my Questions below.
- The experiments do not provide confidence intervals or information regarding the number of random seeds used to compute the metrics. Hence, it is not possible to assess whether the results are not due by chance.
- The paper does not compare the proposed method with state-of-the-art MORL algorithms such as Envelope Q-learning, GPI-LS, or CAPQL. These methods have demonstrated strong performance in various multi-objective tasks, and a comparison is necessary to validate the claims of the proposed method.
- The results for the LS baseline in the experiments are unexpected. In Figure 8, for instance, the LS method fails to reach any of the targets, which is not consistent with the performance of state-of-the-art LS MORL methods in the Reacher environment. This suggests potential issues with the implementation or the underlying RL algorithm used for the LS baseline.
- The claim that the proposed method achieves better controllability because it optimizes for cosine similarity between preferences and values is not well-justified. Other state-of-the-art MORL algorithms, such as CAPQL, are also able to learn continuous and convex Pareto fronts, and it is not clear why optimizing for cosine similarity is a superior measure of controllability.
- Based on Figures 5 and 6, the proposed technique does not show a clear advantage over LS in terms of hypervolume, which is a standard metric for evaluating the quality of the Pareto front. This raises questions about the practical benefits of the proposed method.

### Questions
Below, I have some questions and constructive feedback to the authors:

1) “... Alegre et al. (2023) require learning multiple models to identify the Pareto front” 
This is incorrect. Alegre et al. (2023) introduce a version of their method that uses a single policy conditioned on the preferences $w$, $\pi(s|w)$. This is also done in many state-of-the-art MORL algorithms. 

2) The authors claim to learn a “meta-policy”. However, I do not think “meta-policy” is the appropriate term since the policy learned outputs actions as defined in the original action space of the MDP. In RL, meta-policies are policies that control a standard RL policy by learning in the space of meta-actions that are different than the regular actions.

3) In Figure 1, the PFs are “convex” instead of “concave”. That is, linear scalarization is only able to reach points in the convex part of the PF. The paper is confusing both terms.

4) The idea of training a policy conditioned on agent preferences is well-studied and applied in the MORL literature. The authors are proposing a different representation of the preferences. However, the paper does not discuss that previous MORL algorithms also can control MORL policies via a vector representation.

5) “we sample $p\in\mathcal{P}$ uniformly”. What is the domain of $p$? How do you sample it uniformly from this space?

6) How is the value of $\lambda$ selected in Equations 6 and 7?

7) What does it mean to solve the min-norm problem in the third step at “policy level” vs. “parameter level”? This is not clear.

8) In Definition 4.1, the preferences $p$ are vectors such that their elements sum to 1. However, $v$ does not have this constraint and can have very different magnitudes in its elements. Hence, if the maximum element of $v$ has a value of $10$, this value could always be selected in the max in Eq. 8, and the preference vector would be pushed towards $v$. Is this correct?

9) “$\Pi_{W}$ means the projection to the set of convex coefficients.” It is not clear what does this mean. Please provide a more detailed explanation. What are the coefficients? How is this projection computed?

10) Algorithm 1 and its explanation are very difficult to follow. What is the data collected in line 230? What are the variables $\zeta$? 

11) Equations 9 and 10 require some intuitive explanation. It is not clear how $G$ is computed during the RL learning agent training. For instance, the expected value in Eq. 9 is w.r.t what distribution?

12) Regarding Remark 4.1, how is the value of $\lambda$ increased?

13) In Table 1, how many random seeds were used to compute these metrics? The authors should also provide confidence intervals or dispersions metrics. It is not possible to infer whether the results are due to chance.

14) In Figure 4, why did linear scalarization only achieve a single point? This is very strange since previous MORL algorithms based on linear scalarization have been employed in this problem and have been able to identify many points in the PF.

15) The claim that LS agents are uncontrollable by $p$ is not true given that many previous works have proposed MORL agents that generate different Pareto-optimal solutions conditioned on a preference vector $w$.

16) Based on the results from Figures 5 and 6, and given that no confidence intervals were provided, it is not possible to infer that PreCo results in better Hypervolume than the competitors.

17) The paper has a considerable number of grammar issues. I suggest the authors to carefully review the paper.

### Soundness
2

### Presentation
2

### Contribution
2
