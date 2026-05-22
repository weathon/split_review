Now I have all the information needed to write a consolidated review.

## Summary

This paper introduces In-Context Watermarking (ICW), a novel approach that embeds detectable signals into LLM-generated text purely through prompt engineering, without modifying the decoding process. The authors propose four ICW strategies (Unicode, Initials, Lexical, Acrostics) at different granularity levels, each with a tailored detection method. They evaluate ICW in a Direct Text Stamp (DTS) setting where the instruction is in the system prompt, and an Indirect Prompt Injection (IPI) setting motivated by detecting AI-generated peer reviews. With the capable gpt-o3-mini model, ICW achieves near-perfect detection (ROC-AUC ≥ 0.995) in DTS, matches or exceeds post-hoc baselines in robustness, and preserves text quality.

## Strengths

- **A genuinely new watermarking paradigm.** ICW is the first approach to embed watermarks purely through prompt engineering, requiring only black-box API access. This is a distinct contribution that opens a new direction distinct from existing logit-modification or post-hoc approaches.

- **Strong DTS results on capable models are thoroughly demonstrated.** With gpt-o3-mini, all four ICW strategies achieve ROC-AUC ≥ 0.995 in the DTS setting (Table 2), equalling or exceeding post-hoc baselines PostMark (0.977) and YCZ+23 (0.998). Detection remains high under word deletion, replacement, and LLM paraphrasing (Figure 3, AUC ≥ 0.857 for all methods), and text quality as evaluated by LLM-as-a-Judge is substantially closer to unwatermarked text than baseline methods (Table 3).

- **Four ICW strategies with tailored detection provide a useful trade-off analysis.** The paper systematically explores watermarking at the character (Unicode), word-initial (Initials), word-level (Lexical), and sentence-level (Acrostics) granularities. Table 1 gives an intuitive summary of trade-offs across LLM requirements, detectability, robustness, and text quality, and the detection statistics (z-statistic, Levenshtein distance) are principled.

- **Theoretical false-alarm guarantees are provided.** Appendices B derive closed-form false-positive rate guarantees for Initials and Lexical ICWs, increasing the reliability of the detection methodology.

- **The paper honestly identifies its own limitations.** Section 4.2.2 acknowledges vulnerability to spoofing when the scheme is known, Section 6 discusses directions for improving instructions and treating ICW as an alignment task, and Appendix D.1 investigates two attack scenarios.

## Weaknesses

### Major

- **The IPI setting's covert-transmission mechanism is not experimentally validated.** The IPI experiments (Table 2) concatenate the watermark instruction as *visible text* with the paper content. This tests whether an LLM follows instructions in long-context scenarios — a necessary condition — but does *not* test whether an instruction embedded via 'white text', zero-font, or other obfuscation survives PDF-to-text extraction and reaches the LLM. Since the paper's motivating application (detecting AI-generated peer reviews) depends on covert embedding, this is a significant gap. The authors acknowledge this (Section 3.2: "a detailed investigation of attack and defense methods is left for future work"), but the gap between the claimed use case and what is tested limits the strength of the IPI contribution. The DTS contribution stands independently, but the IPI framing overreaches relative to the evidence.

- **Only proprietary GPT models are evaluated, no open-source models.** ICW is tested only on gpt-4o-mini and gpt-o3-mini. Evaluating on open-source models (e.g., Llama 3, Mistral) of varying capability would clarify whether the approach generalizes across model families or is GPT-specific. This is a standard expectation in LLM watermarking papers and is particularly relevant since ICW's effectiveness is explicitly tied to model instruction-following ability.

### Minor

- **No quantification of robustness against an *aware* adversary.** The paper acknowledges (Section 4.2.2) that the green letter set or green word list can be inferred from a few samples, making the scheme vulnerable to targeted removal or spoofing, and Appendix D.1 investigates some attacks. However, there is no systematic evaluation of how detection degrades under an adversary who knows the scheme and actively counteracts it. This would establish a realistic lower bound on robustness.

- **No confidence intervals or variance reported for main detection results.** Table 2 and Figure 3 report ROC-AUC and T@X%F without any uncertainty estimates. While single-run evaluation is common in this area, the absence of any variance information makes it difficult to assess whether the near-perfect scores (e.g., 1.000 AUC for Acrostics ICW) are stable.

### Trivial

- **"Model-agnostic" in the abstract is imprecise.** The term is used to mean "does not require model-internal access" (which is correct), but could be read as "works equally well on all models" (which Table 2 contradicts). The paper's own framing in later sections is more accurate, but the abstract would benefit from clarification.

## Nice-to-Haves

- A human evaluation of text quality (or example watermarked outputs) would strengthen the text quality claims, since the LLM-as-a-Judge evaluation shows suspiciously high scores for unwatermarked GPT text (4.982/5.000/4.994), suggesting possible judge self-bias.
- The IPI setting could be strengthened by testing whether the hidden instruction survives realistic PDF pipelines (e.g., PyMuPDF extraction) with white-text or zero-font embedding, even on a small scale.

## Removed Points

The following points from the harsh critic review are removed or downgraded:

- **"The IPI setting collapses to DTS because the dishonest reviewer would see the instruction"** — This ignores the paper's explicit threat model (Figure 2, Section 3.2): the instruction is *covertly* embedded by conference organizers (e.g., white text), visible only to the PDF parser, not to the reviewer. The paper discusses this, and the IPI experiments test the necessary condition (instruction following in long context). The critic conflates an untested link with an invalidated concept.
- **"Table 1 detectability rating inconsistent with results"** — Table 1 is explicitly a qualitative summary of trade-offs, not a guarantee of performance on any specific model. The text explains the model dependence clearly.
- **"No statistical significance reported"** — While true, this is standard practice in this area and is a minor omission, not a serious weakness.
- **Typos/formatting criticisms** — Parser artifacts, not author errors.
- **Complaints about missing related work** — Cannot be verified without external sources.
- **Generic "overclaims relative to evidence" framing** — Removed as too broad; the specific claim (IPI covert transmission untested) is retained as a Major weakness.

## Novel Insights

None beyond the paper's own contributions. The key insight — that sufficiently capable LLMs can be prompted to embed detectable statistical signals into their outputs — is the paper's own contribution, not a meta-observation from the reviews.

## Suggestions

1. **Address the IPI validation gap directly.** Even a small-scale experiment showing that a watermark instruction embedded as white text in a PDF survives extraction through common PDF-to-text pipelines (PyMuPDF, pdftotext) and is followed by the LLM would substantially strengthen the IPI claims. If this is not feasible, reframe the IPI contribution as "testing instruction-following in long documents" rather than "covert injection."

2. **Add open-source model evaluation.** Testing ICW on at least one open-source model (e.g., Llama 3-70B, Mistral Large) would clarify whether the approach depends on GPT-specific alignment or generalizes across model families.

3. **Quantify robustness against aware adversaries.** For at least Initials ICW, show detection performance when an attacker has inferred the green letter set (e.g., from 10 watermarked samples) and removed/edited words with those initials.

4. **Add bootstrap confidence intervals** to the main detection results (Table 2). This is a low-effort improvement that significantly strengthens the evidence.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for three bands on "LLM watermarking prompt engineering in-context":
- Weak band (avg < 3.5): Anchors at scores 3.0–3.4 (e.g., jbfDg4DgAk, 3.0 — Sparse Watermarking, Reject; xRi8sKo4XI, 3.0 — Unsupervised Prompt Learning, Reject) — ICW is clearly stronger than these.
- Middle band (3.5–7.5): Anchors from 3.67 to 7.0 — ICW falls in this range.
- Strong band (>7.5): Anchors at 7.6–8.0 (e.g., SnDmPkOJ0T, 8.0 — REEF, Accept) — ICW is clearly weaker than these established papers.

**Round 2 (Narrowing within 4.5–7.0):** Anchors used:
- 0koPj0cJV6 (4.60, "A Watermark for Black-Box Language Models", Reject) — Similar black-box watermarking objective but weaker empirical results, unclear practical motivation, and mixed reviews.
- DEJIDCmWOz (6.00, "On the Reliability of Watermarks for Large Language Models", Accept) — Solid robustness study with comprehensive experiments; comparable empirical quality but less novelty.
- E4LAVLXAHW (7.00, "Black-Box Detection of Language Model Watermarks", Accept) — More rigorous statistical methodology and broader evaluation; stronger than ICW.
- ujpAYpFDEA (7.50, "Can Watermarked LLMs be Identified by Users via Crafted Prompts?", Accept) — Stronger evaluation and clearer contribution.

ICW is **stronger** than the 4.60 paper (which had clearer methodological flaws and weaker results) and **comparable to** the 6.00 paper in overall quality, but **weaker than** the 7.00 and 7.50 papers (which have more thorough evaluation). The paper's novelty is higher than the 6.00 anchor, but its evaluation coverage is sparser, placing it in the same band.

**Final score: 6.0** — The paper introduces a genuinely novel watermarking paradigm with strong DTS results on capable models. The core weaknesses (unvalidated IPI covert transmission, limited model zoo, no open-source evaluation, no informed-attacker quantification) are real but do not invalidate the primary contribution. With revisions to address the IPI gap, this could be a strong contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>