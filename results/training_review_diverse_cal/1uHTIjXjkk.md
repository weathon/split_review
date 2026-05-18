I have enough information to write the final review. Let me now construct it.

---

## Summary

This paper proposes a potential-based diffusion motion planner that learns trajectory-level energy functions via a denoising diffusion objective. The key ideas are: (1) learning a potential landscape over motion planning trajectories that can be efficiently optimized through the diffusion model's annealed sampling process, avoiding the local minima problems of classical potential-based planning; (2) composing independently learned diffusion potential functions by summing their gradients, enabling generalization to unseen combinations of obstacles and constraints. The method is evaluated on 2D (Maze2D), 7D (KUKA arm), and 14D (Dual KUKA) configuration spaces, showing competitive success rates and collision-check efficiency against both classical (RRT*, BIT*, P-RRT*) and learned (MPNet, MπNet, AMP-LS) baselines.

## Strengths

1. **Novel conceptual framing and effective empirical instantiation of potential-based planning via diffusion models.** The paper connects two previously separate ideas — classical potential-based motion planning and diffusion-based trajectory generation — and demonstrates that diffusion models can serve as learnable, optimizable potential landscapes. The approach directly addresses the long-standing local minima problem of classical potential planners: on Maze2D with concave obstacles, the method achieves 100% success vs. 28% for classical potential-based RMP (Table 2), with BIT* requiring 3× the planning time.

2. **Compositionality enables generalization beyond training distribution.** The paper demonstrates that summing gradient fields of independently trained diffusion potential functions allows the model to generalize to environments with more obstacles than seen during training (Figure 7) and to combine static and dynamic obstacle models (Table 3: 96.6–97.5% success vs. 70.4–74.0% for SIPP). The method maintains >95% success composing two 6-obstacle models on 11-obstacle environments where MπNet drops below 60%. This capability is practically valuable for robotics settings where constraints arise ad-hoc.

3. **Strong empirical scaling to high-dimensional configuration spaces.** The method achieves consistent performance across 2D, 7D, and 14D spaces, while baseline success rates degrade sharply with dimensionality. In 14D Dual KUKA, the method leads MπNet by ~35% in success rate while requiring 7× fewer collision checks and lower planning time (0.93s vs. 3.98s).

## Weaknesses

### Fatal
None. The paper's core empirical results appear sound and its main claims are supported by evidence.

### Major

1. **The source of training trajectories is not disclosed, which is critical for interpreting performance claims.** The paper trains on a dataset D of "solved motion planning problems" (line 108) but never specifies how these trajectories were generated — whether by an existing planner (e.g., BIT* or RRT*), an oracle, or hand-crafted ground truth. If the training data came from BIT*, then outperforming BIT* at test time is a form of amortization (still valuable, but changes what the paper demonstrates). If trajectories come from a different source, that changes interpretation further. Without this information, readers cannot assess whether the method's strength comes from the learned potential or from the quality/source of the training data. This is the single most important missing detail in the paper.

2. **The compositionality claim, presented as a main contribution, lacks analysis of when or why additive potentials yield correct samples.** The paper states that the composite potential "will have low energy precisely at motion planning paths which satisfy both constraints" (line 167) and samples by summing gradient fields. However, summing score functions from *independently trained* diffusion models is not theoretically guaranteed to produce samples from the product of the corresponding distributions — the score functions may be uncalibrated relative to each other across denoising steps. While the empirical results are positive, the paper claims compositionality as contribution #3 (line 36) and highlights it in the teaser and Section 4.3, yet provides no analysis of failure modes, conditions under which composition might break, or calibration of the composed scores. The limitations section mentions linear scaling cost but not this more fundamental concern.

### Minor

1. **MPD, a diffusion-based planning baseline, is absent from the main quantitative comparison (Figure 3).** MPD (Carvalho et al. 2023) is included only in Table 2 (concave Maze2D), where it achieves 44.4–77.9% success — well below the proposed method. While the paper notes that many 2D-constrained methods exist (line 53), MPD is a directly relevant diffusion-based planner and its inclusion in the main bar plots would strengthen the experimental comparison.

2. **Collision-check counting is not defined.** The paper reports collision checks as a key metric (Figure 3) but does not specify how checks were counted for each baseline — e.g., whether every node evaluation, edge check, or only final trajectory verification was counted. This matters because the metric structurally favors planners that output a single trajectory without explicit collision checking during generation. The paper should define this precisely for reproducibility.

3. **Probabilistic completeness "proof" (Section 3.6) is a sketch with unjustified assumptions.** The proof assumes (i) the model's output distribution has strictly positive density everywhere, and (ii) every valid trajectory has a full-dimensional open neighborhood of valid trajectories. Neither assumption holds in general — near obstacle boundaries, arbitrarily small perturbations can produce collisions, so property (ii) fails. Additionally, the proof does not account for conditioning on start/goal states or the iterative denoising procedure. This section should either be removed or replaced with a more rigorous argument.

4. **Real-world experiments (ETH/UCY) are qualitative only.** Section 4.5 presents qualitative trajectory visualizations but no quantitative success rates, collision rates, or comparisons against baselines. The paper frames these as "illustrat[ing] the potential" (line 577), which is acceptable for a demonstration, but the lack of numbers limits the strength of the real-world claims.

5. **Neural network architecture for the energy function E_θ is not described.** The paper does not specify whether E_θ is a Transformer, UNet, or MLP, nor does it describe input encoding or parameter count. Architecture is referenced only via a project website link. This hinders reproducibility.

6. **Training cost not reported.** The paper reports planning time but not training time, GPU resources, or number of training problems. This information is relevant for practitioners assessing practicality.

### Trivial
None.

## Nice-to-Haves
- Analyze failure modes in composition (e.g., when do composed potentials produce conflicting gradients?).
- Analyze how the noise scale k in the motion-refining algorithm (Algorithm 2) affects trajectory quality.
- Include quantitative metrics for real-world experiments (success rate, collision rate).

## Removed Points

- **"The method is effectively a standard conditional diffusion model with only a language change"** — This criticism misunderstands the paper's contribution. The paper's framing as potential-based planning with energy-based diffusion training (Du et al. 2023) is a substantively different formulation from standard diffusion planners like Diffuser. The training objective (Eqn 3) directly learns an energy landscape, not just a denoising score. Removed: misunderstanding of the paper.

- **"Collision-check advantage is misleading because it's baked into the design"** — The paper compares against other learned planners (MPNet, MπNet, AMP-LS) on the same metric, so the comparison is fair within each category. All learned planners benefit from amortization. The claim about collision checks is specifically quantified against both sampling-based and learning-based baselines. Removed: the criticism is factually inaccurate about the comparison being misleading.

- **"Composition via naive addition of gradients does not in general correspond to sampling from the product distribution"** — While technically correct as a theoretical concern, this is a standard technique in diffusion models (used in classifier guidance, compositional generation, etc.). Calling it "naive" and "especially problematic" overstates the issue; the paper provides strong empirical validation. Kept as a Major weakness but rephrased to reflect that the lack of *analysis* (not the approach itself) is the gap. The original phrasing is removed as it mischaracterizes a standard technique as fundamentally flawed.

- **Criticisms about the motion-refining algorithm lacking analysis of noise scale k** — This is a reasonable suggestion but is a standard denoising process. The paper shows the algorithm works across three environments with different dimensions (Table 2), which is sufficient empirical validation. Downgraded from the harsh critic's framing to Nice-to-Haves.

- **Suggestions about missing appendix content** — The parser strips appendix sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Explicitly state the planner/data source used to generate training trajectories, the quality filter (if any), and whether trajectories are optimal or merely feasible. Report success rates relative to that oracle if applicable.

2. For the compositionality claim, either (a) provide theoretical conditions under which additive diffusion potentials yield correct samples (e.g., if score functions are well-calibrated and the noise schedule is shared), or (b) clearly delimit the claim to the demonstrated empirical setting and add controlled experiments testing interference between composed potentials from independently trained models in adversarial configurations.

3. Add MPD to the main bar plots in Figure 3 for any environment where it can be run, and define collision-check counting explicitly for each method.

4. Provide the neural network architecture details (at minimum: backbone type, number of parameters, input representation) in the main paper or a referenced appendix.

## Score and Decision

**Score: 5.5 / 10**

The paper presents a novel and empirically well-supported approach to potential-based motion planning via diffusion models. The core idea is sound, the experiments span multiple dimensions and demonstrate meaningful improvements over strong baselines, and the composition results are practically interesting. However, the undisclosed training data source is a significant gap that undermines interpretation of the main results, and the compositionality claim — a highlighted contribution — lacks the theoretical analysis its prominence merits. With clarifications on data generation, expansion of the MPD comparison, and proper scoping of the composition analysis, the paper would be substantially stronger.

**Decision: Reject**

The missing training data provenance and the shallow treatment of the compositionality mechanism are gaps that affect the paper's core evidentiary chain, not minor presentation issues. These are addressable in revision, but in the current form the paper does not make a convincing case for acceptance at a top venue.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>