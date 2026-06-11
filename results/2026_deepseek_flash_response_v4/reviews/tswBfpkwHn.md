Here is the final consolidated review.

---

## Summary

This paper presents the first theoretical analysis of the training dynamics (not just global minima or expressivity) of a one-layer Mamba model for in-context learning (ICL) on binary classification tasks with additive outliers. It proves convergence guarantees (Theorem 1), generalization bounds under distribution-shifted test-time outliers (Theorem 2), and compares against a one-layer linear Transformer, showing the Transformer's sufficient condition requires α < 1/2 (Theorem 4) while Mamba's bound can approach α → 1 under appropriate conditions. The mechanistic analysis (Corollaries 1–2) characterizes how Mamba's gating suppresses outliers and induces an exponential locality bias. Experiments on synthetic data support the theoretical predictions.

## Strengths

1. **First training-dynamics analysis for Mamba in ICL.** Prior theoretical work on Mamba (Li et al., 2024b; Bondaschi et al., 2025) studied loss landscapes or expressivity, not whether SGD provably converges to a generalizing model. Theorems 1 and 2 provide explicit conditions on batch size, iterations, prompt length, and outlier fraction needed for convergence and generalization — a genuinely new theoretical contribution.

2. **Provable separation in outlier tolerance.** Theorem 2 (Mamba: α < min(1, p_a·l_tr/l_ts)) and Theorem 4 (linear Transformer: α < 1/2) give a mathematically stated threshold difference under the identical data model. Figure 2 confirms this qualitatively across three labeling functions (flipped, targeted, random). The separation is not just a vague architectural comparison but a concrete condition contrast.

3. **Mechanistic characterization of gating's dual role.** Corollary 2 quantifies two distinct functions with high-probability bounds: outlier suppression to O(poly(M₁)⁻¹) (Eq. 17) and exponential locality bias Θ(1/2^{j-1}) for the j-th nearest clean example (Eq. 18). Figures 3–4 verify both predictions in 3-layer models, showing the mechanism extends beyond the one-layer analysis.

4. **Honest reporting of architectural trade-offs.** Table 1 shows Mamba outperforms the linear Transformer on farthest-outlier (99.73% vs. 93.68%) and random (99.67% vs. 94.12%) placements but underperforms on closest-to-query placement (82.73% vs. 93.96%), validating the locality bias prediction and providing a balanced picture.

## Weaknesses

### Minor

1. **High-level claims about the Transformer's α < 1/2 limitation conflate sufficient conditions with proven impossibility.** The abstract (line 33) and P2 (line 95) state linear Transformers "can only" generalize when α < 1/2, and Figure 2's caption says linear Transformers "cannot" tolerate more than 1/2. Theorem 4 only establishes a *sufficient condition* — no lower bound shows α ≥ 1/2 is impossible for linear Transformers. The paper does acknowledge this framing at the theorem level (line 187: "The comparison is made between sufficient conditions"), but the abstract and key insights use unqualified language. This is fixable with careful rewriting but is a real discrepancy between the high-level narrative and what the theorems actually establish.

2. **The claim that Mamba tolerates α "going to 1" (line 95) understates the conditions.** Theorem 2 condition (c) requires α < min(1, p_a·l_tr/l_ts). For α → 1, we need p_a·l_tr/l_ts ≥ 1 — requiring p_a close to 1 and/or l_tr >> l_ts. In the experiments (p_a=0.6, l_tr=l_ts=20), the theorem guarantees α < 0.6, yet Figure 2 shows Mamba working at α=0.8. The experiments exceed the theory, which is fine, but the high-level text ("α goes to 1") should more prominently carry the qualifying conditions.

3. **Test-time outliers must lie in the positive cone of training outlier patterns** (Theorem 2, condition (a)). While the paper correctly states this condition, the practical implications are under-discussed: all test-time outliers must be positive linear combinations of the V training outlier patterns. The paper calls this "unbounded number of outlier variations" (line 137), which is technically correct within the span, but outliers in genuinely new directions orthogonal to the training span are not covered. The "James Bond" poisoning example would only be handled if the trigger is in this span.

4. **The CQ vulnerability (Table 1: Mamba 82.73% vs. linear Transformer 93.96%) is a genuine failure mode of gating's locality bias**, but it appears only in Section 4.2 and is not mentioned in the abstract, introduction, or main theoretical sections. The paper's overall narrative foregrounds Mamba's superior robustness without proportionally noting this brittleness. The CQ finding is a predicted consequence of Corollary 2, so it should feature more prominently in the paper's balanced assessment.

5. **No error bars or variance reported for any experimental figures.** This is a standard expectation for empirical results, especially for Figure 2, which is the primary empirical evidence for the α < 1/2 vs. α → 1 claim.

### Trivial

6. The multi-layer (3-layer) experiments in Section 4.2 go beyond the one-layer theory. They are valuable but should be more explicitly flagged as heuristic extensions rather than empirical verifications of the theory.

## Nice-to-Haves

- A matching lower bound or impossibility result showing that α ≥ 1/2 causes the linear Transformer to provably fail (under the same data model) would turn the comparison into a genuine architectural limitation rather than a sufficient-condition gap.
- A brief summary of real-world data results (currently in the appendix) in the main text would help bridge the gap from the stylized synthetic setting.
- The paper could note the practical implication that increasing p_a during training improves test-time tolerance (the p_a·l_tr/l_ts condition), which is an actionable insight.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Linear Transformer is a non-standard baseline"** — The paper explicitly states it compares against *linear attention* Transformers, which are commonly studied in ICL theory (Zhang et al., 2023). Remark 6 acknowledges softmax attention can be more robust. The baseline is consistently labeled "linear Transformer" throughout. The comparison isolates the effect of gating, which is the paper's stated goal.
- **"Training labels on outlier examples are random (only)"** — Definition 1 specifies random labels for training outliers, which is a standard and general choice. The experiments test three labeling functions (flipped, targeted, random) at inference time, which is more thorough than many theory papers.
- **"Missing appendix/proofs/references"** — These are parser artifacts from PDF extraction; they exist in the original submission.
- **Criticism about the lack of discussion of p_a as a practical design parameter** — The paper does discuss this (Remark 3, P1).
- **"The experiments (Figure 2) are on one specific synthetic data instantiation"** — Figure 2 shows three labeling functions across a range of α values. The synthetic data follows the paper's theoretical setup, which is standard practice for theory papers.
- **Strength Finder's generic/superficial strengths** — Several generic strengths (e.g., "This paper addressed an important problem") are removed as they lack specific content.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's main insight — that the paper's high-level claims about the Transformer's limitation are stronger than what the sufficient-condition analysis supports — is valuable but is essentially a presentation critique rather than a novel observation. The strength finder's synthesis correctly identifies the core contributions. The tension between Mamba's robustness and its CQ brittleness (Table 1) is a genuine insight that the paper surfaces but does not fully resolve.

## Suggestions

1. In the abstract and introduction, replace "can only generalize when α < 1/2" with "our analysis guarantees generalization only when α < 1/2" to accurately reflect the sufficient-condition framing.
2. State the conditions for α → 1 (p_a·l_tr/l_ts must be ≥ 1) alongside the claim in P2 and the abstract, e.g., "Mamba maintains accurate generalization even when α approaches 1 (provided p_a·l_tr/l_ts ≥ 1)."
3. Add error bars or multiple-seed results to Figure 2, the primary empirical evidence.
4. Briefly mention the CQ limitation in the abstract or Section 3.1 alongside the robustness claims, so the paper presents a balanced picture from the start.
5. Clarify the practical implications of the span constraint (Theorem 2 condition (a)): what types of "unseen" outliers are and are not covered.

## Score and Decision

**Calibration Process:**

**Round 1 (Bracketing):** Queried three bands:
- Weak anchors (< 3.5): avg 2.5–3.4 — papers applying ICL theory tangentially with weak results. Our paper is clearly stronger.
- Middle anchors (3.5–7.5): Included "Mamba SSMs are Lyapunov-Stable Learners" (avg 4.67, Reject — shallower theory), "Mamba: Linear-Time Sequence Modeling" (avg 6.25 — original Mamba paper, more empirical), "Spatial-Mamba" (avg 7.00, Accept — vision application).
- Strong anchors (> 7.5): avg 7.6–8.0 — e.g., "When can transformers reason with abstract symbols?" (avg 7.60, Accept — cleaner theory leading to architectural modifications, LLM experiments).

**Round 2 (Narrowing):** Queried within (4.5, 6.5) and (6.0, 7.5):
- "One Step of GD is Provably Optimal ICL" (avg 6.00, Accept) — simpler analysis (global minimizer, no training dynamics), no experiments. Our paper has more substantive theory and experiments. → Our paper > 6.00.
- "Trained Transformer Classifiers Generalize" (avg 6.00, Accept) — purely theoretical, no experiments. Our paper has experiments and mechanism analysis. → Our paper > 6.00.
- "How Transformers Implement Induction Heads" (avg 6.20, Reject) — training dynamics analysis. Comparable scope.
- "Toward Understanding In-context vs. In-weight Learning" (avg 6.50, Accept) — gating mechanism analysis with experiments. Comparable.
- "How Many Pretraining Tasks Are Needed for ICL?" (avg 6.75, Accept) — task complexity for ICL, very clean theory.
- "Training Nonlinear Transformers for CoT" (avg 6.50, Accept) — very similar approach: training dynamics + generalization + distribution shift + noise for nonlinear Transformers. Our paper ≈ this one in scope and quality. Same reviewer concerns (simplified architecture, strong data assumptions). Our overclaiming issue is more noticeable. → Our paper ~6.0–6.5.

**Final position:** The paper sits at **6.0**. It makes a genuine and novel theoretical contribution (first Mamba ICL training dynamics), with solid theorems and mechanistic analysis supported by experiments. However, it is held back by the high-level overclaiming (sufficient conditions presented as hard limits) and lack of error bars. These are fixable issues, but they prevent the paper from reaching the clarity level of the 6.5+ anchors.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>