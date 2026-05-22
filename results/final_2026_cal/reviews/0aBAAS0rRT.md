Now I have sufficient calibration data. Let me synthesize the final review.

**Calibration Summary:**

Round 1 bracketing: I queried anchors across three bands. The low band (<3.5) returned papers on unrelated topics (EEG, general channel equalization). The middle band (3.5–7.5) returned the most relevant anchors: AEMP (5.33, withdrawn/reject, CSI masked pretraining), TS-DDAE (4.67, poster, wireless signal pretraining), SPAR (4.40, reject, spatial sensing), and PRLS-RFF (4.00, reject, RF fingerprinting). The high band (>7.5) returned papers from unrelated domains (embodied navigation, LLMs, multimodal reasoning). Initial bracket: **4.0–5.5**.

Round 2 narrowing: I read the full reviews of AEMP (5.33), TS-DDAE (4.67), SPAR (4.40), and SPR (4.50) in detail. SigMap has clearer novelty than AEMP (whose reviewers found the MR+AP combination insufficiently novel) and SPAR (whose spatial-awareness concept was seen as familiar). Its reporting issues (zero-shot overclaim, no variance, radar chart, text/table discrepancy) are fixable but nontrivial. Comparing against the strongest anchor — AEMP at 5.33 — SigMap has stronger component novelty but weaker reporting integrity. I place it slightly below AEMP, at **5.0**.

---

## Summary

This paper proposes SigMap, a multimodal foundation model for wireless localization that combines (1) a cycle-adaptive masking strategy for self-supervised pretraining on CSI data and (2) a "map-as-prompt" framework that encodes 3D building geometry via a GNN into lightweight soft prompts for parameter-efficient fine-tuning. The core idea — using signal periodicity to guide masking and encoding spatial topology as learnable prompts — is conceptually compelling and practically motivated. Experiments on DeepMIMO and WAIR-D datasets show SigMap outperforming baselines (OMP, CNN, SWiT, LWLM) on single-BS and multi-BS localization, with especially strong gains from the map prompt.

## Strengths

- **Cycle-adaptive masking is a genuinely novel pretraining strategy for wireless signals.** Table 3 shows adaptive masking (MAE 0.673 m, CDF@1m 84.5%) outperforms fixed grid-masking (0.770 m, 80.3%) and strip-masking (0.753 m, 75.3%) in multi-BS localization. The idea of detecting CSI periodicity and dynamically disrupting periodic shortcuts is domain-specific and well-motivated, going beyond generic masking.

- **Geographic prompt tuning via GNN-encoded 3D map information is novel and effective.** Algorithm 1 and the Delaunay-triangulation graph construction are clearly specified. Tables 1–2 show map prompts reduce single-BS MAE from 2.275 m to 1.564 m (31.3% improvement) and multi-BS MAE from 0.789 m to 0.673 m (14.7% improvement). Table 4 shows even a 2-D bird's-eye view retains most of the benefit (MAE 1.692 vs. 1.564), demonstrating robustness to geometric simplification.

- **Parameter efficiency during fine-tuning is a genuine practical advantage.** Table 5 shows only 0.085 M parameters (0.7% of total) are updated during fine-tuning, requiring just 30 minutes for 1000 epochs. This is a concrete advantage for practical deployment where retraining a full model is expensive.

- **Strong few-shot generalization results.** Section 4.5 shows SigMap (w/ map) achieving MAE 1.026 m on unseen DeepMIMO O2 (53.2% better than LWLM) and 1.880 m on WAIR-D Scenario-2 (44.3% better), despite fine-tuning only the task heads on ~100 labeled samples per scenario.

## Weaknesses

### Major

- **The abstract and introduction claim "strong zero-shot generalization," but the experiments are few-shot, not zero-shot.** The paper explicitly states in Section 4.5 that "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)." Zero-shot would require no labeled data from the target environment. This is a significant overclaim that misrepresents the strength of the contribution. The actual few-shot results are still impressive; the claim should be corrected to "few-shot" or "parameter-efficient few-shot generalization."

### Minor

- **No measures of variability are reported for any result.** All tables present only point estimates (MAE, RMSE, CDF@1m) averaged over 5 runs, without standard deviations or confidence intervals. Given that some comparisons involve small margins (e.g., SigMap w/o map MAE 2.275 vs. LWLM 2.382 in Table 1; multi-BS RMSE 1.285 vs. 1.178), it is impossible to assess statistical significance.

- **Figure 5 (radar chart) introduces metrics not evaluated in the experimental section.** The radar chart includes axes labeled "AoA," "ToA," and "oss_scenario." AoA and ToA are mentioned only in the preliminaries (Section 2) and are never defined as evaluation metrics or reported in any table. "oss_scenario" is unexplained. The paper does not describe how these values were computed or what data supports them. This either reflects selective reporting or a decorative chart; either way it undermines the evaluation's credibility.

- **Text/table discrepancy for the WAIR-D generalization result.** The generalization table in Section 4.5 reports SIGMAP (w/ map) MAE as **1.880 m** for WAIR-D Scenario-2, but the text reads "1.580 m on WAIR-D Scenario-2." One of these is wrong.

- **The cycle-adaptive masking algorithm is underspecified.** Equation (6) uses `d_final` (the detected periodicity shift), and the text mentions "cross-correlation analysis" and "row-wise cross-correlation." However, the paper does not specify the concrete algorithm: along which tensor dimension cross-correlation is computed, how periodicities are detected from the cross-correlation output, how multiple periodicities are aggregated into a single `d_final`, or what thresholding/selection procedure is used. This makes the paper's central methodological innovation difficult to reproduce independently.

### Trivial

- **The masking ablation (Table 3) compares "adaptive masking" against "grid-masking only" and "strip-masking only."** These baselines differ in both shape and adaptivity. A cleaner ablation would isolate the periodicity-awareness component by comparing adaptive vs. non-adaptive versions of the same mask shape (e.g., both strip-shaped, one with fixed offset and one with periodic offset). The current comparison still demonstrates that adaptive masking works best, but does not cleanly attribute the gain to periodicity-awareness rather than mask shape.

## Nice-to-Haves

- Report multi-BS results for the map-modality ablation (Table 4) to show whether the geometric prompt's benefit persists when multiple BS provide spatial diversity.
- Include linear probing experiments to isolate the quality of the self-supervised representations from the map-prompt contribution.
- Evaluate with varying numbers of labeled samples (e.g., 0 — truly zero-shot — 10, 50, 100) in the generalization setting to characterize data efficiency more thoroughly.

## Removed Points

The following points from the reviews were removed:

- *Harsh critic: "The evaluation does not establish that the pretrained backbone itself is SOTA; headline results conflate two contributions."* — Partially valid but overstated. The paper includes separate ablations for masking (Table 3) and map modality (Table 4). The critic's observation that SigMap w/o map has worse RMSE than LWLM in single-BS (8.532 vs. 5.822) is factually correct but is a single-BS phenomenon; in multi-BS the RMSE gap narrows (1.285 vs. 1.178). Removed as the paper's ablations do partially decouple the contributions.
- *Harsh critic: "Fine-tuning protocol not fully specified (learning rate, optimizer, batch size)."* — These details are standard appendix content. The paper specifies 1000 epochs, ~100 samples, and 0.4% parameter update. Removed as details belong in appendix which may exist in the full submission.
- *Harsh critic: "CSI dimensions not specified."* — The paper provides the tensor form (Eq. 4) and references Appendix B.3. Specific numerical values are appendix-level detail. Removed.
- *Strength Finder: "Radar chart shows multi-metric superiority."* — This strength conflicts with a verified weakness (the chart introduces unevaluated metrics). Removed per the rule that when a strength and weakness disagree, the weakness wins.
- *Strength Finder: "Strong zero-shot/few-shot generalization."* — The strength conflates zero-shot and few-shot, which is precisely the paper's overclaim. Rephrased as a pure strength about few-shot results in the Strengths section above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the zero-shot overclaim** throughout the paper: replace "zero-shot generalization" with "few-shot generalization" or "parameter-efficient adaptation." The few-shot results are genuinely strong and do not need inflated framing.
2. **Add standard deviations** to all tables. The paper already averages over 5 runs; reporting ±std is a minor formatting change that would greatly improve evidential quality.
3. **Remove or properly justify the radar chart.** Either remove Figure 5 entirely, or add a table reporting each axis's metric with clear definitions. If AoA/ToA metrics were computed, describe how.
4. **Fix the WAIR-D discrepancy**: clarify whether the correct value is 1.880 m or 1.580 m in both text and table.
5. **Specify the periodicity detection algorithm** in sufficient detail for reproduction: the cross-correlation dimension, detection/selection procedure for `d_final`, and any thresholding.

## Score and Decision

**Calibration report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| AEMP (CSI localization, masked pretraining) | 5.33 | 1, 2 | Very similar domain. SigMap has clearer novelty but worse reporting integrity. SigMap is slightly weaker overall. |
| TS-DDAE (wireless signal recognition pretraining) | 4.67 | 1, 2 | Different task (recognition vs. localization). SigMap has more novel components. Comparable overall quality. |
| SPAR (distributed sensing, spatial awareness) | 4.40 | 1, 2 | SigMap has clearer domain-specific novelty. SigMap is stronger. |
| PRLS-RFF (RF fingerprinting, SSL) | 4.00 | 1 | Less relevant domain. SigMap is stronger. |
| SPR (EEG SSL, spatial representations) | 4.50 | 2 | Different domain. SigMap has stronger empirical validation. |

Round 1 bracket: 4.0–5.5. Round 2 narrowed to ~5.0 based on comparison with AEMP (5.33), where SigMap's stronger novelty is balanced by its weaker reporting.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>