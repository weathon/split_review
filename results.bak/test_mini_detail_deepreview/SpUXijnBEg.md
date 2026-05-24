Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Direct Optimal Action Learning (DOAL), a framework that avoids backpropagation through iterative sampling chains when training expressive policies (Gaussian, flow, diffusion) in offline RL. The key idea is to reinterpret the BRAC policy gradient as a target-matching objective: instead of end-to-end backprop, DOAL constructs a target action by taking a Q-gradient step from the data action, then trains the policy with a behavior-clone loss toward that target. A batch-normalizing optimizer reparameterizes the regularization coefficient α into a more interpretable trust-region parameter δ. The paper also identifies the tuning of the MaxQ sampling count n_sample as a crucial hyperparameter. Experiments on OGBench and D4RL (Adroit) across three value function families and three policy classes show that DOAL provides modest improvements over strong baselines.

## Strengths

1. **Clean, practical idea for avoiding BPTT in iterative sampling policies.** DOAL replaces end-to-end backpropagation through diffusion/flow sampling chains with a simple target-matching loss. This is conceptually elegant and practically useful: it enables training flow and diffusion policies with standard BC losses (e.g., flow matching) without gradient computation through iterative sampling. The computational benefit is clearly quantified in Figure 2 (DMFQL: 18 NN calls vs MFQL-BPTT: 37 calls; 37 min vs 61 min).

2. **Versatility across value functions and policy classes.** DOAL is demonstrated with three value function families (IQL, Q-learning, regularized Q-learning) and three policy architectures (Gaussian, flow, diffusion). On OGBench, DOAL consistently improves over baselines across all combinations (DIOL 276 vs IQL-Gauss 191; DIFQL 359 vs IFQL 329; DTrigFlow 368 vs TrigFlow 361; DMFQL 443 vs MFQL 418; DMFReBRAC 466 vs MFReBRAC 425). This breadth supports the claim that the framework is general-purpose rather than tied to a specific implementation.

3. **Honest and nuanced reporting of results.** The paper explicitly acknowledges where DOAL works and where it does not: no improvement on D4RL with IQL, dependence on Q-function quality, the tanh limitation, and the fact that improvements are driven by a few tasks while most tasks show similar performance to baselines. The paper also acknowledges that the batch-normalizing optimizer is functionally equivalent to a fixed gradient scale (lines 158, 333). This transparency is a strength.

4. **Identification of the n_sample trade-off in MaxQ sampling.** Proposition 3 (informal) and the surrounding discussion correctly identify the overestimation bias vs. coverage trade-off in MaxQ sampling. Tuning n_sample produces large baseline improvements (e.g., IFQL 329 vs IFQL* 218), which is a practically useful insight regardless of DOAL.

## Weaknesses

### Major

1. **The theoretical connection between BRAC and DOAL is asserted rather than analyzed.** Proposition 1 shows that the BRAC gradient (with deterministic policy and MSE behavior loss) equals the gradient of an MSE objective targeting a^{brac,target} = a + (1/2α)∇_{a'}Q(s,a')|_{a'=π_θ(s)}. DOAL then replaces the gradient evaluation point from π_θ(s) to the data action a. The paper says these objectives are "similar but different" and that DOAL "is a reasonable objective for offline RL in its own right" (line 139), but it provides **no analysis of when or why this approximation is good**. For multimodal policies (flow, diffusion) where the BC loss is not MSE, the connection is even looser. The practical benefits of DOAL are clear, but the claimed theoretical motivation is incomplete — the method stands or falls on its empirical merits, not on Proposition 1.

2. **The experimental improvements of DOAL over already-tuned baselines are modest and inconsistent.** The paper's own analysis shows that tuning n_sample yields large baseline gains (IFQL 329 vs IFQL* 218 = +111), while DOAL's additional improvement over those tuned baselines is much smaller (DIFQL 359 vs IFQL 329 = +30; DTrigFlow 368 vs TrigFlow 361 = +7). On D4RL with IQL, DOAL provides no improvement (DIOL 518 vs IQL-Gauss 520). With Q-learning, DMFQL (614) underperforms MFQL (623) on D4RL total. DOAL only reliably improves on D4RL with regularized Q-learning (DMFReBRAC 630 vs MFReBRAC 614). Meanwhile, a simple tanh-parameterized policy (ReBRAC(tanh): 706) far exceeds all DOAL variants. The paper's core claim — that DOAL enables efficient, effective policy extraction — is not strongly supported when the primary gains come from tuning n_sample rather than from the gradient-based target itself.

3. **Many task-level comparisons are within one standard deviation.** Examples from Table 1: antmaze-large-navigate (DIFQL 67±25 vs IFQL 48±24), puzzle-3x3 (DIFQL 5±2 vs IFQL 5±1). From Table 2: cube-double-play (DMFQL 75±6 vs MFQL 72±4), puzzle-4x4 (DMFQL 14±4 vs MFQL 24±3 — DOAL is worse). The aggregate totals show improvement, but per-task statistical significance is not established. While single-run evaluation with standard deviations is standard in offline RL, the modest aggregate gains combined with many noise-level per-task comparisons weaken the evidence for DOAL's effectiveness.

### Minor

4. **The hyperparameter δ still requires non-trivial tuning.** While δ varies less than α (0.03–0.3 on OGBench vs α spanning 10–1000), it still spans a factor of 10 within each benchmark. Table 3 shows that the effective step size after normalization varies by a factor of ~25 across four environments (6.9×10⁻⁴ to 1.8×10⁻²). The paper's claim that δ is "interpretable" and that it "simplifies" hyperparameter search is valid but overstated — it reduces the search range but does not eliminate search.

5. **DOAL's advantage over the equally efficient ETrigFlow is unclear.** ETrigFlow (score 359 on OGBench) is a one-step diffusion method that also avoids BPTT and uses the BRAC objective. DTrigFlow (368) outperforms it by only 9 points across 9 tasks, and on several individual tasks ETrigFlow is comparable or better (e.g., scene-play: 50 vs 46; antmaze-large: 63 vs 63). This weakens the claim that DOAL's target formulation is meaningfully better than simpler alternatives.

### Trivial

6. The paper says "setting α to 1 is fine" with a reference to an ablation in Appendix F, but that appendix is stripped by the parser. This should be verifiable in the main text or supplementary.

## Nice-to-Haves

- A direct empirical comparison of DOAL's target (gradient at data action) vs. the BRAC target (gradient at policy output) for cases where the latter is feasible (Gaussian policies, one-step sampling). This would directly test whether the target construction matters beyond computational convenience.
- An analysis of the target action distribution: does a^{target} stay within the dataset support? Visualizing the distribution shift would directly address the conservatism concern.
- Sensitivity to the number of diffusion/flow steps used in the policy.

## Removed Points

The following points from the reviewers are removed with justifications:

- **Ablation study in Appendix F mentioned only in passing**: The appendix is stripped by the parser. Per hard rules, criticisms about missing appendix content are removed as they exist in the original submission.
- **Missing baseline comparison to fixed gradient step size (without batch normalization)**: The paper explicitly addresses this (Section 5.3, lines 333), explaining that the batch normalization is functionally equivalent to a fixed scaling factor per environment, and that the advantage is in the reduced hyperparameter range. The critic's concern is already addressed in the paper.
- **Scope limited to two benchmarks (MuJoCo omitted)**: The paper explicitly scopes itself ("We omit some tasks, as no current algorithms can work well", following Park et al., 2025c). Criticizing scope choices outside the paper's stated scope is not a valid weakness.
- **Pure formatting/style nitpicks and references to "missing" elements**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Provide an empirical comparison (even on a simple Gaussian policy) between DOAL's target and the BRAC target to validate the target construction claim directly.
- Report per-seed results or effect sizes for the critical DOAL-vs-baseline comparisons where aggregate totals improve but individual tasks are within noise.
- Include an ablation showing performance as a function of δ across its range on representative tasks, demonstrating the safe operating region.
- Discuss more explicitly the conditions under which DOAL is expected to help vs. hurt (e.g., quantify Q-function gradient quality).

## Score and Decision

**Calibration Summary**

All anchors retrieved across rounds:

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Offline MARL with SS Decomp | mc97L2QVIa.md | 3.00 | R1 (weak) | Much weaker — less clean contribution, narrow scope |
| Offline-to-Online CFDG | cXxfVkRCHJ.md | 3.00 | R1 (weak) | Much weaker — more applied, less contribution |
| RF-POLICY | wQCPHxtzGV.md | 4.75 | R1 (mid) | Comparable — similar scope (flow for offline) but RF-POLICY rejected for weak novelty. This paper has broader evaluation but similar theoretical gap. |
| BDQL | gEdg9JvO8X.md | 3.67 | R1 (mid) | Weaker — unclear contribution, diffusion without policy constraint |
| Energy-Weighted FM | HA0oLUvuGI.md | 6.25 | R1 (mid), R2 | Stronger — cleaner theoretical contribution (provable energy guidance), similar experiment scope, accepted |
| Score-Regularized PO | xCRr9DrolJ.md | 6.25 | R1 (mid), R2 | Stronger — rigorous derivation connecting score functions to behavior regularization, accepted despite modest empirical gains |
| Diffusion Actor-Critic | ldVkAO09Km.md | 6.50 | R2 | Stronger — full framework with stronger empirical results, accepted |
| Value function estimation w/ conditional diffusion | TeeyHEi25C.md | 6.25 | R1 (mid), R2 | Stronger — cleaner problem framing, accepted despite mixed reviews |

**Round 1 bracket**: Plausible range was [4, 6]. The paper is clearly stronger than papers scoring 3–4 (BDQL, CFDG) but not as strong as papers scoring 6.25+ (EFM, SRPO, DAC).

**Round 2 narrowing**: Compared against RF-POLICY (4.75, rejected) and the 6.25 anchors (EFM, SRPO). This paper is somewhat stronger than RF-POLICY (broader evaluation, cleaner idea) but clearly weaker than EFM and SRPO (which had rigorous theoretical derivations supporting their method, whereas DOAL's Proposition 1 is heuristic). The paper lands between these anchors.

**Final score**: 5.0. The paper presents a clean, practical idea with broad empirical validation, but the theoretical motivation is incomplete, and the experimental improvements over well-tuned baselines are modest and inconsistent. The contribution is real but not strong enough for acceptance at a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>