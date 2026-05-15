Now I have all the verification I need. Here is my final consolidated review.

---

## Summary

This paper proposes HuRi, an adaptive risk-aware distributional reinforcement learning method for humanoid robot locomotion. The key idea is to dynamically adjust the risk sensitivity parameter of the Wang distortion function by combining two signals: the interquartile range of the return distribution (capturing intrinsic/aleatoric uncertainty) and the prediction error of a random network distillation module (capturing epistemic/novelty uncertainty). The method is evaluated in simulation (Isaac Gym) and on a real Zerith-1 humanoid robot under various disturbances including heavy loads, pendulum impacts, and sustained external forces.

## Strengths

- **Strong empirical evidence for the adaptive mechanism in simulation (Table 1).** Under continuous centroid disturbances (0–100 N, far exceeding the training range of 0–10 N), HuRi achieves a 95.2% success rate versus 12.4% for PPO, 24.6% for CVaR₀.₅, and 46.3% for HuRi w/o RND. These are large, unambiguous margins that directly support the claim that adaptive risk sensitivity improves robustness against out-of-distribution disturbances.

- **Clean ablation design isolates the contribution of the RND-based uncertainty signal.** The comparison between HuRi and HuRi w/o RND (which removes the parameter-uncertainty component) isolates the contribution of the RND module. Across Table 1's nine conditions, HuRi consistently outperforms the w/o RND variant (e.g., 95.2% vs. 46.3% on continuous centroid disturbance), demonstrating that the parameter uncertainty signal provides meaningful additional information beyond intrinsic uncertainty alone.

- **Real-world deployment with challenging and creative test conditions.** The paper reports real hardware experiments on the Zerith-1 robot including a 3 kg pendulum impact, centroid loads up to 15 kg (~42% of body weight), and foot loads producing significant hip torque. The pendulum-impact setup is a particularly challenging and non-standard test of dynamic disturbance rejection.

- **The dual-uncertainty design (IQR + RND) is conceptually well-motivated.** Distinguishing between aleatoric (IQR) and epistemic (RND) uncertainty and mapping each to policy risk sensitivity is grounded in the distributional RL and exploration literatures. The qualitative beta dynamics in Figure 5 show the expected behavior (higher β on uneven terrain and under sudden pushes), lending face validity to the mechanism.

## Weaknesses

### Fatal
None.

### Major

- **The overall loss function is incompletely specified (Section 3.4).** The text reads "The calculation formula of HuRi's overall loss function is" and then provides no equation — only a prose discussion of the component loss terms (quantile energy loss, MSE on distorted expectations, entropy). While individual terms are defined in Equations (4–6), the weighting coefficients and precise composition into a single objective are absent. This is the single most significant gap in the paper's methodological contribution and a genuine reproducibility obstacle.

- **The adaptive rule's thresholds and design choices are underspecified.** The IQR module uses thresholds `[t_min, t_max]` that are never given numerical values. The additive combination β = β_IQR + β_RND and the discrete mapping of IQR to {-1, 0, 1} are introduced without sensitivity analysis, ablation, or theoretical justification. No experiment varies these thresholds or tests alternative combination rules (e.g., multiplicative, learned). While the approach is intuitively reasonable, the current treatment makes it impossible to assess how sensitive the results are to these choices.

### Minor

- **Limited set of distributional RL baselines.** The sole distributional baseline is CVaR₀.₅ — a single fixed risk parameter. The paper cites several recent distributional RL methods for legged locomotion (Schneider et al. 2024, Shi et al. 2024, Tang et al. 2019, Long et al. 2024) but evaluates against none of them. Including even one such method would strengthen the case that the adaptive mechanism specifically — rather than other architectural or loss differences — drives the gains. As it stands, the comparison chain (PPO → CVaR₀.₅ → HuRi w/o RND → HuRi) is sufficient for internal validation but does not position the method against contemporary alternatives.

- **Statistical reporting is incomplete.** Table 1 reports success rates without error bars or confidence intervals, despite using multiple seeds and trials. Given that Figure 3 does show 95% CIs and the text states "five random seeds, with each seed repeated 10 times," the data for CIs exists but is not presented in the main comparison table. Some simulation comparisons (e.g., Figure 4 velocity errors) also lack uncertainty quantification.

- **The novelty claim ("first to propose adaptive risk-aware policy learning in humanoid robots") is somewhat overstated.** While the specific combination of IQR + RND for modulating the Wang distortion parameter appears novel, the broader idea of adaptive risk sensitivity for locomotion has precedent in the distributional RL literature the paper itself cites. The claim would be more defensible if rephrased to emphasize the specific technical mechanism rather than claiming priority at the task level.

### Trivial

- Section 3.4's prose refers to "MSE loss to the distorted expectations" — slightly garbled phrasing.
- The abbreviation "stac" appears in the state space description without being defined.
- Table 2's caption uses comparative language ("highest," "lowest") without explicitly naming the compared methods — clarified by the table contents in the original PDF but confusing from the caption alone.

## Nice-to-Haves

- **Multi-terrain evaluation.** The paper acknowledges its limitation to flat terrain. Extending training and evaluation to rough/uneven terrain would substantially strengthen the contribution and address a natural next step.
- **Sensitivity analysis on the `[t_min, t_max]` thresholds** and alternative combination rules for β.
- **A time-series visualization of β during a real-world run** overlaid with physical measurements (tilt angle, foot forces) would make the adaptive behavior more concrete than the current qualitative summary.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"No baseline comparisons in real-world experiments"** (Harsh Critic, Critical Issue 2). — The caption of Table 2 states "our method achieved the highest success rate" and "our approach consistently resulted in the lowest velocity error," and the Strength Finder extracts specific baseline numbers from the table. This criticism is factually inaccurate; the table does contain baseline comparisons.

2. **"Safety considerations... often remain unaddressed" contradicts cited works** (Harsh Critic, Section-by-Section Notes). — The word "often" makes this a reasonable generalization even if some cited works address safety. This is a misreading of the paper's phrasing.

3. **Formatting/notation nitpicks** (Harsh Critic: "Equation (1) missing subscript," "θ_i - Tθ_j where Tθ_j likely means (Tθ)_j," "Z_θ^(τ) is not defined"). — These are parser-induced artifacts or minor notation issues recoverable from context. Not substantive weaknesses.

4. **"Section 5 acknowledgment undermines robustness claim."** — The paper acknowledges a limitation in multi-terrain capability, not in robustness under disturbance. These are orthogonal dimensions. This criticism conflates scope limitation with claim invalidation.

## Novel Insights

None beyond the paper's own contributions. The reviewers converge with the paper's self-assessment: the approach is novel and intuitive, the empirical results in simulation are strong and well-supported by ablations, but the method section has a significant specification gap (missing combined loss function), and the evaluation would benefit from more baselines and statistical detail. The most useful cross-cutting observation is that the underspecified loss function is the primary obstacle — not a flaw in the approach, but a presentation gap that prevents full assessment and reproduction.

## Suggestions

1. **Complete Section 3.4** by providing the full combined loss function with explicit weighting coefficients for each term (quantile energy loss, MSE on distorted expectations, PPO surrogate, entropy). This is the single most impactful revision.

2. **Specify the IQR thresholds `[t_min, t_max]` numerically** and either (a) add a sensitivity analysis showing how results vary across a range of values, or (b) provide a principled (e.g., adaptive normalization) method for setting them.

3. **Add error bars or confidence intervals to Table 1** — the data from multiple seeds and trials is already collected and should be reported.

4. **Consider adding at least one recent distributional RL locomotion method** (e.g., the approach of Schneider et al. 2024, which the paper notes is most similar) as an additional simulation baseline.

5. **Reframe the novelty claim** in the Introduction/Abstract from "first to propose adaptive risk-aware policy learning in humanoid robots" to "first to propose [specific technical mechanism — adaptive IQR+RND risk parameter modulation via Wang distortion] for humanoid locomotion."

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>