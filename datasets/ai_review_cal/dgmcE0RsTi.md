- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 8, 6
I have all the information I need. Let me now construct the final consolidated review.

## Summary

This paper proposes SimCAS (Chunk, Align, Select), a framework for extending off-the-shelf transformer PLMs (specifically BART) to long sequences without modifying their architecture. The method (1) chunks the input into segments of the model's maximum length, (2) shares information across chunks by averaging the [S] and [E] special token representations at each encoder layer, and (3) uses a PPO-trained token selector to compress encoder outputs to a manageable size for decoding. Experiments on seven datasets (arXiv, PubMed, GovReport, SummScreen, Multi-News, WCEP, NarrativeQA) show consistent improvements over baselines including SLED, Unlimiformer, PRIMERA, and standard BART.

---

## Strengths

1. **Consistent, large-margin gains across diverse long-sequence benchmarks.** On PubMed (Table 1), BART_large+SimCAS achieves R-1 48.65 vs. the best baseline HEPOS at 47.93. On GovReport (Table 2), SimCAS_base R-1 59.30 vs. Unlimiformer 56.60. On SummScreen, the gap is even larger: 43.45 vs. 34.70. These results are reported on **seven** datasets spanning single-doc summarization, multi-doc summarization, and reading comprehension, demonstrating generality.

2. **Empirical verification of near-linear inference complexity.** Figure 2 (right) shows inference time growing roughly linearly with input length up to 2^14 tokens, and the method handles up to ~350k tokens on a single V100 — far beyond vanilla full-attention limits. The selected token count stays near ~2048 regardless of input length (Figure 2, left).

3. **Ablation study with standard deviations clearly isolates the contribution of each component.** Table 5 reports mean ± std for three ablated variants across all seven datasets. Removing Chunk or Select causes large drops (e.g., NarrativeQA F1 drops from 31.76 → 21.70 and 23.20 respectively), while removing Align gives smaller but generally positive gains (0.76%–2.56%). This directly supports the paper's claim that chunking and selection are the core mechanisms.

4. **Model-agnostic design:** The framework requires no architectural changes to the backbone PLM — it processes chunks as a regular batch and uses the decoder's existing cross-attention for reward computation. This plug-and-play quality is a practical advantage over efficient-attention methods (Longformer, BIGBIRD) that require custom kernels or from-scratch training.

5. **Low-resource evaluation:** Figure 3 shows SimCAS_base outperforming BART_base and LED_base with as few as 10 training examples, with lower variance across random seeds — a practically relevant finding.

---

## Weaknesses

### Fatal
None.

### Major

1. **Positional encoding across chunks is not addressed (structural omission).** BART uses absolute positional embeddings with a maximum length of 1024 tokens. SimCAS chunks longer inputs into segments of exactly this length and processes them as a batch — each chunk independently receives positions 1..S. The paper never specifies how the model distinguishes tokens from different chunks or encodes their global position in the original sequence. The sequential batch alignment (averaging [S] and [E] token representations) shares *some* information across chunks, but it does not encode positional ordering. For tasks where document-level structure matters (SummScreen, NarrativeQA), this is a non-trivial gap. The paper should at minimum explain whether global positions are injected (e.g., by extending positional embeddings or adding sinusoidal encodings based on original token indices) and ideally provide an ablation. As written, the method is underspecified on this point.

2. **Key RL hyperparameters are not reported, hindering reproducibility.** The reward design depends on at least two unreported hyperparameters: $L_{hyper}$ (Eq. 122, the threshold for the skip reward) and $\xi$ (Eq. 110, the reward scaling coefficient). The alternating update schedule for the selector and transformer is described only at a high level ("we alternatively update the selector and transformer") with no information on frequency, number of PPO steps per update, the clipping threshold $\varepsilon$, the learning rates (separate for selector and backbone), or whether the selector is trained from scratch or warm-started. Without these, the RL component — which is central to the method — cannot be independently reproduced or empirically assessed.

3. **Main results lack uncertainty estimates.** Tables 1, 2, and the multi-document tables report single numbers without variance, confidence intervals, or significance tests. This is especially concerning given the very large claimed improvements (e.g., +9 ROUGE-1 on SummScreen over Unlimiformer). While the ablation study (Table 5) does include standard deviations, the main results do not. The absence of error bars for the proposed method makes it impossible to assess whether the claimed gains are reliable. This is a standard expectation for empirical papers and should be addressed.

### Minor

1. **The Sequential Batch Alignment component provides only marginal benefit.** Table 5 shows that removing Align changes performance by only -0.29% to +2.56% across seven datasets, and on Multi-News it *hurts* performance (↓0.29%). The paper's "elaborately designed encoding blocks with an inter-chunk alignment mechanism" (Introduction) overstates the role of this component. The method would be simpler and nearly as effective without it, or the authors should explain why it is retained despite the small effect.

2. **The token selector's state representation discards sequential order among selected tokens.** The state is computed as the average of all previously selected hidden states (Eq. 100), which is a bag-of-tokens representation with no notion of order. The selector cannot distinguish "selected a crucial token 2 positions ago" from "selected a crucial token 50 positions ago" through this state alone. The paper acknowledges the selector is "similar to a chunk-wise RNN" but this averaging mechanism is not recurrent in any meaningful sense. The impact of this design choice on selection quality is not discussed or ablated.

3. **Baseline comparisons rely on numbers from prior papers without re-implementation.** Several baselines (SLED, Unlimiformer, PRIMERA, HEPOS) have results cited from their original publications. The paper does not state whether evaluation setups (max input length, truncation policy, beam size, output length limits) were matched, making it difficult to rule out disparities in experimental conditions.

### Trivial

- The variable $\bar{a}_0$ appears in the denominator of Eq. 121 without being explicitly defined (it can be inferred as the same formula $\bar{a}_j$ with j=0, but stating this clearly would help readability).

---

## Nice-to-Haves

- **Ablation on chunk size.** The chunk size is fixed to the model's maximum (1024 tokens). Exploring different chunk sizes (e.g., 512, 2048 with extended positional embeddings) would strengthen the claim of simplicity and reveal the sensitivity of the method.
- **Comparison using the same backbone architecture.** Comparing BART+SimCAS against LED (different architecture) conflates backbone choice with method effectiveness. Applying SimCAS to an LED backbone (or comparing BART+SimCAS against an LED baseline matched for compute budget) would isolate the contribution.
- **Time/memory breakdown.** Figure 2 shows total inference time but does not break down where time is spent (encoding vs. selection vs. decoding). This would clarify the source of the super-linear behavior beyond 2^17 tokens.
- **Sensitivity analysis for RL hyperparameters $\xi$, $L_{hyper}$, and $\varepsilon$.** Given the complexity of the RL training, showing robustness to these choices would significantly strengthen the paper.

---

## Removed Points

- **"Figure not provided for NarrativeQA"** — REMOVED. The figure (Figure 6, line 330) exists in the paper; the reviewer appeared to miss it.
- **"Linear complexity claim is misleadingly simple"** — REMOVED. The claim is about inference complexity, where encoding is O(N·S) = O(N) (S constant) and decoding is O(M·K) with bounded K. This is a reasonable characterization.
- **"Sentence splitter has no citation"** — REMOVED. The paper cites Moro_Ragazzi_2022 (line 71) for sentence segmentation.
- **"Pearson correlation table is filler"** — REMOVED. The table justifies using BERTScore as a complementary metric, which is a standard practice.
- **"Non-stationary environment not discussed"** — REMOVED. The paper explicitly says "Note that in our setups, the environment (the transformer) changes during the training steps" and describes the alternating update strategy (line 130-131).
- **Strengths that are generic or conflict with weaknesses** — Several strength-finder claims about the paper being "important" or "significant" are generic and removed. Strength 5 (reward design) is retained but with caveats since the weakness about underspecification dominates.
- **"Cross-attention averaging ignores layer-specific patterns"** — REMOVED. Averaging across layers and heads is a standard design choice, not an error. The paper is free to make this choice without justification.

---

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's empirical strengths and the same specification gaps but do not uncover patterns or tensions not already visible in the paper.

---

## Suggestions

1. **Immediately clarify how positional information is handled across chunks.** If no global position is encoded, explain why this is unnecessary or provide an ablation showing that adding it does/does not change results. This is the single most important gap to close.

2. **Report all missing hyperparameters** ($L_{hyper}$, $\xi$, $\varepsilon$, PPO update frequency, learning rates for selector vs. backbone) in a dedicated table.

3. **Add confidence intervals or standard deviations to the main result tables** (Tables 1, 2, and multi-document). Given the large claimed margins, even bootstrapped confidence intervals over a single run would substantially increase credibility.

4. **Reconsider or de-emphasize the alignment component.** Since removing Align yields at most ~2.5% change and hurts on Multi-News, either justify why it is kept (e.g., it enables training stability not captured by the metric) or simplify the framework by removing it.

5. **Provide a simple schematic or note clarifying whether the PPO selector state encoding loses sequential order** and whether the authors explored alternatives (e.g., a learned RNN state, a transformer over selected tokens).

---
