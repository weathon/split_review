## Summary

This paper introduces Diffusion World Models (DWM), a method that adapts diffusion models to autoregressive world modeling by conditioning on a history of observations and per-frame actions. DWM operates directly in pixel space, avoiding the latent bottleneck that constrains prior world models. Experiments in 3D environments (CS:GO, motorway driving) show substantially better visual fidelity (FVD, FID, LPIPS) than DreamerV3 and IRIS at competitive sampling speeds, and Atari experiments demonstrate that DWM can serve as a surrogate environment for training RL agents, achieving competitive or superior scores.

## Strengths

- **Pixel-level diffusion avoids the latent bottleneck trade-off**: By operating directly in pixel space rather than through a compressed latent representation, DWM sidesteps the fundamental tension between token count and visual fidelity that constrains IRIS and DreamerV3. Table 1 shows DWM outperforms IRIS-64 (which uses 64 tokens) on FVD (186 vs. 397 in CS:GO) while being 2.8× faster at sampling (19 vs. 6.9 Hz).

- **Autoregressive generation with per-frame action conditioning**: Unlike video diffusion models that generate blocks of frames simultaneously or condition on a single variable, DWM generates frames one-by-one with causal action dependencies. Section 5.1.2 confirms that novel user-input actions steer the generated visuals as intended (e.g., steer-left moves the camera left), validating closed-loop functionality.

- **Favorable speed–quality trade-off**: DWM's sampling cost scales with denoising steps (τ=20) rather than latent token count K. Table 1 shows DWM achieves substantially better visual quality than DreamerV3 (which is faster at 174 Hz but has FVD of 1215 vs. 186 in CS:GO) while being competitive with or faster than IRIS at comparable quality.

- **Single-architecture, simple training objective**: DWM uses one U-Net with a standard MSE diffusion loss, avoiding the multi-objective end-to-end training of DreamerV3 or the two-stage autoencoder+transformer pipeline of IRIS (Section 3.2), simplifying the training pipeline.

- **Demonstrated utility for sample-efficient RL**: In Atari at 100k frames (Table 2), DWM achieves superhuman scores on Breakout, Krull, and RoadRunner, and outperforms both IRIS and DreamerV3 on Asterix and RoadRunner, validating that diffusion-based world models can effectively support model-based RL.

- **Honest analysis of failure modes**: Section 5.1.2 identifies limitations such as causal confusion (brake input predicting traffic stopping) and instability with out-of-distribution action sequences, attributing these to offline dataset properties rather than inherent weaknesses of DWM.

## Weaknesses

### Fatal
None.

### Major

- **The strongest headline claim is incompletely supported**: The abstract claims DWM is "an excellent choice for simulating visually complex worlds," but "simulating" implies usefulness for decision-making (consistent with the paper's own framing of world models as tools for planning, search, and RL). In the 3D environments (CS:GO, motorway driving), the evaluation stops at visual quality metrics (FVD, FID, LPIPS) — no planning, policy evaluation, imitation learning, or any downstream task is attempted. The RL experiments in Atari demonstrate downstream utility, but Atari has fundamentally simpler visuals than CS:GO or motorway driving. The paper is transparent about this split (Section 5.1 explicitly scopes to "directly evaluating the visual quality"), but the abstract's claim overreaches the evidence. The visual quality results are meaningful on their own, but the paper would be stronger with either a more precisely qualified claim or a downstream evaluation in one of the 3D environments.

### Minor

- **Atari RL comparison uses published baseline numbers rather than re-run under identical conditions**: Table 2 reports DWM results averaged over three training runs, but IRIS and DreamerV3 numbers are taken from prior publications. Differences in random seeds, hyperparameter tuning, early stopping, or hardware can shift results enough to blur the ranking. The issue is common practice in the RL literature and does not invalidate the results, but it adds uncertainty to the ordering on games where DWM underperforms or ties with baselines.

- **No discussion of rollout stochasticity**: Since DWM is a diffusion model, it samples from a distribution at each generation step — rollouts will differ given the same conditioning. The paper does not discuss how this stochasticity affects (or could be controlled for) RL training in imagination, where reproducibility of imagined trajectories can interact with policy learning. A brief discussion would be helpful.

### Trivial
None.

## Nice-to-Haves

- A small-scale downstream evaluation in one of the 3D environments (e.g., using DWM to generate synthetic trajectory augmentations for behavioral cloning in motorway driving) would substantially strengthen the claim that high visual fidelity benefits decision-making in complex visual domains.
- Breaking down training GPU-hours per method in Table 1 would complete the efficiency picture, although the paper already reports that all models were trained under matched conditions (120k updates, batch size 64, 1-2 days on up to 4×A6000 GPUs).

## Removed Points

- **"Paper does not report training compute cost for baselines"**: This criticism is factually incorrect. The paper states on line 191: "All models (baselines and DWM's) were trained for 120k updates with a batchsize of 64, on up to 4×A6000 GPUs. Each training run took between 1-2 days." Training compute is reported for both DWM and baselines under matched conditions.
- **"The ablations (Table 3) are not visible"**: The reviewer correctly notes this is a parser artifact; the table exists in the original submission.
- **Several generic strength-finder outputs**: Dropped strengths that were generic or redundant with the verified strengths above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Qualify the abstract's claim to more precisely reflect what is demonstrated: high visual fidelity in complex 3D environments and downstream RL utility in Atari. Alternatively, add a small-scale downstream evaluation in one of the 3D environments (even a simple behavioral cloning augmentation experiment) to directly support the broader claim.
2. Re-run IRIS and DreamerV3 under the same actor-critic setup for the Atari experiments, or at minimum provide a clear statement about the sensitivity of rankings to comparing against published numbers.
3. Add a brief discussion of how DWM's stochastic sampling affects the reproducibility of imagined rollouts and whether this has any practical implications for policy learning in the Dyna framework.

## Score and Decision

**Originality**: Strong — adapting diffusion models to autoregressive world modeling with frame-stacking and per-frame action conditioning is a novel and well-motivated contribution. **Importance**: The question of how to build high-fidelity world models is central to progress in model-based RL and simulation. **Claims**: The visual quality claims in 3D environments are well-supported by the evidence. The broader claim about being "an excellent choice for simulating visually complex worlds" is partially supported (in Atari for downstream use, in 3D only for visual quality). **Soundness**: The experiments are well-designed and the ablations are informative. The main methodological concern is the published-baseline comparison in Atari. **Clarity**: The paper is clearly written and well-organized. **Value**: The paper makes a clear empirical contribution by demonstrating that diffusion models can achieve substantially better visual fidelity than existing world models at competitive speeds, which is likely to influence future work.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>