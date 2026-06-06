Now I have a full picture of the paper. Let me draft the final review before running calibration searches.Now running all 5 bracketing calibration searches in parallel:Now let me read a few of the most comparable anchor papers for closer evaluation:I now have sufficient information to write the final review. The most comparable anchor in the corpus is `97D725GJtQ` (SemiCLIP, 5.80, Accept) — a CLIP+SSL integration paper with weaker results than CaPT. CaPT is meaningfully stronger: larger margins, more benchmarks, better ablations, and a more novel framework. I also verified all key reviewer claims against the paper text directly.

---

## Summary
CaPT proposes an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning (SSL) to break the label-dependency bottleneck where conventional SSL fails to exploit unlabeled data at extreme label scarcity. A fully fine-tuned unimodal ViT (UPM) and an adapter-tuned CLIP (MPM) are jointly trained via entropy-weighted co-pseudo labels and feature-augmented consistency regularization. CaPT achieves state-of-the-art results across multiple SSL benchmarks, most strikingly +21.38% on CIFAR-100 and +4.05% on EuroSAT under the one-label-per-class setting, while adding only 8% memory and 11% training time overhead over a single-model FreeMatch baseline.

---

## Strengths

- **Dramatic and robust gains in extreme label-scarcity regimes** (Tables 1, 3, 2): CaPT outperforms the best SSL baseline by 21.38% on CIFAR-100 (1 label/class), 9.33% on ImageNet (10 labels/class), and 6.18% on STL-10 (4 labels/class). These margins are sufficiently large that noise, tuning artifacts, or cherry-picking cannot plausibly explain them. Critically, CaPT also exhibits substantially lower variance across seeds than existing methods (Table 1, standard deviations), indicating it is less sensitive to labeled data quality.

- **Well-designed, thorough ablation** (Table 6): Each component is individually ablated. Adapter-tuning alone accounts for −12.73% on EuroSAT when disabled (CaPT-Deb), bidirectional flow matters (−0.88% to −1.49% without it), and even the modest contributions of feature-augmented consistency (−0.57/−1.81%) and entropy weighting (−0.87/−1.57%) are confirmed. The ablation is among the more careful in this line of work.

- **Concrete, multi-faceted motivating analysis** (Figure 1): Figure 1c directly shows that FreeMatch's accuracy gain from unlabeled data collapses to near-zero at 1 label/class on CIFAR-100 — the most direct empirical evidence that SSL's label-dependency is real and exploitable. Figure 1a shows the quality effect via prototypicality ordering. Together these ground the paper's problem statement without relying on the theorem alone.

- **Practical computational efficiency quantified** (Table 4): Adding a full CLIP branch costs only 8% memory and 11% training time over single-model FreeMatch — a striking efficiency claim enabled by CLIP's frozen encoder, which requires only activation and small-adapter gradient memory. The claim is verifiable and directly relevant to practitioners.

- **Cross-modal complementarity is directly visualized** (Figure 3): Attention maps confirm that two unimodal ViTs with different initializations still attend to the same image regions (eye and beak of a rooster), while CLIP attends to a distinct discriminative feature (the comb). This gives direct mechanistic support for the asymmetric co-training design.

- **Adapter-tuning effectively corrects CLIP's prior bias** (Figure 5): Class distribution plots on EuroSAT show raw CLIP concentrating ~25% predictions on a single class; adapter-tuned CLIP achieves a near-uniform distribution. This validates the mechanism rather than just reporting an aggregate number.

---

## Weaknesses

### Fatal
None.

### Major

- **DebiasPL and CLS absent from all result tables**: DebiasPL (Wang et al., 2022a) is the closest prior work — Figure 2 contrasts it architecturally, the introduction argues against it, and the paper's framing depends on the claim that CaPT improves over it. Yet DebiasPL never appears in Tables 1–5 as a competing method. The ablation row "CaPT-Deb" (Table 6) is explicitly described in Section 4.5 as disabling *both* adapter-tuning *and* the vision-model→CLIP flow simultaneously, conflating two distinct design choices. A row that disables only adapter-tuning would cleanly isolate the contribution relative to DebiasPL's approach; as written, the ablation cannot serve this purpose. CLS (Yao et al., 2022) — the paper's most direct methodological predecessor for the co-training component, discussed in both the introduction and related work — is also absent from every result table. Without these direct comparisons, the paper cannot conclusively distinguish how much gain comes from (a) co-training per se, (b) CLIP as the co-training partner specifically, or (c) the adapter-tuning design. The conclusions are likely correct, but the experimental design leaves the argument incomplete.

### Minor

- **SVHN result and FGVCAircraft underperformance are not analyzed** (Table 5): CaPT achieves 81.20% on SVHN at 2 labels/class versus FreeMatch's 67.35%, yet CLIP's zero-shot accuracy on SVHN is only 34.36% — far below any SSL baseline. This is the most surprising positive result in the paper, and it is left entirely unexplained. Conversely, FGVCAircraft at 5 labels/class is the only setting where CaPT trails a baseline (50.12% vs. FreeMatch's 51.43%), and the paper defers entirely to the appendix. These are the two cases where readers most need the paper's analysis.

- **Theoretical framing overstates Theorem 1.1's scope**: Theorem 1.1 uses a Gaussian mixture model with a nearest-prototype classifier — assumptions far from the actual training setup. The paper describes this as establishing "a fundamental limitation of SSL" and lists it as a contribution ("we theoretically establish the label dependency"). The theorem is correct and provides useful vocabulary, but the actual mechanism by which CLIP's text-grounded representations help is not formalized; the theorem only addresses labeled-data statistics. This is a framing issue rather than a structural flaw, but the contribution list overstates what the theorem delivers.

- **Hard pseudo-label choice in Eq. 13 is unmotivated**: The co-pseudo label is formed as a weighted sum of two argmax outputs (one-hot vectors), not soft probabilities. When the two models disagree on the top class but share similar second-order distributions, discarding that uncertainty could increase noise in the supervision signal. This load-bearing design choice is neither motivated nor ablated. An ablation comparing hard vs. soft weighting is straightforward and would either confirm robustness or reveal a gap.

### Trivial
None.

---

## Nice-to-Haves

- Add a separate ablation row that disables *only* adapter-tuning (keeping bidirectional flow) and another that disables *only* bidirectional flow (keeping adapter-tuning), to cleanly isolate each contribution from DebiasPL.
- Bring the SVHN analysis into the main text — the story that adapter-tuning rescues a 34% zero-shot prior to achieve 81% is actually the paper's most compelling demonstration of the co-training mechanism's ability to correct domain-biased CLIP predictions.
- Ablate hard vs. soft weighting in Eq. 13.
- A brief explicit statement in the main text explaining why CaPT's memory overhead is only 8% (CLIP's frozen encoder requires only activation and small-adapter gradient memory) would prevent readers from discounting Table 4.
- One or two settings from Table 1 with CLS as a baseline would directly motivate the asymmetric-modalities design over co-training two unimodal models.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Feature-augmented consistency is a computational workaround being overstated as principled regularization"** (Harsh Critic): Section 3.2.2 explicitly states both motivations: "not only improves the generalization of CLIP but also avoids the need to construct another high-resolution version." The paper clearly acknowledges the efficiency motivation. Removed as strawman.

- **"ImageNet 10-label result is not trivially low supervision"** (Harsh Critic): Ten labeled samples per class across 1000 classes is standard "low-supervision" framing in the SSL community. This is scope-creep criticism. Removed.

- **"CLIP's cross-modal complementarity as a strength" — generic framing** (Strength Finder): The visualization in Figure 3 is concrete and specific, so this strength is retained in its specific form above.

- **CaPT-Ada and CaPT-Deb as general strengths of the ablation** (Strength Finder): Retained in merged form under the ablation strength above.

---

## Novel Insights

The most genuinely novel observation synthesized from the reviews is the interaction between CLIP's domain bias and CaPT's co-training loop: CLIP's zero-shot accuracy on SVHN (34.36%) is far *below* any SSL baseline, yet CaPT achieves 81.20% after adapter-tuning within the co-training loop. This suggests CaPT's value is not CLIP's raw zero-shot quality but rather the combination of (a) cross-modal representational complementarity even when raw CLIP is uninformative, and (b) the co-training loop's ability to progressively correct CLIP's domain-specific biases through UPM supervision. This point is mechanistically richer than what the paper emphasizes, and unpacking it would sharpen the paper's central claim.

---

## Suggestions

1. Add DebiasPL as a direct baseline in at least Tables 1 and 3 (or report one clearly reproducible setting), and split the CaPT-Deb ablation row into two rows that isolate adapter-tuning and bidirectional flow independently.
2. Expand the SVHN analysis into the main text with at least one figure showing the class distribution evolution under adapter-tuning for SVHN, contrasting with EuroSAT. This is the paper's most striking result and deserves a first-class explanation.
3. Ablate hard vs. soft pseudo-label weighting in Eq. 13.
4. Add one row of CLS results in a comparable setting to directly motivate the asymmetric-modalities design.

---

## Score and Decision

**Originality**: High. Asymmetric-modalities co-training with a parameter-efficiently fine-tuned CLIP as the prior provider is a genuinely novel design, distinct from prior CLIP+SSL approaches (CLIP-Adapter, DebiasPL, CLS).

**Importance of research question**: High. Extreme label scarcity (1 label/class) is a practically important regime; identifying and addressing the label-dependency of SSL is well-motivated.

**Claims supported**: Mostly well-supported. The ablation study is comprehensive. The missing DebiasPL and CLS comparisons are genuine gaps but do not invalidate the core claim.

**Soundness of experiments**: Good. Multiple benchmarks, multiple label regimes, consistent results. The variance reduction result is an additional positive signal.

**Clarity of writing**: Good. The framework is clearly explained, the modules are well-named, and the figures are informative.

**Value to the research community**: High. The framework is portable to other VLMs (noted in the conclusion), the efficiency results are practically relevant, and the empirical results are among the strongest in this area.

The paper is above `97D725GJtQ` (SemiCLIP, 5.8, Accept) — which achieves 1–7% improvements and has weaker ablations — and clearly stronger than the rejected `XCg9YcSKCZ` (SelfPrompt, 3.5). The missing DebiasPL/CLS comparisons are the main gap, addressable in revision. The overall contribution is genuine and the empirical support is strong.

**Score: 6.5 | Decision: Accept**

---

# Selected Anchors

<related>["97D725GJtQ", "XCg9YcSKCZ", "kaZAKvjLro", "KZZbdJ4wff", "RgWATMmWmz", "I5S1a1NKxo", "9bMZ29SPVx"]</related>

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>