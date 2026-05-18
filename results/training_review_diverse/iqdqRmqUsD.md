## Summary

SOLD integrates unsupervised object-centric representations (SAVi) into the Dreamer model-based RL framework. By structuring the latent space as object slots and using a transformer dynamics model (built on OCVP) to predict future slot states conditioned on actions, along with a Slot Aggregation Transformer for actor-critic learning, the method achieves strong results on a custom suite of robotic manipulation tasks requiring relational reasoning. The paper also demonstrates that fine-tuning SAVi during RL training (rather than freezing it after pretraining) is critical for handling state distributions unseen during random exploration.

## Strengths

1. **First fully pixel-based object-centric model-based RL algorithm.** The paper correctly identifies and addresses a gap: prior work either used object-centric representations for model-free RL, for planning without learning behaviors, or required ground-truth segmentation masks. SOLD combines unsupervised slot decomposition (SAVi), action-conditional object dynamics (extending OCVP), and Dreamer-style latent imagination into a single end-to-end framework from pixels (Section 1, lines 12-14; Section 3).

2. **Consistent and often large outperformance over DreamerV3 on tasks requiring relational reasoning.** On all eight custom tasks (Figure 4, lines 144, 173), SOLD achieves higher final success rates than DreamerV3, with a particularly pronounced advantage on the *Distinct* (odd-one-out) and *Specific-Relative* variants where relational reasoning is essential. The return curves over training (Figure 5, lines 166, 175) further show faster learning and higher asymptotic returns.

3. **SAVi fine-tuning overcomes a key limitation of prior object-centric RL works.** The paper identifies that freezing the slot encoder after random-policy pretraining fails when the policy must reach states never seen under random exploration. Figure 7 (lines 179, 196) shows that a frozen SAVi cannot reconstruct a lifted block (a state unreachable by random actions), while fine-tuned SAVi recovers it, enabling task completion. This is a genuine practical insight.

4. **Interpretable attention patterns.** The Attention Rollout visualization (Figure 6, line 177) shows the actor's attention focusing on task-relevant objects (robot, target block) while ignoring distractors, even maintaining focus across 15 time-steps of occlusion. This demonstrates that the structured latent space yields inspectable decision-making, a practical benefit over holistic representations.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim of outperforming DreamerV3 is only partially supported.** The abstract and contributions (lines 4, 22) state that SOLD "outperforms DreamerV3 across a range of benchmark robotic environments." However, direct DreamerV3 comparisons are provided **only** on the paper's 8 custom tasks (Figure 4). On Meta-World and DM-Control (line 184), only SOLD's own scores are reported (100% on Button-Press/Hammer; returns of 497 and 645 on Cartpole-Balance/Finger-Spin) — with no baseline comparison. The paper even acknowledges in the Limitations (line 209) that SOLD "struggles to match [DreamerV3's] performance on simpler tasks like Cartpole-Balance," yet never presents DreamerV3's actual scores on these tasks. This means the reader cannot evaluate whether SOLD is competitive on standard benchmarks or whether the claimed advantage is confined to the authors' own object-centric task suite. The core claim needs either (a) explicit DreamerV3 comparisons on Meta-World and DM-Control, or (b) precise scoping to the tasks where comparison data exists. This is the single most consequential gap in the paper.

### Minor

2. **The "Ours w/o OCE" ablation baseline is inadequately specified for clean isolation.** The baseline is described only as "replacing the object-centric encoder-decoder modules with a standard convolutional architecture" (line 137). Several confounds are unclear: does this baseline receive the same SAVi pretraining (10⁶ frames)? Does it use the same transformer-based dynamics model and Slot Aggregation Transformer backbone, or a simpler architecture? Without this transparency, the comparison conflates the object-centric bottleneck with other engineering choices (transformer dynamics, register tokens, ALiBi). The results on the *Distinct* tasks are still *suggestive* — the baseline's near-complete failure there is hard to explain away by architecture alone — but the ablation is not as clean as it should be for a paper claiming that object-centric representations are the causal factor.

3. **The deterministic dynamics limitation undercuts the generality claim but is not quantified.** The paper honestly acknowledges (line 209) that the deterministic world model is a drawback on stochastic tasks like Cartpole-Balance and that this is why SOLD "struggles to match [DreamerV3's] performance" there. However, since DreamerV3's scores on these tasks are not reported, the magnitude of the gap is unknown. Combined with the missing DreamerV3 comparisons (Major weakness #1), the paper's overall claim of broad superiority over DreamerV3 is not well supported by the evidence as presented.

### Trivial

4. **Error bars in Figure 4 are not described.** The caption (line 144) and text (line 173) mention three random seeds but do not state what the error bars represent (standard deviation? standard error? min-max range?). This is a small presentational fix.

5. **No quantitative metric for open-loop predictions.** The qualitative predictions in Figure 3 look good, but adding a quantitative measure (e.g., MSE of predicted vs. encoded slots, or reconstruction MSE over the prediction horizon) would strengthen the dynamics model evaluation.

## Nice-to-Haves

- A controlled comparison on a stochastic variant of one custom task (e.g., adding action noise) would deepen the analysis of whether the deterministic dynamics limitation is fundamental or manageable.
- Reporting the parameter count and architectural details of the "w/o OCE" baseline relative to SOLD would strengthen the ablation's interpretability.

## Removed Points

These points were flagged but removed after verification against the paper:

- **"The paper cannot claim outperformance because tasks were designed by the authors"** — Removed because this is a non-issue: the paper provides DreamerV3 comparisons on those same tasks, which is standard practice when introducing a new benchmark. The tasks are documented and publicly reproducible; the comparison is fair.
- **"Attention visualization claim about discovering task-relevant objects requires evidence beyond attention heatmaps"** — The paper also shows the model succeeding on the tasks with those attention patterns; the attention analysis is a qualitative interpretation, not a central claim of the method. Downgraded to a non-issue.
- **"Missing statistical significance" / "Three seeds is minimal"** — Three seeds with error bars is standard for deep RL papers at major venues. This is not a reasonable criticism.

## Novel Insights

The synthetic review highlights a tension that the paper itself identifies but does not fully resolve: object-centric representations improve relational reasoning tasks but the deterministic dynamics harm stochastic control tasks. This creates a genuine design trade-off for object-centric MBRL — one that points toward a combined approach (object-centric latent structure + stochastic transition model) as a natural next step. The fine-tuning finding (that frozen SAVi fails on states unseen during random exploration) is a practical insight that many prior object-centric RL works overlooked.

## Suggestions

- **Provide DreamerV3 comparisons on Meta-World and DM-Control.** This is the single highest-impact fix. Without it, the abstract and conclusion claims of outperforming DreamerV3 "across a range of benchmark robotic environments" are not supported by the evidence.
- **If the Cartpole-Balance and Finger-Spin results show SOLD underperforming DreamerV3, explicitly scope the claim** (e.g., "SOLD outperforms DreamerV3 on tasks requiring relational reasoning and manipulation, while remaining competitive on tasks where object-centric structure is less advantageous").
- **Describe the w/o OCE baseline in more detail** — specify whether it uses the same transformer dynamics, SAT backbone, and pretraining protocol.
- **Label what Figure 4's error bars represent** in the caption.
- **Add a brief quantitative metric** for open-loop prediction quality (e.g., MSE between predicted and encoded slots over the prediction horizon).

## Score and Decision

The paper proposes a sensible, well-motivated integration of object-centric representations into model-based RL. The contributions on the custom relational reasoning tasks are genuine, and the SAVi fine-tuning finding is practically useful. However, the paper's central comparative claim is not fully supported by the evidence provided: DreamerV3 comparisons are missing on the very benchmarks (Meta-World and DM-Control) that are used to argue for generalizability, and the paper's own limitations section admits SOLD underperforms on one of them. This overclaiming is a substantive issue, but it is addressable — it requires either running the comparisons or tightening the scope of the claim. The technical contribution itself is sound.

**Score**: 6.0 — A decent paper with a real contribution, held back by an overextended central claim that the evidence does not fully support. The method is novel and the results on the custom benchmark are strong, but the paper would be significantly strengthened by scoping its claims to match the actual experimental evidence.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>