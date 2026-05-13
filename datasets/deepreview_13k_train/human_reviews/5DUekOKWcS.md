# Asynchronous Federated Reinforcement Learning with Policy Gradient Updates: Algorithm Design and Convergence Analysis

- Decision: Accept
- Scores: 6, 5, 5, 6, 8

## Abstract
To improve the efficiency of reinforcement learning (RL), we propose a novel asynchronous federated reinforcement learning (FedRL) framework termed AFedPG, which constructs a global model through collaboration among $N$ agents using policy gradient (PG) updates. To address the challenge of lagged policies in asynchronous settings, we design a delay-adaptive lookahead technique \textit{specifically for FedRL} that can effectively handle heterogeneous arrival times of policy gradients. We analyze the theoretical global convergence bound of AFedPG, and characterize the advantage of the proposed algorithm in terms of both the sample complexity and time complexity. Specifically, our AFedPG method achieves $\mathcal{O}(\frac{{\epsilon}^{-2.5}}{N})$ sample complexity for global convergence at each agent on average. Compared to the single agent setting with $\mathcal{O}(\epsilon^{-2.5})$ sample complexity, it enjoys a linear speedup with respect to the number of agents. Moreover, compared to synchronous FedPG, AFedPG improves the time complexity from $\mathcal{O}(\frac{t_{\max}}{N})$ to $\mathcal{O}({\sum_{i=1}^{N} \frac{1}{t_{i}}})^{-1}$, where $t_{i}$ denotes the time consumption in each iteration at agent $i$, and $t_{\max}$ is the largest one. The latter complexity $\mathcal{O}({\sum_{i=1}^{N} \frac{1}{t_{i}}})^{-1}$ is always smaller than the former one, and this improvement becomes significant in large-scale federated settings with heterogeneous computing powers ($t_{\max}\gg t_{\min}$). Finally, we empirically verify the improved performance of AFedPG in four widely-used MuJoCo environments with varying numbers of agents. We also demonstrate the advantages of AFedPG in various computing heterogeneity scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to enhance the efficiency of federated reinforcement learning (FedRL) by introducing an asynchronous framework, AFedPG, which leverages policy gradient (PG) updates from multiple agents without requiring synchronized updates. This approach is designed to address issues related to delayed updates and computational heterogeneity, which are common challenges in federated setups, especially with varying agent speeds and capacities.

### Strengths
Contributions claimed in the paper include,

--Proposes a new asynchronous FedRL algorithm (AFedPG) tailored to policy gradient updates, using a delay-adaptive lookahead technique to manage lagging updates in asynchronous settings.

-- Provides theoretical convergence guarantees, including global and first-order stationary point convergence, for the asynchronous federated policy-based RL.

-- Achieves a linear speedup in sample complexity with an increasing number of agents, reducing the per-agent complexity from $O(\epsilon^{-2.5})$ to $O(\epsilon^{-2.5}/N)$. (However, the proof is unclear and it is hard to see how the authors can avoid a dependence on the delay in the sample complexity.)

  -- Improves time complexity over synchronous methods by reducing the dependency on the slowest agent’s computational time, with gains highlighted in scenarios of high computational heterogeneity.

-- Empirically validates AFedPG's performance in various MuJoCo environments, demonstrating faster convergence (time-wise) over synchronous FedPG and other baselines.

### Weaknesses
In general, the paper is not clearly written. I don't see how the authors were able to avoid a dependence on the delay in their sample complexity. Their current derivations for bounding the error term (from the delay) have many typos and are hard to follow. Specific concerns/questions of the paper include:

-- Step 4 in Algorithm 2 is confusing. Where does the local agent get $d_{k-1}$ from? Did the authors mean $d_{k-\delta_k}$ instead? If the authors meant $d_{k-1}$, the current algorithm descriptions do not mention how $d_{k-1}$ can be made available to agent $i$.

-- A major component of the proof is bounding the error term $e_k := d_{k-\delta_k} - \nabla J(\theta_k)$, which arises from the delay. Equation (30) in the appendix provides a derivation of how $e_k$ can be expressed (and subsequently bounded). However, there seems to be serious typos in equation (30). For instance, in the first line, I am not sure why a term $d_{\delta_{k-1}}$ appears, when $e_k$ is actually $d_{k-\delta_k} - \nabla J(\theta_k)$. This makes it difficult to follow the argument in this derivation, and there is also no explanation of the derivation, which might have made it easier to follow the argument flow. Given that this is a particularly important term to bound to derive either first-order or global convergence rates, the authors should make an effort to clarify and explain these derivations.
 
-- The current convergence bound seems to have no dependence on the delay in the network, which is $N$ in the worst-case (e.g. assuming cyclic update). This is somewhat confusing to me; intuitively, even with a delay-adaptive step size for the $\theta$ update, there should be some price to pay for a cyclic delay structure. My current understanding is that perhaps the authors were able to bypass the dependence on the delay by their handling of the gradient-bias term $e_k$ (caused by the delay). However, given that the current derivation of bounding $e_k$ is highly unclear (see my earlier point), it is not clear to me whether the result as currently stated actually holds. If it holds, the authors should make it a lot clearer how and why they are able to avoid the dependence on the delay, as this is a key part of their contribution. 

-- The definition of the global time is unclear. The authors should make it more precise, and have a formal statement and proof of their current stated bound on the global time being $O(\frac{\bar{t}\epsilon^{-2.5}}{N})$, where $\bar{t} = \frac{1}{\sum_{i=1}^N \frac{1}{t_i}}$. 

--On a related note, the definition of $t_i$ seems a little unclear to me, given that at different iterations, agent $i$ might require varying amounts of time (i.e. there shouldn't be a single time complexity $t_i$ for each agent $i$). The authors should make their definition of what they mean by $t_i$ more precise.

### Questions
See my questions from the previous section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an asynchronous federated reinforcement learning framework. Then it introduces a delay-adaptive lookahead technique and employs normalized updates to integrate policy gradients to deal with the challenges brought by the asynchrony. Furthermore, the paper provides the theoretical global convergence bound. The experiments verify the improved performance of the proposed algorithm.

### Strengths
1. Convergence results are provided. 
2. Asynchronous federated reinforcement learning framework is proposed.

### Weaknesses
1. This paper is not built on a federated framework. FedRL is designed to address heterogeneous environments and allow local agents to perform multiple iterations [1,2]. However, these are not considered in this paper.

2. This work lack necessary comparisons with current works. Actor-critic is a policy-based approach. This paper needs careful comparisons in details with [3] since both emphasize the asynchrony, not mentioned in Introduction briefly.

3. Technical contributions are limited. Authors claimed that even if all agents have an identical environment, each agent collects samples according to different policies because of the delay. This dynamic nature makes both the problem itself and the theoretical analysis challenging. However, this is somehow solved by [3]. The challenges brought by the features of Fed RL are not considered in this paper.

### Questions
4. Why does Proof of theorems lack the index of agent i? Since the server does not aggregate gradients or parameters from agents periodically, Fed RL is not applicable in this paper. Besides, it is just similar to [3]. Notations also make confusing. 

5. What’s the technical contributions beyond existing FedRL? Technical differences of AFedPG compared to FedPG seems limited.

6. Authors first get the results of global convergence, then FOSP results. Why FOSP results are placed first in main text?

### Soundness
3

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
This work investigates federated reinforcement learning with asynchronous synchronizations to improve the time complexity. They introduce the asynchronous federated policy gradient (AFedPG), which tackles lagged policies using a delay-adaptive lookahead. In addition, they present a sample complexity analysis of the algorithm, demonstrating a linear speedup compared to the single-agent scenario.

### Strengths
1. The work provides asynchronous synchronization updates tailored for federated RL.
2. The work presents a tight sample complexity analysis of the proposed algorithm, demonstrating a linear speedup that aligns with the single-agent state-of-the-art.

### Weaknesses
1. The application of asynchronous updates from federated learning to federated policy gradients appears to be incremental, especially since much of the supervised federated learning literature has examined how to manage lagged models, while existing federated reinforcement learning research focuses on addressing the dynamic nature of reinforcement learning in federated settings.
2. It appears that a momentum method was introduced for federated policy gradients in heterogeneous environments to handle online sample collections dependent on $\theta$ in [1]. While the paper emphasizes its novelty by discussing the momentum design (delay-adaptive lookahead), which differs from asynchronous supervised federated learning, it remains uncertain whether this concept is genuinely unique in comparison to prior literature in federated reinforcement learning, which also addresses the issue of online sample collections that vary with policy updates.

### Questions
.

### Soundness
3

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
3

### Summary
This paper proposes a policy-based federated RL with an asynchronous setting to handle varying arrival times of policy gradient updates. Specifically, the authors analyzed the global and FOSP sample complexity as well as time complexity with a concrete algorithm design. The authors also provided simulation results on MuJoCo, which tackle sample and time complexity issues separately. The proposed method is more practical and can be adaptable to various computing heterogeneity scenarios.

### Strengths
* Numerical experiments on MuJoCo demonstrate impressive results that support the better time complexity of the proposed method
* Both FOSP and global sample complexity match the state-of-the-art while the global time complexity can have a tighter bound with heterogeneous arrival times

### Weaknesses
 * The ultimate goal of federated RL is to find the trade-off between sample and communication complexity while the emphasis of this work on communication complexity/strategy is limited and not clear to me. Please elaborate more about what the threshold or event triggered for any agent to have the synchronization/communication with the server in your proposed framework.
* There are some typos in the manuscript. For example, you write *MoJuCo* instead of *MuJoCo* in the caption of Figures 3 and 4.
* In Line 268, you mention *the set of active agents*. Does it mean the agents that can apply global iteration? If so, then the following paragraph mentions that *only one gradient to update the model from the agent who has finished its local computation.* In other words, does it allow more than one agent to apply policy gradient at the same iteration?
* For Figure 3, could you please let PG (N=1)  and AfedPG (N=2) train even longer to see if they can converge to a similar reward as the other two? If they cannot, I feel curious as to why they can't.
* Is there any analysis or experiment of communication cost?

### Questions
* In Line 268, you mention *the set of active agents*. Does it mean the agents that can apply global iteration? If so, then the following paragraph mentions that *only one gradient to update the model from the agent who has finished its local computation.* In other words, does it allow more than one agent to apply policy gradient at the same iteration?
* For Figure 3, could you please let PG (N=1)  and AfedPG (N=2) train even longer to see if they can converge to a similar reward as the other two? If they cannot, I feel curious as to why they can't. 
* Is there any analysis or experiment of communication cost?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an asynchronous federated reinforcement learning framework termed AFedPG for the policy gradient algorithm. It designs a delay-adaptive lookahead technique that can effectively handle heterogeneous arrival times of policy gradients. This work shows theoretical linear speedup in terms of the norm for policy gradient and verifies the speedup effect numerically.

### Strengths
1. The proposed framework handles the delayed arrival of policy-gradient and reduces the waiting time compared to the algorithm for the homogeneous setting.

2. The authors propose their special step size designs to cancel out a second-order error term when conducting the error analysis, which serves as a technical novelty.

3. Numerical experiments demonstrate that the authors accelerate the training process compared to the synchronous algorithm.

### Weaknesses
1. Issues in Section 4. The authors are encouraged to explain more about the concepts of active agents, concurrency, and delay. Specifically, the notion of an 'active agent' and how it relates to the asynchronous update process needs further clarification. The degree of concurrency and how it impacts the algorithm's performance should be discussed more thoroughly, including potential bottlenecks. The paper should also provide a more precise definition of 'delay' in the context of policy gradient updates, including how it is measured and modeled. In algorithm 2, the authors are encouraged to explain more details about model sharing from the central server as how the agents hold $d_{k-1}$ and $\theta_{k-1}$ is not explicitly explained. A clear description of how the central server distributes the updated model parameters and how agents maintain their local copies is necessary. In addition, the authors are encouraged to explain the relationship between their algorithms and the single-agent and homogeneous counterparts in the literature. A discussion of how the proposed asynchronous method compares to existing synchronous and single-agent policy gradient methods would be beneficial, highlighting the advantages and disadvantages. Last, the authors assume that the agents can sample a trajectory with infinite lengths, which is impossible in practice. The authors are recommended to explain more on such assumptions, including the potential impact of trajectory truncation on the convergence properties of the algorithm.

2. Issues in Section 5. (a) In equations 10 and 11, RHS contains a constant term that does not depend on $K$, which originates from the function approximation error as indicated in the appendix. The authors are encouraged to explain this term in the main paper. The significance of this constant term and its implications for the convergence behavior should be discussed in the main text. (b) The authors are encouraged to explain how they get the total waiting time in line 394. The derivation of the total waiting time should be explicitly shown, including any assumptions made in its calculation.

3. Issues in Appendix B (proofs). (a) The authors are encouraged to explain more about the definitions and notations that are already established in the literature, for example, $F_\rho(\theta),\mu_F,\sigma_g$. A brief explanation of these standard notations would improve the readability of the proofs. (b) In Lemmas B.6 and B.7, the authors are recommended to point out the cited lemma in the references. The specific references for these lemmas should be included for verification. (c) The second term in line 1084 should be $(\mathbb{E}\cdot^2)^{1/2}$. (d) In equations 37 and 38, there are typos related to $\nabla$. The gradient operator is not correctly placed in these equations. (e) In line 1028, there is a typo related to $d_{\delta_{k-1}}$.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
