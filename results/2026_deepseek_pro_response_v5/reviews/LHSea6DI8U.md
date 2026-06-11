Now I have enough comparisons. Let me finalize the review.

**Round 1 Bracket**: Based on the anchors, STBP sits between 5.5 and 6.5. It's clearly stronger than the 2.33-4.00 range papers (DIRAD, TFMoE, SKI-CL at 4.40), but has more methodological issues than the 6.75 EAC paper (its direct baseline) and the 6.75-7.00 frequency-domain papers (FreeDyG, FreDF).

**Round 2 Narrowing**: Within the 5.5-6.5 bracket, I compare against TEMPO (6.33, prompt-based time series), SVQ (6.00, VQ for ST forecasting), and FreeDyG (6.75). STBP tackles a harder problem (continual ST forecasting) than TEMPO and has stronger empirical results than EAC. But the two major weaknesses (fine-tuning ambiguity and backbone-vs-CL confound) pull it below the cleaner 6.75 papers. **Final score: 6.0**.

---

## Summary
STBP proposes a continual spatio-temporal forecasting framework combining a frequency-domain backbone (FreNet) with dual-stream linear graph attention (DLGA) and an expandable contextual pattern bank. The backbone extracts stable representations in the frequency domain and captures dynamic spatial correlations at O(N) complexity, while the pattern bank is incrementally expanded and fine-tuned (with the backbone frozen) to mitigate catastrophic forgetting. On two traffic datasets, STBP achieves 21%+ MAE reductions over the best CSTF baseline (EAC); on AIR-Stream the margin is a narrower 2.35%.

## Strengths
- **Strong empirical results on traffic datasets**: STBP achieves 21.44% and 21.93% MAE reduction over EAC on PEMS-Stream and CA-Stream respectively, with consistent gains across all metrics (MAE, RMSE, MAPE) and forecast horizons (3, 6, 12 steps). The few-shot experiment (Table 2) further reinforces these gains, showing STBP maintains a large margin even with 10% training data in subsequent periods.
- **Architecture with clear component-to-challenge mapping**: FreNet targets distributional drift via frequency-domain analysis (Eq. 6), DLGA targets dynamic spatial correlations with O(N) complexity (Eq. 9), and the contextual pattern bank with parameter expansion (Eq. 4) and prompt-based gating (Eq. 5) targets catastrophic forgetting. This design intentionality is well-articulated and gives the architecture strong internal coherence.
- **Diverse baseline selection with appropriate training protocols**: Baselines span conventional STGNNs retrained from scratch (GWNet, STID), online-fine-tuned models (iTransformer), and dedicated CSTF methods (TrafficStream, STKEC, PECPM, STRAP, EAC). Each baseline uses a training regime appropriate to its architecture, making comparisons informative.
- **Controlled scalability experiment**: The toy dataset experiment (Figure 8) directly validates the O(N) scaling claim by comparing linear attention against O(N²) full attention and no-pattern-bank variants across growing node counts with GPU memory as the metric, showing the pattern bank adds only linear overhead.

## Weaknesses

### Fatal
None.

### Major
- **Ambiguity in pattern bank fine-tuning protocol**: The paper states "Only the expanded contextual pattern bank P'_τ is fine-tuned during training" (line 98), where P'_τ = P_{τ-1} || ΔP_τ. It is unclear whether fine-tuning updates *all* of P'_τ (including old embeddings P_{τ-1}) or *only* the newly added parameters ΔP_τ. If old embeddings are updated, the pattern bank itself would suffer from catastrophic forgetting as old node representations drift. If only new embeddings are trained, adaptation of existing nodes to distribution shifts is lost. This ambiguity directly bears on the central claim that the pattern bank mitigates catastrophic forgetting, and the paper offers no clarification.

- **Backbone quality vs. continual learning strategy confound**: The strongest baselines (EAC, TrafficStream, STKEC) use simpler CNN+GCN backbones, while STBP uses a substantially stronger FreNet+DLGA backbone. The paper acknowledges existing CSTF methods use "relatively simple" backbones (line 22). The "Online" ablation (STBP backbone, full fine-tuning, no pattern bank) reportedly reaches "performance comparable to EAC" (line 262), suggesting the backbone alone is already competitive. While the w/o Backbone ablation partially addresses this, the CNN+GCN replacement is drawn from three different models (TrafficStream, STKEC, EAC), making it unclear which architecture was used and whether it was fairly tuned. The evidence that the *integration* specifically drives the gains, rather than the backbone alone, is not as cleanly supported as it could be.

### Minor
- **AIR-Stream results are notably weak and unanalyzed**: STBP achieves only 2.35% MAE improvement over EAC on AIR-Stream, and RMSE is essentially tied (37.76 vs 37.83). The paper reports this transparently but offers no analysis of why the method underperforms on air quality data compared to traffic data. On a third of the tested datasets, the advantage nearly vanishes, which weakens the "general backbone" framing.

- **No per-period performance curves**: The paper reports only averaged metrics across all incremental periods. Per-period curves would directly show whether STBP's advantage grows over successive periods (as expected if it mitigates forgetting) or remains constant (suggesting backbone quality primarily drives the gain). This is a missed opportunity to directly validate the anti-forgetting claim.

- **FreNet contribution not independently ablated**: The paper claims FreNet "makes a notable contribution" (line 262) but there is no "w/o FreNet" ablation variant. FreNet is only tested as part of the bundled "w/o Backbone" variant that replaces both FreNet and DLGA together, so its isolated contribution cannot be assessed.

- **w/o Backbone variant under-specified**: The variant replaces FreNet+DLGA with "CNN and GCN" from "TrafficStream, STKEC, and EAC" (line 244). These three models may have different CNN+GCN backbones. The paper does not specify which specific architecture was used, whether all three were tested and averaged, or whether hyperparameters were re-tuned.

### Trivial
- **Three-group pattern bank design not justified**: The paper uses P^(0), P^(1), P^(2) with distinct roles (gating modulation, gating scaling, attention key) but never explains why three groups are needed rather than one or two, and no ablation across group counts is provided.
- **Privacy and storage claims unsupported**: The claim that the pattern bank offers "privacy protection" and "storage efficiency" (line 104) is asserted without any quantitative comparison to replay-based methods.

## Nice-to-Haves
- Report per-period performance curves to directly illustrate anti-forgetting dynamics.
- Analyze why STBP's advantage narrows substantially on AIR-Stream.
- Include a "w/o FreNet" ablation and report all ablation results in a numerical table rather than only bar charts.
- Clarify the specific CNN+GCN architecture used in the w/o Backbone ablation.
- Report parameter counts alongside the existing time/memory efficiency analysis.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Continual learning protocol under-specified (Harsh Critic)**: The paper states that detailed dataset statistics are in Appendix A.4.1 (line 136). The parser strips appendices; the original submission has these details. The formal streaming graph definition (Section 3) is clear. Demanding all protocol details in the main text is a presentation preference, not an evidential gap.
- **FreNet frequency embedding not constrained (Harsh Critic)**: The learnable frequency embedding F_τ being a free parameter learned end-to-end is standard practice. The FFT → multiply → IFFT mechanism operates in the frequency domain by construction; explicit constraints to "guarantee" low-frequency emphasis are not needed.
- **Backbone scene-agnostic claim misleading (Harsh Critic)**: The paper explicitly states the *backbone* is independent of node count (lines 108-109), not the entire system. The pattern bank is a separate component. The distinction is clear.
- **t-SNE is weak validation (Harsh Critic)**: The t-SNE is presented as qualitative evidence (Figure 3, line 80-81) to validate that the pattern bank captures relevance and heterogeneity, not as proof of the prompt mechanism specifically. This is appropriate for a qualitative visualization.
- **HimNet terminology shared but not contrasted (Harsh Critic)**: The paper does mention HimNet in related work (line 33) and notes its use of "contextual pattern bank." While a deeper comparison would strengthen the paper, this is a presentation enhancement rather than a substantive flaw.
- **Chart-only ablation results (Harsh Critic)**: The paper provides textual discussion of ablation findings (lines 246-262). The bar charts exist but numerical values are not extractable by the parser; the original submission's figures contain readable values. This is a parser artifact.
- **Strength Finder "Well-designed ablation study"**: Qualified — the ablation design includes useful variants but the w/o Backbone variant is under-specified (see Minor weakness).

## Novel Insights
The dual-stream linear attention design that uses the pattern bank P^(2) as an additional key stream (Eq. 9) is a genuinely novel mechanism for injecting stored knowledge into attention computation. By folding the pattern bank into the key computation within an O(N) linear attention framework — computing φ(Q)φ(P^(2))^⊤ V — the model assesses relationships between current inputs and stored patterns without constructing an N×N adjacency matrix. This specific integration connects continual learning objectives with efficient attention in a way not seen in prior CSTF work.

## Suggestions
- **Critical**: Clarify whether old pattern bank embeddings P_{τ-1} are frozen or updated during fine-tuning of P'_τ. This is a one-sentence clarification that resolves the major ambiguity about how the method mitigates forgetting.
- Add per-period performance curves to strengthen the anti-forgetting claim.
- Analyze the weak AIR-Stream result to provide insight into method limitations and domain applicability.
- Add a "w/o FreNet" ablation and report all ablations in a numerical table.

## Calibration Anchors

| Anchor | Path | Score | Round | Comparison |
|---|---|---|---|---|
| DIRAD | ZHTYtXijEn | 2.33 | R1 | Structural adaptation for CL; STBP has far more comprehensive experiments and stronger results |
| Tropical Cyclone GNN | xVbke7yC07 | 2.33 | R1 | Different domain; STBP is substantially stronger |
| Projected Subnetworks | WM5G2NWSYC | 2.00 | R1 | Online CL for few-shot learners; STBP has far more empirical depth |
| CAN | SI6zocV2SS | 1.50 | R1 | Continual learning architecture; STBP has much stronger experimental validation |
| SKI-CL | B1TnT6lUnU | 4.40 | R1 | CL for MTS forecasting; similar problem area; STBP has better results and more datasets |
| TFMoE | vJGKYWC8j8 | 4.00 | R1 | Continual traffic forecasting; STBP has 3 datasets vs 1, better architecture |
| SKI-CL (v2) | URCfZ2NgaR | 5.33 | R1 | Similar to above; STBP has stronger empirical performance |
| KITS | mkjKqeBXkt | 5.67 | R1 | Inductive ST kriging; STBP tackles a harder continual learning problem |
| S2GNN | uiyljVIP0k | 5.40 | R1 | Spectral STGNN; not CL-focused; STBP has a more novel problem framing |
| ST Graph KD | akKNGGWegr | 5.25 | R1 | Knowledge distillation for ST; STBP directly addresses CL which is harder |
| **EAC** | FRzCIlkM7I | **6.75** | R1 | **STBP's main baseline; STBP outperforms EAC but has more methodological ambiguities** |
| RePST | wCNuEA5MSv | 5.50 | R2 | PLM for ST forecasting; different approach; STBP has stronger empirical gains |
| SVQ | 4CFVPCYfJ9 | 6.00 | R2 | VQ for ST forecasting; STBP's CL framing is more challenging |
| TEMPO | YH5w12OUuU | 6.33 | R2 | Prompt-based time series; STBP tackles a harder continual learning setting |
| **FreeDyG** | 82Mc5ilInM | **6.75** | R2 | **Frequency domain for dynamic graphs; comparable methodology quality; STBP has similar strengths and weaknesses** |
| FreDF | 4A9IdSa1ul | 7.00 | R2 | Frequency-enhanced forecasting; cleaner methodology than STBP |
| GraphPulse | DZqic2sPTY | 7.00 | R2 | Topological temporal graphs; stronger theoretical grounding than STBP |

**Bracket**: Round 1 placed STBP between 5.5 and 6.5. Round 2 narrowed this by comparing against TEMPO (6.33), SVQ (6.00), FreeDyG (6.75), and FreDF (7.00). STBP is closest to SVQ (6.00) and TEMPO (6.33) in quality — it has stronger empirical results than both but also has more unresolved methodological ambiguities (the fine-tuning protocol ambiguity and backbone confound). FreeDyG (6.75) and FreDF (7.00) have cleaner methodology presentations and fewer interpretive gaps. STBP directly outperforms EAC (6.75) but EAC had higher review scores because its methodology was presented with fewer ambiguities. **Final score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>