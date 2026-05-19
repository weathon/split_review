- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3
Now I have all the information I need. Let me construct the consolidated review.

---

## Summary

This paper introduces **Motion-Grounded Video Reasoning**, a new task requiring models to output spatiotemporal segmentation masks as pixel-level answers to implicit motion-related questions. The authors collect **GroundMoRe**, a dataset of 1,715 videos, 7,577 questions (four types: Causal, Sequential, Counterfactual, Descriptive), and 249K object masks. They also propose **MoRA**, a baseline combining LLaVA + SAM with a [LOC] token for temporal localization. MoRA achieves 23.13 J&F zero-shot and 27.15 fine-tuned, substantially below human-level performance, confirming the benchmark's difficulty. Twenty-two baselines across four families are evaluated.

## Strengths

1. **Novel task definition that fills a demonstrable gap** — Table 1 systematically compares seven task categories on five criteria (Spatial Context, Temporal Context, Motion Abstraction, Pixel-level Output, Implicit Reasoning). Only the proposed task checks all five boxes, while every existing task is missing at least one. This provides a clear, evidence-based justification for the contribution.

2. **Well-designed dataset with purposeful question typology** — The four question types (Causal, Sequential, Counterfactual, Descriptive) are designed to probe distinct reasoning dimensions. Section 3.2 describes deliberate video selection from four motion-rich scenarios, and Figure 3 shows that most clips (5–15 s) contain motions lasting 2–6 s — providing sufficient temporal context while requiring precise temporal localization.

3. **Comprehensive baseline evaluation across diverse model families** — Table 3 evaluates 22 baselines spanning RVOS models, image/video reasoning segmentation models, and two-stage pipelines. The controlled comparisons include a random baseline (noisy video titles) and dataset diagnostics (Table 4). This thorough benchmarking establishes a realistic performance floor and shows that strong existing models struggle (e.g., SgMg achieves only 17.49 J&F on GroundMoRe vs. state-of-the-art on Ref-YouTube-VOS).

4. **Dataset diagnosis validates the claimed challenges** — Table 4 shows that replacing implicit questions with ground-truth answer expressions improves J&F by 14.29 points on average, and removing temporal context (motion-only clips) degrades performance by 4.68 points. These controlled experiments provide concrete evidence that the dataset tests both implicit reasoning and temporal understanding, as claimed.

5. **Temporal localization ablation isolates the [LOC] head's contribution** — The ablation (Table 6/5) shows a 5.97% relative J&F improvement from adding the temporal localization branch (25.62 → 27.15), with consistent gains across all four question types. This validates that the design meaningfully addresses the temporal dimension of the task.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions (new task, curated dataset, comprehensive baselines) are sound and verifiable from the paper as written.

### Minor

1. **Abstract's 21.5% relative improvement claim is confusingly presented** — The abstract states that MoRA "outperforms the best existing visual grounding baseline model by an average of 21.5% relatively." This figure is approximately correct when comparing the **fine-tuned** MoRA (27.15 J&F, from the ablation table) against the best two-stage baseline SeViLA+SgMg (22.34 J&F, from the main table): (27.15−22.34)/22.34 ≈ 21.5%. However, the main comparison table reports only the **zero-shot** MoRA (23.13 J&F), where the improvement over SeViLA+SgMg is only 3.5%. The abstract neither specifies which baseline defines "best existing visual grounding baseline model" nor which MoRA variant is being compared. This creates ambiguity for readers scanning only the main table, and the phrase needs clarification.

2. **Temporal localization [LOC] mechanism is underspecified** — Section 4.2 states: "The [LOC] embedding will be decoded by an MLP layer into a temporal mask to prevent false activations during frame-wise mask decoding." Several key details are missing:
   - Where is the [LOC] token inserted in the token sequence (beginning, end, after each frame)?
   - How is the output binary temporal mask (length t) used to condition the per-frame SAM decoding? Is it multiplied element-wise, used for frame selection, or applied as attention weighting?
   - How is the temporal mask supervised? The paper mentions "timestamps of the motion" (line 255) but does not specify the loss function (binary cross-entropy over frames?).
   While this is a baseline method in a dataset/task paper (not a methods-first paper), the description is too vague for reproduction. Adding a precise equation or pseudocode would resolve this.

3. **No inter-annotator agreement reported** — The dataset description (Section 3.3) includes quality control steps but does not report quantitative inter-annotator agreement for either question-answer correctness or mask quality (e.g., mask IoU between annotators). For a dataset contribution, this is a common and expected reliability indicator.

4. **No variance or error bars** — The test set has only 382 videos, and some performance differences between methods are small (e.g., MoRA-zs 23.13 vs. SeViLA+SgMg 22.34). Without confidence intervals or standard deviations, it is difficult to assess which differences are meaningful. Reporting variance on the overall J&F metric would strengthen the evaluation.

### Trivial
None.

## Nice-to-Haves

- **A simpler temporal augmentation baseline** — The paper could compare MoRA against a LISA-based video model with a naive temporal extension (e.g., average pooling over frame features or simple frame-level temporal attention) without the dedicated [LOC] head. The current ablation only compares MoRA with/without the [LOC] head, not against a simpler temporal mechanism. This would isolate the benefit of the [LOC] design more cleanly.
- **Failure mode analysis** — The paper notes low absolute scores but does not break down errors: are they primarily temporal (wrong frame selection), spatial (wrong object), or reasoning (wrong object category)? A breakdown by error type would guide future work.
- **Per-question-type qualitative examples for MoRA** — The paper has no qualitative results for MoRA's predictions, making it hard to assess whether the model is genuinely reasoning vs. exploiting spurious correlations.

## Removed Points

These points were raised by reviewers but are removed as per filtering rules, with brief justification:

1. **"Zero-shot" labeling is sloppy/misleading** — *Removed.* The term "zero-shot" is used standardly in the literature to mean "evaluated without fine-tuning on the target dataset." All models in Table 3 (including RVOS models trained on MeViS/Ref-YouTube-VOS and MoRA pre-trained on those datasets) are evaluated without training on GroundMoRe. The usage is consistent and not misleading.

2. **Dataset size is modest compared to Perception Test** — *Removed.* 1,715 videos with 249K pixel-level masks is reasonably "large-scale" for a spatiotemporally annotated dataset. The comparison with Perception Test (which lacks pixel-level motion grounding) is apples-to-oranges.

3. **Missing baseline: video-level LISA with 3D conv** — *Moved to Nice-to-Have.* This is a reasonable suggestion for future work but does not undermine the current evaluation, which already compares 22 baselines across four families.

4. **Pure formatting/style nitpicks** — *Removed.* Per instructions, parser-induced formatting artifacts are not author errors.

## Novel Insights

The most striking finding across the reviews is the **diagnosis experiment in Table 4's cross-reading with the low overall scores**: when explicit referring expressions replace implicit questions, the best RVOS model (SgMg) jumps from 17.49 to 30.16 J&F — nearly double. This reveals that the primary bottleneck is not pixel-level segmentation capability (which these models already have) but rather **the implicit reasoning step that links a motion-related question to the correct entity**. Conversely, the temporal context diagnosis (removing context → 4.68 point drop) shows that temporal understanding is a secondary but non-trivial challenge. This suggests that the next generation of models for this task should focus on improving *reasoning-to-grounding* alignment (e.g., better LLM integration with the segmentation head) rather than fixing segmentation quality per se.

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the abstract's 21.5% claim** — Either (a) specify that this compares the fine-tuned MoRA (27.15 J&F) against the best two-stage baseline (SeViLA+SgMg, 22.34 J&F), or (b) if the zero-shot model is the intended reference, correct the figure to 3.5% relative improvement over SeViLA+SgMg.
2. **Add a precise description of the [LOC] mechanism** — Provide an equation showing how the temporal mask conditions per-frame SAM outputs, specify where in the token sequence the [LOC] token is placed, and state the loss function used for temporal mask supervision.
3. **Report inter-annotator agreement** for both mask quality (average pairwise IoU) and question-answer consistency.
4. **Add error bars or confidence intervals** for the main results (Table 3) to help readers assess the significance of performance differences.
5. **Include qualitative examples** of MoRA's predictions (successes and failures) to give readers intuition about the model's behavior.
