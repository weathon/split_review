Now let me write the final consolidated review.

## Summary

This paper proposes DrS (Dense reward learning from Stages), a method that learns dense, *reusable* reward functions for multi-stage tasks by training discriminators to classify success vs. failure trajectories (rather than agent vs. demonstration trajectories as in standard AIL). For multi-stage tasks, a separate discriminator is trained per stage, and the outputs are combined via a provably monotonic formula (Eq. 5) that preserves stage ordering. The learned rewards are transferred to unseen test tasks within the same task family. The method is evaluated on three ManiSkill task families totaling 1000+ task variants, and the learned rewards enable successful RL training on held-out test objects — substantially outperforming semi-sparse rewards, VICE-RAQ, and ORIL baselines.

## Strengths

1. **Principled departure from AIL's non-reusability problem.** The paper correctly identifies why AIL/GAIL rewards are not reusable (lines 28–30): at convergence the discriminator outputs ½ for both agent and demonstration trajectories. By re-targeting the discriminator to classify *success vs. failure* trajectories using the sparse reward as supervision, the positive/negative gap remains intact throughout training (Section 4.1, line 165). This is a clean, well-motivated departure from prior work that directly addresses a known limitation.

2. **Large-scale reward reuse evaluation on 1000+ task variants.** DrS is evaluated across three ManiSkill task families with non-overlapping train/test objects: Pick-and-Place (74 train / 1600 test), Turn Faucet (10/50), and Open Cabinet Door (4/6) (Section 5.1, lines 271–285). This is the most extensive evaluation of reward reusability I am aware of — most reward learning papers evaluate on at most a handful of tasks, not hundreds or thousands of variants.

3. **Learned rewards enable successful reuse where baselines completely fail.** DrS rewards consistently outperform semi-sparse, VICE-RAQ, and ORIL across all three task families (Fig. 3, line 296–297). VICE-RAQ and ORIL achieve zero success in reward reuse, establishing a clear floor that DrS surpasses.

4. **Systematic ablation demonstrating robustness to stage configuration.** The paper varies the number of stages (3→2→1) and stage definition thresholds (2.5cm→5cm→10cm) (Section 5.4.1, lines 316–328). Two-stage variants still succeed; threshold changes within a reasonable range do not significantly affect performance. This addresses the practical concern that the approach might be brittle to stage design choices.

5. **Provably monotonic reward combination.** Eq. 5 (line 195) combines the semi-sparse stage index with a tanh-bounded discriminator output, and the paper proves that any α < ½ ensures that "the reward of a state in stage k+1 is always higher than that of stage k." This theoretical property ensures the learned reward never mis-orders stages, which is important for incentivizing correct task progression.

6. **Policy fine-tuning shows benefits beyond training-from-scratch.** Section 5.4.2 (lines 330–336) shows that fine-tuning the byproduct policy from the reward learning phase using DrS rewards yields better final performance than fine-tuning with the human-engineered reward. This demonstrates that the learned reward captures useful structure that even a well-designed human reward may miss.

## Weaknesses

### Fatal

None.

### Major

1. **The 1-stage collapse is reported but not analyzed, leaving the claimed mechanism underspecified.** The ablation study (Section 5.4.1, lines 320–323) shows that DrS with a single stage *completely fails* on test tasks. The paper mentions this only in passing: "when reducing the number of stages to 1, the learned reward failed to train RL agents in test tasks, demonstrating the benefit of using more stages." However, Section 4.1 frames success/failure classification as the key innovation that resolves AIL's non-reusability — stating that because "the gap between them remains intact and does not shrink" (line 165), the reward is reusable. If that mechanism were sufficient, the 1-stage version should work at least partially. Its total failure suggests that the stage decomposition is not merely helpful but *essential*, and that success/failure discrimination alone (over the full task horizon) is too weak. The paper does not analyze *why*: is it because positive data becomes too rare over long horizons? because the discriminator overfits? because the signal-to-noise ratio degrades? Without this analysis, there is genuine ambiguity about what DrS actually contributes — is it the success/failure re-targeting, the stage decomposition, or the combination? The paper's framing emphasizes the former, but the evidence points to the latter being the operative mechanism. This does not invalidate the contribution (the multi-stage method clearly works), but it obscures what the core insight is and when the method can be expected to apply.

### Minor

1. **"Comparable to human-engineered rewards" is imprecisely stated.** The paper claims in the abstract (line 8) that learned rewards "achieve comparable performance to human-engineered rewards on some tasks," and in Section 5.3 (line 298) specifies this for Pick-and-Place and Turn Faucet. However, even on those tasks, the description of Fig. 3 suggests the gap is non-trivial, and on Open Cabinet Door the gap appears substantially larger. "Comparable" is doing too much work; quantifying the gap precisely (e.g., "within X% of human-engineered on Y tasks") would better serve the reader and avoid the impression of overclaiming.

2. **The GAIL reward non-reusability comparison is deferred to the appendix.** A core distinguishing argument of the paper (Section 4.1, lines 161–163) is that GAIL-style discriminators produce non-reusable rewards while DrS's do not. Yet the direct experimental comparison — taking a GAIL discriminator trained on the same data and attempting to reuse it — is only listed as an ablation referenced to the appendix (line 341: \ref{sec:basic_ablation}). Since this contrast is the paper's primary differentiating argument from the AIL literature, a quantitative result in the main paper would significantly strengthen the narrative.

3. **No analysis of what the discriminator actually learns.** The paper treats the learned reward as a black box evaluated solely through downstream RL performance. There is no analysis of reward quality (does the discriminator correlate with ground-truth task progress?), discrimination accuracy, or potential failure modes (e.g., does it assign high reward to out-of-distribution states from test objects?). While downstream performance is the most important metric, some diagnostic analysis would help build confidence in the method.

4. **No sensitivity analysis for α (the reward combination weight).** The paper sets α = ⅓ with a brief justification that α < ½ ensures stage ordering (line 195). Since α determines how much the dense discriminator term can modulate the reward within a stage, showing its sensitivity (or lack thereof) would strengthen the robustness claims.

### Trivial

None.

## Nice-to-Haves

- A discussion of whether DrS rewards face similar exploitation risks to offline-learned rewards (the paper discusses this for ORIL at lines 304–305 but not for DrS) when test-task states fall outside the training distribution.
- Statistical significance tests for the gap between DrS and human-engineered rewards on Pick-and-Place and Turn Faucet.
- Analysis of the data imbalance issue (later-stage discriminators have progressively fewer positive trajectories, as fewer trajectories reach those stages during initial exploration).
- VICE-RAQ failure mechanism analysis (the paper offers a plausible hypothesis at line 303 but acknowledges it as speculation).

## Removed Points

The following points raised by reviewers were removed after verification against the paper:

- **"ORIL is an offline method... stacking the deck"** — ORIL is a natural baseline (both methods use classification-based rewards from demonstrations). The paper acknowledges the difference and the comparison is informative.
- **"The method requires training a separate task-specific RL agent from scratch... unmentioned limitation"** — This is explicitly described as the reward learning phase in Algorithm 1 and Section 4; it is not an unmentioned limitation.
- **"Formatting/style concerns" and "appendix/proof missing" points** — The appendix sections referenced in the paper (e.g., \ref{sec:pcd}, \ref{sec:basic_ablation}, \ref{sec:reward_formula}) are stripped by the parser; they exist in the original submission per standard policy.
- **"One underspecified detail: trajectory assignment leads to data imbalance"** — The trajectory assignment procedure (Algorithm 1, lines 222–224) is clearly specified. The data imbalance is a natural consequence acknowledged by the method design, not an oversight.

## Novel Insights

The most instructive tension in the reviews is between the paper's framing (Section 4.1: success/failure classification is the key innovation that solves AIL's non-reusability) and the empirical fact that the single-stage version fails entirely. The reviews collectively surface that this gap is not adequately addressed. A deeper reading of the paper suggests that the *combination* of two mechanisms is what makes DrS work: (a) the success/failure re-targeting prevents the convergence collapse that plagues AIL rewards, and (b) the stage decomposition shortens the effective horizon so that each discriminator faces a tractable classification problem with a reasonable ratio of positive to negative data. The paper's own framing overweights (a) at the expense of (b), and the 1-stage failure is the clearest indicator that (b) is doing heavy lifting. Recognizing this dual mechanism would both sharpen the paper's contribution and provide clearer guidance to practitioners about when DrS can be expected to work.

## Suggestions

1. **Analyze the 1-stage failure.** Even a brief investigation (e.g., discriminator loss curves, positive/negative data ratios, reward values during training for the 1-stage vs. multi-stage case) would clarify the mechanism and substantially strengthen the paper. Is the failure due to data imbalance, horizon length, exploration difficulty, or something else?

2. **Quantify the "comparable to human" claim.** Replace "comparable" with specific numbers (e.g., "within 5% of human-engineered success rate on Pick-and-Place and Turn Faucet, but 40% lower on Open Cabinet Door"). This would be more informative and more honest.

3. **Move the GAIL reward reuse comparison to the main paper** (or at minimum summarize the key result). Since distinguishing from AIL is the paper's central differentiating argument, readers need to see the empirical contrast.

4. **Add a brief analysis of discriminator behavior** — e.g., does the discriminator output correlate with task progress? Are there systematic failures on certain test objects?

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>