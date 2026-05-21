Now I have a clear picture. Let me finalize the review.

**Round-1 bracket**: The anchors at 3.0-3.4 (weak), 4.25-6.75 (middle), and 8.0 (strong) place this paper in the **5.5-7.0** range.

**Round-2 narrowing**: Comparing against the 5.67 anchor (jQ596tXT3k — explaining OOD paradox, limited experiments, hyperparameter sensitivity), the 5.75 anchor (7QDIFrtAsB — NCSN tabular AD, extensive experiments but limited novelty and validation concerns), and the 6.5-6.75 anchors — our paper has stronger theoretical grounding and a conceptual contribution (the definition) than both 5.67/5.75 anchors, but shares their methodological concerns. It's clearly below 8.0. The closest comparison: stronger than 5.75 due to theory + definition, but the hyperparameter issue limits upward movement. **Final score: 6.0**.

Now let me write the review.

---

## Summary

This paper investigates whether the "counterintuitive phenomenon" — where deep generative models assign higher likelihood to out-of-distribution data — occurs in tabular anomaly detection as it does in images. The authors propose a domain-agnostic formal definition of the phenomenon (Definition 3.3) centered on relative model performance, benchmark NF-SLT (a normalizing flow with simple likelihood thresholding) against 12 baselines across all 47 tabular datasets in ADBench, and provide theoretical analysis linking data dimensionality and feature correlation to the phenomenon's rarity in tabular domains.

## Strengths

- **Domain-agnostic formal definition of the counterintuitive phenomenon**: Definition 3.3 operationalizes the concept through two clear conditions — the proportion of comparison models outperforming the generative model (Eq. 2) and a minimum performance gap (Eq. 3). This moves beyond prior vague characterizations and enables consistent evaluation across domains. The application to CIFAR-10 vs. SVHN (Section 3, paragraph 4) concretely demonstrates how the definition works.

- **Comprehensive benchmarking on ADBench**: The evaluation uses all 47 tabular datasets and 10 CV/NLP embedding datasets without cherry-picking, compared against 6 shallow and 6 deep baselines. Table 1 provides a clear, multi-metric summary (AUROC, AUPRC, Avg. Rank, Top2 Ratio, Fail Ratio) that supports the paper's central empirical claim.

- **Theoretical analysis linking dimensionality to likelihood-based detection failure**: Theorem 5.4 derives that under independence assumptions, the lower bound of the expected likelihood gap decreases linearly with dimension. Corollary 5.6 extends this to an upper bound on achievable AUROC that is inversely related to dimensionality. These provide a principled explanation for why lower-dimensional tabular data avoids the inversion phenomenon.

- **Feature-correlation analysis via intrinsic dimension**: The toy Gaussian example (Figure 1, left/center) convincingly demonstrates that ID estimates decrease as feature correlation increases. The comparison of ID estimates between image and tabular datasets (Table 4 top, Figure 1 right) shows tabular data has substantially higher d-Ratio (~40-80%) versus images (~1%), providing empirical support for the correlation-dependence argument.

## Weaknesses

### Fatal

None. The paper's core contributions — the definitional framework, the empirical observation that the phenomenon is rare in tabular data, and the theoretical dimensionality analysis — remain coherent and partially supported even accounting for the issues below.

### Major

- **Hyperparameter selection uses test-set performance across all datasets**: The paper states (Section 4, Evaluation): "the hyperparameter combination with the highest average AUROC for all datasets is selected as the representative hyperparameter combination." Since the data split uses 50% normal for training and the remaining data (normal + abnormal) for testing with no held-out validation set, this means hyperparameters are chosen to maximize performance on the very test data used for reporting. This circular procedure inflates the reported AUROC/AUPRC values and undermines the trustworthiness of the headline comparisons in Table 1. While all models underwent the same protocol (preserving some validity of relative rankings), and selecting a single global configuration across 47 datasets limits the degrees of freedom for overfitting, the absolute performance numbers and the 0.02 fail ratio should be treated as upper bounds rather than unbiased estimates. This is a structural evaluation-design issue that weakens the paper's primary empirical claim.

### Minor

- **Definition 3.3 thresholds (β, γ) are never instantiated**: The paper defines the counterintuitive phenomenon in terms of thresholds β and γ but never specifies numerical values. The experimental discussion uses implicit reasoning ("the minimum performance difference... is 0.02; hence, we cannot assume... a counterintuitive phenomenon has occurred") without stating what γ would need to be. This leaves the definitional contribution incomplete — the reader cannot assess whether the evidence satisfies the definition under any concrete parameterization.

- **The d-Ratio analysis in Table 4 (bottom) is confusing and potentially contradicts the paper's claim**: The paper states "NF-SLT fails to achieve high performance on most datasets with low d Ratio." However, Table 4 (bottom) reports the fraction of rank≥3 datasets with d-Ratio *below* a threshold — only 16% of failed datasets have d-Ratio ≤ 0.1. The conditional appears to be presented in the wrong direction to support the claimed conclusion. The relevant quantity would be P(rank ≥ 3 | low d-Ratio), not P(low d-Ratio | rank ≥ 3). As presented, this part of the evidence for the feature-correlation argument is not interpretable.

- **The dimensionality-reduction experiments do not cleanly test the theorem's assumptions**: The ICA experiment (Table 2) alters the data distribution by extracting independent components; the resize experiment (Table 3) uses Glow with a CNN on raw pixels where independence between pixels does not hold. The paper acknowledges the latter limitation but neither experiment provides a direct test of Theorem 5.4's conditions (independence across dimensions, a well-trained model approximating P). The evidence is suggestive rather than confirmatory.

### Trivial

- No discussion of computational cost or wall-clock time, which is relevant when advocating a practical detection approach.
- Only NICE-based flow results appear in the main evaluation; other flow architectures are deferred to the (stripped) Appendix G.
- Lemma 5.1 and Corollary 5.5 are referenced but not summarized in the main text, making the theoretical argument slightly less self-contained.

## Nice-to-Haves

- Explicitly setting β and γ with a sensitivity analysis across threshold choices would substantially strengthen the definitional contribution.
- Expanding the ID analysis to all 47 tabular datasets with per-dataset d-Ratio values and a proper statistical test (e.g., correlation between d-Ratio and NF-SLT rank) would make the feature-correlation argument more rigorous.
- A proper validation-split protocol (e.g., holding out a subset of normal training data for hyperparameter selection) would restore full credibility to the empirical comparisons.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that hyperparameter issue is "fatal" and "invalidates the empirical evaluation"**: Demoted from fatal to major. The issue is real and serious, but the paper's core thesis — that the phenomenon is rare in tabular data — is supported by multiple independent lines of evidence (theoretical analysis, feature-correlation analysis, the definitional framework applied qualitatively), not solely by the exact AUROC values. All models underwent the same protocol, so relative comparisons retain partial validity.

- **Harsh Critic claim about "Section 5.1... proofs are not visible in the main text"**: The paper states proofs are in Appendix D, which is a stripped section. This is not an author error. The main text does state the theorems.

- **Harsh Critic claim about "the primary model is only a NICE-based flow"**: Acknowledged as a limitation, but moved to trivial since this is a first study establishing the phenomenon, and additional flows are in Appendix G (stripped).

- **Strength Finder claim that "embedding-dataset results extend the argument"**: The embedding results in Table 1 (bottom) are genuinely interesting but the comparison is only against deep models (6 baselines), not the full 12-model set. This strength is partially valid but not as strong as claimed.

- **Harsh Critic: "no ablation on the number of coupling layers or flow architecture depth"** — This is a reasonable suggestion but falls under nice-to-have rather than a weakness. The paper uses a fixed architecture across all datasets, so overtuning to specific datasets is mitigated.

## Novel Insights

The paper's most genuinely novel observation is the synthesis of dimensionality and feature-correlation perspectives into a unified explanation for why the likelihood-inversion phenomenon is domain-dependent. Prior work identified these factors separately (Kirichenko et al. on pixel correlations; Caterini & Loaiza-Ganem on entropy) but did not connect them to a formal definition of the phenomenon or systematically test the connection across 47 datasets. The finding that tabular data's higher intrinsic-dimension-to-ambient-dimension ratio (d-Ratio) correlates with NF-SLT success, while image data's very low d-Ratio correlates with the phenomenon, provides a compact diagnostic that could guide practitioners in choosing when likelihood-based detection is appropriate.

## Suggestions

- Adopt a proper hyperparameter selection protocol: use only training normal data (e.g., via a held-out validation split from the training portion) or cross-validation on the training set. If recomputing all experiments is infeasible, at minimum discuss the limitation transparently and report how sensitive results are to hyperparameter choice.
- Instantiate Definition 3.3 with concrete β and γ values and report, for each dataset, whether the phenomenon is declared under those thresholds. A sensitivity analysis over β ∈ {0.5, 0.7, 0.9} and γ ∈ {0.05, 0.10, 0.15} would make the definitional contribution actionable.
- Fix the d-Ratio analysis in Table 4 (bottom): report what fraction of datasets with d-Ratio below each threshold have rank ≥ 3, rather than the reverse conditional. This would directly test the claimed relationship.

## Score and Decision

**Calibration summary**:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jQ596tXT3k (Explaining OOD Paradox via Likelihood Peaks) | 5.67 | R1/R2 | Similar topic (explaining likelihood inversion); our paper has larger-scale experiments, formal definition, and theoretical analysis → stronger |
| 7QDIFrtAsB (NCSN Tabular AD) | 5.75 | R1/R2 | Similar scale of benchmarking; our paper adds theory + definition but shares methodological concern → stronger |
| CJnceDksRd (DRL Tabular AD) | 5.75 | R2 | Method-focused; our paper is analysis-focused with broader scope → comparable to stronger |
| ndCJeysCPe (Flow-based Generative Model Theory) | 6.33 | R2 | Stronger theoretical rigor but narrower scope; our paper is broader → comparable |
| cJs4oE4m9Q (Deep Orthogonal Hypersphere) | 8.00 | R1 | Novel method + strong theory + clean experiments → clearly above our paper |

**Round-1 bracket**: 5.5–7.0
**Round-2 narrowing**: Comparison with 5.67/5.75 anchors shows our paper is stronger (adds formal definition, theoretical analysis, broader evaluation). Comparison with 6.33 shows comparable quality but different strengths. The hyperparameter issue prevents reaching the 7+ range. **Final score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>