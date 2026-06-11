## Summary

USR 2.0 proposes CTC-driven teacher forcing for pseudo-labelling in unified speech recognition, replacing the slow autoregressive (AR) decoding of USR with fast, parallel CTC-based generation of attention targets. A mixed-sampling strategy intermittently reintroduces AR decoding to mitigate exposure bias. The method achieves ~2× training speedup, strong out-of-distribution robustness (particularly on long utterances, noise, and cross-dataset shifts), and state-of-the-art or competitive results across ASR, VSR, and AVSR with a single unified model at multiple scales.

## Strengths

1. **Well-motivated, clearly explained core idea with a non-trivial insight.** The paper identifies a real bottleneck (AR decoding at every training step) and a structural weakness (decoupled CTC/attention supervision that compounds OOD errors) in the existing USR framework. The proposed fix — feeding greedily-decoded CTC outputs into the decoder via teacher forcing — is simple, directly addresses both problems, and is justified by the key insight that global coherence is unnecessary in pseudo-labelling because teacher and student share the same conditioning (Section 4.1, lines 109–110). This insight is correctly reasoned and elevates the contribution beyond a straightforward engineering tweak.

2. **Strong OOD robustness demonstrated systematically across three distribution-shift dimensions.** The paper evaluates length (Figure 3a: USR 2.0 maintains ~35% WER at 600 frames where USR reaches ~100%), noise (Table 1: consistent gains at all SNR levels from 10 dB to −5 dB for both ASR and AVSR), and dataset shift (Table 3: 15.4% vs. 25.3% on LibriSpeech, 73.7% vs. 80.0% on WildVSR under greedy decoding). The beam-size sweep (Figure 3c) shows the robustness is structural, not dependent on expensive search — USR 2.0 with greedy decoding outperforms USR with large beams. This combination of breadth and magnitude is the paper's strongest empirical contribution.

3. **Clean ablation study that directly validates the causal claims.** Table 4 isolates the effect of each pseudo-label type in each mode. Removing CTC supervision from the decoder in CTC-driven mode degrades OOD from 24.2%→35.1%; removing attention targets degrades ID from 3.2%→3.6%. The large gap between CTC-driven mode (24.2% OOD) and AR-only mode (40.1–45.1% OOD) independently validates the core claim without relying on the Whisper proxy used elsewhere — strengthening confidence that the robustness is real and structurally explained. Figure 4's sweep of mixed-sampling probability produces a clean U-shaped OOD curve matching the expected trade-off. This is a well-executed ablation.

4. **State-of-the-art or competitive results across all three modalities with a single unified model, demonstrated at multiple scales.** Table 2 shows consistent improvements over USR and all modality-specific baselines across model sizes and resource settings (e.g., Large: 21.5% VSR, 1.3% ASR, 1.0% AVSR vs. BRAVEn's 26.6% VSR, 1.2% ASR — with shared parameters). The Huge model (17.6/0.9/0.8) demonstrates scalability to ~2500 hours of unlabelled data. The efficiency gain (~2× faster training, Figure 5) is a concrete practical benefit that stands independently of any WER improvement.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or confidence intervals reported for any WER number.** Every value in every table is a single point estimate. For the small-gap in-distribution comparisons (e.g., Table 2, Base LRS3: VSR 36.0→36.2 regression; ASR 3.2→3.0; AVSR 3.0→2.9 — all differences ≤0.2%), it is impossible to distinguish meaningful improvement from run-to-run noise. The large OOD gaps (e.g., 15.4% vs. 25.3% in Table 3) are clearly robust to this concern, but the paper's in-distribution narrative partly rests on these small differences, and the absence of basic uncertainty quantification weakens that evidence. Comparably-scored papers in this space (e.g., Align With Purpose at ICLR 2025, avg 7.0) report standard deviations.

2. **OOD evaluations use Whisper transcriptions as proxy ground truth without discussing the confound.** Sections 5.1 and 5.3 evaluate on VoxCeleb2, AVSpeech, and LibriSpeech using Whisper transcriptions as ground truth. The reported "WER" is actually a measure of *disagreement* between each model and Whisper. The paper does disclose that Whisper is used "as an oracle" (line 192), but does not discuss whether the improvements could partly reflect alignment with Whisper-specific error patterns rather than true WER. This concern is bounded — it affects all compared methods equally, and the in-distribution results (real labels) independently show gains — but the headline OOD numbers would benefit from an explicit caveat about this proxy.

### Minor

1. **Huge model results use a different training setup than the comparisons they sit alongside.** The Huge row in Table 2 uses LRS2+LRS3 labelled data (vs. just LRS3 for the other rows) and AVSpeech unlabelled data in addition to Vox2. This is flagged with a footnote, but placing the Huge row in the same comparison block invites apples-to-oranges reading. The Huge results are impressive on their own terms but belong in a separate table or with a clearer visual separation.

2. **One low-resource metric regresses slightly.** In Table 2 (Base, LRS3 only), VSR WER goes from 36.0 (USR) to 36.2 (USR 2.0), a 0.2% regression. The paper's characterization "matches or outperforms the state of the art" (line 273) is fair overall, but this cell is a counterexample to the claim that robustness gains "translate to better in-distribution performance" (line 48). Acknowledging this directly would improve accuracy without weakening the paper.

3. **No limitations section.** The paper identifies limitations of USR but does not discuss its own. Relevant items: the method requires a CTC head (not applicable to attention-only models), mixed sampling still requires occasional AR decoding, all experiments use English-only data. A brief limitations paragraph would improve scholarly completeness.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment that equalizes training epochs between USR and USR 2.0 beyond the 50 vs. 75 already noted (Appendix C.5) to further isolate the method's contribution from the speed benefit.
- A brief discussion of the Whisper proxy limitation and why the relative rankings are likely valid despite it.

## Removed Points
These points were flagged for removal; treat with caution.
- **"~40x faster" vs. actual 36x**: The harsh critic computes 0.471/0.013 ≈ 36.2 and questions the "~40x" claim. "~40x" is a reasonable order-of-magnitude approximation for 36x; this is a trivial nitpick and was removed.
- **Training time evidence limited to Figure 5**: The critic claims the abstract's "halves training time" is only supported by one configuration. The paper states the speedup applies across settings (line 275) and Figure 5 covers multiple configurations and model scales. The critic's characterization is not accurate.
- **Missing appendix/proofs**: Removed per instructions — these sections exist in the original submission but are stripped by the parser.
- **Missing related work**: Removed per instructions — I cannot verify the existence of omitted works.
- **Formatting/style nitpicks**: Removed per instructions.

## Novel Insights
The reviews surface an interesting tension: the paper's headline OOD robustness rests partly on a Whisper-proxy evaluation that could theoretically contain a confound, while its cleanest controlled evidence (in-distribution Table 2) shows more modest gains. The ablation study (Table 4) bridges these two bodies of evidence: the large gap between CTC-driven mode (24.2% OOD) and AR-only mode (40.1–45.1% OOD) uses the *same* evaluation protocol and independently validates the core claim without relying on the Whisper proxy. This suggests the OOD robustness is real and structurally explained even if the proxy-based absolute WER numbers shift. The mixed-sampling analysis (Figure 4) further shows the robustness-efficiency trade-off is a clean, tunable knob rather than a brittle hyperparameter — a practical insight that neither review fully connected to the paper's deployability argument.

## Suggestions
1. **Add variance reporting** (standard deviation or confidence intervals) for at least the key in-distribution comparisons (Table 2, small-gap settings) and the ablation study (Table 4).
2. **Add a limitations paragraph** to Section 8 or a new section, covering: (a) CTC head requirement, (b) reliance on occasional AR decoding, (c) English-only evaluation.
3. **Clearly separate the Huge model results** from the standard comparison rows in Table 2, or move them to a separate table with explicit caveats about the different training setup.
4. **Add a brief caveat** in Sections 5.1 and 5.3 noting that OOD evaluations use Whisper transcriptions as a proxy, and while relative rankings are unaffected, absolute WERs should be interpreted with this in mind.
5. **Acknowledge the VSR regression** on Base LRS3 directly in Section 6, clarifying that the main in-distribution gains come from larger unlabelled data regimes.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| UFwefiypla.md (DM-Codec) | 3.00 | R1 | Much weaker — dataset paper, rejected |
| aOPTDchLBz.md (ivrit.ai) | 2.50 | R1 | Much weaker — dataset paper, rejected |
| 4lOWCkhr4g.md (Cross-Lingual PL) | 5.25 | R1 | Weaker — limited novelty, narrower scope |
| eSO9quCgmz.md (Rethinking PL) | 5.00 | R1 | Weaker — general SSL, not speech-specific |
| CIs9x2ZRgh.md (CR-CTC) | 6.75 | R1, R2 | Weaker — ASR-only, simpler method, mixed reviews |
| fUGhVYPVRM.md (Align With Purpose) | 7.00 | R1 | Comparable — similar quality, reported std (which USR 2.0 lacks) |
| FyMjfDQ9RO.md (Sylber) | 6.75 | R1, R2 | Different task (speech representation), comparable quality |
| WEQL5ksDnB.md (CAV2vec) | 6.75 | R2 | Weaker — novelty concerns (similar to AV-HuBERT) |
| M8J0b9gNfG.md (Multilingual VSR) | 6.20 | R2 | Weaker — mainly scaling existing methods |
| dnqPvUjyRI.md (SemiReward) | 6.00 | R2 | Weaker — general SSL, not speech recognition |
| TtKN1TpvUu.md (T2V2) | 6.25 | R2 | Different task (unified ASR/TTS) |
| 3tukjsVyrE.md (Scaling Speech-Text) | 7.00 | R2 | Different task (speech-language models) |
| tyEyYT267x.md (Interpolating AR/DD) | 8.00 | R1 | Stronger — consensus strong accept |
| RvUVMjfp8i.md (Realistic SSL Eval) | 8.00 | R1 | Stronger — consensus strong accept |

**Round 1 bracket: 6.0–7.5.**
**Round 2 narrowing:** USR 2.0 is clearly stronger than CR-CTC (6.75), CAV2vec (6.75), and Multilingual VSR (6.20); comparable to Align With Purpose (7.0) but lacking its variance reporting. It does not reach the consensus 8.0 level.

**Final score: 7.0.** The paper makes a clear, well-validated contribution to a practically important problem. The two major weaknesses (no variance reporting, OOD proxy without caveat) are real but bounded — the large OOD gains dwarf the variance concern, and the ablation study independently confirms the causal mechanism. The paper would be strengthened by addressing these in a revision but they do not undermine acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>