## Summary

This paper proposes UniMoD, a task-aware token pruning method for unified multimodal transformers that handle both generation and understanding tasks. The key idea is to use separate Mixture-of-Depths (MoD) routers per task, guided by ARank-based layer selection and pruning ratios, accounting for different token redundancy patterns across tasks and layers. The method is evaluated on Show‑o (15% FLOPs reduction) and Emu3 (40% FLOPs reduction), showing maintained or slightly improved benchmark performance.

## Strengths

1. **Task- and layer-specific redundancy analysis across unified transformers.** Section 3 systematically examines attention weight patterns (Fig. 2), layer importance (Table 1), token redundancy via ARank (Fig. 3), and task interactions (Fig. 4). This multi-faceted analysis provides a principled foundation for designing task-specific routers, going well beyond the uniform pruning used in prior MoD applications on these models.

2. **Well-controlled Emu3 experiment and fair pruning baselines.** For Emu3, both the baseline and UniMoD are trained from scratch on the same data, providing a clean comparison. UniMoD reduces FLOPs by 40% while achieving comparable or slightly better scores across 8 benchmarks (Table 3). The comparisons against Interleaved Layer skipping and Early Exit (also fine‑tuned) consistently show UniMoD dramatically outperforming those alternatives, confirming that the task‑aware design adds real value beyond naive pruning.

3. **Generality across diverse architectures.** The method is validated on two fundamentally different unified transformer types — Show‑o (diffusion + autoregressive) and Emu3 (fully autoregressive) — and the paper reports extensions to pure diffusion models (DiT, PixArt), larger model scales (8B, 20% FLOP reduction), and more than two tasks. This breadth supports the claim that task‑aware pruning is not limited to a specific architecture.

## Weaknesses

### Fatal
None.

### Major

1. **The Show‑o baseline comparison is not controlled.** For Show‑o, UniMoD is fine‑tuned from a pre‑existing checkpoint using a data mixture (original T2I data + Cambrian for MMU). The "Show‑o" baseline row in Table 3 appears to be the original pre‑trained model evaluated without additional fine‑tuning, not a fine‑tuned no‑pruning control. Because the fine‑tuning itself (new MMU data, additional training steps) can change performance, the comparison cannot cleanly attribute the maintained/improved scores to UniMoD rather than to the fine‑tuning process. The paper needs a controlled experiment: fine‑tune the same checkpoint on the same data *without* pruning and compare that to fine‑tuning with UniMoD. The Emu3 experiment (both baseline and UniMoD trained from scratch on the same data) is properly controlled, but the Show‑o comparison — which accounts for one of the two main model demonstrations — remains confounded. This undermines the central claim of "maintaining performance while reducing FLOPs" for Show‑o.

2. **The GQA score of 0.0 when skipping layer 3 (Table 1) is unexplained and suspicious.** This single anomalous value is not discussed anywhere in the paper. It could indicate a uniquely critical layer, an indexing error, a broken residual connection, or some other artifact. Since the layer‑skipping analysis is presented as motivation for the method, an unexplained 0.0 undermines confidence in the reliability of that analysis and must be clarified.

3. **The FLOPs reduction for Show‑o (15%) translates to only ~2–4% faster training and ~4–9% memory reduction (Table 4).** The paper attributes this to image tokenizer differences (Show‑o uses 1024 tokens/image vs. Emu3's 4096), but does not fully explain why most of the FLOPs savings do not materialize as wall‑clock speedup. If the dominant costs (data loading, non‑transformer operations, router overhead) are not reduced by token pruning, the practical efficiency improvement for Show‑o is modest. While the FLOPs metric is meaningful as a theoretical bound, the paper should more prominently discuss the gap and its implications for deployment.

### Minor

4. **The ARank‑based layer selection is static** — computed once on 50 samples per task and not re‑evaluated during training. The paper does not check whether ARank values or the ordering of layers change as fine‑tuning progresses, nor whether the fixed selection remains optimal.

5. **The connection between the attention‑weight analysis (Sec. 3.2) and the final method is weak.** The conclusion "prune tokens across both modalities" follows generically from observing that attention patterns differ by task, but this is already implied by the standard MoD setup. The analysis does not directly motivate task‑specific routers over simpler alternatives such as modality‑specific routers.

6. **The router architecture and training details are underspecified.** The paper does not describe the router network architecture, whether an auxiliary load‑balancing loss is used, how capacity constraints are enforced, or how tokens from different tasks are separated in the unified sequence. These details are necessary for reproducibility.

7. **The competitive token pruning experiment (Fig. 4) uses a fixed Gumbel‑Softmax capacity of 0.5**, which forces high competition. The conclusion that "generation tokens are more important" may be an artefact of this specific capacity setting; robustness across different capacities would strengthen the claim.

### Trivial
- Notation inconsistency between Eq. (2) and Eq. (4). In Eq. (2), \(D^l\) is the transformer layer. In Eq. (4), \(D_t^l\) is called the "task‑specific router function," mixing the roles of the layer itself and the routing function.
- The "1.30×/iter" notation in Table 4 is not explicitly defined (presumably seconds per iteration).

## Nice-to-Haves
- Adding a baseline that prunes a uniform fraction of tokens from both tasks with a single router (task‑agnostic, same total pruning ratio) would directly quantify the benefit of task‑awareness.
- Reporting variance or multi‑seed results would help assess the stability of routing decisions and benchmark scores.
- Including FID on MS‑COCO zero‑shot generation would make generation results more comparable with the broader literature.

## Removed Points
*Criticism about missing comparison against other MoD variants (γ‑MoD, Token Merging): these operate in different settings and the paper conceptually discusses related work. Direct numerical comparison across different training setups is impractical.*  
*Criticism about missing error bars: single‑seed evaluation is common in this line of work; this is a nice‑to‑have rather than a weakness.*  
*Criticism about the "first work" claim: the paper acknowledges MoMa and positions itself as "first **task‑aware** token pruning" — a reasonable qualification.*  
*Criticism that appendix sections on diffusion models and multi‑task scaling are missing: the parser strips appendix content; these exist in the original submission.*

## Novel Insights
None beyond the paper's own contributions. The core insight — that token redundancy in unified transformers varies by task and layer, motivating task‑specific MoD routers — is the paper's primary contribution and is adequately presented.

## Suggestions
1. **Redo the Show‑o experiment as a controlled fine‑tuning comparison.** Fine‑tune the pre‑trained Show‑o checkpoint on the same data mixture *without* pruning for the same number of steps, and compare to fine‑tuning with UniMoD. This isolates the effect of pruning from the effect of fine‑tuning.
2. **Explain or correct the GQA 0.0 anomaly in Table 1.** If this is a real effect, discuss why. If it is an artifact, remove or qualify the data point.
3. **Add a profiling analysis** showing where training time is spent in the Show‑o loop, so readers can understand the FLOPs–speed gap. Discuss whether the method is better suited to longer sequences.
4. **Re‑compute ARank at training intervals** and report whether the layer ordering stays stable.
5. **Add a uniform‑pruning baseline** (single router, same total fraction pruned) to directly quantify the value of task‑awareness.

## Score and Decision

**Score: 4.5**  
**Decision: Reject**

The paper addresses an important problem with a sensible approach (task‑specific MoD routers) and a reasonably thorough analysis. However, the uncontrolled Show‑o baseline comparison undermines one of the two main empirical demonstrations, and the unexplained GQA 0.0 anomaly plus the large gap between FLOPs savings and practical speedup for Show‑o raise additional concerns. The Emu3 experiment is well‑controlled and provides the strongest evidence for the method's value. With the comparison issue fixed and the analytical loose ends addressed, this would be a solid incremental contribution; in its current form, the evidence does not fully support the headline claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>