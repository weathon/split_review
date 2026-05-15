Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes HSDGNN, a graph neural network for multivariate time-series forecasting that introduces a hierarchical graph perspective: each variable (node) is treated as a sub-graph of its attributes, and two levels of graph convolution model intra-attribute dependencies within a variable and inter-variable spatial dependencies. A second GRU module encodes temporal correlations in evolving graph topologies. Experiments on five real-world datasets (traffic and electricity) show consistent improvements over strong baselines like DDGCRN (up to 15.3% RMSE reduction).

## Strengths

- **State-of-the-art empirical performance.** HSDGNN achieves the best results across all five benchmark datasets and all three metrics (MAE, RMSE, MAPE). The improvements over the strongest baseline (DDGCRN) are substantial (up to 11.8% MAE, 15.3% RMSE, 9.8% MAPE), and the stepwise analysis (Figure 3) confirms these gains hold across all prediction horizons. The low standard deviations across 10 runs indicate reliable improvements.

- **Thorough ablation and hyperparameter robustness.** The ablation study (Table 3) systematically removes each component (intra-dependency module, GRU1, GRU2, dynamic graph, multi-attribute input), and every variant underperforms the full model. The hyperparameter sensitivity analysis (Figure 4) spans embedding dimension, hidden size, number of blocks, and diffusion steps, and HSDGNN remains competitive across all settings — a practical strength.

- **Scalable parameter complexity.** Table 2 shows HSDGNN's parameter count remains nearly constant as the number of variables grows (e.g., 0.07M on PEMSD4 with 307 nodes vs. 0.06M on PEMSD5 with 66 nodes), while baselines like ST-AE and SDGL grow non-linearly. This is a genuine architectural advantage.

- **Clear, well-motivated problem framing.** The paper correctly identifies two real gaps in existing STGNNs: (1) neglecting intra-attribute dependencies among multiple sensor signals, and (2) insufficient handling of temporally evolving spatial topologies. The hierarchical graph abstraction is intuitively appealing and clearly communicated in Figures 1–2.

## Weaknesses

### Fatal
None.

### Major

- **Notation ambiguity in the intra-dependency module undermines reproducibility of the core technical contribution.** The central novelty of the paper is an attribute-level sub-graph convolution "inside each variable node." However, the mathematical formulation (Eq. 2–4) is critically underspecified. The paper writes $\mathbf{E} = \theta(W_I \mathbf{X}_t + b_I)$ and then $\mathbf{R} = \text{ReLU}(\mathbf{E} \cdot \mathbf{E}^T)$, but never states the shape of $\mathbf{E}$ or $\mathbf{R}$. If $\mathbf{X}_t \in \mathbb{R}^{N \times C}$ is the full input tensor, then $\mathbf{E}$ has shape $N \times d$ (one embedding per variable) and $\mathbf{E} \cdot \mathbf{E}^T$ is $N \times N$ — a cross-variable matrix that *contradicts* the claim of operating "inside each variable node." If instead $\mathbf{E}$ is computed per node (yielding $C \times d$ per variable), the paper never specifies this, and the global notation ($\mathbf{E} \cdot \mathbf{E}^T$) is misleading. Either way, the reader cannot determine the actual computation. Since the intra-dependency module is the paper's headline contribution, this ambiguity is a serious flaw that must be resolved.

- **Abstract's efficiency claim contradicts the reported data.** The abstract states that improvement is achieved "without compromising on model size." Table 2 reports HSDGNN has 0.24M–0.35M parameters, while DDGCRN has 0.08M–0.09M — an increase of roughly 3×. Calling this "without compromising" is misleading. The body's more measured language ("comparable model sizes," "better trade-off") is defensible, but the abstract overstates the efficiency.

- **Missing empirical comparison against DMSTGCN.** The related work section explicitly identifies DMSTGCN as "the only work that explicitly models the effects of additional attributes." Yet DMSTGCN is not included as a baseline in Table 1. To substantiate the claim that HSDGNN improves over the state of the art *in multi-attribute modeling*, the most directly related prior method should be compared.

### Minor

- **The second GRU's claimed novelty is overstated.** The paper states that "different from current STGNN approaches which only model spatial and temporal dependency in separate modules, we apply an extra temporal learning component ... to consider the change of graph topology." In practice, GRU₂ simply processes the sequence of spatially aggregated signals — a pattern already present in dynamic-graph STGNNs (e.g., DDGCRN interleaves diffusion with recurrence). The ablation does show that removing GRU₂ hurts performance more than removing GRU₁, which provides some empirical justification, but the *conceptual* novelty is modest and the paper does not clearly distinguish its approach from prior architectures that also interweave spatial and temporal modules.

- **The w/o IDLM ablation does not fully isolate the benefit of graph-based intra-dependency modeling.** The paper compares the full model against a variant without the intra-dependency learning module (w/o IDLM). However, it never specifies how the multiple attributes are handled in this variant — are they simply concatenated and fed through a linear layer, or processed through some other mechanism? Without this specification, a reader cannot determine whether the improvement of the full model over w/o IDLM is attributable to the *graph structure* of the intra-dependency modeling or simply to having more parameters in the module. A baseline that feeds all attributes as a flat feature vector into a standard GRU (with no attribute-level convolution) would cleanly isolate this.

### Trivial
None.

## Nice-to-Haves

- Adding a qualitative visualization of the learned intra-dependency matrix $\mathbf{R}$ for a few variables and timesteps would make the "hierarchical" claim more concrete and interpretable.
- Reporting statistical significance (e.g., paired t-tests) between HSDGNN and the second-best method would strengthen the claim of reliable improvement, given the very small standard deviations reported.
- Extending experiments to datasets with more than 3 attributes (e.g., weather data) would better demonstrate the scalability of the intra-dependency module.

## Removed Points

The following points raised by reviewers are removed with justification:

- *HA std = 0.00 being "impossible":* Removed. HA (History Average) is a deterministic method — it produces identical outputs for identical inputs across runs. A standard deviation of 0.00 is correct, not suspicious.
- *Code repository not accessible:* Removed. The paper states code is available in a repository (footnote). That the parser stripped the footnote URL is a parser artifact, not a paper flaw.
- *Ambiguity about whether $\mathbf{T}$ is a sequence or single hidden state:* Removed. The paper explicitly states "The temporal fusion $\mathbf{T}$ is then comprised of the hidden states $h_{G_1}^t$ ($t \in [-T+1, 0]$)" — a sequence of hidden states. The paper is clear on this point.
- *Second GRU "not an innovation" / indistinguishable from standard recurrence:* Weakened to Minor. The critic's strongest form (that it is "standard and not clearly innovative") is softened. The paper does provide ablation evidence (w/o GRU₂ hurts more than w/o GRU₁) and the architecture difference (GRU₂ operates after diffusion with dynamic $\mathbf{G}$) is a genuine design choice, even if its conceptual novelty is modest.
- *R not being guaranteed symmetric positive semidefinite causing training instability:* Weakened. $\mathbf{E} \cdot \mathbf{E}^T$ is symmetric PSD by construction; ReLU preserves symmetry (applied element-wise). The concern about PSD-breaking is technically correct but minor and unsubstantiated by any observed instability. This is at most a theoretical note, not an empirical weakness.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest evidence (consistent SOTA across 5 datasets with multiple metrics) coexists with its weakest link (ambiguous notation for the very module that is the headline contribution). The harsh critic correctly identifies that the paper's claimed novelty for the second GRU is not clearly distinguished architecturally from prior dynamic-graph STGNNs, yet the ablation study *does* empirically show its removal causes the largest performance drop among all components. This suggests the paper may have discovered a genuinely useful architectural pattern (post-diffusion recurrence on dynamically-generated graphs) whose theoretical rationale is not yet well articulated. Similarly, the intra-dependency module may well be effective, but the current notation prevents the reader from understanding exactly what computation is being performed. The empirical contribution of this paper is stronger than its conceptual framing — the architecture works, but the paper does not yet explain *why* with sufficient precision.

## Suggestions

1. **Clarify the intra-dependency module's tensor shapes.** Specify the exact dimensions of $\mathbf{E}$ and $\mathbf{R}$ in Eq. 2–4. State explicitly whether $\mathbf{R}$ is computed per node (yielding $C \times C$ per variable) or globally. If per-node, provide the batched formulation and comment on the computational cost (which, given $C=3$ in experiments, is negligible — this would address the critic's concern about scalability). If ReLU($\mathbf{E} \cdot \mathbf{E}^T$) is used as the adjacency, discuss whether it is normalized and whether training stability was monitored.

2. **Correct the abstract's efficiency claim.** Replace "without compromising on model size" with a more accurate statement (e.g., "with competitive model size" or "while maintaining favorable scalability").

3. **Add DMSTGCN as a baseline** or clearly justify its exclusion (e.g., citing scalability issues that prevent it from running on these datasets).

4. **Specify the w/o IDLM variant's handling of attributes.** Describe how the multiple attributes are processed when the intra-dependency module is removed. Adding a "flat features" baseline (all attributes concatenated as input to a standard GRU) would cleanly isolate the benefit of the graph-based intra-dependency modeling.

5. **Tone down the framing of the second GRU's novelty.** Acknowledge that the conceptual distinction from prior dynamic-graph STGNNs is incremental, and reframe the contribution as an ablation-confirmed empirical finding rather than a fundamentally new architectural paradigm.

## Score and Decision

**Originality:** The hierarchical graph perspective (variables as sub-graphs of attributes, two-level convolution) is a genuine architectural contribution, though the individual techniques (node-adaptive parameters, dynamic graphs, GRU recurrence) are borrowed from prior work.

**Importance of research question:** High. Accurate multivariate time-series forecasting is practically important (traffic, energy), and the specific gaps identified (intra-attribute dependencies, temporal topology dynamics) are real.

**Claims supported by evidence:** Partially. The SOTA results are strongly supported. However, the central claim about *graph-based* intra-dependency driving improvement is weakened by the notational ambiguity and the underspecified w/o IDLM ablation. The model-size claim is contradicted by the data.

**Soundness of experiments:** Generally sound. Datasets, metrics, and baselines are appropriate. Ablation studies are present. The main gap is the missing DMSTGCN baseline and the underspecified ablation variant.

**Clarity of writing:** Above average for motivation and overall architecture, but below average in the crucial intra-dependency section where tensor dimensions are never stated.

**Value to community:** Moderate. The empirical results are strong and could serve as a competitive benchmark. The hierarchical graph idea is worth further exploration. However, the current form would require significant clarification before the community can build on it reliably.

The paper's empirical contribution is real and its motivation is sound, but the notational ambiguity in its core contribution, the overclaimed efficiency, and the missing key baseline prevent it from being acceptable in its current form. With major revisions addressing these issues, this could be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>