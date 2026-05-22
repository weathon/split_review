Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

DeCodec proposes a neural audio codec that learns hierarchically disentangled representations: (1) speech vs. background sound via a Subspace Orthogonal Projection (SOP) module and Representation Swap Training (RST), and (2) semantic vs. paralinguistic information within speech via Semantic Guidance (SG). The goal is a single universal front-end that can serve reconstruction, speech enhancement, voice conversion, ASR, and TTS through controllable feature selection. The core idea — decoupling speech and BGS within a codec's latent space rather than via a separate front-end separation module — is genuinely novel and well-motivated by the limitations of cascaded pipelines.

## Strengths

- **Novel and well-motivated framework for in-representation-domain speech-BGS decoupling:** To my knowledge, DeCodec is the first neural codec that explicitly learns orthogonal subspaces for speech and background sound within its latent representation. The SOP module (two linear projections with orthogonality loss) and RST procedure (swap-train to enforce subspace-content correspondence) form a creative and principled combination. The ablation (Table 4) provides clear causal evidence: neither SOP alone (SDR-B = -13.15 dB) nor RST alone (SDR-B = -10.67 dB) achieves decoupling, but their combination (SDR-B = 0.49 dB, SDR-S = 7.90 dB) does, validating the design.

- **Competitive speech enhancement results without a dedicated SE model:** Table 2 shows DeCodec achieves the highest DNSMOS OVL (3.39), SIG (3.64), and BAK (4.13) on the without-reverb DNS test set, outperforming discriminative (Inter-SubNet), diffusion (StoRM), and transformer (SELM) baselines on most metrics. The causal variant (DeCodec-c) also performs well, suggesting practical utility. This is a genuine achievement — obtaining strong SE performance as a byproduct of representation design rather than through a task-specific model.

- **Clean ablation study isolating each component's contribution:** Table 4 systematically ablates SOP, RST, and SG with four conditions. The three-way SOP/RST ablation cleanly shows that both modules are necessary and complementary. Adding SG reveals a meaningful trade-off (decoupling quality vs. semantic retention) that, while downplayed in the text, is transparently presented in the data.

- **Broad task coverage and demonstration of versatility:** The paper evaluates on reconstruction, speech enhancement, one-shot voice conversion, ASR, and TTS (latter two in the appendix), demonstrating that a single codec representation can serve multiple downstream tasks without cascaded front-end processing.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed one-shot voice conversion performance:** The abstract and conclusion claim "effective one-shot voice conversion on noisy speech." Table 3 shows a WER of 50.46% — meaning more than half the words are incorrectly transcribed. This does not constitute "effective" by any reasonable standard. While the paper honestly reports the number and discusses the voicing-mismatch cause, the claims in the abstract and conclusion are not supported by the evidence. The comparison baseline (StoRM-SpeechTokenizer at 52.73% WER) is also poor, making the result competitive but not effective in an absolute sense. The authors should either (a) substantially improve VC performance, (b) remove the "effective" claim from high-level summaries, or (c) reframe the contribution as demonstrating hierarchical decomposition capability with the caveat that VC quality currently has significant limitations.

- **Reconstruction comparison confounded by uncontrolled bitrate:** Table 1 compares DeCodec (8 kbps: 4.0+4.0) against EnCodec (6.0 kbps), HiFi-Codec (2.0 kbps), DAC (4.5 kbps), and SpeechTokenizer (4.0 kbps). DeCodec's SDR advantage can be at least partially attributed to its higher bitrate. The paper claims DeCodec "maintains advanced signal reconstruction" while decoupling, but the comparison does not control for this confound. A controlled ablation with a reduced-bitrate DeCodec variant (e.g., lowering SRVQ or NRVQ layers to match ~4-6 kbps) is needed to isolate whether the decoupling design inherently preserves quality or whether the extra bits do the work. This does not invalidate the paper's core claim (decoupled representation learning) — but it weakens the secondary claim about reconstruction parity.

### Minor

- **The theoretical "proof" for RST (Section 3.6) is non-rigorous and should be reframed as intuition, not a proof:** The derivation applies the mean value theorem for vector functions to a decoder containing RVQ and nonlinearities, where differentiability is not guaranteed. The logical step "the left side depends on Zs₁ through ξ, while the right side is independent of Zs₁" does not constitute a formal proof of independence. This does not harm the paper's empirical contribution — Table 4's ablation is the real evidence — but presenting this as a proof is misleading. Reframe as a theoretical intuition or sketch.

- **The SG trade-off is understated:** The text describes adding SG as causing "a slight decrease in SDR" (Section 4.2.4). Table 4 shows SDR-B dropping from 0.49 to -1.11 (positive to negative) and SDR-S dropping from 7.90 to 5.70 (a 28% relative drop). These are material, not slight. The paper should honestly discuss this trade-off, even though SG's benefit (WER* dropping from 41.9% to 25.8%) may justify it.

### Trivial
- Table 1 would benefit from variance or confidence intervals, though this is not required for initial validation.
- The paper could include spectrogram visualizations to make the decoupling claim tangible to readers.

## Nice-to-Haves
- Evaluate a lower-bitrate DeCodec variant (e.g., reducing SRVQ or NRVQ layers) for a more controlled reconstruction comparison.
- Report PESQ/STOI/SI-SDR alongside DNSMOS for the SE evaluation to strengthen the metric set.
- Include a quantitative disentanglement metric (e.g., mutual information between Zs and Zn, or a classification probe on whether Zn contains speech information).

## Removed Points

These points from the input reviews are removed with justification:

1. **"SE comparison is not apples-to-apples"** (Harsh Critic Issue 5): The critique that DeCodec uses a different mechanism (BGS replacement with blank) than dedicated SE models does not invalidate the comparison — both are evaluated on the same task (enhance noisy speech) with the same standard metric (DNSMOS). The different mechanism is inherent to DeCodec's design. The DNSMOS results support the claim of competitiveness/advantage on most metrics. Removed as not a valid weakness.

2. **"Missing related work on representation learning for source separation"**: Per instructions, I cannot mention missing related works without external sources. Removed.

3. **"No variance or significance reported" / "Missing PESQ, STOI"**: DNSMOS is the standard for DNS Challenge evaluations. The lack of these metrics is a minor omission, not a structural weakness. The criticism about variance is a generic nitpick applicable to most papers in this area. Demoted to Trivial/Nice-to-Have.

4. **"Reference speaker SIM of 0.69 may mean 0.83 is inflated"**: This is a misunderstanding. The reference SIM (0.69) measures self-similarity between different utterances of the same speaker, which is expected to be lower than converted-to-reference similarity. Removed as incorrect.

5. **Strength Finder's "Theoretical justification" claim**: As verified, the RST proof (Section 3.6) is non-rigorous — the decoder's non-differentiability (RVQ, nonlinearities) invalidates the MVT application. This strength conflicts with a verified weakness and is removed.

6. **Generic/superficial strengths from Strength Finder** (e.g., "this paper addressed an important problem"): Removed as lacking specific evidence.

## Novel Insights

A genuinely novel observation from synthesizing the reviews is that the paper demonstrates a fundamental tension that any disentangled multi-stream codec will face: decoupling quality and bitrate allocation are inherently coupled. DeCodec's parallel RVQs (4.0 kbps each = 8 kbps total) are not wasteful — they are the mechanism by which two orthogonal subspaces each receive dedicated quantization capacity. This suggests that "fair" bitrate comparisons between entangled and disentangled codecs may be conceptually inappropriate; the right comparison is whether the *joint* value of decoupling + reconstruction at 8 kbps justifies the extra bits over an entangled codec at 6 kbps. The paper would benefit from explicitly making this argument rather than leaving it implicit in the bitrate-discrepant Table 1.

## Suggestions

1. **Revise the high-level claims about VC:** Replace "effective one-shot voice conversion" in the abstract and conclusion with language like "demonstrating hierarchical semantic-paralinguistic decomposition even in noisy conditions, though absolute VC quality (WER 50.46%) remains limited and requires further improvement."

2. **Add a controlled bitrate ablation:** Evaluate a DeCodec variant with reduced bitrate (e.g., fewer RVQ layers or lower-dimensional codebooks) to produce a version at ~4-6 kbps total, and compare reconstruction metrics with baselines at similar bitrates. This would isolate the effect of the decoupling design.

3. **Reframe Section 3.6's "proof" as intuition:** Replace "we theoretically prove" with "we provide a sketch showing the intuition" and acknowledge the non-differentiability of the decoder as a limitation of the formal argument.

4. **Characterize the SG-decoupling trade-off more honestly:** Replace "slight decrease in SDR" with explicit quantification (e.g., "SG reduces SDR-B by 1.6 dB and SDR-S by 2.2 dB relative to SOP+RST alone, but improves WER* by 16.1 points — a trade-off users should consider when selecting configurations").

## Score and Decision

### Calibration Anchors

All anchors from the batch are listed below for comparison:

| Path | Avg Score | Comparison to DeCodec |
|------|-----------|----------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uxDFlPGRLX.md` (FlowDec) | 7.00 | A stronger, more polished codec paper with rigorous experiments. DeCodec is more novel in concept but weaker in execution and calibration. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LfDUzzQa3g.md` (RepCodec) | 5.50 | Similar tier — both have a simple core idea with decent experiments. DeCodec is more ambitious and addresses a harder problem. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/anQDiQZhDP.md` (Vevo) | 5.50 | Comparable quality. Vevo has cleaner execution on its chosen tasks; DeCodec covers more tasks but with uneven results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Id2JMVSQHZ.md` (USC) | 4.80 | Similar topic (disentangled codec). DeCodec has better experimental validation and more honest data presentation (despite overclaims). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xJc3PazBwS.md` | 3.75 | Weaker paper on a related topic. DeCodec is stronger in both novelty and evidence. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UFwefiypla.md` (DM-Codec) | 3.00 | Much weaker execution. DeCodec is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gpKEDj9Dgg.md` | 2.00 | Incomplete paper, far weaker than DeCodec. |

The paper has genuine novelty (first codec-level speech-BGS decoupling), solid empirical support for its core design (Table 4 ablation), and competitive SE results. However, it is marred by overclaims (VC), an uncontrolled bitrate comparison, and a non-rigorous theoretical justification. It compares most closely to the ~5.5 anchor papers (RepCodec, Vevo) but has more significant issues with claim-evidence alignment. Relative to the strong FlowDec paper (7.0), the execution gap is clear.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>