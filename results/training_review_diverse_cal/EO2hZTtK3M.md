Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes CM², an audio-visual speech enhancement (AVSE) framework inspired by phonemic restoration. It introduces two types of contextual information — semantic context (via a Semantic Context Module, SeCM) and signal context (via a Signal Context Module, SiCM) — and fuses them across modalities using a Cross-Context Fusion Module (CCFM) that operates on both time and frequency dimensions. The paper reports large performance gains over prior SOTA, especially at very low SNR (-15 dB). The core motivation and architectural framework are well-conceived, but the empirical evidence does not yet match the scope of the claims, making the paper unsuitable for acceptance in its current form.

---

## Strengths

- **Novel, phonemic-restoration-inspired framework with two complementary context types.** The paper clearly articulates how semantic-level context (inferring missing content from semantic continuity) and signal-level context (exploiting frame-level coherence) are separately motivated by the phonemic restoration phenomenon, and designs distinct modules (SeCM, SiCM) for each. This distinction is absent in prior AVSE work and is a genuine conceptual contribution.

- **Multiple SeCM variants demonstrate robustness of the semantic context idea.** The paper explores three implementations of semantic context extraction: a scratch-trained visual module (SeCM_V), a frozen pre-trained visual-only module (SeCM_PV), and a frozen pre-trained audio-visual module (SeCM_PAV). The ablation (Table 2) shows that even the scratch-trained variant improves performance, indicating the benefit is not purely from large pre-trained models.

- **Informative ablations for semantic and signal context components.** The ablation on encoder layers of AV-HuBERT (Table 3) shows that mid-to-high layers outperform lower layers, consistent with the semantic-level motivation. The comparison of Bimamba vs. conformer for the SiCM (Table 4) further supports the design choice for signal context modeling. These ablations are well-designed and informative.

- **Large reported gains at very low SNR.** The method reports 63.6% relative SDR improvement, 58.1% PESQ, and 20.3% STOI at -15 dB SNR over prior SOTA. These are large enough to be practically meaningful — if the gains hold across datasets and after controlling for confounds.

---

## Weaknesses

### Fatal
None.

### Major

**1. Only one dataset's results are shown despite claiming comprehensive evaluation on four datasets.**
The abstract claims "Comprehensive evaluations across various datasets" and Contribution 3 states "Comprehensive evaluations on four composite datasets." Yet Section 4.1.1 lists four dataset pairs (LRS3+DNS4, GRID+CHiME3, TCD-TIMIT+NTCD-TIMIT, MEAD+DEMAND) and then immediately states: *"Due to space constraints, we only present the experimental results on the widely-used LRS3+DNS4 dataset here."* (line 216). This is a serious gap between claim and evidence. The reported gains at -15 dB are so large that the natural question is whether they generalize beyond one dataset+noise configuration. Even a compact table of key metrics for the remaining three datasets would dramatically strengthen the paper. Without it, the "comprehensive" claim is unsupported, and a reviewer cannot evaluate generalizability.

**2. The claim that visual information plays a critical role in the audio frequency domain is not experimentally validated.**
Contribution 2 states: *"we highlight and have experimentally validated the critical role of visual information along the audio frequency domain."* The CCFM includes separate time-domain and frequency-domain fusion blocks (Section 3.4), motivated by the idea that visual appearance (gender, body shape) correlates with audio frequency characteristics. However, no ablation isolates the effect of the frequency-domain fusion. The existing ablations cover SeCM variants (Table 2), encoder layers (Table 3), and SiCM vs. Conformer (Table 4), but none compares (a) CCFM with only time-domain fusion, (b) CCFM with only frequency-domain fusion, and (c) CCFM with both. Without this, the frequency-domain claim is a design hypothesis, not an experimentally validated finding. Given that this is highlighted as a contribution, the missing evidence is a significant gap.

**3. The large SOTA improvements may be confounded by the pre-trained AV-HuBERT backbone.**
The main results (Table 1) use SeCM_PAV, which is based on robust AV-HuBERT — a large model pre-trained on noisy speech and video. The baselines in Table 1 (AV-Conv-TasNet, DualAVSE, LAVSE, etc.) do not appear to use comparable pre-trained representations. The ablation in Table 2 does show that SeCM_V (scratch-trained) and SeCM_PV (visual-only frozen) also improve over the AOSE baseline, but these variants are not included in the main comparison table. A reader cannot tell whether the reported SOTA-beating numbers come from the proposed contextual modeling or from the pre-trained backbone. The paper needs either (a) a row in the main table with SeCM_V (or another weak variant) to bound the pre-training advantage, or (b) a demonstration that adding AV-HuBERT features to a strong baseline does not close the gap.

### Minor

- **Evaluation only covers negative SNRs.** The training and evaluation range is -15 dB to 0 dB (Section 4.1.2). While low-SNR performance is the paper's focus, the absence of results at positive SNRs (e.g., 5 dB, 10 dB) leaves unclear whether the method degrades performance in easier conditions. Since a practical system encounters a range of SNRs, this is a meaningful omission, though it does not threaten the paper's core claims about extreme-noise regimes.

- **The main comparison table does not include any CM² variant without the pre-trained backbone.** Including SeCM_V or SeCM_PV in Table 1 would give readers a sense of the range of performance and directly address the confound concern. The ablation table (Table 2) is a separate section, not the main comparison.

### Trivial
None.

---

## Nice-to-Haves

- **Multi-layer semantic feature fusion.** The paper observes (Table 3) that different encoder layers of AV-HuBERT capture different aspects of speech quality, and suggests multi-layer fusion could improve performance. Following through on this suggestion would strengthen the method.
- **Visualization of frequency-domain attention.** A plot showing which frequency bins are influenced by visual features in the frequency-domain fusion block would make the visual-frequency claim concrete and memorable.
- **Positive SNR evaluation.** Adding a few rows at 5 dB and 10 dB to Table 1.

---

## Removed Points

These points were flagged by reviewers but removed following the review synthesis rules:

- **"diverging diverging" typo and low-resolution figures** — Removed per formatting/style nitpick rule.
- **"The ablation on semantic layers does not improve the model"** — This is a missed opportunity, not a weakness. Moved to Nice-to-Haves.
- **Strength from Strength Finder: "Comprehensive evaluation across diverse datasets"** — Removed because it conflicts with the verified weakness that only one dataset's results are shown; the weakness wins.
- **"The paper should also cover more recent 2025 work"** — Removed per rule about missing related works and the fact that the reviewer has no external source to confirm existence.

---

## Novel Insights

The reviews surface an interesting tension: the paper's two-tiered context modeling (semantic + signal) is genuinely novel and well-motivated, but the paper simultaneously overclaims on two fronts (multi-dataset comprehensiveness and frequency-domain validation). The harsh critic correctly notes that the paper's claimed contributions outpace its evidence — yet the strength finder's analysis shows that when the overclaims are stripped away, the core framework still has genuine merit. This suggests the paper would benefit from retrenching: presenting the frequency-domain fusion as a design choice rather than a validated finding, and honestly reporting limitations about dataset scope. The most productive path forward is not to broaden the paper but to narrow its claims to match the evidence already presented, then add targeted experiments to support the remaining claims.

---

## Suggestions

1. **Show results for all four datasets.** Even a compact supplementary table with 3 metrics per dataset would address the single biggest weakness.
2. **Add an ablation isolating the frequency-domain fusion block.** Compare CCFM with both domains, time-only fusion, and frequency-only fusion. This directly tests the visual-frequency correlation claim.
3. **Include a non-pretrained variant in the main SOTA comparison table (Table 1).** Add a row for CM² with SeCM_V (scratch-trained) alongside the full model to disentangle the contribution of the contextual framework from the pre-trained backbone.
4. **Add positive-SNR results** (5 dB, 10 dB) to demonstrate no degradation in easier conditions.
5. **Reframe the frequency-domain claim** from "experimentally validated" to "designed to capture" until the ablation supports it.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>