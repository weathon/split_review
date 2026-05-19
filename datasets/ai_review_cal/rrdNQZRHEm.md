- Decision: Reject
- Avg Score: 5.43
- Scores: 6, 8, 5, 5, 5, 6, 3
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

The paper proposes GS-MoE, a weakly-supervised video anomaly detection (WSVAD) framework combining Temporal Gaussian Splatting (TGS) — generating soft pseudo-labels via Gaussian kernels fitted to detected peaks in anomaly scores — with a Mixture-of-Experts architecture where each expert specializes in one anomaly class. A gate model integrates expert predictions with coarse task-aware features. The method achieves 91.58% AUC on UCF-Crime (+3.56% over prior SOTA) and competitive 82.89% AP on XD-Violence.

## Strengths

- **State-of-the-art results on UCF-Crime.** GS-MoE achieves 91.58% AUC, outperforming the previous best model VadCLIP by 3.56% (Table 1). The gain is even larger on the abnormal-only metric AUC_A (83.86% vs. 70.81%, +13.05%), directly supporting the claim that class-specific experts and TGS improve detection of subtle anomalies.

- **Controlled ablation shows TGS loss improves baselines independently.** Fine-tuning the UR-DMU baseline with only the TGS loss yields +1.77% AUC on UCF-Crime and +0.48% AP_A on XD-Violence (Table 2), isolating the benefit of the novel loss formulation from the full architecture.

- **Expert masking ablations prove class-specific necessity.** Masking a given class expert collapses the gate model's AUC for that class to approximately 50% (random), while including it yields high scores (e.g., 86.37% for "Abuse", Table 4). This directly validates the claim that dedicated class experts are critical for capturing category-specific attributes.

- **Large category-wise improvements on complex anomalies.** Figure 4 shows absolute gains of up to +24.3% over baseline on challenging classes such as "Arson", "Assault", and "Fighting", demonstrating the method's effectiveness on subtle real-world anomalies.

- **Cluster-based experts work without predefined class labels.** When anomaly classes are not specified, GS-MoE with 7 cluster-based experts still outperforms prior SOTA by 0.56% AUC on UCF-Crime (Table 5), showing the framework works in realistic deployment scenarios.

- **Ablation studies systematically isolate each component.** Tables 2, 3, 4, and 5 provide step-by-step ablations of TGS, experts, gate model, task-aware features, and cluster-based experts with controlled comparisons.

## Weaknesses

### Fatal

None.

### Major

- **The TGS peak-detection and kernel-generation algorithm is underspecified.** The paper states that peaks $P_1,\dots,P_n$ are "detected" and widths $W_1,\dots,W_n$ are determined (line 129), and that $\sigma_i$ is "the standard deviation of the scores around the peak centered in $P_i$ within the width $W_i$" (line 143), but never specifies the concrete algorithm for any of these operations. How are peaks identified (local maxima above a threshold? persistence-based?)? How is $W_i$ computed (full-width at half-maximum? fixed window? score-based falloff?)? Since the Gaussian kernels and therefore the pseudo-labels depend entirely on these choices, the core technical contribution cannot be independently reproduced from the description alone. Parameters such as minimum peak height, minimum inter-peak distance, and width-estimation rule are absent. This is not a minor implementation detail — it is the algorithmic core of the claimed novelty — and it must be fully specified.

### Minor

- **Self-training dynamics are not analyzed.** The TGS pseudo-labels are generated from the UR-DMU model's own predictions after MIL pre-training, and the same model is then fine-tuned with BCE loss against those pseudo-labels. The paper acknowledges spurious peaks as a concern but addresses it only by pre-training with MIL for "a few iterations" (line 129). There is no analysis of pseudo-label quality (e.g., agreement with ground-truth frames on a validation set), no discussion of whether pseudo-labels are iteratively refined or used as a fixed one-shot target, and no comparison with alternative pseudo-labeling strategies. The ablation shows +1.77% AUC gain — modest enough to be genuine — but the paper does not present evidence that rules out confirmation bias or overfitting to model outputs.

- **XD-Violence results are slightly overclaimed.** The paper describes GS-MoE's 82.89% AP vs. VadCLIP's 84.15% AP as "competitive" (line 185), which is fair. However, the conclusion states the method "consistently outperforms SOTA methods" (line 242), which overstates the XD-Violence case where it trails on the primary AP metric. The claim should be calibrated: GS-MoE is SOTA on UCF-Crime and on XD-Violence AP_A, but not on XD-Violence AP.

- **The large AUC_A improvement lacks analysis.** GS-MoE improves AUC_A by +13.05% (from 70.81% to 83.86%) on UCF-Crime while improving overall AUC by +4.24% (from 87.34% to 91.58%). The paper attributes this to better detection of subtle anomalies, which is plausible, but does not analyze which videos or categories drive the disproportionate AUC_A gain. An analysis of per-video or per-category AUC_A would strengthen the evidence.

- **No statistical significance reported.** All results are single-run with no confidence intervals or variance over seeds. Given the multi-stage training pipeline (MIL pre-training → TGS fine-tuning → expert training → gate training), single-run results weaken evidential weight. At minimum, the main UCF-Crime AUC and XD-Violence AP should be reported with variance.

### Trivial

- The term "Gaussian Splatting" is borrowed from 3D graphics (Kerbl et al., 2023) and the paper does acknowledge this lineage (Section 2.3), but the analogy is loose — the proposed technique fits 1D Gaussian kernels to score peaks, not the 3D scene representation the term normally refers to. A brief note clarifying that this is a distinct technique would avoid confusion.
- Only three qualitative examples are shown (Figure 6); inclusion of failure or borderline cases would be more informative.

## Nice-to-Haves

- A comparison with a direct pseudo-labeling baseline that softens top-k scores without Gaussian weighting, to isolate the benefit of the Gaussian splatting step itself.
- An analysis of pseudo-label quality against ground-truth frame-level labels on a held-out set, to confirm that TGS pseudo-labels correlate with actual anomalous regions rather than model artifacts.
- Discussion of why GS-MoE trails VadCLIP on XD-Violence AP (e.g., multimodal CLIP features vs. I3D features, video duration distribution, category structure).

## Removed Points

These points were flagged for removal and should be treated with caution:

1. **"Circularity in σ_i definition"** (Harsh Critic, Critical Issue 2, Methodology 3.1): The critic claims σ_i is circularly defined. This is incorrect — the paper states σ_i is "the standard deviation of the scores around the peak centered in P_i within the width W_i" (line 143), meaning σ_i is computed from the predicted anomaly scores (data), not from itself. The real issue is that W_i is underspecified, not circularity. Removed as factually inaccurate.

2. **"Missing comparison with Zhang et al.'s pseudo-labeling in experiments"** (Harsh Critic, Related Work): The paper cites Zhang et al. (2023b) in the related work. Not every related work must serve as an experimental baseline; this is a scope preference, not a flaw. Removed as scope creep.

3. **"Questions about expert parameter sharing and training dynamics"** (Harsh Critic, Methodology 3.2): Questions about whether experts share parameters, how many parameters per expert, and class-balance issues are reasonable implementation curiosities but are not weaknesses that threaten the paper's claims. The paper describes the expert architecture at a sufficient level for the claims made. Demoted to nice-to-have.

4. **"Only 3 qualitative examples"** presented as a standalone weakness: Already folded into Trivial. The critic's framing as a core weakness is disproportionate.

5. **Strength Finder's generic endorsements** (e.g., "the problem addressed is important"): These are superficial and lack specific evidence from the paper. Dropped per filtering rules. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between strong empirical results (genuine SOTA on UCF-Crime, rigorous ablations) and an algorithmic core that is underspecified for independent reproduction. This is a resolvable gap — the method appears sound, but the description must be completed before the contribution can be fully evaluated.

## Suggestions

1. **Provide explicit pseudocode** for the peak detection and Gaussian kernel generation algorithm, including: the method for peak identification (e.g., local maxima above a minimum score threshold with a minimum inter-peak distance), the rule for computing each peak's width $W_i$ (e.g., full-width at half-maximum, or score-drop ratio), and the formula for computing $\sigma_i$ from the scores within $W_i$.

2. **Add a pseudo-label quality analysis** comparing TGS pseudo-labels to ground-truth frame-level labels on a validation split. Include a comparison with a simpler baseline (e.g., using raw scores as soft labels without Gaussian weighting) to isolate the benefit of the Gaussian splatting step.

3. **Report main results with variance** over at least 3 random seeds, especially for the primary metrics (UCF-Crime AUC, XD-Violence AP).

4. **Clarify training hyperparameters**: number of MIL pre-training epochs before pseudo-label extraction, number of TGS fine-tuning epochs, learning rate schedules for each stage, and whether experts are trained from scratch or initialized from the task encoder.

5. **Calibrate claims** on XD-Violence — explicitly state that GS-MoE achieves SOTA on UCF-Crime (all metrics) and XD-Violence AP_A, while being competitive on XD-Violence AP.
