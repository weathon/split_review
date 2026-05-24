Now let me finalize the review. I have all I need from reading the paper and comparing against calibration anchors. Let me compile the final review.

## Summary

HiSo proposes a Hessian-informed zeroth-order federated learning method that accelerates convergence while preserving the scalar-only communication property critical for efficient LLM fine-tuning. The key idea is to learn a diagonal Hessian approximation from the scalar updates already transmitted in the ZO-FL protocol — requiring zero additional communication. The paper provides a generalized scalar-only FL framework, a convergence theory that yields the first dimension-independent rate for ZO-FL under whitening assumptions, and empirical results showing 1.4–5.4× speedup over the prior state-of-the-art DeComFL across multiple LLM benchmarks.

## Strengths

- **Elegant core idea with strong motivation:** The paper identifies a genuine tension — curvature information accelerates convergence but transmitting it violates the scalar-only communication constraint — and resolves it by showing that the Hessian approximation can be built from already-transmitted scalar updates. The derivation in Section 4.1 connecting the least-squares ascent direction problem to the Hessian-informed ZO update (Eq. 5–10) is clean and well-justified.

- **Novel theoretical contribution:** Theorem 1 and its corollaries provide the first convergence analysis for Hessian-informed ZO-FL, and Corollary 3 extends the analysis to multiple local updates — something DeComFL's analysis does not support. The whitening analysis in Section 5.1 (Table 1, Figure 4) gives a plausible and rigorously developed explanation for why ZO methods can converge much faster than the pessimistic O(d) bound.

- **Strong empirical validation at scale:** Table 2 demonstrates 1.4–5.4× communication-round speedup over DeComFL when fine-tuning OPT models up to 2.7B parameters on SST-2, QQP, and SQuAD. Table 3 shows HiSo achieves the best accuracy among all ZO baselines while maintaining the lowest total communication cost, and the gap widens with model size.

- **Generalized framework (Algorithm 1):** The paper abstracts the scalar-only communication paradigm beyond ZO-SGD, decoupling the dimension-free property from any specific optimizer. This is a useful conceptual contribution that enables future work to plug in other optimization strategies.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Hessian update ambiguity in Section 4.2:** Two different update equations are presented — one using per-client Δx_{r,τ}^{(i)} and Eq. (12) referencing Δx_{r,0}. The simplified case in Section 4.3 (which uses the global aggregated Δx_t) shows the intended mechanism is consistent and communication-free, but Section 4.2 should be clarified to match. This does not invalidate the core claim, but the presentation creates unnecessary confusion about a central component of the method.

- **Theory-to-practice gap in step-size condition:** Theorem 1's step-size bound includes √(1/L(d+2)), which is dimension-dependent. While the corollaries establish dimension-independent rates under the whitening assumption, the paper does not discuss whether the learning rates used in the LLM experiments satisfy the theoretical condition or whether this condition is a proof artifact. A brief discussion would strengthen the bridge between theory and experiments.

- **Well-approximated Hessian condition is assumed, not proven:** The accelerated rates in Corollaries 1–3 require the learned H to satisfy the well-approximated condition (Definition in Section 5.1). The paper honestly acknowledges this limitation and notes that worst-case performance degrades to DeComFL, but the gap between the assumed condition and the actual update rule (Eq. 12) remains uncharacterized. The MNIST experiment (Figure 5) provides suggestive evidence through the learned H distribution, but a more direct validation — even on a small-scale problem where the true Hessian is computable — would strengthen the argument that the update rule actually produces a well-approximated H.

- **Experimental details deferred to appendix:** The LLM fine-tuning experiments do not specify τ (local steps), μ (smoothing parameter), or learning rate schedules in the main text. While these are presumably in the appendix, core experimental parameters should be summarized in the main paper.

### Trivial

None.

## Nice-to-Haves

- Reporting final converged accuracy for both HiSo and DeComFL (not just rounds-to-match-DeComFL) would give a fuller picture of whether HiSo also achieves a higher accuracy ceiling, not just faster convergence.
- A small-scale experiment comparing the learned H to the true diagonal Hessian (where computable) would provide direct evidence for the well-approximated condition.
- The generalized framework (Algorithm 1) would benefit from a concrete walkthrough showing how HiSo instantiates each step, rather than deferring the full algorithm entirely to the appendix.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim that the Hessian synchronization is fundamentally broken:** The simplified case in Section 4.3 demonstrates that the Hessian is updated using the global aggregated Δx_t, which both server and clients can reconstruct from the broadcast scalar g_t and shared seed. The ambiguity in Section 4.2 is a presentation issue, not a logical inconsistency. The core mechanism is sound.

- **Harsh critic's claim about "missing related works":** Per the rules, I do not introduce missing references as I have no external source to verify them.

- **Strength Finder's generic strengths** about "important problem" or "interesting research question" are removed as they are non-specific.

- **Harsh critic's concern about "whether full model fine-tuning or parameter-efficient method was used":** The paper clearly targets full-model fine-tuning (the communication savings are computed against full-model transmission), and the method operates on all parameters. This is not ambiguous.

- **Harsh critic's nitpick about "up to 90 million times communication savings" needing byte-level anchoring:** This is a presentation preference, not a weakness.

## Novel Insights

The whitening analysis in Section 5.1 and the definition of the "low whitening rank" ζ provide a genuinely new lens for understanding ZO gradient variance. Prior work used the low-effective-rank assumption (Lκ) to tighten the O(Ld) bound, but the paper shows that a learned diagonal preconditioner can further reduce the variance to a quantity ζ that can be dramatically smaller than both Ld and Lκ (Figure 4). The connection to Wiener filtering is insightful and not present in prior ZO-FL work. This analysis independently explains both why the method works and why ZO methods can be surprisingly effective on LLMs.

## Suggestions

- Resolve the Hessian update ambiguity by stating explicitly in Section 4.2 that the update uses the global aggregated Δx_r (as shown in Section 4.3), and note that the server and all clients can compute this identically from the broadcast scalar g_r. Remove or reconcile the per-client equation.
- Add a sentence in Section 5.2 discussing whether the step-size condition √(1/L(d+2)) is practically binding or an artifact of the proof, and whether the learning rates used in experiments satisfy it.
- Summarize the key experimental hyperparameters (τ, μ, learning rate) in a short table or a sentence in the main text for LLM experiments.
- Consider adding a small-scale experiment (e.g., on MNIST or a toy problem) directly comparing the learned H to the true diagonal Hessian to validate the well-approximated condition.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| omrLHFzC37 (DeComFL) | 6.25 | 1 | HiSo directly builds on and improves this method; clearly stronger |
| GYik1jT3gE (Initialization Matters) | 7.00 | 2 | Similar tier — strong theory with some limitations; HiSo has broader empirical validation |
| puTxuiK2qO (AdaFisher) | 6.25 | 2 | Similar diagonal preconditioning idea but single-node; HiSo addresses harder FL setting with stronger theory |
| ZuazHmXTns (PAdaMFed) | 7.60 | 1 | Strong execution, clean theory; HiSo is in the same quality band with minor presentation issues |
| GtlRN48XYA (FeDeRA) | 3.00 | 1 | Weak anchor — HiSo is far stronger |
| p4RAKZ4oik (FedDTPT) | 3.00 | 1 | Weak anchor — HiSo is far stronger |
| pLyjsv1KWH (FedCDD) | 3.00 | 1 | Weak anchor — HiSo is far stronger |
| ArJikvI6xo (GFLAgent) | 3.40 | 1 | Weak anchor — HiSo is far stronger |
| kjn99xFUF3 (FedDA) | 6.00 | 2 | HiSo is stronger — more novel setting, better empirical results |
| ipQrjRsl11 (FL ADMM-Bayes) | 6.20 | 2 | HiSo addresses a more impactful problem with broader validation |
| FK8tl47xpP (Greedy L2O) | 6.25 | 2 | Different domain; HiSo has clearer practical impact |

**Round 1 bracket:** The paper sits between the strong DeComFL anchor (6.25) and the PAdaMFed anchor (7.60), with the "Initialization Matters" paper (7.00) as a natural comparison point.

**Round 2 narrowing:** The round-2 anchors in the 6.0–7.5 range confirm HiSo is clearly above the 6.0–6.25 cluster (FedDA, AdaFisher, DeComFL) and comparable to the 7.0 anchor (Initialization Matters). HiSo's combination of novel methodology, strong theory, and large-scale empirical validation places it at this level. The presentation ambiguity in Section 4.2 prevents it from reaching the 7.5+ tier where execution is nearly flawless (e.g., PAdaMFed at 7.60).

**Final score:** 7.0 — the paper makes a clear, well-supported contribution with minor presentation issues that can be addressed in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>