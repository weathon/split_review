# Learning Optimal Contracts: How to Exploit Small Action Spaces

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We study \emph{principal-agent problems} in which a principal commits to an outcome-dependent payment scheme---called \emph{contract}---in order to induce an agent to take a costly, unobservable action leading to favorable outcomes.
	We consider a generalization of the classical (single-round) version of the problem in which the principal interacts with the agent by committing to contracts over multiple rounds.
	The principal has no information about the agent, and they have to learn an optimal contract by only observing the outcome realized at each round.
	We focus on settings in which the \emph{size of the agent's action space is small}.
	We design an algorithm that learns an approximately-optimal contract with high probability in a number of rounds polynomial in the size of the outcome space, when the number of actions is constant.
	Our algorithm solves an open problem by~\citet{zhu2022sample}.
	Moreover, it can also be employed to provide a $\widetilde{\mathcal{O}}(T^{4/5})$ regret bound in the related online learning setting in which the principal aims at maximizing their cumulative utility over rounds, considerably improving previously-known regret bounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of learning optimal contracts in a principal-agent setting with focus on the setup where the size of the agent's action space is small.

### Strengths
- This paper improves the previous sample complexity bounds for learning optimal contracts in the case when the number of actions is constant.

### Weaknesses
 - It seems to me that the approach of this paper seems to be mostly based on the work of [Letchford et al., 2009; Peng et al., 2019], but this is not explicitly mentioned in the paper. This is acceptable to me, but I expect the authors to discuss and summarize the challenges of extending the previous approach to the current setting.

- Theorem 1 should rather be an observation or proposition than a theorem, since it is a quite obvious fact in learning optimal contracts, even though it might be mentioned explicitly in previous work.

- Definition 1 should rather be an assumption than a definition. I also do not see any benefit of treating this condition as a high probability event. I think you are essentially restricting the learning problem to a subclass of instances where the approximately optimal contract has bounded payment.

- The current notation is not very readable to me, and I would suggest the authors make some efforts on simplifying them. For example, you could use dot product instead of element-wise product over the outcomes spaces in many places.

### Questions
- Do we know any lower bounds for the sample complexity of learning optimal contracts when the action size is small? Do you think it is possible to improve the current method beyond the constant action size case (possibly under other assumptions)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the principal-agent problem where a principal seeks to induce an agent to take a beneficial but unobservable action through contracts. They aim to learn an optimal contract by observing outcomes. The paper proposes an algorithm that can learn an approximately optimal contract within a polynomial number of rounds related to the outcome space size. Specifically, they showed an algorithm with a sample complexity result of O(m^n T^4/5) and also converted it to an explore-then-commit online learning algorithm with sublinear regret.

### Strengths
Learning the optimal principal’s strategy in principal-agent problems when the agent’s type is unknown has become an important problem in those kinds of games with sequential movements. Existing works mainly focused on Stackelberg (security) games. This paper introduced meta-actions to group together the agent’s actions associated with “similar” distributions over outcomes for the specific contract design problem where the agent’s action is unobservable. Then this paper demonstrates how to utilize this idea to learn the approximately optimal contract. The results seem well-executed and the characterization is interesting.

### Weaknesses
One major modeling concern I have is the assumption that the agent will honestly best respond to the principal’s queries, especially if they know that the principal is learning to play against him. This problem is particularly an issue in contract design — if the principal does not know the agent’s utility and wants to learn to play against the agent, then the agent would have strong incentives to manipulate their responses to mislead the principal to learn some non-optimal contracts and would like to do so to benefit himself. This is especially problematic in settings where the agent's true utility function is private information, as the agent has a clear incentive to misrepresent their preferences. The paper does not adequately address the implications of this assumption, nor does it provide any justification for its validity in practical scenarios. The assumption of honest best response is particularly concerning when the agent is sophisticated and aware of the learning process, as this opens the door to strategic manipulation that could severely undermine the learning process. 

On the technical side, I feel like the contribution of this paper might be limited given Peng et al., [2019] and Zhu et al., [2022]. “The core idea of the algorithm is to progressively build two polytopes Ud and Ld” is highly similar to the algorithm proposed by Peng et al. [2019], except that here the agent’s action is not observable, so the authors replace it with some meta action, which is realized by the Action-Oracle. While the introduction of meta-actions is a modification, it is not clear that this modification is substantial enough to warrant a significant contribution. The core algorithm still relies on the same principle of iteratively refining polytopes, and the Action-Oracle, while necessary for the unobservable action setting, seems like a relatively straightforward adaptation. Furthermore, the relaxed assumption regarding the constant volume, which seems to be highly dependent on the result Lemma 4 by Zhu et al. [2022], which shows the Continuity of the principal’s utility function, raises questions about the novelty of the technical contribution. The paper does not clearly delineate the specific technical challenges overcome and how they differ substantially from the existing literature.

### Questions
Could you provide some application domains where your honest-responding agent behavior holds?     
    
   
How is your Lemma 8 different from Lemma 4 by Zhu et al. [2022]? I feel like your results can be directly implied from their result about the Continuity of the principal’s utility function.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper study the sample complexity (and its implication in online learning) of learning the optimal contract in the principal-agent problem. Specifically, they consider the setting where the principal, who does not know the forecast matrix of the agent, offers the agent a contract, and the agent performs the action that maximizes the agent's own utility, and then the principal observes the outcome as a result of the action performed by the agent but not the action itself. The principal may choose different contracts and repeat the above process to figure out the optimal non-negative and bounded contract that maximizes the principal's utility, and the number of repetitions is the sample complexity of this problem.

The main result of this paper is an algorithm that has $\tilde{O}(m^n)$ sample complexity, where $m$ is the number of the outcomes, and $n$ is the number of the actions of the agent. In particular, the sample complexity is polynomial in $m$ when $n$ is a constant.

The key observation underlying this result is that the polytope $\mathcal{P}_i$ containing exactly all the contracts to which the best response of the agent is the same action $i\in[n]$, is defined by $m+n$ inequalities ($m+1$ inequalities that force the contract to be non-negative and bounded, and $n - 1$ inequalities that force the action $i$ to be better than other actions for the agent). Hence, $\mathcal{P}_i$ has at most $\binom{m+n}{m}=\binom{m+n}{n}\le (m+n)^n$ vertices.

The algorithm starts with an outer approximation $\mathcal{P}_i'$ of $\mathcal{P}_i$ ($\mathcal{P}_i'$ is initially defined by the $m+1$ inequalities that force the contract to be non-negative and bounded), and as long as there is some vertex $v$ of $\mathcal{P}_i'$ that is not in $\mathcal{P}_i$ (in other words, the agent's best response to the contract $v$ is some $j\neq i$), it can easily find an inequality (using the structure of the principal-agent problem) that approximately corresponds to the constraint ``action $i$ is better than action $j$ for the agent'', and then it adds this inequality to $\mathcal{P}_i'$. After the algorithm iteratively finds $n-1$ such inequalities, $\mathcal{P}_i'$ will be approximately same as $\mathcal{P}_i$. Moreover, to find one such constraint for the current iterate $\mathcal{P}_i'$, the algorithm only needs to evaluate at most all the contracts corresponding to all the vertices of $\mathcal{P}_i'$, the number of which is bounded $(m+n)^n$ by the key observation above.

### Strengths
* The result is original, and the idea is simple and nice.
* The writing is good overall.

### Weaknesses
I think the biggest weakness of this paper is that it studies the setting without prior distribution of the agent's type.
* First of all, I feel that the sample complexity problem is not well-motivated in this setting -- If I'm the principal, when an agent comes, I won't try to find my optimal contract merely for this agent by signing the agent multiple times with different contracts and observing the outcomes. I would only use this approach, when there is a large candidate pool, and I do not know the prior distribution of the candidates' skills.
* Moreover, the previous work of [Zhu et al. 2022] studies the setting with prior distribution of the agent's type. Their open question is also posed in that setting, so I think ``solves an open problem by Zhu et al.'' is an overclaim.

On a separate note, the space of contract considered in this paper is different from that in [Zhu et al. 2022]. In this paper, the contract is bounded in the sense that the sum of the payments for all outcomes is bounded by some number $B$, but in [Zhu et al. 2022], the contract is bounded in the sense that the payment of each outcome is bounded by some number $B$. That is, even in the narrow setting without prior distribution, the problem studied by this paper is not quite the same as the original one.

### Questions
Could you address the comments in the weakness section?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
