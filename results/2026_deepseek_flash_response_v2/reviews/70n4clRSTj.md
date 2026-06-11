## Summary

The paper introduces SpookyBench, a synthetic video benchmark that encodes content (text, object shapes, dynamic scenes) exclusively through motion patterns in noise-dominated frames—individual frames appear as random noise, but content becomes visible when viewed across time due to opposing motion cues. On this benchmark, all 15+ tested video-language models (including GPT-4o, Gemini, Qwen, InternVL, and many open-source models) achieve exactly 0% accuracy, while humans achieve ~98%. The paper argues this reveals a fundamental "time blindness" in current architectures.

## Strengths

1. **Novel, cleanly-designed benchmark that isolates a specific capability.** The generation procedure (Algorithms 1 and 2) is deterministic, reproducible, and clearly described. The SNR analysis (Basic SNR of −39 to −49 dB across categories) quantitatively confirms individual frames carry negligible spatial signal, validating the design premise.

2. **Comprehensive model coverage across scales and families.** The paper evaluates 25+ models spanning diverse architectures (LLaVA, Qwen, InternVL, VideoLLaMA, Gemini, GPT-4o), sizes (2B to 78B+), and access types (open/closed source), all yielding identical 0% results. This breadth makes a compelling case that the failure is architectural rather than model-specific.

3. **Frame-rate ablation rules out temporal sampling as the explanation (Section 4.3).** Humans degrade from 95.6% at 30 FPS to 0% at 1 FPS, while VLMs score 0% at every frame rate. This cleanly shows the issue is not about having enough frames or higher temporal resolution.

4. **Fine-tuning experiment strengthens the architecture-limitation claim (Section 4.4).** Training InternVL2.5-8B and Qwen2-VL-7B on 400 SpookyBench videos for 10 epochs still yields 0% test accuracy, demonstrating the failure is not attributable to domain mismatch or insufficient exposure.

## Weaknesses

### Major

1. **Framing-construct mismatch.** The paper persistently describes SpookyBench as evaluating "purely temporal understanding" (Abstract), "temporal reasoning capabilities" (Conclusion), and the ability to "capture purely temporal patterns" (Introduction). Motivating examples include firefly bioluminescence, Morse code, and neuroscience of interval timing (Paton & Buonomano 2018, Mauk & Buonomano 2004). However, the benchmark tests **motion-based figure-ground segregation from noise**—a specific perceptual capability where spatially-structured content (a mask) is made visible by coherent motion of noise patterns. This is meaningfully different from discrete-event temporal patterns (flash sequences, tone patterns). The benchmark is valuable, and the failure it reveals is genuine, but the paper overstates the generality of its findings. The "time blindness" framing implies a broader deficiency than what the evidence supports.

2. **No model output analysis.** The paper reports 0% accuracy for every model with zero variance, but provides no concrete examples of what models output, no confusion matrices, and no analysis of whether responses correlate with ground truth at any detectable level. The paper mentions "examination of model output revealed consistent failure modes" (lines 317–319) but gives zero examples. Are models saying "I see noise," guessing wrong labels, or producing gibberish? For a benchmark paper whose central finding is zero performance across all models, this omission significantly weakens the interpretability of the result.

3. **Under-specified fine-tuning experiment (Section 4.4).** The paper reports fine-tuning two models on 400 SpookyBench videos for 10 epochs with LlamaFactory, achieving 0% test accuracy. Critical details are missing: What was the train/test split? (451 total videos, 400 for training leaves only 51 for testing.) Was LoRA used or full fine-tuning? Which parameters were updated (vision encoder, connector, LLM)? What were learning rate, batch size, and other hyperparameters? Without these, the experiment cannot be properly evaluated or replicated. The claim that failure is "fundamental architectural" is plausible but not fully supported at this level of reporting.

### Minor

4. **Small human evaluation sample.** The main human study uses 6 participants (Section 4.2) and the frame-rate experiment uses 3 (Section 4.3). The low variance across annotators (±0.7–3.1%) and high agreement mitigate this concern somewhat, but a larger sample with formal inter-annotator metrics (e.g., Fleiss' kappa) would be standard practice for establishing a human baseline in a benchmark paper.

5. **Confusing exposition in Section 3.3.2 (Binary SNR Threshold Effect).** The text states "Prompts performed best (40% accuracy)" and discusses Chain-of-Thought reasoning, but it is unclear whether this refers to human or model performance. Since all models get 0% in the main evaluation, the 40–100% accuracy figures likely come from humans, yet "prompting" and "CoT" language is model-centric. This section needs clarification.

6. **The SNR metrics (Section 3.3) are defined by the authors and are not standard perceptual metrics.** While they provide internal consistency and show that individual frames contain negligible signal, they are not validated against any external measure of perceptibility. This limits their interpretability beyond the paper's own framework.

### Trivial

None.

## Nice-to-Haves

- A no-noise control condition (same content masks at full contrast) would clarify whether models fail specifically on motion-based perception or would also struggle with the recognition component.
- A comparison with optical-flow-based baselines (e.g., RAFT + classifier) would establish whether the task is solvable by current vision pipelines at all and would ground the claim about architectural limitations.
- A probe analysis (linear probe on frozen model embeddings) could reveal whether failure occurs at the representation level or the decoding/LLM level.
- Additional qualitative examples of model responses (actual outputs from several models across categories) would help readers interpret the 0% result.

## Removed Points

The following points from the inputs are removed with justification:

1. **"Suspiciously clean results at exactly 0% with 0.0 std dev"** — Removed. This is exactly what one would expect if every model fails on every video. The paper acknowledges this and describes examining outputs. Calling it "suspicious" without evidence of error is unwarranted alarmism.

2. **Strength Finder generic strengths** (e.g., "addressing an important problem") — Removed. These lack concrete evidence and are superficial.

3. **"Missing related works" / "Missing appendix"** — Removed per hard rules. The parser strips these sections; they exist in the original submission.

4. **Criticisms about SNR metrics not being standard** — Retained as Minor #6 but softened. The metrics are internally consistent and serve their stated purpose of validating the design premise.

5. **"No discussion of whether any model attempts to output something relevant"** — Subsumed by Major #2 (model output analysis).

6. **Strengths that conflict with verified weaknesses** — The Strength Finder's claim about "quantitative SNR validation that spatial information is absent" is partially valid but the SNR metrics are not standard (see Minor #6). The Strength Finder's claim about "controlled human evaluation" is fair but the sample size is small (Minor #4).

## Novel Insights

The reviews collectively surface a tension that the paper itself does not fully resolve: the benchmark's design (opposing-noise motion segmentation) and the paper's framing (discrete-event temporal patterns from fireflies/Morse code) point to different capabilities. The paper's actual contribution—demonstrating that VLMs fundamentally cannot perform motion-based figure-ground segregation from noise—is a genuine and striking finding. An insightful reframing would position SpookyBench as a test of *motion-based perceptual grouping* (a specific temporal-spatial capability) rather than *temporal reasoning* (a broader construct), and would acknowledge that the benchmark may not generalize to other forms of temporal understanding like event sequencing or interval timing. This recalibration would strengthen rather than weaken the paper, since the benchmark's practical value as a diagnostic tool is independent of whether it tests "pure temporal reasoning."

## Suggestions

1. **Reframe the paper's claims** to precisely describe what SpookyBench tests: motion-based figure-ground segregation from noise. Replace the "time blindness" framing with language that accurately characterizes the specific perceptual capability being evaluated.

2. **Add qualitative examples of model outputs.** Show actual responses from several models across all three categories. This single addition would substantially strengthen the paper's ability to support its central claim.

3. **Fully specify the fine-tuning configuration:** train/test split, LoRA vs full fine-tuning, learning rate, which parameters were updated, optimizer, and training-set accuracy.

4. **Add a no-noise control condition** (masks rendered at full contrast without noise) to isolate whether models fail on motion perception or content recognition.

5. **Clarify Section 3.3.2** by explicitly stating whether the SNR threshold analysis uses human or model data, and if the latter, how it is consistent with the 0% result in the main evaluation.

## Score and Decision

### Calibration Anchors

All retrieved anchors (across Rounds 1 and 2):

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| TemporalBench (Wto5U7q6I2) | 4.20 | R1 | Our paper has stronger benchmark novelty and more striking results; clearly better. |
| ViLMA (liuqDwmbQJ) | 6.00 | R1, R2 | Similar benchmark-paper quality, but ViLMA has more thorough analysis. Our paper ≈ ViLMA, slightly below. |
| TVBench (fCi4o83Mfs) | 6.75 | R1, R2 | More rigorous benchmark design principles and analysis. Our paper is weaker. |
| VideoNIAH (ZJo6Radbqq) | 5.75 | R2 | Similar synthetic benchmark approach with comparable rigor. Our paper ≈ VideoNIAH. |
| Vinoground (a1P5kh2oo8) | 5.75 | R2 | Our paper has stronger novelty (Vinoground was criticized for limited novelty); comparable analysis depth. Our paper slightly better. |
| T3 (sHAvMp5J4R) | 6.80 | R2 | Deeper analysis and a constructive method for improvement. Our paper is weaker. |
| PhysBench (Q6a9W6kzv5) | 8.00 | R1 | Far more comprehensive; our paper is not at this level. |
| Data-Type (WyEdX2R4er) | 8.00 | R1 | Different domain; not directly comparable. |

**Round 1 bracket**: Between 4.5 and 6.5.

**Round 2 narrowing**: The paper is comparable to VideoNIAH (5.75) and Vinoground (5.75), below ViLMA (6.00) and TVBench (6.75). The benchmark novelty is stronger than Vinoground's, but the missing model output analysis and framing issues pull it down relative to ViLMA.

### Final Assessment

The paper introduces a genuinely novel benchmark that reveals a striking and important limitation of current video-language models. The core finding—that all tested models fail completely on motion-based figure-ground segregation from noise—is worth reporting to the community. However, the paper's framing overextends the claims ("temporal reasoning," "time blindness") relative to what the benchmark measures, the absence of model output examples undermines interpretability of the headline 0% result, and the fine-tuning experiment lacks critical implementation details. These issues are addressable but, in the current form, hold the paper back from being a clear accept at a top venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>