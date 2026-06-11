## Summary

DIPOLE proposes a new RL algorithm for diffusion policy optimization. Starting from a KL-regularized RL objective, the paper introduces a greedified regularization scheme whose closed-form solution naturally decomposes into two "dichotomous" policies (π⁺ for reward maximization, π⁻ for reward minimization) weighted by bounded sigmoid functions instead of the unstable exponential weight used in prior work. At inference, the two policies are combined via a linear score combination structurally identical to classifier-free guidance, enabling adjustable greediness via hyperparameter ω. Experiments span 39 RL tasks on ExORL and OGBench (offline and offline-to-online) plus a 1B-parameter VLA model fine-tuned on the NAVSIM autonomous driving benchmark.

## Strengths

1. **Clean theoretical derivation replacing unstable exponential weighting with bounded sigmoid weights.** The paper identifies the optimality-stability trade-off of exp(βG) weighting (Eq. 4) and derives, via a greedified KL-regularized objective (Eq. 5), a closed-form solution (Eq. 6) that decomposes into sigmoid-weighted dichotomous policies (Eqs. 7-8). Because σ(βG) ∈ [0,1], the training losses in Eq. (9) avoid the explosion problem of Eq. (4). This is a concrete mathematical improvement over the prior weighted-regression line of work.

2. **The CFG-style score combination at inference is an insightful connection.** The paper shows (Eq. 10) that ∇_a log π^*(a|s) = (1+ω)∇_a log π^+(a|s) − ω∇_a log π^−(a|s), which is structurally identical to classifier-free guidance. This enables adjusting greediness at inference time by varying ω, a practical advantage that the exponential-weighting baseline (Eq. 4) does not offer.

3. **Strong empirical performance across diverse RL benchmarks with statistical rigor.** On ExORL (Table 1), DIPOLE achieves the highest score on 7 of 9 tasks with non-overlapping standard deviations on most (e.g., Walker-stand 953±4 vs. next-best IFQL 873±6). On OGBench (Table 2), DIPOLE achieves best or near-best on 4 of 6 categories. The offline-to-online results (Table 3) show strong fine-tuning gains. All results are averaged over 8 seeds with standard deviations reported.

4. **Demonstrated scaling to a 1B-parameter VLA model for autonomous driving.** The NAVSIM experiment shows DIPOLE fine-tuning improves a strong imitation-learning VLA baseline from 88.3 to 89.7 PDMS on the navtrain split (standard protocol), with further gains on the navtest split (94.8) where fair comparison against DPPO navtest (89.0) shows a 5.8-point advantage. This demonstrates the method's scalability to billion-parameter models.

## Weaknesses

### Fatal

None.

### Major

1. **The navtest result (94.8 PDMS) compares across different training protocols without adequate caveat.** The paper presents a variant trained on the NAVSIM test split (justified as a "human take-over" scenario) and reports a 6.5-point gain over the DP-VLA baseline (88.3) that was trained on the standard train split. The baselines in the same table (UniAD, PARA-Drive, Transfuser, Hydra-MDP) follow the standard train/test protocol, so comparing DIPOLE navtest against them is not apples-to-apples. The more interpretable controlled comparison is the navtrain variant (89.7, +1.4 PDMS). The paper does explain the variant's rationale, but the main text ("substantial 6.5-point PDMS improvement") does not adequately flag the protocol difference when presenting this as the headline result. Mitigating factor: The DPPO navtest row (89.0) provides a fair within-protocol comparison that still shows DIPOLE's advantage on the test split (94.8 vs. 89.0).

2. **Missing ablation: single diffusion model with sigmoid-only weighting.** The core claim is that the dichotomous decomposition avoids the instability of exp-weighting. The most direct test would be training *one* diffusion model with σ(βG) weighting (π⁺ only, no π⁻, no CFG combination) and comparing directly to the full two-model DIPOLE. Without this, it is unclear whether the improvement comes from the bounded sigmoid weighting itself or from the two-model + CFG combination. CFGRL is a related baseline but differs on two dimensions at once (hard threshold vs. sigmoid, and π⁻=μ vs. learned), so improved performance over CFGRL does not substitute for this ablation.

### Minor

3. **"Perfect controllability" is overstated.** The abstract claims "perfect controllability over the greediness of action generation." The evidence is that ω can be varied at inference time, which provides flexible control but falls short of "perfect" — there is no formal analysis of monotonicity, achievable range, or Pareto frontier coverage. The claim should be calibrated to "flexible controllability."

4. **Table 1 caption overclaims "DIPOLE achieves the best performance."** While DIPOLE is best on 7 of 9 ExORL tasks, it substantially underperforms IFQL and FQL on both Jaco tasks (e.g., Jaco reach-top-right: DIPOLE 117 vs. FQL 224). The caption should acknowledge these exceptions.

5. **Computational cost of training two diffusion models is not discussed.** Training separate ϵ⁺ and ϵ⁻ models doubles the parameter count and training compute relative to single-model methods (IFQL, FQL). The VLA experiment mitigates this via LoRA modules, but the RL benchmarks train two full models. The paper frames the method as "simple and scalable" without acknowledging this trade-off.

6. **Limited analysis of the ω hyperparameter.** The paper introduces ω as a "greediness factor" but provides no sensitivity analysis showing how varying ω affects performance or whether the effect is monotonic. This would strengthen the controllability claim.

### Trivial

None.

## Nice-to-Haves

- Add the single-model ablation (π⁺ only with σ(βG) weighting) to isolate whether the two-model CFG combination is necessary.
- Provide an ω sensitivity plot on at least one or two tasks.
- Report training time / parameter count comparison against single-model baselines.

## Removed Points

The following criticisms from the input were removed with justification:

- **Critic training details missing from main text:** The paper references Appendix D for implementation details. Since the appendix is stripped by the parser, penalizing its absence is not appropriate per policy.
- **Section 3.1 "adoption" claim weakly supported:** This is a subjective observation about the literature, not a substantive weakness that threatens the paper's claims.
- **Clarity on DPPO navtest training split:** The table clearly labels "DP-VLA w/ DPPO navtest," consistently using the "navtest" notation to indicate the data split. This is already clear.
- **Statistical significance / rejection sampling questions:** The paper reports 8 seeds with standard deviations and explicitly distinguishes the "w/o rs" variant. These are adequately addressed.
- **Missing related works:** Per policy, I cannot penalize missing citations.

## Novel Insights

None beyond the paper's own contributions. The CFG-to-RL connection is the paper's own insight, not something derived from the reviews.

## Suggestions

1. Add the single-model (π⁺ only with σ(βG) weighting) ablation.
2. Recalibrate claims: change "perfect controllability" to "flexible controllability"; qualify the Table 1 caption with "generally achieves the best performance" and note Jaco exceptions.
3. Present the NAVSIM navtrain result as the primary controlled comparison, and flag the navtest result as an exploratory variant with explicit caveat in the main text.
4. Add an ω sensitivity plot.
5. Discuss computational cost trade-offs (two models vs. one model) in the main text.

## Score and Decision

### Calibration Process

**Round 1 — Bracketing:** Searched across weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands using queries about diffusion policy RL with weighted regression. Low-end anchors (BDQL 3.67, Offline-to-Online CFDG 3.00, Latent Diffusion Planning 3.40) were clearly weaker — incremental contributions, narrower evaluation, or flawed methodology. High-end anchors (8.0, mostly in different domains) had no notable weaknesses. Initial bracket: **5.5–7.5**.

**Round 2 — Narrowing:** Retrieved additional anchors in the (5.5, 7.5) range:

| Paper | Score | Decision | Comparison |
|-------|-------|----------|------------|
| SRPO (xCRr9DrolJ) | 6.25 | Accept | **Weaker**: narrower evaluation (D4RL only), contribution more incremental, mixed reviews |
| DAC (ldVkAO09Km) | 6.50 | Accept | **Comparable**: similar theoretical depth, broader validation needed; both have issues |
| EFM (HA0oLUvuGI) | 6.25 | Accept | **Weaker**: core idea (Q-weighted loss) not new; some reviewers questioned novelty |
| Reasoning with Latent Diffusion (tGQirjzddO) | 6.33 | Accept | **Slightly weaker**: overclaiming concerns, missing evaluations on several tasks |
| DMBP (ZULjcYLWKe) | 7.00 | Accept | **Different contribution**: narrower (robustness module) but cleaner evaluation |

DIPOLE's theoretical contribution (dichotomous decomposition with the CFG connection) is cleaner and more novel than SRPO, EFM, and the latent diffusion paper. Its evaluation breadth (39 RL tasks + VLA scaling) exceeds all anchors. However, the NAVSIM test-split presentation issue and the missing ablation prevent it from reaching the 7.0+ level.

**Final assessment:** DIPOLE is comfortably stronger than papers at 6.25 and comparable to DAC at 6.50. Given its cleaner theory but notable presentation issues, the score is set at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>