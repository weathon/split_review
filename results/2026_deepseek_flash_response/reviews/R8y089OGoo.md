Now let me write the final review.

## Summary
This paper proposes DIPOLE, an RL algorithm for diffusion policies that replaces the unstable exponential weighting in standard KL-regularized RL with a greedified objective that decomposes into two bounded sigmoid-weighted dichotomous policies. The positive policy maximizes reward, the negative minimizes it, and inference combines their scores via a CFG-style linear combination (1+ω)ε⁺ − ωε⁻. The method is evaluated on 39 RL tasks across ExORL and OGBench (offline and offline-to-online) and on a 1B-parameter VLA driving model on the NAVSIM benchmark.

## Strengths

1. **Principled theoretical derivation resolving the exp-weighting instability.** The paper identifies that the unbounded `exp(βG)` term in standard KL-regularized RL (Eq. 3) causes an optimality-stability tradeoff. By proposing a greedified KL objective (Eq. 5) and solving for the optimal policy (Theorem 1, Eq. 6), the derivation shows the exponential term decomposes into sigmoid-weighted positive and negative policies via the identity `σ(x)/(1−σ(x)) = exp(x)` (Eqs. 7–8). Both policies use strictly bounded weights in [0,1], directly addressing the exploding-loss problem.

2. **Novel theoretical connection to classifier-free guidance (CFG).** The derivation yields `∇log π* = (1+ω)∇log π⁺ − ω∇log π⁻` (Eq. 10), which is formally identical to CFG. This provides principled theoretical backing that prior heuristic approaches (e.g., CFGRL's indicator-based weighting) lack. The hyperparameter ω offers controllable greediness during inference.

3. **Strong empirical results on ExORL with 8 seeds.** DIPOLE outperforms all baselines on 7/9 ExORL tasks, often by substantial margins (e.g., Walker stand 953±4 vs. next-best IFQL 873±6; Cheetah run-backward 350±15 vs. IFQL 310±24). The variant without rejection sampling still outperforms CFGRL on most tasks, showing the benefit comes from the algorithmic design rather than inference-time tricks.

4. **Scalability demonstrated on a 1B-parameter VLA driving model.** DIPOLE fine-tuning of the DP-VLA model on NAVSIM achieves a PDMS of 94.8 (navtest), the highest score in the table. Even on the standard navtrain split, the improvement (88.3→89.7) is positive and consistent across safety and progress metrics.

## Weaknesses

### Major

1. **AD navtest result trains on the evaluation split, making the headline +6.5 PDMS gain uninterpretable as evidence of general capability.** The paper trains a variant on the navtest split (line 211: "we provide a variant of our model trained on the test split") and reports 94.8 PDMS vs. the imitation baseline 88.3. While the paper discloses this, the navtest result is presented prominently ("demonstrating its potential for real-world autonomous driving applications") alongside the navtrain result. The proper evaluation on navtrain yields a more modest +1.4 PDMS (88.3→89.7). The large gap between +1.4 and +6.5 strongly suggests most of the observed gain on navtest is attributable to training on the evaluation distribution rather than to the RL algorithm itself. **This does not invalidate the core RL benchmark results**, but it means the AD experiment cannot be taken as clean evidence for DIPOLE's effectiveness — it should be treated as exploratory.

2. **No direct comparison against the exp-weighted regression baseline (Eq. 4) that motivates the method.** The paper's core motivation (Section 3.1) is that exp-weighted regression suffers from instability and inefficient learning. Yet DIPOLE is never compared against a method that simply uses Eq. (4) with a properly tuned temperature β and a clipping mechanism — the most direct ablation. The baselines used (IQL, ReBRAC, CFGRL, IFQL, FQL) differ from DIPOLE in multiple ways beyond the weighting scheme. Without isolating the effect of switching from exp-weighting to the dichotomous decomposition, it is impossible to attribute DIPOLE's gains specifically to the proposed mechanism rather than to sigmoid weighting alone, multi-model effects, or better hyperparameter tuning. This is a gap in the evidence supporting the paper's central claim.

### Minor

1. **Computational cost of training two diffusion models is not discussed.** DIPOLE trains two separate diffusion models (ε⁺ and ε⁻) per Eq. (9), doubling training cost relative to single-model methods like FQL or IFQL. LoRA modules mitigate this in the AD experiments, but the RL benchmarks appear to train two full models. The paper does not acknowledge this tradeoff or compare against baselines with a comparable compute budget (e.g., an ensemble of two models).

2. **Missing exp-weighted regression ablation study.** Beyond point 2 above: a controlled experiment on a simple task (e.g., one ExORL domain) comparing (a) exp-weighted regression (Eq. 4), (b) single-model sigmoid-weighted regression without dichotomous decomposition, and (c) full DIPOLE would directly test the paper's motivating claims. Its absence weakens the claimed causal link between the dichotomous decomposition and observed improvements.

3. **No sensitivity analysis for ω and β in the main text.** The greediness factor ω and temperature β are central hyperparameters, but the paper does not show how performance varies with them or provide guidelines for setting them (presumably deferred to the missing appendix). Including a brief sensitivity summary in the main text would strengthen the paper.

4. **FQL hyperparameter selection asymmetry.** The paper states FQL's α was selected "with optimal performance in ExORL" (line 169), implying task-specific tuning. It is unclear whether DIPOLE's hyperparameters were tuned per-domain or held fixed, which could affect the comparison.

### Trivial

- None beyond the formatting artifacts introduced by the PDF extraction process.

## Nice-to-Haves
- Qualitative analysis of what the negative policy actually learns (e.g., visualizing action distributions of π⁺ and π⁻ on a simple task).
- Analysis of robustness to critic/advantage estimation quality, since DIPOLE relies on advantage estimates for weighting.
- Comparison against an ensemble-of-two diffusion models with rejection sampling to isolate the benefit of the dichotomous design vs. simply having two models.

## Removed Points
These points were identified in the raw reviews but removed after cross-checking against the paper:
- **"Greedified objective is a design choice, not a derivation"**: The paper is transparent that Eq. (5) is a novel greedified objective; it does not claim it is the only KL formulation.
- **"Under-specified critic role"**: The paper states advantage estimation is used and refers to the appendix for details — standard practice.
- **"Overstated claim about completely resolving the issue"**: The claim refers to the specific technical problem of loss being dominated by high-return samples in exp-weighted regression; sigmoid weighting indeed bounds weights to [0,1] vs. unbounded exp, so this is technically correct.
- **Missing related works**: Hard rule — cannot confirm existence of unlisted works.
- **Formatting/style nitpicks and typos**: Parser artifacts, not author issues.
- **Reproducibility concerns about missing appendix content**: The appendix exists in the original submission; the parser strips it.

## Novel Insights
The harsh critic correctly identifies the central tension in the paper: the cleanest empirical story (RL benchmarks) shows solid but not transformative gains, while the most eye-catching result (AD at 94.8 PDMS) uses a non-standard evaluation protocol. The strength finder's emphasis on the theoretical derivation is well-placed — the sigmoid-to-exponential identity decomposition connecting KL-regularized RL to CFG is the paper's most original intellectual contribution, and it is stronger than the empirical evidence supporting it. The missing exp-weighted regression baseline is the most actionable finding across both reviews: it is the single experiment that would most directly validate or refute the paper's causal narrative.

## Suggestions
1. **Add the missing exp-weighted regression baseline** — on at least one ExORL domain, compare against a method using Eq. (4) with tuned β and optional clipping. This directly tests whether the dichotomous decomposition is responsible for the gains.
2. **Restructure the AD presentation** — treat the navtrain result as primary and clearly separate the navtest result as an exploratory/application variant with an explicit methodological caveat.
3. **Include a brief sensitivity analysis** for ω and β in the main text (even if only on one domain), and clarify whether DIPOLE's hyperparameters were tuned per-domain or globally.

## Score and Decision
Based on comparative calibration against accepted papers in the diffusion RL space (DAC 6.50, SRPO 6.25, EFM 6.25, LDCQ 6.33), DIPOLE is stronger due to its cleaner theoretical contribution, more extensive evaluation (39 tasks vs. typical D4RL benchmarks), and large-scale AD deployment. However, two non-trivial weaknesses (test-split AD training, missing exp-weighted baseline) prevent it from reaching the 8+ tier. It is clearly above the 6.25–6.5 cluster and below the strongest papers at 7.5–8.

**Round 1 bracket**: 5.5–7.5 (based on comparison to SRPO at 6.25 and What Makes a Good Diffusion Planner at 7.50)

**Round 2 anchors**:
- DAC (6.50, /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ldVkAO09Km.md): Similar domain (diffusion + offline RL with KL constraints). DIPOLE has more novel theoretical contribution and more extensive experiments → DIPOLE is stronger.
- EFM/QIPO (6.25, /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HA0oLUvuGI.md): Weighted diffusion loss approach; reviewers raised novelty concerns. DIPOLE is clearly stronger.
- SRPO (6.25, /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/xCRr9DrolJ.md): Mixed reviews on novelty. DIPOLE is stronger.
- LDCQ (6.33, /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tGQirjzddO.md): Latent diffusion + BCQ. DIPOLE has broader experiments and cleaner theory → comparable or slightly stronger.

**Final calibration**: DIPOLE sits above the 6.25–6.5 cluster but below a clean 7.5+ paper, due to the two major weaknesses that reduce confidence in the empirical narrative.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>