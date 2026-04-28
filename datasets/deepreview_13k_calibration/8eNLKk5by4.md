# Optimal Strong Regret and Violation in Constrained MDPs via Policy Optimization

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
We study online learning in \emph{constrained MDPs} (CMDPs), focusing on the goal of attaining sublinear \emph{strong} regret and \emph{strong} cumulative constraint violation.
	Differently from their standard (weak) counterparts, these metrics do \emph{not} allow negative terms to compensate positive ones, raising considerable additional challenges.
	\citet{Exploration_Exploitation}~were the first to propose an algorithm with sublinear {strong} regret and {strong} violation, by exploiting linear~programming.
	Thus, their algorithm is highly inefficient,
	leaving as an open problem achieving sublinear bounds by means of policy optimization methods, which are much more efficient in practice.
	Very recently,~\citet{mullertruly} have partially addressed this problem by proposing a policy optimization method that allows to attain $\widetilde{\mathcal{O}}(T^{0.93})$ strong regret/violation.
	This still leaves open the question of whether \emph{optimal} bounds are achievable by using an approach of this kind.
	We answer such a question affirmatively, by providing an efficient policy optimization algorithm with $\widetilde{\mathcal{O}}(\sqrt{T})$ \emph{strong} regret/violation.
	Our algorithm implements a primal-dual scheme that employs a state-of-the-art policy optimization approach for adversarial (unconstrained) MDPs as primal algorithm, and a UCB-like update for dual variables.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies efficient online policy optimization in "*loop-free*" constrained MDPs (CMDPs) that slightly generalizes finite-horizon episodic CMDPs, where by "efficient" it refers to avoiding any optimization over the space of occupancy measures. In the *bandit-feedback* setting, it proposes $\texttt{CPD-PO}$, a primal-dual policy optimization algorithm built upon $\texttt{PO-DB}$ that achieves $\tilde{\mathcal{O}}(\sqrt{T})$ *strong* regret/violation bounds.

### Strengths
1. The paper studies a known open problem in literature that is of theoretical interest. The idea to consider *strong* versions of regret and constraint violation is reasonable and well justified.
2. The proof is checked to be correct, and the results do advance the theoretical understanding of policy optimization in CMDPs to a certain level.
3. I like Section 5.2 that compares the proposed algorithm against known algorithms.

### Weaknesses
1. This paper only deals with finite-horizon episodic MDPs with *bandit feedback*, which is a more restrictive setting than Efroni et al. (2020) and Müller et al. (2024). It seems a little unfair to directly compare against those algorithms that do not require bandit feedback. While the authors claim to close the open problem raised by Efroni et al. (2020), the comparison is not entirely direct given the difference in assumptions. Specifically, the bandit feedback setting limits the information available to the algorithm at each step, which can significantly impact the achievable performance and makes it harder to directly compare against algorithms that have access to more information.
2. The algorithmic contribution is limited since $\texttt{CPD-PO}$ largely builds upon $\texttt{PO-DB}$, only adding a simple binary dual update scheme. The core of the algorithm relies heavily on existing techniques, and the novelty is primarily in the specific combination of these techniques. The dual update, while necessary for constraint satisfaction, does not introduce a significant algorithmic innovation. It would be more impactful if the algorithm introduced a novel approach to policy optimization or constraint handling.
3. Despite the theory-oriented approach of this paper, it is still helpful to include at least some simulation results to illustrate the applicability of the proposed algorithm. The absence of empirical validation makes it difficult to assess the practical relevance of the theoretical results. The paper would benefit from a demonstration of how the algorithm performs in a simulated environment, even if it is a simplified one. This would help to bridge the gap between theory and practice.
4. The paper does not discuss about its limitations and future directions.
    * For example, the algorithm seems intractable since it requires the exact value of $\rho$, which is generally unavailable in practice. It would be much better if it can work with only an upper/lower bound of $\rho$, which does not seem to be the case here. The need for the exact value of $\rho$ is a significant limitation, as it is a parameter that is often unknown in real-world scenarios. The algorithm's reliance on this parameter makes it less practical and limits its applicability. A discussion of how to address this limitation would be beneficial.
5. Suggestions on writing:
    * Avoid squeezing key formulations (i.e., the *loop-free* MDP setting) into the footnote, even given the page limit. The definition of the loop-free MDP is crucial for understanding the scope of the paper, and it should be presented in the main text rather than in a footnote. This would improve the readability and clarity of the paper.
    * Clearly convey your message and ideas in the explanatory paragraphs following any mathematical results. For example, the paragraphs following Lemma 3 can be improved (What's the "aforementioned parameters"? Why does eq. (2) hold?). The explanations following mathematical results should be more detailed and explicit. The reader should not have to guess the meaning of terms or the reasoning behind equations.
    * The constants in Lemma 1 & 2 seem inconsistent from those in Lemma 6, up to a numerical factor. The inconsistency in constants across different lemmas is confusing and should be addressed. The authors should clarify why the constants differ and ensure that the results are consistent.
6. Minor typesetting issues:
    * There are a few typos in the paper: $K$ should be $L$ in line 5 of Algorithm 2; missing $i$ in $i \in [m]$ in line 904; etc.
    * I would personally avoid using $\verb|\nicefrac|$ or anything similar to it because it makes fractions hard to read, esp. when you have something like $A+B+C / D+E+F$.

### Questions
Since loop-free MDPs are only a slight generalization of episodic MDPs, the dependency on $H$ also matters. Is $\tilde{\mathcal{O}}(L^5)$ the optimal dependency we can expect here (where $L$ is the horizon length)?

### Soundness
3

### Presentation
2

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
The paper studies an online learning problem in constrained MDPs. The authors propose a new constrained online learning algorithm that leverages an existing unconstrained policy optimization oracle. The authors prove that this method has the optimal regret and constrained violation bounds in a strong sense. This improves the state of the art bound of online learning in constrained MDPs.

### Strengths
- It is crucial to characterize stronger regret and constraint violation in online constrained MDPs since the transitional average performance metrics may obscure policy cancellation that is not permitted in safe policy learning. 

- The authors provide an optimal regret and constraint violation bound by only considering the non-negative terms. This improves the previous suboptimal bound in the online constrained learning setting. 

- The authors propose a new primal-dual online learning algorithm, which is different from the previous work that studies the strong regret and constraint violation. Rather than using regularization, the authors introduce several changes to the standard primal-dual methods: (1) binary dual update; (2) synthetic loss for policy optimization; (3) optimize policy through an existing adversarial policy optimization oracle.

### Weaknesses
 - The authors focus on the basic tabular case of constrained MDPs. This method needs further generalization to extend beyond the tabular case.

- It would be helpful if the authors could clarify the motivation behind the techniques used in the proposed algorithm. Notably, the standard primal-dual policy optimization suffers the oscillation issues, potentially causing linear strong regret and constraint violation. Specifically, the paper does not clearly explain why a binary dual update is used, or why a synthetic loss is necessary for policy optimization. The connection between these choices and the avoidance of oscillations needs to be more explicit.

- The proposed algorithm employs an existing adversarial policy optimization oracle to update the policy. The policy optimization oracle is designed in the adversarial setting, while the constrained MDP problem assumes stochastic rewards, costs, and fixed transitions. It would be helpful if the authors could explain the rationale behind this choice. Furthermore, the paper does not discuss the potential implications of using an adversarial oracle in a stochastic environment, such as whether the adversarial nature of the oracle introduces any bias or instability in the learning process.

- The adversarial policy optimization oracle minimizes the average type regret. It would be helpful if the extra technique to obtain a tighter regret bound can be highlighted. The paper does not clearly articulate how the specific design of the synthetic loss function, combined with the binary dual update, allows for a tighter regret bound compared to standard primal-dual approaches. A more detailed explanation of this mechanism would be beneficial.

- To illustrate the practical utility and verify the algorithm's performance, it would be helpful if the authors provided experimental results.

### Questions
- What is the role of the probability distributions in line 129 in algorithm? 

- How large the margin $\rho$ is? What is the practical implication when it is infinitely small?

- Is it efficient to run the adversarial policy optimization oracle? 

- Can the authors point out the new analysis that avoids the oscillation issue in typical primal-dual methods or compare their key analysis ideas?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies online learning in constrained MDPs with strong regret and strong violation, where the negative terms are not allowed to compensate for positive ones. For this problem, this paper’s algorithm uses a primal-dual approach with UCB-like updates on the dual variables. The method achieves optimal $O(\sqrt{T})$ strong regret/violation, which improves the $O(T^{0.93})$ bound in the state-of-the-art works.

### Strengths
+ The concept of strong constraint violation is more relevant for safe-critical applications. It is also more challenging and technical than the conventional violation.

+ The paper proposed a primal-dual algorithm with an interesting dual design. The theoretical performance on regret and violation is also provided.

### Weaknesses
- The paper missed a few important related references (e.g., [1] and [2]), where the strong violation has been investigated and better results than this paper have been established. In [1], the OptPess-LP algorithm can satisfy the constraints instantaneously, which seems better than $O(\sqrt{T})$ strong violation.  In [2], the paper proposed a model-free method to achieve $O(\sqrt{T})$ strong violation. It would be better to discuss these papers in detail and highlight the differences. Specifically, the paper should clarify how its primal-dual approach compares to the LP-based method in [1], especially given that [1] achieves zero constraint violation under certain conditions, and how it differs from the model-free approach in [2].

- The algorithm requires Slater's condition and the knowledge of Slater's constant $\rho$, which is usually not practical in most critical applications. Besides, the regret is in the order of $O(1/\rho),$ it could be problematic when $\rho$ is close to zero. The paper should acknowledge that the dependence on $\rho$ in the regret bound could be a significant limitation in practice, and discuss potential ways to mitigate this issue, such as adaptive methods for estimating $\rho$ or algorithms that are less sensitive to the value of $\rho$.

- I understand it is a theory paper; however, including numerical experiments to validate the proposed algorithm would be beneficial. For example, the baselines could be Efroni et al. (2020), [1] and [2]. The paper should provide a more detailed computational analysis, comparing the complexity of its dynamic programming and policy optimization approach with the linear programming approach used in [1]. The analysis should consider the number of states and actions, and discuss the practical implications of the different computational requirements.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

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
This paper studies learning constrained tabular MDPs with strong regret and violation guarantees. Prior works in this setting are either computationally inefficient or highly suboptimal. This work provides the first computationally efficient policy optimization algorithm with optimal $\sqrt{T}$ regret. The authors achieve this by leveraging the advance of adversarial MDPs for the primal update and an optimistic estimation for the dual update.

### Strengths
1. The problem studied in this paper is well-motivated and the strong regret/violation metric is reasonable.
2. The author successfully improves the regret bound in this setting from $T^{0.93}$ to the optimal $\sqrt{T}$ for computationally efficient algorithms. This is a huge improvement.
3. The writings are clear and discussion about previous works are sufficient.

### Weaknesses
1. This paper's algorithm and regret bound rely on a problem-dependent factor $\rho$, which could be small and lead to worse regret. The dependence on $\rho$ is concerning because it is not clear how this parameter can be controlled or estimated in practice. A small value of $\rho$ would significantly degrade the performance, potentially negating the benefit of the improved $\sqrt{T}$ regret. The paper should provide more insight into the practical implications of this dependence and discuss scenarios where $\rho$ might be particularly small.
2. This paper does not have an empirical comparison. Although this is typically not necessary for a theoretical paper, simulation results like Muller et al. [2024] could be helpful. The lack of empirical validation makes it difficult to assess the practical relevance of the theoretical results. While the theoretical analysis is rigorous, it is important to demonstrate that the algorithm performs well in practice, especially given the dependence on the potentially problematic $\rho$ parameter.
3. A conclusion and discussion section is lacking.

### Questions
1. Could the authors provide more technical reasons why $\rho$ is required in this paper? Does this factor also appear in previous papers?
2. Is there any regret lower bound in this setting that is related to the number of constraints $m$?

### Soundness
3

### Presentation
3

### Contribution
3
