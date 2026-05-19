- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5
Now I have thoroughly verified the paper against the reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces **DTVLT**, a multi-modal benchmark for visual language tracking (VLT) that uses LLMs to generate diverse text descriptions across five tracking datasets (OTB99_Lang, GOT-10k, LaSOT, TNL2K, MGIT), covering short-term, long-term, and global instance tracking. The benchmark provides four granularities of text (initial/dense × concise/detailed), producing 240.8K sentences and 5.2M words — 45.9× more text than existing human-annotated VLT benchmarks. The paper evaluates three VLT trackers (MMTrack, JointNLT, UVLTrack) under direct testing and retraining, finding that multi-granular text reveals algorithmic bottlenecks (e.g., JointNLT's sensitivity to distribution shift).

## Strengths

- **Massive scale and coverage**: DTVLT provides 240.8K sentences (5.2M words) across 13,134 videos with 8.17M total frames — far exceeding any existing VLT benchmark. It is the only benchmark covering short-term, long-term, and global instance tracking simultaneously (Table 1, line 83). The dense descriptions alone are 45.9× larger than all official human annotations combined (line 168).

- **Multi-granular text generation**: The four-way design (initial/dense × concise/detailed) is a principled advance over existing benchmarks that offer only a single-sentence-per-video annotation (OTB99_Lang, LaSOT, TNL2K) or uniformly dense text (MGIT). This enables fine-grained analysis of how text length, density, and specificity affect tracking performance — something no prior benchmark supports (Table 2, Figure 2).

- **Experimental evidence that the benchmark reveals algorithmic blind spots**: The direct-testing results (Table 3) show that JointNLT drops from 65.1→55.1 AUC (OTB99_Lang) and UVLTrack drops from 64.0→60.8 AUC (MGIT) when given LLM-generated text, while MMTrack (which handles variable-length input) maintains or improves performance. This demonstrates that DTVLT surfaces distribution-shift vulnerabilities that single-granularity benchmarks cannot detect — directly supporting the claim that existing VLT benchmarks allow "memorize the answer" behavior (line 233).

- **Practical generation efficiency**: The pipeline generates text at 2 seconds per frame on a single RTX-3090 GPU (line 168), demonstrating that LLM-based annotation is scalable and cost-effective compared to the expensive manual process of prior benchmarks.

- **Dual evaluation protocol**: Using both zero-shot (direct testing with official weights) and retraining (50 epochs) provides complementary views of how trackers respond to diverse text, strengthening the analysis beyond what a single evaluation mode would offer (Section 5.1, lines 186-188).

## Weaknesses

### Fatal
None.

### Major

- **No validation of generated text quality.** The paper's core product is LLM-generated text, yet it provides zero assessment of whether those texts are correct, coherent, or useful. The paper reports word counts, vocabulary size, and generation speed, but no human evaluation, no automated quality metrics (e.g., CLIP score, captioning metrics against ground-truth video content), no error analysis, and no inspection of failure cases in the text. The claim that the LLM "produces high-quality, diverse text" (abstract, line 4) is asserted without evidence. This undermines confidence in the benchmark: performance differences between conditions could reflect LLM artifacts (e.g., hallucinated attributes, irrelevant scene descriptions) rather than meaningful variation in semantic granularity. For a benchmark contribution, basic quality assurance is essential.

- **Limited experimental scope for the conclusions drawn.** Three trackers (MMTrack, JointNLT, UVLTrack) are evaluated, all with similar Transformer-based architectures. The paper draws broad conclusions — that trackers "memorize answers," that "sequence generation is more conducive to learning unified visual-language features" (line 233), that "the current algorithm's handling of long texts... needs refinement" — from this small, homogeneous sample. Without evaluating trackers with different design paradigms (e.g., region-proposal-based methods like SNLT, temporal-consistency methods like QueryNLT), these conclusions are not generalizable. Additionally, the retraining protocol (50 epochs on top of official weights with mixed data including RefCOCOg) is non-standard and confounds adaptation to new text with potential overfitting or hyperparameter mismatch. The paper does not report per-granularity breakdowns for the retraining results (Figure 3 shows only aggregate mean differences), making it impossible to see which text types caused improvement or degradation.

- **No control isolating text source from text structure.** The "Official" vs. DTVLT comparisons (Table 3) confound text source (LLM vs. human), text granularity (single vs. multi-granular), and vocabulary shift simultaneously. Without a control condition using human-written text at the same granularity (e.g., human-written dense concise/detailed descriptions for a subset), the paper cannot attribute performance differences to the LLM generator's content vs. the multi-granular structure it advocates. This weakens the central claim that multi-granular LLM text is the active ingredient.

### Minor

- **LLM and generation details are not specified in the paper.** The paper cites DTLLM-VLT for the generation pipeline but does not state which LLM model was used (e.g., GPT-4, LLaMA, or another), the prompt template, temperature, any filtering or post-processing, or how video frames and bounding boxes are fed to the LLM (single frame vs. multiple frames). While the cited paper may contain these details, a self-contained benchmark paper should document its annotation methodology at a level that allows informed critique and reproducibility.

- **Bad case analysis is anecdotal.** Only three failure cases are shown (Figure 4), and they describe generic tracking challenges (appearance change, background interference) rather than cases where the *text itself* misleads the tracker (e.g., hallucinated attributes causing drift). This misses an opportunity to validate whether the generated text introduces new failure modes or faithfully captures the visual content.

- **Retraining results lack granularity breakdown.** Figure 3 plots mean differences across all conditions but does not show per-granularity breakdowns, making it impossible to see which text types (initial concise, dense detailed, etc.) drove improvement or degradation for each tracker.

### Trivial
- Several minor grammatical issues exist throughout (e.g., "bacause" in Figure 1 caption, line 21; "The vocabulary is rich" is asserted rather than demonstrated quantitatively).
- The paper claims the 100-frame update frequency is "optimal" (line 159) without ablation; this should be softened to "motivated by the 4-second memory threshold."

## Nice-to-Haves
- Adding more diverse baselines (e.g., SNLT, QueryNLT) to strengthen the generality of the conclusions.
- A controlled experiment holding text source constant (all LLM) while varying only granularity to isolate the effect of multi-granularity itself.
- Per-sequence or per-category error analysis to reveal specific failure modes tied to text properties.
- Confidence intervals or variance estimates for key results, especially on smaller datasets like OTB99_Lang (99 videos).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not interrogate why JointNLT declines"** — Factually incorrect: the paper explicitly states "JointNLT and UVLTrack sets 50 as a maximum limit and truncates the excess information" (line 184). This is a valid explanation for the performance drop.
- **"SNLT, GTI, AdaSwitcher, QueryNLT... are absent — the paper does not cite the most current works"** — UVLTrack is included as a baseline. The other methods are cited in the related work (line 62). The hard rule prohibits citing missing related works.
- **"No statistical significance or variance"** — Single-run evaluation is standard practice in SOT/VLT benchmarking. Requesting confidence intervals for every comparison is beyond community norms for this type of contribution.
- **"Open-source generation code... the community needs the pipeline"** — The paper states it will release the toolkit (abstract, line 4). Per the hard rule, reproducibility nitpicks about implementation details are removed. The LLM model identity concern is retained as a minor weakness above.
- **"The claim that MGIT text is 'excessively lengthy and complex' is a framing choice, not an established fact"** — This is a critique of the paper's motivation framing, not of its methodology or results. The paper is entitled to its characterization.
- **"The claim that 'sequence generation is more conducive to learning unified visual-language features' is post-hoc"** — The paper provides supporting reasoning: MMTrack treats VLT as token generation and avoids text length truncation (line 184). The experimental results show MMTrack outperforming, which is consistent with this interpretation.

## Novel Insights

The harsh critic's diagnosis — that the lack of text quality validation is the structurally weakest point — is correct and important. However, the critic's assertion that this makes the benchmark "untrusted" is overstated: the experimental results demonstrate that DTVLT surfaces meaningful algorithmic differences (e.g., JointNLT's text-length sensitivity), and the fact that MMTrack improves with DTVLT text provides indirect evidence that the generated text is usable. The more novel observation is that the paper conflates two distinct research questions — "does multi-granular text improve evaluation?" and "does LLM-generated text work as well as human text?" — and the experimental design does not separate them. The strength finder correctly identifies the benchmark's scale and multi-task coverage as genuine contributions, but these are undercut by the absence of any quality gate on the core product.

## Suggestions

1. **Validate a sample of generated text.** Select 500-1000 descriptions across granularities and have human annotators rate correctness, informativeness, and consistency with the video. Report error categories (hallucination, irrelevant detail, accurate description). This single addition would dramatically strengthen the paper's credibility as a benchmark contribution.

2. **Add a human-text control at matched granularity.** On a subset (e.g., OTB99_Lang), have humans write concise/detailed text at initial and dense frequencies. Compare tracker performance on LLM vs. human text at the same granularity to isolate the effect of text source.

3. **Expand baseline coverage.** Add at least 1-2 more diverse VLT trackers (e.g., an RPN-style method like SNLT and a temporal-matching method like QueryNLT) to support the claim that the benchmark reveals general algorithmic bottlenecks rather than idiosyncrasies of three similar architectures.

4. **Report per-granularity results for the retraining experiment** so readers can see which text types drive improvement or degradation.

5. **State the specific LLM used, prompt template, and any filtering** in the final version or a supplementary document.
