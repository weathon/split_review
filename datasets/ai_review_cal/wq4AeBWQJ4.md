- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

GROOT presents an algorithm-system co-design framework for GNN-based verification of large circuit designs on a single GPU. The approach combines domain-specific 4-bit node features (encoding node type and edge polarity), graph partitioning with boundary edge re-growth to fit large graphs into GPU memory, and custom GPU kernels (HD-kernel and LD-kernel) optimized for the polarized degree distribution observed in EDA graphs. Evaluated on CSA multipliers, Booth multipliers, and technology-mapped circuits, GROOT achieves up to 59.38% memory reduction (enabling single-GPU processing of a 134M-node 1024-bit CSA multiplier that would otherwise require multiple GPUs), 99.96% classification accuracy, and a 1.23×10⁵× speedup over the traditional ABC tool.

## Strengths

1. **Domain-aware node features with clear justification**: The 4-bit feature encoding (Section 3.2, Fig. 3c) distinguishes PI, PO, internal nodes, and input-edge polarity — a concrete improvement over GAMORA's 3 features. The encoding is well-explained with explicit examples.

2. **Partitioning + edge re-growth enables single-GPU processing of previously infeasible graphs**: The memory reduction results (Section 5.2, Fig. 8) are the paper's strongest empirical contribution. On a 1024-bit CSA multiplier with batch size 16 (134M nodes, 268M edges), GROOT reduces memory by 59.38%, enabling processing where GAMORA runs out of memory even on multiple GPUs (Table 2).

3. **Custom GPU kernels tailored to EDA workload**: The HD-kernel and LD-kernel design (Section 4, Figs. 4, 5) is detailed with concrete mechanisms (static workload partitioning, tree-based accumulation, degree sorting, row-assembling). The kernels achieve up to 10.28× acceleration over GNNAdvisor on Booth datasets (Fig. 10), demonstrating domain-specific kernel design matters.

4. **Dramatic and well-documented speedup over traditional verification**: GROOT achieves 1.23×10⁵× speedup over ABC for 1024-bit CSA multipliers (Section 5.3, Fig. 9a), with runtime comparable to GAMORA while using only a single GPU — a practically meaningful result.

5. **Size generalization without retraining**: Training on 8-bit multipliers and testing on up to 1024-bit multipliers (Section 5.1) demonstrates non-trivial transfer, and the paper honestly reports when this fails (tech-mapped/FPGA circuits showing lower accuracy).

## Weaknesses

### Fatal
None.

### Major

1. **Partitioning and edge re-growth algorithms are not specified** — The paper's title and framing center on "graph edge re-growth" and "graph partitioning," yet (i) the graph partitioning algorithm is never named or described (Section 3.3 merely states "we utilize a graph partitioning algorithm"), and (ii) the boundary edge re-growth approach that recovers accuracy is mentioned repeatedly in results (Sections 5.1, 5.3) but never defined algorithmically. These are listed as key contributions (Section 1, contribution ii), but the reader cannot evaluate, reproduce, or even understand what was actually done. This is a structural gap: for a paper whose methodology is central, the lack of specification undermines the contribution's verifiability.

2. **"Verification accuracy" actually measures node classification, and end-to-end verification success is not reported** — Figures 6–7 and the abstract report "verification accuracy," but the actual metric is node classification accuracy for detecting XOR/MAJ gates (Section 5.1; Section 3.3 describes the pipeline). While classification accuracy is relevant — incorrect gate detection would break algebraic rewriting — the paper never validates that the 99.96% classification accuracy translates to successful verification (e.g., what fraction of equivalence checks pass?). The 100% accuracy reported for several CSA multiplier configurations (Fig. 6a–b) is unusual and, without variance measures or harder test cases, raises questions about task difficulty rather than confirming method strength.

3. **Missing ablations on key design choices** — Several central claims lack isolation experiments: (a) No ablation comparing 4-node features vs. GAMORA's 3-node features (Section 3.2 claims superiority but never isolates this variable). (b) No ablation comparing different partitioning strategies (e.g., METIS vs. random vs. spectral) to show the chosen approach is responsible for the results. (c) No ablation of edge re-growth vs. no re-growth for the same partition count — the recovery numbers (8.7%, 12.62%) are cited, but it is unclear how much of the "recovery" is from re-growth vs. inherent graph redundancy. (d) No comparison against a simpler baseline such as training GraphSAGE on full graphs (where memory permits) to measure how much partitioning itself hurts accuracy.

4. **Generalization mechanism is unexplained** — Training on 8-bit and testing on up to 1024-bit multipliers (Section 5.1) is a striking result, but the paper provides no analysis of why this works. No representation analysis (e.g., feature distribution comparison across sizes, t-SNE of learned embeddings) is offered. The explanation ("structural regularity of multipliers") is a post-hoc assertion, not a demonstrated property. The tech-mapped results (accuracy <80%, Fig. 6d) and FPGA results (~71–90%, Fig. 7) suggest the method transfers poorly outside highly regular structures, but the paper does not analyze what structural differences cause this.

### Minor

1. **10% boundary edge claim is asserted without evidence** — The observation that "approximately only 10% of boundary edges (nodes) between clusters" (Sections 1, 3.3) is central to the partitioning motivation but is never empirically demonstrated with the datasets used. Showing the distribution across graph sizes and types would strengthen the motivation.

2. **GPU kernel evaluation is decoupled from end-to-end pipeline** — The kernel runtime comparison (Fig. 10) measures SpMM operations in isolation against generic kernels (cuSPARSE, MergePath-SpMM, GNNAdvisor). While this is informative, the paper never measures the contribution of the custom kernels to end-to-end verification runtime (Fig. 9 uses the full GROOT framework). The paper would benefit from an ablation showing total verification time with vs. without the custom kernels (substituting generic SpMM).

3. **No variance or confidence measures reported** — Accuracy results (Section 5.1) are reported as single deterministic numbers without error bars, confidence intervals, or runs across multiple seeds. For a learned system, this makes it impossible to assess result stability.

### Trivial

- The claim about tree-based accumulation saving "about half the number of cycles compared to AtomicAdd" (Section 4) is stated without experimental measurement.
- The "wid" variable in the HD-kernel description (Section 4) appears to mean "width" but is not formally introduced before use.

## Nice-to-Haves

- An ablation comparing GraphSAGE against other GNN architectures (GCN, GAT) would strengthen the claim that the method works well with the chosen model.
- A discussion of limitations — the paper does not acknowledge that the approach is tuned to structured multiplier-like circuits and may not generalize to arbitrary netlists, even though the evidence (tech-mapped, FPGA results) suggests this.
- Reporting end-to-end verification success rate (i.e., what fraction of equivalence checks pass after XOR/MAJ detection) would directly validate the practical claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Table 1 referenced but not shown"** — The parser strips tables; the table exists in the original submission. (Parser artifact)
- **"Missing related works on GNN scalability techniques"** — Per policy, missing related works are not evaluated as weaknesses. (Policy rule)
- **"warpmax and nz_max hyperparameters not specified"** — Per policy, undisclosed hyperparameters for configurable kernel parameters are considered reproducibility nitpicks, not substantive weaknesses. (Policy rule)
- **"Batch processing essential for GPU throughput is asserted without support"** — This is a standard, widely accepted claim in GPU computing, not a weakness. (Factually standard)
- **"Missing appendix content / proofs"** — The parser strips appendices from all papers; they exist in the original submission. (Parser artifact)
- **General-area-of-concern sweep points** (e.g., "evaluation lacks rigor" without a specific anchor) — Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's stated findings — the memory reduction and size generalization are genuinely noteworthy — and properly identify the main methodological gap (underspecified algorithms) without introducing surprise insights.

## Suggestions

1. **Specify the partitioning algorithm** (name the method, state its objectives/constraints) and **provide pseudocode or a citation+description of the edge re-growth algorithm**. This is the single most important revision.
2. **Rename "verification accuracy" to "gate classification accuracy"** or, better, report end-to-end verification success rate directly.
3. **Add ablations**: (a) 4-feature vs. 3-feature comparison; (b) different partitioning strategies; (c) edge re-growth vs. no re-growth at matched partition counts; (d) end-to-end runtime with vs. without custom kernels (substituting generic SpMM).
4. **Provide variance measures** (e.g., multiple random seeds for training, error bars on accuracy plots).
5. **Analyze the 8-bit → 1024-bit generalization** with a brief representation analysis (e.g., feature space overlap, difficulty calibration) to move beyond post-hoc explanation.
