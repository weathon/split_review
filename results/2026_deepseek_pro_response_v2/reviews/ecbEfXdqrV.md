Now I have a clear picture. Let me finalize the review.

**Comparison summary of anchors:**
- **NCSN tabular AD (5.75)**: Method paper, limited novelty, unfair comparison criticisms. Our paper is clearly stronger with broader scope, theory, and better methodology.
- **MCM (6.67)**: Strong method paper for tabular AD with 20 datasets, 9 baselines. Our paper surpasses it with 57 datasets, 12 baselines, theoretical analysis, controlled experiments, and feature correlation analysis.
- **AnoLLM (6.75)**: LLM-based tabular AD, innovative but limited benchmarking. Our paper is more comprehensive.
- **On Diffusion Modeling for AD / DTE (7.00)**: Closest comparison — also uses ADBench, investigates generative model for tabular AD. Has novel method (DTE) but limited theory and concerns about kNN outperforming it. Our paper has more theoretical depth (Theorem 5.4, Corollary 5.6) and controlled experiments (Tables 2-3) but the definitional shift and entropy gap are concerns. Comparable overall, with our paper slightly stronger in scope and analysis.
- **Deep Orthogonal Hypersphere Compression (8.00)**: Unanimous 8s, clean theoretical method paper. Our paper has more diverse contributions but also more weaknesses, putting it below this tier.

**Final score: 7.0**

---

## Summary
This paper investigates why the counterintuitive likelihood phenomenon — where deep generative models assign higher likelihood to OOD data than in-distribution data, famously observed in image anomaly detection — rarely occurs in tabular anomaly detection. The authors propose a domain-agnostic formal definition of the phenomenon based on relative model performance, conduct extensive experiments across all 47 tabular and 10 CV/NLP embedding datasets from ADBench with 12 baselines, and provide theoretical and empirical analysis linking the rarity of the phenomenon in tabular data to lower dimensionality and weaker feature correlation compared to images.

## Strengths
- **Comprehensive empirical benchmarking**: Table 1 shows NF-SLT achieving the best average AUROC (0.8575), best average rank (3.43), highest Top2 ratio (0.45), and lowest Fail ratio (0.02) across all 47 tabular datasets from ADBench, outperforming 12 baselines including specialized deep anomaly detectors. The use of the full ADBench suite without subset selection directly addresses selection-bias concerns (Shwartz-Ziv & Armon, 2022).
- **Controlled dimensionality experiments (Tables 2-3)**: Using ICA-preprocessed images to vary retained component count, Table 2 demonstrates that under the H(P) > H(Q) condition, AUROC improves as dimension decreases (e.g., CelebA/SVHN: 0.1207 at d=1024 rising to 0.4711 at d=30). Table 3 provides complementary evidence with raw image resizing, showing the CelebA/SVHN AUROC crossing 0.5 (0.1541 → 0.7037), demonstrating that reducing spatial dimension can reverse likelihood inversion.
- **Feature-correlation analysis via intrinsic dimension**: The d_Ratio (ID/ambient dimension) analysis in Table 4 and Figure 1 provides quantitative evidence that tabular data has weaker feature correlation than images: image datasets show d_Ratio ~1-2% while tabular datasets range from 0.389 to 0.810. The within-domain analysis shows that among 25 tabular datasets where NF-SLT underperforms (rank ≥ 3), 84% have d_Ratio ≥ 0.5.
- **Theoretical framework linking dimension to likelihood inversion**: Theorem 5.4 and Corollary 5.6 extend Caterini & Loaiza-Ganem (2022)'s likelihood-gap decomposition to explicitly incorporate dimensionality, providing a principled explanation for why lower-dimensional tabular settings avoid likelihood inversion.
- **Explanation for CV/NLP embedding success**: The paper estimates intrinsic dimensions of ADBench embedding representations (CIFAR-10: d=23, SVHN: d=18 vs. ambient 1000), showing they exhibit higher d_Ratio than raw pixels, which explains NF-SLT's strong performance on embedding datasets and independently corroborates Kirichenko et al. (2020).

## Weaknesses

### Fatal
None.

### Major
- **Definitional shift from likelihood inversion to relative performance**: Definition 3.3 operationalizes the counterintuitive phenomenon through relative model performance (fraction of comparison models outperforming NF-SLT by margin > γ) rather than through direct likelihood inversion as in the literature (Nalisnick et al., 2019a). The paper justifies this shift (lines 25-27) by arguing the direct criterion is too strict — any AUROC below 100% would qualify. However, the relationship between "NF-SLT underperforms other models" and "OOD data gets higher likelihood than in-distribution data" is not analytically established. A model could exhibit likelihood inversion yet still outperform comparison models if those models also fail, or conversely underperform for reasons unrelated to likelihood inversion. The paper should explicitly discuss the scope and limitations of its definition relative to the original phenomenon.
- **Entropy estimation methodology unspecified for Tables 2-3**: The bold vertical line in Tables 2 and 3 partitions results by whether H(P) > H(Q) or H(P) < H(Q), and this partitioning drives the interpretation of the dimensionality experiments (line 162: "when H(P) > H(Q) holds, the AUROC increases as the dimensionality decreases"). The paper provides no description of how these entropies were estimated, what estimator was used, or what uncertainty is associated with the estimates. Differential entropy estimation in high dimensions is challenging, and without this information, the empirical validation of Theorem 5.4 cannot be fully assessed.

### Minor
- **Hyperparameter selection on aggregate metric**: The paper selects "the hyperparameter combination with the highest average AUROC for all datasets" (line 122). While this is not per-dataset tuning, it does optimize the reported metric across the evaluation set. Whether baseline models received the same treatment is not clearly confirmed.
- **Cross-domain d_Ratio comparison potentially confounded by ambient dimension**: The paper acknowledges that ID estimators underestimate at high true dimensions (line 220). Image datasets with d=3072 will mechanically yield lower d_Ratio than tabular datasets with d~10-100 even under similar correlation structures. The within-domain analysis (Table 4 bottom) is not affected, but the headline image-vs-tabular comparison should acknowledge this confound more explicitly.
- **β and γ thresholds not in main text**: Definition 3.3's thresholds are deferred to Appendix B. Since the definition is central to the paper's claims, readers cannot fully assess the operationalization from the main text alone.

### Trivial
- Per-dataset AUROC for the 47 tabular datasets is reported only in aggregate (Table 1 top); individual results would strengthen transparency but aggregate metrics already support the claims.
- The CIFAR-10/SVHN row in Table 2 (left side) shows AUROC moving from 0.3311 at d=1024 to 0.3143 at d=30, which does not show monotonic improvement for this particular pair — though the overall trend across pairs is consistent.

## Nice-to-Haves
- A direct measurement of the original likelihood-inversion phenomenon (e.g., the proportion of anomaly samples receiving higher likelihood than the median normal sample) alongside Definition 3.3 would strengthen the bridge to the literature.
- A dimension-manipulation experiment directly on tabular data (e.g., subsampling features) would provide more direct evidence linking dimension to the domain difference.
- Using a held-out validation split or separate tuning dataset for hyperparameter selection would strengthen methodological rigor.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim that the definitional shift is "fatal" and "structural"**: Overstated. The paper explicitly justifies its operationalization (lines 25-27). While the shift warrants acknowledgment and clarification, it does not invalidate the paper's contributions. The core empirical finding — NF-SLT performs strongly on tabular data — stands regardless. Downgraded from fatal to major.
- **Harsh Critic claim about "Lemma 5.1 and Corollary 5.5 never stated in main text"**: These are in the stripped Appendix D. Per review protocol, weaknesses about missing appendix content are removed since the original submission includes the appendix.
- **Harsh Critic claim that "the paper's definition cannot recover the original phenomenon; it can only detect competitive underperformance"**: Overstates the disconnect. The original phenomenon manifests as catastrophic NF underperformance, which Definition 3.3 is designed to detect. The paper's CIFAR-10/SVHN example (line 79) demonstrates the definition correctly identifies the known image-domain case.
- **Harsh Critic concern about "the imdb embedding result NF-SLT AUROC = 0.5013" showing the phenomenon**: The paper explicitly addresses this (line 124): the gap is only 0.038, which fails the γ-threshold. The harsh critic's speculation that it "may actually exhibit the original counterintuitive phenomenon" is at odds with the paper's operational definition.
- **Harsh Critic suggestion that only NICE was used and more expressive flows should be tested**: Results for other flows are in Appendix G (stripped, but present in original submission).
- **Strength Finder "thorough experimental protocol"**: Slightly weakened by the hyperparameter optimization concern. Partially retained.

## Novel Insights
The paper's synthesis of intrinsic dimension estimation with the tabular-vs-image domain comparison is genuinely novel. Using d_Ratio as a proxy for feature correlation strength and showing that tabular data clusters near the identity line while image data falls far below it (Figure 1 right) provides a quantitative, replicable lens for understanding why modeling assumptions that work in one domain may fail in another. The embedding analysis — showing that CV/NLP embeddings of images have higher d_Ratio than raw pixels — independently explains why NF-SLT succeeds where raw-pixel NF methods fail, connecting the correlation hypothesis to practical deployment scenarios.

## Suggestions
- State the specific β and γ values in the main text so Definition 3.3 is self-contained.
- Describe the entropy estimation method used for the H(P) > H(Q) partitioning in Tables 2-3, including the estimator and any uncertainty quantification.
- Add a discussion paragraph explicitly relating Definition 3.3 to the original Nalisnick et al. (2019a) likelihood-inversion criterion, clarifying what each captures and what the paper's definition can and cannot detect.
- Report per-dataset AUROC for NF-SLT on the 47 tabular datasets, either in the main text or clearly referenced appendix table.

## Score and Decision

**Anchor papers referenced across all rounds:**

| Paper | Path | Score | Round | Comparison |
|---|---|---|---|---|
| Normalizing Flows for OOD Detection via Latent Density Estimation | 6Z8rZlKpNT | 3.40 | R1 (weak) | Image-based OOD with NFs; narrower scope, less comprehensive. Our paper is substantially stronger. |
| Dealing with OOD in Prediction Problem | i28ZjVxl81 | 2.50 | R1 (weak) | Basic OOD on tabular, far below our paper's quality. |
| Flow-based imputation of small data | rcmhydaEJp | 3.00 | R1 (weak) | NF for imputation, different task, smaller scale. |
| Anomaly Detection by Estimating Gradients of Tabular Data (NCSN) | 7QDIFrtAsB | 5.75 | R1 (mid), R2 | Novelty and methodology concerns. Our paper is clearly stronger in scope, theory, and rigor. |
| DRL: Decomposed Representation Learning for TAD | CJnceDksRd | 5.75 | R1 (mid) | Method paper for tabular AD. Our paper has broader contributions. |
| MCM: Masked Cell Modeling for AD in Tabular Data | lNZJyEDxy4 | 6.67 | R1 (mid), R2 | Strong tabular AD method. Our paper surpasses it in benchmark scale, theoretical depth, and analysis breadth. |
| AnoLLM: LLMs for Tabular AD | 7VkHffT5X2 | 6.75 | R2 | Innovative but limited benchmark scale and methodological concerns. Our paper is stronger. |
| On Diffusion Modeling for AD (DTE) | lR3rk7ysXz | 7.00 | R2 | Closest comparison — also uses ADBench, generative modeling for tabular AD. Our paper matches it empirically but adds theory (Theorem 5.4, Corollary 5.6) and controlled experiments. Slightly stronger overall. |
| Deep Orthogonal Hypersphere Compression | cJs4oE4m9Q | 8.00 | R1 (strong), R2 | Clean theoretical method paper, unanimous 8s. Our paper has more diverse contributions but also more weaknesses, placing it below this tier. |

**Round 1 bracket:** 6.0–8.0, based on the paper clearly surpassing NCSN (5.75) and falling below the 8.0 unanimous-accept anchors.

**Round 2 narrowing:** The paper is comparable to or slightly stronger than DTE (7.00) and clearly stronger than MCM (6.67) and AnoLLM (6.75). The two major weaknesses (definitional shift not fully addressed, entropy estimation unspecified) prevent it from reaching the 8.0 tier occupied by papers with cleaner theoretical contributions and fewer methodological gaps.

**Final score:** 7.0 — a solid accept with clear strengths in empirical scale, theoretical analysis, and domain insights, burdened by two addressable major weaknesses around the definitional operationalization and entropy estimation methodology.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>