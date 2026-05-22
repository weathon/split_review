Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a novel paradigm for LLM watermarking that operates purely through prompt engineering—requiring no access to model weights, logits, or decoding. The authors propose four strategies (Unicode, Initials, Lexical, Acrostics) at different linguistic granularities, each with a tailored detection method. They evaluate ICW in two settings: Direct Text Stamp (DTS), where the user voluntarily applies the watermark, and Indirect Prompt Injection (IPI), where the watermark is covertly embedded into documents (e.g., conference papers) to detect AI misuse. With a capable model (GPT-o3-mini), all four methods achieve near-perfect detection (AUC ≥ 0.995) while preserving text quality, demonstrating a fundamentally new watermarking approach that could become more powerful as LLMs advance.

## Strengths

- **A genuinely new paradigm for LLM watermarking.** ICW works through prompt engineering alone, without modifying decoding or requiring model-internal access. This fills a real gap: third parties (conference organizers, content distributors) who cannot rely on provider-side watermarking now have a mechanism that works through the standard API. Table 2 shows that with GPT-o3-mini, all four ICW methods achieve ROC-AUC ≥ 0.995 in both DTS and IPI settings.

- **Systematic evaluation across two settings, four strategies, and multiple attacks.** The paper evaluates detection (Table 2), robustness (Figure 3: word deletion, replacement, LLM paraphrasing), and text quality (Table 3: LLM-as-a-Judge). ICW methods match or exceed post-hoc baselines (PostMark, YCZ+23) on detection while maintaining substantially better text quality (e.g., Lexical ICW Overall score 4.808 vs. PostMark's 2.997 in Table 3).

- **Effectiveness scales with model capability, supporting a forward-looking claim.** Table 2 directly contrasts GPT-4o-mini (fails for 3/4 strategies) with GPT-o3-mini (all 4 succeed), grounding the paper's conclusion that ICW will become increasingly powerful as LLM instruction-following improves—a rare and honest empirical limitation that doubles as a research roadmap.

- **Competitive robustness against paraphrasing.** Under LLM paraphrasing attacks (Figure 3), Initials, Lexical, and Acrostics ICW maintain AUC ≥ 0.887, outperforming YCZ+23 (0.557) and competitive with PostMark (0.841). This is notable given that ICW is not embedded at the token level but via high-level linguistic constraints.

## Weaknesses

### Major

- **The statistical guarantee for Lexical ICW's false-positive control is not properly justified in the main text.** The paper sets γ = |V_G|/|V| for Lexical ICW (Section 4.2.3), which would only give correct FPR calibration under the null if every word were equally likely. Natural language has heavily skewed word frequencies; the expected proportion of green words under the null is Σ_{w∈V_G} p(w), not |V_G|/|V|. The paper claims a "theoretical guarantee on controlling the false alarm rate" (Section 4.2.3) and defers details to Appendix B (stripped from this review). If the appendix treatment does not adjust for non-uniform word frequencies, the reported T@1%F and T@10%F numbers are calibrated to a miscalibrated null and cannot be trusted. This is a concrete technical gap that needs clarification or correction. The Initials ICW approach (estimating γ from the Canterbury Corpus) does not share this problem.

- **The IPI setting evaluation does not test the most obvious countermeasure.** The paper's flagship application (detecting LLM-generated peer reviews) relies on the reviewer failing to notice or remove the hidden watermarking instruction. While Section 6 mentions evaluating an "ignore prior prompts" attack in the appendix (stripped), the paper does not evaluate the simplest and most likely defense: the reviewer who strips invisible/white text from the PDF before feeding it to the LLM. Stripping zero-font or white-colored text is trivially automated (pdftotext, grep, or any PDF reader's "show invisible text" feature). The paper acknowledges this scope limitation ("detailed investigation of attack and defense methods is left for future work"), but because the IPI scenario is the primary motivating application, the absence of even a basic adaptive-adversary experiment weakens the practical claims.

### Minor

- **"Model-agnostic" framing is imprecise.** The abstract calls ICW "a model-agnostic, practical watermarking approach." ICW is agnostic to model *architecture* and *internal access*, but the experiments show it is highly dependent on model *capability* (GPT-4o-mini fails for 3 of 4 strategies). The paper acknowledges this dependency in the conclusion but the abstract's phrasing could mislead readers into expecting broader applicability than demonstrated. The paper would be better served by "black-box" or "API-only" rather than "model-agnostic."

- **The word-replacement attack is tuned to the Lexical ICW's vulnerability.** The evaluation's word replacement attack replaces nouns, verbs, adjectives, and adverbs—precisely the word classes the Lexical ICW targets. The paper acknowledges this (Section 5.2.2), but the asymmetric effect (Lexical ICW AUC drops from 0.995 to 0.758 under replacement) should be more prominently discussed as a limitation of this particular strategy rather than presented alongside the other robustness results without explicit caveat in the comparison narrative.

- **LLM-as-a-Judge scores may partially reflect watermark detectability rather than quality.** The judge model (gemini-2.0-flash) may penalize watermarked text for statistical anomalies rather than genuine quality degradation. The clarity scores are notably lower for watermarked text (e.g., Initials ICW Clarity 3.706 vs. unwatermarked 4.994). Without human evaluation or a discussion of this confound, it is unclear how much of the clarity drop reflects actual readability loss vs. the judge detecting the watermark signal.

### Trivial

- Table 1's caption says "Darker circles indicate higher values" while the "LLM requirements" column header has a down-arrow (↓), creating a brief interpretive inconsistency. (Likely a formatting artifact.)

## Nice-to-Haves

- A human evaluation study comparing watermarked vs. unwatermarked review quality would strengthen the claim about imperceptibility in the IPI peer-review application.
- Testing ICW with open-source models of known capability (e.g., LLaMA-3-70B) would improve reproducibility and help calibrate which model capability level is "sufficient." The paper mentions open-source experiments in Appendix D.3 (stripped); if those results are positive, they deserve main-text attention.

## Removed Points

The following points from the harsh critic review were evaluated and removed:

- **"The paper does not evaluate any adaptive adversary"** — Removed because the paper explicitly states in Section 6 that it evaluates the "ignore prior prompts" attack in Appendix D.1. The claim of zero adaptive-adversary evaluation is factually incorrect. (The "strip invisible text" concern is retained as a separate valid point.)

- **"Comparison with baselines is unfair because baselines operate in a different pipeline stage"** — Removed. The paper clearly lists baselines and ICW operates in a different regime; the comparison is informative, not deceptive. If anything, the asymmetry favors the baselines (post-hoc methods have the advantage of operating on the final text).

- **"The paper claims major LLM providers don't use watermarks which is contestable"** — Removed. This is a minor factual aside, not central to the contribution, and the paper qualifies it with "to our knowledge."

- **"Missing discussion of per-example vs. aggregate detection / minimum text length"** — Removed. The paper already addresses output length effects in the ablation study (Section 6, Appendix D.1).

- **"No concrete FPR reporting"** — Merged into the main statistical concern (Major weakness 1). The T@1%F and T@10%F metrics are concrete FPR reporting; the issue is the calibration of those thresholds, not the absence of reporting.

- **"Adversary defense strategies not listed"** — Removed. The paper explicitly lists at least one (detecting and removing the embedded instruction) and scopes further investigation as future work. This is appropriate for an exploratory paper.

- **Strength: "Theoretical false-alarm guarantee"** — Merged into the weaknesses. The strength claimed by the Strength Finder is partially undermined by the miscalibration concern for Lexical ICW.

- **Strength: "Open-source code provided"** — Retained but de-emphasized as a minor supporting point, not a core strength.

## Novel Insights

The key insight that emerges from reading the reviewers and the paper is that ICW occupies a fundamentally different position in the watermarking design space from prior work. Existing methods (KGW, Aaronson, PostMark) treat watermarking as a *sampling-time* or *post-hoc* property; ICW treats it as an *instruction-following* property. This means ICW's effectiveness is bounded not by statistical detection theory but by the LLM's instruction-following ability—a capability that is rapidly and predictably improving. The practical implication is that ICW may transition from "interesting proof-of-concept" to "deployable solution" on a known trajectory, while traditional watermarking methods have already plateaued in their achievable trade-offs. The paper's calibration weakness (Lexical ICW's null model) and its incomplete adversarial evaluation in the IPI setting are concrete problems, but they are fixable without altering the core insight—if the null model is corrected and the instruction delivery method is made robust to simple stripping (e.g., distributing the instruction across the document body, not just invisible text), the practical viability increases substantially.

## Suggestions

- Correct the Lexical ICW null model: replace γ = |V_G|/|V| with an empirically estimated γ = Σ_{w∈V_G} p̂(w) from a held-out corpus, or use a permutation-based test that avoids the uniform-frequency assumption entirely. Show empirical FPR vs. theoretical FPR curves to validate calibration.

- Add an IPI experiment where the hidden instruction is stripped (simulating a reviewer who removes invisible text or converts PDF to plain text) and re-run detection. If detection fails, discuss what instruction-delivery mechanisms could resist this (e.g., distributing the instruction across visible content, using formatting cues the LLM preserves but humans ignore).

- Replace "model-agnostic" with a more precise term such as "black-box" or "API-only" throughout the paper to avoid overclaiming.

- Include the open-source model results from Appendix D.3 in the main text to broaden the evidence base.

## Score and Decision

**Round 1 bracketing:** Three calibration queries across score bands returned anchors at avg scores 2.67–3.00 (weak/rejected papers), 5.00–6.50 (middle band), and 8.00 (top-tier oral/posters). The ICW paper is clearly above the low band and well below the top band, placing it in the 4.5–7.0 range.

**Round 2 narrowing:** Within the bracket I examined full reviews and scores of five anchors:
- *LLM Fingerprinting via Semantically Conditioned Watermarks* (6.50, Oral): A strong fingerprinting paper with thorough experiments. ICW is more novel as a paradigm but has a weaker theoretical foundation. Comparable overall.
- *PMark* (7.00, Poster): Distortion-free semantic watermarking with solid theory. ICW is less theoretically complete but more broadly applicable. Slightly below PMark.
- *OpenStamp* (5.00, Reject): Weight-modification watermarking. ICW is clearly stronger in novelty and scope.
- *PRO* (5.00, Reject): Open-source watermarking. ICW has a clearer motivating scenario and more comprehensive evaluation.
- *Detecting Benchmark Contamination Through Watermarking* (5.00, Reject): Narrower application. ICW has broader impact.

**Final score:** The ICW paper introduces a genuinely novel paradigm and provides solid feasibility evidence, placing it above the 5.00-range papers. However, the uncorrected null model in the Lexical ICW statistical guarantee and the incomplete adversarial evaluation in the IPI setting prevent it from reaching the 6.5–7.0 level. It sits between the 5.00 and 6.50 anchors, comparable to but slightly below the LLM Fingerprinting paper (6.50) due to the statistical concern. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>