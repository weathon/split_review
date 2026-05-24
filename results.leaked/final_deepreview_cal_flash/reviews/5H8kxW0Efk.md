Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes a data-driven approach to combinatorial optimization that learns the update dynamics of an Ising machine via a small MLP, trained with zeroth-order (evolutionary) optimization. The core idea — applying algorithm unrolling to Ising-machine dynamics for NP-hard Max-Cut — is novel, and the paper provides insightful analysis showing that momentum-like effects emerge spontaneously during training. Empirical results on G-set Max-Cut benchmarks demonstrate that the learned dynamics (dNPIM) achieve competitive or better time-to-solution compared to hand-tuned Ising machine baselines (CAC, CFC, dSBM) on 4 of 5 instance groups.

## Strengths

1. **Genuinely novel approach combining algorithm unrolling with Ising machines.** The paper applies algorithm unrolling — a technique previously limited to convex or continuous optimization — to NP-hard combinatorial optimization (Max-Cut/Ising). The MLP parameterization with odd symmetry, Fourier temporal basis, and the cNPIM/dNPIM variants are well-motivated design choices. This is a distinct departure from the GNN-based paradigms that dominate neural CO, and the paper makes a clear case for why this direction is promising.

2. **Insightful analysis of learned dynamics.** Section 4 is the strongest part of the paper. Figure 2 demonstrates that a single-layer network, starting from random weights, first learns greedy steepest descent and then spontaneously develops momentum-like behavior — a non-trivial emergent property of reward maximization. The contrast between cNPIM (continuous coupling, higher average reward but overfits and fails on hardest instances) and dNPIM (discrete coupling, more robust) in Section 4.5 is particularly valuable, offering architectural guidance beyond the paper's core results.

3. **Strong Ising-machine benchmark results.** Table 2 shows dNPIM achieving lower median TTS than three strong hand-crafted Ising machines (CAC, CFC, dSBM) on 4 of 5 G-set instance groups, with the planar unweighted case as the exception. Since TTS inherently accounts for both per-trajectory speed and success probability, this is a meaningful comparison. The baselines also undergo per-instance-type tuning, making the comparison fair along that dimension.

4. **Parameter-efficient and principled training.** The use of zeroth-order evolutionary optimization (rather than backpropagation or REINFORCE) is well-motivated by the vanishing/exploding gradient problem in long unrolled trajectories. The total parameter count is small (tens to low hundreds), and the method requires no gradient computation through the dynamics, which is a practical advantage.

## Weaknesses

### Major

1. **Unfair comparison protocol in Table 1 (neural CO benchmarks).** dNPIM is reported as "top 30" — the best out of 30 parallel trajectories — while the baselines (DiffUCO, SDDS, LTFT) report mean ± std over an unspecified number of runs. Taking the best of 30 introduces selection bias that is not matched in the baseline evaluation. The paper's justification ("less computationally intensive per trajectory") is incomplete: for MIS-large and MaxCut-large, dNPIM takes 1:20 vs 0:03 for the baselines, so the total budget is not matched either. **This means the claimed solution-quality advantages in Table 1 cannot be attributed to algorithmic superiority without further controls.** The core contributions of the paper do not depend on this comparison, but it is the primary evidence for the neural-CO benchmarking claim and needs to be fixed (either single-trajectory reporting or matched-budget comparison).

2. **No discussion of training cost.** The paper reports inference-time TTS and wall-clock benchmarks but says nothing about the computational cost of training. Zeroth-order evolutionary methods require many function evaluations across many epochs, which can be substantial. For a practitioner weighing whether to adopt this approach, knowing whether the upfront training cost is justified by the inference-time gains is essential. This is standard in Learning to Optimize papers and its absence makes the practical claims feel incomplete.

3. **Planar-instance failure is under-discussed.** The paper acknowledges that dNPIM fails badly on the `N=800, P, +` planar unweighted instances (TTS 4.42e07 vs 1.81e06 for CAC), but frames this as a minor exception. Planar graphs are a structurally distinct and well-studied class; the failure suggests a systematic limitation rather than a random outlier. The paper would benefit from analyzing *why* dNPIM fails on these instances — is it a training-distribution issue, an architectural limitation, or something deeper? Without this, the claim of "almost all problem instances" feels like it papers over a meaningful gap.

### Minor

4. **Table 1 speed comparison is confounded by implementation.** The paper notes that the speed difference on large instances "could have something to do with the sparse graph library used for the results in Sanokowski et al. (2025) as opposed to the dense PyTorch matrix-matrix product used in our implementation." This is an honest caveat, but it means we cannot evaluate whether dNPIM is actually slower or just less optimized. Using a sparse implementation for dNPIM would clarify this.

5. **The "first application of algorithm unrolling to NP-hard CO" claim is slightly overscoped.** The paper acknowledges that Chen et al. (2024) applied algorithm unrolling to integer linear programming (ILP). Since ILP is NP-hard, the novelty is more precisely "first application to *quadratic unconstrained* NP-hard problems" or "first application to Max-Cut/Ising." This is a minor nuance but should be corrected.

### Trivial

None that survive filtering.

## Nice-to-Haves

- **Single-trajectory results for Table 1.** Reporting the median/mean of dNPIM over individual trajectories (not top-30) would separate the quality of the learned dynamics from the combinatorial benefit of multiple trials. This would be the cleanest way to address Weakness #1.
- **Analysis of the planar-instance failure.** Even a brief investigation using the paper's existing toolkit (e.g., comparing weight patterns, overfitting tendencies, or coupling-field statistics between planar and non-planar instances) would significantly strengthen the paper.
- **Training cost reporting.** Reporting total wall-clock time, number of epochs, and number of function evaluations required for training would allow practitioners to assess the method's overall value.

## Removed Points

- *"The Ising-machine SOTA claim is overstated because the paper compares TTS of the trained solver against TTS of hand-tuned baselines but the cost of training dNPIM is enormous."* — **Removed** because the training cost not being discussed is a genuine weakness (retained as Major #2), but the claim that the cost is "enormous" is speculative; the paper does not report training cost, so we cannot assert it is enormous. The framing of "overstated" based on an unquantified cost is too strong without evidence.
- *"The paper should characterize its method as a complementary approach rather than a general improvement."* — **Removed** as a framing suggestion rather than a concrete weakness; the paper already acknowledges the planar failure case.
- *Various formatting/style nitpicks and requests for larger training sets* — **Removed** per filtering rules.
- *Missing related works* — **Removed** per hard rules (cannot verify existence of missing references).
- *"Cannot be independently verified" type reproducibility concerns* — **Removed** per hard rules.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface any unexpected synthesis or cross-cutting pattern that the paper itself does not already articulate.

## Suggestions

1. **For Table 1**: Provide a budget-matched comparison. Either report dNPIM's single-trajectory performance alongside the "top 30" results, or run all methods for the same total compute budget and compare the best solution found within that budget. If single-trajectory dNPIM is competitive, that is a more honest and compelling result.
2. **For the planar-instance failure**: Investigate what distinguishes these instances and why dNPIM struggles. Even a simple diagnostic (e.g., does the trained network's coupling-field distribution differ on planar vs. non-planar instances?) would add value.
3. **Report training cost**: Add a table or paragraph documenting the computational resources, wall-clock time, and number of function evaluations required for training (and fine-tuning) for each benchmark.
4. **Calibrate the "first application" claim**: Qualify that algorithm unrolling has been applied to ILP (Chen et al., 2024) and that the present work focuses on quadratic unconstrained NP-hard problems.

## Score and Decision

**Bracketing (Round 1):** The most topically similar anchors span weak (scores 1.67–3.00 for incremental or flawed CO papers), middle (4.25–6.75 for solid CO papers with some issues), and strong (8.00–9.00 for exceptional papers). The initial bracket is **5.0–6.5**.

**Narrowing (Round 2):** Within this bracket, the closest topical anchors are:
- *ROS* (5.67, Reject) — GNN-based Max-k-Cut; NPIM has stronger novelty and analysis → NPIM is better.
- *Non-Equilibrium Dynamics* (6.00, Accept) — hybrid Ising solver; all 5 reviewers gave 6. Comparable quality: NPIM has more novel methodology but more notable evaluation weaknesses.
- *DISCO* (5.75, Reject) — diffusion solver for CO; similar quality tier but NPIM has clearer novelty.
- *QRF-GNN* (4.25, Reject) — incremental GNN for QUBO; NPIM is clearly stronger.
- *PQQA* (6.75, Accept) — sampling-based CO solver; stronger empirical evaluation than NPIM.
- *Unified Neural Solvers* (6.25, Accept) — framework paper; NPIM has more specific, cleaner contribution.

NPIM sits comfortably above the 4–5 range but has meaningful evaluation weaknesses that prevent it from reaching the 6.5+ tier. The strongest comparable anchor is the Non-Equilibrium Dynamics paper (6.00, Accept), which NPIM matches in overall quality but with a different profile: stronger novelty/analysis but weaker evaluation.

**Final Score: 6.0** — The paper makes a genuinely novel contribution to neural CO by introducing algorithm unrolling for Ising-machine dynamics, supported by insightful analysis of the learned behavior. The Ising-machine benchmarks (Table 2) are compelling. However, the neural-CO comparison (Table 1) has a significant protocol issue that needs correction, and the missing training-cost discussion and planar-instance gap are notable omissions. The paper merits acceptance with mandatory revisions to address the evaluation concerns.

**MY FINAL SCORE:** <score>6.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>