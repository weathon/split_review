Now I have a thorough understanding of the paper. Let me verify the critic's specific technical claims against the actual paper content.

**Verifying Claim 3 (σ_y histograms vs. Theorem 2):** The critic claims σ_y < 1 for all y does not guarantee inequality (12). But inequality (12) is:
∑ σ_y · P[V ≤ Q^{class}_{1-α}(y)] ≤ ∑ P[V ≤ Q^{class}_{1-α}(y)]

Since σ_y ≥ 0 (both numerator and denominator are probabilities), σ_y < 1 for each y implies σ_y · P[V ≤ Q^{class}_{1-α}(y)] < P[V ≤ Q^{class}_{1-α}(y)] term-by-term, so summing preserves the inequality. The critic is factually wrong. **REMOVED.**

**Verifying Claim 1 (theory-practice disconnect):** Section 4.1 says "k-CCP uses different inflated coverage for each class c: 1-α̃_c > 1-α." Section 5.1 says "uniformly add g/√n to inflate the nominated coverage 1-α to each baseline." The score threshold inflation is described globally, not class-specifically. Equation (11) for k̂(y) uses α - g/√n_y (class-specific n_y) for the rank threshold. There is a genuine ambiguity about how α̃_y is set in practice. **KEPT — major.**

**Verifying Claim 2 (non-constructive Theorem 1):** Theorem 1 depends on ε_y (population top-k error) which is unknown. Equation (11) provides an empirical procedure for k̂(y) but doesn't explicitly connect back to Theorem 1's condition. The paper does not explain δ selection or show how the empirical procedure instantiates the sufficient condition. **KEPT — major.**

---

## Summary

This paper proposes k-CCP, a conformal prediction method that achieves class-conditional coverage and smaller prediction sets on imbalanced data by calibrating both a conformity score threshold and a label-rank threshold per class (double-calibration). The paper provides theoretical analysis (Theorems 1-2) and experiments on four benchmark datasets showing 30-50% reduction in average prediction set size over CCP while maintaining coverage.

## Strengths

- **Novel and well-motivated double-calibration design.** The key idea — restricting candidate labels by both an inflated score threshold and a calibrated rank threshold per class (Equation 9) — is principled and transparently reduces to CCP when k̂(y)=C. This addresses a genuine limitation of existing class-conditional CP methods that produce large prediction sets on imbalanced data.

- **Consistent and substantial empirical gains.** Table 1 shows k-CCP reduces APSS by 30-50% over CCP across four datasets, two imbalance ratios, three imbalance types, and two scoring functions (e.g., mini-ImageNet ρ=0.1 EXP: 1.42 vs 2.51 for CCP). The UCR is controlled to the same or smaller value, confirming size reduction does not come at the cost of coverage.

- **Theorem 1 establishes a class-conditional coverage guarantee.** The theorem identifies a sufficient condition (inflation bounded by ε_{n_y}+δ+ε_y) under which k-CCP provably achieves class-conditional coverage, providing theoretical grounding for the method.

- **Theorem 2 gives a conditional guarantee of smaller prediction sets.** The σ_y quantity cleanly captures the trade-off between inflated score threshold and rank restriction. The experimental verification that σ_y < 1 on real datasets (Figure 1, last column) demonstrates the practical relevance of the condition (as I verify below, σ_y < 1 for all y is sufficient for inequality (12)).

## Weaknesses

### Fatal
None.

### Major

- **Disconnect between the theoretical prescription (class-specific inflation) and the experimental procedure (global inflation tuning).** Theorem 1 and Remark 2 prescribe a class-specific inflation α̃_y satisfying α̃_y ≤ α − ε_{n_y} − δ − ε_y, where ε_{n_y} depends on the per-class calibration size n_y. However, the experimental evaluation (Section 5.1) states: "we uniformly add g/√n to inflate the nominated coverage 1−α to each baseline, and tune g on validation." This uses a single global inflation g/√n (with total n, not class-specific n_y) applied uniformly to all methods including k-CCP. The paper does not explain how this global tuning procedure instantiates — or is even related to — the class-specific condition in Theorem 1. The rank threshold in Equation (11) does use class-specific √n_y, which adds to the confusion about which quantities are class-specific vs. global. This gap between what the theory promises and what the experiments actually implement substantially weakens the claim of a "provable" guarantee for the method as evaluated. The authors should either (a) derive a guarantee that applies to their actual tuning procedure, or (b) implement the class-specific inflation from Theorem 1 and verify that coverage still holds.

- **Theorem 1 is stated in terms of quantities that are not instantiable from finite calibration data.** The condition α̃_y ≤ α − ε_{n_y} − δ − ε_y depends on ε_y (the population-level top-k error) and a free parameter δ with no guidance on selection. The paper provides Equation (11) as a practical way to set k̂(y) using α − g/√n_y, but never explains how this connects to Theorem 1's sufficient condition or how one would verify the inequality holds for the true ε_y. The theoretical result is presented as a guarantee, but it is not shown that the algorithmic procedure (tuning g on validation) produces parameters that satisfy Theorem 1's condition. This decouples the theory from the method that is actually evaluated.

### Minor

- **Ambiguity in how g is used for k-CCP.** The evaluation says g/√n is added to "each baseline" for inflation. For CCP and cluster-CP, this inflation applies to the score threshold. For k-CCP, g also appears in Equation (11) for the rank threshold calibration (with √n_y rather than √n). It is unclear whether k-CCP uses one g for both thresholds, or if the same g controls both the score inflation and the rank calibration. This ambiguity makes reproduction difficult.

- **No ablation isolating the contribution of the two thresholds.** The double-calibration uses both an inflated score threshold and a rank threshold. An ablation (k-CCP with only the rank condition but no score inflation, or with only score inflation but no rank condition) would help attribute the size reduction to the two components. Currently the two mechanisms are coupled.

- **The concentration constant in ε_{n_y} is not derived or justified.** The formula ε_{n_y} = √(3(1−α)log(2/δ)/n_y) appears without explanation of the factor 3(1−α). Since the bound's constants matter for whether the inequality can realistically be satisfied, some justification (or citation) would strengthen the theoretical presentation.

- **Proposition 1's notation is dense and the conditions are not easily interpretable.** The terms (1/n_{y'} + ξ') and the specific form of the inequalities in (7) are presented without intuition or derivation. While the proposition serves as motivation and does not need to be central, clearer exposition would help.

### Trivial
- "hiderline" appears as garbled text in the parser output — likely a formatting artifact, not in the original.
- The reference to "Algorithm 1" is mentioned but its content is missing (parser-stripped, not a paper error).

## Nice-to-Haves
- An explicit step-by-step procedure showing how α̃_y is computed from calibration data for each class, with any free parameters (δ, g) explained.
- An ablation study separating the contribution of the inflated score threshold from the rank threshold.
- Direct computation of both sides of inequality (12) on the test set, rather than only showing σ_y histograms (though as noted, σ_y < 1 for all y is mathematically sufficient for (12)).

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"The σ_y histograms do not verify Theorem 2's condition."** — Factually incorrect. If σ_y < 1 for all y, then σ_y · P[V ≤ Q^{class}_{1-α}(y)] < P[V ≤ Q^{class}_{1-α}(y)] term-by-term, so summing gives inequality (12). The paper's claim that σ_y < 1 is a stronger condition than (12) is mathematically correct. Removed.

2. **Missing related works / "could not cover Y"** — I do not have external sources to verify what is missing. Removed per instructions.

3. **Pure formatting/style nitpicks** (typos, grammar, whitespace) — These are parser artifacts, not author errors. Removed.

## Novel Insights

The reviews reveal a substantive tension that goes beyond the paper's own presentation: the paper's theoretical framework (Theorem 1) calls for class-specific coverage inflation that depends on per-class calibration set size, error rates, and concentration bounds, but the experimental implementation falls back on a global tuning parameter g that is simpler but unconnected to the theory. This is not a case of a "missing ablation" or "need more experiments" — it is a structural mismatch between the provable guarantee claimed and the heuristic actually validated. The paper's empirical results are strong enough to stand on their own as a demonstration that rank-aware double-calibration reduces prediction set sizes. But the paper sells itself as providing provable guarantees for its method as evaluated, and that claim is weakened by this gap. The most productive path forward would be to either: (a) derive a guarantee for the actual g/√n tuning procedure (which may be feasible under some conditions), or (b) implement the class-specific inflation from Theorem 1 using empirical estimates of ε_y and show that coverage is maintained. Either direction would align the contribution's packaging with its technical content.

## Suggestions

- **Align theory and practice.** Either derive a class-conditional coverage guarantee that applies to the global g/√n tuning procedure, or implement the class-specific inflation from Theorem 1 (with a concrete δ choice) in the experiments and verify UCR is still controlled.
- **Clarify the role of g.** State explicitly how g enters both the score threshold inflation (global √n or class-specific √n_y) and the rank threshold calibration (Equation 11). If the same g is used for both, say so; if different, use different symbols.
- **Add an ablation.** Compare (a) k-CCP variant with rank threshold only (no score inflation), (b) score inflation only (no rank threshold), and (c) full k-CCP, to isolate which mechanism drives the size reduction on imbalanced data.

## Score and Decision

The paper proposes a novel and well-motivated method, demonstrates clear empirical improvements on multiple benchmarks, and provides a useful theoretical framing. However, the disconnect between the theoretical guarantees (which require class-specific inflation) and the experimental implementation (which uses global tuning) is a significant weakness that undermines the claim of a "provable" guarantee for the method as evaluated. The empirical contribution is strong enough to warrant acceptance, but the theoretical claims need tightening.

**Score: 6.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>