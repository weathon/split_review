I have thoroughly read the paper and verified the reviewer claims against the actual paper content. Let me now produce the consolidated review.

## Summary

DeCodec proposes a neural audio codec that learns disentangled representations by projecting audio embeddings into orthogonal subspaces for speech and background sound (via a Subspace Orthogonal Projection module and Representation Swap Training procedure), and further decomposes speech into semantic and paralinguistic components via semantic guidance. The system aims to serve as a universal front-end for multiple audio tasks including reconstruction, speech enhancement, voice conversion, ASR, and TTS. The core technical ideas are novel and the ablation study validates that both proposed components (SOP + RST) are jointly necessary for decoupling.

## Strengths

- **Explicit speech–BGS decoupling validated by controlled ablation**: Table 4 cleanly shows that using either SOP or RST alone yields SDR-B below -10 dB (no decoupling), while the joint use (Ablation-3) achieves SDR-B of 0.49 dB and SDR-S of 7.90 dB. This pinpoints the necessity of both components.

- **State-of-the-art speech enhancement from a codec model**: Table 2 reports that DeCodec achieves competitive or best DNSMOS scores compared to specialized SE models (Inter-SubNet, StoRM, SELM) on both synthetic and real test sets, demonstrating that representation-domain decoupling is a viable SE paradigm.

- **Unified multi-task capability in a single model**: The same DeCodec model handles audio reconstruction (Table 1), speech enhancement (Table 2), one-shot voice conversion with background removal (Table 3), and is shown (in the full version) to provide noise-robust features for ASR and controllable features for TTS — combining capabilities that previously required separate pipelines.

- **Improved noisy VC over cascaded separation+codec pipelines**: Table 3 shows DeCodec achieves WER 50.46% for one-shot VC on noisy speech vs. 52.73% for StoRM + SpeechTokenizer, suggesting that representation-domain decoupling introduces less signal distortion than front-end time-domain separation.

- **Causal variant with practical viability**: Both causal and non-causal versions are evaluated; the causal DeCodec-c maintains competitive performance (e.g., SDR 6.79 on clean speech, DNSMOS OVL 3.31), supporting real-time applicability.

## Weaknesses

### Major

1. **Uncontrolled bitrate in reconstruction comparisons (Table 1)**: DeCodec operates at 8 kbps (4+4 kbps for speech and BGS streams), while baselines use 2–6 kbps. Reconstruction quality (SDR, mel distance) is sensitive to bitrate, so the reported improvements could reflect the extra bits rather than the disentanglement architecture. A controlled comparison — either a standard codec at 8 kbps or a lower-bitrate DeCodec matching the baselines — is needed to support the claim that the system "maintains advanced signal reconstruction while decoupling representations."

2. **Overclaimed "universal" disentanglement — BGS reconstruction quality is poor**: The paper's central framing as a "universal disentangled representation learner" implies that both the speech and BGS subspaces are usable. However, the full model's best BGS reconstruction SDR (SDR-B) is -1.11 dB (DeCodec-c with SG, Table 4). No downstream task in the main paper demonstrates useful BGS *preservation* — all tasks focus on BGS *suppression*. The system is effective at discarding BGS but does not support faithful BGS reconstruction, making the "universal" claim significantly overstated relative to the evidence provided.

3. **SE evaluation relies solely on DNSMOS**: Table 2 uses only DNSMOS (a non-intrusive metric) for speech enhancement evaluation. Standard objective metrics in the SE literature — PESQ, STOI, SI-SDR — are absent. This makes it difficult to compare against prior SE work and limits the strength of the "superior speech enhancement" claim. (DNSMOS alone can be biased; the paper does not report any reference to these standard metrics anywhere.)

### Minor

4. **RST "proof" is not rigorous**: Section 3.6 presents a mean-value theorem argument as a theoretical proof that RST forces disentanglement, but the derivation assumes the decoder is approximately linear near quantized vectors and that the Jacobian does not depend on the speech representation — assumptions not justified for a deep neural network. The paper should either provide a more formal analysis (e.g., via mutual information) or clearly label this as an intuition, with the ablation study as the primary evidence.

5. **"Angular matrix" undefined (Section 3.4)**: The argument that orthogonality loss yields orthogonal projection matrices relies on the condition that YY^T "satisfies the angular matrix," a term introduced without definition or explanation. This makes the theoretical connection between the loss and the desired property unclear.

6. **Reference SIM of 0.69 unexplained (Table 3)**: The reference speech's self-similarity (SIM) is reported as 0.69, which is atypically low for a self-similarity measure. The paper provides no explanation for this value, making the VC similarity comparisons (where converted speech achieves 0.83, higher than the reference) difficult to interpret.

7. **No WER for noisy speech reconstruction (Table 1) and mel distance claim needs precision**: Table 1 reports WER only for clean speech, omitting noisy WER despite the paper's emphasis on noise robustness. Separately, the claim that DeCodec "outperforms … other baselines in noisy scenarios" for mel distance is imprecise — DAC achieves 0.69 vs. DeCodec's 0.81, so the statement should be qualified.

8. **SG-induced trade-off noted but not analyzed (Table 4)**: Adding semantic guidance reduces SDR-S from 7.90 to 5.70 and SDR-B from 0.49 to -1.11 while improving ASR WER from 41.9% to 25.8%. This trade-off is acknowledged but receives no discussion of whether reconstruction loss could be compensated (e.g., with more codebook entries or different bit allocation).

### Trivial

9. Typo "SOP vlock" (should be "block") in Section 4.2.4 (line 252).

## Nice-to-Haves

- **Demonstrate BGS preservation in a downstream task**: The most direct way to validate the "universal" claim is to show that the BGS representation alone can reconstruct background sound with meaningful quality (e.g., compare SDR-B against a standard separation model like Conv-TasNet) or evaluate a task such as TTS with environmental sound, where BGS preservation is valuable.
- **Control for bitrate**: Reduce DeCodec's total bitrate to match key baselines (e.g., 6 kbps) and re-run Table 1, or increase baseline codecs to 8 kbps. This isolates the effect of the architecture from the effect of additional bits.
- **Add standard SE metrics**: Report PESQ, STOI, and SI-SDR alongside DNSMOS for speech enhancement, enabling direct comparison with the cited SE baselines.
- **Compare against separation+codec cascade for reconstruction**: A pipeline that first separates speech and BGS (e.g., Conv-TasNet) then encodes each stream with a standard codec would quantify the advantage of avoiding front-end distortion.
- **Clarify the RST derivation**: Either provide a more rigorous information-theoretic analysis or explicitly state that the derivation is an intuition supported by the ablation study.

## Removed Points

*These points were raised in the input reviews but are not included in the main review, for the reasons stated.*

- **"ASR and TTS results not presented in main paper"**: The parser strips appendices, which in the original submission contain Appendix F (ASR) and G (TTS). The main paper references these experiments. This is not a weakness of the submitted paper.
- **"Stronger theoretical guarantee needed for RST"** (from Strength Finder): The claim that Section 3.6 provides a "formal derivation" or "theoretical guarantee" is inaccurate — the derivation is not rigorous. This strength was removed because it is factually inaccurate about the paper's content; the derivation is an intuitive argument, not a proof.
- **"Limitations should be in main text"**: The paper states that limitations are in Appendix H. This is a presentation choice, not a flaw in the paper's technical content.
- **Criticisms about missing related work citations**: The hard rules prohibit penalizing missing related works.
- **Formatting nitpicks and reproducibility complaints about undisclosed hyperparameters**: These are either parser artifacts or out of scope for a conference submission.

## Novel Insights

The two-reviewer synthesis surfaces a tension not explicitly discussed in the paper: the method demonstrably *separates* speech and BGS into distinct subspaces (validated by the ablation study), but the quality of the BGS subspace is far below what a task requiring BGS would need. This liminal space — useful separation but asymmetric reconstruction fidelity — is a recurring pattern in representation disentanglement work that the paper would benefit from acknowledging. The RST procedure, which swaps representations across independently sampled mixtures, is a genuinely clever technical device that could inform future work on unsupervised disentanglement in other domains.

## Suggestions

1. Temper the "universal" framing — position the method as a codec that provides controllable BGS suppression and semantic-paralinguistic decomposition, with the BGS subspace being a limited but useful auxiliary feature.
2. Add a same-bitrate baseline to Table 1 (either DeCodec at ~6 kbps or a standard codec at 8 kbps).
3. Add PESQ, STOI, and SI-SDR to the SE evaluation.
4. Define "angular matrix" or replace this reasoning with a more standard linear algebra argument.
5. Either strengthen the RST derivation or clearly label it as an intuition.
6. Explain the reference SIM of 0.69 and discuss why converted speech can exceed it.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>