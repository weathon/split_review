## Summary

This paper proposes a co-design algorithm for soft robots in which morphology and control are jointly optimized using a Graph Attention Network (GAT)-based controller with a topology-consistent weight-inheritance scheme (MAPWEIGHTS). During evolutionary search, parent controllers are transferred to morphologically modified offspring by reusing shared GAT and MLP hidden layers and remapping actuator-output weights via spatial correspondence, with new actuators randomly initialized. The approach is evaluated on four EvoGym tasks against two MLP baselines (with and without inheritance), showing fitness gains on three of four tasks and reduced variance across runs.

---

## Strengths

- **Topology-consistent inheritance enables broader parameter sharing across morphologies.** Because GAT message-passing kernels operate on arbitrary graphs, all hidden layers—including the full GAT encoder and MLP hidden layers—can be inherited intact regardless of changes in sensor/actuator count (Algorithm 2, lines 3–4). This is a genuine architectural advantage over MLP transfer, where variable input dimension forces ad-hoc treatment of the encoder layers, not just the output head.

- **Substantial fitness gains on Thrower-v0 and meaningful improvements on Pusher-v1.** Figure 3 shows GAT variants reaching fitness ~6.0–6.3 versus MLP baselines at ~3.3 on Thrower-v0, a near-doubling. Pusher-v1 also shows GA-GAT-PPO-Local-Transfer outperforming both MLP conditions. These are non-trivial margins.

- **Qualitative coordination analysis (Figure 4) directly supports the key claim.** The GAT-evolved robots on Thrower-v0 develop a two-actuator coordinated throwing strategy resembling human mechanics, whereas MLP baselines use a single actuator and consistently fall short of the target. This provides mechanistic, interpretable evidence for the advantage of the graph-structured policy.

- **Task-appropriate local vs. global representation finding.** Section 5.1 shows GA-GAT-PPO-Local-Transfer excels on tasks requiring component-level coordination (Pusher, Thrower, Carrier) while GA-GAT-PPO-Global-Transfer prevails on Catcher, which demands whole-body synchronization. This is a concrete, task-grounded finding rather than a generic claim.

---

## Weaknesses

### Fatal
None.

### Major

- **The stated motivation about decentralized local control is contradicted by the implemented architecture.** Section 3 explicitly claims "GNNs model robots as interconnected components, allowing actuators to act locally while obtaining global sensor and actuator information from their neighboring nodes." However, the actual architecture (Section 3, paragraph before Algorithm 2) performs a single round of message passing and then *averages over all nodes* into a single fixed-length vector, which is fed to a shared MLP head producing all actuator commands simultaneously. Actuator commands are not computed per-node from local subgraphs—they all come from the same pooled representation. The Local-Transfer variant assigns individualized node features but still average-pools before the decision head. This mismatch between the motivating claim and the design is not a minor imprecision; the paper's framing of "local," "decentralized" control is incorrect for the architecture as built. The empirical advantage of the GAT architecture is plausibly due to relational feature encoding improving the pooled representation and enabling architecture-invariant parameter transfer—a defensible and interesting claim that does not require the decentralized-control framing.

- **The ablation design cannot isolate the two claimed contributions, and the abstract overclaims it.** The introduction and abstract claim "ablations isolating the effects of graph policies and inheritance." However, the four conditions are: GAT+inheritance (×2 variants), MLP+inheritance, and MLP-no-inheritance. There is no GAT-without-inheritance condition. One can compare GAT+inheritance vs. MLP+inheritance (isolating architecture, both with inheritance) and MLP+inheritance vs. MLP-no-inheritance (isolating inheritance for MLP), but not GAT vs. MLP at the representation level independent of inheritance, nor the independent value of inheritance on top of the GAT representation. Given that both claimed contributions (graph representation and inheritance scheme) are always conflated in the "ours" conditions, the paper cannot attribute the observed gains to either one independently. The specific overclaim in the abstract should be corrected, and a GAT-no-inheritance condition added.

### Minor

- **Carrier-v1 shows no advantage for any method, contradicting the "consistently match or surpass" claim.** Figure 3 shows all four methods converging to essentially the same high fitness on Carrier-v1. The paper's Section 5.1 claims "Our GAT-based approaches consistently match or surpass the performance of MLP-based baselines"—the word "consistently" is not supported. The paper should present this case more honestly.

- **Only three independent evolutionary runs—very small for high-variance evolutionary search.** The standard deviation bands in Figure 3 are visibly large, particularly early in training. Three runs is below the norm for evolutionary computation experiments, and claims about variance reduction should be interpreted cautiously given this sample size.

- **The spatial matching procedure in MAPWEIGHTS is critically underspecified.** Algorithm 2, line 1 states "Compute node correspondence C : V_k → V_u ∪ {∅} by spatial matching" with no further detail. For voxelized robots where mutations add, remove, or relocate voxels, the choice of matching algorithm (nearest-neighbor, Hungarian assignment, etc.) directly determines which actuator weights get copied vs. randomly initialized. This is a reproducibility gap that affects all downstream results.

- **A single-hop GAT has limited receptive field on a 5×5 voxel grid.** The paper states "one attention-based message passing round" (Section 3). On a 5×5 grid, one-hop neighbors cover only directly adjacent voxels; most voxels cannot aggregate information from across the body. Whether this is an intentional design choice for computational efficiency or a capacity limitation deserves brief justification.

### Trivial

- **Section 5.3 draws a strong conclusion from a visual inspection of morphologies without quantification.** The claim that "task requirements strongly shape the space of feasible morphologies, whereas the controller architecture mainly influences learning speed" is stated as a clear conclusion from Figure 5, but no measure of morphological diversity or similarity is reported across the 3×4×4 grid of designs. This should be softened to a qualitative observation.

---

## Nice-to-Haves

- Adding a GAT-without-inheritance condition (GA-GAT-PPO-no-transfer) would complete the 2×2 ablation matrix and cleanly attribute gains to representation vs. inheritance vs. their interaction.
- Reporting model parameter counts for GAT vs. MLP conditions would rule out capacity-driven explanations.
- Extending to more than three evolutionary runs, or reporting effect sizes with bootstrap confidence intervals, would strengthen statistical claims.
- A brief specification of the spatial matching algorithm (even pseudocode) would substantially improve reproducibility.
- The motivational framing in Section 3 could be rewritten to emphasize the true mechanism of advantage: *architecture-invariant parameter sharing via graph structure* enables more of the controller to be reused when topology changes, rather than the incorrect claim about per-actuator local computation.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic Issue #3 (inheritance mechanism not novel vs. MLP baseline):** The critic argues the MAPWEIGHTS scheme is "structurally identical in spirit" to MLP transfer. This conflates surface similarity with the key technical difference: for GATs, the shared layers encompass the full encoder (all message-passing and attention kernels), which is architecture-invariant across graph sizes. For MLPs, the encoder input dimension changes with sensor count and cannot be straightforwardly transferred. The GAT design genuinely allows broader parameter sharing. This criticism should be demoted or removed — it misunderstands the source of the advantage.

- **Strength Finder: "task requirements strongly shape morphologies" conclusion.** The paper's claim from Figure 5 inspection is listed as a strength ("Supporting strength: local vs. global analysis"). The finding about local vs. global attention is a valid supporting strength; the broader conclusion about morphologies is unsupported and retained as a Minor weakness. Conflating both weakens the review.

- **Strict reading of "decentralized control" as fatal.** The harsh critic frames the local-control motivation mismatch as making the paper unpublishable ("structural problem"). However, the empirical contribution (gains on EvoGym, particularly Thrower-v0) does not depend on the decentralized-control claim being true. The architecture's advantage via relational encoding and architecture-invariant transfer is real and the paper demonstrates it empirically. Downgraded to Major rather than fatal.

---

## Novel Insights

The most genuinely novel observation across the reviews—partially obscured by framing issues in the paper itself—is that the primary advantage of the GAT architecture for morphological inheritance is not per-actuator local computation (as the paper claims) but rather *architecture-invariant parameter reuse*: because message-passing kernels operate on any graph, the full encoder can be copied intact across morphologies of varying size, leaving only the actuator output head to require node-level matching. This means that as morphological changes grow more drastic, GAT-based policies degrade more gracefully than MLPs because a larger fraction of learned parameters remains valid. The Thrower-v0 result (near-doubling of fitness) and the emergence of two-actuator coordinated strategies provide suggestive evidence that this broader inheritance supports qualitatively different behavioral capabilities, not just faster convergence.

---

## Suggestions

1. **Restructure the ablation matrix:** Run GA-GAT-PPO without inheritance to fully isolate the contributions of representation and inheritance. This would take the paper from "suggestive" to "causal" in its claims.
2. **Rewrite the decentralized-control motivation** in Section 3 to accurately describe the architecture: GAT + global pooling + MLP head. Replace the local/decentralized framing with an accurate account of why the architecture is superior for inheritance (architecture-invariant encoder layers).
3. **Specify the spatial matching algorithm** in Algorithm 2 (at minimum, state the method: e.g., "nearest-neighbor by Euclidean distance of voxel centroids").
4. **Increase evolutionary runs to at least 5**, or add a sensitivity analysis, to reduce uncertainty in variance estimates.
5. **Remove or heavily qualify** the claim in the abstract about "ablations isolating the effects of graph policies and inheritance" until the corresponding GAT-no-inheritance condition exists.
6. **Correct the Carrier-v1 framing** in Section 5.1 — "consistently match or surpass" is not accurate when one task shows equivalent performance across all methods.

---

**Originality:** The application of GAT-based controllers with topology-consistent inheritance to soft-robot co-design is incremental but technically specific. The concept is a natural extension of prior graph-policy and transfer-RL work; the novelty lies in the EvoGym instantiation and the MAPWEIGHTS procedure. *Moderate.*

**Importance of research question:** Scalable controller inheritance under morphological mutation is a real and recognized bottleneck in evolutionary robotics. *Moderate-high.*

**Claims supported:** The empirical results partially support the core claim, but the abstract's "ablations isolating" statement is not true, the architectural motivation is inconsistent with the design, and Carrier-v1 contradicts the "consistently" claim. *Weak-moderate.*

**Soundness:** The EvoGym setup is standard and comparisons are fair. The PPO training and GA hyperparameters follow established protocols. The three-run sample size and missing ablation condition are substantive gaps. *Moderate.*

**Clarity:** The methodology is mostly clear, but the decentralized-control framing in Section 3 will actively mislead readers, and the spatial matching step is unexplained. *Moderate.*

**Community value:** Provides a concrete, benchmarked demonstration that graph-structured policies improve robustness under morphological evolution on a standardized platform. Useful to the evolutionary robotics and embodied AI communities. *Moderate.*

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>