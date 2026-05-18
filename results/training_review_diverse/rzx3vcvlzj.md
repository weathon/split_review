Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper introduces TIGER, a time-frequency domain speech separation model that achieves extreme parameter efficiency (0.82M parameters, 94.3% reduction vs TF-GridNet) through frequency band-split, multi-scale selective attention (MSA), and full-frequency-frame attention (F³A). It also contributes EchoSet, a dataset with realistic reverberation (including object occlusions and material properties from Matterport3D) and random overlap. On EchoSet, TIGER (large) reaches 14.22 dB SDRi, surpassing TF-GridNet's 13.73 dB. The paper demonstrates that models trained on EchoSet generalize better to real-world recordings than those trained on Libri2Mix or LRS2-2Mix.

## Strengths

- **Extreme parameter and MAC reduction while exceeding SOTA on the most realistic dataset.** TIGER (large) achieves 14.22 dB SDRi on EchoSet, surpassing TF-GridNet's 13.73 dB, while reducing parameters by 94.3% (0.82M vs. 14.43M) and MACs by 95.3% (15.27 G/s vs. 323.75 G/s). This directly supports the core claim of a lightweight model that beats SOTA on complex, realistic data (Tables 1, 2).

- **EchoSet demonstrably narrows the gap to real-world audio.** Models trained on EchoSet produce higher-quality separated speech on real-world recordings than those trained on Libri2Mix or LRS2-2Mix (Figure 2). The dataset's design—room/object materials, same-acoustic-scene mixing, random overlap—provides a more faithful training environment than prior benchmarks (Table 1 in paper).

- **Band-split with low-frequency prioritization reduces computational load while improving performance** compared to no split (NonSplit) or even split. LowFreqNarrowSplit achieves SDRi 13.15 dB with 7.65 G/s MACs, versus NonSplit's 11.53 dB with 40.89 G/s MACs (Table 3), validating the prior-knowledge-guided compression strategy.

- **The MSA and F³A modules are more efficient than alternative sequence-modeling structures (LSTM, Mamba, SRU) while maintaining competitive performance.** Ablations show removing either module degrades performance (Table 4), and replacing them with LSTM/Mamba/SRU substantially increases parameters and MACs without consistent performance gain (Tables 5, 6).

- **First sub-1M parameter speech separation model to rival SOTA on challenging, reverberant conditions.** TIGER (small, 0.82M params) achieves only 0.6 dB SDRi below TF-GridNet on EchoSet (13.15 vs. 13.73 dB), while all other models have ≥2.3M parameters (Tables 1, 2). This is a genuinely novel efficiency result.

## Weaknesses

### Fatal
None.

### Major

- **Weak empirical validation of EchoSet's generalization claim.** The paper argues that EchoSet-trained models generalize better to real-world conditions, but the real-world test set is described only as "10 real-world environments and recording audio from 40 speakers from the LibriSpeech test set" with no information about the number of test mixtures, acoustic properties of those environments, recording equipment, or statistical uncertainty. Results are shown only as a figure (Figure 2) without numerical values, standard deviations, or per-utterance distributions. With an uncharacterized test set, the claim that EchoSet-trained models "generalized better" is suggestive but not convincing. This weakens one of the paper's two main contributions, because the real-world generalization advantage of EchoSet over LRS2-2Mix and Libri2Mix is not reliably established. The paper would benefit from reporting exact numerical results, confidence intervals, and more detail about the test environment.

### Minor

- **Missing STFT parameters.** The paper does not state the STFT window size, hop size, or FFT size anywhere. While $F=321$ can be inferred from the NonSplit scheme (321 sub-bands = 321 frequency bins), the actual STFT configuration is essential for reproducibility and for interpreting the band-split design. This should be reported.

- **No variance or multi-run statistics.** All performance numbers (Tables 1, 3, 4, 5, 6) appear to be single-run results. Speech separation models can exhibit non-trivial variance across runs. The key comparison on EchoSet (TIGER large 14.22 vs. TF-GridNet 13.73 SDRi) involves a margin where knowing statistical reliability matters. While single-run reporting is common in the field, the paper's claims about surpassing SOTA would be stronger with multi-run statistics.

- **Ambiguity about the real-world test mixing method.** The paper says the real-world test follows "the same mixing method as LRS2-2Mix" but does not clarify whether the mixing method (gain, overlap ratios) differs from EchoSet's generation pipeline. This matters for interpreting Figure 2, since the test data's resemblance to either EchoSet or LRS2-2Mix affects what the comparison actually shows.

- **F³A module's scalability to longer utterances is not discussed.** The F³A module merges the time dimension $T$ into the channel dimension ($E \times T$) for self-attention over $K$ sub-bands. When $T$ is large (e.g., >300 frames for longer utterances), the attention map computation involves a matrix of size $K \times (E \times T)$, which could become computationally heavy. The paper should discuss how this scales to utterances beyond 6 seconds.

### Trivial

- **Band-split ablation comparison between NormalSplit (47 sub-bands) and LowFreqNarrowSplit (67 sub-bands) is confounded by both $K$ and split design.** However, the key comparison that supports the paper's claim (LowFreqNarrowSplit vs. EvenSplit, both at 67 sub-bands) cleanly isolates the split strategy. This is a minor presentational issue, not a flaw in the conclusion.

## Nice-to-Haves

- Providing an acoustic analysis of EchoSet (RT60 distributions, direct-to-reverberant ratios) compared to WHAMR! and LRS2-2Mix would strengthen the "high-fidelity" claim beyond the single real-world test.
- A brief survey of sub-1M parameter separation models (e.g., very small Conv-TasNet variants) in the related work would contextualize the claim of being the first sub-1M model to rival SOTA.
- Reporting per-utterance SDRi distributions (box plots or histograms) for the key comparisons would help assess whether improvements are consistent or driven by a small subset of examples.
- The overlap ratio distribution in EchoSet would be useful for understanding dataset characteristics.

## Removed Points

- **"Surpassing SOTA" framing criticism** — The reviewer claimed the abstract and introduction frame TIGER as "uniformly surpassing SOTA," but the abstract explicitly scopes the claim: *"On EchoSet and real-world data, TIGER significantly reduces... while achieving performance surpassing state-of-the-art (SOTA) model TF-GridNet."* The introduction similarly scopes it to EchoSet (line 31). The paper already qualifies this correctly; the body properly explains the regression on simpler benchmarks. This criticism misreads the paper.

## Novel Insights

The reviews collectively highlight a pattern that is not explicit in the paper itself: TIGER's design philosophy — using prior knowledge about speech frequency distribution (band-split with narrower low-frequency bands) combined with interleaved frequency/time attention — creates a model whose *relative* advantage grows precisely where existing models struggle most (complex reverberation, real-world acoustics). On simple anechoic benchmarks, TIGER is merely competitive; on realistic data, it pulls ahead while being orders of magnitude cheaper than TF-GridNet. This suggests the community's standard evaluation protocol (Libri2Mix/WSJ0-2mix) may systematically underreward architectures designed for real-world deployment. The EchoSet dataset, even with its limited real-world validation, represents a step toward addressing this evaluation gap, and the weakness identified in the real-world validation points to exactly where future work should invest: larger, well-characterized real-room test sets.

## Suggestions

1. **Strengthen the real-world validation**: Report exact numerical values from Figure 2, add error bars (or at least standard deviation across test utterances), and provide more detail about the 10 environments (room sizes, RT60 ranges, microphone placement). This is the single most impactful improvement.
2. **Report STFT parameters** (window size, hop size, FFT size) explicitly in the experimental setup for reproducibility.
3. **Add multi-run statistics** for the main comparisons (at minimum, TIGER vs. TF-GridNet on EchoSet) to establish that the 0.49 dB SDRi gap is statistically reliable.
4. **Clarify the real-world test mixing protocol** — whether it follows EchoSet's or LRS2-2Mix's pipeline — to remove ambiguity about what Figure 2 actually compares.
5. **Discuss F³A scalability** to longer utterances, or add a note about the typical frame count used in experiments.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>