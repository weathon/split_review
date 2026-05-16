Now I have verified all claims against the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a new problem setting called Realistic Open-world Long-tailed Semi-supervised Learning (ROLSSL), which drops the assumption of consistent distributions between known and novel classes and assumes labeled known-class data is far scarcer than unlabeled data. To address this setting, the authors propose Dual-stage Post-hoc Logit Adjustment (DPLA), which adaptively scales logits based on sample frequency, class count, and dataset size in the first stage, and dynamically reweights unlabeled data contributions in the second stage. Experiments across six datasets show substantial accuracy gains over the OpenLDN baseline.

## Strengths

1. **Defines a more realistic problem setting (ROLSSL)** that removes the unrealistic assumption of identical distributions between known and novel classes and accounts for scarce labeled data. This is clearly formalized in the problem formulation (Section 3.1) and contrasted with prior settings in Table 1.

2. **Achieves substantial and consistent performance gains over the OpenLDN baseline** across all six datasets and three distribution types. For example, on CIFAR‑10 with Uniform distribution, overall accuracy increases from 24.2% to 50.5% (Table 1); on SVHN with Consistent distribution, novel-class accuracy jumps from 0.5% to 35.4% (Table 2). The improvements are large enough to be practically meaningful.

3. **Validates each component of DPLA through ablation studies.** The ablation table on SVHN (Section 4.4) shows that adding the first-stage adjustment, second-stage adjustment, and pseudo-label refinement each progressively improves performance, confirming that all components contribute.

4. **Evaluates across a broad range of datasets** (CIFAR‑10, CIFAR‑100, ImageNet‑100, Tiny ImageNet, Oxford‑IIIT Pet, SVHN) with three distribution mismatches (Consistent, Reversed, Uniform), demonstrating generality.

5. **Identifies and diagnoses a failure mode** of existing methods under ROLSSL — the degradation of novel-class recognition during training (Section 4.3) — and provides a textual description of how DPLA avoids this collapse.

## Weaknesses

### Major

- **Only one baseline in the ROLSSL setting.** The paper compares DPLA exclusively against OpenLDN under all long-tailed open-world conditions. The related work (Section 2) explicitly cites BACON (Bai et al., 2024) and NCDLR (Chuyu et al., 2023) as methods designed for open-world long-tail SSL (OLSSL), yet neither is evaluated. The paper's motivation criticizes existing OLSSL methods for assuming consistent distributions — but never shows that those methods actually fail under ROLSSL. Without head-to-head comparisons against at least adapted versions of BACON, NCDLR, or long-tailed SSL methods (e.g., DASO, ACR) ported to the open-world scenario, the reader cannot assess whether DPLA genuinely advances the state-of-the-art or whether the reported gains are an artifact of using a single, non-long-tail baseline. This gap undermines the main claim of the paper.

### Minor

- **Missing values for several key hyperparameters.** The first-stage scaling factor (Eq. 3) depends on $\mathcal{C}_{base}$ and $\mathcal{S}_{base}$, which are never given concrete values or a rule for determination. The ablation (Section 4.4) only varies a multiplicative scalar, not these base parameters. The second-stage weight (Eq. 5) uses $\alpha$ and $\beta$ with no stated values or sensitivity analysis. The pseudo-label adjustment temperature $\tau_2$ (Eq. 6) is also unspecified. These are core parameters of the proposed method, not appendix-level implementation details.

- **No variance estimates.** All tables report single accuracy values with no standard deviations or confidence intervals. Given the well-known sensitivity of SSL and open-world learning to random seeds and initialization (the paper itself notes that OpenLDN sometimes succeeds due to "favorable initialization"), the significance of observed improvements — especially modest ones on Tiny ImageNet and Oxford-IIIT Pet (often 1–4%) — cannot be evaluated without multiple runs.

- **Concrete imbalance ratios not reported.** The paper defines $\gamma$ for labeled known classes and novel classes (Section 3.1) but never states the actual numerical imbalance ratios used in experiments (e.g., $\gamma$ = 100 or 10), making it impossible to reproduce the exact data splits.

- **MixMatch integration underspecified.** The paper mentions incorporating MixMatch during the second stage (Section 4.1) but does not explain how it interacts with the logit adjustment losses — whether its pseudo-labels are also adjusted, at what stage it is applied, or how mixup and sharpening interact with the balanced cross-entropy loss. The sentence "More details on these implementation strategies and parameter settings, e.g." is cut off, suggesting details may exist in a parser-stripped appendix, but the main text should be self-contained on this point.

- **Scaling factor formula lacks individual justification.** The form $10 \cdot (\lceil\mathcal{C} / \mathcal{C}_{base}\rceil) \cdot \sqrt{\mathcal{S} / \mathcal{S}_{base}} \cdot \mathcal{F}$ is introduced with a reference to "detailed in Ablation," but the ablation only studies a combined scalar multiplier, not the individual contribution of each term (ceil ratio, square root of size ratio). The rationale for these specific functional forms is never explained.

- **Learning curves not shown.** The discussion in Section 4.3 describes how OpenLDN's novel-class accuracy collapses during training while DPLA avoids this, but no accuracy-vs-epoch plots are provided. Curves would strongly support this claim.

### Trivial

- **Minor phrasing inconsistency in Table 1 caption.** The S/N Consistency column marks OLSSL as "Yes" (consistent distributions), but the introduction text (line 15) says "Existing OLSSL methods follow a setting where the number of known classes is consistent with that of unknown classes in labeled data" — this conflates two different uses of "consistent" (distribution shape vs. count). Minor clarification needed.

- **The dataset description says "To evaluate the effectiveness of OpenLDN"** rather than "to evaluate DPLA" (line 130), an apparent copy-paste oversight.

## Nice-to-Haves

- **No limitations section.** The paper does not discuss limitations of ROLSSL (e.g., the three distribution types are still parametric; real-world novel-class distributions could be arbitrary) or of DPLA (e.g., dependence on knowing $c_t = c_k + c_n$, which is artificial since $c_n$ is unknown in open-world settings). A limitations discussion would strengthen the paper.

- **Figures 3–4 scaling-factor ablation** would benefit from numerical accuracy values in a companion table, since the PDF-rendered axis labels may be hard to read.

## Removed Points

These points are flagged to be removed; treat them with caution.

- ***"Asterisk in OpenLDN rows unexplained":** Removed — there is no asterisk notation in the tables; the critic likely misread LaTeX table formatting.

- ***"OpenLDN listed with — in top section but appears in long-tail sections for ImageNet-100":** Removed — this is standard notation indicating that OpenLDN was not evaluated on balanced ImageNet-100 but was evaluated on the long-tailed variant. Not a weakness.

- ***"Missing asterisk/text formatting":** Removed — these are parser artifacts, not author errors.

- ***"50.1% claim in abstract is misleading":** Removed — the claim is factually correct as an absolute improvement (CIFAR-10 Uniform novel accuracy: 3.8% → 53.9%, an absolute gain of 50.1 percentage points). Reporting absolute improvements is standard.

- ***"Pairwise similarity loss and entropy regularization not defined":** Removed — the paper cites prior work for these components, which is standard practice.

- ***"Missing appendix content" / "More details…e.g."**: Removed per the rule that parser-stripped appendix content may have existed in the original submission.

- ***Generic/filtered strength from Strength Finder**: Removed a generic strength that added no concrete content beyond what is covered by other strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new interpretation or connection that the paper itself does not already present.

## Suggestions

1. **Add at least 2–3 more baselines under the ROLSSL setting.** The most critical addition would be adapted versions of BACON and NCDLR (the OLSSL methods discussed in the paper). If these are not publicly available, adapt long-tailed SSL methods (DASO, ACR) to the open-world framework. Without this, the paper cannot substantiate its claim that existing OLSSL methods fail under ROLSSL.

2. **Report all core hyperparameters** ($\mathcal{C}_{base}$, $\mathcal{S}_{base}$, $\alpha$, $\beta$, $\tau_2$) with how they were selected (e.g., fixed across datasets or tuned per dataset). Report the imbalance ratio $\gamma$ used in each experiment.

3. **Run experiments with 3–5 random seeds** and report mean ± std. This is particularly important given the paper's own observation that OpenLDN's success depends on "favorable initialization" (Section 4.3).

4. **Add learning curves** (accuracy vs. epoch) for the discussion in Section 4.3 to visually demonstrate the novel-class accuracy collapse that OpenLDN suffers and DPLA avoids.

5. **Clarify the MixMatch integration** — how it interacts with the logit adjustment losses, whether its pseudo-labels are also adjusted, and the exact training schedule.

## Score and Decision

The paper identifies a genuinely important and realistic problem setting and proposes a method with clear empirical gains over a single baseline. However, the central weakness — comparing against only one baseline (OpenLDN) when the paper's own motivation critiques existing OLSSL methods (BACON, NCDLR) — prevents the evaluation from establishing DPLA as a validated advance rather than a promising technique that beats a weak baseline. The missing hyperparameter values and lack of variance estimates further reduce confidence. These are fixable with additional experiments and disclosure, but in the current form the contribution is not convincingly supported.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>