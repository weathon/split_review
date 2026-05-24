Now I have a thorough understanding of the paper and all reviewer inputs. Let me write the consolidated final review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces In-Context Watermarking (ICW), a method that embeds detectable signals into LLM outputs purely through prompt engineering — requiring no access to model logits, decoding, or internal state. It proposes four ICW strategies (Unicode, Initials, Lexical, Acrostics) evaluated in a direct setting (DTS) and an indirect prompt injection setting (IPI) where watermark instructions are covertly embedded in documents to detect AI-generated reviews.

## Strengths

- **Novel watermarking paradigm via prompt engineering alone**: ICW is a genuine departure from existing methods, which all require access to the LLM's decoding process. By relying on instruction-following and in-context learning, ICW enables third parties (conference organizers, etc.) to watermark text without any privileged access to the model. This is a meaningful conceptual contribution. (Section 1, Section 3.1)

- **Impressive detection accuracy on capable LLMs**: With GPT-o3-mini, all four ICW strategies achieve AUC ≥ 0.995 in both DTS and IPI settings, and TPR at 1% FPR exceeds 0.9 for three of four methods (Table 2). This demonstrates clear proof-of-concept.

- **Strong robustness to paraphrasing**: Under paraphrasing attacks, Initials, Lexical, and Acrostics ICWs maintain AUC 0.887–0.924 on GPT-o3-mini, substantially outperforming the YCZ+23 baseline (0.557) and competitive with PostMark (0.841). (Figure 3)

- **Systematic design of four complementary strategies**: The paper presents Unicode, Initials, Lexical, and Acrostics ICWs with tailored detection methods and clearly articulates trade-offs across LLM requirements, detectability, robustness, and text quality (Table 1). Both Initials and Lexical ICWs come with theoretical false-positive rate guarantees (Appendix B).

- **Preserved text quality**: ICW watermarked texts from GPT-o3-mini receive LLM-as-a-Judge overall scores of 4.28–4.81 (on a 1–5 scale), close to unwatermarked output (4.99) and well above PostMark (2.997) and YCZ+23 (3.865). (Table 3)

## Weaknesses

### Fatal
None.

### Major

1. **IPI setting evaluated without comparison against post-hoc AI-text detectors.** The IPI scenario is the paper's flagship application, yet no comparison is made against readily available detection alternatives such as GPTZero, DetectGPT, or other zero-shot AI-text detectors on the same reviews. The paper mentions these tools in the introduction as suffering from "low accuracy and high false positive rates" but provides no evidence for this claim in the IPI context and never benchmarks them against ICW. A conference organizer weighing options would need to know whether ICW actually improves detection over simpler approaches. The paper's justification that watermarking baselines (PostMark, YCZ+23) are inapplicable in IPI is valid for those particular methods, but it does not excuse the absence of detector baselines. This is the most significant gap: it weakens the paper's central application claim.

2. **Limited model coverage (only two OpenAI models, one provider).** The evaluation is restricted to GPT-4o-mini and GPT-o3-mini — both from OpenAI and sharing a common lineage. Results show that ICW is nearly ineffective on GPT-4o-mini for three of four strategies, indicating sharp capability dependence. Without testing on other proprietary models (Claude, Gemini) or open-source models (LLaMA-3, Mistral, Qwen), the paper cannot characterize the capability threshold needed for ICW to be viable. The claim of being "model-agnostic" (abstract) is contradicted by the paper's own results and the paper's explicit finding that ICW "is highly dependent on the capability of the underlying LLMs." This needs to be recalibrated.

3. **No uncertainty or variance estimates for main results.** Table 2 and Figure 3 report point estimates without confidence intervals, standard deviations, or any measure of statistical reliability. Since each condition uses 500 watermarked and 500 human texts, bootstrap intervals are feasible and would allow readers to assess whether differences between methods or models are meaningful. Without this, it is impossible to tell, for instance, whether Lexical ICW's AUC of 0.995 vs. Acrostics' 1.000 on GPT-o3-mini reflects a genuine difference or noise.

### Minor

1. **"Model-agnostic" claim is overstated.** The abstract calls ICW "a model-agnostic, practical watermarking approach." The paper's own results show that ICW only works on capable instruction-following models (it largely fails on GPT-4o-mini for three of four strategies). The paper acknowledges this in the body (Section 5.2.1, contributions), but the abstract's phrasing is misleading. The real contribution — that ICW works on sufficiently capable models and will improve as models improve — is compelling enough without this overclaim.

2. **Robustness evaluation does not target IPI-specific threats.** The robustness experiments (random deletion, word replacement, paraphrasing) are reasonable for general watermark evaluation but do not address the specific threat model of the IPI setting. A dishonest reviewer would likely take targeted countermeasures: stripping invisible text from the PDF before input, using a weaker model that does not follow instructions, or prompting the LLM without the full paper text. The paper mentions an "ignore prior prompts" attack in the appendix, but other obvious countermeasures are not discussed. For the IPI setting to be convincing, these practical attack surfaces need analysis.

3. **Empirical FPR at the claimed thresholds is not verified.** The paper reports TPR at 1% FPR thresholds but does not verify that the test achieves the nominal false positive rate on held-out human text. For hypothesis-testing-based detection schemes (Initials, Lexical, Acrostics), reporting empirical FPR on a held-out set of human-written text is standard practice.

### Trivial
None.

## Nice-to-Haves

- **Test on open-source models to map the capability threshold.** The paper hypothesizes that ICW improves with model capability — testing on a range of open-source models (LLaMA-3-70B, Mistral-Large, Qwen2.5) could make this argument quantitative rather than speculative.

- **Include a concrete attack study for the IPI setting.** Simulating a reviewer who strips hidden text, uses a non-compliant model, or prepends "ignore instructions" would give readers a realistic sense of operational robustness.

- **Ablation on instruction format.** The paper uses hand-crafted instructions. A brief study on how few-shot examples, chain-of-thought, or different instruction phrasings affect compliance and detection rates would be informative.

## Removed Points

- *"Acrostics is misspelled in Table 1"*: The paper consistently uses "Acrostics ICW" — this is an intentional method name, not a typo.

- *"Model-agnostic claim appears in Section 1"*: "Model-agnostic" appears only once in the abstract, not in Section 1. The paper is clear in the body that ICW depends on model capability. This is a real but very minor overclaim in the abstract, already captured in Minor Weakness 1.

- *"The paper should test Claude, Gemini, LLaMA, etc."*: This is valid and retained as Major Weakness 2; the removed phrasing is about the specific model names which I've incorporated.

- *"Missing appendix content"*: The appendix is stripped by the PDF parser, not missing from the paper. All claims about appendix content should be disregarded per instructions.

- *Various pure formatting/style nitpicks and grammar complaints*: Removed per instructions.

## Novel Insights

The most interesting observation that goes beyond the paper's own claims is the tension between ICW's model-agnostic framing and its demonstrated model dependence. The paper inadvertently provides evidence for a broader thesis: as LLMs become more instruction-following capable, prompt-based control signals become viable where they were not before. The paraphrasing robustness results (particularly Initials ICW maintaining AUC > 0.99 under deletion and replacement, and > 0.88 under paraphrasing) suggest that embedding watermarks into high-level lexical or structural features rather than token-level biases may offer fundamentally better robustness — a finding with implications beyond the ICW framework.

## Suggestions

1. Add a comparison against post-hoc AI-text detectors (GPTZero, DetectGPT, or a fine-tuned classifier) on the IPI task to show that ICW provides measurable improvement over the status quo.
2. Expand evaluation to at least 2–3 additional models from different providers/families to characterize the capability threshold.
3. Report bootstrap confidence intervals for all AUC and TPR@FPR estimates.
4. Recalibrate the "model-agnostic" language in the abstract to reflect the paper's actual findings.
5. Add an empirical FPR verification on held-out human text for the hypothesis-testing-based ICW schemes.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Queries on weak anchors (score < 3.5): None retrieved with topical similarity; irrelevant.
- Middle anchors (3.5–7.5): "A Watermark for Black-Box Language Models" (4.60, Reject), "On the Reliability of Watermarks" (6.00, Accept), "SIRA" (4.75, Reject), "Can Watermarks be Used to Detect LLM IP Infringement" (5.80, Accept), "Optimizing Adaptive Attacks" (5.50, Reject).
- Strong anchors (> 7.5): Mostly inapplicable topics (privacy, model fingerprinting, benchmark cheating).

**Initial bracket:** 5.0 – 6.5.

**Round 2 — Narrowing:**
- "Prompt engineering watermark LLM black-box" queries (4.5–6.5): "A Watermark for Black-Box Language Models" (4.60, Reject) — weaker method (rejection-sampling based, less practical) and presentation issues; our paper is stronger. "Double-I Watermark" (5.25, Reject) — different problem (model copyright); comparable quality. "Semantic Invariant Robust Watermark" (5.50, Accept) — stronger evaluation and theory; our paper is comparable in novelty.
- "Indirect prompt injection LLM watermark" queries (5.5–7.5): "Can Watermarks be Used to Detect LLM IP Infringement" (5.80, Accept) — similar evaluation breadth issues, accepted; comparable quality. "Black-Box Detection of Language Model Watermarks" (7.00, Accept) — stronger evaluation, broader scope; our paper is weaker.

**Final score determination:** The paper sits below "On the Reliability of Watermarks" (6.00) due to narrower evaluation and missing IPI baselines, but clearly above "A Watermark for Black-Box Language Models" (4.60) and "SIRA" (4.75). It is comparable to "LIDet" (5.80) in terms of novelty and evaluation limitations, and comparable to "Semantic Invariant Robust Watermark" (5.50). Given the genuine novelty but incomplete evaluation, the score is 5.5.

### Anchors Used
| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| jbfDg4DgAk (Sparse Watermark) | 3.00 | 1 | Weaker; our paper has a clearer contribution |
| xRi8sKo4XI (Unsupervised Prompt Learning) | 3.00 | 1 | Different topic, irrelevant |
| t15cWqydys (Inferring from Logits) | 3.00 | 1 | Different topic, irrelevant |
| 3MDmM0rMPQ (Inverse Prompt Engineering) | 3.00 | 1 | Different topic, irrelevant |
| DEJIDCmWOz (Reliability of Watermarks) | 6.00 | 1,2 | Stronger; well-executed analysis with thorough evaluation |
| NvSwR4IvLO (Can AI Text be Reliably Detected?) | 4.67 | 1 | Weaker; evaluation scope concerns, disputed contribution |
| 8Me0Y01mkY (SIRA) | 4.75 | 1 | Weaker; limited novelty, execution concerns |
| RKQcJ1lXNT (Optimizing Adaptive Attacks) | 5.50 | 1 | Comparable; both have evaluation gaps |
| 0koPj0cJV6 (Watermark for Black-Box LMs) | 4.60 | 2 | Weaker; less practical approach, presentation issues |
| 0KHW6yXdiZ (End-to-End Logits Watermark) | 5.25 | 2 | Comparable; different approach (logit-based) |
| ecbRyZZmKG (Double-I Watermark) | 5.25 | 2 | Comparable; model copyright focus |
| 6p8lpe4MNf (Semantic Invariant Robust WM) | 5.50 | 2 | Slightly stronger; better evaluation |
| KRMSH1GxUK (Watermarks for LLM IP) | 5.80 | 2 | Comparable; similar evaluation breadth concerns |
| E4LAVLXAHW (Black-Box Detection of WMs) | 7.00 | 2 | Stronger; broader scope, rigorous |
| DEJIDCmWOz (Reliability of Watermarks) | 6.00 | 2 | Stronger (detailed above) |
| 9k0krNzvlV (Learnability of Watermarks) | 5.75 | 2 | Comparable; similar scope |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>