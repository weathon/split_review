Here is my consolidated final review.

---

## Summary

SigMap proposes a multimodal foundation model for wireless localization that combines (1) a cycle-adaptive masking strategy for self-supervised pre-training on CSI data, and (2) a "map-as-prompt" framework that encodes 3D building geometry via a GNN and prepends the representation as a soft prompt to a transformer backbone during fine-tuning. Experiments on DeepMIMO and WAIR-D datasets show that the full model (CSI + map prompt) achieves MAEs of 1.564 m (single-BS) and 0.673 m (multi-BS), outperforming signal-only baselines, while fine-tuning only 0.7 % of total parameters.

## Strengths

- **Map-as-prompt design is a clean and principled contribution.** Encoding 3D building geometry via Delaunay triangulation + GCN and injecting it as a prepended soft prompt into a frozen transformer backbone is a well-motivated, parameter-efficient architecture for multimodal signal-geometry fusion. The ablation in Table 4 (3-D mesh → 2-D birdview → no-map) cleanly isolates the map-derived gains: MAE improves from 2.275 m to 1.564 m with a 3-D map, and even a 2-D birdview retains most of the benefit (1.692 m), indicating the prompt mechanism robustly captures topological/LoS cues.

- **Consistent empirical gains across tasks and datasets.** In multi-BS collaborative localization (Table 2), SigMap with map achieves 0.673 m MAE and 84.5 % CDF@1 m, improving over SigMap w/o map (0.789 m, 77.5 %) and the best baseline LWLM (0.828 m, 75.6 %). These gains replicate across single-BS, DeepMIMO O2, and WAIR-D Scenario-2, and the map prompt consistently provides additional improvement over the no-map variant.

- **Parameter efficiency is clearly demonstrated.** Fine-tuning updates only 0.085 M parameters (0.7 % of total) and completes in 30 minutes; inference is 0.83 ms per sample. These numbers are concrete and well-documented.

- **Cycle-adaptive masking shows measurable benefit on key metrics.** Adaptive masking achieves 0.673 m MAE and 84.5 % CDF@1 m vs. 0.753 m/75.3 % for strip-masking and 0.770 m/80.3 % for grid-masking (Table 3), supporting the claim that disrupting periodic shortcuts yields better feature learning on the primary accuracy metric.

## Weaknesses

### Major

- **Headline comparisons pit a map-augmented method against signal-only baselines.** Tables 1 and 2 compare SigMap "w/ map" (which receives 3-D building geometry) against OMP, CNN, SWiT, and LWLM — none of which have access to any map data. The SigMap "w/o map" ablation (same backbone, no map) roughly matches or slightly exceeds the best baseline (e.g., 2.275 m vs. 2.382 m MAE single-BS; 0.789 m vs. 0.828 m multi-BS), so the headline gap is largely attributable to the extra map modality rather than a superior learning mechanism on the signal alone. To substantiate the claim that the map-prompt mechanism itself advances the state of the art, the paper needs to compare against map-aware localization methods (or adapt baselines to ingest the same 3-D map features). Without this, the evaluation design cannot cleanly support the "state-of-the-art" conclusion drawn for the full multimodal system.

- **The NLoS-aware attention mechanism (Eq. 11) appears in Section 4.2 with no prior description in the methodology.** The paper states "The key advantage stems from our NLoS-aware attention mechanism that explicitly models multi-path propagation" and gives Eq. 11, but this mechanism is never introduced in Section 3 (Methodology). The notation \( \mathbf{o}_s^{(i)} \) and \( \mathbf{W}_{\text{NLoS}} \) are not defined in the main text, and it is unclear whether this is part of the geographic prompt, a separate architectural component, or a post-hoc analysis tool. This gap undermines reproducibility and confuses what the "key advantage" actually is.

### Minor

- **"Zero-shot" generalization is mislabeled.** The abstract and contributions section claim "strong zero-shot generalization in unseen environments," but Section 4.5 fine-tunes task heads on approximately 100 labeled target samples per scenario — this is few-shot learning. The paper itself uses the phrase "this few-shot learning setup" on line 329, contradicting its own high-level claims. The results are still impressive given only 100 samples, but the framing should be corrected.

- **Cycle-adaptive masking results are mixed and lack analysis.** Adaptive masking achieves better MAE (0.673 m vs. 0.753 m) and CDF@1 m (84.5 % vs. 75.3 %) than strip-masking, but *worse* RMSE (1.099 m vs. 0.972 m). The paper offers no explanation for this RMSE regression, no analysis of why the masking matters (e.g., attention maps, reconstruction quality, or evidence that periodic shortcuts are actually suppressed), and no statistical significance tests. The central methodological innovation needs stronger empirical support.

- **Inconsistent numerical reporting.** The WAIR-D Scenario-2 MAE for SigMap w/ map is listed as **1.880 m** in the table (line 348) but as **1.580 m** in the body text (line 352). These numbers differ by 0.3 m, which is a non-trivial discrepancy.

- **How the dominant periodicity \( d_{\text{final}} \) is computed from cross-correlation is not specified.** Equation (6) depends on \( d_{\text{final}} \) as the "detected periodicity shift," but the paper never describes the cross-correlation procedure used to obtain it. This makes the core masking strategy irreproducible from the main text alone.

- **No variance or confidence intervals reported.** The paper states results are averaged over 5 independent runs but provides no standard deviations, confidence intervals, or error bars in any of the main results tables (Tables 1, 2, 3). This makes it impossible to assess the statistical significance of the reported improvements.

### Trivial

- **Figure reference error in Section 4.4:** The text says "Two-dimensional and three-dimensional map ablations are illustrated side-by-side in Figure 1," but Figure 1 shows propagation paths, not map modality ablations. This appears to be a cross-reference mistake.

- **Radar chart metric "oss_scenario" is never defined.** The term appears only in the Figure 5 caption.

## Nice-to-Haves

- Comparing against map-aware baselines (e.g., an MLP that concatenates distance-to-building or LoS flags with CSI) would cleanly isolate the benefit of the GNN-based prompt mechanism.
- Visualizing learned attention on the geographic prompt token across spatial locations would strengthen the claim of "interpretable fusion."
- A true zero-shot experiment (no fine-tuning, just pre-trained backbone + map prompt) would substantiate the generalization claims.

## Removed Points

These points were flagged by the reviewers but are removed for the following reasons:

- **Criticism about street-level photograph speculation:** The harsh critic noted the paper speculates about using street-level photos with no data. This is clearly labeled as future work by the paper itself, not a claimed contribution. **Removed.**
- **Criticism about GNN being retrained per environment making parameter efficiency misleading:** The paper transparently reports that θ_gnn, θ_proj, and θ_task are all fine-tuned (0.085 M params, 30 min). This is still genuinely efficient. **Removed — overstates the issue.**
- **Criticism about missing comparison with CrowdBERT and signal-guided MAE:** The paper cites these as related work but does not compare against them. Valid in principle, but the meta-reviewer cannot assess code availability or experimental compatibility across these works. **Moved here — peripheral to core claims.**
- **Strength Finder claim about "strong zero-shot generalization":** Since the experiment is few-shot, not zero-shot, this strength conflicts with a verified weakness (see above). **Moved here.**
- **Criticism about "physics-informed" claims lacking theoretical analysis:** The paper does not repeatedly claim "physics-informed" — the phrase barely appears. The critic overstates this. **Removed.**
- **Criticism about "missing real-world evaluation":** Requesting a real-world dataset as a necessity goes beyond the paper's stated scope (simulated ray-tracing evaluation is standard for this line of work). **Removed — scope creep.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension not discussed in the paper: the map-as-prompt mechanism achieves most of its gain from relatively coarse topological/LoS cues (even a 2-D birdview retains ~92 % of the MAE improvement over no-map), which raises the question of whether the full 3-D GCN encoding is necessary or whether a simpler geometric featurization would suffice. The paper's own data suggest an interesting research direction — lightweight proxies for 3-D maps — that the authors note as future work but do not explore.

## Suggestions

1. **Fix the zero-shot framing** throughout the paper (abstract, contributions, and conclusion) to accurately say "few-shot" or "minimal-shot" generalization with ~100 labeled samples.
2. **Add map-aware baselines** — at minimum, an MLP that processes hand-crafted map features (distance to nearest building, LoS probability per BS) concatenated with CSI to control for the extra modality.
3. **Explain the \( d_{\text{final}} \) computation** from cross-correlation to make the masking strategy reproducible.
4. **Clarify the role of Eq. (11)** — is it part of the prompt mechanism, a separate attention layer, or an analysis tool? If it is a core component, move it to Section 3.
5. **Resolve the WAIR-D number inconsistency** (1.880 m vs. 1.580 m).
6. **Add variance statistics** (std or 95 % CI) to the main results tables since results are averaged over 5 runs.
7. **Provide analysis for the cycle-adaptive masking** — explain why RMSE worsens despite MAE/CDF improvement, and add qualitative evidence (attention maps or reconstruction visualizations) that periodic shortcuts are suppressed.

## Score and Decision

The paper introduces a genuinely novel architecture (map-as-prompt via GNN encoding of 3-D geometry) and demonstrates consistent gains across multiple tasks and datasets with impressive parameter efficiency. However, the evaluation design conflates the value of the map modality with the value of the learning mechanism, the central masking innovation has incomplete empirical support, and the paper over-claims (zero-shot → few-shot). These are addressable weaknesses, but they weaken the submission in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>