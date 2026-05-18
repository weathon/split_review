Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

IntelLLM proposes two strategies — Center of Gravity Eviction (CGE) and Remote Gap Localization (RGL) — for KV cache compression in LLMs without fine-tuning. The paper claims that by exploiting the high sparsity of attention weights (>90%), these strategies can retain only the most important tokens, achieving 50% cache compression while matching or exceeding the full-cache baseline on LongBench with Llama-3-8B-Instruct and Mistral-7B-inst-v0.2.

## Strengths

- **Empirical evidence for attention sparsity (Section 3.3):** The paper provides a concrete analysis showing that with a threshold of 1/t, over 90% of attention weights are sparse across layers and heads (Figure 1c). This directly supports the paper's core assumption that only a small fraction of tokens carry long-range importance, justifying aggressive compression in principle.

- **Low computational overhead:** The measured latency increase is only 2.37 ms on top of 900.84 ms (2.63%) for 8K sequences, demonstrating that the eviction logic adds negligible runtime cost relative to the 50% memory savings.

- **No fine-tuning required:** The method integrates as a plug-in to existing LLMs with "minimal code modifications," which is a practical design choice that enhances deployability.

- **Ablation study confirms both components contribute:** Table 3 (though visible only as an image) shows performance degradation when either CGE or RGL is removed, providing evidence that both strategies independently benefit long-text reasoning.

## Weaknesses

### Fatal

- **Core method is not adequately specified.** Three independent problems converge here: (1) **Algorithm 1 is truncated** after a single line (line 137: "1 $A^{0}\gets Q K^{T}/\sqrt{d}$") — the eviction logic that should define the entire contribution is missing. (2) **CGE is described in contradictory terms:** the abstract and the introduction (line 4) state that CGE "prioritizes the retention of key tokens by **shielding** the center of gravity of attention," while Section 4.1 (line 118) states "we adopt a strategy of **evicting** the attention center of gravity." These are opposite operations — one protects the center of gravity, the other removes it. The mathematical derivation in Section 4.1 (line 108–124) argues for evicting the dominant weight to restore softmax balance, but the abstract claims the opposite. The reader cannot determine what CGE actually does. (3) **RGL is never formally specified.** Section 4.2 describes a failed naive positional reassignment experiment and a hypothesis for why it failed, but never defines the actual RGL mechanism that was used in the experiments. The ablation section references "positional distance interval settings" but does not specify what these are or how they are computed. Since the methods (CGE and RGL) are the paper's entire contribution, this under-specification and self-contradiction prevent the paper from being evaluated for correctness, reproducibility, or novelty.

### Major

- **Missing comparisons to the most relevant baselines.** The paper compares to full-cache inference, StreamingLLM, and LM-Infinite — all window-based approaches. However, IntelLLM is a *selective eviction* strategy that retains a sparse subset of important KVs. The natural comparison class is other eviction-based compressors that also operate without fine-tuning: H2O, SnapKV, Keyformer, and similar methods. Not a single one is benchmarked or even cited in the experimental section (the paper mentions none of these names). Given that the central claim is outperforming full cache at 50% compression, the absence of comparisons to the most directly competing methods is a serious gap that leaves the claim unsubstantiated relative to the current state of the art.

- **Mismatch between the abstract's strong claim and the evidence.** The abstract claims IntelLLM "consistently outperforms full KV models" with 50% cache. The results section (line 161) uses more measured language: "close to or even exceeding." The reported improvement is ~1 point on average for Llama-3-8B-Instruct. This is a modest gain on a single benchmark (LongBench) with two models. No statistical significance is reported, no per-task breakdown is available in the text (the tables are image-only), and the paper does not discuss *why* compression would improve over the full model — a surprising result that warrants deeper analysis (e.g., does eviction act as a denoising regularizer? Are there distributional artifacts in LongBench?). Without this discussion or a breakdown of where gains/losses occur, the "consistently outperforms" claim in the abstract overstates what the data supports.

### Minor

- **Theoretical derivation does not clearly connect to the implemented method.** Section 4.1 derives a standard softmax manipulation (subtracting the maximum logit) and uses it to motivate evicting the "center of gravity." However, the logic linking the mathematical identity to a concrete eviction policy is unclear, and the derivation appears consistent with evicting the dominant token while the abstract claims the opposite (shielding). The concepts of "head gravity" and "tail gravity" regions are introduced (line 126) but without specifying how these regions are selected in practice, what thresholds are used, or how this connects to the derivation.

### Trivial

- The paper introduces the term "extra-domain inference" when the standard term in the literature is "length extrapolation" or "out-of-domain length generalization." This is a minor terminology choice.

## Nice-to-Haves

- A hypothesis for why 50% cache compression can *improve* over full cache (e.g., eviction as denoising, reduction of attention noise from irrelevant tokens) would significantly strengthen the paper's credibility.
- Per-task breakdown of results (not just averages) to show where gains and losses occur.
- The ablation descriptions in Section 5.2 could be clearer about what specific configurations of "head gravity scaling" and "positional distance intervals" were tested.

## Removed Points

- The harsh critic's claim that the paper "cannot be evaluated for correctness or reproducibility" due to missing algorithm — **Kept in Fatal** as it is factually verified (Algorithm 1 is truncated, CGE description is contradictory, RGL is unspecified). This is not an overstatement given the severity of the under-specification.
- The harsh critic's suggestion that latency measurements are insufficient — **Downgraded.** The latency measurement is adequate for an initial efficiency claim and is standard in the field.
- The harsh critic's broader claim that the paper "should not be accepted in its current form" — **Kept as the overall judgment,** but the severity assessment is my own synthesis, not a direct citation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the CGE contradiction.** Commit to a single, unambiguous description: does CGE *protect* the center of gravity (retain those tokens) or *evict* it (remove those tokens)? The abstract, Section 4.1, and Algorithm 1 must all be consistent. If the method evicts the center of gravity (as Section 4.1's derivation suggests), revise the abstract and introduction accordingly. If it shields/retains it, revise Section 4.1.
2. **Complete Algorithm 1.** Provide full pseudocode showing the eviction decision logic, how the head/tail gravity regions are selected, and how RGL modifies positional encodings. This is the single most critical fix.
3. **Formally specify RGL.** Provide the definition of the positional distance interval, how it is computed, and how it differs from the failed naive approach described in Section 4.2.
4. **Add baselines.** Compare against H2O, SnapKV, or Keyformer, which are the most directly relevant methods for eviction-based KV cache compression without fine-tuning.
5. **Tone down the abstract's claim.** Replace "consistently outperforms full KV models" with "performs comparably to or slightly better than full KV models" (or similar) unless substantially more evidence is provided.
6. **Discuss the improvement mechanism.** Add a paragraph analyzing why compression at 50% can sometimes outperform the full-cache model. Even a brief hypothesis would make the result more credible.

## Score and Decision

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>