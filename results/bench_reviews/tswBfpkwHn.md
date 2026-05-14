Now I have enough information to write the consolidated review. Let me compile it carefully, verifying each claim against the paper.

---

## Summary

This paper provides the first theoretical analysis of training dynamics for a one-layer Mamba model on in-context learning (ICL) of binary classification tasks in the presence of additive outliers. The authors reduce Mamba to a linear attention plus nonlinear gating formulation, characterize how the gating parameters evolve during SGD training (a two-phase analysis spanning Lemmas 4–5), and prove convergence guarantees (Theorem 1) and robustness to distribution-shifted outliers at test time (Theorem 2). They also provide a parallel analysis for linear Transformers (Theorems 3–4) to isolate the effect of the nonlinear gating, showing that linear Transformers fail when the outlier fraction exceeds 1/2 while Mamba can tolerate α approaching 1. Experiments on synthetic and real-world (SST-2) data validate the theoretical predictions.

## Strengths

- **First training-dynamics analysis of Mamba for ICL with outliers.** The two-phase characterization of gating parameter evolution (Lemmas 4–5, proof sketch in Appendix A) is technically non-trivial and fills a gap in the theoretical understanding of Mamba. Prior work (Li et al., 2024b; 2025b) studied expressiveness/global minima but not training dynamics. This is a genuine analytic contribution.

- **Clean mechanistic interpretation.** Corollary 1 shows that the trained linear attention component concentrates weight on context examples sharing the query's relevant pattern (analogous to induction heads). Corollary 2 shows that the nonlinear gating (i) suppresses outlier-containing examples to near-zero weight, and (ii) imposes an exponential decay in gating values with index distance from the query. These mechanisms are validated in multi-layer experiments (Figures 3–4).

- **Rigorous isolation of the gating effect via controlled comparison.** By analyzing a linear Transformer under the identical data and training setup (Theorems 3–4, setting gating to 1), the paper cleanly separates what the gating contributes. The comparison reveals a real trade-off: Mamba requires larger batch sizes and more iterations but can tolerate far higher outlier density. This is a more honest framing than claiming unconditional superiority.

- **Experimental validation aligns with theoretical thresholds.** Figure 2 confirms the predicted α > 1/2 failure for linear Transformers and Mamba's robustness up to α ≈ 0.8. Table 3 in the appendix shows softmax attention achieves comparable robustness to Mamba, and the paper explicitly discusses this, appropriately scoping the theoretical comparison.

## Weaknesses

### Fatal

None.

### Major

- **Abstract and framing occasionally overclaim relative to the evidence.** The abstract states Mamba "maintains accurate predictions even when the proportion of outliers exceeds the threshold that a linear Transformer can tolerate" — this is technically correct but could be misread as a general claim about Transformers, not specifically linear Transformers. The introduction poses "Under what conditions can Mamba outperform Transformers for ICL?" (line 73) without the "linear" qualifier. The main theoretical results (Section 3.4) and Remark 6 are properly scoped, but some high-level framing could mislead a casual reader. The paper should consistently use "linear Transformer" throughout the abstract and introduction to match the theoretical scope.

### Minor

- **Limited experimental exploration of the parameter space.** The experiments use a single setting: V=3 outlier patterns, κ_a=2, p_a=0.6. Theorem 1's conditions involve scaling relationships between V, κ_a, p_a, and batch size that are not empirically probed. Varying V or κ_a would test whether the gating mechanism scales as the theory predicts. The paper's own appendix (Tables 4–5) shows softmax attention maintains robustness across α values — similar ablation across V or κ_a for Mamba would strengthen the empirical support.

- **Verification gap between theoretical conditions and experimental settings.** Theorem 1 requires B ≳ max{...} with terms scaling as β⁻⁴V²κ_a⁻²(1-p_a)⁻². While the bound is likely satisfied for the chosen parameters, the paper does not verify that the experimental setup meets the theoretical conditions (batch size, number of iterations, etc.). Computing these for the reported experiments would connect theory and practice more concretely.

- **Narrow test of Theorem 2's outlier generalization claim.** Theorem 2 condition (a) allows test outliers that are positive linear combinations of training outliers (Σλ_i ≥ L > 0). The experiments use three predefined combinations, all with positive coefficient sums. The boundary case — combinations with near-zero or exactly zero total coefficient, which would violate condition (a) — is not tested. Probing this boundary would clarify the sharpness of the theoretical condition.

### Trivial

- **Real-world SST-2 experiments use only 8 context examples** (Appendix B.2), which is very small. The PCA justification (Table 6) shows 78.90% accuracy with 10 components vs. 80.05% baseline — a 1.15% gap described as "close to the baseline," which is debatable.

- **The claim that deeper layers "exhibit the same trend" (Section 4.2)** is stated without nuance. While appendix figures support this for the specific setting, deeper layers in multi-layer models often learn qualitatively different functions; a brief qualification would be appropriate.

## Nice-to-Haves

- Testing Mamba's gating robustness when outlier pattern magnitude κ_a is close to irrelevant pattern magnitude would probe whether the gating distinguishes outliers by direction (as the theory assumes) rather than magnitude alone.
- A quantitative comparison of empirical convergence rates against the theoretical bounds in Theorem 1 (e.g., how many iterations are actually needed vs. T_M) would strengthen the theory-practice connection.
- Training a linear Transformer with a learned scalar per-position weight (a minimal "gated Transformer" baseline) would test whether Mamba's *specific* gating design matters or whether any learnable weighting mechanism suffices. This is beyond the paper's scope but would sharpen the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Issue 1 (unfair comparison is "methodologically invalid"):** The critic argues that comparing Mamba to a linear Transformer with gating fixed to 1 is unfair because it deprives the Transformer of any outlier-handling mechanism. **Removal justification:** The paper explicitly frames this comparison as isolating the gating effect: "Such an analysis is conducted to rigorously probe how the nonlinear gating affects model training... as the gating is the only difference between the two architectures" (Remark 6). The paper also includes softmax attention results in Appendix B.1 showing comparable robustness, acknowledging the limitation of the linear Transformer comparison. The harsh critic's characterization of this as a "straw man" is itself a misreading — the comparison is a controlled ablation, not a claim about all Transformers. The abstract and intro phrasing could be tightened (see Major weakness above), but the comparison design is methodologically sound for its stated purpose.

- **Harsh Critic Issue 2 (training setup "doesn't show this actually works"):** The critic claims the paper never demonstrates the gating-outlier separation emerges reliably. **Removal justification:** Figure 4 directly demonstrates this — gating values for outlier-containing examples (red) are near zero while clean examples (green) are large, exactly as Corollary 2 predicts. The critic's real concern is about ablations across hyperparameters (V, κ_a), which is valid (see Minor weakness) but does not mean the separation is undemonstrated.

- **Harsh Critic's claim about Corollary 2 being "architecturally inevitable":** **Removal justification:** The exponential decay is a consequence of the multiplicative gating structure, but that the gating *learns to produce values in (0,1) that realize this decay selectively on clean examples while suppressing outliers* is not inevitable — it's a learned behavior. Lemma 4 and Lemma 5 characterize this learning process.

- **Strength Finder's "Direct theoretical comparison with linear Transformers" as an unqualified strength:** This is partially covered by the controlled comparison strength above, with the qualification noted in the Major weakness.

- **Harsh Critic's formatting/style nitpicks:** All removed per hard rules.

- **Harsh Critic's concern about missing ablations for the training data requirements and phase transition monitoring:** These are moved to Minor/Nice-to-Have with appropriate downgrading. For a theory paper, not monitoring the phase transition or computing data requirements is standard — the contribution is the theoretical characterization, not the empirical verification of every condition.

- **Harsh Critic's concern about V' including negative coefficient combinations:** The paper does test combinations with negative individual coefficients (v*_3' = -0.7 v*_1 + 0.5 v*_2 + 0.5 v*_3), just with positive total sum (0.3 > 0). The boundary at zero/near-zero sum is not tested, which is covered in the Minor weakness.

## Novel Insights

The paper's two-phase analysis of gating training (Lemmas 4–5) reveals something genuinely interesting about how nonlinear gating learns under SGD with noisy labels: in the early phase, outlier-containing examples contribute canceling gradients (since labels are random), driving the gating parameter w to suppress them, while clean examples provide consistent signal. This "cancellation-then-amplification" dynamic is distinct from standard feature learning analyses and is specifically enabled by the multiplicative gating structure. The paper also uncovers a subtle vulnerability: the exponential decay in gating values (Corollary 2(ii)) means that when outliers are placed closest to the query (CQ setting), clean examples get pushed away and their gating weights decay, creating a failure mode not present in attention-based architectures. This CQ sensitivity is a genuinely novel empirical finding with practical implications for prompt design.

## Suggestions

- **Tighten the abstract and introduction to consistently say "linear Transformer"** rather than occasionally using unqualified "Transformer." This is a one-sentence fix that would resolve the main framing concern.
- **Add a small ablation varying V or κ_a** to probe whether the gating mechanism scales. Even V ∈ {3, 5, 7} at fixed κ_a would substantially strengthen the empirical validation.
- **Compute whether the experimental settings satisfy Theorem 1's batch size and iteration requirements** — a paragraph in the appendix would close the theory-practice verification gap.
- **Test one boundary case for Theorem 2 condition (a)** — e.g., a test outlier with coefficient sum close to 0 — to demonstrate the sharpness of the positive-sum requirement.

---

This paper addresses an important and timely question — the theoretical underpinnings of Mamba's ICL capabilities and robustness. It makes a genuine contribution through the first training-dynamics analysis of Mamba's gating mechanism, a clean mechanistic interpretation, and a controlled theoretical comparison with linear Transformers. The core theoretical results (Theorems 1–2, Corollaries 1–2) are well-supported by the proofs and synthetic experiments. The main limitations are presentational (occasional overclaiming in the abstract/introduction framing) and empirical (limited parameter-space exploration), none of which undermine the core contribution. The paper sits above the typical borderline-theory-paper threshold: it is more substantive and better-executed than the rejected Mamba ICL theory paper at 5.00, but falls short of the polished, tightly-scoped theoretical contributions at 7.50. Compared to the accepted-poster Mamba training dynamics paper at 5.00, this paper adds the outlier robustness dimension and a cleaner mechanistic story, meriting a slightly higher score.

Now comparing against all calibration anchors:

- **kmK3WSCOCT (7.50, Accept Oral):** Tighter, more elegant theoretical results with a constructive proof connecting Mamba to optimal statistical estimators. Current paper is weaker — the theoretical framework is less crisp and the framing has issues.
- **VAv1rrPR1A (7.50, Accept Poster):** Different topic but similarly well-executed. Current paper is weaker.
- **KZLeg0MQ2r (6.00, Accept Poster):** Clean theoretical results with direct validation. Current paper is comparable but slightly weaker due to framing issues.
- **YDl4vqQGP (6.00, Accept Poster):** Empirical Mamba paper, not directly comparable.
- **hvpKqEYJjj (5.00, Accept Poster):** Very similar scope — Mamba training dynamics theory. Current paper is stronger (outlier dimension, cleaner mechanistic interpretation, comparison to Transformers).
- **3KPsog4mpy (5.00, Reject):** Mamba ICL theory, rejected. Current paper is clearly stronger (training dynamics, not just expressivity).
- **0GNBqoYcAP (4.67, Accept Poster):** Different topic, not comparable.
- **C0AQNXhTiY (4.50, Reject):** SSM theory, different focus. Current paper stronger.
- **lhvdbCiiE6 (3.33, Reject):** Mamba-2 SGD simulation, no training dynamics. Current paper clearly stronger.
- **yLA9l9hykz (2.67, Reject):** Empirical, no theoretical guarantees. Current paper clearly stronger.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>