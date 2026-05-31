## Summary
The paper proposes **ELMUR**, a transformer for long-horizon partially observable RL/imitation learning that augments *each transformer layer* with an external memory, connected via bidirectional token↔memory cross-attention and updated by an **LRU-style replace-or-rewrite (convex blend)** rule. The paper claims very large effective-horizon extensions and reports results on a synthetic long corridor T-Maze, POPGym-48, and the MIKASA-Robo sparse-reward manipulation suite.

## Strengths
- **Clear architectural/mechanistic proposal (layer-local memory + bidirectional cross-attention + LRU rewrite).** The abstract and overview (Fig. 1) specify the central design: “Each layer maintains memory embeddings, interacts with them via bidirectional cross-attention, and updates them through an LRU memory module using replacement or convex blending” (Abstract; Fig. 1 caption).
- **Ablation evidence that the proposed memory management components matter (at least on the targeted memory toy task).** On RememberColor3-v0, removing LRU and/or relative bias causes large drops: *No LRU* \(0.43\pm0.22\), *No rel. bias; No LRU* \(0.22\pm0.11\), and *Shared memory* \(0.45\pm0.03\) versus baseline \(1.00\pm0.00\) (Table 3; see also the RQ5 paragraph at lines 261–262).

## Weaknesses

### Fatal
None.

### Major
- **Headline “effective horizon up to \(100{,}000\times\)” claim is not adequately supported in the visible main text beyond assertion + (partially elided) single-task evidence.** The abstract and conclusion state: “ELMUR extends effective horizons up to 100,000 times beyond the attention window” (Abstract; Conclusion). However, in the provided main-text extraction, the crucial supporting details for how that factor is computed/validated are not actually present (e.g., the T-Maze setup details, the exact attention window used in that experiment, and the “effective horizon” derivation referenced in the conclusion). What *is* visible is that the ablation section itself frames performance as strongly capacity/segmentation conditioned (“when \(M \ge N\)… near-perfect; when \(M < N\)… drops sharply,” lines 261–262), which undercuts the generality of the “\(100{,}000\times\)” framing unless the paper explicitly ties those conditions to the horizon claim in the main narrative.
- **POPGym statistical reporting is too weak to support fine-grained “wins on more than half the tasks” claims.** The paper states POPGym uses “three independent runs” and shows “95% confidence intervals computed over these three means” (Fig. 5 caption, lines 280–281). With \(n=3\), the plotted CIs are not very informative, and the paper does not (in the visible text) provide paired tests or additional seeds to substantiate task-by-task superiority claims. Given the claim “outperforms baselines on more than half of the tasks” (Abstract), this is a meaningful evidential gap.

### Minor
- **Sensitivity/instability in the memory update hyperparameters is acknowledged but not contextualized for the main benchmarks.** The ablation text reports “Intermediate blending (\(\lambda \approx 0.4-0.6\)) is unstable… larger initialization \(\sigma\) mitigates collapse” (lines 261–262; Fig. 6). This is useful honesty, but the paper does not (in the visible main text) connect this sensitivity to POPGym/MIKASA robustness (e.g., whether those tasks require careful tuning, or whether stable regions are broad in practice).
- **Ablations are restricted to RememberColor3-v0, leaving component-level causality on the flagship domains unverified in the visible text.** Table 3 and RQ5 are only on RememberColor3-v0 (lines 261–273). Given the abstract’s strongest applied claim is MIKASA-Robo (“best success rate on 21/23… aggregate +70%,” Abstract), it would strengthen credibility to show at least one key ablation (e.g., removing LRU, shared vs per-layer memory) on the robotics benchmark as well.

### Trivial
None.

## Nice-to-Haves
- Add a compact table (in the main text) reporting **parameter counts and runtime/throughput** for ELMUR and the major baselines on each benchmark, plus a short statement of **what is held fixed** across methods (training updates, data, compute budget). This would make it easier to interpret whether gains stem from the memory mechanism versus general capacity/compute differences.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Baselines are not compute-matched / unfair comparisons due to extra cross-attention and MoE.”** The provided main-text extract does not contain the necessary baseline configuration details (parameter counts, FLOPs, training budgets, or explicit fairness protocol) to *verify* unfairness. It is reasonable to *request* compute reporting (Nice-to-have above), but not to assert unfair comparison as a confirmed weakness from the visible text alone.
- **“T-Maze protocol may be trivial due to cue repetition/segmentation artifacts.”** The visible text does not include the T-Maze experimental protocol details; without those specifics, this criticism would be speculative.

## Novel Insights
The ablation section implies ELMUR’s performance on at least one representative memory task is governed by a fairly crisp *capacity vs. required-segment-count* condition (\(M \ge N\) versus \(M < N\)) and can exhibit instability in intermediate rewrite blending regimes. This suggests the method’s practical success may hinge less on “implicit long-term credit assignment” and more on predictable storage provisioning and stable rewrite dynamics—an angle the paper could emphasize more explicitly when framing its “effective horizon” claims.

## Suggestions
- Make the **“effective horizon”** claim falsifiable in the main text: define it precisely, show how the \(100{,}000\times\) number is computed, and report the exact experiment(s) and settings that achieve it.
- Strengthen POPGym evidence: increase seeds beyond 3 or add a **paired statistical analysis** over tasks/runs consistent with the “wins on more than half” statement.
- Add at least one **component ablation on MIKASA-Robo** (e.g., remove LRU; shared vs per-layer memory) to demonstrate that the mechanism driving gains in RememberColor also drives the robotics improvements.

## Score and Decision
**Originality:** Solid—layer-local memory integrated at every layer with explicit token↔memory interactions and bounded LRU-style rewrite is a clear architectural contribution.  
**Importance:** High potential for long-horizon robotics/partial observability, but the paper’s strongest framing hinges on extreme-horizon and large robotics gains.  
**Support for claims:** Mixed—the RememberColor ablations are strong; POPGym stats are weakly supported (3 seeds); and the most extreme horizon claim is asserted more strongly than is substantiated in the visible main text.  
**Experimental soundness:** Some good practices (ablation suite; sanity check on CartPole), but limited statistical power on POPGym and missing domain-ablation linkage for robotics in the visible text.  
**Clarity:** Generally clear in the extracted sections (especially RQ5/Table 3/Fig. 5 captions), though key support for headline claims is not present in the visible main text.  
**Value to community:** Potentially valuable if the extreme-horizon claim and robotics improvements are more rigorously and transparently substantiated.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>