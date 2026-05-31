## Summary

This paper investigates whether the "counterintuitive likelihood phenomenon" — where deep generative models assign higher likelihoods to anomalous (OOD) samples than to normal (in-distribution) samples — also occurs in tabular anomaly detection, as it does in the image domain. The authors (1) propose a formal, domain-agnostic definition of the counterintuitive phenomenon based on relative AUROC performance against baseline models; (2) show empirically across all 47 tabular and 10 CV/NLP embedding datasets in ADBench that simple likelihood testing via normalizing flows (NF-SLT using NICE) rarely exhibits this phenomenon and in fact outperforms 12 baseline models; and (3) provide theoretical and empirical analyses explaining why — linking reduced dimensionality (via a likelihood-gap theorem) and lower feature correlation (via intrinsic dimension analysis) as the key factors.

---

## Strengths

- **Comprehensive, bias-free empirical evaluation**: Using every dataset in ADBench (47 tabular + 10 CV/NLP) without selection, and comparing against 12 diverse baselines (6 shallow + 6 deep), the authors convincingly show NF-SLT achieves the best mean AUROC (0.8575), AUPRC (0.6398), average rank (3.43), top-2 ratio (0.45), and lowest fail ratio (0.02). This is a genuinely surprising positive result for a simple, decades-old method (NICE), and the scale of the evaluation makes selection-bias arguments hard to sustain.

- **Formal definition of the counterintuitive phenomenon (Definition 3.3)**: The prior literature treated this phenomenon informally, conflating hard datasets with genuine likelihood failure. The proposed relative-AUROC definition cleanly separates these cases by requiring both that a majority of baselines outperform the generative model (condition on β) and that the performance gap is non-trivial (condition on γ). This is a useful conceptual contribution that generalizes across domains.

- **Theorem 5.4 + Corollary 5.6 and empirical support**: The authors extend the likelihood-gap expression of Caterini & Loaiza-Ganem (2022) to derive that the lower bound of the expected likelihood gap between normal and abnormal distributions decreases linearly with ambient dimension d under an independence assumption, and that the AUROC upper bound degrades correspondingly. The ICA-based dimensionality reduction experiment (Table 2) provides compelling empirical validation: AUROC for CIFAR-10/SVHN improves monotonically as retained ICA components decrease from 1024 to 30, while the reverse direction (SVHN/CIFAR-10) degrades, consistent with the entropy condition.

- **Intrinsic dimension as a correlation proxy**: Showing that tabular datasets have d-Ratio (ID/ambient dimension) near 1 while image datasets have d-Ratio near 0.002–0.019 is a concrete, quantitative explanation of why the inductive bias of CNNs (exploiting pixel locality) does not apply to tabular settings. The toy Gaussian autoregressive covariance experiment validates the ID-correlation link. The finding that NF-SLT fails most often on low-d-Ratio tabular datasets (Table 4, lower section) ties the two analyses together.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 5.4 assumes full dimensional independence**: The theorem's central structural assumption is P = ∏ p_i(x_i) and Q = ∏ q_i(x_i), i.e., all dimensions are mutually independent. Real tabular data violates this. The paper invokes Fact 1.2 to argue correlations are weak in tabular data, but weak correlation ≠ independence. The theoretical guarantee (linear decrease in likelihood-gap lower bound with d) is formally valid only in this idealized setting. For correlated tabular distributions, the bound's tightness is unclear, and no analysis of robustness to violations of this assumption is provided.

2. **Definition 3.3 leaves β and γ unspecified in the main paper**: The full specification is deferred to Appendix B (unavailable due to parsing). Without knowing the exact values, the reader cannot independently verify whether the reported experimental outcomes satisfy the definition. The motivating CIFAR-10/SVHN example (AUROC 6.4% vs. 90%+) is clearly covered, but where the boundary sits for borderline tabular cases (e.g., the "yeast" dataset) remains opaque. Even a single illustrative numerical instantiation in the main text would substantially strengthen the paper's self-containedness.

3. **Potential confound in the dimensionality experiment (Table 2)**: The ICA reduction experiment uses RealNVP with MLP backbone, while the image baseline uses Glow with CNN backbone (Table 3). Switching both the dimensionality and the architecture simultaneously makes it difficult to attribute AUROC changes solely to dimensionality. A controlled experiment holding architecture fixed while varying dimensionality would yield cleaner evidence.

### Minor

1. **CV/NLP embedding results** (Table 1, bottom): NF-SLT also dominates on most embedding datasets. The explanation (embeddings have higher d-Ratio than raw pixels) is plausible and consistent with Kirichenko et al. (2020), but it is somewhat post-hoc. The imdb failure case (0.5013) is dismissed because the gap is small, which is reasonable under Definition 3.3 but warrants brief quantitative justification.

2. **Choice of NICE as the representative flow**: NICE is one of the simplest, oldest NF architectures. The good performance could partially arise from its limited expressiveness acting as an implicit regularizer that avoids overfitting to "complexity" patterns in training data. While Appendix G reports other flows, the main text does not analyze whether and why simpler architectures are preferable.

3. **d-Ratio as a proxy for correlation is indirect**: The argument is: high correlation → low ID → low d-Ratio → worse NF performance. This chain is suggestive but is not formalized beyond the toy Gaussian example. The toy example assumes autoregressive structure; heterogeneous tabular features may have complex non-linear dependencies not captured by Pearson-type correlation.

### Trivial
None worth noting given parser damage expectations.

---

## Nice-to-Haves

- Explore whether modern flow architectures (e.g., coupling flows with attention, flow matching) change the conclusions or alter the d-Ratio threshold at which performance degrades.
- A short ablation in the main text specifying the β/γ values used and showing sensitivity to those choices would make Definition 3.3 fully self-contained.
- Extending Theorem 5.4 to distributions with bounded or weak correlation (e.g., using mixing conditions or factor models) would substantially strengthen the theoretical contribution.

---

## Novel Insights

The most genuinely novel observation is the empirical inversion: NF-SLT, using the simplest normalizing flow (NICE) and only the raw likelihood score, outperforms 12 dedicated anomaly detection methods—including sophisticated deep models—across a full benchmark without any selection. This directly contradicts the prevalent intuition (inherited from image results) that likelihood-only tests are unreliable. The theoretical framing linking this success to the dimensionality regime and intrinsic dimensionality ratio (d-Ratio) provides a principled way to predict *when* the counterintuitive phenomenon is likely to emerge in any domain, not just tabular data. The finding that even CV/NLP embeddings avoid the phenomenon because their d-Ratio is substantially higher than raw pixel data offers a testable explanatory framework for why representation learning "cures" likelihood inversion in images.

---

## Suggestions

- Specify β and γ numerically in the main text and add a brief robustness analysis showing results change little for nearby parameter values.
- Add an experiment holding the NF architecture fixed (MLP-based RealNVP) while varying dimensionality via ICA to cleanly isolate the dimensionality effect from architectural effects.
- Discuss or bound the error introduced by the independence assumption in Theorem 5.4, e.g., via a covariance-aware extension or empirical verification on synthetic correlated data.
- Report variance/confidence intervals in Table 1 (AUROC and AUPRC), since 10-run averages are computed; the overall superiority of NF-SLT could be underscored with statistical tests.

---

## Score and Decision

The paper addresses a well-motivated question, answers it with unusually comprehensive experiments (no selection bias), makes a clear conceptual contribution (Definition 3.3), delivers a surprisingly strong practical result (NF-SLT dominates across the board), and provides supporting theory and ID analysis. The main weaknesses—the independence assumption in Theorem 5.4 and the incompletely specified definition—are real but do not undermine the core empirical finding, which is robust across 57 datasets and 12 baselines. The work brings actionable value to practitioners using normalizing flows for tabular anomaly detection.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>