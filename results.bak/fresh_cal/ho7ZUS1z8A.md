Now I have a thorough understanding of the paper and can evaluate all reviewer claims against the actual text. Let me write the consolidated review.

---

## Summary

This paper proposes MoE-SVD, a training-free SVD-based compression framework for Mixture-of-Experts LLMs. The method introduces selective decomposition guided by a sensitivity metric, V-matrix sharing across experts, and U-matrix trimming to address challenges specific to MoE architectures (decomposition sensitivity, mismatched activation statistics, and expert redundancy). Experiments on Mixtral-8×7B, Phi-3.5-MoE, DeepSeek-MoE-16B, and Mixtral-8×22B show large improvements over existing SVD-based compression methods (ASVD, SVD-LLM) that collapse on MoE models.

## Strengths

1. **Novel diagnosis of why SVD fails on MoE**: Figure 1 and the accompanying analysis identify three concrete obstacles — decomposition sensitivity (initial/final expert layers cause disproportionate perplexity spikes), mismatch of dense-LLM activation statistics (OWL values do not correlate with per-layer decomposition impact on MoE), and expert redundancy (high CKA similarity of decomposed V-matrices). This evidence directly motivates the paper's technical components and distinguishes it from naively applying dense-model SVD methods.

2. **Selective decomposition metric validated**: Table 3 compares uniform SVD, OWL-based non-uniform SVD, and the proposed sensitivity-based non-uniform decomposition on Mixtral-8×7B. The proposed metric yields the lowest perplexity and highest accuracy across compression ratios, supporting the core claim that a tailored decomposition strategy is needed for MoE.

3. **Matrix trimming improves perplexity (counterintuitive but documented)**: Table 4 shows that increasing the number of trimmed U-matrices leads to strictly lower perplexity on WikiText-2. This directly supports the claim that expert weight redundancy is being reduced by the sharing/trimming scheme.

4. **Consistent and large margins over SVD baselines**: At 20% compression on Mixtral-8×7B, MoE-SVD achieves WikiText-2 perplexity of 5.94 vs 9.44 (ASVD) and 13.45 (SVD-LLM); at 60% compression, MoE-SVD maintains 33.24 while all SVD baselines exceed 3000 perplexity. Similar trends hold for Phi-3.5-MoE and on common-sense reasoning tasks. These margins demonstrate that the method solves a real failure mode of existing SVD approaches on MoE.

5. **Generalization across MoE architectures**: Results on DeepSeek-MoE-16B (0.56→0.42 avg accuracy) and Mixtral-8×22B (0.70→0.57) in Table 6 show the method is not limited to a single model family.

6. **Thorough ablation and robustness analysis**: Calibration data robustness (Table 5 — WikiText-2 vs C4), sensitivity to sample count and random seed (Figure 5), combination with GPTQ quantization (Table 8), and LoRA fine-tuning (Table 7) provide a well-rounded empirical characterization.

## Weaknesses

### Fatal
None.

### Major

1. **Method sections (2–3) are absent from the extracted text**: The paper jumps from Section 1 (Introduction) directly to Section 4 (Experiments). The detailed technical exposition of MoE-SVD — how the sensitivity metric is computed, the exact procedure for selective decomposition, the V-matrix sharing implementation, the U-matrix trimming mechanism, and the formal definition of compression ratio — is not present. While this is likely a PDF extraction artifact (the abstract and conclusion outline the method at a high level), it prevents full evaluation of technical soundness, novelty, and reproducibility. *The paper as presented cannot be fully assessed.*

2. **Baseline comparison is narrow relative to the claims**: The experiments compare only against SVD-based methods (vanilla SVD, ASVD, SVD-LLM). The introduction cites MoE-specific compression methods (expert pruning, dynamic skipping; Lu et al., 2024; He et al., 2024; Liu et al., 2024a), yet none appear in the experiments. The paper's limitations section states MoE-SVD is "orthogonal to previous pruning-based approaches" and deliberately omits such comparisons. This defense is reasonable for positioning MoE-SVD as a decomposition-based alternative, but the abstract's claim of "consistently outperform[ing] existing compression methods" is too broad without at least one representative MoE-specific baseline (e.g., expert pruning at comparable compression ratios) to contextualize the trade-offs.

3. **"Minimal performance degradation" is overstated at high compression**: The abstract and conclusion describe the 60% compression result as achieving "minimal performance degradation." At 60% compression on Mixtral-8×7B, WikiText-2 perplexity reaches 33.24. While this is dramatically better than baselines that exceed 3000, it represents severe degradation relative to the uncompressed model (which would be ~4–5 perplexity). The paper would benefit from honestly characterizing the compression-performance frontier — the method works well at 20–30% compression but degrades substantially at 60% — and reserving "minimal degradation" for the lower compression regime.

### Minor

1. **Original model performance not shown in the main results table**: Table 2, which reports the primary comparison, does not include a row for the original (uncompressed) model perplexity/accuracy for Mixtral-8×7B and Phi-3.5-MoE. Table 6 includes original performance for other models, so the omission in the main table is inconsistent. Without the original values, the reader cannot gauge absolute degradation. This should be added.

2. **Inference speedup is modest relative to parameter reduction**: At 60% parameter compression, the achieved speedup is 1.52–1.53×. A 60% reduction in parameters would naively suggest up to 2.5× speedup if compute-bound. The paper does not analyze why the speedup is lower (likely memory-bandwidth bottlenecks). A brief discussion would strengthen the acceleration claims.

3. **"Compression ratio" is not formally defined**: The paper uses "60% compression ratio" but the reported memory reduction is to 43.45% of original (i.e., a 56.55% reduction). The discrepancy is small but the definition should be explicit — does it refer to parameter count reduction, rank reduction, or memory footprint reduction?

4. **U-matrix trimming explanation is insufficient**: Table 4 shows that trimming more U-matrices *improves* perplexity. The paper attributes this to "reduction of experts, resulting in more stability." This is counterintuitive (removing more components of the weight matrices improves performance) and deserves a more thorough mechanistic explanation — are trimmed matrices encoding noisy/low-signal information? The current explanation is too brief.

### Trivial
None.

## Nice-to-Haves

- Adding at least one MoE-specific pruning baseline (e.g., expert-level pruning at comparable compression ratios from He et al. 2024) would substantially strengthen the empirical positioning, even if MoE-SVD is framed as complementary.
- Reporting standard deviations or multiple-run statistics for key perplexity/accuracy results.
- Analysis of the offline computational cost of performing SVD on all expert layers.
- A more detailed breakdown of where the inference speedup comes from (expert size reduction vs. reduced expert count vs. memory bandwidth effects).

## Removed Points

- **"Missing method description" treated as fatal by harsh critic**: Downgraded from Fatal to Major. The omission of Sections 2–3 from the extracted text is severe but is almost certainly a PDF extraction artifact, not author negligence. The high-level method is described in the abstract and introduction, and the experimental validation provides evidence of functionality. In a real submission these sections would be present.
- **"No original model performance" framed as a critical omission**: The paper does describe original performance in Table 6 for other models. The omission in Table 2 is a minor inconsistency (addressed in Minor weaknesses above), not a fatal flaw.
- **Harsh critic's section-by-section nitpicks about "no comparison with pruning" framed repeatedly**: Consolidated into a single Major weakness above. The repetition inflated the severity.
- **Criticism that Table 2 is "missing"**: Table 2 is referenced and its contents are described in detail in the text (lines 46–47). The table itself is an image not rendered in the extracted text, which is a parser limitation.
- **Strength Finder's claim about "Measurable inference speedup" as a separate strength**: Retained implicitly under strengths 4 and 5 but not listed as a separate bullet since the acceleration (1.52–1.53×) is modest relative to the compression achieved, as noted in Minor weaknesses.
- **Criticisms about "typos, missing punctuation, formatting artifacts"**: Removed per instructions — these are parser errors, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations about the paper that the paper itself does not already articulate or imply.

## Suggestions

1. **Include a row for the original (uncompressed) model in Table 2** so the reader can assess absolute degradation at each compression level.
2. **Add at least one MoE-specific compression baseline** (e.g., expert pruning at comparable compression ratios) to contextualize where SVD-based compression sits relative to pruning-based approaches. Even a brief discussion acknowledging the trade-offs would strengthen the paper.
3. **Define "compression ratio" explicitly** — state whether it refers to parameter count reduction, memory footprint reduction, or rank reduction, and ensure the reported memory savings are consistent with the definition.
4. **Tone down the "minimal performance degradation" framing** for high compression ratios (50–60%). The method's genuine strength is that it prevents catastrophic collapse (where baselines exceed 3000 perplexity) rather than achieving minimal absolute degradation.
5. **Provide a brief analysis of inference speedup** — explain why 60% parameter reduction yields only ~1.5× speedup (likely memory-bandwidth bound) and what this implies for deployment scenarios.
6. **Expand the explanation of U-matrix trimming** — why does removing more components of the weight matrices improve perplexity? Is the redundant information actually harmful/outlier-prone?

## Score and Decision

The paper introduces a well-motivated SVD-based compression framework for MoE LLMs, supported by a clear diagnosis of why existing SVD methods fail on MoE and experiments showing large improvements over those methods. However, the evaluation is compromised by two issues: (1) the method sections (2–3) are absent from the extracted text, preventing full technical assessment; and (2) the baseline comparison is limited to SVD methods only, while the paper's claims are framed broadly. Additionally, some claims about "minimal degradation" are overstated at high compression ratios. These issues are addressable, but in the current form the paper does not provide sufficient evidence to fully validate its central claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>