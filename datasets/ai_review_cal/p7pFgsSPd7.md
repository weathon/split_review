- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5
Now I have all the information needed to write the consolidated review.

---

## Summary

This paper proposes Sample-aware RandAugment (SRA), a search-free automatic data augmentation method that dynamically adjusts augmentation magnitude per sample using a heuristic cosine-similarity-based Magnitude Instructor Score (MIS). SRA uses an asymmetric batch-split strategy where one sub-batch receives random augmentation (exploration) and the other receives MIS-guided augmentation (refinement), with shared weight updates. The method achieves 78.31% Top-1 accuracy on ImageNet with ResNet-50, claiming state-of-the-art among search-free methods, and shows competitive results on CIFAR benchmarks while requiring no search cost and only ~1.1× training time overhead.

## Strengths

1. **State-of-the-art search-free ImageNet accuracy with practical overhead.** SRA achieves 78.31% Top-1 on ImageNet (ResNet-50), outperforming all compared search-free methods and doing so without any search procedure. The total training cost (Fig. 2) places SRA at the top-left corner of the performance-vs-cost scatter plot, and the extra per-epoch time is only ~1.1× on CIFAR-100 (105 vs. 96 s/epoch).

2. **Principled, closed-form sample-awareness without policy networks.** The MIS module (Eqs. 1-2) uses cosine similarity between softmax probabilities and one-hot labels, with a class-count-based scaling factor γ = ε / log(c). This provides a simple, search-free way to adapt augmentation magnitude per sample while normalizing across tasks with different numbers of classes. Prior sample-aware methods (MetaAugment, SelectAugment) require separate policy networks or reinforcement learning.

3. **Asymmetric batch-split design is validated by ablation.** The ablation study (Table 6) confirms that both the exploration (random augmentation) and refinement (MIS-guided) branches contribute significantly — removing either reduces accuracy by ~0.7–1.2% on CIFAR-100. This supports the core design claim that both components are necessary.

4. **Compatibility with other frameworks is empirically demonstrated.** SRA integrates with Tied Augment (outperforming Tied-RA on both CIFAR-10 and CIFAR-100) and with Batch Augment (±8), achieving 88.25% on SS-26-2x96d CIFAR-100 with only 200 epochs vs. 600+ for TA ±8. This shows the method is not tied to a single training recipe.

5. **Feature distribution visualization supports the design intuition.** Figure 3 provides t-SNE evidence that MIS-guided augmented samples tend to lie at cluster boundaries, qualitatively confirming that the method generates hard samples near decision boundaries.

## Weaknesses

### Fatal
None.

### Major

- **Batch size ambiguity in the central ImageNet comparison.** SRA uses a batch size that is "twice of the traditional one" (Sec. 3.2). The reproduced RA baseline on ImageNet is said to be run "under our settings" (Sec. 4.2), but it is never specified whether this includes the doubled batch size. If the RA baseline uses a standard batch (e.g., 256) while SRA uses 512, the 78.31% vs. 77.59% gap could partially reflect batch-size effects on batch normalization, learning rate dynamics, and generalization rather than the augmentation strategy alone. This does not invalidate the method, but it makes the headline comparison less clean than claimed. The authors should either (a) report RA with the same doubled batch, or (b) explicitly argue why the difference is negligible, with supporting evidence.

### Minor

- **Missing uncertainty estimates on ImageNet results.** The paper states "All experiments are run for three times, the average performance and standard deviations of which are reported for self-implemented experiments" (Sec. 4), and standard deviations are given for CIFAR experiments. However, the ImageNet results in Table 2 (the paper's headline numbers) are reported without any variance measure. Given that the 78.31% vs. 77.59% gap is the paper's flagship result, the absence of error bars makes it impossible to assess whether this is a reliable improvement or within run-to-run noise.

- **"Outperforms search-free methods" claim is over-reaching on CIFAR-100.** On CIFAR-100 with SS-26-2x96d, SRA (87.99%) is slightly *worse* than TA (Wide) (88.15%), and on CIFAR-100 with WRN-28-10, SRA (84.12%) is comparable to TA (Wide) (84.25%). The paper acknowledges this in Sec. 4.1, but the abstract and contributions use broad language ("outperforms current search-free AutoDA methods in a variety of settings," "state-of-the-art among search-free methods") without clearly flagging the exception. A more precise framing would strengthen the paper's credibility.

### Trivial

- The paper uses the phrasing "without plenty of tricks" (abstract, line 18); this is informal and should be reworded.
- The hyperparameter ε is introduced and said to be "scaled by log(c)" (Eq. 2), but the paper never discusses how ε is chosen (cross-validation? prior?). A brief clarification would help reproducibility.

## Nice-to-Haves

- **Sensitivity analysis for ε.** Currently ε is a free hyperparameter tuned per dataset. Showing accuracy vs. ε across a range of values (e.g., 0.5–4.0) on one or two datasets would demonstrate robustness and help future users set it in practice.
- **MIS distribution analysis during training.** Does the distribution of MIS values shift, stabilize, or oscillate as training progresses? This could provide evidence that the feedback loop is stable and beneficial.
- **Learning rate scaling discussion.** If SRA uses a doubled effective batch size, the learning rate may need adjustment. A brief statement on whether any LR tuning was performed (and if not, why not) would preempt a natural concern.
- **Overhead estimate for ImageNet.** The 1.1× time overhead is reported only for CIFAR-100 with WRN-28-10. An estimate for ImageNet (500k images, ResNet-50) would strengthen the practical claim.

## Removed Points

- **"TA (Wide) numbers are from different training configurations" (Harsh Critic, Sec. 4.1).** The paper notes it includes "only methods with similar epochs and tricks" and acknowledges the limitation of cross-paper comparisons. This is not a specific weakness — it's a general caveat common to AutoDA papers. REMOVED as generic.

- **"No explicit comparison to AWS in the main table" (Harsh Critic).** The paper explicitly explains why AWS is excluded (unavailable code, unreported settings; Sec. 4.2) and mentions it in text. REMOVED — the authors provide a reasonable justification.

- **"Cosine similarity undefended against miscalibration" (Harsh Critic, Sec. 3).** This is speculative — the paper does not claim MIS is a calibrated measure, only that it is a useful heuristic. Table 6 shows it works empirically. REMOVED as speculative.

- **"γ ∝ 1/log(c) assumption is untested" (Harsh Critic).** The assumption (uniform probability yields same MIS across tasks) is a design principle, not a claim that needs testing — it's the motivation for the formula. The formula is validated by the overall results. REMOVED as over-reading a design rationale as an untested assumption.

- **"SRA vs. TA ±8 comparison mixes different epochs" (Harsh Critic).** The paper explicitly highlights using 200 vs. 600+ epochs as a *strength* (SRA achieves better results with fewer epochs). This is not a weakness. REMOVED — this is a positive result, not a flaw.

- **Several "Strengthening the Paper on Its Own Terms" items** already appear in Weaknesses or Nice-to-Haves above (batch size control, error bars, ε sensitivity, MIS analysis). No need for duplication.

## Novel Insights

The main insight from the reviews is that the paper's core weakness is not methodological but presentational: the batch size ambiguity and missing error bars are straightforward to fix but currently muddy the paper's strongest claim. The method itself (MIS + asymmetric batch-split) is well-designed and supported by ablation studies. The reviews do not surface any hidden flaw that would undermine the approach itself.

## Suggestions

1. **Clarify the batch size used for the RA baseline on ImageNet.** This is the single most impactful fix. If the RA baseline used the same doubled batch size, state this explicitly. If not, run an additional experiment or explain why the difference is negligible with evidence (e.g., show that adding 0.24% on ImageNet from batch-size alone is unlikely).
2. **Add standard deviations to the ImageNet table** (Table 2). The paper already runs three repetitions — report the variance.
3. **Tone down the "outperforms" framing in the abstract** to match the CIFAR-100 results where SRA is competitive but not strictly better than TA (Wide) on all models. Use "achieves state-of-the-art among search-free methods on ImageNet" and "competitive with search-free alternatives on CIFAR."
4. **Briefly describe how ε is chosen** (e.g., validation set sweep, or fixed by prior).
