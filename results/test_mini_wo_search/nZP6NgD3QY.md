Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

---

## Summary

This paper introduces AdaMerging, an unsupervised method for multi-task model merging that learns per-task or per-layer merging coefficients via entropy minimization on unlabeled test data. The key idea is to replace the single, grid-searched λ used in Task Arithmetic/Ties-Merging with automatically learned coefficients, treating each task vector (or each layer of each task vector) differently. Experiments on eight image classification benchmarks with CLIP ViT-B/32 and ViT-L/14 backbones show substantial gains over existing task-vector merging methods in performance, generalization to unseen tasks, and robustness to distribution shifts.

## Strengths

1. **Significant and consistent performance gains over strong baselines.** Table 1 shows Layer-wise AdaMerging achieves 80.1% average accuracy on eight tasks with ViT-B/32, compared to Task Arithmetic (69.1%) and Ties-Merging (72.4%) — an 11-point improvement over the former. Table 2 confirms similar gains on ViT-L/14 (90.8% vs. 84.5%/86.0%). These improvements are consistent across nearly all individual tasks.

2. **Empirical justification of entropy as a valid proxy objective for coefficient learning.** Figure 2 provides two pieces of evidence: (a) grouping test samples by entropy shows that lower-entropy bins consistently have lower average prediction loss, and (b) the Spearman correlation between entropy and loss across all eight tasks is 0.87. This grounds the core methodological choice in data rather than pure intuition.

3. **Demonstrated generalization to unseen downstream tasks.** Table 3 shows that when merging six seen tasks, AdaMerging achieves 70.0% on held-out tasks (MNIST/EuroSAT) vs. 61.7% for Task Arithmetic and 59.6% for Ties-Merging. A second unseen-task pair (RESISC45/SVHN) shows a similar advantage (55.5% vs. 51.1%/53.9%). Because these tasks were never used for coefficient optimization, this is a clean evaluation that directly supports the generalization claim.

4. **Robustness across seven test distribution shifts.** Table 4 consistently shows AdaMerging outperforming Task Arithmetic across all corruptions (Motion Blur, Impulse Noise, Gaussian Noise, Pixelate, Spatter, Contrast, JPEG Compression), with average improvements per corruption ranging from 5.8% to 11.2%. The robustness experiment optimizes coefficients on the clean test set and evaluates on corrupted data — a valid out-of-distribution evaluation.

5. **Automatic discovery of interpretable coefficient patterns.** Table 5 shows that learned task-wise coefficients differ substantially across tasks (e.g., 0.14 for Cars vs. 0.40 for GTSRB in Task-wise AdaMerging), and Figure 3 reveals that shallow layers consistently receive smaller coefficients than deep layers. This aligns with the intuition that shallow layers learn general features while deep layers are task-specific, and demonstrates that the method captures meaningful structure without manual tuning.

## Weaknesses

### Fatal
None.

### Major

1. **The evaluation protocol is not clearly specified regarding test-data reuse.** The paper states that entropy minimization is performed on "unlabeled multi-task test samples" (line 137) to optimize merging coefficients, and reports "average accuracy of MTL model on the test set of all tasks" (line 174). No description is given of any split between data used for coefficient optimization and data used for evaluation. If the same test samples are used for both, the main performance results (Tables 1, 2) are transductive — they measure how well the model adapts to the specific test set it saw, not generalization to unseen data from the same distribution. While this is consistent with the test-time adaptation literature that inspires the method (Tent, ICLR 2021), **the paper does not acknowledge this transductive nature or discuss its implications**. The asymmetry with baselines is also unaired: Task Arithmetic and Ties-Merging use a single λ, which Fig. 1 (caption) indicates was selected as the "best average accuracy" value (λ=0.3), implying they also peek at the test set but only for one scalar. AdaMerging optimizes many coefficients on test data, which is a qualitatively different level of access. The paper's mention that "even if only 0.1% or 1% of unlabeled tests are available, our method can have significant performance improvements" (line 154) suggests awareness of this concern, but no corresponding results are reported, and the main tables remain ambiguous. **This is the single most important issue to resolve.** The generalization experiment (Table 3) and robustness experiment (Table 4) provide partial corroborating evidence that is not affected by this concern in the same way, which prevents this from being a fatal flaw, but the main performance claims in Tables 1–2 need clarification.

### Minor

1. **No comparison to a test-time adaptation baseline.** Since the method draws explicit inspiration from Tent and TTA, a natural baseline would be to apply standard TTA (e.g., entropy minimization of the full model weights) to a merged model with a fixed coefficient, then compare against optimizing only the coefficients. This would isolate whether the benefit comes from the coefficient adaptation scheme or simply from entropy minimization on test data. Missing this comparison weakens the ablation story.

2. **The 0.1%/1% data-efficiency claim is stated but unsupported by experimental results.** Line 154 asserts that even minimal test data yields significant improvements, but no table or figure in the paper reports results with these fractions. This is a potentially valuable practical result that should be backed with evidence.

3. **No discussion of limitations or failure cases.** The paper does not discuss scenarios where unlabeled test data from all tasks is unavailable (e.g., merging public models without target data), the potential for the proxy objective to misalign with task-specific goals, or any instability in coefficient optimization. A brief limitations paragraph would strengthen the paper's scholarly completeness.

### Trivial

- None.

## Nice-to-Haves

- Report results with a clean held-out split (e.g., 20% of test data for coefficient optimization, 80% for evaluation) to directly address the evaluation protocol concern.
- Report variance or confidence intervals across multiple runs (e.g., different random seeds for coefficient optimization).
- Provide wall-clock time or iteration counts for coefficient optimization to substantiate the "very cheap" claim.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Baselines are not on equal footing because they select λ without test data access"** (Harsh Critic, Critical Issue 2). **REMOVED — factually inaccurate.** The paper's Fig. 1 caption states that Task Arithmetic and Ties-Merging "achieved the best average accuracy when coefficient λ=0.3," indicating their λ was also selected based on test-set performance (trying multiple values and picking the best one). The critic's assumption that baselines use a validation set is not supported by the paper. The asymmetry in *degree* of test-data access (one scalar vs. many coefficients) is real and is handled in Major weakness 1 above, but the claim that baselines have *no* test data access is wrong.

- **"The correlation analysis shows Spearman=0.87 but does not demonstrate causality"** (Harsh Critic, Section-by-Section on Methodology). **REMOVED — speculative and not a concrete weakness.** The paper does not claim causality; it claims correlation as a justification for using entropy as a *surrogate* objective, which is exactly what correlation evidence supports. Demanding causality is setting an inappropriate bar.

- **"The 11% improvement is likely inflated by the evaluation protocol"** (Harsh Critic, Abstract & Introduction). **REMOVED — speculative framing.** The protocol issue is real and is captured in Major weakness 1, but asserting *inflation* as a foregone conclusion without evidence is not appropriate for a review.

- **"Some of the robustness improvement could be due to unfair advantage of test-data access"** (Harsh Critic, Section-by-Section on Robustness). **REMOVED — speculative and partially contradicted by the paper.** The robustness experiment optimizes on *clean* test data and evaluates on *corrupted* test data — this is a distribution shift setting where the "unfair advantage" argument is substantially weaker. The critic provides no specific anchor in the paper for why this concern applies here.

- **Several generic strengths from the Strength Finder** (e.g., "addressed an important problem," "practical data efficiency" beyond what is shown). **REMOVED — generic or insufficiently supported.** The data efficiency strength is kept but downgraded to a minor weakness (unsupported claim) rather than a strength.

## Novel Insights

The reviews converge on a core observation that the paper itself only partially acknowledges: the method's reliance on test data for coefficient optimization is simultaneously its main innovation and its main evaluation liability. The harsh critic correctly identifies that the evaluation protocol is underspecified, but overreaches by calling this "fatal" — the generalization and robustness experiments provide meaningful corroborating evidence that would survive even a strict held-out evaluation. A genuinely novel insight that emerges from both reviews is that the paper would benefit from disentangling two distinct sources of gain: (a) the flexibility of per-task/per-layer coefficients (which could, in principle, be set via grid search on a validation set), and (b) the automatic optimization via entropy minimization on target data. An ablation that compares AdaMerging against a version that sets per-task coefficients manually (even on a subset of tasks) would cleanly separate these factors.

## Suggestions

1. **Clarify the evaluation protocol upfront.** Add a subsection explicitly stating whether the test data used for coefficient optimization is disjoint from the test data used for accuracy reporting. If the current evaluation is transductive (same data for both), say so, explain that this is consistent with the TTA literature, and ideally add a secondary experiment with a held-out split (e.g., 20% for optimization, 80% for evaluation) to show that the gains persist under a stricter protocol.

2. **Add a TTA baseline.** Apply entropy minimization (e.g., via Tent) to a merged model with fixed Task Arithmetic coefficients on the same unlabeled test data. This would isolate whether the improvement comes from coefficient adaptation specifically or from test-time entropy minimization more broadly.

3. **Support the data-efficiency claim with results.** If even 0.1% or 1% of test data yields significant gains, include a small figure or table showing performance vs. fraction of test data used.

4. **Acknowledge the data-requirement asymmetry explicitly.** Discuss scenarios where unlabeled target-domain data is available (e.g., an entity merging its own fine-tuned models and collecting unlabeled queries) vs. scenarios where it is not (e.g., merging public models without any target data).

## Score and Decision

**Overall assessment:** The paper addresses a well-motivated problem, proposes a sound method with a clear justification (entropy as a proxy for loss, validated via Spearman correlation), and provides extensive experiments across performance, generalization, robustness, and coefficient analysis. The core weakness is the underspecified evaluation protocol regarding test-data reuse, which prevents full confidence in the main tables. However, the generalization and robustness experiments provide partially orthogonal evidence that the method delivers meaningful gains even under cleaner evaluation settings. The paper is a solid contribution that would be strengthened substantially by clarifying the evaluation protocol and adding the suggested ablations.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>