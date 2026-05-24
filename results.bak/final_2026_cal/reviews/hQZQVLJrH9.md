Now I have all the information I need. Let me write the consolidated review.

## Calibration Report

**Round 1 — Bracketing:**
- Low band (< 3.5): I3IeAZvxB4 (3.33, Reject) — Painless Activation Steering, weaker theory and experiments.
- Middle band (3.5–7.5): KYaNRqJ7ho (4.50, Reject) — Z0-Inf influence functions paper; 9lycwRxAOI (6.00, Accept) — Tracking Equivalent Mechanistic Interpretations; EDPvNhTOLK (6.00, Reject) — Directional Influence Function; 8epkNiuAQC (4.67, Accept) — Influence Dynamics.
- High band (> 7.5): No relevant anchors.

**Round 2 — Narrowing (bracket 4.5–6.5):**
- guSVafqhrB (4.67, Accept) — Fine-Grained Activation Steering: broader experiments, weaker theory.
- dGQubVJQx6 (5.00, Reject) — Concept Identifiability: theoretical focus,limited experiments.
- J4GYMiE3JT (6.50, Accept) — Structural Inference: strong theory on small model.

**Comparison:** This paper has stronger and more novel theory than the Fine-Grained Steering paper (4.67), but narrower experiments with unresolved issues (equation (2) inconsistency, slope 1.5 unexplained, workflow undemonstrated, underperforming CAA). It is weaker than the Directional Influence Function (6.00, Reject) on experimental rigor and completeness. The paper sits between these — stronger theory than 4.67 but more unresolved flaws than 6.00.

**Final score: 5.0**

---

## Summary

This paper proves a first-order equivalence between activation steering and influence functions. It derives the Influence-Aligned Steering (IAS) vector as the minimum-norm activation perturbation that matches a given influence-based logit shift, provides an alignment diagnostic γ, a spectral optimality condition for steering direction selection, a no-free-lunch theorem for when steering provably cannot replace influence, and generalization bounds for low-rank steering. Experiments on GPT-2 Medium (detoxification) and ResNet-50 (spectral analysis) provide initial empirical support.

## Strengths

1. **Novel theoretical bridge between two previously separate lines of work.** Theorem 4.2 establishes a closed-form duality: any steering vector corresponds to a signed measure over training data with ℓ₁ norm equal to the steering magnitude, and vice versa. This is the first explicit mapping between activation steering and influence functions, and it opens the door to a unified workflow.

2. **Clean geometric characterization of feasibility.** Theorem 5.1 quantifies the relative logit error of steering in terms of γ(x), the smallest principal-angle cosine between the Jacobian subspaces. Theorem 6.2 proves that when γ(x) ≤ ρ < 1, no activation perturbation can achieve more than a fraction ρ of the influence logit displacement — a crisp impossibility result that gives practitioners a principled stopping rule.

3. **Principled spectral direction selection.** Theorem 5.3 replaces heuristic steering-direction construction with a spectral recipe: the top eigenvector of a Fisher-influence matrix maximizes expected first-order logit change under an ℓ₂ budget. The accompanying power-iteration estimator is practical.

4. **Practical alignment diagnostic.** Computing γ(x) and ‖λ*‖ requires only two Jacobian-vector products, providing a cheap pre-check for whether steering is viable or weight-space editing is needed. Figure 2 shows monotonic increase in γ with layer depth, supporting the heuristic of selecting later layers.

## Weaknesses

### Major

1. **Equation (2) in Section 3.2 is inconsistent.** The paper writes Δh* = J_{h→y}^⊤ J_{θ→y} Δθ, which is missing the pseudoinverse (J_{h→y}J_{h→y}^⊤)^†. The correct expression from the Lagrangian is Δh* = J_{h→y}^† J_{θ→y} Δθ. While Theorem 5.2 gives the correct formula, the inconsistency in the core derivation section undermines confidence and must be fixed. This is a presentation error, not a structural flaw (the correct formula appears in Theorem 5.2), but it needs correction.

2. **The slope discrepancy (1.50) in Figure 1 is not explained.** The paper reports that predicted vs. actual logit shifts have a fitted slope of 1.50 with cosine 0.978, and describes this as "consistent with the expected linear regime." A slope of 1.5 means the actual logit shift is 50% larger than the first-order prediction — a systematic multiplicative bias, not just random O(α²) noise. The paper needs to explain this discrepancy or adjust its claim. The high cosine (0.978) shows directional correctness, which is encouraging, but the slope requires reconciliation.

3. **The data-provenance workflow is claimed but never demonstrated.** The paper prominently advertises "steer first, trace provenance" and states that Corollary 1 "pinpoints the fewest training examples to relabel/remove/examine." Yet no experiment shows this mapping: no qualitative example of top-weighted training documents, no sanity check that those documents are causal, no comparison to baseline attribution methods (TracIn, gradient similarity). This is a gap between the paper's stated practical value and the evidence provided.

4. **IAS underperforms CAA on detoxification without discussion.** In Table 1, IAS achieves toxicity 0.0164 vs. CAA's 0.0150 and perplexity 13701 vs. 13291 — worse on both metrics. The paper presents these numbers without comment. If IAS is intended as a principled alternative that also provides attribution, the trade-off needs to be discussed (e.g., "IAS is marginally worse but provides attribution"). Additionally, no confidence intervals or statistical significance is reported.

5. **Experiments are narrow.** Only one model (GPT-2 Medium), one task (detoxification), one layer (ℓ=8). No comparison to influence-based methods (e.g., directly removing influential training examples). No hyperparameter search. The ResNet-50 spectral experiment (Figure 3) tests whether the spectral direction differs from random, not whether it produces a good steering direction. No comparison to CAA or other steering methods on vision tasks.

### Minor

6. **Theorem 6.1 (Rademacher bound) treats IAS as a weight perturbation, but IAS is defined as an activation perturbation.** The theorem describes the model as f_θ + αUV^⊤ (a rank-k weight change), with the sketch claiming "IAS changes only a rank-k submatrix of the layer weight." This connection from activation perturbation to weight perturbation is not explained. The bound may still hold, but the derivation path is unclear.

7. **Theorem 4.2 and Corollary 1 need more rigorous justification.** The "idea of the proof" for Corollary 1 is circular as written: it assumes the result (‖ρ_s‖₁ = |α|) to prove minimality. A proper proof (presumably in the appendix) is needed.

### Trivial

8. **Lemma 5.4** rewrites γ₁γ₂ as √(1-(1-γ₁²))√(1-(1-γ₂²)), which is an identity since √(1-(1-γ²)) = γ. While not incorrect, this is an unnecessarily convoluted way to state γ₁₂ ≥ γ₁γ₂.

## Nice-to-Haves

- Adding error bars/confidence intervals to all experiments.
- Evaluating on additional models (e.g., LLaMA) and tasks (e.g., sentiment steering) to demonstrate generalizability.
- Comparing against influence-based baselines for data attribution (TracIn, etc.) in the data-provenance workflow.
- Moving the toy linear example from Appendix C to the main paper to illustrate the algebra.

## Removed Points

- **Criticism about missing appendix content (proofs, toy example):** Removed per instructions — the parser strips these sections; they exist in the original submission.
- **Criticism about not citing Basu et al. (2021) properly:** The reference appears in the bibliography (line 435-436). The paper mentions influence function limitations indirectly (damped Hessian, Gauss-Newton surrogate). The reviewer's claim is inaccurate.
- **Criticism that Lemma 5.4 is "either trivial or misstated":** Removed. The inequality γ₁₂ ≥ γ₁γ₂ is a meaningful composability result; the algebraic identity that follows is just an alternative expression and does not invalidate the lemma.
- **Strength Finder claims about the paper being "the most important piece of evidence" etc.:** Removed as overly promotional/redundant.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fix equation (2) to read Δh* = J_{h→y}^† J_{θ→y} Δθ, consistent with Theorem 5.2.
2. Investigate and explain the slope of 1.5 in Figure 1 — is it due to damping λ, the Gauss-Newton approximation, or genuine higher-order effects?
3. Provide at least one end-to-end example of the data-provenance workflow: pick a steering vector, compute ρ_s, show top-5 most influential training examples, and verify that removing/down-weighting those examples produces a similar behavioral change.
4. Add confidence intervals and statistical significance to all experimental results (Table 1, Figure 1, Figure 2).
5. Expand experiments to at least one additional model family and one additional task to demonstrate generalizability.
6. Discuss the IAS vs. CAA comparison honestly, explaining the trade-off between performance and the additional attribution capability.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| I3IeAZvxB4 | 3.33 | R1 | Painless Activation Steering — weaker theory and experiments; our paper is stronger |
| KYaNRqJ7ho | 4.50 | R1 | Z0-Inf influence functions — comparable empirical limitations but less theoretical depth |
| EDPvNhTOLK | 6.00 | R1 | Directional Influence Function — stronger experimental validation of the core method |
| 8epkNiuAQC | 4.67 | R1 | Influence Dynamics — theory-driven with similar practical gap issues |
| guSVafqhrB | 4.67 | R2 | Fine-Grained Activation Steering — broader experiments, weaker theory |
| dGQubVJQx6 | 5.00 | R2 | Concept Identifiability — theoretical focus, limited experiments |
| J4GYMiE3JT | 6.50 | R2 | Structural Inference — stronger theory-experiment integration |

**Round-1 bracket:** 4.5–6.5  
**Round-2 narrowing:** The paper is stronger than the Fine-Grained Steering anchor (4.67) on theory but weaker on experiments and has more unresolved issues. It is weaker than the DIF anchor (6.00) in experimental rigor. Placed at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>