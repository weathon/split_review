Now I have sufficient calibration context. Let me produce the final consolidated review.

**Round 1 Bracket:** Based on the calibration search, the EAC paper (FRzCIlkM7I, 6.75) is the most directly comparable anchor — same subfield (continual ST forecasting with prompts), same baselines. Weak anchors (<3.5) are clearly below this paper's quality. Strong anchors (>7.5) are top-tier accepted papers that don't have the attribution and control issues this paper has. My initial bracket is **5.0–7.0**.

**Round 2 Narrowing:** The EAC paper (6.75) received scores of 3, 8, 8, 8. The STBP paper has stronger empirical results (21% MAE reduction vs EAC) but faces more significant attribution issues (backbone-only variant beating EAC without any continual learning). FreeDyG (6.75, 8/6/8/5) and FreDF (7.0, 8/6/8/6) represent frequency-domain contributions in related areas but without the attribution ambiguity. Compared to these, STBP's empirical demonstration is stronger but its causal attribution is weaker. The missing controls (per-period results, pattern bank vs EAC on same backbone) would likely prevent it from reaching the 6.75–7.0 range. I place it around **6.0**.

---

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a general-purpose backbone (FreNet for frequency-domain temporal modeling, DLGA for linear-complexity graph attention) with a contextual pattern bank (three groups of trainable prompts expanded incrementally on a frozen backbone). On three real-world benchmarks, STBP achieves substantial improvements: 21% MAE reduction on traffic datasets and 2.35% on an air-quality dataset over the best CSTF baseline (EAC). The paper is well-engineered and the empirical results are strong, but the attribution of gains between the backbone and the continual learning mechanism is not fully disentangled.

## Strengths

- **Dual-stream linear graph attention (DLGA) with O(N) complexity.** DLGA (Eq. 7–9) combines random-feature-map linear attention with the pattern bank as an additional key stream, reducing spatial complexity from O(N²) to O(N) while incorporating prompt knowledge. The ablation (Fig. 4) shows substantial degradation when DLGA is removed (MAE increases from ~15 to ~25 on PEMS-Stream), and the toy-dataset experiment (Fig. 8, third plot) verifies the memory scaling advantage.

- **Frequency-domain network (FreNet) addressing distributional drift.** FreNet (Eq. 6) applies FFT with a learnable frequency embedding to extract stable periodic/trend components, targeting distributional drift that prior CSTF backbones (CNN+GCN) do not explicitly handle. The "w/o Backbone" ablation (replacing FreNet+DLGA with CNN+GCN) incurs large error increases on all three datasets, confirming FreNet's importance.

- **Substantial and consistent empirical improvement.** STBP outperforms all baselines across three datasets and multiple horizons (Table 1), with an especially large margin on traffic data (21.44% MAE reduction on PEMS-Stream, 21.93% on CA-Stream over the best baseline EAC). The few-shot experiment (Table 2) further shows STBP maintains its advantage when only 10% of training data is available, demonstrating the pattern bank's value for knowledge retention under data scarcity.

- **t-SNE visualization of learned pattern clusters.** The visualization (Figs. 3, 6) shows that the pattern bank autonomously forms semantically meaningful clusters (nodes with similar traffic rhythms grouped together) and correctly assigns new nodes to existing clusters — providing interpretability for the otherwise black-box prompt representations.

- **Scalability analysis.** The toy-dataset experiment (Fig. 8) directly demonstrates O(N) vs O(N²) GPU memory scaling, and the speed-accuracy scatter plots show STBP achieves its accuracy gains with competitive training time.

## Weaknesses

### Major

- **The backbone alone (without any continual learning mechanism) already outperforms all CSTF baselines, muddling attribution.** In the ablation (Fig. 4), the "Online" variant — the STBP backbone trained end-to-end without the pattern bank — achieves MAE ~22 on PEMS-Stream, surpassing EAC's ~26. This means the backbone design (FreNet + DLGA) alone provides a substantial portion of the improvement over prior CSTF methods. The paper partially acknowledges this ("the spatio-temporal backbone alone attains performance comparable to EAC under online training") but does not sufficiently recalibrate its claims. The main practical advance may be the backbone architecture, with the pattern bank as a secondary (though still valuable) addition. The paper would benefit from more directly stating this and restructuring its narrative accordingly.

### Minor

- **No ablation of the three prompt groups individually.** The pattern bank uses three groups of prompts (P⁰, P¹, P²) with distinct roles (gating, multiplicative interaction, dual key in attention), but the paper never removes them one at a time to measure their individual contributions. Without this, we cannot tell whether all three are necessary or whether a single prompt pool (as in EAC) would suffice within the STBP architecture. This is a concrete, addressable gap.

- **Missing the critical control: STBP's pattern bank vs. EAC's prompt pool on the same backbone.** The paper does not compare the three-group prompt design against EAC's single-pool prompt mechanism when both are attached to the same STBP backbone. Since the "Online" (no prompts) variant already beats EAC, we need this control to attribute gains specifically to the prompt interaction design (three groups, gating, dual-stream attention) rather than to the backbone. Without it, the value of the prompt design over simpler alternatives is unclear.

- **No per-period results.** Table 1 reports metrics averaged across all incremental periods. For a continual learning paper, a plot of MAE across periods (or dataset-expansion stages) is standard practice — it reveals whether STBP maintains its advantage as the graph grows, whether forgetting occurs, and whether the gap to EAC is stable or widening. The paper could add such a plot without changing any experiments.

- **Missing model capacity and compute reporting.** The paper does not report parameter counts, FLOPs, or concrete GPU memory (MB/GB) for STBP or the baselines. Given the "scalable" framing and the use of a more complex backbone, this omission makes it hard to judge whether gains come from added capacity or better architecture. The memory figure (Fig. 8) shows a toy-dataset scaling curve but does not include comparative memory for EAC or other CSTF methods.

- **The "w/o Backbone" ablation is ambiguous.** It replaces the backbone with "the ones used in TrafficStream, STKEC, and EAC" — it is unclear whether this is an averaged result, a selection of one representative backbone, or a separate result per backbone. This should be clarified.

### Trivial

- Figure descriptions in the text (Figs. 4–8) are duplicated and the OCR-rendered tables are hard to parse; these are parser artifacts and not author issues.
- Minor: the paper claims the backbone is "node-count independent" but only evaluates on datasets with moderate node counts (hundreds); the claim is conceptually justified by the lack of a fixed adjacency matrix but this is worth hedging.

## Nice-to-Haves

- Add quantitative clustering metrics (e.g., silhouette score, NMI) to the t-SNE analysis to make the "pattern bank distinguishes nodes" claim rigorous.
- Ablate FreNet individually (replace with a standard temporal module like TCN while keeping DLGA) to isolate the frequency-domain contribution, rather than only replacing the full backbone.
- Compare the memory footprint of the pattern bank (in MB) to replay-based methods (e.g., TrafficStream's buffer) to substantiate the privacy/storage advantage claimed in Sec. 4.2.
- Test the backbone on a dataset with a substantially different graph structure to demonstrate the "general" claim more concretely.

## Removed Points

- **"Claimed novelty overstated relative to EAC"** — The harsh critic characterized this as a near-fatal framing issue. However, the paper positions itself as engineering refinements (three-group prompt design + better backbone) rather than a fundamentally new paradigm, and it cites EAC appropriately as a baseline. The similarity to EAC is a real observation but is more accurately expressed as a need for better controls (covered above) than a novelty inflation claim. The paper does not claim to invent prompt-based continual learning for CSTF.
- **"Prompt-based gating not justified (Eq. 5)"** — The critic asked for ablation of the specific multiplicative gating formulation. While this would strengthen the paper, it is a standard design choice (residual-style gating with learnable parameters) and the paper provides intuitive motivation. It is a request for deeper analysis, not a weakness.
- **"Efficiency study missing numerical values"** — The scatter plots (Fig. 8) do provide relative visual comparison; this concern is about presentational precision rather than a substantive flaw.
- **"t-SNE visualizations are qualitative"** — While true, the visualizations are accompanied by concrete examples (cluster time-series plots) that ground the claims. The rigor concern is reasonable but the strength of the claim is appropriately modest.
- **"FreNet contribution not quantified"** — The "w/o Backbone" ablation does ablate FreNet (by replacing the full backbone with CNN+GCN). Separate individual ablation is a nice-to-have, not a missing piece.
- **Strengths dropped from Strength Finder:** Several claimed strengths were generic or superficial: "comprehensive experimental validation" is partially kept but de-emphasized; generic statements about "addressing an important problem" were dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the critical control**: Compare STBP's three-group pattern bank against EAC's single-prompt pool on the STBP backbone (freeze backbone, only expand prompts). This single experiment would cleanly separate the prompt-design contribution from the backbone contribution and is the most actionable way to strengthen the paper.
2. **Report per-period results**: Add a line plot showing MAE across incremental periods for STBP and the top baselines (EAC, PECPM) for at least one dataset.
3. **Ablate the three prompt groups individually**: Remove P⁰, P¹, P² one at a time in the ablation study to show which design choices matter.
4. **Add parameter counts and FLOPs** to the efficiency table, and include the concrete memory usage of EAC alongside the toy-dataset scaling curve.
5. **Rephrase the "general" backbone claim** more precisely: the backbone is adjacency-matrix-free and node-count-independent, which enables zero-shot transfer to new nodes — this is already stated but could be highlighted earlier.
6. **Clarify the "w/o Backbone" setup**: specify whether the result is from a single backbone or averaged across multiple.

## Score and Decision

**Round 1 bracket (explicit):** 5.0–7.0, anchored by EAC at 6.75 (same subfield) and weak papers below 3.5.

**Calibration anchors used:**

| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| FRzCIlkM7I (EAC) | 6.75 | R1 | Most directly comparable: both are prompt-based CSTF methods. STBP has stronger empirical results (21% MAE reduction) but weaker novelty attribution (backbone alone beats EAC). EAC had a cleaner conceptual framing (expand/compress principles). STBP is slightly weaker overall due to attribution ambiguity. |
| mkjKqeBXkt (KITS) | 5.67 | R1 | Spatio-temporal kriging with incremental training. Different task, but similar evaluation rigor. STBP is clearly stronger. |
| URCfZ2NgaR (SKI-CL) | 5.33 | R1 | Continual MTS forecasting with structural knowledge. Different domain, weaker experiments. STBP is stronger. |
| 82Mc5ilInM (FreeDyG) | 6.75 | R2 | Frequency-enhanced dynamic graphs. STBP has more comprehensive experiments but similar frequency-domain novelty level. Comparable quality. |
| 4A9IdSa1ul (FreDF) | 7.00 | R2 | Frequency-enhanced time series forecasting. Cleaner contribution with theory + experiments. STBP's contribution is more engineering-heavy. STBP is slightly weaker. |
| 5IvTw0qMKj (C²INet) | 4.67 | R2 | Continual trajectory prediction. Different domain, less convincing results. STBP is stronger. |

**Narrowing:** Round 2 placed STBP between the 5.33–5.67 range (clearly stronger) and the 6.75–7.00 range (weaker than the cleanest contributions but comparable to EAC's consensus). The decisive factor is the attribution problem (backbone alone beats baselines), which is a genuine weakness that EAC did not face to the same degree.

**Final score: 6.0** — solid paper with impressive empirical results, genuine architectural contributions (FreNet, DLGA), and addressable weaknesses. Not top-tier due to muddled attribution and missing controls, but clearly above the acceptance threshold with appropriate revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>