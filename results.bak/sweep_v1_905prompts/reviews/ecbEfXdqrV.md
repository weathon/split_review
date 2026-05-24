Now I have sufficient calibration data. Let me synthesize the final review.

**Calibration synthesis:**

| Anchor | Score | Decision | How it compares |
|--------|-------|----------|----------------|
| 7QDIFrtAsB (NCSNAD) | 5.75 | Reject | Similar empirical scope, but NCSNAD had limited novelty; our paper has stronger theoretical framing and definitional contribution |
| Vi6p2TeujL (PTAD) | 4.25 | Reject | Complex method with reproducibility concerns; our paper is clearer and better motivated |
| lNZJyEDxy4 (MCM) | 6.67 | Accept | Strong novel method with extensive ablations; our paper is slightly weaker on methodological novelty but has stronger theoretical+empirical breadth |
| CJnceDksRd (DRL) | 5.75 | Accept | Similar empirical scope and theory gaps; accepted despite weaknesses |
| jQ596tXT3k (OOD Paradox) | 5.67 | Reject | Tackles similar phenomenon but weaker empirical scope; our paper has much larger evaluation |
| gRXLa6LS3J (FoMo-0D) | 5.75 | Reject | Novel approach but baseline concerns; our paper has more comprehensive evaluation |
| kBNIx4Biq4 (Injective Flows) | 6.50 | Accept | Strong theoretical contribution; our paper has comparable theoretical analysis but broader empirical work |

**Round 1 bracket:** [5.0, 7.0]
**Round 2 narrowed to:** [5.5, 6.5]
**Final score:** 6.0 — comparable to DRL (5.75, Accept) and the OOD paradox paper (5.67) but with larger empirical scope and clearer writing; weaker than MCM (6.67) on methodological novelty but has stronger theoretical framing.

---

## Summary

This paper investigates whether the "counterintuitive phenomenon" (where generative models assign higher likelihood to anomalous than normal data, observed in images) occurs in tabular anomaly detection. It contributes: (1) a domain-agnostic definition of the phenomenon based on relative performance against comparison models, (2) a large-scale empirical study on all 47 ADBench tabular datasets plus 10 CV/NLP embedding datasets showing that normalizing flow with simple likelihood test (NF-SLT) achieves highest average AUROC (0.8575) and lowest fail ratio (0.02) among 13 models, and (3) theoretical and empirical analyses linking this success to lower dimensionality and weaker feature correlations in tabular data.

## Strengths

- **Large-scale, unbiased evaluation.** The paper uses all 47 tabular datasets from ADBench without selection (motivated by Shwartz-Ziv & Armon's critique of selection bias) and compares against 12 baselines including both shallow and deep methods. NF-SLT achieves the best average AUROC (0.8575), average rank (3.43), Top2 ratio (0.45), and near-zero fail ratio (0.02). This is the most comprehensive empirical test of likelihood-based AD for tabular data to date.

- **Formal definition of the counterintuitive phenomenon.** Definition 3.3 introduces two explicit conditions (majority of comparison models must outperform the generative model, and the minimum gap must exceed a threshold) that improve upon vague prior notions of "likelihood overlap." This enables consistent, quantifiable detection across domains.

- **Theoretical analysis linking dimensionality to likelihood gap.** Theorem 5.4 and Corollary 5.6 formally analyze how increasing dimension can degrade the likelihood gap and AUROC upper bound, providing a domain-agnostic explanation for why low-dimensional tabular data avoids the phenomenon. Controlled ICA-based dimensionality reduction experiments (Table 2) support the theory.

- **Feature correlation analysis via intrinsic dimension.** Section 5.2 introduces the d-Ratio (ID/ambient dimension) to quantify correlation. The toy Gaussian experiments (Figure 1) convincingly show ID decreases with correlation strength, and the comparison between tabular (d-Ratio up to 0.81) and image data (d-Ratio ~0.003) is striking. The analysis of CV/NLP embeddings using this framework is also insightful.

- **Clear, well-organized writing.** The paper is well-structured, the motivation is clearly stated, and the connection between the two explanatory perspectives (dimensionality and correlation) is logically developed.

## Weaknesses

### Major

- **The definition of the counterintuitive phenomenon is presented but never operationalized with concrete thresholds.** Definition 3.3 introduces parameters β (proportion threshold) and γ (gap threshold), but the paper never specifies their values. When the yeast dataset is discussed (0.02 AUROC gap dismissed as too small), no γ is stated. When the CIFAR-10/SVHN example is claimed to satisfy the definition (Section 3), β and γ are not computed. The central claim that the phenomenon is "consistently rare" cannot be verified quantitatively without these thresholds. The formal definition is a good structural contribution, but its practical use requires operationalization.

### Minor

- **Hyperparameter selection methodology is non-standard and insufficiently justified.** The paper selects hyperparameters that maximize *average AUROC across all 47 datasets* for each model. This unusual protocol is applied uniformly to all models, so it does not selectively bias toward NF-SLT, but it differs from the common practice of per-dataset validation tuning or using default configurations. A sensitivity analysis comparing alternative protocols (e.g., per-dataset tuning) would strengthen the evidence.

- **No variance or statistical significance reported.** Table 1 reports averages from 10 runs but no standard deviations or confidence intervals. Given that several comparisons are close (e.g., NF-SLT vs. ICL: 0.8575 vs. 0.8208), it is unclear which improvements are statistically significant.

- **The theoretical analysis (Theorem 5.4) assumes independent dimensions, which does not hold for real data.** The paper acknowledges this and conducts experiments with correlated images (Table 3), but the resizing results sometimes contradict the theory (e.g., SVHN/CelebA where AUROC *improves* as dimension decreases despite ℍ(SVHN) < ℍ(CelebA)). The offered explanation about increased correlation from resizing is reasonable but undermines the claim that the theorem straightforwardly explains the rarity in tabular data.

- **The connection between the feature correlation analysis (d-Ratio) and the counterintuitive phenomenon is indirect.** Table 4 (bottom) shows that low d-Ratio correlates with NF-SLT not being top-3, but does not check whether those cases actually satisfy Definition 3.3 (i.e., that comparison models *significantly* outperform NF-SLT). The two analyses would be strengthened by linking them directly.

### Trivial

- Table 2's column header says "number of PCs" but the text describes using ICA components; this minor inconsistency should be resolved.

## Nice-to-Haves

- Applying other normalizing flow architectures (beyond NICE) to the main evaluation, to verify the effect is not specific to one flow type (the paper notes this is in Appendix G).
- A worked example computing β and γ for the CIFAR-10/SVHN case to illustrate the definition.

## Removed Points

- *Criticism about the definition conflating likelihood inversion and relative performance:* The paper's definition explicitly separates these into Assumptions 3.1 and 3.2 and requires both conditions. This is a feature, not a flaw.
- *Criticism that hyperparameter selection "inflates" NF-SLT's performance relative to baselines:* The same selection protocol is applied to all 13 models uniformly. The claim that it advantages NF-SLT over DeepSVDD/DAGMM is speculative and unsupported by evidence in the paper.
- *Criticism about PCA vs ICA terminology in Table 2:* Minor terminology issue that does not affect results.
- *Strength Finder's generic strength about "addressing an important problem":* Removed as it is superficial and not specific to the paper's contributions.
- *Criticism about missing related work comparisons:* Cannot verify without external sources.
- *Criticism about formatting, typos, or missing appendix content:* Parser artifacts in the extracted version.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify concrete values for β and γ** in Definition 3.3 and report how many datasets satisfy the definition under those thresholds. This would make the central claim precise and reproducible.

2. **Add a robustness check** for the hyperparameter selection protocol: compare the current across-dataset tuning against per-dataset tuning (with held-out validation) or default hyperparameters.

3. **Report standard deviations** for the main results in Table 1, given that 10 repeated runs were performed.

4. **Strengthen the link** between the feature correlation analysis and the counterintuitive phenomenon by checking whether datasets with low d-Ratio actually satisfy Definition 3.3 (with specified thresholds).

## Score and Decision

**Bracket analysis:** Round 1 bracketing placed the paper in [5.0, 7.0]. Round 2 narrowing queried within [(4.5, 6.5)] for tabular AD benchmarks and [(5.5, 7.5)] for normalizing flow theory. The paper is comparable to DRL (5.75, Accept) on empirical scope and to the OOD paradox paper (5.67, Reject) on theoretical ambition, but exceeds both in breadth of evaluation. It is weaker than MCM (6.67, Accept) on methodological novelty but has stronger theoretical framing and larger-scale experiments. The definitional weakness (thresholds unspecified) prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>