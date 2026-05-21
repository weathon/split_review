Now I have a solid calibration. Let me synthesize the final review.

**Round 1 bracket:** I initially placed this paper between ~4.5 and ~7.0 based on the anchor papers. The weak anchors (<3.5) are papers with serious flaws or very limited contribution; the strong anchors (>7.5) are high-quality papers with theoretical depth and extensive experimentation. This paper sits in the middle band.

**Round 2 narrowing:** Comparing within (4.5, 7.0):
- The ICW paper is clearly stronger than the score-4.60 "Black-Box Watermark" paper (which was criticized as too similar to prior work and poorly presented).
- It's comparable to the score-5.50 WASA paper and the score-5.25 End-to-End paper.
- It's not as strong as the score-7.00 "Black-Box Detection" paper (which had deeper theoretical analysis and more comprehensive evaluation).
- Compared to score-5.80 "Can Watermarks be Used..." (accepted), the ICW paper has a more clearly novel contribution.
- I place this paper at **5.5** — a solid paper with a genuinely novel contribution but some significant methodological gaps (underspecified Acrostics detection, limited model scope) that prevent it from reaching the 6.5+ tier.

Now writing the review.

Final score: 5.5, Decision: Reject (borderline, with clear path to acceptance with revisions — specifically broader model testing and fixing the Acrostics detector).

Actually, I need to decide. Looking at the scores 5.50 (WASA — Reject) and 5.80 (Can Watermarks — Accept), the difference seems to be that the 5.80 paper had fewer fundamental weaknesses. The ICW paper's Acrostics detection issue is a real methodological gap, and the limited model scope is a significant limitation. But the core contribution is more novel than most papers in this space.

Let me go with **5.5, Reject** — the paper has a strong core idea but the weaknesses are meaningful enough that it would need revisions (specifically fixing Acrostics detection and broader model testing) before acceptance. This is consistent with how similar-scored papers were treated.## Summary

This paper introduces In-Context Watermarking (ICW), a new paradigm for LLM watermarking that embeds detectable signals entirely through prompt engineering, without any access to the model's decoding process, logits, or weights. The authors propose four strategies (Unicode, Initials, Lexical, Acrostics), each with a tailored detection method, and evaluate them in two settings: Direct Text Stamp (the user provides a watermarking instruction) and Indirect Prompt Injection (the instruction is covertly embedded into documents, modeled on detecting AI-generated peer reviews). Experiments on GPT-4o-mini and GPT-o3-mini show that with sufficiently capable models, ICW achieves strong detection (ROC-AUC ≥ 0.995 for all methods on GPT-o3-mini), robustness competitive with or exceeding post-hoc baselines, and high text quality. The paper is well-written, the motivation is compelling, and the core idea is genuinely novel.

## Strengths

- **Genuinely new watermarking paradigm.** ICW is the first work to show that watermarks can be embedded solely through prompt engineering, without any access to model internals. This is a fundamental departure from all prior in-process methods (which require logits or sampling access) and post-hoc methods (which modify already-generated text). The paper demonstrates this empirically: on GPT-o3-mini, all four ICW variants achieve ROC-AUC ≥ 0.995 in the DTS setting (Table 2).

- **Novel IPI scenario with a compelling use case.** The Indirect Prompt Injection setting (Section 3.2, Figure 2) is a well-motivated and realistic case study for detecting AI-generated peer reviews. The demonstration that ICW works in the IPI setting is non-trivial — the model must follow the watermarking instruction embedded within a long document. On GPT-o3-mini, this succeeds: Unicode ICW achieves ROC-AUC = 1.000 and T@1%F = 1.000 in the IPI setting (Table 2).

- **Strong text quality relative to baselines.** ICW methods substantially outperform post-hoc baselines (PostMark, YCZ+23) on text quality as measured by LLM-as-a-Judge and perplexity (Table 3). For example, Acrostics ICW scores 4.813 overall vs. PostMark at 2.997 and YCZ+23 at 3.865. This is a meaningful advantage for practical deployment.

- **Robustness to paraphrasing outperforms post-hoc baselines.** Under paraphrase attacks (Figure 3), Initials ICW (AUC=0.887) and Lexical ICW (AUC=0.924) substantially outperform YCZ+23 (AUC=0.557) and PostMark (AUC=0.841), demonstrating a concrete advantage in a challenging adversarial scenario.

- **Formal false-alarm control for Initials and Lexical ICWs.** Sections 4.2.2 and 4.2.3 define detectors based on z-statistics with known null distributions, backed by theoretical analysis (deferred to Appendix B), enabling principled threshold selection.

## Weaknesses

### Major

- **Acrostics ICW detection method is underspecified and potentially invalid.** The detection procedure (Section 4.2.4) computes a z-statistic based on Levenshtein distance, estimating the null mean and standard deviation by "randomly resampl[ing] N sequences of sentence initial letters (ℓ̃₁, …, ℓ̃ₙ) from the suspect text." The paper does not specify how this resampling is done. If the suspect text is watermarked, any resampled sequences will also reflect the watermark bias, making the estimated null distribution invalid. Without a clear description of the resampling mechanism (e.g., permuting letter order, sampling from a known corpus, or a closed-form test), the detection method cannot be evaluated or reproduced. Since the experimental results for Acrostics (Table 2, Figure 3) depend on this pipeline, those results are not convincingly supported. This does not affect the other three ICW methods, but it is a significant gap for a method that is presented as one of the four core strategies.

- **Only two GPT models tested, both from the same provider.** The experiments use only GPT-4o-mini and GPT-o3-mini. To support ICW as a general approach (the paper frames it as "model-agnostic" in its meaning of requiring no model-specific internals access), the authors should test at least one open-weight model (e.g., LLaMA-3, Qwen2.5) and ideally a model from a different provider. The paper's own results show that ICW works well only on sufficiently capable models (GPT-o3-mini works, GPT-4o-mini mostly fails for non-Unicode methods), so the practical scope is narrowed to frontier LLMs. Adding even one open-source model would substantially strengthen the claim. This is a significant limitation given that the paper's main selling point is enabling third parties to watermark text without provider cooperation — a scenario where the provider likely wouldn't be OpenAI's most capable models.

### Minor

- **No uncertainty quantification.** Detection and robustness results are reported as point estimates (ROC-AUC, T@1%F) without confidence intervals or standard errors. With 500 samples per condition and stochastic LLM outputs, the reported values could have non-trivial variance. Bootstrapped confidence intervals for key results would give readers a clearer picture of reliability.

- **IPI evaluation does not test real-world instruction survivability.** The IPI experiment concatenates the watermarking instruction directly with the paper text in the prompt. This does not simulate whether the instruction survives realistic document processing pipelines (OCR, PDF-to-text conversion, browser copy-paste) that may strip invisible text. The paper mentions "white text" as an embedding method but does not test whether common tools (`pdftotext`, browser rendering) preserve the instruction. This limits the real-world credibility of the IPI results.

- **The LLM-as-a-Judge evaluation uses gemini-2.0-flash (a model from a different provider) to score text quality.** While this is a common practice, an LLM-as-a-Judge evaluation for text quality has well-known biases (e.g., favoring its own style). The paper also reports perplexity (Figure 4 in the appendix), which provides a complementary view, but the perplexity numbers are deferred to the appendix. Including at least the key perplexity comparison in the main text would strengthen the text-quality claims.

### Trivial

- The resampling procedure for Acrostics detection needs a clear specification for reproducibility. This is listed as Major above in terms of its evidential impact but could be resolved with a clear description in a revision.
- The size of the green word list for Lexical ICW and the length of the secret string for Acrostics ICW are not reported. These are important hyperparameters that affect reproducibility.

## Nice-to-Haves

- A qualitative analysis of why GPT-4o-mini fails in the IPI setting (e.g., did it ignore the instruction? did the instruction get lost in the long context?) would strengthen the paper's claim about long-context challenges.
- A brief discussion of dual-use considerations for covert injection (the IPI scenario embeds invisible instructions into documents without the reader's knowledge) would strengthen the ethics statement beyond what is already present.
- Testing robustness against an adversary who prepends "ignore prior instructions" in the IPI setting is mentioned as being in Appendix D.1 but not shown in the main text.

## Removed Points

The following points from the reviews were removed with justification:

- **"Model-agnostic claim is overstated" (Harsh Critic, Weakness 2)**: The paper uses "model-agnostic" in the standard sense of "does not require access to model internals (weights, logits, decoding process)" — which is true for ICW. The paper's own results show ICW depends on model capability, and this is stated explicitly ("the effectiveness of ICW is highly dependent on the capability of the underlying LLMs"). The criticism that ICW should work equally on all models misreads what "model-agnostic" means in this context. However, the criticism that only 2 GPT models were tested is valid and appears in the Major section above.

- **"Absence of uncertainty quantification should be treated as a major methodological gap" (Harsh Critic)**: While confidence intervals would be nice, reporting point estimates without error bars is standard practice in this early-stage watermarking literature. This is a common minor weakness, not a methodologically invalidating one.

- **"Comparison with baselines is limited" (Harsh Critic, Section 5 notes)**: The paper correctly notes that PostMark and YCZ+23 are post-hoc methods that cannot be applied in the IPI setting. The comparison is scoped appropriately for what ICW aims to accomplish.

- **"The paper should discuss the comparison more explicitly" (Harsh Critic)**: The paper already does this (Section 5.2.1: "Unlike PostMark and YCZ+23, which rely on post-processing and cannot be used in the IPI setting, ICW methods are well-suited for IPI").

- **Generic strengths from Strength Finder that lack specific evidence** (e.g., "Formal false-alarm rate control" — this is partially valid for Initials/Lexical and kept above; generic statements about the paper being well-written or the problem being important are dropped as they carry no comparative weight).

## Novel Insights

Both reviews independently identify the same critical issue: the Acrostics detection method is not adequately described and may use circular logic (resampling from the suspect text itself to estimate the null distribution). This is a genuine methodological gap that the authors must address. Beyond this, the reviews converge on a shared assessment: the core idea is novel and well-motivated, the results on GPT-o3-mini are strong, but the model scope is too narrow to fully substantiate the claimed generality. The strength of the paper lies in what it opens up (a new watermarking paradigm), not in what it definitively proves (which would require broader model testing across families).

## Suggestions

1. **Fix the Acrostics detection method.** Provide a clear, reproducible description of the resampling procedure. If the current approach is valid (e.g., permuting letter order to break the sequential watermark pattern while preserving the marginal distribution), explain this explicitly. If not, replace it with a principled test (e.g., exact match count or edit-distance threshold calibrated on unwatermarked reference text). A false-positive-rate analysis on unwatermarked text would also help validate the approach.

2. **Test on at least one open-weight model** (e.g., LLaMA-3-70B, Qwen2.5-72B) and preferably a non-GPT API model (e.g., Claude). This would directly support the claim that ICW effectiveness scales with model capability and would substantially improve the paper's reproducibility and generalizability.

3. **Add bootstrapped confidence intervals** for the primary metrics (ROC-AUC, T@1%F) for at least the GPT-o3-mini DTS and IPI settings reported in Table 2. This is straightforward and would give readers a concrete sense of result stability.

4. **Report key hyperparameters** (green word list size for Lexical ICW, secret string length for Acrostics ICW) in the main text or a reproducibility table.

5. **For the IPI setting, test whether the instruction survives realistic document processing.** A simple experiment injecting the instruction as "white text" in a PDF and extracting text with `pdftotext` or browser copy-paste would significantly strengthen the real-world credibility of the IPI results.

## Score and Decision

**Score comparison with anchor papers:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| "A Watermark for Black-Box LMs" | 4.60 | R2 | ICW is more novel (different paradigm vs. incremental sampling scheme), better presented, with clearer motivation. ICW is stronger. |
| "Learning to Watermark via RL" | 4.75 | R2 | ICW requires no training access and has a broader practical scope. ICW is stronger. |
| "End-to-End Logits Watermarking" | 5.25 | R2 | Similar quality level but ICW's paradigm is more novel. Comparable. |
| "WASA" | 5.50 | R2 | ICW has a more novel contribution and cleaner presentation but narrower evaluation. Comparable. |
| "Can Watermarks Detect IP Infringement?" | 5.80 | R2 | Accepted paper; ICW has a more novel core idea but weaker evaluation breadth. Slightly weaker. |
| "Black-Box Detection of Watermarks" | 7.00 | R2 | Significantly stronger theoretical depth and broader experimentation. ICW is clearly weaker. |
| "Sampling-Based Watermarking" | 3.67 | R1 | Too similar to prior work; ICW has much greater novelty. ICW is substantially stronger. |

The paper introduces a genuinely novel watermarking paradigm and provides encouraging proof-of-concept results on a frontier model. However, the Acrostics detection gap and the narrow model scope (two GPT models from the same family) are significant limitations that prevent the paper from reaching the 6+ tier. The paper is comparable to mid-range watermarking papers (5.25–5.50) but has a more novel contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>