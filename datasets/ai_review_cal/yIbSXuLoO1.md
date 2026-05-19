- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have all the information I need to produce a thorough, verified final review. Let me construct it.

## Summary

This paper introduces Set-Size Dependent Combinatorial Multi-Armed Bandits (SSD-CMAB), a variant where each base arm has up to \(L\) reward distributions depending on the size of the super arm it belongs to. The key structural property — order preservation (the ranking of base arms is consistent across super-arm sizes) — is leveraged by the proposed SortUCB algorithm, which operates in three phases: Elimination (remove the \(M-L\) worst arms), Sorting (rank the top \(L\) arms), and UCB (exploit the reduced candidate set). Theoretical upper and lower bounds are provided, and experiments on small synthetic instances show competitive performance.

---

## Strengths

1. **Novel problem formulation.** SSD-CMAB (Section 2) is a clean, well-motivated extension of CMAB that captures a genuine real-world phenomenon (reward dependence on super-arm size with order preservation). The paper correctly identifies that this structure is underexplored relative to submodularity-based set dependence.

2. **Algorithm design that exploits the structure.** SortUCB (Section 3) uses the order preservation property to collapse the exponential super-arm space to just \(L\) candidates (\(O(M\log M)\) per time slot, line 81). This is the paper's main algorithmic contribution and is non-trivial.

3. **Theoretical guarantees with both upper and lower bounds.** Theorem 1 bounds regret by \(O(\max\{M\delta_{L,\max}/\Delta_{L,\min}^2,\; L^2/\Delta_{S,\min}\}\log T)\). The second term \(O(L^2/\Delta_{S,\min}\log T)\) replaces the \(O(ML^2/\Delta_{S,\min}\log T)\) that a black-box CMAB reduction would incur, removing the \(M\) factor from that term. Theorem 2 provides a complementary instance-dependent lower bound.

4. **Empirical validation of the scaling advantage.** Experiment 4 (Figure 1d, \(M=8\), \(L\) from 3 to 8) directly confirms the theory: SortUCB's regret stays nearly flat as \(L\) increases, while CombUCB1 and MPMAB‑s grow rapidly. Experiments 1–3 provide consistent supporting evidence across different gap structures.

---

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguous sampling strategy in the Elimination Phase.** The paper states (line 55): "uniformly pulling super arms with the largest number of base arms (i.e., super arms of size \(L\))" but does not specify *which* super arms of size \(L\) are pulled, nor how the pulls guarantee that every base arm receives enough samples under distribution \(P_{i(L)}\). The analysis in Lemma 1 requires comparable pull counts across arms, but without a concrete selection rule this cannot be verified from the description. The experiments (\(M=L=8\) in Experiment 1, where only one super arm of size 8 exists) sidestep the issue. This is a clarity gap in a methods paper that should be resolved with a precise rule (e.g., pull a uniformly random size-\(L\) subset of the current candidate set \(\mathcal{B}\)) and a justification that it yields the needed coverage. The flaw is **not fatal** — a reasonable implementation exists and the core idea is clear — but it must be fixed for reproducibility.

### Minor

2. **Informal comparison with the CMAB baseline bound.** Remark 2 claims improvement from \(O(ML^2/\Delta_{S,\min}\log T)\) to \(O(M+L^2)\) factors by citing Kveton et al. (2015). Two caveats: (i) the first term' s denominator \(\Delta_{L,\min}^2\) can be arbitrarily small — the paper's rejoinder (line 101) that "in most real-life cases \(\Delta_{L,\min}\) is not that small as \(\Delta_{S,\min}\)" is an empirical assertion, not a theoretical guarantee; (ii) the cited CMAB bound lacks a square on \(\Delta_{S,\min}\), which differs from some standard formulations (e.g., CombUCB1 often yields \(O(ML\log T/\Delta^2)\)). These points weaken the quantitative superiority claim, though the structural improvement in the \(M\) vs. \(L\) dependence remains valid.

3. **Lower bound only partially matches the upper bound.** The paper's own Remark 4 concedes that the first terms align only when the minimum over \(\ell\in[L]\) "consistently falls on \(L\)" and \(\ell^*\) is not near \(M\). This is a narrow condition, and no argument is given that it is typical. The "partially tight" characterization is accurate but the gap is larger than the framing suggests.

4. **SD-CMAB extension (Section 5) is underdeveloped.** The section spans only 15 lines of text plus a theorem statement. The term "\((\alpha_h,\beta_h)\)-efficient" in Remark 5 is used but never formally defined in the extracted text. No algorithm pseudocode, proof sketch, or experiments are provided. This feels like a preliminary sketch rather than a substantive contribution.

5. **Limited experimental scope.** Only two baselines (CombUCB1 and MPMAB‑s) are compared. The main experiment uses \(M=L=8\) — small-scale. No ablation isolating the benefit of the Sorting Phase (e.g., comparing SortUCB against UCB directly on the size-\(L\) candidate set without sorting) is included. Standard deviations are shown as shaded regions but no statistical tests are reported.

### Trivial
- The abstract's informal lower bound notation \(\min_{k\in[L]}\{(M-L)\delta_k/\Delta_k^2\}\) differs from the formal statement in Theorem 2, though this is not unusual for an abstract-level summary.

---

## Nice-to-Haves
- Include a "UCB-on-\(L\)-candidates" baseline that skips the sorting step but directly applies UCB to the \(L\) size-optimal super arms, to isolate the value of the order-learning phases.
- Provide a worst-case example (e.g., \(\Delta_{L,\min}\) very small) and discuss when the bound may not improve over the black-box CMAB reduction.
- Add error bars or confidence intervals to experiments.

---

## Removed Points
- **"The algorithm is not fully specified / irreproducible" treated as Fatal** — The text gives sufficient information to implement a reasonable version (pull random size-\(L\) subsets from the candidate set). The ambiguity is real but the paper is not "broken." Demoted to Major.
- **"No code is provided"** — Removed per rules (reproducibility nitpick about large artifacts).
- **"Missing related works / baselines"** about specific papers — Removed; the reviewer cannot confirm which works exist or whether they are substantively relevant.
- **"The proof sketch is too high level"** — For a 7-page paper, proof sketches are appropriate. Softened; the only concrete gap (Lemma 1's dependency on the unspecified sampling rule) is already covered in the Major weakness.
- **"Notation mismatch in abstract"** — This is an informal abstract-level summary, standard practice. Removed.
- **"Worst-case discussion missing"** — The paper acknowledges the \(\Delta_{L,\min}\) issue in Remark 2. Removed as already addressed.
- **Pure formatting/style nitpicks and typos** (parser artifacts) — Removed.
- **Strength Finder's generic strengths** ("important problem," "interesting question") — Removed as superficial/unsupported.
- **Strength Finder's "Extension to SD-CMAB" strength** — Conflicts with verified weakness #4 that the extension is underdeveloped. Weakness wins; removed from strengths.

---

## Novel Insights
None beyond the paper's own contributions.

---

## Suggestions
1. **Precisely specify the sampling rule in the Elimination Phase.** State that at each time step, the algorithm draws a uniformly random subset of size \(L\) from the current candidate set \(\mathcal{B}\), and explain why this ensures each arm receives comparable samples under \(P_{i(L)}\) (by standard concentration with semi-bandit feedback).
2. **Provide the pseudocode for Algorithm 1** in the main text (currently an image that may not render). This single change would resolve most of the ambiguity concerns.
3. **Tighten the bound comparison.** Explicitly state the gap definitions used in the CMAB baseline bound to clarify the comparison, and discuss regimes where \(\Delta_{L,\min}\) could hurt SortUCB's performance relative to the baseline.
4. **Expand the SD-CMAB section** with at least a proof sketch and a concrete example showing the \((\alpha_h,\beta_h)\)-efficiency concept.

---

**Overall Assessment:** The paper introduces a novel, well-motivated CMAB variant and a clever algorithm that exploits order preservation to dramatically reduce the exploration space. The theoretical analysis provides both upper and lower bounds, and experiments confirm the predicted scaling behavior. The main weakness is an ambiguity in the algorithm's sampling strategy that must be clarified. On balance, the contribution is solid and deserves acceptance after addressing the sampling specificity.
