Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

## Summary

SigMap proposes a wireless localization foundation model combining two innovations: (1) cycle-adaptive masked pretraining that disrupts periodic CSI patterns to prevent shortcut learning, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into soft prompt tokens for parameter-efficient fine-tuning. The model is evaluated on the DeepMIMO and WAIR-D datasets, showing substantial improvements over baselines in single-BS and multi-BS localization, including strong few-shot transfer to unseen environments.

## Strengths

- **Cycle-adaptive masking is well-motivated and empirically effective on key metrics:** The strategy (Section 3.3) addresses a real problem — periodic CSI patterns enabling shortcut learning — by detecting dominant periodicities via cross-correlation and generating adaptive strip/grid masks (Eq. 6, Fig. 3). Table 3 shows adaptive masking achieves 0.673m MAE and 84.5% CDF@1m in multi-BS localization, outperforming both static grid (0.770m, 80.3%) and strip masking (0.753m, 75.3%) on these metrics.

- **Geographic prompt tuning delivers substantial single-BS localization gains:** Table 1 shows SigMap with map prompts reduces MAE from 2.275m to 1.564m (31% improvement) and more than doubles CDF@1m from 31.0% to 60.5% compared to the no-map variant. The 2D vs 3D ablation (Table 4) further confirms that most of the benefit comes from topological/LoS cues, with only 8% MAE degradation when dropping height information.

- **Parameter-efficient few-shot transfer to unseen environments:** Table 4.5 demonstrates SigMap with map achieves 1.026m MAE on DeepMIMO O2 and 1.880m MAE on WAIR-D's 100 real-world city scenes, outperforming LWLM by 53.2% and 44.3% respectively, while updating only 0.4% of parameters (85k trainable vs 11.73M frozen, Table 5). The two-stage paradigm of self-supervised pretraining + prompt-based fine-tuning is architecturally clean and practical.

## Weaknesses

### Major

- **NLoS-aware attention mechanism (Eq. 11) is undefined in the methodology:** Section 4.2 introduces an "NLoS-aware attention mechanism" with Equation 11 using notation (`o_s^(i)`, `W_NLoS`, `φ(·)`) that never appears in Section 3. The methodology defines only a simple MLP head for single-BS localization (Eq. 8) and an attention-based fusion for multi-BS (Eqs. 9-10). The paper attributes single-BS performance gains to this mechanism ("The key advantage stems from our NLoS-aware attention mechanism"), but readers cannot verify what component is actually responsible or how it connects to the described architecture. This is a significant clarity gap between the method description and the experimental claims.

- **"Zero-shot generalization" claim contradicts the few-shot protocol used:** The abstract and contributions (Section 1.2) claim "strong zero-shot generalization," but Section 4.5 explicitly states that "only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)" and calls this a "few-shot learning setup." Since the GNN prompt module and task heads are updated on target-environment data (Section 3.4 specifies that `θ_gnn`, `θ_proj`, and `θ_task` are trained), this is few-shot transfer, not zero-shot. The abstract overclaims the method's capability.

- **No statistical significance testing:** All results are reported as single values averaged over 5 independent runs (Section 4.1), but no standard deviations, confidence intervals, or significance tests are provided. This is critical because Table 3 reveals that strip masking achieves better RMSE (0.972m) than the claimed-best adaptive masking (1.099m) — without variance estimates, the reader cannot judge whether the MAE/CDF@1m gains of adaptive masking are statistically meaningful or within noise.

### Minor

- **Cycle-adaptive masking is under-specified:** Section 3.3 states that "we compute shift patterns using cross-correlation analysis" but does not specify over which dimensions of the CSI tensor the correlation is computed, nor how the final shift `d_final` is selected from the correlation output. These details matter for reproducibility.

- **Figure 5 radar chart uses undefined metrics:** The axes include "AoA," "ToA," "NLoS," and "oss_scenario" — none of these are defined as evaluation metrics anywhere in the paper. It is unclear what values are plotted or how they were computed. The figure reads as a rhetorical device rather than an informative evaluation.

- **Strip masking RMSE advantage not discussed:** In Table 3, strip masking achieves 0.972m RMSE vs. adaptive masking's 1.099m, yet the paper only highlights MAE and CDF@1m where adaptive wins. This selective reporting should be acknowledged and discussed.

- **Limited interpretability despite claims:** The paper claims "interpretable fusion of environmental constraints" (Section 1.2), but provides no attention-map analysis, no probe of what the geographic prompt encodes, and no explanation of how the model uses the prompt to resolve multipath ambiguity. The 2D vs 3D ablation is informative but does not constitute interpretability analysis.

### Trivial

- Numerical inconsistency: Section 4.5 text states "1.580 m" for WAIR-D while Table 4.5 lists "1.880 m" for SigMap (w/ map) on WAIR-D Scenario-2.

## Nice-to-Haves

- An analysis probing what geometric information the geographic prompt captures (e.g., by ablating specific building features or visualizing prompt-conditioned attention patterns) would strengthen the interpretability claim.
- Comparison against a few-shot baseline that also has access to environmental maps (e.g., a map-conditioned variant of LWLM) would isolate the benefit of the prompt-tuning paradigm from the benefit of simply having map access.
- Explicit discussion of limitations — the evaluation is entirely on synthetic ray-tracing data; qualifying this scope would improve scientific honesty.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim: "Incoherent model description (fatal, structural)"** — Overstated. The core two-stage framework (transformer backbone + cycle-adaptive masking pretraining + geographic prompt fine-tuning + task heads) is coherently described in Sections 3.1–3.5. The problem is specifically with Eq. 11 in Section 4.2, not with the entire model description. Demoted from fatal to major.

- **Harsh Critic claim: missing dataset-split details and pre-training data scale** — The paper defers configuration details to Appendix B.3, which is stripped by the parser. Per instructions, criticisms about missing appendix content are removed.

- **Harsh Critic claim: "no complexity discussion" for the GNN over large 3D scenes** — Speculative concern. The GNN uses only 2 graph convolution layers with global mean pooling, and the GNN is trained during fine-tuning (not run at inference for every sample). The paper additionally reports that inference takes 0.83 ms/sample (Table 5), suggesting practical feasibility.

- **Harsh Critic demand for "real-world validation or explicit limitation"** — Scope creep. Ray-tracing synthetic data (DeepMIMO, WAIR-D) is standard for wireless localization research. The paper's claims are appropriately scoped to these benchmarks.

- **Harsh Critic claim: single prompt token has "severely limited" information capacity** — Speculative. The empirical results (Tables 1, 2, 4.5) show the prompt works effectively; speculating about capacity limits without evidence is not a valid criticism.

- **Strength Finder: "comprehensive multi-metric benchmarking" via Figure 5** — The radar chart metrics are undefined, so this claimed strength is invalid.

- **Strength Finder: "zero-shot generalization"** — Corrected to few-shot transfer; the result remains strong but the framing is wrong.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface genuinely novel observations about the work that the paper itself does not contain.

## Suggestions

- **Reconcile Eq. 11 with the methodology:** Either (a) describe the NLoS-aware attention mechanism in Section 3.5 with consistent notation and explain how it applies to single-BS localization, or (b) remove Eq. 11 and attribute the single-BS gains to the geographic prompt itself (which is the more parsimonious explanation — the prompt provides environmental context that helps the transformer implicitly differentiate LoS/NLoS paths, and the ablation in Table 1 supports this).

- **Replace "zero-shot" with "few-shot"** throughout the abstract and contributions. The few-shot result is genuinely strong and does not need exaggeration.

- **Add standard deviations** to all result tables and discuss where differences are statistically meaningful, particularly the RMSE inversion in Table 3.

- **Define or remove Figure 5's radar chart axes.** If the axes represent normalized composite scores, explain how they are computed. Otherwise, remove the figure — Tables 1–4 already provide sufficient quantitative evidence.

- **Specify the cross-correlation computation** for cycle-adaptive masking: which tensor dimensions, and the procedure for selecting `d_final`.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| NormWear | XhdckVyXKg | 3.00 | R1 (low) | Significantly weaker — limited results, unclear contribution |
| ECG Foundation Model | 7zJDTnogdG | 3.33 | R1 (low) | Weaker — mixed scores, fundamental concerns |
| PowerGPT | ntSP0bzr8Y | 3.00 | R1 (low) | Weaker — generic foundation model |
| DASFormer | 7ipjMIHVJt | 5.25 | R1 (mid) | Weaker — unclear scope, insufficient baselines, rejected |
| MapLearn | PdwrCm5Msr | 4.75 | R2 (lower-mid) | Weaker — limited practical impact, simulation-only testing |
| EM-GANSim | 29JDZxRgPZ | 6.00 | R2 (upper-mid) | Comparable domain but rejected; SigMap has more novel contributions but similar presentation issues |
| G2PTL | sP0Aev2Gis | 6.33 | R2 (upper-mid) | Stronger — clearer methodology, but rejected |
| FECCT | 7KDuQPrAF3 | 6.25 | R1 (upper-mid) | Stronger — clearer methodology, better evaluation rigor, accepted |
| SmartPretrain | Bmzv2Gch9v | 6.75 | R2 (high-mid) | Clearly stronger — model-agnostic, rigorous evaluation, accepted |

**Round 1 bracket:** 5.0–6.5. The paper is clearly above the 3.0–3.5 band and below the 7.5+ band.

**Round 2 narrowing:** The paper sits between DASFormer (5.25) and EM-GANSim (6.00). SigMap's core contributions (cycle-adaptive masking, geographic prompt tuning) are more innovative than EM-GANSim's GAN application, but SigMap shares similar presentation weaknesses (undefined components, overclaimed capabilities). It is weaker than FECCT (6.25) which had cleaner methodology and more rigorous evaluation despite concerns about code-length limitations.

**Final placement:** 5.5 — a borderline paper with genuine technical contributions but presentation issues (undefined Eq. 11, zero-shot overclaim, no statistical testing) that prevent acceptance in current form. A revised version addressing these would be in the 6.0–6.5 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>