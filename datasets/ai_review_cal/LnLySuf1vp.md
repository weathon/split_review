- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes SpikeGCL, a graph contrastive learning framework built on spiking neural networks that learns 1-bit binarized node representations. The framework partitions node features into T non-overlapping groups (one per time step), processes each with a peer GNN encoder whose later layers share parameters, and binarizes the outputs via spiking neurons. A blockwise surrogate gradient training strategy is introduced to address vanishing gradients in deep SNNs. Results on 6 benchmark graphs show that SpikeGCL achieves accuracy within 1–2 points of the best full-precision GCL methods while using dramatically fewer parameters (~37× on ogbn-MAG) and lower theoretical energy (~7100× reduction versus the average baseline).

## Strengths

1. **First GCL framework producing binary representations via SNNs** — The paper is the first to combine spiking neural networks with graph contrastive learning for learning 1-bit node representations. This is a novel and timely direction given the growing need for efficient graph models on resource-constrained devices.

2. **Empirically demonstrated efficiency–accuracy trade-off** — Table 1 shows SpikeGCL achieves 70.9% on ogbn-arXiv (vs. 71.6% best, BGRL/GGD) and 32.0% on ogbn-MAG (vs. 32.4% best, SUGRL), while Table 2 reports 6.6 KB parameters and 0.18 mJ energy on MAG versus average baselines of 246.4 KB and 1279.1 mJ. These concrete numbers demonstrate that the binary representations, when properly trained, yield accuracy close to full-precision methods with orders-of-magnitude efficiency gains.

3. **Feature grouping avoids graph repetition overhead** — The non-overlapping feature partitioning strategy (Section 4.1) avoids the memory and computational overhead of repeating the full graph multiple times (as done in SpikingGCN). This is a concrete architectural improvement that directly enables scaling to larger graphs.

4. **Parameter sharing across peer encoders** — Sharing all but the first layer across T peer GNNs (Section 4.3) is a practical design that limits parameter growth with increasing T and avoids overfitting. This is clearly motivated and contributes to the observed parameter efficiency.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 does not support the expressiveness claim in the abstract** — The informal Theorem 1 states that SpikeGCL can approximate a full-precision GNN with hidden dimension *d/T*, where d is the embedding dimension and T is the number of time steps. The abstract claims "comparable expressiveness with its full-precision counterparts," but the theorem compares against a GNN that is *T times narrower* (e.g., if T=8, a full-precision GNN with dimension d/8). This is not "comparable expressiveness" with the same-size full-precision GNNs the paper benchmarks against (which use d=256–512). The theorem's guarantee is about a weaker reference model, so the paper's central theoretical claim is overstated. This does not invalidate the empirical results, but it means the theory cannot be cited as supporting the main claim as written.

2. **Blockwise training is proposed as a contribution but never experimentally validated** — Section 4.4 introduces blockwise training to address vanishing gradients in deep SNNs and lists it as a main contribution ("We address the challenge of training deep SNNs with a simple blockwise learning paradigm" — Contribution 3). However, the experiments contain *no comparison* between blockwise training and standard end-to-end surrogate gradient training within the same SpikeGCL framework. Without this ablation, the reader cannot determine whether blockwise training helps, hurts, or is even necessary. The baseline SNN methods (SpikingGCN, SpikeNet, GC-SNN, GA-SNN) all use end-to-end surrogate gradients and are compared against as black boxes, so the claimed advantage of blockwise training is entirely unsubstantiated.

3. **Theoretical energy consumption numbers lack a documented methodology** — Table 2 (efficiency) reports energy in mJ with no explanation of how these values are computed. The caption says "theoretical energy consumption" but no energy model, operation costs, spike rate assumptions, or technology node is stated. The wild variation across baselines on the same dataset (e.g., Computers: DGI 0.5 mJ, GRACE 1.1 mJ, CCA-SSG 17 mJ, BGRL 25 mJ — a 50× range) suggests uncontrolled architectural differences. Without a documented methodology, these numbers cannot be verified or meaningfully compared. This undermines the paper's core efficiency claims.

### Minor

1. **No experimental setting details reported** — The paper does not report the hidden dimension d, the time step T used in Table 1, the number of layers L, the margin m in the ranking loss, the optimizer and learning rate, or the number of blocks in blockwise training. This makes the results difficult to reproduce and the design choices impossible to evaluate.

2. **No ablation of the feature grouping strategy** — The partitioning of features into non-overlapping groups (Section 4.1) is a central design choice, but there is no ablation comparing it against an alternative that processes the full feature vector (e.g., repeating the graph as in SpikingGCN, or using a different SNN input encoding). Without this, it is unclear whether the 1–2 point accuracy gap relative to the best full-precision methods stems from the grouping strategy or from binarization itself.

3. **The margin m in the ranking loss is never studied** — The margin ranking loss (Eq. 1) depends on a hyperparameter m, described as important for focusing on hard negatives. No sensitivity analysis or even the chosen value is reported.

4. **Abstract/contribution overclaim relative to Table 1** — The contribution list states SpikeGCL "performs on par with or even sometimes better than advanced full-precision competitors." In Table 1, SpikeGCL never achieves the top accuracy on any dataset; it trails the best full-precision method by 0.1–1.4 percentage points. "On par with" is fair (the gaps are small), but "sometimes better" is not supported by the presented data.

### Trivial

None with sufficient confidence — all observed presentation issues (e.g., the informal theorem statement, vague blockwise training description) are substantive enough to appear above.

## Nice-to-Haves

- An analysis of spike sparsity (firing rates) would directly validate the energy-efficiency mechanism and is standard practice in SNN papers.
- A study of the representation bitwidth trade-off (1-bit vs. 2-bit vs. 4-bit) would characterize the Pareto frontier of accuracy vs. efficiency.
- A justification for preferring margin ranking loss over InfoNCE/NT-Xent would strengthen the contrastive learning section.
- Ablation of different spiking neuron models (IF vs. LIF vs. PLIF) would demonstrate the robustness of the framework.

## Removed Points

The following points from the input reviews are removed with justification:

- **"The 32x compression is a property of any binarized representation, not specific to SpikeGCL"** — True but irrelevant to evaluating the paper. The paper's contribution is learning *useful* binarized representations, not inventing binarization itself.
- **"The grouping strategy fundamentally limits expressiveness" as a fatal flaw** — This is a plausible hypothesis but is speculative without an ablation test. It is retained as Minor weakness #2 (missing ablation) rather than a fatal structural flaw.
- **"Missing appendix" and "missing proofs in appendix"** — The appendix is stripped by the PDF parser; this is an artifact of the review format, not an author error.
- **"SpikeGCL never outperforms the best method" (as an overriding criticism)** — The abstract says "outperforms *many*" not "outperforms *all*." SpikeGCL does outperform GCN, GAT, Bi-GCN, BinaryGNN, DGI, and GRACE on several datasets. The overclaim is specifically about "sometimes better than advanced full-precision competitors" (Contribution 4), which is retained as Minor #4.
- **Strength Finder's "Blockwise training mitigates vanishing gradients" (as a strength)** — This is a *claimed* contribution but is not experimentally validated. It cannot be listed as a confirmed strength; it is a proposal. The weakness about it being unvalidated is retained as Major #2.
- **Critic's claim that "the feature grouping may be capping performance" is a category-concern sweep** — It is not a specific identified problem but an area-of-concern speculation. The absence of an ablation is a concrete weakness (Minor #2), not evidence of a fundamental cap.
- **Formatting/style nitpicks, speculation about "could be" issues** — Removed per instruction.

## Novel Insights

None beyond the paper's own contributions. The combination of SNNs with GCL for binary representations is itself the novel contribution. The reviews did not surface a higher-level insight not already present in the paper. The key tension — that Theorem 1's comparative model (dimension d/T) is weaker than the actual full-precision baselines — was identified by the critic and is a real gap between the paper's framing and its evidence, but it is a limitation of the paper rather than a novel observation about the field.

## Suggestions

1. **Align the theory with the claim**: Either (a) retarget Theorem 1 to compare against a full-precision GNN of hidden dimension d (not d/T) if such a result holds, or (b) revise the abstract and introduction to accurately describe what the theorem guarantees — that SpikeGCL approximates a *narrower* full-precision GNN, and that the empirical results show competitive performance with *full-size* GNNs despite this theoretical gap.

2. **Ablate blockwise training**: Add an experiment comparing SpikeGCL trained with blockwise training vs. standard end-to-end surrogate gradient backpropagation-through-time, keeping all other components identical. If blockwise training is truly beneficial for large T, this comparison will demonstrate it; if not, the claim should be removed or downgraded.

3. **Document the energy model**: Provide a complete, reproducible description of how theoretical energy is computed for all methods, including operation costs (e.g., energy per MAC vs. per spike), assumed spike rates (for SNN methods), hidden dimensions used by each baseline, and any normalization applied. Without this, the efficiency table is unverifiable.

4. **Report experimental configurations**: State the hidden dimension d, the T used in Table 1, the number of layers L, the margin m, and the block size (number of time steps per block) for every dataset. This is necessary for reproducibility.

5. **Add the missing grouping ablation**: Compare SpikeGCL against a variant that processes the full feature vector (e.g., by repeating the graph T times) while keeping the same encoder architecture, spiking neuron, and training procedure. This isolates the effect of the grouping design.
