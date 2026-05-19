- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed. Let me compose the consolidated review.

---

## Summary

SparseDFF proposes a method for one-shot learning of dexterous manipulation by constructing view-consistent 3D dense feature fields from sparse RGBD observations (4 fixed cameras). The key ideas are (1) distilling DINO features onto a 3D point cloud, (2) training a lightweight feature refinement network with contrastive loss on a single demonstration to improve cross-view consistency, and (3) pruning inconsistent points to create a clean feature field. The hand pose in a target scene is then optimized by minimizing feature differences to the demonstration under physical constraints. Real-world experiments on a Shadow Dexterous Hand (24 DoF) with both rigid and deformable objects show generalization across poses, object categories, and scene configurations.

## Strengths

- **Sparse-view 3D DFF construction that breaks the dense-view bottleneck.** Prior DFF methods (Shen et al., Kerr et al., Rashid et al.) rely on NeRF-based reconstruction requiring dense camera sweeps. SparseDFF instead performs point-cloud-based distillation from only K sparsely sampled RGBD scans (Sec. 3.1, Fig. 1), trained in ~300s on a single demonstration. This is a clear and practical improvement that enables one-shot deployment scenarios where dense camera movement is infeasible.

- **Real-world one-shot dexterous manipulation with cross-category generalization.** The method achieves real-world success rates of 60–100% on cross-category transfer (e.g., Bowl1 demo → Mugs: 80%; Monkey demo → SmallBear: 60%) on a 24-DoF Shadow Dexterous Hand (Tables 1–2, Fig. 5). This goes significantly beyond prior DFF-based manipulation work, which was limited to parallel grippers on geometrically similar objects. The gap over the naive DFF baseline (e.g., 0% vs 100% on Box1→Box2, 0% vs 60% on Monkey→SmallBear) demonstrates that the refinement and pruning mechanisms are not incremental.

- **Feature refinement and point pruning mechanisms are visually shown to be necessary.** The ablation figures (Figs. 6–7 in the paper) provide direct visual evidence: the refinement network concentrates low-energy regions at the hand's target location, while the baseline has scattered energy; the pruning mechanism removes outlier points and yields stable hand poses. While the ablations are qualitative rather than quantitative, the visual contrast is stark and consistent with the downstream success-rate improvements.

- **Real-world hardware validation with multiple sensors.** The method is evaluated on a physical Shadow Dexterous Hand + UR10e arm with four calibrated Azure Kinect sensors, using real point clouds with noise, occlusions, and deformable objects (Sec. 4, "Environment"). This is a practical achievement over methods evaluated solely in simulation or on clean synthetic data.

- **Beyond grasping: diverse hand-object interactions.** The paper demonstrates not just functional grasping but also head caressing and butt patting (Fig. 8), showing the feature field supports arbitrary end-effector poses beyond prehensile actions.

- **Efficient runtime.** Training takes ~300s (20K iterations) and target optimization takes ~20s (300 iterations) on a single RTX 3090 (Sec. 4). This is practical for one-shot deployment and far faster than NeRF-based DFF methods requiring hours of rendering.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited baseline comparison.** The paper compares against only two methods: (i) a naive DFF baseline (direct DINO back-projection without refinement/pruning), which is essentially an ablation of the paper's own contributions, and (ii) UniDexGrasp++ evaluated in simulation with a state-based model (no real-world noise). While these comparisons demonstrate the value of the paper's specific components, there is no comparison to any alternative one-shot manipulation method — the paper cites Wei et al. (2023) in related work as the closest comparable approach but does not benchmark against it or any other existing method. The DFF baseline is informative but insufficient to fully contextualize the method's overall performance relative to the state of the art.

- **No statistical confidence in quantitative results.** All success rates (Tables 1–2) are based on 10 trials per condition. For several conditions (e.g., Bowl2: 80%, CatBowl: 60%, FloatingMug: 40%, Monkey→SmallBear: 60%), the wide confidence intervals implied by N=10 make the precise numbers unreliable. The large effect sizes (e.g., 80% vs. 0% against DFF) are meaningful, but the exact magnitudes of the lower-performing conditions are imprecise.

- **Ablations are purely qualitative.** The ablation studies for the feature refinement network (Fig. 6) and point-pruning mechanism (Fig. 7) are shown only as PCA-colored feature visualizations and energy maps. No quantitative metric (e.g., success rate with/without each component, feature correspondence accuracy, optimization convergence statistics) is provided. While the visual evidence is suggestive, the paper claims these components are "central" to the method (Sec. 3.1–3.2) but provides no experimental numbers proving they causally drive performance.

- **Missing failure-case analysis.** Cross-category transfer results are uneven (40–60% on Bowl→FloatingMug, Monkey→SmallBear, SmallBear→Monkey), but the paper does not analyze why these conditions fail while others succeed. There is no discussion of failure cases, feature similarity maps for failed grasps, or characterization of when the cross-scene feature correspondence assumption breaks down. This limits the reader's ability to assess the method's robustness boundaries.

- **Missing implementation details that hinder reproducibility.** Several hyperparameters are mentioned but values are not given: the radius *r* and threshold *δ* for point-pruning (Eq. 4, line 93–98), the contrastive learning temperature *τ* (Eq. 2, line 85), and the architecture of the "shallow per-point MLP" and projection head *g* (Sec. 3.1). The distance function *d(·,·)* in the penetration energy terms (Eq. 5) is also not defined.

- **"Beyond grasping" section lacks quantitative evaluation.** The diverse hand-object interactions (head caressing, butt patting, Fig. 8) are presented with qualitative examples only — no success rates or metrics are reported, making these claims difficult to evaluate.

### Trivial
- The paper does not include a limitations paragraph in the conclusion (Sec. 5), which would help frame the method's scope for future work.

## Nice-to-Haves

- Conducting ablations on the number of camera views (e.g., 2 or 3 cameras vs. 4) would help characterize the method's sensitivity to view count.
- Comparing against an alternative feature backbone (e.g., CLIP or LSeg instead of DINO) would illuminate whether the findings are encoder-dependent or more general.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No code or model release is mentioned"** — Removed per rules: criticism about release status of something not promised or standard to require. This is a soft suggestion at most.
- **"Total number of objects is small"** — Removed as a generic criticism. 4 rigid + 3 deformable object sets with real-world hardware evaluation is a reasonable experimental scope.
- **"No comparison to other feature backbones (CLIP, LSeg)"** — Removed as scope creep. The paper is about a specific method for sparse-view DFF with DINO; comparing feature backbones is a separate investigation and not a core flaw.
- **"Evaluation uses manually positioned hand model" criticism** framed negatively — Removed; this is explicitly described in the paper (Sec. 4, lines 151–152), is standard practice in one-shot manipulation research, and the paper does not claim fully automated demonstration generation.
- **Laundry list of hypothetical limitations** (fewer cameras, lighting, textureless objects) — Removed; these are generic what-if questions not grounded in any experiment or evidence in the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely reinforce each other on the core strengths (novel sparse-view DFF construction, real-world dexterous manipulation results) and agree on the main weaknesses (limited baselines, qualitative-only ablations, small-N statistics). No reviewer identified a capability or failure mode the paper itself does not already surface.

## Suggestions

1. **Add quantitative ablations:** Report success rates (or an optimization-based metric) with and without the refinement network and the pruning mechanism, using the same 10-trial protocol as the main experiments. This would directly substantiate the claim that these components are "central" to performance.
2. **Expand the baseline set:** Even one additional comparison — for example, adapting a geometric correspondence method (related to Wei et al. 2023) to the same objects in simulation, or running SparseDFF alongside UniDexGrasp++ on the same platform — would significantly strengthen the contextualization of results.
3. **Analyze failure cases:** For the 40–60% conditions in Tables 1–2, show what the optimized hand pose looks like, measure the final feature distance vs. successful cases, and discuss why the feature field underperforms. This would turn a weak point into a strength.
4. **Report confidence intervals or trial-level data** for the success rates, or increase N for the lower-performing conditions to improve statistical reliability.
5. **Report hyperparameter values** for *r*, *δ*, *τ*, and the MLP architecture in the main text or appendix for reproducibility.
