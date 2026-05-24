Now I have sufficient context. Let me write the consolidated review.

## Summary

This paper proposes Steady Thought (ST), a framework to mitigate "under-thinking" in large reasoning models—where models abandon promising reasoning trajectories prematurely. ST operates in three stages: (1) segmenting responses into thoughts via entropy-based detection, (2) generating "committed" completions of each thought by suppressing switch-indicating words (e.g., "wait", "alternatively") during decoding, and (3) performing thought-level preference optimization (STPO) that treats the completed trajectory as chosen and the original switch-heavy trajectory as rejected. Experiments across DeepSeek-R1-Distill (1.5B, 14B) and Qwen3-8B on MATH-500, AIME 2024, GSM8K, and LiveCode show accuracy gains of up to 5.3% alongside token reductions of 19–39%, with OOD generalization to code reasoning.

## Strengths

1. **Principled formalization of under-thinking as a preference optimization problem.** Section 2.1 defines commit and switch trajectories (Eq. 2) using the Bradley-Terry model, connecting under-thinking to an optimization objective in a way absent from prior ad-hoc suppression approaches.

2. **Thought-level preference optimization (STPO) delivers finer-grained supervision than response-level methods.** The STPO loss (Eq. 7) conditions on a specific thought prefix, providing a focused learning signal at the point of divergence. Table 4 shows STPO clearly outperforms SFT (+4.0 pt) and DPO (+2.6 pt) on MATH‑500 while also reducing tokens, demonstrating that thought-level supervision is measurably more effective.

3. **Consistent accuracy and efficiency gains across diverse model scales.** Table 1 reports improvements across three models (1.5B–14B) and four datasets: e.g., on Qwen3-8B overall accuracy rises by 3.12 % while output length drops by 25.5 %; on DeepSeek‑R1‑Distill‑Qwen‑1.5B accuracy increases by 1.9 % with 24.9 % fewer tokens. These results directly validate the central claim that ST mitigates under‑thinking without sacrificing performance.

4. **Superior trade‑off compared to existing under‑thinking mitigation methods.** ST achieves higher accuracy than NoThink, NOWAIT, and SEAL while typically using far fewer tokens. For instance, SEAL on Qwen3-8B raises accuracy by 2.35 % but *increases* tokens by 8.4 %, whereas ST raises accuracy by 3.12 % while *reducing* tokens by 25.5 % (Table 1). This demonstrates that ST's selective approach yields a better balance than global suppression.

5. **Out‑of‑distribution generalization to code reasoning.** Although trained only on math data, ST improves accuracy on LiveCode (e.g., Qwen3-8B +5.3 %, tokens –19.0 %; Table 1), indicating the framework teaches general reasoning principles rather than dataset‑specific patterns.

6. **Informative ablations on key components.** Table 3 systematically explores the entropy threshold, showing a clear optimum and the trade‑off between segmentation granularity and data quality. Table 4 isolates the effect of the training objective, confirming that STPO is critical for both accuracy and efficiency compared to SFT or DPO.

## Weaknesses

### Major

1. **No variance or confidence intervals for main results (Table 1).** The paper averages eight runs for AIME (30 problems) and two for LiveCode, but reports only point estimates without standard deviations, confidence intervals, or significance tests. For a 30-problem benchmark, a swing of 1–2 correct answers changes accuracy by 3–7 %, making it impossible to assess whether the claimed improvements (e.g., +1.9 % for DeepSeek-1.5B overall) are reliable or within noise. This is the most consequential evaluation gap.

2. **The claim that ST "preserves the ability to explore necessary alternatives" is not directly tested.** The paper states this repeatedly (e.g., lines 90–91) but offers only the PCT reduction in Table 2 as evidence. A lower percentage of correct intermediate thoughts is compatible with the model simply reaching answers faster, not necessarily with preserved exploration flexibility. No experiment evaluates whether ST still allows productive switching when the current thought is genuinely unpromising (e.g., on problems requiring multiple distinct reasoning paths). Without such evidence, this claim remains unsupported.

3. **No validation of thought segmentation accuracy or completion quality.** The entire preference pipeline depends on (a) reliably detecting thought boundaries via an entropy threshold, and (b) generating coherent completions via logit suppression. The paper provides neither human evaluation of segmentation quality nor analysis of whether forced-decoded completions are fluent, faithful to the original thought, or free of artifacts. If segmentation is noisy or completions are garbled, the preference pairs become mislabeled and the model may learn spurious patterns. The entropy threshold ablation (Table 3) provides indirect validation, but direct quality analysis is absent.

### Minor

1. **The PCT metric in Table 2 does not directly measure "invalid switching."** The paper interprets a lower PCT as indicating fewer abandoned promising thoughts, but it could also result from the model reaching correct answers faster (and thus generating fewer intermediate correct thoughts overall). The accuracy improvement makes the net effect benign, but the metric conflates two explanations.

2. **The SFT/DPO ablation (Table 4) is limited to one model (1.5B) and lacks experimental detail.** Extending this comparison to the 8B and 14B models in the main table would strengthen the claim that STPO is necessary. The paper also does not specify whether DPO was tuned for length sensitivity (e.g., using average log-probability) before concluding STPO's superiority.

3. **No decontamination analysis is reported.** The training set (omni-math) is used with a correctness filter on completions, and its overlap with MATH-500 and AIME 2024 is not checked. While the OOD results on LiveCode suggest the gains are not from memorization, a direct decontamination check would rule out inflation from test-set leakage.

4. **The trigger word list for logit suppression is not enumerated.** The paper mentions "wait" and "alternatively" as examples but does not provide the full list. Without this, it is unclear whether the list is exhaustive and whether it generalizes across domains.

5. **The paper lacks a dedicated limitations section.** Several limitations—reliance on a correct-answer oracle (preventing application to open-ended tasks), sensitivity to the entropy threshold, and the cost of generating completions for all promising thoughts—are not discussed.

### Trivial

- The entropy threshold is tuned only for the 1.5B model in the main text; the appendix (stripped) may cover other models, but the main text does not report chosen thresholds for Qwen3-8B and 14B, nor the criterion for selecting them.

## Nice-to-Haves

- A human evaluation (e.g., 100 examples) of whether entropy-based segmentation aligns with human judgments of "thought change," and whether the completed responses are fluent and faithful.
- An experiment on a subset of problems that genuinely require exploring multiple hypotheses (e.g., multi-path math or science problems) to directly test whether ST preserves beneficial switching.
- An ablation replacing entropy-based segmentation with simpler step-level splitting (using only ".\n\n") and replacing logit suppression with greedy decoding for thought completion, to isolate the contribution of each design choice.
- Reporting training compute (e.g., number of training steps, data size, GPU hours) to enable comparison of practical efficiency with baselines.
- Evaluation on additional non-math OOD domains such as logical reasoning (LogiQA) or science questions (GPQA) to further demonstrate generality.

## Removed Points

Points from the inputs that were removed with justification:

- **"The main results table should include training-based baselines (SFT on concise CoT data, RL with length penalty)"** — The paper already includes SFT and DPO ablations in Table 4; the main-table comparison against NoThink/NOWAIT/SEAL is appropriate since these are the established under-thinking mitigation methods. Demoting this to *Nice-to-Have*.
- **"No qualitative examples in main text"** — The paper references Appendix B for examples; the appendix is stripped by the parser. This is an artifact of the review format, not a paper flaw.
- **"Missing β, γ, learning rate, batch size, training steps, hardware"** — These are reproducibility details that may appear in the stripped appendix (referenced as Appendices D and E). Standard reporting practice but the hard rules classify undisclosed hyperparameters as nitpicks.
- **"Entropy threshold tuning only for one model"** — The paper explicitly states "We provide threshold tuning results on more models and datasets in the appendix D" (line 301); the appendix is stripped.
- **"AIME2024 anomaly contradicts general narrative"** — The paper already discusses this case (Section 4.4.1): "when smaller models tackle high-difficulty problems, they tend to increase the frequency of thought transitions to find the optimal solution." The criticism ignores the paper's own explanation.
- **"Training cost not reported in main text"** — The paper references Appendix E for consumption discussion; appendix is stripped.
- **"Figures 1a/1b unclear"** — This is a presentation opinion; the critic's own framing says "The narrative is acceptable."
- **"Missing related works"** — Hard rule prohibits this.
- **General speculative concerns about segmentation/completion quality without testing them** — Moved to the validated version above which notes the absence of direct validation rather than speculating about negative outcomes.
- **"The paper does not mention that SEAL also uses test-time modifications"** — The paper describes SEAL accurately; this is a non-issue.
- **"Appendix not available"** — Parser artifact; hard rule prohibits this.

## Novel Insights

None beyond the paper's own contributions. The key insight—that under-thinking can be addressed by segmenting reasoning into thoughts, generating committed continuations via targeted logit suppression, and training with fine-grained preference pairs at the thought level—is the paper's own contribution rather than something surfaced by the reviews.

## Suggestions

1. **Add confidence intervals or standard deviations to all main results (Table 1).** For AIME (30 problems), bootstrap resampling over the eight runs would be particularly informative. If some improvements are not statistically significant at conventional levels, state this transparently.

2. **Directly test the claim about preserved exploration flexibility.** Construct a small set of problems where the correct solution genuinely requires exploring multiple paths (e.g., problems with plausible but incorrect distractor approaches) and verify that ST does not reduce switching on these relative to the base model.

3. **Provide a small-scale validation of segmentation quality.** Sample 50–100 responses, have a human annotator mark thought boundaries, and report agreement with the entropy-based segmentation. Similarly, spot-check 50 completed responses for fluency and reasoning coherence.

4. **Extend the SFT/DPO ablation to at least one additional model (e.g., Qwen3-8B)** and include the results alongside the main table or in the main ablation section. Specify whether DPO used length normalization.

5. **Add a brief limitations paragraph** to the conclusion discussing the reliance on verifiable answers, sensitivity to the entropy threshold, and computational cost of the completion stage.

6. **Report the trigger word list** used for logit suppression, either in the main text or a clearly referenced appendix section.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| TPO | O0sQ9CPzai | 6.33 | R1, R2 | Similar in topic (preference optimization for reasoning). ST has broader model coverage (3 vs 1 model) but slightly weaker evaluation rigor (no error bars). Comparable quality overall. |
| IUPO | bGGMLWAGMc | 5.50 | R1, R2 | Similar goal (improving reasoning via preference optimization). ST has stronger novelty (thought-level pipeline) and broader experimental scope. |
| Rational Metareasoning | jRZ1ZeenZ6 | 5.00 | R1, R2 | Similar goal (efficiency in reasoning). ST has stronger empirical results across more models and achieves both accuracy *improvement* and token reduction rather than just maintaining performance. |
| LD-DPO | CuwjD3cazX | 5.00 | R2 | Different topic (length bias in DPO). Hard to compare directly, but ST has more comprehensive evaluation. |
| LOGO | FSlfoBIctk | 5.25 | R2 | Different topic (long-context alignment). Less directly comparable. |

**Bracketing (R1):** The paper sits between ~5.0 and ~7.0 — stronger than the rejected papers at 5.0–5.5 (Rational Metareasoning, IUPO, LD-DPO) but weaker than the strong accepts at 8.0. **Narrowing (R2):** Compared to TPO (6.33, accept), ST has comparable novelty and broader model/dataset coverage but lags in evaluation rigor. The paper is closest to TPO in topic and quality, suggesting a score near TPO's lower bound.

**Final score: 6.0**

The paper presents a genuinely novel framework with solid empirical results across multiple models and datasets, demonstrating both accuracy gains and substantial token reductions. However, the absence of variance reporting, an untested central claim about exploration flexibility, and unvalidated segmentation quality prevent a higher score. These gaps are addressable, and the core contribution is sound.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>