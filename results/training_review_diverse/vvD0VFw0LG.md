I now have a complete picture of both the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

PruningBench presents the first comprehensive benchmark for structural pruning, evaluating 16 existing pruning methods across multiple CNN and ViT architectures (ResNet18/50, VGG19, ViT-small, YOLOv8) on classification (CIFAR, ImageNet) and detection (COCO) tasks. The benchmark introduces a unified four-stage framework (sparsifying, grouping via DepGraph, iterative pruning, finetuning) to enforce controlled comparisons—holding FLOPs, parameter budgets, grouping strategy, and finetuning fixed—and produces 13 leaderboards from 645 pruned models. The central empirical finding is that simple weight-norm-based criteria (MagnitudeL1, MagnitudeL2) are robust top performers across most settings, and no single method consistently dominates.

## Strengths

- **Largest systematic evaluation of structural pruning methods to date.** The paper evaluates 16 methods across 5 architectures and 3 datasets/tasks, producing 645 pruned models and 13 leaderboards (Section 4). No prior work has compared this breadth of structural pruning methods under a single controlled framework.

- **Explicitly identifies and addresses three critical pitfalls in prior evaluations.** Table 1 documents how prior works suffer from limited comparisons, inconsistent experimental settings, and failure to control FLOPs/parameter budgets. PruningBench directly mitigates all three via its unified framework—a genuine contribution that advances evaluation standards for the field.

- **Separates sparsifying-stage (regularizer) and pruning-stage (importance criterion) methods.** The framework cleanly isolates the component under test: when benchmarking importance criteria, the sparsifying step is skipped and grouping+finetuning are fixed; when benchmarking regularizers, the pruning stage uses a fixed criterion (Section 2, Figure 1). This yields apples-to-apples comparisons that prior work conflated.

- **Designed for extensibility and reproducibility.** The paper provides interfaces for implementing new importance criteria and sparsity regularizers (Section 1, Appendix A.3.1), and states that an online platform will allow users to customize and reproduce experiments. This lowers the barrier for community adoption.

## Weaknesses

### Fatal
None.

### Major

- **Faithfulness of re-implementations is unvalidated.** The paper states it "systematically evaluates 16 existing structural pruning methods" but provides no evidence that its re-implementations reproduce the performance reported in the original papers. Given the unified framework (DepGraph grouping + iterative pruning) may differ from how methods were originally designed and evaluated, the leaderboard rankings could reflect implementation artifacts rather than genuine differences between algorithms. A benchmark paper's central claim is trustworthy comparison, and this gap directly undermines that trust. At minimum, reproducing a single data point from each original paper under PruningBench's closest settings would substantially strengthen credibility.

- **No discussion of limitations or potential bias from framework design choices.** The paper standardizes three components: DepGraph-based automatic grouping, iterative pruning with a fixed schedule, and a shared finetuning protocol. While standardization is the point, the paper does not acknowledge that these choices embed assumptions that may favor or disadvantage particular methods. For example, methods originally designed for one-shot pruning or for layer-specific grouping are forced into the DepGraph + iterative mold. Without any sensitivity analysis (e.g., comparing rankings under alternative grouping schemes or pruning schedules), the paper cannot demonstrate that its framework is neutral with respect to the methods compared. A brief limitations subsection discussing these caveats would significantly improve scholarly thoroughness.

### Minor

- **Main paper foregrounds only two leaderboards.** Due to space constraints, only ResNet50 on CIFAR100 (Table 2) and ViT-small on ImageNet (Table 3) appear in the main text; the remaining 11 leaderboards (including all detection results on COCO) are relegated to the appendix. While this is standard practice, briefly referencing at least one cross-task or cross-architecture result (e.g., detection trends or findings from VGG19) in the main text would better demonstrate the benchmark's breadth and give readers a concrete sense of the scope.

### Trivial
None.

## Nice-to-Haves

- **Sensitivity analysis:** Running a subset of methods under an alternative grouping scheme (e.g., manual layer-wise grouping) and a one-shot pruning variant, then comparing whether rankings shift, would substantially strengthen claims about the framework's fairness.
- **Reproduction validation:** For each of the 16 methods, reporting at least one data point from the original paper under the closest possible PruningBench settings to validate re-implementations.
- **Foregrounding surprising findings:** If the benchmark reveals cross-architecture or cross-task trends (e.g., ViT vs. CNN differences, detection-specific behavior), highlighting these in the main text would strengthen the paper's narrative beyond the (somewhat expected) finding that weight-norm methods are robust.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"The paper does not clarify which stages are fixed when evaluating each type"** — The paper explicitly states: "Note that this stage [Sparsifying] is skipped when benchmarking methods on importance criteria" and "Grouping stage and the finetuning stage are fixed the same for benchmarking all pruning methods" (Section 2, Figure 1 caption). The reviewer's claim is factually incorrect.

- **"Section 4.2 findings are missing from the main paper"** — The extracted text shows Section 4.1 ending with "Now we provide more detailed analyses... by answering the following questions," followed by a gap before Section 5. This is a parser artifact; Section 4.2 exists in the original submission. Per policy, parser-stripped content should not be penalized.

- **"Section 3 training details are missing from main paper"** — Section 3 (PruningBench Settings) content was stripped by the parser. It exists in the original submission.

- **"Detection results not shown in main paper"** — The paper acknowledges space constraints and refers readers to 13 leaderboard tables in the appendix. This is standard practice for benchmark papers with extensive results, not a flaw.

- **"The finding that weight-norm methods perform well is not novel, consistent with Blalock et al. 2020"** — Blalock et al. 2020 studied *unstructured* pruning; this paper's setting is *structural* pruning, where the parameter grouping and budget control are different. The comparison conflates two distinct regimes.

## Novel Insights

The reviews reveal a tension inherent in benchmarking structural pruning: standardization (fixing grouping, pruning schedule, finetuning) is necessary for controlled comparison, but the very act of standardizing embeds design choices that may not be neutral across methods. The paper's weakness is not that it standardizes—that is its contribution—but that it does not acknowledge or characterize the trade-offs involved. A stronger version of this paper would frame its framework not as a neutral arbiter but as a *specific* standardized setting whose inductive biases are transparently documented and empirically probed. The community would benefit more from an honestly scoped benchmark than from one that claims comprehensiveness without examining its own blind spots.

## Suggestions

1. Add a short "Limitations and Design Choices" subsection discussing how DepGraph grouping and iterative pruning may interact with method families differently.
2. Validate re-implementations by reproducing at least one data point per method from the original paper under the closest possible settings.
3. Include a sensitivity experiment (even on a small subset of methods) comparing rankings under a different grouping or pruning schedule to probe framework neutrality.
4. Move at least one cross-task finding (e.g., from COCO detection) into the main text to illustrate the benchmark's breadth.

## Score and Decision

This paper addresses a genuine need—the structural pruning community lacks standardized evaluation—and its scope (16 methods, 5 architectures, 3 tasks, 645 experiments) is impressive. The separation of sparsifying-stage and pruning-stage methods is a well-motivated design choice, and the extensibility features are a practical contribution. However, the two major weaknesses directly impact trust in the benchmark's core output: the leaderboard rankings. Without validated re-implementations and without acknowledging/discussing potential biases in the fixed framework choices, the paper's central claim—providing "a more comprehensive picture of the state of the field"—is insufficiently supported. These issues are addressable with additional analysis and exposition, and a revised version would be a strong candidate for acceptance. In its current form, the paper is borderline but falls short of the reliability threshold expected of a benchmark contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>