Now I have enough calibration data. Let me finalize the review.

**Round 1 Bracket:** Based on the comparison anchors — strong reject (2.0-2.33), weak (3.75-4.25), middle (4.67-5.75), middle-upper (6.50-6.75), strong (8.00) — this paper falls in the 5.0-6.5 range.

**Round 2 Narrowing:** Anchors at 5.67 (jQ596tXT3k - OOD paradox through LID), 5.75 (7QDIFrtAsB - NCSN for tabular AD, extensive ADBench experiments), 5.75 (CJnceDksRd - DRL for tabular AD), 6.00 (3a505tMjGE - AVOID for VAE OOD), and 6.67 (lNZJyEDxy4 - MCM, accepted). 

The paper under review is comparable to 7QDIFrtAsB (5.75) in empirical scope (both use ADBench extensively) but has stronger theoretical contributions. However, it has a significant definitional issue (redefining the counterintuitive phenomenon via AUROC comparison rather than likelihood inversion) that the 5.75 anchors do not. It is clearly below MCM (6.67) in methodological clarity and contribution focus. I place it at **5.5**.

---

## Summary
This paper investigates whether the "counterintuitive phenomenon" — where deep generative models assign higher likelihood to OOD/anomalous data than to in-distribution data — extends from images to tabular anomaly detection. The authors propose a domain-agnostic definition (Definition 3.3) based on relative AUROC performance, conduct experiments on all 47 tabular and 10 CV/NLP embedding datasets from ADBench with 12 baselines, and find that NF-SLT (NICE flow with likelihood test) performs strongly (AUROC 0.8575, Fail Ratio 0.02). They offer a two-part explanation: lower dimensionality (Theorem 5.4, Corollary 5.6) and weaker feature correlations (quantified via intrinsic dimension) in tabular data.

## Strengths
- **Comprehensive, selection-bias-free benchmark (Table 1):** The paper evaluates on all 47 tabular and 10 CV/NLP embedding datasets from ADBench against 12 baselines (6 shallow, 6 deep). NF-SLT achieves the best AUROC (0.8575), best average rank (3.43), and lowest Fail Ratio (0.02). This directly addresses Shwartz-Ziv & Armon (2022)'s critique of selective dataset reporting.
- **Controlled dimensionality-reduction experiments (Tables 2 and 3):** The ICA-based experiment (Table 2) isolates dimension effects under independence — e.g., CIFAR-100/SVHN AUROC rises from 0.0843→0.3490 as dimension drops from 1024 to 30 when H(P) > H(Q). Table 3 tests in a non-independent setting with bilinear resizing and Glow, showing consistent trends and even recovering AUROC > 0.5 (CelebA/SVHN: 0.1541→0.7037 at 8×8). Both tables include reversed-entropy conditions, ruling out the possibility that dimension reduction always helps regardless of entropy ordering.
- **Feature correlation quantification via intrinsic dimension (Figure 1, Table 4):** The paper validates the correlation-ID relationship with synthetic Gaussian experiments (Figure 1 left/center), then applies TwoNN/MLE to real data. Image datasets show d Ratios of 0.2–1.9% while tabular datasets like magicgamma (0.700) and waveform (0.810) are far higher. The bottom of Table 4 shows that among datasets where NF-SLT ranks ≥3, 92% have d Ratio ≥ 0.7, linking feature correlation to NF-SLT performance even within tabular data.
- **Theoretical analysis of dimensionality (Theorem 5.4, Corollary 5.6):** The paper extends Caterini & Loaiza-Ganem (2022)'s likelihood-gap decomposition by analyzing the dimension-dependent term, showing the expected likelihood gap degrades linearly with dimension under independence assumptions. This provides a principled mechanism for why low-dimensional tabular data avoids the phenomenon.

## Weaknesses

### Fatal
None.

### Major
- **Definition 3.3 measures relative model performance, not likelihood inversion:** The original counterintuitive phenomenon (Nalisnick et al., 2019a) is defined concretely: OOD samples receive higher likelihood than in-distribution samples under the generative model. Definition 3.3 replaces this with a benchmark-relative AUROC comparison — a phenomenon occurs when a majority of comparison models outperform the generative model by a significant margin. These are different quantities: a model could have correctly ordered likelihoods but poor AUROC due to overlapping distributions, or inverted likelihoods with AUROC > 0.5. The paper acknowledges limitations of the original definition (lines 24–27) and explicitly motivates its redefinition, but the paper's title, abstract, and framing present the work as studying "the counterintuitive phenomenon" as if the two definitions are interchangeable. The empirical findings about NF-SLT's strong performance are robust regardless, but the paper should explicitly distinguish its operationalized definition from the original likelihood-inversion concept.
- **Hyperparameter selection uses test-set performance (line 122):** The paper states: "the hyperparameter combination with the highest average AUROC for all datasets is selected as the representative hyperparameter combination." This means hyperparameters are chosen to maximize performance on the same data used for evaluation, producing optimistically biased AUROC estimates. While the paper appears to use a single global hyperparameter choice across all datasets (mitigating per-dataset overfitting), and this practice is not uncommon in unsupervised anomaly detection where labeled validation data is unavailable, it remains a methodological concern that inflates reported performance relative to a proper held-out tuning protocol.

### Minor
- **Gap between mean likelihood gap (Theorem 5.4) and AUROC bound (Corollary 5.6):** Theorem 5.4 establishes that the lower bound of the expected likelihood gap decreases linearly with dimension, but AUROC depends on the full overlap of likelihood distributions, not just their mean difference. Corollary 5.6 adds moment-scaling assumptions to bridge this gap, but the derivation is consigned to Appendix D and the connection is gestured at rather than fully substantiated in the main text. The empirical results in Tables 2–3 provide convergent support, so this does not undermine the paper's conclusions, but the theoretical AUROC claim should be presented with appropriate caution.
- **The paper never reports actual likelihood values for in-distribution vs. OOD data:** Given that the original phenomenon concerns likelihood inversion, reporting these values for even a few representative datasets would directly address the question without relying solely on the AUROC-based proxy. This would strengthen the paper's case considerably.
- **Rank ≥ 3 as indicator of NF-SLT difficulty (Table 4 bottom):** With 13 total models, rank 3 is approximately the 77th percentile — not clearly a "failure." The paper is transparent about this threshold, but the analysis would be more informative with a finer-grained breakdown or a justification for this specific cutoff.

### Trivial
None.

## Nice-to-Haves
- Testing with additional flow architectures (RealNVP, residual flows) on the full tabular benchmark to confirm the findings generalize beyond NICE. The paper mentions Appendix G contains these results.
- Direct in-distribution vs. OOD likelihood histogram comparisons on a few representative tabular datasets to complement the AUROC-based analysis.
- Per-dataset validation splits or cross-validation for hyperparameter tuning rather than test-set optimization.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **β and γ unspecified (Harsh Critic):** The paper states "The fully rigorous formulation of Definition 3.3 is provided in Appendix B." The appendix is stripped by the parser — these values exist in the original submission. Per hard rule: REMOVED.
- **"Only NICE is used" (Harsh Critic):** The paper notes "the results of applying other flows to NF-SLT are included in Appendix G." The appendix is stripped. Per hard rule about missing appendix: REMOVED.
- **CV/NLP embeddings don't test the phenomenon in the image domain (Harsh Critic):** The paper is explicit that these are embedding datasets, not raw images, and discusses them separately (Table 1 bottom, Section 5.2 final paragraph). This is a reviewer misreading. REMOVED.
- **CIFAR-10/SVHN validation of Definition 3.3 is circular (Harsh Critic):** The definition is designed to capture known cases so it can be applied to new domains. Using a canonical case as a validating example is standard practice, not circular reasoning. REMOVED.
- **Assumption 3.1 is questionable — comparison models could be strong while likelihoods are merely uninformative (Harsh Critic):** This hypothetical scenario does not occur in the paper's empirical results (NF-SLT achieves strong absolute AUROC of 0.8575, not ≈0.5). The concern is speculative and does not affect any reported finding. REMOVED.
- **"VAEs and GANs cannot obtain the estimated likelihood" (line 53) is not strictly true (Harsh Critic):** While VAEs provide a lower bound and GAN-based density estimators exist, the paper's statement is a reasonable simplification for the flow-centric context. REMOVED as a nitpick.
- **Fail Ratio is a restatement of NF-SLT having good rank (Harsh Critic):** The paper uses Fail Ratio as supporting evidence, not as the operationalization of the definition. The definition itself is given by Equations (2) and (3). REMOVED as a misunderstanding.

## Novel Insights
The paper's most genuinely novel observation is the operationalization of feature correlation through the d Ratio (intrinsic dimension / ambient dimension) and its connection to NF-SLT performance. The synthetic validation (Figure 1 left/center) cleanly demonstrates that stronger correlation reduces estimated ID, and the application to real datasets reveals a stark domain gap: image datasets have d Ratios of ~1% while tabular datasets are orders of magnitude higher (0.4–0.8). This provides a measurable, domain-agnostic quantity that predicts when likelihood-based anomaly detection will succeed, going beyond generic claims about "heterogeneity" and offering a concrete direction for future work on when and why likelihood-based OOD detection fails.

## Suggestions
- Reframe the paper's central claim more precisely: rather than "the counterintuitive phenomenon is rare in tabular data," state "NF-SLT is a competitive anomaly detector on tabular data, and the mechanisms that cause likelihood inversion in images (high dimension, strong feature correlation) are largely absent in tabular settings." This preserves the paper's contributions while avoiding the definitional tension.
- Include a small table or figure showing actual in-distribution vs. OOD likelihood distributions for 3–4 representative tabular datasets, directly demonstrating that likelihood ordering is preserved.
- If feasible, report results using a held-out validation split for hyperparameter selection, or explicitly discuss the limitations of the current protocol and why labeled validation data is unavailable in the unsupervised anomaly detection setting.

## Anchor Comparison

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| OOD Paradox through LID | jQ596tXT3k | 5.67 | R1/R2 | Similar topic (OOD, likelihood, flows). Our paper has broader empirical scope (57 vs 8 datasets) but a more significant definitional tension. Comparable. |
| NCSN for Tabular AD | 7QDIFrtAsB | 5.75 | R1/R2 | Similar empirical scope (ADBench). Our paper has stronger theoretical analysis but comparable methodological concerns (validation set usage). Comparable. |
| DRL for Tabular AD | CJnceDksRd | 5.75 | R2 | Method paper accepted at 5.75. Our paper is an investigation rather than a method proposal; different contribution type but similar overall quality. |
| AVOID for VAE OOD | 3a505tMjGE | 6.00 | R2 | Stronger theoretical analysis and clearer contribution framing than our paper. Our paper's definitional issue makes it slightly weaker. |
| MCM for Tabular AD | lNZJyEDxy4 | 6.67 | R1 | Clearly stronger — novel method, clean evaluation, well-justified contribution. Our paper is below this level. |
| Soft Checksums | aAI92OHA4t | 2.33 | R1 | Strong reject — fundamentally different quality tier. Our paper is far above. |
| Deep Orthogonal Hypersphere | cJs4oE4m9Q | 8.00 | R1 | Strong accept — fundamentally different quality tier. Our paper is far below. |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowing:** The paper sits between 7QDIFrtAsB (5.75) and 3a505tMjGE (6.00) in empirical contribution, but the definitional redefinition issue pulls it below both. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>