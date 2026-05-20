Now I have a clear picture of the calibration landscape. Let me write the final consolidated review.

**Round-1 bracket**: Based on comparisons with anchors, the paper sits in the (1.5, 3.5) range. The ivrit.ai paper (avg 2.5) had a genuine large-scale dataset contribution but was rejected; this paper has a plausible idea but an evaluation that is fundamentally incomplete. It is clearly weaker than the pronunciation-lexicon paper (avg 3.75) which had novel methodology and solid experiments, and clearly weaker than papers in the middle band (3.5–7.5) like the ASR fusion paper (avg 6.6) which had thorough evaluation. It is somewhat comparable to ivrit.ai (2.5) but with less concrete contribution — ivrit.ai at least had a clear dataset; this paper's dataset is underspecified and its evaluation doesn't match its claims.

**Round-2 narrowing**: Within (1.5, 3.5), comparing to the Precision/Recall Reject Curves paper (avg 1.5) — this paper is better than that (that had a fundamentally flawed premise). Comparing to ivrit.ai (2.5) — this paper is slightly weaker since its evaluation is more fundamentally broken. Comparing to the pronunciation-lexicon paper (3.75) — this paper is clearly weaker. I'd place this paper at **2.5**.

---

## Summary

This paper proposes a two-stage ASR pipeline (Whisper-Large-v3 → LLM with LoRA) for improving transcription of medication names in low-resource healthcare settings. The idea is to use a fine-tuned LLM (Llama-2/3) for second-pass rescoring/correction of Whisper's N-best hypotheses.

## Strengths

- **Domain-specific application with a clear practical motivation**: The problem of ASR errors on medication names in clinical settings is real and consequential; the paper correctly identifies that generic ASR models struggle with pharmaceutical terminology, accent variability, and noisy environments common in low-resource healthcare.

- **Efficient fine-tuning on limited hardware**: The use of LoRA (rank r=4) with 8-bit training on a single NVIDIA V100 GPU in Google Colab (Section 4.1) demonstrates computational feasibility for resource-constrained environments, aligning with the stated low-resource focus.

- **Custom dataset creation**: The authors curated Pharma-Speak, a dataset of ~600 medication names with trade and chemical names, split into 506 training and ~94 test samples. Though underspecified in the paper, this represents a concrete resource for the domain.

## Weaknesses

### Major

- **Fundamental metric mismatch between the central claim and the evaluation**: The abstract and conclusion claim "significant reduction in Word Error Rate (WER)" but Section 4.1 states "We used ROUGE score to evaluate the performance of the model." WER and ROUGE measure fundamentally different things — WER measures transcription accuracy (deletions/substitutions/insertions at the word level) while ROUGE measures n-gram overlap (a text generation metric). Table 1 lists values 13.45, 25.10, 7.98, 7.45 under an unlabeled "Result" column, so the reader cannot even tell whether these are ROUGE scores, WER percentages, or something else entirely. This mismatch undermines the paper's core evidential claim.

- **No in-house baseline on the same test set**: The only baseline mentioned is "a benchmark of 21%" (Section 4.2), attributed to "finetuning of the ASR model itself." No citation is provided, no indication of which test set this was measured on, and no in-house reproduction is reported. This means that even if the Table 1 values are WER, the reader cannot determine whether the improvement comes from the LLM rescoring or from differences in test data, model configuration, or evaluation protocol. A controlled ASR-only result on the same Pharma-Speak test set is the single most important missing piece.

- **Dataset critically underspecified**: Pharma-Speak is described as "an open source dataset which had about 600 medication names prescribed globally with their trade names which we curated ourselves" (Section 4.1). Since the pipeline uses Whisper to generate N-best hypotheses from audio, the dataset must consist of audio recordings, but the paper provides: no information on whether clips are single words, phrases, or sentences; no recording conditions; no speaker demographics or accent diversity; no noise profile; no sampling rate; and no description of how audio was paired with ground-truth text. Without these details, the results cannot be interpreted or reproduced.

- **Incomplete and uninterpretable results table**: Table 1 shows only 4 of 15 epochs (epochs 7, 9, 11, 13) with no explanation of why these particular epochs were selected, why epoch 9 exhibits a large spike (25.10), and no error bars, confidence intervals, or run-to-run variance. A single run with no variance metrics cannot support any statistical conclusion.

### Minor

- **Model name inconsistency**: The abstract states "LLaMA 3" while Section 4.1 lists "Llama-2-8b Instruct model." These are different models with different architectures and capabilities. The paper's core experimental setup is ambiguous.

- **Vague method description**: Section 3 describes the approach as "second-pass rescoring" but Figure 1 shows the LLM generating a "Corrected Hypo" (a generated output), which is closer to generative error correction than rescoring. No prompt template, loss function, or training objective is described. It is unclear whether the LLM scores/re-ranks the N-best list or generates a new transcription from scratch.

- **Novelty claim is not well-supported**: The paper states "to the best of our knowledge, this is the first of its kind done within the medication name domain" but the cited related work (Hyporadise, Whispering LLaMa) already performs LLM-based ASR error correction in other domains. The contribution is incremental (applying an existing paradigm to a new domain) and the paper does not identify what domain-specific technical challenges were addressed beyond the data change.

### Trivial

- Table 1 column header "Result" should specify the metric being reported.

## Nice-to-Haves

- Adding a simple n-gram LM rescoring baseline would help isolate the benefit of the LLM rescoring component.
- Reporting WER alongside ROUGE (or instead of ROUGE) would align with the paper's stated claims and community norms for ASR evaluation.
- Clarifying the dataset description (audio duration, recording conditions, speaker diversity) would significantly strengthen reproducibility.

## Removed Points

- **"Demonstrated WER reduction over ASR baseline"** (Strength Finder #1): Removed because the paper does not actually report WER (it reports ROUGE) and the baseline "21%" is not from the same controlled experiment. This claimed strength is contradicted by the paper's own evidence.
- **"Creation and use of a custom medication-name dataset"** as a core strength: Downgraded from strength; the dataset is too vaguely described to count as a demonstrated contribution.
- **Generic strengths about problem importance and task relevance**: Removed as they are not specific, evidence-grounded strengths of this paper's execution.
- **Criticism about missing related work**: Removed per instruction — no external verification possible.
- **Reproducibility concerns about hyperparameters**: Removed as these are addressed in Section 4.1.
- **Criticism about missing appendix content**: Removed per instruction — appendices are stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same structural problems the paper exhibits without revealing any hidden strength or unexpected pattern.

## Suggestions

1. **Conduct a controlled experiment**: Report WER on the Pharma-Speak test set for (a) Whisper-Large-v3 alone, (b) Whisper + a simple n-gram LM rescoring, and (c) Whisper + LoRA-tuned LLM rescoring. This is the minimal experiment needed to support the claimed contribution.
2. **Align claims with evaluation**: Either use WER as the evaluation metric (and report it) or change the abstract and conclusion to claim ROUGE-based improvement instead of WER reduction.
3. **Provide a datasheet for Pharma-Speak**: Describe the audio data format, recording conditions, speaker demographics, and how audio clips are paired with ground-truth transcriptions.
4. **Clarify the LLM identity** (Llama-2 vs. LLaMA 3) throughout the paper.
5. **Report results with variance**: Run the experiment multiple times or provide bootstrap confidence intervals.

## Score and Decision

**Anchors used for calibration:**

| Path | Avg Human Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews/fnBYPL5Ged.md | 2.00 | 1 (low) | Worse — CPLLM had a cleaner if weak evaluation; this paper's evaluation is fundamentally broken |
| /home/wg25r/review_agent/human_reviews/JiWlVYB4rh.md | 3.00 | 1 (low) | Slightly worse — EchoQA at least had a clear dataset contribution; this paper's dataset is underspecified |
| /home/wg25r/review_agent/human_reviews/K1bv86Uvbp.md | 3.00 | 1 (low) | Similar rigor level — both have significant gaps but this paper's claims are less substantiated |
| /home/wg25r/review_agent/human_reviews/oBmaLuEJda.md | 3.00 | 1 (low) | Similar — both have plausible ideas but weak evaluation |
| /home/wg25r/review_agent/human_reviews/QqjFHyQwtF.md | 6.60 | 1 (mid) | Much stronger — that paper had thorough baselines, ablations, and statistically sound experiments |
| /home/wg25r/review_agent/human_reviews/LrmPGtnros.md | 6.75 | 1 (mid) | Much stronger — HAINAN had rigorous evaluation across multiple datasets |
| /home/wg25r/review_agent/human_reviews/aOPTDchLBz.md | 2.50 | 2 (narrow) | Slightly stronger — ivrit.ai had a real 10k-hour dataset contribution but was still rejected |
| /home/wg25r/review_agent/human_reviews/2CxkRDMIG4.md | 1.50 | 2 (narrow) | Worse — that paper had a fundamentally flawed framing; this paper at least has a plausible idea |
| /home/wg25r/review_agent/human_reviews/AUi9y7wJBN.md | 3.75 | 2 (narrow) | Stronger — pronunciation-lexicon paper had solid methodology and experiments despite other issues |

**Round-1 bracket**: (1.5, 3.5). **Round-2 narrowing**: After comparing against the most similar low-scoring anchors, the paper sits at the lower end of this band — it has a plausible idea but the evaluation is fundamentally broken (metric mismatch, no controlled baseline, underspecified dataset). The paper is weaker than ivrit.ai (2.5) which at least had a clear tangible contribution, and much weaker than mid-band papers (3.5–7.5) which had sound evaluation.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>