## Summary

CCAT proposes a two-stage framework for mitigating modality imbalance in multimodal learning. In Stage 1, a shared classifier is pretrained with bidirectional cross-attention and mutual-information-based contribution regularization to produce an "unbiased" initialization. In Stage 2, this classifier is frozen during modality-alternating encoder training, with lightweight per-modality LoRA adapters bridging the distribution shift from fused to unimodal features; a sample-level secondary update mechanism further targets severely imbalanced instances. CCAT reports state-of-the-art results on three benchmarks (CREMA-D, Kinetic-Sound, MVSA).

---

## Strengths

- **Consistent and substantial empirical improvements across three benchmarks**: Table 1 shows CCAT outperforming all baselines, with +6.76% over LFM on Kinetic-Sound, +1.35% on CREMA-D, and +1.92% on MVSA versus MMPareto. Gains hold across both multimodal and unimodal evaluation columns, suggesting genuine balance improvement rather than cherry-picked metrics.

- **Novel classifier-centric framing**: Prior alternating-training approaches (MLA, Reconboost) focus on encoder-level interference. CCAT is distinct in targeting structural bias in the *classifier* as the residual bottleneck. Figure 1's contribution-tracking experiment (CCAT reaching 0.65/0.35 vs. MLA's 0.90/0.10) directly motivates this view with empirical evidence.

- **Component-wise ablation with clear patterns**: Table 2 shows that removing classifier freezing, alternating training, secondary updates, or LoRA each degrades multimodal accuracy. The joint configuration consistently outperforms all ablated variants, confirming that each design element contributes independently.

- **Sample-level secondary update is clearly effective**: Table 2 shows removing secondary updates (Sec: ✗) drops CREMA-D Multi from 85.89% to 83.06% and KS Multi from 79.29% to 78.25%, a consistent ~1.0–2.0% improvement from re-optimizing severely imbalanced samples identified via contribution scores (Eq. 6–7, Algorithm 1 lines 11–15).

- **Quantitative feature-space analysis beyond classification accuracy**: Figure 5 provides t-SNE visualizations alongside Calinski-Harabasz (CH), Silhouette (SH), and Davies-Bouldin (DB) metrics. CCAT achieves CH=242.55, SH=0.24, DB=1.28 versus MLA's CH=198.98, SH=0.19, DB=1.42, offering an independent signal that the frozen classifier fosters more discriminative representations.

---

## Weaknesses

### Fatal
None.

### Major

- **The ablation cannot isolate the frozen-classifier mechanism from the pretrained initialization.** Table 2's "Fix: ✗" ablation row unfreezes the classifier but still starts from the *pretrained, regularized* classifier (Section 3.2). There is no row testing "freeze a vanilla (non-pretrained) classifier + alternating training + LoRA." The paper's central interpretive claim—that *freezing* is the operative mechanism preventing bias entrenchment—therefore cannot be confirmed by the ablation. Both the unbiased initialization (from bidirectional cross-attention + MI regularization) and the freezing mechanism are confounded. The "Fix: ✗" degradation (85.89% → 82.80% on CREMA-D Multi) could plausibly reflect the loss of a stable pretrained anchor rather than anything inherent to freezing itself.

- **No computational cost comparison despite an additional pretraining stage.** Baselines MLA, MMPareto, and LFM do not include a full additional pretraining phase with bidirectional cross-attention and a separate training schedule. CCAT's gains over these methods may be partly attributable to additional effective training and richer fusion during pretraining, not only to the frozen-classifier insight. The paper reports no wall-clock time, FLOPs, or epoch-count breakdown, making it impossible to assess whether the gains are cost-efficient relative to simply training longer or adding a pretraining stage without the specific CCAT design choices.

### Minor

- **LFM is missing from the MVSA comparison without explanation.** Table 1 shows "-" for LFM on MVSA. Since CCAT outperforms LFM on both other datasets, the omission weakens the completeness of the MVSA comparison and may leave readers wondering whether LFM was not applicable, not reproducible, or simply not run on that benchmark.

- **The theoretical analogy between class and modality imbalance is informal and somewhat overstated.** Section 3.1 presents Eq. (3) — which assumes $f = \gamma_1 f^{(1)} + \gamma_2 f^{(2)}$ with "implicitly learned modality utilization coefficients" — as the basis for a "unified theoretical framework" and "a proof of their underlying similar[ity]." However, this linear approximation does not correspond to the actual architecture (which uses cross-attention fusion during pretraining and decision-level fusion at inference). The analogy is useful for motivation but is not a formal proof; the framing in the Section 3.1 header ("provides a proof") overstates its rigor.

- **The LoRA distribution-shift claim is only partially supported.** Section 3.3 explicitly acknowledges the mismatch between pretraining (classifier trained on cross-attention fused features $\mathbf{f}_i$) and inference (classifier applied to unimodal features $\mathbf{z}^m$ with LoRA correction). LoRA removal on CREMA-D Multi yields a modest degradation: 85.89% → 84.68% (Table 2). Whether rank-2 or rank-8 LoRA truly closes a cross-modal-fusion-to-unimodal distribution gap, or whether the system simply learns to tolerate it, is not analyzed. This does not undermine the overall results but leaves the motivation for LoRA partially unverified.

### Trivial

- **Figure 4 caption states "MVSA shows a peak at β=0.25 (80.54%)" but the underlying data table in the same figure shows MVSA peaks at β=0.05 (80.73%).** The implementation details also confirm β=0.05 for MVSA and the reported MVSA result (Table 1) is 80.73%. The caption is internally inconsistent with the data; this should be corrected.

---

## Nice-to-Haves

- An ablation row testing a *frozen but non-pretrained* (randomly initialized, or jointly trained without MI regularization) classifier would directly isolate the freezing mechanism from the unbiased initialization. This is the most important experiment to add given the current confound in Table 2.
- A tracking experiment showing gradient norm contributions from each modality's encoder to the classifier, as a function of whether the classifier is frozen or not, would directly validate the mechanistic gradient-suppression narrative in Section 3.1 without relying solely on contribution values measured at the feature level.
- Wall-clock training time or total FLOPs relative to MLA, LFM, and MMPareto would clarify the practical cost of the added pretraining stage.
- Testing on a dataset with more symmetric modality quality would help characterize when CCAT's constraints help vs. over-regularize.

---

## Removed Points

*These points were considered but filtered; treat with caution.*

- **"Inference on unimodal features contradicts pretraining motivation" (Harsh Critic, framed as structural incoherence):** The paper explicitly acknowledges this gap at the start of Section 3.3 and introduces LoRA specifically to address it. The paper's motivation for pretraining is to obtain an unbiased classifier anchor, not to permanently fuse at inference. This is an addressed design tension, not an unacknowledged contradiction. Demoted from Major to a minor concern (already noted above).

- **"Abstract claim that CCAT prevents dominance is too strong given 0.65/0.35 remaining imbalance" (Harsh Critic):** The abstract says "preventing bias toward any modality" and the introduction says "preventing bias toward any modality." The 0.65/0.35 vs. 0.90/0.10 comparison in Figure 1 is a dramatic improvement and the paper frames this as a reduction, not elimination. This reads as a legitimate improvement rather than a false claim; the distinction is minor and does not affect the empirical contributions.

- **"Sequential grid search creates misleading two-table presentation" (Harsh Critic, re: Table 3 vs. Figure 4 MVSA numbers):** Table 3 reports the best LoRA rank at r=8 for MVSA (79.58%), while Figure 4 then shows the threshold grid at r=8 giving 80.73% at β=0.05. The implementation details explicitly state the final configuration (r=8, β=0.05) and the final result (80.73%). Sequential search naturally produces intermediate numbers; this is not misleading given the stated procedure.

- **"Testing on datasets with more symmetric modalities" (Harsh Critic, scope extension):** CCAT is evaluated on three established benchmarks covering different modality pairs. Requesting additional datasets is a scope extension beyond the paper's contribution.

- **Strength Finder strength: "Novel theoretical unification [provides rigorous motivation]":** Partially removed — the analogy is useful as motivation but is not formally rigorous (see Minor weakness above). Kept as supporting motivation rather than a core strength.

---

## Novel Insights

The paper's most interesting conceptual contribution is the observation that modality imbalance and class imbalance share a common gradient-suppression mechanism mediated through the shared classifier — and the corresponding strategy of anchoring the classifier externally (by pretraining and freezing it) rather than intervening on encoder gradients. This reframes alternating training failures as a classifier-entrenchment problem rather than an encoder-interference problem. While the theoretical derivation is informal, the empirical Figure 1 data — showing that alternating training alone barely changes the contribution ratio while CCAT dramatically reduces it — supports the view that classifier dynamics are the binding constraint. The LoRA adapter design (per-modality low-rank corrections to a frozen shared classifier) is an elegant engineering response to the distribution-shift problem created by this approach, though its adequacy is only partially validated.

---

## Suggestions

1. **Add the critical ablation**: "Freeze a randomly initialized or jointly trained (non-regularized) classifier + alternating training + LoRA" as a Table 2 row. If this performs similarly to the full CCAT, the unbiased initialization is not critical; if it collapses, reframe the contribution as the combination of pretraining + freezing rather than freezing alone.
2. **Report training cost**: Include wall-clock time per run, or total training epochs (pretraining + alternating), for CCAT vs. MLA, LFM, and MMPareto.
3. **Correct the Figure 4 caption**: Change "MVSA shows a peak at β=0.25 (80.54%)" to "β=0.05 (80.73%)" to match the data table and implementation details.
4. **Clarify LFM omission on MVSA**: Either report the LFM result or explain in a footnote why it was omitted (e.g., method incompatibility with text-image data or unavailable implementation).
5. **Soften Section 3.1 framing**: Replace "provides a proof of their underlying similar[ity]" with "provides an informal illustration of their optimization-level analogy" to accurately represent the formality of the argument.

---

## Score and Decision

**Originality**: 3/5 — The classifier-centric framing for modality imbalance is genuinely novel in the alternating training setting; LoRA adaptation to a frozen multimodal classifier is creative. The individual components (LoRA, MI-based contribution scoring, alternating training) are borrowed, but their combination and motivation are new.

**Importance of Research Question**: 4/5 — Modality imbalance is a well-recognized bottleneck; addressing its classifier-level component is a meaningful and underexplored direction.

**Claims Supported**: 3/5 — Empirical claims (state-of-the-art accuracy) are well-supported. The mechanistic claim (freezing, not just initialization, is the key) is not cleanly isolable from the ablation.

**Soundness of Experiments**: 3/5 — Three benchmarks, three seeds, ablations covering all components. Main gap: confound between pretraining and freezing in the ablation; no cost normalization.

**Clarity of Writing**: 3/5 — Generally clear structure. Minor inconsistencies (Figure 4 caption, Table 3 vs. Figure 4 intermediate numbers) slightly reduce readability.

**Value to Research Community**: 4/5 — Offers a practical method with consistent gains; the classifier-freezing paradigm may inspire follow-up work in multimodal settings.

The paper makes a real, novel contribution with strong empirical support, but the central mechanistic story is not fully verified by the ablation. This is a meaningful limitation that the authors could address in rebuttal with one targeted experiment. The paper is at the borderline between weak accept and accept; the empirical strength tips it toward acceptance with required revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>