Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes PA-RL (Parameterization-Agnostic RL), an offline-to-online RL fine-tuning approach that replaces the policy gradient with a supervised learning loss on "optimized" actions. The optimization combines global re-ranking of multiple action samples by Q-value with local gradient ascent on actions, then trains the policy via standard maximum likelihood. The key claimed contribution is that this single algorithm works across Gaussian, diffusion, and autoregressive categorical transformer policies without per-class modifications. Experiments span simulated benchmarks (D4RL AntMaze, FrankaKitchen, CALVIN) and real WidowX robot tasks with diffusion policies, plus a result claimed for OpenVLA (7B parameter model).

## Strengths

- **Universality across policy classes demonstrated.** PA-RL is tested with diffusion policies (simulated and real-world), autoregressive categorical transformer policies (simulated), and Gaussian policies (via the base Cal-QL/IQL/RLPD algorithms). Table 2 shows a 224% improvement over offline initialization for autoregressive transformer policies, and Table 1 shows strong results across three distinct simulated benchmarks. This is the paper's core contribution and it is supported by evidence.

- **Strong simulated fine-tuning results.** PA-RL + Cal-QL achieves a claimed 13% aggregate improvement over the next best method after 1k episodes of fine-tuning (Table 1). On the CALVIN task with raw visual observations, the paper reports a 69% improvement over the next best method. Learning curves (Figure 2) show PA-RL dominating or matching baselines throughout training.

- **Real-robot fine-tuning of diffusion policies.** On a real WidowX robot, PA-RL improves a pre-trained diffusion policy by 20–35% within 50–110 minutes of autonomous interaction (Table 3). This includes a distribution-shift scenario (task b) where filtered BC cannot even be seeded. These are practically meaningful results.

- **Ablation provides design insight.** Table 4 examines the contribution of global vs. local optimization on two tasks, showing that global optimization is critical on diverse data (antmaze-large-diverse), while both are important on narrower data (CALVIN). This provides useful practical guidance despite the limited task coverage.

- **Clean integration with existing RL algorithms.** PA-RL only modifies the policy improvement step, leaving critic training (Cal-QL, IQL, RLPD) unchanged. This is clearly documented in Section 4.3 and Algorithm 2, making the method easy to adopt in existing pipelines.

## Weaknesses

### Fatal

None.

### Major

- **The most striking claimed result (OpenVLA) is not supported by any experiment in the main paper body.** The abstract and introduction state that "PA-RL is the first RL method to improve 7 billion parameter OpenVLA by 75% within 40 minutes of real-world interaction." However, the real-robot section (5.2) describes only WidowX experiments with diffusion policies. No table, figure, experimental setup description, or even a reference to an appendix section for the OpenVLA result appears anywhere in the main text (Sections 1–6). While the appendix (stripped by the parser) may contain this experiment, the main paper body should at minimum reference it and present key numbers. A headline claim of this magnitude must be verifiable from the main paper. This is an evidential gap in the paper as presented.

### Minor

- **No error bars, standard deviations, or seed counts on the main simulated or real-robot results.** Tables 1, 2, and 3 report single numbers. The learning curves in Figure 2 are described as showing PA-RL "largely stays above the performance of all other methods" but are presented without confidence bands. Given the known variability of RL fine-tuning, the claimed improvements (13% aggregate, 69% on CALVIN, 224% for transformers) cannot be assessed for statistical significance. This weakens confidence in the quantitative claims.

- **No direct experimental comparison to an AWR or filtered-BC baseline in the simulated benchmarks.** The paper's core methodological claim is that using optimized *current-policy* actions is more aggressive and effective than weighting/filtering *dataset* actions as in AWR (Section 4.3, Equation 4.6). However, the simulated experiments compare against IDQL, DPPO, DQL, and standard Cal-QL — none of which is a simple AWR baseline. A controlled comparison (same critic, same policy class, but using dataset actions weighted by Q-values vs. PA-RL's optimized actions) would directly test the paper's central intuition. The real-robot filtered BC comparison covers only one task.

- **Missing control for the RLPD experiment.** Table 2 (left) shows PA-RL+diffusion outperforming Gaussian policies in the RLPD hybrid-RL setting. But since standard RLPD uses a Gaussian policy, the improvement could partly stem from greater policy expressivity rather than PA-RL's optimization mechanism. A control using RLPD with a diffusion policy but without PA-RL's optimization loop (e.g., standard policy gradient for diffusion) is absent.

- **Cal-QL modification without discussion of conservatism guarantees.** The paper replaces the current-policy action samples in the Cal-QL Bellman backup and conservative penalty with optimized actions from π°pt (Section 4.3, Algorithm 2). This is a non-trivial change to a theoretically motivated algorithm. The paper does not discuss whether this affects the conservatism properties or provides an empirical check (e.g., does the Q-function remain calibrated?).

- **Ablation limited to two tasks.** Table 4 compares PA-RL variants with/without global/local optimization on only antmaze-large-diverse and CALVIN. The resulting conclusions ("global optimization is important in general, but local optimization is useful when dataset action distributions are narrow") are plausible but speculative given the narrow empirical basis.

### Trivial

- **Phrasing of the novelty claim.** The statement "PA-RL enables fine-tuning diffusion and autoregressive policies entirely via RL" (abstract/intro) could be read as implying prior work does not fine-tune diffusion policies via RL at all. The related work correctly acknowledges DPPO, DQL, and IDQL, which do fine-tune diffusion policies. The intended novelty is that the *same* algorithm works for both classes — this should be stated more precisely in the abstract.

## Nice-to-Haves

- A quantitative characterization of the CALVIN dataset's multimodality (e.g., number of action modes per state, action variance) would strengthen the claim that expressive policies are beneficial.
- A discussion of how sensitive the real-robot results are to the quality of the pre-trained critic (trained on only 20 demos).
- Wall-clock time analysis and how the hyperparameters k (number of samples) and T (local gradient steps) scale with policy size, especially for large models like OpenVLA.
- Reporting per-trial outcomes or bootstrapped confidence intervals for the real-robot success rates in Table 3.

## Removed Points

These points were removed from the main weaknesses with justification:

1. **"Claim about poor performance across policy classes not directly tested"** — The paper tests Gaussian vs. diffusion vs. autoregressive and shows standard SAC/Cal-QL (Gaussian) transfers poorly to diffusion policies, while PA-RL works across classes. The criticism is a strawman; the supporting evidence is adequate.

2. **"Equation 4.6 Taylor expansion is not a proof"** — The paper explicitly states "Obtaining the LHS of Equation 4.6 requires Taylor's expansion at every step of local optimization, under the assumption that step size α is small enough." The paper is transparent about this being intuition. This is not a flaw.

3. **"Related work should discuss more online methods"** — This is scope creep; the paper's focus is offline-to-online fine-tuning, and it cites the relevant comparison points (CEM-based online methods, Neumann et al., Shao et al.) with an explanation of why they differ.

4. **"Paper should test more policy classes"** — The paper tests three distinct classes (Gaussian, diffusion, autoregressive categorical transformer) which is substantial for a single paper. Demanding more is scope creep.

5. **Formatting/style nitpicks and typo claims** — These are parser artifacts, not author errors.

## Novel Insights

The reviews surface a tension that the paper does not fully address: PA-RL's "parameterization-agnostic" claim rests on the observation that existing RL algorithms entangle the policy gradient computation with the policy class. But PA-RL replaces the gradient entirely with supervised learning on optimized actions — meaning it sidesteps rather than solves the gradient-computation problem. The key question the paper should more directly address is whether the decoupling of action optimization from policy training is fundamentally better than per-class gradient methods, or merely a pragmatic workaround. The missing AWR baseline and the missing RLPD+diffusion control would speak directly to this. The reviews do not add significant novel insight beyond what is already apparent from reading the paper.

## Suggestions

1. **Move the OpenVLA experiment into the main paper body**, or if space is constrained, at minimum add a paragraph with a summary table and a clear reference to the appendix section where the full details appear.

2. **Add error bars (standard deviations over at least 3–5 seeds) to all main tables and learning curves.** For the real-robot results, provide bootstrapped confidence intervals or per-trial outcomes.

3. **Include an AWR-style baseline** on at least 2 simulated tasks: use the same critic training but replace PA-RL's optimized-action loss with an advantage-weighted NLL on dataset actions. This directly tests the paper's core claim about the value of action optimization.

4. **Add the missing control for the RLPD experiment** — RLPD with a diffusion policy but without PA-RL's optimization loop — to disentangle the contribution of policy expressivity from the contribution of the optimization procedure.

5. **Briefly discuss the Cal-QL modification.** Even a sentence acknowledging that the conservatism properties may change and pointing to an empirical check (e.g., Q-value calibration plot) would suffice.

## Score and Decision

The paper proposes a sensible and well-motivated method with genuine empirical contributions: it demonstrates a single RL algorithm that effectively fine-tunes diffusion policies (in simulation and on a real robot) and autoregressive transformer policies. The simulated results are strong and the real-robot results on WidowX are practically meaningful. However, the paper's most attention-grabbing claim (OpenVLA) is not supported by any experiment in the main body, and the main quantitative results lack error bars, making the strength of the improvements uncertain. The missing AWR baseline is a methodological gap that weakens the paper's central comparison. These are addressable issues, but in their current form they reduce the confidence in the paper's claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>