I've read the full paper. Now I'll verify key claims and proceed with calibration.

Verified findings:
- Eq. 11 (NLoS-aware attention) IS introduced in §4.2 with no prior description in Methodology — VERIFIED
- §4.5 text says "1.580 m on WAIR-D" but table shows 1.880 m — VERIFIED inconsistency
- §4.5 says "0.4 %" while §4.6 says "0.7%" — VERIFIED inconsistency
- §4.4 refers to "Figure 1" for side-by-side ablation, but Figure 1 is propagation paths — VERIFIED
- §4.5 conflicts with §3.4: §4.5 says "only the downstream task heads are fine-tuned ... backbone remains frozen" but §3.4 explicitly trains θ_gnn, θ_proj, θ_task — VERIFIED inconsistency
- Eq. 6 references d_final and j_0 without describing how they are computed — VERIFIED
- No std deviations despite "averaged over 5 runs" — VERIFIED
- Table 4 numbers confirm 2D captures most of map gain — VERIFIEDRound 1 bracket: The paper has interesting ideas (map-as-prompt for wireless localization) but suffers from serious methodological gaps (Eq. 11 undefined in methodology), multiple numerical inconsistencies (1.580 vs 1.880, 0.4% vs 0.7%, Figure 1 misreference), and a contradictory description of what's fine-tuned. Comparable to weak-to-middle anchors. I'll bracket between **3 and 5**.I have enough calibration data. Let me finalize the review.

**Round 2 anchors examined:**
- PowerGPT (3.0): foundation model claim with multiple referencing errors, low completion — very similar pattern to SigMap
- MLO-MAE (4.4): novel masking idea but presentation problems and method specification gaps
- Presto (4.75): clean SSL pretraining transformer with reasonable execution

**Comparison:** SigMap has more compelling story than PowerGPT (better ablations, multiple datasets), but worse methodological clarity than Presto (Eq. 11 missing from §3, multiple numerical inconsistencies, contradictory descriptions of fine-tuning targets). It sits between PowerGPT (3.0) and MLO-MAE (4.4)/Presto (4.75).

---

## Summary

SigMap proposes a multi-modal foundation model for wireless localization with two contributions: (1) a "cycle-adaptive" masking strategy for SSL pre-training that aims to disrupt periodic shortcuts in CSI, and (2) a "map-as-prompt" mechanism that converts a 3D scene mesh (via Delaunay triangulation + a 2-layer GCN + mean pooling) into a single learnable prompt token prepended to a pre-trained Transformer at fine-tune time. Experiments on DeepMIMO O1/O2 and WAIR-D report meaningful gains over LWLM/SWiT/CNN/OMP baselines for single-BS, multi-BS, and few-shot transfer scenarios.

## Strengths
- **Map-as-prompt ablation is informative.** Tables 1, 2, and 4 quantify the contribution of the geographic prompt: single-BS MAE drops 2.275→1.564 m, multi-BS 0.789→0.673 m, and a 2-D bird's-eye prompt recovers most (≈82%) of the gain from the full 3-D mesh — useful evidence that the prompt carries topological rather than purely geometric content.
- **Parameter-efficient transfer recipe.** Table 5 shows fine-tuning only ≈0.085 M parameters with the backbone frozen, completing 1000 fine-tune epochs in 30 minutes — a concrete, reproducible efficiency claim grounded in numbers.
- **Reasonable cross-scenario evaluation footprint.** Evaluating zero-shot on both DeepMIMO O2 and WAIR-D (100 scenes) goes beyond the more common single-test-scene setup, even if the analysis is shallow.

## Weaknesses

### Fatal
None — the issues below are real and serious but the core idea (map-as-prompt) and the headline ablation (with/without map across multiple scenarios) are coherent and would survive a revision.

### Major
- **A reportedly key result-producing module (Eq. 11, "NLoS-aware attention") is introduced only in the Results section (§4.2) and is absent from §3.** The single-BS table is credited to this mechanism ("The key advantage stems from our NLoS-aware attention mechanism…"), but the architecture, where the mechanism is inserted, what tokens it attends across in a single-BS configuration, and how it differs from Eq. 9 are never specified. As written, the single-BS result in Table 1 cannot be reproduced from §3, and the method that is evaluated does not match the method that is described.
- **The cycle-adaptive masking procedure is under-specified.** Eq. 6 references `d_final` (a "detected periodicity shift") and a starting offset `j_0`, but the row-wise cross-correlation procedure that yields them is not given. Table 3 compares "grid only," "strip only," and "adaptive" — but since "adaptive" is the union/interleaving of those two, this ablation cannot disentangle "cycle-aware" from "more diverse masking." The motivating claim that prior SSL methods exploit periodic shortcuts is asserted, not demonstrated.
- **Internal inconsistency about what is fine-tuned.** §3.4 explicitly trains θ_gnn, θ_proj, and θ_task during fine-tuning ("the only parameters updated during fine-tuning are those of the GNN, the projection MLP, and the task-specific head"). §4.5 states "only the downstream task heads are fine-tuned… while the self-supervised backbone remains frozen." These cannot both be true. This matters because the "zero-shot / 100-sample transfer" claim hinges on whether the GNN is re-trained on the target scene, frozen, or somewhere in between.

### Minor
- **Numerical inconsistencies that erode trust in the headline numbers.** §4.5 text reports "1.580 m on WAIR-D Scenario-2" while the corresponding table reports 1.880 m. Parameter efficiency is "0.4 %" in §4.5 and "0.7 %" in §4.6. §4.4 directs the reader to "Figure 1" for a side-by-side 2-D/3-D ablation, but Figure 1 is the propagation-paths illustration. With effect sizes claimed to three decimals over 5-run averages, these slips are conspicuous.
- **No variance reporting despite "averaged over 5 independent runs."** Standard deviations / confidence intervals are absent across all tables. With CDF@1m differences sometimes ≤5 percentage points, this is a meaningful omission for reading the ablations.
- **WAIR-D 100-scene aggregate is reported as a single row.** Given WAIR-D is the only genuinely out-of-distribution test of "map-as-prompt," a per-scene or per-geometry breakdown would substantially sharpen the central claim; aggregating into one number is a missed opportunity.
- **Single-token compression of the scene.** A 3D scene's "rich spatial-topological relationships" is compressed via GlobalMeanPool into one D-dimensional prompt token (Algorithm 1, line 10). There is no comparison against multi-token prompt variants, which is the obvious design ablation.

### Trivial
- The single-BS attention mechanism (Eq. 11) and the multi-BS attention (Eq. 9) appear functionally near-identical and should be related explicitly in the text.

## Nice-to-Haves
- One experiment that decouples "geographic prompt as method" from "geographic prompt as the generator of the test signal" — e.g., perturbing or partially corrupting the map at test time and observing graceful degradation, or evaluating on measured (non-ray-traced) CSI. This would convert the marquee "w/ map vs. w/o map" comparison into a causal test of the conditioning mechanism. This is currently in the "nice-to-have" tier because the cross-dataset (O2, WAIR-D) results partially address it.
- A probing/interpretability analysis that ties the prompt to LoS/NLoS decomposition as §2.2 claims, since the paper currently makes that claim implicitly.
- A map-aware baseline (e.g., a fingerprinting/geometric hybrid that also consumes the map) so the comparison isn't between map-aware SigMap and map-blind everyone else.

## Removed Points
*These points were flagged for removal — treat them with caution.*

- **"Synthetic-to-synthetic with information channel concern" framed as evidential-fatal.** The harsh critic argues that because the map M deterministically generates H_CSI via ray-tracing, supplying M at test time means the model is given the generator of its test signal. This is a legitimate concern in spirit, but it is partially addressed by the WAIR-D evaluation (different map, different scenes, only ~100 fine-tune samples) and would require external information (measured CSI) to fully resolve. Demoted to a Nice-to-Have above rather than a Major.
- **Critique that map-as-prompt benefits are "really just 2D."** The harsh critic argues Table 4 shows ~82% of map gain comes from 2D, only ~18% from 3D — true, but the paper itself acknowledges this ("near-overlapping error bars indicate that most of the topological benefit is retained even without vertical detail"). Already addressed.
- **Strength about "strong zero-shot generalisation."** The Strength Finder frames the WAIR-D / O2 results as "zero-shot," but the paper explicitly fine-tunes on ~100 samples per target scene, so this is few-shot, not zero-shot. Demoted; the underlying result is real, but the framing in the Strength Finder over-claims.
- **Strength about "attention-based multi-BS fusion."** Standard learned-attention pooling over BS [CLS] tokens; not a distinctive contribution on its own merits.

## Novel Insights
None beyond the paper's own contributions. The framing of a 3D map as a soft prompt over a CSI foundation model is genuinely interesting, but the reviewers (and the paper) do not surface analysis that goes beyond the headline ablations.

## Suggestions
1. Move Eq. 11 and the architectural description of the "NLoS-aware attention" into §3 with a clear specification of how it differs from Eq. 9.
2. Fully specify the periodicity-detection procedure (the row-wise cross-correlation that yields `d_final`, `j_0`) and add at least one baseline against standard random/MAE-style masking.
3. Reconcile §3.4 and §4.5 explicitly: state whether θ_gnn and θ_proj are retrained on the target scene's 100 samples, frozen from O1_3p5, or partially retrained.
4. Fix the inconsistent numbers (WAIR-D 1.580 vs 1.880; 0.4% vs 0.7%) and the "Figure 1" reference in §4.4. Add standard deviations across the 5 runs to all main tables.
5. Add a per-scene breakdown on WAIR-D and at least one map-perturbation experiment to convert the "w/ map vs. w/o map" comparison into a causal test.

## Axis evaluation
- **Originality:** Reasonable — casting a 3D map as a learnable prompt over a CSI foundation model is a defensible angle on a crowded space, even if individual ingredients (GCN + prompt tuning + masked SSL) are off-the-shelf.
- **Importance of question:** High — robust cross-scenario wireless localization matters for 5G/6G applications.
- **Soundness of claims:** Weak — a result-producing component is described only in the results; cycle-adaptive masking lacks the comparison that would isolate "cycle-aware" from "more diverse"; "fine-tuned components" descriptions contradict between §3.4 and §4.5.
- **Soundness of experiments:** Mixed — the ablation footprint is reasonable, but no variance estimates and multiple numeric inconsistencies make headline magnitudes hard to trust.
- **Clarity:** Below bar for a method paper — the central method does not match what is evaluated; reference errors and inconsistent statistics throughout.
- **Value to community:** Moderate — the map-as-prompt idea is publishable in principle, but the execution would need to be tightened substantially before the community can build on the specific numbers reported.

## Anchor table
| Path | Avg | Round | Comparison to SigMap |
|---|---|---|---|
| XhdckVyXKg.md (NormWear wearable FM) | 3.00 | R1 weak | Both claim foundation-model framing without sufficient validation; SigMap is similar but has slightly more ablation breadth |
| ntSP0bzr8Y.md (PowerGPT) | 3.00 | R1 weak | Very similar pattern: foundation-model framing + multiple referencing errors + completion-level issues |
| 7zJDTnogdG.md (ECG FM) | 3.33 | R1 weak | Both signal-domain SSL FMs; SigMap more concrete on application but with method-spec gaps |
| LqB8cRuBua.md (Diffusion SigFormer) | 2.00 | R1 weak | Substantially weaker than SigMap |
| 9TClCDZXeh.md (Wireless GA Transformer) | 7.00 | R1 mid | Much stronger — clean math, clean evaluation; SigMap below |
| 29JDZxRgPZ.md (EM-GANSim) | 6.00 | R1 mid | Cleaner method spec than SigMap but with its own gaps; SigMap below |
| 7KDuQPrAF3.md (FM for ECC) | 6.25 | R1 mid | Cleaner contribution than SigMap |
| NPNUHgHF2w.md (CBraMod EEG) | 6.75 | R1 mid | Cleaner contribution than SigMap |
| 9pW2J49flQ, bWcnvZ3qMb, OvoCm1gGhN, vrBVFXwAmi | 8.00 | R1 strong | Off-topic strong anchors; not used |
| Iip7rt9UL3.md (Presto) | 4.75 | R2 narrow | Cleaner SSL story; SigMap below due to internal inconsistencies |
| KJ1w6MzVZw.md (Cross-domain TS FM) | 3.80 | R2 narrow | Comparable foundation-model framing with weak validation; SigMap close |
| 0JcPJ0CLbx.md (Revisit MAE 3D med) | 3.75 | R2 narrow | Comparable execution quality |
| oVZ9XaOSFK.md (MLO-MAE) | 4.40 | R2 narrow | Novel masking idea but with presentation problems; SigMap below due to undefined Eq. 11 |
| ax4ZOytBV2.md (Multi-modal prompt GNN) | 4.50 | R2 narrow | Comparable graph-prompt setup; SigMap close on average |
| 92vMaHotTM.md (Edge prompt tuning GNN) | 5.50 | R2 narrow | Cleaner graph prompt-tuning contribution; SigMap below |
| nFcgay1Yo9.md (Scale-Free GLM) | 5.75 | R2 narrow | Cleaner contribution |
| kSBIEkHzon.md (Graph FM via task-trees) | 5.25 | R2 narrow | Comparable framing; SigMap below |

**Round 1 bracket:** 3–5, anchored by PowerGPT (3.0) at the low end and EM-GANSim (6.0) at the high end.
**Round 2 narrowing:** SigMap is most similar to PowerGPT (3.0), Cross-domain TS FM (3.80), and MLO-MAE (4.4). Its experimental footprint is slightly better than PowerGPT but its method-spec gaps and inconsistencies are worse than MLO-MAE. Final placement around 3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>