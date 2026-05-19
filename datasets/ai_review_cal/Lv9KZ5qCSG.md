- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces EyeFairness-30k, a dataset of 30,000 subjects with paired 2D SLO fundus images and 3D OCT scans, six demographic attributes (age, gender, race, ethnicity, preferred language, marital status), and diagnostic labels for three major eye diseases (AMD, DR, glaucoma). It also proposes a Fair Identity Scaling (FIS) method that combines group-level learnable weights with per-sample loss history to reweight training batches, and a Performance-Scaled Disparity (PSD) metric that normalizes group-AUC disparity by overall AUC.

## Strengths

- **First large-scale 3D medical fairness dataset.** The paper's comparison (Table 1) shows prior 3D medical fairness datasets max out at 550 subjects (COVID-CT-MD, ADNI 1.5T, AMD-OCT). EyeFairness-30k's 30,000 subjects with both 2D and 3D imaging fills a genuine gap: no public 3D medical fairness dataset of this scale existed before.

- **FIS consistently improves minority-group AUC.** In the race experiments (Table 2, 2D fundus), FIS raises AUC for Black subjects from 68.55→73.22 (AMD), 71.88→74.15 (DR), and 72.57→75.61 (glaucoma), while also improving overall AUC. Similar gains appear for Hispanic subjects (Table 6) and across both imaging modalities.

- **Ablation study validates the group+individual scaling rationale.** Figure 2 systematically varies the fusion weight \(c\) across three diseases, showing that the combination (\(c=0.5\)) outperforms either pure individual (\(c=0\)) or pure group (\(c=1\)) scaling on both overall AUC and Mean PSD, supporting the paper's design motivation.

- **PSD reveals accuracy-fairness interactions that traditional metrics miss.** The paper honestly reports cases where FIS improves AUC but worsens PSD (e.g., ethnicity results in Table 6: best AUC, worst PSD). These inconsistencies are explicitly discussed as evidence that multiple fairness metrics are needed, not swept under the rug.

- **Extensive evaluation coverage.** Experiments span three identity attributes (race, gender, ethnicity), two imaging modalities (2D fundus, 3D OCT), and three diseases, totaling 18 disease-modality-attribute combinations compared against two SOTA baselines.

## Weaknesses

### Fatal

None. The dataset contribution is real and the core claims are not invalidated by any single fundamental flaw.

### Major

- **Insufficient dataset documentation for responsible use as a fairness resource.** The paper does not describe the data collection pipeline, inclusion/exclusion criteria, label verification process (beyond stating ICD code / VF test origin), or annotation quality control. For a dataset intended to support fairness research—where label noise and selection bias can interact with demographic attributes—this is a significant gap. The demographic skew (78.6% White, 3.8% Hispanic, 1.8% Spanish-speaking, 91.6% English-speaking) is reported but its implications for statistical power and which fairness questions the dataset can/cannot support are not discussed. There is no limitations section and no discussion of ethical considerations beyond a one-sentence IRB / de-identification statement. A datasheet or comparable structured documentation is essential for a dataset being released to the community.

- **Insufficient baselines for the FIS method.** The method is compared against only two baselines (adversarial training [Beutel et al. 2017] and fair contrastive loss [Wang et al. 2022]). Group DRO (Sagawa et al. 2019)—a closely related adaptive reweighting method that the paper *cites* in its related work—is not used as a baseline. Standard simple approaches (inverse-group-frequency reweighting, resampling, fairness constraints) are also absent. The claim that FIS shows "superior performance compared with various SOTA models" is unsubstantiated when the comparison set is this narrow. This is compounded for 3D experiments, where FSCL is inapplicable, leaving only a single baseline (Adv) for 3D OCT comparisons.

- **Incomplete specification of the FIS method.** The loss equation uses a learnable group-weight parameter \(\beta_{a}\) but provides no update rule or training procedure for \(\beta\). The text calls it a "learnable weighting parameter," which implies gradient-based learning, but this is never stated explicitly. The paper does not explain why the individual loss from the *previous* batch (\(\ell_i^{t-1}\)) is used rather than the current batch's loss, nor does it discuss how the batch-size scaling factor \(|\mathcal{B}^t|\) in the numerator interacts with the leading \(1/|\mathcal{B}^t|\) term. The temperature \(\tau\) (set to 1 with no analysis) and the choice of \(c=0.5\) (shown in ablation but without a practical guideline for choosing it on new datasets) lack sufficient discussion.

- **No discussion of limitations or ethical considerations.** For a fairness dataset released to the community, the absence of a limitations section (single-institution data, label noise from ICD codes, generalizability to other populations, incompleteness of available demographic attributes) and the absence of ethical discussion (how patient consent was handled, re-identification risks given the rich demographic attributes, guidelines for responsible use) are significant omissions that could hinder responsible adoption.

### Minor

- **The PSD metric is heavily overclaimed as a contribution.** PSD is simply \(\text{std}(\text{group AUCs}) / \text{overall AUC}\) (or \(\max|\text{diff}| / \text{overall AUC}\)). This is a straightforward normalization of an existing disparity measure by overall performance. The paper frames it as a "new metric" and a core contribution (contribution 3 in the introduction), which inflates its novelty. It is a useful reporting convention but not a technical contribution of the same weight as the dataset.

- **Statistical rigor is limited.** Results are reported over only three random-seed runs with no confidence intervals or significance tests. For fairness evaluations with small subgroups (e.g., 3.8% Hispanic, 1.8% Spanish-speaking), variance in per-group AUC estimates can be high, making it difficult to assess whether reported improvements (often 1–2% AUC) are real or noise.

- **3D baselines are weaker than 2D baselines.** The paper appropriately excludes FSCL from 3D experiments (since effective 3D augmentation strategies are not established), but this leaves only a single baseline (Adv) for 3D OCT comparisons across all three attributes and three diseases, making the 3D conclusions less robust.

### Trivial

- Line 68 contains a typo: "where \(c=1\) means group scaling alone, and \(c=1\) indicates individual scaling alone" — the second instance should be \(c=0\).
- Per-group sample counts are not explicitly stated (percentages alone are given; counts for 30k subjects are calculable but should be reported directly).

## Nice-to-Haves

- A structured datasheet or expanded documentation covering the data extraction pipeline, inclusion/exclusion criteria, label verification, and known biases.
- Intersectional group analysis (e.g., Black women, Hispanic men) and an assessment of which intersections have sufficient sample sizes for meaningful fairness evaluation.
- Benchmarking against a wider set of standard fairness approaches (Group DRO, reweighting, resampling, fairness constraints) to demonstrate the dataset's value as a testbed.
- Validation against external cohorts or known population statistics to assess the dataset's representativeness.
- The FIS method's sensitivity to \(c\) and \(\tau\) should be discussed with practical guidance for other practitioners.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- The critic claimed the paper "does not cite Group DRO (Sagawa et al., 2019)." **Factually incorrect.** Group DRO is cited on line 31 of the related work section under "fair batch training." The criticism about *not comparing* against it is retained as a Major weakness.
- The critic's assertion that the dataset and code "cannot be verified" because the link is anonymous during double-blind review. Per instructions: REMOVE any criticism questioning the existence or release status of cited resources.
- The critic claimed the paper "dismisses" inconsistent PSD results. **Factually incorrect.** The paper explicitly discusses cases where AUC improves but PSD degrades (e.g., ethnicity results, glaucoma OCT) and frames them as evidence that multiple metrics are needed (lines 101, 113). The paper does not dismiss these results.
- The critic's statement that "no published studies have been performed to assess and address the fairness issue in eye disease screening" (from the introduction) is a claim made *by the paper itself* about prior work, not a weakness. Not a reviewer finding.
- Concerns about "dated" backbone choices (EfficientNet-B1 is from 2019 but remains widely used). Demoted to a subjective opinion; removed.
- Concerns that small batch sizes "could exacerbate instability." Speculative without evidence; removed.
- Criticisms about missing random seed specifications. Per instructions: remove nitpicks about reproducibility details.
- The claim that "backbone choices are dated" and "no motivation" — EfficientNet-B1 is a standard medical imaging backbone and the paper states it is "widely considered as one of the best backbone models for medical imaging tasks." This is adequate motivation.

## Novel Insights

The reviews surface a tension that the paper never fully resolves: the dataset is a genuine and needed contribution, but the paper tries to package three contributions (dataset + method + metric) and does none of them at the depth expected for a resource that the community will build on. The FIS method's approach of combining group-level \(\beta\) with per-sample loss history is a reasonable design intuition, but the thin evaluation (only two baselines, one for 3D) means it reads as a proof-of-concept demo rather than a validated method. The PSD metric is correctly identified by both harsh and strength reviewers as a double-edged sword: it surfaces accuracy-fairness trade-offs that raw DPD/DEOdds miss, yet it is a trivial normalization presented as a novel contribution. The honest reporting of contradictory PSD results (where AUC improves but PSD worsens) is a strength in transparency but also undermines the claim that FIS is consistently beneficial.

## Suggestions

1. **Reframe the paper around the dataset as the primary contribution.** Demote FIS to a preliminary application demonstrating dataset utility. Present PSD as a simple reporting convention, not a novel metric. This would make the paper's actual strength (the dataset) the centerpiece and reduce the vulnerability of overclaimed secondary contributions.
2. **Add a comprehensive datasheet** covering data collection, inclusion/exclusion criteria, label verification, per-group counts, demographic skew implications, and known biases. Add a limitations section and an ethical considerations paragraph (consent, re-identification risk, responsible use guidelines).
3. **Expand the experimental validation** to include several standard fairness methods (Group DRO, inverse-probability weighting, resampling) on the dataset, demonstrating the dataset's value as a fairness benchmark rather than only showcasing FIS.
4. **Report confidence intervals or bootstrap estimates** for AUC and PSD across more runs to establish statistical significance.
5. **Clarify the FIS method**: specify how \(\beta\) is learned (explicit gradient update or something else), explain the role of the \(|\mathcal{B}^t|\) scaling factor, and add a brief discussion of why \(\ell_i^{t-1}\) is used instead of \(\ell_i^t\).
