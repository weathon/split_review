Now I have a solid calibration. Let me write the final consolidated review.

**Round 1 bracket**: The paper clearly sits between the <3.5 anchors (avg ~2.5–3.25, mostly rejected, serious flaws) and the >7.5 anchors (avg ~7.6–8.0, Oral/strong Accept). Bracketed range: 4–7.

**Round 2 narrowing**: Compared to Equ277PBN0 (5.75, Accept Poster — FL + prompt learning + DP, limited baselines, no stats tests), Fed-DPT has stronger ablation and broader baselines. Compared to TD3SGJfBC7 (6.25, Accept Poster — test-time CLIP adaptation, stronger SOTA, more comprehensive), Fed-DPT is somewhat weaker. The paper sits between 5.75 and 6.25.

Now the full review.

---

## Summary

This paper proposes Fed-DPT, a federated learning method for domain-aware image classification. It uses both visual and textual prompt tuning on a frozen CLIP backbone. Each client (corresponding to one domain) trains a domain-specific text prompt, while visual prompts are shared and aggregated via FedAvg. An attention mechanism weights text features from different domains based on the visual features, and an L2 loss aligns the weighted text and visual representations. Experiments on DomainNet, OfficeHome, and PACS show improvements over CLIP-based federated baselines, with the strongest gains on DomainNet (68.4% vs. 63.2% for PromptFL, +5.2%).

## Strengths

- **Domain-specific text prompts with attention-based weighting yield clear accuracy gains.** Table 3 shows that the full Fed-DPT (68.4%) substantially outperforms the domain-agnostic dual-prompt variant (63.5%), confirming that the core technical novelty — attention-weighting of domain-specific text features — contributes +4.9%. This is the single strongest piece of evidence for the method.

- **Systematic ablation of design choices.** Tables 4a–4d evaluate momentum update, prompt length, communication frequency, and visual prompt aggregation mode, providing empirical justification for each architectural decision (e.g., momentum contributes +2.2%; prompt length of 16 is optimal).

- **Robustness to realistic label heterogeneity.** In the decentralized setting (30 clients, each domain split into 5 via Dirichlet sampling), Fed-DPT's accuracy drops only 1.5% (68.4% → 66.9%), compared to 3.6% and 2.9% for FedAvg and FedProx. This strengthens the practical relevance of the method beyond the simple one-client-per-domain setup.

- **Parameter efficiency.** By freezing CLIP encoders and optimizing only prompt tokens, Fed-DPT avoids the performance degradation seen when conventional FL methods scale from ResNet-50 to ViT-Base (FedAvg drops from 54.7% to 55.2% on DomainNet, while Fed-DPT achieves 68.4%).

## Weaknesses

### Major

- **No uncertainty estimates on main results.** The paper reports averages over three trials without standard deviations or confidence intervals in Tables 1 and 2. On PACS, the improvement over PromptFL is only 0.5% (97.2% vs. 96.7%); on OfficeHome, 1.9% (82.9% vs. 81.0%). Without error bars, the reader cannot assess whether these gains on smaller benchmarks are statistically significant or simply noise. The DomainNet gains (5.2%) are large enough to withstand this concern, but the missing variability estimates weaken the evidence across the board.

### Minor

- **Inference procedure is underspecified.** While the training objective (Equation 7) aligns visual features with weighted text features, the paper never explicitly states how the trained prompts are used to classify a test image across *multiple classes*. The standard CLIP inference (Equation 1 with trained prompts) is implied but not described — e.g., whether the per-class text features use the same attention weights derived from the test image's visual prompts, and how the weighted text features per class interact with the final classification decision. This gap undermines reproducibility and should be clarified.

- **Privacy claim is overstated.** Section 4.4 asserts that sharing per-domain text prompts has "the same level of privacy-preserving capabilities as FedAvg." However, each text prompt is trained exclusively on one domain's data and then broadcast to all clients, which is qualitatively different from FedAvg where model updates are functions of all data at a client. Domain identity (e.g., "sketch" vs. "real") could be inferred from the prompts — the paper itself demonstrates a decoding procedure in the appendix. The dismissal ("it is actually very difficult to decode them") does not justify equivalence to FedAvg's privacy properties, especially in settings where a client's domain identity is sensitive.

- **L2 loss claim is unsupported.** The paper states that the ℓ2 loss "yields better predictive performance and allows more flexible training compared with cross-entropy" (Section 4.2) but provides no ablation or experimental evidence for this claim. Additionally, Equation 7 computes cosine similarity, not ℓ2 distance (though the two are equivalent on the unit sphere since both f_V and f_T are ℓ2-normalized). The inconsistency in naming should be fixed.

### Trivial

- Equation 7 is written as ⟨f_V, f_T⟩/(‖f_V‖·‖f_T‖) but described as an "ℓ2 loss." Since both vectors are normalized, maximizing this cosine similarity is equivalent to minimizing ℓ2 distance on the sphere. The naming should be made consistent (either call it cosine similarity or explicitly state the equivalence).

## Nice-to-Haves

- An ablation comparing the L2/cosine loss to cross-entropy would validate the unusual training objective.
- Reporting standard deviations for all main results (even with only three trials) would improve interpretability, especially on the two smaller benchmarks.
- A variant without domain-specific prompt sharing (e.g., only sharing aggregated/global prompts) would help characterize the privacy-utility trade-off.
- Counting trainable parameters for each method would strengthen the "parameter-efficient" claim.

## Removed Points

- *Comparison to non-CLIP baselines is unfair/misleading*: The paper clearly labels FedAvg and FedProx as "Conventional federated learning methods" in a separate block in Tables 1 and 2. Including these as reference points is standard practice, and the paper's strongest evidence for the method comes from comparisons against CLIP-based competitors (PromptFL, FedCLIP). The gap is indeed due to the CLIP backbone, but this is transparent from the tables. Removed as not a substantive weakness.

- *Small gains on OfficeHome and PACS (critic point #3)*: Subsumed by the error-bars weakness above. The magnitude of the gains is a property of the data, not a flaw in the paper. The real issue is the lack of uncertainty estimates to assess significance.

- *Criticism that the 14.8% improvement claim is over zero-shot CLIP*: The paper clearly states "improves the original CLIP by a large margin of 14.8%." The context makes clear this is vs. zero-shot CLIP (53.6% → 68.4%). This is standard and not misleading.

- *Strength finder's claim about "privacy and interpretability consideration"*: This conflicts with the verified weakness about overstated privacy claims, so it is dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation that the paper itself does not already contain or acknowledge.

## Suggestions

1. **Explicitly describe the inference pipeline.** Add a short paragraph (or a sentence in Section 4.2) explaining how a test image is classified: compute f_V, compute attention weights w_i via visual prompts, compute f_T = Σ w_i f_T^i for each class, then use cosine similarity (Equation 1) for the final prediction.
2. **Add standard deviations to all accuracy tables.** Even with three trials, mean ± std would allow readers to judge variability. If the paper can report per-domain std across three random seeds, that would be ideal.
3. **Tone down or better justify the privacy claim.** Either (a) provide empirical evidence (e.g., do membership inference or domain-identification attacks on the shared prompts) or (b) acknowledge that sharing domain-specific prompts may leak domain identity and discuss mitigation strategies or alternative aggregation schemes.
4. **Ablate the L2 vs. cross-entropy loss choice** to substantiate the claim made in Section 4.2.
5. **Fix the naming of the loss** in Equation 7 to avoid confusion between ℓ2 distance and cosine similarity.

## Score and Decision

**Round-1 bracket**: The paper clearly outperforms rejected anchors in the <3.5 band (weak baselines, serious methodological flaws) and falls short of Oral-accept anchors in the >7.5 band (stronger SOTA, more comprehensive evaluation). Bracket: **4–7**.

**Round-2 narrowing**: Compared to:
- *Equ277PBN0* (5.75, Accept Poster): FL + prompt learning + DP. More novelty concerns and limited baselines. Fed-DPT has stronger ablation and broader evaluation. Fed-DPT is slightly stronger.
- *U0P622bfUN* (5.25, Reject): FL + foundation models. Fundamental assumption issues. Fed-DPT is clearly stronger.
- *NJqu7xwXZk* (5.0, Reject): FL + discrete prompt learning. Questionable motivation. Fed-DPT is clearly stronger.
- *TD3SGJfBC7* (6.25, Accept Poster): Test-time CLIP adaptation. Stronger SOTA results, more comprehensive. Fed-DPT is slightly weaker.

Fed-DPT sits between the Equ277PBN0 (5.75) and TD3SGJfBC7 (6.25) anchors. The core idea is well-motivated and the DomainNet ablation convincingly demonstrates the value of the domain-specific mechanism. However, the missing inference specification, lack of error bars, and overstated privacy claim hold it back from being a stronger paper.

Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>