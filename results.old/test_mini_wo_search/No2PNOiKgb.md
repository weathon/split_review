Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper presents a method for convex primitive decomposition of indoor scenes. The key innovations are (a) incorporating negative (CSG-style) boolean primitives to allow set-difference operations and (b) an ensembling strategy with a refine-then-choose selection mechanism. On the NYUv2 benchmark, the method substantially outperforms prior SOTA (Vavilala et al. and Kluger et al.), achieving ~33% relative reduction in AbsRel depth error (0.096→0.064).

## Strengths

- **Refine-then-choose ensembling is convincingly superior to select-then-refine.** Table 2 (tab:ft_gt) directly compares both strategies: for the positive-only ensemble, select-then-refine yields AbsRel 0.076 while refine-then-select yields 0.066; for the pos+neg ensemble, the numbers are 0.076 vs 0.064. This demonstrates a genuine empirical finding — the refinement outcome is a poor predictor of initial fit quality, and polishing first then selecting is clearly better.

- **The overall method strongly outperforms prior SOTA on NYUv2.** Table 3 (tab:auc_gt) shows the best ensemble achieves AUC@50=91.5, AUC@20=82.0, mean distance=18.8 cm, median=6.58 cm, compared to Vavilala et al. (86.9, 72.5, 26.6 cm) and Kluger et al. (77.2, 62.7, 20.8 cm). Even individual networks (e.g., 28 positive primitives, AbsRel=0.073) beat the prior best AbsRel=0.096 — meaning the improvements come from training innovations (data augmentation, annealing, loss design) independent of the ensemble.

- **The biased inside-sample loss (L_inside) provides a clear performance boost in relevant regimes.** Table 4 (tab:bias) shows that for a network with 12 primitives and 1 negative, turning off the bias (w_inside=0) gives AbsRel=0.122, which drops to 0.090 with w_inside=0.1 — a 26% relative improvement. The intuition that this loss forces negatives to "cut out" over-covered inside regions is well-motivated.

- **Data augmentation correctly handling camera calibration yields tangible gains.** Table 5 (tab:aug) shows horizontal/vertical flips reduce AbsRel from 0.080 to 0.074 and improve segmentation accuracy from 0.652 to 0.667 for a 24-primitive positive-only network.

- **The paper is transparent about limitations.** The Discussion section honestly addresses the computational cost (13 minutes per image for full ensemble) and the difficulty of demonstrating that primitives simplify reasoning tasks — a refreshing degree of candor.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of negative primitives is not properly isolated from ensemble size effects, and claims about their benefit are not cleanly supported.** The paper frames negatives as a core contribution alongside ensembling (title, abstract, introduction, contributions list). However, the critical comparison in Tables 2 and 3 pits a **5-network positive-only ensemble** against a **15-network pos+neg ensemble** (the 5 positive-only networks plus 10 variants with 1-2 negatives). The reported improvements (e.g., AbsRel 0.066→0.064, AUC@50 91.2→91.5) could come entirely from having a larger, more diverse candidate pool rather than from the negative primitive representation itself. This is not a speculative concern — the paper's own individual-network results (Table 2) show that adding negatives *often degrades* performance (e.g., 12 primitives: 0 negatives=0.086, 1 negative=0.090, 2 negatives=0.088; 16 primitives: 0.079→0.083→0.087). The paper acknowledges that negatives "only occasionally help on average" at the individual level, but never provides a controlled test (e.g., 5-network pos-only vs. 5-network pos+neg, or 15-network pos-only vs. 15-network pos+neg) to substantiate the ensemble-level claim. This weakens the paper's second stated contribution about boolean primitives.

### Minor

- **No error bars or repeated-run statistics.** For a paper reporting improvements of ~33% relative over prior SOTA, single-run results without variance estimates make it difficult to assess whether the improvements are statistically significant. This is especially relevant for the small-margin differences (e.g., 91.2 vs. 91.5 AUC@50) that distinguish the pos-only from pos+neg ensemble.

- **The "refinement using GT depth map" description is ambiguous on first reading.** The paper says "applying refinement procedure on all test images using the GT depth map" and later "minimizing the training loss w.r.t the input depth map." These must be the same quantity for the evaluation to be realistic; stating this explicitly would avoid confusion.

### Trivial
None.

## Nice-to-Haves

- A controlled ablation separating the effect of negatives from ensemble diversity (e.g., compare a 5-network pos-only ensemble to a 5-network pos+neg ensemble with matched total member count).
- A brief discussion of failure cases for negatives — scenes where negative primitives are selected versus rejected, and why.
- Additional qualitative results showing failure cases of the overall method.

## Removed Points

- **"Overstatement of evidence for negative primitives in abstract/introduction"** — The paper actually qualifies negatives carefully: the abstract attributes "very significant improvements" to *both* (a) negatives *and* (b) ensembling together; the introduction explicitly says "on their own, negative primitives produce small improvements." The statement "negative primitives are useful in a large fraction of images" is supported by Fig. 2 showing negatives selected ~half the time. This criticism misreads the paper's actual claims.

- **"Comparison with prior work uses only two baselines"** — The two baselines (Vavilala et al., Kluger et al.) are the established SOTA methods for this specific task on NYUv2. Criticizing this as insufficient is unfair without evidence that additional relevant baselines exist.

- **"Qualitative comparison is limited"** — The paper provides qualitative results in Fig. 1 and a detailed case study of negative primitives in Fig. 2. More would be welcome but this is not a weakness.

- **"No confidence intervals / statistical significance" (from Strengthening the Paper)** — Kept as minor weakness (see above), but the critic's framing as a critical omission is overstated; single-run benchmarking on large test sets is standard practice in this sub-area.

- **"Missing related works"** — Removed per instructions (cannot verify without external sources).

- **Strength Finder: "Negative primitives consistently improve ensemble accuracy"** — This strength claim is not well-supported given the uncontrolled comparison (5 vs. 15 networks). The improvement is small and could be attributed to ensemble size diversity. Demoted from strength to a mitigated positive: the ensemble including negatives does achieve the best numbers, but the contribution of negatives per se is not isolated.

## Novel Insights

None beyond the paper's own contributions. The two reviews arrived at the same central finding: the refine-then-choose ensembling strategy is clearly effective and well-supported, while the contribution of negative primitives is confounded with ensemble size and not cleanly demonstrated. The reviews did not surface any strengths, weaknesses, or connections the paper itself does not already articulate.

## Suggestions

1. **Provide a controlled ablation for negatives.** Compare a 5-network pos-only ensemble against a 5-network pos+neg ensemble (e.g., 12/1, 16/1, 20/1, 24/1, 28/1) with matched member count. If the improvement persists, the negatives claim is substantiated. If not, reframe the contribution to focus on ensembling and note that negatives provide value mainly by increasing architectural diversity in the pool.
2. **Report multiple seeds** for the headline ensemble results to give confidence in the reported numbers, especially for small-margin comparisons.
3. **Clarify the GT depth usage** in the refinement description — state explicitly that the GT depth map is the input depth map used during refinement.
4. **Add a brief failure analysis** for negative primitives: what types of scenes benefit, and what types degrade?

## Score and Decision

**Originality:** Good — first application of CSG set-difference primitives to indoor scenes; novel refine-then-choose ensembling strategy.  
**Importance of research question:** High — primitive decomposition is a long-standing vision problem with implications for geometric reasoning.  
**Claims well supported:** Mixed — the overall method outperforms SOTA convincingly, but the negative primitive claim specifically lacks controlled evidence.  
**Soundness of experiments:** Good overall, with one significant confounding issue.  
**Clarity of writing:** Clear, well-structured, honest about limitations.  
**Value to community:** High — provides a strong new baseline and a useful ensembling technique.

The paper demonstrates a genuinely effective method for primitive decomposition that substantially advances SOTA. The refine-then-choose ensemble strategy is well-validated and independently valuable. The weakness regarding negative primitives is real but addressable — it does not invalidate the core contributions (the ensemble approach, the training improvements, and the overall SOTA results). The paper is transparent about its limitations and the mixed individual-network results for negatives. With controlled evidence for negatives or a reframing of the claims, this would be a strong contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>