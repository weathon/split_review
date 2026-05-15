Now I have a complete picture. Let me cross-check each reviewer claim against the paper and produce the final consolidated review.

---

## Summary

This paper proposes a method for improving generalization in RLHF by introducing group invariant learning. It automatically discovers data groups via a classifier trained to maximize variance of group returns (adversarial group discovery), then optimizes the policy to minimize that variance. An adaptive KL penalty further adjusts regularization strength per inferred group. Experiments on Llama 2 7B across harmfulness, helpfulness, and summarization tasks show consistent improvements over SFT, PPO, PPO+KL, and DPO, with both GPT-4 and human evaluation.

## Strengths

- **First application of group invariant learning to RLHF without requiring group annotations.** The paper adapts the adversarial group discovery framework (building on Creager et al., V-REx) specifically to the RL setting, where the data distribution shifts as the policy updates. The method automatically distinguishes challenging from easy data (Figure 2, left panels) and narrows the performance gap between groups (right panels), which is qualitatively demonstrated.

- **Adaptive KL penalty that adjusts regularization per inferred group.** Equation 8 scales the KL penalty by the probability of belonging to the highest-performing group, allowing more exploration on hard groups and tighter constraints on well-performing groups. The ablation study (Table 2) confirms this component contributes on top of the group invariant learning term, and the training curves (Figure 3) show better reward per unit of KL divergence.

- **Thorough evaluation including both in-distribution and out-of-distribution tests with human validation.** The paper evaluates on three datasets (Anthropic-Harmful, Anthropic-Helpful, OpenAI-Summary) using both GPT-4 and human evaluators, with good consistency between the two. OOD generalization is tested on PKU-SafeRLHF and CNN Dailymail. The main results table (Table 1) provides full win/tie/lose percentages across all comparisons.

- **Ablation analysis isolating each component's contribution.** Table 2 compares the full method against variants without group invariant learning and without dynamic KL, showing that GIL provides the primary gain while dynamic KL adds a secondary boost.

## Weaknesses

### Fatal
None.

### Major
None that rise to the level of undermining the paper's core claims or methodology.

### Minor

- **The transition from soft assignments to group-return computation is underspecified.** The paper introduces a classifier producing soft assignments \(p_\phi(g|\tau)\) (line 198) and states it "replaces manual group division with a probability distribution," yet the group-return equation (Eq. 3) uses a hard indicator \(\mathbbm{1}\{g_{\tau_i}=g\}\). Exactly how \(R_g(\theta)\) is computed from soft probabilities—whether via weighted averaging, argmax, or some other aggregation—is never stated. While a reader familiar with Creager et al. (2021) can infer a reasonable implementation (soft-weighted averaging), the omission means the optimization objective in Eq. 4 is not fully specified as written. The authors should clarify this in a revision.

- **The "highest-performing group" used in the adaptive KL is not formally defined.** Equation 8 uses \(p_\phi(g_{\text{high}}|x,y)\), but the paper never specifies how \(g_{\text{high}}\) is identified—whether it is the group with the highest current average return, the group with the steepest recent improvement, or something else. This makes the adaptive penalty procedure ambiguous.

- **OOD results are only presented in bar charts without numerical values.** The OOD evaluation (Figure 2) is reported as win/tie/lose bar charts but the precise percentages are not given in a table or the caption. The only concrete number referenced in the text is a single comparison ("reduces the rate of losing to PPO from 32.2% to 12.8%" in one setting). Providing the full numerical breakdown for all OOD comparisons would allow readers to verify the claimed "increased probability of winning."

- **The adaptive KL penalty's safety implications are not analyzed.** The paper correctly notes that relaxing the KL penalty on "hard" groups encourages exploration on challenging data (lines 247–249). However, the standard justification for the KL penalty in RLHF is precisely that the reward model is unreliable far from the SFT distribution. The paper does not analyze whether the reward model remains accurate for outputs generated under the relaxed constraint, nor does it provide any safeguard against reward hacking on these groups. An analysis of reward-model reliability per inferred group would strengthen this contribution. (The ablation does show a modest gain—approximately 5% win rate increase on Harmful, 4% on Helpful—which partially mitigates the concern.)

### Trivial

- The paper's "first attempt to introduce group invariant learning into RL" claim (line 83) is qualified with "to the best of our knowledge" and is specific to *group invariant learning* (unsupervised group discovery + invariant learning), not invariant learning in general. This is accurate but the phrasing may invite unnecessary debate; a softer formulation would be prudent.

- Figure 2 in the OOD section is referenced as "Figure 2" in the caption but the label `\label{fig:ood_evalation}` is used; the main text refers to it correctly.

## Nice-to-Haves

- **Validation of what the inferred groups represent.** The paper shows that the two inferred groups have different reward dynamics (Figure 2) but does not analyze whether these correspond to interpretable categories (e.g., topic, length, difficulty). Such analysis would strengthen the mechanism story.

- **Comparison against distributionally robust or risk-sensitive RL baselines** (e.g., CVaR optimization, group DRO adapted to RL) would further contextualize the method's contribution to robust generalization. However, the paper's primary scope is introducing group invariant learning to *RLHF*, and the standard RLHF baselines (SFT, PPO, PPO+KL, DPO) are the most directly relevant. The absence of DRO/CVaR comparisons is not a flaw in the paper as written, but adding them would strengthen it.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No comparison against robust or distributionally robust RL baselines"** — Demands comparisons (CVaR, DRO, IRM for RL) outside the paper's stated scope. The paper's contribution is bringing group invariant learning to the RLHF pipeline, and the relevant baselines are the standard RLHF methods (SFT, PPO, PPO+KL, DPO), all of which are included. The paper mentions DRO in related work but does not claim to outperform it. This is scope creep.

- **"Overstatement: first attempt to introduce group invariant learning into RL"** — The paper qualifies this claim with "to the best of our knowledge" and specifically says "group invariant learning" (unsupervised group discovery + invariant learning), which is distinct from prior work on IRM for RL where groups must be known. The criticism misunderstands the specific claim being made.

- **"PPO without KL is an unfair opponent"** — The paper includes PPO w/ KL as a baseline and the method is compared against it on equal footing. PPO without KL is included for completeness and the paper explicitly notes (line 338) that PPO becomes unstable without regularization. This is not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface clarity issues (soft-to-hard assignment, definition of "highest-performing group") that the authors should address, but do not introduce fundamentally new observations about the method or results.

## Suggestions

1. **Clarify the soft-to-hard assignment transition.** Specify whether \(R_g(\theta)\) is computed via soft-weighted averaging using \(p_\phi(g|\tau_i)\) as weights, or via a hard argmax. A one-sentence statement would resolve the ambiguity.
2. **Define "highest-performing group" explicitly.** State whether \(g_{\text{high}}\) is identified by the group with the highest current average return, or by some other criterion.
3. **Add a table with numerical OOD win/tie/lose percentages.** The bar charts are helpful for visualization but a supplementary table with exact numbers would support verifiability.
4. **Include a brief analysis of reward-model accuracy across inferred groups**, especially for the groups where the KL penalty is relaxed, to address the safety concern.
5. **Consider adding a sensitivity analysis on the number of groups \(M\)** (currently binary, following Creager et al.). Even a brief note on whether performance is sensitive to this choice would be informative.

## Score and Decision

The paper proposes a novel and well-motivated method (group invariant learning + adaptive KL for RLHF), provides reasonably thorough experiments across multiple tasks with both automatic and human evaluation, and includes ablation analysis. The core claims are supported by evidence. The main weaknesses are clarity issues in the method specification (soft-to-hard assignment, definition of "highest-performing group") and the OOD results being presented without numerical values. None of these undermine the paper's contribution, but they should be addressed in a revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>