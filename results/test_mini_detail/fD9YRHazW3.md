Now I have a solid calibration. Let me produce the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a method that embeds detectable watermarks into LLM-generated text **solely through prompt engineering**, requiring no access to the model's decoding process, logits, or weights. The authors propose four ICW strategies at different granularities (Unicode, Initials, Lexical, Acrostics), each paired with a statistical detection method, and evaluate them in a Direct Text Stamp (DTS) setting and an Indirect Prompt Injection (IPI) case study motivated by detecting AI-generated peer reviews. Experiments on GPT-4o-mini and GPT-o3-mini show that with a sufficiently capable LLM, ICW achieves near-perfect detection (AUC ≥ 0.995), competitive or better robustness than black-box post-hoc baselines under paraphrasing attacks, and higher text quality than those baselines.

## Strengths

1. **Genuinely novel approach to LLM watermarking.** ICW operates without any access to model internals, logits, or decoding process — a strictly weaker access model than all existing in-process watermarking methods and even post-hoc methods that require the generated text after the fact. This opens a new direction for watermarking research that leverages in-context learning and instruction-following rather than decoding intervention.

2. **Comprehensive exploration of four different ICW strategies.** The paper systematically designs and evaluates Unicode, Initials, Lexical, and Acrostics ICW, providing a clear analysis of trade-offs among LLM capability requirements, detectability, robustness, and text quality (Table 1). This gives practitioners a practical framework for choosing the right granularity.

3. **Strong empirical evidence of feasibility with capable LLMs.** Table 2 shows that with GPT-o3-mini, all four ICW variants achieve ROC-AUC ≥ 0.995 in both DTS and IPI settings, with several methods reaching T@1%F > 0.93. This is the strongest evidence that prompt-based watermarking can work in principle.

4. **Better text quality preservation than the strongest black-box baseline.** Table 3 demonstrates that ICW methods (e.g., Lexical ICW overall = 4.808, Acrostics ICW = 4.813) score much closer to unwatermarked text (4.992) than PostMark (2.997) in the LLM-as-a-Judge evaluation, while maintaining comparable or better detection performance.

5. **Stronger robustness than baselines under paraphrase attacks.** Figure 3 shows Initials ICW (AUC = 0.887) and Lexical ICW (AUC = 0.924) maintain higher detection after LLM paraphrasing than the best baseline PostMark (AUC = 0.841), demonstrating the redundancy advantage of embedding watermarks throughout generation.

6. **Theoretical false-alarm control for Initials and Lexical ICW.** The paper derives z-statistic detectors with false-positive rate guarantees (Appendix B), which strengthens reliability compared to heuristic prompt-based watermark proposals.

## Weaknesses

### Fatal
None.

### Major

1. **IPI case study lacks empirical validation of covert instruction embedding.** The paper motivates ICW with the IPI peer-review scenario (Section 3.2, Figure 2) and proposes embedding watermarking instructions via white text or zero-font-size text, but the IPI experiments (Table 2) concatenate the instruction explicitly with the paper text — they do not test whether the instruction survives actual PDF rendering and parsing when hidden. The paper acknowledges this gap ("a detailed investigation of attack and defense methods is left for future work," line 106) and positions IPI as a case study rather than a fully validated application. However, because the IPI scenario is a primary source of significance in the introduction and abstract, the gap between claimed application and validated setup is substantial enough to weaken the overall contribution. The core ICW contribution stands on the DTS results, but the paper over-weights the IPI framing relative to what is empirically demonstrated.

2. **Detection evidence is concentrated on a single high-capability model class.** The paper tests only GPT-4o-mini and GPT-o3-mini. On GPT-4o-mini, Initials ICW (AUC 0.572), Acrostics ICW (AUC 0.590), and to some degree Lexical ICW (AUC 0.910 DTS / 0.889 IPI) range from near-random to moderate. The paper is transparent about this dependency ("ICW effectiveness highly depends on the capabilities of the underlying LLMs," Table 2 caption, line 225), and the abstract hedges appropriately ("as LLMs become more capable, ICW offers a promising direction"). However, with only two models tested, the generality of the claims is limited. Running on at least one additional capable model (e.g., GPT-4o, Claude Sonnet, Gemini 1.5 Pro) would substantially strengthen the evidence that ICW works across model families, not just within a single provider's product line.

### Minor

3. **No targeted adversarial robustness evaluation.** The robustness tests (random deletion, synonym replacement, LLM paraphrasing) are all untargeted text corruptions. The paper acknowledges that Initials ICW is "vulnerable to spoofing attacks if the green letter set is inferred" (Section 4.2.2) and that Lexical ICW exposes the green word list in the prompt. An adversary aware of the scheme could trivially remove or evade these watermarks (e.g., replacing every word starting with a green letter). A targeted attack experiment — even a simple one — would bound the practical security of the method rather than just its resilience to random noise. The paper lists this as future work (Section 6), which is reasonable but leaves an important gap.

4. **Canterbury Corpus baseline may not match the evaluation distribution.** The detection z-statistic for Initials and Lexical ICW estimates the expected proportion γ of green tokens from the Canterbury Corpus (lines 151-152). The experiments use ELI5 as the human text, which may have a different initial-letter distribution. If the distributions differ systematically, the detection rates could be biased. Estimating γ from the control text in the evaluation set would remove this concern.

5. **Text quality evaluation relies on a single LLM judge.** The paper uses gemini-2.0-flash as the quality evaluator (Section 5.1) with a prompt in Appendix E (not inspectable). LLM-as-a-Judge is standard practice but can have systematic biases. The paper reports perplexity from LLaMA-3.1-70B as a complementary metric (Appendix D.1), which strengthens the evaluation somewhat, but including at least a small-scale human evaluation or a second judge model would increase confidence in the quality claims.

### Trivial
None.

## Nice-to-Haves
- Test the IPI scenario with actual covert embedding (white text, zero-font) in real PDFs across different PDF readers and LLM API pipelines.
- Include a broader model zoo (GPT-4o, Claude Sonnet, Gemini 1.5 Pro) to establish where the capability threshold lies for each ICW strategy.
- Provide a formal justification or fix for the Acrostics detection resampling approach (the current method is conservative but this should be explicitly argued).
- Analyze sensitivity of Acrostics detection to punctuation, lists, and bullet points that create many short "sentences."

## Removed Points
These points were flagged by reviewers but are removed for the reasons stated:
- **"Acrostics detection is circular because resampling from suspect text is biased"** — This critique misunderstands the method. Resampling from the suspect text produces a conservative null distribution (harder to detect watermarks, not easier), so the approach is valid. Removed as factually incorrect.
- **"Model-agnostic claim is misleading because ICW doesn't work on weaker models"** — The paper is transparent about capability dependence (Table 2 caption, lines 225-226, contribution list line 45). "Model-agnostic" refers to not requiring access to model internals, not to equal performance across all models. Removed as a strawman.
- **"No key management discussion"** — Standard scope creep for an initial exploration paper. Removed.
- **Strengths removed:** Generic statements about the problem being "important" or "timely" without specific evidence.

## Novel Insights

A genuinely novel observation that emerges from synthesizing the reviews is that ICW exposes a fundamental shift in how watermarking research should think about access assumptions. Existing watermarking is built on the premise that the watermarker controls (or at least modifies) the decoding process. ICW shows that with sufficiently capable models, the watermark can instead be a **property of the prompt** — meaning watermarking capability scales with model capability rather than requiring the watermarker to have privileged access. This inverts the conventional power dynamic: in the traditional setting, only model owners can watermark; in the ICW setting, any third party who can interact with an LLM API can watermark. The flip side — that ICW is trivially evadable by an adversary who sees the prompt — is also surfaced sharply by the reviews. This suggests the most impactful direction for follow-up work is not better ICW schemes but *defenses against prompt-aware adversaries*, which the current paper does not address.

## Suggestions

1. **Reframe the IPI contribution.** The paper would be stronger if it either (a) ran a realistic covert-embedding experiment (white text in a PDF, submitted to an LLM parser), or (b) explicitly scoped down the IPI claim to "what happens when the instruction reaches the model" and deferred the covert-channel problem to future work in a clearly bounded way.
2. **Add at least one more model family.** Even one additional capable model (e.g., Claude Sonnet, Gemini 1.5 Pro) would significantly strengthen the generalization claim.
3. **Add a simple targeted attack experiment.** For Initials ICW, test detection after replacing all words starting with green letters with synonyms not starting with those letters. This would bound the method's security.
4. **Change the z-statistic baseline estimation.** For Initials ICW, estimate γ from the unwatermarked control text in the same evaluation set rather than from the Canterbury Corpus, to avoid potential distribution mismatch.
5. **Provide a short human evaluation sample or a second LLM judge** for text quality.

## Score and Decision

**Calibration Round 1 (Bracketing):** Three queries on LLM watermarking / prompt engineering topics returned anchors in three bands: low-band (avg 3.0, weak papers), mid-band (avg 3.67–5.75, reject/marginal accept), and high-band (avg 8.0+, oral/posters in different subfields). The paper sat clearly in the mid-to-upper-mid range based on novelty and experimental quality.

**Round 1 bracket:** 5.5–7.5.

**Calibration Round 2 (Narrowing):** Read four anchors in full:
- **Codable Watermarking** (JYu5Flqm9D, avg 5.75, Accept poster): Extends Kirchenbauer to multi-bit; in-process watermarking requiring model access. Less novel than ICW. ICW is clearly stronger → score > 5.75.
- **Learnability of Watermarks** (9k0krNzvlV, avg 5.75, Accept poster): Distillation-based watermark transfer; criticized for limited novelty. ICW is more novel and has clearer contributions → score > 5.75.
- **DNA-GPT** (Xlayxj2fWp, avg 6.67, Accept poster): Training-free detection, different problem (detection only, not watermarking). ICW's contribution is comparable in novelty but has more open weaknesses (limited models, unvalidated IPI) → score slightly below 6.67.
- **Optimizing Adaptive Attacks** (RKQcJ1lXNT, avg 5.5, Reject): Adaptive attack evaluation; good methodology but rejected. ICW is substantially stronger.

**Final score determination:** The ICW paper introduces a genuinely novel and well-executed idea. The main results (Table 2, Figure 3, Table 3) are clean and convincing within their scope. The weaknesses are real but manageable: the IPI framing is somewhat overblown relative to what is empirically tested, the model zoo is narrow, and no targeted adversarial robustness is evaluated. These are limitations of an initial exploration, not fatal flaws. The paper is significantly stronger than the 5.75 anchors and comparable to the 6.67 anchor but with more scope limitations. I place it between these.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>