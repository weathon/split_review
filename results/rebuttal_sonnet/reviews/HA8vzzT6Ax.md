## Summary

The paper introduces a quantitative, KL-divergence-based measure of watermark strength (WS = I(w; ζ)) and shows it governs p-value decay rates (Theorem 3.1), is maximized when tokens are deterministic functions of pseudorandom numbers (Theorem 3.2), and is achieved by both Gumbel-max and asymptotic SynthID (Theorem 3.3). The paper casts the watermark strength vs. speculative sampling efficiency trade-off as a constrained optimization (Definition 3.2), derives explicit Pareto curves, and proposes Algorithm 1 — pseudorandom draft-token acceptance — proven to simultaneously achieve maximum WS and maximum speculative sampling efficiency (Theorem 4.1), constructively overturning the prior binary impossibility of Hu & Huang (2024).

---

## Rebuttal Assessment

---

**Weakness:** Pareto curves derived for a single simulated (Q, P) pair
**Author's response:** Partially address
**Assessment:** Partially convincing — The author makes a legitimate theoretical argument that the *dominance ordering* at the endpoints is theory-grounded. Theorem 3.3 guarantees that Google's endpoints achieve WS = Ent(P) for *any* P, and the kernel structure in Appendix C.2 provides basis for the intermediate comparison. However, the author explicitly concedes that "these quantitative gaps do depend on the chosen pair," and the critical claim in the paper — "Google's class achieves higher watermark strength than Hu's at *matched sampling efficiency*" — is about the intermediate curve shape, not the endpoints. This intermediate-efficiency dominance claim is supported only for the simulated pair. Section 3.2 remains explicit: "we plot the trade-off curves for simulated Q and P." The rebuttal doesn't add new data and offers "future work" for validation on Llama/Gemma pairs already used in Section 5.
**Score impact:** Weakness downgraded (from major to minor) — The theoretical grounding for endpoint ranking is legitimate, but the intermediate curve ordering is genuinely illustration-only.

---

**Weakness:** Conservative temperature choices with unexplained scope
**Author's response:** Partially address
**Assessment:** Partially convincing, but incomplete — The author correctly notes that Theorem 4.1 is temperature-agnostic; the three properties (unbiasedness, max SSE, max WS) hold for any P and Q regardless of temperature parameterization, and this is straightforwardly verified from the theorem's proof structure. However, the author explicitly acknowledges: "Whether the relative gap between Ars-τ and Ars-Prior shrinks at temperature 1.0 is an open empirical question that we cannot answer from the data reported in the paper." Section 5 states temperatures of 0.5 (Gumbel-max) and 0.7 (SynthID) to "make results more pronounced." The paper claims "practical deployment" but tests only at sub-unity temperatures. The detection improvement in Figure 2 — the main empirical result — is unvalidated at deployment temperatures.
**Score impact:** Weakness unchanged — Honest acknowledgment of the empirical gap; the paper does not contain the missing temperature data.

---

**Weakness:** Theoretical bridge from WS maximization to detection improvement is incomplete
**Author's response:** Acknowledge
**Assessment:** Unconvincing as a rebuttal — The author confirms the gap: Section 4.2 explicitly states "this does not guarantee optimal detection efficiency" (verified in paper), and the mechanism is described only informally in Section 4.2 without a formal proposition. The empirical evidence supports the practical claim but the formal link from WS to detection efficiency is absent. Honest acknowledgment does not remove the weakness.
**Score impact:** Weakness unchanged (minor).

---

**Weakness:** Sensitivity of τ calibration in Ars-τ not characterized
**Author's response:** Acknowledge
**Assessment:** Honest acknowledgment — Section 5 confirms 1,000 training samples are used and no sensitivity analysis is reported. Acknowledged but not addressed.
**Score impact:** Weakness unchanged (minor).

---

## Strengths

- **Quantitative WS measure with statistical grounding.** Definition 3.1 defines WS(P_ζ) = E_ζ[D_KL(P_ζ ∥ P)] = I(w; ζ). Theorem 3.1 proves this governs the p-value decay rate under the UMP test, directly linking the measure to sample complexity.
- **Elegant characterization of maximal strength.** Theorem 3.2 shows WS ≤ Ent(P) with equality iff P_ζ is degenerate. Theorem 3.3 confirms Gumbel-max and SynthID (m→∞) achieve this maximum — non-trivial, informative results.
- **Pareto frontier formulation with clean decoupling.** Lemma 3.1 proves speculative sampling is the optimal kernel, allowing the constrained problem (Definition 3.2/Eq. 10) to be decoupled cleanly. The derivation is correct and elegant.
- **Provably optimal Algorithm 1.** Theorem 4.1 simultaneously proves unbiasedness, SSE = 1 − TV(Q, P), and WS = Ent(P), constructively overturning the prior impossibility under the new quantitative measure. Three-component decomposition (ζ^D, ζ^T, ζ^R) is natural and well-motivated.
- **Empirical validation.** Figure 2 confirms AATPS under Algorithm 1 matches standard speculative sampling (K ∈ {2, 3, 4}), and Ars-τ/Bayes-MLP improve TPR@FPR=1% over prior-based methods and approach oracle performance near 200 tokens. LogPPL confirms output quality is preserved.
- **Two model pairs.** Results on Llama-68M/7B and Gemma-2B/7B pairs across two datasets (EL15 for QA, C4 for open-ended generation) provide reasonable empirical breadth.

---

## Weaknesses

### Fatal
None.

### Major
None — the previously major Pareto curve weakness is downgraded given the author's legitimate theoretical argument that endpoint dominance is theory-grounded.

### Minor

- **Pareto curves: intermediate-efficiency ordering illustrated for one simulated pair.** The dominance of Google's class over Hu's class *at the endpoints* is theory-grounded (Theorem 3.3, Appendix C.2). However, the claim that Google's class dominates at *matched intermediate efficiency* — the central comparative message of Figure 1 right panel — is supported only for one simulated (Q, P) pair. The author concedes quantitative gaps depend on the pair and defers validation on the Llama/Gemma pairs (already available in Section 5) to future work. This is a meaningful but not fatal evidential gap.

- **Conservative temperatures not validated at deployment settings.** Theorem 4.1 is temperature-agnostic (theory holds), but the detection improvement in Figure 2 is demonstrated only at temperatures 0.5 (Gumbel-max) and 0.7 (SynthID). The paper explicitly says these were chosen to "make results more pronounced." Whether Ars-τ maintains its advantage over Ars-Prior at temperature 1.0 is unverified. For a paper claiming "practical deployment," this is a meaningful empirical gap.

- **Informal WS-to-detection bridge.** The mechanism by which pseudorandom acceptance improves detection (ζ^R deterministically identifies the source model, eliminating signal averaging) is described informally in Section 4.2 and is not cast as a formal result. Remark 3.1 explicitly separates WS from detection efficiency. The empirical evidence supports the claim, but the theoretical bridge is absent.

- **τ calibration sensitivity not characterized.** Section 5 uses 1,000 validation samples for τ calibration. Degradation with smaller calibration sets is unreported, limiting practical guidance.

### Trivial
None.

---

## Nice-to-Haves

- Show Pareto curves for one real model pair (Llama or Gemma, already used in Section 5) to confirm intermediate-efficiency dominance ordering is robust to (Q, P) choice.
- Add a supplementary figure reporting TPR@FPR=1% at temperature 1.0 for one watermark scheme to address deployment-temperature concern.
- Provide a brief formal proposition connecting the information in ζ^R to a likelihood-ratio improvement (the informal argument in Section 4.2 is already compelling; formalizing it would close the gap between WS theory and detection practice).
- Report τ calibration sensitivity (TPR vs. validation set size) to assist practitioners with limited labeled data.

---

## Novel Insights

The paper's deepest insight is that pseudorandom acceptance — making the acceptance coin a deterministic function of ζ^R — simultaneously satisfies the degenerate-distribution condition required for maximum watermark strength (Theorem 3.2) *and* preserves the marginal acceptance probabilities required for maximum speculative sampling efficiency. This unification principle reveals that what makes speculative sampling maximally efficient (coupling output to a specific token) is structurally identical to what constitutes maximum watermark strength under the KL-divergence definition. The consequent observation that the Hu & Huang impossibility result is an artifact of a binary strength definition — and that a quantitative measure resolves it constructively — is a meaningful conceptual contribution. The secondary insight, that ζ^R encodes source-model identity and enables deterministic test-statistic selection (replacing probabilistic averaging), further bridges the gap between theoretical WS gains and practical detection improvements.

---

## Suggestions

1. Add one Pareto curve figure using the Llama or Gemma model pair from Section 5 to ground the intermediate-efficiency dominance claim empirically.
2. Add a supplementary ablation reporting TPR@FPR=1% at temperature 1.0 to validate the detection improvement under practical deployment conditions.
3. Convert the informal argument in Section 4.2 (ζ^R reduces source-model uncertainty) into a brief formal proposition, even under simplified assumptions, to close the theory-to-detection gap.

---

## Score and Decision

**Rebuttal impact:**

The rebuttal makes one substantive theoretical point: the dominance ordering of Hu's vs. Google's classes at the *endpoints* of the Pareto curve is theory-grounded (Theorems 3.2, 3.3), not purely simulation-dependent. This partially addresses the major Pareto curve weakness, downgrading it from major to minor. However, the intermediate-efficiency comparison — the actual message of Figure 1 right panel — remains validated only for one simulated pair, and the author explicitly acknowledges this. The temperature weakness is honestly acknowledged as an open empirical question. The other two minor weaknesses are acknowledged without resolution.

**Net change:** One major weakness downgraded to minor. Score impact: +0 to +0.5. The paper's core theoretical machinery (Theorems 3.1–3.3, Theorem 4.1) remains rigorous and well-supported. The remaining weaknesses are minor and do not undermine the central contribution. Score stays at 7.0.

| Axis | Assessment |
|------|------------|
| Originality | High — quantitative WS measure, Pareto frontier characterization, pseudorandom acceptance principle are all novel |
| Importance | High — resolves a practical barrier to deploying watermarked LLMs at scale |
| Claims well-supported | Mostly yes — core theorem (Thm. 4.1) is rigorously proven; Pareto comparison partially theory-grounded but intermediate shapes illustrated on one pair; detection improvement at standard temperatures unverified |
| Soundness of experiments | Good but limited by conservative temperatures |
| Clarity | High — well-organized, notation consistent |
| Value to community | Solid — provides an actionable algorithm and principled framework |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>