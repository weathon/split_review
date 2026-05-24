Now I'll compile the final review.

## Summary

This paper identifies and formalizes a label-dependency limitation in existing SSL methods—where pseudo-label quality degrades with the quantity/quality of labeled data—and proposes CaPT, a co-training framework that integrates a parameter-efficiently tuned multimodal CLIP model with a fully fine-tuned unimodal vision network. The asymmetric-modalities design mitigates the pattern-homogeneity bottleneck of prior co-training methods. CaPT achieves state-of-the-art results across multiple benchmarks, with particularly large gains under extreme label scarcity (e.g., +21.38% on CIFAR-100 with 1 label per class), while adding modest computational overhead (8% memory, 11% time).

## Strengths

1. **Novel asymmetric-modalities co-training framework.** CaPT jointly trains a unimodal vision network (fully fine-tuned) with a multimodal CLIP model (adapter-tuned), using entropy-weighted co-pseudo labels. This design is well-motivated: Figure 3 and Appendix B demonstrate that CLIP's attention patterns diverge substantially from those of pure-vision ViTs (e.g., attending to a rooster's comb vs. the eye/beak), providing genuinely complementary views that enrich mutual learning beyond the CLS approach of co-training two unimodal networks.

2. **Strong and consistent empirical results across diverse settings.** CaPT outperforms 12 established SSL methods on 14 of 15 evaluation settings across USB benchmarks (Tables 1), ImageNet (Table 2), extreme low-label regimes (Table 3), and fine-grained datasets (Table 5). The gains are particularly compelling under extreme label scarcity: on CIFAR-100 with 1 label per class, CaPT achieves 82.51% vs. 61.13% (FreeMatch) and 60.49% (RegMixMatch)—a >21% absolute improvement.

3. **Comprehensive ablation study validates design choices.** Table 6 systematically ablates each component (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM, w/o feat aug., equal weights), showing that every component contributes. Crucially, "only MPM" (CLIP alone with adapter tuning) achieves 68.32% vs. CaPT's 84.83% on CIFAR-100 2-label, demonstrating that the co-training dynamic, not just CLIP's prior, drives the gains.

4. **Computational efficiency is demonstrated.** Table 4 shows CaPT adds only 8% memory (5050 vs. 4676 MiB) and 11% time (0.1044 vs. 0.0939 sec/iter) over FreeMatch while achieving significantly higher accuracy. This addresses a practical concern about deploying CLIP in SSL.

5. **Generalization across domain shift is evidenced.** On fine-grained datasets where CLIP's zero-shot accuracy is weak (e.g., SVHN 34.36%, StanfordCars 52.63%), CaPT still substantially outperforms baselines (e.g., +14.01% on StanfordCars 5-label), suggesting genuine SSL improvement beyond CLIP's prior.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with published CLIP-based SSL methods.** The paper systematically compares against 12 SSL methods without CLIP access, but the most direct way to establish that CaPT's co-training design (not just CLIP's prior) is responsible for the gains is to compare against published SSL methods that also use CLIP. DebiasPL (Wang et al., 2022a) is cited and discussed but not directly compared in the main tables. The ablation variant "CaPT-Deb" approximates it but is not the exact algorithm (it disables adapter-tuning and vision-model→CLIP flow, whereas DebiasPL uses CLIP zero-shot high-confidence selection without adapter tuning). A direct comparison on the same benchmarks—or on a subset such as CIFAR-100 2-label—would cleanly separate the contribution of CaPT's co-training design from the benefit of simply having CLIP in the loop. This is the paper's most significant evaluative gap.

### Minor

1. **Theoretical motivation is disconnected from the proposed method.** Theorem 1.1 provides a bound on pseudo-label error for a nearest-prototype classifier under a Gaussian mixture model. While it plausibly illustrates that labeled-sample quality/quantity affects pseudo-label accuracy, the bound contains a $(K-1)2^{d/2}$ multiplicative factor that makes it vacuous for any realistic input dimension $d$ (e.g., $d=224^2\times 3$). More importantly, the theorem does not inform the design of CaPT—it motivates the *problem* (label dependency), not the *solution* (asymmetric-modalities co-training). The paper would be better served by either (a) tightening the analysis to connect to CaPT's actual mechanism (e.g., how CLIP's prior changes the bound), or (b) reducing the theory to a brief intuitive argument and using the freed space for additional empirical analysis.

2. **Data contamination from CLIP's training data is discussed but could be addressed more quantitatively.** The paper acknowledges this concern in Section 4.4 and Appendix M, and the fine-grained benchmark results (Table 5) provide partial evidence against data leakage. However, per-dataset CLIP zero-shot accuracy on every benchmark's test set would help readers assess how much of CaPT's advantage is attributable to CLIP's prior vs. SSL improvement. For instance, on CIFAR-100 2-label, CLIP zero-shot gets 65.10%, adapter-tuned CLIP gets 74.90%, and CaPT gets 84.83%—reporting the headroom above the best CLIP-only baseline would sharpen the analysis.

3. **Entropy weighting dynamics are not analyzed.** The paper proposes entropy-based weights $\Gamma^a$ and $\Gamma^b$ that should shift from CLIP-dominant (early training) to UPM-dominant (late training), but no analysis of this trajectory is provided. A figure showing how these weights evolve during training would strengthen the claims about adaptive weighting and provide insight into when and how CLIP's prior is most useful.

### Trivial

- Figure 1 caption references "Set 1 and Set 2" for the radar chart, while the main text describes "Set 0, Set 1, Set 2" (three sets). Clarify which sets are shown.
- The unimodal network backbone (ViT-S/16 pre-trained on ImageNet, following USB) should be stated explicitly in the main text rather than deferred to Appendix F.

## Nice-to-Haves

- An ablation on the confidence-thresholding mechanism (described after Eq. 15) would clarify its interaction with entropy-based weighting.
- Testing with a larger CLIP variant (e.g., ViT-L/14) or alternative PEFT methods (LoRA) would strengthen robustness claims.
- The same $\lambda$ is used for both feature Mixup (Eq. 9) and co-pseudo label mixing (Eq. 14)—a brief ablation uncoupling these would confirm the design choice.

## Removed Points

These points from the reviewers were removed after verification against the paper:

1. *"The bound depends on $\eta$ through $\varepsilon_n$ but is stated as a probability over draws; the presentation is confusing."* — This is factually incorrect. $\eta$ appears in the probability statement ("with probability at least $1-\eta$") and through $\varepsilon_n$ (which contains $\log(K2^{d/2}/\eta)$) in the bound. The presentation is standard.
2. *"The paper does not discuss data contamination."* — The paper explicitly states in Section 4.4: "To preclude any advantage for CaPT arising from potential overlap between CLIP's corpus and simple benchmarks" and refers to Appendix M for in-depth discussion. The concern is partially addressed, though could be more quantitative (see Minor weakness #2).
3. *"The comparison with FreeMatch on time/memory is unfair because FreeMatch does not include CLIP."* — The purpose of Table 4 is to show the *overhead* of adding CLIP, not to claim a fair resource-equivalent comparison. The table clearly states the absolute values, and the modest overhead strengthens the practicality claim.
4. *"Standard deviations for CaPT are suspiciously low."* — Low variance when a strong prior (CLIP) stabilizes training is an expected behavior, not a flaw. The paper could discuss this, but it's not a weakness.

## Novel Insights

The most insightful synthesis across the reviews is that the paper's strongest evidence for its core claim comes not from the large-margin CIFAR-100 results (where data contamination is hardest to rule out) but from the fine-grained benchmarks (Table 5): on SVHN, StanfordCars, and Flowers102—where CLIP zero-shot is modest (34–61%)—CaPT still outperforms baselines by substantial margins (up to +14%). This cross-dataset pattern triangulates the contribution: if gains were purely from CLIP's prior, they would collapse on fine-grained datasets where CLIP is weak. That they remain large suggests the co-training framework genuinely improves SSL beyond simply inheriting CLIP's weights.

## Suggestions

1. **Include at least one published CLIP-based SSL baseline.** The single highest-leverage improvement is to run DebiasPL (or a faithful re-implementation) on 2–3 of the main benchmarks (e.g., CIFAR-100 2-label, EuroSAT 2-label). Even a subset of settings would address the central evaluation gap.
2. **Tighten or trim the theory.** Either connect Theorem 1.1 to the actual co-training mechanism (e.g., show how CLIP's bounded bias $B$ is reduced by adapter tuning), or reduce it to a brief intuitive paragraph and use the space for additional analysis (e.g., entropy weight dynamics).
3. **Report CLIP zero-shot accuracy for every test set.** Add a row to each main table showing the CLIP zero-shot accuracy on that dataset, enabling readers to directly compute the headroom above CLIP's prior.
4. **Make the unimodal backbone explicit in the main text.** State that UPM uses ViT-S/16 pre-trained on ImageNet-1K following USB conventions, preferably in Section 3.1.

## Score and Decision

Based on calibration against human-reviewed anchors:

**Round 1 bracketing** (all queries: "semi-supervised learning CLIP model co-training"):
- Weak band (<3.5): anchors at 2.50–3.40 — rejected/withdrawn papers with major flaws
- Middle band (3.5–7.5): anchors at 4.25–5.80 — mixed; SemiCLIP (5.80, poster) is closest in topic
- Strong band (>7.5): anchors at 8.00 — spotlight/oral papers, clearly stronger contributions

**Round 1 bracket: 5.5–7.5.**

**Round 2 narrowing** (queries targeting SSL + CLIP + framework papers in the 5.5–8.0 range):
- SemiCLIP (5.80, poster, topic-matched anchor): Semi-supervised CLIP adaptation with semantic concept mining + trapezoidal consistency. CaPT has larger gains (up to 21.38% vs. 1.72–6.58%), a more novel framework, and stronger ablation. **CaPT is stronger.**
- C-CLIP (6.50, poster): Continual learning for CLIP. CaPT's experimental evaluation is comparably thorough, and CaPT's contribution (integrating VLMs into SSL) addresses a problem of at least equal importance. **CaPT is comparable.**
- DiffMatch (6.67, poster): Semi-supervised semantic segmentation with diffusion models. Comparable theoretical depth and experimental rigor. **CaPT is comparable.**
- Understanding CLIP Transfer (6.50, poster): Theoretical analysis of CLIP. CaPT has stronger empirical contributions but weaker theory. **Comparable overall.**

CaPT is clearly stronger than the 5.80 anchor (SemiCLIP) and comparable to the 6.50–6.67 anchors, placing it above the bottom of the bracket but below the 8.00 level. The paper has a genuine contribution (asymmetric-modalities co-training), thorough experiments, and a careful ablation. The main weakness is the absence of a direct comparison with published CLIP-based SSL baselines, which prevents fully isolating the co-training contribution. This is a significant but not fatal gap.

**Final score: 6.5 — a solid paper with real contributions and some addressable weaknesses.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>