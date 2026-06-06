---

## Summary

USR 2.0 presents CTC-driven teacher forcing as a replacement for autoregressive pseudo-label generation in Unified Speech Recognition (USR), feeding the teacher's greedily decoded CTC outputs into the attention decoder for a single-pass generation of attention-based pseudo-labels. Combined with a mixed sampling strategy (50% AR mode) to mitigate exposure bias, the resulting framework achieves approximately 2× training speedup, substantially improved out-of-distribution (OOD) robustness across long utterances, noisy audio, and cross-dataset evaluations, and state-of-the-art in-distribution WERs on LRS3/LRS2/WildVSR—all within a single unified model for ASR, VSR, and AVSR.

---

## Strengths

- **~2× training speedup across model scales, empirically verified**: Figure 5 shows USR 2.0 reaching the same VSR WER in roughly half the wall-clock time for Base (LRS3), Base+ (LRS3+Vox2), and Large (LRS3+Vox2) settings. The speedup is attributed both to faster per-step computation (parallel attention PL generation) and faster convergence (50 vs. 75 epochs).

- **Dramatic OOD robustness improvements across multiple axes**: Figure 3a shows USR WER rising to ~80–100% at 500–600 frames while USR 2.0 stays flat; Table 1 shows consistent superiority under babble noise from 10 dB to 0 dB; Table 3 shows large cross-dataset gains (e.g., LibriSpeech WER 15.4% vs. 25.3% for USR under greedy decoding). These improvements span long utterances, noise, and domain shift simultaneously.

- **Tight, informative ablations directly support design choices**: Table 4 isolates contributions cleanly: removing CTC supervision from the decoder raises OOD WER from 24.2% to 35.1% (CTC-driven mode, row 2), while removing attention-based targets raises ID WER from 3.2% to 3.6% (row 4), directly confirming that each component serves a distinct role.

- **Mixed sampling study provides a well-calibrated trade-off curve**: Figure 4 shows that OOD performance is stable for AR sampling probabilities from 0.0 to ~0.6 but degrades sharply approaching 1.0, while ID performance improves monotonically with more AR. This cleanly justifies the default choice of 0.5 and provides practitioners with actionable guidance for tuning.

- **State-of-the-art in-distribution results with a unified model**: Table 2 shows USR 2.0 matching or surpassing modality-specific self-supervised baselines across low- and high-resource settings. The scaled Huge model achieves 17.6%/0.9%/0.8% VSR/ASR/AVSR on LRS3—new SOTA with a single model.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theoretical argument in Section 4.1 is stronger for incoherence than for incorrectness under OOD conditions.** The "Global coherence" paragraph argues that "global incoherence does not hinder learning" because teacher and student share the same CTC-derived prefix, making knowledge transfer stable. This is convincing when CTC errors are benign (blank removal, repetition artifacts). Under genuine OOD distribution shift, however, CTC may produce recognition errors, and a wrong CTC prefix will produce systematically misconditioned attention pseudo-labels that are not merely incoherent but incorrect. The paper partially addresses this via mixed sampling (Section 4.2 states: "CTC's conditional-independence assumptions may also occasionally yield imperfect CTC predictions on challenging, in-distribution segments"), but the quantitative exposure to this failure mode under heavy OOD shift is not characterized. The empirical results in Table 3 and Figure 3 validate the approach, but the theoretical justification in Section 4.1 does not fully account for this case. A brief concrete argument—e.g., that the token-wise cross-entropy gradient depends on per-position conditional distributions rather than on the sequence-level correctness of the prefix—would make the core claim more airtight.

- **Inconsistent inference protocol across evaluation tables.** Table 2 (in-distribution LRS3) uses beam size 40 with joint CTC-attention decoding; Table 1 (noise robustness) uses beam size 30; Table 3 (OOD datasets) uses greedy decoding. The paper notes that greedy decoding is appropriate for pseudo-labelling, which is a reasonable justification, but the OOD and noise robustness improvements are reported under different protocols. Figure 3 already shows both greedy and beam search results for long utterances—extending beam-search results to Table 3 or Table 1 would allow a direct assessment of whether robustness gains persist at inference-relevant decoding quality.

### Trivial

- **Speculative extensions in Section 8.** The conclusion briefly mentions handwriting recognition, music transcription, and DNA/protein sequencing as potential applications. These domains have fundamentally different noise profiles and alignment structures; the transferability of CTC-driven teacher forcing is non-trivial. This is standard forward-looking discussion but is too brief to be substantive.

---

## Nice-to-Haves

- A qualitative analysis of cases where CTC-driven PLs and AR PLs diverge (e.g., showing specific examples where CTC errors propagate into attention pseudo-labels vs. where they are corrected) would make the theoretical account in Section 4.1 more concrete and convincing.
- Reporting both greedy and beam-search WER for Table 3 and Table 1 (analogous to Figure 3's dual presentation) would unify the evaluation story and clarify how much of the robustness benefit persists at full inference quality.
- Standard deviations across training runs for key results in Tables 1–3 would strengthen confidence in smaller gains (e.g., 2.5% vs. 2.4% ASR WER in Table 2).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Whisper oracle reliability in Figure 3 and Table 3 (harsh critic, framed as major):** The critic notes that Whisper has a length-dependent error profile that could introduce correlated noise into the WER axis of Figure 3. While technically true, since both USR and USR 2.0 are evaluated against the same Whisper references, systematic bias cancels in the relative comparison. The qualitative finding—USR 2.0 is more robust to longer inputs—is sound. Demoted and effectively removed as a standalone weakness; not worth noting given the comparative nature of the experiment.

- **Missing standard deviations (harsh critic):** Requesting variance estimates across pseudo-labelling runs is a non-standard demand for large-scale semi-supervised speech recognition, where single-run evaluation is the community norm. Moved to Nice-to-Haves.

- **Gray-highlighting inconsistency in Table 4 (harsh critic):** Purely a presentation nitpick. Removed per hard rules.

- **Conclusion "puffery" about DNA/protein sequencing (harsh critic):** This is standard speculative discussion in a conclusion section and does not affect the paper's contributions. Moved to Trivial.

- **Strength Finder: "addresses an important problem" style generic claims** — filtered per instructions; only specific, evidence-backed strengths retained above.

---

## Novel Insights

The core insight that CTC-driven teacher forcing is effective precisely *because* coherence is unnecessary in pseudo-labelling—when teacher and student share the same forced input, the student learns a stable mapping from a coherent CTC prefix to the teacher's conditional next-token predictions, without needing the output sequence to be globally coherent—is the paper's most conceptually original contribution. This reframes what has traditionally been viewed as a limitation of non-autoregressive models (lack of sequential dependencies) as an asset in self-training: the separation of the coherent conditioning signal (CTC prefix) from the per-position prediction target allows the attention decoder to learn robust conditional representations without being exposed to cascading AR errors during pseudo-label generation. The coupling mechanism—where CTC and attention supervision become aligned and jointly predict the same length sequence—is an elegant byproduct that also explains the OOD robustness gains beyond mere speedup.

---

## Suggestions

1. Add a brief paragraph in Section 4.1 explicitly characterizing the case of CTC recognition errors (not just incoherence artifacts): show analytically or empirically that token-wise cross-entropy under a partially incorrect CTC prefix still produces useful gradients, or bound the degradation relative to a perfect prefix. This would close the main theoretical gap.

2. Extend Figure 3's dual greedy/beam-search presentation to Table 3 (at minimum) to allow readers to assess whether OOD gains persist at inference-quality decoding.

3. Consider adding a short qualitative example table (possibly in an appendix) contrasting CTC PLs, CTC-driven attention PLs, and AR PLs on a few OOD samples—this would make the method's mechanism tangible and support the intuitions in Section 4.1.

---

## Evaluation on Key Axes

- **Originality**: The CTC-driven teacher forcing idea is novel and elegant within the semi-supervised speech recognition setting, though it builds incrementally on USR. The key insight—that PL coherence is unnecessary when conditioning is matched—is a genuine conceptual contribution. *Moderate-high.*
- **Importance of research question**: OOD robustness and training efficiency for unified multimodal speech recognition are practically significant and under-explored in the semi-supervised setting. *High.*
- **Claims well-supported**: Yes. The ~2× speedup claim, OOD robustness claims, and in-distribution SOTA claims are all backed by multiple tables and figures with clear comparisons. Ablations directly attribute gains to specific design choices. *Strong.*
- **Soundness of experiments**: Comprehensive evaluation across noise, length, and domain shift; ablations are tight; multiple model scales tested. Minor concern around inconsistent decoding protocols across tables. *Strong with one caveat.*
- **Clarity of writing**: The paper is clearly structured, with well-motivated problem setup, clean mathematical presentation, and honest discussion of trade-offs. *High.*
- **Value to research community**: High practical value. Faster, more robust semi-supervised training for unified speech recognition is directly deployable, and the CTC-driven TF paradigm is likely applicable beyond AVSR. *High.*

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>