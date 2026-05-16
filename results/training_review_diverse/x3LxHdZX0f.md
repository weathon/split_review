Now I have a thorough understanding of the paper. Let me produce the final review.

## Summary

PUMA presents a secure MPC inference framework for Transformer models using 2-out-of-3 replicated secret sharing. It contributes accurate polynomial approximations for GELU and Softmax, faithful MPC implementations of Embedding and LayerNorm, and an end-to-end system that loads pre-trained models without retraining or architectural modification. Experiments show accuracy within 0.011 of plaintext across GLUE tasks, ~2× speedup over MPCFormer, and the first-ever MPC evaluation of LLaMA-7B (~200 seconds per token).

## Strengths

- **First MPC evaluation of a 7B-parameter model.** PUMA demonstrates secure inference of LLaMA-7B at ≈200 seconds/token with 1.794 GB communication, a clear first result that validates the paper's title and represents a genuine engineering achievement (lines 6, 229–231). The serialization optimization (automatically chunking oversized secret-shared structures) is a practical contribution that enabled this result (lines 227–228).

- **Near-plaintext accuracy without retraining.** Across Bert-Base/Large, RoBERTa-Base, and GPT2-Base/Medium/Large, PUMA's accuracy differs from plaintext by ≤0.011 (GLUE) and perplexity by ≤0.02 (Wikitext-103) (lines 174–179). This directly supports the claim that the polynomial approximations and secure protocols preserve model quality without fine-tuning — a capability prior open-source frameworks lacked.

- **~2× speedup over MPCFormer with a conservative comparison.** PUMA shows 1.375–1.916× runtime improvement on BERT models and 2.250–2.414× on GPT2 models (line 188). The comparison is run in the same environment with re-implemented baselines (line 151). Notably, the comparison is conservative: MPCFormer's architecture is simpler (BatchNorm instead of LayerNorm, ReLU instead of GELU, client-side one-hot), so PUMA achieves speedup despite computing more expensive per-layer operations — making the result stronger, not weaker.

- **Faithful implementation of missing layers.** MPCFormer replaces LayerNorm with BatchNorm (causing a catastrophic accuracy drop from 0.616 to -0.020 MCC on CoLA) and lacks secure Embedding. PUMA implements both faithfully, recovering accuracy to 0.613 (lines 149–150, footnote). This architectural completeness is a core differentiator.

- **First open-source end-to-end framework for pre-trained Transformers in MPC.** PUMA loads models directly from Hugging Face without retraining or modification (line 40). This is a practical contribution that lowers the barrier for deploying secure inference on existing models.

- **Efficiency gains scale with model size.** The speedup over MPCFormer grows for larger GPT2 models (line 190), suggesting the optimizations are particularly effective at scale — important for the large-model setting PUMA targets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Accuracy comparison with MPCFormer is indirect.** The paper demonstrates MPCFormer's accuracy loss via a plaintext experiment replacing LayerNorm with BatchNorm (MCC 0.616 → -0.020). While this convincingly shows the impact of a single architectural change, it does not simulate the combined effect of *all* of MPCFormer's approximations (ReLU for GELU + quadratic Softmax + BatchNorm) under secure inference. A plaintext ablation that applies all MPCFormer-style approximations simultaneously would provide stronger evidence for the claim that "MPCFormer cannot achieve similar accuracy." The current evidence is strongly suggestive but indirect (lines 148–151).

- **No statistical variance reported.** Runtime, communication, and accuracy results are reported without standard deviations or multiple-run statistics (lines 142, 174–188). While MPC protocols are largely deterministic, runtime can vary due to CPU contention and network jitter, and fixed-point rounding can exhibit run-to-run variation under truncation. Repeating key experiments (even 2–3 runs) would strengthen the reliability of the reported numbers.

- **Lack of a dedicated limitations section.** The conclusion briefly notes that "inference cost is still quite high" (line 236), but the paper would benefit from a limitations paragraph discussing: the semi-honest, no-collusion threat model; the one-hot embedding overhead for longer sequences (honestly discussed in §5.3 but not in a limitations context); the network requirements (1 ms RTT, 5–20 Gbps); and the high hardware requirements for LLaMA-7B (1 TB RAM servers). Acknowledging these upfront would strengthen the paper's scholarly rigor.

- **LLaMA-7B timing ambiguity.** The paper states that "given an input sentence of 8 tokens, PUMA can output one token in around 200 seconds" (line 231). It is not fully clear whether this 200 seconds is the end-to-end time for processing all 8 input tokens *plus* generating 1 output token, or only the time for generating the single token after the inputs have been processed. The distinction matters for understanding the cost of autoregressive generation (where each subsequent token requires a fresh forward pass). The stripped table may have clarified this, but the current text is ambiguous.

### Trivial

- **Citation specificity for the "first open-source" claim.** The contribution bullet claims PUMA is "the first open-sourced MPC solution that supports accurate inference of pre-trained Transformer models without further modifications" (line 40). The paper names MPCFormer as the only open-source alternative (line 54) but does not explicitly enumerate *which* prior works are closed-source or require architectural modifications — a small clarity improvement for the claim.

## Nice-to-Haves

- **Per-operation cost breakdown.** A breakdown of runtime by operation (matrix multiplication, GELU polynomial, Softmax polynomial, LayerNorm, Embedding) for both PUMA and MPCFormer would help readers understand which specific optimizations contribute the most to the 2× speedup. This is not necessary to validate the core claim (which holds conservatively given the architectural asymmetry), but would strengthen the paper's scientific contribution.

- **Ablation of approximation quality.** Replacing PUMA's GELU polynomial with ReLU (in plaintext) and reporting the accuracy change would quantitatively demonstrate that the high-quality approximation is necessary for accuracy preservation. Similarly for Softmax. This would reinforce the claim that PUMA's approximations are both efficient and accurate.

- **Mitigation discussion for one-hot overhead.** The paper honestly acknowledges that one-hot embedding in MPC reduces efficiency gains for longer sequences (lines 214–215). A brief discussion of potential mitigations (e.g., trusted-client preprocessing for token IDs, or alternative embedding protocols) would be useful.

- **Comparison to published numbers from closed-source frameworks.** While direct runtime comparison is not possible, citing published efficiency numbers from frameworks like Iron, PrivFormer, or Bumblebee for context (even without re-running) would help position PUMA in the broader landscape.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Unfair baseline comparison — speedup conflates protocol improvement with architectural simplification."** This criticism is factually backward. MPCFormer's architecture (BatchNorm instead of LayerNorm, ReLU instead of GELU, client-side one-hot) is *simpler and cheaper* per operation than PUMA's full Transformer. PUMA achieves 2× speedup *despite* computing more expensive operations per layer. The asymmetry favors the baseline, not the author's method, making the speedup claim *conservative*. Per hard rules, removed as factually wrong.

2. **"Protocol details are missing due to `\input` statements."** The reviewer correctly notes this is a parser artifact (the protocols were present in the original PDF). Per hard rules, removed.

3. **"The paper should compare against more MPC frameworks."** The paper clearly explains that MPCFormer is the only open-source alternative (line 54). Demanding comparison against frameworks that would require re-implementation is scope creep. Moved to Nice-to-Haves.

4. **Various formatting/style nitpicks.** Per hard rules, removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself misses. The insights all stem from what PUMA already reports: that faithful MPC inference of a 7B model is feasible within minutes, that high-quality polynomial approximations preserve accuracy without retraining, and that the main remaining bottleneck is the one-hot embedding overhead for long sequences.

## Suggestions

1. Add a plaintext ablation applying MPCFormer's full set of approximations (ReLU + quadratic Softmax + BatchNorm) to quantify the combined accuracy loss.
2. Clarify whether the LLaMA-7B "200 seconds" covers only the output generation step or the entire forward pass including the 8 input tokens.
3. Report at least 2–3 runs of key runtime and accuracy experiments with standard deviations.
4. Add a brief limitations section covering the threat model, network requirements, one-hot overhead, and hardware cost.
5. Consider adding a per-operation runtime breakdown to help readers attribute the speedup.

## Score and Decision

This is a strong empirical systems paper with a clear novelty — the first MPC evaluation of a 7B-parameter Transformer — supported by solid accuracy preservation, thorough comparisons (conservatively favoring the baseline), and practical engineering contributions (serialization chunking, faithful LayerNorm/Embedding). The weaknesses are all minor or addressable: indirect accuracy evidence for the baseline, missing variance reporting, no dedicated limitations section, and a minor timing ambiguity. No fatal or major flaw threatens the core claims. The paper makes a genuine contribution to the field of secure ML inference.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>