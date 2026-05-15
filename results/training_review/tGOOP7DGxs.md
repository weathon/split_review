Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes KRAKEN, a graph transformer framework for large-scale graphs (millions to billions of nodes). Its core technical innovation is a tokenization strategy (Algorithms 1–2) that combines offline 2-hop neighbor sampling with precomputed 1-hop and 2-hop context features, enabling a claimed 4-hop receptive field through only 2-hop operations. A local Transformer module processes these tokens, and a global module (adapted from GOAT) uses a fixed-size codebook for linear-complexity global attention. The framework is validated on ogbn-products, snap-patents, and ogbn-papers100M, reporting a 3× speedup, a 16.8% gain on snap-patents, and a 5.9% improvement on ogbn-papers100M over constrained baselines.

## Strengths

- **Strong empirical results on non-homophilic and massive graphs.** On snap-patents (non-homophilic), KRAKEN-full achieves 70.21% accuracy vs. the best constrained baseline NAGphormer-ns2 at 60.11% — a 16.8% absolute improvement. On ogbn-papers100M (111M nodes), KRAKEN-full achieves 64.73% vs. GOAT-full-ns2's 61.12% (+5.9%) within a 48-hour budget, demonstrating genuine scaling to one of the largest public graph benchmarks.

- **Principled framework design with explicit criteria.** The paper defines two design principles — Model Capacity (D1: local + global information) and Scalability (D2: efficient 2-hop retrieval, constant-complexity global module, and potential distributed deployment) — and builds KRAKEN to satisfy them jointly. This provides a reusable recipe for future large-graph Transformer work beyond the specific method.

- **Offline sampling decouples graph access from training.** Algorithm 1 (LocalNodes) samples neighbor sets offline on CPU before training, can be parallelized across cores and machines, and does not require the full graph to reside in a single machine's memory. This converts large-graph learning into a standard sequence learning problem on fixed tokens, a practical advantage for billion-node graphs where in-memory adjacency is infeasible.

## Weaknesses

### Fatal
None.

### Major

- **On ogbn-products, KRAKEN does not outperform all baselines under the same 2-hop constraint.** KRAKEN-full (79.81%) is beaten by GOAT-local-ns2 (81.17%), a simpler local-only model. The paper describes KRAKEN as "competitive" but does not explain why adding the local Transformer + global module actually *hurts* performance relative to a cheaper local baseline. This weakens the claim that the tokenization design is broadly superior, and raises the question of whether the global module or the Transformer-based local aggregation is necessary on homophilic graphs where GOAT's simpler local mechanism is both better and faster.

- **The "4-hop receptive field through 2-hop operations" claim is not rigorously validated.** The mechanism relies on precomputed context features C⁰ = ÃH and C¹ = Ã²H being retrieved for each sampled neighbor. The paper provides no ablation comparing versions with only node features, only 1-hop context, only 2-hop context, or concatenating them differently. It also does not compare against an actual 3-hop or 4-hop sampling baseline to show the proposed approximation is beneficial. Without such validation, it is unclear whether the claimed 4-hop access is genuinely driving improvements or is simply leveraging smoothed feature aggregations that could be replicated with 1-hop or 2-hop precomputed features alone.

- **On ogbn-papers100M, only a single baseline is compared.** The paper acknowledges this is due to computational constraints, but a single comparison against GOAT-full-ns2 is insufficient to substantiate the claim that KRAKEN "scales" better than existing approaches on the largest benchmark. Other scalable methods (e.g., GraphSAGE, NAGphormer with similar constraints) are absent. While the absolute improvement (64.73 vs. 61.12) is notable, the lack of baselines limits confidence in the generality of the result.

### Minor

- **GT-sparse-ns2 reports zero standard deviation (60.76±0.00 on ogbn-products, 47.81±0.00 on snap-patents) across 4 runs.** A zero standard deviation on a stochastic task is suspicious and could indicate collapsed predictions, a bug in the evaluation, or numerical issues. The paper does not comment on this.

- **The runtime comparison lacks hardware specifications.** Figure 1 reports per-epoch training times but does not state the GPU/CPU hardware used, the batch sizes, or implementation details. Since speed comparisons between models with different codebases and optimization levels are sensitive to these factors, the 3× speedup claim is less informative than it could be.

- **No ablation isolating the tokenization components.** The paper evaluates KRAKEN-local vs. KRAKEN-full (i.e., local module vs. local+global), but does not ablate within the local module itself (e.g., using only node features H without context features C, or using only 1-hop context features). This would help attribute improvements to specific design choices.

- **The distributed training capability is mentioned as a design criterion (D2) but never tested.** While the paper correctly argues that offline sampling enables distributed deployment in principle, no experiment demonstrates this in practice. An experiment partitioning the graph across machines would strengthen the scalability claims considerably.

### Trivial

- **The abstract's phrasing "3× speedup and 16.8% performance gain on ogbn-products and snap-patents" is ambiguous.** A casual reader could misread this as both metrics applying to both datasets. Clarifying the "respectively" distribution (speedup on ogbn-products, gain on snap-patents) in the abstract would help.

- **The paper's constraint suffix (\textbackslash constraintname) is never explicitly spelled out** (e.g., "ns2" or "2-hop") in the main text, though the caption in Table 1 clarifies it means "only up to 2-hop computations."

## Nice-to-Haves

- Compare against unconstrained versions of GOAT and NAGphormer to show KRAKEN is competitive with them despite the 2-hop constraint.
- Measure and report the precomputation cost for C⁰ and C¹ on ogbn-papers100M, since this is a one-time overhead that affects total time-to-accuracy.
- Analyze qualitatively what the global module contributes on snap-patents (e.g., attention weights to distant nodes), which would strengthen the D1 narrative.
- Report standard deviations for epoch-time measurements.

## Removed Points

*These points were flagged for removal by the meta-reviewer due to factually incorrect claims, strawman arguments, or parser artifacts. They are noted here in case the human evaluator wishes to consult them.*

- **"The paper does not specify the number of layers."** — *Factually wrong.* The paper states on line 223: "We implement single layer of Transformer encoder in the local and global modules," with a footnote explaining why multi-layer was not used.
- **"Hyperparameters are in an appendix that is stripped."** — *Parser artifact.* The appendix exists in the original submission but was stripped by the PDF-to-text pipeline.
- **"The paper's headline results are based on comparing against intentionally weakened versions, not stated clearly enough — systematic misrepresentation."** — *Not supported.* The paper consistently uses the "-\constraintname" suffix for all constrained baselines and explicitly states in Section 4.1: "The goal of our experimental setup is to show how the scalability constraints affect existing models' capabilities, which can be addressed by \frameworkname{}." The abstract and introduction also reference "scalable setting" and "scalable baselines." The evaluation protocol is transparent, not misleading, though the abstract's phrasing could be clearer.
- **"Computing C¹ = Ã²H is computationally prohibitive for ogbn-papers100M."** — *Overstated.* C¹ can be computed as Ã(ÃH) — two sparse-dense matrix multiplications — without explicitly forming Ã², which is efficient for graphs with billion edges. The paper's notation is standard.
- **"Ablation vs. unconstrained baselines required."** — *Scope creep.* The paper's stated scope is evaluating models under the D2 scalability constraint (2-hop only); comparing against unconstrained models that violate D2 is outside this scope.
- **"Algorithm 1 samples from the full node set when neighborhood is empty — this makes tokens meaningless for disconnected graphs."** — *Standard fallback used in many GNN sampling papers. Not a meaningful weakness without evidence that this case occurs frequently in the evaluated datasets.*

## Novel Insights

The most interesting finding from the reviews, beyond the paper's own contributions, is the sharp performance reversal between KRAKEN and GOAT-local across homophilic vs. non-homophilic datasets. On ogbn-products (homophilic), GOAT-local-ns2 (81.17) beats KRAKEN-full (79.81), yet on snap-patents (non-homophilic), GOAT-local-ns2 collapses to 40.95 while KRAKEN-full achieves 70.21. This suggests that KRAKEN's Transformer-based local module with precomputed context features is qualitatively better at leveraging long-range structural information when local homophily breaks down — but on highly homophilic graphs, GOAT's simpler local MPGN may actually be more effective. The paper does not discuss this inversion, but it points to an interesting trade-off: the added complexity of KRAKEN's local tokenization may only pay off on non-homophilic or long-range tasks. This is worth investigating as a potential failure mode or as guidance for practitioners choosing between the two architectures.

## Suggestions

1. **Ablate the tokenization design.** Compare KRAKEN-local against variants using: (a) only raw node features H (no context), (b) only 1-hop context C⁰, (c) only 2-hop context C¹. This would validate the 4-hop receptive field claim and identify which component drives the gains.

2. **Investigate and explain the ogbn-products failure case.** KRAKEN-full underperforms GOAT-local-ns2 on ogbn-products. A careful analysis (e.g., does the global module degrade representations? Is the Transformer local module overfitting?) would strengthen the paper and guide future improvements.

3. **Run at least one additional baseline on ogbn-papers100M** (e.g., NAGphormer-ns2 with constrained sampling) to make the scalability claim more robust.

4. **Report hardware specifications** for all runtime measurements, and consider including a runtime breakdown (precomputation vs. training per epoch) to clarify the 3× speedup claim.

5. **Explain the zero standard deviation of GT-sparse-ns2** — either as a known property of the model under the 2-hop constraint, or as a potential bug to be fixed.

6. **Clarify the abstract's "respectively" construction** to avoid any ambiguity about which metric applies to which dataset.

## Score and Decision

This paper addresses an important and timely problem — scaling graph transformers to graphs with 100M+ nodes — and presents a technically sound framework with a clear design rationale. The strongest evidence (16.8% gain on snap-patents, 5.9% on ogbn-papers100M) supports the core claim that the framework can scale effectively. However, the paper has notable weaknesses: the ogbn-products results do not support the superiority claim even under the paper's own constraints, the 4-hop receptive field is not ablated, and the largest-dataset evaluation is thin. These are addressable with additional experiments but reduce confidence in the current presentation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>