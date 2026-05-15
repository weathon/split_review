Now I have a complete picture. Here is the final consolidated review.

---

## Summary

This paper investigates whether flat reward maxima in policy parameter space imply robustness in reinforcement learning. It proposes a theoretical link (Proposition 1) connecting flatness of the reward landscape to action robustness, and provides extensive empirical results using SAM+PPO across three MuJoCo environments under action noise, mass/friction perturbations, and reward noise. The experiments show that SAM+PPO consistently outperforms standard PPO and the robust RL baselines RNAC and RARL across most tested scenarios.

## Strengths

- **Broad empirical evaluation across multiple perturbation types.** The paper tests action noise (Fig. 3), torso mass variations (Fig. 4), friction coefficient changes (Fig. 5), joint mass-friction perturbations (Fig. 6, Table 1), and reward noise (Table 2) across three continuous control environments. This breadth goes well beyond the action-only tests in prior flatness-for-RL work (Lee et al., 2024), directly supporting the claim that flatter reward landscapes correlate with robustness against diverse environmental variations.

- **Quantitative reward flatness measurement.** Table 3 reports two standard flatness metrics (maximum Hessian eigenvalue λ_max and LPF flatness) demonstrating that SAM+PPO converges to flatter minima than PPO, and Figure 7 provides corresponding surface visualizations. This gives reproducible evidence for the flatness difference, which earlier work on reward flatness in RL often lacked.

- **Favorable comparison with established robust RL baselines.** SAM+PPO outperforms RNAC and RARL in most perturbation scenarios (Figs. 4–6, Table 1), showing that a simple flatness-promoting modification to PPO achieves competitive or better robustness without the complexity of adversarial training. This is a meaningful empirical result.

- **Important and under-explored research question.** Understanding the connection between reward landscape geometry and RL robustness is practically important, and the paper tackles it with a clear framing.

## Weaknesses

### Major

1. **Definition 1 is too strong to be practically meaningful, which undermines the theoretical contribution.**  
   Definition 1 requires that for *all* parameter perturbations ‖ε‖ ≤ ℰ, the expected return under π_{θ*+ε} is *exactly* r* (the optimal return). In continuous parameter spaces with neural network policies, this condition is essentially never satisfied — it defines a perfectly flat plateau of identical maximal return rather than a minimum with low curvature. The standard notion of flatness in optimization allows the objective to decrease, just slowly. Because Proposition 1 and the claimed "rigorous link" between flatness and action robustness depend on this definition, the theoretical argument rests on a premise that has no practical instantiation. This does not invalidate the empirical results, but it means the paper substantially overclaims what the theory establishes. The definition could be repaired by using an inequality (e.g., return ≥ r* − δ), but this would require re-deriving the proposition.

2. **The empirical evaluation does not establish that flatness *causes* robustness — it shows correlation with a single method.**  
   The paper compares SAM+PPO against PPO, RNAC, and RARL, reporting that SAM+PPO achieves flatter reward landscapes (Table 3) and better robustness. However, it never isolates the mechanism: (a) no ablation varies the SAM radius ρ to test whether increased flatness monotonically improves robustness; (b) no other flatness-promoting method (e.g., SWA, Entropy-SGD) is included to see if *any* flatness method yields robustness; (c) no control exists for the fact that SAM is a different optimizer that may affect convergence quality beyond flatness. Without these controls, the central causal claim — that flatness itself drives robustness — is an unwarranted inference from correlation. This is the most significant empirical weakness.

### Minor

3. **Key figures lack error bars or variance measures.**  
   Figures 3, 4, and 5 plot average returns under various perturbations without any indication of variance. While the paper states that experiments were conducted over five independent trials with 100 evaluation runs each, the absence of error bars, shaded regions, or confidence intervals makes it impossible for the reader to assess the reliability and significance of the reported improvements. This is straightforward to fix.

4. **Flatness metrics are not reported for RNAC and RARL.**  
   Table 3 reports λ_max and LPF flatness only for PPO and SAM+PPO. If the paper's central claim is that flatter minima imply better robustness, then reporting flatness metrics for all baselines (including RNAC and RARL) would provide crucial evidence for whether inferior robustness indeed correlates with sharper minima across methods. Without this, the reader cannot distinguish between "flatness causes robustness" and "SAM+PPO happens to be a better optimizer."

5. **The informal link to transition and reward robustness (Remark 1.2) does not constitute theoretical grounding for those experiments.**  
   Remark 1.2 is explicitly labeled as "informal" and provides only intuitive reasoning. The paper then runs experiments on transition perturbations (mass, friction) and reward noise, presenting them as if they follow from the same theoretical framework. In reality, the theory (Proposition 1) formally covers only action robustness. The transition and reward experiments are valuable empirical explorations, but the paper should more clearly separate what is theoretically established from what is empirically observed, rather than implying a unified theoretical umbrella.

6. **Reward noise experiment tests training-time noise, not test-time robustness.**  
   Section 5.4 adds reward noise during training rather than at test time, which tests a different phenomenon (robustness to noisy training signals) from what Remark 1.2 suggests (robustness to reward function perturbations at deployment). The paper explains its choice (test-time noise would trivially average out), but the mismatch between the claimed motivation and the actual experiment should be clarified.

### Trivial

- Definition 1 overloads the symbol ε to mean both the perturbation radius and the perturbation vector, which is momentarily confusing.
- Figure 6 heatmaps are presented without numerical summaries in the figure itself (though Table 1 provides aggregate numbers).

## Nice-to-Haves

- An ablation study varying the SAM radius ρ and measuring both flatness metrics and robustness would directly test the monotonicity assumption and significantly strengthen the causal claim.
- Including other flatness-promoting optimizers (SWA, Entropy-SGD) as baselines would help isolate flatness as the mechanism.
- Reporting flatness metrics (λ_max, LPF) for RNAC and RARL would make the cross-method comparison complete.

## Removed Points

- **Criticism that Proposition 1 lacks a proof or derivation.** Per the review guidelines, appendix/proof sections are stripped by the parser from all papers and exist in the original submission; this criticism cannot be verified from the parsed text.
- **Criticism that the 2D navigation example is "not quantitatively evaluated."** This is a motivating illustration, not a main experiment; requiring quantitative evaluation here is scope creep.
- **Criticism that Remark 1.2 is "speculation" with no argument.** The remark explicitly labels itself as informal and provides reasoning for both reward and transition perturbations. The criticism mischaracterizes what the paper claims.
- **Strength Finder claim about "formal theoretical linkage" as a core strength.** Given the Definition 1 issue (Major weakness #1), this strength is overstated and conflicts with a verified weakness; the weakness takes precedence.
- **Strength Finder claim about "informal extension to transition and reward robustness."** This is generic and lacks specific evidential backing beyond what is already in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main novel insight is that the paper's causal claim (flatness → robustness) is undersupported: the theory uses an idealized definition that is never satisfied in practice, and the experiments correlate flatness with robustness via a single method without isolating the mechanism. This highlights a gap between how the paper frames its contribution and what its evidence actually supports.

## Suggestions

1. **Revise Definition 1** to use an inequality-based condition (e.g., expected return ≥ r* − δ for ‖ε‖ ≤ ℰ), and re-derive or restate Proposition 1 accordingly. This would make the theoretical framework realistic and useful.
2. **Add error bars** (or shaded regions indicating standard deviation/standard error) to Figures 3, 4, and 5 to enable readers to assess significance.
3. **Run a SAM radius ablation** (vary ρ and measure both λ_max/LPF and robustness) to directly test whether increased flatness monotonically improves robustness.
4. **Report flatness metrics for RNAC and RARL** in Table 3, or explain why they cannot be computed.
5. **Clearly delineate** in the narrative which claims are theoretically established (action robustness only) and which are supported by empirical observation alone (transition and reward robustness).
6. **Add at least one alternative flatness-promoting method** (e.g., SWA) as a baseline to help isolate flatness as the causal mechanism.

## Score and Decision

The paper tackles an important question and provides broad empirical evidence that SAM+PPO outperforms several baselines across diverse perturbations. However, the theoretical foundation is built on an unrealistic definition that makes Proposition 1 practically vacuous, and the empirical design does not isolate flatness as the causal mechanism — it shows only correlation with a single method. The paper's central claim is oversold relative to what the evidence supports. A major revision addressing the theoretical definition and adding proper causal controls (ablation, alternative flatness methods, complete flatness reporting) could make this a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>