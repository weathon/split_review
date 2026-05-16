Now I have all the information needed to write the review. Let me compose it.

## Summary

This paper proposes M3L (Masked Multimodal Learning), a method that jointly learns visual-tactile representations through a masked autoencoder (MAE) while simultaneously optimizing a PPO policy, sharing the encoder between both objectives. The method is evaluated on three simulated robotic manipulation tasks (tactile insertion, door opening, dexterous in-hand cube rotation). The key claims are that M3L improves sample efficiency over end-to-end RL, unlocks zero-shot generalization to unseen objects and scene variations, and — notably — that multimodal training benefits even vision-only policies at test time.

## Strengths

- **Zero-shot generalization consistently improves across tasks.** On tactile insertion (unseen peg shapes), door opening (randomized hinge dynamics), and in-hand rotation (doubled mass, perturbed camera), M3L outperforms vision-only MAE and end-to-end baselines. These results directly support the paper's central claim that joint visual-tactile representations generalize better than single-modality or sequential processing. (Fig. 6 / generalization results)

- **Multimodal training yields representations that benefit vision-only policies, nearly closing the gap with full multimodal deployment.** In all three tasks, "M3L (vision policy)" — trained with touch but deployed without it — outperforms the vision-only MAE baseline and approaches M3L's performance. This is a practically significant finding for sim-to-real scenarios where tactile sensors may not be available on the real robot. (Fig. 6)

- **Sample efficiency gains are consistently demonstrated.** Learning curves (Fig. 7) show that representation-learning methods (M3L, vision-only MAE, sequential) all reach higher success rates faster than end-to-end PPO with the same encoder, confirming the value of the self-supervised reconstruction objective.

- **The method is evaluated across three distinct manipulation tasks** with different contact patterns and scene variations, and the key trends hold consistently, strengthening the generality of the findings.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No contrastive baseline despite motivational claims.** The paper motivates MAE by stating that "as opposed to other representation learning approaches, such as contrastive learning, MAEs do not need discovering new data augmentations and invariances to design positives and negatives" (Sec. 4, line 120). However, no contrastive or other alternative multimodal representation learning method is included as a baseline. The paper's own baselines (vision-only MAE, sequential, end-to-end) are reasonable, but this rhetorical framing invites a comparison that is never tested, making it impossible to tell whether the observed benefits are attributable to the MAE objective specifically or to multimodality and joint encoding more generally. This does not invalidate the paper's claims against the baselines tested, but it would strengthen the paper to either include such a baseline or soften the comparative language.

- **Hyperparameter fairness is not fully documented.** For the in-hand rotation task, M3L uses a specialized alternating gradient schedule ("one RL gradient step every *n* representation learning gradient steps," Sec. 5.2) that differs from the two-objective joint optimization used in the other tasks. The paper does not clarify whether the baselines (vision-only MAE, sequential, end-to-end) were optimized under comparable schedules or with equivalent tuning effort. Since the vision-only MAE and sequential baselines also have representation-learning phases, it is unclear whether the alternating schedule was applied to them. Without this information, a reader cannot rule out the possibility that some of M3L's advantage on this task stems from differential tuning rather than the method itself.

- **The role of cross-modal attention is only partially ablated.** The sequential baseline prevents cross-modal attention and performs worse on door opening, providing some evidence. However, the paper claims that "attention across vision and touch lead[s] to better overall performance" (Sec. 6) without providing attention visualizations, probing of modality contributions, or a cleaner ablation (e.g., processing modalities separately with late fusion). The sequential baseline confounds the attention mechanism with the training procedure (sequential gradient propagation). A "frozen cross-attention" or late-fusion control would more cleanly isolate the contribution of joint attention.

- **Several hyperparameters and implementation details are missing.** The balancing weight *β_T* for the touch reconstruction loss (Eq. 2) is not specified anywhere. The exact grid resolution used in the tactile insertion mesh (described as "a grid of smaller boxes" but not parameterized) is not given. The frame-stacking length used per task is stated as 4 for all baselines (Sec. 6.2) for the main experiments, but the frame-stacking ablation is only shown for the tactile insertion task, leaving it unclear whether 4 frames is optimal for all three tasks. The alternating schedule's *n* value for the in-hand task is also unreported.

- **Some generalization details are underreported.** For the door opening generalization test, the paper reports using "10× higher friction and damping coefficients for hinges" during testing but does not specify the training values of these parameters, making it difficult to quantify the generalization gap.

- **No statistical tests on key comparisons.** The generalization bar plots (Fig. 4) show point estimates with error bars across 5 seeds, but no significance tests are reported. On door opening, the gap between M3L and M3L (vision policy) appears small and could be within noise. Paired tests across seeds would help assess robustness.

### Trivial

- The early convolution layers are described as helpful for reconstruction details but are not ablated, making the claim untested within this paper.

## Nice-to-Haves

- A contrastive visual-tactile baseline (even if simpler than M3L) would directly test the paper's motivational claims about MAEs vs. contrastive methods.
- Reporting wall-clock time or GPU-hours per method would contextualize the sample-efficiency gains against computational cost.
- Attention-map visualizations from the ViT encoder (e.g., attending from visual patches to taxels registering contact) would strengthen the cross-modal attention claim.
- The frame-stacking ablation could be extended to the other two tasks to verify that the finding is not task-specific.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No discussion of prior work using MAE with RL in pretraining-finetuning fashion (e.g., MVP, MT-ORT)."** — This is factually incorrect. The paper explicitly cites MVP, mv_mwm, and seo2023masked in Sec. 2 (Related Work) and discusses pretraining-finetuning in Sec. 7 (Limitations): "Previous work that only relied on visual data leveraged MAEs in a pretraining fashion, with a large encoder trained off-domain and directly deployed." Removed per Hard Rule 2 (factually wrong).

2. **Abstract phrase "remarkably" is overstated.** — A stylistic judgment about wording that does not affect the substance. Removed per Hard Rule 5 (formatting/style nitpick).

3. **Ambiguity in sequential baseline description ("do the two modalities share the same encoder weights?")** — The paper states: "an M3L architecture trained independently for the different modalities in sequence. At each MAE training iteration, we first propagate the gradient for vision and then for touch." This clearly describes the same architecture with the same weights, differentiated by the order of gradient propagation. Removed per Hard Rule 2 (misunderstand the paper).

4. **Number of generalization objects not reported** — The paper states "18 different training peg shapes, and 2 novel pegs (rectangle and V-shape)." This is a factual reporting in the paper. Removed per Hard Rule 2 (already addressed).

5. **Weakness about missing appendix content** — Not present in the original criticism, but the paper's appendix was stripped by the parser. The paper's content is intact for the main text.

## Novel Insights

None beyond the paper's own contributions. The key insight — that multimodal MAE training with touch produces representations that benefit even vision-only policies — is the paper's own finding, and the reviews do not add a deeper or different interpretation of the results.

## Suggestions

- Report the missing hyperparameters (*β_T*, grid resolution, alternating schedule *n*) and training friction/damping values. This is essential for reproducibility.
- Add a brief note confirming whether the alternating gradient schedule was applied to the baselines on the in-hand task, or state the tuning protocol used for each baseline.
- Run a simple paired significance test (e.g., across 5 seeds with 25 episodes each) on the key generalization comparisons, especially M3L vs. M3L (vision policy) on door opening.
- If space permits, include a late-fusion variant (separate modality processing with post-hoc fusion) to more cleanly isolate the contribution of early cross-modal attention.

## Score and Decision

The paper makes a solid contribution: it demonstrates that joint visual-tactile masked autoencoding improves both sample efficiency and generalization over reasonable baselines, and the finding that multimodal training benefits vision-only deployment is practically valuable. The weaknesses are real but minor — none invalidate the core claims. The missing contrastive baseline is the most significant gap but is partially mitigated because the paper's main claims (improvement over vision-only MAE, end-to-end, and sequential) are all tested. The hyperparameter fairness concern is addressable. This is a solid paper that would benefit from revision but is acceptable in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>