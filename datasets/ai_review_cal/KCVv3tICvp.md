- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper identifies a gap in the siloed development of audio codecs and language models for TTS, and proposes three codec-LM co-design techniques: (i) a framewise codec encoder that avoids overlapping receptive fields, improving LM log-likelihood (>8%) and end-to-end metrics; (ii) LM codebook level dropout (CL drop), which trains a single LM to evaluate all RVQ level counts efficiently; and (iii) longer frame durations that double inference speed without degrading quality. Experiments on a modified DAC codec with a Mamba2+Transformer LM show that combining all three techniques yields simultaneous gains in speed and quality relative to a causal siloed baseline.

## Strengths

- **Framewise encoder is a simple, elegant, and effective intervention.** The observation that overlapping receptive fields in the codec encoder are detrimental to the downstream LM, and the proposed fix of reshaping waveform inputs before the encoder (requiring no architectural changes, as noted in Sec. 4.1), is well-motivated by the paper's analysis of the encoder–decoder asymmetry. Table 1 shows consistent improvements across all end-to-end metrics.

- **CL drop is a practical method for a real hyperparameter tuning problem.** The paper demonstrates (Fig. 2) that the optimal number of RVQ levels for end-to-end performance differs from the codec-only reconstruction optimum, and that CL drop tracks the performance of 12 separately trained LMs using a single training run. This is a concrete efficiency gain for practitioners.

- **Longer frame duration finding yields actionable co-design insight.** The paper shows that doubling frame duration (11ms → 22ms) while adjusting codebook size to maintain bitrate can double inference speed while preserving TTS quality (Table 2). This is a practical result with clear engineering implications.

- **All three techniques are complementary and combine well.** Table 3 demonstrates that the combined system achieves both speed gains and quality improvements, showing the three proposals are additive rather than conflicting.

- **Systematic investigation of multiple codec hyperparameters in a co-design context.** Unlike prior work that treats the codec as fixed, the paper jointly studies frame duration, codebook size, number of RVQ levels, and receptive field structure, painting a more complete picture for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **No comparison against any external TTS system.** The paper evaluates all proposed methods only against its own siloed baselines (Non-causal, Causal, All-frame, Framewise — all variants of the same modified DAC codec). No comparison is made to any published TTS system (e.g., VALL-E, VoiceBox, NaturalSpeech 3, or any codec-LM baseline from the literature). This limits assessment of whether the co-design principles generalize to competitive systems. While the paper's claims are framed as relative improvements, the lack of any external anchor means a reader cannot judge whether these techniques would produce meaningful gains in a state-of-the-art context. The paper would be significantly strengthened by at least one comparison to a published system on the same metrics.

### Minor

- **CL drop distribution $\mathcal{P}(q)$ is never specified.** The paper defines the dropout distribution $\mathcal{P}(q)$ (Sec. 4.2, Equation 4) and states "the choice of $\mathcal{P}(q)$ is critical in preserving the trends" (line 114), but never reveals what distribution was actually used in experiments. Was it uniform over $\{1,...,Q\}$? Skewed toward lower levels? Tuned on a validation set? This is a genuine reproducibility gap — the core CL drop technique cannot be independently replicated without this detail.

- **No ablation of the combined system.** Table 3 evaluates all three techniques together but does not isolate the contribution of each individual technique in the combined setting. An ablation (e.g., full system vs. framewise-only, CL-drop-only, longer-frames-only) would clarify whether the gains are additive, synergistic, or dominated by a single technique.

### Trivial

None.

## Nice-to-Haves

- Testing on additional codec architectures (e.g., EnCodec) would help demonstrate that the co-design principles are not DAC-specific.
- An explicit discussion of the gap between the paper's absolute performance and published TTS systems, even if no direct comparison is added, would help readers calibrate the significance of the findings.
- Adding error bars or statistical significance tests for key comparisons would strengthen the quantitative claims.

## Removed Points

These points were considered but removed after verification against the paper:

1. **"Non-causal codec achieves best FAD but paper doesn't discuss it"** — REMOVED (factually incorrect). The paper explicitly states at line 161 that Non-causal "achieves strongest performance in all aspects" but is "not low-latency streamable." The comparison of interest is between Causal and Framewise (both streamable), and the paper is clear about this scope.

2. **"No ablation of LM architecture (Mamba2+Transformer)"** — REMOVED (strawman). The paper cites external validation that hybrid SSM+attention outperforms either approach alone (Waleffe et al., 2024; Hatamizadeh & Kautz, 2024). This is sufficient justification; an additional ablation would add little.

3. **"Statistical significance / stdev not reported in text"** — REMOVED (parser artifact). The paper states "Stdev over 5 runs follow ±" at Table 1 (line 139). The actual values are in the table image, which the parser stripped. The paper reports variance; this is a rendering issue.

4. **"Missing appendix / figures / tables"** — REMOVED (parser artifact). The paper references Fig. 3, Tables 2–3, which are images not rendered by the parser. They exist in the original submission.

## Novel Insights

A genuinely novel observation emerges from synthesizing both reviews: the paper identifies a fundamentally asymmetric effect of overlapping receptive fields in the codec encoder versus decoder — helpful for reconstruction (decoder side) but harmful for downstream language modeling (encoder side). This framing reframes a standard architectural choice as a co-design liability, and the proposed fix (reshaping inputs, not changing architecture) is elegant. This encoder–decoder asymmetry insight goes beyond any single technique and could inform future codec designs more broadly.

## Suggestions

1. **Specify the CL drop distribution** used in experiments — this is the single most actionable fix for reproducibility.
2. **Add at least one external TTS baseline comparison** (e.g., VALL-E or a SpeechTokenizer-based system) on WER, NISQA, and speaker similarity on LibriTTS-R test-clean. This would substantially raise the paper's impact.
3. **Include an ablation study** of the combined system (Table 3) to show each technique's marginal contribution.
