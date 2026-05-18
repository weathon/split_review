Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper addresses adversarial defense for neural VRP methods, a crucial but underexplored problem. It proposes the Collaborative Neural Framework (CNF), an ensemble-based approach with two novel components: (1) a global adversarial attack that iteratively attacks the best-performing model in the ensemble to generate stronger adversarial instances, and (2) an attention-based neural router trained via RL to distribute training instances across models for better load balancing and collaborative efficacy. Experiments on TSP and CVRP with two attack methods show CNF consistently outperforms vanilla AT, hardness-aware reweighting (POMO_HAC), and diversity training (POMO_DivTrain) on both clean and adversarial metrics, while also improving out-of-distribution generalization.

## Strengths

1. **Addresses a well-motivated, underexplored problem with clear empirical grounding**: The paper identifies that defense of neural VRP methods is "crucial yet underexplored" (Abstract, Section 1) while prior work focuses on attack. It provides empirical evidence of the accuracy-robustness trade-off in VRPs (Fig. 0), establishing a concrete gap.

2. **Consistent SOTA across both standard and adversarial metrics**: In Table 1, CNF(3) outperforms all baselines (POMO_AT, POMO_HAC, POMO_DivTrain) on TSP and CVRP at n=100 and n=200 across Uniform, Fixed Adv., and Adv. metrics. For instance, on TSP100 Fixed Adv., CNF(3) achieves 0.236% gap vs. POMO_AT(3) 0.295% and POMO_HAC(3) 0.344%. On CVRP100 Uniform, CNF(3) attains 1.073% vs. POMO_AT(3) 1.256%.

3. **Global adversarial instance generation is a principled and validated innovation**: The method generates adversarial instances by attacking the best-performing model at each inner maximization step (Eq. 5, Section 4.1), explicitly accounting for the ensemble effect. The ablation in Fig. 2a confirms its contribution — removing global adversarial instances degrades performance (from 0.118% to 0.155% on Uniform).

4. **Neural router with RL-based training provides measurable benefit**: The attention-based router (Section 4.2) adaptively distributes instances to models. Fig. 2c shows M-TopḰ (the default strategy) outperforms all alternatives (Random, Self-training, I-TopḰ, M-Sample) on both Uniform and Fixed Adv. metrics.

5. **OOD generalization improved as a byproduct**: Table 2 shows CNF(3) achieves the best gaps on cross-distribution (Rotation 0.193%, Explosion 0.084%) and cross-size (Uniform 50: 0.036%, Uniform 200: 1.383%) tasks, outperforming POMO_HAC(3) consistently.

6. **Extensive ablation studies systematically validate design choices**: The paper ablates components (Fig. 2a), the number of models (Fig. 2b), and routing strategies (Fig. 2c), providing empirical grounding for each design decision.

7. **Versatility across VRP variants and attack methods**: CNF is demonstrated with both POMO (TSP, CVRP) and MatNet (ATSP) under two distinct attack models (Zhang et al. 2022, Lu et al. 2023), establishing generality.

## Weaknesses

### Fatal
None.

### Major

1. **Unsubstantiated claim about surpassing AT(9)**: The conclusion states "It even surpasses vanilla AT trained with nine models" (line 361), but no POMO_AT(9) baseline appears anywhere in the experiments. This claim is presented as an experimental finding without supporting evidence. Either the comparison should be included, or the claim should be removed. This is an overclaim that undermines the credibility of the paper's positioning on computational trade-offs.

2. **Computational cost of the neural router is not quantified**: The outer minimization requires: (a) evaluating all M models on the full set of instances to get cost matrix R, (b) training each model on selected TopḰ instances, (c) re-evaluating all models to get R', and (d) updating the router. This is a significant overhead relative to vanilla AT. The paper reports inference time but no wall-clock training time for CNF vs. baselines. Since the contribution is an ensemble defense method, practical viability depends on whether the added training cost is justified. A comparison of total training time (pretraining + AT warm-start + collaborative training) across methods is needed.

### Minor

3. **Missing numerical values for critical hyperparameters**: The attack budget ε and attack steps T are not numerically specified. The paper says "we set the attack budget within a reasonable range based on the attack methods" (line 102) and lists T as an input to Algorithm 1 but never gives its value. These details are essential for reproducibility and understanding the threat model.

4. **Global attack's added value could be more directly demonstrated**: The ablation (Fig. 2a) shows the global attack helps, but the paper does not compare the difficulty of global vs. local adversarial instances directly (e.g., their loss values or optimality gaps after T iterations). The mechanism by which the global attack provides benefit — oscillating best-model selection vs. genuinely harder instances — remains somewhat opaque.

5. **Statistical significance claims are unverifiable**: The paper states "we have conducted t-test with the threshold of 5% to verify statistical significance" (line 271) but reports no p-values, confidence intervals, or variance estimates. Given that some gaps are small (e.g., 0.118% vs. 0.135% on TSP100 Uniform for CNF(3) vs. POMO_HAC(3)), a reader cannot assess whether the differences are reliable.

6. **Fixed Adv. metric has a known limitation explicitly acknowledged but not resolved**: The paper correctly notes that Fixed Adv. "mimics the black-box setting" where adversarial instances are generated by attacking the pretrained model. Since CNF starts from this same pretrained model, the Fixed Adv. instances may be more familiar to CNF than to baselines. The paper notes consistency between Fixed Adv. and Adv. metrics as validation, but using a truly independent surrogate model (e.g., AM instead of POMO) would be a cleaner black-box evaluation.

### Trivial
None.

## Nice-to-Haves

- A single-model variant of CNF (without ensemble but with the neural router's distribution mechanism adapted) would help disentangle whether OOD improvements come from robustness or from ensemble variance reduction.
- Acknowledging the meta-learning perspective of the router (the reward signal minR − minR' is a session-level comparison before/after a training step) would connect CNF to the learning-to-learn literature.
- Reporting sensitivity of the global attack to the number of attack steps T would help practitioners set this hyperparameter.

## Removed Points

These points were assessed against the paper and removed with justification:

1. **"Global attack may be a mirage" (framing).** The reviewer suggested the global attack might oscillate and produce no stronger instances. However, Fig. 2a directly shows that removing the global attack degrades performance (0.118% → 0.155% on Uniform). The claim that improvement "is driven entirely by the neural router and increased diversity from having more instances" is contradicted by this ablation. The underlying concern (lack of direct hardness comparison) is retained as Minor weakness #4, but the "mirage" framing is removed.

2. **"Missing comparison with Tramèr et al. ensemble AT."** The paper already cites Tramèr et al. (tramer2018ensemble) in the related work (line 62) and explains why domain-specific differences prevent direct transfer. Per the guide rules, missing related works are not to be mentioned.

3. **"The trade-off claim is weakly justified."** The paper provides empirical evidence of the trade-off (Fig. 0, comparing POMO vs POMO_AT), cites prior theoretical work (Tsipras et al., Zhang et al.), and connects it to the Geisler et al. capacity argument. The suggestion to train a single larger-capacity model is a reasonable strengthening experiment but the trade-off claim as stated is supported.

4. **"OOD improvement is modest."** The improvements are consistent across all six OOD settings in Table 2. While not large in absolute terms, the pattern is clean and the relative improvements are meaningful (e.g., Explosion: 0.084% vs 0.107% = 21% relative). This is a byproduct, not the paper's core claim.

5. **Meta-learning framing suggestion.** This is not a weakness — it is an observation about what the paper could additionally acknowledge. Moved to Nice-to-Haves.

## Novel Insights

The reviews highlight one observation that goes beyond the paper's own framing: the neural router's training procedure is structurally reminiscent of meta-learning / learning-to-learn, where the reward signal (minR − minR') compares performance before and after a full training step at the session level. This perspective could clarify why the router's gradient (Eq. 7) works despite the high-dimensional action space — it is effectively optimizing a one-step meta-objective. The paper does not draw this connection, and doing so would strengthen its theoretical framing.

## Suggestions

1. **Remove or substantiate the AT(9) claim.** Either add a POMO_AT(9) baseline to Table 1 (even in an ablation) or remove the statement from the conclusion.
2. **Report wall-clock training time** for CNF vs. POMO_AT(1), POMO_AT(3), and POMO_HAC(3) across both problem scales.
3. **Specify the numerical values of ε (attack budget) and T (attack steps)** used in all experiments.
4. **Report p-values or confidence intervals for the key comparisons** in Table 1, especially where gaps are small.
5. **Add a direct comparison of global vs. local adversarial instance difficulty** (e.g., loss values or optimality gaps after T attack steps) to validate the global attack mechanism.
6. **Provide more detail on the neural router architecture** (number of attention heads, layers, embedding dimensions) — this may be in the stripped appendix and should be in the main text.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>