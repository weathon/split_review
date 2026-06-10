Here is my consolidated final review.

---

## Summary

This paper proposes the first algorithms for Conservative Contextual Bandits (CCBs) with general non-linear cost functions, moving beyond the multi-armed and linear settings that bounded all prior work. The core idea is a reduction to online regression via Inverse Gap Weighting (IGW) exploration, producing two algorithms — C-SquareCB (squared-loss oracle) and C-FastCB (KL-loss oracle) — with sub-linear and first-order regret guarantees, respectively. Neural instantiation via OGD provides end-to-end regret bounds, and experiments on six OpenML datasets show improvement over the existing CCB baseline (C-LinUCB).

## Strengths

- **First CCB algorithms for general non-linear cost functions**, removing the linearity requirement that bounded all prior work (lines 37–38: "algorithms and regret guarantees for the general case do not exist"). The algorithms operate under only a realizability assumption and an online regression oracle.

- **C-FastCB provides the first first-order regret bound for CCBs**, scaling with the optimal cumulative loss L* rather than the horizon T (Theorem 4.1, eq. 4.4). No prior CCB work — including the linear case — achieved this data-dependent improvement.

- **Novel analytical technique for bounding baseline pulls (n_T) without confidence sets** (Remark 3.3, lines 234–236). The analysis relates n_T to the squared/KL loss of the regression oracle, bypassing the need for the upper/lower confidence bounds on parameter estimates that the linear-case analysis relied on and which are unavailable for general function classes.

- **Avoids the proven Ω(T) worst-case pitfall of Neural UCB/Thompson Sampling** (lines 39–40, citing Deb et al., 2024). By using IGW-based exploration instead of UCB, the proposed algorithms circumvent a known failure mode that would extend to any UCB-based conservative modification.

- **Handles adversarially chosen contexts** (line 58), unlike several prior neural bandit works that require i.i.d. contexts from a fixed distribution.

## Weaknesses

### Fatal
None

### Major
None

### Minor

- **Limited experimental baselines**: The regret comparison (Figure 1) is restricted to C-LinUCB, a linear method. While C-LinUCB is the only existing CCB algorithm, showing that a non-linear method outperforms a misspecified linear method on non-linear problems is unsurprising. The paper would benefit from comparisons that isolate the contribution of the conservative IGW reduction — e.g., comparing against a non-conservative SquareCB (with a post-hoc safety filter) or against standard neural bandit methods adapted to respect a safety constraint — to demonstrate that the specific algorithmic structure adds value beyond any non-linear function approximator.

- **Safety condition relies on theoretical oracle regret bounds**: The safety conditions for C-SquareCB (eq. 7, term (C)) and C-FastCB (Algorithm 2, line 264) involve the oracle's regret bound (reg_sq(m_{t-1}) or reg_kl(T)) — theoretical quantities not directly available to the algorithm. The paper does not discuss how these would be obtained in practice (e.g., by substituting known worst-case bounds or treating them as hyperparameters). This is a gap between the theoretical description and any practical instantiation.

- **Structural asymmetry between the two safety conditions**: The C-SquareCB safety condition (eq. 7) uses reg_sq(m_{t-1}) (oracle regret evaluated on observed m_{t-1} data points) and includes a log(4/δ) term consistent with high-probability concentration. The C-FastCB condition (Algorithm 2, line 264) uses reg_kl(T) (total-horizon bound) and lacks the log(4/δ) term. The paper does not explain this asymmetry. The C-FastCB condition additionally requires advance knowledge of the horizon T. Furthermore, the C-FastCB regret bound is stated for *expected* regret (Theorem 4.1, line 295), while C-SquareCB's is high-probability — this difference in guarantee type is not discussed.

- **Missing experimental details**: The value of α used in experiments is not reported, and no ablation studies show how regret or constraint violation varies with α. The network width is unspecified ("two layered neural network," line 395). These omissions hinder reproducibility and assessment of the conservatism mechanism.

### Trivial
- Figure 1 (regret curves) does not include error bars or confidence bands despite being "averaged over 10 runs," making it difficult to assess result variability.

## Nice-to-Haves
- An ablation comparing the fixed-action baseline against a stronger learned baseline (e.g., from offline data) would demonstrate the safety mechanism under more realistic conditions.
- Reporting the empirical number of baseline-action rounds (n_T) — a central quantity in the theoretical analysis — would directly validate the analysis.
- Clarifying why the C-FastCB bound is in expectation while C-SquareCB's is high-probability, given both theorems state "with probability 1-δ."

## Removed Points
These points were assessed and removed as either unsubstantiated, violating hard rules, or redundant:

- **Request for Neural UCB / Neural Thompson Sampling baselines**: Removed because these are non-conservative algorithms. Comparing regret between a safety-constrained algorithm and an unconstrained one is not apples-to-apples. The paper does compare against vanilla (non-conservative) versions of its own algorithms in Figure 2.
- **Claim that experiments do not support the paper's central claim**: The empirical claim is outperforming "the existing baseline" for CCBs, which is C-LinUCB. The experiments support this. The paper is primarily a theory contribution with illustrative experiments.
- **Complaint about γ_t schedule for C-FastCB not defined in main text**: Removed per the hard rule about missing appendix content. The paper references \eqref{eq:gamma-schedule} and describes the episodic structure in Remark 4.2 (lines 305–307); the explicit formula is in the appendix (stripped by parser).
- **Criticism about fixed-action baseline being too easy**: Removed — fixed baselines are standard in the CCB literature, and the paper follows the standard evaluation protocol from prior work (bandit_bake).
- **"Strengthening the Paper on Its Own Terms" suggestions**: Moved to Nice-to-Haves where appropriate. These are recommendations, not weaknesses of the current submission.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add at least one experiment showing the effect of varying α on the regret/constraint-violation tradeoff.
- Report the empirical number of baseline rounds (n_T) for each dataset to connect the theory to the experiments.
- Include a brief discussion of how the safety condition quantities (reg_sq, reg_kl) would be set in practice (e.g., using known bounds from the neural regression analysis).
- Add error bars or confidence bands to the regret curves.
- Explain the structural asymmetry between the two safety conditions and the difference in guarantee type (high-probability vs. expectation).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>