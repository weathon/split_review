Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper addresses the disconnect between neural audio codec design and language model (LM) training in codec-LM systems for TTS and audio generation. It proposes three complementary co-design techniques: (1) a framewise codec encoder that removes overlapping receptive fields to improve downstream LM modeling, (2) LM codebook level dropout (CL drop) to efficiently tune the number of RVQ levels used during LM training, and (3) increasing codec frame duration (with compensating codebook size adjustments) to approximately double inference speed. The combined system achieves improvements in intelligibility, audio quality, and speaker control while nearly doubling inference speed relative to a siloed baseline.

## Strengths

- **Framewise encoder yields consistent end-to-end gains.** The paper shows that removing overlapping receptive fields in the codec encoder improves LM negative log-likelihood by over 8% and consistently beats the causal baseline on all end-to-end TTS metrics (intelligibility, audio quality, speaker control) and unconditional music FAD (Table 1). This is a novel, non-obvious co-design insight — the framewise encoder _hurts_ codec reconstruction but _helps_ the LM, and the net effect on end-to-end TTS is positive.

- **CL drop is a practical technique for efficient hyperparameter tuning.** Training 12 individual LMs to find the optimal number of RVQ levels is prohibitively expensive; CL drop trains a single LM that can be evaluated at any level count. The paper validates that CL drop's performance profile tracks individually trained LMs (Figure 3), a practically useful contribution that directly reduces the cost of navigating the codec-LM design space.

- **Doubling frame duration yields meaningful inference speedup with comparable quality.** The paper shows that increasing frame duration from 11ms to 22ms with appropriate codebook size adjustments yields roughly 2× inference speedup with no degradation in WER, NISQA, or speaker similarity (Table 2). This directly links a codec hyperparameter to LM efficiency in a practically actionable way.

- **The combined system demonstrates that co-design strategies are complementary and synergistic.** Applying all three techniques together (Table 3) achieves doubled inference speed while improving all end-to-end TTS metrics over a strong non-causal baseline, showing that the individual interventions do not conflict and can be deployed jointly.

- **Clear identification of the non-monotonic effect of RVQ levels on end-to-end performance.** Figure 2 sharply contrasts the monotonic improvement of codec reconstruction with the peaked end-to-end TTS performance (optimal at 9 levels), providing compelling motivation for both the CL drop technique and the broader co-design framing.

## Weaknesses

### Fatal
None.

### Major

- **CL drop's tracking property is validated on music generation, but all TTS experiments rely on it.** The paper demonstrates that CL drop's performance profile across different RVQ level counts tracks that of individually trained LMs using unconditional music generation (Figure 3, FAD metric). However, every TTS experiment in the paper that involves tuning Q′ (Tables 2 and 3) uses CL drop without task-specific validation that the tracking property holds for TTS. Music and TTS have fundamentally different codec and LM characteristics (e.g., rhythmic vs. phonetic structure, conditioning inputs), so this gap is non-trivial. Without knowing whether CL drop's TTS performance profile matches individually trained LMs, the reported TTS results carry unaccounted-for uncertainty. The paper does not acknowledge this limitation. *This is fixable (e.g., by training a small number of individual LMs for TTS at selected Q′ values to verify the trend) but as presented, it undermines the strength of claims that rely on CL drop for TTS.*

- **The dropout distribution 𝒫(q) used in CL drop experiments is not specified.** Section 4.2 correctly notes that the choice of 𝒫(q) is "critical" for preserving the performance trends, and Figure 3 shows that a non-uniform distribution works better than uniform. Yet the paper never states which specific distribution was used in the TTS experiments (Tables 2, 3). This is a reproducibility gap — without this detail, other practitioners cannot replicate the results, and the reader cannot assess whether a suboptimal distribution choice could be inflating or deflating the reported metrics.

### Minor

- **The inference speedup claim would benefit from a profiling breakdown.** Table 3 reports a substantial system-level speedup, attributed primarily to halving the LM sequence length via increased frame duration. However, no analysis disentangles the contributions from the LM itself, the codec's reduced frame rate, the framewise encoder's impact, or any other factors. The hardware, batch size, and measurement methodology (e.g., whether it includes full codec encode + LM sampling + codec decode) are also absent. While this does not invalidate the speedup claim, it makes the result harder to interpret and reproduce.

- **The combined system (Table 3) lacks a controlled ablation that isolates CL drop's contribution.** The full system uses CL drop, while the siloed baseline uses an individually trained LM at a fixed Q′. This confounds the codec changes with CL drop's effect. A cleaner comparison would include an ablation where the full system uses an individually trained LM at the optimal Q′ (e.g., Q′=9 from Figure 2), so the reader can see how much of the gain comes from codec changes vs. from better level selection via CL drop.

- **No human listening test is reported.** The paper relies on NISQA as a proxy for audio quality. While NISQA is shown to correlate well with human judgments, the framewise encoder degrades codec reconstruction (Mel-L1). A small-scale human evaluation would strengthen the claim that end-to-end TTS quality genuinely improves despite the worse reconstruction.

### Trivial
- The abstract states "doubled inference speed" as an exact figure, while the combined speedup in Table 3 is approximately 2.9×. The discrepancy is minor (the claim is approximately correct) but could be clarified with "approximately" or "nearly doubled."
- The paper references a footnote (footnote 4 about the choice of 𝒫(q) being "critical") that appears to have been deferred to an appendix or supplementary, which is stripped by the parser. If this detail exists in the appendix, it should be in the main text for reproducibility.

## Nice-to-Haves
- Validate CL drop on TTS by training a small number of individual LMs at selected Q′ values (e.g., Q′ = 6, 9, 12) and comparing their end-to-end metrics to CL drop's.
- Profile inference speed by component (codec encode, LM sampling steps, codec decode) to clarify where the speedup originates.
- Analyze whether framewise codes have lower entropy or better structure (e.g., separability) that explains why the LM finds them easier to model.
- Provide qualitative examples (spectrograms or audio samples) comparing TTS outputs from the baseline and full system, particularly for speaker control.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper:

- *Criticism about codec training on YouTube podcasts while evaluation uses LibriTTS-R*: The paper is transparent about this mismatch, it is a common practical choice, and it does not bias comparisons since all compared codecs were trained on the same data.
- *"All-frame" row in Table 1 not being a sensible baseline*: The paper includes it as an ablation to isolate the effect of framewise encoding vs. framewise decoding, which is useful for understanding.
- *Request for larger dataset or more models*: The current scale (1.7K hours codec training, 550 hours LM training) is already substantial for a method-development paper.
- *Criticism of missing appendix or proofs*: These are parser-stripped; they exist in the original submission.
- *Complaint about "not yet released" code/weights*: The paper explicitly states intent to open source upon publication, which is standard.
- *Pure formatting/typo nitpicks*: These are parser artifacts.

## Novel Insights

Beyond the paper's own contributions, a notable observation emerging from the reviews is that the framewise encoder result — where degrading codec reconstruction metrics actually *improves* end-to-end TTS — challenges a deeply ingrained assumption in the field. This suggests that the standard practice of optimizing codecs solely for reconstruction fidelity may be actively harmful for downstream generation tasks, and opens a potentially rich line of inquiry into what properties of a codec's latent space (e.g., temporal locality, information distribution across frames) matter most for language modeling. The non-monotonic relationship between RVQ level count and end-to-end performance (Figure 2) further reinforces this point: more information (more levels, better reconstruction) does not linearly translate to better generation.

## Suggestions

1. **Most critically**: Validate CL drop for TTS — either by training a few individual TTS LMs at different Q′ values to verify the tracking trend, or by explicitly acknowledging the limitation and reporting results with individually trained LMs as a control. Without this, the TTS results in Tables 2 and 3 rely on an unvalidated assumption.

2. **Specify 𝒫(q)** for reproducibility. State which dropout distribution was used in all experiments, even if the choice was heuristic.

3. **Add a controlled ablation in Table 3**: Compare the full system (framewise + CL drop + 22ms) against the full system with an individually trained LM at the best Q′ (e.g., Q′=9) to isolate CL drop's contribution from the codec changes.

4. **Clarify inference speed measurement methodology** (hardware, batch size, whether it includes full pipeline) and ideally provide a component-level breakdown.

## Score and Decision

This paper makes a solid contribution by proposing and evaluating concrete, architecture-agnostic co-design strategies for neural codec LMs. The framewise encoder is the most convincing and well-supported technique — it is simple to implement, grounded in clear reasoning, and delivers consistent gains. The frame-duration analysis is practically useful and likely to influence how practitioners configure codec-LM systems. The primary weakness is that CL drop — used in all TTS experiments — lacks task-specific validation of its tracking property, introducing uncertainty into some of the reported results. This is an addressable gap, not a fatal flaw. The paper's core contributions (framewise encoder, co-design framing, frame-duration analysis) stand on their own.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>