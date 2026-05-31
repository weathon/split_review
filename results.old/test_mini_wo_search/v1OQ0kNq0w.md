Here is my consolidated review.

---

## Summary

MotionRL proposes a multi-reward reinforcement learning framework for fine-tuning text-to-motion generation, jointly optimizing text adherence, motion quality, and human preferences. The key technical contributions are: (1) formulating three complementary reward signals within an RL loop, (2) a batch-wise Pareto-optimal selection strategy that avoids unstable reward-weighted averaging, and (3) learned reward-specific prompt tokens that allow inference-time trade-off control. On the HumanML3D benchmark, the method achieves the best reported R-Precision Top-1 (0.531) and MM-Dist (2.898) among approaches that do not use ground-truth motion length, and also obtains favorable perception-model scores.

## Strengths

- **Novel multi-reward RL formulation for text-to-motion generation.** The paper jointly optimizes three distinct rewards (text adherence, motion quality, and human preferences) within an RL fine-tuning loop, extending prior single-reward RL work (InstructMotion) to a multi-objective setting. The three rewards are defined explicitly in Section 3.1 (Eqs. 3–7), and the ablation in Table 2 confirms that combining all three yields the best overall trade-off (Top-1 0.531, FID 0.064, Perception 0.494).

- **Batch-wise Pareto-optimal sample selection as an alternative to weighted sum.** Instead of manually tuning weights across conflicting objectives, the algorithm selects non-dominated samples within each batch and optimizes only those, addressing the known training instability of multi-reward RL. Algorithm 1 provides a concrete description of the dominance-based filtering, and the approach is well-motivated by reference to prior work on Pareto-set learning.

- **State-of-the-art quantitative performance on the HumanML3D benchmark.** MotionRL achieves the highest R-Precision Top-1 (0.531), Top-2 (0.721), Top-3 (0.811), and lowest MM-Dist (2.898) in Table 1 among all methods that do not use ground-truth motion length, while obtaining competitive FID (0.066) — notably improving over its baseline InstructMotion (Top-1 0.505 → 0.531, FID 0.099 → 0.066).

- **Reward-specific tokens for controlled generation at inference.** The method learns separate prompt tokens for each reward, enabling inference-time control over the text-adherence / motion-quality / human-preference trade-off without manual weight tuning. This is described in Section 2.2 and qualitatively supported by the reward curves in Figure 3 (showing how different tokens shift the model's output).

## Weaknesses

### Fatal
None.

### Major

- **The core Pareto selection claim is not evaluated with standard metrics.** The only evidence supporting the Pareto-optimization claim is Figure 3, which plots reward curves during training. These curves use the same reward functions the model is trained to maximize, so they do not demonstrate improvement on the paper's own evaluation metrics (R-Precision, FID, Perception). The raw numbers in the commented-out table (lines 356–375) suggest a Pareto vs. no-Pareto comparison was planned, but the visible paper contains no table reporting Top-1, FID, or Perception for "ours w/o Pareto" vs. "ours." This is a critical gap because Pareto selection is one of the paper's two core technical contributions; without standard-metric evidence, the reader cannot assess whether Pareto selection actually improves over a simple multi-reward baseline (e.g., weighted sum of rewards in the same RL framework). This weakness directly undermines a central claim and must be resolved for the paper to be accepted.

- **User study is reported without any methodological information.** Figure 2(b) shows a bar chart comparing "Our Success Rate" against a "Baseline Success Rate," with the caption stating "scores given by real human evaluators for the model-generated motions." The paper provides **zero** detail about: number of participants, number of comparisons per participant, which baseline model(s) were compared against, how "success" was defined, whether responses were collected through pairwise preference or Likert-style ratings, or any measure of statistical significance. Without this information, the user study is uninterpretable as evidence for human preference alignment. The claim that "the results demonstrate that our method generates motions that are more consistent with human preferences" is unsupported by the evidence presented.

- **Ambiguity in how the Pareto selection operates across reward-specific token groups.** Section 3.3 (Algorithm 1) samples N motions per reward-specific token (K groups of N samples). The dominance comparison loop (lines 184–195) iterates i=1 to N and j=1 to N, but it is unclear whether this loop operates over all K×N samples (in which case the loop bounds should be K×N, not N) or over each group separately (in which case the Pareto comparison would not capture cross-objective trade-offs across different reward prompts). The notation `r_{ki}` is also ambiguous regarding which sample's reward vector is being compared. This ambiguity affects the reproducibility of the core algorithm and needs to be clarified.

### Minor

- **Reward normalization method is not specified.** The paper states only that rewards were "normalized … to constrain them within the same order of magnitude" (line 161), without describing the normalization procedure (z-score across batch, fixed scaling constants, min-max, or something else). Since the three rewards come from different models with different scales, the normalization method matters for both Pareto dominance comparisons and RL training stability. This detail should be provided for reproducibility.

- **Connection between Pareto selection and PPO loss computation is underspecified.** Algorithm 1 computes the objective `J_r` from Pareto-selected samples and then says "Update π_θ using Proximal Policy Optimization (PPO)." The standard PPO actor loss (Eq. 8) uses advantage functions computed from a critic. It is not explained whether advantages are computed only for Pareto-selected samples or for all K×N samples, nor how the Pareto objective `J_r` and the PPO loss interact (e.g., does `J_r` replace the PPO actor loss, or is it added?). A clear computational graph connecting Pareto selection → advantage estimation → loss computation would resolve this.

- **Motion quality reward uses ground-truth motion, with no discussion of overfitting risk.** Equation (5) defines `r_m` as a distance to the ground-truth motion embedding for the same text prompt. If RL fine-tuning uses the same HumanML3D training split used for supervised pretraining, this reward could encourage memorization of the training motions rather than genuine quality improvement. The paper does not clarify whether this reward is computed on held-out data or the same training set, nor does it discuss this limitation.

### Trivial
None.

## Nice-to-Haves

- Reporting confidence intervals or standard deviations for the main quantitative results (Table 1) and the reward ablation (Table 2), as some metric values are very close.
- Ablation on the batch size N (number of samples per token) and number of reward-specific tokens K, to show sensitivity of the Pareto selection.
- A discussion of the computational cost of generating K×N motions per training iteration.
- A limitations section addressing potential overfitting to the perception model, sensitivity to reward scaling, and the scope of the method.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Claim that novelty claim is overstated ("InstructMotion already uses RL").** The paper's novelty claim is specifically about *multi-reward* RL with Pareto selection, not RL itself. InstructMotion uses single-reward RL for text adherence only. The paper states "the first approach to utilize Multi-Reward Reinforcement Learning" — this is defensible and not an overstatement. *Removed: factually inaccurate criticism.*

- **Criticism of the commented-out table values (5.23, 5.31) as "clearly out of range."** This table is in a `\begin{comment}` block and is not presented in the paper. The values are typographical placeholders or formatting artifacts from the LaTeX source extraction, not author errors. *Removed: commenting on non-visible content due to parser artifact.*

- **Missing code release / reproducibility complaints.** These question the existence of materials not required for review. *Removed: violates hard rule.*

- **Missing related work.** As per policy, I do not have external sources to verify omissions. *Removed per instruction.*

- **Formatting/style nitpicks and typo complaints.** Parser artifacts, not author errors. *Removed per instruction.*

## Novel Insights

Beyond the paper's own contributions, a notable observation emerges from comparing the strengths and weaknesses: the method shows a clear tension between achieving strong results on automatic metrics (Table 1) and providing rigorous evidence for the specific algorithmic novelties (Pareto selection, human preference alignment). The R-Precision improvements are genuinely competitive and well-documented, but the paper's signature components — which are what distinguish it from a straightforward RL fine-tuning of InstructMotion — lack the same evidentiary standard. This pattern suggests the method may ultimately work well even without the Pareto machinery (i.e., the gains may come primarily from the multi-reward signal), or conversely that Pareto selection is crucial but the current evaluation does not prove it. Resolving this tension would significantly strengthen the contribution.

## Suggestions

1. **Provide a proper Pareto ablation table** comparing "ours w/o Pareto" (e.g., using weighted sum of the three rewards, or training on all samples without filtering) vs. "ours" on the same metrics as Table 1 (Top-1, FID, Perception, MM-Dist), with standard deviations.
2. **Report full user study methodology:** number of participants, number of comparisons, which baselines, how "success" was defined, raw win/loss counts, and a significance test (p-value or confidence interval).
3. **Clarify Algorithm 1:** state explicitly whether the dominance check runs over K×N samples (with corrected loop bounds) or per reward-token group. Clarify how `r_{ki}` indexes samples across groups. Describe how Pareto-selected samples feed into the PPO advantage and loss computation.
4. **Specify the reward normalization method** and discuss whether the motion quality reward uses held-out data or training data (and the associated overfitting risk).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>