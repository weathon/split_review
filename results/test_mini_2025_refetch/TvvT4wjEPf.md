Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

## Summary
This paper addresses the overflow problem in FHE-based (CGGI) RNN inference when using single-ciphertext quantization. The authors propose Overflow-Aware Activity Regularization (OAR), a training-time technique that pushes pre-activations into "correct" overflow regions where wrap-around does not flip the sign. Combined with the ModSign activation function, OAR enables practical encrypted RNN inference at 5-6 bit precision. Results show 90.82% encrypted accuracy on MNIST (within 0.17% of plaintext) at 2.1s latency for a 1.9M-parameter two-layer RNN — a substantial improvement over prior SHE-based work.

## Strengths

1. **Well-motivated and clever approach to a real obstacle.** The paper identifies a concrete problem (overflow in single-ciphertext FHE RNNs) that prior work either ignored or accepted as a cost. The central insight — that overflow can be harmless if values land in the "correct" regions of the modulus — is clear, intuitive, and leads to a natural regularizer (OAR) that penalizes values in incorrect regions. This is a genuinely creative solution.

2. **Dramatic empirical gains at low precision.** Table 1 reports that OAR lifts accuracy from 9.88%→80.73% (+71%) at 5-bit and from 46.82%→89.35% (+43%) at 6-bit. These are not incremental improvements — they are the difference between unusable and competitive performance. The OAR metric confirms the mechanism: pre-activations in correct regions jump from ~60% to ~99.8%.

3. **State-of-the-art encrypted RNN latency.** The regular model achieves 2.10s per sample with 90.82% accuracy (Table 3, param set 2). Prior work (SHE) reported 576s for a smaller 180K-parameter single-layer RNN on a different task. Even accounting for task and hardware differences, demonstrating sub-3s encrypted inference for a multi-layer 1.9M-parameter RNN is a genuine advance.

4. **Scaling experiment validates the approach.** The enlarged 128×128-input RNN (8.4M params, 128 timesteps) achieves 87.56% encrypted accuracy (Table 3), confirming OAR's utility beyond the base model. The linear latency scaling (4.57× for 4.57× more timesteps) shows no unexpected overhead.

5. **Sensitivity analysis of the regularization rate.** Table 2 systematically varies the OAR rate from 0 to 10⁻² for both 5-bit and 6-bit, identifying 10⁻⁴ as optimal and revealing that 5-bit is substantially more sensitive to the rate — useful practical guidance.

## Weaknesses

### Fatal
None.

### Major

1. **Single-dataset evaluation (MNIST only).** All experiments, including the "enlarged" variant, are on MNIST digit classification. The paper's framing ("Towards Practical Large-Scale Privacy-Preserving RNNs") implies broader applicability to domains where RNNs are deployed (speech recognition, financial forecasting). Demonstrating OAR on a second sequential task — even a simple one like command-word recognition or character-level language modeling — would substantially strengthen the case that the method generalizes rather than exploiting properties of MNIST row processing.

2. **Accuracy discrepancy between OAR evaluation and encrypted evaluation tables.** The plaintext accuracy for the 6-bit OAR₂ model at rate 10⁻⁴ is reported as **92.11%** in Table 2 (Section 4.1.2) but as **90.99%** in Table 3 (Section 4.2). Similarly, the enlarged model's plaintext accuracy is **92.69%** (Section 4.1.4) but **92.27%** in Table 3. The paper states that models used for encrypted evaluation come "from sections 4.1.2 and 4.1.4, trained with 6-bit OAR₂ at a rate of 10⁻⁴." If the evaluation protocols are different (e.g., Table 3's "plaintext" uses ModSign during evaluation while Table 2 may use a different setup), this must be stated explicitly. As presented, the reader cannot tell which baseline is correct, and the claimed "negligible disparity of -0.17%" (based on 90.99% in Table 3) would be larger if the correct baseline is 92.11%.

### Minor

3. **The 274× latency comparison to SHE is cross-dataset and cross-hardware.** The paper compares its MNIST results (2.1s, two A100 GPUs) against SHE's Penn Treebank results (576s, unspecified hardware). While the improvement is impressive, a direct comparison on the same task and comparable hardware would be far more informative. The paper should present this caveat more prominently rather than leading with the 274× figure.

4. **No direct controlled comparison to Anonymous (2025) on their exact setting.** The paper's narrative positions OAR as recovering the -25% accuracy drop reported in Anonymous (2025). However, the reference work used 11-bit precision, while this paper operates at 5-8 bits. The recovery claim is therefore indirect — it relies on reasoning about what would happen rather than a direct experiment. A single row testing Anonymous (2025)'s 11-bit setting with and without OAR would solidify this claim.

5. **Output-layer MAE for the enlarged model lacks interpretability.** Table 4 reports an output MAE of 53.06 for the enlarged model (param set 1). Without knowing the dynamic range of the pre-activations, this number is hard to evaluate — is 53.06 large or small relative to typical values? The paper notes this is out of a "max of 1024," but that is the number of units, not a value range.

### Trivial
None.

## Nice-to-Haves
- **Report the computational overhead of OAR during training.** The paper trains for 1000 epochs. Does OAR add noticeable training time? A practitioner would want to know.
- **Show the OAR metric for the encrypted models.** Table 1 reports the OAR metric for plaintext models; showing it for the actual encrypted models (trained with OAR) would confirm that the regularization remains effective under real FHE noise.
- **Test on a second task beyond MNIST** (as noted under Major weaknesses, this would elevate the paper substantially).

## Removed Points

- **"ModSign is trivial, calling it 'proposed' overstates novelty"** (from Harsh Critic): The paper introduces ModSign as a necessary adaptation of the sign function for the modulus-aware training setting. Whether "proposed" is warranted is a matter of framing, not a correctness issue. ModSign is a small piece but is not claimed as a major contribution.
- **"No comparison to SHE on the same task"** (from Harsh Critic): Already covered by Weakness #3 (cross-dataset comparison). Not a separate point.
- **"Abstract only mentions 274× without caveats"** (from Harsh Critic): This is a presentation preference, not a substantive weakness.
- **"OAR metric is never used beyond Table 1"** (from Harsh Critic): Valid as a nice-to-have, but not a weakness — the paper's core claims don't depend on it.
- **"OAR is a training-time heuristic rather than principled"** (from Harsh Critic): The paper itself acknowledges this in the conclusion. Not a weakness.
- **Various generic/superficial strengths from Strength Finder** (e.g., "Introduction of ModSign activation function" — this is a tiny contribution; "Low error metrics" — the enlarged model errors are quite high, undermining this as a strength): Removed as inflated or conflicting with verified weaknesses.

## Novel Insights
None beyond the paper's own contributions. The key novel insight — that overflow can be divided into correct and incorrect regions, and that a penalty-based regularizer can guide pre-activations toward correct regions — is the paper's own contribution and is well-articulated.

## Suggestions
1. **Resolve the accuracy discrepancy.** Clarify whether the 92.11% (Table 2) and 90.99% (Table 3) differ due to evaluation protocol (ModSign vs. standard sign, checkpoint selection, etc.). If the 90.99% value is correct for the encrypted evaluation setup, explain why.
2. **Add one row to Table 2** testing Anonymous (2025)'s 11-bit setting with and without OAR, even on MNIST, to directly substantiate the "recovery" claim.
3. **Report the dynamic range** of pre-activations alongside the MAE numbers in Table 4 so the error metrics are interpretable.
4. **Test on at least one additional sequential task** (e.g., keyword spotting on Speech Commands) to demonstrate task generality.

## Score and Decision

Now let me provide the calibration anchor comparison. My round-1 bracket was 4–7. After round 2, I compared against:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DCT-CryptoNets (lPJUQsSIxm) | 6.33 | 1, 2 | Accepted poster; broader evaluation (CIFAR-10, ImageNet). Current paper is slightly weaker due to MNIST-only eval and accuracy inconsistency. |
| CipherPrune (mUMvr33FTu) | 6.25 | 2 | Accepted poster; broader evaluation, cleaner comparison. Current paper is weaker on evaluation breadth. |
| MPC-Minimized LLM (beAlX6RjsW) | 6.33 | 2 | Rejected; similar contribution level but the rejection was due to other issues. |
| AERO (CPBdBmnkA5) | 6.0 | 2 | Rejected despite 6.0 because it lacked actual PI implementation. Current paper is stronger (end-to-end encrypted eval). |
| Towards Cheaper Inf. (oOwDQl8haC) | 5.75 | 2 | Accepted poster; similar contribution style (quantization overflow mitigation), evaluated on multiple datasets. Comparable quality. |
| HANs (tqYx8DgL0u) | 3.67 | 1 | Rejected; substantially weaker. |
| Compensating Nonlinear (jU3zRzUBiD) | 4.0 | 1 | Rejected; weaker contribution. |

The paper sits between the stronger accepted papers (DCT-CryptoNets at 6.33, CipherPrune at 6.25) and the weaker works (HANs at 3.67, Compensating at 4.0). It is most comparable to Towards Cheaper Inference (5.75) — both tackle overflow in quantized computation with a training-time fix, both have solid experimental validation but notable gaps. However, the current paper's MNIST-only evaluation and the accuracy discrepancy make it slightly weaker. I therefore place it at **5.5** — marginally above acceptance threshold, with the expectation that the accuracy inconsistency and MNIST-only concern are addressed for final publication.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>