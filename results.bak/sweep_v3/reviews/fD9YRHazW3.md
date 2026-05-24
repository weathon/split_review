Now I have sufficient calibration. Let me produce the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a method to embed detectable signals into LLM output *solely through prompt engineering*, without any access to model weights, logits, or decoding process. The paper proposes four strategies at different granularities (Unicode, Initials, Lexical, Acrostics) with corresponding detection methods, evaluated in both a direct (DTS) setting and an Indirect Prompt Injection (IPI) setting motivated by detecting AI-generated peer reviews. Experiments with GPT-o3-mini show that all four ICW strategies achieve ROC-AUC ≥ 0.995 in DTS and ≥ 0.997 in IPI, with robustness to paraphrasing exceeding standard post-hoc baselines and text quality close to unwatermarked output.

## Strengths

- **First prompt-based watermarking that requires no model access.** ICW operates purely through instruction engineering, requiring only API-level interaction with the LLM. This is a genuinely different paradigm from all existing in-process watermarking methods (Kirchenbauer, Aaronson, etc.) that require logit or sampling access, and from post-hoc methods that modify already-generated text. The IPI setting (Section 3.2, Table 2) demonstrates AUC ≥ 0.997 for GPT-o3-mini in a scenario where no existing method applies.

- **Systematic exploration of four strategies with clear trade-off characterization.** Table 1 qualitatively summarizes the trade-offs among LLM requirements, detectability, robustness, and text quality. Table 2, Figure 3, and Table 3 provide quantitative validation: e.g., Initials ICW achieves AUC=0.887 under paraphrasing vs. 0.557/0.841 for YCZ+23/PostMark (Figure 3); Lexical ICW achieves Overall score 4.808 vs. unwatermarked 4.992 (Table 3). This enables practitioners to choose a scheme appropriate for their threat model.

- **Robustness to paraphrasing exceeding or matching standard post-hoc baselines.** In the DTS setting with GPT-o3-mini, Initials (0.887), Lexical (0.924), and Acrostics (0.922) ICWs all outperform YCZ+23 (0.557) and PostMark (0.841) under paraphrasing attacks (Figure 3), while being applicable in the IPI setting where those baselines cannot be deployed.

- **Formal false-alarm guarantees for Initials and Lexical ICWs.** Section 4.2.2 and 4.2.3 state theoretical control over the false positive rate via z-statistics, with full derivations in Appendix B, providing rigor beyond purely empirical prompt-based approaches.

## Weaknesses

### Major

- **Evaluation limited to two GPT-family models (GPT-4o-mini, GPT-o3-mini), both from the same provider.** The title, abstract, and framing refer to "Large Language Models" generally, and the conclusion states ICW's effectiveness "will improve as LLMs become more capable." However, the experiments only test two models from the same API provider and family. The central claim — that ICW leverages in-context learning and instruction following — would be significantly strengthened by demonstrating effectiveness on at least one model from a different provider (e.g., Gemini, Claude, or an open-source model like Llama-3.1-70B). The paper's own results show that GPT-4o-mini fails for three of four strategies (Initials AUC=0.572, Acrostics AUC=0.590, Lexical AUC=0.910), confirming sensitivity to model capability, but the current evidence cannot distinguish whether this is a GPT-specific phenomenon or a general one.

### Minor

- **The IPI experiment does not test the covert injection mechanism.** The paper motivates ICW with a peer-review scenario where instructions are hidden via "white text" or zero-font-size text (Section 3.2). The experiment, however, simply concatenates the watermarking instruction as plain text at the end of the paper. While this tests whether ICW works in long-context scenarios, it does not validate whether the instruction survives realistic hidden-injection pipelines (e.g., PDF text extraction from white-on-white text). The paper should either add this validation or explicitly frame the results as an upper bound / best-case analysis and discuss the practical gap.

- **Detection results reported without variance or confidence intervals.** With 500 samples per condition, all results in Table 2, Figure 3, and Table 3 are reported as point estimates with no standard deviations or confidence intervals. Given AUC values near 1.0, this is less concerning for claims of high effectiveness, but it does limit the ability to assess the stability of comparisons between methods (e.g., whether a 0.001 difference in AUC is meaningful), and the lack of variance is a systematic omission.

- **LLM-as-a-Judge evaluation may exhibit bias toward LLM-style prose.** Table 3 shows gemini-2.0-flash assigns unwatermarked GPT-o3-mini text an Overall score of 4.992/5.000, while human text scores 4.235/5.000. This suggests the judge may systematically favor machine-written text, making the high scores of ICW methods (e.g., Lexical 4.808, Acrostics 4.813) less informative as evidence of quality preservation. Perplexity results (Figure 4, Appendix) provide a more objective complement but are relegated to the appendix.

- **Perplexity results are in the appendix rather than the main text.** Figure 4, which provides an objective quality metric not subject to LLM-judge bias, is placed in Appendix D.1. Moving it to the main paper (e.g., alongside or replacing aspects of Table 3) would strengthen the quality evaluation.

### Trivial

- Unicode ICW robustness is discussed qualitatively (Section 5.2.2) but excluded from the quantitative robustness figure (Figure 3) — a brief quantitative inclusion (even if poor) would be more complete.

## Nice-to-Haves

- Ablating vocabulary size for Lexical ICW to study the detectability–quality trade-off.
- Reporting the false positive rate empirically on a set of human-written academic reviews (rather than relying solely on the Canterbury Corpus-based theoretical estimate for Initials ICW).
- A cost/overhead analysis noting the token-length impact of including vocabulary lists in Lexical ICW prompts.
- Evaluating whether the watermark instruction degrades the *quality of the generated review* in the IPI setting (e.g., via human evaluation of review helpfulness).

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Conference organizers cannot modify camera-ready PDFs"** (harsh critic, Strengthening §1) — The paper's footnote 1 explicitly addresses this by proposing organizers (not authors) do the embedding, and notes authors could also do it but organizers are more impartial. The concern is about deployment logistics, not method validity.

2. **"GPTZero is a less useful baseline"** (harsh critic, Section-by-Section) — Reviewer preference; including an additional standard baseline (even with expected poor performance) is standard practice and does not harm the paper.

3. **"Ignore prior prompts attack not discussed"** (harsh critic, Missing Parts) — The paper explicitly mentions investigating this attack in Appendix D.1 (line 291): "We investigate two potential attacks... the other evaluates detection performance when an adversary prepends the instruction 'ignore prior prompts'." The critic missed this.

4. **"Canterbury Corpus distribution may not match peer-review text"** (harsh critic, Section-by-Section) — This is a reasonable theoretical concern but applies to the *initial letter distribution*, which is known to be remarkably stable across English text varieties. The paper flags the appendix for details. This is a minor point that does not warrant inclusion as a separate weakness.

5. **Generic reproducibility nitpicks** (harsh critic, various) — The code is provided, detailed settings are in Appendix C, and the method is described clearly in the main text. Requests for hyperparameter tables are standard but the code repository satisfies reproducibility.

## Novel Insights

The synthesized reviews surface an observation not fully articulated in the paper itself: ICW essentially transforms watermarking from a *generation-process* control problem into a *prompt-following* evaluation problem. This reframing has a sharp consequence: the quality of the watermark depends directly on the LLM's instruction-following competence, meaning ICW is *monotonically improvable* as LLMs advance — unlike logit-based schemes that face fundamental statistical trade-offs. However, this also means ICW effectiveness is a moving target: a method that works on GPT-o3-mini may fail on a weaker model, and conversely, a future model's improved instruction following may make some ICW strategies trivially detectable but simultaneously make the watermark easier to spoof. This duality — where method effectiveness and vulnerability both scale with model capability — is worth deeper analysis than the paper currently provides.

## Suggestions

1. **Broaden model evaluation** to include at least one non-OpenAI model (e.g., Gemini 2.0, Claude 3.5 Sonnet) to substantiate the claim that ICW generalizes across LLMs.
2. **Test the covert injection pipeline** — embed instructions as white/zero-font text in a PDF, extract text with a standard parser, and confirm the instruction survives — or at minimum, explicitly characterize the current IPI results as an ideal-case upper bound.
3. **Add confidence intervals or standard deviations** to all detection, robustness, and quality metrics.
4. **Move perplexity results** (Figure 4) to the main text to provide an objective quality complement to the LLM judge scores.

## Score and Decision

### Calibration Anchors (from retrieval)

| Anchor | Avg Score | Comparison to paper under review |
|--------|-----------|----------------------------------|
| `ujpAYpFDEA` (Can Watermarked LLMs be Identified via Crafted Prompts?) | 7.50 | Stronger model breadth (multiple LLMs tested); similar writing quality. The ICW paper is more novel in method but narrower in evaluation. |
| `E4LAVLXAHW` (Black-Box Detection of LM Watermarks) | 7.00 | Rigorous statistical tests across multiple open-source models and APIs. ICW paper is more novel in watermarking approach but less comprehensive in model coverage. |
| `6p8lpe4MNf` (Semantic Invariant Robust Watermark) | 5.50 | Similar scope (LLM watermarking), mixed reviews. ICW paper is more novel (prompt-based vs. logit-based) and has clearer, more comprehensive experiments. |
| `0koPj0cJV6` (Watermark for Black-Box LMs) | 4.60 | Black-box watermarking paper rejected for practical concerns. ICW paper is more novel (truly no model access needed) and avoids the practical pitfalls of that paper. |
| `eKGEsFdpin` (Sampling-Based Watermarking) | 3.67 | Derivative work rejected for insufficient novelty vs. Kirchenbauer. ICW paper is substantially more novel. |
| `jbfDg4DgAk` (Sparse Watermarking in LLMs) | 3.00 | Weak results and limited evaluation. ICW paper is far stronger in both results and thoroughness. |

The paper's core contribution — watermarking purely through prompt engineering — is genuinely novel and well-demonstrated with strong empirical results. The primary weakness is evaluation breadth: only two GPT-family models are tested, limiting the generality of the claims. This is a concrete gap but not a fatal one, as the paper is transparent about limitations and the central mechanism is not inherently model-specific. Compared to the calibration anchors, the paper sits above the mid-range (4.6–5.5) papers in novelty and rigor, but below the top-tier (7.0–7.5) papers in evaluation completeness. A score of 6.5 reflects a solid, novel contribution with identifiable but addressable gaps.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>