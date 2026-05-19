Now I have thoroughly read the paper. Let me now produce the final consolidated review.

## Summary

This paper introduces *category information amount* (IA), defined as the volume of a class's perceptual manifold (computed from the determinant of a regularized covariance matrix of instance embeddings), as a measure of category learning difficulty in object detection. The authors observe that IA has higher negative correlation with per-class AP than instance count does, and propose the Informativeness-Guided Angular Margin (IGAM) Loss, which dynamically adjusts angular decision boundaries based on IA ratios. A low-cost covariance-merging strategy enables end-to-end IA updates. Experiments on LVIS v1.0, COCO-LT, and Pascal VOC show consistent gains, especially on rare categories (+2.4% AP_r vs. second-best on LVIS with R-50-FPN).

## Strengths

- **Novel perspective on category difficulty:** The paper demonstrates that instance count has near-zero correlation with per-class AP on Pascal VOC (a balanced dataset), while IA shows consistently stronger negative correlation (−0.68 to −0.65) on LVIS and COCO-LT (Table 1, Figure 2). This is the first work to report this finding specifically for object detection and provides a principled alternative to instance-count-centric rebalancing.

- **Substantial and consistent gains on rare categories:** IGAM achieves state-of-the-art results on LVIS v1.0 rare categories — 17.7% AP_r with R-50-FPN, surpassing the second-best method (BACL) by 2.4% (Table 4) — while maintaining competitive AP on frequent categories (AP_f within 0.3% of the best method). On COCO-LT, IGAM outperforms the second-best method on the rarest group (AP₁) by 2.3–3.0% (Table 5). These gains hold across two backbones and multiple detection frameworks (Faster R-CNN, Cascade Faster R-CNN, Mask R-CNN).

- **Practical dynamic update mechanism:** The local-to-global covariance merging strategy (Section 3.3) reduces additional memory requirements by 56–74% (from 295.72 MB to 78.29 MB on MS COCO-class settings), making end-to-end IA updates feasible during training without storing all instance embeddings.

- **Reduction in model bias:** On LVIS v1.0, IGAM reduces the variance of class-wise AP by approximately 50% compared to Seesaw (Figure 4), suggesting that IA-guided margin allocation produces fairer decisions across the category spectrum.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation that isolates the role of information amount vs. the margin framework itself.** The paper's central claim is that IA is superior to instance count for guiding decision boundaries. However, all comparisons (Tables 3–5) compare IGAM against cross-entropy or existing long-tail methods. There is no ablation comparing IGAM against: (a) the cosine-softmax baseline (Equation 5, the loss without any margins), (b) a version with a *uniform* angular margin applied to all classes, or (c) a version where the margin is based on *instance count* instead of IA. Because the paper does not isolate whether the improvements come from the cosine-normalization framework alone or from IA-guided margin adjustment specifically, the core causal claim ("IA leads to better decision boundaries") is not directly tested. This is the most significant gap in the experimental validation.

- **No statistical significance or multiple-run variability reported.** All tables report single-run results. On Pascal VOC, the overall mAP improvement over the second-best method is 0.8% and 1.1% — well within typical run-to-run variation in object detection. On LVIS, while improvements on rare categories are larger (2.4%, 1.6%), the absence of error bars means the reader cannot assess whether even these gains are stable. Given that many baselines (Seesaw, EFL, C2AM) are close on overall AP, the paper needs at least 3 runs with standard deviations to establish that IGAM's advantages are not artifacts of a favorable seed.

### Minor

- **λ hyperparameter sensitivity not investigated.** The harsh critic mentions a scaling factor λ in the margin formula (Equation 7). The paper's parsed text appears to have this equation as a stripped image, so the exact formulation is not fully accessible in the available text. If λ exists, the paper tunes the cosine scale *s* (Table 2) but does not examine the sensitivity of results to λ, nor suggest a principled default. Since a method requiring fine-grained tuning of an additional hyperparameter reduces practical utility, this should be addressed.

- **Correlation analysis would benefit from statistical rigor.** Table 1 reports Pearson correlations between IA and AP (−0.68 to −0.65) but provides no confidence intervals or p-values. While the paper provides a useful correlation comparison between IA and instance count (Figure 2), including interval estimates would strengthen the claim that IA is a significantly better predictor of difficulty.

- **Model bias analysis (Figure 4) lacks numerical breakdown by frequency group.** The claim of ~50% variance reduction is reported in text, but there is no breakdown showing whether this reduction comes from improving tail categories, harming head categories, or both. The paper should verify that frequent-category AP is not disproportionately sacrificed.

- **Dynamic update strategy evaluation is limited to storage cost.** Section 3.3 compares storage but does not report training time overhead per epoch or an ablation showing that the dynamic update (vs. a static IA computed at epoch 0) materially improves performance.

### Trivial
None.

## Nice-to-Haves

- Compare against an instance-count-based margin version within the same IGAM framework to directly test the claim that IA is superior to instance count for margin allocation.
- Report multiple seeds (3) with standard deviations for the main tables.
- Provide a sensitivity analysis over the margin scaling parameter (if λ exists in the formula).
- Include a breakdown of model bias variance by frequency group (rare, common, frequent).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Cherry-picked evaluation on Pascal VOC"** — The original harsh criticism claimed the paper selected five categories post-hoc in a misleading way. However, the paper states that *Table 6 presents the performance of each method across all categories as well as the overall performance.* The full per-class matrix is shown; the five categories are highlighted for discussion emphasis, not to hide results. The overall mAP is also reported (77.7% vs. 76.9%, +0.8%). The underlying concern about statistical significance is retained as a Major weakness above, but the "cherry-picking" framing is inaccurate.

- **"Correlation analysis: no comparison with instance-count correlations on the same datasets"** — Figure 2's caption explicitly states it shows *"Pearson correlation coefficients between category information amount and category average precision and between category instance count and category average precision, under two backbone networks and three loss function settings."* This indicates both correlations are shown. The claim is therefore factually incorrect about what the paper contains.

- **"Circularity in IA computation"** — The critic argues that computing IA from the same model being evaluated introduces circularity. However, this is the standard approach used in the prior work the paper builds on (DSB, Ma et al. 2023a). If IA were computed from a separate model, it would measure that model's geometry, not the current model's. This is a design choice, not a flaw.

- **"No justification for determinant as the right measure"** — The paper explicitly justifies this via the manifold distribution hypothesis and the volume interpretation of the covariance determinant (Section 3.1, lines 106–110). This is standard in information geometry.

- **"No ablation of dynamic update necessity"** — While it would strengthen the paper, the dynamic update is a practical engineering mechanism; the core contribution is the IA-guided margin. The paper focuses on storage efficiency, which it quantifies. This is a reasonable scope choice.

## Novel Insights

The harsh critic and strength finder together surface a meta-level observation that the harsh critic does not fully articulate: the paper's empirical case is strongest where it measures a *quantity* (IA's correlation with AP) and weakest where it tests a *causal mechanism* (IA-guided margins specifically driving the improvements). The strengths focus on the measured improvements on rare categories (which are genuine and substantial), while the harsh critic zeroes in on the absence of the ablations that would convert correlation into causation. The synthesis of these two perspectives reveals that the paper's main gap is experimental design, not conceptual — the idea itself is well-motivated and the raw results are promising, but the evidence chain has a missing link. This is a more precise diagnosis than either input alone provides.

## Suggestions

1. Add an ablation that replaces IA with instance count in the same angular-margin framework. If IGAM (IA-based) outperforms IGAM (count-based), the core claim is directly validated.
2. Add the cosine-softmax baseline (Equation 5, uniform margins) as a row in Table 4 to establish the baseline improvement from the margin framework alone.
3. Report 3 runs with standard deviations for the main results (LVIS Table 4, Pascal VOC Table 6).
4. Investigate λ sensitivity over at least 3–5 values or propose a principled default based on the IA distribution.
5. Provide a frequency-group breakdown of the variance in Figure 4 to show that variance reduction is not achieved by sacrificing frequent-class performance.

## Score and Decision

**Originality:** 7/10 — The concept of using manifold volume to guide margins in detection is novel. The finding that IA correlates better with AP than instance count is a useful empirical observation.

**Importance of research question:** 8/10 — Category bias in object detection is an important problem, and moving beyond instance-count-based reasoning is a timely direction.

**Claims well-supported:** 6/10 — The correlation analysis supports the motivation, and the SOTA results on rare categories are compelling. However, the missing ablation (IA vs. count in the same margin framework) weakens the central causal claim. No error bars further reduce confidence.

**Soundness of experiments:** 6/10 — Reasonably thorough across three datasets and multiple backbones, but missing key controls and statistical grounding.

**Clarity of writing:** 7/10 — The motivation, method derivation, and main results are clearly presented. Some equation details are lost to parsing artifacts in the available text.

**Value to the research community:** 7/10 — The IA concept and the dynamic covariance merging technique are both reusable by the community. The paper opens a new direction for detection beyond instance count.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>