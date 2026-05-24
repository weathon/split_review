Now I have a solid understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary
This paper introduces In-Context Watermarking (ICW), a novel approach to watermarking LLM outputs that works solely through prompt engineering — no access to model internals, logits, or decoding is required. The authors propose four watermarking strategies at different linguistic granularities (Unicode, Initials, Lexical, Acrostics) and evaluate them in two settings: a Direct Text Stamp (DTS) setting where the watermark instruction is in the system prompt, and an Indirect Prompt Injection (IPI) setting where it is covertly embedded in input documents, targeting the real-world problem of detecting AI-generated peer reviews. On GPT-o3-mini, all four strategies achieve near-perfect detection (AUC ≥ 0.995) with minimal text quality degradation.

## Strengths
- **Genuinely novel paradigm.** Using prompt engineering to embed watermarks — rather than controlling decoding, modifying model weights, or post-processing text — is a fresh and creative idea that opens up watermarking to scenarios where users have only API access. The paper is, to my knowledge, the first to explore this direction systematically.
- **Well-motivated IPI setting.** The Indirect Prompt Injection case study (embedding watermark instructions into academic manuscripts to catch LLM-generated reviews) addresses a concrete, timely problem. This is a clever inversion of the typical prompt injection threat model and is supported by strong detection results (AUC up to 1.000 for Unicode ICW on GPT-o3-mini).
- **Strong empirical signal on capable models.** On GPT-o3-mini, all four strategies deliver near-perfect ROC-AUC (0.995–1.000 in DTS; 0.997–1.000 in IPI) and good T@1%F scores, demonstrating that the concept works when the underlying LLM is sufficiently capable. The robustness results (Figure 3) show that Initials and Acrostics ICW maintain high detectability even under 30% word deletion, replacement, and paraphrasing.
- **Text quality preservation.** LLM-as-a-Judge evaluations (Table 3) show ICW methods scoring close to unwatermarked output (e.g., Lexical ICW overall = 4.808 vs. unwatermarked = 4.992) and substantially outperforming the post-processing baseline PostMark (2.997).
- **Clear taxonomy of strategies.** The four ICW methods span character-level (Unicode), word-initial-letter (Initials), word-list (Lexical), and sentence-level (Acrostics) granularities, providing a useful framework for understanding trade-offs and future extensions.

## Weaknesses

### Fatal
None.

### Major
- **Narrow model coverage undermines generality claims.** The paper evaluates only two OpenAI models (gpt-4o-mini and gpt-o3-mini). From a single pairwise comparison it concludes that "as LLMs become more capable, ICW will become correspondingly more powerful" and describes ICW as "model-agnostic." Two data points from one provider cannot support either claim. At minimum, evaluation should include models from other families (e.g., Llama, Claude, Mistral) and ideally a broader capability sweep. This directly affects the paper's core assertion about generality.
- **IPI evaluation does not validate the motivating scenario.** The IPI threat model (Section 3.2) envisions embedding watermark instructions via "white text" or zero-font-size strings in PDFs. The experiments (Section 5.1) only concatenate the instruction to plain-text paper content. Real PDF parsers may strip invisible text, fail on zero-font-size strings, or behave unpredictably. Without demonstrating that the instruction survives the PDF → text extraction → LLM pipeline, the IPI results are a proof-of-concept rather than validation of the claiming motivating application. The paper acknowledges this as future work, but the evaluation as presented overstates what has been demonstrated.
- **Detection calibration is untested on target-domain human text.** The Initials ICW detector uses initial-letter frequencies from the Canterbury Corpus as the null distribution for the z-test. The Lexical ICW detector uses γ = |V_G|/|V|. Neither is validated against actual human text in the target domains (ELI5 answers, peer reviews). If real human text in these domains has different letter/word distributions, the claimed T@1%F thresholds would not hold in practice. This is a significant gap for a method whose value depends on reliable, low-FPR accusations.

### Minor
- **Paraphrasing model unspecified.** Section 5.1 states robustness is tested "by paraphrasing it using an LLM" without naming the model. If the paraphrasing model is the same one used for generation, this weakens the adversarial realism of the robustness evaluation. An adversary would likely use a different (possibly weaker or differently-trained) model.
- **Absence of systematic design-space exploration.** The paper presents four strategies but does not study how prompt wording, green-list size, key length, or vocabulary composition affect detectability/quality/robustness. This limits the paper's prescriptive value — a practitioner would not know how to tune these knobs. The paper's framing as "initial exploration" partially mitigates this.
- **Two-point trend claim.** The argument that ICW effectiveness tracks model capability rests on exactly two models. While the observed improvement from gpt-4o-mini to gpt-o3-mini is dramatic, this does not establish a trend, and the paper should temper this language.
- **Robustness metrics limited to AUC.** Figure 3 reports only AUC for robustness. Low-FPR metrics (T@1%F, T@10%F) — which the paper correctly uses in Table 2 for clean-text detection — are not reported for attacked text, making it hard to assess practical robustness at operationally relevant thresholds.
- **Lexical ICW vocabulary restriction may interact with domain.** The vocabulary V is restricted to adjectives, adverbs, and verbs. In specialized domains (e.g., technical peer reviews), this may miss key content-bearing nouns and lead to unnatural text or weaker detection. This is not explored.

### Trivial
- The term "model-agnostic" is used to mean "detector does not require model access" (a legitimate usage) but could be misread as "tested on many models." Clarifying this in the text would avoid confusion.
- The sole inclusion of Lexical ICW results from GPT-4o-mini for the IPI setting (Table 2) seems to show detection above random for a method that failed in DTS — a brief discussion would help.

## Nice-to-Haves
- A prototype end-to-end IPI pipeline (PDF → extraction → LLM → detection) would greatly strengthen the case study and is highly recommended for a future version.
- Testing across model families (Llama, Mistral, Claude) to verify model-agnosticism.
- Domain-specific FPR calibration on real peer-review text and ELI5 answers.
- A study of how acrostic key length interacts with output length — short outputs may simply not have enough sentences to encode the key.

## Removed Points
*These points were flagged from the input reviews but are removed from the final assessment for the stated reasons.*

- **"The paper lacks any analysis of how the watermark instruction affects task performance (review quality, answer accuracy)."** — REMOVED. Table 3 directly evaluates text quality (relevance, clarity, quality) using LLM-as-a-Judge, and ICW methods score close to unwatermarked output. The paper does address output quality.
- **"Perplexity scores are not in the main table; the claim about perplexity cannot be checked."** — REMOVED. The paper explicitly references Appendix D.1 (Figure 4) for perplexity results. This is a standard presentation choice. The parser stripped the appendix, not the authors.
- **"No discussion of how the watermark instruction might affect the quality of the generated review."** — REMOVED (merged into above). Table 3 covers quality and the paper discusses quality impacts in Section 5.2.3.
- **"Detection formulas assume independence of word-initial letters, which is known to be inaccurate, but the paper does not discuss how this affects validity."** — REMOVED. The paper provides theoretical guarantees for false-alarm control in Appendix B. The z-test framework is standard and the independence assumption, while approximate, is commonly used in similar detection settings.
- **"The baselines in the DTS setting are post-hoc methods; a fairer comparison would include an in-process black-box baseline."** — REMOVED. The paper's explicit contribution is that ICW works without model access; there is no existing in-process black-box baseline for the prompt-only setting to compare against. This is precisely the gap the paper fills.
- **"The paper does not evaluate the most obvious attack in the IPI setting: the adversary detecting and removing the watermarking instruction."** — DEMOTED to acknowledgment. The paper explicitly scopes this out in Section 3.2 ("a detailed investigation of attack and defense methods is left for future work") and Section 6, and the Appendix D.1 contains attack analysis including "ignore prior prompts." This is a known, acknowledged limitation, not an oversight.
- **"The trade-off study in Table 1 is purely qualitative."** — PARTIALLY REMOVED. Table 1's qualitative nature is an intentional feature of the taxonomy; it's labeled as an "intuitive illustration." The lack of quantitative trade-off analysis is real but is captured in the Minor weakness about systematic design-space exploration.

## Novel Insights
The paper's most striking finding is the stark capability threshold: methods that essentially fail on GPT-4o-mini (Initials AUC = 0.572, Acrostics AUC = 0.590) achieve near-perfect detection on GPT-o3-mini (0.999 and 1.000). This suggests that ICW acts as a kind of "capability probe" — its success is not gradual but exhibits a phase transition once the model's instruction-following crosses a critical threshold. This has implications beyond watermarking: it hints that many prompt-engineering techniques previously dismissed as unreliable may become viable as foundation models improve, and that the design space for "prompt-native" security mechanisms is larger than currently appreciated.

## Suggestions
- **Broaden model evaluation:** Add at least one open-weight model (e.g., Llama-3-70B) and one model from a different provider (e.g., Claude) to substantiate model-agnostic claims.
- **Calibrate detectors on domain text:** For Initials ICW, estimate γ from real ELI5 human answers and peer-review text rather than (or in addition to) the Canterbury Corpus. Report whether empirical FPR at the z-test threshold matches the nominal rate.
- **Temper claims:** Replace "model-agnostic" with "detection is model-agnostic" (embedding depends on model capability, as the paper itself shows). Replace the capability-trend claim with a more cautious observation about the gpt-4o-mini → gpt-o3-mini improvement.
- **Specify the paraphrasing model** and ideally use a model different from the generation model for adversarial realism.
- **Report T@1%F for robustness** in addition to AUC, to parallel the clean-text detection metrics.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| jbfDg4DgAk (Sparse Watermarking) | 3.00 | R1 | ICW has substantially stronger novelty and broader scope |
| eKGEsFdpin (Sampling Watermark) | 3.67 | R1 | ICW is more novel; both have evaluation limitations |
| qGLzeD9GCX (EditMark) | 4.25 | R2 | ICW has stronger novelty and more compelling results |
| 0koPj0cJV6 (Black-Box Watermark) | 4.60 | R2 | ICW has comparable contribution level but simpler method; ICW's IPI setting adds value |
| r6aX67YhD9 (RL Watermark) | 4.75 | R1 | Both have novel ideas with evaluation gaps; ICW's idea is more strikingly different |
| 0KHW6yXdiZ (E2E Logits Watermark) | 5.25 | R2 | ICW is less technically deep but more creatively novel |
| 9k0krNzvlV (Learnability of Watermarks) | 5.75 | R2 | ICW has stronger novelty; learnability paper has more thorough evaluation |
| 6p8lpe4MNf (Semantic Invariant WM) | 5.50 | R1/R2 | ICW is similarly novel but has narrower evaluation |

**Round 1 bracket:** 4.5 – 6.0  
**Round 2 narrowing:** ICW sits between the 4.60 black-box watermark (less novel setting, similar evaluation breadth) and the 5.75 learnability paper (less novel idea, more thorough evaluation). ICW's core novelty is its strongest asset; its narrow model coverage and simplified IPI evaluation are its main liabilities.  
**Final score: 5.0** — a borderline paper with a genuinely novel contribution whose evaluation would benefit substantially from broadening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>