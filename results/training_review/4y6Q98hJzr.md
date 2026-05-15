Now I have a thorough understanding of the paper and all the reviewer claims. Let me synthesize the final review.

## Summary

This paper documents an empirical phenomenon during domain continual pre-training of LLMs: task performance initially drops before recovering (a V-shaped curve), which the authors term a "stability gap" adapted from continual learning. They propose three strategies (multi-epoch training on a high-quality subset, data selection, and distribution-matched data mixing) to mitigate this drop and improve efficiency. Experiments on OpenLlama-3B and TinyLlama show the strategies improve medical task accuracy from 36.2% to 40.7% using 40% of the original token budget, and deployment on Llama-3-8B yields Llama-3-Physician, which achieves strong medical benchmark performance.

## Strengths

- **Systematic documentation of a practically relevant empirical phenomenon.** The paper provides clear evidence of a V-shaped performance trajectory during domain continual pre-training, observed across two model scales (OpenLlama-3B, TinyLlama), two domains (medical, legal), and multiple evaluation checkpoints (Figures 2a-b). The finding that performance initially drops before recovering is a useful observation for practitioners and challenges the naive assumption of monotonic improvement.

- **Demonstration that multi-epoch training on a high-quality, distribution-matched subset improves both efficiency and peak performance.** The combined strategies (5B high-quality tokens × 4 epochs, with pre-training-like data mixing) achieve 40.7% average medical accuracy vs. 36.2% for the 50B × 1 epoch baseline, using only 20B total tokens (Table 1). The ablation in Figure 4a separates the contribution of multi-epoch training from data quality selection, and the results on Llama-3-8B (Table 2) show the approach generalizes to a stronger base model.

- **Extension to instruction tuning.** Section 5.4 (Figure 5) shows the same V-shaped pattern appears during instruction tuning and the proposed strategies (quality selection + mixing with general instructions) remain effective, achieving strong results with only 25% of the instruction data budget.

## Weaknesses

### Fatal
None.

### Major

- **Section 5.2 ("Factor Analysis") contains no quantitative analysis.** Despite being a titled subsection and referenced as providing analysis of learning rate, subset size, and data mixture rate, it consists of a single paragraph of qualitative assertions (e.g., "a learning rate that is too high leads to significant drops") with no tables, figures, or numerical results. For a paper whose practical contribution is a set of training strategies, the absence of any data on how critical hyperparameters affect outcomes is a significant omission. Readers cannot assess the robustness or optimality of the chosen settings.

- **Unsupported claim about GPT-3.5 in the conclusion.** Line 144 states the model "outperforms the closed-source GPT-3.5 model," but no comparison with GPT-3.5 is presented anywhere in the paper — Table 3 compares with GPT-4, not GPT-3.5. This claim is unsupported by the evidence provided and should be removed or substantiated.

- **Missing control baselines weaken the mechanistic attribution.** The paper attributes the improvement to "mitigating the stability gap," but does not include two natural controls: (a) 5B tokens × 1 epoch, which would isolate the multi-epoch effect from data selection, and (b) 50B tokens × multiple epochs, which would test whether the stability gap is inevitable with large-scale one-pass training or specific to the training configuration. Without these, the contribution of the "stability gap" framing vs. simpler explanations (multi-epoch training is beneficial, data quality matters) cannot be disentangled. The freeze-top-5-layers baseline achieves 38.9% (competitive with the 40.7% result) and is not adequately discussed.

### Minor

- **The theoretical framing as "stability gap" is adapted from continual learning but the evidence is correlational.** The paper acknowledges (line 62-63) that "directly applying the concept...is not feasible" and proposes a "self-replay" adaptation. The evidence for the gradient-decomposition mechanism (plasticity vs. stability gradients) rests on the correlation between general-task V-shapes (Figure 3a) and aggregate layer-wise weight updates (Figure 3b). This is a plausible explanation but is not causally tested — the paper does not introduce an explicit replay loss to verify that strengthening the stability gradient directly mitigates the drop. The strategies could be motivated without the framework.

- **The V-shaped curve during instruction tuning (Figure 5a) is described as "similar to the phenomenon observed in the continual pre-training process," but the drop is very small and the dynamics of multi-task fine-tuning differ from continual pre-training. The connection is plausible but weakly evidenced.

### Trivial
None.

## Nice-to-Haves

- Adding a 5B × 1 epoch baseline and a 50B × multi-epoch baseline would cleanly separate the effects of data quantity, epoch count, and data quality.
- Reporting per-task performance curves (not just averages) across checkpoints would reveal whether the V-shape is consistent across individual medical benchmarks.
- Showing training loss curves alongside benchmark performance would help distinguish distribution-mismatch explanations from the stability gradient explanation.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

1. **Criticism about "Table 6 is not in the paper"** — Table 6 was in the appendix, which the parser strips from all papers. The original submission contains it. Removed per hard rule about parser-stripped content.

2. **Criticism about missing related work citations** (e.g., "similar dynamics are documented in fine-tuning literature... the paper does not cite or discuss this") — Per rule: do not mention missing related works without external sources to confirm their existence.

3. **Criticism about "40% of the original training budget is ambiguous"** — The paper explicitly states in Section 3.1 that the budget is 50B tokens (following prior work), and the method uses 20B tokens. The 40% figure is well-defined.

4. **Strength Finder's claim that "Section 5.2 further analyzes the impact of key hyperparameters... providing practical guidance"** — Factually incorrect; Section 5.2 contains no quantitative data. Removed as a strength that conflicts with verified weakness.

5. **Strength Finder's claim about "comprehensive comparisons and factor analysis"** — The comparisons part (Table 1) is valid but already covered under core strengths; the "factor analysis" part is factually wrong.

## Novel Insights

The harsh critic's observation that the "self-replay" argument does not cleanly map onto the gradient decomposition framework is insightful — the paper would benefit from either providing direct causal evidence (e.g., an explicit replay experiment) or acknowledging the framework as an analogy rather than a mechanistic explanation. The critic's point about the freeze-top-5-layers baseline (38.9% vs. 40.7%) being competitive is also noteworthy: it suggests that protecting top-layer representations alone goes a long way, which could motivate simpler approaches than the full pipeline. The existence of the V-shape during instruction tuning, while affirmed by the paper, is noted by the critic to involve very different dynamics (multi-task fine-tuning), and this tension deserves explicit discussion.

## Suggestions

1. Fill Section 5.2 with actual quantitative results (tables/figures showing learning rate sweeps, subset size sweeps, and data mixture ratio sweeps).
2. Remove or substantiate the unsupported GPT-3.5 claim in the conclusion.
3. Add the 5B × 1 epoch and 50B × multi-epoch baselines, or at minimum explicitly discuss why they are omitted and acknowledge the confounding factors in the efficiency claim.
4. Tone down the mechanistic claims about the "stability gap" and reframe the contribution as an empirical finding with a plausible but unverified explanation — the practical strategies stand on their own empirical merit.
5. Discuss the freeze-top-5-layers baseline's competitive performance and explain why the proposed strategies are preferable beyond the marginal accuracy gain.

## Score and Decision

The paper makes a useful empirical contribution (the V-shaped phenomenon is genuinely interesting and practically relevant) and the combined training strategies produce real improvements. However, the empty "Factor Analysis" section, the unsupported GPT-3.5 claim, and the missing control baselines are substantive issues that need to be addressed. The paper would benefit from a more honest framing that separates the robust empirical observations from the loosely-attached theoretical explanation. I recommend a borderline assessment — the core findings are reproducible and valuable, but the presentation overclaims in places and some essential analysis is absent.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>