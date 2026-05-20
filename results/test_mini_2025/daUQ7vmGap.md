Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper investigates whether Dynamic Sparse Training (DST) — originally designed for efficiency — improves model robustness against common image corruptions compared to conventional Dense Training. Through experiments on 9 scenarios spanning CIFAR-C, ImageNet-C/3DCC, and UCF101, across multiple CNN and transformer architectures and several DST algorithms (SET, RigL, MEST, GraNet), the authors find that DST at low-to-moderate sparsity (10–50%) consistently achieves higher corrupted accuracy. Spatial and spectral analyses suggest DST acts as an implicit regularizer, reducing sensitivity to high-frequency information.

## Strengths

- **Comprehensive validation across 9 diverse scenarios (Table 2).** Every DST algorithm (RigL, MEST_g, GraNet_g) outperforms the dense baseline on every scenario tested: CIFAR10-C, CIFAR100-C, TinyImageNet-C, ImageNet-C, ImageNet-3DCC, and UCF101 video. This sweeping consistency is the paper's strongest evidence for its central claim.

- **Large gains on high-frequency, high-severity corruptions.** On ImageNet-C, MEST_g at sparsity 0.1 achieves nearly 25% relative accuracy improvement over the dense baseline for impulse and Gaussian noise at severity 5 (Figure 3). This identifies precisely where DST's advantage is largest — a specific, falsifiable finding.

- **Spectral analysis provides a mechanistic explanation (Figure 7).** The frequency-attenuation experiment shows that DST models (e.g., ResNet34 at 0.5 sparsity on CIFAR100) are less affected by high-frequency removal than dense models, while both are equally affected by low-frequency removal. This directly supports the claim that DST reduces reliance on high-frequency information, aligning with the corruption types where DST excels.

- **Spatial visualization of implicit regularization (Figure 5).** Heatmaps of non-zero weight counts show that DST models concentrate sparsified weights on specific input-output channel pairs, effectively "sparsifying away" less important features. This provides a clear visual intuition for how DST differs from dense training's soft weight decay.

- **Extension beyond image CNNs (Section 4.3).** The paper validates the finding on video (UCF101 with 3D ResNet50 and I3D) and transformers (DeiT-base on ImageNet-C), showing the phenomenon is not architecture-specific.

## Weaknesses

### Major

- **Clean (uncorrupted) accuracy is not reported.** This is the most significant omission. In a robustness study, standard practice is to report clean accuracy alongside corrupted accuracy so the reader can assess whether robustness gains come at the cost of general performance. The paper's central claim — that DST "outperforms" Dense Training — is specifically about *robustness* accuracy, so this does not invalidate the claim, but it leaves a critical gap in the evaluation. For instance, if DST's clean accuracy were notably lower than dense, the practical value of the robustness advantage would be diminished.

- **No error bars or measures of variability.** All results (Figures 2–4, Tables 1–2) are single-point estimates. For ImageNet-scale results where margins are as small as ≤0.5 percentage points (Table 2: Dense 38.38 vs. RigL 38.70), standard deviations from multiple runs are essential to assess whether these differences reflect a real effect or run-to-run noise. For smaller-scale experiments (CIFAR, TinyImageNet), which are inexpensive enough to run with ≥3 seeds, the omission is especially problematic. This gap weakens confidence in the claim across the board, not just for the borderline ImageNet margins.

### Minor

- **No static sparse baseline.** The paper's hypothesis concerns *Dynamic* Sparse Training specifically, but no experiment compares DST to a network of the same sparsity with a *fixed* mask (e.g., pruning at initialization). Without this control, it is unclear whether the robustness benefit comes from sparsity *per se* or from the *dynamic reorganization* of connections. The stated DSCR hypothesis ("DST outperforms Dense Training") is validated by the existing comparisons, so this does not undermine the core claim — but it limits the specificity of the attribution.

- **Cost-savings claim is ambiguous without hardware context.** The paper states "at least 40% of both training computational and memory costs can be saved" but acknowledges in a footnote that this assumes hardware with sparse matrix product support. On standard hardware, DST simulated with binary masks incurs the same FLOPs as dense training. The distinction between theoretical parameter savings and actual runtime savings needs clearer upfront treatment.

### Trivial

None.

## Nice-to-Haves

- **Static sparse baseline** (prune at initialization with fixed mask, or LTH) would cleanly isolate whether the *dynamic* aspect is responsible for the robustness gain. This would strengthen the mechanistic claims in Section 5.
- **Breakdown by severity level** for the overall results in Figure 2 (currently only shown by corruption type in Figure 3).
- **Clean accuracy** as a column in Table 2 would make the evaluation self-contained.
- **Discussion of failure cases** (e.g., at very high sparsity where DST may underperform) would improve balance.

## Removed Points

*These points were raised in the inputs but are being removed or demoted for the reasons stated below.*

- **"Small margins on ImageNet undermine the claim"** — This is subsumed by the error-bars weakness. The margins are indeed small, but the paper also shows larger margins on CIFAR100-C (~4 pp) and UCF101 (~1–3 pp). The consistency across all 9 scenarios reduces the concern that ImageNet-scale results are noise; however, without error bars this remains a risk.
- **"Missing hyperparameter reporting"** — The paper states key hyperparameters are in the appendix. The appendix is stripped by the parser; this is not an author error.
- **"Cost claim should distinguish theoretical vs. actual savings"** — The paper partially addresses this in footnote 4, though a more prominent treatment would be better. Moved to Minor.
- **"Clarify averaging procedure for robustness accuracy"** — Figure 2 caption states the averaging is across corruption types and severity levels, which is standard. This is already sufficiently clear.
- **Strength Finder's generic praise** (e.g., "the problem is important") — Removed for being generic/superficial. Only strengths with specific evidence anchors are retained.

## Novel Insights

None beyond the paper's own contributions. The finding itself — that DST, designed for efficiency, unintentionally and consistently improves corruption robustness — is the paper's core novel insight, and the spectral analysis provides a plausible mechanistic explanation.

## Suggestions

1. **Report clean accuracy** for every configuration as a separate column in Table 2, or as a supplementary table with the same layout.
2. **Add error bars.** For CIFAR and TinyImageNet experiments, run with at least 3 seeds and report mean ± std. For ImageNet-scale experiments, if single-run is the only feasible option, explicitly caution that the small margins may not be statistically significant.
3. **Add at least one static sparse baseline** (e.g., SNIP or GraSP at initialization) to help attribute the effect to *dynamic* sparsity rather than sparsity alone.
4. **Clarify the real-world cost savings** upfront: distinguish between theoretical FLOP/parameter reduction and achievable wall-clock speedup on current hardware.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| XMaPp8CIXq (Always-Sparse Training) | 3.00 | R1 | Weaker — proposed a sparse training method but with incremental contribution; the current paper has a more novel finding |
| zgHamUBuuO (Sparling) | 3.00 | R1 | Weaker — different problem domain (sparse activations), less comprehensive evaluation |
| mORwTTZfWq (Adversarial Attack Robust dataset pruning) | 5.60 | R1 | Similar quality — both study robustness with some missing rigor; current paper broader but has methodological gaps |
| **qbw861vueP (BiDST)** | **4.33** | **R1** | **Most topically relevant anchor** — DST methodology paper with methodological concerns (mask differentiability). Current paper is empirically cleaner but lacks error bars and clean accuracy, which BiDST also lacked for its ImageNet results |
| CSZKElOtG5 (MeanSparse) | 4.25 | R1 | Similar quality — robustness via sparsification, rejected despite interesting idea; current paper has broader scope |
| kDoKXaucJV (Sparse-Guard) | 4.75 | R2 | Slightly weaker — limited to MNIST/FashionMNIST; current paper has broader experimental validation |
| yAcLwJu9qs (Assessing VCR) | 5.50 | R2 | Similar — both study corruption robustness with significant experimentation; VCR had presentation issues, current paper has clean accuracy/error-bar gaps |
| 7GCRhebJEr (Robustness via Bregman) | 5.00 | R2 | Similar — method paper for robustness with mixed reviews; current paper is more of an empirical finding |
| 0IqriWHWYy (Watch Out!! Your Confidence) | 4.25 | R2 | Weaker — narrower focus on confidence as vulnerability factor |
| S1qSHSFOew (CSI 3D Point Cloud) | 5.50 | R2 | Different domain (3D point clouds); similar score range |
| ud8FtE1N4N (The Journey Matters) | 6.67 | R2 | Stronger — accepted poster with systematic sparse pretraining study; better methodological rigor |
| 60lNoatp7u (NeurRev) | 6.67 | R2 | Stronger — accepted poster with well-supported DST method and system validation; the current paper lacks comparable evidential rigor |
| 1ndDmZdT4g (Dynamic Sparse No Training) | 6.00 | R2 | Stronger — accepted poster with clear methodology and thorough experiments on LLMs |
| oXh0939Zzq (Dynamic Low-Rank Sparse) | 5.20 | R2 | Borderline — accepted poster but with mixed scores (3,3,6,6,8); comparable quality |

**Round 1 bracket:** 4 – 6.5. The paper is clearly above the 2–3 range of the weak anchors and below the 7.5+ range of the strong accept anchors.

**Round 2 narrowing:** The paper sits between BiDST (4.33) and NeurRev (6.67), and is most comparable to Assessing VCR (5.50) and Bregman divergence (5.00). Relative to these middle-band anchors, the paper has a genuinely novel empirical finding with broad validation, but lacks two standard elements of robustness evaluation (clean accuracy, error bars) that the other papers in this range typically provide. It has broader scope than Sparse-Guard (4.75) but similar rigor gaps. It is weaker than NeurRev (6.67, accepted) largely because NeurRev had proper multi-seed experiments and system validation.

**Final score:** 5.0. The paper uncovers a genuinely interesting and potentially impactful phenomenon, supported by broad experimentation. However, the omission of clean accuracy and lack of any variability measures are significant methodological gaps that lower confidence in the reported margins, particularly on ImageNet-scale experiments. These gaps are addressable and the paper could become a solid 6+ contribution with the additions described in Suggestions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>