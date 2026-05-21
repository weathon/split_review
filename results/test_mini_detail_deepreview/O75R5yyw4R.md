Now I have all the evidence I need. Let me construct the final consolidated review.

## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward reward-aligned distributions. The method is evaluated across two language backbones (MDLM, LLaDA-8B) and one image backbone (MaskGIT) with multiple reward functions, achieving consistently strong results across tasks. The paper further provides insightful analysis of effective timesteps and the iteration-vs-particle tradeoff.

## Strengths

- **Novel and principled method tailored to discrete diffusion.** The core idea — using noising-denoising as an MCMC proposal within a Metropolis framework to enable iterative refinement of intermediate states — directly addresses the unique challenge of discrete diffusion where tokens are fixed once generated and gradients are unavailable. This contrasts with prior work that searches over trajectories (DSearch, DTS) or propagates multiple particles (SMC, FK), offering a genuinely different approach to test-time scaling.

- **Consistent performance advantage across tasks, backbones, and modalities.** Figure 2 shows IterRef outperforming FK, SVDD, SoP, and BoN on Toxicity, Sentiment, CoLA, and Perplexity with both MDLM and LLaDA-8B, often achieving higher reward at 2T–4T NFEs than baselines achieve at 32T NFEs. Table 1 further demonstrates a clear lead on MaskGIT with CLIPScore (e.g., 35.8 vs. 34.8 for the nearest baseline at NFE=16). This consistency across two very different discrete diffusion architectures and two modalities (text + image) makes the empirical case compelling.

- **Genuinely insightful analysis of discrete diffusion dynamics.** Table 2 systematically shows that later denoising stages (0.1T) are far more impactful than early stages (0.9T) — a finding that differs from continuous diffusion where early steps dominate content. Table 3 reveals that increasing iteration depth \(k\) consistently outperforms increasing particle count \(N\) at equal compute, directly justifying the paper's core design choice of iterative refinement over trajectory search. These analyses provide actionable insights beyond the method itself.

- **Practical engineering contributions reduce computational cost.** The choice of balancing function (Eq. 2) eliminates the auxiliary sampling step, and the pool-reuse strategy avoids regenerating candidates on rejection. These are non-trivial implementation details that make MTM tractable for 8B-parameter models.

## Weaknesses

### Fatal

None.

### Major

1. **No measure of variance or statistical significance for any experimental result.** All figures and tables report only point estimates (typically means over 20 generations per prompt, 15 prompts). The paper does not report standard deviations, confidence intervals, or error bars anywhere. Given the inherent variability in language generation and the modest prompt counts, it is impossible to assess whether the reported improvements are reliable. For example, in Figure 2(b) Sentiment with LLaDA, IterRef and FK curves appear to overlap at several NFE levels; without variance information, the claimed advantage cannot be evaluated. While reporting error bars on every point may not be standard in all settings, the lack of any variance information — not even per-seed standard deviations despite using 3 seeds — is a significant evidential gap that should be addressed.

2. **The reversibility assumption in Proposition 1 is stated without justification or discussion.** Proposition 1 claims convergence to the optimal distribution "Assume that \(q\) and \(p_\theta\) form a reversible Markov kernel." However, the paper provides no argument that trained discrete diffusion models satisfy this property, nor does it discuss whether the MTM sampler remains approximately valid when reversibility is violated. This is not fatal — the paper is correctly explicit about the assumption — but it weakens the theoretical contribution because the reader cannot gauge whether the convergence guarantee applies in practice. The paper would be strengthened by an empirical check (e.g., testing detailed balance on proxy distributions) or at least a discussion of why this assumption is reasonable for absorbing-state diffusion models.

### Minor

3. **Ethics Statement contains an apparent inconsistency.** The Ethics Statement says the work "intentionally includes experiments that increase the toxicity of generated text in order to stress-test discrete diffusion-based language models." However, all main-body experiments involving toxicity are about *reducing* toxicity (detoxification, Section 4.5) or using a Toxicity reward that penalizes toxic content (Section 4.2). If the stress-test experiments exist only in the appendix, the main text should cross-reference them; as presented, the statement is misleading about the paper's actual content.

4. **Baseline hyperparameters may not be optimally configured for each backbone.** The paper states that "hyperparameters for baselines are favorably configured by following the original papers" (Section 4.1). Following original settings is reasonable, but different backbones (MDLM vs. LLaDA-8B) could benefit from different configurations. A brief sensitivity study or validation-set tuning would strengthen the comparison fairness, though given that IterRef still outperforms baselines by large margins, this is unlikely to change the overall conclusions.

### Trivial

None.

## Nice-to-Haves

- **Pareto frontier visualization.** Figure 2 shows reward vs. NFE but does not explicitly mark Pareto-optimal points. A table or figure identifying the Pareto frontier would directly support the "more effective scaling" claim.

- **Wall-clock time analysis in main text.** The paper notes that NFE conflates generative-model calls and reward-model calls, which have different relative costs depending on model scale, and defers wall-clock analysis to the appendix. A brief summary of the key conclusion in the main text would preempt fairness concerns.

- **Intuitive explanation of why the chosen balancing function yields uniform importance weights.** The paper says "the derivations are provided in Appendix D.2" (which was stripped by the parser). A short intuitive sketch in the main text would help readers understand why the specific forms in Eq. (3) emerge.

## Removed Points

These points were raised by the reviewers but are removed per the filtering rules; they are listed here only for completeness.

- **Criticism that the derivation of the acceptance ratio is deferred to the appendix.** The parser strips appendix content from all papers; the derivation exists in the original submission. This is a presentation-choice, not a missing-argument issue.
- **Request for missing proofs.** Same reason — the parser strips appendices.
- **Criticism about "8x faster" not being sufficiently qualified.** The paper already uses "up to 8×" wording and specifies the setting (MDLM on Toxicity at a specific threshold). The qualification is adequate.
- **Criticism that the balancing function role is not explained intuitively.** The paper does state: "Intuitively, the importance weight \(w_n\) corresponds to uniform sampling over the proposals, while the acceptance rate \(\beta\) ensures that the overall procedure converges toward reward-aligned sampling." This provides the needed intuition.
- **Criticism about pool reuse validity (auxiliary sample not drawn from K).** The paper addresses this: "Since the candidates were already drawn i.i.d. from the same transition kernel, the pool remains a valid proposal set." This is a defensible claim.
- **Formatting/presentation nitpicks.** Parser artifacts, not author errors.

## Novel Insights

The most novel insight emerging from the cross-referencing of the reviewers is that **the analysis of effective timesteps (Table 2) — showing later stages matter more for discrete diffusion — is stronger evidence for the paper's core claim than any single performance number.** The harsh critic correctly identifies this as "the most credible evidence," since it studies monotonic trends rather than point estimates, and the strength finder flags it as a genuinely novel finding that contradicts continuous diffusion intuition. The convergence of these two perspectives suggests that the paper's analytical contributions (Section 4.4) are its most robust and distinctive feature, even more than the already-strong performance numbers.

## Suggestions

1. **Add confidence intervals or error bars to all main results.** Given the modest prompt set (15 prompts, 20 samples each), bootstrapped confidence intervals or per-seed standard deviations would add substantial credibility to the quantitative claims.

2. **Empirically verify or discuss the reversibility assumption.** Even a simple diagnostic on a small-scale proxy would greatly strengthen the convergence claim.

3. **Resolve the Ethics Statement inconsistency.** If toxicity-increasing experiments exist in the appendix, add a cross-reference; otherwise, correct the statement to match the main paper content.

## Score and Decision

**Calibration anchors consulted across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DDPP (Ombm8S40zN) — Steering MDMs via posterior prediction | 6.25 | R1, R2 | Same domain (discrete diffusion steering). DDPP requires training a secondary model; IterRef is test-time only. DDPP has cleaner theory (three well-motivated variants), but IterRef has broader cross-modality results and a more novel algorithmic idea. Comparable quality. |
| Guidance for discrete diffusion (XsgHl54yO7) — CTMC-based guidance | 6.50 | R2 | Both address guidance for discrete models. Reviewer feedback noted "weak innovation" as the guidance method was seen as a straightforward extension. IterRef's core idea (MTM with noising-denoising) is more original. IterRef has stronger empirical validation across more diverse settings. IterRef is slightly stronger. |
| SDDS (peNgxpbdxB) — Scalable discrete diffusion samplers | 6.00 | R1, R2 | Memory-efficient training for discrete diffusion. Accepted but noted for limited empirical validation. IterRef's experiments are more extensive. IterRef is at least as strong. |
| SVDD (2fgzf8u5fP) — Soft value-based decoding | 3.80 | R1 | Rejected due to concerns about baseline fairness, alpha setting, and bias. IterRef has a cleaner methodology and avoids these issues. IterRef is substantially stronger. |
| DNO (x1uv2gdjKV) — Direct noise optimization | 5.50 | R2 | Inference-time alignment. Rejected due to missing baselines and reward hacking concerns. IterRef has broader validation and more principled approach. IterRef is clearly stronger. |
| Planned Denoising (MJNywBdSDy) — Planner+denoiser for discrete diffusion | 5.75 | R2 | Accepted but noted for computational cost and clarity issues. IterRef has better cross-modality results. IterRef is slightly stronger. |
| DRaFT (1vmSEVL19f) — Direct reward fine-tuning | 6.00 | R2 | Accepted. Different approach (requires training). DRaFT benefits from more thorough ablations. IterRef's novelty is higher. Comparable quality. |

**Initial bracket (Round 1):** Between approximately 3.5 and 7.5, with the paper sitting above the rejected anchors (~3–4) and within the band of accepted discrete-diffusion steering/guidance papers (5.75–6.50).

**Narrowing (Round 2):** The paper is closest to the cluster of accepted papers scoring 5.75–6.50 (DDPP, Guidance, SDDS, Planned Denoising). It is clearly stronger than the rejected papers (SVDD, DNO) but does not reach the 8+ level of the continuous-diffusion acceleration papers (Shortcut Models, Consistency Models), which address a more mature area with more polished exposition and exhaustive experiments.

**Final score relative to anchors:** Slightly above the median of the Round-2 anchors. Comparable to DDPP (6.25) and stronger than Planned Denoising (5.75) and SDDS (6.00), but below the 8+ tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>