I have all the information I need. Let me now synthesize the review.

**Round 1 bracket**: after reviewing the weak anchors (all avg < 3.5, Reject), middle anchors (3.5-7.5), and strong anchors (avg > 7.5), the paper clearly sits in the middle band — it is substantially stronger than papers scoring ≤ 3.5 (which are mostly preliminary or poorly executed) but does not reach the quality bar of the 8.0-level papers. Initial bracket: **4.5 – 7.0**.

**Round 2 narrowing**: comparing to the most topically similar anchors:
- vs **Stutter** (avg 4.50, Reject): DND addresses Stutter's major failings — efficiency analysis, better-controlled selection, consistent improvements, scalability. DND is clearly stronger.
- vs **CoTFormer** (avg 5.75, Accept): comparable quality. Both have adaptive computation. CoTFormer's theoretical framing is cleaner but DND has better empirical scope (multiple scales, MoE) and more thorough ablation.
- vs **D2O** (avg 5.80, Accept): comparable. D2O excels in efficiency evaluation; DND excels in training strategy and ablation.
- vs **Learning How Hard to Think** (avg 6.50, Accept): DND is slightly weaker — that paper has stronger baselines and better uncertainty handling.
- vs **OrthoRank** (avg 5.25, Reject): DND is clearly stronger in methodology and evaluation breadth.

Final placement: between CoTFormer (5.75) and Learning How Hard to Think (6.50), closer to CoTFormer due to the error-bars gap and limited baselines. **Score: 5.5**.

## Summary

The paper proposes Dynamic Nested Depth (DND), a post-training method that identifies "critical" tokens via a learned router and gives them an extra pass through the same transformer layer. The key technical contributions are a router-controlling loss (score dispersion + distribution preservation) and a threshold-control scheme (buffer proportional control + EMA synchronization) that together achieve precise token-level selection. DND is evaluated on three small dense models (Qwen3-1.7B, Llama3.2-1B, Gemma3-1B) and one large MoE model (Qwen3-30B-A3B), showing consistent improvements over SFT baselines with modest compute overhead (91-93% throughput retention).

## Strengths

1. **Novel and well-motivated training strategy for token-choice routing precision.** The paper identifies a genuine problem — token-choice routers lack the built-in ratio control of top-k routing — and designs a two-part solution (score dispersion loss + distribution preservation loss, combined with EMA-synchronized buffer-proportional threshold control). The ablation in Table 4 cleanly isolates the value of this strategy: the full method (+1.88 avg) substantially outperforms a z-loss-only variant (+1.01 avg), proving the training strategies matter, not just the architecture.

2. **Scalability to large MoE models demonstrated.** Unlike the most closely related prior work MOR (limited to 1B), DND is successfully applied to Qwen3-30B-A3B — a 30B-parameter MoE model — achieving +0.87 average improvement across 17 benchmarks with only 0.03M additional parameters and 91-93% throughput retention. This directly supports the claim of plug-and-play post-training applicability to large sparse architectures.

3. **Empirical verification of the critical-token hypothesis.** The analysis in Figures 4a and 4b is genuinely informative: token selection frequency positively correlates with logit entropy (r=0.3359), and the nested pass reduces this entropy for frequently selected tokens (r=-0.5811). This provides quantitative evidence that the router selects genuinely uncertain tokens and that the extra computation resolves that uncertainty — not just a correlational artifact.

4. **Thorough ablation study.** Table 4 systematically ablates router control, threshold control, selection ratio (10/20/30%), and layer range. The ablation shows that both control components contribute and that 20% selection with middle layers active is the sweet spot. This is more comprehensive than most papers in this area.

## Weaknesses

### Major

1. **No uncertainty quantification across runs.** Every reported number is a single point. For the large MoE model (Table 2), the average gain is 0.87% with several tasks showing gains below 0.3% (BBH +0.13, MATH-500 +0.20, AIME24 +0.91, CMMLU +0.37). Without error bars, multiple seeds, or even a paired significance test, it is impossible to distinguish genuine improvements from run-to-run noise — especially for the large model where training is expensive and typical benchmark variance can reach 0.5-1%. This is the single largest threat to the paper's central claim.

2. **FLOPs efficiency analysis is not in the main paper.** The claim that 20% token selection adds "only about 6% extra FLOPs" is relegated entirely to Appendix A (stripped from this version). Given that the efficiency argument is central to the method's value proposition — the paper's title emphasizes "Boosting" with "minimal computing increase" — at least a summary derivation should appear in the main body. The throughput measurements in Table 3 are helpful but only cover batch=1 on a single H100; real serving conditions with variable batch sizes and KV-cache optimizations could change the relative overhead.

### Minor

3. **Limited baseline comparisons.** The main experiments compare DND-augmented SFT against vanilla SFT on the same base model and, for Qwen3-1.7B, against ITT. This is a necessary sanity check but insufficient to establish that the *dynamic selection* mechanism (rather than the extra computation itself) drives the gains. The paper would benefit from a baseline where the same extra FLOPs are applied uniformly to all tokens (a fixed-depth increase) to isolate the value of selective allocation. Similarly, a comparison against simply adding the same number of parameters via wider hidden dimensions or extra layers would contextualize DND's parameter efficiency.

4. **ITT comparison limited to the smallest model.** The comparison with ITT is conducted only on Qwen3-1.7B (Table 1). To substantiate the claim that DND outperforms this existing approach, the comparison should be extended to at least one larger model (e.g., Qwen3-30B-A3B).

5. **Hyperparameter sensitivity of loss weights and control parameters not explored.** The router control loss has two balancing coefficients (λ_sd, λ_dp), and the threshold control involves α (proportional gain), γ (EMA smoothing), and the buffer size. No analysis is provided on how sensitive the final performance is to these values, leaving open the question of whether the reported results depend on careful tuning.

6. **Layers used for the large model not explicitly stated in the main text.** The ablation on Qwen3-1.7B reports that keeping ~4 layers at each end works best, and states this configuration "was retained in the DND experiments on Qwen3-30B-A3B." However, the actual L_s and L_e values for the 30B model are not given, which impedes reproducibility.

### Trivial

7. The paper mentions "CMMMLU" in the evaluation suite description (Sec. 4.1) but refers to it as "CMMLU" in Table 2. Minor inconsistency.

## Nice-to-Haves

- A hyperparameter sensitivity study for λ_sd, λ_dp, α, γ, and buffer size would strengthen the claim that the method is robust rather than dependent on fine-tuned knobs.
- The fusion design uses the raw router score p as a gating factor (Eq. 4). Since p is a sigmoid output, the gate could be sensitive to router calibration. An analysis of the learned β values and whether the router scores are well-calibrated would be informative.
- The causal effect of selected tokens could be tested more directly — e.g., by ablating (removing) selected tokens and measuring the drop in output quality.

## Removed Points

- **"No comparison against simply adding more parameters / extra layers"**: This asks the paper to address a scope different from what it claims. The paper is about dynamic computation allocation, not about parameter scaling. The comparison would be nice but its absence is not a flaw in evaluating what the paper claims to do.
- **"No comparison against early-exit strategies repurposed for budget improvement"**: These methods target efficiency (reducing computation) rather than quality improvement, which is DND's goal. Scope creep.
- **"The improvement on the large model is small enough to fall within typical benchmark variance"**: This is speculation. The gains are consistently positive across all 17 tasks (zero degradations), which has low probability under random noise. The consistency itself is weak evidence, though error bars would make this rigorous.
- **"The paper would be strengthened by analyzing whether the router's output is calibrated enough to serve as a reliable gate"**: Interesting but speculative. The empirical results demonstrate the router works; calibration analysis is a nice-to-have, not a weakness.
- **"FLOPs analysis should be in main paper"**: Kept as Minor. The throughput numbers are in the main paper, which partially addresses this.
- **"Comparison with ITT only on small model"**: Kept as Minor.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is the *dual nature* of the token selection evidence. The positive entropy-selection correlation (Fig. 4a) and the negative entropy-change correlation (Fig. 4b) together support a causal story: the router identifies tokens the model is uncertain about, and the nested pass reduces that uncertainty. This is stronger than the standard "our method works because the numbers go up" argument. The paper could lean into this more by presenting it as a feedback-loop verification of the method's internal mechanism.

However, the reviews also surface a structural tension: the gains on the large MoE model are concentrated in coding and agent tasks, while general knowledge tasks show near-zero improvements. This heterogeneity is either a strength (the method targets complex reasoning) or a weakness (it doesn't help general knowledge), and the paper does not resolve this ambiguity.

## Suggestions

1. **Add error bars for at least the main results (Tables 1 and 2).** For the large model where running multiple seeds is expensive, a bootstrap analysis over tasks or a paired sign test (17 tasks × consistent positive sign) would provide statistical evidence at minimal computational cost.

2. **Move a FLOPs derivation summary to the main text.** A single formula or paragraph showing how 20% selection → ~6% extra FLOPs (accounting for attention's quadratic cost with packed sequences) would make the efficiency claim falsifiable in the main paper.

3. **Add a "uniform depth" baseline where the same extra FLOPs are applied to all tokens.** This would directly test whether the *dynamic selection* mechanism, rather than the extra computation per se, is responsible for the gains.

4. **Expand the ITT comparison to at least one larger model** to support the claim that DND outperforms existing approaches.

## Score and Decision

The paper presents a well-motivated method with a novel training strategy, clean ablation evidence, and encouraging results across multiple model scales. The main weaknesses — lack of error bars, FLOPs derivation in the appendix rather than the main paper, and limited baselines — are real but addressable. The method's core contributions (the router control + threshold control design, the empirical verification of token-selection behavior, and the successful scaling to a 30B MoE model) represent a solid step forward for token-level adaptive computation.

**Score: 5.5**  
**Decision: Accept**

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| lvhEptUoFF (retrieval) | 3.00 | R1 | Much weaker — different domain, rejected |
| ulGwcj1egv (FiRST) | 3.00 | R1 | Much weaker — limited evaluation, rejected |
| 7DY2DFDT0T (EfficientSkip) | 2.50 | R1 | Much weaker — preliminary, rejected |
| 7X65yoKl3Y (ALLoRA) | 3.33 | R1 | Much weaker — LoRA tuning, rejected |
| 7igPXQFupX (CoTFormer) | 5.75 | R1, R2 | Comparable — both adaptive computation, both accepted, similar strengths/weaknesses |
| 6qUUgw9bAZ (Learning How Hard to Think) | 6.50 | R1, R2 | Slightly stronger — better baselines and error analysis |
| UvYrFbKj8j (Stutter) | 4.50 | R1 | Weaker — same concept but far less thorough, rejected |
| fswihJIYbd (ADePT) | 7.00 | R1 | Different domain (prompt tuning) |
| HzBfoUdjHt (D2O) | 5.80 | R2 | Comparable — both dynamic token operations, both accepted |
| oXh0939Zzq (LoSA) | 5.20 | R2 | Slightly weaker — mixed reviews, some strong concerns |
| SYv9b4juom (OrthoRank) | 5.25 | R2 | Slightly weaker — token selection but rejected |
| xOtOfdbBqK (spec. decoding) | 5.75 | R2 | Different topic (speculative decoding) |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>