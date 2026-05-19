Now I have enough calibration context. Let me synthesize the final review.

## Calibration Bracket and Final Score Determination

**Round 1 bracket**: 5.0 – 7.0 (the paper is clearly stronger than 3-range weak anchors but not at the 8+ oral level of unrelated topics).

**Round 2 narrowing**: I read RTA (5.50, Reject), L-TTA (5.00, Accept Poster), CLIP-DR (4.67, Reject), RAM-TTT (4.67, Reject), and MRAD (6.00, Accept Poster). RA-TTA is stronger than RTA, L-TTA, CLIP-DR, and RAM-TTT in terms of novelty and evaluation breadth. It is comparable to MRAD (6.00, Accept Poster) — both present a novel retrieval-based approach in domains dominated by parametric methods, both have extensive evaluation (17 vs 16 datasets), and both have similar minor weaknesses about variance reporting. RA-TTA's performance margins (2.49–8.45%) are clearer and more consistent than MRAD's improvements. I place RA-TTA slightly above MRAD at **6.5**.

---

## Summary

This paper proposes RA-TTA (Retrieval-Augmented Test-Time Adaptation), a training-free method that adapts VLMs at test time by retrieving external images from a web-scale database. The key innovation is using fine-grained text descriptions — generated offline by LLMs for each class — as a semantic bridge: first, text descriptions relevant to the test image are selected (image-to-description); then, external images matching those descriptions are retrieved (description-to-image). The retrieved images are fused with the VLM's initial prediction using an optimal-transport-based relevance scoring mechanism. Evaluated on 17 datasets, RA-TTA outperforms all compared methods (tuning-based, description-based, and retrieval-based) with average improvements of 2.49–8.45%.

---

## Strengths

1. **Novel and well-motivated approach.** The use of fine-grained text descriptions as a retrieval bridge is a creative and principled solution to the problem that naive image-to-image similarity often retrieves semantically irrelevant images. The analogy to document chunking in RAG (line 25–27) is apt and helps explain why this design works.

2. **Strong empirical results across diverse benchmarks.** RA-TTA achieves the best average accuracy on 12/13 transfer learning datasets (Table 1) and all 4 distribution shift datasets (Table 2), with consistent margins over both non-retrieval and retrieval-based methods. The improvement over Ensemble on ImageNet variants (+9.18%) is particularly notable.

3. **Ablation validates all components.** Table 3 shows that disabling description-based retrieval (Var. 1→Var. 2), description-based adaptation (Var. 2→Var. 3), and image weighting (Var. 3→RA-TTA) each degrades accuracy on FGVC Aircraft, confirming that all three components contribute positively.

4. **Training-free and practical.** Unlike tuning-based TTA methods (TPT, RLCF), RA-TTA requires no backpropagation or parameter updates, making it computationally efficient at test time.

---

## Weaknesses

### Major
None.

### Minor

1. **Ablation scope limited to one dataset.** The ablation study (Table 3) is conducted only on FGVC Aircraft — the dataset where RA-TTA's gains are largest. Repeating the ablation on at least 2–3 additional datasets spanning different granularities (e.g., ImageNet for coarse, Stanford Cars for fine-grained) would strengthen confidence that each component generalizes.

2. **No variance estimates reported.** The method involves stochastic augmentations (M=100 views, random cropping/flipping) and percentile-based selection, yet all tables report only point estimates. While single-run evaluation is common in CLIP-based TTA papers, reporting variance (e.g., over 3–5 runs with fixed seed sets) would allow readers to assess the statistical reliability of the claimed margins, some of which are sub-1% on ImageNet variants.

3. **Handling of classes outside the retrieved set is only implicit.** Equation (10) defines \(\hat{p}(c|x^{\text{test}})\) only for classes \(c \in \mathcal{C}\) (those whose descriptions were selected). The natural interpretation is \(\hat{p}=0\) for \(c \notin \mathcal{C}\), which completes the specification coherently (the convex combination in Eq. 11 remains normalized). However, the paper never states this explicitly, nor does it analyze how often the correct class falls outside \(\mathcal{C}\) or how this affects performance. A brief coverage analysis would suffice to close this gap.

### Trivial

1. The OT-based aggregation (Eq. 8) is not compared against simpler alternatives (e.g., non-OT weighted averaging). The ablation in Table 3 disables *image weighting* entirely but does not isolate whether *OT specifically* matters over a straightforward weighted average using the same weights. This would be a straightforward additional variant.

---

## Nice-to-Haves

- **Coverage analysis**: Report how frequently the correct class appears among the selected descriptions (\(\mathcal{C}\)) across datasets. If coverage is near-perfect, the concern about classes outside \(\mathcal{C}\) is largely moot.
- **Baseline database discussion**: A brief discussion of how SuS-X and Neural Priming performed in their original database setups vs. the shared LAION-based setup would preempt questions about whether the comparison favors RA-TTA's design.
- **Runtime analysis**: A table reporting per-image inference time for RA-TTA vs. tuning-based TTA methods (which require backpropagation) would highlight the practical advantage.
- **Failure cases**: One or two examples where RA-TTA underperforms a baseline would strengthen the qualitative analysis.

---

## Removed Points

1. **"Comparison to retrieval-based baselines may be unfair"** (Harsh Critic #3) — The paper explicitly states (line 188–189): "We construct the database for retrieval-based methods, including SuS-X-LC, Neural Priming, and our proposed RA-TTA" using the same keyword-matching procedure on LAION2B. All methods share the same external data source, so the comparison is fair. That SuS-X was originally evaluated on a different database (ImageNet train set) does not make this comparison unfair; it tests whether each method can effectively leverage the same noisy web-scale database, which is a valid and practical setting.

2. **"Underspecified handling ... could systematically harm performance" (Harsh Critic #1, characterization as fatal)** — The specification is implicit but complete: \(\hat{p}=0\) for classes outside \(\mathcal{C}\) is the standard convention. The convex combination in Eq. (11) is properly normalized. This is a minor clarity issue, not a structural gap. The concern about "systematically harming performance" is speculative without evidence of low coverage. Demoted to Minor.

3. **"No statistical variance reported" as a major weakness** — Single-run evaluation is the standard practice in CLIP-based TTA papers (e.g., TPT, RLCF, CuPL). While variance reporting would improve the paper, its absence does not undermine the core claims. Demoted to Minor.

4. **Strength Finder claims about problem importance, generic praise** — Removed per filtering rules as they are generic/superficial. Only the concrete, evidence-backed strengths (1–5 from Strength Finder) are retained.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder align on the paper's main claims and do not surface unexpected insights.

---

## Suggestions

1. Explicitly state the handling of \(\hat{p}(c|x^{\text{test}})\) for \(c \notin \mathcal{C}\) (Eq. 10) and add a coverage analysis showing how often the correct class is among the selected descriptions across datasets.
2. Add variance estimates (standard deviation over 3–5 runs with different seeds) to Tables 1, 2, and 3.
3. Extend the ablation study (Table 3) to at least 2–3 additional datasets (e.g., ImageNet, Stanford Cars, SUN397) to demonstrate that each component matters broadly, not just on the dataset with the largest gains.
4. Add an ablation variant that replaces OT aggregation with a simple weighted average (using the same weight vectors \(\mathcal{U}, \mathcal{V}\)) to isolate the benefit of the optimal transport framework.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>