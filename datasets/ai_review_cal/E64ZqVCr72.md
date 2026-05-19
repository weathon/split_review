- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3
Now I have all the information I need to produce the consolidated review. Let me verify the key claims against the actual paper text before writing.

## Summary
The paper proposes a feature-disentanglement network (FDN) for active domain adaptation (ADA) in medical image classification. It decomposes images into domain-specific and task-specific features, then selects informative target-domain samples via a composite score combining uncertainty, domainness, density, and novelty. The method is evaluated on CAMELYON17 (histopathology) and NIH→CheXpert (chest X-ray) benchmarks, with ablation studies on loss terms and selection criteria.

## Strengths

- **Well-motivated feature-disentanglement framework for cross-domain informative sample selection.** The FDN separates domain-specific (`z_dom`) and task-specific (`z_task`) features, with loss terms that encourage task-feature alignment across domains (L₂) while decorrelating domain and task features (L₃). The design is grounded in the intuition that a classifier trained on source `z_task` should produce reliable uncertainty estimates on target `z_task`, enabling active learning under domain shift. The ablation results confirm each loss term contributes: removing L_base drops average AUC substantially on CAMELYON17.

- **Composite informativeness score with ablated component contributions.** The four-criteria score (uncertainty, domainness, density, novelty) is more principled than single-criterion selection for cross-domain settings. The domainness criterion (Eq. 8) uses percentile-based thresholds (η₁=30th, η₂=75th) to reject both outliers and redundant samples — a design informed by prior work (Fu et al., 2021). Table 4 ablations show that removing Q_novel produces the largest drop (0.842→0.812), and each of the four components contributes positively.

- **Consistent reported improvements over baselines on two medical imaging tasks.** The proposed method achieves higher AUC than AADA, CLUE, BADGE, and other baselines on CAMELYON17 (Table 2) and the NIH→CheXpert transfer (Table 4). The ablation studies (removing one loss or one informativeness term at a time) consistently produce degradation, supporting that the full pipeline contributes to performance.

## Weaknesses

### Fatal
None.

### Major

- **Only one of 14 disease labels is reported for the chest X-ray experiments, raising cherry-picking concerns.** Table 4 explicitly states "We focus on Infiltration condition" for the NIH→CheXpert transfer. Since both NIH ChestXray14 and CheXpert contain 14 disease labels, reporting results for a single label is insufficient to demonstrate general effectiveness. Without average AUC across all conditions or results for the other 13 labels, the reader cannot assess whether the method works broadly or only on this specific finding. This is a significant evidential gap.

- **Missing critical ablation: the contribution of feature disentanglement itself is not isolated.** The ablations remove individual loss terms (L₁, L₂, L₃, L_base) and individual informativeness components (Q_unc, Q_dom, Q_density, Q_novel), but there is no baseline that applies the *same four scores* to standard image features (e.g., the penultimate layer of a DenseNet-121 without disentanglement). Since L_base already aligns z_task with pre-trained DenseNet features, the natural question is: why not just use those DenseNet features directly for active selection? Without a "no disentanglement" baseline, the paper cannot support its central claim that the disentanglement architecture adds value for informative sample selection under domain shift.

- **No error bars, confidence intervals, or multiple-run statistics are reported.** All results are single-point AUC values. Several ablation differences are small (e.g., reported drops of ~0.01–0.02 AUC). Without variance estimates, it is impossible to know whether the observed differences are statistically significant or within the noise of a single run. Given the standard practice in medical imaging benchmarks, reporting at least mean±std over multiple random seeds is expected.

- **Unclear whether the experimental evaluation compares methods in the correct setting.** The paper defines ASDA (supervised, with labeling) and AUDA (unsupervised, without labeling) as distinct settings (Section 3). The ablation studies use the "AUDA" label (e.g., "AUDA_w/o_L₁"). However, the baseline methods (AADA, CLUE, BADGE) are designed for the *supervised* active DA setting where selected target samples are labeled. If the experiments compare these baselines in the unsupervised AUDA setting (where no labels are obtained for selected samples), the baselines are placed at an unfair disadvantage because their core selection mechanisms assume labeling. The paper does not explicitly state which setting (ASDA vs. AUDA) the main comparisons in Tables 2 and 4 use, nor does it describe how the baselines were adapted to the alternative setting. This ambiguity undermines the validity of the comparisons.

### Minor

- **No learning curves or performance as a function of budget.** Section 4.1 states "As we add samples to the training set we report the test accuracy for every 10% increase of the training set," but the tables report only single final AUC values. The budget B (number of selected samples) and stopping criterion ("no further change in validation performance") are not quantified. Active learning evaluation fundamentally requires showing *rate* of improvement vs. number of selected/labeled samples.

- **The density score description uses contradictory terminology.** Eq. 9 defines Q_density = (1/K)·Σ⟨z_taskⁱ, z_taskᵏ⟩ as average cosine similarity. The text then says "A higher average feature distance indicates that the sample is more similar to other samples." Cosine similarity and feature distance are inversely related, so "higher feature distance" implying "more similar" is incorrect. The equation is correct; the prose should say "higher average cosine similarity." This is confusing but does not affect the math.

- **Hyperparameters are tuned per dataset without sensitivity analysis.** The procedure in Section 4.4 involves tuning 8 λ parameters and 2 η parameters sequentially on a held-out validation set for each dataset. While the stepwise tuning is described, no sensitivity analysis is provided (e.g., how performance varies as each λ is perturbed). Given the large number of hyperparameters, overfitting to the specific datasets is plausible.

### Trivial
- The hyperparameter reporting in the CheXpert section (line 171) contains garbled repeated text due to PDF extraction artifacts (e.g., "0.9,\lambda_{D e n s i t y}=0.9,\lambda_{D e n s i t y}=0.9" repeated). This should be cleaned up.

## Nice-to-Haves
- Qualitative analysis (t-SNE of z_task features, examples of high- vs. low-scoring samples) would strengthen the claim that the informativeness criteria select meaningful samples under domain shift.
- Discussion of the computational cost of the FDN (two autoencoders + base classifier) and the O(N²) cost of the novelty criterion per round would be helpful for practitioners.

## Removed Points

These points were raised by reviewers but are removed (with justification):

1. **"Conceptual conflation between active learning and sample selection for UDA"** — The paper clearly distinguishes ASDA (supervised, with labeling) from AUDA (unsupervised, without labeling) in Section 3, line 42. The problem formulation in Section 1 explicitly includes "the ability to obtain labels for a fixed budget of target instances." There is no conflation; the paper simply addresses both settings within a unified framework. *However*, the related concern about whether the *evaluation* correctly aligns baselines with the appropriate setting is retained as a Major weakness above (point 4).

2. **"Sign error in density score"** — Eq. 9 correctly uses cosine similarity (higher = more similar = denser). The text's use of "feature distance" is a terminology error, not a math error. Retained as a Minor terminology issue above.

3. **"State-of-the-art performance claim unsupported"** — Generic claim; the reported numbers do show improvements over baselines. The concern about evaluation validity is captured under the Major weaknesses above.

4. **"No discussion of robustness to different amounts of target data"** — Nice-to-have but not a core weakness.

5. **"Missing related works"** — Removed per instructions (cannot verify external sources).

6. **"Formatting/presentation nitpicks"** — Removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already present.

## Suggestions

1. **Report all 14 disease conditions** (or a reasoned subset with justification) for the NIH→CheXpert experiments, or provide average AUC over all labels.
2. **Add a "no disentanglement" baseline:** apply the same four informativeness scores to penultimate-layer features from a pre-trained DenseNet (without the FDN) for active selection.
3. **Specify the experimental setting clearly** for each comparison table: are the results in the ASDA setting (samples labeled) or AUDA setting (samples unlabeled)? Explain how baselines were adapted if the setting differs from their original design.
4. **Report learning curves** (AUC vs. number of selected/labeled target samples or vs. budget B), at least for one representative task, with error bars over multiple runs.
5. **Improve the density score prose** to say "cosine similarity" instead of "feature distance" to avoid confusion.
