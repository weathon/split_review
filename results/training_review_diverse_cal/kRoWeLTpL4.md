Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes CP-Fuse, an inference-time algorithm that adaptively fuses two language models (each trained on disjoint copyrighted subsets) to prevent regurgitation of protected content. The method uses a per-token convex optimization that yields a balancing property — neither base model dominates the generation — which empirically reduces exact-match substring length by 20–25× while preserving utility (pass@1, fluency). CP-Fuse also works as a wrapper for training-time mitigation methods like goldfish loss.

## Strengths

1. **Substantial and consistent reduction in copyright infringement across diverse metrics.** Table 1 shows CP-Fuse reduces exact-match substring length from ~1400 to ~70 characters (20–25×) compared to overfitted models, outperforming all baselines (SystemPrompt, MemFree, cpδ) on both code and text tasks. On code tasks, the JPlag plagiarism score drops from near 1.0 to 0.03. These results directly support the paper's central claim.

2. **Preservation of utility while cutting infringement.** Table 2 shows CP-Fuse maintains pass@1 on code benchmarks (APPS: 0.47, MBPP: 0.43, HumanEval: 0.28) at parity with overfitted models, while MemFree degrades significantly (APPS drops to 0.32). Story fluency on WritingPrompts is also preserved (2.17 vs. 2.17). This refutes the assumption of an inevitable protection–quality trade-off.

3. **Principled mechanism with empirical validation.** Lemma 3 (balancing property) provides a formal explanation of why CP-Fuse prevents domination by either model. Figure 2 experimentally confirms that cumulative log-likelihoods remain equalized during CP-Fuse generation, while cpδ lets one model dominate — directly validating the mechanism that distinguishes CP-Fuse from prior token-wise cpδ.

4. **Flexibility as a post-hoc wrapper.** Section 4.3 shows CP-Fuse applied atop goldfish-loss-trained models further reduces exact-match lengths (e.g., from 84.68 to 20.68 on one split), demonstrating compatibility with training-time strategies.

5. **Robustness against extraction attacks.** Section 4.4 shows that even with increasing prefix length, CP-Fuse's exact-match length stays ≤27 characters and BLEU below 0.04, confirming the balancing property prevents adversaries from forcing regurgitation via prompted prefixes.

## Weaknesses

### Fatal
None.

### Major

1. **The separability assumption is central but never stress-tested.** CP-Fuse's entire pipeline depends on constructing two disjoint copyrighted subsets. The experiments enforce this perfectly by partitioning a single dataset — every sample is treated as copyrighted and the splits are non-overlapping. This is the ideal scenario. In real-world deployment, copyrighted material (e.g., the same book, codebase, or infringing phrase) could appear in both splits, breaking the balancing property. The paper acknowledges this as future work (conclusion), but provides no empirical probe of how protection degrades as the assumption is gradually violated. Without such a stress test, claims about practical effectiveness are only validated under an idealized condition. The paper would be substantially strengthened by adding a controlled experiment (e.g., introducing 5–20% overlap between splits) to reveal the method's robustness boundary.

### Minor

2. **Theoretical framing overstates continuity with NAF.** The paper motivates CP-Fuse as "inspired by the k-NAF framework" and positions the per-token optimization (Equation 2) as an approximation of the global NAF objective. However, Equation 2 is a *new* per-token formulation rather than a derived approximation of the global KL-minimization — it is introduced ad hoc, and the resulting balancing property is a consequence of this specific formulation, not of any provable NAF guarantee. The paper does not claim to satisfy the NAF bound, but the surrounding framing ("inspired by," "principled theoretical explanation") implies a tighter continuity than actually exists. Clarifying what CP-Fuse guarantees (the balancing property) and what it does not (any quantitative bound on regurgitation) would strengthen the paper's theoretical contribution on its own terms rather than by association.

3. **Utility evaluation lacks a full-data baseline.** CP-Fuse combines two models each fine-tuned on 3k examples. The paper compares utility (pass@1, fluency) against the individual 3k models, but never against a single model trained on the full 6k dataset (which would be the natural baseline for "how much utility is sacrificed for protection"). CP-Fuse preserves utility relative to the half-models, but may underperform a model with access to all the training data. Including this baseline would contextualize the utility cost of CP-Fuse's protection mechanism and strengthen the "does not compromise quality" claim.

4. **Computational cost is not quantified.** The grid search over α and β is performed per token, which carries real inference-time overhead. The paper does not report tokens/second or relative latency compared to a single model. This information is important for practitioners evaluating the method's practicality.

### Trivial

5. **"Average value above the 95th percentile" is ambiguous.** The paper reports metrics "averaged at the 95th percentile" — it is unclear whether this means (a) computing the 95th percentile of the per-sample distribution and averaging values at or above that threshold, or (b) averaging only the top 5% of values.

6. **Grid search discretization details relegated to appendix.** The paper mentions the grid ([0,2) in 10 steps, [2,10] in 9 steps) only briefly and defers justification to the appendix. A sentence explaining why performance saturates beyond ~10 steps would help readers assess the cost–benefit trade-off without consulting the appendix.

## Nice-to-Haves

- A brief discussion of when CP-Fuse *might* produce garbled or incoherent output — e.g., when both base models assign high probability to sharply conflicting tokens, the averaged distribution could be flat. The paper notes that CP-Fuse "generates tokens that are consistent with at least one of the two combined models" (line 372), which addresses the concern implicitly, but an explicit failure-mode analysis would improve completeness.
- A dedicated limitations paragraph in the main text (beyond the brief mention in the conclusion) discussing sensitivity to grid discretization, number of models, divergence function choice, and the separability assumption.

## Removed Points

- **"The examples in Appendix C (presumably) suggest no such degradation"** — This is speculative about the content of the appendix, which is not visible in the extracted text. Removed as conjecture.
- **"The paper does not explore whether CP-Fuse itself introduces any analogous failure modes"** — This is partially addressed by the paper's explicit statement (line 372) that CP-Fuse "generates tokens that are consistent with at least one of the two combined models," and by the qualitative examples showing no degradation. Moved to Nice-to-Haves.
- **The critique about "missing appendix" content** — Per the hard rules, appendix sections are stripped by the parser; they exist in the original submission.

## Novel Insights

The reviews surface one genuinely useful observation not foregrounded in the paper: CP-Fuse's balancing property creates an *implicit adversarial defense* — even with increasing prefix length from a memorized story (Figure 4, Section 4.4), exact-match length stays essentially constant. This suggests the balancing mechanism functions as a hard constraint on regurgitation length that does not degrade with stronger extraction pressure, which is a stronger property than "it reduces memorization on average." The connection between the formal balancing property (Lemma 3) and this empirical saturation behavior under attack is worth making explicit.

## Suggestions

1. **Add a controlled stress test of the separability assumption.** Introduce 5%, 10%, and 20% overlap between the copyrighted splits and measure the degradation in protection metrics (EM length, BLEU, JPlag). This single experiment would dramatically increase the paper's practical relevance.
2. **Include a full-data utility baseline** — train a single model on the combined 6k examples (without protection) and report its pass@1/fluency. This directly answers "how much utility is sacrificed for protection."
3. **Explicitly decouple the NAF motivation from the CP-Fuse guarantees.** Restructure the theoretical framing to: (a) state the balancing property as the paper's own guarantee, (b) position the NAF framework as inspiration/context, and (c) clarify that no NAF bound is claimed.
4. **Report inference latency** (tokens/second) of CP-Fuse relative to a single model in a one-sentence addition to the experimental setup.

## Score and Decision

This paper presents a novel, well-motivated, and empirically validated method for inference-time copyright protection. The idea is clean, the experiments are carefully designed across multiple datasets and metrics, and the results convincingly demonstrate the core claims under the stated conditions. The main weakness — lack of empirical stress-testing of the separability assumption — is a genuine gap but does not invalidate the contribution, as the method's behavior in the ideal setting is a necessary first step. The paper acknowledges the limitation transparently.

**Originality:** Strong — adaptive model fusion for copyright protection is novel.  
**Importance:** High — timely problem with practical relevance.  
**Claims supported:** Mostly yes, with one caveat about the separability assumption.  
**Soundness:** Solid for the tested regime.  
**Clarity:** Well-written overall; one ambiguous metric description.  
**Value:** Positive contribution to the emerging inference-time copyright safeguards literature.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>