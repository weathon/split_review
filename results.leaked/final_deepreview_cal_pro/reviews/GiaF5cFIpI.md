Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes a real-time adaptive framework for designing high-dimensional neural stimulations that drive latent population dynamics in desired directions. The pipeline integrates three components: (1) streaming construction of latent spaces (including a novel sjPCA method), (2) a nonparametric kernel regression model that learns the state-dependent mapping from stimuli to latent-space perturbations, and (3) a constrained optimization procedure that selects stimulation patterns to align observed effects with a target latent direction. The method is evaluated on synthetic data and on two real neural datasets (calcium imaging, electrophysiology) with simulated stimulations.

## Strengths

- **Integrated pipeline for a novel problem.** The paper is the first to combine streaming latent tracking, nonparametric stimulus-response learning, and constrained optimization into a single real-time framework for driving latent neural dynamics. This addresses a genuine gap: prior work addresses pieces of this problem but no existing method ties them together for adaptive closed-loop stimulation design.

- **Adaptive kernel regression convincingly handles non-stationary stimulus-response mappings.** The nonparametric \(\hat{S}\) estimator (Equation 7) uses temporal kernel weighting to adapt to both sudden flips (recovering within 15s) and continuous rotation of the stimulus-response mapping, substantially outperforming a stimulation-blind baseline (Figure 2e). This demonstrates the core modeling advantage of the approach.

- **Stimulation optimization produces well-aligned perturbations under simple mappings.** On the toy model, the designed stimuli achieve far better alignment with target latent directions than random single-neuron, random group, or shuffled controls (Figure 4a). For feasible targets, 517/600 optimizations achieve misalignment under 1° (Figure 4b), establishing that the differentiable optimization over the kernel regressor works as intended when the stimulus-response mapping is identity or known.

- **Real data modeling component validated.** On calcium imaging data with simulated stimulations and response delays, the learned \(\hat{S}\) model reduces 1-step-ahead prediction error compared to a blind model (Figure 3c), confirming that the stimulus-response learning component transfers to real neural recordings.

- **Novel streaming sjPCA method converges to offline solution.** The streaming jPCA formulation with Orthogonal Procrustes stabilization (Equation 2) matches the offline jPCA subspace within seconds on simulated data (Figure 1a), providing a useful new tool for real-time rotational dynamics analysis.

- **Real-time feasible.** All components run end-to-end in under 100ms, with average latency below 10ms per timestep, making the approach compatible with live experimental use.

## Weaknesses

### Fatal

None.

### Major

- **The sparsity penalty in Equation (8) is incorrectly formulated.** The objective minimizes \(\lambda_1(\|u\|_0^{\max} - \|u\|_1)\) with \(u \in [0,1]\). Since \(\|u\|_0^{\max}\) is a constant (the target number of active neurons), minimizing \(-\lambda_1\|u\|_1\) *rewards* large \(\|u\|_1\) values, encouraging dense rather than sparse solutions — the opposite of what the paper claims. The correct formulation for encouraging \(\|u\|_1 \approx n\) would use an absolute value or squared deviation. This error means the paper's claim of enforcing sparse stimulation constraints is not supported by the mathematics as written. The optimization results (Figure 4) may still be valid due to the cosine-similarity term dominating, but the sparsity enforcement is compromised.

- **No comparison with existing adaptive stimulation methods.** The paper cites Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), and Bayesian variational inference (Draelos & Pearson, 2020) for stimulation design, yet the experiments compare only against random baselines and a stimulation-blind model. Without comparisons to methods that also adaptively select stimulations, the evidence for the method's advantage remains a sanity check rather than a demonstration of progress over the state of the art.

- **The full stimulation-optimization loop is tested only on the toy model, not on real data.** The real-data experiments (Figure 3) validate only the stimulus-response modeling component (learning \(\hat{S}\)), not the closed-loop optimization of Equation (8). The headline claim that the method can design stimulations to drive latent dynamics under realistic experimental constraints is therefore supported only by synthetic experiments. The paper acknowledges this limitation in the Discussion but the gap between the claim and the evidence remains substantial.

### Minor

- **The "non-simple" stimulus-response mapping used for closed-loop experiments in Figure 5 is never specified.** The reader cannot assess how challenging the test case is or what structure the kernel regression must learn. The statement that learning rates are similar for simple and non-simple mappings is uninterpretable without knowing what the non-simple mapping entails.

- **The stimulation optimization procedure is underspecified.** No solver, initialization strategy, step-size regime, or handling of box constraints is provided. The gradient derivation for the differentiable kernel regressor is not shown. This hinders reproducibility and makes it difficult to assess whether the optimization reliably finds good solutions or requires careful tuning.

- **The parallel latent-space evaluation (Figure 1c) is disconnected from the main stimulation narrative.** The ability to compare latent spaces and select the most predictive one is intriguing, but it plays no role in the subsequent stimulation experiments. The paper would be stronger if this capability were either integrated into the closed-loop story or de-emphasized.

- **The streaming sjPCA construction is described only at a high level.** The Sherman-Morrison update for the streaming least-squares solution is mentioned but not derived. How the time derivative \(\dot{X}\) is computed online and how many samples are buffered are not specified, limiting independent re-implementation of this component.

### Trivial

- The response delay \(d\) is mentioned as a parameter but its impact on \(\hat{S}\) accuracy and stimulation design is not systematically assessed, only illustrated with a single example (Figure 3).

## Nice-to-Haves

- Testing the closed-loop stimulation pipeline on real data with a more realistic stimulation forward model (e.g., incorporating spatial point-spread functions, variable opsin expression) would substantially strengthen the evidence that the method can work under experimental conditions.

- An ablation showing how the sparsity penalty (once corrected) affects the number of active neurons in optimized stimuli would validate the constraint enforcement claim.

- Reporting the distribution of per-neuron intensities and how often the optimized stimuli respect the intended cardinality limit would support claims of experimental feasibility.

- Integrating the parallel latent-space comparison into the stimulation story — e.g., demonstrating that switching latent spaces leads to better stimulation outcomes — would unify the paper's narrative.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"The evaluation does not actually test the method's core claim on real data with realistic stimulation physics."** — This duplicates the Major weakness about toy-model-only optimization but overstates it. The paper *does* test the stimulus-response modeling component on real data, just not the full optimization loop. The core claim has two parts (modeling and optimization), and the real-data evidence for modeling is legitimate. Kept the concern about optimization at Major but removed the blanket statement.

- **"Missing appendix / proofs in appendix"** — The parser strips appendices from all papers. This is an artifact of the review system, not an author error. Removed.

- **Requesting confidence intervals for large-scale benchmarks** — The paper reports standard deviations in most cases (e.g., "2.21 ± 0.9" for simple mapping). Removed.

- **"Streaming jPCA and kernel-regression update mechanics are missing details that would be needed for independent re-implementation"** — Kept as Minor but downgraded from the harsh critic's framing as a critical gap. The core ideas are clear; the missing implementation details are standard for a conference paper and can be supplied in code.

- **"The paper does not discuss or measure the effect of the response delay d on the accuracy of Ŝ"** — Moved to Trivial. The paper does illustrate one delay case, and a full systematic study is beyond reasonable scope for a methods paper.

## Novel Insights

The paper's most novel insight is that a differentiable nonparametric kernel regressor can serve as both the learned stimulus-response model and the surrogate for gradient-based stimulation optimization, enabling the optimization to adapt to idiosyncratic, non-stationary mappings without assuming a parametric form. The integration of streaming latent tracking with this adaptive modeling-and-optimization loop creates a genuinely new capability: the ability to design high-dimensional stimuli for low-dimensional latent targets in real time, even as the stimulus-response relationship drifts. The demonstration that temporal kernel weighting alone is sufficient to recover from both sudden flips and continuous rotation of the mapping (Figure 2d-e) is a clean, convincing empirical finding that supports the design philosophy.

## Suggestions

- **Fix the sparsity penalty.** Replace \(\lambda_1(\|u\|_0^{\max} - \|u\|_1)\) with a proper sparsity-inducing term such as \(\lambda_1\|u\|_1\) (for u ≥ 0, minimizing L1 encourages sparsity) or \(\lambda_1|\|u\|_1 - n|\) if the goal is to hit exactly n active neurons. Show the effect on the number of active neurons in optimized stimuli.

- **Add at least one comparison against an adaptive method.** Bayesian optimization over the latent space with a Gaussian process surrogate is a natural baseline and would contextualize the benefits of the proposed differentiable kernel-regression approach.

- **Run the full optimization pipeline on the real data recordings** (even with simulated stimulations), not just the Ŝ modeling component. This would close the gap between the toy-model optimization results and the paper's headline claim.

- **Describe the non-simple mapping used in Figure 5** so readers can assess the difficulty of the closed-loop test.

- **Specify the optimization solver and gradient computation** used for Equation (8), or reference the appendix section where these details appear.

## Score and Decision

### Anchor comparison summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BBldjKEBlJ (QuantFormer) | 3.00 | R1-low | Not comparable; our paper is substantially stronger in novelty and evaluation. |
| FwW3jqchtY (iSSM) | 5.00 | R1-mid, R2 | Closest topical match. Both address causal perturbation of neural dynamics. iSSM has theory (identifiability proofs); our paper has a more complete pipeline and addresses a more actionable problem (stimulation design vs. modeling). Our paper is somewhat stronger but shares similar evaluation gaps. |
| LNp7KW33Cg (HDA) | 5.00 | R1-mid, R2 | Domain adaptation for BCIs. Less relevant. Our paper has stronger novelty. |
| wCUw8t63vH (Spectral learning) | 6.80 | R1-mid | More rigorous methodologically with strong theory. Our paper is weaker on theoretical grounding but addresses a more directly impactful applied problem. |
| cNmu0hZ4CL (Optimal transport) | 8.00 | R1-high | Significantly stronger paper — polished, rigorous, well-validated. Our paper does not reach this tier. |
| WQwV7Y8qwa (MR-SDS) | 5.80 | R2 | Similar scope ambition. MR-SDS has more comprehensive real-data application but also significant presentation issues. Our paper has a cleaner, more focused contribution but weaker empirical validation. Comparable quality overall, slightly below. |
| 3usdM1AuI3 (BRAID) | 6.25 | R2 | Stronger empirical validation, more comprehensive baselines. Our paper's evaluation gaps are more significant. |

**Round 1 bracket:** 5.0–7.0 (between iSSM at 5.0 and the spectral learning paper at 6.80).

**Round 2 narrowing:** The closest anchors are iSSM (5.0), MR-SDS (5.80), and BRAID (6.25). Our paper sits between iSSM and MR-SDS: it has a more novel integrated pipeline than iSSM but weaker empirical validation than MR-SDS, and clearly below BRAID. The three Major weaknesses — the sparsity penalty error, missing comparisons, and toy-model-only optimization — prevent it from reaching the 6.0+ tier. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>