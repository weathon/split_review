Now I have thoroughly analyzed the paper. Let me write the consolidated review.

## Summary

The paper proposes ExID, an offline RL algorithm that leverages imperfect domain knowledge (structured as decision trees) to overcome performance degradation in limited-data settings. The key ideas are: (1) a regularization term aligning the critic's Q-values with teacher actions for states covered by domain knowledge, and (2) an adaptive teacher-update mechanism that refines initial heuristics when the critic's actions have higher expected Q-values with lower uncertainty. Evaluation is conducted on OpenAI Gym, MiniGrid, sales promotion, and simglucose datasets.

## Strengths

- **Novel domain-knowledge regularization with adaptive teacher update**: The two-stage mechanism — first regularizing the critic via Eq. 4, then selectively updating the teacher via Cond. 6 and Eq. 7 when the critic is more confident and higher-rewarding — goes beyond simple action blending. The ablation in Fig 5c shows this adaptive update yields higher final reward than warm-start alone or no teacher update on Cartpole, supporting the claim that the teacher can improve beyond initial heuristics.

- **Meaningful average performance improvements**: Across OpenAI Gym environments with 10% partial data, ExID achieves at least 27% average improvement over CQL\_D (the best domain-knowledge-augmented baseline). The real-world Sales Promotion dataset provides a particularly convincing validation — a 10.49% profit increase under genuine (not artificially constructed) data scarcity.

- **OOD-state generalization analysis**: Figure 4 plots the Q-value difference between the learned policy's actions and expert actions for states absent from the reduced buffer. ExID maintains a smaller difference than CQL, providing direct evidence that the regularization helps the critic avoid overestimating OOD actions for states covered by domain knowledge.

- **Clear ablation of hyperparameters and domain-knowledge quality**: Figures 5a–b systematically vary λ and k on Lunar Lander, showing graceful degradation outside the optimal range. Figure 6 demonstrates that even sub-optimal domain knowledge (Rule 3) can recover near-optimal performance after teacher updates, while extremely poor knowledge (Rule 5) harms performance — honestly characterizing boundary conditions.

- **Explicit definition of the limited-data problem**: Definition 4.1 formally characterizes the reduced buffer, and the paper links the failure of standard offline RL in this setting to Theorem 1 of Fujimoto et al. (2019b), providing clear theoretical motivation.

## Weaknesses

### Fatal
None.

### Major

- **Ad-hoc construction of limited-data settings limits generality of results**: The paper defines environment-specific removal rules (Mountain Car: position > −0.8; Cartpole: cart velocity > −1.5; Lunar Lander: angle < −0.04; Minigrid: obstacles on the right) with no systematic variation in data-scarcity levels. There is no sensitivity analysis — e.g., testing at 5%, 10%, 20% removal, or comparing different removal schemes (random masking, low-density state removal, high-reward state removal). Because the method's claimed advantage hinges on handling precisely these missing state regions where domain knowledge applies, the experimental design risks circularity. The real-world SP dataset partially mitigates this concern, but the benchmark results alone are not a reliable test of the method's generality.

- **No error bars or statistical significance measures**: Results are reported as averages over 3 seeds without standard deviations, confidence intervals, or significance tests. Given that gains vary substantially across settings (e.g., large improvements on Mountain Car vs. near-zero gains on Cartpole Expert and Lunar Lander Expert), the reader cannot determine whether reported differences are reproducible or within noise. The claim of "at least 27%" average improvement cannot be properly assessed without variance information.

- **Uneven gains across settings are not adequately discussed**: On Expert datasets, ExID improves dramatically on Mountain Car but shows negligible gains on Cartpole (near ceiling at 500) and Lunar Lander. On Replay datasets, gains are large for Cartpole but zero for Mountain Car. The paper highlights the strongest successes without qualifying the near-zero gains or discussing the patterns behind why ExID helps in some settings and not others. This weakens the claim of "substantial average performance increase" without qualification.

### Minor

- **Problem motivation demonstrated on only one environment**: The claim that SOTA offline RL algorithms "perform sub-optimally when confronted with limited data confined to specific regions" is supported by a single example (CQL on Mountain Car, Fig 1). A broader preliminary study across environments would strengthen the motivation.

- **Domain knowledge representation is restrictive**: The method assumes domain knowledge can be expressed as a small decision tree over state variables. While this works for the tested low-dimensional tasks, the paper does not discuss how "intuitive human-expert insights" in domains like healthcare or robotics would be encoded, nor the effort required. The paper acknowledges this limitation in the conclusion, and Section 5.6 partially addresses it via quality ablation, but the scope of applicable domains remains a significant constraint.

- **Teacher-update ablation only for one environment**: Figure 5c shows the contribution of the adaptive teacher update only for Cartpole. Similar plots for Mountain Car, Lunar Lander, and MiniGrid would strengthen claims about the mechanism's generality.

- **OOD generalization analysis only for Mountain Car**: The Q-value difference analysis (Figure 4) is conducted only for Mountain Car. Results for Cartpole, Lunar Lander, and MiniGrid would be more convincing.

- **Continuous-domain extension mentioned but not evaluated**: The paper states "we extend this to continuous domain" (Sec. 4) but provides no experiments on continuous control tasks (e.g., HalfCheetah, Walker2d). Even a proof-of-concept would help substantiate this claim.

- **Synthetic data quality for teacher training not analyzed**: The teacher is trained on states uniformly sampled over state boundaries, which "may have state combinations that will never occur" (as the paper acknowledges). There is no analysis of how this synthetic data quality affects teacher reliability, nor comparison with alternative generation strategies (e.g., perturbing observed states). The concern is partially mitigated by the fact that regularization applies only to real states, but the teacher's pre-training quality matters.

### Trivial
None that are meaningful beyond formatting.

## Nice-to-Haves

- Test the method under alternative data-deletion schemes (random masking, removal of low-density states, removal of high-reward states) to demonstrate robustness beyond the specific hand-crafted removal rules.
- Include a systematic variation of data-scarcity levels (5%, 10%, 20%) rather than a single fixed level.
- Analyze how the quality of synthetic training data for the teacher affects downstream performance, perhaps by comparing teachers trained on uniform boundary samples vs. perturbed buffer states.
- Expand teacher-update and domain-knowledge-quality ablations to more environments.
- Add a continuous-domain proof-of-concept experiment.

## Removed Points

These points were flagged by reviewers but are removed from the main review (treat with caution):

- **"Algorithm pseudocode is in missing Appendix C"** — REMOVED per instruction: missing appendix content is a parser artifact, not an author error.
- **"References to Appendix A (theoretical implications) cannot be verified"** — REMOVED per instruction: missing appendix sections are parser artifacts.
- **"Uncertainty threshold is not specified — just a comparison of means"** — REMOVED: the condition IS fully specified (Cond. 6) as a comparison of mean uncertainty between critic and teacher actions. A relative comparison is a valid specification; the reviewer wanted an absolute threshold, which is a design choice, not a missing detail.
- **Strength: "Consistent and substantial performance gains across diverse limited-data settings"** — REMOVED due to conflict with verified weakness about uneven/inconsistent gains across settings. Rephrased as "meaningful average performance improvements" in the Strengths section instead.
- **"Missing related works"** — REMOVED per instruction: I cannot verify existence of missing citations without external sources.
- **"Typos/formatting/style nitpicks"** — REMOVED per instruction: parser artifacts and presentation issues are not author errors.
- **Criticism about reproducibility (missing hyperparameters, implementation details)** — REMOVED: hyperparameters are deferred to App. G, which is standard practice. Trivial implementation details are impractical to include in a submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the method that the authors themselves have not articulated.

## Suggestions

1. **Report mean ± std across seeds for all results** and, where meaningful, note whether differences are statistically significant (e.g., via paired tests across seeds). This is essential for the paper's central empirical claim.

2. **Systematize the limited-data construction**. Instead of ad-hoc removal rules per environment, use a principled procedure (e.g., remove states with low visitation density via a density estimate, or randomly mask a controlled fraction of the state space). Report results across multiple removal intensities and types. This would show that ExID's advantage is not an artifact of a specific deletion scheme.

3. **Add a short section or paragraph explicitly discussing the pattern of results** — where ExID helps most, where it helps least, and why. This would turn the uneven gains from a liability into a more informative scientific finding.

4. **Expand the teacher-update ablation to at least 2–3 environments** to demonstrate that the mechanism generalizes beyond Cartpole.

5. **Either add continuous-domain experiments or remove the claim of continuous extension** — a single sentence with no evaluation risks overclaiming.

## Score and Decision

This paper addresses a real and under-explored problem — offline RL with limited data and OOD states — with a sensible mechanism (domain-knowledge regularization + adaptive teacher refinement). The core idea is clearly presented, the real-world Sales Promotion case study is convincing, and the ablations provide useful characterization of the method's behavior. However, the evaluation has two significant weaknesses: the limited-data settings are constructed in an ad-hoc, environment-specific manner that likely biases results in the method's favor, and the lack of error bars makes the reported gains difficult to assess. These issues are addressable but weaken the paper in its current form. The paper would benefit from major revisions focused on a more rigorous experimental protocol.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>