Now I have a solid calibration. Let me synthesize the final review.

## Summary

GPUDrive is a GPU-accelerated, multi-agent driving simulator built on the Madrona engine that achieves over 1 million agent steps per second (ASPS) using data from the Waymo Open Motion Dataset. The simulator supports LiDAR, radial filter, and human-like view-cone observations, provides gymnasium-compatible PyTorch/JAX interfaces, and includes pre-trained RL baselines. The paper demonstrates that IPPO can train agents to 95% goal-reaching on individual scenes in minutes and that per-scene training time amortizes to ~15 seconds when scaling to 1024 scenarios.

## Strengths

1. **Demonstrated throughput of 2–3 orders of magnitude over CPU baselines**: GPUDrive achieves a peak of 2.3M ASPS and 200K–500K CASPS (controllable-agent steps per second), compared to ~15K ASPS for Nocturne (Figure 3). This is the paper's strongest piece of evidence and is clearly supported by multiple measurements across consumer (RTX 4080) and datacenter (A100) GPUs.

2. **Well-motivated engineering design with clear evidence of impact**: The use of BVH acceleration for collision checks, polyline decimation (10–15× point reduction via Visvalingam-Whyatt), and memory allocation proportional to actual agent counts (rather than maximums) are concretely described and directly connected to the scalability results (Section 3.1).

3. **LiDAR observation is ~3× faster than radial filter (Figure 4)**: This is a distinct and practically meaningful advantage — it shows that GPU-accelerated sensor simulation is not a trade-off against speed, and it positions GPUDrive as the only simulator in Table 1 that provides GPU-accelerated sensor simulation alongside data-driven features.

4. **Amortized training time decreases with scenario count**: The paper documents that per-scene training cost drops from ~2.2 min at 32 scenarios to ~15 sec at 1024 scenarios (Figure 6). This sub-linear scaling is a real strength: it demonstrates that the simulator's parallelism overhead is efficiently amortized, making multi-scenario RL feasible on a single GPU.

5. **Comprehensive comparison to 15 existing simulators (Table 1)**: The table systematically covers multi-agent support, GPU acceleration, sensor simulation, expert data, sim agents, and routes/goals, providing clear positioning relative to prior work.

## Weaknesses

### Fatal
None. The core claims about simulator throughput and scalability are well-supported by the experiments presented.

### Major

1. **No held-out evaluation of trained agents — training curves are on training scenarios**. The paper reports "solving" scenes to 95% goal-reaching and treats this as evidence that GPUDrive enables practical RL, but every reported metric (Figures 5, 6) is measured on the same scenarios used for training. There is no validation split, no generalization metric, and no analysis of whether the learned policies transfer to unseen scenarios. The paper frames this as "solving" scenes (Section 4.2: "we mark a scene as solved when agents can navigate to their designated target position 95% of the time"), but the claim being demonstrated is rapid scene-specific memorization, not learning of generalizable driving policies. For a benchmark that aims to "unlock multi-agent learning as a tool for generating capable self-driving planners," this gap undermines the central demonstration of the simulator's utility for learning. *Verification: Section 4.2 and Figure 5 caption refer to "training performance" on "10 scenarios from the WOMD" with no mention of a held-out split.*

2. **Waymax comparison is insufficiently documented**. The paper states "we could not run more than 16 environments in parallel due to Out of Memory (OOM) issues" (Section 4.1), but provides no configuration details: GPU memory capacity, observation type used, number of agents per world, batch size, or whether Waymax was used with default or optimized settings. Since this comparison is central to the claim that GPUDrive "surpasses Waymax" and appears in Figure 3 (right panel), the lack of documentation makes it unreproducible. The claim may well be correct (Waymax's JAX-based static memory allocation is a known limitation), but the current evidence does not enable the reader to verify it. *Verification: Section 4.1, lines 164–165; the text does not provide any configuration details for the Waymax run.*

### Minor

3. **Title and headline throughput metric emphasize ASPS when CASPS is the operationally relevant number**. The title advertises "1 Million FPS" and the abstract says "over a million simulation steps per second" — both referring to ASPS, which counts all objects including parked cars, cyclists, and pedestrians. The paper's own RL experiments report 200K–500K CASPS (Section 4.2), which is the throughput a user of the simulator actually obtains for learning. The paper does transparently report both metrics and explains the distinction, so this is primarily a framing concern, but it is misleading for a benchmark paper to lead with a number that overstates usable throughput by ~5×.

4. **No collision or off-road rates in training curves**. The training curves (Figure 5) show only goal-reaching rate. For driving, collision rates and off-road events are equally important dimensions of agent quality. The "solve" definition includes "without colliding or going off-road" (Section 4.2), but neither metric is plotted or tabulated, making it impossible to assess whether the 95% goal-reaching comes at the cost of frequent collisions. *Verification: Figure 5 only shows "Training performance (%)" — from context, this is goal-reaching rate only.*

5. **Out-of-distribution test claim is unsupported**. The paper states that trained agents are "extremely aggressive about reaching their goals and can be used as an out-of-distribution test for proposed driving agents" (Section 3.2), but provides no evidence of this property, no characterization of what "aggressive" means quantitatively, and no protocol for how they should be used as adversaries. *Verification: Section 3.2, last paragraph of "Available driving simulation agents."*

### Trivial
None.

## Nice-to-Haves
- Report collision and off-road rates alongside goal-reaching in Figure 5.
- Provide hardware/configuration details for the Waymax comparison (GPU model, memory limit, observation type, number of agents per world).
- Add an analysis of scenario difficulty diversity in the 1000-scene training subset.
- Clarify the resolution/ray count used for LiDAR observations.

## Removed Points
- **"Table 1's GPU-Accel column is misleading for CARLA"**: CARLA uses GPU for rendering but its physics and simulation loop are CPU-driven; the column reflects whether the *simulation itself* (not rendering) is GPU-accelerated. This is a reasonable categorization.
- **"Figure 3 does not show Waymax in the left panel"**: This is a figure layout choice, not a weakness — Waymax is shown in the right panel.
- **"No discussion of Waymax's JIT compilation strategy or memory model"**: This is a depth-of-comparison concern subsumed by Major Weakness 2 (insufficient documentation of the comparison), not a standalone issue.
- **Strength Finder generic strengths** (e.g., "the paper addresses an important problem"): Removed per filtering rules; these add no specific information.

## Novel Insights
The review process surfaces a tension that the paper itself does not directly address: GPUDrive's primary contribution is as a *systems engineering achievement* (throughput, memory efficiency, sensor support), yet the paper is submitted to the "Datasets and Benchmarks" area, which requires evidence that the simulator enables meaningful research progress. The speed numbers are genuinely impressive and well-measured, but the benchmark claims rest on RL training demonstrations that are evaluated on training data only. This mismatch between the paper's framing (a benchmark for multi-agent driving research) and its strongest evidence (raw simulation throughput) is the central unresolved issue.

## Suggestions
1. **Add a held-out evaluation**: Evaluate the agents trained in Section 4.2 on 100+ unseen scenarios from the WOMD. Report goal-reaching, collision, and off-road rates separately on this held-out split. This single experiment would transform the paper from "we can memorize scenes fast" to "the simulator enables learning of generalizable driving policies."
2. **Document the Waymax comparison**: Report the GPU model, memory capacity, observation type, number of agents per world, and any settings used. If the comparison was run with a specific configuration, say so. This is a simple, factual addition.
3. **Lead with CASPS in the abstract**: The abstract currently says "over a million simulation steps per second" without qualification. Adding "of which ~200K–500K are controllable agents" would be more transparent and would not weaken the paper — 200K CASPS is still very fast.

## Score and Decision

**Round 1 bracketing**: The first calibration search placed the paper in the 3.5–7.5 band. Below 3.5: papers with withdrawn/rejected decisions and fundamentally flawed methods (scores 2.5–3.25). Above 7.5: oral/spotlight papers with strong theory or comprehensive evaluation (scores 8.0). GPUDrive has clear evidence for its core engineering claims but missing evaluation rigor, placing it clearly in the middle band.

**Round 2 narrowing**: Anchors read in full:
- **POGEMA (5.67, accepted poster)**: Benchmark paper with extensive algorithm evaluation but criticized for simple tasks. GPUDrive has stronger technical novelty but weaker evaluation methodology. *Comparable overall; GPUDrive slightly weaker on evaluation rigor.*
- **LCSim (4.75, withdrawn/rejected)**: Traffic simulator with diffusion-based agents but CPU-only, slow, and had overclaimed novelty. *GPUDrive is clearly stronger.*
- **DriveArena (5.75, rejected)**: High-fidelity generative simulation, criticized for lack of novelty (combination of existing methods). *GPUDrive has clearer engineering novelty but similar evaluation gaps.*
- **Trajeglish (6.0, accepted poster)**: Traffic modeling paper with clean methodology but small improvements. *GPUDrive has stronger engineering evidence but missing held-out evaluation.*

**Final score**: 5.5. The paper's engineering contribution is solid and well-evidenced, but the held-out evaluation gap and the opaque Waymax comparison are significant omissions for a benchmark paper. Addressing these would make this a strong 6+ paper. In its current form, the core speed claims are supported, but the benchmark framing is incomplete.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>