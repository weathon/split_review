Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proves a first-order equivalence between activation steering and influence functions. It shows that any infinitesimal steering vector can be represented as a signed weighting over training data (and vice versa), providing a closed-form duality (Theorem 4.2). The paper derives: (i) a geometric alignment diagnostic γ that predicts when steering can match influence (Theorem 5.1); (ii) spectral optimality giving the best steering direction under a norm budget (Theorem 5.3); (iii) generalization bounds for low-rank steering (Theorem 6.1); and (iv) a no-free-lunch theorem showing when steering is provably insufficient (Theorem 6.2). Experiments on GPT-2 Medium detoxification compare the proposed Influence-Aligned Steering (IAS) to Contrastive Activation Addition (CAA).

## Strengths

- **Closed-form duality between steering and influence (Theorem 4.2).** The paper proves that any steering vector can be exactly reproduced by a signed measure over training data, and conversely, providing the first direct mathematical link between these previously separate techniques. The construction (ρ_s) and residual bound are explicit and actionable.

- **Geometric alignment diagnostic with theoretical guarantees (Theorem 5.1).** The relative logit error of optimal steering is bounded by √(1−γ²), where γ is the smallest principal-angle cosine between activation and parameter Jacobian subspaces. This yields a cheap, actionable pre-check (two backward passes) telling practitioners when steering can succeed.

- **Spectral optimality result (Theorem 5.3).** Under an ℓ₂ norm budget, the steering vector maximizing expected first-order logit change is the top eigenvector of a Fisher-influence matrix Σ. This provides a principled alternative to hand-crafted steering directions, with a scalable power-iteration estimator.

- **No-free-lunch theorem (Theorem 6.2).** If γ ≤ ρ < 1, no activation-space edit can achieve more than a factor ρ of the logit displacement achievable by a weight-space perturbation. This formalizes when steering is provably insufficient.

- **Empirical verification of first-order linearity.** Over 5000 prompt-token pairs, predicted vs. actual logit shifts from IAS have cosine 0.978, supporting the core equivalence claim in the directional sense.

- **Layer-depth alignment trend (Figure 2).** The diagnostic γ monotonically increases from 0.64 (layer 0) to 0.94 (layer 11) in GPT-2 Medium, consistent with the theory that later layers provide better subspace overlap.

## Weaknesses

### Fatal

None.

### Major

- **Anomalous perplexity values (Section 7.1, Table 1).** The reported baseline perplexity on WikiText for GPT-2 Medium is 14,333. Typical GPT-2 Medium perplexity on WikiText is ~20–30; the reported value is ~500× too high. The steered variants (13,291 and 13,701) are similarly anomalous. This suggests a systematic evaluation bug — possibly an incorrect metric computation (e.g., mean loss rather than exponentiated mean) or a corrupted/miniscule evaluation set. While the toxicity comparison (mean) may still be internally consistent, the perplexity values are uninterpretable and erode confidence in the experimental setup.

- **Core practical workflow is not demonstrated.** The paper repeatedly claims (Abstract, Section 4.1, Corollary 1) that IAS provides a constructive algorithm to map steering vectors back to causal training examples via the signed measure ρ_s. Section 4.1 promises "see Section 7" for this demonstration, but Section 7 never computes ρ_s or verifies that top-weighted examples are causally related to the undesired behavior. The central practical payoff of the duality — closing the loop from steering to data attribution — remains purely theoretical. This is a significant gap for a paper that motivates its contribution through this workflow.

- **Spectral optimality experiment does not test steering (Section 7.4).** Theorem 5.3 claims the top eigenvector of Σ maximizes expected first-order logit change under a norm budget. The experiment (Figure 3) tests whether the spectral radius of Σ is significant under label permutation (p=0.00498). This validates that Σ has non-random structure, but it does not test whether steering with the estimated eigenvector *actually achieves larger logit changes* than random directions. The headline implication of the theorem — optimal steering — is left unvalidated.

### Minor

- **Slope of 1.5 in Figure 1 is reported but not discussed.** The first-order equivalence experiment shows cosine 0.978 (supporting the core directional claim) but slope 1.50 — meaning the actual logit shift is 50% larger than predicted. The paper describes this as "consistent with the expected linear regime" without discussing the systematic magnitude discrepancy. This should be addressed (e.g., by sweeping α to characterize the small-edit regime boundary, or noting that slope ≠ 1 can arise from uncalibrated influence magnitude ϵ vs. steering magnitude α).

- **Limited model and task scope.** Main experiments use only GPT-2 Medium on detoxification. The spectral experiment uses ResNet-50. No results are shown for more recent architectures (LLaMA, Mistral, Gemma) or additional tasks beyond toxicity reduction, limiting generalizability claims.

- **No runtime or memory benchmarking.** The paper claims IAS requires only "two backward passes per input" and a rank-d pseudoinverse (Section 2) and is computationally efficient, but no wall-clock time or memory measurements are provided against baselines (CAA, influence functions).

- **γ diagnostic shown for only one model.** The layer-depth alignment trend (Figure 2) is only shown for GPT-2 Medium. Testing γ across other architectures would strengthen the claim that this diagnostic is broadly useful.

- **No ablation on damping parameter λ.** The spectral direction depends on (H + λI)⁻¹, but the paper does not investigate how λ affects the steering direction or the optimality claim.

- **No error bars or variance for γ measurements.** Figure 2 shows only median γ across prompts; variability across inputs is unknown.

### Trivial

None.

## Nice-to-Haves

- The paper could characterize the "small-edit" regime by sweeping α and measuring where the first-order approximation degrades.
- A small-scale experiment (e.g., on a linear model) directly validating that ρ_s from a steering vector matches influence-based data attribution would ground the duality claim.
- An ablation on the damping parameter λ for the spectral direction would strengthen Theorem 5.3.

## Removed Points

- **"Influence functions are never actually run":** REMOVED (factually incorrect). The paper does compute influence functions — they are used as the "predicted" values in Figure 1. The predicted logit shifts Δy^IF(x) = J_{θ→y}(x) Δθ_ε are generated from the influence function formula and compared against the actual IAS steering shifts.

- **Missing related works:** REMOVED per instructions (no external source to verify existence of claimed omissions).

- **"No discussion of when Im(J_{θ→y}) ⊆ Im(J_{h→y}) fails":** The paper extensively discusses this through γ and Theorem 5.1. The alignment diagnostic is the centerpiece. PARTIALLY ADDRESSED.

- **"Formatter/typo nitpicks" and "appendix missing":** REMOVED (parser artifacts, not author errors).

- **"Method soundness concerns about missing proofs in appendix":** REMOVED (appendix is stripped by parser; content exists in original submission).

## Novel Insights

The reviews surface a sharp disconnect between the quality of the theoretical contribution and the quality of the experimental validation. The harsh critic accurately identifies three concrete problems in the experiments (anomalous perplexity, slope ≠ 1, missing data-attribution validation) that are verifiable from the paper text. But several of the critic's more sweeping claims are either factually wrong (influence functions are never run) or speculative (the slope of 1.5 being framed as contradicting linearity despite cosine 0.978). The Strength Finder, meanwhile, correctly identifies the theoretical strengths but misses that the central practical workflow is not actually demonstrated. The net picture is a paper with a genuinely novel and well-executed theoretical core that is let down by incomplete experiments that fail to validate the paper's own headline claims.

## Suggestions

1. **Fix the perplexity evaluation.** The reported values (14,333 baseline on WikiText for GPT-2 Medium) are clearly wrong. Debug the evaluation pipeline and re-run.
2. **Demonstrate the data-attribution workflow.** Take a steering vector for toxicity, compute ρ_s, and verify that top-weighted training examples are causally related. This is the paper's signature practical claim and must be shown.
3. **Validate spectral optimality via actual steering.** Compute the top eigenvector of Σ, apply it as a steering vector, and measure logit changes against random directions. Show that it outperforms baselines.
4. **Discuss the slope discrepancy.** Explain why the fitted slope is 1.5 (not 1.0) in Figure 1. A sweep over α would help characterize the linear regime boundary.
5. **Add experiments on larger/current architectures** (e.g., LLaMA-3, Mistral) to demonstrate generalizability beyond GPT-2 Medium.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Painless Activation Steering (I3IeAZvxB4) | 3.33 | R1 weak | This paper has far stronger theory |
| Belief Dynamics Unify ICL and Steering (XyQ5ui62mm) | 4.50 | R1 mid | Similar unification ambition; current paper has cleaner, more rigorous theory |
| Dynamically Scaled AS (wMtS3brldm) | 5.00 | R2 | Practical steering method; current paper has stronger theory but less thorough experiments |
| ODESteer (CFewUmgIIL) | 5.00 | R2 | Comparable: unified theoretical framework with moderate experiments. ODESteer was accepted at this score with experiments on multiple models |
| Fine-Grained AS (guSVafqhrB) | 4.67 | R2 | More practical contribution; current paper has deeper theory |
| Steering MoE (v5Yl9V8rJs) | 5.50 | R2 | Practical MoE steering; accepted with strong experiments across 6 LLMs |
| Towards a Unified View (JenMBia97B) | 5.50 | R2 | Similar unification framing; rejected due to methodological issues |
| COLD-Steer (afV4qzquBN) | 6.00 | R2 | Strong theory + comprehensive experiments; accepted. Current paper has comparable theory but weaker experiments |
| Activation Steering with PID (vzkEX2SwFD) | 6.00 | R2 mid | Control-theoretic steering; accepted with experiments on multiple models and tasks |
| Directional Influence Function (EDPvNhTOLK) | 6.00 | R1 mid | Influence function extension; strong theory + moderate experiments |

**Round 1 bracket:** 3.5–7.5, narrowed to 4.5–6.5.

**Round 2 narrowing:** The paper sits between ODESteer (5.00, accepted) and COLD-Steer (6.00, accepted). Its theoretical contribution is stronger than ODESteer's, but its experiments are notably weaker — limited to GPT-2 Medium with a perplexity bug, while ODESteer ran on Falcon-7B, Mistral-7B, and Llama-3.1-8B. The core practical workflow is not demonstrated. At the same time, the theory is clearly stronger and more original than the Belief Dynamics paper (4.50, rejected).

**Final score:** 5.0. The paper's theoretical contribution is genuinely novel and well-executed, with multiple theorems that provide a clean unification. However, the experimental validation is insufficient — especially the anomalous perplexity values, the missing data-attribution demonstration, and the unvalidated spectral optimality claim. These gaps prevent the paper from meeting its own stated ambitions. The theoretical core merits attention, and the issues are fixable, but the paper in its current form overclaims what has been empirically validated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>