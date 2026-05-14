Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper presents a theoretical analysis of how a one-layer Mamba model learns in-context learning (ICL) for binary classification tasks when prompts contain additive outliers. The authors decompose Mamba into a linear attention component plus a nonlinear gating layer, and prove convergence guarantees (Theorem 1) and generalization bounds for distribution-shifted outliers (Theorem 2). They compare against one-layer linear Transformers (gating removed), showing that while Mamba requires more training iterations, it can tolerate a higher fraction of outlier examples (α → 1, versus α < 1/2 for linear attention). The analysis characterizes the gating mechanism: it suppresses outlier-containing examples and induces exponential decay in importance based on index distance from the query (Corollary 2). Experiments on synthetic and real (SST-2) data support the theoretical findings.

## Strengths

- **First training-dynamics analysis of Mamba with gating for ICL.** The two-phase analysis of gating parameter training (Lemmas 4 and 5) — where the gating first learns to detect outlier patterns and then saturates to suppress them — is a genuinely novel technical contribution. Prior work (Li et al., 2024b, 2025b) studied global minima or expressivity, not SGD training dynamics of gating.

- **Clean theoretical framework for isolating the role of gating.** By deriving Mamba's output as linear attention + gating (Equation 3), and noting that removing gating recovers linear attention, the paper provides a principled way to study what the gating mechanism contributes. This is scientifically sound ablation, not a "weakened baseline."

- **Provable robustness condition for Mamba beyond the linear attention threshold.** Theorem 2 establishes that Mamba can maintain accuracy when α < min(1, p_a·l_tr/l_ts), which can approach 1, whereas Theorem 4 shows linear Transformers require α < 1/2. The synthetic experiments (Figure 2) validate this boundary across three outlier-labeling schemes.

- **Honest discussion of Mamba's CQ vulnerability.** The paper identifies and explains (via Corollary 2's exponential decay mechanism) why Mamba catastrophically fails when outliers are placed closest to the query (Table 1: 82.73% vs 93.96% for linear Transformer). The appendix even explores a mitigation strategy. This transparency is a strength, not a weakness.

## Weaknesses

### Fatal
None.

### Major

- **Parameter regime feasibility is not verified.** Theorem 1's conditions (ii) and (iii) involve multiple interacting constraints (e.g., Vβ⁻⁴ ≲ κ_a ≲ Vβ(1-p_a)p_a⁻¹ϵ⁻¹, combined with B ≳ β⁻⁴V²κ_a⁻²(1-p_a)⁻²logϵ⁻¹). The paper never demonstrates that there exists a non-empty set of parameters (M₁, V, β, κ_a, p_a, l_tr, B, η) that satisfies all conditions simultaneously. While asymptotic notation makes feasibility plausible for sufficiently small ϵ, the absence of any concrete worked example weakens the reader's confidence that the theorem covers a meaningful regime.

- **The experimental α range does not match the theory's strongest claim.** The paper claims Mamba works "even when α goes to 1" (Remark 5), but the experiments test only up to α = 0.8 (Figure 2). Testing α values closer to 1 (e.g., 0.90, 0.95) would substantially strengthen the empirical backing for the headline claim. Similarly, the experiments fix p_a = 0.6 and do not systematically vary p_a or l_tr to test the theory's predicted scaling laws (e.g., the (1-p_a)⁻¹ dependence in iteration count).

- **Softmax attention comparison in the appendix tells a different story.** Table 3 shows that softmax attention matches or slightly exceeds Mamba on FQ (99.40% vs 99.73%) and R (99.26% vs 99.67%) settings, and dramatically outperforms on CQ (99.28% vs 82.73%). While the paper correctly scopes its main comparison to *linear* attention, a casual reader of the abstract — "maintains accurate predictions even when the proportion of outliers exceeds the threshold that a linear Transformer can tolerate" — could easily miss the "linear" qualifier. The paper would be strengthened by including the softmax comparison more prominently and explicitly discussing what the comparison with linear attention *does* and *does not* tell us.

### Minor

- **Mamba's CQ failure highlights a fundamental trade-off, not just a secondary limitation.** The mechanism the paper identifies for Mamba's robustness (gating-induced exponential decay toward nearby examples) is precisely the same mechanism that causes catastrophic failure when outliers are near the query. This trade-off between outlier suppression and positional bias is a core architectural property, not a peripheral issue. The paper acknowledges it but treats it as a secondary observation rather than a central finding that could reshape the paper's narrative.

- **The data model is highly stylized.** Orthogonal relevant/irrelevant/outlier patterns and a fixed set of V training outliers whose test variants are positive linear combinations are far from real LLM pre-training data. While this is standard for theoretical work, the paper does not discuss how violations of orthogonality or the specific outlier structure would affect the analysis.

- **No systematic experimental verification of the theory's quantitative predictions.** The synthetic experiments use fixed parameter values (Section 4.1, p_a = 0.6, specific κ_a, β, etc.) but do not test whether varying these parameters produces the scaling behaviors predicted by Theorems 1-4 (e.g., how required iterations scale with (1-p_a)⁻¹, or how the tolerable α depends on p_a·l_tr/l_ts).

### Trivial
- The theoretical notation in the main text (e.g., conditions with ≳ and ≲ that mix multiple parameters) could benefit from an explicit interpretability table showing the direction of each inequality.

## Nice-to-Haves
- A concrete numerical example showing parameters satisfying all constraints in Theorem 1 simultaneously would greatly increase confidence in the theoretical results.
- Testing α > 0.8 (e.g., 0.95) in experiments and systematically varying p_a to validate predicted scaling would strengthen the claim that "α goes to 1."
- Extending the softmax attention comparison to the same multi-layer setting used for Mamba in Section 4.2 and discussing the implications would help readers calibrate the paper's claims.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"The comparison between Mamba and linear Transformers is fundamentally misaligned"** — REMOVED: The paper explicitly scopes its theoretical comparison to "linear Transformers" (abstract, Remark 6). This is a controlled ablation (Mamba = linear attention + gating; removing gating gives linear attention), not a weakened baseline. The critic misreads the paper's claims.

- **"Softmax attention matches or exceeds Mamba in all settings"** — REMOVED: Table 3 shows Mamba outperforms softmax on FQ (99.73% vs 99.40%) and R (99.67% vs 99.26%). Softmax only dramatically exceeds Mamba on CQ (99.28% vs 82.73%). The factual claim is incorrect, though the CQ gap is a valid concern addressed above.

- **"The SST-2 experiment uses DistilBERT embeddings and PCA projections that may favor the paper's data model"** — REMOVED: This is a valid concern about real-world validation, but the paper already acknowledges this is an approximate validation using PCA, and the result is consistent with the synthetic experiments. This is a reasonable methodology for a theory paper.

- **Formatting and typo complaints** — REMOVED per instructions (parser artifacts).

## Novel Insights

The most interesting insight from synthesizing the reviews is that the paper's central theoretical contribution — characterizing the two-phase gating dynamics — actually predicts a fundamental architectural trade-off that the paper's framing underemphasizes. The exponential-decay mechanism that enables Mamba's robustness to high outlier fractions (by suppressing far-position outliers) is the same mechanism that makes it uniquely vulnerable to near-query outliers. This means Mamba does not provide uniformly "better" robustness than alternatives; it provides a *different kind* of robustness with a clear failure mode. The paper's narrative positions the CQ result as a secondary observation, but it could more honestly be presented as the key architectural insight: the gating mechanism creates an inevitable tension between positional recency bias and outlier robustness that softmax attention, by not having this gating structure, avoids. This reframing would make the paper both more honest and more scientifically interesting.

## Suggestions

1. Add a concrete parameter regime example satisfying all constraints of Theorem 1 in a table or footnote.
2. Include the softmax attention and multi-head comparisons more prominently — possibly as a main experiment with analysis — and explicitly discuss what conclusions the paper's comparison does and does not support.
3. Test α values closer to 1 (0.9, 0.95) and vary p_a systematically to validate the predicted scaling.
4. Reframe the paper's narrative to present the robustness-vs.-positional-bias trade-off as a central finding rather than a secondary limitation.
5. Verify some of the theory's scaling predictions (e.g., (1-p_a)⁻¹ dependence of iteration count) experimentally.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `kmK3WSCOCT.md` (Mamba ICL Markov chains) | 7.50 | Stronger paper: cleaner theoretical story, proven optimality (Bayes/minimax), clear link to experiments. The paper under review is less clean and has more caveats. |
| `hvpKqEYJjj.md` (Mamba training dynamics) | 5.00 | Accept Poster. Very similar in scope and methodology to the paper under review — both analyze simplified one-layer Mamba training dynamics with synthetic data. The paper under review has a somewhat more novel gating analysis (two-phase dynamics) but less thorough experiments. |
| `3KPsog4mpy.md` (Mamba ICL feature learning) | 5.00 | Reject. Similar topic and approach. Reviewers questioned novelty relative to prior Transformer analysis. The paper under review has clearer novelty (first Mamba training dynamics with gating) and better-scoped claims. |
| `lhvdbCiiE6.md` (Hybrid Mamba-2 ICL) | 3.33 | Reject. Weaker technical contribution (expressivity, not training dynamics). The paper under review has stronger theoretical novelty. |
| `8cDoHzqDXP.md` (Mamba recall scaling) | 3.33 | Reject. Suffered from lack of novelty relative to prior work. The paper under review has more original theoretical analysis. |
| `2g8vgmyXgQ.md` (Transformer ICL nonlinear) | 5.00 | Reject. Similar structure (training dynamics analysis, synthetic experiments). Comparable quality. |
| `EAfMzT8ZLy.md` (Transformer induction heads) | 4.50 | Withdrawn. Limited novelty relative to prior work. |

This paper is most comparable to `hvpKqEYJjj.md` (accepted at 5.0) and `2g8vgmyXgQ.md` (rejected at 5.0). It has genuine theoretical novelty (first analysis of Mamba gating training dynamics in two phases) that distinguishes it from the rejected papers, but also clear limitations (unverified parameter regime, α not tested close to 1, softmax results that complicate the narrative). The paper's contributions are real and non-trivial, meriting a borderline score.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>