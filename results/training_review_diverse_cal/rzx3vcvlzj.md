Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me produce the final consolidated review.

## Summary

This paper presents TIGER, a lightweight time-frequency domain speech separation model using frequency band-splitting, multi-scale selective attention (MSA), and full-frequency-frame attention (F³A). It also introduces EchoSet, a speech separation dataset with realistic reverberation simulated via SoundSpaces 2.0 and Matterport3D. TIGER achieves competitive or superior performance on EchoSet (14.22 dB SDRi, surpassing TF-GridNet's 13.73) while using only 0.82M parameters and 15.27 G/s MACs — reductions of 94.3% and 95.3% respectively.

## Strengths

1. **Dramatic efficiency gains with competitive performance on reverberant data.** TIGER (large) achieves 0.82M parameters and 15.27 G/s MACs, compared to TF-GridNet's 14.43M and 323.75 G/s, while surpassing TF-GridNet on EchoSet (14.22 vs. 13.73 dB SDRi) and being competitive on LRS2-2Mix (15.3 vs. 15.7). The efficiency advantage is clearly documented across params, MACs, GPU time, GPU memory, and CPU time in Table 2.

2. **EchoSet is a genuine contribution toward realistic evaluation.** The dataset uses SoundSpaces 2.0 with Matterport3D scenes, accounting for object occlusions and material properties — going beyond WHAMR!'s rectangular-room-only reverberation. Table 1 shows that as datasets become more complex (Libri2Mix → LRS2-2Mix → EchoSet), TIGER's relative performance improves, and Figure 1 indicates models trained on EchoSet generalize better to real-world recordings than models trained on Libri2Mix or LRS2-2Mix.

3. **First sub-1M-parameter speech separation model with SOTA-comparable results.** At 0.82M parameters, TIGER (small) achieves 13.15 dB SDRi on EchoSet (close to TF-GridNet's 13.73) and 17.09 dB on Libri2Mix. This is a meaningful milestone for deployment in resource-constrained settings.

4. **Comprehensive ablation study validates architectural choices.** Tables 4–6 systematically ablate band-split schemes, MSA, and F³A modules, showing each component's contribution and the efficiency-performance trade-offs against alternatives like LSTM, Mamba, and SRU. The honesty of presenting LSTM's higher raw SDRi (13.92 vs. 13.15) at 2.5× parameters and 6.5× MACs is commendable.

## Weaknesses

### Fatal
None.

### Major
1. **The cinematic sound separation claim is unsubstantiated.** Lines 253–254 claim a 39.4% SDR improvement over BSRNN with 97.3% fewer parameters and 77.6% fewer MACs, but provide no dataset description, evaluation protocol, number of test samples, or tabular results. A two-sentence report with a project page link does not constitute evidence. For a claim this striking, the lack of any experimental detail undermines the paper's credibility — even though this is not the paper's central contribution. Either this claim needs to be removed or fully supported with the same rigor as the speech separation experiments.

2. **The real-world evaluation (Figure 1) lacks numerical results and experimental detail.** The paper reports only a bar chart without SDRi/SI-SDRi values, number of test mixtures, confidence intervals, or variance. Lines 170–172 describe the setup as "10 real-world environments and recording audio from 40 speakers" but do not state how many mixtures were created, whether each mixture was recorded separately, or the precise recording protocol (room dimensions, microphone placement). For a dataset whose stated purpose is "bridging the gap between model training and real-world applications," this evaluation is too attenuated to rigorously support the claim that EchoSet-trained models generalize better.

### Minor
3. **The exact band-split configuration (frequency bin boundaries) is not reported**, compromising full reproducibility. The paper states (line 325) that LowFreqNarrowSplit "offered finer splits in low-frequency bands" and that "human speech typically ranges from 85 Hz to 1100 Hz," but never gives the concrete mapping from frequency bins to sub-band widths G_k. This is a core architectural choice that directly affects parameter count and model behavior, and must be fully specified for replication.

4. **Baseline hyperparameters may not be optimally tuned for EchoSet.** The paper says (line 257) "The training configuration of TIGER and other models was the same" — but models like TF-GridNet, BSRNN, and TDANet have many task-specific knobs (LSTM hidden size, number of layers, attention heads, frame size) that were originally optimized on WSJ0-2mix or Libri2Mix. Using identical training configurations without tuning baselines on the new EchoSet dataset could disadvantage them relative to TIGER, which was designed for this setting. This weakens the headline claim that TIGER *surpasses* TF-GridNet on EchoSet.

5. **The TF-GridNet MACs value (323.75 G/s) differs substantially from a scaled expectation based on the original publication.** The original TF-GridNet paper reports 351.7 G MACs for 4-second audio samples. While MACs do not always scale linearly with input length (e.g., self-attention is O(T²)), the discrepancy is large enough to warrant explanation, especially since the paper states MACs are computed "for one second of audio at 16 kHz" (line 173). The authors should clarify whether different FFT sizes, hop lengths, or counting methodology accounts for this difference.

### Trivial
- In Table 1, "SudoRM-RF1.0x" appears — standardize capitalization.
- "effciency" typo in the Section 6.2 heading (line 249).

## Nice-to-Haves
- A cross-dataset experiment (e.g., train on EchoSet, test on WHAMR!) would further validate whether TIGER's advantage reflects genuine robustness or dataset-specific adaptation. Not required for acceptance but would strengthen the contribution.
- Error bars on Tables 1 and 2 (at least for the main SDRi/SI-SDRi results) would improve confidence in the comparisons, though this is not standard practice in all speech separation papers.
- A limitations section discussing potential overfitting to SoundSpaces 2.0's specific reverberation model, the gap on clean data (Libri2Mix), and the modest size of the real-world test set would improve paper maturity.

## Removed Points

These points from the original reviews were removed; they are flagged for awareness but should be treated with caution:

- **"Cross-dataset evaluation on WHAMR! missing"** — The paper already evaluates on three datasets (Libri2Mix, LRS2-2Mix, EchoSet) using in-domain train/test. Demanding an additional cross-dataset evaluation on a fourth dataset is scope creep beyond what is needed to support the paper's claims.
- **"SOTA claim not novel because 'comparable' is loosely defined"** — The paper honestly reports that on simpler datasets TIGER lags behind TF-GridNet (6% on Libri2Mix, 2% on LRS2-2Mix). The claim is qualified and data-supported.
- **"Missing error bars on all results"** / **"Missing limitation section"** — These are suggestions that improve presentation but are not standard requirements for this class of paper. They are folded into Nice-to-Haves.
- **"MACs comparison misleading without controlling for input length"** (the full claim about chunk size differences) — The paper explicitly states MACs are "calculated for one second of audio at 16 kHz" (line 173), which controls for input duration. The remaining concern about implementation differences is covered in Minor Weakness #5.
- **"The first sub-1M-parameter claim needs qualification"** — The paper already qualifies this in context: TIGER achieves *comparable* (not superior) performance on standard benchmarks while being dramatically smaller. The data in Table 1 supports this honestly.
- **"The MSA vs LSTM trade-off should be more explicitly acknowledged"** — The paper already presents this trade-off transparently in Table 5 and discusses it in the text (lines 329–330).

## Novel Insights

The most interesting pattern across the reviews is that the paper's strongest claim (surpassing TF-GridNet on realistic data) rests on precisely the combination that also generates the most scrutiny: a new dataset (EchoSet) where the baseline (TF-GridNet) has not been tuned, and a real-world test that lacks numerical rigor. This creates a circular vulnerability — the model's advantage is demonstrated primarily on the authors' own evaluation setup. What would break this circle is a single clean experiment: train both TIGER and the best-tuned baseline on EchoSet and test on an independent, well-established reverberant benchmark. The fact that this experiment does not appear suggests either an oversight or (more optimistically) that the authors can add it in revision. Either way, the paper's core technical value — an extremely lightweight architecture with well-designed frequency-domain processing — is not in doubt; what is in doubt is whether its superiority over strong baselines in complex environments is as clean as claimed.

## Suggestions

1. Provide the exact frequency bin ranges for LowFreqNarrowSplit and all band-split schemes in an appendix.
2. Either remove the cinematic sound separation claim or provide full experimental details (dataset, protocol, tabular results).
3. Report numerical SDRi/SI-SDRi values with variance from the real-world evaluation, along with the number of test mixtures and a description of the recording procedure.
4. Clarify the TF-GridNet MACs calculation methodology and resolve the discrepancy with the original paper's reported values.
5. Consider a cross-dataset evaluation (EchoSet-trained → WHAMR! test) to decouple the method evaluation from the new dataset evaluation.

## Score and Decision

The paper makes two clear contributions — a genuinely lightweight architecture and a carefully constructed realistic dataset — and supports these with extensive ablations. The weaknesses are real but addressable: the cinematic claim is a presentation issue, the real-world evaluation needs numbers, and the baseline tuning concern is a common but valid limitation. None of these threaten the core findings about TIGER's efficiency or EchoSet's value. The paper merits acceptance subject to minor revisions addressing the documentation gaps.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>