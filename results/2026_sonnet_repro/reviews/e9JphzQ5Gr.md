Now let me run the calibration searches.Now I have sufficient calibration data. Let me compile the final review.

---

## Summary

CaPT introduces an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning (SSL). The core insight is that CLIP's vision-language representations provide a label-independent prior that can unlock unlabeled data when labeled supervision is critically scarce. CaPT couples a fully fine-tuned unimodal network with an adapter-tuned CLIP model via entropy-weighted co-pseudo labels and feature-level consistency regularization. Results are strong across multiple benchmarks, most notably a 21.38% improvement on CIFAR-100 with one labeled sample per class (Table 3).

---

## Strengths

- **Strong, consistent empirical gains across benchmarks**: Table 1 shows +4.09% on CIFAR-100 with 2 labels/class and +6.18% on STL-10 with 4 labels/class over the prior best (RegMixMatch). Table 2 shows +9.33% on ImageNet with 10 labels/class. Table 3 confirms a 21.38% improvement on CIFAR-100 with one label/class and 4.05% on EuroSAT — the gains are not narrowly achieved on one dataset.

- **Clean ablation isolating each component**: Table 6 systematically ablates CaPT-Ada, CaPT-Deb, CaPT-Uni, single-module variants, feature augmentation, and entropy weighting. The results confirm each design choice is load-bearing (e.g., −12.73% without adapter tuning on EuroSAT, −16.40%/−16.38% without full UPM capacity).

- **Computational efficiency**: Table 4 shows CaPT adds only 8% memory and 11% training time over FreeMatch while delivering +6.23% accuracy on CIFAR-100 with 2 labels/class. This is a non-trivial result given CaPT runs a second transformer branch.

- **Visual cross-modal complementarity evidence**: Figure 3 shows that two unimodal ViTs attend to similar regions (eye/beak of rooster), while CLIP attends to a distinct discriminative part (the comb), directly supporting the paper's claim that asymmetric modalities mitigate the pattern-homogeneity bottleneck of standard co-training.

- **Bias mitigation demonstrated empirically**: Figure 5 shows adapter-tuned CLIP produces a markedly more balanced class distribution than zero-shot CLIP on EuroSAT, and this improvement is tied to a 12.73% accuracy gain in Table 6.

- **Compelling motivating evidence for SSL's label dependency**: Figure 1c directly shows that FreeMatch on CIFAR-100 with one label/class gains nearly nothing from added unlabeled data, validating the paper's framing. Figure 1a and 1b quantify both quantity and quality effects. These figures make the problem statement concrete without requiring the theorem.

---

## Weaknesses

### Fatal
None.

### Major

- **DebiasPL and CLS absent from all main result tables** — DebiasPL (Wang et al., 2022a) is the closest prior work (also integrates CLIP into SSL) and CLS (Yao et al., 2022) is the closest methodological predecessor (co-training two models in an SSL setting). Neither appears in Tables 1–5. For DebiasPL, the paper offers CaPT-Deb in Table 6, but as defined in Section 4.5, CaPT-Deb "disables adapter-tuning *and* vision model→CLIP flow," simultaneously removing two distinct design choices. This conflation prevents a clean attribution of gains over DebiasPL's approach. For CLS, the paper argues at length in Section 2 that asymmetric modalities are superior to symmetric co-training of two unimodal networks, but never tests this claim in a head-to-head result. Without CLS in the tables, readers cannot determine from the paper alone how much of CaPT's improvement derives from co-training per se versus from CLIP's cross-modal prior specifically.

- **Theorem 1.1 framing overstates the theoretical contribution** — The theorem derives a pseudo-label error bound under a Gaussian mixture model with a nearest-prototype classifier (Section 1). Both assumptions are far from the actual setting (deep networks with adaptive thresholding, real data). The conclusion — that prototype bias *B* and small *n_min* increase error via reduced effective margin *g/2 − r* — is readily accepted by practitioners without formal proof. The Introduction frames this as "theoretically establishing the label dependency" of SSL as a headline contribution, but the theorem does not formalize *why* CLIP helps or how the co-training dynamics reduce the bound. The empirical motivating evidence in Figure 1 is independently convincing; the theorem adds vocabulary but not mechanistic insight.

### Minor

- **SVHN anomalous result underanalyzed** — Table 5 shows CaPT achieves 81.20% on SVHN with 2 labels/class versus FreeMatch's 67.35%, a 14-point gain, despite CLIP's zero-shot accuracy on SVHN being only 34.36% — well below SSL baselines. This is the most surprising result in the paper (adapter-tuned CLIP rescuing a severely biased prior to outperform baselines by 14 points) and the least discussed. Section 4.4 notes only "Except for FGVCAircraft (discussed in Appendix N), CaPT outperforms competing methods across all other datasets." Whether the UPM's feedback is driving the SVHN recovery, or the adapter alone calibrates CLIP's prior, is a meaningful empirical question the paper leaves unanswered.

- **Hard pseudo-label fusion in Eq. 13 unmotivated and unablated** — The co-pseudo label is defined as a weighted sum of *hard* argmax outputs (Eq. 10, 13: $\tilde{q}^c = \Gamma^a \hat{q}^a + \Gamma^b \hat{q}^b$), discarding second-order prediction uncertainty. When both models are confident in different classes, the resulting co-pseudo label is a diffuse mixture of two one-hot vectors, which may be less informative than weighting the soft distributions $q^{w,a}$ and $q^{w,b}$ directly. This design choice is neither motivated in the text nor ablated in Table 6. Given that it is load-bearing in the PFM, it deserves explicit justification.

### Trivial
None.

---

## Nice-to-Haves

- A **symmetric CaPT ablation** — co-training a vision-only ViT (from identical pre-training as the CLIP visual encoder but without text alignment) against UPM — would sharpen the claim that CLIP's cross-modal prior specifically (not just any diverse second model) drives the gains. If CLIP's text grounding uniquely contributes, this ablation would make that case decisively.
- A brief **analysis of SVHN adaptation** (does the adapter alone rescue the biased prior, or does UPM feedback dominate?) would make the "reliable prior through co-training" argument substantially more concrete.
- The ImageNet 10 labels/class setting corresponds to 10,000 total labeled samples; a sentence clarifying whether this is considered "low-label" relative to ImageNet's scale (1.2M training images, 1000 classes) would help calibrate the reader's expectations.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic criticism of feature-augmented consistency regularization as "merely a workaround"**: The paper explicitly acknowledges both motivations in Section 3.2.2 — "Feature-augmented consistency regularization not only improves the generalization of CLIP but also avoids the need to construct another high-resolution version of the unlabeled image." The ablation confirms it contributes (+0.57%/+1.81%). Framing this as novel regularization alongside an efficiency motivation is reasonable; the harsh critic's complaint about framing overstatement is too minor to retain.

- **Criticism of Table 4 efficiency claim requiring explicit explanation of gradient memory savings**: The paper gives the numbers (8% memory, 11% time) in the main text; the mechanistic explanation (frozen encoder, adapter-only gradient memory) is a reasonable detail for supplementary material. Not a substantive weakness.

- **Harsh critic suggestion that CaPT-Deb is an "unfaithful reproduction of DebiasPL"**: CaPT-Deb is explicitly an *ablation variant* of CaPT (Section 4.5), not a claimed reproduction of DebiasPL. The weakness is correctly that DebiasPL itself is absent from main tables — retained above — but the ablation design complaint is partially misdirected.

- **Harsh critic concern about FGVCAircraft result deferred to Appendix N**: The paper acknowledges the FGVCAircraft limitation explicitly in Section 5 ("CLIP's prior is less informative on certain fine-grained datasets such as FGVCaircraft") and notes it discusses more powerful VLMs for such cases. The appendix strip rule applies; deferring one outlier analysis to the appendix is not a main-text flaw.

- **Criticism of Theorem 1.1 as "completely wrong"**: The theorem is not mathematically wrong; it is a valid bound under its stated assumptions. The weakness is framing overstatement (retained above as Major), not a mathematical error.

---

## Novel Insights

The most genuinely novel observation this paper surfaces — supported by the attention map evidence in Figure 3 and the ablation in Table 6 — is that the *mode* of CLIP integration matters more than the fact of integration. DebiasPL's one-directional, biased-prior injection fails badly on domain-shifted datasets (EuroSAT −12.73%), while asymmetric bidirectional co-training with adapter tuning recovers that loss and compounds gains. The pattern-homogeneity bottleneck in symmetric co-training (two unimodal ViTs attending similarly, Figure 3) and its resolution through cross-modal asymmetry is a clean, concrete, and field-relevant finding. The Figure 1c result — that SSL gains from unlabeled data collapse to near-zero at one label/class — is also sharper empirical documentation of a widely sensed but rarely quantified failure mode.

---

## Suggestions

1. Add DebiasPL (Wang et al., 2022a) and CLS (Yao et al., 2022) to the main result tables for at least one or two benchmark settings. A single additional column each would close the most significant evidential gap.
2. Add an ablation of hard vs. soft pseudo-label weighting in Eq. 13 to Table 6 — this is a load-bearing design choice that deserves at least one ablation row.
3. Soften the theoretical framing: state that Theorem 1.1 provides an *analytic characterization* of the dependency, rather than claiming it "establishes" a fundamental limitation. The theorem's value is as a vocabulary and motivating lens, not as a mechanistic proof.
4. Include a brief paragraph in Section 4.4 explaining the SVHN result — the adapter's ability to recover a badly biased prior (+46.84% from CLIP's 34.36% zero-shot to CaPT's 81.20%) is actually one of CaPT's strongest demonstrations and should be analyzed, not omitted.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 97D725GJtQ (SemiCLIP) | 5.80 | R1/R2 | Most topically similar; CaPT has larger gains, more comprehensive evaluation, more novel design — clearly stronger |
| dnqPvUjyRI (SemiReward) | 6.00 | R2 | Comparable SSL method paper; CaPT has larger margins, more benchmarks, stronger motivation — slightly stronger |
| RgWATMmWmz (Weakly Supervised + CLIP) | 4.75 | R1 | Weaker; narrower evaluation, incremental vs CaPT's clear gains |
| 1rgMkDWfYV (Noisy Label + CLIP) | 4.50 | R1 | Weaker; different problem setting, smaller contribution |
| 25kAzqzTrz (FixMatch theory) | 8.00 | R1 | Stronger; deeper theoretical contribution and tight theory-empirical link; CaPT's theory is weaker |
| RvUVMjfp8i (SSL Open Environments Benchmark) | 8.00 | R1 | Different type (benchmark paper); comprehensive across modalities; CaPT is a method paper with strong but narrower scope |
| vG9dVXwXQV (VLM Selection) | 6.33 | R2 | Different problem; roughly comparable methodological contribution level |
| g1fkhbhHjL (Black Sheep VLM) | 7.00 | R2 | Solid contribution with good empirical coverage; CaPT's empirical gains are larger but theoretical depth is comparable |

**Round 1 bracket**: 5.5–7.5

**Round 2 narrowing**: CaPT is clearly above SemiCLIP (5.8) and SemiReward (6.0): its empirical margins are far larger, the benchmark coverage more thorough, and the design more principled. It approaches but does not reach the 7.0–8.0 tier anchors due to the missing DebiasPL/CLS comparisons in main tables (which constitute a genuine evidential gap on the core claim of superiority over related work) and the overstated theorem framing. The paper lands in the 6.5 range: meaningfully above the 6.0 accepts, below the 7.0–8.0 tier.

**Score**: **6.5**
**Decision**: **Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>