## Summary

R2PS introduces the first framework for worst-case robust, real-time pursuit strategies in graph-based pursuit-evasion games (PEGs) under partial observability. The paper (1) proves that the existing DP distance-table algorithm yields strictly optimal strategies even when the evader moves asynchronously (observing the pursuers' chosen action before acting), (2) proposes a belief preservation mechanism that efficiently summarizes observation history into a compact evader-position distribution, and (3) embeds belief preservation into the EPG cross-graph RL framework, yielding a GNN pursuer that zero-shot generalizes to unseen real-world graphs and consistently outperforms PSRO policies trained directly on those same graphs.

---

## Strengths

- **Rigorous asynchronous-move optimality (Theorem 2, Corollary 1, Lemma 1):** The paper proves that the DP distance table D constructed by Algorithm 1 remains strictly optimal for both pursuer policy (1) and asynchronous evader policy (3). Lemma 1 establishes the minimax property of D; Theorem 2 shows pursuer guarantees capture within d steps and evader avoids capture in fewer than d steps from any state with D(s)=d. This is a non-trivial and clean theoretical result that underpins the whole framework.

- **Effective belief preservation mechanism (Equations 4–7, Lemma 2, Table 1):** The belief update is O(|V|) per timestep and Lemma 2 formally guarantees that it reduces to the perfect-information policy when Pos is a singleton. Table 1 empirically shows DP_belief achieves 0.36–0.94 against the optimal asynchronous evader at observation range 2, consistently beating DP_Pos (0.24–0.73) and the shortest-path baseline (0.00–0.29) across all 10 test graphs.

- **Zero-shot generalization to unseen real-world graphs (Table 2):** The RL pursuer, trained on 300 synthetic and urban graphs without ever seeing the 10 test graphs, consistently outperforms PSRO trained directly on those same test graphs against all four evader strategies. The advantage is especially pronounced against DPasync: R2PS reaches 0.76–1.00 on Scotland-Yard, Downtown, and Big Ben while PSRO obtains 0.00–0.24.

- **Demonstrated real-time inference advantage (Table 3):** The GNN policy achieves inference in under 0.01 s on GPU for graphs with up to 2065 nodes, versus 33–139 s for DP recomputation. The O(n²m) inference complexity vs. Õ(n^{m+1}) for DP is derived formally in Section 4.2, and Table 3 validates this at scale.

- **Belief update ablation (Table 4):** Reducing belief update frequency from every step to every 2 or 3 steps sharply reduces success rates (e.g., Scotland-Yard drops from 0.73 → 0.34 → 0.28), and using true opponent information improves rates (Scotland-Yard 0.73 → 0.99). This concretely demonstrates that the belief mechanism is both functional and beneficial.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation isolating the belief mechanism in the RL setting.** Table 4 shows belief update frequency matters, but the paper does not compare the cross-graph RL policy trained (a) without any partial-observability handling (feeding only currently observed positions), (b) with Pos-based guidance (DP_Pos as reference, Equation 5), and (c) with the full belief mechanism (DP_belief, Equation 6). In other words, while the DP experiments in Table 1 establish DPbelief > DPPos, there is no ablation establishing that the *RL* version of "with belief" beats "without belief." Because belief preservation is the paper's most novel algorithmic contribution, the absence of this three-way ablation in the RL setting leaves the source of generalization gains ambiguous: the gain could come from the cross-graph adversarial curriculum, the belief encoding, or both. This is the single most important missing experiment.

### Minor

- **"Worst-case robust" framing is partially overstated relative to results.** Against BRasync (the best-responding evader trained on the test graphs), success rates are 0.10 (Hollywood), 0.20 (Sagrada Familia), 0.23 (The Bund), and 0.27 (Times Square) — Table 2. The paper frames this as "over 50% in half of the graphs," which is technically true but paints an incomplete picture. For a paper explicitly motivated by real-world security applications, these rates warrant a more measured discussion of when the system is and is not operationally adequate, and why certain graphs (long-diameter, sparse graphs like Hollywood) consistently yield low performance. The paper notes graph topology as a factor but provides no analysis.

- **Performance degradation on larger graphs not analyzed.** Table 3 (large-scale graphs, 744–2065 nodes) shows Times Square drops from 0.95 (Table 2, 171 nodes) to 0.56, and Hollywood from 0.38 to 0.46 (slight improvement here, but Times Square is clearly worse). The paper notes "desirable overall performance" without investigating whether degradation is caused by graph scale, topology changes from finer discretization, or both. For the paper's claim of "real-time applicability to dynamically changing large-scale scenarios," this gap is worth acknowledging.

- **Informal "exponential level" claim in Section 4.1.** The paragraph states "the cross-graph policy will be improved at an exponential level across a diverse training corpus." This is an informal intuitive argument by analogy to half-space exclusion in policy space, and is neither formalized nor empirically substantiated. It should be qualified explicitly as intuition or removed.

### Trivial

- **No variance reported on success rates.** Table 2 and Table 3 present only point estimates over 500 runs. For cases like Sagrada Familia DPasync (0.20 Ours vs. 0.00 PSRO) and Hollywood BRasync (0.10), reporting standard errors would strengthen the empirical claims at no cost.

---

## Nice-to-Haves

- An analysis correlating per-graph success rates against simple structural properties (diameter, average degree, cyclomatic number) would sharpen the paper's understanding of when the method is expected to work well and turn the empirical section from a performance listing into a mechanistic analysis.
- An experiment testing with m=3 pursuers would complement the existing m=2 results, especially given the paper's own citation of the result that 3 pursuers suffice to capture on any planar graph (Fromme & Aigner, 1984). Even a brief test would show whether the approach scales across pursuer counts.
- A brief characterization of the intermediate observation-range regime (range 2–5) on harder graphs like Hollywood and Sagrada Familia, as Table 6 (Appendix) is noted in the text but is not discussed in depth in the main paper.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[PSRO is a structurally mismatched baseline]** The harsh critic argues the PSRO comparison is unfair because PSRO is not a generalization method. However, the paper's design is intentionally asymmetric: if even a specialist trained directly on the test graphs fails to match a zero-shot generalizing policy, this is a stronger demonstration of generalization quality. The paper explicitly states this comparison as evidence for zero-shot robustness, not as a head-to-head equilibrium quality comparison. The asymmetry favors the baseline (PSRO trains on test graphs; R2PS does not), so this is the correct experimental design for the claim being made. REMOVED per the hard rule on asymmetric comparisons that favor the baseline.

- **[Asynchronous-move assumption is too strong or poorly justified]** The harsh critic calls the justification "informal." Section 2.1 explicitly frames the asynchronous setting as a worst-case for security purposes and the theoretical results are rigorous. The informal motivation ("the worst evader may have good predictions") is an intuition for why the model is relevant, not a claim requiring formal proof. REMOVED as a non-substantive critique of model motivation rather than method correctness.

- **[Success rates are low in absolute terms for security applications]** While the low numbers on some graphs are acknowledged as a Minor weakness above in the context of the paper's framing, the broader criticism that any sub-100% rate is operationally unacceptable is a scope-creep criticism imposing standards the paper does not claim to meet. The paper provides a relative improvement claim, not a guaranteed-capture claim. PARTIALLY REMOVED; the framing concern is retained as Minor.

- **[No variance/CI for all tables]** The absence of error bars is noted as Trivial above. Elevated to a potential methodological concern by the harsh critic, but given 500-run averaging and the magnitude of most differences (e.g., 0.76 vs. 0.00), this does not threaten the core claims. Retained as Trivial only.

---

## Novel Insights

The most genuinely novel finding is that a single DP distance table D computed under synchronous-move dynamics serves as a unifying oracle: it induces strictly optimal strategies under both synchronous and asynchronous evader moves (Theorem 2), generalizes gracefully to partial observability through belief averaging (Lemma 2, Table 1), and provides an effective policy guide for cross-graph RL via Equation 8. This reuse of a single precomputed table across three distinct settings — perfect information synchronous, perfect information asynchronous, and partial observability — is the paper's most elegant structural insight, and it substantially reduces the engineering complexity of extending PEG solutions to realistic settings.

---

## Suggestions

1. **Add the critical RL ablation (most important):** Run the cross-graph RL pipeline in three conditions: (a) no partial-observability handling (observed positions only as input), (b) DP_Pos as reference policy with Pos-extended state, (c) full belief mechanism as in R2PS. This would directly attribute the generalization gains to the belief mechanism, which is the paper's core algorithmic contribution.

2. **Moderate the "worst-case robust" language for low-performance graphs:** Acknowledge explicitly in Section 5.2 (or the conclusion) that Hollywood Walk of Fame, Sagrada Familia, and The Bund represent graphs where the current approach has limited practical capture rates, and identify graph-structural correlates (diameter appears to be a key predictor, e.g., Hollywood: diameter 31, Sagrada Familia: diameter 25 vs. Grid Map: diameter 18).

3. **Remove or caveat the "exponential level" claim** in Section 4.1 paragraph 3, or present it explicitly as intuition rather than a methodological claim.

4. **Add standard errors** to Table 2 and Table 3 at minimum for the closest and most surprising results.

---

## Evaluation on Key Axes

- **Originality:** High. The extension of DP optimality to asynchronous moves, and the belief preservation mechanism for partial observability in cross-graph PEG RL, are genuinely new. The integration with EPG is well-motivated rather than superficial.
- **Importance of research question:** Solid. Pursuit-evasion under partial observability with real-time constraints is practically relevant and theoretically interesting.
- **Claims well-supported:** Mostly, with one notable gap: the key RL-level contribution (belief mechanism) lacks a direct ablation in the RL setting. The theoretical claims and DP-level claims are fully supported.
- **Soundness of experiments:** Good. The evaluation covers 10 real-world graphs, 4 evader strategies, both small and large-scale graphs, and includes an ablation on belief update conditions. The main gap is the missing no-belief RL baseline.
- **Clarity of writing:** Good overall. Section 4.1 has one informal speculative paragraph that should be revised.
- **Value to research community:** Good. This is the first partial-observability extension of the EPG framework, with principled theoretical foundations and practical results. It opens a clear line of follow-on work.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>