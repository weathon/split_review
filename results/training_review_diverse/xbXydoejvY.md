Here is the final consolidated review.

---

## Summary

This paper proposes Channel-Wise Parameter Sharing (CWPS), a method for knowledge transfer that shares parameters at the granularity of individual neurons/channels rather than entire layers, along with a Composite Parent Model Search (CPMS) that assigns each channel to the most similar parent weight via a distance metric. The paper targets incremental and multi-task learning for convolutional backbones and reports competitive accuracy-to-parameter trade-offs on the ImageNet-to-Sketch and DomainNet benchmarks.

## Strengths

- **Novel channel-level granularity for parameter sharing.** The paper identifies a natural granularity gap — prior methods share at the layer level (too coarse) or individual weight level (too fine, breaking neuron atomicity) — and proposes sharing at the channel/neuron level, which is a well-motivated intermediate point. Section 3.2.2 and Figure 1 clearly articulate this distinction and formalize per-kernel assignment via Equations (3)–(5).

- **CPMS provides an efficient, similarity-based search for parent channels.** The search avoids combinatorial optimization by using a simple L2/cosine distance per channel, requiring only a short warm-up fine-tuning phase (one-quarter of total epochs) to obtain reference weights. Equation (3) formalizes this as an argmin over distance, making it simple and reproducible.

- **Competitive accuracy-to-parameter ratio on standard benchmarks.** Table 1 shows CWPS achieving 79.3% mean accuracy with 0.8× backbone parameters on ImageNet-to-Sketch, outperforming parameter-efficient methods like TAPS (77.6%, 0.7×) and Piggyback (76.0%, 2.0×). Table 2 shows CWPS exceeding AdaShare on DomainNet with higher accuracy and fewer parameters. These results support the paper's central claim.

- **Task-relation quantification from shared neurons.** The method naturally produces a measure of inter-task relatedness from the proportion of shared channels, and Figure 4 (right) shows this aligns with semantic intuition (e.g., Sketch–Flowers stronger than Cars–Flowers). This is a useful byproduct of the approach.

- **Ablation study for the λ trade-off parameter.** Table 3 and Figure 5 systematically explore the effect of λ on accuracy and parameter count, revealing an optimal range of 0.3–0.7 and validating the method's tunability.

## Weaknesses

### Fatal

None.

### Major

- **CPMS search is not validated with controlled ablations.** The search is presented as a core contribution, but the paper provides no comparison against simple baselines such as: (a) random assignment of parent channels, (b) assigning all channels from the single most similar previous task (a layer-level heuristic), (c) using only the pretrained backbone as the parent source, or (d) varying the similarity metric or warm-up duration. Because the final model blends child and parent channels via a mask, it is impossible to isolate whether improvements come from the similarity-based search or merely from having *any* parent parameters available. This is a significant methodological gap that undermines the claim that CPMS "greatly reduces the search space fine-grained control brought."

- **The λ hyperparameter is used throughout the ablation study but never defined in the methodology.** λ appears in Table 3 and Figure 5, and the paper discusses its effect (λ < 0.3 → overfitting; λ > 0.7 → performance drop). From context λ likely controls the strength of mask regularization (e.g., a sparsity penalty on the mask that trades off accuracy vs. parameter count), but this is never stated explicitly. A reader cannot meaningfully interpret the ablation without knowing what λ controls. This is a basic clarity failure.

- **Standard training details are missing, affecting reproducibility.** The paper does not report: number of epochs, batch size, learning rate schedule, optimizer choice, weight initialization strategy for child parameters, or the total training budget. The only mention is "one-quarter of the total training epochs" for the warm-up, but the total is unspecified. Without these details, the fairness of the comparisons in Tables 1 and 2 cannot be fully assessed.

### Minor

- **The mask training procedure is underspecified.** The paper references Yan et al. (2021) for "mask generation" and describes the forward-pass role of the mask (Eq. 6–8) and the soft-to-hard transition, but does not explain: what loss or regularization drives the mask toward sparse discrete choices, how the mask is initialized, or how hardening (binarization) is performed. While motivated by prior work, this is a core mechanism that should be at least sketched in the paper itself.

- **The "precision-to-parameter ratio" is never formally defined as a metric.** The paper uses this phrase repeatedly but reports only raw accuracy and parameter proportion separately. A formal trade-off metric (e.g., mean accuracy divided by log parameter count, or a Pareto-dominance analysis) would strengthen the quantitative claims.

- **No runtime or FLOPs comparison is provided despite efficiency claims.** The paper claims "efficient" knowledge transfer, "fewer iterations," and that CWPS "would not reduce the inference speed compared to fine-tuning," but provides no wall-clock time, FLOPs, or search-cost measurements. Given that the method includes a warm-up fine-tuning phase and pairwise channel comparisons across all previous tasks, some quantification of the actual training and inference cost is needed.

- **No standard deviations or multi-seed results are reported.** The paper mentions "several experiments" in the metrics description, but no variance information is provided for any table. While this alone is not fatal, it weakens the reliability of the reported SOTA comparisons.

### Trivial

None.

## Nice-to-Haves

- A controlled ablation of CPMS against random parent assignment and all-from-one-task assignment would cleanly isolate the search contribution.
- A formal definition of the λ regularization term and its role in the loss function.
- Wall-clock training time and inference throughput comparisons with baseline methods.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Mask vs. child training dynamics not analyzed"** (Harsh Critic, Critical Issue #3): The paper clearly describes the pipeline in Figure 3(a) and Section 3.2: warm-up fine-tune → search → training stage with soft mask → hard mask stage. The child parameters and mask are trained simultaneously in the third stage. The reviewer's confusion about when the mask is learned stems from the pipeline description being clear but perhaps not explicit enough about gradient flow. This does not constitute a genuine weakness — the pipeline is correctly specified.

- **"Algorithm 1 referenced but absent"** (Harsh Critic, Missing Parts): The algorithm's behavior is described in prose in Section 3.3. The formal pseudocode is likely in the appendix, which was stripped by the parser. This is a parser artifact, not an author omission.

- **"Missing related work (LoRA, Adapter, prefix tuning)"** (Harsh Critic, Section-by-Section Notes): The paper explicitly scopes itself to convolution-based vision backbones. Transformer-focused methods operate on a different architecture class and are not directly comparable. The reviewer acknowledges this ("they are not directly comparable") but still lists it as a weakness.

- **"Figure 4 resolution is low"** (Harsh Critic, Section-by-Section Notes): Parser artifact from PDF extraction. The original submission likely has proper resolution.

- **"Parameter counting ambiguity"** as a major issue: The paper states "the proportion of all model parameters to the parameters of the pre-trained backbone" (Table 1 caption, Section 4.1 Metrics). For incremental learning, each task introduces its own child parameters (full backbone size) and parent parameters are shared from previous tasks. The description "proportion of all model parameters" is tolerably clear for the setting — it means the total parameters used per task relative to the backbone size. This is a minor clarity point at most, not a major ambiguity.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core gap (missing CPMS ablation, undefined λ) but do not reveal any insight about the method or results that the paper itself does not already state or imply.

## Suggestions

1. **Ablate CPMS directly.** Compare the full method against: (a) random channel assignment, (b) all-parent-channels from the single most similar previous task, (c) using only the pretrained backbone as parent. Show that the similarity metric matters by comparing L2 vs. cosine vs. a learned metric.

2. **Define λ explicitly in Section 3.** State that λ is the weight of a sparsity regularization term on the mask (or whatever it actually controls), and give the full loss function in the methodology.

3. **Report standard training details.** Add a table or paragraph specifying epochs, batch size, optimizer, learning rate schedule, initialization, and total training budget for each benchmark.

4. **Report runtime.** Provide wall-clock training time per task and inference throughput to substantiate the efficiency claims.

5. **Define the trade-off metric.** If claiming "precision-to-parameter ratio," either define it as a formal quantity (e.g., accuracy / log(params)) or show a Pareto frontier plot.

## Score and Decision

The paper presents a well-motivated idea — channel-wise parameter sharing fills a genuine granularity gap in the literature — and shows competitive accuracy-to-parameter results. However, the paper has significant presentation and validation gaps: the CPMS search component (a claimed contribution) is never directly ablated, a key hyperparameter (λ) is used in experiments without being defined, and training details are too sparse for reproducibility. These issues are fixable but, in the current form, prevent the paper from being accepted.

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>