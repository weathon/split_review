## Summary

This paper proposes In-Context Watermarking (ICW), a method for watermarking LLM outputs purely through prompt engineering — without any access to model weights, logits, or decoding process. It designs four watermarking strategies at different granularity levels (Unicode, Initials, Lexical, Acrostics), each with tailored detection methods. It also introduces the Indirect Prompt Injection (IPI) setting where watermarking instructions are covertly embedded in input documents (e.g., conference papers) to detect LLM-generated peer reviews. Experiments on two OpenAI models show that with a sufficiently capable model (GPT-o3-mini), ICW achieves near-perfect detection (AUC ≥ 0.995 for all methods) while maintaining better text quality than post-hoc baselines.

## Strengths

- **Novel problem framing and approach**: ICW is the first systematic exploration of watermarking through prompt engineering alone, without privileged model access. This fills a genuine gap — scenarios where the detector has no control over or access to the LLM's decoding process. The four strategies (Unicode, Initials, Lexical, Acrostics) span character- to sentence-level granularity, and each comes with a tailored detection method. The paper validates that ICW works purely through API-level prompting (Section 5.1), which is a genuinely different operating point from all prior watermarking work.

- **IPI setting is a novel and well-motivated contribution**: The Indirect Prompt Injection threat model (Section 3.2, Figure 2) addresses a real problem that neither in-process nor post-hoc methods can handle — detecting LLM-generated peer reviews when the detector has no access to the model used. The paper demonstrates feasibility on GPT-o3-mini (AUC ≥ 0.997 for all four methods in IPI), showing that watermark instructions can be followed even when embedded within a long document. This scenario is impossible with existing approaches and is a genuinely new application of watermarking.

- **Better text quality than post-hoc baselines at comparable detection**: Table 3 shows ICW methods (e.g., Lexical ICW Overall=4.808, Acrostics ICW Overall=4.813) produce text quality far closer to unwatermarked LLM output (Overall=4.992) than PostMark (Overall=2.997), while matching or exceeding the baselines' detection AUC (Table 2). The paper explains this concretely: Lexical ICW constrains at the word level rather than character level, and Acrostics ICW constrains only sentence-initial letters, leaving the rest of generation unconstrained.

- **Systematic comparison across granularity levels with documented trade-offs**: The paper designs ICW at character, word-initial, word, and sentence levels, and the empirical results consistently corroborate the expected trade-offs — Unicode ICW works across all models but is fragile (Section 5.2.2); Initials/Lexical ICW require stronger models but are robust to editing and paraphrasing attacks (Figure 3).

## Weaknesses

### Fatal
None.

### Major
- **Limited model scope contradicts the "model-agnostic" framing**: The paper tests only two models, both from OpenAI. On GPT-4o-mini, only Unicode ICW works reliably (AUC=1.000); Initials ICW (0.572 DTS / 0.620 IPI), Acrostics ICW (0.590 / 0.592) are near-random, and Lexical ICW is marginal (0.910 / 0.889). On GPT-o3-mini, all methods achieve AUC ≥ 0.995. The abstract calls ICW a "model-agnostic, practical watermarking approach," but the non-trivial methods have only been validated on a single frontier model from one provider. The paper acknowledges that ICW effectiveness depends on LLM capability (Section 5.2.1), yet the claims in the abstract and title do not reflect this dependency. Without testing on at least one open-weight model (e.g., Llama-3) or a different proprietary model (e.g., Claude), the generalizability claim is unsupported. This is the paper's central weakness: the evidence covers one model family while the language claims broad applicability.

### Minor
- **No statistical uncertainty reported**: All results in Table 2, Table 3, and Figure 3 are point estimates without confidence intervals, error bars, or variance measures. With n=500 per condition, sampling variance exists, and many AUC values cluster near 1.0. Without error bars, it is unclear whether the small differences between methods (e.g., Initials 0.999 vs. Acrostics 1.000) are meaningful or within noise.

- **Acrostics ICW detection uses a potentially biased null distribution**: The detection method (Section 4.2.4) estimates the null distribution by resampling sentence-initial-letter sequences from the suspect text itself. If the text has a natural bias in sentence-initial letters (e.g., a paper about "Language Models" may start many sentences with "L" or "M"), the resampled null could be systematically distorted, potentially leading to uncontrolled false positive rates. The paper does not validate false positive rates on human-written text for this method.

- **IPI scenario has practical gaps that the motivating application depends on**: The IPI scenario relies on embedding invisible instructions (e.g., "white text") in PDFs. These can be detected by selecting/highlighting text, viewing PDF source code, or using accessibility tools. A reviewer who copy-pastes text (stripping invisible content) or paraphrases the paper before prompting the LLM would bypass the watermark. The paper acknowledges these are attack/defense considerations left for future work (Section 3.2, lines 100-101), but since the IPI scenario is the paper's primary motivating application, the practical viability remains uncertain.

- **Unicode ICW — the only method that works across model capabilities — has limited practical utility**: Unicode ICW achieves perfect detection by inserting zero-width spaces, but these are trivially removed by LLM-based paraphrasing, cross-platform copy-paste, standard PDF text extraction, and text normalization pipelines. The paper acknowledges this fragility and transparently excludes Unicode ICW from the robustness figure (Figure 3, line 230). However, this means the only truly model-agnostic method is also the one with the most limited real-world applicability.

### Trivial
None.

## Nice-to-Haves
- Adding a comparison against in-process watermarking methods (e.g., Kirchenbauer et al. 2023, Aaronson 2023) would help quantify the performance trade-off of giving up model access, even though the deployment scenarios differ.
- Testing on a broader range of models — at least one open-weight model (e.g., Llama-3-70B) and one non-OpenAI proprietary model — would substantiate or refute the paper's claim that ICW effectiveness correlates with model capability.
- Testing whether hidden IPI instructions survive common PDF-to-text pipelines (e.g., PyMuPDF, pdfplumber) before LLM processing would strengthen the IPI application claims.

## Removed Points
- **"Baselines are angled / straw man comparison"**: Removed. The paper compares against post-hoc methods (PostMark, YCZ+23) which are the natural baselines for a black-box setting. The paper does not frame this as "winning" against in-process methods; it correctly notes those methods require model access. The criticism misunderstands the paper's contribution.
- **"Table 1 filled/empty circles are decorative"**: Removed as a presentation nitpick.
- **"Bahri et al. 2024 should be a baseline"**: Removed. Bahri et al. is still an in-process method requiring control over decoding (via repeated sampling). Not applicable in ICW's setting.
- **"LLM-as-a-Judge prefers GPT-o3-mini style"**: Removed. The comparison is between ICW methods and baselines using the same model, so the judge bias is constant across conditions.
- **"Missing related works"**: Removed per instructions.
- **"Missing hyperparameters / reproducibility details"**: Removed. Implementation details are deferred to Appendix C, standard practice for this venue.
- **"IPI not tested on GPT-4o-mini"**: Factually wrong — Table 2 shows IPI results for GPT-4o-mini (though they are poor). The paper does test this.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface a perspective on the ICW approach that the paper itself does not already discuss.

## Suggestions

1. **Re-scope the claims.** The abstract and title should reflect that ICW is a feasibility study demonstrating that frontier models can follow watermarking prompts, rather than a "model-agnostic, practical" solution. The results are genuinely interesting when framed appropriately.
2. **Add confidence intervals or error bars** to all main results (Table 2, Table 3, Figure 3) to allow readers to assess the reliability of differences between methods.
3. **Validate Acrostics ICW false positive rates** on human-written text to verify the resampling-based detection is well-calibrated under realistic sentence-initial letter distributions.
4. **Test on at least one open-weight model** (e.g., Llama-3-70B) and one non-OpenAI proprietary model to establish generalizability or honestly scope the claims to the observed correlation with model capability.

---

**Calibration anchors used:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|-----------|
| A Watermark for Black-Box LMs | 4.60 (Reject) | 1, 2 | Most comparable setting (black-box access). ICW has greater novelty (prompt-only vs. sampling-based) but thinner evaluation. ICW is slightly stronger. |
| Sparse Watermarking in LLMs | 3.00 (Reject) | 1 | Lower quality watermark paper. ICW clearly stronger. |
| On the Reliability of Watermarks | 6.00 (Accept) | 1 | Well-executed robustness study with thorough experiments. ICW is weaker in evaluation breadth. |
| WASA: Watermark-based Source Attribution | 5.50 (Reject) | 2 | Different focus (source attribution). ICW is similar overall quality but different evaluation strengths/weaknesses. |
| Can Watermarks Detect LLM IP Infringement | 5.80 (Accept) | 2 | Well-defined problem but limited baselines. ICW is comparable in overall quality. |
| Watermarking: Semantic-aware Speculative Sampling | 6.00 (Reject) | 2 | Strong theory but proof issues. ICW is weaker theoretically but has a cleaner idea. |
| I Know You Did Not Write That | 3.67 (Reject) | 1, 2 | Low-quality watermark paper with limited novelty. ICW clearly stronger. |
| Black-Box Detection of LM Watermarks | 7.00 (Accept) | 1, 2 | Different problem (detecting existing watermarks). Strong execution. ICW is weaker. |

**Round 1 bracket:** 4.0 – 6.0
**Narrowing process:** The closest comparable paper (A Watermark for Black-Box LMs, 4.60, Reject) shares a constrained-access setting. ICW is more novel (prompt-only) but has thinner evaluation (only 2 models from same provider). Papers at 5.5–6.0 have broader evaluation or stronger theory. ICW sits between these bands.
**Final score:** 5.0 — a creative, well-motivated idea with significant evaluation limitations that prevent the current evidence from fully supporting the claimed scope.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>