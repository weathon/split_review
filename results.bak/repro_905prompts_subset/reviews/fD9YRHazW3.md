Now I have all the information needed to produce a calibrated final review. Let me synthesize everything.

## Summary

This paper introduces In-Context Watermarking (ICW), a paradigm for embedding detectable watermarks into LLM-generated text entirely through prompt engineering, without any access to the model's internal decoding, logits, or sampling process. Four strategies (Unicode, Initials, Lexical, Acrostics) are proposed and evaluated in both a direct text stamp (DTS) setting and an indirect prompt injection (IPI) setting motivated by detecting AI-generated peer reviews. Experiments with GPT-o3-mini show strong detection performance (AUC up to 1.000) and robustness comparable or superior to post-hoc watermarking baselines.

## Strengths

- **Novel watermarking paradigm requiring no model access.** The paper introduces a genuinely new approach — watermarking via prompt engineering alone — that operates in settings where existing in-process methods (Kirchenbauer et al., Aaronson, etc.) are inapplicable because the embedder has no access to logits, weights, or decoding. The four strategies (Unicode, Initials, Lexical, Acrostics) are well-motivated with clear trade-offs summarized in Table 1. This is a significant conceptual departure from prior work.

- **Strong detection results with capable LLMs.** With GPT-o3-mini, Acrostics and Unicode ICW achieve ROC-AUC of 1.000 in the DTS setting (Table 2), and Initials, Lexical, and Acrostics all exceed 0.995 in DTS and 0.997 in IPI. These results validate that sufficiently capable LLMs can reliably follow watermarking instructions embedded in prompts or concatenated with long documents.

- **Superior robustness against paraphrasing compared to post-hoc baselines.** Under LLM-based paraphrasing attacks, Lexical ICW (AUC 0.924) and Acrostics ICW (AUC 0.922) substantially outperform PostMark (AUC 0.841) and YCZ+23 (AUC 0.557), as shown in Figure 3. This is a meaningful practical advantage.

- **Theoretical false positive rate control.** For Initials and Lexical ICWs, the paper provides a theoretical guarantee on controlling the false alarm rate via z-statistic detection, with derivations in Appendix B. This formal grounding distinguishes ICW from purely heuristic approaches.

## Weaknesses

### Major

- **IPI experiments do not validate the real-world covert-embedding scenario.** The paper's central motivating application is the peer-review setting, where conference organizers covertly embed a watermarking instruction into a paper PDF (e.g., as white text, zero-font, or transparent text) so that a reviewer who copies the PDF into an LLM produces detectable watermarked output. However, the IPI experiments simply concatenate the watermark instruction to the paper text in the prompt (Section 3.2: "the stamped text \tilde{t} is given by concatenating the two"). The paper does not test whether LLMs extract and follow instructions that are hidden via any obfuscation method — white-on-white text, zero-font-size characters, PDF metadata, or any other technique that would survive realistic PDF text extraction pipelines. The paper acknowledges this as future work ("a detailed investigation of attack and defense methods is left for future work"), but the gap is significant: the most salient claimed use case is not experimentally validated. The IPI results are best interpreted as demonstrating that LLMs follow watermarking instructions in long-context scenarios, which is useful but weaker than the paper's framing suggests.

### Minor

- **LLM-as-a-Judge evaluation shows likely systematic bias that is not acknowledged.** In Table 3, unwatermarked GPT-o3-mini text receives near-perfect scores (Relevance 4.982/5, Quality 5.000/5, Clarity 4.994/5), while human-written text from ELI5 scores substantially lower (4.318, 4.440, 3.946). This strongly suggests the gemini-2.0-flash judge systematically prefers LLM outputs, making comparisons between watermarked and unwatermarked text along this metric unreliable for assessing *absolute* quality degradation. The paper does use perplexity as a complementary metric (results in Appendix D.1), which is appropriate, but the main text relies heavily on the LLM judge scores without discussing this bias. Fortunately, the key comparisons (ICW vs. baselines) use the same judge, so relative rankings are less affected.

- **Detection metrics lack uncertainty quantification.** All detection metrics (ROC-AUC, T@1%F, T@10%F) are reported as point estimates on 500 watermarked and 500 human texts. For T@1%F, which corresponds to only 5 false positives out of 500, the variance is non-negligible. Bootstrapped confidence intervals or standard errors would significantly improve scientific rigor, especially given that some comparisons between methods are close.

- **Experiments limited to two proprietary models.** All experiments use only GPT-4o-mini and GPT-o3-mini, both from OpenAI. Evaluating on at least one open-weight model (e.g., LLaMA-3-70B, Qwen2.5-72B) would strengthen the claim that ICW is a general approach not specific to a particular API. This does not invalidate the results but limits generalizability claims.

### Trivial

- Table 1's "LLM requirements" dimension is presented qualitatively via filled/unfilled circles without any quantitative backing or measurement, making it hard to compare across strategies.

## Nice-to-Haves

- **Validate IPI with actual covert embedding techniques** (e.g., white-on-white text, zero-font, metadata injection) — this would directly test the motivating peer-review scenario.
- **Supplement LLM-as-a-Judge with human evaluation** or an A/B preference test between watermarked and unwatermarked texts.
- **Report detection metrics with bootstrapped 95% confidence intervals** to support rigorous comparison.
- **Evaluate on open-weight models** to strengthen generality claims beyond OpenAI's API.

## Removed Points

- The harsh critic's concern about "the paraphrase attack does not specify the LLM used for paraphrasing" — this detail would be in Appendix C, which is stripped by the parser from all papers. The original submission contains this information.
- The harsh critic's claim that "perplexity results are deferred to the appendix" as a weakness — the paper explicitly mentions both LLM-as-a-Judge and perplexity in Section 5.1 Evaluation Metrics, reports the LLM judge in the main table, and notes the perplexity results are in Appendix D.1. This is standard practice.
- The strength finder's claim that Acrostics ICW achieves "perfect" 1.000 in both DTS and IPI — IPI is 0.997, not 1.000, but this minor inaccuracy in the strength finder does not meaningfully affect the review.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Extend the IPI experiments to include at least one realistic covert-embedding technique (white text or zero-font) to validate the peer-review motivating scenario directly.
- Add bootstrapped confidence intervals to all detection metrics reported in Table 2 and Figure 3.
- Include at least one open-weight LLM (e.g., LLaMA-3-70B, Qwen2.5-72B) in the evaluation to broaden the empirical scope.
- Acknowledge and discuss the LLM judge's apparent bias toward AI-generated text in the main text, and consider adding a small human evaluation sample.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>