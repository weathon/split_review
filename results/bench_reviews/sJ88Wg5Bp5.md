Now let me run calibration search:Now I have enough information to write the consolidated meta-review.

---

## Summary

ViDA proposes a dual-adapter approach for Continual Test-Time Adaptation (CTTA) that decomposes adaptation into a low-rank branch (capturing domain-shared/general knowledge to mitigate catastrophic forgetting) and a high-rank branch (capturing domain-specific knowledge to mitigate error accumulation), governed by a Homeostatic Knowledge Allotment (HKA) strategy that dynamically weights each branch per-sample based on uncertainty. Experiments span four benchmarks—ImageNet-C (both ViT-Base and ResNet50), CIFAR10C/100C, Cityscapes-to-ACDC segmentation, and foundation models (DINOv2, SAM)—with consistent gains over prior work.

---

## Strengths

- **Principled dual-adapter design backed by complementary empirical evidence.** Low-rank adapters exhibit lower inter-domain JS divergence across all 14 domain shifts (Fig. 2a), while high-rank adapters achieve lower intra-class divergence within individual domains (Fig. 2b). t-SNE plots (Fig. 1b) and CAM visualizations (Fig. 3) corroborate this decomposition. The design directly maps onto two distinct failure modes of CTTA.

- **Substantial and consistent empirical improvements across four benchmarks.** On ImageNet-C with ViT-Base, ViDA achieves 43.4% error vs. 50.0% for VDP (prior SOTA), a 6.6% gain. On segmentation (Cityscapes-to-ACDC), it achieves 61.9% mIoU vs. 58.6% for CoTTA (+3.3%). CIFAR100C gains (+8.1% vs. Source) are the largest across any CTTA baseline on that benchmark.

- **Ablation validates each design component cleanly.** Table 6 shows ViDA_h alone (-5.1%), ViDA_l alone (-4.6%), combined (-10.2%), adding HKA (-12.4%), and inverted HKA (-10.9%) relative to source. The inverse-HKA experiment (Ex_6 = 46.3% vs. Ex_5 = 43.4%) directly confirms that the uncertainty-based gating direction matters.

- **Foundation model compatibility demonstrated explicitly.** Applying ViDA to DINOv2 (+4.8%) and SAM (+5.2%) encoders on CIFAR10C, especially while CoTTA *degrades* DINOv2 by −4.3% and barely affects SAM (−0.1%), is a concrete and surprising finding with practical relevance.

---

## Weaknesses

### Fatal

None. The paper's empirical contributions are real; the concerns below are serious but addressable.

### Major

- **Key competing baselines absent from all main comparison tables.** RMT (Dobler et al., 2023) and SATA (Chakrabarty et al., 2023) are cited in related work as directly relevant CTTA methods addressing error accumulation, yet neither appears in any comparison table. EcoTTA appears only as a single mean number in the ResNet50 row and is entirely absent from the ViT-Base table (Table 1)—the paper's primary showcase—as well as from CIFAR tables. The claim of "state-of-the-art" cannot be substantiated without these comparisons. This is the single most actionable issue; including these baselines would either reinforce or substantially revise the SOTA claim.

- **Adapter warm-starting on source data creates an undisclosed asymmetry relative to baselines.** Section 4.1 states adapters are "train[ed] for several iterations on classification datasets (e.g., ImageNet)"—the source domain for the main benchmark. Every baseline (TENT, CoTTA, VDP, EcoTTA) starts directly from the frozen source model without adapter pre-training. The number of warm-up iterations is not reported, and the paper provides no ablation comparing random initialization vs. source-pretrained initialization. This advantage is potentially significant: an adapter pre-trained on the source distribution is structurally equivalent to a supervised head start that no baseline receives. This matters most for the 6.6% gain over VDP on ImageNet-C ViT-Base—interpreting how much of this gain is architectural vs. initialization-derived is currently impossible.

### Minor

- **Re-parameterization claim is inconsistent with per-sample HKA weighting.** Section 3.2 states adapters "can be projected into the pre-trained model by re-parameterization, ensuring no extra parameter increase." However, HKA computes per-sample λ_h and λ_l as functions of U(x) (Eq. 4). Standard re-parameterization requires folding branches with *fixed* scalar weights into a single matrix; with input-dependent λ, the effective weight changes per sample and cannot be pre-merged. The paper conflates inference-time *parameter count* (unchanged, as adapter weights are added to the original weight matrix at a fixed state) with the *dynamic computation* of HKA, which still runs at inference. The claim needs to be clarified: re-parameterization applies only when λ is fixed, but HKA is dynamic. This is a precision issue that somewhat overstates the inference efficiency.

- **Post-hoc nature of the rank-behavior causal claim.** The motivation in Section 3.1 claims low-rank adapters *cause* domain-shared extraction and high-rank adapters *cause* domain-specific extraction. The supporting evidence (Figs. 2a, 2b) characterizes trained adapters—they show correlation, not causation. There is no controlled experiment varying rank while holding training procedure and initialization constant. This does not invalidate the method but weakens the mechanistic narrative.

### Trivial

- **MC Dropout parameter m is never specified.** For reproducibility and interpretation, the number of MC Dropout passes used to compute U(x) should be stated explicitly.
- **Threshold Θ = 0.2 lacks justification.** No sensitivity analysis or empirical rationale is provided for this choice.

---

## Nice-to-Haves

- Ablation on adapter initialization: random vs. source-pretrained. This would clarify whether the performance gains stem from architecture or warm-start, and would be a direct response to the major concern above.
- Rank sensitivity analysis for d_l ∈ {1, 4, 16} and d_h ∈ {32, 64, 128}—not to validate the architecture (it clearly works), but to show where the behavioral transition between "domain-shared" and "domain-specific" extraction occurs.
- Histogram of λ_h and λ_l values across the 15 corruption domains would empirically confirm that HKA is doing meaningful per-sample adaptive weighting rather than collapsing to a near-constant split.
- Sensitivity of performance and uncertainty estimates to the number of MC Dropout passes m.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"SAM misrepresentation" claim (Harsh Critic):** The paper explicitly states (Section 4.4): "we only use the pre-trained encoder of SAM and add a classification head, which is fine-tuned on the source domain." The disclosure is present and clear. The critic's characterization of this as a misrepresentation is itself a misreading.

- **"ACDC single-access constraint violation" (Harsh Critic):** The CTTA preliminary specifies that each individual *sample* is seen once; the cyclic Fog→Night→Rain→Snow setup repeats *conditions*, not *images*. This is the standard segmentation CTTA protocol following yang2023exploring (cited in the paper). The critic conflates domain cycling with sample re-use.

- **"Domain Generalization is just adaptation benefit, not DG" (Harsh Critic):** The paper follows the standard leave-one-domain-out protocol (citing zhou2021domain, li2017deeper) and directly tests on 5 unseen corruptions without any adaptation. The large gap between ViDA (42.3%) and CoTTA (48.0%) on unseen domains—despite CoTTA also having adapted—indicates more than generic adaptation benefit. Calling this "DG ability" is appropriate within standard evaluation conventions.

- **"JS divergence confound from more EMA updates in later domains" (Harsh Critic):** While an interesting methodological concern, the low-rank adapter shows lower JS divergence than the source model *and* the high-rank adapter across *all* 14 domain shifts, not just positions 9–13. This consistency across the sequence weakens the specific EMA-confound argument.

- **"Foundation model experiment not comparable to Table 2" (Harsh Critic):** The paper presents this experiment (Table 2 right panel and Table with DINOv2/SAM) separately and makes no claim of direct comparability to ResNet/ViT results. The scope criticism (SAM not used for segmentation here) is scope-creep; the paper is studying encoder adaptation under distribution shift.

---

## Novel Insights

The most genuinely novel observation—beyond the empirical results—is that adapter *rank* induces a natural representational specialization: low-rank bottlenecks appear to act as implicit domain-invariant filters by suppressing redundant features, while high-rank bottlenecks over-parameterize enough to fit domain-specific variation. If this causal relationship could be validated with controlled experiments varying only rank, it would offer a principled hyperparameter design criterion for future PEFT-based CTTA methods. The HKA strategy's use of MC Dropout uncertainty as a per-sample routing signal—rather than a global domain-level switch—is a practically useful idea even if its threshold and pass count require better specification.

---

## Suggestions

1. **Add RMT and SATA to all main comparison tables.** This is the minimum necessary to substantiate the SOTA claim. If their codebases are publicly available, include them on all four benchmarks or explain clearly why comparison is architecturally infeasible.
2. **Report an ablation with random adapter initialization** (or at least disclose the number of source warm-up iterations). Even a brief sensitivity table showing performance with 0, 100, 500, and 2000 source iterations would allow readers to assess the initialization contribution.
3. **Clarify the re-parameterization claim**: specify precisely that "no extra parameter increase" refers to static parameter count after merging at fixed λ, and that HKA adds *computational* (not parametric) overhead at inference.
4. **Report variance** across seeds or runs for ablation results, particularly for the 0.7% margin between Ex_4 and Ex_6 and for the CIFAR results.

---

## Score and Decision

**Anchor papers reviewed:**

| Path | Avg Human Score | Comparison to ViDA |
|------|----------------|-------------------|
| `yD2JMeKumt.md` (DOTA, TTA of VLMs) | 6.00 (Reject) | Solid TTA method with strong baselines and human feedback, but has hyperparameter tuning and evaluation protocol issues; ViDA has cleaner methodology but weaker baseline coverage |
| `eXrUdcxfCw.md` (CTTA prototype-based) | 4.80 (Reject) | Simpler method, fewer benchmarks, limited novelty; ViDA clearly stronger in empirical scope and architectural novelty |
| `6yJuDK1DsK.md` (FEATHER, lifelong TTA adapters) | 4.50 (Reject) | Most topically similar paper; same adapter-for-CTTA premise but limited to CNN/BN, fewer benchmarks, no segmentation; ViDA is clearly stronger |
| `TSZh4610VG.md` (C-CoTTA controllable CTTA) | 4.25 (Reject) | Model-based CTTA, weaker empirical gains, limited scope |
| `WM5G2NWSYC.md` (Projected Subnetworks, low anchor) | 2.00 (Reject) | Much weaker: no clear contribution, minimal evaluation; not comparable |
| `YHUGlwTzFB.md` (Active TTA, high anchor) | 6.75 (Accept) | Theoretical guarantees + empirical work on TTA; ViDA lacks theory but has broader empirical coverage |
| `4wk2eOKGvh.md` (TTE, high anchor) | 6.50 (Accept) | Similar empirical focus, ensemble approach for TTA; comparable scope and quality to ViDA but without the missing-baseline problem |
| `LGIhipNvCQ.md` (TUI conformal CTTA) | 4.25 (Reject) | Conformal prediction for CTTA; less empirical depth than ViDA |

**Assessment:** ViDA is clearly above FEATHER (4.5) and the prototype-based CTTA papers (~4.8) due to stronger novelty, richer empirical coverage, and the foundation model generalization results. The two major concerns—missing RMT/SATA baselines and the source-data initialization asymmetry—prevent it from reaching the accepted papers at 6.5–6.75. DOTA (6.0, Reject) is a useful peer comparison: it has strong novel contributions with some evaluation clarity issues, similar to ViDA's situation. Given that ViDA's methodological concerns (especially the initialization advantage and missing baselines) are slightly more impactful than DOTA's, a score of **5.5** is appropriate—solid work with real contributions, but revision-requiring before the SOTA claim can be accepted at face value.

**Originality:** Moderate-to-good. The dual-adapter design is a clean and original synthesis. The HKA mechanism is incremental on existing uncertainty-based TTA ideas but contextualized well.  
**Importance:** The CTTA problem is practically significant; an adapter-based approach that also handles foundation models has clear value.  
**Claim support:** Empirical results are compelling but the SOTA claim is undercut by missing baselines and the initialization asymmetry.  
**Soundness:** The core design is sound; the re-parameterization inconsistency and post-hoc motivation are minor but real.  
**Clarity:** Good. The paper is well-organized and the method description is clear.  
**Value to community:** Would be high if the baseline comparisons were complete.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>