## Summary

GROOT is an algorithm-system co-design framework for GNN-based circuit verification on single GPUs. It combines (i) 4-bit AIG-aware node features (node type + input-edge polarity), (ii) graph partitioning with a boundary edge re-growth mechanism that recovers accuracy lost from partitioning, and (iii) two custom CUDA SpMM kernels (HD-kernel, LD-kernel) optimized for the polarized degree distribution of EDA graphs. The evaluation targets XOR/MAJ gate detection in large multipliers (CSA, Booth, technology-mapped), reporting 99.96% accuracy on a 1,024-bit CSA with 134M nodes at 59.38% memory reduction, ~1.23×10⁵× speedup over the traditional ABC tool, and up to 10.28× kernel-level speedup over GNNAdvisor.

## Strengths

- **Enables single-GPU inference on graphs that previously required multiple GPUs or were infeasible.** GROOT reduces memory footprint by 59.38% for a 1,024-bit CSA multiplier with batch size 16 (134M nodes, 268M edges), fitting it on a single A100 80GB where even that GPU would otherwise be insufficient (Figure 8(b)). This is a concrete scalability result that addresses a documented limitation of prior work (GAMORA requires multi-GPU, as noted on the introduction).

- **Boundary edge re-growth recovers substantial accuracy lost from partitioning.** The paper reports specific accuracy recoveries of 8.7% for a 32-bit CSA multiplier (Section 5.1) and 12.62% for a 32-bit Booth multiplier via the re-growth approach. This mechanism is the key algorithmic innovation that makes aggressive partitioning feasible without collapsing GNN message-passing quality.

- **Custom GPU kernels exploit the polarized degree distribution of EDA graphs and