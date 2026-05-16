I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces Dynamic Adapter Merging (DAM), a rehearsal-free domain-incremental learning method for Video Question Answering (VidQA). DAM sequentially trains lightweight domain-specific adapters (≤5% of backbone parameters) for each dataset, uses a non-parametric centroid-based router to score adapters at test time for samples from unknown domains, and dynamically merges the top-k adapter weights to compensate for inaccurate router predictions. On a benchmark of six VidQA datasets with a 1.2B-parameter FrozenBiLM backbone, DAM outperforms the best prompt-based baseline (S-Prompts) by 9.1% average accuracy with 1.9% less forgetting, and the method extends to image-based VQA with a 4.1B-parameter BLIP-2 model.

## Strengths

1. **First systematic exploration of rehearsal-free DIL for VidQA on large models.** The paper identifies a realistic and underexplored problem — existing DIL methods were designed for image classification with relatively small domain gaps, while VidQA introduces major disparities in domain, dataset size (up to 48×), video duration, and cross-modal reasoning. The constructed benchmark of six diverse VidQA datasets makes this setting concrete and reproducible.

2. **Dynamic adapter merging is principled and well-motivated by empirical evidence.** The paper shows that merging multiple adapters provides the largest gains precisely when the router is inaccurate: Table 3 shows a 4.9% gain when router accuracy is 51.0% (MSVD) versus only 0.2% when accuracy approaches perfection (LSMDC). Figure 4 further demonstrates up to ~30% relative improvement when router accuracy drops to 0%. This direct link between the method's motivation and its empirical behavior is the paper's strongest evidence.

3. **Consistent and substantial SOTA improvements across settings.** DAM achieves a 9.1% average accuracy gain over S-Prompts with 1.9% less forgetting on VidQA (Table 1), and 4.4% gain with 1.2% less forgetting on VQA (Table 4). The improvement holds across all six individual datasets and generalizes to a different backbone (BLIP-2) and task (image VQA), demonstrating robustness beyond a single configuration.

4. **Simple non-parametric router outperforms learned alternatives.** Table 2 shows that the centroid-based cosine-similarity router (no trainable parameters) yields better downstream VidQA accuracy than the learned routers from L2P, S-Prompts, and CODA-Prompt. This is a practically valuable finding — it removes a source of optimization instability and makes the method easier to adopt.

## Weaknesses

### Fatal
None.

### Major

1. **Missing variance estimates for all main results.** The paper reports "results averaged from 5 runs with different random seeds" (Section 4) but provides no standard deviations, confidence intervals, or significance tests. The claimed 9.1% improvement over S-Prompts and 6.8% gap between DAM and EwC (77.1 vs. 70.3) need statistical context — especially given the challenging setting (48× dataset size imbalance, high domain diversity) that likely inflates variance. Without this, the reader cannot assess whether the observed differences are reliable or within noise. The tables are embedded as images, so I cannot verify whether std devs appear in them — but the paper text never mentions them, and the reviewer's point stands.

2. **Only one domain order is tested.** All experiments use a single fixed training order (iVQA → MSVD → MSRVTT → LSMDC → ActivityNet → TGIF). Domain-incremental methods are known to be sensitive to domain order (e.g., early-trained adapters may dominate via initialization propagation). Without at least one alternative ordering (e.g., reverse, random), the relative gains over baselines may partially reflect order artifacts rather than method quality. This is the most impactful missing ablation.

### Minor

3. **Forgetting metric is not defined in the paper.** The text states "Following (Wang et al., 2022c;b), we use the average accuracy and forgetting as the evaluation metrics" (Section 4), but never defines how forgetting is computed for this domain-incremental VidQA setting. The cited references define forgetting in class-incremental settings — it is not obvious how that carries over to DIL where the task (answering questions about videos) is the same across domains. The "1.9% less forgetting" claim is uninterpretable without a precise definition.

4. **Continual initialization scheme is not ablated.** The paper initializes each domain's adapter from the last-trained adapter's weights (Section 3.1), arguing this "leads to a smoother parameter space" for merging. However, no experiment compares this against training each adapter from scratch (random initialization) or from the same base weights. It is unclear how much of the benefit comes from weight inheritance versus the adapter architecture itself.

5. **Router feature extraction is underspecified.** Section 3.2 computes centroids by averaging "multimodal video-language features extracted by a pretrained model *f*." FrozenBiLM produces separate visual and text representations that interact through cross-attention — it is not specified how a single feature vector per video-question pair is obtained (e.g., pooled cross-modal output? concatenation? CLS token?). Since the router is a central component, this is essential for reproducibility.

6. **Temperature τ=0.01 is set without justification or sensitivity analysis.** The softmax temperature in the router (Section 3.2) is a key hyperparameter that controls how sharply the router selects adapters. No ablation or motivation for this specific value is provided.

7. **No results for k>2 in adapter merging.** Table 3 compares k=1 (no merging) vs. k=2, but does not report k={3,4,5,all}. Since the paper argues that static merging of all adapters is ineffective, showing the full curve from k=1 to k=all would more thoroughly characterize the trade-off and confirm that k=2 is genuinely optimal rather than simply untested for larger values.

8. **No absolute accuracy values for the OOD scaling experiment (Figure 3).** Figure 3 reports only normalized accuracy. The absolute accuracy values should also be reported so readers can assess the actual performance levels, not just relative trends.

9. **Computational overhead of merging is asserted without measurement.** The paper states merging has "negligible computational overhead" (Section 3.3) but provides no concrete comparison (e.g., FLOPs, wall-time, or latency per sample) to substantiate this efficiency claim.

### Trivial

10. Table column headers and training order in Table 1: The training domain order is described as "left to right" but the first column appears to be individual dataset columns. The presentation could be clearer about which columns correspond to which domain.

## Nice-to-Haves

- A comparison to rehearsal-based methods (VQACL, CLCrossVQA) adapted to the same backbone would provide useful context, though the paper's focus on rehearsal-free DIL is clear and defensible. This is scope-creep rather than a core flaw.
- A wider sweep of the merging hyperparameter k beyond 2 (see Weakness #7) would strengthen the merging analysis.
- An alternative domain order ablation (see Weakness #2) is the single highest-leverage addition.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing comparison to VQACL/CLCrossVQA as a structural flaw**: The paper explicitly scopes to rehearsal-free DIL and correctly categorizes these as rehearsal-based methods (Section 2). Demanding that a rehearsal-free paper include rehearsal-based baselines is a scope-creep request. However, a softened version (Nice-to-Have) is retained above.
- **Criticism about prompt token placement in FrozenBiLM**: The paper states "add L=10 prompt tokens prepended to their existing tokens as was done in (Wang et al., 2022b)" — this follows established methodology. The concern is not a structural weakness and the detail is standard in the field.
- **Various formatting and presentation nitpicks** about table layout: These are parser artifacts from the PDF extraction, not author errors.
- **"No validation set" / "reproducibility concern about cited models"**: The paper cites standard models (FrozenBiLM, BLIP-2, CLIP, DeBERTa) that are publicly available. Any criticism doubting their existence or release status is removed per hard rules.

## Novel Insights

The most insightful finding to emerge across the reviews is the **inverse relationship between router accuracy and the value of merging** — the method's core thesis is that dynamic merging is not a universal enhancement but a targeted remedy for router failures. The synthetic experiment (Figure 4) demonstrating ~30% relative improvement at 0% router accuracy makes this relationship concrete and goes beyond what a typical DIL paper provides. This finding has implications beyond VidQA: it suggests that dynamic merging strategies could benefit any DIL setup where domain prediction is inherently ambiguous (e.g., fine-grained domain distinctions, heavily imbalanced dataset sizes). The paper's evidence that a simple non-parametric router outperforms complex learned routers (Table 2) further reinforces the idea that in DIL with large domain gaps, simplicity and stability of the router matter more than its capacity.

## Suggestions

1. **Report standard deviations for all main results** (Tables 1, 4) and include a simple significance test (e.g., paired comparison of DAM vs. S-Prompts across datasets using a Wilcoxon signed-rank test).
2. **Test at least one alternative domain order** (e.g., reverse order or random permutation) to verify that DAM's relative gains are not order artifacts.
3. **Define the forgetting metric explicitly** in the evaluation section.
4. **Ablate the continual initialization scheme** by comparing against adapters trained from scratch (same random init) to isolate the benefit of weight inheritance.
5. **Specify how the multimodal feature vector $f(x)$ is obtained** from FrozenBiLM for the router centroids.
6. **Include an ablation of the temperature hyperparameter** $\tau$ and report results for a wider range of merging sizes $k$.

## Score and Decision

The paper tackles a novel and important problem (rehearsal-free DIL for VidQA), proposes a well-motivated solution (DAM), and provides consistent empirical improvements across two model families and two tasks (VidQA and VQA). The weaknesses are real but addressable — they require additional experimental validation and clarifications, not a redesign of the method or a change to the core claims. The paper is a solid contribution to both the continual learning and video-language communities.

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>