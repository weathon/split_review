## Summary

NDS introduces a novel iterative search framework for vehicle routing problems that replaces the conventional autoregressive *construction* paradigm with a learned *deconstruction* policy: a neural network selects customers to remove from a solution, and a greedy insertion algorithm rebuilds the solution. Trained via REINFORCE without requiring reference solutions, NDS achieves strong numerical results across CVRP, VRPTW, and PCVRP with up to 2000 customers, outperforming state-of-the-art OR methods on 11 of 12 test settings and substantially outperforming prior learning-based approaches.

## Strengths

1. **Novel and well-motivated paradigm shift**: The paper replaces the dominant autoregressive construction paradigm with a learned deconstruction policy within a ruin-and-recreate search framework. This is a genuine departure from the existing literature and is clearly motivated by the throughput bottleneck of neural construction methods (line 24: 10k solutions/s for POMO vs. 120k/s for NDS).

2. **Ablations convincingly validate each architectural and algorithmic choice**: Table 2a shows that removing both the message passing layer (MPL) and tour encoding layer (TEL) causes a 1.5% performance drop on PCVRP; Table 2b shows that learned insertion order contributes significantly over random ordering; Table 2c shows that replacing the learned deconstruction policy with the Christiaens & Vanden Berghe (2020) heuristic causes up to 1.5% degradation. These ablations directly validate the paper's core design decisions and are a significant strength.

3. **Strong generalization across distribution shifts**: Section 4.4 (Table 3) evaluates NDS on CVRP instances with different vehicle capacities and location distributions, showing minimal performance gaps between in-distribution and out-of-distribution settings. This is a practically important result that goes beyond what most RL-for-CO papers demonstrate.

4. **Concrete scalability evidence**: Figure 3 shows that solving 1000-customer instances requires only 61% more runtime and 23% more memory than 100-customer instances, despite a 10× increase in problem size — providing useful evidence for practical applicability.

## Weaknesses

### Fatal
None.

### Major

1. **GPU-hardware asymmetry undermines the headline claim about surpassing OR methods.** The paper states that "All approaches are restricted to using a single CPU core" (line 143) and "we parallelize solely on the GPU, requiring only a single CPU core during test time" (line 110). In practice, NDS performs its core computation — DNN inference for 200 rollouts per instance with 8–128 augmentations — on an Nvidia A100 GPU (6912 CUDA cores), while HGS and SISRs are restricted to a single CPU core. The paper's central claim of surpassing state-of-the-art OR methods "under equal runtime" (line 256) conflates algorithm quality with hardware acceleration. The paper acknowledges GPU reliance as a limitation in the conclusion (line 258), but the abstract and introduction frame the results as an unqualified algorithmic victory. Notably, the paper's own throughput numbers reveal that SISRs explores 270k solutions/second (CPU) while NDS explores 120k/second (GPU), meaning the OR method is more than twice as computationally efficient per solution evaluated — yet this is never discussed.

   *Why this is major, not fatal*: The method's core innovations (learned deconstruction paradigm, architecture, training procedure) are validated by the ablations and by the fair comparisons against other learning-based methods (SGBS-EAS, LEHD, GLOP) where all use GPUs. The paper could be accepted with re-framed claims. However, the current framing is misleading.

### Minor

1. **Test-time initial solution is unspecified.** Section 3.4 describes improving "an initial solution s₀" but never states how s₀ is obtained at test time. During training, the paper generates N single-customer tours and improves them with J NDS steps (lines 55–59). The paper should explicitly state the test-time initialization procedure, as it affects the search trajectory and is necessary for reproducibility.

2. **No variance or confidence intervals for main results.** The test sets for N≥500 contain only 100–128 instances, but Table 1 reports no standard deviations, confidence intervals, or statistical significance measures. With modest gaps in some settings (e.g., "small advantage" over SISRs on larger instances, line 147), the reader cannot assess result reliability. This is standard practice in some parts of the CO literature, but for a venue like ICLR, it is a notable absence.

3. **16× augmentation difference between problem types is unexplained.** CVRP and VRPTW use 8 augmentations while PCVRP uses 128 (line 145) — a 16× difference with no justification. Since augmentations provide parallel search capacity, this raises the question of whether PCVRP results are inflated by additional parallel exploration rather than the method's intrinsic quality.

4. **"First learning-based approach" claim is not properly supported.** Line 26 states NDS is "the first learning-based approach that achieves this milestone" (surpassing OR methods). Given the GPU asymmetry issue (Major #1), this claim is not supported by the presented evidence. Beyond that, such priority claims are incidental to the paper's contribution and should be removed or replaced with a more precise statement.

5. **Time window handling in greedy insertion is not described.** Line 63 states that "various constraints, such as vehicle capacity limits, are taken into account" during greedy insertion. Time windows introduce substantially more complex feasibility constraints (ordering dependencies) than capacity alone. The paper should describe how insertion feasibility is checked under time windows.

### Trivial
None.

## Nice-to-Haves

- The throughput comparison (line 24: SISRs 270k/s vs. NDS 120k/s) actually provides evidence that NDS's *guidance* is better — it achieves superior results despite evaluating fewer solutions. The paper could strengthen its argument by discussing this angle.
- Running NDS on CPU-only (even if much slower) to compare solution quality at a fixed *solution-count budget* would disentangle algorithm quality from hardware acceleration.
- An analysis of how solution quality improves with training duration would strengthen the paper.

## Removed Points
These points are flagged as removed; treat them with caution.

1. **Harsh critic's assertion that GPU asymmetry is "fatal" and paper "should not be accepted"**: Removed because the paper acknowledges GPU reliance as a limitation (line 258); the core contribution (learned deconstruction paradigm) is validated by fair ablations and comparisons against other learning-based methods that also use GPUs; the issue is addressable through re-framing rather than being structurally fatal.

2. **"Ablations use reduced training, magnitudes may differ"**: Removed because this is a generic concern that applies to virtually all ablation studies in ML, where full-scale ablations are cost-prohibitive. The paper's ablations are already thorough relative to the norm in this field.

3. **"Comparison to SISRs/HGS inherits hardware asymmetry in OOD experiments"**: Removed because this is redundant with Major #1.

## Novel Insights

The most interesting observation that emerges from reading the reviews against the paper is the throughput tension the paper does not exploit. SISRs examines 270k solutions/second on a single CPU core while NDS examines 120k/second on an A100 GPU — the OR method is >2× more computationally efficient per solution evaluated. Yet NDS achieves better results. This actually implies the learned deconstruction policy provides genuinely superior search guidance that more than compensates for lower raw throughput. The paper currently treats throughput as a pure win ("NDS can process 120k solutions per second") without acknowledging that this advantage exists only relative to other neural methods (10k/s for POMO), not to the OR methods. A more nuanced framing — that NDS trades some raw throughput for smarter search — would actually strengthen the paper's case for the learned approach.

## Suggestions

- Reframe the central claim to honestly reflect the GPU-assisted nature of the comparison. For example: "NDS, accelerated by GPU parallelism, achieves better results than CPU-bound OR heuristics within equal wall-clock time, and the learned deconstruction policy is shown via ablations to be superior to heuristic deconstruction."
- Explicitly state how the test-time initial solution s₀ is generated (and consider comparing results from different initialization strategies).
- Report confidence intervals or standard deviations for main results in Table 1, or at minimum acknowledge the lack of statistical testing as a limitation.
- Justify the 16× augmentation difference between CVRP/VRPTW and PCVRP, or report PCVRP with 8 augmentations.
- Remove or soften the "first learning-based approach" claim.
- Describe how time window constraints are handled during greedy insertion.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>