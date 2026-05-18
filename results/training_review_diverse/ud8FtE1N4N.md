Now I have thoroughly verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper studies sparse pre-training of LLMs and makes two main contributions. First, it proposes a unified scaling law that replaces the total parameter count in the Chinchilla law with the *average number of active parameters* during training, showing empirically that this modified law (Equation 2) fits 30 data points (3 model sizes × 5 sparsity levels × 2 training durations) with a mean absolute error of 0.016. Second, through a systematic search over 80 configurations, it identifies a simple schedule — 25% dense training, 50% iterative pruning, 25% sparse recovery — that achieves near-optimal final loss across sparsity levels and training durations for a 162M model, and finds that optimal hyperparameters transfer from dense pre-training.

## Strengths

- **Unified scaling law with empirical validation.** The central idea — that replacing total dense parameters with the average number of active parameters suffices to extend the Chinchilla law to sparse pre-training — is elegant and empirically supported. Figure 1 directly shows four sparse/dense model pairs with matching average active parameters achieving nearly identical final loss despite different training dynamics. The fitted law achieves a mean absolute prediction error of 0.016 across 30 diverse configurations (Section 5.3, Figure 3), which is competitive with the fit quality of the original Chinchilla law.

- **Systematic identification of a simple optimal schedule.** The paper evaluates 80 sparse pre-training configurations (Section 6.1) and identifies a clear prescription: allocate 25% of total compute to dense training, 50% to gradual pruning, and 25% to sparse recovery. This finding is robust across sparsity levels (20–80%) and training durations (10× and 20× Chinchilla-optimal) for the 162M model, and the optimal hyperparameters (learning rate, batch size) transfer directly from dense pre-training (Figure 5). This is actionable for practitioners.

- **Largest-scale study of sparse pre-training to date.** The largest model requires 4.5×10²⁰ FLOPs, over 5× the compute of the largest model in prior sparse pre-training scaling law work (Frantar et al., 2023). The study covers model sizes from 58M to 468M with up to 80% sparsity, substantially extending the empirical basis for sparse pre-training research.

- **Honest treatment of limitations.** The paper explicitly acknowledges the lack of adequate hardware support for unstructured sparsity (Section 7), the reliance on perplexity as a proxy for model quality, and the limited scale of the study due to computational constraints. This transparency is commendable.

## Weaknesses

### Major

- **Optimal schedule validated on only one model size.** The sparsity schedule search in Section 6.1 (Figures 4, 5) and the closer analysis in Section 6.2 (Figures 6a–6d) are conducted entirely on the 162M model. The resulting prescription (25%/50%/25%) is then applied to all three model sizes (58M, 162M, 468M) for the scaling law fitting without verifying that it is also optimal for 58M and 468M. If the optimal schedule is model-size dependent, the scaling law fit could be based on suboptimal configurations for those sizes. While the good fit quality (MAE 0.016) provides some indirect evidence that the schedule is reasonable across sizes, direct validation on at least one additional size is needed to support the claim that the prescription generalizes.

- **Scaling law fitted to a narrow range of model sizes.** The scaling law is fitted to only 3 model sizes (58M, 162M, 468M), spanning roughly an 8× range. By comparison, Chinchilla (Hoffmann et al., 2022) uses 7 sizes spanning 40M to 16B (~400× range). While the paper acknowledges computational constraints, the practical value of the law for predicting the behavior of much larger models (a stated goal) is uncertain without validation over a wider size range or a held-out analysis. The good in-sample fit (30 data points, 5 free parameters) does not guarantee predictive robustness.

### Minor

- **Theoretical justification (Section 5.2) falls short of a rigorous derivation.** The section claims to provide an "analytical derivation" of the scaling law (Equation 2), but what is actually presented is a heuristic motivation. Starting from a single-term power law in compute (L(C) = (A/C)^α) and performing a Taylor expansion, the argument shows that the total change in loss is proportional to the average number of active parameters. This provides useful intuition for *why* N̄ might be the right quantity, but it does not derive the specific two-term additive Chinchilla form (A/N̄^α + B/D^β + E). The contribution list (item 2) states "a theoretical analysis... that justifies using the average number of active parameters" — this is a fair characterization of what is delivered, but the phrasing "analytical derivation" (line 118) overpromises. The paper would benefit from either strengthening the derivation or reframing this section as an intuitive justification.

- **"Lossless compression" claim is unqualified.** The paper states that sparse pre-training yields a "2× lossless compression rate" at 80% sparsity (Section 7). This is based solely on validation perplexity on the C4 dataset. The paper acknowledges the limitation of not evaluating downstream tasks, but the term "lossless" in the main text is not explicitly qualified to reference perplexity. A reader scanning the paper could easily over-interpret this claim. A short qualification (e.g., "lossless with respect to validation perplexity") would prevent misinterpretation.

### Trivial

- **Figure 2 discussion could be clearer.** The explanation of how the stability of C_{0:k-1}^{-α-1} follows from the estimated α values is somewhat terse (line 153–155), and the garbled text in the parser output suggests the exposition may benefit from tightening.

- **Fitted parameter values (A, B, E, α, β) and their confidence intervals are not reported.** Providing these would allow other researchers to use the proposed scaling law.

## Nice-to-Haves

- Validate the optimal schedule on at least one additional model size (e.g., 58M or 468M) using a few schedule variations at a representative sparsity level. This is the highest-leverage addition given the paper's central practical claim.
- Add a hold-out or cross-validation analysis for the scaling law (e.g., fit on 2 model sizes and predict the 3rd, or leave-one-sparsity-level-out). This would substantially strengthen confidence in the law's robustness.
- Report the fitted values of A, B, E, α, β and their uncertainty intervals.
- If possible, include a small set of downstream task evaluations to corroborate the perplexity-based findings, even on a subset of configurations.

## Removed Points

- The harsh critic's concern about Figure 2 clarity being "incomplete" is partly attributable to parser-induced garbled text (line 154). The paper's argument is serviceable. This is a minor presentation issue that does not affect the core claims.
- The harsh critic's suggestion that the paper should "stop claiming it as a theoretical contribution" — the contribution list (item 2) describes a "theoretical analysis," which is accurate. Only the in-section phrasing "analytical derivation" (line 118) overreaches. The weakness is kept but downgraded to Minor.
- No other removed points: the remaining criticisms were verified against the paper and found to be substantively accurate.

## Novel Insights

The most interesting insight to emerge from the reviews — beyond the paper's own contributions — is the tension between the paper's two main claims. The scaling law (using average active parameters) is validated across all three model sizes simultaneously, yet the schedule that generates the data for that law is only shown to be optimal for one of them. The fact that the law fits well despite this potential mismatch either (a) suggests the 25/50/25 schedule is indeed near-optimal across sizes (which would strengthen the paper if confirmed), or (b) implies the scaling law is robust to modest deviations from the optimal schedule, which is itself a useful property. The paper does not disentangle these two possibilities, and doing so would be a valuable extension.

## Suggestions

1. Run a small number of schedule variations (e.g., 0%, 25%, 50% dense compute) for the 58M or 468M model at one representative sparsity level (e.g., 60%) to validate that the 25/50/25 prescription generalizes.
2. Perform a leave-one-out cross-validation on the scaling law data: fit on 2 model sizes and predict the 3rd; report prediction errors.
3. Soften the "analytical derivation" language in Section 5.2 to "theoretical motivation" or "heuristic justification."
4. Qualify the "lossless compression" claim explicitly (e.g., "lossless with respect to validation perplexity on C4").
5. Report the fitted parameter values (A, B, E, α, β) for reproducibility.

## Score and Decision

This paper makes a solid empirical contribution: it proposes a simple, unified scaling law for dense and sparse pre-training, validates it across 30 configurations with good fit quality, and identifies an actionable optimal schedule through systematic search. The weaknesses are real — the schedule is validated on only one model size, the scaling law covers a narrow size range (~8×), and the theoretical section overreaches — but none are fatal to the core claims. The main empirical findings are well-supported by the experiments presented, and the paper is transparent about its limitations. With the suggested additions (particularly schedule validation on another size and scaling law cross-validation), the paper would be a strong contribution.

**Originality**: Good — the average-active-parameter framing is a novel perspective that unifies prior dense and sparse scaling laws.
**Quality**: Solid — careful experimental design, systematic sweeps, honest limitations.
**Clarity**: Generally clear, with minor exposition issues in the theory section.
**Significance**: Useful for practitioners working on efficient LLM training and for researchers studying scaling laws.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>