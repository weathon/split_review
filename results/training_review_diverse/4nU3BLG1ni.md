Now I have a complete picture. Let me synthesize my findings into a consolidated review by verifying each claim against the actual paper text.

---

## Summary

This paper introduces DDSE, the first algorithm for decentralized multi-player multi-armed bandits (MMAB) with stochastic delayed feedback — a realistic but previously unexplored setting. The key algorithmic idea is a leader-follower structure with periodic communication phases that use an intentionally outdated consensus set (\(\mathcal{M}_{p-q}\)) to avoid collisions when players receive feedback at different times. The paper provides regret upper bounds for DDSE (Theorem 2), a lower bound for the centralized setting (Theorem 1), and an analysis of a no-delay-estimation ablation (Theorem 3) showing that ignoring delay leads to an exponential regret penalty. Experiments on synthetic and real-world spectrum data compare DDSE against six existing MMAB algorithms and the ablation.

## Strengths

1. **Novel problem formulation addressing a genuine gap.** The paper correctly identifies that all existing decentralized MMAB algorithms assume immediate feedback, which does not match practical cognitive radio networks where spectrum sensing and transmission introduce delays (Section 1). Formalizing stochastic delayed feedback in the decentralized MMAB setting is a meaningful contribution that opens a new research direction.

2. **Clever algorithmic mechanism with theoretical justification.** The core idea — using the most recent *fully-received* consensus set \(\mathcal{M}_{p-q}\) rather than the latest \(\mathcal{M}_{p}\) to maintain synchronization — is simple yet effective. The theoretical analysis (Theorem 2 vs. Theorem 3) rigorously demonstrates that this avoids an exponential regret term \(\exp(\mathbb{E}[d]/(KM) + \sigma_d^2/(2K^2M^2))\) that arises from naive delay-oblivious updating. This contrast cleanly justifies the algorithm's core design choice.

3. **Rigorous theoretical analysis.** The paper provides both regret upper bounds (decentralized) and a lower bound (centralized), showing the upper bound matches the lower bound up to constant and additive terms that are independent of \(T\). Lemma 1 and Lemma 2 decompose the regret into exploration and communication phases, with the communication-phase regret shown to be constant in \(T\). Theorem 3's analysis of the ablation provides strong evidence that the delay-adaptive mechanism is essential.

4. **Experimental validation on both synthetic and real-world data.** The paper evaluates DDSE across varying delay expectations, delay variances, and numbers of players (Figures 1-2), and on real spectrum measurement data (Figures 4-5), comparing against six baselines plus the ablation. The consistent performance advantage and the ablation comparison provide evidence that the algorithmic innovations translate to practice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Underspecified delay estimation procedure.** The paper mentions that the full DDSE estimates \(\hat{\mu}_d^j\) and \((\hat{\sigma}_d^2)^j\) (line 146 contrasts the ablation "does not estimate" these), and the bounds depend on \(\mathbb{E}[d]\) and \(\sigma_d^2\), but the text never explicitly describes how players compute these estimates from observed delays. While a standard sample-mean and sample-variance approach would suffice, the absence of any specification is a gap for reproducibility. (The algorithm pseudocode — "Algorithm 1" — is referenced but was stripped by the parser; if it contains these details, this point is moot; if not, it remains a gap.)

2. **"Near-optimal" claim resting on a centralized lower bound.** Theorem 1 provides a lower bound for the *centralized* setting, while Theorem 2 is a regret upper bound for the *decentralized* setting. The paper acknowledges this (line 157: "we compare our results with the centralized lower bound to evaluate how the additional information exchange impacts regret reduction") and shows the gap is constant in \(T\). This is a standard and defensible approach. However, the claim of "near-optimality" would be stronger if accompanied by a lower bound for the decentralized setting itself, or at least a discussion of whether the extra \(O\big(\frac{M\sum_{k>M}\Delta_k}{K-M}\sqrt{\sigma_d^2\log K}\big)\) term is unavoidable.

3. **Baselines used without discussion of delay impact.** The experiments evaluate six existing MMAB algorithms (SIC-MMAB, MCTopM, etc.) without any modification for delayed feedback, and the paper states "Parameters are set the same with the original works" (line 223). This is a valid and informative comparison for showing that *naive application* of existing algorithms fails under delay. However, the paper would be strengthened by briefly discussing *why* unmodified use is a reasonable comparison (i.e., these algorithms have no built-in mechanism to handle delay, so the experiment tests exactly what happens when they encounter delays). Without this discussion, the comparison's interpretation is left implicit.

4. **Large constants and minimum-gap dependence in bounds.** The regret upper bound (Theorem 2) involves large constants (323, 195) and a term \(C_1 = 4M e^{-\delta^2/2}/\delta^2\) that depends on the minimum gap \(\delta\) and can blow up for small \(\delta\). The paper does not discuss whether these constants are artifacts of the analysis or inherent, nor does it address the \(\delta\) dependence. A brief discussion would help readers assess the tightness.

### Trivial
- Table 1 defines \(\tilde{d}_1, \tilde{d}_2, \tilde{d}_3\) but the prose explains their role in the bounds only briefly (line 18-19, 35-37). Adding a sentence clarifying which terms they appear in would help readability.
- The communication phase is described in prose with three parts (lines 136-140); providing a compact summary of the three-part structure in pseudocode form would aid comprehension.

## Nice-to-Haves

- **Adapted baselines:** The paper could strengthen the empirical evaluation by adapting one or two baselines to handle delay (e.g., inserting a waiting period after each pull until feedback arrives) and showing that even adapted versions still underperform DDSE. This would address a natural reader question: "Could existing algorithms be trivially fixed?"
- **Guidance on choosing \(\theta\):** The quantile parameter \(\theta\) appears in the bounds and the algorithm (via the quantile function \(d(\theta)\)), but no practical guidance is given for setting it. A brief discussion relating \(\theta\) to the trade-off between regret and confidence would be useful.
- **Experiments with non-Gaussian / heavy-tailed delays:** The paper uses Gaussian rewards and sub-Gaussian synthetic delays. Testing with heavy-tailed delay distributions (e.g., log-normal) would probe the robustness of the sub-Gaussian assumption.

## Removed Points

The following points from the reviews were removed or downgraded after verification against the paper:

- **"Unfair and invalid baseline comparisons render experimental evaluation uninformative"** (Critic's Point 1): The paper compares existing algorithms unmodified in a new setting for which they were not designed. This is a standard and informative comparison — it demonstrates exactly what the paper claims: that existing algorithms fail under delay. The critic's claim that this is "fatal" and "invalid" is overblown. The comparison is legitimate; the paper could add a brief justification, but the experiments are not uninformative. Moved to Minor weakness #3 above.

- **"Algorithm description incomplete" — sub-points about missing Algorithm 1 pseudocode and common clock synchronization**: The paper references "Algorithm 1" (line 127), which was likely stripped by the PDF parser. Per the hard rules, parser-stripped content is assumed to exist. The assumption of a shared time index is standard in the MMAB literature and stated in the paper (players know their rank and total count, line 127). These are parser artifacts or standard assumptions, not author errors.

- **"How players determine q in a decentralized way"**: The paper explains that \(q\) is determined by finding the most recent communication phase whose feedback has been fully received (line 146: "Denote \(p'\) as the communication phase whose result is the most recent to have been completely received"). This is a clear and sensible description for a decentralized setting where each player locally tracks received feedback.

- **Strength Finder's "rigorous experimental validation"**: The description is kept but reframed more carefully to note the baseline issue. The core claim that experiments validate DDSE's effectiveness is accurate.

- **Strength Finder's "near-optimal theoretical guarantees with lower bound"**: Kept but qualified to note the centralized vs. decentralized caveat, which appears in Minor weakness #2.

## Novel Insights

The reviewer feedback surfaces an interesting tension that the paper does not fully address: the cost of decentralization under delay manifests both as explicit communication-phase regret (constant in \(T\)) and as an implicit constraint that forces players to use stale information (\(\mathcal{M}_{p-q}\) instead of \(\mathcal{M}_p\)). The paper's central trade-off is that using older information avoids collisions but slows reaction to changing best-arm estimates. The ablation analysis (Theorem 3) convincingly shows the exponential penalty of using *too recent* information, but the paper does not explore whether there exists a *sweet spot* — i.e., an optimal \(q\) that balances staleness against collision risk. This could be a fruitful direction for follow-up work.

## Suggestions

1. Add a brief description of how players empirically estimate \(\mathbb{E}[d]\) and \(\sigma_d^2\) from observed delays (e.g., via running sample mean and variance). This fills the main reproducibility gap.
2. Add a short paragraph qualifying the "near-optimal" comparison: clarify that the gap relative to the centralized lower bound includes an unavoidable cost of decentralization, and note whether the extra \(O(\sqrt{\sigma_d^2 \log K})\) term is conjectured to be necessary.
3. Add one sentence explaining *why* unmodified baselines are a reasonable comparison: "These algorithms have no mechanism to handle delay, so the experiment shows what happens when they encounter it without modification."
4. Discuss the large constants (323, 195) and the \(\delta\) dependence in \(C_1\) — even a brief note about whether these are artifacts of the proof technique would help.
5. Provide a compact pseudocode or table summarizing the communication phase steps (remove, add, notify) for quick reference.

## Score and Decision

The paper addresses a meaningful and underexplored problem with a well-motivated algorithm and solid theoretical analysis. The weaknesses are minor and addressable: no structural flaws or fatal methodological gaps exist. The core contributions (problem formulation, algorithmic mechanism with provable guarantees, and experimental validation) are solid. The paper merits acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>