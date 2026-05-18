## Summary

This paper demonstrates a simple yet effective finding: CLIP models trained on small-scale datasets (CC12M, CC3M) benefit substantially from resetting the learning rate scheduler and training for a few additional epochs. The intervention yields consistent gains of 4–11% absolute on zero-shot ImageNet accuracy across multiple architectures (ResNet-50, ViT-B-32, ViT-B-16), saturates after only 3 extra epochs, and produces results competitive with far more complex CLIP modifications. The paper also shows that the improvement disappears at large scale (LAION-400M) and that training from scratch with a multi-cycle cosine schedule outperforms the standard single-cycle schedule.

## Strengths

- **Large, consistent, and reproducible gains from a trivial intervention.** A ResNet-50 CLIP trained on CC12M jumps from 31% to 41.7% ImageNet zero-shot accuracy solely by resetting the LR scheduler and training for 10 more epochs (Table 2, Figure 1). This ~10-point absolute gain is striking for a method that requires no architectural changes, no loss modification, and no additional data.

- **Gains are consistent across architectures and evaluation tasks.** Table 2 reports improvements of 4–11% for ResNet-50, ViT-B-32, and ViT-B-16 on ImageNet, ImageNetV2, and ObjectNet, establishing the phenomenon is not architecture-specific.

- **Computational overhead is minimal.** Figure 3 shows that performance saturates after only 3 extra epochs across all three architectures, making the procedure nearly free.

- **Compelling boundary condition via negative result.** Table 6 shows that applying the same restart procedure to a ViT-B-32 trained on LAION-400M yields no improvement, cleanly demonstrating the phenomenon is specific to the small-data regime.

- **Figure 5 (multi-cycle cosine from scratch) is a clean, standalone result.** Training with a multi-cycle cosine schedule from the start outperforms the standard single-cycle schedule with fewer total epochs. This is practically useful for anyone training CLIP from scratch on small data.

- **Figure 4 (early restart)** shows that stopping training at epoch 10 and restarting reaches 37% after only 20 total epochs — outperforming the standard model's 31% after 75 epochs. This suggests a far more efficient training pathway.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental details prevent full reproducibility.** The paper never specifies the optimizer (AdamW? SGD? betas?), learning rate value, batch size, weight decay, warmup steps, exact schedule parameters (initial LR, minimum LR, cycle length), how "resetting the scheduler" is implemented (back to the full initial LR and full schedule, or a shortened cycle?), dataset preprocessing/deduplication, or whether results are single-run or averaged over seeds. For a paper whose entire contribution is a training protocol, these omissions are serious.

- **The "undertrained" framing overclaims what the evidence supports.** The paper's own results in Section 3.4 (Figure 5) show that using a multi-cycle cosine schedule from scratch outperforms the single-cycle schedule. Section 3.1 states that accuracy saturates after epoch 40 under the original schedule. Together, these results suggest the core issue is *schedule suboptimality*, not insufficient training. The term "undertrained" implies the model has not been trained long enough, but the evidence points to a poor schedule choice. A model trained for 75 epochs that plateaus after 40 is not undertrained in any standard sense — it has been trained with a suboptimal schedule. The paper would be stronger and more honest if it framed the contribution around recovering from a poor LR schedule post-hoc.

- **The comparison with prior methods (Table 7) is not controlled.** The paper compares its method against SLIP, FLIP, CLIP+CR, etc., but does not establish whether these baselines were trained under comparable conditions (same dataset, backbone, compute budget, hyperparameters). The paper also does not test whether the baseline methods could themselves be improved by the same restart strategy. If they can (which is plausible), the claim of competitiveness is weakened. Additionally, only ImageNet accuracy is reported for this comparison, while the paper's own method is evaluated on more tasks in Table 2 — an asymmetry that makes the comparison less informative.

### Minor

- **No analysis of why the restart works.** The paper treats the improvement as a black-box result. Understanding why — e.g., analysis of loss landscapes, gradient norms, representation similarity before/after restart, or whether the benefit comes from escaping a sharp minimum — would significantly strengthen the contribution. As it stands, readers are left to speculate about the mechanism.

- **Limited evaluation of the negative result on LAION-400M.** Section 3.5 tests only one model (ViT-B-32) and one dataset. While the result is suggestive, it is insufficient to support the sweeping claim "CLIP models trained on large datasets are less likely to be undertrained."

- **No discussion of overfitting.** The paper does not report training loss or validation loss trajectories, only zero-shot accuracy. On small datasets like CC12M, additional training could in principle cause overfitting, but this is not examined.

### Trivial
None.

## Nice-to-Haves

- A control experiment showing what happens if training continues without resetting the LR (i.e., with LR fixed at the final cosine minimum) would cleanly isolate whether the benefit is from the restart mechanism or merely from seeing more data.
- Testing whether the restart strategy is additive on top of other CLIP improvements (SLIP, FLIP, etc.) would strengthen the practical relevance.
- A breakdown of the restart's effect on the text encoder vs. the image encoder would be informative.

## Removed Points

- **"The paper never isolates whether the benefit comes from the restart mechanism (high LR) or from the extra epochs."** The paper partially addresses this: Section 3.1 states accuracy saturates after epoch 40 and "simply training for longer does not significantly affect accuracy," and Figure 3 shows saturation after 3 restart epochs. This does not fully isolate the mechanism (a true control would hold LR fixed), but the paper does provide relevant evidence. Weakened to a minor point and moved to Nice-to-Haves.

- **"Baseline comparisons are uninformative and potentially unfair."** The strength of this criticism is reduced because the paper's claim is modest ("competitive results") and the comparisons, while imperfect, are reported honestly. Moved from "Evidential" (fatal-level framing) to Minor weakness.

- **Strength Finder's generic strengths removed:** "The paper provides direct, testable alternative training schedule" — this is already covered by other strengths. "All experiments use standard public datasets" — this is generic and not a distinctive strength.

## Novel Insights

None beyond the paper's own contributions. The key observation — that a simple LR reset gives large gains on small-scale CLIP models — is itself the novel insight. The reviewers' analyses add no fundamentally new interpretation beyond what the paper already states.

## Suggestions

1. Add a dedicated "Experimental Setup" section specifying optimizer, hyperparameters, LR schedule parameters, dataset versions, and whether results are averaged over multiple seeds.
2. Add a control experiment: continue training for 10 epochs with LR fixed at its cosine-decayed minimum (no reset). This would cleanly separate the benefit of the restart from the benefit of additional data exposure.
3. Add an analysis section investigating the mechanism (e.g., loss landscape visualization, gradient norm trajectories, or representation similarity between original and restarted models).
4. Reframe the contribution around recovering from suboptimal LR schedules rather than "undertraining," which more accurately reflects what the evidence shows.
5. In Table 7, report whether the baseline methods could also benefit from an LR reset, or at minimum discuss this caveat explicitly.
6. Add standard deviation/error bars to all quantitative results.

## Score and Decision

**Calibration Anchors (all retrieved from calibration search, one batch):**

| Anchor | Avg Score | Comparison to This Paper |
|--------|-----------|--------------------------|
| Interpreting CLIP's Image Representation via Text-Based Decomposition | 8.00 | Deep, rigorous analysis with extensive experiments and clear applications — far stronger than this paper |
| Compositional Entailment Learning for Hyperbolic VLMs | 8.00 | Novel method with large-scale training and strong empirical results — substantially stronger |
| Understanding Transferable Representation Learning in CLIP | 6.50 | Theoretical + empirical contribution with rigorous experimental design — stronger |
| CityAnchor: City-scale 3D Visual Grounding | 6.50 | Extensive experiments and clear engineering contribution — stronger |
| When, Why and How Much? Adaptive LR Scheduling | 5.80 | Theoretical grounding + comprehensive evaluation across 10 problems — stronger in rigor |
| Leveraging Knowledge Graphs for Efficient CLIP Training | 5.33 | Dataset contribution with solid experiments and clear scope — slightly stronger |
| FastCLIP | 3.67 | CLIP optimization paper with limited novelty and unclear writing — this paper is clearer with a more surprising finding |
| CLIP Model is an Efficient Online Continual Learner | 3.80 | Missing comparisons and methodological concerns — similar quality, this paper has cleaner results |
| Hybrid Classification-Regression Adaptive Loss | 3.00 | Incremental, limited experiments — weaker |

This paper reports a genuinely useful and surprising observation, and the core experiments are clearly communicated. However, it suffers from (a) missing reproducibility-critical experimental details, (b) an overclaimed "undertrained" framing that its own evidence undercuts, (c) no analysis of the mechanism, and (d) uncontrolled baseline comparisons. Relative to the calibration anchors, it sits between the weaker CLIP papers (FastCLIP, CLIP Continual Learner) and the moderately-rated papers (Knowledge Graphs, Adaptive LR Scheduling). It is more insightful and practically useful than FastCLIP, but far less rigorous than the 5.5+ papers.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>