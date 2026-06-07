Let me finalize the review now.

## Summary

This paper proposes Sample Weight Decay (SWD), a method that weights replay buffer samples by recency (linear decay based on sample age) to mitigate plasticity loss in deep RL. The theoretical contribution is a gradient analysis in Fitted Q-Iteration showing that the initial gradient at each iteration decays as Θ(1/k) due to distribution shift in the replay buffer. SWD is motivated as counteracting this decay by prioritizing recent data. Experiments across DMC, MuJoCo, and ALE with SAC, TD3, and Double DQN show consistent performance improvements, and a reverse-ablation (SWA, which weights older samples more) provides bidirectional evidence for the temporal direction.

## Strengths

1. **Theorem 3 isolates a concrete Θ(1/k) gradient decay mechanism from replay-buffer structure.** The gradient decomposition in Equation (4) identifies a distributional-shift term whose magnitude scales as 1/k, arising from the recursive empirical distribution in Proposition 1. This provides a formal, non-trivial mechanism linking replay buffer non-stationarity to gradient attenuation — a connection that existing plasticity work (ReDo, Plasticity Injection, ReGraMa) does not establish.

2. **The SWA counterfactual (reverse weighting) provides bidirectional causal evidence.** Figure 5 shows that SWA — which assigns higher weights to older samples — reduces gradient L1 norms, reduces GraMa, and degrades performance relative to both SWD and uniform sampling. This rules out the hypothesis that any non-uniform reweighting explains the improvement, isolating the temporal direction (recency prioritization) as the causal factor.

3. **Consistent improvements across a diverse experimental grid.** SWD improves performance across three algorithms (SAC, TD3, Double DQN), three benchmark suites (DMC, MuJoCo, ALE), multiple UTD ratios (1, 2, 5), and multiple network architectures. The method is simple, with minimal computational overhead (a bucket-based approximation is mentioned in Section 6.6).

## Weaknesses

### Major

1. **Contradictory definition of the GraMa metric (Section 6.3, line 232).** The paper states: "Notably, a larger GraMa value indicates a weaker learning capability of the neural network." Yet every result then treats higher GraMa as evidence of better plasticity. Figure 6 uses higher GraMa for SWD vs. SAC to claim SWD "effectively mitigates the loss of plasticity." Figure 5 uses higher GraMa for SWD than SWA as evidence that SWD has better plasticity. If larger GraMa = weaker learning, then SWD (higher GraMa) would have weaker learning capability than SAC — the exact opposite of what the paper argues. The correlation of GraMa with gradient L1 norms in Figure 5 (both higher for SWD, lower for SWA) further indicates the stated interpretation is inconsistent with the data. This contradiction makes the paper's primary evidence for plasticity mitigation (Q2) uninterpretable as written. The authors must clarify the correct interpretation of GraMa and reconcile it with their results.

2. **SOTA claim is not supported by the evidence provided.** The paper claims "SOTA performance on challenging DMC Humanoid tasks" (abstract, contributions). The evidence for this is a comparison against three methods (ReGraMa, S&P, Plasticity Injection) on a single task (Humanoid Run) using a single architecture (SimBa). In Figure 8, SWD alone achieves ~240 IQM vs. S&P at ~220 — with overlapping confidence intervals given typical RL variance. A single-task comparison against a limited set of prior methods does not justify a SOTA claim, especially in the absence of comparisons with recently published strong results on these benchmarks.

3. **The theory-experiment gap is underaddressed.** The theoretical analysis is developed for FQI with the target-drift term eliminated by setting f̂_{H+1}≡0. Experiments test TD3, SAC, and Double DQN — none of which are FQI, and all of which have non-negligible target drift from periodic target network updates and (in actor-critic) policy gradients. The paper states the theory "can be readily extended" (Section 4) and that "analogous analytical findings hold for entropy-regularized MDPs" but provides no formal extension. The claimed "theoretically grounded" framing of SWD rests on an unverified transfer; the theory motivates the method but does not prove it correct for the algorithms tested.

### Minor

4. **The claim that SWD "neutralizes" the 1/k attenuation is intuitive but unproven.** The paper states SWD "neutralizes the 1/k attenuation, restoring gradient magnitude" (Section 5) but never formally shows that the linear weighting scheme w_i = max(w_min, 1 − age_i/T) reverses the specific 1/k decay. No derivation of the gradient magnitude under SWD is given, nor is there analysis relating T and w_min to the required counteraction. The empirical evidence (Figure 5b showing higher gradient L1 norms) is consistent with the intuition but falls short of a principled demonstration. The paper would benefit from either a formal characterization or a more measured claim (e.g., "empirically counteracts" rather than "neutralizes").

5. **The "orthogonality" claim is not well-supported.** SWD+S&P achieves essentially identical aggregate metrics to SWD alone (~240 IQM in both cases, Figure 8). If the methods are orthogonal, one would expect SWD+S&P to clearly exceed SWD alone. As presented, the result suggests SWD alone may capture most of the benefit, making the orthogonality claim inconclusive.

6. **Statistical reporting gaps for UTD experiments.** Figure 7 reports only point estimates (+25.4%, +17.3%, +30.1%) without confidence intervals or error bars, making it impossible to assess whether these differences are statistically significant.

7. **The NTK degeneration section (Section 4.1) does not connect to the method or experiments.** It is presented as theoretical context for prior methods but does not inform SWD and is not tested. The paper acknowledges it "focuses on the second mechanism," but the NTK discussion inflates the claimed theoretical contribution without adding substance to the method.

8. **Figure 7 label says "IOM" instead of "IQM"** (line 238).

## Nice-to-Haves

- A more formal characterization of what gradient magnitude SWD produces as a function of T and w_min (even a simplified setting) would strengthen the theory-to-method link.
- Extending the method comparison to more environments (beyond Humanoid Run) and more baselines would substantiate the SOTA claim.
- The UTD results would benefit from visible confidence intervals.

## Removed Points

These points from the inputs were removed after verification:

- "GraMa contradiction is fatal/structural" — Kept but downgraded from Fatal to Major. The contradiction is real but corrigible, and the performance results and gradient L1 norms stand independently of the GraMa interpretation.
- "Theory and experiments set in incompatible algorithmic regimes" — Kept but downgraded from Structural to Minor weakness #3. The distribution-shift mechanism transfers in spirit, but the formal connection is incomplete.
- "Missing appendix/proofs/related works" — Removed per hard rules (parser strips appendix; unknown external works assumed to exist).
- "Computational overhead not discussed" — Removed. The paper mentions a bucket-based approximation in Section 6.6. This is adequate for a main-track paper.
- "Should compare SWD on top of each existing method individually" — Removed as scope creep; demonstrating orthogonality with one representative method (S&P) is a reasonable choice.
- "Paper should discuss trade-off of reduced data diversity from oversampling recent data" — Removed as generic/speculative.
- Strength about "SWD+S&P outperforms both methods individually" — Weakened (moved to Minor weakness #5) because the data shows SWD alone ≈ SWD+S&P, not a clear additive improvement.
- Generic strengths about "addressing an important problem" — Removed as lacking specificity.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Resolve the GraMa definition — either correct the statement on line 232 to match the paper's usage, or explain the apparent contradiction.
2. Temper the "SOTA" and "theoretically grounded" claims to match what is actually demonstrated (consistent improvement across benchmarks; theory-motivated rather than theory-grounded).
3. Add confidence intervals to Figure 7.
4. Consider adding a more formal (even simplified) analysis connecting the SWD weighting scheme to the 1/k gradient decay.

## Score and Decision

**Calibration anchors used (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Neuroplastic Expansion | 20qZK2T7fa | 6.50 (Accept) | R1 | Stronger experiments, more baselines. Current paper weaker — has unresolved GraMa contradiction. |
| Towards Perpetually Trainable | KIq6p9iv2q | 5.75 (Reject) | R1/R2 | Similar overclaiming issues but more thorough mechanism analysis. Current paper similar quality but with a more serious internal contradiction. |
| Curvature Explains Loss of Plasticity | SkF7NZGVr5 | 5.50 (Reject) | R1 | Limited evaluations, incomplete explanation. Current paper has broader experiments but also issues. |
| Stay Hungry, Keep Learning | QmXfEmtBie | 5.25 (Reject) | R2 | Limited to PPO; current paper has broader algorithmic validation but a more serious internal flaw. |
| Influence Estimation (PIToD) | EWNH3QTSxd | 3.75 (Reject) | R2 | Much weaker paper overall. Current paper is clearly stronger. |

**Round 1 bracket:** 3.5–6.5. **Round 2 narrowing:** 4.5–5.5. The paper is slightly weaker than "Towards Perpetually Trainable" (5.75) because its core evidentiary claim (plasticity mitigation via GraMa) is compromised by an internal contradiction. It is stronger than "Stay Hungry, Keep Learning" (5.25) due to broader algorithmic validation (3 algorithms vs. 1) and the SWA counterfactual design. **Final score: 5.0.**

The paper has a clean, simple method and consistent performance improvements across a broad experimental grid. However, the GraMa definitional contradiction undermines the central plasticity evidence, the SOTA claim is unsupported by the scope of comparisons, and the theoretical grounding is weaker than claimed. At ICLR standards these issues are too significant for acceptance in the current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>