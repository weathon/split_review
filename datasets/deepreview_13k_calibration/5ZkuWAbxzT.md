# Sharp Analysis for KL-Regularized Contextual Bandits and RLHF

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
\emph{Reverse-Kullback-Leibler} (KL) regularization has emerged to be a predominant technique used to enhance policy optimization in reinforcement learning (RL) and reinforcement learning from human feedback (RLHF), which forces the learned policy to stay close to a reference policy. While the effectiveness and necessity of KL-regularization have been empirically demonstrated in various practical scenarios, current theoretical analysis of KL-regularized RLHF still obtains the same $\cO(1 / \epsilon^2)$ sample complexity as problems without KL-regularization. To understand the fundamental distinction between policy learning objectives with KL-regularization and ones without KL-regularization, we are the first to theoretically demonstrate the power of KL-regularization by providing a sharp analysis for KL-regularized contextual bandits and RLHF, revealing an $\cO(1 / \epsilon)$ sample complexity when $\epsilon$ is sufficiently small. 

    We further explore the role of data coverage in contextual bandits and RLHF. While the coverage assumption is commonly employed in offline RLHF to link the samples from the reference policy to the optimal policy, often at the cost of a multiplicative dependence on the coverage coefficient, its impact on the sample complexity of online RLHF remains unclear. Previous theoretical analyses of online RLHF typically require explicit exploration and additional structural assumptions on the reward function class. In contrast, we show that with sufficient coverage from the reference policy, a simple two-stage mixed sampling strategy can achieve a sample complexity with only an additive dependence on the coverage coefficient. Our results provide a comprehensive understanding of the roles of KL-regularization and data coverage in RLHF, shedding light on the design of more efficient RLHF algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors provide a new analysis of contextual bandits under KL regularization that achieves an improved sample complexity guarantee. Then, they study the RLHF problem where under coverage assumptions on the reference policy and they provide a tight algorithm under this assumption. In the end, they provide experimental results.

### Strengths
1) Improved sample complexity for contextual bandits under KL regularization with a novel analysis using the property of strong convexity due to the KL regularizer

2) Lower bound for the contextual bandit problem under KL regularization that is tight with the upper for sufficiently small $\epsilon$

3) Lower bound for the RLHF problem with preference feedback

4) Design of an algorithm for the RLHF problem with guarantees that match the lower bound.

### Weaknesses
1) Cannot see the tradeoff between $\eta$ and the number of samples needed. Even from the experimental results, the lower $\eta$ the better the performance.

2) The O(1) coverage assumption is unclear if it is a reasonable one or not a provided way to check so.



### Questions
1) In line 294 it says that "it is obvious that $D^2 \leq C_{GL}$. Could you please provide a proof for that?

2) In line 374 is $s_i \sim \pi_0$ a typo, where does $s_i$ come from?

3) Can you provide a specific example where you compute the coverage of the reference policy and it is O(1)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper provides sharp theoretical analyses for KL-regularized contextual bandit (CB) and RLHF problems. It first studies the theoretical benefits of KL regularization in CB and RLHF and shows that KL regularization improves the sample complexity to $O(1/\epsilon)$, while for unregularized problems $O(1/\epsilon^2)$ samples are required. The paper then studies the role of data coverage. In particular, a two-stage mixed sampling strategy is proposed to achieve sample complexity with only additive dependence on the policy coverage coefficient if the data coverage is sufficient, while previous results often depend on the coverage coefficient multiplicatively. The paper also provides a local policy coverage coefficient and derives sample complexity which has multiplicative dependence on this weaker notion than global policy coverage. Numerical experiments are provided to support the theories.

### Strengths
1. The paper is written clearly and the main results are well delivered. 

2. The paper establishes an integrated theory that provides both lower and matching upper bounds for CB/RLHF sample complexity. The derivations are solid. 

3. RLHF with KL regularization is predominant in LLM alignment. Studying this problem through a theoretical lens has sufficient significance in helping gather insights into designing more efficient RLHF methods.

### Weaknesses
1. I have concerns about the coverage assumptions in the paper and their relation to the practical use case of RLHF in LLM alignment. The policy coverage (Definition 2.7 and 2.8) is assumed for reference policy $\pi_0$. In RLHF, such reference policy is typically a fine-tuned LLM that can have extremely low if not zero probability for some actions (e.g. nonsense responses). In this case, the global policy coverage coefficient can blow up to infinity, and the local policy coverage coefficient can be large (as the KL constraint is in expectation). The current paper only derives additive dependence results for global policy coverage, which can be vacuous if the global coefficient is infinity. On the other hand, the dependence on the local coefficient is still multiplicative (as discussed in Section 3.4), which can be extremely large. 

2. I also have concerns regarding the sample complexity upper bounds. The paper claims to first study the effect of KL regularization in improving the sample complexity for policy optimization from $O(1/\epsilon^2)$ to $O(1/\epsilon)$. However, such $O(1/\epsilon)$ sample complexity result already exists for general strongly convex regularizers [1], which include KL regularization as a special case since the reference policy is assumed to have sufficient coverage. Hence it is likely that the upper bound for CB is already known (given that CB is a special case of MDP). For RLHF, its difference from CB mainly comes from the additional reward learning step, so I expect there could be more explanation on why $O(1/\epsilon)$ samples are sufficient for reward learning from preference data. However, the current version of the paper seems to lack such comparisons/remarks, which in my opinion are necessary for understanding the mechanism of RLHF (just as strong convexity of KL divergence for CB). For baselines, previous literature suggests that reward learning takes $O(1/\epsilon^2)$ samples. 

[1] Lan, Guanghui. "Policy mirror descent for reinforcement learning: Linear convergence, new sampling complexity, and generalized problem classes." Mathematical programming 198, no. 1 (2023): 1059-1106.

[2] Zhu, Banghua, Michael Jordan, and Jiantao Jiao. "Principled reinforcement learning with human feedback from pairwise or k-wise comparisons." In International Conference on Machine Learning, pp. 43037-43067. PMLR, 2023.

### Questions
1. In Definition 2.7 (and 2.8), is the sup taken over $x\in\mathrm{supp}(d_0)$? The current notation is a bit confusing.

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
2

### Summary
The paper provides a novel lower bound of Omega(1/epsilon) for the sampling complexity of finding epsilon-suboptimal solutions in KL-regularized contextual bandit problems. 

The paper then models the online KL-regularized RLHF problem as the KL-regularized contextual bandit problem and proposes a two-stage sampling algorithm. Using the strong convexity of the KL-regularization, the paper shows that the algorithm has sampling complexity O(1/epsilon), with an additive term that depends on the coverage coefficient of the reference policy.

### Strengths
The paper provides sharper analysis of the sampling complexity of KL-regularized contextual bandit problems, and provides novel results on the dependency of the sampling complexity on the data coverage.

### Weaknesses
The paper provides a novel lower bound of Omega(1/epsilon) for the sampling complexity of finding epsilon-suboptimal solutions in KL-regularized contextual bandit problems.

The paper then models the online KL-regularized RLHF problem as the KL-regularized contextual bandit problem and proposes a two-stage sampling algorithm. Using the strong convexity of the KL-regularization, the paper shows that the algorithm has sampling complexity O(1/epsilon), with an additive term that depends on the coverage coefficient of the reference policy.

The paper might benefit from some polishing. For instance, the definitions of some key terms are not rigorous (see questions below). In addition, the proof may lack rigor. For instance, line 320 – 321 uses Taylor expansion, and thus, if my understanding is correct, the equality (and the following inequality) does not hold.

### Questions
- In definition 2.7, line 219 – 221, and definition 2.8, line 231 – 233, what does ``x sampled from d_0’’ mean in the sup? 

- Is there any benefit of using more than 2-stages of sampling?

- Can the authors provide more intuition why the number of samples needed are different in the first and the second stages of the algorithm, as presented in Theorem 3.3?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the RLHF problem for contextual bandits, and aims to obtain a tight sample complexity on the problem. They consider both the reward observation setting and preference observation setting, and provide upper and lower bounds for each. Interestingly, they are able to show that including the KL constraint in the problem allows them to obtain a sample complexity that scales as $1/\epsilon$ instead of the more familiar $1/\epsilon^2$.

### Strengths
To my knowledge, this is the first work to obtain a tight bound on the sample complexity of RLHF with KL regularization. This is a commonly used setting in practice and as such it is important that we understand the sample complexity. It is interesting that one can obtain a $1/\epsilon$ rate as compared to the $1/\epsilon^2$ that might be expected.

### Weaknesses
1. The main coverage condition (Definition 2.6) is extremely strong. This will scale at least with the number of contexts: if we take $\theta = \theta’$, and choose $b(x) = 0$ for $x \neq x_0$ and $b(x_0) = B$ where $x_0$ is the minimum probability context under $d_0$, then the expression given in Definition 2.6 will scale as $1/d_0(x_0) \ge M$ for $M$ the number of contexts. Thus, the main sample complexity results of the paper (Theorem 3.3 and Theorem 4.4) really scale with the size of the context space. In general it is not acceptable to obtain a sample complexity scaling with the size of the context space, as this is typically extremely large, so these results are only meaningful asymptotically as $\epsilon \rightarrow 0$. This issue arises because the coverage condition is defined with a supremum over all possible parameter pairs $\theta, \theta'$, which leads to a worst-case scenario that is highly sensitive to the distribution $d_0$. A more reasonable condition would likely involve an average case analysis over the parameter space, or a condition that is less sensitive to the minimum probability context.
2. Furthermore, the result is also not tight in the regime where $\eta$ is very large. As $\eta$ increases, the KL regularization term becomes less significant, and the problem should approach the standard contextual bandit setting. However, the current bounds do not reflect this, and instead continue to increase with $\eta$. This suggests that the analysis is not capturing the correct behavior in the limit of no regularization.
3. The statement on Line 294 that $D^2 \le C_{GL}$ is not correct as a result of this ($C_{GL}$ in general will not scale with context size).
4. The statement in Theorem 3.1 and Theorem 4.3 that the coverage condition is $O(1)$ is also then incorrect—it should be $\log N_{\mathcal{R}}(\epsilon)$ I believe. The current claim that the coverage condition is $O(1)$ is misleading, as the definition itself involves a supremum over a potentially large set of parameters, which will likely scale with the complexity of the reward function class. This needs to be made explicit in the theorems.
5. The problem setting could be clarified somewhat. In particular, it should be made more explicit that when a policy is $\epsilon$-optimal, this is with respect to $Q(\pi)$, the reward + KL objective, rather than just the reward. The latter is typically more standard for RL, so it should be made clear that the objective considered here is different. The current presentation could lead to confusion, as the standard goal in RL is to maximize the expected reward, and the KL regularization is an additional constraint that is not always present.
6. The writing could be improved. There are various unclear or poorly worded statements (the following list is not exhaustive—please go through the paper carefully and resolve other such issues):
	* Line 59: “DPO suffers from a drop of chosen probability”. I am not sure what this means.
	* Line 62: “the learned model is easy to be hacked and become biased”. Grammatically incorrect, revise wording.
	* Line 64: The sentence starting with “Hence, the KL-regularization..” Is the first time KL regularization is mentioned. It seems like it needs to be introduced earlier for this sentence to read well.
	* Line 283: “identifically” is not a word.
7. There are also several issues with informal technical statements being made that are not necessarily correct:
	* Line 76: RLHF has been demonstrated to outperform offline methods because “it has further interactions with human or preference oracle”. It is not clear that this the reason (or what exactly is even meant by this sentence). This statement is too vague and does not provide a concrete explanation of why RLHF might outperform offline methods. It could be due to better exploration, more accurate reward signals, or other factors, and this needs to be clarified.
	* Line 273: It is much more standard in modern offline RL to obtain bounds under single policy concentrability (ie only one policy is covered). Thus, the claim that global coverage is standard in offline RL is too strong. The statement that global coverage is standard in offline RL is inaccurate, as many modern offline RL methods rely on single-policy concentrability assumptions, which are much weaker. This needs to be revised to reflect the current state of the field.
	* Definition 2.6: What is the $\pi$ referred to here? It is not clear. The definition of the coverage condition is unclear, as the policy $\pi$ is not defined. It is not clear if this is the optimal policy, or some other policy, and this needs to be specified.
	* Line 291: The supremum is over $x \sim d_0$. What does this mean? That the sup is taken over all $x$ in the support of $d_0$? This should be clarified (the same notation is used elsewhere as well). The notation used in Line 291 is ambiguous. It is not clear if the supremum is taken over all $x$ in the support of $d_0$, or if it is a supremum over the expectation with respect to $d_0$. This needs to be clarified for the reader.
	* Remark 3.2: The final sentence in this remark is not justified by Theorem 3.1. Simply showing a lower bound that is smaller than the lower bound for the standard contextual bandit does not imply that the true sample complexity is lower as the lower bound may just be loose—an upper bound is required to show this (which at this point in the paper has not been stated). Therefore, I would suggest removing this sentence.

### Questions
1. Is the scaling with $D^2$ really necessary in Theorem 3.3 and Theorem 4.4 or can this be reduced to $C_{GL}$?
2. For $\eta$ very large (corresponding to no regularization), one would hope to recover the standard complexity bounds for contextual bandits, but this is not the case in any of the upper bounds (all of which will continue to increase as $\eta$ increases). I suspect a more refined analysis may allow one to obtain the minimum of the current complexity and the standard contextual bandit complexity. Could the authors comment on this?

### Soundness
3

### Presentation
2

### Contribution
2
