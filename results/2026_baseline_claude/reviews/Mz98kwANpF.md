## Summary

This paper challenges the prevailing paradigm in multi-task LoRA fine-tuning that structural diversity (via multiple specialized adapters/heads) is the key to effective MTL performance. Through a series of controlled ablations, the authors first show that a simplified multi-head LoRA (M-LoRA) with *high* inter-head similarity outperforms complexity-focused methods like R-LoRA and HydraLoRA. They further demonstrate that simply increasing the rank of a standard single-adapter LoRA matches or exceeds these multi-component architectures at comparable parameter budgets. Building on these observations, they propose Align-LoRA, which adds a KL-divergence-based alignment loss to encourage shared task representations in the down-projection matrix A, with zero additional inference overhead (weights remain mergeable).

---

## Strengths

- **Well-supported counter-intuitive finding**: The M-LoRA paradox (Section 3.2) is compellingly demonstrated with quantitative inter-head similarity measures (Figure 2) and Table 1 performance numbers. The finding that the highest-similarity heads (M-LoRA ~0.85 median cosine similarity) outperform diversity-enforced variants is a genuine, surprising empirical contribution that challenges the design philosophy of prior work.

- **Align-LoRA-K shows consistent gains across models and scales**: Table 4 and Table 5 demonstrate that the KL-divergence variant achieves the highest performance across Qwen2.5-3B, 7B, 14B and LLaMA3-8B with *fewer* trainable parameters (0.20%) than competitors (0.25%). In Table 5 on the 8-task benchmark, A-LoRA-K beats the next-best method (M-LoRA, 78.51) by 1.55 points on 3B and 1.49 points on 7B.

- **Practical advantage**: Unlike multi-component LoRA variants with non-mergeable routers, Align-LoRA incurs zero inference latency. This is a meaningful practical distinction, not just a theoretical one.

- **Robustness analysis**: The hyperparameter sensitivity sweep (Figure 3) shows consistent improvement over baselines for λ ∈ [0.01, 0.50], suggesting the method is not tuned to a narrow operating range.

- **Cross-model validation**: The rank-scaling experiment (Tables 2–3) is conducted on LLaMA2 (7B, 13B) and Qwen2.5 (7B, 14B), providing evidence that the finding is not architecture-specific.

---

## Weaknesses

### Fatal
None.

### Major

1. **Overstated claims about A-LoRA-M**: Throughout the paper, the authors assert that "both A-LoRA-K and A-LoRA-M significantly outperform the baselines," but this is factually incorrect in several places. In Table 4, A-LoRA-M scores 47.53 on Qwen2.5-7B, which is *below* baseline LoRA (48.36), M-LoRA (48.44), and R-LoRA (48.32). In Table 5, A-LoRA-M (78.35 and 82.31) consistently lags behind M-LoRA (78.51 and 82.46) on both model scales. The consistent underperformance of A-LoRA-M relative to M-LoRA in the multi-task adaptation setting contradicts the paper's claim that representation alignment via MMD is a validated general strategy. The paper does not explain why the MMD and KL variants diverge so starkly or under what conditions each is appropriate.

2. **Theoretical bound conflates representation and data distributions**: The generalization bound in Section 5.3 includes the term `(λ/M) Σ Δ(D_i, D_j)`, where `Δ(D_i, D_j)` is described as the data distribution discrepancy between tasks. The alignment loss, however, operates on low-dimensional representations `φ_{T_i}(x) = A · X̃_{T_i}` — outputs of the down-projection in the latent space, not the raw data distributions. The bound implicitly assumes that reducing representation-level KL divergence reduces data-level discrepancy, but this connection is not established. Additionally, the same symbol `λ` appears both as the training hyperparameter controlling alignment loss weight *and* as a bound coefficient, conflating two distinct quantities unless their equivalence is formally justified. This weakens the theoretical contribution substantially.

### Minor

1. **Ablation for M-LoRA's dropout is indirect**: The paper claims that multi-head dropout is the critical mechanism enabling M-LoRA's success (Section 3.3). The ablation supporting this is indirect — it compares removing the router from HydraLoRA (no dropout) vs. M-LoRA (dropout kept). A direct ablation of M-LoRA with and without dropout would provide cleaner evidence for this specific claim.

2. **Inconsistent evaluation setups across tables**: Tables 1, 2/3, 4, and 5 each use different subsets of methods, different models, and different training/evaluation datasets. While each table is internally valid, this fragmentation makes it difficult to obtain a unified picture of how all methods compare.

### Trivial
- In Figure 3, the flat lines for LoRA and R-LoRA at 74.00% look like they have no variance across λ values, which is expected since λ doesn't apply to them, but presenting them as two visually overlapping constants could be misleading to a quick reader.

---

## Nice-to-Haves

- An analysis of *when* task-shared vs. task-specific objectives are preferable (e.g., task relatedness, domain overlap) would strengthen the practical guidance.
- Extending experiments to include a standard LoRA + alignment-loss-only baseline (without the M-LoRA structure) more directly would isolate the contribution of alignment from the contribution of the architecture change.
- Visualizing the representation alignment (similar to the t-SNE mentioned in the appendix references) in the main paper would strengthen the mechanistic story.

---

## Novel Insights

The most genuinely novel observation in this paper is the "diversity paradox" in multi-head LoRA: methods that explicitly enforce head diversity (lower inter-head cosine similarity, as in R-LoRA) are outperformed by a simpler variant that produces highly redundant heads (M-LoRA, similarity ~0.85). This insight reframes multi-task LoRA research—not as a problem of how to separate task-specific knowledge, but as a problem of how to consolidate shared knowledge. The operational insight that applying KL-divergence alignment on the output of matrix A (the empirically validated task-general component) provides consistent performance gains with *fewer* parameters than complex multi-router architectures is a practical contribution that merits attention. The claim is more nuanced than "shared knowledge is better," since the A-LoRA-M inconsistency suggests the alignment objective matters, not just the concept of alignment.

---

## Suggestions

- Provide a direct ablation of M-LoRA with dropout removed to cleanly verify the dropout hypothesis.
- Investigate and discuss why A-LoRA-M (MMD alignment) underperforms A-LoRA-K (KL alignment) and in some cases falls below standard LoRA, rather than presenting both as uniformly successful.
- Revise the theoretical section to clearly distinguish between alignment in representation space and alignment of task data distributions; alternatively, add a lemma bounding the gap between the two.
- Report standard deviations or confidence intervals for key results to allow assessment of statistical significance.

---

## Score and Decision

The paper delivers a genuine empirical challenge to a prevailing assumption in multi-task LoRA—that structural diversity is necessary—and backs it up with evidence across multiple model families and scales. Align-LoRA-K is a practical, principled, and consistently effective method with no inference cost penalty. These are real contributions. However, the overstatement of A-LoRA-M's performance, the theoretical boundary that conflates representation-level and data-level distributions, and the somewhat indirect ablation for the dropout mechanism are meaningful issues. Overall, the work is above the typical ICLR borderline and contributes useful knowledge to the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>