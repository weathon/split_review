I now have a thorough understanding of the paper and can verify each claim. Let me write the consolidated review.

---

## Summary

This paper proposes UGDA (Uncertainty-Gradient based Data Augmentation), a method for refining reward models in RLHF by selectively augmenting training data with on-policy interaction samples. UGDA operates in three stages: (1) training reward LoRA ensembles for uncertainty estimation, (2) selecting the most uncertain and gradient-influential samples from policy interaction data, and (3) relabeling those samples using an expert (GPT-4 or human) and retraining the reward ensembles with an MSE regression loss. Experiments on the HH dataset with Gemma-2B/7B reward models show consistent improvements over baselines across multiple evaluation metrics (Table 2, Figure 2-3).

## Strengths

1. **Novel two-stage data selection combining uncertainty and gradient influence**: The paper proposes a principled pipeline that first filters by reward ensemble variance (uncertainty) and then by Adam influence (gradient-based). The ablation study (Figure 4) shows that removing either component (UGDA-UN or UGDA-GR) hurts performance, and random selection (UGDA-RA) also underperforms the full method. This confirms that both selection criteria and their combination contribute meaningfully.

2. **Consistent empirical gains across diverse evaluations**: UGDA achieves the best Avg_Reward and Var_Reward on both helpful and harmless test settings for Gemma-2B and Gemma-7B reward models (Table 2). It also outperforms baselines on GPT-4 pairwise comparisons (Figures 2, 5) and on AlpacaEval, Arena-Hard, and MT-Bench (Figure 3). The improvements hold across multiple metrics and evaluation protocols.

3. **Robustness to noisy preference data**: In experiments with 20% flipped preference labels (Table 3, Figure 5), UGDA degrades less than baselines and still wins GPT-4 comparisons. This demonstrates practical robustness beyond the clean-data setting.

4. **Efficient use of interaction data**: By setting both selection thresholds to 0.5, only ~25% of the collected interaction data is used for reward model refinement, yet performance improves over full-data baselines. This suggests the selection mechanism is genuinely identifying valuable samples.

## Weaknesses

### Fatal
None.

### Major

1. **The gradient influence validation set is drawn from the original preference distribution, not the policy distribution, undermining the "policy-aware" claim.** The paper states the validation set for gradient-based selection uses "the instruction and chosen responses from the test sets of two subtasks (i.e., helpful and harmless)" (Section 5.1), which are from the original HH dataset — the same distribution as the initial preference data. However, the samples being selected are from the **policy interaction distribution**. The paper claims the influence score measures "influential data for policy optimization" (Section 1), but it is actually measuring influence on the original validation set. No argument is given that influence on the original distribution transfers to influence on the shifted policy distribution. This gap makes the gradient selection step less principled than the paper's framing suggests. A validation set drawn from held-out policy interaction samples would be more directly relevant.

2. **The contribution of the expert relabeling vs. the data selection mechanism is not fully disentangled.** The paper's core framing is about solving the off-distribution problem by selecting on-policy samples. However, the relabeling step introduces a stronger supervisor (GPT-4) as the source of training targets. The ablation study (Figure 4) does show that selection (UGDA) outperforms random selection with the same expert relabeling (UGDA-RA), which partially addresses this concern. However, there is **no ablation that replaces the expert with the proxy reward model's own scores** — i.e., using the same selected samples but with the reward model's own predictions as training targets. Without this, it is impossible to know whether the method would provide any benefit in the setting the paper claims to address (where no stronger expert is available). The method as presented is at least partly a knowledge distillation pipeline, and the paper does not acknowledge this.

### Minor

1. **Baseline descriptions are ambiguous.** The paper states "for the baselines, without loss of generality, we conduct experiments by randomly select 25% of the interaction data with GPT-4 annotator for the reward model refining" (Section 5.1). It is unclear which baselines this applies to. PPO, LCB, and UWO do not normally involve retraining the reward model on interaction data; if the authors modified these methods to include such retraining, this should be explicitly stated and justified. Only RLR (Reward LoRAs Retraining) clearly involves retraining. This ambiguity makes the main results (Table 2, Figures 2–3) harder to interpret than they should be.

2. **The switch from pairwise preference loss to MSE regression loss is not justified, and no comparison to alternatives is provided.** The initial reward model is trained with a Bradley-Terry pairwise preference loss (Equation 1), but the refining stage uses MSE loss on absolute scores (Equation 14). The paper provides no argument that this regression objective preserves or improves the reward model's ranking ability — which is what matters during PPO. No comparison is made to using the same pairwise loss with the relabeled samples. This weakens the methodological narrative.

3. **The quantile projection (Equation 13) is underspecified.** The paper writes `Quantile_5(R_i^PPO(x,y), j)` but does not state what data distribution the quantiles are computed over. If computed over the interaction dataset itself, this creates circularity — the reward model's own predictions define the target values. This must be clarified.

4. **No sensitivity analysis for the selection thresholds.** Both thresholds are set to γ=0.5 and η=0.5, yielding a 25% subset. No analysis is provided showing how performance varies with different thresholds or subset sizes. This is important for understanding the method's sensitivity.

5. **GPT-4 pairwise comparisons are partially circular.** Since GPT-4 is used both as the relabeling expert during training and as the judge for pairwise comparisons (Figures 2, 5), these evaluations may favor UGDA simply because the reward model was trained to match GPT-4's preferences. The paper partially mitigates this by also evaluating with Llama2-13B (Table 2) and on instruction-following benchmarks (Figure 3), but it does not discuss this circularity or include a fully independent evaluation (e.g., human evaluation).

### Trivial

- The paper does not discuss the computational overhead of the gradient influence computation (requires storing gradients for all interaction samples at multiple checkpoints), nor compare it to the cost of simpler baselines.

## Nice-to-Haves

- An ablation that replaces the expert (GPT-4) relabeling with the proxy reward model's own scores (or a simple baseline like training on all interaction data with GPT-4 labels). This would cleanly isolate the data selection contribution from the expert supervision contribution.
- Sensitivity analysis on the threshold parameters γ and η.
- A comparison between MSE loss and pairwise preference loss for the refining stage.
- Discussion of when the expert (GPT-4) might be biased or unreliable, and how the method behaves in that case.

## Removed Points

These points from the reviews are excluded or downgraded for the following reasons:

- **"The paper does not report results on other datasets (e.g., Reddit TL;DR)"**: Scope creep — a paper can focus on one primary dataset without being evaluated on every possible domain. Removed.
- **"The writing quality is poor, with frequent grammatical errors"**: These are likely parser artifacts or minor presentation issues irrelevant to the technical contribution. Removed per hard rules.
- **"If the expert were unavailable, UGDA would have no way to correct off-distribution errors"**: Re-framed as a missing ablation (see Major Weakness 2) rather than a structural flaw. The paper does show selection + expert > random + expert, so the selection mechanism adds value; the missing piece is a no-expert baseline.
- **"The results may be an artifact of aligning to GPT-4"**: The paper also evaluates with Llama2-13B (Table 2) and on instruction-following benchmarks (Figure 3), which provides some independent validation. Downgraded to Minor (point 5).
- **"The ablation study does not ablate the expert relabeling itself"**: Accurate criticism, kept in Major Weakness 2 but rephrased to acknowledge that the UGDA-RA baseline partially addresses this.
- **"The gradient influence computation requires storing gradients... computationally heavy"**: A valid observation but not a weakness of the contribution itself. Downgraded to Trivial.

## Novel Insights

The reviews collectively surface an interesting tension: the paper's most compelling evidence (Table 2's Llama2-13B evaluation and Figure 3's benchmark results) does not use the same model (GPT-4) that served as the relabeling expert, suggesting the gains are not purely an artifact of distillation-oriented alignment. Yet the paper's own framing — "solving off-distribution" — is somewhat at odds with what the method actually does: selective knowledge distillation from a stronger model onto on-policy samples. The most interesting question neither the paper nor the reviews fully resolve is whether the selection mechanism would still yield improvements if the expert were replaced by a weaker but still reasonable signal (e.g., the ensemble's own mean score), which would test whether the core contribution is the selection or the supervision source. This is a clean experiment for future work.

## Suggestions

1. **Clarify the validation set for gradient influence computation** by using held-out policy interaction samples rather than the original test set, or provide a theoretical/empirical justification for why influence on the original distribution transfers.
2. **Add an ablation using the proxy reward model's own scores** (with the same selected samples) to separate the effect of data selection from the effect of stronger supervision.
3. **Explicitly describe each baseline's training procedure**, clarifying which baselines involve retraining the reward model on interaction data and which do not.
4. **Add a sensitivity study** for the selection thresholds γ and η.
5. **Specify the reference distribution** for the quantile projection in Equation 13.
6. **Discuss the computational cost** of the gradient influence computation relative to baselines.

## Score and Decision

The paper proposes a reasonable combination of existing ideas (uncertainty + gradient selection, expert relabeling, LoRA ensembles) and demonstrates clear empirical gains. However, two major weaknesses prevent strong acceptance: (a) the gradient influence validation set is mismatched with the claimed "policy-aware" objective, and (b) the expert relabeling component is not ablated, so the contribution of data selection versus distillation from a stronger model is not fully separated. These issues are addressable in revision but weaken the paper's core narrative in its current form. The empirical results are solid but the methodological justification has gaps.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>