## Summary

This paper investigates whether the "counterintuitive phenomenon" — wherein deep generative models assign higher likelihoods to anomalous/OOD data than to in-distribution data — occurs in tabular anomaly detection settings. The authors propose a formal, domain-agnostic definition of the phenomenon (Definition 3.3) based on comparative AUROC performance, conduct an extensive benchmark across 47 tabular and 10 CV/NLP embedding datasets from ADBench (against 12 baselines), and show that a simple normalizing flow likelihood test (NF-SLT) is consistently the top performer. They further provide a theoretical explanation via dimensionality (Theorem 5.4, Corollary 5.6) and an empirical explanation via feature correlation (d Ratio analysis).

---

## Strengths

- **Comprehensive, bias-free benchmark (Table 1):** The evaluation spans all 47 tabular and 10 CV/NLP embedding datasets in ADBench, explicitly motivated by avoiding selection bias (Shwartz-Ziv & Armon, 2022). With 12 baselines and 10-repeat averaging, NF-SLT achieves average rank 3.43, top-2 ratio 0.45, and fail ratio 0.02 — far stronger than any comparison model — making the core empirical claim robustly grounded.

- **Domain-agnostic operational definition (Definition 3.3):** Prior characterizations of the counterintuitive phenomenon were vague or dataset-specific. The paper introduces a quantitative definition based on relative AUROC ranking (Equations 2–3), which allows consistent cross-domain evaluation and directly explains why the "yeast" dataset (minimum AUROC gap of 0.02 vs. MCM) does not constitute a genuine occurrence of the phenomenon.

- **Dimensionality reduction experiment partially confirms theory (Table 2):** For CIFAR-100/SVHN, AUROC rises from 0.0843 at 1024 ICA components to 0.3490 at 30 components, and for CelebA/SVHN from 0.1207 to 0.4711, providing direct empirical support for the claim that reduced dimensionality alleviates likelihood inversion when H(P) > H(Q) holds. The right-side cases (where H(P) < H(Q)) show the expected monotone decrease, demonstrating internal consistency.

- **d Ratio analysis is the most direct mechanistic support (Figure 1, Table 4):** The quantification of feature correlation via the ratio of intrinsic dimension to ambient dimension yields a concrete, measurable contrast: tabular d Ratios range 0.389–0.810 while image d Ratios cluster near 0.002–0.019. Table 4 (bottom) shows that among the 25 datasets where NF-SLT doesn't rank first, those with low d Ratio are systematically over-represented, directly linking correlation structure to model performance. The Gaussian toy experiment (Figure 1, left/center) validates that higher correlation reduces estimated intrinsic dimension.

- **CV/NLP embedding consistency (Table 1, bottom):** NF-SLT outperforms all deep baselines on 9/10 embedding datasets, with the single exception (imdb) showing only a 0.0385 AUROC gap that fails to meet the gap criterion in Definition 3.3. The intrinsic dimension estimates for CIFAR-10 and SVHN embeddings (23 and 18 at 1000 ambient dimensions, vs. 11 and 7 at 3072 raw dimensions) extend the d Ratio explanation beyond tabular data.

---

## Weaknesses

### Fatal
None.

### Major

- **Independence assumption in Theorem 5.4 is not universally satisfied in tabular data, limiting the theorem's explanatory scope.** Theorem 5.4 explicitly requires P = ∏pᵢ(xᵢ) and Q = ∏qᵢ(xᵢ) to be product (independent) distributions. The paper simultaneously argues in Section 5.2 that tabular datasets with low d Ratio have correlated features, and Table 4 (top) shows tabular datasets spanning d Ratios of 0.389–0.810 — meaning substantial correlation exists in many cases. The claim in the Introduction ("although there are datasets in the tabular domain that have higher dimensions than images or strong correlation...") explicitly acknowledges exceptions but does not demarcate where Theorem 5.4 applies. As a result, the theorem cannot serve as a full theoretical foundation for the main result; it applies only to the subset of near-independent tabular datasets. The paper partially compensates with the empirical d Ratio analysis, but the connection between the independence-dependent theorem and the broad empirical claim is underdeveloped. The paper should either scope the theorem more carefully or provide a version that handles bounded correlation.

### Minor

- **Table 2 (ICA experiment) provides mixed, not uniform, support for Corollary 5.6.** The CIFAR-10/SVHN pair — arguably the most prominent case from prior work — shows negligible improvement as dimensionality drops from 1024 to 30 (0.3311 → 0.3143), while CIFAR-100/SVHN and CelebA/SVHN show clearer improvements. The authors do not discuss why CIFAR-10/SVHN behaves differently from the other two pairs under ICA reduction, which weakens the claim that "when H(P) > H(Q) holds, the AUROC increases as the dimensionality decreases."

- **The entropy condition H(P) > H(Q) — the trigger for the counterintuitive phenomenon under Theorem 5.4 — is never empirically verified for the tabular datasets in ADBench.** Section 5.1 uses this condition to explain image-domain failure, but if many tabular AD tasks naturally satisfy H(P) < H(Q) (normal data has lower entropy than anomalous data), the favorable behavior of NF-SLT could be partly attributed to the entropy relationship being favorable rather than solely to dimensionality effects. Even approximate entropy estimates for representative tabular datasets would clarify whether the theorem's dangerous condition is commonly encountered.

- **The d Ratio analysis is fully detailed for only 4 tabular datasets in Table 4 (top).** Figure 1 (right) provides a visual overview of all ADBench datasets, but explicitly reported d Ratios and ID estimates for the full 47-dataset pool would strengthen the claim that tabular datasets *generally* exhibit high d Ratio. The current presentation makes it difficult to quantitatively assess how universal the tabular/image separation is.

### Trivial
None worth noting beyond parser artifacts.

---

## Nice-to-Haves

- Providing β and γ values explicitly in the main text (not just Appendix B) would make Definition 3.3 immediately self-contained and allow readers to assess threshold sensitivity without consulting the appendix.
- A sensitivity analysis showing whether the "rare" conclusion is robust to ±20% variation in β and γ would demonstrate that the result is not an artifact of specific threshold choices.
- Reporting the d Ratio for all 47 tabular datasets and plotting per-dataset AUROC directly against d Ratio (rather than bucketed thresholds in Table 4 bottom) would convert the correlation analysis from suggestive to quantitatively compelling.
- Relaxing the independence assumption in Theorem 5.4 — even to a bounded-pairwise-correlation setting — would substantially extend the theorem's applicability to the actual tabular datasets studied.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic – Definition is circular with AUROC (partially):** The critic argues that the AUROC-based definition conflates "does NF-SLT work?" with "does likelihood inversion occur?" This is a thoughtful concern, but the paper explicitly motivates the definition by showing that direct likelihood comparison is insufficient (Section 3, paragraph 2). The operationalization via comparative ranking is a deliberate design choice, not an oversight. Removed as overstated.

- **Harsh Critic – β and γ values absent from main text (structural gap):** The paper explicitly states "The fully rigorous formulation of Definition 3.3 is provided in Appendix B." Per hard rules, criticisms of missing appendix content must be removed. The β/γ specificity concern is retained only as a nice-to-have.

- **Harsh Critic – Minimum gap statistic in Equation 3 is weakly motivated and easy to satisfy:** The critic claims using minimum gap makes the condition easy to satisfy, but this misreads the equation. The minimum gap condition in Equation 3 requires that *every* outperforming model exceeds the threshold γ — a stricter condition than using average gap. The critic's reasoning is factually incorrect about the direction of the stringency; removed.

- **Harsh Critic – Hyperparameter selection asymmetry:** The paper states the highest-average-AUROC selection criterion for all models (Section 4, "Evaluation"), not exclusively NF-SLT. The concern about asymmetric tuning is speculative and relies on assumptions about comparison model setup that are not established by the paper. Hyperparameter details are in Appendix F. Removed per hard rules about appendix and per the speculative nature of the claim.

- **Harsh Critic – Table 3 (bilinear interpolation) shows AUROC decreasing with dimension, attributed post-hoc to bilinear interpolation strengthening correlations:** This is a valid observation that the paper addresses explicitly: "Since this experiment uses raw images, independence between pixels is not guaranteed, so the theorem presented in Appendix D cannot be applied." The experiment is explicitly scoped as a non-theorem-supporting check of dimensionality trends, not as proof of the theorem. The post-hoc nature of the bilinear explanation is noted but the paper honestly scopes the experiment's purpose. Removed as overstated.

- **Strength Finder – "addresses an important problem"** (generic): Removed as insufficiently concrete.

---

## Novel Insights

The d Ratio — ratio of intrinsic dimension to ambient dimension, estimated via TwoNN/MLE — provides a genuinely practical diagnostic for predicting when likelihood-based anomaly detection will succeed or fail, both within and across domains. The finding that tabular datasets from ADBench cluster near d Ratio ≈ 0.4–0.8 while image datasets cluster near d Ratio ≈ 0.002–0.02 quantifies a long-suspected qualitative difference. The secondary finding (Table 4, bottom) that even within tabular data, NF-SLT's failure rate correlates monotonically with decreasing d Ratio (from 16% failure at d Ratio < 0.1 to 100% at d Ratio ≥ 0.8, where "failure" means rank ≥ 3) provides a usable practitioner heuristic: compute the d Ratio of a new tabular dataset before deciding whether to use NF-SLT. This is a modestly novel, actionable insight beyond the paper's stated contributions.

---

## Suggestions

1. **Scope Theorem 5.4 explicitly** to near-independent distributions and frame Section 5.2 as the complementary empirical explanation for correlated tabular data, making clear that the two analyses cover different regimes rather than presenting the theorem as a general explanation.
2. **Add a scatter plot of per-dataset NF-SLT AUROC vs. d Ratio** across all 47 tabular datasets (with regression line) to quantitatively demonstrate the correlation between d Ratio and performance.
3. **Include a brief entropy analysis** (even k-NN entropy estimates) for a sample of tabular datasets to clarify how often H(P) > H(Q) holds in tabular AD and whether the theoretical failure condition is commonly encountered.
4. **Discuss the CIFAR-10/SVHN ICA anomaly** (Table 2, left column) — the minimal improvement for that pair relative to CIFAR-100/SVHN and CelebA/SVHN warrants at least a sentence explaining why the entropy condition alone may not be sufficient.

---

## Score and Decision

**Axis assessment:**
- *Originality*: The research question (does the image-domain phenomenon generalize to tabular?) is well-framed and the d Ratio analysis is a concrete novel contribution, but the overall approach is a systematic benchmark study rather than a fundamental methodological innovation. Moderate originality.
- *Importance*: Tabular anomaly detection is widely practiced; showing a simple, principled baseline consistently outperforms complex alternatives is practically valuable.
- *Claims well-supported*: The core empirical claim (phenomenon is rare) is strongly supported. The theoretical claim (dimensionality explains it) is well-supported in the independence regime but has acknowledged scope limitations.
- *Soundness of experiments*: High — comprehensive coverage of ADBench, 10-repeat averaging, full hyperparameter search.
- *Clarity*: Generally clear and well-organized; the independence assumption gap in Section 5.1 is underemphasized.
- *Community value*: High as a reference study; practitioners can use Table 1 directly and the d Ratio heuristic practically.

The paper's core contribution is empirically solid and the theoretical framework, while limited in scope, provides genuine insight. The major weakness (independence assumption scope) does not invalidate the core finding — it limits the reach of the theorem, not the empirical result. Borderline accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>