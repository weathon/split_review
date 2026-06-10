Here is my consolidated review.

---

## Summary

This paper proposes MFCGD and AdaMFCGD, two momentum-based variance-reduced algorithms for nonconvex federated composition optimization. The key theoretical claim is that both algorithms achieve $\tilde{O}(\epsilon^{-3})$ sample complexity and $\tilde{O}(\epsilon^{-2})$ communication complexity, improving on prior federated compositional methods (ComFedL, LocalMOML, FEDNEST, Local-SCGDM). AdaMFCGD further introduces a unified adaptive matrix framework that can incorporate various adaptive learning rate schemes. The paper provides convergence analysis under non-i.i.d. data and standard assumptions.

## Strengths

- **Provably lower complexity bounds than prior work**: Table 1 and Theorems 1–2 establish $\tilde{O}(\epsilon^{-3})$ sample and $\tilde{O}(\epsilon^{-2})$ communication complexity, improving on the best prior rates of $O(\epsilon^{-4})$ and $O(\epsilon^{-3})$ respectively (Local-SCGDM). These bounds are derived from the convergence analysis in Remarks 3.1 and 3.2, and represent a concrete theoretical advance over existing federated composition methods.

- **Unified adaptive matrix framework**: AdaMFCGD (Algorithm 1, lines 218–219, 246–250) introduces a flexible adaptive matrix $A_t$ that can instantiate multiple adaptive learning rate schemes (element-wise Adam-style via $a_t = \vartheta_t a_{t-1} + (1-\vartheta_t)\bar{w}_t^2$, norm-type via $a_t = \vartheta_t a_{t-1} + (1-\vartheta_t)\|\bar{w}_t\|$, etc.). The paper explicitly contrasts this with prior adaptive FL methods such as local-AMSGrad (Chen et al., 2020) which are restricted to specific adaptive learning rates (lines 271–272), making this a genuinely more general contribution.

## Weaknesses

### Fatal

- **Experiments section is entirely empty despite being claimed as a core contribution**: Section 5 ("Numerical Experiments") contains only an introductory sentence and two subsection headings ("Robust Federated Learning" and "Task-Distributed Meta Learning") with *no content whatsoever* — no datasets, no baselines, no hyperparameters, no figures, no tables, no results of any kind (lines 420–426). The paper's abstract (line 10) states "We conduct the numerical experiments on robust federated learning and distributed meta learning tasks to demonstrate the efficiency of our algorithms," and contribution (3) (line 105) lists "Experimental results demonstrate efficiency of our algorithms" as a main contribution. These claims are unfulfilled. A paper that advertises experimental validation as a stated contribution and then provides none cannot be accepted for publication. This is not a case of weak experiments — it is a case of the paper not delivering what it explicitly promises.

### Major

- **Parameter constraints in the convergence theorems are unverified for feasibility**: Theorems 1 and 2 (lines 367–368, 397–398) specify a dense web of interdependent constraints on parameters $k, n, \gamma, c_1, c_2, c_3, \rho, B, \Theta, q$ with multiple cross-dependencies. For instance, $c_1$ must simultaneously satisfy both a lower bound ($c_1 \geq \frac{2}{3k^3} + B$, where $B$ itself depends on $c_2, \gamma, q, L_{fg}, C_{fg}, \rho, \Theta$) and an upper bound (via $c_1^2 + c_2^2 \leq \frac{(24)^4 q^2 \gamma^4 L_{fg}^4 C_{fg}^4}{9\rho^4}$); $\gamma$ has both upper and lower bounds that intertwine $\rho, q, L_{fg}, C_{fg}, L, k, n$, and $(c_1^2+c_3^2)^{1/4}$. The remarks (lines 376–383, 405–416) hand-wave feasibility by assuming "$k=O(1), \rho=O(1), c_1=O(1), c_2=O(1), c_3=O(1), n=O(q^3)$" without demonstrating that these asymptotic choices satisfy the concrete inequalities simultaneously. The $\Theta + \frac{BC_g^2\rho^2}{(24)^2 L_{fg}^2 C_{fg}^2} \leq \frac{5\rho^2}{48}$ constraint (Theorem 1) is particularly opaque. Without showing that a feasible assignment of constants exists, the claimed convergence rates rest on an unverified premise. This is especially consequential in the absence of experiments, which could have at least empirically verified that the algorithms converge under reasonable parameter settings.

### Minor

- **No limitations or discussion of practical challenges**: The paper acknowledges no limitations of its approach. Several are worth noting: (a) the bounded gradient assumption (Assumption 2) is strong for deep learning models, though projections are used to enforce it; (b) the large constants in the bounds (e.g., factors of 24, 864, $L_{fg}^4 C_{fg}^4$) suggest the asymptotic complexity advantage may only kick in at impractically small $\epsilon$ values; (c) the extensive parameter tuning required by the constraint set is a practical concern.

### Trivial

None.

## Nice-to-Haves

- Explicitly constructing a concrete assignment of all parameter constants satisfying the constraints in Theorem 1/2 would significantly strengthen the theoretical contribution.
- A limitations section discussing practical challenges (parameter tuning, projection reliance, constant sizes) would improve the paper's framing.

## Removed Points

These points from the reviewers are flagged for removal. Treat them with caution.

- *Harsh critic's point about "big-O hides constants, making practical advantage unclear"*: This criticism is generic and applies to essentially every theoretical optimization paper that uses big-O notation. It is not a specific weakness of this paper. Removed as a generic concern that does not harm the core claim.

- *Harsh critic's point about algorithm clarity at synchronization steps and adaptive matrix behavior*: The algorithm structure is standard for FedAvg-type methods and is sufficiently clear from Algorithm 1 (lines 214–235). The behavior of $A_t$ (generated at sync steps, held constant during async steps per line 225) is explicitly described. Removed as an overly nitpicky presentation critique.

- *Harsh critic's point about missing appendix/proofs*: The instructions forbid criticizing missing appendix content. Removed.

- *Strength finder's point about "explicit non-i.i.d. data heterogeneity"*: This is standard for federated learning papers and does not constitute a distinctive strength, though it is kept as a supporting observation. Downgraded to supporting context rather than a standalone strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation that transcends what the paper itself claims.

## Suggestions

1. The experiments section must be completed with concrete results (convergence curves, datasets, baselines, hyperparameters) before the paper can be considered for publication. The two applications described in the introduction (robust FL and task-distributed meta learning) provide clear testbeds.
2. Demonstrate the feasibility of the parameter constraints in Theorems 1 and 2 by providing an explicit numeric assignment or a constructive proof that a feasible region exists.
3. Add a limitations paragraph or section discussing practical parameter selection, the strength of the bounded gradient assumption, and the regime in which the complexity improvement becomes practically meaningful.

## Score and Decision

The paper presents a genuine theoretical contribution (improved complexity bounds, a unified adaptive matrix framework), but the fatal absence of the experiments section — which the paper itself lists as a core contribution — makes it incomplete for publication. The unverified feasibility of the complex parameter constraints further weakens the theoretical claims. The paper cannot be accepted in its current form.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>