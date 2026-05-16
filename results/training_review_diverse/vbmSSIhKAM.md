Now I have a thorough understanding of the paper. Let me synthesize the final review.

**Verification of key claims against the paper:**

Let me check one more thing — whether the paper mentions which specific systems are used as ASR-based baselines, since the critic says the ASR pipeline is not described.

The paper mentions "ASR-based dialogue systems" and "direct dialogue systems (such as Qwen2-Audio)" but never specifies:
- Which ASR model(s) were used for the ASR-based pipeline
- Which text-based LLM was paired with ASR
- Configuration details (temperature, decoding strategy, etc.)

The paper says "All of our prompt templates are included in the Supplementary Material" — but the supplementary material itself is not in the main paper (which is standard). However, the choice of ASR model and text LLM is not just a prompt template — it's a critical methodological detail. This is a valid concern.

Also checking: the critic says the paper doesn't evaluate statistical significance. Looking at Table 4 and Figure 2 descriptions, there are no error bars or significance tests mentioned. This is a valid (minor) concern.

Let me also verify the "first benchmark" claim. The paper says: "We present the first benchmark for evaluating the ability of spoken dialogue systems to understand acoustic information beyond speech content." SD-Eval (Ao et al., 2024) evaluates 4 acoustic attributes but uses non-dialogue data. The paper's Table 1 shows this comparison. The claim is specifically about "spoken dialogue systems" — SD-Eval is not dialogue-based. So the claim is defensible but could be more precise.

Now I have everything I need to produce the final review.## Summary

This paper introduces **VoxDialogue**, a fully synthetic spoken dialogue benchmark that evaluates systems on their ability to understand 12 acoustic attributes beyond speech content — spanning speaker information (age, gender, accent, language), paralinguistic features (emotion, volume, speed, fidelity, stress, non-verbal expressions), and environmental information (audio events, music). The benchmark comprises 4.5K multi-turn dialogues with attribute-specific synthesis pipelines and evaluates both ASR-based and direct spoken dialogue systems, finding that ASR pipelines fail on acoustically-dependent attributes while direct dialogue systems struggle with context. The contribution is a step toward more comprehensive evaluation of spoken dialogue understanding.

## Strengths

- **Most comprehensive acoustic attribute coverage for spoken dialogue evaluation.** Table 1 systematically compares VoxDialogue against 7 existing benchmarks (SUPERB, AirBench, Audio-Flamingo, SpokenWOZ, SD-Eval, LeBenchmark, Dynamic-SUPERB), showing that VoxDialogue uniquely covers all 12 attributes within a dialogue setting. Prior benchmarks either cover fewer attributes (SD-Eval covers 4), use non-dialogue data, or evaluate text-based interactions only. This is a genuinely useful resource for the community.

- **Novel per-attribute synthesis pipeline with distinct technical strategies.** Section 3.2 (Stage 2) details attribute-specific generation methods: conditional TTS with style instructions for gender/speed/emotion; text markers for stress/language/non-verbal cues; post-processing (downsampling to simulate fidelity loss, power scaling for volume, event splicing for audio/music); zero-shot TTS with age-specific reference timbres; and edge-TTS for multi-accent generation. This pipeline design is a technical contribution in itself, enabling the large-scale creation of controlled acoustic test data.

- **Systematic evaluation reveals meaningful performance patterns across system types.** Table 4 and Section 4.4 show that ASR-based systems outperform on context-driven attributes (speaker info, emotion) while direct dialogue systems (Qwen2-Audio) excel on acoustically-dependent attributes (speed, fidelity, audio, music). The finding that SALMONN's BLEU scores are inflated by repetition (87.53 BLEU on Stress but 0.97 lower GPT-score than Qwen2-Audio) is a concrete demonstration of why lexical overlap metrics alone are insufficient for this task. These results support the paper's central thesis that acoustic understanding requires direct audio processing.

## Weaknesses

### Major

- **Baseline configurations are critically underspecified.** The paper evaluates "ASR-based dialogue systems" without identifying which specific ASR model, which text-based LLM, what decoding parameters (temperature, top-p, etc.), or how dialogue history was formatted. For a benchmark paper whose experimental findings are a core contribution, this omission prevents reproducibility and makes it impossible to determine whether observed differences reflect genuine acoustic understanding gaps or simply poor system/task fit. The paper mentions prompt templates are in supplementary material, but the model choices themselves — not just prompts — are missing from the main text.

- **Evaluation metrics do not directly measure the stated contribution.** The paper claims to evaluate "understanding of acoustic information beyond words," yet the primary quantitative metrics (BLEU, ROUGE-L, METEOR, BERTScore) are all text-based lexical/semantic overlap measures. A response that correctly uses acoustic cues but diverges lexically from a single reference would score poorly. The GPT-based metric (Table 4) is more appropriate — it assesses attribute awareness on a 1–4 scale — but the paper provides no human evaluation to validate that GPT scores correlate with human judgments of attribute-appropriate responses. The core empirical conclusions thus rest on metrics that are at best a proxy for the claimed capability. The paper should include a human agreement study for the GPT metric or design attribute-specific accuracy measures (e.g., did the response correctly adjust volume/address age/etc.).

### Minor

- **Fully synthetic data with insufficient naturalness validation.** All 4.5K dialogues are LLM-generated scripts rendered via TTS, with no human–human or human–system speech data. Stage 5 mentions "human annotators for additional quality checks" but provides zero details: number of annotators, instructions, pass/reject rate, or inter-annotator agreement. For a benchmark intended to measure real-world spoken dialogue capability, this validation gap weakens confidence that the acoustic attributes are naturally manifested rather than exaggerated or caricatured. A small-scale human evaluation of naturalness and attribute fidelity (even 100 samples) would substantially strengthen credibility.

- **Task mismatch confound for direct dialogue systems is acknowledged but not controlled.** Section 4.4 notes that Qwen-Audio produces "descriptive sentences" and SALMONN "repeats parts of the query," observing that these models are designed for QA-style interactions rather than dialogue. This is a fair limitation discussion, but the paper could strengthen its claims by attempting to prompt these models for dialogue-appropriate behavior (e.g., a system prompt instructing natural conversational responses) to isolate acoustic understanding from task mismatch.

- **No statistical significance reported.** Table 4 and Figure 2 report point estimates without error bars, confidence intervals, or significance tests. With ~300 dialogues per attribute, variance could be meaningful, and the reader cannot assess whether reported differences (e.g., Qwen2-Audio's lead over FunAudioLLM on acoustic attributes) are robust.

- **Human verification details missing for both data quality and ethical filtering.** Stage 5 (data quality) and the ethical discussion ("manual filtering of all potentially sensitive data") both mention human involvement without specifying criteria, number of annotators, or agreement rates. These are opaque quality gates.

### Trivial

- The claim "first benchmark for evaluating the ability of spoken dialogue systems to understand acoustic information beyond speech content" is defensible but could be more precise: SD-Eval (Ao et al., 2024) already evaluates gender, age, accent, and emotion, though on non-dialogue data. The paper's novelty lies in dialogue context + broader attribute coverage — stating this explicitly would preempt the natural comparison.

- The edge-TTS tool used for accent generation is proprietary, limiting full reproducibility of the data synthesis pipeline.

## Nice-to-Haves

- A per-attribute accuracy metric (e.g., classifier-based or human-validated GPT scoring for each of the 12 attributes individually) would align evaluation more directly with the paper's stated goal of measuring acoustic understanding.
- A small-scale human evaluation of dialogue naturalness and attribute fidelity on a random 100-sample subset would substantially increase confidence in the synthetic data quality.
- Providing sample audio files in the supplementary material would help reviewers assess data quality directly.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Paper does not release data/code at review time."** — REMOVED per hard rule: questioning release status of cited resources is not permitted. The paper states all data and code will be open-sourced.
- **"No systematic survey or user study to confirm the 12 attributes are the most impactful."** — REMOVED as scope creep. The paper identifies attributes based on analysis and examples; demanding a user study to justify attribute selection is beyond the paper's scope and turns it into a different kind of work.
- **"Pure formatting/style nitpicks" and "typos/spelling" related to parser artifacts.** — None present in the critic's review; flagged defensively.

## Novel Insights

The most novel insight emerging from the review process is the observation that **existing direct audio-language models (Qwen-Audio, SALMONN) are fundamentally mismatched to dialogue-style evaluation** — they produce descriptive or repetitive outputs that inflate n-gram overlap scores while producing poor qualitative judgments. This reveals a structural gap in the current model landscape: the models best equipped to process acoustic information are trained on QA data, not dialogue data, creating a confound that any benchmark in this space must address. Separating "acoustic understanding capability" from "dialogue appropriateness" is a nontrivial methodological challenge that VoxDialogue partially surfaces but does not fully resolve.

## Suggestions

- **Specify all baseline configurations** in a dedicated table: ASR model name/checkpoint, text LLM name/version, decoding parameters (temperature, top-p, max tokens), dialogue history formatting, and any system prompts used (beyond those in supplementary material).
- **Add a human validation study for the GPT-based metric** (50–100 samples scored by both GPT and human annotators, reporting Spearman correlation and agreement rates). This would substantially strengthen the paper's empirical foundation.
- **Report error bars or confidence intervals** for all quantitative results (Table 4 and Figure 2), computed via bootstrapping across attribute subsets.
- **Expand Stage 5 (Human Verification) with concrete numbers**: number of annotators, task instructions, pass/rejection rate, and inter-annotator agreement (Cohen's κ or similar).
- **Consider per-attribute scoring** in addition to the holistic GPT metric — e.g., for the Volume subset, explicitly verify whether the model's response addressed the volume cue appropriately.

## Score and Decision

This paper addresses a genuine gap, the benchmark is well-motivated, and the per-attribute synthesis pipeline represents a substantive technical contribution. The experimental evaluation reveals interesting and non-obvious findings about current model limitations. However, two issues are significant enough to weigh against acceptance: (1) the baseline configurations are underspecified to the point that the experimental findings cannot be independently reproduced or interpreted, and (2) the evaluation metrics do not directly measure the paper's central construct (acoustic understanding) — the text-based metrics and unvalidated GPT metric form a weak basis for the paper's main empirical claims. These are addressable in revision but are not trivial fixes.

The paper would be strong with these revisions. In its current form, the contribution is promising but the evidence does not yet fully support the claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Weak Reject</orange>