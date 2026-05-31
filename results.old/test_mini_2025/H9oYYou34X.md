## Summary

This paper introduces Markovian compressors (BanLast and KAWASAKI) for distributed optimization with compressed communication. Unlike standard compressors that independently sample coordinates at each iteration, these compressors use a Markov chain to track which coordinates were selected in the last *K* iterations and reduce the probability of reselecting them. The compressors are embedded into QSGD (MQSGD) and an accelerated variant (AMQSGD), with convergence rates provided for non-convex, PL, and strongly convex settings. Experiments on logistic regression and ResNet-18/CIFAR-10 show convergence improvements over random sparsification and other baselines.

## Strengths

1. **Novel concept of Markovian compressors.** The idea of making the compressor's stochasticity depend on previous iterations via a Markov chain (Definitions 5 and 6) is genuinely new. Prior work on compressed communication uses independent or memoryless randomness; this paper is the first to formalize and analyze compressors whose coordinate-selection probabilities evolve as a Markov chain. Theorem 1 proves ergodicity and uniform stationary distribution for both BanLast and KAWASAKI, establishing the asymptotic unbiasedness needed for convergence analysis.

2. **First convergence theory for SGD with Markovian compressors.** Theorem 2 provides rates for MQSGD in non-convex and PL settings with explicit dependence on the mixing time τ and compression ratio d/m. The proof introduces a "stepping back" technique (inequality (4) and equation (5)) to handle the non-stationary bias arising from the Markovian compressor—a methodological innovation over the standard i.i.d. analysis. The accelerated variant (Theorem 3) achieves sublinear convergence with improved condition-number dependence.

3. **Empirical gains on a practical deep-learning task.** Table 1 reports ResNet-18/CIFAR-10 results over 5 runs with mean ± std: KAWASAKI achieves 89.05 ± 0.294 test accuracy vs. 87.9 ± 0.179 for Rand-5%, with correspondingly lower training loss and gradient norm. Figure 3 shows that Markovian compressors can be combined with Natural compression, demonstrating flexibility. These results suggest practical value beyond the theoretical baselines.

4. **Honest discussion of the theory–practice gap.** Section 2.4 transparently compares the derived rates with those of unbiased QSGD, pinpoints the sources of the worse constants (d²/m² instead of d/m, dependence on τ), and acknowledges that the theory predicts better performance for small K while experiments benefit from moderate K. This intellectual honesty strengthens the paper's credibility—the claims are tempered and the limitations are clear to the reader.

## Weaknesses

### Major

1. **Logistic regression experiments shown as "best runs" without error bars.** The caption of Figure 1 states *"All hyperparameters are fine-tuned, and best runs are selected."* The logistic regression results (the only source of evidence for those datasets) consist of single-curve plots with no indication of variance across seeds or hyperparameter choices. This makes it impossible to assess whether the observed improvements are statistically significant or cherry-picked. The ResNet-18 experiments partially address this concern via Table 1 (mean ± std over 5 runs), but the ResNet-18 *figures* (Figure 2 caption: *"Best runs for each method are displayed"*) also only show selected runs. The authors should report average curves with error bars for all experiments, or at minimum provide a clear justification for single-run plots alongside supporting statistics.

### Minor

2. **Incomplete specification of KAWASAKI hyperparameters for reproducibility.** The paper states that a "normalization activation function" is used (Section 3.1) and lists three examples in Definition 6. The figure captions use notation like `KAWASAKI(28, 50, [p_i], [p_i], d/10)` for logistic regression and `KAWASAKI(10, 5, p_r, 1/||p_r||, d/20)` for ResNet-18. The mapping from the three candidate π_Δ functions to these specific choices, the value of the forgetting rate *b*, and the meaning of `[p_i]` are not fully clarified. This should be fixed for reproducibility.

3. **No discussion of memory/storage overhead.** BanLast stores the set of selected coordinates from the last *K* iterations, and KAWASAKI tracks counts. For very high-dimensional models (e.g., large language models), storing *K* binary vectors of dimension *d* could incur significant memory overhead. A brief remark on this practical consideration would strengthen the paper.

### Trivial

4. **Figure 2 caption states "Best runs for each method are displayed"** while Table 1 shows proper mean ± std for the same experiment. This inconsistency between figure and table could confuse readers.

## Nice-to-Haves

- **Comparison with error-feedback compressors (e.g., EF21).** Error feedback is the dominant paradigm for biased compressors and also uses past information (the compression error). Adding EF21 as a baseline would contextualize the benefits of Markovian compressors against this well-studied alternative.
- **Ablation of *K* in the main text.** The appendix mentions tuning analysis for *K*; moving this to the main text would help demonstrate the mixing-time trade-off discussed in Section 2.4.
- **Empirical estimate of mixing time τ.** If feasible, computing or estimating τ for the compressors used and overlaying it with convergence curves would help bridge theory and practice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Theory-practice gap as a weakness.** The harsh critic cited the gap between theoretical rates and practical performance. However, Section 2.4 of the paper *explicitly and transparently* discusses this gap, acknowledges the worse constants, references lower bounds showing τ cannot be avoided, and frames the theory as a first step. A paper is not weakened by honestly disclosing its limitations; this is a virtue, not a flaw.
- **Missing comparison with EF21.** The paper cites EF21 in Related Work and its scope is the introduction of Markovian compressors, not exhaustive benchmarking. Requesting additional baselines is a suggestion, not a weakness of the presented work.
- **Constraint d ≥ (K+1)m for BanLast not discussed for small models.** The paper states this constraint explicitly on line 117. The critic's own note acknowledges this ("the paper mentions this constraint"). The paper does discuss it.
- **Activation function underspecification in theory.** Theorem 1 states the condition (permutation-equivariance) and says the three examples satisfy it. This is adequate for the theoretical claims.

## Novel Insights

None beyond the paper's own contributions. The main synthesis across the reviews is that the paper's honesty about its theoretical limitations (Section 2.4) is a genuine strength that should be preserved, and the single most impactful fix is improving the experimental reporting for the logistic regression results.

## Suggestions

1. Re-run the logistic regression experiments with at least 5 random seeds and report mean ± std or median with error bands, replacing the current "best runs" plots.
2. For ResNet-18, show mean curves (with shading) in Figure 2 consistent with the statistics reported in Table 1 instead of "best runs" curves.
3. Specify the exact π_Δ activation function and *b* value for each KAWASAKI configuration used in the experiments. Clarify the notation `[p_i]` and `p_r, 1/||p_r||`.
4. Add a brief paragraph on the memory/storage overhead of storing the last *K* selections.
5. (Optional) Include a comparison with an error-feedback compressor such as EF21 to better contextualize the empirical results against the most prominent competing paradigm.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CORE (ER1VDuwWvB) — Reject | 3.67 | 1 | Weaker: this paper had fundamental issues with unsupported claims and incorrect table entries |
| Det-CGD (ZEZ0CPmoSI) — Accept (Poster) | 5.00 | 2 | Slightly weaker: limited experiments (logistic regression only), stronger assumptions; our paper has more novelty |
| LASER (TCJbcjS0c2) — Reject | 5.83 | 2 | Comparable, but LASER was rejected mainly for limited novelty; our paper's Markovian compressors are more novel |
| MoTEF (CMMpcs9prj) — Accept (Poster) | 6.60 | 2 | Slightly stronger: more thorough theoretical contribution and cleaner experimental methodology |
| SGD with Memory (Qzd4BloAjQ) — Accept (Poster) | 6.75 | 2 | Stronger theory but weaker experiments; our paper has better empirical breadth but weaker theory |

**Round 1 bracket:** Between 4 and 7 (clearly above weak-reject band, clearly below strong-accept band).

**Round 2 narrowing:** The paper is stronger than Det-CGD (5.0) and LASER (5.83) but weaker than MoTEF (6.6) due to the experimental reporting issues. The main claim—that Markovian compressors can accelerate convergence in practice despite worse theoretical constants—is novel and supported by the ResNet-18 results. However, the logistic regression "best runs" problem prevents full confidence in the broader evidence base.

**Final score: 6.0** — a solid contribution with a genuinely novel idea and decent supporting evidence, held back by an experimental reporting issue for the logistic regression experiments and some underspecified details. Both issues are fixable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>