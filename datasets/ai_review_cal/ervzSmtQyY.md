- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the evidence needed to construct a careful, verified review.

## Summary

2-3 sentence summary of the paper's contribution.

The paper introduces Fair MEDL, a framework that combines mixed-effects deep learning (MEDL) with adversarial debiasing to simultaneously handle clustered (non-i.i.d.) data and improve fairness across sensitive attributes. The method is evaluated on three datasets (Adult, IPUMS, Heritage Health) spanning classification and regression, using equalized odds, demographic parity, and counterfactual fairness. The results show substantial fairness improvements (e.g., 86.4% reduction in TPR SD for Age on IPUMS) while maintaining predictive performance, with additional evidence of confound mitigation via probe experiments.

## Strengths

- **Large, statistically significant fairness improvements on IPUMS (classification).** On seen occupations, the Fair(ADB) MEDL-NNet reduces TPR SD for *Age* from 0.162 to 0.022 (86.4%, p<0.001), for *Race* from 0.122 to 0.051 (58.2%, p<0.001), and for *Sex* from 0.134 to 0.061 (54.5%, p<0.001) (Table 2, lines 497-505). These are large effect sizes with rigorous statistical testing (120 resamples per model), providing direct evidence that the framework delivers on its core fairness claim.

- **Extension to regression with adapted fairness metrics.** The paper formally adapts equalized odds, demographic parity, and counterfactual fairness for regression (Section 3.2, lines 78-144) and validates on Heritage Health. Counterfactual fairness for *Sex* improves by 56.5% (0.092 → 0.040) under Fair MEDL ME (p<0.001, line 659). This goes beyond prior works focused on classification.

- **Demonstrated OOD generalization of fairness.** On IPUMS unseen occupations, Fair(ADB) MEDL-NNet FE reduces TPR SD for *Age* from 0.272 to 0.101 (62.9%, p<0.001) and for *Sex* from 0.177 to 0.101 (42.9%, p<0.001) (Table 2, lines 509-528). This shows the framework maintains fairness on out-of-distribution clusters, a setting rarely validated.

- **Systematic ablation and baseline comparisons.** The paper compares adversarial debiasing (ADB) vs. absolute correlation loss (ACL), finding ADB yields more consistent fairness with smaller accuracy reduction (1% vs 1.6%, line 409, Table S7). It also compares Fair(ADB) MEDL-NNet against Fair(ADB) DA-NNet (without random effects), confirming the full framework's advantages (Discussion, line 673).

- **Minimal accuracy-fairness trade-off.** On Adult, AUROC drops only from 0.890 to 0.882 and accuracy from 0.813 to 0.805 (Table 1). On IPUMS, balanced accuracy shows only minor fluctuations (Table S13). This evidence supports the claim that substantial fairness gains come with minimal predictive cost.

## Weaknesses

### Fatal

None.

### Major

- **Abstract reports aggregate percentages without dataset/metric context.** The abstract states: "improves fairness by 86.4% for *Age*, 64.9% for *Race*, 57.8% for *Sex*, and 36.2% for *Marital status*" (line 4) without specifying that these come from different metrics and settings (IPUMS TPR SD for Age, IPUMS CF for Sex, IPUMS TPR SD for Marital-status). The 64.9% for Race is not straightforwardly traceable: the closest verifiable number in the main body is 58.2% (IPUMS TPR SD for Race, line 553), while 64.9% only appears in the Discussion with range qualifiers (line 677). A reader of the abstract alone could reasonably infer uniform improvement across all settings, which is misleading — e.g., Race counterfactual fairness on Adult stays flat at 0.024→0.025 (line 346), and Age CF on IPUMS actually worsens slightly (0.040→0.047, Table 3). The abstract numbers should be accompanied by their dataset, metric, and model variant.

### Minor

- **Probe experiments compare against conventional NNet rather than MEDL without fairness.** The probe experiments (Figures 4, 6, HH probe figure) show that Fair(ADB) MEDL-NNet de-weights confounding probes while a "conventional NNet" does not. The paper frames this as the framework's ability to "mitigate Type I and II errors." However, MEDL models (without fairness) already have this confound-mitigation capability (as noted in the paper's own motivation). Comparing against a conventional NNet conflates the MEDL architecture's contribution with the fairness component's contribution. A comparison against MEDL-NNet (without fairness) would isolate whether adding fairness preserves or degrades MEDL's inherent confound-mitigation ability. This weakens the specific claim about fairness preserving MEDL's interpretability benefits (line 680).

- **IPUMS counterfactual fairness for Age worsens without discussion.** The paper notes that "we observe a slight decrease in fairness for *Age*" in IPUMS counterfactual fairness (line 600: MEDL-NNet ME CF 0.040 → Fair(ADB) MEDL-NNet ME CF 0.047). This is mentioned but not analyzed. Since this is one of the three primary fairness metrics and the result moves in the opposite direction from the claimed improvement, a brief discussion of why the adversarial debiasing procedure may not improve this metric for Age (e.g., structural confounding, multi-valued sensitive attribute difficulty) would strengthen the paper's analysis.

- **Adversarial training dynamics not described.** The loss functions for the fairness adversaries A_F and A_M are provided (Equations 2-4), but the paper does not specify whether the adversary and main network are trained simultaneously or via alternating gradient updates, whether a gradient reversal layer is used, or how the fairness hyperparameters λ_FE and λ_ME are tuned relative to the main loss. This information is needed for reproducibility, even if the implementation follows standard practices from Yang et al. (2023).

- **Missing plain NN + fairness baseline for isolating MEDL's contribution.** The main comparisons are MEDL-NNet (no fairness), Fair(ADB) DA-NNet (ablation without random effects but with cluster adversary), and Fair(ADB) MEDL-NNet (full model). A standard feedforward network with the same adversarial debiasing subnetworks (no cluster adversary, no random effects, no MEDL loss terms) is not included. Such a baseline would directly quantify the marginal benefit of the MEDL structure for fairness — the paper's central claim. The existing ablation (DA-NNet) still includes the MEDL cluster adversary, so it does not fully isolate the contribution of MEDL over a plain NN.

### Trivial

- **Typo in numerical result.** Line 553 states TPR SD for *Sex* drops "to 0.0061" in Fair(ADB) MEDL-NNet, but Table 2 (line 505) shows 0.061. The 54.5% improvement is correctly computed from 0.061, so the "0.0061" is a transcription error (an extra zero). This should be corrected.

## Nice-to-Haves

- **Add a plain NN + adversarial debiasing baseline** (no cluster adversary, no random effects). This would quantify the marginal fairness benefit of the MEDL architecture over a standard fairness-only approach.
- **For probe experiments, add MEDL-NNet (without fairness) as a comparison.** This would isolate whether fairness enhancement degrades or preserves MEDL's confound-mitigation capability.
- **Quantify probe experiment results statistically.** The feature importance comparison is qualitative (bar charts). A quantitative measure (e.g., rank of probes over multiple runs, permutation feature importance with confidence intervals) would strengthen the claim.
- **Provide a summary table mapping abstract percentages** to specific dataset × metric × model settings for transparency.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Counterfactual fairness computation is underspecified and potentially invalid"** (Harsh Critic #1): The paper explicitly states the procedure: "changing a sensitive attribute to a counterfactual value, while keeping all other covariates the same" (line 115), and "(s', x) is a sample in a counterfactual world where sample x is assigned an alternative s'" (line 124). The critic's claim that "the paper does not describe how these counterfactuals are generated" is factually incorrect given these lines. The *limitations* of this approach (plausibility of counterfactual samples) are a valid discussion point, but the claim of underspecification is wrong. *Removed because the criticism is factually incorrect about what the paper describes.*

- **"Heritage Health results are modest, contradicting abstract framing"** (Harsh Critic, Section-by-Section): The critic argues the abstract implies larger gains than Heritage Health shows. However, the abstract's 86.4% is explicitly from IPUMS (as verified in the body, line 553), not Heritage Health. Improvements on Heritage Health range from ~7% (Age MSE SD) to 56.5% (Sex CF), which the paper presents honestly. *Removed because it misattributes claims the paper never made about Heritage Health.*

- **"Comparison to Yang et al. is qualitative"**: The comparison in the Discussion (line 677) is appropriately qualitative for a Discussion section. *Removed because it demands a standard of comparison not required for this section.*

- **"Tables are hard to follow" / "would benefit from summary tables"**: This is a formatting/style suggestion. *Removed per formatting/style nitpick rule.*

- **"GitHub link should be in main paper"**: The paper states "Our implementation is publicly available on GitHub" (line 4). The link may be in the appendix. *Removed per rule about missing appendix content.*

- **"Statistical significance for probe experiment"**: The probe experiments are qualitative validation of confound mitigation, which is a secondary contribution. *Moved to Nice-to-Haves.*

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors themselves do not articulate.

## Suggestions

1. **Revise the abstract** by adding context for each percentage improvement (e.g., "On IPUMS classification, TPR SD for Age improved by 86.4%...") or replace specific numbers with representative ranges. Ensure every number in the abstract is directly traceable to a table/line in the main paper.

2. **Add a plain NN + fairness baseline** (standard feedforward network with adversarial debiasing, no MEDL components) to Tables 2 and 3. This would directly measure the marginal benefit of the MEDL structure for fairness.

3. **For probe experiments, include MEDL-NNet (without fairness)** as a baseline alongside the conventional NNet. If the probe experiments are meant to show that fairness preservation doesn't degrade MEDL's confound mitigation, this comparison is essential.

4. **Describe the adversarial training procedure** (simultaneous vs. alternating updates, use of gradient reversal layers) in Section 3.4-3.5.

5. **Briefly discuss why IPUMS counterfactual fairness for Age worsens** (line 600). Even a short paragraph noting possible reasons (e.g., multi-valued Age brackets, structural confounding) would strengthen the analysis.

6. **Correct the typo** on line 553: "0.0061" should be "0.061".
