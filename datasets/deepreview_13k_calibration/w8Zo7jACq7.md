# Model-Free, Regret-Optimal Best Policy Identification in Online CMDPs

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 6, 6, 3, 6

## Abstract
This paper considers the best policy identification (BPI) problem in online Constrained Markov Decision Processes (CMDPs). We are interested in algorithms that are model-free, have low regret, and identify an approximately optimal policy with a high probability. 
Existing model-free algorithms for online CMDPs with sublinear regret and constraint violation do not provide any convergence guarantee to an optimal policy and provide only average performance guarantees when a policy is uniformly sampled at random from all previously used policies. In this paper, we develop a new algorithm, named Pruning-Refinement-Identification (PRI), based on a fundamental structural property of CMDPs proved in \cite{Koo_88,Ros_89}, which we call {\em limited stochasticity}.  The property says for a CMDP with $N$ constraints, there exists an optimal policy with {\em at most} $N$ stochastic decisions. 
The proposed algorithm first identifies at which step and in which state a stochastic decision has to be taken and then fine-tunes the distributions of these stochastic decisions. Assuming the CMDP instance is well-separated\footnote{The exact definition can be found in Section \ref{sparsity}.}, PRI achieves trio objectives: (i) PRI is a model-free algorithm; and (ii) it outputs an approximately optimal policy with a high probability at the end of learning; and (iii) PRI guarantees $\tilde{\mathcal{O}}(H\sqrt{K})$ regret and zero constraint violation for well separated CMDPs\footnote{{\bf Notation:} $f(n) = \tilde{\mathcal O}(g(n))$ denotes $f(n) = {\mathcal O}(g(n){\log}^k n)$ with $k>0.$ The same applies to $\tilde{\Omega}.$}, which significantly improves the best existing regret bound $\tilde{\mathcal{O}}(H^4 \sqrt{SA}K^{\frac{4}{5}})$  under a model-free algorithm, where $H$ is the length of each episode, $S$ is the number of states, $A$ is the number of actions, and the total number of episodes during learning is $2K+\tilde{\cal O}(K^{0.25}).$ We further present a matching lower via an example that shows under any online learning algorithm, there exists a well-separated CMDP instance such that either the regret or violation has to be $\Omega(H\sqrt{K}),$ which matches the upper bound by a polylogarithmic factor.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the paper, the authors propose a model-free algorithm for deterministic CMDP (deterministic, in terms of rewards and constraints) which guarantees \sqrt{T} regret bound and constraint violation. Moreover, the algorithm proposed outputs a near-optimal policy with high probability.

### Strengths
The paper is well written. Furthermore, the authors propose the first model-free algorithm achieving \sqrt{T} regret and violations in CMDPs which outputs a near optimal policy, which is a non-trivial result.

### Weaknesses
1) Since the paper refers to deterministic CMDP (and even assuming the generalisation to stochastic rewards and constraints to be trivial), the notion of violation proposed seems to be weak. Indeed, [Efroni et al., 2020]  model-based methods, achieves optimal sublinear violation when the cancellations between episodes are not possible.
2) The algorithm strongly relies on the Triple-Q algorithm, employing it as subroutine. Thus, the algorithmic novelty is partial.
3) The assumption that the CMDP’s LP has a unique solution is strong. Since it is relaxed in the second part of the paper, I do not see any reason to focus half of the paper on this case. Same reasoning holds for assumption 3. 
4) The theoretical results hold only for Large K, while no guarantees are provided if the number of episodes is small.
5) In chapter 6, when the assumption on unique solution is relaxed, the authors introduce additional strong assumptions. For example, Assumption 4 states that the algorithm is given as input a lower bound on the probability of visiting every state-action pairs (when it is not 0) under the optimal policies belonging to the extreme point of the decision space.
6) Given that the main novelty of the paper concerns the model-free nature of the algorithm (indeed, model-based algorithms achieves better theoretical guarantees), the authors should devote more space clarifying which is the improvement in terms of the computational complexity of the algorithm proposed with respect to prior works.

### Questions
Triple-Q assumes that salter condition holds. I assume this must be true even in your case, since Triple-Q is employed in PRI algorithm. Is it right?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a model-free algorithm for online constrained MDP. The algorithm is based on Triple Q and a novel pruning-refinement-identification algorithm. This paper also highlights a limited stochasticity property of the optimal policy for constrained MDP that has been overlooked in the literature. The proposed algorithm enjoys both sublinear regret and constraint violation, which improves the existing algorithm in the literature. Simulation results also show performance improvement.

### Strengths
1. The paper is well-written. 
2.

### Weaknesses
My only suggestion for improving the clarity is to add a short review of Triple-Q to make the paper more self-contained. Other questions are discussed in the next box.

Q1: in equation (3), does $\rho^n$ mean the exponential of $\rho$, or just a constant that differs with $n$? If it is an exponential of $\rho$, can the authors explain why considering this special form? What's the difficulty of considering general $\rho_n$? If it is indeed a constant that takes different values with $n$, then I suggest using $\rho_n$ to avoid confusion.

Q2: In Algorithm 1, what is K is unknown? How to implement the algorithm? Does Theorem 1-3 still hold?

Q3: In section 7, why does Triple Q have a much smaller negative constraint violation? Is it because Triple Q becomes very conservative in the end? But shouldn't the conservativeness reduce as learning continues? Besides, instead of total constraint violation, what's the total number of episodes or stages of constraint violation?

### Questions
Q1: in equation (3), does $\rho^n$ mean the exponential of $\rho$, or just a constant that differs with $n$? If it is an exponential of $\rho$, can the authors explain why considering this special form? What's the difficulty of considering general $\rho_n$? If it is indeed a constant that takes different values with $n$, then I suggest using $\rho_n$ to avoid confusion.

Q2: In Algorithm 1, what is K is unknown? How to implement the algorithm? Does Theorem 1-3 still hold?

Q3: In section 7, why does Triple Q have a much smaller negative constraint violation? Is it because Triple Q becomes very conservative in the end? But shouldn't the conservativeness reduce as learning continues? Besides, instead of total constraint violation, what's the total number of episodes or stages of constraint violation?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the reinforcement learning problem for constrained MDPs in the tabular setting, and proposes a model-free algorithm that returns a policy with with sublinear $\tilde{\mathcal{O}}(\sqrt{K})$ regret and constraint violation with high probability.

### Strengths
- Exploiting specific structural properties of policies and occupancy measures in the constrained MDP case, the paper proposes an effective model-free learning algorithm with a good regret and acceptable constraint violation performance. Instead of best-iterate convergence, a stronger regret result was proved. These results may be good contributions.
- The paper is extremely well-written. The algorithm design and analysis were discussed very clearly.

### Weaknesses
 - Although the algorithm achieves a better regret bound compared to Triple-Q in (Wei et al., 2022a), this improvement comes at the expense of increased constraint violation. Is there a tradeoff between regret and constraint violation? If so, is it possible to achieve this tradeoff by using different hyperparameters?

 - How does the minimum state-exploration probability $p_{min}$ in Assumption 3 appear in the regret and constraint violation bounds?

- Should Assumption 3 hold for any greedy policy $\pi$? It looks a little strong in its current form.

### Questions
- How does the minimum state-exploration probability $p_{min}$ in Assumption 3 appear in the regret and constraint violation bounds? 

- Should Assumption 3 hold for any greedy policy $\pi$? It looks a little strong in its current form.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a model-free algorithm for episodic constrained MDP that identifies the best policy within $\tilde{\mathcal{O}}(1/\sqrt{K})$ error and generates the optimal $\tilde{\mathcal{O}}(\sqrt{K})$ regret which vastly improves upon the best known model-free result.

### Strengths
The authors present a novel technique for proving the regret guarantees of CMDP. This might be useful in other constrained optimization setups. Overall, the paper reads well.

### Weaknesses
### weaknesses:
 Please see the questions below.

 1. Episodic CMDP can be considered a special case of infinite-horizon average reward CMDP. An average reward CMDP can be transformed into an episodic CMDP by substituting $T=HK$ and augmenting a time index modulo $H$ in the state description. Therefore, Table 1 should also include the equivalent results obtained from the average reward CMDP literature. Specifically, it would be beneficial to see how the regret bounds and best policy identification results compare when translated between these two settings.

 2. It is not clear from the related works if the model-free best policy identification (BPI) approach has been considered in the literature solely for unconstrained MDP. If yes, then the best regret bound in that category should be pointed out. If not, then this should be stated to highlight the novelty of the present work in extending BPI to the constrained setting.

 3. The term $M$ in Lemma 2 has not been explicitly defined. While it is used later in the paper, its first appearance should be accompanied by a clear definition to ensure the reader's understanding.

 4. There should be a policy initialization in Algorithm 1. The algorithm, as presented, lacks an initial policy to start the optimization process. This omission needs to be addressed to ensure the algorithm's completeness.

 5. Please use a different notation for the coefficients in $(11)$. The current one is similar to the notation of an action, potentially leading to confusion. A distinct notation, such as $\alpha_m$, would enhance clarity.

 6. It seems that the number of optimization variables in $(11)$ is $\mathcal{O}(A^{SH})$ which could make the problem prohibitive for a large state space. This should be clearly stated in the paper. Specifically, the paper should discuss the computational complexity of solving the linear program in (11) and how it scales with the size of the state and action spaces.

 7. Assumption 1 indicates that the design of the algorithm requires knowledge about the optimal occupancy measure which is highly unlikely in practice. This assumption significantly limits the applicability of the proposed algorithm. The paper should discuss the implications of this assumption and explore potential relaxations or alternative approaches that do not require such knowledge.

 8. It seems that Assumption 2 is redundant for finite state and action spaces. The paper should clarify if this assumption is indeed necessary in the context of finite MDPs or if it can be removed without affecting the theoretical results.

 9. The policy identification stage is run for $\mathcal{O}(MKH)$ number of steps and as stated before, $M$, in the worst-case can be $\mathcal{O}(A^{SH})$. Why this bound does not appear in the final regret should be intuitively explained. A more detailed explanation of how the policy identification stage contributes to the overall regret bound is needed.

 10. Theorem 3 dictates the BPI result assuming perfect pruning which does not happen with at most $\mathcal{O}(K^{-0.1})$ probability. In the introduction, this probability is mentioned to be $\mathcal{O}(1/\sqrt{K})$. Please clarify. This discrepancy between the introduction and Theorem 3 needs to be resolved to ensure the accuracy of the presented results.

### Questions
1. Episodic CMDP can be considered a special case of infinite-horizon average reward CMDP. An average reward CMDP can be transformed into an episodic CMDP by substituting $T=HK$ and augmenting a time index modulo $H$ in the state description. Therefore, Table 1 should also include the equivalent results obtained from the average reward CMDP literature.

2. It is not clear from the related works if the model-free best policy identification (BPI) approach has been considered in the literature solely for unconstrained MDP. If yes, then the best regret bound in that category should be pointed out.

3. The term $M$ in Lemma 2 has not been explicitly defined. 

4. There should be a policy initialization in Algorithm 1.

5. Please use a different notation for the coefficients in $(11)$. The current one is similar to the notation of an action.

6. It seems that the number of optimization variables in $(11)$ is $\mathcal{O}(A^{SH})$ which could make the problem prohibitive for a large state space. This should be clearly stated in the paper.

7. Assumption 1 indicates that the design of the algorithm requires knowledge about the optimal occupancy measure which is highly unlikely in practice.

8. It seems that Assumption 2 is redundant for finite state and action spaces.

9. The policy identification stage is run for $\mathcal{O}(MKH)$ number of steps and as stated before, $M$, in the worst-case can be $\mathcal{O}(A^{SH})$. Why this bound does not appear in the final regret should be intuitively explained.

10. Theorem 3 dictates the BPI result assuming perfect pruning which does not happen with at most $\mathcal{O}(K^{-0.1})$ probability. In the introduction, this probability is mentioned to be $\mathcal{O}(1/\sqrt{K})$. Please clarify.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the best policy identification (BPI) problem in online Constrained Markov Decision Processes (CMDPs), focusing on the development of a model-free algorithm with low regret that identifies an optimal policy with high probability. A new algorithm, Pruning-Refinement-Identification (PRI), is proposed, leveraging a newly discovered structural property of CMDPs named limited stochasticity. PRI ensures near-optimal policy output with a high probability and guarantees improved regret and constraint violation bounds in the tabular setting.

### Strengths
The result that there are at most $N$ states with a stochastic policy seems interesting. Here $N$ is the number of constraints.

### Weaknesses
1. Some assumptions of this paper seem a bit strong. In particular, this paper requires that each state-action pair can be visited with nontrivial probability $p_{min}$. Also, Assumptions 2 and 5 seem unnatural to me. When comparing with existing works, it would be nice to also compare with the assumptions made in these works. In particular, Assumptions 2 and 5 require a lower bound on the deviation of the value function based on the total variation distance of the occupancy measure, which is a strong requirement. It is not clear if this assumption holds for any non-trivial CMDP model beyond simple bandit settings. This assumption needs more justification and discussion.

2. Technically, this works seems a combination of Triple-Q with additional policy fine-tuning. It would be great to highlight the technical novelty. In particular, I wonder whether PRI can be used together with any online RL algorithm for CMDP with sublinear regret and constraint violation.

3. It would be great if the authors could conduct some simulation experiments that shows the the optimal policy is found, not just regret and constraint violation.

### Questions
1. When will Assumptions 2 and 5 hold?
2. Why do you need the policy to be unique in the first part of the theory?
3. In Theorem 4, do you get exactly an optimal policy or an approximate one as in Theorem 3.
4. Can you replace Triple-Q with any efficient CMDP algorithm as long as the regret and constraint violation are sublinear? Suppose the regret is $K^{\alpha}$ and constraint violation is $K^{\beta}$. What would be the error in learning the policy? I am asking because it seems that the proof of Theorem 3 only requires some regret and constraint violation results.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
