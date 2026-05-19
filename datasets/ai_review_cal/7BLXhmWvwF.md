- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8
Now I have a thorough understanding of the paper and all the claims. Let me produce the consolidated review.

## Summary

This paper addresses robotic manipulation of objects with varying geometries and deformable objects by framing the problem as a heterogeneous graph. The authors propose HEPi (Heterogeneous Equivariant Policy), which combines SE(3)-equivariant message passing (via the PONITA backbone) with explicit modeling of distinct actuator and object node types using separate kernels for each interaction type. They also introduce a benchmark of seven manipulation tasks (rigid insertion with diverse objects, rope manipulation, cloth hanging) in NVIDIA IsaacLab, and demonstrate that HEPi outperforms Transformer and homogeneous EMPN baselines, particularly on complex 3D tasks.

## Strengths

1. **Explicit heterogeneous graph design with formal guarantee of information flow.** Section 3.2 defines distinct update rules for object and actuator nodes with separate kernel parameters. Proposition 3.1 proves that HEPi's fully-connected inter-edges allow any actuator node to receive information from any object node in a single layer, unlike locally-connected alternatives that may require multiple hops. This directly justifies the design choice to avoid information bottlenecks.

2. **Strong empirical advantage on the most challenging 3D tasks.** Figure 3 shows HEPi significantly outperforming both Transformer and homogeneous EMPN baselines on cloth-hanging-3D and rigid-insertion-two-agents-3D — the highest-dimensional tasks where heterogeneity and geometric structure matter most. The paper honestly notes where methods perform comparably (e.g., rigid-sliding-2D), strengthening the credibility of the clear wins on harder tasks.

3. **Training stabilization via Trust Region Projection Layers.** Figure 8 demonstrates that TRPL provides stable performance across tasks while PPO struggles in high-exploration 3D environments like cloth-hanging-3D. This is a practical contribution: TRPL enables stable policy updates with minimal hyperparameter tuning, which is valuable for the complex, high-dimensional settings studied.

4. **Novel benchmark with structured difficulty progression.** Section 4.1 introduces seven tasks in IsaacLab that systematically vary difficulty from simple 2D rigid sliding to multi-actuator 3D cloth hanging, with uniformly randomized initial/target configurations. This provides a structured testbed for geometry-aware RL that goes beyond existing benchmarks.

5. **Generalization and robustness analysis.** Figure 5 shows HEPi generalizes to unseen objects (outperforming Transformer) and maintains performance across low- and high-resolution meshes under varying Gaussian noise levels, demonstrating practical robustness.

6. **Efficiency analysis of attention mechanisms.** Figure 7 shows that adding attention nearly doubles training time without improving final performance, providing empirical justification for HEPi's simpler non-attention design.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity about training algorithm consistency across comparisons.** The paper introduces TRPL in Section 3.2 as "the method we adopt" and presents it as a component of HEPi. However, it never explicitly states whether the Transformer and EMPN baselines in the main comparison (Figure 3) were trained with the same TRPL algorithm or with PPO. Given that Figure 8 shows TRPL substantially helps Transformer on cloth-hanging-3D, this gap is significant. The fact that Figure 8 reports both HEPi+TRPL and Transformer+TRPL results suggests the authors had access to TRPL-trained Transformer results, which mitigates the concern somewhat, but the paper should be explicit. This needs to be clarified in the rebuttal — if baselines used a different training algorithm, the core architectural comparison is confounded.

### Minor

- **Baseline architectures are under-specified.** The "naive EMPN" baseline is mentioned repeatedly but never described: does it use the same PONITA backbone but with homogeneous graph (all nodes treated identically)? How are actuator and object nodes handled? The Transformer baseline is also vague on architecture details (number of layers, hidden dimensions, positional encoding scheme). While hyperparameter details may reside in an appendix (stripped by the parser), the in-paper description of what these baselines *are* should be clearer for the reader to assess fairness of comparison.

- **Equivariance claim is slightly overstated.** The abstract and introduction state HEPi is "SE(3)-equivariant" and "constrained to be SE(3)-equivariant" without qualification. Section 3.1 correctly notes that PONITA's discretization on S² "sacrifices exact equivariance." The high-level claims should be qualified as "approximately equivariant" or the practical implications of the discretization discussed.

- **Proposition 3.1 is oversold as a "theoretical justification."** The proposition that fully-connected inter-edges allow direct information flow while local connections may not is a basic consequence of graph connectivity. It is a reasonable design motivation but does not constitute a theoretical contribution on par with the empirical results. The paper should reframe this as a design rationale rather than a theoretical justification.

- **Heterogeneity is not ablated cleanly.** The comparison between HEPi (separate kernels per edge type) and EMPN (homogeneous kernels) is informative, but it conflates multiple differences. A cleaner ablation — HEPi vs. a variant using a single shared kernel across all edge types while keeping the same heterogeneous graph structure — would isolate the contribution of per-type kernels from the benefits of the graph structure itself.

- **TRPL benefit not tested on EMPN baseline.** Figure 8 tests TRPL vs. PPO only on HEPi and Transformer. If the EMPN baseline also benefits substantially from TRPL, its relatively poor performance in Figure 3 may be partly an artifact of using PPO. Reporting EMPN+TRPL results would strengthen the claim that HEPi's architecture, not just its training algorithm, drives the improvement.

- **Reward functions are not described.** Section 4.1 describes the tasks but provides no reward specification. Reward design is central to RL and critical for reproducibility. This information may be in the appendix, but it should be noted in the main text.

### Trivial

None.

## Nice-to-Haves

- **Final performance table.** Adding a table reporting mean returns and standard deviations for each method at convergence (alongside the learning curves) would help readers quantify the magnitude of improvements and assess statistical significance more readily.
- **Quantify sample efficiency.** The paper qualitatively notes sample efficiency advantages; reporting environment steps to reach 50%/90% of converged performance would strengthen this claim.
- **Characterize the approximate equivariance.** An experiment measuring HEPi's performance under increasing rotational perturbations could quantify how much the approximate equivariance degrades and validate that the inductive bias is meaningfully preserved.
- **Additional baseline: non-equivariant heterogeneous GNN.** Isolating the benefit of equivariance from heterogeneity (beyond the Cloth-Hanging analysis in Figure 4) would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about benchmark not being publicly available.** Hard Rule: remove any criticism questioning release status of cited entities. The paper cites the benchmark framework (IsaacLab); the benchmark tasks are described in the paper.
- **Criticism about missing heuristic/non-learning baseline.** Scope creep — the paper compares against Transformer and EMPN baselines, which are standard for this setting. Demanding a non-learning baseline goes beyond the paper's stated scope.
- **Criticism about compute resources not mentioned.** Trivial implementation detail; not standard to require in all ML papers.
- **Criticism about Proposition 3.1 proof not in main text.** The proof is presumably in the appendix (stripped by the parser). The Hard Rule states parser-stripped appendix content should not be flagged.
- **Criticism about "typos, formatting"** — parser artifacts, not author errors.
- **Strength Finder's framing of "theoretical guarantee" in Strength 1** — softened in the weakness section above to avoid contradiction with the verified weakness about Proposition 3.1 being oversold.

## Novel Insights

The convergence of two established ideas — equivariant message passing and heterogeneous graph networks — produces a concrete practical benefit in exactly the regime where each alone struggles: high-dimensional 3D manipulation with deformable objects and multiple actuators. The key insight (visible in Figure 3) is that homogeneous EMPN gets stuck in local optima on tasks requiring exploration (rigid-pushing-2D, rigid-insertion-2D+z) while Transformer fails on high-dimensional 3D tasks, but HEPi's separation of actuator/object processing alleviates both failure modes. This suggests that for underactuated manipulation (few actuators controlling many object nodes), explicitly routing information through type-specific channels is more important than the specific aggregation mechanism or even the strength of the equivariant inductive bias.

## Suggestions

1. **Explicitly state the training algorithm used for each baseline in Figure 3** and confirm all models used the same RL algorithm. This single clarification resolves the most impactful ambiguity in the paper.
2. **Describe the "naive EMPN" baseline architecture** — is it the PONITA backbone on a homogeneous graph? How are actuator/object nodes distinguished (or are they merged)?
3. **Reframe Proposition 3.1** as "design motivation" or "connectivity analysis" rather than "theoretical justification" to avoid overclaiming.
4. **Add a shared-kernel ablation** comparing HEPi against a variant using a single set of kernel parameters for all edge types, keeping the heterogeneous graph structure identical.
5. **Report EMPN+TRPL results** on at least the cloth-hanging-3D task to rule out the training-algorithm confound for that baseline.
6. **Qualify equivariance claims** in the abstract and introduction as "approximately SE(3)-equivariant" or add a brief qualifier referencing the discretization.
