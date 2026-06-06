Now I have enough data for calibration. Let me synthesize the final review.

**Calibration anchor summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SemiCLIP | 97D725GJtQ | 5.80 | 1 | Similar topic (semi-supervised CLIP), smaller gains (1.7-6.6%), CaPT is clearly stronger |
| Cleaning label noise w/ CLIP | 1rgMkDWfYV | 4.50 | 1 | Uses CLIP for noisy labels, different problem, weaker results, CaPT much stronger |
| Understanding FixMatch | 25kAzqzTrz | 8.00 | 1 | Theoretical SSL paper with all 8s, very different contribution type, CaPT is not at this level theoretically |
| SemiReward | dnqPvUjyRI | 6.00 | 2 | Pluggable SSL pseudo label quality, 13 benchmarks, marginal gains. CaPT clearly stronger |
| ITIT | kNjrhD67LP | 7.00 | 2 | Cycle consistency for unpaired VL training, different domain, strong results. Similar tier |
| DiffMatch | 85G2t3yklD | 6.67 | 2 | SSL semantic segmentation with generative models, theoretical derivation for class imbalance. Similar rigor level |
| OOD Unlabeled Data | Bo6GpQ3B9a | 7.00 | 2 | DRO+SSL theoretical framework. Different type, strong theory |
| Selective Mixup | rxVBKhyfSo | 7.00 | 2 | Fine-tuning for non-decomposable objectives, different focus |

**Round 1 bracket**: 5.5–8.0 (between SemiReward/SemiCLIP at ~5.8 and FixMatch theory at 8.0)

**Round 2 bracket**: 6.0–7.0 (CaPT is clearly stronger than SemiReward 6.0, clearly stronger than SemiCLIP 5.80; comparable to DiffMatch 6.67 and ITIT 7.00 in contribution quality)

**Final score**: CaPT's massive empirical gains (+21% on CIFAR-100), clean architecture, thorough ablations, and theoretical motivation place it above SemiReward (6.0) and DiffMatch (6.67). The baseline fairness issue (no CLIP-integrated comparison) and inconsistent gains across datasets prevent it from reaching 7.0 alongside ITIT and OOD. I'll score **6.5**.

## Summary
This paper proposes CaPT (CLIP as a Prior Teacher), an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning by jointly training a fully fine-tuned unimodal ViT and an adapter-tuned CLIP model, exchanging co-pseudo labels through an entropy-weighted fusion module. The paper provides a theoretical analysis formalizing SSL's label dependency problem and reports substantial empirical gains in extreme low-label regimes (e.g., +21.38% on CIFAR-100 with 1 label/class).

## Strengths
- **Theoretical grounding of label dependency (Theorem 1.1, Eq. 1)**: Derives a concrete pseudo-label error bound under a Gaussian-mixture model showing error decays exponentially in (g/2 − r)²/σ², rigorously motivating why SSL degrades when labeled data is scarce or poor quality. This goes beyond empirical observation to provide a formal foundation for the paper's motivation.

- **Large empirical margins in extreme low-label regimes (Tables 2–3)**: CaPT achieves 82.51% vs 61.13% (FreeMatch) on CIFAR-100 with 1 label/class — a 21.38% margin (Table 3). On ImageNet with 10 labels/class, CaPT achieves 67.68% vs 58.35% for RegMixMatch (Table 2). These margins are substantial and directly demonstrate that CLIP's prior knowledge can unlock unlabeled data utility when labeled data is extremely scarce.

- **Efficient integration with minimal overhead (Table 4)**: Only 8% more memory (5050 vs 4676 MiB) and 11% more training time (0.1044 vs 0.0939 sec/iter.) over FreeMatch, while actually using less memory and time than RegMixMatch. The feature-level augmentation strategy (Section 3.2.2) that avoids re-passing high-resolution images through CLIP's frozen encoder is a well-motivated efficiency design.

- **Thorough ablation study validating each design choice (Table 6)**: Systematically isolates contributions: removing co-training ("only UPM" and "only MPM") drops 6–17%; removing adapter-tuning (CaPT-Deb) drops 3–13% especially on CLIP-bias-sensitive datasets; removing bidirectional flow (CaPT-Uni) loses 0.9–1.5%; entropy weighting outperforms equal weighting by 0.9–1.6%. Each component shows measurable, non-trivial contributions.

- **Asymmetric-modalities design motivated by concrete visual evidence (Figure 3)**: Attention maps demonstrate that CLIP's vision encoder produces substantially different attention patterns than unimodal ViTs (e.g., on a "rooster," CLIP attends to the comb while pure-vision ViTs focus on the eye and beak), concretely motivating the cross-modal complementarity and distinguishing CaPT from prior co-training work like CLS.

## Weaknesses

### Fatal
None

### Major
- **No comparison against CLIP-integrated SSL methods in main results** — All 12 baselines in Tables 1–3 are pure SSL methods without access to CLIP or any VLM. While the ablation (Table 6) includes CaPT-Deb as an approximation of DebiasPL and shows adapter-tuning + bidirectional flow adds 3.8–12.7%, this uses CaPT's own infrastructure rather than a reproduced baseline. The paper acknowledges DebiasPL and CLS in text and Figure 2 but neither appears as a baseline in the main results. This is the most significant issue: the co-training architecture's contribution (validated by ablations) is clear, but the total gain attributed to CLIP's prior vs. the architecture cannot be precisely decomposed from the main results alone.

### Minor
- **Inconsistent magnitude of gains suggests method value is contingent on CLIP's domain fit** — The headline +21.38% on CIFAR-100 (1 label/class) vs. +0.72% on CIFAR-10 (Table 3); and CaPT loses to FreeMatch on FGVCaircraft at 5 labels (50.12% vs 51.43%, Table 5). The paper acknowledges FGVCaircraft (Appendix N) but doesn't explicitly characterize the general pattern: gains correlate with CLIP's prior quality for each domain. This doesn't invalidate the contribution but the "breaking label dependency" framing could be more precisely scoped to datasets where CLIP has a useful prior.

- **STL-10 anomaly deserves discussion** — Adapter-tuned CLIP alone achieves 96.86% on STL-10 (4 labels), higher than CaPT's 96.07% (Table 1, last two rows). This means co-training slightly hurts CLIP's performance while greatly helping the unimodal network (83.85% → 96.07%). This is worth acknowledging as it may reveal a failure mode where co-training dilutes a strong prior, especially on STL-10 which has OOD unlabeled samples.

### Trivial
None

## Nice-to-Haves
- Quantifying CLIP zero-shot accuracy per dataset vs. CaPT's gain to transparently characterize when the method provides value
- Reporting results at moderate label counts (e.g., 10%, 25% of labels) to confirm CaPT doesn't hurt performance in non-extreme regimes
- Brief analysis of whether the soft co-pseudo label (Eq. 13) with sub-unit mass acts as beneficial label smoothing

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh critic's "theoretical gap" claim**: The paper never claims the theorem proves CaPT provably breaks label dependency; it uses the theorem to motivate the problem and CaPT addresses it empirically. This is standard for method papers and is not a genuine weakness.
- **Harsh critic's claim about abstract potentially misleading**: The gains ARE across multiple benchmarks and the abstract accurately states the numbers and settings. This is a style nitpick.
- **Strength finder's "comprehensive evaluation breadth" as strength**: While true, this is somewhat generic. The specific evidence from each table is already cited above.

## Novel Insights
The key observation emerging from the reviews is that CaPT's gains are fundamentally contingent on CLIP's domain-specific prior quality, creating a bimodal performance story: dramatic improvements (20%+) on datasets where CLIP's prior aligns well (CIFAR-100, SVHN, Flowers102) versus marginal or negative effects where it doesn't (CIFAR-10, FGVCaircraft). The asymmetric-modalities co-training design is validated by the ablations as genuinely necessary — both "only UPM" and "only MPM" substantially underperform — confirming this is not simply "use CLIP predictions as pseudo labels." The STL-10 case where adapter-tuned CLIP outperforms CaPT reveals an interesting failure mode where co-training can actually dilute a strong prior.

## Suggestions
- Add a direct comparison against DebiasPL (or a faithfully reproduced version) in the main results to control for the knowledge source
- Include a brief analysis correlating CLIP's zero-shot accuracy per dataset with CaPT's gain
- Discuss the STL-10 anomaly where adapter-tuned CLIP outperforms CaPT

## Score and Decision

**Evaluation axes:**
- **Originality**: The asymmetric co-training of a fine-tuned ViT with an adapter-tuned CLIP via entropy-weighted co-pseudo labels is a novel and well-motivated design. The attention divergence argument (Figure 3) providing evidence for why cross-modal co-training is superior to uni-modal co-training is insightful.
- **Importance**: Addressing SSL's label dependency in extreme low-label regimes is an important practical problem. The framework's portability to stronger future VLMs adds long-term relevance.
- **Soundness of claims**: The theoretical analysis correctly motivates the problem. The empirical claims are supported by extensive experiments, though the gains' inconsistency across datasets suggests the claims could be more precisely scoped.
- **Experiments**: Comprehensive evaluation across 15+ dataset/condition combinations, ImageNet scale, fine-grained benchmarks, and thorough ablations. The main gap is the absence of CLIP-integrated baselines in main results.
- **Clarity**: The paper is well-structured, the method is clearly specified (Eqs. 2–15), and the three-module architecture is intuitive. Figures are informative.
- **Value to community**: Establishes a practical framework for integrating VLMs into SSL with demonstrated real-world efficiency gains. The code is provided.

**Score: 6.5** — Positioned above SemiReward (6.0, which had marginal gains and unclear rewarder mechanism) and DiffMatch (6.67, which had comparable rigor but focused on a narrower segmentation task). Below the 7.0 anchors (ITIT, OOD Unlabeled Data) due to the baseline fairness issue and inconsistent gains. The massive empirical margins in extreme low-label settings, clean architectural design with thorough ablations, and theoretical motivation are the main strengths. The absence of CLIP-integrated comparisons and domain-contingent gains are the main concerns.

**Decision: Accept** — The paper makes a clear contribution: it identifies and formalizes a real problem (SSL's label dependency), proposes a well-designed solution (asymmetric co-training with CLIP), and provides strong evidence that it works in extreme settings. The framework is practical (8% memory overhead) and extensible to future VLMs. The baseline fairness concern is real but partially addressed by ablations; the inconsistent gains reflect CLIP's domain-specific priors rather than a flaw in the method itself.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>