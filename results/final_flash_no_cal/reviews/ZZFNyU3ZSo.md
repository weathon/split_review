Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes UniMoD, a task-aware token pruning method for efficient training of unified multimodal transformers. Through empirical analysis of attention weight patterns, layer importance via the ARank metric, and task interactions, the authors establish that token redundancy varies significantly across tasks and layers. UniMoD uses separate, per-task Mixture-of-Depths (MoD) routers with a layer-switch module that selects which layers to prune based on ARank scores. Applied to Show-o and a re-implemented Emu3, the method reduces training FLOPs by 15–40% while maintaining or slightly improving benchmark performance. Ablation studies confirm that both the task-specific routers and the layer selection mechanism are necessary.

## Strengths

1. **Well-motivated by a thorough empirical analysis.** Section 3 systematically examines attention-weight patterns across four unified transformers (Fig. 2), layer importance through layer-skipping experiments (Table 1), token redundancy via ARank across layers (Fig. 3), and task interactions via competitive token pruning (Fig. 4). This analysis provides concrete evidence that token redundancy is both layer-dependent and task-dependent, directly motivating the task-aware design.

2. **Consistent FLOPs reduction with maintained performance.** Table 3 shows that UniMoD reduces training FLOPs by 15% on Show-o (51.1→43.3 TFLOPs) and 40% on Emu3 (89.0→53.5 TFLOPs), while achieving comparable or slightly better scores on most benchmarks. Table 4 confirms the FLOPs reductions translate into measurable training speedups and memory savings.

3. **Ablations demonstrate the necessity of the key design choices.** Table 5 compares UniMoD against three variants: Basic MoD, without the layer-switch module, and without task-aware routers. The full method substantially outperforms all variants on both generation (GenEval: 0.61 vs. 0.15–0.50) and understanding benchmarks, providing causal evidence that both task-specific routers and ARank-based layer selection are essential.

4. **Generality across different unified architectures.** UniMoD is validated on two fundamentally different unified architectures: Show-o (diffusion generation + autoregressive understanding) and Emu3 (fully autoregressive). The paper also extends the method to pure diffusion models (DiT, PixArt) in the appendix, demonstrating wider applicability.

5. **Efficiency gains scale with model size.** Section 5.2 reports that on an 8B-parameter Show-o backbone, FLOPs reduction rises to 20% (vs. 15% on the 1.3B model), suggesting the method becomes more beneficial as model scale increases.

## Weaknesses

### Fatal

None.

### Major

1. **The Emu3 validation is conducted on a re-implementation, not the official model.** The paper transparently states that "our full Emu3 results differ from the original paper because we use alternative training datasets, as the official code and data are not publicly available." This means the "Emu3" baseline in Table 3 is a custom variant trained on different data (LLaVA-v1.5-mix-665K for understanding). While the internal comparison (UniMoD vs. this re-implemented baseline) is valid, it is impossible to know whether the reported performance levels match the published Emu3. The improvements over this baseline are small (MME 901 vs. 881, GenEval 0.48 vs. 0.46) and could be within noise or dataset differences. This substantially weakens one of the paper's two main experimental validations. The Show-o results (which use official models and data) remain solid, but the paper's overall strength would benefit from either calibrating the re-implementation against published numbers on a subset of benchmarks, or presenting the Emu3 results as secondary.

### Minor

2. **The Layer Switch Module specification is underspecified in its link to the final configuration.** Section 4.1 describes a procedure that uses ARank to (i) select half the layers with lowest values and (ii) derive pruning ratios by normalizing ARank by sequence length. However, Section 5.1 reports specific settings that are not explicitly derived from this procedure in the paper: e.g., "transform the last 12 layers into MoD layers" (which is consistent with ARank if those layers have the lowest values, but the paper does not show this mapping), "scale the capacity from 1 down to 0.2" for MMU, and "prune 20% of the tokens in the later layers" for T2I. The connection between the ARank-based estimation and these specific numbers is not spelled out, making it unclear how much of the final design is determined by the formal procedure vs. manual tuning.

3. **No variance or statistical significance is reported for any benchmark result.** Given that several improvements over baselines are small (e.g., +1–2 points on MME, GenEval 0.48 vs. 0.46), it is unknown whether these differences are stable across training runs. Reporting standard deviations or multiple-seed averages would substantially strengthen the reliability of the results.

4. **The empirical analysis in Section 3 is primarily demonstrated on Show-o.** While ARank values are reported for multiple models (Fig. 3), the detailed layer-skipping experiments (Table 1), task interaction analysis (Table 2), and competitive token pruning (Fig. 4) are conducted on Show-o alone. This limits confidence that the motivating observations generalize equally to fully-autoregressive models like Emu3, where the task-redundancy patterns may differ.

### Trivial

5. The paper states it "select[s] the half of layers with the lowest [ARank] values" but never justifies why 50% (rather than e.g., 30% or 70%) is the appropriate fraction. No sensitivity analysis is provided for this hyperparameter.

6. The description of how T2I MoD, MMU MoD, and Shared MoD layers behave during mixed-task batches is unclear: when a batch contains both task types simultaneously, how are tokens routed through the three layer types?

## Nice-to-Haves

- A comparison to a state-of-the-art efficient-training baseline applied to the same architecture (e.g., a properly tuned MoMa-like approach on Show-o). The "Basic MoD" ablation is a useful starting point, but its FLOPs (40.8) are lower than UniMoD (43.3), and the paper dismisses MoMa in Related Work without experimental comparison. Matching the FLOPs budget across all methods would further strengthen the evaluation.
- Sensitivity analysis for the fraction of converted layers (e.g., 25%, 50%, 75%) and for the pruning-ratio estimation method, to demonstrate robustness of the design choices.
- A brief limitations section discussing scenarios where task-specific routers might struggle (e.g., interleaved task sequences, ambiguous token-task assignment) and the overhead of maintaining per-task routers.

## Removed Points

These points were raised in the reviews but are removed after verification against the paper:

1. **"Basic MoD ablation is unfair because FLOPs are not matched"** (Harsh Critic). The paper states "each ablation experiment maintains the same pruning rate as our method" (Sec. 5.3). The small FLOPs difference (40.8 vs. 43.3 TFLOPs) reflects the overhead of additional routers, not different pruning rates. Basic MoD prunes more aggressively (fewer FLOPs) yet performs worse, which actually strengthens the paper's case. **Removed.**

2. **"Equation (4) is essentially standard MoD with a task subscript"** (Harsh Critic). This is expected — the novelty lies in the task-aware architecture and the ARank-based layer selection, not in a new routing formula. Criticizing the equation for being standard is not a genuine weakness. **Removed.**

3. **"Inconsistency between ARank-based selection and 'last 12 layers'"** (Harsh Critic, overstated). The Show-o model has at least 23+ layers; "last 12" is approximately half. From Figure 3, later layers consistently have lower ARank values, so selecting the last 12 is consistent with "select the half with lowest ARank." The paper could be clearer about this connection, but no actual inconsistency exists. Demoted to Minor (point 2 above). **Original framing removed.**

4. **Speculative fatal claims about Emu3 results** (Harsh Critic: "impossible to know whether the claimed 40% FLOPs reduction with maintained performance would hold against the actual Emu3"). The FLOPs reduction is architectural and would be the same regardless of training data; the benchmark comparison is internal to the authors' setup. The weakness lies in external validity, not in the internal experiment. Demoted to Major accordingly. **Overblown framing removed.**

5. **"Attention weight analysis is mostly qualitative"** (Harsh Critic). The analysis is appropriate for an empirical motivation section; the quantitative conclusions come from ARank values and the competitive token-pruning experiment (Fig. 4). This is not a meaningful weakness. **Removed.**

## Novel Insights

The key insight that emerges from reading the reviews against the paper is that the paper's strongest evidence comes from the Show-o experiments and the ablation study (Table 5). The task-aware router design is genuinely shown to be critical: the "w/o task-aware router" variant catastrophically degrades generation quality (GenEval 0.50 vs. 0.61). However, the paper would be significantly strengthened by presenting the Emu3 results more cautiously and by making the connection between the principled ARank-based method and the final implementation choices explicit.

## Suggestions

1. **Address the Emu3 issue.** Either (a) calibrate the re-implementation against published Emu3 numbers on at least 2–3 shared benchmarks (e.g., VQAv2, MME) and report both, or (b) reframe the Emu3 experiments as a demonstration of UniMoD on an Emu3-like architecture using alternative data, and soften the claims accordingly.

2. **Make the Layer Switch Module fully explicit.** Show a concrete example of how ARank values map to pruning ratios and which layers are selected. If the "last 12 layers" are indeed the 12 with lowest ARank, state this directly. If specific numbers (20% pruning, capacity 1→0.2) are manually tuned, acknowledge this and report sensitivity.

3. **Add variance estimates.** Run 2–3 seeds for the main experiments (Show-o baseline and UniMoD, or at least the ablations) and report standard deviations to establish significance.

4. **Clarify the mixed-batch behavior.** Describe how T2I, MMU, and Shared MoD layers operate when a batch contains samples from both tasks — specifically, which router processes which tokens.

## Score and Decision

This paper addresses a relevant and timely problem with a well-motivated approach. The core contribution — task-specific routers for MoD in unified transformers — is supported by thorough empirical analysis and convincing ablation studies on Show-o. The primary weakness is the reliance on a re-implemented Emu3 baseline, which limits the strength of the second experimental validation but does not invalidate the overall contribution. The method is clearly described, the results are positive, and the work is likely to be useful to the community. With the Emu3 issue addressed and better specification of the layer-selection procedure, this would be a strong paper.

**Score: 7.0**

**Decision: Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>