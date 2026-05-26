Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper investigates whether the well-known "counterintuitive phenomenon" (where generative models assign higher likelihoods to anomalous/OOD data than to in-distribution data) occurs in tabular anomaly detection. It proposes a domain-agnostic formal definition (Definition 3.3) based on relative performance against comparison models, then conducts extensive experiments on all 47 tabular datasets and 10 CV/NLP embedding datasets from ADBench with 12 baselines. The paper finds that NF-SLT (Normalizing Flow Simple Likelihood Test) achieves the highest average AUROC (0.8575), Top2 Ratio (0.45), and lowest Fail Ratio (0.02), and provides theoretical and empirical analyses linking the rarity of the phenomenon in tabular data to lower dimensionality and weaker feature correlation compared to images.

## Strengths

1. **Domain-agnostic formal definition of the counterintuitive phenomenon.** Definition 3.3 (Section 3) provides clear quantitative conditions using β and γ thresholds and a minimum performance gap, addressing the lack of precise formalization in prior work that relied on ad-hoc comparisons.

2. **Large-scale, unbiased empirical evaluation.** The paper uses all 47 tabular and 10 CV/NLP embedding datasets from ADBench without selection bias (acknowledging Shwartz-Ziv & Armon, 2022), and compares against 12 baseline models spanning shallow and deep anomaly detection methods. NF-SLT achieves the highest average AUROC (0.8575), highest Top2 Ratio (0.45), and lowest Fail Ratio (0.02) on tabular data (Table 1).

3. **Theoretical analysis linking dimensionality to likelihood degradation.** Theorem 5.4 proves that under independence and an entropy condition, the lower bound of the likelihood gap decreases linearly with dimension. Corollary 5.6 connects this to an inversely related upper bound on AUROC, providing a theoretical basis for why high-dimensional images are more susceptible to the phenomenon.

4. **Empirical validation of the dimensionality effect on image data.** ICA-based dimension reduction (Table 2) and bilinear image resizing (Table 3) experiments show that reducing image dimensionality consistently improves AUROC in the regime where the entropy condition holds, supporting the theoretical prediction.

5. **Feature correlation analysis via intrinsic dimension.** The paper quantifies overall feature correlation through the d-Ratio (ID / ambient dimension). Image datasets have d-Ratio ~0.002–0.019 while tabular datasets reach 0.389–0.810 (Table 4, Figure 1). The analysis further shows a monotonic relationship between correlation strength and ID reduction in synthetic Gaussian data (Figure 1 left/center), and that 84% of datasets where NF-SLT ranks ≥3 have d-Ratio below 0.5 (Table 4 bottom).

6. **Explanation for success on CV/NLP embeddings.** The estimated ID of CIFAR-10 and SVHN embeddings (23 and 18 relative to ambient 1000) is higher than for raw pixels, explaining why NF-SLT performs well on these embeddings despite the image origins.

## Weaknesses

### Fatal
None.

### Major

1. **Definition 3.3 is proposed but never directly operationalized.** The definition introduces parameters β and γ, yet the paper never specifies their values, discusses how they should be set, or computes per-dataset whether the conditions hold. Instead, the empirical argument relies on aggregate metrics (Avg. Rank, Top2 Ratio, Fail Ratio) and qualitative gap comparisons (e.g., the 0.02 gap on 'yeast'). The paper claims the phenomenon is "rare" using reasoning consistent with the spirit of the definition, but does not implement the definition itself. The fully rigorous formulation is deferred to Appendix B (stripped in this version), but the main text lacks any concrete threshold application. This gap between the stated methodology and the evidence presented weakens the central claim.

### Minor

1. **Hyperparameter selection conflates model selection and evaluation.** The paper states that "the hyperparameter combination with the highest average AUROC for all datasets is selected" — meaning test-set performance was used to choose a single global hyperparameter configuration. No separate validation split is described. While the global (rather than per-dataset) selection mitigates the most severe overfitting concerns and the procedure applies to all models equally (so relative comparisons remain meaningful), the reported absolute AUROC values may be optimistic and do not represent unbiased estimates of generalization performance.

2. **No variance or uncertainty reported despite 10 repeated experiments.** Table 1 reports only mean AUROC and AUPRC without standard deviations, confidence intervals, or statistical tests. For small performance gaps (e.g., 0.02 on 'yeast' discussed in the text), the reader cannot assess whether differences are meaningful relative to experimental noise.

3. **Limited intrinsic dimension analysis for CV/NLP embeddings.** The ID analysis supporting the explanation for NF-SLT's success on embeddings is performed only for CIFAR-10 and SVHN embeddings (2 of 10 embedding datasets). The paper then generalizes conclusions about "embeddings having higher ID ratios" to all 10 datasets without direct evidence for the remaining 8 (20news, agnews, amazon, imdb, yelp, etc.).

4. **Non-standard data split relative to ADBench protocol.** The paper uses a 50-50 normal-data split (following Zong et al., 2018) rather than ADBench's default 80-20 protocol, without comparing results under the standard split or justifying the deviation. This makes direct comparison with prior ADBench findings difficult.

5. **Theoretical analysis rests on strong assumptions that are not met by real data.** Theorem 5.4 assumes independent dimensions and perfect density estimation; Corollary 5.6 additionally assumes specific moment scaling conditions. The paper acknowledges these limitations (e.g., "Since this experiment uses raw images, independence between pixels is not guaranteed, so the theorem...cannot be applied"), but the connection between the idealized theory and the real tabular data experiments remains largely suggestive rather than demonstrative.

6. **Feature correlation analysis conflates low intrinsic dimension with correlation.** The paper equates low d-Ratio with strong feature correlation, but many factors beyond correlation (manifold structure, data sparsity, estimation bias) can reduce ID estimates. The synthetic Gaussian example isolates correlation cleanly, but for real tabular data the interpretation is less direct.

### Trivial
None.

## Nice-to-Haves

- **Operationalize Definition 3.3** by choosing explicit β and γ values (e.g., β = 0.5, 0.6 and γ = 0.05, 0.1) and computing per-dataset whether the counterintuitive phenomenon occurs. This would directly test the paper's own criterion.
- **Adopt a proper validation split** for hyperparameter selection, or at minimum compare results under the ADBench default split on a subset of datasets to establish robustness.
- **Report per-dataset results with variance** (e.g., mean ± std over the 10 runs) in an appendix, summarized for the main claims.
- **Discuss the sensitivity** of the phenomenon classification to different β/γ choices and to the set of comparison models used.
- **Provide a characterization** of the types of tabular datasets where NF-SLT performs less well (low d-Ratio datasets), giving a more balanced picture of when likelihood-based detection might still face challenges.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **OOD vs anomaly detection conflation (Harsh Critic Section-by-Section Note on Introduction/Footnote 1):** The paper explicitly acknowledges the distinction in Footnote 1 ("Although the two tasks slightly differ, we consider OOD detection and anomaly detection to be the same task") and refers to Appendix A for full task definitions. This is a transparent design choice, not a weakness. **Reason for removal:** The paper already addresses this; it is a stated assumption, not an oversight.

- **Theoretical analysis "provides intuition rather than proof" characterization:** The paper acknowledges the limitations of its theoretical assumptions (e.g., noting when theorems cannot be applied to real data). The theoretical analysis is intended as explanatory framing, not as a formal proof that covers all real cases. **Reason for removal:** The paper is transparent about the scope of the theory; the criticism restates what the paper already acknowledges.

- **"Strengthening the Paper on Its Own Terms" suggestions** (operationalize Definition 3.3, adopt validation procedure, report variance): These are constructive suggestions, not weaknesses. They have been incorporated into the Nice-to-Haves section above.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the paper's framing and evidence imply that the *type* of anomaly detection task may be as important as the data modality for determining whether likelihood-based methods are reliable. The paper's success on CV/NLP embeddings (which are high-dimensional but semantically meaningful) suggests that the relevant factor is not dimensionality *per se* but whether the features capture semantic signal or low-level pixel statistics. This insight — that the failure mode in images may be specific to raw pixel representations rather than to high-dimensional data in general — is an interesting synthesis that the paper partly makes but could develop further.

## Suggestions

1. **Most important:** Specify concrete β and γ thresholds and apply Definition 3.3 directly to each dataset, reporting how many datasets satisfy the counterintuitive phenomenon condition. This bridges the gap between the formal definition and the empirical evidence.
2. When possible, add a validation split for hyperparameter selection, or at minimum report results under the ADBench default 80-20 split on a subset of datasets to demonstrate robustness.
3. Add standard deviations or confidence intervals to Table 1 (or a supplementary table) to allow readers to assess the significance of observed differences.
4. Extend the ID analysis to the remaining CV/NLP embedding datasets (beyond CIFAR-10 and SVHN) to strengthen the generalization claim about embeddings.
5. Clarify the hyperparameter selection procedure: was the same global selection applied to all 12 baseline models, or only to NF-SLT? If the former, state this explicitly.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>