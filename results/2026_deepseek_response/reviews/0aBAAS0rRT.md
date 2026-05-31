## Summary

The paper proposes SigMap, a wireless localization foundation model that combines (1) cycle-adaptive masked modeling that dynamically adjusts masking patterns based on channel periodicity to prevent shortcut learning during self-supervised pre-training, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into lightweight soft prompts for parameter-efficient fine-tuning. Experiments on simulated datasets (DeepMIMO, WAIR-D) show improvements over baselines including LWLM, SWiT, CNN, and OMP.

## Strengths

- **Cycle-adaptive masking clearly outperforms fixed masking strategies**: Table 3 shows adaptive masking achieves 0.673 m MAE and 84.5% CDF@1m vs. 0.770 m/80.3% (grid) and 0.753 m/75.3% (strip), directly supporting the claim that dynamic periodic disruption improves representation learning beyond simple interpolation.

- **Geographic prompt tuning enables efficient cross-scenario adaptation**: The generalization experiment (Section 4.5) reports 1.026 m MAE on DeepMIMO O2 and 1.880 m on WAIR-D Scenario-2, outperforming LWLM by 53.2% and 44.3% respectively, while updating only ~0.7% of parameters. This is a practically meaningful result.

- **Map integration produces large and consistent gains**: SIGMAP with map improves over without-map by 31.2% (single-BS, Table 1: 1.564 vs 2.275 m) and 14.7% (multi-BS, Table 2: 0.673 vs 0.789 m). The 2-D birdview ablation (Table 4: 1.692 m) retains most of the benefit, confirming robustness of the prompt mechanism.

- **Parameter efficiency is well-demonstrated**: Table 5 reports 0.085 M trainable params (0.7% of total), 30-minute fine-tuning, and 0.83 ms/sample inference, making the practical deployability claim credible.

- **Attention-based multi-BS fusion achieves strong absolute accuracy**: 0.673 m MAE at 84.5% CDF@1m with 4 base stations (Table 2) substantially beats all baselines by clear margins.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed "zero-shot" generalization.** The abstract and contribution list (Sections 1, 1.2) claim "strong zero-shot generalization in unseen environments." However, Section 4.5 explicitly states: "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario). This few-shot learning setup..." This is few-shot adaptation, not zero-shot. The framing misrepresents the contribution — the paper would be stronger if it honestly characterized this as few-shot / efficient adaptation.

2. **Verifiable numerical error in generalization results.** The text in Section 4.5 states "SIGMAP reaches 1.026 m MAE on DeepMIMO O2 and **1.580 m** on WAIR-D Scenario-2" (line 340), but the corresponding table (line 336) shows **1.880 m** for WAIR-D Scenario-2. This is a clear inconsistency that undermines trust in the reported results and suggests sloppy data handling.

3. **NLoS-aware attention (Equation 11) introduced ad-hoc in results section.** Equation 11 in Section 4.2 presents an "NLoS-aware attention mechanism" with variables (o_s^(i), W_NLoS) that are never defined in the methodology (Section 3). This mechanism is not described in Section 3, not shown in Figure 2, and appears suddenly to explain performance. Either a key architectural component was omitted from the method section, or the explanation is an afterthought — either case indicates a serious coherence problem.

4. **No error bars or variance reporting.** All main tables (Tables 1–4, generalization table) report single numbers averaged over 5 runs without standard deviations or confidence intervals. Given moderate differences in some comparisons (e.g., 0.673 vs 0.789 m in Table 2), the reader cannot assess whether improvements are statistically meaningful.

### Minor

5. **Narrow baseline set.** Only four baselines are compared (LWLM, SWiT, CNN, OMP). OMP is a weak classical baseline. Several self-supervised approaches discussed in related work (CrowdBERT, signal-guided masked autoencoders, WirelessGPT) are not included, weakening the "state-of-the-art" claim.

6. **Underspecified cycle-adaptive masking computation.** Equation (6) defines the mask pattern given d_final, but the paper never explains how d_final is computed from cross-correlation. The description ("compute shift patterns using cross-correlation analysis") is too vague to reproduce without guessing.

7. **Inconsistent parameter efficiency claim (0.4% vs 0.7%).** Line 340 mentions "updating only 0.4% of parameters" while line 352 says "only 0.7% of the total parameters." From Table 5 (0.085M/11.730M ≈ 0.72%), the correct figure is ~0.7%. The 0.4% claim is inconsistent.

8. **No comparison to full fine-tuning of the same model.** Table 5 compares parameter counts only against pre-training. Without a performance comparison between prompt tuning and full fine-tuning, it is unclear whether prompt tuning sacrifices accuracy for efficiency or achieves comparable results.

9. **Entirely simulated evaluation.** All experiments use ray-tracing simulated data (DeepMIMO, WAIR-D). No real-world measurements are included. The paper does not acknowledge this as a limitation.

### Trivial

10. The paper does not discuss why strip-masking achieves lower RMSE (0.972) than adaptive masking (1.099) in Table 3, while claiming adaptive masking is superior overall.

## Nice-to-Haves

- Add standard deviations or confidence intervals to all tables.
- Include at least one relevant self-supervised baseline (e.g., masked autoencoder without cycle-adaptive masking).
- Add an ablation replacing the map prompt with random learnable tokens of the same size.
- Compare against full fine-tuning of the same backbone to isolate parameter-efficiency benefit.
- Provide interpretability analysis (attention maps, prompt token similarity across scenes).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Delaunay triangulation in 3D space being computationally heavy"** — speculation about computational cost, not a verified issue from the paper.
- **Harsh Critic: "The physics background is overly verbose"** — subjective style preference, not a substantive weakness.
- **Harsh Critic: "Does not engage with prior work on map-aided localization"** — scope-of-related-work argument not verifiable from the paper alone.
- **Harsh Critic: Various formatting nitpicks** — removed per instructions.
- **Strength Finder: Generic strengths about "addressing an important problem"** — removed per instruction to drop generic/superficial strengths.
- **Strength Finder: "2D variant retaining most improvement is a nuanced finding"** — somewhat generic and conflicts with verified weakness about simulated-only evaluation.

## Novel Insights

None beyond the paper's own contributions. The strengths and weaknesses identified by the reviewers largely track the paper's stated contributions and gaps; no reviewer surfaced a genuinely unexpected observation about the method or results.

## Suggestions

1. **Fix the core framing**: Replace "zero-shot" with "few-shot" or "parameter-efficient adaptation" throughout the paper, including the abstract. Report the exact number of labeled samples used.
2. **Correct the numerical error**: Ensure the WAIR-D Scenario-2 MAE is consistently reported (1.880 m per the table).
3. **Integrate NLoS-aware attention into Section 3 methodology**: Either fully describe it as part of the architecture, or remove Equation 11 from Section 4 and replace it with an ablation analysis.
4. **Add standard deviations** to all tables based on the 5 runs already performed.
5. **Resolve the 0.4%/0.7% inconsistency** and use the correct figure.
6. **Add a full fine-tuning comparison** to clarify whether prompt tuning maintains accuracy.
7. **Acknowledge the simulated-only evaluation** as a limitation and discuss real-world applicability.
8. **Clarify how d_final is computed** in the cycle-adaptive masking for reproducibility.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>