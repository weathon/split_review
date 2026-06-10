## Summary

This paper proposes G4RL, a framework that learns subgoal representations by training a graph encoder-decoder on a dynamically constructed state graph during exploration. The learned subgoal space is then used to compute intrinsic rewards for both the high-level and low-level agents in goal-conditioned hierarchical RL (GCHRL). The method is tested on three Ant-based MuJoCo environments by plugging into HIRO and HRAC, showing consistent improvements.

## Strengths

- **Dynamic graph construction without domain-specific knowledge (Sec 3.1).** The paper builds and updates a state graph entirely from exploration, with no pre-crafted graphs or expert data. Node matching via a distance threshold, edge-frequency updates, and a fixed-size eviction policy (oldest-node or weakest-node) are concretely specified. This is a clean departure from prior graph-based methods that rely on pre-specified graphs.

- **Dual intrinsic-reward integration addressing both hierarchy levels simultaneously (Sec 3.4, Eqs 9–10).** The high-level intrinsic reward penalizes subgoals that are difficult to reach in the learned subgoal space, and the low-level intrinsic reward augments the standard Euclidean-distance reward with a subgoal-space term. The ablation study (Figs 2–3) confirms that the full dual-intrinsic variant outperforms either high-level-only or low-level-only variants, showing both components contribute.

- **Adaptive training schedule for the online graph encoder-decoder (Sec 3.3).** The change-tracking variable \(c\), with differential weighting for node replacements versus edge updates, and a threshold-based trigger \(\beta(N^2 - N)\), is a practical solution to the problem of varying update rates during online training. This avoids both high early-episode variance and later over-training.

- **Consistent empirical improvement across all tested settings (Fig 1).** G4RL improves both HIRO and HRAC on all three environments (AntMaze, AntMaze-Sparse, AntGather) using 5-run averages. The sparse-reward setting (AntMaze-Sparse) is a particularly relevant test for the paper's stated goals.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation scope is too narrow to support the generality claimed.** The paper claims G4RL "can be incorporated into any existing GCHRL method to enhance performance" (Abstract) and positions itself within a general graph+RL trend. However, experiments are limited to: (a) **three environments, all Ant-based MuJoCo tasks** sharing the same morphology and action space; (b) **two base GCHRL methods (HIRO and HRAC)** that belong to the same lineage, with HRAC being a direct extension of HIRO. No diverse domains (e.g., visual, robotic manipulation, navigation with different morphologies) or methods outside the HIRO family are tested. For a paper claiming broad generality, the evidence base is thin.

- **No error bars, confidence intervals, or statistical significance measures.** Curves in Figure 1 are reported as 5-run averages "smoothed equally for better visualization" (line 182) with no indication of variance. Without variance information, the reader cannot assess whether the observed improvements are consistent across runs or driven by outliers. At a top venue, this is a meaningful gap in experimental rigor.

### Minor

- **The central claim of handling unseen states is not tested.** The paper repeatedly emphasizes that the graph encoder-decoder "can evaluate unseen states" (lines 7, 103) — a legitimate advantage over using raw graph lookups. However, no experiment validates this. The subgoal space visualization (Sec 4.4, Fig 4) only maps states encountered during training; it does not probe generalization to held-out or novel states. This claim remains unsupported by evidence.

- **Subgoal space evaluation is purely qualitative.** The PCA-based visualization (Fig 4) is interpreted as showing increasingly connected subgoal representations, but PCA projections of high-dimensional embeddings can be misleading. A quantitative metric (e.g., correlation between subgoal-space inner products and actual reachability, or graph reconstruction accuracy on held-out pairs) would substantiate the claim that the encoder is learning better representations over time.

- **Architectural details of the encoder are under-specified in the main text.** The encoder is described as "a feed-forward network (FFN) with several layers" (line 107) with no information on number of layers, hidden dimensions, activation functions, or output dimension. While some of these may appear in the appendix (stripped by the parser), the main text should characterize core architectural choices at a level that allows basic assessment of the method.

### Trivial

None.

## Nice-to-Haves

- Testing on at least one GCHRL method outside the HIRO lineage (e.g., a pixel-based or different high/low-level formulation) to probe generality.
- A direct test of unseen-state generalization: hold out a subset of encountered states from graph construction during training and check whether the encoder's pairwise inner products for those states predict the held-out adjacency structure.
- Reporting a quantitative metric of subgoal space quality alongside the PCA visualization.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper. Treat them with caution if referenced:

- *"No comparison to other graph-based RL methods"* — The cited graph-based works address different problems (graph search, world models, representation learning) and are not GCHRL methods. The paper's contribution is a plug-in module for GCHRL; the natural comparison is GCHRL with/without the module. Requiring comparison to methods solving different problems is scope creep.

- *"Missing implementation details undermine reproducibility (hyperparameter values)"* — Per hard rules, criticisms about hyperparameter values deferred to the appendix are removed (the parser strips appendix sections from all papers). The encoder architecture being under-specified in the main text is retained as a minor point above.

- *"Claim that 'no prior work has attempted to address them in combination' is overstated because HRAC addresses high-level subgoal selection"* — The paper's claim is about combining *both* high-level exploration efficiency *and* low-level subgoal representation quality. HRAC only addresses the high-level component. The claim is accurate as written.

- *"Decoder loss may cause collapsed representations"* — Reanalysis of Eq 8 shows the loss function naturally prevents collapse: connected node pairs (non-zero adjacency targets) produce gradients that push representations away from zero and force differentiation between nodes. The critic's concern about driving representations toward zero would increase loss on connected pairs, so the trivial solution does not minimize the loss. This criticism is not supported by the math.

- *"Strength: encoder-decoder generalizes to unseen states"* — Removed because it conflicts with the verified weakness that this claim is not tested. Per rules: "when a strength and weakness disagree, the weakness wins."

- *"Strength: subgoal space visualization showing learned structure"* — Removed because the visualization is qualitative and the weakness about it being unevidenced is retained. PCA projections alone are insufficient as a strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Broaden the evaluation** to include at least one non-Ant environment and one GCHRL method outside the HIRO lineage. Even a single additional domain (e.g., a continuous control task with a different morphology, or a 2D navigation task) would meaningfully strengthen the generality claim.
2. **Report error bars or variance** on all learning curves (e.g., shaded regions showing std or quartiles across runs).
3. **Directly test the unseen-state claim** by holding out a subset of states from graph construction and measuring whether the encoder produces meaningful inner-product predictions for those held-out states.
4. **Add a quantitative metric** for subgoal space quality (e.g., correlation between subgoal-space inner products and actual reachability in steps) to complement the PCA visualization.

## Score and Decision

**MY FINAL SCORE: <score>4.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**