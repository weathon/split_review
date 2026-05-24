Now I have everything verified. Let me produce the final consolidated review.

## Summary

This paper proposes In-Context Watermarking (ICW), a method to embed detectable signals into LLM-generated text solely through prompt engineering, without modifying the model's decoding process. Four strategies (Unicode, Initials, Lexical, Acrostics) are explored across a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study motivated by detecting AI-generated peer reviews. Experiments on GPT-4o-mini and GPT-o3-mini show that with sufficiently capable models, ICW achieves detection accuracy, robustness, and text quality comparable to or exceeding existing post-hoc watermarking baselines that require model access.

## Strengths

- **Novel problem formulation addressing a real practical gap.** ICW embeds watermarks entirely through prompt engineering, requiring no access to model weights, logits, or decoding. This is fundamentally different from prior in-process watermarking (which requires model-side control) and is concretely motivated by the peer-review scenario (Section 1, Figure 1). The paper identifies a genuine use case where third parties need watermarking capability but have no influence over the LLM provider.

- **Near-perfect detection with capable LLMs is empirically demonstrated.** On GPT-o3-mini, all four ICW strategies achieve detection AUC ≥ 0.995 in both DTS and IPI settings (Table 2). Unicode and Acrostics ICW reach AUC 1.000 in DTS; in the IPI setting, Unicode achieves AUC 1.000 and the other three methods each reach AUC ≥ 0.997. This directly supports the central claim that ICW works when the underlying LLM has strong instruction-following ability.

- **ICW methods show strong robustness that exceeds baselines in key regimes.** Under word-deletion and replacement attacks, Initials ICW achieves AUC 0.999 and Acrostics ICW AUC 1.000, outperforming YCZ+23 and PostMark (Figure 3). Under paraphrasing, Initials (AUC 0.887), Lexical (AUC 0.924), and Acrostics (AUC 0.922) all exceed YCZ+23 (0.557) and approach PostMark (0.841). This demonstrates that the better ICW methods maintain detectability under realistic text transformations.

- **Text quality is close to unwatermarked output and substantially exceeds baselines.** On GPT-o3-mini, Lexical ICW (Overall 4.808) and Acrostics ICW (Overall 4.813) score near the unwatermarked baseline (4.992) while PostMark scores only 2.997 and YCZ+23 scores 3.865 (Table 3), indicating that ICW does not meaningfully degrade response quality.

- **Practical validation in a realistic long-context case study.** In the IPI peer-review setting, all ICW methods achieve detection AUC ≥ 0.997 on GPT-o3-mini (Table 2), despite the watermarking instruction being embedded within a full-length academic paper, demonstrating reliable operation in the long-context scenario the paper targets.

## Weaknesses

### Fatal
None.

### Major

- **Limited model coverage undermines the "model-agnostic" claim.** The abstract claims ICW is a "model-agnostic" approach, but experiments only test two models from a single provider (OpenAI). The paper itself acknowledges that "ICW effectiveness highly depends on the capabilities of the underlying LLMs," and methods that work well on GPT-o3-mini (Initials AUC 0.999, Acrostics AUC 1.000 in DTS) perform poorly on GPT-4o-mini (AUC 0.572 and 0.590, barely above chance). Testing across different model families (e.g., Llama-3, DeepSeek, Gemini) is needed to substantiate the general applicability claim. This does not invalidate the results on the tested models, but it limits confidence that the approach transfers broadly.

### Minor

- **The IPI threat model's practical feasibility is not validated against realistic text-processing pipelines.** The IPI setting assumes reviewers will input the full PDF into an LLM, with the watermarking instruction hidden as white text. The paper does not test whether the watermark survives standard PDF-to-text extraction (e.g., `pdftotext` or copy-paste from a PDF viewer) that may strip invisible characters. While the paper acknowledges this is left for future work (Section 3.2), the motivating case study would be substantially strengthened by even a simple validation that the watermark persists through common document-processing operations.

- **PostMark's anomalously low text-quality scores raise questions about the LLM-as-a-Judge evaluation.** PostMark achieves Relevance 2.648 and Clarity 2.494 (Table 3) — far below what one would expect from a paraphrasing-based watermark that should preserve content. This large discrepancy (compared to ICW scores above 4.5 for the same dimensions) is not explained in the paper and could indicate a flaw in the evaluation prompt or process that systematically penalizes PostMark's outputs. Since PostMark is a key baseline, this anomaly affects how favorably ICW's text-quality advantage is interpreted.

- **Initials and Acrostics ICW barely work on GPT-4o-mini yet the paper's broader framing leans heavily on "model-agnostic" language.** Table 2 shows Initials ICW AUC = 0.572 and Acrostics AUC = 0.590 in DTS with GPT-4o-mini. While the paper reports these numbers, the abstract describes ICW as a "model-agnostic, practical watermarking approach" without qualification regarding the capability threshold. A more precise characterization of the LLM capabilities required would strengthen the paper.

- **Unicode ICW's robustness profile is easy to misread from the main paper.** Table 2 reports Unicode ICW AUC = 1.000 for unmodified text, but this method is excluded from the robustness figure (Figure 3) because it is "highly fragile to transformations such as LLM-based paraphrasing or cross-platform transmission" (Section 5.2.2). A reader viewing only Table 2 could mistakenly infer that Unicode ICW is uniformly robust. The paper should make the fragility of this method more prominent.

- **Key management and synchronization in the IPI setting is underspecified.** For Acrostics ICW, the detector must know the exact secret sequence ζ used for each generation. The paper mentions using "a long ζ and different short subsequences per generation" (Section 4.2.4) but does not explain how subsequences are selected or how the detector determines which subsequence corresponds to which paper among hundreds of submissions.

- **No confidence intervals or standard errors for detection results.** Table 2 reports point estimates without uncertainty quantification. Given 500 samples per condition, bootstrapped confidence intervals would inform whether the differences between methods are statistically reliable.

### Trivial
None.

## Nice-to-Haves

- **Test at least one non-OpenAI model.** Even a single experiment on an open-weight model (e.g., Llama-3-70B, DeepSeek V3) would substantially strengthen the generalizability claim.
- **Include a human judgment study on watermark perceptibility.** For methods claiming imperceptible watermarking, even a small-scale human evaluation would be valuable.
- **Test the IPI watermark's survival through PDF-to-text conversion.** A simple experiment would validate the motivating scenario.
- **Report false positive rates at more stringent thresholds** (e.g., T@0.1%FPR) relevant to the peer-review deployment context.
- **Investigate and explain the PostMark quality anomaly** — either verifying that the evaluation is fair or identifying a systematic issue.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Scalability of Lexical ICW: the paper does not report vocabulary size used in experiments."* — The paper states implementation details are in Appendix C, which was stripped by the parser. This criticism cannot be verified.
- *"The paper should test whether watermarked text is distinguishable by human readers."* — This is not a standard expectation for LLM watermarking papers; most do not include human studies. Moved to Nice-to-Have.
- *"False positive rates at realistic thresholds: for peer review, 1% FPR may be unacceptable."* — The paper already reports T@1%F and T@10%F, which is standard practice. The question of deployment-specific thresholds is a reasonable discussion point but not a weakness.
- *"The paper does not specify which LLM was used for the paraphrasing attack."* — The paper states "paraphrasing using an LLM" in Section 5.1. While it could be more specific, this is a minor implementation detail common in the field.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated findings and limitations, without identifying unexpected empirical patterns or cross-paradigm connections that the authors missed.

## Suggestions

1. Add at least one non-OpenAI model to the evaluation to substantiate the general applicability claim. A clear failure case on a weaker model would actually strengthen the paper's secondary thesis that ICW improves with LLM capability.
2. Validate the IPI threat model against realistic PDF-to-text conversion and copy-paste operations. Even a negative result would be informative.
3. Investigate the PostMark quality anomaly — verify that the LLM-as-a-Judge prompt does not systematically penalize paraphrased text, and consider adding human judgments on a subset.
4. Clarify the capability threshold: replace or qualify "model-agnostic" with a more precise characterization of the LLM abilities required for each ICW method.

## Score and Decision

**Calibration anchors used (all rounds):**

**Round 1 (bracketing):** Low band (avg <3.5): Windtalkers (3.0), DMark (3.0), p-Mark (2.0), dMARK (3.33). Mid band (3.5–7.5): PRO (5.0, reject), CATMark (5.33), Combinatorial Watermarking (4.5, reject), OpenStamp (5.0, reject). High band (>7.5): LLMs Get Lost (8.0), Transducing LMs (8.0), Generative Universal Verifier (8.0), Gaia2 (8.0).

**Round 1 bracket:** 5.5–6.5 (clearly above rejected watermarking papers at 5.0, below strong accepted papers at 7.0+).

**Round 2 (narrowing):** PMark (7.0, accept poster), LLM Fingerprinting via Semantically Conditioned Watermarks (6.5, accept oral), plus anchors from round 1's mid band re-used: PRO (5.0), OpenStamp (5.0), Benchmark Contamination Watermarking (5.0), Watermarking Diffusion LMs (5.0).

**Comparison to anchors:** The ICW paper is substantially more novel than PRO (5.0) and OpenStamp (5.0) — both propose incremental modifications to existing decoding-based frameworks, while ICW introduces a genuinely new paradigm (prompt-only watermarking). The experimental validation is cleaner and the problem motivation is sharper. However, the ICW paper is weaker than PMark (7.0), which combines a formal theoretical framework with comprehensive evaluation, and somewhat weaker than the LLM Fingerprinting paper (6.5), which has more thorough robustness evaluation and broader model coverage. The ICW paper's main gap is evaluation breadth (2 models, 1 provider), which limits confidence in generalizability more than the accepted anchors' evaluations do.

**Final score: 6.0.** The paper makes a genuine, non-obvious contribution with clean evidence that the core idea works on capable LLMs. It is not a top-tier paper (the evaluation breadth is too narrow for that), but it is clearly above the reject threshold and addresses an important practical gap. The contribution is well-supported within its tested scope.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>