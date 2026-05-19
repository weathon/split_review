- Decision: Accept
- Avg Score: 5.83
- Scores: 6, 8, 6, 8, 6, 1
Now I have a thorough understanding of the paper. Let me synthesize everything.

## Summary

This paper presents TIGER, a lightweight time-frequency-domain speech separation model (0.82M parameters) that employs frequency band-split, multi-scale selective attention (MSA), and full-frequency-frame attention (F³A) modules to achieve high efficiency. Additionally, it introduces EchoSet, a reverberation+noise dataset rendered via SoundSpaces 2.0 using realistic acoustic simulations from Matterport3D scenes. On EchoSet, TIGER (large) achieves 14.22 dB SDRi, surpassing TF-GridNet (13.73 dB) while reducing parameters by 94.3% and MACs by 95.3%. On standard benchmarks (Libri2Mix, LRS2-2Mix) TIGER trails TF-GridNet by small margins but remains competitive, especially given its dramatically lower cost.

## Strengths

1. **Very large efficiency gain with competitive quality**: TIGER (large) uses 0.82 M parameters vs. TF-GridNet's 14.43 M (94.3% reduction) and 15.27 G/s MACs vs. 323.75 G/s (95.3% reduction), while exceeding TF-GridNet on EchoSet (14.22 vs. 13.73 dB SDRi) and on real-world test data. This is the first sub-1M parameter speech separation model with SOTA-comparable performance (Table 1, Table 2).

2. **EchoSet improves real‑world generalization**: Models trained on EchoSet produce better separation on real-world recordings than models trained on Libri2Mix or LRS2-2Mix (Figure 1). EchoSet's rendering pipeline accounts for object occlusions, material properties, and random overlap ratios — factors absent from prior datasets (Table 1 comparison, Section 4).

3. **MSA module validated as more efficient than alternatives**: Replacing MSA with LSTM, Mamba, or SRU increases parameters by 2.5–2.9× and MACs by 2.7–6.5× while SDRi is similar or only marginally better (Table 5). This cleanly demonstrates the efficiency advantage of the multi-scale selective attention design.

4. **Band‑split leveraging speech prior knowledge demonstrably helps**: The LowFreqNarrowSplit scheme (finer low-frequency bands) achieves 13.15 dB SDRi vs. NonSplit (11.53 dB), NormalSplit (12.94 dB), and EvenSplit (12.80 dB) at the same parameter count (Table 4), validating the use of speech-domain knowledge.

## Weaknesses

### Fatal

None.

### Major

- **Baseline training protocol on EchoSet is not specified for the main comparison.** The caption for Table 1 states "Models are trained and tested on corresponding datasets," but the paper does not clarify whether baselines (TF-GridNet, BSRNN, etc.) were re-run on EchoSet using consistent hyperparameters, learning schedules, and early stopping — or whether numbers were taken from original papers (where available) or from other experimental conditions. The ablation section (Section 7.3, line 257) explicitly says "The training configuration of TIGER and other models was the same" — but this statement is scoped to the ablation studies only, not to the main results. Since TIGER's headline claim (surpassing SOTA on complex data) hinges on the EchoSet comparison, and given that the margins against TF-GridNet are small (0.49 dB SDRi), the paper must be transparent about how each baseline's EchoSet numbers were produced. This is a transparency issue affecting credibility of the central claim.

### Minor

- **No variance estimates reported anywhere.** None of the tables report standard deviations, confidence intervals, or number of random seeds. While single-run evaluation is common in the speech separation literature, the gap between TIGER and TF-GridNet on EchoSet (0.49 dB SDRi) is small enough that seed-to-seed variation could matter. Reporting variance (at least for the key comparison) would substantially strengthen the evidential foundation.

- **Real-world validation evidence is too thin.** The claim that EchoSet-trained models generalize better to real-world data rests solely on a bar chart (Figure 1) with no numeric SDRi/SI-SDRi values, no error bars, and no explicit breakdown of the number of test mixtures or per-environment results. The real-world test set (10 environments, 40 speakers) is described only briefly. The paper should report actual numbers with variance for this experiment.

- **Cinematic sound separation claim is unsupported.** A single sentence (Section 7.2) reports a 39.4% SDR improvement over BSRNN with no details on the dataset, evaluation metric, number of sources, or experiment configuration. This should either be substantially expanded with proper experimental setup or removed.

- **EchoSet release commitment is incomplete.** The paper promises code release after acceptance (line 173) but does not commit to releasing the EchoSet dataset itself or the generation scripts. Since EchoSet is a named contribution, readers should be able to reproduce it.

### Trivial

- **MLC network details unspecified.** The encoding stage (Section 3.3.1) mentions a "multi-layer convolutional (MLC) network" without specifying the number of layers, kernel sizes, or whether dropout is used. The downsampling depth parameter D is also not given a concrete value tied to the band-split configuration.

## Nice-to-Haves

- The minor gap between TIGER and TF-GridNet on LRS2-2Mix (2% drop) and Libri2Mix (6% drop) could be discussed in terms of where the quality loss comes from, to help future work close the gap on simpler data too.
- The "more complex scenarios favor TIGER" pattern is interesting; a brief hypothesis about *why* the band-split + F³A design handles reverberation better than TF-GridNet's architecture would deepen the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Abstract being misleading** (from Harsh Critic): The abstract says "On EchoSet and real-world data, TIGER ... surpass[es] SOTA model TF-GridNet" — this is qualified by the specific setting. The Introduction (line 31) further clarifies that TIGER's superiority grows with dataset complexity. The abstract is not inaccurate. **Removed** as factually incorrect reading.

2. **WHAMR! "Only room" is an oversimplification** (from Harsh Critic): The paper's Table 1 describes WHAMR!'s reverberation as "Only room" — this is an accurate characterization of WHAMR!'s scope (ISM, rectangular rooms), not a misrepresentation. **Removed.**

3. **LRS2-2Mix "different scenes" vs. EchoSet "same scene" as a confound** (from Harsh Critic): The critic speculates that EchoSet's same-scene design might explain better generalization without implying greater realism. This is speculation; the paper's claim is about the rendering fidelity (object occlusions, materials), not about the scene-counting design choice. **Removed** as speculative.

4. **"LRS2-2Mix is a dataset, not a mixing method"** (from Harsh Critic): The paper says the real-world data "followed the same mixing method as LRS2-2Mix" — this refers to the mixing procedure described in the cited TDANet paper (li2022efficient) that introduced LRS2-2Mix. This is a standard cross-reference. **Removed** as a misunderstanding.

5. **GPU speed advantage is modest / inference time discussion** (from Harsh Critic): The critic notes that TIGER's GPU time (74.51 ms) is similar to TDANet Large (74.27 ms) and suggests this is worth commenting on. This is a neutral observation, not a weakness. The paper reports the numbers transparently. **Removed.**

6. **"Likely favors TIGER" framing** (from Harsh Critic, point 1): The claim that the EchoSet comparison "likely favors TIGER because baselines were not properly adapted" is speculative. The verifiable weakness is that the baseline training protocol is not documented — not that it must be unfair. The weakness is retained in Major above in its factual form, but the speculative "likely favors" framing is removed.

7. **Strength about "This is the first sub‑1 M parameter speech separation model that matches or exceeds SOTA quality"** (from Strength Finder): The strength is supported, but it is subsumed by Strength 1 in my list above (merged).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the transparency gap around baseline evaluation on EchoSet as the central actionable concern, but do not produce a fundamentally novel observation about the architecture or dataset that the authors themselves missed.

## Suggestions

1. **Clarify baseline protocol on EchoSet**: Add a sentence to the experimental setup explicitly stating whether baselines were reproduced with author code / standard configs, or whether numbers were taken from papers, for each dataset. If baselines were re-run on EchoSet, confirm the training configuration consistency.

2. **Add variance for the headline comparison**: Report SDRi and SI-SDRi over at least 3 random seeds for TIGER and TF-GridNet on EchoSet, ideally with standard deviation or a significance test.

3. **Provide numeric values for real‑world test**: Replace or supplement Figure 1 with a table of SDRi/SI-SDRi values with error bars, and specify the number of test mixtures.

4. **Commit to EchoSet release**: State whether the rendered audio files, the generation scripts, or both will be released.

5. **Expand or remove the cinematic sound separation experiment**: As written, the claim is too thin to be evidence.

6. **Specify MLC and D**: Add a brief note about the MLC network layers/kernels and the value of D used in the experiments.
