## Summary

This paper provides the first training-dynamics analysis for a one-layer Mamba model trained to perform in-context learning (ICL) on binary classification tasks with additive outliers. The core technical contribution is a reformulation of one-layer Mamba as a linear attention mechanism followed by a nonlinear sigmoid gating layer (Eq. 3), which enables convergence guarantees (Theorem 1), ICL generalization under distribution-shifted outliers (Theorem 2), and a theoretical comparison against one-layer single-head linear Transformers (Theorems 3–4). The paper proves that Mamba can tolerate an outlier fraction α approaching 1 (provided p_a · l_tr/l_ts ≥ 1), while a linear Transformer fails beyond α = 1/2, and provides mechanistic Corollaries characterizing how the linear attention selects matching-pattern examples and the gating suppresses outlier-containing ones.

---

## Strengths

- **First convergence/sample-complexity guarantee for Mamba in ICL** (Theorem 1, Eq. 10): Explicitly characterizes required batch size, iterations, prompt length, and outlier magnitude under the outlier-contaminated training setting. This is the Mamba counterpart to prior Transformer results (Zhang et al., 2023; Li et al., 2024a) and fills a genuine gap in the literature.

- **Quantified outlier robustness advantage over linear Transformers** (Theorems 2 vs. 4): Theorem 2 allows α → 1 when p_a · l_tr/l_ts ≥ 1, while Theorem 4 caps the Transformer at α < 1/2. This is a concrete, precisely quantified robustness gap derived from the same unified framework, not an informal empirical claim.

- **Mechanistic interpretability via Corollaries 1 and 2**: Corollary 1 (Eq. 16) shows the linear attention concentrates weight on same-pattern examples; Corollary 2 (Eqs. 17–18) shows gating near-zeros out outlier examples and decays exponentially with index distance for clean examples. These directly explain how Mamba achieves robust ICL.

- **Empirical validation directly matching the theory** (Figures 2–4, Table 1): Figure 2 confirms the α thresholds from Theorems 2 and 4 on synthetic data, achieving <0.01 error at α = 0.8 for Mamba vs. error inflation past α = 0.5 for linear Transformer. Figures 3 and 4 directly verify Corollaries 1 and 2. Table 1 honestly reports the CQ failure case alongside the theory's predicted explanation.

- **Correct architectural scoping and comparison justification** (Section 2, Remark 6): The paper explicitly states the comparison is to linear Transformers (not softmax Transformers), justifies the choice in Remark 6 as isolating the gating mechanism, and notes that large Transformers with appropriate design can also be robust. The abstract correctly uses "linear Transformer."

---

## Weaknesses

### Fatal
None.

### Major

- **Position-sensitivity failure case is theoretically unresolved (Table 1):** Table 1 shows that when outliers are placed closest to the query (CQ), Mamba accuracy drops to 82.73% while the linear Transformer holds at 93.96%. The paper correctly explains this as the exponential decay in Corollary 2 (Eq. 18) penalizing clean examples that are pushed farther from the query. However, the existing theory (Corollary 2, Theorem 2) only guarantees good performance under uniform/arbitrary outlier placement — it does not provide a bound for the CQ regime and does not modify condition (c) of Theorem 2 to reflect position-dependent outlier placement. In adversarial settings (e.g., the data-poisoning motivation in Section 1), a rational attacker would precisely target the CQ placement to exploit this weakness. The theory therefore does not characterize its own most dangerous failure mode, and Table 1 presents a result where Mamba is strictly worse than the linear Transformer without a theorem that explains the regime boundary. Providing a bound in the CQ case (even informally via a corollary) would make the theory self-contained and convert Table 1 from a limitation to a theoretically predicted regime transition.

### Minor

- **The orthogonality of outlier patterns to all task patterns (Section 3.2) is a structural assumption that goes unexamined in terms of robustness to violations.** The condition v_s* ⊥ μ_j, v_s* ⊥ ν_k for all j, k is what allows gating-based suppression to operate independently of attention-based pattern matching. The paper does not discuss how the guarantees degrade when outliers partially correlate with task-relevant patterns — a natural concern given the adversarial motivations in Section 1. A brief discussion (even qualitative) of this sensitivity would strengthen the paper's positioning.

- **Theoretical bound vs. experiment mismatch for α (Section 4.1 vs. Theorem 2):** With the experimental parameters l_tr = l_ts = 20 and p_a = 0.6, condition (c) of Theorem 2 requires α < min(1, 0.6 × 20/20) = 0.6. Yet Figure 2 shows Mamba achieving <0.01 error at α = 0.8. The paper's comment that results are "consistent" with the theory is not precise: the experiment exceeds the theoretical sufficient condition. This is not a contradiction (sufficient conditions are rarely tight), but the discrepancy should be explicitly acknowledged so readers do not conclude the theorem's bound matches the empirical threshold.

### Trivial

- The conclusion/future-work section (Section 5) is exceptionally brief and mentions only "designing general Mamba-based language/multi-modal models," without engaging with any of the open theoretical questions the paper itself surfaces (non-orthogonal outliers, position-dependent guarantees, multi-head or softmax extensions). A more informative discussion of theoretical open problems would better serve the community.

---

## Nice-to-Haves

- Surfacing a brief summary of the real-world experiments (Appendix B.2) in the main text would connect the theory to the motivating data-poisoning application more directly, given that Section 1 and Example 1 use language-task poisoning as the primary motivation.
- A convergence-rate experiment (epochs vs. error for Mamba vs. linear Transformer) would directly verify the Θ(l_tr) multiplicative factor in T_M vs. T_T claimed in Remark 4, beyond the fixed-endpoint comparison in Figure 2.
- The window for κ_a in Theorem 1 condition (ii) — V·β^{-4} ≲ κ_a ≲ V·β(1−p_a)p_a^{-1}ε^{-1} — is non-empty only when the lower bound is less than the upper bound; a brief characterization of this feasibility region and its dependence on β, V, ε would aid practitioners applying the results.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Framing problem: abstract/title use 'Transformers' and 'linear Transformers' interchangeably"** (Harsh Critic): Removed. Upon reading the abstract directly, it says "the proportion of outliers exceeds the threshold that a **linear** Transformer can tolerate." The abstract is correctly scoped. Section 1.1 Contribution 2 explicitly says "one-layer single-head **linear** Transformers." Remark 6 provides an explicit caveat about large softmax Transformers. The framing is adequate; this was a misread.

- **"Remark 4 compares sufficient conditions, not tight bounds, and convergence rate claim is not experimentally verified"** (Harsh Critic): Removed. This is standard practice in theoretical neural network analysis (the paper explicitly notes in Section 3.4 "comparison is made between sufficient conditions... a common practice used in existing works"). Applying a standard that demands tight or empirically verified convergence bounds for theory papers would be non-standard for the field.

- **Generic "significance depends only on comparison against a weak baseline"**: Removed. The comparison against a linear Transformer is the *stated* methodological choice made to isolate the effect of gating; it is not a cherry-picked weak baseline but a controlled theoretical comparison. Remark 6 acknowledges the scope limitation explicitly.

- **Strength Finder claim: "realistic corruption modeling covering a wide range of noisy testing prompts"** — retained in weakened form. The test outlier model does allow arbitrary positive combinations of training outliers and arbitrary labeling functions, which is broad. However, the orthogonality assumption still limits this claim in adversarial directions.

---

## Novel Insights

The paper's most genuinely novel theoretical insight is the mechanistic decomposition in Corollaries 1 and 2: the linear attention and nonlinear gating in Mamba perform *complementary* functions that can be separately analyzed and learned — attention for task-relevant pattern selection, gating for outlier suppression and local bias. This decomposition explains the ICL robustness advantage quantitatively (not just qualitatively) and gives a precise theoretical account of the "induction head"-like phenomenon in a linear attention setting. The position-sensitivity result in Table 1 — where the gating's local bias becomes a liability when adversarial examples appear near the query — is a direct prediction of Corollary 2 and constitutes a novel, falsifiable characterization of when Mamba's structural advantage reverses.

---

## Suggestions

1. Extend the theoretical framework to bound generalization error in the CQ (closest-to-query) outlier placement regime. Corollary 2's exponential decay formula (Eq. 18) already gives the key quantity; a corollary bounding performance as a function of how many outliers precede the first clean same-pattern example would complete the picture.
2. Add a one-paragraph discussion in Section 3.2 or 5 about the effect of partial correlation between outliers and task-relevant patterns, even if only informally. This directly addresses the main scope limitation relative to the adversarial applications in Section 1.
3. Clarify in the Section 4.1 discussion that the experimental success at α = 0.8 (with p_a = 0.6, l_tr = l_ts = 20) exceeds the theoretical sufficient condition, and explain that sufficient conditions being non-tight is expected — this prevents misreading of the "consistent with the theory" claim.

---

## Assessment by Axis

**Originality:** High — first training-dynamics and ICL generalization analysis for Mamba, using a clean linear-attention + gating decomposition novel to this architecture.
**Importance:** High — Mamba is practically significant, and ICL robustness to poisoning/outliers is an open theoretical question with empirical backing (Park et al., 2024).
**Claims supported:** Good — Theorems are proven within stated assumptions, experiments directly verify each theoretical prediction (including the failure case). The α = 0.8 vs. theoretical α < 0.6 point is imprecisely explained but not contradictory.
**Soundness:** Good — proofs are clearly structured within their assumptions, which are transparently stated. No incorrect reasoning identified.
**Clarity:** Good — theorem-remark structure is effective; mechanisms are explained; scope is adequately qualified in Remark 6. Conclusion is thin.
**Community value:** High — provides a theoretically grounded mechanistic explanation for observed empirical behavior of Mamba in ICL, with precise sufficient conditions comparable to prior Transformer theory.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>