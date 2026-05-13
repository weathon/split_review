# Rethinking Actor-Critic: Successive Actors for Critic Maximization

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Value-based actor-critic approaches have been widely employed for continuous and large discrete action space reinforcement learning tasks. Traditionally, an actor-network is trained to find the action that maximizes the critic (action-value function) with gradient ascent.
We identify that often an actor fails to maximize the critic because (i) certain tasks have challenging action-value landscapes with several local optima, and (ii) the critic landscape varies non-stationarily over training. This inability to find the optimal action often leads to sample-inefficient training and suboptimal convergence. To address the challenge of better maximization of the critic's landscape, we present a novel reformulation of the actor by employing a sequence of sub-actors with increasingly tractable action-value landscapes.
In large discrete and continuous action space tasks, we demonstrate that our approach finds actions that better maximize the action-value function than conventional actor-network approaches, enabling better performance. [https://sites.google.com/view/complexaction](https://sites.google.com/view/complexaction)

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper claims that actor often finds actions that cannot maximize the critic and this leads to sample inefficient training and suboptimal convergence. The paper proposes an algorithm that roughly works as follows. First, in addition to a primary critic, another K actors and critics are initialized, and they are queried in order: an actor’s input depends on all previous actors’ outputs; second, the action with highest primary critic value is executed; third, K updates applied to the K actor-critic pairs; last, the primary critic is updated by its own maximum action. Experiments are conducted to verify their claims.

### Strengths
1. The presentation is reasonably clear. 

2. The proposed problem regarding the actor often cannot align well with the maximum action worths studying, it looks interesting to me.

### Weaknesses
The critical claims are not well-supported: 1) why the proposed method can help find maximum action; 2) the connection between finding maximum action and improved sample efficiency; 3) the actual benefit of the proposed algorithm, is it from finding the maximum, or ensemble, or exploration? 4) experiments are not well-designed; 4) highly related works are missing. 

To support the claim of the paper, the following experiments need to be done: 
1. add experiments to verify the proposed method does find action with a higher action value; current version directly jumps into sample efficiency, leaving the critical claim unverified; 
2. The connection between finding the maximum action and improved sample efficiency is not supported, please justify;  would it introduce overestimation that hurts learning? 
3. please add ensemble-based exploration method for comparison, as it is known that ensemble would provide benefits of enhancing sample efficiency. Another purpose of adding ensemble is to verify if the main benefit really comes from finding the maximum action or from exploration, If it is the letter, then the pitch of the paper should be modified and another set of baselines aiming at better exploration should be compared. 
4. Any comments on the convergence of such an algorithm? I am a bit concerned that the update of an actor depends on all previous actors output could result in high non-stationarity. This would make the training difficult. 
5. The proposed algorithm seems to have much higher computation cost, which weaken the practical utility. 

Potential flaws of the experiment design. 
1. In the algorithm, it seems at each time step, the algorithm update both policy and critic parameters K times, do the authors do the same thing for baselines? 
2. Please add baselines as suggested by below missing related works. 

There are several missing references that are highly relevant: 

1. A model reference adaptive search method for global optimization by Jiaqiao et al.
2.  Q-learning for continuous actions with cross-entropy guided policies by Riley et al.
3.  Greedy Actor-Critic: A New Conditional Cross-Entropy Method for Policy Improvement by Samuel et al
4. CEM-RL: Combining evolutionary and gradient-based methods for policy search by Alois et al. 
5. Wire fitting algorithm by Baird et al. the title is likely RL with high-dimensional continuous actions. 

Among these, 2,3,4 are highly relevant and should be also compared. Please explain what the differences are between your work and those existing ones and comment on the significance of such difference. I consider this one of the critical weaknesses of this work.

### Questions
see above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a continuous actor value optimization method to address the issue that traditional single actor-critic algorithms are prone to failing into local optima, in order to improve sampling efficiency and final performance in large discrete action spaces and continuous action spaces. The effectiveness of the proposed method is ultimately demonstrated through experiments.

### Strengths
This paper presents a novel reformulation of the actor. I think that addressing the challenge of better maximization value function by "pruning" an optimization landscape is an interesting work.

### Weaknesses
1) The writing expression is not sufficiently clear and the logic is confusing, especially in Introduction and Related Work sections. It is difficult to understand the structure of the article. The contribution is not clear, and it is not suitable to use a large space to introduce the experimental environment.
2) This paper lacks many vital technical explanations, including an introduction to deep-set and FiLM layer, the motivation behind their usage, and analysis of their effects. For example, the paper does not clarify why a DeepSet architecture is suitable for summarizing past actions, or how the FiLM layer conditions the actor's policy. The lack of these details makes it difficult to assess the validity of the proposed approach. Furthermore, the paper does not analyze the impact of different design choices for these components, such as using an LSTM or a Transformer for action summarization instead of DeepSet, or alternative conditioning methods for the actor.
3) The experimental results are not sufficiently reliable. The baselines are outdated. There is no mention of hyperparameter sensitivity or setting experiments. Furthermore, the paper does not provide sufficient detail on the experimental setup, such as the specific hyperparameters used for each baseline, the range of values explored during hyperparameter tuning, and the criteria used for selecting the final hyperparameters. This lack of detail makes it difficult to reproduce the results and assess the validity of the experimental comparisons. The choice of only 3 seeds in some experiments, such as Figure 4, raises concerns about the statistical significance of the results. Additionally, the modification of the experimental setup may not be fair, as other baselines may not have been designed specifically to address the problem presented in this paper. The experiment in the Appendix only has the Easy environments, what about the other Hard environments?

### Questions
1) In Relate Work, the introduction of prior work is outdated. Please supplement it with the latest relevant work.
2) The work presented in this paper seems to fall under the domain of ensemble methods. It may be necessary to supplement it with relevant work and introduce ensemble-based value optimization algorithms as additional baselines.
3) In Algorithm 1, the "state s" in lines 8 and 10 need clarification.
4) Does the proposed method in this paper suffer from the problem of action values overestimation?
5) Why only select 3 seeds in some experiments, such as Figure 4?
6) Is the modification of the experimental setup fair? Other baselines may not have been designed specifically to address the problem presented in this paper.
7) The experiment in the Appendix only has the Easy environments, what about the other Hard environments?
8) Due to the utilization of ensemble methods, I am concerned about the computational efficiency of the algorithm. Please supplement the experiments or provide an analysis.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied an interesting problem that the training of the policy network often cannot effectively optimize the learned value function. This could lead to sub-optimal learning performance and ineffective exploration. To address this issue, this paper proposed a new ensemble technique that utilizes a sequence of separately trained actor-critic pairs to gradually refine/restrict the action space being considered. The newly proposed algorithm has been experimented on multiple benchmark problems with both discrete and continuous action spaces. The performance results showed that the new algorithm can achieve better overall performance across all the benchmark problems.

### Strengths
It is a well-known problem in the literature that the trained policy network in an actor-critic algorithm may often fail to optimize the learned value function. This inconsistency could potentially weaken the performance of the learning process. This paper developed an interesting new algorithm to address this issue. The effectiveness of the new algorithm is also evidenced by promising experiment results.

### Weaknesses
While the idea of using a series of successive actor-critic pairs to gradually refine/restrict the action space is interesting, however, this also means that the action selection decision from the policy network may be highly sensitive to the minor nuances of the learned critic. This often introduces bias to the learning process, resulting in degraded learning stability and restricted exploration. Hence, the downside of using multiple successive actor-critic pairs should be extensively examined in this paper. It is important to know why successively restricting the action space based on the trained critic will not affect the learning stability with a solid theoretical foundation. It is also important to know why this actually helps to improve the effectiveness of exploration, rather than restricting exploration, as claimed by the authors.

Since the newly proposed algorithm uses an ensemble of actor-critic pairs, it is related to ensemble actor-critic algorithms. Hence, in section 2, it seems necessary for the authors to review existing ensemble actor-critic methods and clearly highlight the key novelty of the new algorithm, compared to existing ensemble algorithms. Furthermore, the experiment study should include more state-of-the-art ensemble baselines, in order to clearly show the advantages of the new algorithm over existing ensemble algorithms.

Some parts of the new algorithm design seem to lack technical clarity. In particular, it is not clear to me how deep-set is used to produce Z as a concatenation of previously selected actions and state. It is also unclear how FiLM is used to enable a policy to choose its actions that are conditional on Z. Meanwhile, The motivations and rationales of using deep-set and FiLM should be clearly explained and strongly justified.

The authors stated that their new ensemble technique can be applied to many different actor-critic algorithms. Given this statement, it is not clear why they focus primarily on applying their new technique to TD3 alone. To demonstrate the wide applicability of the new technique, the authors should study its possible application to other algorithms, such as SAC.

I don't quite understand some mathematical formulas presented in this paper. For example, I don't know how to find the optimal action a' based on the primary critic, as part of the final training objective, which is further conditional on $\Pi$. The formula for policy gradient in the final training objective also misses some brackets such as }. Meanwhile, it remains questionable why the policy gradient formula is valid, i.e. what kind of gradient is being calculated and why the gradient allows the trained policy network to maximize the expected return. I think more detailed and thorough theoretical analysis is necessary to justify the validity and effectiveness of the proposed training objective.

Some statements in this paper are not easy to understand. For example, what does it mean by "navigate the action-value landscape more proficiently" on page 1? What does it mean by "distribute the optimization load over to the critic" on page 5? What does it mean by "slower than the original inefficiencies of the actor" on page 5? What does it mean precisely for the optimization landscape of Q to be more tractable? If the number of local optima of Q's landscape can be reduced, to which extent can such reduction be actually achieved?

The English presentation of this paper may need to be improved. The authors are highly recommended to conduct more rounds of proof-reading of their paper to substantially improve the presentation clarity and quality.

### Questions
Why will successively restricting the action space based on the trained critic not affect the learning stability and improve the exploration effectiveness?

Why is the new policy gradient formula valid, i.e. what kind of gradient is being calculated and why the gradient allows the trained policy network to maximize the expected return?

Please refer to the previous section regarding questions on the clarity of some statements.

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
The paper presents a novel reformulation of the actor by employing a sequence of sub-actors, which solves the problem of non-convex and high-dimensional, and non-stationary during action-value optimization landscape training. The logical assumption stated by the authors is an ensemble of successive actor-critic modules can collectively navigate the action-value landscape more proficiently than a single, monolithic actor. The authors demonstrate improvement over continuous and large discrete action space reinforcement learning tasks.

### Strengths
The paper is well written and well structured. The idea of successive actor modules for "pruning" all actions with Q-values lower than the baseline is interesting and (to the best of my knowledge) novel. The experimental setup (especially on large discrete action space RL tasks and more discontinuous variants of continuous RL tasks) appears rigorous.

### Weaknesses
1.The paper's central assumption feels reasonable, and the experiment seems to confirm it. But there is no theoretical proof.
2.The key parts of the successive actor-critic modules adopt both ‘deep-set’ and ‘FiLM’ methods, but lack a description of potential advantages and an explanation of alternative methods.
3.From the structure of the proposed method, it can fluidly integrated into other widely adopted RL algorithms. In the experiment, TD3 was selected as the baseline. Is it possible to add other RL methods to the ablation study to illustrate the applicability of the method.
4.FIG. 1 is a diagram illustrating the core ideas of the paper. Can 'tractable' be explained from the perspective of real data in the experimental part? FIG. 4 seems intended to explain, but is insufficient.

### Questions
1.Algorithm 1, line 17 has a prominent '{' symbol. What is the difference between $(s_t|A)$ and $(s_t,A)$ in formulas $a=\pi_{i}(s_t|A)$ and $\pi_{\phi_i}(s_t,A)$.
2.Legend should be added to FIG. 7, although it is related to FIG. 3.
3.Although there is not enough time to go through the source code carefully, it is recommended that the method abbreviation be consistent in the code(called FLAIR) and the paper(called SAVO).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
