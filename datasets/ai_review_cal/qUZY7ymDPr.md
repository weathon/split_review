- Decision: Reject
- Avg Score: 4.80
- Scores: 6, 6, 3, 6, 3
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes PPLLaVA, a method that uses CLIP-based prompt-guided attention weights to drive convolution-style pooling of video tokens, achieving aggressive compression (~80-90%) while retaining instruction-relevant information. The model integrates three components: fine-grained vision-prompt alignment via CLIP text encoder, prompt-guided 3D pooling for flexible token reduction, and a CLIP context extension for long prompts. The approach is evaluated across multiple video benchmarks (VCG Bench, Video-MME, MVBench, MSVD, MSRVTT, ActivityNet) and image benchmarks, demonstrating strong performance with significantly improved throughput compared to full-token baselines.

## Strengths

- **State-of-the-art performance with dramatic efficiency gains**: Across Tables 1, 2, and 3, PPLLaVA achieves top or near-top scores on multiple benchmarks (e.g., PPLLaVA-DPO achieves 3.73 on VCG Bench vs. 3.66 for LLaVA-Next-Video-DPO; 53.6 overall on Video-MME with subtitles), while using only 1024 visual tokens and achieving ~3× higher throughput (4.6 s/video vs. 15.0 s/video for the no-pooling baseline). These gains are consistently supported by the reported numbers.

- **Quantitative motivation for addressing video redundancy**: Section 3.1 provides a concrete certificate-length analysis on Video-MME, showing all tested models degrade on high-redundancy videos (e.g., LLaVA-Next-Video drops 3.5 pts) and that manual frame selection recovers 0.6–1.1 pts. This directly motivates the need for prompt-aware token selection.

- **Maintained image performance despite video specialization**: Table 5 shows PPLLaVA outperforms LLaVA-Next-Video and even some dedicated image models on image benchmarks (MMMU 37.9 vs. 34.2, MMB-ENG 68.9 vs. 64.7, POPE 88.46 vs. 83.10), demonstrating no catastrophic forgetting — surprising and noteworthy for a video-focused method.

- **Thorough component-level ablation**: Table 6 (ablation:overall) decomposes the contributions of prompt-guided pooling and CLIP context extension, showing each provides consistent gains on both VCG Bench and Video-MME (pooling: +0.01 VCG avg, +1.5 Video-MME; context extension: +0.11 VCG avg, +1.1 Video-MME).

- **Qualitative evidence of prompt-awareness**: Figure 5 visualizes attention weights shifting dramatically based on the user's question (e.g., "girl's feelings" focuses on face vs. "number of 3D objects" focuses on objects), directly illustrating the mechanism.

## Weaknesses

### Fatal
None.

### Major

- **Training/inference discrepancy in CLIP text encoder input**: Section 3.2 (method) states: "Specifically, we input the user's question into the CLIP text encoder to obtain the text feature c" (line 92). However, Section 3.3 (training) states: "During training, both questions and answers are fed into the CLIP text encoder to better capture prompt-vision relevance" (line 132). These statements directly conflict. At inference, the answer is unavailable, meaning the attention weights S that guide pooling are computed from question+answer during training but from question-only at test time. The paper neither acknowledges this discrepancy nor explains how it is resolved. If the model learns to rely on answer tokens to produce useful attention weights, the inference-time behavior would be operating on a fundamentally different distribution. This is a structural concern that must be clarified — either the method description is wrong (and only questions are used at both stages) or the training protocol introduces a mismatch that needs validation.

- **Missing ablation isolating prompt-guidance from compression**: Table 6 compares "no pooling" (4608 tokens) with "+Prompt-guided Pooling" (1024 tokens), but this conflates two effects: (a) the benefit of compression itself, and (b) the guidance from the prompt. The paper never compares prompt-guided pooling to *unweighted average pooling at the same token count (1024 tokens)*. The only average-pooling baseline (LLaVA-Next at 576 tokens) uses a different base model and different token count, making it uninformative for isolating this effect. Since prompt-awareness is the paper's core novelty, the absence of this direct comparison means the central claim that prompt-guidance (rather than compression alone) drives improvement is not empirically supported.

### Minor

- **CLIP context extension not directly validated**: The paper claims linear interpolation of positional embeddings gave inferior results and proposes asymmetric interpolation instead (lines 112-116). However, no direct comparison between linear interpolation and the proposed asymmetric method appears in any table or figure. The overall improvement from adding context extension (+0.11 VCG avg, +1.1 Video-MME overall in Table 6) does not isolate the interpolation method. A minimal ablation comparing (a) random extension, (b) linear interpolation, and (c) asymmetric interpolation would be needed to support this claimed improvement.

- **SOTA claims should be qualified**: The abstract and introduction claim "state-of-the-art performance across various video benchmarks." On Video-MME (Table 3), PPLLaVA* (7B) achieves 53.6 overall with subtitles, while LLaVA-Next-Video-34B achieves 54.9. The paper should consistently qualify "among 7B models" where applicable, and acknowledge benchmarks where the model is not the absolute best (e.g., PPLLaVA-DPO's CO score of 3.81 on VCG Bench vs. LLaVA-Next-Video-DPO's 4.08).

- **DPO baseline attribution unclear**: In Table 1, the row "LLaVA-Next-Video~$\dag$" (line 159) is marked with a dagger but no citation is provided. The paper should state whether these are reproduced results or from a prior work, and clarify the hyperparameter setup for fair comparison.

- **DPO causes non-trivial drop on multiple-choice benchmarks**: In Table 9, adding DPO (row 5 vs. row 3) improves VCG Bench from 3.32 to 3.73 but drops MVBench from 57.1 to 55.8 and Video-MME from 50.0 to 49.3. The paper describes this as "a minimal side effect on multiple-choice benchmarks" (line 388), but a ~1-2 point drop is non-trivial and should be analyzed rather than minimized.

### Trivial
None.

## Nice-to-Haves
- A comparison of prompt-guided pooling vs. uniform average pooling at the same compression ratio (1024 tokens) would cleanly validate the core novelty.
- Reporting variance or multiple-seed results for the smaller deltas (e.g., 3.21 vs. 3.20, 53.6 vs. 53.2) would help assess significance.
- Adding a parameter-count and FLOPs comparison table with baselines would strengthen the efficiency argument.
- A brief failure analysis (e.g., cases where prompt guidance hurts) would improve depth.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"Token count inconsistency for 8-frame row"**: The reviewer claimed the 8-frame no-pooling row (4608 tokens) was inconsistent with earlier tables. This is incorrect — the PPLLaVA spatial token count per frame (576 at 336×336 resolution, 4608/8=576) differs from LLaVA-Next-Video's per-frame token count (144 at different resolution/pooling setup). The numbers are internally consistent within PPLLaVA's own setup.
- **"Resolution difference complicates image benchmark comparison"**: The reviewer noted LLaVA-Next-7B uses 672×672 vs. PPLLaVA's 336×336. This actually strengthens the paper's case (PPLLaVA matches or beats LLaVA-Next-7B at half the resolution), so it is not a weakness.
- **"Statistical significance / variance reporting"**: Generic request that is standard for large-scale benchmarks where single-run evaluation is the norm. Not a substantive weakness of this paper.
- **"Threshold of 0.5 for CLIP similarity is arbitrary"**: The certificate-length analysis is a motivating experiment, not a core contribution. The threshold is standard for CLIP cosine similarity. This criticism is too granular for a paper with this scope.
- **"Missing appendix/reproducibility details"**: Parser strips appendix sections from all papers; these details exist in the original submission.
- **Generic formatting and presentation nitpicks**: These are parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions. The central insight — using CLIP text encoder attention weights as dynamic pooling kernels for convolution-style video token compression — is itself the paper's novel contribution, and the reviews do not surface additional novel perspectives beyond what the paper provides.

## Suggestions
1. **Resolve the CLIP text encoder discrepancy**: Clarify whether the CLIP text encoder receives only the question (as in Section 3.2) or both question and answer (as in Section 3.3) during training. If both are used, explain how the mismatch with inference is handled, and ideally provide an ablation using only questions during training to validate that the method works without answer leakage.
2. **Add an ablation comparing prompt-guided pooling vs. uniform average pooling at the same token count (1024 tokens on PPLLaVA)**: This directly tests whether prompt-guidance contributes beyond compression.
3. **Add a direct comparison of asymmetric vs. linear interpolation for the CLIP context extension** to validate the claimed advantage.
4. **Qualify SOTA claims** to specify "among 7B models" where appropriate, and acknowledge benchmarks where the model is not the absolute best.
5. **Provide a citation or clarify the source** of the LLaVA-Next-Video-DPO baseline results, and analyze the MVBench/Video-MME drop under DPO.
