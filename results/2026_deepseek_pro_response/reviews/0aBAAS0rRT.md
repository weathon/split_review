Now I have a clear picture. Let me finalize the review and assign a score.

**Bracket**: Round 1 placed SigMap in **4.0-6.0**. Round 2 narrowed this: LPTM (3.80) is clearly worse — it has similar issues plus missing baselines and unclear notation, but no novel architectural contribution like map-as-prompt. DASFormer (5.25) and VLM-Promptable-RL (5.50) are somewhat better — their methodologies are at least coherent even if their evaluations are limited. SigMap's phantom NLoS attention mechanism is a more fundamental coherence problem that neither of those papers has. SigMap is worse than DASFormer (5.25) but better than LPTM (3.80), landing at **~4.5**.

---

## Summary
This paper proposes SigMap, a two-stage foundation model for wireless localization. In pre-training, a transformer backbone is trained via masked autoencoding with "cycle-adaptive masking" designed to prevent models from exploiting periodic shortcuts in CSI data. In fine-tuning, a GNN encodes a 3D building map into a single prompt token prepended to the frozen transformer, enabling parameter-efficient adaptation. The method is evaluated on DeepMIMO ray-tracing simulations and WAIR-D, showing improvements over several baselines.

## Strengths
- **Physically grounded problem formulation**: Section 2 derives the CSI decomposition into LoS/NLoS components (Eq. 1) and links multipath geometry to the localization objective (Eq. 3), providing principled motivation for why map-conditioned prompts should help resolve multipath ambiguity.
- **Concrete parameter efficiency evidence**: Table 5 reports 11.73M pre-trained parameters with only 0.085M (0.7%) updated during fine-tuning, with 30-minute fine-tuning and 0.83ms inference, supporting deployability claims.
- **Informative map modality ablation**: Table 4 compares 3D map (MAE 1.564m), 2D bird's-eye (1.692m), and no-map (2.275m) for single-BS localization, revealing that a 2D view retains ~92% of the 3D benefit — a practically useful finding since 2D maps are widely available.
- **Cross-scenario generalization evidence**: Table 4.5 tests on two unseen environments (DeepMIMO O2 and WAIR-D Scenario-2 with 100 real-world city layouts), showing SIGMAP with map outperforming LWLM by 53.2% and 44.3% respectively using only ~100 fine-tuning samples.
- **Well-motivated masking problem diagnosis**: The observation that standard random/grid masking allows models to exploit periodic CSI structure is specific to wireless signals and non-obvious from vision/NLP SSL literature.

## Weaknesses

### Major
- **NLoS-aware attention mechanism (Eq. 11) is invoked as the key performance driver in Section 4.2 but is entirely absent from the methodology (Section 3).** Section 4.2 states that SIGMAP's single-BS advantage "stems from our NLoS-aware attention mechanism that explicitly models multi-path propagation" and presents Eq. (11) as the core formulation. However, Section 3 describes only a standard ViT-style transformer with self-attention (Q, K, V); there is no mention of any NLoS-specific attention mechanism. The symbols `o_s`, `φ`, and `W_NLoS` used in Eq. (11) are never defined. Either the mechanism exists and is undocumented, or it was introduced post-hoc in the results narrative. Either way, the reader cannot determine what the model actually is, making the central architectural claim unevaluable.

- **"Zero-shot generalization" claim in the abstract and contributions contradicts the experimental protocol.** The abstract promises "strong zero-shot generalization in unseen environments" and Contribution 3 repeats this. Section 4.5 then describes fine-tuning task heads with approximately 100 labeled target samples per scenario — explicitly characterized as a "few-shot learning setup." This is not zero-shot generalization, and the claim overstates what was demonstrated.

- **Main evaluation is in-distribution, leaving the value of pre-training untested.** Section 4.1 states that DeepMIMO O1_3p5 is used "for both pre-training and fine-tuning" in the main results (Tables 1-2). Since pre-training and evaluation draw from the same simulated environment, a model trained from scratch on the same labeled data might perform comparably. No such baseline is included, so the core claim that pre-training adds value over supervised learning is not validated for the main results.

- **Cycle-adaptive masking is described at an insufficient level of detail for reproducibility.** This is one of the paper's two core methodological contributions. The description states that shift patterns are computed "using cross-correlation analysis" (line 133) but never specifies: (a) what signals are cross-correlated, (b) how the dominant periodicity is extracted from the cross-correlation output, or (c) how the parameter `d_final` in Eq. (6) is derived. Eq. (6) itself merely describes a diagonal shift mask that could be implemented without any periodicity detection. Without these details, the method cannot be reproduced.

### Minor
- **Numerical discrepancies between text and tables.** The prose in Section 4.5 reports 1.580 m MAE for WAIR-D Scenario-2, but the corresponding table reports 1.880 m — a 0.3 m difference. The prose also claims "updating only 0.4% of parameters" while Table 5 and Section 4.6 report 0.7%. These inconsistencies erode confidence in the reported numbers.

- **No variance reported despite stating results are averaged over 5 independent runs.** For localization errors where method differences can be a few tenths of a meter, the reader cannot assess whether reported rankings are statistically stable.

- **Architecture-only gains over the strongest baseline are narrow.** SIGMAP (w/o map) vs. LWLM yields MAE improvements of only 4.5% for single-BS (2.275 vs. 2.382 m) and 4.7% for multi-BS (0.789 vs. 0.828 m). Without variance estimates, it is unclear whether these margins are significant, and the bulk of SIGMAP's advantage comes from the map modality rather than the architectural innovations.

- **Masking ablation (Table 3) omits a random-masking or no-masking baseline.** Only grid, strip, and adaptive masking are compared, so it is unclear whether any structured masking is necessary.

- **Generalization experiments (Section 4.5) compare only against LWLM.** SWiT, CNN, and OMP — present in the main results — are absent, weakening the breadth of the generalization claim.

- **Radar chart (Figure 5) has undefined axes.** Terms like "AoA," "ToA," "NLoS," and "oss_scenario" are not explained as evaluation dimensions, making the chart uninterpretable.

## Nice-to-Haves
- The single global prompt vector design (compressing the entire spatial configuration into one token) could be discussed — why not per-BS prompts or spatially distributed prompt tokens?
- A discussion of when the map-as-prompt approach might fail (e.g., inaccurate/outdated maps, rural environments without constraining geometry) would strengthen the paper.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "baseline comparisons do not control for access to map information" as a fatal flaw.** The paper includes SIGMAP (w/o map) as the proper ablation control. The narrow gains over LWLM are noted as a Minor weakness instead.
- **Harsh Critic point about "existing SSL methods ignore cyclic patterns" stated without citation.** This is a research gap framing statement in Section 1.1, not a factual claim requiring citation. Removed as a nitpick.
- **Harsh Critic claim about multipath enabling rough positioning being "debatable."** This is a background statement setting up motivation, not a central claim. Removed as scope creep.
- **Strength Finder claim about Delaunay triangulation being "geometrically principled."** While true, Delaunay triangulation is a standard spatial graph construction technique; calling it a strength oversells a routine design choice. Removed as superficial.
- **Strength Finder claim about multi-BS attention being "interpretable."** The attention mechanism (Eqs. 9-10) is standard learned attention; calling it interpretable is overselling. Removed.

## Novel Insights
The map modality ablation (Table 4) — showing that a 2D bird's-eye view retains 92% of the full 3D map benefit — is a genuinely useful empirical finding. It suggests that the primary value of geographic prompting comes from topological / line-of-sight cues rather than precise 3D geometry, with practical implications for deployment using widely available 2D map data instead of expensive 3D meshes.

## Suggestions
- Resolve the NLoS attention mechanism's status: either integrate it into Section 3 with full description, motivation, and ablation, or remove Eq. (11) from Section 4.2 if it is not actually part of the model.
- Replace "zero-shot generalization" with "few-shot generalization" throughout.
- Add a "trained from scratch on labeled data" baseline for the main DeepMIMO O1 results to test whether pre-training adds value.
- Report standard deviations for all tables.
- Fix the numerical discrepancies (1.580 vs. 1.880; 0.4% vs. 0.7%).
- Provide algorithmic detail for cycle-adaptive masking sufficient for reproduction.
- Include random-masking and no-masking baselines in Table 3.
- Include all baselines from the main results in the generalization experiments (Section 4.5).

## Anchor Comparisons
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| LPTM (cross-domain time series) | 3.80 | R2 | SigMap has a more novel contribution (map-as-prompt) and better experimental structure overall |
| DASFormer (SSL for seismic) | 5.25 | R1 | DASFormer's methodology is at least internally coherent; SigMap's phantom NLoS mechanism is a worse problem |
| VLM Promptable Reps for RL | 5.50 | R2 | Similar evaluation limitations but VLM-PR's methodology is coherent; SigMap has a structural coherence issue |
| Foundation Models + Hypernetworks | 5.50 | R2 | Accepted despite modest novelty due to thorough evaluation; SigMap's idea is more novel but execution is worse |
| Wi-GATr (wireless geometric transformer) | 7.00 | R1 | Clearly stronger: well-described methodology, diverse evaluation, real-world validation, no coherence problems |

**Round 1 bracket**: 4.0–6.0. Round 2 narrowed this to ~4.5 — SigMap is better than LPTM (3.80) but worse than DASFormer (5.25) due to the NLoS mechanism coherence problem, zero-shot overclaim, and numerical errors.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>