Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper observes that small-scale CLIP models (trained on CC3M/CC12M) plateau in accuracy, and shows that resetting the learning rate scheduler and training for a few extra epochs yields large gains (e.g., 31% → 41% ImageNet zero-shot for ResNet-50 on CC12M). The paper frames this as evidence that these models are "undertrained" and demonstrates the practical effectiveness of this simple procedure.

## Strengths

- **Genuinely surprising and practically useful empirical finding.** Figure 1 shows a CLIP model plateauing at ~31% ImageNet accuracy after 75 epochs on CC12M, then jumping to ~41% after just 10 additional epochs with a reset LR schedule — a 10% absolute gain. This is a striking result that could benefit researchers with limited compute budgets.

- **Remarkable efficiency.** Figure 3 shows the performance gain saturates after only 3 extra epochs across multiple architectures (ResNet-50, ViT-B-32, ViT-B-16). The overhead is negligible.

- **Early restart surpasses full training.** Figure 4 shows that restarting after just 10 of 75 planned epochs yields a model reaching 37% accuracy after 20 total epochs, surpassing the full 75-epoch model (31%). This suggests the standard cosine schedule is suboptimal and the paper's procedure recovers lost potential.

- **Negative result on LAION-400M validates the scope.** Table 6 shows the restart procedure does not improve a ViT-B-32 trained on LAION-400M. This controlled comparison strengthens the paper's claim by showing the effect is specific to small-scale training, and the paper honestly reports this limitation.

- **Multi-cycle cosine schedule from the start also helps.** Section 3.4 shows that using a cyclic LR schedule from the beginning of training outperforms the standard single-cycle cosine schedule, providing a complementary actionable recommendation.

## Weaknesses

### Fatal

None.

### Major

- **The central "undertrained" claim is not cleanly isolated from the LR-restart mechanism.** The paper attributes the improvement to "undertraining" — i.e., the model simply needs more training. However, the experiment conflates two factors: (a) more training steps and (b) a reset to a high learning rate that can escape sharp minima. The paper does **not** test the obvious control: *continue training with a very small constant LR* (no restart). If constant-LR continuation also improves accuracy, the "undertrained" label is plausible. If it does not, the improvement is an LR-reset artifact (escaping a sharp basin), and the paper's central framing is misleading. This is the single most important missing experiment, and it affects whether the paper's main claim can be taken at face value.

### Minor

- **Unequal compute in Table 7 comparison.** Table 7 compares the paper's method (41.7% on ImageNet) against methods that train from scratch with modified objectives (e.g., SLIP: 34.0%). The competing methods are trained for some fixed budget (typically 75 epochs on CC12M), while the paper's method uses the baseline checkpoint *plus* extra epochs — effectively more total compute. While the accuracy gap is large enough (41.7% vs. next best 36.2%) that unequal compute alone cannot explain it, the comparison would be fairer by either (a) using equal total epochs for all methods or (b) applying the restart to each competing method's checkpoint. The authors should at minimum discuss how the extra compute affects the comparison.

- **No error bars or multiple seeds.** All figures and tables report single-run results. Given that some comparisons involve small gaps, the lack of variance estimates weakens confidence in the reported numbers.

- **Baseline provenance in Table 2 is underspecified.** The table says "performance reported by the literature" without citing which specific papers or confirming whether training setups match. The paper should train its own baselines under identical conditions or at least clearly cite the sources.

- **Why 15 extra epochs for LAION (Section 3.5) when 3 sufficed for small-scale?** The paper does not justify this choice. If the method is meant to be simple with a fixed heuristic, this inconsistency needs explanation.

### Trivial

- The paper's title ("Your CLIP Model Might Be Undertrained") is somewhat broader than the evidence supports, which is limited to small-scale models. The paper acknowledges this in Section 3.5, so the issue is solely about presentation scope. The title is not factually wrong given the "might be" qualifier.

## Nice-to-Haves

- An ablation comparing the proposed restart with simply continuing training at a constant small LR (this is listed as a Major weakness, not a nice-to-have — it genuinely affects the core claim).
- Extending the analysis to additional smaller-scale datasets beyond CC3M/CC12M to further validate the generality of the finding.
- Application of the restart procedure to checkpoints of the competing methods from Table 7, if available, for a fairer comparison.

## Removed Points

- **Criticism that the title/abstract are too sweeping given the LAION negative result.** The paper explicitly studies this in Section 3.5 and reports it honestly. The title says "might be" — this is appropriately cautious, and the abstract states "especially those trained on smaller datasets." This is not a real weakness. → Moved from review.

- **Strength Finder's claim that Table 7 comparison shows the method is "competitive with" other approaches without caveats.** I've kept this strength but qualified it with the unequal-compute concern in Weaknesses.

- **Critic's point about "why 15 epochs for LAION" is noted but is a minor detail, not a structural weakness.** Kept in minor weaknesses.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an insight not fully explored in the paper: the observed phenomenon may be more about the *design of the LR schedule* than about undertraining per se. Figure 4's finding that restarting after just 10 epochs surpasses the 75-epoch baseline suggests the standard cosine schedule is actively harmful in the later stages of training on small datasets. This could point to a more general principle — that aggressive LR schedules designed for web-scale training are poorly calibrated for smaller datasets where gradients remain informative for longer. The multi-cycle cosine result (Section 3.4) partially addresses this, but the mechanism (sharp minima escape vs. genuine undertraining) remains unexamined.

## Suggestions

1. **Run the constant-LR continuation experiment.** Without this control, the paper's central claim is ambiguous. This one experiment would either validate or reframe the entire contribution.

2. **Report all results with at least 3 random seeds** and include error bars or confidence intervals.

3. **Equalize the total training budget** in Table 7, or apply the restart to the checkpoints of competing methods, or at minimum discuss the unequal compute honestly.

4. **Cite the exact sources** for baseline numbers in Table 2, or train those baselines under identical conditions.

5. **If the constant-LR baseline does not improve**, reframe the paper around "LR restarts improve small-scale CLIP models" rather than "CLIP models are undertrained."

## Score and Decision

I read the following anchor papers from the calibration set for comparative scoring:

| Path | Avg Human Score | Comparison to This Paper |
|------|----------------|--------------------------|
| S5yOuNfSA0 — Understanding Transferable Representation Learning and Zero-shot Transfer in CLIP | 6.50 (Accept) | Stronger theoretical depth and more rigorous experiments; our paper has a more surprising empirical finding but weaker controls |
| tnBaiidobu — Does CLIP's generalization mainly stem from high train-test similarity? | 5.75 (Accept) | Better experimental design (multiple seeds implied) and clearer scope; our paper has a more actionable finding but weaker methodology |
| qm46g9Ri15 — AlignCLIP | 5.25 (Reject) | Similar level of technical contribution; our paper has a more surprising finding but similar concerns about evaluation breadth |
| a4nSE2kpoq — HyperCLIP | 4.00 (Reject) | Our paper has a clearer and more impactful empirical finding |
| JetCx7Tpgb — OrthSR | 4.20 (Reject) | Our paper's finding is more novel and surprising; OrthSR has marginal gains over baselines |
| FbQLFsBbTe — FastCLIP | 3.67 (Reject) | Our paper reports a simpler, more striking finding with broader practical utility |
| G9Ea7mlqGO — CLIP as Efficient Online Continual Learner | 3.80 (Reject) | Our paper faces fewer confounding issues in its experimental design |
| HfJxXbXlYJ — LLM2CLIP | 3.00 (Reject) | Our paper is better written and has a cleaner contribution |

**Relative positioning:** This paper has a genuine and surprising finding, but the missing constant-LR control and the absence of error bars place it below the well-executed empirical papers (tnBaiidobu at 5.75, S5yOuNfSA0 at 6.50). It is stronger than the papers scoring 3–4, which either have marginal gains, unclear framing, or presentation issues. The paper's central thesis is not fully validated by the current experiments, pulling it down.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>