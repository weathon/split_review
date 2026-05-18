Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Channel-Wise Parameter Sharing (CWPS), a method for knowledge transfer that shares parameters at the neuron/channel level rather than at the layer or weight level. It is paired with a Composite Parent Model Search (CPMS) that efficiently determines which channels from previously trained tasks should be reused for a new task. The method is evaluated on the ImageNet-to-Sketch incremental learning benchmark and the DomainNet multi-task learning benchmark, showing competitive accuracy with substantially fewer task-specific parameters compared to layer-wise sharing baselines such as TAPS, PackNet, and Piggyback.

## Strengths

- **Competitive accuracy with far fewer parameters than layer-wise methods**: CWPS achieves mean accuracy comparable to the top-performing methods (the paper transparently states that only Fine-Tuning and Spot-tune achieve higher mean accuracy, but both require ≥1× backbone parameters per task). Against methods that also share parameters (TAPS, PackNet, Piggyback, etc.), CWPS achieves better or comparable accuracy with significantly fewer parameters. This directly supports the claimed precision-to-parameter ratio advantage.

- **CPMS search produces interpretable task relations**: Figure 4 (right) qualitatively shows that the channel assignment patterns reflect intuitive semantic relationships between datasets (e.g., Sketch and Flowers share more neurons than Cars and Flowers). This validates that the search method captures meaningful task relatedness without requiring additional supervision.

- **Natural extension from incremental to multi-task learning**: The method extends straightforwardly via an iterative joint training procedure (Algorithm 1), and Table 2 shows that CWPS maintains its parameter efficiency advantage in the multi-task setting against AdaShare, a dedicated multi-task learning method.

- **Architecture generality**: CWPS is evaluated on ResNet-50, ResNet-18, and DenseNet-121 across two benchmarks, supporting the claim that it can be applied to any network composed of linear and convolutional layers.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental comparison with contemporary parameter-efficient methods.** The paper's Discussion (Sec. 5) names Mixture of Experts, model merging, pruning, and prompt-based methods as relevant alternatives, yet none appear in the experimental tables. More critically, adapter-based approaches (LoRA, Residual Adapters) and prompt-based continual learning methods (L2P, DualPrompt) are standard in parameter-efficient transfer and multi-task learning but are absent from the evaluation. The paper's headline claim is "state-of-the-art precision-to-parameter ratio," but the set of baselines is largely from 2018–2022 (TAPS, PackNet, Piggyback, Spot-tune, AdaShare). Without comparisons against these widely used families of methods, the evidence does not fully support the claimed state-of-the-art status.

- **Hyperparameter λ not specified for main results.** The loss-balancing hyperparameter λ controls the trade-off between accuracy and parameter count. An ablation is shown in Table 3 and Figure 5 using ResNet-18 with 3 training iterations, but the paper never states which λ value was used to produce the headline results in Tables 1 and 2 (ResNet-50, DenseNet-121). Since λ directly determines where on the accuracy–parameter frontier the reported results lie, this omission makes the main results difficult to interpret, reproduce, or compare fairly against baselines.

### Minor

- **No variance or statistical uncertainty reported.** All results in Tables 1 and 2 are single point estimates without error bars, standard deviations, or confidence intervals. For a method whose claimed gains over TAPS are small (on the order of 1% mean accuracy), the absence of any variance measure makes it impossible to assess whether the improvements are systematic or reflect a single favorable run.

- **CPMS initial-training phase not ablated.** The search relies on training the child model for "one-quarter of the total training epochs" (line 108) to obtain reference weights for parent selection. No ablation explores how varying this fraction (e.g., 5%, 10%, 50%) affects the quality of parent selection or final accuracy, leaving the robustness of this heuristic unexamined.

- **λ ablation uses a different backbone than main results.** The hyperparameter study (Table 3) uses ResNet-18, while the main results use ResNet-50 and DenseNet-121. The λ trend may not generalize across architectures, and no validation procedure is described for choosing λ in practice.

- **Task relation metric not precisely defined.** Figure 4 (right) shows "shared neuron" counts between task pairs, but the paper never defines how this metric is computed from the CPMS assignments or whether the measure is stable across runs.

- **Training cost not quantified.** The Conclusion acknowledges "increased video memory usage during training and requiring more steps to save models" as limitations, but provides no quantification (GPU hours, peak memory, training FLOPs). For a method presented as "efficient," the omission of training cost data leaves an incomplete picture.

- **Task ordering sensitivity not explored.** In the incremental learning experiments (Sec. 4.2), tasks are processed in a fixed order. The paper does not discuss whether results depend on the order in which tasks are presented, a known confound in incremental learning evaluations.

### Trivial
None.

## Nice-to-Haves

- An ablation where parent channels are selected randomly instead of via CPMS, to directly validate the necessity and contribution of the search mechanism.
- An analysis of activation distribution statistics in composite parent models compared to homogeneous parents, to address the (speculative) concern about heterogeneous channel composition.
- A normalized efficiency metric such as "mean accuracy per additional parameter" or "relative accuracy retention per percentage of backbone parameters used."

## Removed Points

These points were considered but removed for the stated reasons:

1. **"Potential instability of the composite parent model (heterogeneous channel sources)"** — The paper explicitly states that batch normalization layers are excluded from sharing (line 87: "some layers, such as Batchnorm2d… we do not need to exchange their parameters among tasks"), partially addressing this concern. The remaining concern is speculative — there is no evidence in the paper that heterogeneous compositions cause training instability, and the critic offered no demonstration that they do. Not a verified weakness.

2. **"Mask training details insufficient for reproducibility"** — The paper references Yan et al. (2021) for the mask generation method and distinguishes between soft-mask and hard-mask stages (line 155). Requiring a full re-description of an existing technique goes beyond reasonable reproducibility expectations for a paper in this area.

3. **"CWPS does not achieve the highest accuracy"** — The paper transparently acknowledges this: "only two methods, Spot-tune and Fine-Tuning, get a better mean accuracy than CWPS" (line 193). The paper's claim is explicitly about precision-to-parameter ratio, not absolute accuracy dominance. This is a correct characterization of the paper's own results, not a weakness.

4. **"Multi-task extension: unclear whether worst model is dropped before or after its channels are used as parents"** — The algorithm description (line 167) states that replacement occurs after evaluation: "we only save the model with the best performance… and we replace the weights from the worst model." The concern is not clearly substantiated from the text.

5. **"Discussion section reads as a literature review"** — A stylistic/subjective judgment, not a structural weakness.

## Novel Insights

None beyond the paper's own contributions. The two reviewers primarily debated the sufficiency of the evaluation rather than uncovering surprising or contradictory findings about the method itself.

## Suggestions

1. Add comparisons with at least one modern parameter-efficient method (e.g., LoRA for multi-task or a prompt-based method for incremental learning) to substantiate the state-of-the-art claim.
2. State the exact λ value used for each main result, and ideally show that results are robust across a reasonable range of λ.
3. Report results across multiple random seeds (3–5) with mean and standard deviation for the headline tables to establish statistical reliability.
4. Quantify the training cost (GPU memory, training time per task) to complement the inference-parameter-centric evaluation.
5. Define the "shared neurons" metric used in the task-relation analysis (Figure 4, right) explicitly, and consider a simple quantitative validation (e.g., correlation with a task similarity measure from features).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>