Now I have all the evidence I need. Let me write the final consolidated review.

## Summary
This paper proposes SigMap, a multimodal foundation model for wireless localization that introduces two innovations: (1) a cycle-adaptive masking strategy for self-supervised pre-training on CSI data that disrupts periodic shortcuts, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into lightweight soft prompts for parameter-efficient cross-scenario adaptation. The model is pre-trained on DeepMIMO simulated data and evaluated on single-BS and multi-BS localization tasks, with generalization tests on a second DeepMIMO scenario and the WAIR-D dataset.

## Strengths

- **Cycle-adaptive masking addresses a genuine failure mode in SSL for periodic signals**: The paper identifies that standard masked autoencoding allows models to exploit periodic structure in CSI as shortcuts, and validates in Table 3 that adaptive masking improves MAE from 0.770m (grid-masking) to 0.673m in multi-BS localization — a 12.6% improvement. This is a well-motivated, domain-specific adaptation of masked modeling.

- **Map-as-prompt framework achieves dramatic parameter efficiency with strong results**: The geographic prompt mechanism (Section 3.4) restricts fine-tuning to only 0.085M trainable parameters (0.7% of the 11.73M total), yet achieves 1.564m MAE in single-BS and 0.673m in multi-BS localization, outperforming LWLM (2.382m and 0.828m respectively) while updating orders of magnitude fewer parameters (Table 5). This is a practical contribution for deployment.

- **Generalization to unseen environments is demonstrated with limited supervision**: On DeepMIMO O2 and WAIR-D Scenario-2 (100 real-world city scenes), SIGMAP with map achieves 1.026m and 1.880m MAE respectively, outperforming LWLM by 53.2% and 44.3% (Table 4.5) with only ~100 target samples for fine-tuning. The WAIR-D evaluation across 100 diverse city layouts provides reasonable evidence of cross-scenario transfer.

- **Ablation on map quality cleanly isolates the value of 3D geometry**: Table 4 shows that 2D bird's-eye polygons increase MAE by only 8% relative to full 3D meshes (1.692 vs 1.564m), while removing maps entirely raises MAE by 45% (2.275m). This helps attribute the gain to topological/LoS cues rather than fine geometric detail.

## Weaknesses

### Major

- **Inconsistent reporting of WAIR-D results**: The main text (line 613) states that SIGMAP achieves "1.580 m on WAIR-D Scenario-2," but the corresponding table entry (line 608) shows **1.880m** MAE for SIGMAP (w/ map). The improvement percentage of 44.3% over LWLM's 3.375m is consistent with 1.880m, not 1.580m, confirming that 1.580 is an error. Data inconsistencies of this nature undermine trust in the results and must be corrected.

- **"Zero-shot generalization" claim is misleading**: The abstract claims "strong zero-shot generalization," but all generalization experiments fine-tune on ~100 labeled target samples (described as a "few-shot learning setup" in line 589-590). True zero-shot evaluation — applying the pre-trained model directly to a new environment without any fine-tuning — is never reported. This is a meaningful gap: the abstract claims a capability the experiments do not test.

- **Insufficient ablation of the geographic prompt mechanism**: The "w/o map" condition (Table 1, 2, 4) removes both the prompt tokens and the geographic information simultaneously. This conflates two effects: (a) the benefit of prompt-based fine-tuning as a parameter-efficient adaptation strategy, and (b) the benefit of geographic content specifically. Without comparing against prompt tuning with random (non-geographic) prompts or full fine-tuning with maps, it is impossible to attribute the observed gains to the geographic information versus the prompt mechanism itself. This is a core gap for a paper whose claimed contribution centers on geographic integration.

- **Limited evaluation breadth for a "foundation model" claim**: The main results (Tables 1-3) come from a single simulated dataset (DeepMIMO O1_3p5). While the generalization section adds two settings, the pre-training, fine-tuning, and main evaluation all use the same ray-tracing simulator (Remcom Wireless InSite via DeepMIMO). A "foundation model" framing implies broad competence across diverse conditions; the current evaluation — one simulated urban scenario with two transfer targets — does not support this scope. Real-world CSI data with hardware impairments and non-ideal propagation is never tested.

### Minor

- **High RMSE/MAE ratio suggests heavy-tailed errors**: For single-BS localization, RMSE (5.675m) is 3.6× the MAE (1.564m). This far exceeds the Gaussian expectation (~1.25×) and indicates extreme outliers. The paper reports no median error or percentiles (e.g., P90), making it difficult to assess whether the approach systematically fails in certain conditions — which is precisely the scenario that matters most for real-world deployment.

- **Cycle-adaptive masking mechanism is partially underspecified**: Section 3.3 and Appendix B.4 describe cross-correlation-based periodicity detection and shift pattern augmentation, but the precise computation of `d_final` (the detected periodicity shift used in Equation 6) is not specified. The augmentation introduces free parameters (N_a=8, N_s=32, random starts) whose sensitivity is never ablated. It is unclear whether the gains come from periodicity detection or the random augmentation parameters.

- **Geographic prompt generation uses standard GCN with symmetric normalization on a heterogeneous graph**: Algorithm 1 applies the standard GCN update (`˜D^{-1/2} ˜A ˜D^{-1/2}`) on a graph where building vertices and base station nodes serve fundamentally different roles. While this may work empirically, no justification is provided for why a homophilic graph operator is appropriate for this heterogeneous structure.

### Trivial

- Table 4.5 appears mislabeled as "Table 4.5" rather than "Table 5" — numbering should be sequential.
- The 1.580 vs. 1.880 WAIR-D discrepancy (discussed above) is a clear copy-editing error.

## Nice-to-Haves

- **Random-prompt baseline**: Comparing map-derived prompts against learned random prompts (no geographic content) would cleanly isolate the value of geographic information from the prompt mechanism itself.
- **True zero-shot evaluation**: Reporting pre-trained model performance without any fine-tuning on new environments would substantiate the "zero-shot" claim in the abstract.
- **Median/percentile error metrics**: Given the high RMSE/MAE ratio, reporting P50 and P90 errors would clarify whether failures are concentrated or dispersed.
- **Real-world CSI validation**: Even a small-scale real-world test would significantly strengthen the practical relevance claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Only one additional unseen scenario tested"**: Factually incorrect — the paper tests two (DeepMIMO O2 and WAIR-D Scenario-2, the latter covering 100 city scenes). The reviewer's own text later acknowledges "exactly two settings."
- **"No comparison to any method that uses map information"**: SIGMAP is the first approach to integrate 3D maps into CSI-based localization. Demanding comparison to non-existent methods is a strawman. The paper compares against the best available baselines (LWLM, SWiT, CNN, OMP).
- **"Parameter count suspiciously low for a transformer backbone"**: A transformer with feature dimension 512 and moderate depth (likely 4-6 layers) plausibly yields ~11.7M parameters. The reviewer compares to ViT-Base (768 dim, 12 layers, ~86M) which is a different architecture class.
- **"SWiT (2024) and LWLM (2025) are outdated/weak"**: These are the most recent (2024-2025) learned localization methods. OMP is a standard classical baseline. The claim is unsupported.
- **Pure formatting/style nitpicks**: Removed per policy (parser artifacts, not author errors).
- **"GCN assumes homophily" concern**: This is a minor theoretical observation that lacks empirical evidence of harm. Deferred to Nice-to-Haves.
- **"Section C reads as post-hoc justification"**: This is a subjective stylistic judgment, not a substantive weakness.

## Novel Insights

The most striking pattern across the reviews is that both supporters and critics agree the core ideas (periodic-aware masking, geographic prompts) are well-motivated and address real gaps in wireless SSL. The disagreement centers sharply on execution: whether the evaluation is sufficient to support the "foundation model" framing. This reveals a fundamental tension in specialized-domain foundation model papers — the ICLR community increasingly expects broad multi-task, multi-dataset evaluation standards from NLP/vision, while wireless localization is an emerging domain where even a single simulator-based benchmark with two transfer targets represents meaningful progress relative to prior practice. The paper would benefit from either expanding its evaluation scope or tempering its claims to match the evidence.

## Suggestions

1. **Fix the WAIR-D data inconsistency** (1.580 → 1.880 in the text) and verify all numerical values match between tables and prose.
2. **Add a random-prompt ablation**: Fine-tune with randomly initialized (non-geographic) prompts to isolate whether map content or the prompt structure drives the gains.
3. **Report true zero-shot performance** (no target-sample fine-tuning) to substantiate the abstract's claim.
4. **Report median error and P90** alongside MAE/RMSE to characterize the error distribution, especially given the high RMSE/MAE ratio.
5. **Temper the "foundation model" language** in the abstract and title unless evaluation is expanded to more diverse conditions (real-world data, different frequency bands, different array geometries).

## Score and Decision

**Calibration Anchors** (all from ICLR 2026 human reviews under /home/wg25r/review_agent/human_reviews_2026/):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `3AbyfpQgR2.md` (AEMP) | 5.33 | Same domain (CSI localization + SSL). AEMP had weaker novelty but stronger evaluation (real-world data, multiple public datasets). SigMap has more novel ideas but narrower evaluation. **SigMap slightly weaker overall.** |
| `DmCof7cMTc.md` (GRF-LLM) | 4.00 | Same domain (wireless + environment integration). GRF-LLM had strong novelty concerns (incremental to WRF-GS). SigMap's technical contributions are cleaner. **SigMap stronger.** |
| `be4ey66fhk.md` (SPAR) | 4.40 | SSL for distributed sensing with spatial awareness. Similar pattern: motivated contributions, some ablation gaps, limited evaluation breadth. **Comparable quality.** |
| `64Ea2Dx0JJ.md` (VLM GeoPriv) | 5.50 | Accepted poster. Different domain but well-executed benchmark paper. Stronger evaluation methodology. **SigMap weaker.** |
| `PUm9OaFNvf.md` (FlowletFormer) | 4.00 | BERT adaptation for traffic classification. More incremental than SigMap. **SigMap stronger.** |
| `StD1GnueIb.md` (GeoReasoning) | 3.50 | Localization with limited baselines, new dataset. Weak evaluation. **SigMap stronger.** |
| `eDxZ6MR2FL.md` (LLM Time Series) | 3.50 | Methodological flaws in evaluation. **SigMap is stronger methodologically.** |

SigMap has genuine technical contributions (cycle-adaptive masking, geographic prompts) that are well-motivated by the domain. However, it suffers from a concrete data inconsistency (WAIR-D), an overclaimed "zero-shot" narrative, and evaluation breadth insufficient for its "foundation model" framing. Comparing against the anchors, it sits between the rejected papers (avg 4.0) and the marginal accepts (avg 5.3-5.5) — stronger in novelty than most rejects but held back by execution issues that prevent acceptance at the current bar.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>