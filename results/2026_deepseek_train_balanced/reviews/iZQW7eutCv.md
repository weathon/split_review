## Summary

This paper proposes pEBR, a probabilistic approach to embedding-based retrieval. It models the relevance scores of items for a given query as following either a truncated exponential distribution (ExpNCE) or a Beta distribution (BetaNCE), and uses the CDF of that distribution to derive a query-dependent dynamic cutoff threshold. Experiments on an 87-million-click industrial dataset compare pEBR to DSSM with fixed-number and fixed-score cutoffs, reporting improvements in both Precision@1500 and Recall@1500.

## Strengths

- **Well-motivated problem with a principled solution.** The paper correctly identifies that fixed-number and fixed-score retrieval cutoffs are suboptimal: head queries have many relevant items while tail queries have few. The CDF-based threshold derivation (Equations 178, 195-198) provides a mathematically grounded way to vary the cutoff per query, and the ablation in Table 2 verifies that the mechanism indeed retrieves more items for head queries and fewer for tail queries as intended.

- **The ablation study provides direct evidence that the mechanism works as designed.** Table 2 shows head queries retrieve ~2253 items vs. ~1805 for tail queries at CDF=0.99, and this ordering holds across all eight tested thresholds. Figure 3 corroborates this with histograms. This demonstrates that the dynamic cutoff successfully captures query semantic breadth.

- **The method improves both precision and recall over both baselines across all query categories simultaneously** (Table 1). While the absolute improvements are modest (0.44–0.79% recall, 0.148–0.256% precision absolute), the consistent pattern — larger recall gains on head queries, larger precision gains on tail queries — aligns with the paper's theoretical expectations.

## Weaknesses

### Major

- **Experimental design confounds the loss function and the cutoff mechanism.** The paper compares "DSSM-topk" and "DSSM-score" (both presumably trained with a standard DSSM loss, then cut off by fixed-number or fixed-score) against pEBR (trained with the proposed BetaNCE loss *and* cut off by CDF). Because the loss function *and* the cutoff strategy change simultaneously, it is impossible to attribute the reported improvements to the probabilistic loss function itself versus the dynamic thresholding mechanism. The critical missing comparison is: a model trained with the standard loss but using the same CDF-based cutoff (post-hoc), and a model trained with BetaNCE loss but using a fixed cutoff. Without this 2×2 decomposition, the central claim that the probabilistic loss drives improvement is unsupported.

- **The metric comparison is inherently asymmetric.** DSSM-topk retrieves exactly 1500 items per query, while pEBR retrieves more items for head queries (~2253) and fewer for tail queries (~1805, at CDF=0.99), with the average tuned to 1500. This allocation mechanically favors pEBR: retrieving more items for head queries (which have more relevant items) inflates recall, while retrieving fewer items for tail queries (which have few relevant items) inflates precision. Some of the reported gains may therefore reflect the allocation mechanism rather than the quality of the learned representations. The paper does not control for this.

- **Baselines are too weak for the claims made.** There is no comparison against:
  - A model trained with standard InfoNCE loss (which the paper explicitly builds on),
  - Other two-tower retrieval models,
  - A model using a learned query-dependent temperature *without* the Beta/exponential distributional assumption,
  - A simple post-hoc distribution fit applied to standard DSSM scores.
  Without these, the 0.44–0.79% recall improvements over the simplest fixed-cutoff baselines do not constitute strong evidence that the probabilistic framework is superior to existing alternatives.

- **No measure of variance or statistical significance.** With 87M training samples, the reported improvements (e.g., 0.256% absolute precision increase over DSSM-topk) could easily be noise. No standard deviations, confidence intervals, or statistical tests are reported, making it impossible to assess whether these small differences are meaningful.

### Minor

- **The novelty claim is overstated.** The paper states it is "the first to introduce probabilistic modeling into embedding based retrieval" (line 53). However, InfoNCE (Oord et al., 2018), which the paper explicitly builds on, is already a noise contrastive estimator derived from probabilistic principles. The actual contribution — making the temperature query-dependent and using specific distributional families for CDF thresholding — is a legitimate but incremental extension, not a paradigm shift.

- **Head/torso/tail query splits are never defined.** The paper uses these categories throughout the experiments and ablation (Tables 1–2, Figures 2–3) but never specifies the criteria (e.g., query frequency thresholds). This makes the analysis non-reproducible.

- **No empirical analysis of the learned temperature parameters.** The method hinges on the query-dependent temperature τ_q, but the paper never shows the learned values, their distribution across queries, how they correlate with query popularity, or whether they behave as expected.

- **The β_g = β_k assumption is presented with minimal justification.** The argument that the background distribution and positive distribution share the same "number of failures" (lines 214–215) is conveyed in roughly two sentences. Given that this assumption is central to the BetaNCE derivation, it deserves more thorough justification or sensitivity analysis.

- **The MLE-based formulation (Section 3.3) is presented and then immediately dismissed** ("may lead to suboptimal performance," line 154). This subsection does not contribute to the final method and takes space that could have been used for more rigorous ablation or analysis.

### Trivial

- None that survive the filtering discipline.

## Nice-to-Haves

- Disentangle the loss function from the cutoff mechanism (2×2 ablation: standard loss + fixed cutoff, standard loss + CDF cutoff, proposed loss + fixed cutoff, proposed loss + CDF cutoff).
- Compare against standard InfoNCE with a global (non-query-dependent) temperature to gauge the contribution relative to the most natural baseline.
- Compare against a model with a learned query-dependent temperature but without the Beta/exponential distributional assumption, to isolate whether the specific distribution families matter.
- Report variance (e.g., standard deviation over multiple runs or bootstrapped confidence intervals).
- Define head/torso/tail splits explicitly and analyze the learned τ_q values.

## Removed Points

The following points from the inputs were removed with justification:

- **"The precision values are extremely low (0.3–0.6%)"** (Harsh Critic): The paper acknowledges this explicitly (line 271: "the precision value is relatively very low") and explains it's because k=1500 was chosen to optimize recall. This is not a weakness — it is a stated design choice.

- **"The t-SNE visualization adds little evidence"** (implied in Harsh Critic): While t-SNE can be sensitive to hyperparameters, the visualization (Figure 2) is presented qualitatively and the paper does not make strong quantitative claims from it. It serves as an illustrative example, which is acceptable for an ablation study.

- **"HMM/CRF/LDA references are not directly connected"** (Harsh Critic): The related work section surveys probabilistic modeling broadly. While this could be tighter, it does not constitute a weakness of the method or experiments.

- **"The paper's opening characterization that the field universally uses a fixed number or fixed cosine threshold is presented as absolute"** (Harsh Critic): The paper states this as a problem statement about *common* industrial practice. This is a reasonable characterization and does not misrepresent the field.

- **Strength: "Visual evidence that item-distribution dispersion correlates with query popularity"** (Strength Finder): The t-SNE visualization of three examples is too thin to serve as a strength; it is a qualitative illustration at best. Moved here for completeness.

## Novel Insights

The core insight — that using the CDF of a distributional assumption over relevance scores yields a principled, query-dependent retrieval threshold — is sensible and practically motivated. The key tension the reviews surface is that the paper cannot determine whether this insight produces gains because of the distributional modeling itself or simply because any dynamic allocation (even a simple one) beats a static cutoff. This is a genuine gap that future work could address with a more careful decomposition.

## Suggestions

1. Add the 2×2 ablation (standard loss ± dynamic cutoff, proposed loss ± dynamic cutoff) to isolate the contribution of each component.
2. Add a standard InfoNCE baseline with a global (non-query-dependent) temperature.
3. Report variance or confidence intervals for all metrics.
4. Define head/torso/tail splits explicitly.
5. Show the distribution of learned τ_q values and correlate them with query frequency.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>