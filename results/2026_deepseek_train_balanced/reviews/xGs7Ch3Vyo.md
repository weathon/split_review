Now let me produce the final review.

## Summary
The paper introduces RAFT (Regression-Aware Fine-Tuning), a method for fine-tuning decoder-only LLMs on regression tasks. RAFT directly minimizes the squared error of the MALI predictor (the expected value under the model's output distribution), rather than using log-perplexity or separate predictive heads — aligning the fine-tuning objective with the evaluation metric while respecting the autoregressive pre-training objective. The paper provides theoretical analysis (Lemmas 1-3), a unified view of LLM regression approaches, and empirical results on Amazon reviews and STSB benchmarks.

## Strengths

1. **RAFT provably recovers the Bayes-optimal predictor despite operating on a restricted grid (Lemma 3).** Lemma 3 proves that the minimizer of the RAFT loss over a finite grid (e.g., {1,2,3,4,5}) yields the Bayes-optimal predictor over the full continuous space, provided the grid contains the min and max of the target range. This is a non-trivial and well-proven theoretical result that directly supports the method's principled design.

2. **Formal theoretical grounding for the misalignment of standard fine-tuning for regression (Lemmas 1-2).** The paper proves that log-perplexity fine-tuning combined with either standard decoding or MALI decoding can produce squared error arbitrarily close to (N/2)² even when the learned distribution deviates from the true distribution by an arbitrarily small ε in L1 distance. This is a genuine theoretical advance over prior work (Lukasik et al., 2024) that proposed MALI decoding but did not analyze fine-tuning misalignment.

3. **RAFT consistently outperforms all baselines across all reported settings (Table 3).** On Gemma-2 2B and 9B across five dataset splits, RAFT achieves the lowest RMSE in every setting. The advantage is often substantial (e.g., Music 2B: 0.50 vs 0.52 for predictive head and 0.88 for standard fine-tuning+MALI; Wireless 2B: 0.47 vs 0.51). Standard deviations (≤0.02) are small, indicating stable results across 3 runs.

4. **Ablations cleanly isolate the source of RAFT's advantage (Section 5.3).** The comparison of RAFT vs. learnable-RAFT (a more flexible learned predictor) vs. random initialization provides direct evidence that alignment with the pre-training next-token prediction objective — not predictor expressivity — drives RAFT's gains. Learnable-RAFT does not improve over RAFT, but RAFT collapses under random initialization, cleanly disentangling two competing explanations.

5. **Empirical validation of grid robustness, confirming Lemma 3 (Table 5).** RAFT performs well even with minimal grids (e.g., just the digit '5'), and the paper tests five different grid configurations. This provides strong empirical support for the theoretical claim that a coarse digit grid is sufficient.

## Weaknesses

### Major

- **The predictive head baseline is underspecified (Table 3, lines 268-269).** The main comparison table reports a single column "Predictive head," but the paper cites two distinct prior approaches: Fernandes et al. (2023) (final-token logit on a special token) and Zhuang et al. (2023) (mean pooling of output embeddings). It is never stated which variant (or both, selecting the better one) produced the results in Table 3. Since the paper's central claim (RAFT outperforms predictive head approaches) depends on this comparison, the ambiguity undermines reproducibility and interpretability. The paper should either specify which variant was used or report both separately.

### Minor

- **Scope claim exceeds what is demonstrated in the main body (Contributions §1, §5.1).** Contribution (iii) claims a "systematic comparison ... across multiple datasets and LLMs," and §5.1 states "We experiment with Gemma-2 and PaLM-2 instruction-tuned model families." However, only Gemma-2 results appear in the main body (Table 3). MovieLens-1M is listed as a dataset (§5.1) with no results shown in the main text. If these results exist in an appendix, the main body should reference them; if not, the scope claim should be narrowed. This is a presentation gap rather than a methodological flaw.

- **Limited hyperparameter search (§5.1).** Only two learning rates (1e-4, 1e-5) were tested for fine-tuning. Given the well-known sensitivity of LLM fine-tuning to learning rate, it is plausible that some baselines (especially standard fine-tuning and the predictive head) could improve with more extensive tuning, potentially changing the relative comparisons. A broader search would strengthen the claim of a "systematic" comparison.

- **Lemma 3's condition on grid coverage is not discussed in practice (§3.4).** Lemma 3 requires that the grid contains the min and max of the target range. The paper does not discuss how practitioners should select a grid satisfying this condition for regression problems where the target range is unknown a priori or potentially unbounded, limiting practical guidance.

### Trivial

None.

## Nice-to-Haves
- Statistical significance tests (e.g., paired comparisons) would clarify which differences in Table 3 are reliable given the variance, as some RAFT vs. predictive head differences are within 0.01 RMSE (STSB settings).
- An experiment with continuous or broader-range targets (beyond the 1-5 digit range) would substantiate the claim of general applicability, though Lemma 3 and the grid ablation partially address this.

## Removed Points
The following points raised by the reviewers were removed because they are not valid weaknesses upon verification against the paper:

- **Theoretical limitations being "existence results" not "general impossibility"**: The paper clearly states Lemmas 1-2 as existence proofs ("For any ε > 0, there exists P, p such that...") and uses appropriately measured language ("can cause," "can significantly deviate"). The framing is correct; this is not a weakness.
- **Statistical significance testing presented as a weakness**: Downgraded to nice-to-have; single-run evaluation with reported std devs is the norm for this setting.
- **Missing results from the "appendix"**: The parser strips appendices. Results claimed to exist in the paper may be in the appendix; noted as a main-body scope gap instead.
- **Non-digit targets / broader range**: Well-addressed by Lemma 3 and Table 5 grid ablation.
- **Computational cost of scoring the grid**: A 5-element grid imposes negligible overhead.
- **Generic "important problem" strengths from the Strength Finder**: Removed as not concrete to this paper's specific contributions.
- **The "experimental evaluation is substantially narrower than the paper claims" as a fatal/structural issue**: Merged into the minor scope claim gap; does not invalidate the core contributions.

## Novel Insights
None beyond the paper's own contributions. The two input reviews are largely convergent: they agree that RAFT is a clean, well-motivated, theoretically grounded method with consistent empirical support, and that the main weaknesses are about presentation scope and baseline specification rather than the method's validity.

## Suggestions
1. **Clarify the predictive head baseline in Table 3.** State explicitly which prior work's variant (Fernandes et al. final-token logit, Zhuang et al. mean pooling, or both) produced the reported numbers, and ideally report them as separate rows.
2. **Align the main body scope claims with what is presented.** Either (a) move PaLM-2 and MovieLens results into the main body, (b) add explicit "see Appendix" references, or (c) narrow the claims to match the Gemma-2/Amazon+STSB scope.
3. **Broaden the hyperparameter search** or report sensitivity to learning rate for the main comparisons to rule out the concern that baselines are undertuned.
4. **Add a brief discussion** of how practitioners can select a grid that satisfies Lemma 3's min/max condition for problems with unknown or unbounded target ranges.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>