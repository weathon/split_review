Now let me write the final consolidated review.

## Summary

This paper introduces L-TTA, a test-time adaptation method for vision-language models operating under long-tailed test distributions. L-TTA combines three co-designed mechanisms: Synergistic Prototypes (SyPs) combining Deterministic and Exclusionary Prototypes to enrich tail-class representations, Rebalancing Shortcuts (RSs) with a class re-allocation loss for learnable adaptation, and Balanced Entropy Minimization (BEM) to counter head-class bias in standard entropy minimization. Experiments across 15 datasets with imbalance ratios of 10/20/50 show consistent improvements over 11 existing VLM TTA methods, with gains of 1–3% in accuracy and macro-F1.

## Strengths

- **Novel problem formulation.** The paper is the first to study TTA under long-tailed settings specifically for VLMs, and it identifies two VLM-specific failure modes — Text-induced Tail Erosion and Modality-bias Amplification (Section 1, lines 38–39) — that go beyond the challenges present in unimodal or balanced TTA. This motivates the method in a principled way rather than simply applying a long-tailed loss to an existing TTA pipeline.

- **Consistent and broad empirical validation.** L-TTA is evaluated on 15 datasets across three benchmarks (OOD, cross-domain, corruption) at three imbalance ratios (10/20/50), using 11 baseline methods. On the OOD benchmark (Table 1, imb=10), L-TTA surpasses the next-best method by 1.47% in OOD average accuracy and 3.61% in macro-F1. On the corruption benchmark (Table 3), gains reach 2.87% accuracy and 2.64% macro-F1. Gains are consistent rather than cherry-picked, which strengthens the reliability of the claims.

- **Well-structured ablations.** Table 6 systematically decomposes each component: DPs alone (68.68% acc), adding RS (+1.08%), EPs alone (67.54%), combining both prototypes with RS (70.94%), and the full pipeline with BEM (71.30%). This allows the reader to attribute the improvement to specific design choices.

- **Efficiency is competitive.** Table 4 shows L-TTA runs in 1.45h (vs. 18.30h for RLCF and 27.70h for WATT) and uses 1.89 GB memory. The harmonic mean on the corruption benchmark (46.08) comfortably exceeds all baselines, showing the gains are not at prohibitive computational cost.

- **Generalization to stronger backbones.** Table 5 extends L-TTA to ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG, with average gains of ~1.5% accuracy and ~1.8% macro-F1 across all of them. This addresses a common failure mode where a method designed for CLIP ViT-B/16 does not transfer well.

## Weaknesses

### Major

None.

### Minor

- **Failure modes are identified but not directly validated.** The paper motivates the method by two failure modes (Text-induced Tail Erosion and Modality-bias Amplification), yet no experiment directly measures whether L-TTA resolves them. For example, per-class accuracy grouped by "rich" vs. "poor" classes (to track Text-induced Tail Erosion) or a cross-modal alignment metric (cosine similarity between visual and textual embeddings) pre- and post-adaptation (to track Modality-bias Amplification) would convert the motivation from plausible storytelling into measured evidence. This is a gap — the method is claimed to solve these specific problems, but the paper only shows aggregate accuracy/F1, not that the identified mechanisms are what drive the improvement.

- **No standard deviations reported despite claiming 5 runs.** The paper states "5 runs for each experiment" (line 154) but does not report variance in any of the main tables (Tables 1–5). Given that the method involves stochastic elements (random cropping, EMA updates, attention), this is important for assessing whether the reported improvements are statistically significant, especially for the 1–3% margins.

- **Theoretical propositions are not substantive.** Propositions 1 and 2 (lines 132–143) formalize that EM biases toward head classes and that BEM reduces this gap. The assumptions are vague ("split C into C_head and C_tail with certain measurements"), the proofs are deferred to the appendix, and the conclusions are intuitive. These should be presented as formalized intuitions rather than as rigorous theoretical guarantees; the paper would be stronger with this reframing.

- **Ablation in Table 6 lacks a "vanilla EM" baseline.** The ablation removes components progressively but never includes a condition with standard entropy minimization using only the original CLIP predictions (no DPs, no EPs, no RSs, no BEM). The closest condition is DP-only, which already uses the novel prototype mechanism. A "vanilla EM" baseline would isolate what the entire L-TTA pipeline adds over standard VLM TTA.

### Trivial

- **Hyper-class vector count K is ambiguous.** The implementation states "K = 0.3" (line 208), and the ablation (Figure 4.c) varies K from 0.1 to 1.0. The paper should clarify that K is a fraction of the number of classes (i.e., K = 0.3 means K×C hyper-class vectors).

- **Table 5 has empty cells for TPT on MetaCLIP-BigG** without explanation. If TPT cannot be applied to this backbone, a note should clarify why.

## Nice-to-Haves

- Comparing L-TTA against class-imbalance TTA methods (SAR, DELTA, LAME) adapted to VLMs would be informative, though the paper has a legitimate rationale for excluding them (they are designed for non-VLM backbones, and the paper argues that applying them to VLMs causes cross-modal degradation). If the authors have preliminary evidence of this degradation (beyond Figure 1(b.2)), including it would strengthen this argument.

- The EP update mechanism (Eq. 5) could accumulate noisy features for tail classes, since φ_c ≈ 1 for tail class updates on essentially every sample. A brief analysis of EP quality vs. class frequency (e.g., via t-SNE visualization) would address this concern.

## Removed Points

- **"HM is never defined"** — Factually wrong. Table 4 caption explicitly states: "Here HM is the harmonic mean of Accuracy and Macro-f1" (line 286–287). Removed.

- **"First to study claim is misleading"** — The paper's claim is situated in the VLM context. The abstract says "As the first attempt to solve this problem" where "this problem" is long-tailed TTA for VLMs. The related work (Section 2.1, line 58) explicitly discusses non-VLM TTA methods for non-i.i.d. data and distinguishes the paper's focus. One contribution sentence (line 47) says "first TTA for long-tailed settings" without the VLM qualifier, which is slightly imprecise, but this is a minor framing issue that does not undermine the paper's contribution. Removed.

- **Missing comparisons with DELTA/SAR/LAME** — These are non-VLM TTA methods designed for different backbones (CNNs). The paper focuses on VLM TTA and explicitly states that applying unimodal methods to VLMs causes modality-bias amplification (line 38). Including adapted versions would be informative but not required; their absence does not invalidate the empirical claims. Downgraded to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add error bars (standard deviations) to all main tables where 5 runs are claimed.
2. Add direct validation of the two failure modes: per-class accuracy grouped by text-prior confidence (Failure Mode 1) and a cross-modal alignment metric over the course of adaptation (Failure Mode 2).
3. Include a "vanilla EM" baseline to the ablation study (standard entropy minimization with CLIP's original predictions, none of the L-TTA components).
4. Clarify that K is a fraction of the number of classes (K × C hyper-class vectors).
5. Reframe Propositions 1 and 2 as formalized intuitions rather than carrying theoretical weight they do not support.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Decision | Round | Comparison to L-TTA |
|--------|-----------|----------|-------|---------------------|
| DOTA (VLM TTA) | 6.00 | Reject | R1 | L-TTA is stronger: more novel problem, broader evaluation, fewer methodological gaps |
| ROSITA (open-world VLM TTA) | 4.67 | Reject | R1 | L-TTA is substantially stronger |
| BLG (long-tailed CLIP) | 4.67 | Reject | R1 | Different setting, L-TTA has broader evaluation |
| DART (TTA with class shift) | 5.67 | Reject | R2 | L-TTA is stronger: 15 vs. ~4 datasets, avoids labeled intermediate data requirement |
| SlimTTT (resource-efficient TTT) | 6.00 | Reject | R2 | Different focus; L-TTA has fewer methodological gaps |
| Multi-label BEM (TTA) | 6.25 | Accept | R1 | Comparable quality; L-TTA has broader evaluation |
| RLCF (VLM TTA, CLIP reward) | 6.67 | Accept | R2 | Comparable; L-TTA has more specific problem framing |
| Concept drift MLLM | 7.00 | Accept | R2 | Higher scope/quality; L-TTA is more narrowly focused |

**Round 1 bracket:** (4.5, 7.5). **Round 2 narrowing:** L-TTA is clearly above the reject anchors in its topical cluster (DOTA at 6.0, DART at 5.67) and comparable to the accept anchors (Multi-label BEM at 6.25, RLCF at 6.67). The paper's weaknesses are presentation/validation gaps rather than fatal methodological flaws, and its strengths (novel problem, broad evaluation, well-ablated components) are substantial.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>