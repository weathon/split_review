Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper presents the first systematic study of how curriculum learning (CL) affects privacy risks in machine learning models. Through extensive experiments on 9 datasets with multiple CL methods (bootstrapping, transfer learning, baseline, anti-curriculum), it evaluates membership inference attack (MIA) and attribute inference attack (AIA) effectiveness. The key findings are: (1) CL slightly increases MIA vulnerability (0.01%–2.46%), with a much larger effect on difficult samples (gap up to 4.23%); (2) CL does not increase AIA vulnerability; (3) existing defenses remain effective under CL, albeit with accuracy trade-offs. The paper also proposes a difficulty-calibrated MIA (Diff-Cali) that improves TPR at low FPR.

## Strengths

- **First systematic quantification of CL's privacy impact.** The paper evaluates 9 real-world datasets (6 image, 3 tabular), 4 CL variants, and multiple attack families (NN-based, metric-based, label-only MIA; NN-based AIA). Tables 1 and 2 provide comprehensive evidence that CL modestly increases MIA vulnerability, and the evaluation spans multiple architectures (ResNet-18/34, MobileNet) to confirm the pattern generalizes.

- **Identification of disparate privacy impact on difficult samples.** This is the paper's most novel and actionable finding. The paper demonstrates that CL increases MIA accuracy much more for high-difficulty samples than easy ones, with gaps up to 4.23% on CIFAR100. Figure 2 shows attack accuracy by difficulty bucket; Figure 3 shows confidence scores narrowing for difficult members under bootstrapping/transfer learning. The memorization analysis (Figure 5) provides a principled explanation: CL forces stronger memorization of difficult samples via data ordering, not data value (corroborated by KNN-Shapley analysis in Figures 6–7).

- **Memorization and data-valuation analysis provide causal evidence.** The memorization experiment (Figure 5) isolates that data ordering—not just repetition—causes CL to memorize difficult samples more strongly. The KNN-Shapley analysis (Figures 6–7) differentiates the effect from data value, confirming that difficulty, not value, drives the increased vulnerability. This elevates the paper beyond a purely observational study.

- **Evidence that CL does not increase AIA vulnerability.** Table 5 shows normal training yields higher or comparable AIA accuracy to all CL methods across three datasets (Place100, Place60, UTKFace). This finding isolates CL's privacy impact to membership inference, not attribute inference, and is explained by the fact that difficulty scores are computed from the original task labels, not sensitive attributes.

- **Comprehensive attack methodology coverage.** The paper evaluates 7 attack variants including NN-based (black-box-top3), 4 metric-based attacks, label-only attacks, the existing Cali calibration method, and the proposed Diff-Cali attack, providing a thorough picture of how different attack strategies interact with CL.

## Weaknesses

### Fatal
None.

### Major

- **The proposed attack's advantage over existing calibration is not fully demonstrated on the key metric.** The paper builds on Watson et al.'s calibration-based MIA (referred to as "Cali") but does not compare Diff-Cali against Cali on TPR at low FPR—the very metric where Diff-Cali claims its main advantage. Table 3 shows Diff-Cali has higher overall accuracy than Cali (e.g., 0.8519 vs 0.7889 on normal training), but the TPR@lowFPR plots in Figure 6 only compare Diff-Cali against the standard NN-based attack, not against Cali. This makes it difficult to assess whether the improvement comes from using difficulty scores specifically, or simply from having a better calibration procedure than the existing Cali implementation. A direct TPR@lowFPR comparison between Diff-Cali and Cali would resolve this.

- **Defense evaluation is limited to one dataset and one architecture.** The defense experiments (Table 4) use only CIFAR100 with ResNet-18. While this is acknowledged as a limitation, the claim that "DP-SGD can reverse the impact of CL on MIA" (Finding 6) and the broader finding that "none of the studied defenses can significantly drop MIA accuracy while maintaining target model accuracy" would be substantially stronger if validated on at least one additional dataset or model architecture. Different datasets (e.g., with more or fewer classes) and model sizes may interact differently with DP-SGD under CL.

### Minor

- **Practical significance of the small overall MIA increase is unclear.** The paper honestly describes the effect as "slightly more vulnerable" and reports increases of 0.01%–2.46%. However, given that baseline MIA accuracy is already very high (often >90%), a 1–2% increase means the attacker already identifies most members; the additional gain is marginal. The paper's key and well-supported contribution is the *disparate impact on difficult samples*, not the small aggregate increase. The framing could better emphasize this differential effect as the primary finding rather than the aggregate increase.

- **The attack requires knowledge of difficulty scores, an additional assumption.** The proposed Diff-Cali attack assumes the adversary has access to the difficulty scores used by the target model's CL method. While this is feasible if the adversary can replicate the difficulty measurer (e.g., by training a shadow model), it is an extra informational assumption that the standard NN-based attack does not need. The paper acknowledges this implicitly but does not discuss the practical scenarios where such scores would be available to an adversary.

- **Some standard deviations reported as 0.0000.** In Table 3, several metric-based attacks report standard deviations of exactly 0.0000. While this likely reflects deterministic attack thresholds rather than measurement error, it looks suspicious and should be clarified (e.g., with a footnote noting these are deterministic). Without clarification, readers may question the measurement precision.

- **AIA results have low baseline accuracy.** The AIA attack accuracy is 10–17% for Place100/Place60 and 52% for UTKFace (vs 42% random baseline). The conclusion that CL does not increase AIA vulnerability is sound, but the analysis would benefit from a more explicit discussion of whether the AIA setting is meaningful when overall accuracy barely exceeds random guessing.

### Trivial
- The paper uses `\attack{}` as a command name throughout; the rendered name in the PDF should be verified to be descriptive rather than a placeholder.

## Nice-to-Haves
- A control experiment measuring the relationship between MIA accuracy and the train-test accuracy gap under each training method would help isolate whether CL's effect on MIA is independent of overfitting.
- Computational cost analysis of the proposed Diff-Cali attack (training shadow models + computing difficulty scores) relative to standard NN-based attack would help practitioners assess adoption.
- Evaluating Diff-Cali against defenses beyond DP-SGD (e.g., MemGuard, MixupMMD) would be informative, though not required given the paper's scope.

## Removed Points
These points are flagged to be removed; treat them with caution:
1. **"Advanced attack methodology is not in main text"** — The attack description is in an `\input{advanced_attack}` file which was stripped by the parser; it exists in the original submission. Removed per parser artifact rules.
2. **"The paper uses 'attack' as a placeholder name"** — This is a formatting nitpick about a LaTeX command; the rendered PDF would show the proper name. Removed per formatting nitpick rules.
3. **"Connection between data ordering and memorization noted before (Shumailov et al.)"** — The paper already cites Shumailov et al. (line 21) and distinguishes its contributions. Removed as already addressed.
4. **"Attack only evaluated against standard training and CL methods, not against defenses"** — The paper evaluates Diff-Cali under DP-SGD (line 610: "attack accuracy for normal and bootstrapping are dropped to 53.67% and 53.09%"). This claim is factually incorrect. Removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Reframe the paper's primary contribution around the *disparate impact on difficult samples* rather than the small aggregate MIA increase; this is the most novel and practically actionable finding.
2. Add a direct TPR@lowFPR comparison between Diff-Cali and the existing Cali method to clearly establish the advantage of using difficulty scores.
3. Extend the defense evaluation to at least one additional dataset (e.g., Tiny ImageNet) to strengthen the generalizability of Finding 6.
4. Add a footnote explaining the 0.0000 standard deviations in Table 3 (e.g., "attack thresholds are deterministic").
5. Discuss the practical feasibility of the adversary obtaining difficulty scores in realistic threat models.

## Score and Decision

The paper makes a solid empirical contribution as the first systematic study of privacy risks in curriculum learning. The core finding about disparate impact on difficult samples is well-supported and non-trivial. The evaluation is thorough in its coverage of datasets, CL methods, and attack variants. The main weaknesses are the incomplete comparison of the proposed attack against the existing calibration baseline on the key metric, and the limited scope of the defense analysis — both addressable. The contributions are genuine and the paper will be a useful reference for the community.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**