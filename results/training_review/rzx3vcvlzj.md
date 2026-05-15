Now I have a thorough understanding of the paper and can verify each reviewer claim against the source text. Let me compile the final review.

## Summary

This paper presents TIGER, a lightweight time-frequency speech separation model built on frequency band-splitting, multi-scale selective attention (MSA), and full-frequency-frame attention (F³A), along with EchoSet, a simulated dataset with realistic reverberation (accounting for object occlusions and material properties via SoundSpaces 2.0 and Matterport3D). TIGER achieves 0.82M parameters (94.3% fewer than TF-GridNet), 15.27 G/s MACs (95.3% reduction), and surpasses TF-GridNet on EchoSet (14.22 vs 13.73 dB SDRi), while models trained on EchoSet show improved generalization to a real-world test set.

## Strengths

- **Drastic efficiency gain with maintained/improved performance on complex data**: TIGER (large) uses 0.82M parameters and 15.27 G/s MACs versus TF-GridNet's 14.43M and 323.75 G/s — reductions of 94.3% and 95.3% — yet achieves higher SDRi on EchoSet (14.22 vs 13.73 dB) and competitive performance on Libri2Mix and LRS2-2Mix (Tables 1–2). The parameter-efficient design is genuinely novel and well-motivated: the band-split strategy compresses frequency information using prior knowledge about speech frequency distributions, and the interleaved time-frequency processing is a clean architectural contribution.

- **Comprehensive ablation studies validate each module**: Tables 4–7 systematically isolate the contributions of the band-split strategy (NonSplit vs. LowFreqNarrowSplit: 11.53→13.15 dB SDRi with 81% MACs reduction), MSA module (removing MSA drops SDRi from 13.15 to 7.58 dB), and F³A module. The comparisons replacing MSA/F³A with LSTM, Mamba, and SRU show that the proposed modules offer competitive performance with substantially lower computational cost (e.g., MSA: 7.65 G/s vs. LSTM: 49.38 G/s, Table 6).

- **EchoSet introduces a more principled reverberation simulation**: Unlike WHAMR! (rectangular rooms only) or LRS2-2Mix (mixing recordings from different scenes), EchoSet uses SoundSpaces 2.0 with Matterport3D scenes to simulate reverberation that accounts for object occlusions, material properties, and non-rectangular room geometries, with random overlap ratios (Section 4). This is a meaningful step toward more realistic training/evaluation conditions.

- **Generalization evidence across domains**: The cinematic sound separation results, though sketchily reported, and the consistent trend across three datasets of increasing difficulty (Libri2Mix → LRS2-2Mix → EchoSet) both support the architecture's broad applicability.

## Weaknesses

### Fatal
None.

### Major

- **The real-world evaluation is critically underspecified, weakening the EchoSet generalization claim.** The paper states only: "selecting 10 real-world environments and recording audio from 40 speakers from the LibriSpeech test set" and "followed the same mixing method as LRS2-2Mix" (Section 5). Critical details are missing: (1) Were the recordings made by playing back audio through a loudspeaker and re-recording, or by having human speakers read the utterances? (2) What were the 10 environments, and were they held out from EchoSet? (3) Results are shown only as a bar chart (Figure 1) without numeric values, error bars, or sample sizes. The claim that "EchoSet bridges the gap to real-world applications" rests heavily on this evaluation, yet it cannot be reproduced or properly assessed. At minimum, the recording procedure needs full specification, and numeric results with error bars should be reported. The paper would be significantly strengthened by evaluating on an independent published real-world corpus (e.g., CHiME-3 or WHAMR! real recordings).

- **Cinematic sound separation results lack experimental detail.** The paper reports that TIGER achieves a "39.4% increase of SDR in performance" over BSRNN with 97.3% fewer parameters and 77.6% fewer MACs, but provides no dataset description, no table, no evaluation protocol, and no information about the BSRNN baseline source. This is a substantial claim presented as an afterthought in a single sentence. Either remove it or provide proper experimental backing (dataset size, composition, evaluation metrics, and comparison table).

### Minor

- **The paper does not explicitly state whether baseline performance numbers come from re-implementation or original papers.** While Table 2 reports training GPU time and GPU memory for all baselines (strongly implying they were all re-trained in the same environment), the paper never says "we re-trained all baselines using the official code under the same training configuration." A single sentence clarifying this would remove ambiguity, especially for readers concerned about fair comparison.

- **TIGER (small) has higher MACs (7.65 G/s) than some efficient baselines (Conv-TasNet: 7.19 G/s; SudoRM: 4.65 G/s).** The paper correctly emphasizes parameter reduction (94.3% fewer than TF-GridNet), but the MACs advantage over the most efficient prior models is more modest. This should be acknowledged to avoid overclaiming on efficiency across all dimensions.

- **The MSA module's average pooling kernel size is unspecified.** The paper states that average pooling layers λ(·) are used to downsample multi-scale features to the same frequency resolution (Section 3.3), but does not specify the kernel size or stride for these pooling operations.

### Trivial
- The abstract's "improved the performance by about 5%" is a reasonable rounding of the 3.6% (SDRi) and 6.8% (SI-SDRi) improvements — not a meaningful error, but precise reporting would be better.

## Nice-to-Haves

- Release the real-world test set recordings (or a detailed protocol for constructing a comparable one) to substantiate the EchoSet generalization claim.
- Analyze the distribution of F³A attention weights or logit ranges across layers to confirm that the √(E×T) scaling factor does not cause saturation (though the successful training suggests no practical issue).
- Show whether TIGER's performance advantage on EchoSet is consistent across different SDR levels and overlap ratios.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Baseline results are not sourced or reproduced"** (Harsh Critic Issue 1) — Table 2 reports training GPU time and GPU memory for *all* baselines (Conv-TasNet, DualPathRNN, SudoRM, A-FRCNN-16, TDANet, BSRNN, TF-GridNet), and the Table 1 caption states "Models are trained and tested on corresponding datasets." This conclusively demonstrates that all baselines were re-run under the same conditions as TIGER. The paper could be more explicit, but the criticism as presented is invalid.

2. **"F³A attention scaling factor is ill-defined and likely incorrect"** (Harsh Critic Issue 3) — The paper's scaling is √(E×T), where the query and key have shape K × (E×T). This follows the standard Transformer scaling convention 1/√(d_k), where d_k = E×T. The formulation is mathematically correct. The reviewer's claim that this is "not the standard √d_k" is mistaken. No evidence of numerical instability or performance degradation is presented, and the model trains successfully.

3. **"Band-split ablation doesn't isolate the band-split strategy vs. overall architecture"** — Table 4 directly compares NonSplit (no band-split, each frequency point as a sub-band) against three band-split strategies using the same architecture. This properly isolates the effect of band-splitting. The criticism misreads the ablation design.

4. **Editorial nits about "about 5%" discrepancy** — The improvement is 3.6% (SDRi) and 6.8% (SI-SDRi); "about 5%" is a reasonable approximate average, not a reporting error.

## Novel Insights

The most interesting finding is the interaction between dataset complexity and TIGER's relative performance: on the simplest dataset (Libri2Mix, clean), TIGER trails TF-GridNet by 6%; on the more realistic LRS2-2Mix the gap narrows to 2%; and on the most complex dataset (EchoSet) TIGER surpasses TF-GridNet entirely. This suggests that the band-split + interleaved time-frequency design is not merely efficient but actually provides a *representational advantage* in challenging acoustic conditions — possibly because the frequency-compressed representation implicitly regularizes against reverberation artifacts that larger models overfit to. This pattern is worth deeper investigation beyond the current paper.

## Suggestions

1. **Flesh out the real-world evaluation**: Provide a detailed description of the recording setup (playback hardware, microphone, room dimensions), specify whether the 10 environments overlap with EchoSet scenes, report numeric results with error bars for Figure 1, and ideally evaluate on an established real-world corpus as complementary evidence.

2. **Provide a table for cinematic sound separation** with dataset statistics, evaluation protocol, and the full comparison with BSRNN (and ideally additional baselines). A single sentence with percentage improvements is insufficient for a claimed SOTA result.

3. **Add a sentence clarifying baseline reproduction**: e.g., "All baseline models were re-trained using official implementations under the same training configuration and STFT parameters as TIGER, with hyperparameters from the original papers."

4. **Specify the average pooling kernel sizes** in the MSA encoding stage description.

## Score and Decision

The paper makes genuine contributions: TIGER offers a novel and effective architecture for lightweight speech separation with compelling efficiency-performance trade-offs, and EchoSet provides a more realistic simulation dataset than existing options. The ablations are thorough and the results on standard benchmarks are competitive. The main weaknesses are the underspecified real-world evaluation and the sketchy cinematic separation results — both addressable through improved reporting rather than fundamental design flaws. The core model contribution is solid and well-supported.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>