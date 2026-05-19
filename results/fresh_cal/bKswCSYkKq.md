Let me proceed to write the final consolidated review based on my thorough analysis of the paper.

---

## Summary

This paper addresses the stability-plasticity dilemma in deep reinforcement learning by proposing NBSP, a method that (1) identifies "RL skill neurons" via a goal-oriented correlation score between neuron activation patterns and task success/failure, and (2) freezes these neurons via gradient masking combined with experience replay during new-task learning. Experiments on Meta-World (4 task pairs) and Atari (4 game pairs) show that NBSP retains prior task performance while learning new tasks, outperforming EWC, ANCL, and an importance-based variant. An ablation reveals that applying the method to the critic network contributes more to the balance than applying it to the actor.

## Strengths

- **First neuron-level method addressing both stability and plasticity simultaneously in DRL.** The paper explicitly positions itself at a finer granularity than prior network-level methods (EWC, ANCL), and the claim is well-supported by the related work survey (§2, §3.2). This is a genuinely novel framing.

- **Consistent empirical advantage across all evaluated task pairs.** On all four Meta-World task pairs, NBSP achieves near-1.0 success rates on both the first and second tasks, while baselines (EWC, ANCL, Importance-based NBSP) fail on at least one task for most pairs. The pattern replicates on four Atari game pairs, demonstrating generalization across discrete and continuous action spaces (Fig. 4, Fig. 7, §4.2, §4.4).

- **Ablation cleanly isolates the contribution of gradient masking vs. experience replay.** Figure 5 (§4.3) shows that the replay-only variant retains some knowledge but degrades, while NBSP (masking + replay) achieves the best balance. This disentanglement strengthens the claim that neuron-level gradient masking on skill neurons is essential.

- **Actor-critic dissection provides actionable insight for future research.** Figure 6 (§4.3) shows that NBSP-Critic outperforms NBSP-Actor in knowledge retention, and only the full NBSP achieves optimal balance. The paper offers a mechanistic explanation grounded in actor-critic training dynamics (critic updates are recursive with target networks; actor updates depend on the critic). This is a useful secondary contribution beyond the method itself.

## Weaknesses

### Fatal

None.

### Major

- **Missing a control: the identification method is not validated against random neuron selection.** The core novelty is identifying RL skill neurons via a goal-oriented score (Eq. 4), but the paper never compares against a baseline that freezes a randomly selected set of neurons of the same size. The comparison against Importance-based NBSP (which uses weight-magnitude importance) shows that the goal-oriented metric differs from importance-based selection, but it does not rule out the possibility that *any* fixed subset of frozen neurons would achieve similar results. Without this control, the claim that the goal-oriented identification is essential is incompletely supported. (*Evidence: §3.2 describes the identification method; §4.2 compares to Importance-based NBSP only.*)

- **Incomplete reporting of the actor-critic ablation.** The paper shows the actor-critic ablation (Figure 6) for only two of the four Meta-World task pairs while stating "for most task pairs, such as <drawer-open, drawer-close> and <window-open, window-close>…" (§4.3, line 160), implying additional results were collected but not presented. Without seeing all four pairs, the robustness of the finding that "the critic plays a more critical role" cannot be fully assessed. This is an evidentiary gap, not a minor omission.

- **The "significantly outperforms" claim lacks statistical support.** The paper states that NBSP "significantly outperforms existing approaches" (abstract, conclusion), yet no statistical significance tests (e.g., paired bootstrap, Mann-Whitney U) are reported. Several error bars in the figures (Figs. 4, 7) show noticeable overlap between conditions. With only 5 seeds per condition, the evidence is suggestive but does not meet the standard implied by "significantly." At minimum, final success rates/returns with standard errors should be tabulated for all conditions. (*Evidence: abstract line 4, §4.2, §4.4; no p-values or confidence intervals appear in the paper.*)

### Minor

- **Baseline hyperparameter tuning is not discussed.** EWC and ANCL were originally designed for supervised continual learning. The paper adapts them to DRL but provides no evidence that their hyperparameters (e.g., regularization strength for EWC, auxiliary network architecture for ANCL) were tuned for the RL setting rather than carried over from classification. This does not invalidate NBSP's empirical advantage (which is consistent across all pairs), but it tempers the confidence one can place in the absolute strength of the "outperforms" claim, since suboptimally tuned baselines could systematically underperform.

- **The Atari identification procedure is underspecified.** For Atari, the evaluation criterion is "based on the return over an episode" (line 64), which is a continuous value. The identification method (Eqs. 1–4) binarizes activations and evaluation criteria relative to their means. It is not explained how the continuous episode return is converted into the binary indicator needed for Eq. (3) — e.g., whether the return at each time step is compared to the mean, or whether an episode-level binarization is used. This affects the reproducibility of the Atari experiments. (*Evidence: §4.4, line 169; §3.2, Eqs. 1–4.*)

### Trivial

- The claim that "average success rates approach 1.0" (line 137) is slightly optimistic — for example, Figure 4(c) shows NBSP plateauing around 0.9 rather than 1.0.

## Nice-to-Haves

- Adding a random-neuron baseline would substantially strengthen the core claim about the identification method.
- Reporting final performance in a table (with standard errors) across all conditions and running statistical tests would directly support the "significantly outperforms" language.
- Including the two missing task pairs in the actor-critic ablation (Figure 6) would remove a concern about selective reporting.
- A brief limitations section acknowledging the correlation-based identification, the limited number of task pairs, and the scope of claims would improve the paper's intellectual honesty.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper never specifies how many RL skill neurons are selected or how the threshold is set"** — The parser strips appendix sections from all papers; these details (e.g., top-k percentage, threshold value) would have been specified in the original submission's appendix and are absent only due to parsing. The main paper states "the number of RL skill neurons varies depending on the complexity of the task" (line 79), which is consistent with an appendix providing the concrete rule.
- **"Missing related work discussion (CLEAR, RAR, Progress & Compress)"** — Per the meta-reviewer instructions, missing related works cannot be raised because the reviewer has no external sources to confirm their existence.
- **"Axis ranges differ across figures (Figure 4c has y-axis from 0 to 1, others from 0 to 1.0)"** — Pure formatting nitpick. The parser strips formatting; the original submission does not have these issues.
- **"No hyperparameters given (learning rate, batch size, etc.)"** — The paper references CleanRL's SAC implementation (line 117), providing the standard baseline configuration. NBSP-specific parameters (interval k, neuron selection details) would be in the appendix per the above point.
- **"The method is not validated as causal"** — The paper never claims causal identification of skill neurons; it proposes a correlation-based score, which is an appropriate level of claim for an empirical method paper. The relevant experimental concern (missing random baseline) is retained as a Major weakness above.

## Novel Insights

The integration of the harsh critic's articulation of the missing-evidence gaps with the strength finder's documentation of the paper's concrete achievements produces a clear picture: the paper's core idea (neuron-level gradient masking based on goal-correlated neurons) is genuinely novel, well-motivated, and yields consistently positive results across two benchmarks. However, the evidentiary framework has specific holes that prevent the paper from fully substantiating its strongest claims. The most interesting tension is between the paper's framing of the neuron identification as a key contribution and the missing control (random masking) that would directly test whether the identification matters beyond any fixed neuron freeze. The actor-critic finding is the paper's most robust secondary contribution, as it comes with both empirical evidence and a mechanistic rationale tied to the structure of actor-critic algorithms.

## Suggestions

1. Add a random-neuron masking baseline to directly validate that the goal-oriented identification method adds value over an arbitrary fixed neuron freeze of the same size.
2. Report final success rates/returns with standard errors in a table for all conditions, and include statistical significance tests (e.g., paired bootstrap) to support the "significantly outperforms" claim.
3. Complete the actor-critic ablation by presenting results for all four Meta-World task pairs, not just two.
4. Clarify the Atari identification procedure: how is the continuous episode return mapped to the binary indicator in Eq. (3)?
5. Disclose the concrete rule for selecting RL skill neurons (top-k percentage or score threshold) and the interval k for experience replay, if not already in the appendix.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>