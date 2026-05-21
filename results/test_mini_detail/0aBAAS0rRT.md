Now I have all the evidence I need. Let me write the consolidated review.

## Bracketing Summary

**Round 1 bracket**: I initially placed this paper between **4.0 and 6.0** by comparing against:
- Weak anchors (<3.5): ECG foundation model (3.33), time-series SSL (3.0), signal recognition (2.0) — the current paper is clearly stronger than these.
- Middle anchors (3.5–7.5): Wi-GATr (7.0, accepted poster), P-MapNet (5.0, rejected), AddressVLM (5.75, rejected), radar point cloud (4.5, withdrawn). Wi-GATr is stronger (real-world validation, clearer contribution); the others are comparable or weaker.
- Strong anchors (>7.5): Not relevant.

**Round 2 narrowing**: I searched for anchors in (4.0, 5.5) and (5.0, 6.5). The most relevant were DASFormer (5.25, rejected — SSL pre-training for signal data, similar SSL+downstream paradigm) and the radar point cloud paper (4.5). The current paper is stronger than DASFormer in methodological novelty (map-as-prompt is genuinely new), but DASFormer had slightly cleaner framing of its claims.

**Final score: 5.5** — The paper has a genuine methodological contribution (map-as-prompt, cycle-adaptive masking) and strong quantitative results, but is held back by a verifiable overclaim (abstract says "zero-shot," experiments are few-shot with 100 labeled samples) and simulated-only evaluation without adequate limitations discussion. It sits close to AddressVLM (5.75) and DASFormer (5.25) — papers with interesting ideas and solid experiments but with presentation/claim issues or incomplete validation that kept them below threshold.

---

## Summary

This paper proposes SigMap, a multimodal foundation model for wireless localization that introduces (1) a cycle-adaptive masking strategy for self-supervised pre-training that adaptively disrupts periodic CSI patterns, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into lightweight soft prompts for parameter-efficient cross-scenario adaptation. The model is pre-trained on DeepMIMO data and fine-tuned (with ~0.7% of parameters) on downstream localization tasks.

## Strengths

- **Map-as-prompt delivers strong cross-scenario gains with minimal parameter updates.** Table 4.5 shows SigMap with map achieving 1.026 m MAE on DeepMIMO O2 and 1.880 m on WAIR-D, outperforming LWLM by 53% and 44% respectively while updating only 0.085M parameters (0.7% of total). This directly supports the claimed parameter-efficient cross-scenario adaptation.

- **Geographic prompt integration yields consistent improvements across all tasks.** In multi-BS (Table 2), SigMap with map reaches 0.673 m MAE / 84.5% CDF@1m vs. 0.789 m / 77.5% without map. In single-BS NLoS (Table 1), MAE improves from 2.275 m to 1.564 m. The ablation cleanly isolates the benefit of the map-conditioned prompt.

- **Parameter efficiency is concretely quantified.** Table 5 reports fine-tuning uses 0.085M trainable params (30 min for 1000 epochs) and inference takes 0.83 ms/sample — specific, verifiable efficiency numbers uncommon in this area.

- **Cycle-adaptive masking improves MAE and CDF@1m over static strategies.** Table 3: adaptive masking achieves MAE 0.673 m / CDF@1m 84.5% vs. grid-masking (0.770 m / 80.3%) and strip-masking (0.753 m / 75.3%).

## Weaknesses

### Fatal
None.

### Major

- **The claimed "zero-shot" generalization is not zero-shot — it is few-shot.** The abstract states the model "exhibits strong zero-shot generalization in unseen environments," and Section 1.2 claims "strong zero-shot generalization to unseen environments and base station configurations." However, Section 4.5 explicitly describes a few-shot setup: *"only the downstream task heads are fine-tuned using limited target samples (approximately 100 instances per scenario)… This few-shot learning setup"* (lines 329–330). Zero-shot means no target-environment labels at all; fine-tuning on 100 labeled samples is few-shot. This is a concrete overclaim in the paper's headline framing that must be corrected. The cross-scenario results are still impressive as few-shot adaptation — the paper should simply re-label them accurately.

### Minor

- **All experiments use simulated (ray-traced) data only.** Both DeepMIMO and WAIR-D generate CSI via ray-tracing on map geometries. The paper phrases this as "100 real-world city scenes extracted from OpenStreetMap" (line 327), but this refers to the map geometries, not measured field data. No real-world CSI measurements are used. For a paper claiming to be a "foundation model" with practical applicability, the absence of real-world validation should be explicitly discussed as a limitation rather than only implied by the data descriptions.

- **The cycle-adaptive masking shows an unexplained inconsistency across metrics.** In Table 3, adaptive masking improves MAE (0.673 vs. 0.753 for strip) and CDF@1m (84.5% vs. 75.3%) but has *worse* RMSE (1.099 m) than strip-masking (0.972 m) — a ~13% degradation. The authors do not comment on this. If a proposed key component worsens one metric, this deserves discussion, even if the overall trade-off favors the proposed method.

- **No variance or statistical significance reported.** The paper states results are "averaged over 5 independent runs" (line 251) but reports only point estimates. Given that some comparisons show small margins (e.g., SigMap w/o map at 2.275 m MAE vs. LWLM at 2.382 m in single-BS), the absence of standard deviations or confidence intervals makes it impossible to assess whether these differences are meaningful.

- **The core cycle-detection mechanism is underspecified.** Equation (6) references `d_final` (detected periodicity shift) and `j_0` (starting offset) without explaining how these are computed from the cross-correlation analysis. This is a reproducibility gap — a reader cannot implement the method from the paper as written.

### Trivial

- The radar chart (Figure 5) has unlabeled axes, making it difficult to interpret what each spoke represents.
- The CDF curves are referenced ("shown in B.5") but the appendix is not included in the submission.

## Nice-to-Haves

- Include baselines that also use map information (e.g., feeding GNN-derived map features into LWLM) to isolate whether the benefit comes from the map information per se or from the specific prompt integration mechanism.
- Add a qualitative analysis showing localization heatmaps or failure cases to help understand where the map-prompt interaction helps or fails.
- Ablate the multi-BS attention fusion design choices (learned attention vs. uniform weighting).

## Novel Insights

The most interesting observation emerging from the reviews is that the geographic prompt mechanism appears to derive most of its benefit from topological/LoS constraints rather than fine-grained 3D geometry: the 2D bird's-eye variant degrades MAE by only 8% compared to the full 3D mesh (Table 4), and the paper openly acknowledges this. This is not a weakness per se — it suggests the prompt framework is robust to geometric simplification and points toward a practical upgrade path (street-level photographs as prompts). However, this finding also reframes the contribution: the paper's framing emphasizes "3D geographic information" as a differentiator, but the evidence suggests the value is primarily in the topological graph structure, not the third dimension.

## Suggestions

1. **Remove or redefine the "zero-shot" claim.** Replace it with "few-shot" or "cross-scenario generalization" throughout the abstract, contributions, and title. If zero-shot is actually intended, run experiments with no target-environment labels at all. Given the strong few-shot results, honest reframing would not diminish the paper's value.
2. **Add an explicit limitations paragraph** acknowledging that all experiments use ray-traced data, and discussing what steps would be needed for real-world deployment.
3. **Report standard deviations for all main results** (Tables 1–4, 4.5), especially where margins are small.
4. **Discuss the RMSE inconsistency** in the cycle-adaptive masking ablation. Even a brief explanation would address a credibility gap.
5. **Specify the computation of `d_final`** in Equation (6) — how is the dominant periodicity computed from cross-correlation?

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>