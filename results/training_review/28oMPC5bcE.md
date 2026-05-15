Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces UNComp, a training-free compression scheme that uses matrix entropy (effective rank) to measure model uncertainty across layers and heads, then adaptively compresses both hidden states (during prefilling) and KV cache (during decoding). The method groups layers and heads by their effective rank to apply differentiated compression rates. Experiments on 4 LLMs across 16 LongBench tasks show competitive or state-of-the-art results among training-free compression methods, with a 1.58× prefill speedup and KV cache reduction to 4.74% of original size.

## Strengths

- **Novel use of matrix entropy to guide adaptive compression across both layers and heads.** The paper introduces truncated matrix entropy as a principled measure of uncertainty, showing empirically that Q and K matrices exhibit similar entropy trends across layers, and that entropy varies significantly across heads. This provides a more informed grouping mechanism than uniform compression. The approach is training-free and requires only a small calibration set (Wikitext2) for grouping.

- **Strong empirical performance across diverse models and tasks.** In Table 1, UNComp variants achieve the highest or second-highest average scores across all 4 models (Llama2-7B/13B, Llama3-8B, Mistral-7B) among 5 training-free compression methods on 16 LongBench tasks. For example, on Llama3-8B at 4.74% KV size, Ours-group reaches 40.21% average vs. 38.88% for the next best (PyramidKV).

- **Demonstrated prefill speedup from hidden-state compression.** Table 3 shows a 1.58× prefill speedup (48.78s vs. 77.34s) on a single A100, with throughput improvements of 6.4× at batch size 32 vs. FullKV at batch size 6. This addresses a practical bottleneck that most KV cache compression methods overlook.

- **Extreme compression robustness.** Table 2 shows that even at 12 tokens per head (1.56% effective KV size), UNComp maintains an average score of 26.08% vs. FullKV's 30.54%, substantially outperforming baselines at 64 tokens (e.g., PyramidKV 22.06%, SnapKV 20.38%). Head deletion (2 heads/layer) yields only 1.58 points below full KV.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Asymmetric compression rule for layers vs. heads is explained but inadequately validated.** The paper uses the same effective-rank metric to drive opposite behaviors: higher entropy → more token eviction for layers, but higher entropy → fewer tokens evicted for heads. The paper does provide reasoning (lines 89–91: across layers tokens share information so individually informative tokens make discarding safe; across heads different information is captured so informative heads should be preserved). However, no ablation tests the alternative assignment, and the rationale is presented as a post-hoc observation rather than a principled derivation. A controlled experiment swapping the direction for either dimension would significantly strengthen the claims.

2. **The claim of "outperforming FullKV" in needle-in-a-haystack is overstated and lacks statistical support.** Examining Table 4: on Llama2-4k, Ours-group-stage achieves 98.80% vs. FullKV's 98.70% (a +0.10% difference). On Llama3-8k, both UNComp variants are *below* FullKV (Ours-group 84.13% vs. FullKV 84.99%). The abstract's claim that "UNComp outperforms the full-size KV cache" in this task is too broad — it is true only for one of two tested models, and neither comparison includes confidence intervals or multiple seeds. The small magnitude of the reported advantage (0.10%) warrants caution. The conclusion's phrasing ("specific needle-in-a-haystack tasks") is more accurate but the abstract should match.

3. **Eigenvalue elbow-point detection is underspecified.** Truncated matrix entropy (Section 3.2) requires selecting the top‑k eigenvalues before an "elbow point." No algorithm for detecting this elbow is specified (e.g., kneedle, maximum curvature, fixed threshold), and no sensitivity analysis is provided. Since the grouping and compression rates depend on this choice, the method is not fully reproducible as described.

4. **Threshold ε for determining compression stages (Eq. 6) is not specified or analyzed.** The number of layer groups C depends on ε, yet its value is never given, nor is its impact on downstream performance studied. Together with the elbow point issue, the compression pipeline has two unspecified hyperparameters that could affect results.

5. **UNComp's qualitative advantage over a method with the same budget but uniform head compression is not isolated.** Because UNComp uses both (a) differentiated head compression rates and (b) hidden-state compression during prefilling, it is unclear how much of the gain comes from each component. The paper compares Ours-group (KV-only compression) and Ours-group-stage (both), but a cleaner ablation would compare UNComp's differentiated head grouping against a uniform-head variant at the same *total* KV budget.

### Trivial
- The needle-in-a-haystack experiment (Table 4) would benefit from full-length context KV size baselines being stated explicitly for each model (the paper reports 9.38% compression for Llama2 and 4.74% for Llama3 in Table 1 but only states "KV size = 384" for the needle table).

## Nice-to-Haves
- Repeating the main evaluation at a fixed *fraction* of original KV size (e.g., 5%, 10%) alongside the fixed absolute budget would address whether the advantage holds across compression levels.
- An analysis of the elbow-point sensitivity (varying the detection method and reporting performance changes) would strengthen reproducibility.
- Error bars or multiple-seed results for the needle-in-a-haystack and main benchmark tables would make small performance differences interpretable.

## Removed Points
- **Criticism about "contradictory" asymmetry being "never explained or reconciled."** The paper does explain the asymmetry (lines 89–91): across layers, tokens share information with depth so individually informative tokens can be discarded; across heads, different heads capture different information so informative heads should be preserved. This is a design rationale, not a contradiction. The criticism is inaccurate in claiming it is wholly unexplained, though the validation is thin (kept above as Minor #1).
- **Criticism about fixed absolute KV size being unfair.** Fixing the absolute budget is a standard evaluation practice in compression research. The paper reports the resulting compression ratios (9.38%, 4.74%) transparently. This is a valid experimental design choice, not a flaw. Moved to Nice-to-Haves as an alternative viewpoint.
- **"CHAI is given a different compression scheme making comparison misleading."** The paper acknowledges this explicitly in the Table 1 caption. It is not a hidden weakness.
- **"Speedup is orthogonal to the entropy-based grouping."** The hidden-state compression *is* the method's contribution and uses entropy-based grouping. This is not a weakness.
- **Criticism about the introduction not formally tying "uncertainty" to compressibility.** Matrix entropy is the formal definition. The paper is clear about this.
- **Strength Finder claims that conflict with verified weaknesses.** The needle-in-a-haystack strength is retained but constrained as discussed above.
- **Generic strengths from the Strength Finder.** Removed generic phrasing and kept only strengths backed by specific evidence from the paper.

## Novel Insights
The reviewers' perspectives mostly corroborate the paper's own claims and identify the same limitations the paper partially acknowledges. One genuinely novel observation from cross-referencing the critiques: the paper's core technical contribution — using matrix entropy as a signal for adaptive compression — is promising, but the key question is whether the asymmetric layer-vs-head rule is an artifact of the specific experimental setup or a genuinely generalizable property of transformer representations. The paper lacks the controlled ablation that would distinguish these cases. This is the single most important question for future work.

## Suggestions

1. Add an ablation that swaps the compression direction: apply the "head rule" to layers and the "layer rule" to heads, to verify that the asymmetric policy is indeed better than either uniform or reversed assignment.
2. Specify the elbow-point detection algorithm (or at minimum the exact eigenvalue cutoff criteria used in the experiments) and report sensitivity to this hyperparameter.
3. Add confidence intervals or multiple-seed results for key comparisons, especially the needle-in-a-haystack task where small differences are claimed as advantages.
4. Report the value of ε used in Eq. 6 and perform a sensitivity sweep on it.
5. Soften the abstract's claim about needle-in-a-haystack ("UNComp outperforms the full-size KV cache") to reflect that this occurs on specific models/datasets.

## Score and Decision

The paper addresses a relevant problem (efficient long-context LLM inference) with a novel approach (matrix-entropy-guided adaptive compression) that is training-free and yields solid empirical gains. The main weaknesses — insufficient validation of the asymmetric compression rule, a moderately overstated needle claim, and underspecified procedural details — are addressable in revision and do not invalidate the core contribution. The evaluation is comprehensive (16 tasks, 4 models, 2 GPU architectures) and the results are competitive.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>