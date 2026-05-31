## Human Reviewer 1

### Summary
This paper studies the problem of online inventory optimization, which is a setting where the decision-maker sequentially chooses the order-up-to level such that the warehouse capacity is not exceeded, with the goal to minimize the total cost according to some loss function (that is revealed after choosing an action). They use the "sell-out period" as a measure of the difficulty of the environment. They propose an algorithm that uses the doubling trick to handle the fact that the sell-out period is not known, a base smoothed online convex optimization algorithm, and also a projection from the output of the base algorithm to the feasible set.

### Strengths
- The algorithm appears to improve the regret rate beyond prior work that studied this problem. However, it is not clear that the referenced works are using the same assumptions as this paper.
- The algorithm appears to provide dynamic regret rates in this setting, which appear to be new. There is a clear motivation for the utility of such analysis.
- The use of smoothed OCO in this problem is a nice idea, although it is unclear to me how novel this idea is with respect to the literature.

### Weaknesses
- The comparison in Table 1 does not appear to be quite a fair comparison. In particular, the warehouse constraint in prior work Hihat et al. (2023) is a general convex set, whereas the one in the paper restricts the sum of the items to be less than the capacity. This seems to be quite a restrictive assumption of the items take up different space in the warehouse.
- I found some of the presentation to be poor to the point that it was difficult to verify the theoretical results in the paper. I point these out and ask for clarification in the Questions section.

### Questions
- In Remark 1, the paper seems to suggest that the gradient of $\ell(y_t) = p \max(d_t - y_t)$ can be computed without knowledge of $d_t$. However, this is not correct.
- It seems that in the definition of $L_\max$, the sum over the items of the demand is greater than capacity. Otherwise, it seems to not make sense.
- I found the first sentence of Definition 2 to be nonsensical.
- Do all of the works in Table 1 use the same notion of $L_\max$? I understand that the notation is different, but is the underlying quantity the same?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper addresses Online Inventory Optimization (OIO) in non-stationary environments, a variant of Online Convex Optimization (OCO). It proposes a two-stage projection algorithm (base learner + feasible-region projection) that connects OIO to Smoothed OCO (SOCO), achieving near-optimal dynamic regret $\tilde{O}(\sqrt{L_{max}T(1+P_T)})$. The paper also provides the first $\Omega(\sqrt{L_{max}T})$ lower bound for OIO.

### Strengths
1. The two-stage projection strategy effectively eliminates carryover stock constraints by linking OIO to SOCO, a key innovation addressing dynamic environment limitations of prior OIO works.
2. The paper establishes matching upper/lower bounds for OIO regret, and derives a lower bound as a valuable byproduct.

### Weaknesses
1. The paper does not evaluate the computational overhead of its algorithm. For example, the SOGD base learner requires $K=\lfloor\log_2 T/(32\max(L,1)\log T)\rfloor+1$ experts and combiners, and the doubling trick involves restarting the base learner; the growth of computational cost with T or $L_{max}$ is unreported, which is critical for real-time inventory applications.

2. The ideal comparator $u_t=d_t$ assumes $d_t\leq D$ to satisfy $u_t\in C(0)$. However, the paper does not discuss how the algorithm performs when demand $d_t>D$, which is a common real-world scenario, nor does it clarify whether the regret bound remains valid when $u_t$ must be capped at D.

### Questions
1. Could you provide preliminary insights into extending the framework to include lead time or fixed ordering costs?
2. In the high-probability extension of $L_{max}$, can you quantify how $\delta$ influences the choice of $L_{max}$?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 3

### Summary
This paper addresses the Online Inventory Optimization (OIO) problem , which is an extension of Online Convex Optimization (OCO) that includes constraints from carryover stock. The authors make a strong case that the standard static regret metric is unsuitable for OIO, especially in non-stationary environments where demand fluctuates, as the best fixed strategy is often a poor comparator.  The main contribution is a new algorithm that provides a near-optimal dynamic regret guarantee , comparing the algorithm's performance to a time-varying sequence of decisions. This approach cleverly reveals a connection between OIO and Smoothed Online Convex Optimization (SOCO). This connection allows the authors to develop an algorithm with a dynamic regret bound of $\tilde{\mathcal{O}}(\sqrt{L_{max}T(1+P_{T})})$ and an improved static regret of $\tilde{\mathcal{O}}(\sqrt{L_{max}T})$, which is a $\sqrt{L_{max}}$ improvement over existing work. The authors also provide a matching $\Omega(\sqrt{L_{max}T})$ lower bound for the static regret, resolving an open question from prior literature.

### Strengths
1. The paper is well structured and self-contained, with helpful summaries of prior results (Table 1). The example provided on page 1 does a good job of illustrating why dynamic regret is the more appropriate metric.

2. The connection between OIO and SOCO via the projection lemma (Lemma 1) is interesting. It reduces a stateful inventory constraint problem to a well-studied smoothed OCO form.

3. The paper provides the first near-optimal dynamic regret bound for the setting. Furthermore, it improves the static regret bound and provides a matching lower bound, which is solid. The appearance of $\sqrt{L_{\max}}$ is well motivated.

### Weaknesses
1. The paper is purely theoretical and lack of experimental validation.

2. The paper simplifies the problem by assuming a linear warehouse capacity constraint.  The authors admit this is a limitation and that their proofs rely on it. This is a fair limitation, but it does reduce the generality of the result.

3. The connection to adaptive regret or meta-OCO methods (e.g., MetaGrad, Ader) is acknowledged, but it’s unclear if simpler baselines could reach similar dynamic regret under relaxed constraints.

### Questions
1. Could you provide a bit more intuition for $L_{\max}$? For example, in a simple stochastic setting with i.i.d. demand,  what would $L_{max}$ correspond to?

2. The doubling trick restarts the base learner and the set $\mathcal{L}_t$ seems to include the lengths of all previously completed cycles plus the current lengths of all active cycles. Does tracking this set introduce any significant computational or memory overhead, especially for large $N$?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3