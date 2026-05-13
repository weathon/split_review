Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

AutoNeRF proposes using trained modular exploration policies to autonomously collect data for NeRF training in 3D indoor environments, replacing manual data collection. The paper introduces four reward functions (explored area, obstacle coverage, semantic coverage, viewpoint coverage) for training the exploration policy and proposes a multi-task evaluation framework that goes beyond standard rendering metrics to assess NeRFs on mapping, planning, and pose refinement tasks. Empirical results on 5 Gibson-tiny validation scenes show modular policies consistently outperform frontier-based and end-to-end baselines across all downstream tasks.

## Strengths

- **Multi-task evaluation framework for NeRFs is a genuine contribution.** Prior NeRF work evaluates almost exclusively on rendering metrics; this paper evaluates on map quality, planning success (PointGoal and ObjectGoal), and pose refinement (Tables 2–5), which directly supports the robotics motivation and provides a more informative assessment of how exploration policy choice impacts downstream utility (Section 4.3).

- **Consistent empirical advantage of modular policies across all tasks.** Across all four evaluation tasks and all metrics, modular policies outperform both frontier-based exploration and end-to-end RL baselines. The margins are substantial: e.g., PSNR improves from ~23–24 (best E2E) to ~25 (modular), and PointGoal Success from 32.8 (best E2E) to 39.5 (modular cov.) — a ~7-point gap (Tables 2–5).

- **The viewpoint coverage reward is a principled and novel contribution.** The 3D map `m^{view}` discretized into 12 angle bins (Section 4.1) is specifically designed to capture multi-view diversity needed for NeRF training, going beyond standard coverage-based exploration rewards. Table 3 shows it achieves the highest occupancy accuracy (88.1) and map precision (37.4), confirming it captures structural information effectively.

- **Table 6 provides honest assessment of the sim-to-real gap.** The comparison between GT semantics and Mask R-CNN semantics (mIoU dropping from 83.2 to 61.1, ObjectGoal Success from 15.8 to 6.8) is transparent about the performance drop when removing simulator privileges, which many papers in this space would omit.

- **Demonstrated scalability to house-scale scenes and practical application for policy adaptation.** The paper shows qualitative mesh reconstructions of full apartments (Figure 3) and quantitative evidence that AutoNeRF-reconstructed meshes can be used to finetune PointGoal navigation policies, improving Success from 90.2 to 92.9 (Table 1).

## Weaknesses

### Fatal
None.

### Major

- **Main results rely on ground-truth camera poses and semantics, undermining the "autonomous" claim.** The paper frames itself as enabling "autonomous" NeRF construction, but all main quantitative results (Tables 2–5) use privileged pose and semantic information from the simulator (Section 4.2: "In our experiments, we leverage privileged pose and semantics information from simulation"). Table 6 shows semantic mIoU drops from 83.2 to 61.1 and ObjectGoal Success from 15.8 to 6.8 when switching to Mask R-CNN — demonstrating the version that actually works well is not fully autonomous. Crucially, no experiment tests pose noise (e.g., from SLAM drift), which is known to severely degrade NeRF quality. The paper thus establishes strong results for an oracle-assisted pipeline, but the gap to a truly autonomous system remains unquantified for pose estimation and large for semantics. This limits the practical significance of the claims.

- **All quantitative comparisons rest on 5 test scenes with no variance reporting.** Every table reports results from 5 scenes in Gibson-tiny val, with 5 rollouts per scene (25 total trajectories per method). No standard deviations, confidence intervals, or significance tests are reported. Some margins between methods are modest (e.g., Ours (obs.) PSNR=25.56 vs. Ours (view.) PSNR=25.17; Ours (cov.) PointGoal SPL=39.0 vs. Ours (view.) SPL=38.6). With 5 scenes and no variance, it is impossible to assess whether these differences are meaningful rather than noise. This is a significant gap for drawing reliable comparative conclusions, especially about reward function design.

- **Comparison between exploration strategies confounds architecture with strategy.** The modular policies use a built semantic map, depth-based occupancy mapping, Mask R-CNN semantics, and a Fast Marching local planner. The end-to-end baselines from Ramakrishnan et al. use a fundamentally different (and less information-rich) observation/action pipeline. The modular policy's superiority may reflect its richer input representation and analytical local planning rather than the exploration strategy itself. The claim that "modular trained exploration models outperform" is thus confounded — it is a system-level comparison, not an isolated test of exploration strategies. An ablation controlling for the perceptual/planning infrastructure would be needed to isolate the contribution of the global policy.

### Minor

- **The viewpoint coverage reward only accounts for horizontal viewing angle.** The 3D map `m^{view}` discretizes angles into V=12 bins on the floor plane (Section 4.1), capturing azimuth diversity but not vertical look direction or distance to surfaces — both relevant for NeRF quality. This is partially justified by the agent's action space (floor-plane navigation only), but limits the claim that this reward captures "viewpoint diversity" in the full sense needed for novel view synthesis.

- **House-scale reconstruction and adaptation experiments use a different NeRF variant (vanilla Semantic NeRF) than the main experiments (Semantic Nerfacto) without bridging comparison.** Section 4.2 acknowledges this switch was made because "meshes are of higher quality" with vanilla NeRF, but no experiments compare the two variants on the same evaluation protocol, making it hard to contextualize these qualitative results with the quantitative tables.

- **The adaptation experiment (Table 1) uses only 4 scenes and lacks variance.** The upper bound also uses a 10× higher learning rate (2.5e-5 vs 2.5e-6), making the ceiling less directly comparable. The improvement (90.2→92.9 Success) is modest and hard to assess without variance.

### Trivial
None.

## Nice-to-Haves

- **Pose noise experiment**: Adding Gaussian noise to GT poses at varying magnitudes would bound real-world NeRF quality degradation and substantially strengthen the practical relevance argument.

- **Controlled ablation isolating the global policy from the modular infrastructure**: Running E2E baselines with access to the same semantic map and Fast Marching local planner would clarify how much of the performance gap comes from the exploration strategy vs. the architectural scaffolding.

- **Standard deviations across scenes/rollouts**: Even with 5 scenes, reporting variance would allow readers to assess the reliability of claimed differences between methods.

- **Closed-loop active exploration**: The current pipeline is open-loop (explore → train NeRF). Using NeRF uncertainty to guide further data collection would connect more directly to the active NeRF literature cited in Section 2.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing active NeRF baselines (ActiveNeRF, ActiveRMAP)"** — The paper explicitly addresses this (Section 2, line 39), noting these methods "target very small scenes in non-robotic scenarios." Adapting them to large indoor robotic exploration would require substantial engineering outside the paper's scope, and these methods address a fundamentally different (object-level) problem setting.

- **"Rendering evaluation underspecified (number of sampled poses, distribution)"** — The paper states the poses are "uniformly sampled camera poses within the scene, independently of the trajectory taken by the policy" (Section 4.3), which is sufficient specification. This is a minor reproducibility detail rather than a methodological concern.

- **"No failure cases shown"** — While showing failure modes could strengthen the discussion, their absence does not undermine the quantitative claims.

- **"The 'single episode' claim is untested without oracle information"** — The paper demonstrates that a single episode of exploration *with oracle NeRF training inputs* produces useful representations. The concern about oracle inputs is already captured in the major weakness about privileged information. This specific framing duplicates that concern.

## Novel Insights

The key insight emerging from this work is that standard visual coverage (as optimized by frontier-based exploration) produces surprisingly poor NeRF training data — not because the scene isn't covered, but because coverage ≠ viewpoint diversity. The modular policies enter rooms and capture multi-angle observations of objects, which matters more for neural radiance fields than mere spatial coverage. This disconnect between exploration objectives (coverage) and representation objectives (multi-view consistency) is an important conceptual finding that should inform future active vision for neural rendering systems.

## Suggestions

- Report means ± std across the 5 scenes × 5 rollouts to allow readers to assess statistical significance of claimed differences between methods and reward functions.
- Add an experiment with noisy (e.g., SLAM-simulated) camera poses to quantify the real-world performance gap, since GT poses are the single largest oracle assumption.
- Add an ablation where E2E baselines are given the semantic map and analytical local planner, to isolate the contribution of the global exploration policy from the modular infrastructure.

## Score and Decision

AutoNeRF addresses a real and timely problem, proposes a reasonable modular approach with a genuinely useful multi-task evaluation framework, and shows consistent improvements over baselines. However, the empirical foundation has significant gaps: all main results depend on privileged simulator information (GT poses and semantics), no variance is reported on 5 test scenes, and the comparison confounds architecture with exploration strategy. These issues don't invalidate the contribution but substantially weaken the claims about "autonomous" NeRF construction and the relative merits of different exploration strategies.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>