Now I have all the information I need. Let me consolidate the final review.

---

## Summary

This paper proposes SpikeGCL, the first framework to integrate spiking neural networks (SNNs) with graph contrastive learning (GCL) to produce binarized (1-bit) node representations. The key ideas are: (i) partitioning node features into T non-overlapping groups to create sequential inputs for SNNs without repeating the full graph, (ii) using spiking neurons to emit binary spike trains as representations, (iii) a blockwise surrogate gradient training strategy to mitigate vanishing gradients, and (iv) a theoretical guarantee linking SNN expressiveness to that of full-precision GNNs. Experiments on 6 datasets show SpikeGCL achieves 95–99% of the accuracy of full-precision GCL methods while offering substantial storage compression (~32×) and parameter reduction.

## Strengths

- **First integration of SNNs with GCL for binarized representations.** The paper explicitly states (line 56) it is "the first to explore the feasibility of implementing graph self-supervised learning with SNNs for learning binarized representations." This opens a genuinely new direction at the intersection of efficient graph learning and neuromorphic computing.

- **Feature grouping strategy provides real computational benefits over prior graph SNNs.** Unlike prior approaches (SpikingGCN, SpikeNet) that repeat the entire graph T times, SpikeGCL partitions node features into T non-overlapping groups (§3.1). This yields direct memory and computational advantages — SpikeGCL scales to OGB datasets (arXiv, MAG) while SpikingGCN and SpikeNet run out of memory or time out (Table 1 footnotes).

- **Competitive accuracy on 6 datasets despite binary representations.** On Computers, SpikeGCL achieves 88.9% vs. 90.3% (BGRL); on Photo 93.0% vs. 93.5% (GA-SNN); on arXiv 70.9% vs. 71.6% (BGRL/GGD); on MAG 32.0% vs. 32.4% (SUGRL). These results demonstrate that binarized representations can approach full-precision performance when properly trained.

- **Substantial parameter and storage compression.** Table 2 shows SpikeGCL uses 6.6 KB parameters on MAG vs. 246.4 KB average for full-precision GCL methods, and achieves ~32× representation storage compression (1-bit vs. 32-bit). The parameter sharing strategy (§3.2) across peer GNNs is a practical design that enables this efficiency.

- **Bi-level augmentation tailored to SNN characteristics.** Feature shuffling (§3.3) exploits the sequential feature-partitioning design to create hard negatives, a motivated architectural choice that contributes to the contrastive learning effectiveness.

## Weaknesses

### Major

- **Missing results on three standard benchmark datasets (Cora, CiteSeer, PubMed).** The paper lists these three citation graphs among its 9 adopted datasets in §6 (line 233), but Table 1 only reports results on 6 datasets (captioned "six large scale datasets"). These three are among the most widely used transductive benchmarks in GCL and appear consistently in the baselines the paper compares against (DGI, GRACE, CCA-SSG, BGRL, SUGRL, GGD). Their omission from the evaluation table is a structural gap: the reader cannot assess how SpikeGCL behaves on smaller, sparser graphs where GCL methods face different challenges, nor compare directly to standard leaderboards. This is the highest-priority issue to address.

- **The theoretical guarantee (Theorem 3.1) has a significant gap relative to the paper's claims.** The theorem states an approximation bound between *firing rates* of SpikeGCL and a full-precision GNN *whose hidden dimension is d/T* — not d. However, the full-precision GCL methods the paper compares against in experiments operate at the *full* hidden dimension d. The theorem therefore compares the SNN to a reduced-capacity full-precision model, not to the actual models used in the experimental evaluation. The paper's claim that "ours has comparable expressiveness with its full-precision counterparts" (abstract, line 43) is not supported by this theorem in the way a reader would naturally interpret it. Additionally, the theorem analyzes firing rates (rate coding), while the actual training uses binary spike trains directly (with a projection head to continuous space), creating a second disconnect between theory and practice. The paper acknowledges (§5) that "the approximation is defined using the firing rates... which measures only a restricted set of inductive biases," but this does not resolve the d/T vs. d issue.

### Minor

- **No ablation of blockwise vs. end-to-end surrogate gradient training.** The paper presents blockwise surrogate gradient learning (§4.4) as a central contribution for addressing vanishing gradients in deep SNNs, yet provides no experiment comparing it to standard end-to-end surrogate gradient learning for SpikeGCL itself. Without this control, it is unclear whether (a) blockwise training actually helps, (b) vanilla surrogate gradient training suffers from vanishing gradients in this setting, or (c) any benefit comes from the local contrastive objectives rather than the gradient cutoff. Figure 4 compares SpikeGCL to other SNN methods but does not isolate this variable.

- **Energy efficiency methodology is underspecified and contains internal inconsistencies.** The paper reports "theoretical energy consumption (mJ)" in Table 2 and claims "up to ~7x energy reduction" (line 50) and "~7x less energy consumption" on MAG (line 285), yet Table 2 shows SpikeGCL at 0.18 mJ vs. 1279.1 mJ average on MAG — a ~7106× improvement, not ~7×. The 13× improvement on Computers (0.038 vs. 0.5 for DGI, the most efficient full-precision baseline) also exceeds the "~7x" claim. These internal inconsistencies, combined with the absence of any description of the energy calculation methodology (AC vs. MAC operations? hardware model? spike rates? equation or formula?), make the energy numbers unverifiable. The paper does provide empirical training time and memory usage in Figure 4, but the energy figures specifically lack methodological grounding.

- **Key hyperparameter T (number of time steps) not reported for main experiments.** T is a critical design choice that controls the accuracy-efficiency trade-off, and the paper varies it from 5 to 30 in Figure 4. However, the specific T value used for the main experimental results in Table 1 is never stated. This makes the results difficult to reproduce.

- **Evaluation protocol for linear classification is not described.** The paper does not specify how the linear classifier is trained (epochs, learning rate, weight decay, split ratio, number of runs/seeds for the variance estimates in Table 1). Standard practice in GCL papers includes these details.

- **The paper does not discuss training-time costs.** The conclusion (§7) does not acknowledge that SNNs with surrogate gradients still require backpropagation through time during training, and the claimed energy savings are primarily inference-time benefits. Training-time GPU memory and time are partially covered in Figure 4 but not discussed qualitatively.

### Trivial

- No explicit limitations section, though the paper acknowledges some caveats inline (e.g., "restricted set of inductive biases" in §5).

## Nice-to-Haves

- A direct comparison between SpikeGCL and a full-precision version of the *same architecture* (same grouping strategy, same encoder — but with ReLU instead of spiking neurons and continuous outputs) would isolate the cost of binarization and strengthen the core claim.
- Empirical runtime and peak memory measurements on a real device (CPU/edge) for all baselines would substantiate the efficiency claims beyond theoretical estimates.
- An ablation of the margin ranking loss vs. more common GCL objectives (InfoNCE, Barlow Twins) would justify the design choice.

## Removed Points

- *"The comparison to binarized methods is difficult to interpret because Bi-GCN and BinaryGNN are supervised"* — The table clearly marks methods with U/S/B columns. While the protocols differ, the comparison is standard and transparent. **Removed** because the paper already labels methods by type.
- *"Figure 4 does not isolate the effect of T on SpikeGCL alone"* — Figure 4 does show SpikeGCL's own metrics as T varies; it is the other three subfigures that show it alongside competitors. **Removed** as factually incorrect.
- *"The 32× storage compression applies only to final representations, not intermediate activations during training"* — This is standard for representation compression claims; training-time intermediate storage is a separate concern. **Removed** as scope creep.
- *"The contrastive objective (margin ranking loss) is unusual for GCL"* — A preference point, not a weakness. **Moved to Nice-to-Haves.**
- *"The paper should also cover more tasks/datasets"* — Would turn this into a broader paper. **Removed** as scope creep.
- *Pure formatting/style nitpicks, missing appendix references, reproducibility complaints about trivial details* — All removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the theoretical guarantee and the actual experimental comparison (d/T vs. d), and the inconsistency between the claimed "~7×" energy savings and the far larger numbers in Table 2 — but neither reviewer identifies a structural blind spot the authors themselves could not have anticipated.

## Suggestions

1. **Add results on Cora, CiteSeer, PubMed** to Table 1 (or a separate table). These are the standard benchmarks for GCL and their absence is the single most glaring omission.
2. **Report the specific T value** used for each dataset in the main experiments, and describe the linear evaluation protocol (split, learning rate, epochs, seeds).
3. **Disclose the energy calculation methodology** — provide the formula, state whether AC vs. MAC operations are counted, specify the assumed hardware energy cost and spike rates. Reconcile the "~7×" claim with the actual table values.
4. **Add an ablation of blockwise vs. end-to-end surrogate training** on at least one medium-sized dataset to validate the vanishing-gradient claim.
5. **Clarify the theoretical claim**: explicitly state that Theorem 3.1 compares to a GNN of dimension d/T (not d), and discuss the implications for the paper's expressiveness claims. If possible, extend the analysis or add a discussion of why the d/T comparison is meaningful.

## Score and Decision

This paper tackles a timely and genuinely novel direction — the first to bring SNNs into graph contrastive learning for binarized representations. The core idea is sound, the feature grouping strategy is a practical improvement over prior graph SNNs, and the empirical results on 6 datasets are competitive. However, the evaluation is incomplete (missing 3 standard benchmarks), the theoretical guarantee does not align with the experimental comparisons it claims to support, a central methodological contribution (blockwise training) is unablated, and the efficiency claims rest on an opaque energy methodology with internal inconsistencies. These issues are all addressable with additional experiments and clarifications, but in their current state they weaken the paper's evidence for its core claims.

**Score: 5.5/10** — a paper with a promising direction and genuine contributions, held back by significant but fixable gaps in evaluation and presentation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>