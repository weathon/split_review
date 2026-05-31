Now let me do the calibration search to anchor the score.Now let me read one more anchor to sharpen the calibration:## Summary

This paper presents the first theoretical analysis of training dynamics and in-context learning (ICL) generalization for a one-layer Mamba model. The central contribution is showing that Mamba's nonlinear gating mechanism enables robustness to arbitrarily high fractions of outlier-containing context examples (approaching 1 under suitable prompt-length conditions via Theorem 2), whereas the corresponding linear Transformer baseline collapses above α = 1/2. The result is supported by mechanistic corollaries showing how the trained attention concentrates on same-pattern examples and how the gating suppresses outliers while inducing position-dependent exponential decay.

---

## Strengths

1. **First training-dynamics convergence guarantee for Mamba in ICL.** Theorem 1 provides quantitative sufficient conditions (batch size, iterations, outlier magnitude, prompt length) for achieving ε training loss — the first such result for a Mamba model. This is directly analogous in scope and novelty to the first training-dynamics analyses for linear/nonlinear Transformers in ICL.

2. **Concrete mechanistic characterization of the Mamba ICL mechanism.** Corollaries 1 and 2 are quantitative, not qualitative. Equation (16) proves the linear attention concentrates on same-pattern examples; equations (17)–(18) prove the gating suppresses outlier examples (G → near 0) and imposes exponential decay in clean examples with index distance from the query. This directly explains *how* Mamba achieves robustness, not just *that* it does, and connects to the "induction head" literature as noted in Remark 7.

3. **Clean empirical validation.** Figure 2 directly verifies the theoretical threshold predictions: Mamba maintains < 10⁻² error up to α ≈ 0.8 across all three outlier labeling conditions, while the linear Transformer collapses above α = 0.5. Figures 3 and 4 verify Corollaries 1 and 2 respectively in a 3-layer model, showing the mechanism persists beyond the one-layer theoretical scope.

4. **Rigorous quantitative Mamba–Transformer comparison.** Theorems 3 and 4 derive exact linear Transformer counterparts, enabling a precise comparison of sufficient conditions in Remarks 4 and 5. The trade-off (Mamba needs larger batch sizes and more iterations but tolerates α → 1 vs. α < 1/2) is quantified, not just asserted.

5. **Distribution-shift generalization under realistic outlier variation.** Theorem 2 handles test-time outliers that are positive linear combinations of training outlier patterns (condition (a)), allows arbitrary label functions on corrupted examples (Definition 2), and permits different outlier magnitudes at test time — modeling a range of practical poisoning scenarios.

---

## Weaknesses

### Fatal
None.

### Major

**1. The Transformer comparison is against a linear (softmax-free) baseline, but the framing in abstract and Section 1.1 partially obscures this — why it matters.**
The central comparative claim — Mamba tolerates α → 1 while "Transformers" can only tolerate α < 1/2 — is proven against a linear Transformer obtained by setting G = 1 in equation (3), i.e., Mamba with gating disabled. The comparison is correctly described in Section 2 and Section 3.4, and Remark 6 does acknowledge that "large Transformer models, with appropriate training methods and ICL prompt design, can indeed achieve favorable robustness." However, Section 1.1 Contribution 2 states "Mamba demonstrates superior robustness to a high density of outliers in ICL" without qualification, and the abstract uses "linear Transformers" once but then returns to language implying general Transformer superiority. Because the paper's significance rests heavily on the Mamba-vs-Transformer comparison, the gap between what is proven (against a softmax-free linear baseline) and what is implied (general superiority) is consequential for readers who may not reach Remark 6. The abstract and Section 1.1 should consistently say "linear Transformer" and include Remark 6's qualifier upfront.

**2. The theoretical robustness guarantee does not cover the CQ failure case revealed in Table 1.**
Table 1 shows that when outliers are placed closest to the query (CQ setting), Mamba's accuracy drops to 82.73% — below the linear Transformer's ~94% in all three placement conditions. The paper correctly explains this via Corollary 2(ii): clean examples are pushed farther from the query, and their gating values decay exponentially per equation (18). However, Theorem 2 and Corollary 2 do not provide a generalization bound for the CQ placement regime, nor any theorem quantifying how severe the degradation is or under what conditions it occurs. This is a substantive theoretical gap: the paper's own tools predict the failure mechanism but cannot bound it. In adversarial ICL settings (the data-poisoning motivation of Figure 1 and Example 1), an attacker would rationally place corrupted examples near the query, making this the most practically relevant adversarial regime. Table 1 is currently an empirically honest but theoretically unresolved limitation.

### Minor

**3. The α-threshold in Theorem 2 does not match the stated experimental parameters.**
Condition (c) of Theorem 2 requires α < min(1, p_a · l_tr / l_ts). With p_a = 0.6 and l_tr = l_ts = 20 as stated in Section 4.1, this gives a guaranteed upper bound of α < 0.6. Yet Figure 2 demonstrates Mamba maintaining < 10⁻² error at α = 0.8. Remark 3 notes that α "can be close to 1 if p_a · l_tr / l_ts ≥ 1," but this requires l_tr > l_ts, which is not satisfied in the experiments. The sufficient condition is simply not tight, which is standard and not alarming, but the paper never acknowledges this discrepancy. A sentence in Section 4.1 noting that the sufficient condition yields a guarantee only up to α < 0.6 for these parameters, and that empirical performance exceeds this bound, would clarify the relationship between theory and experiment.

**4. The outlier magnitude window in Theorem 1 condition (ii) may vanish at high outlier fractions.**
Condition (ii) requires V·β⁻⁴ ≲ κ_a ≲ V·β·(1−p_a)·p_a⁻¹·ε⁻¹. As p_a → 1, the upper bound collapses while the lower bound remains fixed, potentially making the window infeasible. Remark 1 discusses the meaning of the bounds qualitatively, but does not characterize when the window is non-empty as a function of p_a. Since the "approaches 1" robustness claim relies on high p_a training, this interaction deserves a sentence.

### Trivial
None.

---

## Nice-to-Haves

- **Theoretical bound on the CQ failure case**: Given that Corollary 2(ii) already produces the exponential decay prediction in equation (18), deriving even an informal bound on the worst-case generalization error when all outliers are within distance d of the query would convert Table 1 from an empirical surprise into a theoretically predicted regime boundary.
- **Training convergence curve experiment**: Remark 4 states Mamba requires Θ(l_tr) more iterations than the linear Transformer. A direct training curve comparison would verify this quantitative prediction.
- **Brief main-text summary of the real-world experiment** (Appendix B.2): the motivating example throughout the paper is natural-language poisoning (Figure 1, Example 1), so even one paragraph on the real-data findings would connect the theory to its stated application.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

**Removed — Orthogonality assumption limits adversarial applicability (Harsh Critic):** The critic notes that v_s* ⊥ μ_j and v_s* ⊥ ν_k (Section 3.2) may not hold when attackers correlate outlier directions with task-relevant signals. This is a standard limitation of data-model-based ICL theory — the same assumption appears throughout the literature this paper builds on. Criticizing its absence is scope creep for a first-results paper. Demoted below Minor.

**Removed — Framing Table 1 as a contradiction of the robustness narrative (Harsh Critic):** The paper does not claim position-invariant robustness. Corollary 2(ii) explicitly predicts exponential decay with position distance. Table 1 is the empirical confirmation of this predicted failure mode, not a contradiction. Retained only as Major weakness #2 for the missing theoretical bound on the CQ case.

**Removed — "Experiments use different parameters than described" as a fatal discrepancy (Harsh Critic):** The parameters are clearly stated (Section 4.1). The discrepancy between the theory's sufficient bound (α < 0.6) and the experimental result (α = 0.8) simply reflects looseness of sufficient conditions — entirely standard. Retained only as Minor weakness #3 about the lack of acknowledgment.

**Removed — Strength "additional experiments referenced in appendix" (Strength Finder):** Generic; not a specific contribution of this paper.

**Removed — Strength "realistic corruption modeling" (Strength Finder):** Subsumed by Strength 5; not concrete enough as a standalone claim.

---

## Novel Insights

The most novel observation from the combined reviews is the mechanistic duality the paper establishes: linear attention and nonlinear gating in Mamba address orthogonal aspects of ICL robustness. The attention implements pattern-matching (an induction-head analog in linear attention), while the gating simultaneously implements outlier suppression and position-based local bias. These two functions are cleanly separable in the theoretical framework precisely because outlier patterns are orthogonal to task-relevant patterns — a structural assumption that enables the gating to be trained independently for outlier detection without interfering with the attention's pattern-matching. The position-sensitivity finding (Table 1) is the natural flip-side of this clean separation: when the two functions interact adversarially — outliers near the query force the gating to suppress nearby clean examples — robustness degrades below the linear Transformer baseline. This regime boundary is both theoretically predicted and empirically confirmed, and constitutes the most important open problem the paper leaves for future work.

---

## Suggestions

1. **Rewrite the abstract and Section 1.1 Contribution 2** to consistently say "one-layer single-head linear Transformer" in place of "Transformer" or "linear Transformer," and include Remark 6's key qualifier upfront.
2. **Add one sentence in Section 4.1** noting that the sufficient theoretical bound for these parameters is α < 0.6, and that Figure 2's success at α = 0.8 reflects looseness of the bound.
3. **Extend Corollary 2 or add a Remark/Proposition** bounding worst-case generalization error in the CQ regime, using the decay inequality in equation (18).
4. **Characterize the feasibility window** of κ_a in condition (ii) of Theorem 1 as a function of p_a, clarifying when the window is non-empty at high outlier fractions.

---

## Score and Decision

**All calibration anchors (with comparisons):**

*Round 1:*
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| n7n8McETXw | 6.50 | R1 | Closest analog: first theoretical analysis of training dynamics for a new ICL setting; paper under review is comparable in scope, contribution quality, and experimental support |
| ikwEDva1JZ | 6.50 | R1 | ICL theory "first steps" paper; comparable |
| aKJr5NnN8U | 6.50 | R1 | ICL in-context vs. in-weight theory; comparable |
| HuBFimORiz | 4.33 | R1 | Markovian ICL global optimality; rejected; clearly below the paper under review |
| oZtt0pRnOl | 8.00 | R1 | Privacy-preserving ICL with DP; stronger empirical breadth |
| STUGfUz8ob | 7.60 | R1 | Abstract symbol reasoning theory; stronger and broader |
| Tzh6xAJSll | 7.60 | R1 | Scaling laws for associative memories; stronger |

*Round 2:*
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| DVlPp7Jd7P | 6.50 | R2 | Single-location regression theory; comparable single-mechanism ICL theory |
| 8p3fu56lKc | 6.00 | R2 | Linear self-attention ICL theory; comparable or slightly below |
| 97rOQDPmk2 | 7.33 | R2 | Two-layer Transformer + SignGD; more technically complex, higher score |
| EGjvMcKrrl | 6.00 | R2 | SSM generalization analysis; rejected; paper under review is stronger |
| AL1fq05o7H | 6.25 | R2 | Original Mamba paper resubmission; mixed scores |
| DjeQ39QoLQ | 6.50 | R2 | Robustifying SSMs via diagonalization; comparable |

**Round 1 bracket: 5.5–7.0.**

**Round 2 narrowing:** The paper is clearly better than EGjvMcKrrl (6.0, rejected) and 8p3fu56lKc (6.0, accepted). It is most comparable to n7n8McETXw (6.5), DVlPp7Jd7P (6.5), and DjeQ39QoLQ (6.5). The two Major weaknesses — the framing concern about the linear Transformer comparison and the unresolved theoretical gap in the CQ position case — place this paper slightly below the 6.5 anchors. The 6.5 anchors all had comparable scopes without a theoretically unresolved failure mode exhibited in their own main-text experiments. I settle at **6.0**.

**Decision: Accept** (marginal). The "first analysis" contribution to the Mamba ICL theory literature is genuine, the core technical results (Theorems 1–4, Corollaries 1–2) are sound within the stated assumptions, experiments cleanly verify the predictions, and the mechanistic corollaries provide insight beyond what was previously known. The weaknesses are real but addressable in revision and do not invalidate the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>