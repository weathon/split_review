Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper uses sparse autoencoders (SAEs) to study in-context learning (ICL) in a 2B-parameter model. It makes two main methodological contributions: (1) Task Vector Cleaning (TVC), an optimization procedure that decomposes task vectors into a sparse sum of <4 SAE latents while preserving steering performance, and (2) adaptations of Sparse Feature Circuits (SFC) to larger models and ICL. Using these methods, the paper identifies two causally relevant feature families: *task-execution features* that activate just before task completion and can induce zero-shot task performance, and *task-detection features* that activate on completed task instances and are causally connected to execution features through attention.

## Strengths

- **TVC produces sparse, performant task vector decompositions.** Figure 3a shows TVC matches original task vector steering performance until layer 14, while Figure 3b shows it reduces active SAE features from ~15 to <4 on average at layer 12. The comparison against four baselines (original task vectors, naive SAE reconstruction, ITO with two L0 targets) is thorough and supports the method's advantage.

- **Task-execution features show task-specific causal relevance in steering experiments.** Figure 5 demonstrates that individual executor features boost exactly one task (or a group of related tasks like translation to English) when steered into zero-shot prompts, and do not significantly affect unrelated tasks. Table 1 shows these features activate predominantly on arrow tokens, consistent with their hypothesized role. This is a clean, interpretable finding.

- **Circuit specificity is validated through cross-task ablation.** Figure 6 shows that ablating the top-IE nodes for one task degrades faithfulness only for that task (and related tasks in the same category), leaving unrelated tasks largely unaffected. This provides evidence that the discovered circuits are task-specific rather than generic ICL components.

- **SFC adaptation to larger models and ICL is a non-trivial engineering contribution.** The token position categorization (Section 4.1.1) and loss modification (Section 4.1.2) address real challenges in scaling SFC from toy tasks to a 2B-parameter model processing structured ICL prompts.

## Weaknesses

### Major

- **The causal connection experiment between detection and execution features is critically under-specified.** The paper states (line 221): "We then ablated detection directions while fixing attention patterns and measured the decrease in execution activations." Neither "fixing attention patterns" nor the ablation procedure itself is explained. The metric is a change in SAE latent activations rather than a direct behavioral measure (e.g., task loss). Without a clear, formal description of the intervention, the strong causal claim that Figure 8 purportedly supports cannot be properly evaluated. This is the paper's most significant experimental gap, as the detection→execution causal link is central to the paper's narrative.

- **TVC evaluation lacks held-out generalization checks.** The TVC algorithm optimizes sparse decomposition weights by minimizing NLL on a batch of zero-shot prompts. The paper reports steering performance (Figure 3a) but never specifies whether the evaluation uses the same prompts as the optimization batch or a held-out set. No cross-validation or generalization experiment is reported. Without evidence that the discovered features generalize to unseen prompts for the same task, it is unclear whether TVC captures genuine abstract task representations or overfits to prompt-specific patterns. Given the extreme sparsity (<4 features), this is a real risk.

- **No variance or uncertainty estimates are reported.** All steering effects (Figures 5, 7) and ablation results are presented as point estimates without confidence intervals, standard errors, or replication across random seeds. Given the relatively small number of tasks and the optimization involved, the reader cannot assess the reliability or stability of the results.

### Minor

- **Novelty relative to prior ICL circuit work is acknowledged but not sharply delineated.** The paper mentions (line 235) that Wang et al. "finds similar results with different terminology (information flow instead of circuits, 'label words' instead of task-detection features)." However, it does not systematically compare the discovered features against those prior findings or explain what the SAE lens specifically adds that was not accessible with earlier methods. The paper gestures at "interpretability, precision" but does not substantiate this claim.

- **The paper overstates its claims in the abstract/introduction.** The phrase "uncovering two of the most important causally implicated feature families behind ICL" is too strong: only two families are identified, there is no evidence they are *the* most important, and the causal evidence for the detection→execution link is incomplete (see Major weakness).

- **Two tasks (person profession, present simple gerund) show anomalously weak detection→execution connections** (noted line 227), and two other tasks (person profession, football player position) were excluded from Figure 6 due to unstable faithfulness (line 206). The paper mentions these briefly but does not investigate or explain them. While honest, this raises questions about the generality of the findings.

- **Activation mass tables (Tables 1, 2) and steering heatmaps (Figures 5, 7) would benefit from numerical values in the text.** The figures are not visible in this text extraction, but the descriptions of the findings could be more precise with reported statistics.

### Trivial

- None.

## Nice-to-Haves

- A sensitivity analysis for TVC hyperparameters (L1 regularization coefficient, optimizer settings) would strengthen reproducibility. The paper mentions sweeps across models but provides no detailed sensitivity results.
- The SFC faithfulness threshold analysis (0.5 with "a few hundred" nodes) would benefit from discussion of whether circuits at this scale are meaningfully interpretable, or whether the complexity is intrinsic to ICL.
- Explicit confidence intervals or bootstrap estimates for the main steering and ablation results would substantially improve scientific rigor.

## Removed Points

These points were raised by reviewers but are excluded from the main review for the reasons noted:

- *"TVC algorithm details (optimizer, learning rate, steps) relegated to appendix"* — The appendix is stripped by the PDF parser; these details exist in the original submission. Removed per the rule about missing appendix content.
- *"The small number of tasks limits generality"* — The paper uses the established dataset from Todd et al. (2024), which spans several categories. This is a standard scope, not a weakness.
- *"Overfitting concern: 'the optimization target is the same batch of prompts used to measure success'"* — This is asserted by the reviewer but the paper does not explicitly state whether the batches are the same. The concern about absent held-out evaluation is retained in Major weaknesses above, but the specific claim that they are identical batches is speculative and removed.
- *"Related work missing"* — Removed per the rule that I cannot confirm missing references without external sources.
- *"Unfair comparison with baselines"* — The comparison favors the author's method, and the baselines selected (original task vector, naive SAE reconstruction, ITO) are standard and appropriate. The asymmetry favors the author's method, not the baselines.
- Various formatting/typo/style nitpicks — Removed per the rules on parser artifacts and formatting.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension between the paper's ambitious causal claims and the evidence provided, but do not introduce genuinely novel analytical perspectives beyond what a careful reading of the paper would reveal.

## Suggestions

1. **Clarify the causal intervention in Section 4.2.** Provide a formal description of what "ablating detection directions" and "fixing attention patterns" means. Consider replacing the complex intervention with a simpler zero-ablation of detection features at relevant positions, measuring downstream task loss rather than execution feature activations. This would produce a cleaner test of the detection→execution link.

2. **Add held-out prompt evaluation for TVC.** Run TVC on a training set of prompts, then evaluate the resulting sparse decomposition on held-out prompts for the same task. Report whether the steering performance gap between TVC and the original task vector remains comparable on held-out data. This single addition would substantially increase confidence that TVC identifies genuine task features rather than overfitting.

3. **Add uncertainty estimates.** Report confidence intervals, standard errors across prompt batches, or replication across random seeds for the main steering and ablation results (Figures 3, 5, 6, 7, 8).

4. **Reduce the strength of the claim** in the abstract ("two of the most important causally implicated feature families") to something more measured like "two causally relevant feature families" — the current phrasing overstates what is demonstrated.

5. **Systematically compare** the task-detection features against the "label words" phenomenon from Wang et al. to clarify whether the SAE lens reveals genuinely new structure or reframes known findings in a different basis.

## Score and Decision

This paper makes solid methodological contributions (TVC, SFC adaptation) and presents interesting evidence for task-specific feature families in ICL. The main weaknesses — an under-specified causal experiment and lack of held-out generalization checks for TVC — are addressable but significant. The core findings are plausible and the methods are well-motivated. I recommend acceptance conditional on addressing the major concerns.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>