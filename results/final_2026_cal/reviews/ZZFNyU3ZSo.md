Now I have all the information I need. Let me synthesize the final review.

**Calibration Summary:**

**Round 1 bracket:** (3.5, 7.0)
- Weak band (<3.5): TREWA (3.33), Subjective Depth Transformers (3.00), PREP (3.33), Non-Deep ViTs (3.00) — all had fundamental issues that UniMoD does not share
- Middle band (3.5-7.5): UTP (4.50), MMTok (5.00), UniPruneBench (4.50), Learning Compact Vision Tokens (4.50) — token pruning papers, most relevant comparison
- Strong band (>7.5): Verifier (8.00), NavFoM (8.00), RL (8.00), Text-to-3D (8.00) — fundamentally different class of papers

**Initial bracket:** [4.0, 6.0]

**Round 2 narrowing (4.0-6.0):**
- Uni-X (5.00, accept poster) — unified multimodal model with analysis + method; similar structure to UniMoD; got mixed scores (8,4,4,4)
- LaTtE-Flow (5.00, reject) — unified model for generation + understanding
- Nuwa (5.50, accept poster) — stronger token pruning paper with better evaluation
- PruneSID (5.50, accept poster) — efficient token pruning
- TokenSculpt (5.50, reject) — video token pruning

**Comparisons:** UniMoD is most comparable to Uni-X (5.0) and UTP (4.50). It has better empirical analysis than UTP, and a similar structure to Uni-X (analysis → method → experiments), but weaker baselines than both. Nuwa (5.5) has stronger evaluation rigor.

**Final score: 5.0** — positioned between UTP (4.50) and Nuwa (5.50), comparable to Uni-X (5.00). The paper has genuine contributions (first systematic analysis of token redundancy in unified transformers, task-aware MoD design) but notable evaluation gaps (weak baselines, no variance reporting).

---

## Summary

This paper studies token redundancy in unified multimodal transformers (models handling both generation and understanding). Through analysis of attention weights, layer importance via ARank, and competitive token pruning, the authors find that token redundancy varies by task and layer. They propose UniMoD, which uses separate task-specific routers and ARank-guided layer selection to prune tokens during training. Experiments on Show-o (1.4B) and Emu3 (8.5B) show 15–40% FLOPs reduction with maintained or improved performance on several benchmarks.

## Strengths

- **Comprehensive empirical analysis (Section 3).** The paper systematically examines attention weight patterns (four models), ARank-based token redundancy across layers (four models), layer importance via inference skipping (Table 1), and competitive token pruning between tasks (Figure 4). This is the first such analysis that jointly considers task differences and layer differences in unified transformers, going beyond prior single-task or single-model studies (γ-MoD, MoMa). The competitive pruning experiment (Figure 4) is especially compelling — it directly quantifies the imbalance where generation tokens dominate when tasks compete, providing concrete motivation for separate task-specific routers.

- **FLOPs reduction with maintained or improved performance (Table 3).** On Show-o, UniMoD reduces TFLOPs from 51.1 to 43.3 (15%) while improving MME (1056→1093.7) and DSG (72.2→73.6). On Emu3, FLOPs drop from 89.0 to 53.5 (40%) with comparable GenEval (0.46→0.48) and DSG (79.0→80.0). The benefits are more pronounced on Emu3 due to its longer image token sequences (4096 vs 1024), which is honestly acknowledged.

- **Ablation studies isolate design components (Table 5).** The "w/o task-aware router" variant (single router) performs competitively on understanding tasks (MME 1052 vs UniMoD's 1093.7; GQA 54.4 vs 54.5) but much worse on generation (GenEval 0.50 vs 0.61). Removing the layer switch module drops MME to 920.3. This cleanly confirms that task-aware routing primarily helps generation quality while ARank-based layer selection helps both.

- **Concrete training-cost measurements (Table 4).** The paper reports per-iteration time and memory, not just FLOPs. For Emu3, training cost drops from 3.56×/iter to 2.80×/iter, providing evidence that the method reduces real overhead, not just theoretical FLOPs.

## Weaknesses

### Major
None.

### Minor

- **Baselines are too weak to be informative.** The paper compares against Interleaved Layer Skipping (removing every other layer entirely) and Early Exit (stopping at layer 12). Both are deliberately destructive and predictably collapse performance — they do not represent reasonable efficient-training alternatives. The paper does include a "w/o task-aware router" ablation (single router with ARank-based layer selection), which is a more meaningful comparison, but it operates at 40.8 TFLOPs vs UniMoD's 43.3 (~6% less compute). While the GenEval gap (0.50→0.61) is large enough to survive this compute difference, the understanding-task gaps are very small (GQA 54.4 vs 54.5; POPE 80.2 vs 80.3). An equal-compute single-router baseline would strengthen the central claim that task-awareness is necessary. A direct comparison to a MoMa-style single-router MoD adapted to Show-o/Emu3 at matched FLOPs would be the clearest evidence.

- **No statistical significance or variance reported.** All results in Tables 3, 4, and 5 are point estimates with no error bars or discussion of multiple runs. Given that several reported differences are small (e.g., Show-o GQA: 56.3 vs 54.5; CLIP_score: 0.331 vs 0.332 on Show-o, 0.318 vs 0.321 on Emu3), one cannot assess whether these represent genuine degradation, improvement, or noise. The paper's claim of "maintaining or improving performance" would be substantially stronger with 3-5 runs and standard deviations.

- **Incomplete justification for separate routers on Emu3.** The paper's Observation 3 (Section 3.3, Figure 3c) states that Emu3 exhibits *similar* ARank values across tasks — meaning token redundancy is comparable for generation and understanding. Yet the method still applies separate task-specific routers to Emu3. The attention-weight analysis (Observation 1, Figure 2) does show different patterns across tasks for Emu3, which could justify task-specific routing even when ARank is similar, but the paper never makes this connection explicitly. The paper should either (a) show that task-specific routers outperform a single router on Emu3 controlling for compute, or (b) clearly articulate why attention-pattern differences (not ARank differences) motivate separate routers on Emu3.

- **Layer switch module is underspecified.** The description "approximate each layer's pruning ratio by normalizing its ARank score by the sequence length" is vague — no concrete formula or normalization method is given. The choice of "half of layers" with lowest ARank appears arbitrary without sensitivity analysis. The reliance on 50 samples per task to compute ARank raises concerns about stability and reproducibility. These details should be concretely specified or shown to be robust via ablation.

### Trivial

- Table 3: UniMoD on Show-o GQA drops from 56.3 to 54.5 (a 1.8-point decrease) but the paper's abstract claims "maintaining or improving" performance. While other metrics do improve, this should be noted more transparently.

## Nice-to-Haves

- A Pareto frontier plot in the main text showing the FLOPs-performance trade-off across multiple pruning ratios would strengthen the paper.
- The paper could discuss the overhead of multiple routers (additional parameters, memory) and scenarios where task-specific pruning might fail.
- An attempt to adapt MoMa (Lin et al., 2024b) as a baseline on Chameleon-like unified models would test generality and strengthen the comparison, though the authors note MoMa lacks generation results.

## Removed Points

These points were flagged as potentially relevant but removed for the reasons noted:

1. **"Missing related works about token merging (ToMe) or visual token reduction"** — The paper's focus is on *training-time* MoD-style token pruning for unified transformers, not inference-time token merging. The related work covers MoMa, γ-MoD, and MoE-LLaVA (the most directly relevant prior work on MoD-based pruning for multimodal models). This is scope-appropriate.

2. **"The claim about Lumina-mgnt showing similar attention patterns is speculative"** — The paper attributes this to "interleaved training with consistent design" which is a reasonable interpretation. The claim does not drive the method design and is presented as a secondary observation.

3. **"The conclusion that pruning should target tokens across both image and text modalities is a weak inference"** — This follows logically from Observation 1 (attention weights for both modalities vary by task). It's a reasonable inference, not a weak one.

4. **"The layer-skipping experiment is too coarse"** — It's acknowledged as a simple diagnostic experiment, and the paper primarily relies on the more informative ARank analysis. The coarseness is acceptable for a preliminary observation.

5. **"The training datasets for Emu3 are described vaguely"** — The paper states "LLaVA-v1.5-mix-665K plus Show-o T2I data" and acknowledges results differ from original Emu3 due to different training data. This is sufficient transparency for an empirical paper.

## Novel Insights

The competitive token pruning experiment (Figure 4) is the paper's most novel and insightful contribution: when generation and understanding tokens compete under a capacity constraint, generation tokens are consistently retained at much higher rates across all layers. This cleanly quantifies a tension that prior work on MoD for multimodal models (MoMa, γ-MoD) never examined. Combined with the finding that removing one task barely affects the other's performance (Table 2), this provides strong evidence that task-specific pruning is both necessary and feasible. The observation that ARank-guided layer selection (not task-aware routing) drives most of the understanding-task improvements while task-aware routing is critical for generation quality is a nuanced result that could inform future efficient-training designs.

## Suggestions

- **Replace the Interleaved Layer Skipping and Early Exit baselines** with a properly adapted single-router MoD that matches UniMoD's total FLOPs. This would cleanly isolate the benefit of task-awareness vs. uniform token pruning. The current baselines are too weak to be probative.

- **Report means and standard deviations over 3–5 runs** for all main results, especially given the small deltas on several metrics (GQA, CLIP_score). If multiple runs are computationally prohibitive, acknowledge this limitation explicitly.

- **Clarify the Emu3 justification.** Either add an Emu3 ablation showing that task-specific routers outperform a single router at matched compute, or explicitly connect the attention-weight differences (Figure 2c) — not ARank — to the need for separate routers on Emu3.

- **Concretely specify the ARank normalization formula** used for pruning ratio estimation, and add a sensitivity analysis for the "half the layers" selection threshold.

- **Include a main-text Pareto frontier plot** showing performance vs. FLOPs at multiple pruning ratios, to better characterize the efficiency-performance trade-off.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| jdu24QufJY | 3.33 | R1 weak | TREWA — token pruning in ViTs via wavelet; fundamental issues, weaker than UniMoD |
| exMMxIakjl | 3.00 | R1 weak | Subjective Depth Transformers — dynamic routing, unclear contributions |
| 2TK9CLwMGA | 3.33 | R1 weak | PREP — training-free token pruning; less relevant |
| jm2AIiD1bQ | 3.00 | R1 weak | Non-Deep ViTs — structural reparameterization; different problem |
| mTR9CVXpFv | 4.50 | R1 mid | UTP — token pruning for LMMs; similar weaknesses (no variance, missing baselines), less analysis |
| GvPdSWZT31 | 5.00 | R1 mid | MMTok — training-free token pruning; stronger evaluation |
| Vu7iQO3f9u | 4.50 | R1 mid | UniPruneBench — token pruning benchmark; mixed reviews |
| aB2pQrPXXI | 4.50 | R1 mid | Learning Compact Vision Tokens — token compression; similar weaknesses |
| DM0Y0oL33T | 8.00 | R1 strong | Universal Verifier — unrelated topic, much stronger paper |
| kkBOIsrCXh | 8.00 | R1 strong | Navigation Foundation Model — unrelated |
| oBXfPyi47m | 8.00 | R1 strong | RL with world models — unrelated |
| kI27Niy4xY | 8.00 | R1 strong | Text-to-3D — unrelated |
| IJLIYpCkwz | 5.00 | R2 | Uni-X — unified multimodal model with analysis+method; most comparable; got (8,4,4,4) |
| R1HcIN90A1 | 4.40 | R2 | ModalMix — data mixing for multimodal models; less relevant |
| lVpWNivXEU | 5.00 | R2 | LaTtE-Flow — unified model; rejected |
| 9aI6XUDYLX | 4.00 | R2 | BLIP3-o — unified model family; different scope |
| DqfKOHqzh9 | 5.50 | R2 | TokenSculpt — video token pruning; stronger evaluation |
| C9yclwdquU | 5.50 | R2 | Nuwa — token pruning for VLMs; stronger evaluation than UniMoD |
| i36E5Ezm0H | 5.50 | R2 | PruneSID — token pruning; stronger evaluation |
| 57IX6gnZ0 | 5.50 | R2 | VisionTrim — token pruning; stronger evaluation |

**Round-1 bracket:** [3.5, 7.0] → narrowed to [4.0, 6.0]

**Final calibration:** UniMoD is comparable to Uni-X (5.0) in structure and contribution magnitude, but has notably weaker baselines. It is stronger than UTP (4.50) and Learning Compact Vision Tokens (4.50) because it tackles the harder problem of *training-time* pruning for *unified* models with a richer empirical analysis. It is weaker than Nuwa (5.50) and PruneSID (5.50) on evaluation rigor. The paper's genuine contributions (task-aware token redundancy analysis for unified transformers, competitive pruning experiment) and reasonable method design place it at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>