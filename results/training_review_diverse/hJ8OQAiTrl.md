I've thoroughly verified all claims against the paper. Let me now produce the consolidated review.

---

## Summary

This paper proposes CoST, a framework that combines structural and textual information for graph reasoning tasks by alternatingly training a graph neural network (GNN) and a pre-trained language model (PLM). The training is motivated by a variational objective that factorizes candidate targets, enabling the two models to be optimized in alternation rather than jointly, which avoids scalability issues on large graphs. The paper reports state-of-the-art results across homogeneous and heterogeneous graph reasoning benchmarks including FB15k237, WN18RR, and Wikidata5M.

## Strengths

- **Consistent empirical gains across diverse benchmarks.** CoST achieves the best MRR and Hits@k on all homogeneous datasets (AmazonSports, AmazonClothing, MAGGeology, MAGMath in Table 2; CitationV8, GoodReads in Table 3) and all heterogeneous datasets (FB15k237, WN18RR in Table 4; Wikidata5M in Table 5). The gains over strong structure-only methods like NBFNet and A\*Net on heterogeneous benchmarks (e.g., +4.2 MRR on FB15k237) are particularly meaningful because those baselines use the same structural information and the comparison is well-controlled.

- **Architecture-agnostic improvement verified by ablation.** Ablation experiments in Figure 3a show that CoST improves three different GNN backbones (RGCN, CompGCN, NBFNet) on FB15k237 and WN18RR. This demonstrates that the framework's benefit generalizes beyond a single GNN architecture choice.

- **Scalability to large graphs.** Experiments on CitationV8 (2.3M nodes) and Wikidata5M (4.5M nodes) show that CoST scales where joint training of GNN and PLM would be prohibitive, directly addressing the key challenge stated in the introduction.

- **Rapid convergence of alternating training.** Convergence analysis in Figure 3b on FB15k237 and WN18RR shows near-optimal performance within a few alternating steps, mitigating the concern that alternating procedures require costly iterative cycles.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap between the variational derivation and the actual algorithm.** The paper presents Theorem 2.1 claiming equivalence between the original GNN objective and a variational bound, then derives alternating updates motivated by ELBO maximization and KL divergence minimization. However, the transition from "minimize KL divergence" to "sample hard pseudo-targets from a multinomial distribution and optimize a contrastive loss" (Equations 8-9 for the PLM, and Equation 11-12 for the GNN) is heuristic, not derived. The paper states the KL is "challenging" to optimize and then "alternatively" uses pseudo-targets, but never explains why the contrastive objective in Equation 9 approximates the KL minimization. The GNN optimization (Section 2.3.2) is similarly approximated via sampling without showing how the weighted contrastive objective (Equation 12) follows from the ELBO. This gap does not invalidate the empirical results, but it means the variational framing gives an "illusion of rigor" rather than a tight derivation. The paper would be stronger if it either (a) provided a noise-contrastive estimation argument connecting the loss to the KL, or (b) dropped the variational framing and presented the method as an empirically motivated co-training heuristic.

2. **The GNN backbone used in homogeneous graph experiments (Tables 2, 3) is not specified.** The paper states the GNN-based baselines are GCN, GraphSAGE, and GATv2, but never states what GNN architecture CoST itself uses for these datasets. This makes it impossible to determine whether CoST's large improvements over the GNN baselines come from the alternating training or simply from using a stronger GNN backbone. (Note: the critic's claim that NBFNet is used is an assumption — the paper does not state this.) On heterogeneous graphs (Table 4), where the backbone is NBFNet and baselines include NBFNet, the comparison is fair and the gains are credible. But the homogeneous graph results, which constitute a substantial portion of the empirical demonstration, are difficult to interpret without this information.

3. **No ablation isolating the alternating training from the backbone choice on the homogeneous graphs.** A natural controlled experiment would be to compare CoST's full alternating training against the same GNN backbone with static PLM embeddings (no alternating updates), on the same datasets where the backbone is identified. On heterogeneous graphs, the ablation in Figure 3a partially addresses this by showing improvement over the pre-trained GNN model, but on homogeneous graphs no such isolation is provided. Combined with Weakness 2, the reader cannot attribute the homogeneous-graph gains to the claimed innovation.

### Minor

1. **No comparison against a "fixed PLM + same GNN backbone" baseline on any dataset.** The paper compares CoST against structure-only baselines and text-only baselines, but the most direct way to isolate the value of alternating training is to compare CoST against its own GNN backbone using static (unfine-tuned) PLM embeddings. This comparison would cleanly measure what the alternating update adds. On heterogeneous datasets, the pre-trained GNN model (before alternating training) serves as a weak proxy for this, but the paper does not explicitly frame it as such or ensure the backbone matches.

2. **Standard deviations / confidence intervals are not reported for any result.** Given the paper's strong claims ("state-of-the-art across representative benchmark datasets"), the absence of variance estimates makes it impossible to assess whether the reported gains are statistically reliable or could stem from run-to-run variance. While single-run evaluation is not uncommon in graph reasoning, the field increasingly expects some measure of variability.

3. **Computational cost is not discussed.** The alternating training involves updating both a GNN and a PLM, each of which is independently expensive. On datasets like Wikidata5M (4.5M nodes) and CitationV8 (2.3M nodes), wall-clock time, GPU-hours, and memory requirements would be important for practitioners evaluating whether the method is practical for their use case.

### Trivial
None.

## Nice-to-Haves
- An analysis of how the GNN and PLM pseudo-targets evolve (agreement rate, confidence calibration) would provide a direct sanity check on the assumption that alternating updates make their predictions mutually informative.
- Additional discussion of hyperparameter sensitivity for \(L\) (number of alternating steps), \(\gamma\), and \(\tau\) would strengthen reproducibility, though these are manageable in supplementary material.
- The PLM objective (Equation 9) is written as a softmax ratio; clarifying whether this is a binary cross-entropy or a multi-class InfoNCE loss would help implementation.

## Removed Points

The following points from the original reviews were removed per consolidation rules:

1. **"CoST uses NBFNet as its GNN backbone for homogeneous graphs"** — The paper does not state what backbone CoST uses for homogeneous graph experiments. This claim is an unsupported assumption and is removed. The underlying concern (missing specification) is preserved as Major Weakness 2.

2. **"Missing hyperparameters (epochs, learning rates, convergence criteria)"** — Per the instruction to remove nitpicks about reproducibility such as undisclosed hyperparameters, this is removed. The broader issue about missing experimental details is captured in Major Weakness 2.

3. **Strength Finder claim about "theoretical grounding"** — Removed because it conflicts with the verified weakness about the theory-practice gap. The alternating training framework is a genuine contribution, but the theoretical derivation is incomplete.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the GNN backbone for all experiments.** Specify what architecture CoST uses on each dataset, ideally in the experimental setup section or a dedicated reproducibility table.

2. **Add a controlled baseline: same GNN backbone with static PLM embeddings.** On at least the heterogeneous datasets where the backbone is known (NBFNet), compare against NBFNet + frozen BERT embeddings. This directly isolates the benefit of alternating training.

3. **Either tighten the variational derivation or honestly reframe the method as a heuristic co-training scheme.** If the contrastive loss with hard pseudo-targets cannot be rigorously derived from the KL divergence, the paper should acknowledge this explicitly rather than presenting the variational argument as the core intellectual framing.

4. **Report standard deviations** (at least across 3-5 seeds) for the main results, particularly the state-of-the-art claims.

5. **Include computational cost information** (training time, GPU memory, number of alternating cycles) for at least one large-scale dataset.

## Score and Decision

This paper tackles a genuinely difficult and important problem — integrating structural and textual information for graph reasoning without the prohibitive cost of joint GNN+PLM training. The empirical results on heterogeneous benchmarks (where the backbone is known and the baselines include strong methods like NBFNet) are credible and meaningful. The ablation studies demonstrate that the framework benefits multiple GNN architectures. These are real contributions.

However, two interconnected problems weaken the paper. First, the missing specification of the GNN backbone on homogeneous graphs — combined with the lack of an ablation isolating the alternating training from the backbone choice — makes a substantial fraction of the empirical results difficult to interpret. Second, the variational derivation is presented as a principled motivation but the actual algorithm is a heuristic approximation, creating a mismatch between the paper's framing and its practice. Neither issue alone is fatal (the heterogeneous experiments and architecture ablations support the core claim), but together they prevent the paper from being fully convincing in its current form.

The paper needs a major revision to address these gaps. On balance, the paper's contributions are genuine but not yet presented with sufficient rigor and completeness.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>