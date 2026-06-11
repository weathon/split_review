Now I have enough comparison anchors. Let me synthesize everything into the final review.

**Comparison summary:**
- **WiMTR (4.00)**: CSI-based wireless sensing paper. Our paper is stronger — better ablations, cross-scenario evaluation.
- **Conditional MAE (4.75)**: Masking strategy paper. Cleaner execution but limited novelty. Our paper has more domain-specific novelty but worse coherence issues.
- **PointHDMAE (5.20)**: Domain-specific MAE with novel pre-training. Cleaner than ours, fewer fundamental issues.
- **SleepSMC (5.75)**: Accepted paper with solid methodology. Our paper is clearly below this.

Our paper sits around **4.0** — the three Major weaknesses (undefined NLoS attention, zero-shot misrepresentation, under-specified core algorithm) prevent it from reaching the 4.75-5.20 range, but its genuine contributions (cycle-adaptive masking, map-as-prompt, cross-scenario results) keep it above the 3.0-3.5 range of papers with fundamental technical errors.

---

## Summary
This paper proposes SigMap, a wireless localization model combining (1) cycle-adaptive masked pre-training on CSI data to prevent periodic shortcut learning, and (2) a geographic prompt tuning mechanism that encodes 3D environment maps via GNNs into soft prompt tokens for parameter-efficient cross-scenario adaptation. Experiments on DeepMIMO and WAIR-D show improvements over several baselines, particularly in multi-BS settings and cross-scenario transfer.

## Strengths
- **Cycle-adaptive masking addresses a real domain-specific challenge**: The identification that CSI data contains exploitable periodicities that standard random masking fails to disrupt is well-motivated, and the proposed shift-aware masking (Eq. 6) provides a principled countermeasure. The ablation in Table 3 shows adaptive masking achieving 0.673m MAE and 84.5% CDF@1m vs. 0.770m/80.3% for grid masking, confirming the benefit over fixed patterns.
- **Map-as-prompt GNN encoding is a clean, parameter-efficient design**: Encoding 3D building meshes and BS positions into a heterogeneous graph via Delaunay triangulation, processing through a 2-layer GCN, and projecting to a single prompt token (Algorithm 1) is a sensible approach. Table 4 isolates the contribution: 3D map achieves 1.564m MAE vs. 2.275m without map — a 45% degradation that demonstrates map conditioning is not marginal.
- **Cross-scenario generalization with frozen backbone**: Section 4.5 evaluates on two unseen environments (DeepMIMO O2, WAIR-D Scenario-2 with 100 real-world city scenes) using only ~100 fine-tuning samples while keeping the backbone frozen. Results (1.026m MAE on O2, 1.880m on WAIR-D) show substantial improvements over LWLM, providing evidence that the pre-trained representations transfer across environments.
- **Parameter efficiency is concretely demonstrated**: Table 5 shows fine-tuning trains only 0.085M parameters (0.7% of 11.730M total) in 30 minutes with 0.83ms/sample inference latency.

## Weaknesses

### Fatal
None.

### Major
- **Undefined NLoS-aware attention mechanism invoked as "key advantage" (Eq. 11)**: Section 4.2 introduces Eq. (11) with symbols `o_s^(i)`, `W_{NLoS}`, and `φ` and states "The key advantage stems from our NLoS-aware attention mechanism that explicitly models multi-path propagation." These symbols and this mechanism appear nowhere in Section 3 (Methodology). The methodology defines a standard transformer backbone, cycle-adaptive masking, GNN-based prompt generation, and task-specific MLP heads — plus multi-BS attention fusion (Eqs. 9–10) — but contains no NLoS-aware attention component. A `grep` of the full paper confirms `o_s` and `W_{NLoS}` appear only in Eq. (11). This means either (a) a mechanism the paper credits as central to its results is absent from the method description, making the paper unreproducible, or (b) Eq. (11) is a post-hoc explanatory device that does not correspond to the actual model. Either way, the chain of reasoning between model design and results is broken at a point the paper itself identifies as critical.
- **"Zero-shot" claim contradicts the experimental protocol**: The abstract claims "strong zero-shot generalization in unseen environments" and Contribution 3 claims "strong zero-shot generalization to unseen environments and base station configurations." Section 4.5 then describes fine-tuning with "approximately 100 instances per scenario." Using 100 target-domain training samples makes this few-shot transfer learning, not zero-shot generalization. The distinction matters: zero-shot implies no target-domain training at all. The paper's framing overstates the contribution.
- **Cycle-adaptive masking algorithm is under-specified at its core**: Section 3.3 states that "we compute shift patterns using cross-correlation analysis" to determine `d_final` (the periodicity shift in Eq. 6) but never specifies: which signals are cross-correlated, over what lag range, how the dominant periodicity is selected from the correlation output, or how `d_final` is derived. This is the central technical novelty of the pre-training stage, and the description remains at a high-level intuition without algorithmic detail needed for reproduction.

### Minor
- **GCN update rule inconsistent between Algorithm 1 and text**: Algorithm 1 (line 165) uses a GraphSAGE-style update with separate self-loop weights `W^(l)` and neighbor-aggregation weights `U^(l)`. The accompanying text equation (after line 189) describes the standard Kipf & Welling GCN with symmetric normalization `D̃^{-1/2} Ã D̃^{-1/2}`. These are different parameterizations. This appears to be a writing inconsistency rather than a methodological error, but it reflects carelessness.
- **"Interpretable fusion" claimed but never demonstrated**: Contribution 2 claims map prompts "enable interpretable fusion of environmental constraints," but the paper provides no attention maps, no probing of what the prompt encodes, and no analysis of which environmental features the model uses. The entire 3D map is compressed into a single vector via global mean pooling, discarding spatial resolution. The interpretability claim is unsubstantiated.
- **Strip masking achieves best RMSE in the masking ablation without acknowledgment**: In Table 3, strip masking achieves RMSE 0.972m vs. adaptive masking's 1.099m, yet the paper declares adaptive masking the "best trade-off" without discussing this inversion. A practitioner optimizing for worst-case error might prefer strip masking.
- **Pre-training on a single scenario weakens "foundation model" framing**: The paper pre-trains exclusively on DeepMIMO O1_3p5, yet uses "foundation model" language that conventionally implies broad pre-training across diverse data distributions.

### Trivial
- **Numerical error in Section 4.5 text**: The text states SIGMAP achieves "1.580 m on WAIR-D Scenario-2" while Table 4.5 reports 1.880 m. The percentage improvement (44.3%) matches 1.880, confirming 1.580 is a typo.
- **Figure 5 radar chart includes undefined metrics and methods**: The chart axes reference "AoA," "ToA," "NLoS," "oss_scenario," and method "CMP" — none of which are defined or discussed in the evaluation protocol. The figure appears generated for a different or expanded evaluation.

## Nice-to-Haves
- No standard deviations or confidence intervals are reported despite results being "averaged over 5 independent runs." Error bars would clarify whether the modest gaps between some methods are statistically meaningful.
- The transformer backbone architecture (number of layers, hidden dimension, number of heads, sequence length) is deferred entirely to an appendix. Core architecture details should be summarized in the main text.
- A random-masking baseline in the masking ablation (Table 3) would better isolate whether the claimed periodicity-shortcut problem is real — currently the ablation only compares against structured patterns (grid, strip).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **RMSE pattern inversion claim for main method**: The Harsh Critic claimed LWLM beats SIGMAP on RMSE in Tables 1-2 and that the paper selectively reports metrics. Verified against the paper: SIGMAP (w/ map) beats LWLM on RMSE in both tables (5.675 vs. 5.822 in Table 1; 1.099 vs. 1.178 in Table 2). The RMSE inversion only occurs for the w/o map ablation, not the main method. The paper's main method wins on all three metrics. Removed as factually incorrect when applied to the main method.
- **Missing map-augmented baselines**: The Harsh Critic notes absence of methods that also use map information. However, no specific map-augmented baselines are cited as having been omitted, and the paper includes SIGMAP w/o map as a direct ablation. Removed as speculative without specific citations.
- **Missing appendix concerns**: The parser strips appendices from all papers; any criticism about missing details in an appendix is removed per protocol (applies to backbone architecture details, dataset configuration, CDF curves referenced as "B.5").
- **Pure formatting/style/typographical nits**: All removed as parser artifacts.

## Novel Insights
The paper's approach of using GNN-encoded 3D maps as soft prompts (rather than as input features or conditioning signals) for a frozen pre-trained signal backbone is a genuinely interesting design pattern. It suggests that explicit geometric graph encodings could serve as prompt-like conditioning for other domains where spatial constraints are known but traditionally concatenated or injected via cross-attention.

## Suggestions
- Either define the NLoS-aware attention mechanism fully in the methodology and demonstrate it is part of the actual model, or remove Eq. (11) and the associated claim from Section 4.2. The multi-BS attention fusion (Eqs. 9–10) already provides a legitimate attention mechanism.
- Replace "zero-shot" with "few-shot" throughout, or clearly distinguish that the backbone is frozen (zero-shot) while task heads are few-shot adapted. The current framing is misleading.
- Specify the cross-correlation algorithm for periodicity detection: which CSI dimensions, lag range, peak selection criterion, and derivation of `d_final`.
- Add an analysis of what the geographic prompt encodes (e.g., via probing classifiers or attention visualization) to support the interpretability claim, or drop the claim.
- Resolve the Algorithm 1 / text GCN inconsistency.

## Score and Decision

**Anchor comparison (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| WiMTR (q3WzT2mrhB) — WiFi CSI mesh regression | 4.00 | R1 | Our paper is stronger: better ablations, cross-scenario evaluation |
| Conditional MAE (JfcLYCqOkQ) — multi-shot masking study | 4.75 | R2 | Our paper has more domain-specific novelty but worse coherence issues (undefined mechanism, overclaiming) |
| PointHDMAE (KJkbmBcZRx) — hybrid-domain point cloud MAE | 5.20 | R2 | Our paper is weaker: PointHDMAE has cleaner execution, no undefined components |
| SleepSMC (B5VEi5d3p2) — multimodal sleep staging | 5.75 | R1 | Our paper is clearly weaker: SleepSMC has more thorough evaluation and no coherence issues |
| MLO-MAE (oVZ9XaOSFK) — downstream-guided masking | 4.40 | R2 | Comparable to our paper in ambition and execution level |

**Round 1 bracket**: The paper falls between WiMTR (4.00) and SleepSMC (5.75), narrowed to approximately 4.0–5.5.

**Round 2 narrowing**: Within this bracket, the paper is closer to Conditional MAE (4.75) and MLO-MAE (4.40) but has more serious coherence problems than either. The three Major weaknesses — an undefined mechanism invoked as the "key advantage," a zero-shot/few-shot misrepresentation, and an under-specified core algorithm — are concrete, verifiable issues that undermine confidence in the paper's central claims and reproducibility. The paper is weaker than Conditional MAE (4.75) due to these coherence gaps, but stronger than WiMTR (4.00) due to more extensive experiments and cross-scenario evaluation.

**Final score: 4.0.**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>