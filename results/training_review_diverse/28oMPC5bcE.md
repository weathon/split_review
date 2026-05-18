Now I have thoroughly read the paper and verified all claims against the source. Let me produce the consolidated review.

## Summary

UNComp proposes a training-free, uncertainty-aware compression framework that uses matrix entropy (effective rank) of query hidden states to adaptively group layers and attention heads, applying differentiated compression rates to both hidden states (prefilling stage acceleration) and the KV cache (decoding stage). The method achieves a 1.58× prefilling speedup, compresses the KV cache to 4.74–9.38% of original size, and maintains accuracy within 1–2 points of the full-size model across 16 LongBench tasks and 4 LLMs.

## Strengths

- **Prefilling-stage speedup through hidden-state compression**: Unlike prior work that compresses only the KV cache after generation, UNComp compresses hidden states *before* generating the KV cache, yielding a measured 1.58× prefilling speedup on A100 (Table 3: 48.78s vs. 77.34s) and 1.16× on MI210. This directly addresses a gap in existing eviction-based methods.

- **Extreme KV-cache compression with near-lossless accuracy**: At a KV cache size of 384 tokens (9.38% of full), Ours-group achieves 32.57 avg. on Llama2-7B vs. FullKV's 33.34 (Table 1). Across four models (Llama2-7B/13B, Llama3-8B, Mistral-7B), the method consistently ranks first or second among compression baselines on the LongBench average.

- **Training-free adaptive grouping via matrix entropy**: The effective-rank measure (truncated matrix entropy of Qₘ) is computed once on a small Wikitext2 calibration set and transfers across all test data without fine-tuning. This avoids the costly retraining required by MQA/GQA methods while still providing non-uniform compression across layers and heads.

- **Graceful degradation under extreme compression**: When retaining only 12 tokens per head or deleting 2–4 heads entirely, the method stays within 2–3 points of FullKV (Table 2, e.g., Ours-delete-2-heads 28.96 vs. FullKV 30.54). This supports the validity of differentiated compression based on effective rank.

- **Comprehensive evaluation**: Experiments cover 16 LongBench tasks, 4 LLMs, and 2 GPU architectures (NVIDIA A100, AMD MI210) with time, memory, and throughput broken down by component.

## Weaknesses

### Major

- **Core assumption linking matrix entropy to compressibility is not directly validated**. The paper hinges on the claim that layers with higher effective rank contain more informative tokens individually, therefore more tokens can be discarded without hurting performance. For heads, the opposite rule is applied (higher entropy → fewer tokens evicted). This asymmetry is crucial, yet no ablation directly tests it — e.g., comparing the effect of random eviction from high-entropy vs. low-entropy layers while controlling for layer depth. The support offered (Figure 1 showing entropy trends, plus citations to prior work) is circumstantial. The strong empirical results of the full method provide *indirect* validation, but the paper's claimed theoretical explanation remains an untested hypothesis. This does not invalidate the empirical contribution, but it weakens the paper's narrative.

### Minor

- **Key hyperparameters are not reported, harming reproducibility**. The following values are omitted: the entropy-difference threshold ε (Eq. 4, which determines how layers are grouped), the step sizes Δs_h and Δs, the number of recent tokens *l* used for cumulative attention scoring and H/R analysis, and the size of the Wikitext2 calibration set. While the conceptual framework is clear, an independent implementation cannot be built without these values. The paper should provide a complete hyperparameter table or algorithmic pseudocode.

- **Needle-in-a-haystack claim is slightly overstated**. The abstract and introduction state that UNComp "surpasses the performance of the full-size KV cache." Table 4 shows this is true for Llama2-4k (98.80 vs. 98.70) but *not* for Llama3-8k, where both UNComp variants (83.73, 84.13) fall below FullKV (84.99). The conclusion more carefully says "in specific needle-in-a-haystack tasks," which is accurate. The broader claims should be qualified to match the evidence.

- **Method description is fragmented without a clean algorithmic summary**. The compression pipeline involves inter-layer grouping (Eq. 4–6), inter-head grouping (Eq. 7), token eviction based on cumulative attention, head replacement via cosine distance, and H/R ratio selection via Pearson correlation. These components are spread across subsections with no single pseudocode block showing the full decision flow. While each piece is described individually, the lack of an end-to-end summary makes it harder to verify the method.

### Trivial

- **The effective-rank heatmap (Figure 3 in the paper) is presented but not interpreted in the main text**. The caption describes it as "the heatmap of erank_k across layers and heads," but the text does not explain what patterns it reveals or how it informed design choices, making it a missed opportunity to strengthen the motivation.

- **"Thermodynamic chart" is referenced parenthetically but not discussed** in the main text body.

## Nice-to-Haves

- A direct ablation testing the core claim: compare token eviction from high-entropy vs. low-entropy layers (controlling for depth) to directly measure whether the hypothesized relationship holds.
- An ablation of the head-replacement mechanism for pruned heads, evaluated in isolation.
- Sensitivity analysis on the choice of calibration dataset (e.g., using LongBench samples vs. Wikitext2).
- Variance or confidence intervals for the main results, especially needle-in-a-haystack.

## Removed Points

These points were removed from the review because they misread the paper, are factually wrong, or evaluate the paper against the wrong standard:

- **"CHAI comparison is inequitable"** (Harsh Critic #3, second part): The reviewer claims the comparison is unfair because CHAI uses a 77.54% compression ratio (retains more memory). The paper *explicitly* notes this difference in the table caption and still shows UNComp outperforms CHAI with *less* memory — this makes the result *stronger*, not weaker. Removed as factually backwards.
- **"Throughput conflation"** (Harsh Critic #5): The reviewer argues the 6.4× throughput gain conflates memory savings with computational speed. The paper separately reports the 1.4× single-batch speedup and explains that the larger batch is enabled by memory reduction. This is standard practice in systems-oriented ML papers and is transparently presented. Removed as not a genuine flaw.
- **"Compression rate discrepancy for Llama3 not explained"** (Harsh Critic #3, first part): The KV cache is fixed at 384 tokens; the compression ratio varies because different models have different full KV sizes (different numbers of layers, heads, head dimensions). This is a straightforward arithmetic consequence, not an omission.
- **"Training-free label should be qualified"**: The calibration stage uses forward passes on Wikitext2 — no gradient updates. "Training-free" is used consistently with community standards for this class of methods (see also H2O, SnapKV, PyramidKV).
- **"Why not just use eigenvalue count instead of entropy?"**: This is a design choice, not a weakness. Entropy provides a principled information-theoretic measure, and the paper's empirical results validate its effectiveness.
- **"Selection of Qₘ weakly justified"**: The paper provides justification (Qₘ and Kₘ have similar trends, Qₘ has larger range, less representation collapse). This is adequate for an empirical design choice.
- **Generic nitpicks** about missing related work, typos/formatting, and "strawman" criticisms that misunderstand the paper's scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a complete table of all hyperparameter values (ε, *l*, Δs_h, Δs, calibration set size) in the main text or appendix.
2. Add an ablation that directly validates the entropy-compressibility relationship — e.g., compare uniform eviction between high- and low-entropy layers.
3. Qualify the needle-in-a-haystack claim to reflect that on Llama3-8k the compressed version is slightly below FullKV.
4. Include a single algorithmic pseudocode block summarizing the full decision flow.
5. Add a brief interpretation of the effective-rank heatmap (Figure 3) to strengthen the motivation.

## Score and Decision

**Overall assessment**: The paper introduces a novel and effective approach to LLM inference compression with a genuinely useful theoretical framing (matrix entropy for adaptive grouping). The empirical evaluation is comprehensive and the results are competitive. The main concerns are (a) the central theoretical claim linking entropy to compressibility is asserted but not directly validated via ablation, and (b) missing hyperparameter values hurt reproducibility. Neither issue invalidates the empirical contribution — the method works well regardless of whether the specific entropy-compressibility explanation is correct. These are addressable in a revised version.

**Originality**: High — matrix entropy as a grouping signal for non-uniform compression is novel.
**Quality**: Good — careful evaluation across 4 models, 16 tasks, 2 GPU platforms.
**Clarity**: Adequate but could be improved with a pseudocode summary and hyperparameter table.
**Significance**: Solid — training-free adaptive compression for long-context LLM inference is practically important.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>