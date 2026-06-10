## Summary

MMAU is a 10k-instance, multi-domain (speech, environmental sounds, music) multiple-choice benchmark for evaluating audio-language models. It covers 27 distinct skills across information extraction (3.5k) and reasoning (6.5k) tasks, with human-annotated questions designed to require expert-level knowledge. The paper evaluates 18 open-source and proprietary models plus cascaded captioning+LLM baselines, finds the best LALM (Gemini Pro v1.5) achieves only 52.97% against a human baseline of 82.23%, and provides diagnostic experiments (noise substitution, skill-wise breakdown, error-type classification) that yield actionable insights for the community.

## Strengths

- **Scale and systematic coverage that exceeds prior audio benchmarks**: MMAU provides 6.5k reasoning questions across all three audio domains (speech, sound, music), compared to AIR-Bench's 0.8k reasoning questions. Table 2 shows it is the only benchmark combining all three domains with substantial reasoning volume, directly supporting the paper's claim of addressing a gap left by prior work.

- **Noise probe experiment provides a clean behavioral diagnostic**: Section 4.2 replaces audio with Gaussian noise and measures performance change. The finding that MuLLaMa and SALMONN show "little change" while GAMA, Qwen2-Instruct, and Gemini Pro exhibit significant drops is a concrete, reproducible test that no prior audio benchmark conducts, and it directly shows that MMAU can distinguish models that genuinely process audio from those exploiting language priors.

- **Human-annotated error-type breakdown quantifies where models fail**: Section 4.5 reports a manual categorization of 500 errors into perceptual, reasoning, knowledge, extraction, and annotation types. The findings—55% perceptual errors for Qwen2-Audio-Instruct, 64% for Gemini Pro—are specific, actionable diagnostics that go well beyond aggregate accuracy and directly support the paper's claim of enabling "in-depth analysis of model responses."

- **Large human–model performance gap confirms the benchmark is not saturated**: Human accuracy at 82.23% on test-mini vs. the best LALM at 52.97% and best cascaded approach at 58.74% leaves a ~29-point gap. This is concrete evidence that MMAU measures capabilities well beyond current SOTA, unlike many benchmarks where models quickly approach ceiling performance.

- **Skill-specific analysis across difficulty levels reveals strengths and weaknesses are skill-dependent, not difficulty-dependent**: Section 4.4 shows models excel in certain skills across all difficulty levels (Phonemic Stress Pattern Analysis) but consistently struggle with others (Temporal Reasoning), with Gemini Pro's accuracy nearly flat across easy/medium/hard (39.60/43.82/36.03) despite large skill-level variation. This is a more nuanced result than aggregate accuracy per tier.

## Weaknesses

### Major
None. The core contribution is well-supported; the issues below are transparency/framing concerns that are addressable.

### Minor

- **Self-assessed difficulty ratings and "first comprehensive" framing are asserted but not independently validated**: The paper calls itself "the first comprehensive benchmark" for audio reasoning (lines 29, 67), yet AIR-Bench (Yang et al., 2024) also covers all three domains with 19k samples and 0.8k reasoning questions. Table 2's "Difficulty Level" (4.5 for MMAU, 2.5 for AIR-Bench) and "Expert Comments" are ratings by the paper's own experts, not independently validated. The quantitative differences are real (6.5k vs 0.8k reasoning), but the dismissive characterization of prior work ("basic acoustic information retrieval with minimal reasoning depth") would benefit from side-by-side evidence rather than self-assessment.

- **Human evaluation protocol is completely opaque**: The paper reports human accuracy at 82.23% on test-mini (line 216, Table 2) but provides no information about how many annotators participated, their qualifications, whether this was crowdsourced or an expert panel, the evaluation protocol, or inter-annotator agreement. Without these details, the human ceiling—a key reference point—is hard to interpret or reproduce.

- **Data sources are not disclosed**: The curation pipeline (Step 1, line 99) mentions "diverse audio corpora, including speech, music, and environmental sounds" but does not name the specific sources. This matters for reproducibility, contamination analysis, and understanding potential domain biases.

- **No inter-annotator agreement reported**: The curation pipeline involves multiple expert annotation/filtering steps (Steps 3, 4, 6), skill labeling, difficulty rating, and error classification (Section 4.5), yet no measure of inter-annotator agreement is reported for any of these steps.

- **Per-model prompt optimization risks inconsistent evaluation**: Line 204 states "we experiment with various prompt sets across all LALMs and report the best results." Reporting per-model best scores means different prompts may have been used for different models, which can introduce inconsistency in a benchmark intended for standardized comparison. The specific prompts used per model should be reported.

- **MCQ format limits but does not invalidate the "reasoning" framing**: All 10k questions are multiple-choice, which tests recognition of the correct answer rather than open-ended production of a reasoned response. The paper acknowledges this limitation (line 307), but the language throughout—"expert-level reasoning," "simulating expert-level cognitive processes"—is in tension with the format. MCQ-based reasoning evaluation is standard practice (MMLU, MMMU), but the framing would be more precise if calibrated accordingly.

### Trivial

- **Noise experiment results lack numerical values in text**: Section 4.2 describes performance changes qualitatively ("remains largely unaffected," "significant drop") without reporting the actual accuracy numbers or drops, which would make the diagnostic more useful.

## Nice-to-Haves

- A side-by-side comparison (e.g., 50–100 matched examples from MMAU and AIR-Bench) demonstrating why MMAU questions require deeper reasoning would strengthen the novelty claim.
- A breakdown of which fraction of questions can be answered from captions alone vs. requiring direct audio access would help disentangle audio perception from text reasoning.
- A contamination analysis (e.g., n-gram overlap between MMAU text/audio sources and model training data) would be a useful addition.

## Removed Points

These points were flagged by the harsh reviewer but are removed with justification:

- **GPT-4 option augmentation contamination risk** (removed: speculative, and more fundamentally, GPT-4 generates *distractors* (wrong options), not correct answers—if a model were "contaminated" by GPT-4 patterns, it would be more likely to select GPT-4-looking wrong options, making the benchmark harder, not easier, for such models).
- **Wrapfigure hard to parse** (removed: formatting nitpick).
- **Missing appendix details** (removed: appendix content stripped by PDF parser, not a paper flaw).
- **Temperature/decoding parameters not specified** (removed: trivial implementation detail).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Disclose the specific audio corpora used as data sources (Step 1).
2. Provide full details on the human evaluation: number of annotators, qualifications, protocol, and inter-annotator agreement scores.
3. Report inter-annotator agreement for the error-type classification (Section 4.5) and for difficulty/skill labeling during curation.
4. Include concrete numerical values for the noise experiment performance drops in the text.
5. Replace or supplement "first comprehensive" framing with a more precise characterization of what MMAU adds over the closest prior benchmark (AIR-Bench): e.g., 8x more reasoning questions, broader skill coverage, expert-annotated difficulty tiers.
6. Standardize the evaluation prompt or at least disclose the specific prompts used per model.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>