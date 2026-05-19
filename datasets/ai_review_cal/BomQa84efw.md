- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 5, 3, 5, 6
Now I have a thorough understanding of the paper and all the reviewer claims. Let me cross-check each against the actual text and produce the consolidated review.

---

## Summary

This paper proposes **dMel**, a speech tokenization method that discretizes log mel-filterbank energies into uniform ordinal bins using dataset-wide min/max ranges — requiring no encoder, no learned codebook, and no residual vector quantization. The authors evaluate dMel within a decoder-only transformer (LM-style) on ASR and TTS tasks, comparing against HuBERT-KM and SpeechTokenizer. The core finding is that this simple, training-free discretization achieves competitive or better WER on both tasks while dramatically simplifying the tokenization pipeline.

## Strengths

- **Training-free tokenization achieves the best WER among compared tokenizers in an LM architecture.** dMel requires no pretrained encoder or vector quantization, yet in the unified decoder-only transformer it achieves the lowest WER on both ASR (test-clean 4.2% vs HuBERT+KM 5.8% and SpeechTokenizer 6.9%, Table 5) and TTS (WER 4.3% vs 9.5% and 11.4%, Table 4). Table 2 explicitly marks dMel as training-free while the others require pretraining.

- **Discretization negligibly impacts acoustic and semantic information.** Table 1 (tab:teaser) shows that ASR WER on waveforms reconstructed from dMel is nearly identical to that from continuous Mel (e.g., 2.23% vs 2.13% with P-WaveGAN), and ASR models trained directly on dMel versus Mel yield similar WER (2.5% vs 2.4% for seq2seq). This directly supports the claim that discretization preserves both acoustic and semantic content.

- **Independent channel-level prediction simplifies the modeling architecture.** Section 2.2 notes that "all frequency channels at time frame t for dMel tokenizer are predicted independently and in parallel," avoiding the coarse-to-fine hierarchical dependencies required by RVQ-based acoustic tokens. This architectural simplicity is a genuine advantage.

- **Honest ablation isolates the source of ASR performance degradation.** Table 7 (tab:asr-ablation) decomposes the WER gap between the LM-style model and strong CTC/Seq2Seq baselines, showing that switching from Mel to dMel causes only small degradation (e.g., CTC dev-clean 2.1%→2.3%), while switching from CTC to the LM-style architecture causes the large drop (2.3%→3.4%). This diagnostic analysis confirms that dMel itself is not the bottleneck.

- **Lightweight vocoder achieves competitive reconstruction quality.** dMel with a 1M-parameter ParallelWaveGAN vocoder at 40Hz (Table 3) attains WER 2.51%, comparable to SpeechTokenizer (99M total params, WER 2.41%) and EnCodec (14M params, WER 2.03%), while using far fewer parameters.

## Weaknesses

### Fatal
None.

### Major
- **The joint speech-text model severely degrades ASR, but the abstract overstates this as a success.** The core advertised benefit of dMel (beyond the tokenization itself) is enabling a single model for both ASR and TTS. However, Table 8 shows that in the joint model, ASR WER degrades from 4.2%→7.6% (test-clean) and from 10.4%→20.0% (test-other), while TTS is essentially unchanged (4.3%→4.4%). The abstract states that dMel "pave[s] the way for efficient and effective joint modeling of speech and text" — but the presented evidence shows the joint model is largely non-functional for ASR. The conclusion appropriately acknowledges this ("further work is needed"), but the abstract and some framing (Section 3.6 title: "Unlocking Joint Speech-Text Modeling") overstate the result. This does **not** invalidate the paper's core contribution (the dMel tokenization itself is separately validated), but it narrows the significance: dMel is primarily a strong tokenizer for *separate* ASR or TTS models, not a demonstrated solution to joint modeling.

### Minor
- **The abstract's superiority claim lacks the architectural caveat present in the body.** The abstract claims dMel "performs better than other existing speech tokenization methods" without qualification. In the body, the comparison is explicitly within a single LM-style architecture — a setting that naturally disadvantages residual-quantization-based tokenizers (which are designed for coarse-to-fine AR+NAR pipelines). The paper transparently acknowledges this (e.g., the SpeechTokenizer AR-only model gets 11.4% WER vs its intended 6.5% AR+NAR setup), so the criticism is not about dishonesty but about framing that outruns the evidence.

- **Evaluation is limited to clean, studio-quality data.** All experiments use LibriSpeech and related clean datasets. The paper itself identifies "improving generalization to low-resource / out-of-domain data" as a key open challenge (Related Work, point iii) but does not test dMel on noisy speech, different microphone conditions, or low-resource settings. While this does not invalidate the in-domain results, it limits the practical significance of the finding that a globally-normalized discretization (using dataset-wide min/max) works well.

### Trivial
- The paper does not report training time or inference speed comparisons, even though dMel's simpler tokenization and 40Hz frame rate likely offer practical efficiency advantages that would be useful to quantify.
- TTS WER results in Tables 4, 6, and 9 lack confidence intervals or error bars, unlike the ASR results which do report them.

## Nice-to-Haves

- Test dMel on at least one out-of-domain or noisy dataset (e.g., CommonVoice with varied recording conditions) to assess whether the dataset-wide min/max discretization generalizes.
- Analyze whether there is any benefit to modeling cross-channel dependencies (e.g., a small linear projection across frequency channels) — this would either validate or refine the independence assumption.
- Report inference speed and training time relative to baselines.
- The joint modeling experiment could be improved with text-only pretraining, as the authors speculate. A brief diagnostic (e.g., is the ASR degradation due to data imbalance, modality competition, or architecture) would strengthen the paper.

## Removed Points

*These points were flagged by reviewers but are removed for the following reasons:*

1. **"Comparison is staged in an architecture that disadvantages them"** — The paper transparently uses the same LM architecture for all tokenizers and explicitly notes that SpeechTokenizer achieves 6.5% WER in its native AR+NAR setup vs 11.4% in the AR-only setup. The comparison is fair for the paper's stated purpose (evaluating tokenizers within a single-stage LM). The real issue is just the abstract's unqualified phrasing, which is already captured as a Minor weakness above.

2. **"The method's simplicity raises a significance question"** — This is a subjective assessment of scope, not a concrete weakness. Every paper has scope boundaries. The finding that a trivial discretization works well is itself the non-obvious contribution.

3. **"No statistical significance reported"** — Partially false. ASR results in Table 5 include confidence intervals. TTS results lack them, but this is standard practice for automatic WER evaluations on fixed test sets.

4. **"Speaker embedding d-vector details missing"** and **"Span masking details vague"** — Likely in the appendix, which is stripped by the parser. Per instructions, missing appendix content should not be penalized.

5. **"Codebook size — why 16?"** — The paper discusses the trade-off in Section 3.4 (Table 6 ablation), noting that 16 bins performs best overall, with plausible explanations for the degradation at 8 and 32 bins.

6. **Strength: "Joint speech-text modeling is demonstrated as a viable direction"** — This conflicts with the verified weakness (joint model ASR degrades severely). Per instructions, weakness wins; this strength is dropped.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a trivial uniform quantization of mel-filterbanks works as well or better than sophisticated learned tokenizers in a decoder-only LM — is already the paper's central contribution. The reviews do not surface any additional unarticulated insight.

## Suggestions

1. **Temper the abstract's wording.** Replace "performs better than other existing speech tokenization methods" with a qualified statement such as "within a single decoder-only transformer, dMel achieves competitive or better ASR and TTS performance compared to other tokenization methods while requiring no training."

2. **Either remove the joint modeling claim from the abstract and introduction, or reframe it explicitly as preliminary work.** The joint model's severe ASR degradation (4.2%→7.6% test-clean, 10.4%→20.0% test-other) means it does not support the "effective joint modeling" narrative. The conclusion already handles this honestly — the abstract should follow suit.

3. **Add confidence intervals to TTS WER results** (Tables 4, 6, 9) to match the ASR reporting standards used elsewhere.

4. **Report training/inference speed** to quantify the efficiency advantage of dMel's simpler tokenization and lower frame rate.
