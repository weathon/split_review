Now I have all the information I need to cross-check the reviewer claims against the paper. Let me construct the consolidated review.

## Summary

This paper introduces a diffusion-model-based approach to potential-field motion planning. The authors train an energy-based model over trajectories (parameterized as a diffusion model) that serves as a learned "potential" landscape, then optimize by denoising from Gaussian noise. The paper demonstrates strong results on 2D, 7D, and 14D motion planning benchmarks and proposes compositional generalization by summing separately trained diffusion potentials at test time, enabling handling of more obstacles or combinations of constraints than seen during training.

## Strengths

- **Learned diffusion potential effectively avoids local minima that plague traditional potential-based methods.** On Maze2D environments with concave obstacles, the proposed method achieves 100% success while the classical potential-based planner RMP succeeds only 28% (Table 2). This directly addresses the long-standing local-minima problem and is a genuine empirical advance.

- **Strong performance in high-dimensional configuration spaces.** In the 14-DoF Dual KUKA environment, the method surpasses the state-of-the-art learned planner MπNet by ~35% in success rate while requiring less planning time and 7× fewer collision checks (Figure 3, Section 4.2). The method scales gracefully where sampling-based baselines degrade significantly.

- **Composition empirically enables out-of-distribution generalization.** The paper demonstrates that summing diffusion potentials at test time can handle more obstacles than seen during training (Figure 5, obstacle count generalization from 6→11), combine static and dynamic obstacle models (Table 3, 97.5% success vs. SIPP's 74%), and merge constraints from different training distributions (Table 3, Static 1+Dynamic). This is a practically useful capability.

- **The refinement scheme (Section 3.4) is simple and effective.** Boosting Dual KUKA success rates from ~47% to ~81% (Table 1) is a meaningful practical contribution.

## Weaknesses

### Fatal
None. The paper's empirical contributions are real and supported by evidence, even if some claims are overstretched.

### Major

- **The compositionality claim lacks theoretical grounding and a critical experimental baseline.** 
  The paper asserts (Section 3.3) that summing diffusion energy functions yields a composite whose minimum corresponds to trajectories satisfying both constraints. This is valid only if the constraints are independent given the trajectory (i.e., the joint score decomposes as a sum of conditional scores). The paper neither states this conditional-independence assumption, discusses when it holds or fails, nor provides a derivation. This is not just a theory gap: the lack of a jointly trained baseline (training one diffusion model on the full obstacle set) means we cannot tell whether composition actually outperforms simply training on more diverse data. Without this comparison, the central contribution of "generalization through composition" is incompletely supported.

- **No quantitative results for the composed real-world scenes.** 
  Section 4.4 evaluates on ETH/UCY with 10 pedestrians by composing two models each trained on 5 pedestrians, but reports only qualitative visualizations (Figure 11). No success rate, collision rate, or planning time is given for the composed case. This makes the real-world composition claim essentially anecdotal.

- **No ablation on the composition strategy.** 
  Algorithm 1 sums energy gradients uniformly. The paper does not explore whether different weighting schemes matter, especially when composing models trained on qualitatively different distributions (e.g., static vs. dynamic obstacles). Ablating this choice would strengthen the empirical support for composition.

### Minor

- **The probabilistic completeness proof (Section 3.5) is trivial and does not contribute.** 
  The proof assumes the learned density assigns positive mass to all trajectories and then argues that with infinite samples, a valid trajectory will be found almost surely. This holds for any model with full support (including a randomly initialized MLP), does not leverage any property of the diffusion process, and provides no practical sample-complexity guarantees. It should be removed or replaced with a meaningful analysis.

- **The diffusion baseline MPD (Carvalho 2023) is only compared in Table 2 (concave obstacles), not in the comprehensive evaluation of Figure 3.** Since MPD is a diffusion-based motion planner, including it in the main comparisons would strengthen the evaluation.

- **Compositional success degrades substantially in higher dimensions but this is not discussed.** 
  Figure 5 shows compositional success dropping from ~100% to ~90% in Maze2D (2D) but from ~72% to ~40% in KUKA (7D). The paper does not analyze why, or whether the conditional-independence assumption is more severely violated in higher-dimensional configuration spaces.

- **The classifier-free guidance scale (2.0) is given without motivation or ablation.** 
  Section 3.2 sets this value without discussion of how it was chosen or how sensitive results are to it.

- **The refinement scheme's noise scale \(k\) (Algorithm 2) is not analyzed.** 
  The paper does not study how \(k\) affects the trade-off between preserving trajectory morphology and successfully fixing collisions.

- **The limitations section (Section 5) is too brief.** 
  It mentions suboptimality and linear scaling of composition cost, but does not acknowledge the theoretical gap in composition, the independence assumption, or when composition might fail.

### Trivial

- The "Before" success rates in Table 1 vary slightly across different \(R\) values (e.g., KUKA: 71.3, 69.5, 69.8), which appears to be from different random seeds but is not explicitly explained.

## Nice-to-Haves

- Comparing composition to a diffusion model trained with joint conditioning (variable number of obstacles) would directly measure whether composition is necessary or just convenient.
- A visual analysis of failure cases in composition (e.g., why the KUKA composition degrades more than Maze2D) would clarify limitations.
- Analyzing how different composition weightings affect performance, especially when combining models from different training distributions.
- A discussion of the conditions under which summing conditional scores yields a valid joint distribution (citing work on compositional EBMs or score composition) would strengthen the theoretical framing.

## Removed Points

These points from the reviews were removed after cross-checking against the paper; treat them with caution:

- **"Inconsistent baseline comparison in composite figures inflates gap"** (Harsh Critic, Issue 2, sub-point 4): The reviewer claimed MπNet\*/MPNet\* trained on 6 obstacles and tested on 7+ is an unfair comparison. However, the composition method is also tested OOD without retraining; both methods face the same distribution shift. The comparison fairly evaluates which approach handles OOD generalization better. Removing retraining for baselines is not unfair — it is the experimental premise.

- **"RMP not in main comparisons"** (Section-by-Section Notes): The paper includes RMP where it is most informative (concave obstacles, Table 2). Including it in all base comparisons would add clutter without insight, as RMP is well-known to struggle generically. This is a reasonable design choice, not a weakness.

- **"Abstract overpromises"** (Section-by-Section Notes): The claim "significantly outperforming both classical and recent learned motion planning approaches" is supported by the reported results on 2D/7D/14D environments. It is not overly broad given the evidence.

- **Strength "Theoretical guarantee of probabilistic completeness"** (Strength Finder, point 4): As noted in the Minor weaknesses above, this proof is trivial and does not distinguish the method from any density estimator with full support. This is not a genuine strength.

- **Strength "Real-world validation on pedestrian datasets"** (Strength Finder, point 5): The base real-world results are qualitative, and the composed real-world results (10 pedestrians) are also qualitative-only. Without quantitative metrics, this is at best a preliminary illustration, not a validated strength.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between composition-by-potential-addition and the implicit conditional-independence assumption. The paper's empirical success on simple obstacle sets (where obstacle positions are independent given the trajectory) versus its degradation in higher dimensions (where configuration-space interactions create dependencies) suggests that composition actually works well when the constraints are nearly independent given the trajectory, and degrades when they interact. This pattern, if confirmed with further analysis, would both validate the approach in its intended regime and clarify its fundamental limitation — a nuance the paper does not currently provide. None beyond the paper's own contributions.

## Suggestions

1. **Add a jointly trained baseline** for the obstacle-count composition experiments. Train a single diffusion model on a variable number of obstacles (e.g., uniformly sampled 4–12) and compare its success on 7+ obstacle environments to the composed model. This directly addresses whether composition is better than joint training.

2. **Acknowledge and empirically probe the independence assumption.** State clearly that summing potentials yields a valid composite distribution when constraints are independent given the trajectory. Test this by constructing environments where obstacles clearly interact (e.g., overlapping obstacles in C-space) and reporting whether composition still works.

3. **Provide quantitative results for the composed ETH/UCY experiment** (10 pedestrians), including success rate and collision count.

4. **Conduct an ablation on composition weighting** (uniform vs. learned vs. heuristic scaling), particularly when composing qualitatively different models (static + dynamic).

5. **Remove or meaningfully revise the probabilistic completeness proof.** Either replace it with finite-sample guarantees or remove it entirely — the current version is vacuous.

6. **Discuss the degradation of composition in higher dimensions** (KUKA vs. Maze2D in Figure 5) and analyze whether this correlates with violations of the independence assumption in C-space.

## Score and Decision

The paper presents a novel and useful application of diffusion models to motion planning, with strong empirical results on base environments — particularly in high-dimensional spaces where learned baselines struggle. The refinement scheme is a practical contribution, and the composition experiments, while incomplete, suggest a promising capability.

However, the paper's central framing contribution — compositionality enabling principled generalization — is significantly under-supported. The theoretical basis is absent (independence assumption neither stated nor tested), the experimental evidence has critical gaps (no joint training baseline, no quantitative real-world composition results, missing ablations), and the probabilistic completeness proof is vacuous. These issues do not invalidate the base method's merit, but they prevent accepting the paper at its face value. A major revision addressing the compositionality claims would be needed for the paper to meet its stated ambitions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>