I now have a thorough understanding of the paper and have verified all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper presents the first systematic empirical study of how curriculum learning (CL) — training models from easy to hard samples — affects privacy risks, specifically membership inference attacks (MIA) and attribute inference attacks (AIA). Across 9 datasets, 3 architectures, 4 CL variants, and multiple attack/defense methods, the authors find that CL makes target models slightly more vulnerable to MIA (especially for difficult samples, which show disproportionately larger effects up to 4.23%), does not increase AIA vulnerability, and that a proposed difficulty-calibrated MIA (Diff-Cali) improves true-positive rates at low false-positive rates. Existing defenses remain partially effective under CL, though at accuracy costs.

## Strengths

- **First systematic study of privacy risks in curriculum learning.** The paper identifies and fills a genuine gap — prior privacy attack research assumed standard stochastic training, while CL's structured data ordering could plausibly affect memorization and vulnerability. The paper explicitly distinguishes CL from related but different techniques like contrastive learning (line 21), and the related work survey (line 669) confirms no prior work investigated this direction.

- **Disparate vulnerability of difficult samples under CL is convincingly demonstrated.** The paper shows that CL's impact on MIA is concentrated on difficult training samples (up to 4.23% higher attack accuracy for CIFAR100, Figure 2), with the mechanism supported by memorization analysis (violin plots of prediction probabilities, Figures 5–7) and KNN-Shapley valuation. This finding goes beyond the small average effects and identifies a structurally meaningful phenomenon, backed by both attack accuracy breakdowns by difficulty level and confidence score analysis.

- **Comprehensive evaluation across diverse settings.** The study covers 8 datasets for MIA (5 image + 3 tabular), 3 datasets for AIA, 3 network architectures (ResNet-18/34, MobileNet), compares 4 CL methods plus normal training, and tests multiple attack types (NN-based, metric-based, label-only). Results are reported with standard deviations over 5 runs (Tables 1–3), providing robust evidence that observed trends hold across varied settings.

- **Diff-Cali attack proposes a novel use of difficulty information.** The proposed difficulty-calibrated MIA exploits the difficulty scores exposed by CL to calibrate membership predictions, achieving better TPR at low FPR compared to standard NN-based attacks (Figure 14). This is a genuine methodological contribution that leverages the paper's own empirical insights.

## Weaknesses

### Fatal
None.

### Major

- **The DPSGD defense evaluation uses ε = 124,496, which provides no meaningful differential privacy guarantee.** The paper is transparent about this (line 579) and explains the reasons (200 epochs, large model, small batch size for fair comparison), but the inclusion of DPSGD as a "defense" at this epsilon is misleading. At ε > 10⁵, adding noise is mathematically indistinguishable from unconstrained perturbation; the experiment shows that adding massive noise reduces MIA accuracy — but this tells us nothing about whether DPSGD *as a privacy-preserving training method* works under CL. The abstract (line 8) and conclusion (line 689) state that DPSGD is "still effective under CL," which conflates "noise reduces attack accuracy" with "DPSGD provides a meaningful privacy-utility tradeoff under CL." The paper's own Finding 6 correctly centers on the tradeoff ("None of the studied defenses can significantly drop the MIA accuracy while maintaining the target model accuracy"), but the surrounding language overstates what the DPSGD experiment demonstrates. The authors should either run DPSGD with a properly tuned configuration that achieves meaningful ε (or at minimum cite and discuss what ε values prior CL-compatible DP work achieves), or explicitly state that this experiment is an ablation on the effect of noise injection rather than a privacy defense evaluation.

- **The key metric supporting Diff-Cali's advantage (TPR at low FPR) is shown for only one dataset (CIFAR100).** The TPR/FPR analysis in Figure 14 — where Diff-Cali achieves "much higher TPR at low FPR" and outperforms random chance where NN-based attacks fail — is the paper's strongest claim for the proposed attack, yet it is presented only for CIFAR100. The bucket accuracy analysis (Figure 21) does include Tiny ImageNet, but the core claim about improved low-FPR behavior is not replicated there. Given that other empirical trends vary substantially across datasets (e.g., Purchase shows opposite behavior for bootstrapping vs. normal training, Table 2), it is not safe to assume Diff-Cali's advantage generalizes. Replicating the TPR/FPR analysis on at least one additional diverse dataset (e.g., Tiny ImageNet or a tabular dataset) is necessary to support the claim that Diff-Cali's advantage is robust.

### Minor

- **The effect sizes underlying the main MIA finding are small and the paper could better contextualize their practical significance.** The paper is transparent about this — using "slightly" throughout (abstract, lines 29, 281, 687) and reporting 0.01%–2.46% improvements for image datasets. However, without benchmarking against natural variation across random seeds, architectural choices, or dataset splits, the reader cannot assess whether a 1–2% attack accuracy increase at an already-high baseline (often >85%) represents a meaningful privacy risk increase. The paper's key contribution is discovering the *existence* of the phenomenon and the disparate impact on difficult samples — the small average effect sizes do not undermine this. A brief discussion benchmarking effect sizes against natural variation would strengthen the claims.

- **Memorization analysis (Section 5.2) is conducted on a single dataset (CIFAR100) with one training method (bootstrapping) and 800 samples.** While the violin plots and KNN-Shapley analysis are well-designed and provide a principled explanation, repeating this analysis on at least one additional dataset (e.g., Tiny ImageNet) would increase confidence that the mechanism generalizes. The paper acknowledges its limitations (line 648), so this does not invalidate the claims.

- **The AIA analysis offers a plausible but unverified explanation** for why CL does not increase vulnerability (difficulty scores based on the original task do not influence the sensitive attribute, lines 568–569). A control experiment checking whether the difficulty measure correlates with the sensitive attribute would strengthen this negative finding.

- **The cost of Diff-Cali is not discussed.** Since Diff-Cali requires a difficulty measurer (an additional trained model), its computational overhead relative to standard NN-based attacks should be stated so practitioners can evaluate the tradeoff.

### Trivial
None.

## Nice-to-Haves

- The paper could briefly discuss whether anti-curriculum (which decreases MIA accuracy below normal training) could be adapted as a privacy-aware training strategy, preserving some of CL's accuracy benefits while reducing vulnerability. The data already shows this direction (anti-curriculum reduces attack accuracy) but it is treated only as a baseline.

- A brief justification of why black-box-top3 is the most appropriate MIA variant for CL settings, and how CL might affect confidence distributions across top-k predictions, would help readers assess the attack choices. (The paper does cite prior work showing NN-based attacks generally outperform others, line 226.)

## Removed Points

- *Criticism about contrastive learning being closely related.* The harsh critic stated "recent work on contrastive learning (He et al. 2021) is closely related methodologically; a brief comparison of how CL's impact differs from contrastive learning would contextualize the novelty." The paper explicitly distinguishes itself from contrastive learning (line 21: "CL modifies the data order, which differs from many new techniques such as contrastive learning") and discusses the comparison in the AIA section (line 565). This criticism reflects a misunderstanding of the paper's scope.

- *Criticism that the paper should discuss whether CL could be adapted to reduce privacy risks.* This is scope creep — the paper's focus is on *measuring* risks, not on designing mitigations. The paper briefly mentions this as future work (line 637). Asking the authors to redesign CL is outside the paper's stated goals.

- *Criticism about small effect sizes presented as a structural/fatal flaw.* The paper consistently uses "slightly" to describe the magnitude and is fully transparent about effect sizes. The critic inflated this into a core weakness, but the paper's contribution is documenting a phenomenon — not making a claim about large effect magnitudes.

## Novel Insights

The most interesting observation that emerges from combining the reviews with the paper is that CL's impact on privacy is fundamentally asymmetric: it increases MIA vulnerability (especially for difficult samples) but *decreases* AIA vulnerability compared to normal training. This asymmetry suggests that the mechanism through which CL affects privacy is specific to label-space memorization rather than representation-space leakage — a distinction that could guide future work on when training interventions create or mitigate privacy risks. The memorization analysis (Figure 5) connecting CL's data ordering to stronger memorization of difficult samples, combined with the KNN-Shapley analysis showing that this effect is specific to difficulty rather than data value, provides a concrete hypothesis for why CL creates disparate privacy impacts.

## Suggestions

1. **Retire or reframe the DPSGD experiment.** Either run DPSGD with a properly tuned configuration (larger batch size, fewer epochs, calibrated to achieve ε < 10 per Bu et al. 2022 which the authors cite), or explicitly reframe it as an ablation on noise injection's effect on CL rather than a privacy defense evaluation.

2. **Extend the Diff-Cali TPR/FPR analysis to at least one more dataset** (Tiny ImageNet or a tabular dataset) to demonstrate that the improved low-FPR performance generalizes beyond CIFAR100.

3. **Quantify the practical significance** of the observed effect sizes. For example, report the increase in an attacker's true positive rate at fixed low false positive rates (e.g., 0.1% FPR) across all datasets, comparing normal vs. CL training.

4. **Expand the memorization analysis** to at least one additional dataset (Tiny ImageNet) to confirm the mechanism generalizes.

5. **Add a brief computational cost comparison** for Diff-Cali vs. standard NN-based attacks so practitioners can evaluate the tradeoff.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>