Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket:** Between 6.0 and 7.5. The weak anchors (3.0) are simple data augmentation papers with limited novelty, clearly below DIPOLE. The strong anchors (8.0) are theory-deep papers (confounded POMDPs with convergence proofs) that DIPOLE doesn't match in theoretical depth.

**Round 2 narrowing:** 
- DAC (score 6.50): Diffusion actor-critic with KL-constrained policy iteration. DIPOLE has more elegant theoretical contribution (dichotomous decomposition + CFG connection), much more comprehensive evaluation (39 tasks vs D4RL), and better presentation.
- SRPO (score 6.25): Score-regularized policy optimization. DIPOLE has stronger theory and evaluation.
- CTRL (score 6.50): RL-based conditional control for diffusion. DIPOLE is more comprehensive.
- DIPOLE is clearly above all these anchors in both theoretical contribution and evaluation breadth, but has notable weaknesses (Jaco gap, rejection sampling confounding).

DIPOLE sits around 7.0 — above the 6.25-6.50 diffusion RL papers but with weaknesses that keep it below 7.5+.

## Summary

This paper proposes DIPOLE, an RL algorithm for diffusion policy optimization that reformulates the KL-regularized objective so the optimal policy decomposes into two bounded "dichotomous policies" — one maximizing and one minimizing reward — both weighted by sigmoid functions instead of unstable exponential weights. At inference, the combined score function resembles classifier-free guidance, enabling controllable greediness via a single hyperparameter. Evaluations span 39 offline/offline-to-online RL tasks on ExORL/OGBench plus a 1B-parameter VLA for autonomous driving on NAVSIM.

## Strengths

- **Elegant theoretical decomposition (Eq. 7–8, Theorem 1):** The paper shows that exp(βG) can be decomposed into two bounded sigmoid-weighted policies π⁺ and π⁻, directly addressing the training instability of exponential weighting while preserving optimality. The derivation is mathematically correct and insightful.

- **Principled RL-theoretic connection to classifier-free guidance (Eq. 10):** The optimal policy's score function satisfies ∇_a log π* = (1+ω)∇_a log π⁺ − ω∇_a log π⁻, providing the first principled RL grounding for CFG-style guidance in decision-making. This also positions CFGRL as a less flexible special case.

- **Comprehensive evaluation across diverse settings:** Tables 1–2 show strong results on 39 tasks (best on 7/9 ExORL tasks, best or near-best on 6/6 OGBench categories). Table 3 shows competitive offline-to-online transfer. Table 4 demonstrates scalability to a 1B-parameter VLA with a 6.5-point PDMS improvement on NAVSIM.

- **Better data utilization:** Both high- and low-return samples are weighted meaningfully — π⁺ with σ(βG) and π⁻ with 1−σ(βG) — resolving the dominance of high-return samples in exponential weighting.

- **Controllable greediness via single hyperparameter ω:** Provides an inference-time knob analogous to CFG guidance scale without retraining.

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged underperformance on Jaco manipulation tasks with misleading caption:** In Table 1, DIPOLE scores 117±18 and 110±12 on Jaco tasks, while FQL scores 224±17 and 222±42 — roughly double. IFQL also substantially outperforms (193±9 and 181±11). Despite this, the table caption states "DIPOLE achieves the best performance," which is factually incorrect for 2 of 9 tasks. The paper's text hedges with "most domains" but provides no analysis of why the method struggles on manipulation tasks while excelling on locomotion. This omission makes it difficult to assess the method's scope of applicability — if the bounded sigmoid weighting systematically underperforms on tasks with certain reward landscape characteristics, that is important information that should be analyzed.

- **Rejection sampling substantially confounds the training-method contribution:** Table 1 shows dramatic gaps between "DIPOLE w/o rs" and "DIPOLE" (with rejection sampling): Walker stand 793→953, Walker walk 679→910, Cheetah run-backward 227→350. These inference-time improvements are larger than DIPOLE's advantage over baselines in many cases. While IFQL also uses rejection sampling (making the system-level comparison fair), the paper does not analyze whether DIPOLE's dichotomous decomposition creates uniquely strong synergy with rejection sampling. Without ablations comparing all methods with and without rejection sampling, it is unclear how much of the improvement comes from the training algorithm versus the inference procedure.

### Minor

- **Greedified objective narrative reads as reverse-engineered:** Eq. (5) introduces a KL penalty toward a value-reweighted reference policy μ·σ(βG)/Z(s). The paper presents this as motivated by "greedier learning objective" with "similar spirit" to offline RL methods. However, placing σ(βG)/Z(s) inside the KL divergence is extremely particular and produces exactly the desired dichotomous decomposition. The paper's narrative presents this as a forward derivation from first principles, which is not fully convincing. A more transparent presentation acknowledging the objective was designed to yield the decomposition and arguing for it on the basis of its properties would be stronger.

- **Computational cost of training two diffusion models not discussed for benchmarks:** The paper addresses "computation efficiency" as a challenge but requires two full diffusion models for benchmark experiments. For VLA, LoRA modules mitigate this (Section 3.3), but for ExORL/OGBench, the doubled parameter count and training cost are not reported. Wall-clock training time and parameter counts vs. single-model baselines would be informative.

### Trivial
None.

## Nice-to-Haves
- A discussion of how the Q-function/advantage estimates are obtained and how sensitive DIPOLE is to their quality would strengthen reproducibility (deferred entirely to appendix).
- The NAVSIM navtest fine-tuning protocol (94.8 PDMS) uses test data without ground-truth, justified as simulating RL in take-over situations, but the lack of other methods evaluated under this protocol makes it hard to contextualize.
- CFGRL comparison on OGBench would strengthen the claims about theoretical superiority over CFGRL.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting/typos/nitpicks — parser artifacts, not paper problems.
- Generic "evaluation could be more rigorous" concerns without specific anchors.
- Missing related works claims — cannot verify external references exist.

## Novel Insights
The paper's genuinely novel insight is the connection between KL-regularized RL and classifier-free guidance via the dichotomous decomposition. By showing that the optimal policy's score function decomposes as a linear combination of two stably-trained bounded-weight policies (Eq. 10), the paper provides the first principled RL-theoretic grounding for CFG-style guidance in decision-making. This both explains why heuristic approaches like CFGRL work and reveals their limitations (indicator-based weighting vs. sigmoid weighting). The decomposition also provides a natural mechanism for utilizing both high- and low-return data, which is a practical bonus of the theoretical framework.

## Suggestions
1. Correct the Table 1 caption and add analysis of the Jaco underperformance (even a brief hypothesis about reward landscape characteristics).
2. Add an ablation on a representative subset comparing all methods with/without rejection sampling.
3. Report wall-clock training time and parameter counts for benchmark experiments.
4. Consider a more transparent narrative for Eq. (5) — acknowledge the objective was reverse-engineered from the desired decomposition and argue for it based on its desirable properties.

## Calibration Anchors

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | cXxfVkRCHJ | 3.00 | Simple CFG data augmentation for O2O RL — much weaker novelty and evaluation than DIPOLE |
| 1 | PiHGrTTnvb | 3.00 | Closed-loop diffusion control — different domain, limited scope |
| 1 | RFJGFrMvYj | 1.50 | Two-stage controlled image generation — unrelated domain, very weak |
| 1 | Fk4Op9wpEp | 3.00 | Pose-conditioned ControlNet with RL — limited scope and novelty |
| 1 | fcJKzwlwcs | 4.80 | Diffusion planner with pre-training — less rigorous theory, smaller evaluation |
| 1 | XLCqhdaMpy | 4.50 | Latent weight diffusion — different approach, limited evaluation |
| 1 | CKqiQosLKc | 3.75 | Energy-based policy sampling — different focus, limited results |
| 1 | svp1EBA6hA | 6.50 | RL for conditional control of diffusion — good RL framing but limited to image generation |
| 1 | uKZdlihDDn | 7.60 | Diffusion for fluid simulations — different domain, strong results |
| 1 | 8BAkNCqpGW | 8.00 | Policy gradient for confounded POMDPs — deeper theoretical contribution |
| 1 | fV0t65OBUu | 8.00 | Optimal covariance matching for diffusion — different domain |
| 1 | CxXGvKRDnL | 8.00 | Diffusion for compression — different domain |
| 2 | TeeyHEi25C | 6.25 | Value estimation with conditional diffusion for control — less comprehensive |
| 2 | tGQirjzddO | 6.33 | Latent diffusion for offline RL — different approach, less theory |
| 2 | ldVkAO09Km | 6.50 | Diffusion actor-critic (DAC) — similar topic but DIPOLE has better theory + evaluation |
| 2 | xCRr9DrolJ | 6.25 | Score regularized policy optimization — interesting insight but weaker evaluation |
| 2 | o2uHg0Skil | 6.25 | KL regularization failure modes — different focus (safety) |
| 2 | lF2aip4Scn | 6.50 | Demonstration-regularized RL — different theoretical focus |
| 2 | MOEqbKoozj | 6.25 | Simple policy optimization — different focus (TRPO/PPO variants) |
| 2 | OyyE1FDdrQ | 6.67 | q-exponential family for policy optimization — interesting but different scope |

**Round 1 bracket:** 6.0–7.5. DIPOLE is clearly above all weak anchors (3.0–4.8) and below the strongest anchors (8.0) which have deeper theoretical depth.

**Round 2 narrowing:** DIPOLE sits above the 6.25–6.50 diffusion RL papers (DAC, SRPO, CTRL) due to its more elegant theoretical decomposition, CFG connection, and far more comprehensive evaluation (39 tasks + NAVSIM vs. D4RL). The weaknesses (Jaco gap, rejection sampling confounding, derivation narrative) keep it from 7.5+.

**Final score: 7.0** — a solid paper with genuine theoretical insight and comprehensive evaluation, held back by unanalyzed failure modes and confounded ablations.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>