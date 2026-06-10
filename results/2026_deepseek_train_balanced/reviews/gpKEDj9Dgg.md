Now I'll produce the final review.

## Summary

This paper proposes using a LoRA-tuned LLM for second-pass rescoring of Whisper-Large-v3 N-best hypotheses to improve ASR transcription of medication names in low-resource healthcare settings. The idea of applying LLM-based ASR rescoring specifically to the medication name domain is a plausible direction, but the paper as written contains fatal structural flaws that prevent its claims from being evaluated.

## Strengths

- **First targeted application to medication name recognition**: The paper identifies a concrete gap — prior ASR+LLM rescoring work (Hyporadise, Whispering LLaMa) focused on general domains, and prior healthcare ASR+LLM work (Kanithi et al., 2024) assumed high-resource settings. Applying LLM rescoring to medication name transcription is a new domain-specific instantiation (Section 1, line 15; Section 2, line 27).

- **Well-motivated domain choice with patient-safety rationale**: Section 1 provides specific examples of dangerous transcription errors (hyper- vs. hypo-, rifampin vs. rifampicin) and cites legal risks (Ajami, 2016), concretely justifying why medication names specifically need improved ASR accuracy (lines 13–14).

- **LoRA configuration is concretely specified**: The paper specifies LoRA rank r=4, 8-bit training, 15 epochs, learning rate 1e-4, batch size 64, and a single V100 GPU (Section 4.1, lines 44–46). These details are useful for reproducibility of the LLM fine-tuning component.

## Weaknesses

### Fatal

- **Dataset as described lacks audio data, making the claimed ASR pipeline impossible to execute.** The paper's pipeline requires Whisper-Large-v3 to process audio and generate N-best hypotheses (Section 4.1, point 2). But the dataset is described only as "about 600 medication names prescribed globally with their trade names which we curated ourselves" separated into "506 rows for the training and the rest for testing" (Section 4.1, point 4). There is no mention of audio recordings, speaker demographics, recording conditions, or any acoustic data anywhere in the paper. The "Pharma-Speak" dataset mentioned in the abstract is never described in the body. Without speech input, Whisper cannot generate N-best hypotheses, and the entire rescoring pipeline collapses. This is a structural flaw verifiable from the paper as written — the experimental setup cannot support the claimed method.

### Major

- **No actual results are reported for the claimed evaluation**. The abstract claims "a significant reduction in Word Error Rate (WER) across multiple epochs." Yet the experiment section states "We used ROUGE score to evaluate the performance of the model" (Section 4.1, point 5). No WER numbers are reported anywhere. No ROUGE scores are reported anywhere. The single quantitative claim — "This result is significantly better than the finetuning of the ASR model itself with the use of speech dataset achieving a benchmark of 21%" (Section 4.2, line 50) — does not state what 21% refers to (WER? ROUGE? CER?), provides no baseline numbers, no confidence intervals, and no significance test. Table 1 is referenced but is an unreadable image. The evaluation provides no verifiable evidence for the paper's central claim.

- **The abstract claims a different method than the experiment implements.** The abstract states the paper "fine-tuned the Whisper-Large ASR model on a custom dataset, Pharma-Speak, and applied the LLaMA 3 model for second-pass rescoring." The experiment section (4.1, point 1) says "The experiment employs the Llama-2-8b Instruct model" — a different model family (LLaMA 3 vs. Llama 2), and "Llama-2-8b" does not exist as a released model (Llama 2 has 7B, 13B, 70B variants). The experiment section only describes fine-tuning the LLM, not Whisper. The "Pharma-Speak" dataset is never defined. These inconsistencies between the abstract and the experiment make it impossible to determine what was actually done.

- **No baseline comparisons against any existing method.** The paper cites Hyporadise (Chen et al., 2024), Whispering LLaMa (Radhakrishnan et al., 2023), and MEDIC (Kanithi et al., 2024) as related work but provides no comparison against any of them. The only comparison mentioned is "the finetuning of the ASR model itself" — a baseline that is itself not described, not run, and for which no numbers are reported.

### Minor

- **The LLM rescoring procedure is not specified.** The methodology describes LoRA generically (Section 3) but does not explain the actual rescoring mechanism: what prompt is used, how N-best hypotheses are fed to the LLM, how the model's output is converted to a score, or how the final transcription is selected from the N-best list. The phrase "the adaptor module gets the capability to forecast the real transcription from the N-best theories" (Section 3, line 40) is too vague to be replicable.

- **Very limited dataset size (506 training samples) and acknowledged lack of comprehensiveness** (Section 4.3). While the paper acknowledges this, it further limits confidence in the proposed approach.

### Trivial

None.

## Nice-to-Haves

- If the dataset actually contains audio (which is necessary for the pipeline), this must be clearly described, including recording conditions, speaker information, and how Whisper was used to generate N-best hypotheses from it.
- Comparison against simpler rescoring methods (e.g., an n-gram language model rescoring) would help isolate the contribution of the LLM component.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Typos and grammatical issues** ("acheievng," "ysed," "LLamA," "sophiscticated"): Removed per hard rules — these are treated as parser artifacts from the PDF extraction process, not author errors in the original submission.
- **"No code or data release mentioned," "no reproducibility statement"**: Removed — code release is not a requirement for paper evaluation.
- **"No qualitative examples of ASR errors corrected by the LLM"**: Removed — this is a nice-to-have, not a required element.
- **Strength: "Fully specified reproducible configuration"**: Removed — conflicts with the verified fatal weakness (the dataset is not described as containing audio, so the setup is not reproducible as described).

## Novel Insights

None beyond the paper's own contributions. The observation that existing ASR+LLM rescoring work has not been applied to medication names is noted by the paper itself but is a domain application, not a methodological insight.

## Suggestions

1. **Clarify the dataset.** If audio data exists, describe it in full: how was it collected, what does it contain, how were Whisper's N-best hypotheses generated from it. If no audio data exists, the paper cannot claim an ASR pipeline and the framing must be fundamentally revised.
2. **Resolve the model identity.** Pick one model (LLaMA 3 or Llama 2) and be consistent. Correct the model size if it is mis-specified.
3. **Report actual evaluation numbers.** If WER is claimed, report WER for both the Whisper baseline and the LLM-rescored output, with confidence intervals or error bars. Report the ROUGE scores if that is the chosen metric. Provide baseline comparisons against existing methods.
4. **Align abstract with experiments.** Either describe the Whisper fine-tuning in the experiment section or remove that claim from the abstract. Describe "Pharma-Speak" if it is a real dataset.

## Score and Decision

MY FINAL SCORE: <score>1.0</score>
MY FINAL DECISION: <decision>Reject</decision>