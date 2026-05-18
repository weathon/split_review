Now I have a clear calibration picture. Let me write the final consolidated review.

## Summary

This paper introduces **distributed neural architectures (DNAs)**, where each token follows a learned, content-dependent path through a collection of modules (transformer blocks, attention, MLP, identity) via end-to-end trained routers. The authors train DNA models at ViT-Small and GPT-2 Medium scales, show they are competitive with dense baselines, and analyze emergent patterns including power-law path distributions, module specialization, and interpretable compute allocation. The paper is framed as a feasibility study rather than a SOTA pursuit, with the interpretability analysis being its strongest contribution.

---

## Strengths

1. **Novel and ambitious architecture concept.** DNAs generalize MoE, MoD, weight sharing, and early exit into a unified framework where tokens discover their own computational paths. The idea of learning *both* which modules to use and in what order, end-to-end, is genuinely novel and opens a new design space.

2. **Interpretability analysis is compelling and well-controlled.** The path-based grouping of patches (Fig. 3) convincingly shows that low-rank paths aggregate edges/color regions while high-rank paths capture specific concepts (brass instruments, puzzle pieces). The reconstruction visualization (Fig. 4) demonstrates that routing decisions develop from texture/edges to object-level features. The comparison against random-network baselines is a good sanity check.

3. **Demonstrated feasibility in two domains.** Vision (ImageNet, within ~1% of ViT-Small) and language (FineWeb-Edu, competitive with GPT-2 Medium on 5/7 benchmarks) provide a breadth of evidence that DNAs are trainable across fundamentally different tasks.

4. **Emergent compute allocation is interpretable.** The analysis in Fig. 5 shows that the vision model allocates compute roughly proportional to visual complexity (boundary-heavy images get more compute), and the qualitative examples are convincing. The finding that compute and parameter savings are uncorrelated is a non-trivial observation.

5. **Power-law path distribution is a clean quantitative finding.** The fact that trained paths follow a power-law (exponent -1.2 for language, -1 for vision) and that even random networks produce a power-law with exponent -1 is a well-characterized emergent property.

---

## Weaknesses

### Major

- **Compute efficiency claim is overstated for language.** The abstract claims "minor effects on performance" from compute savings, but the top-2 DNA with 30% skip degrades substantially: HellaSwag drops from 41.8→35.5 (−6.3), LAMBADA from 34.0→23.8 (−10.2), BoolQ from 61.0→52.9, and validation loss jumps from 2.674→2.784. These are not "minor effects." The vision skip model (78.8% vs. 79.8%, −1.0%) supports the claim better, but the language results directly contradict the broad statement in the abstract.

- **No comparison against the most relevant baselines (MoE, MoD).** The paper positions DNAs as a natural generalization of MoE, MoD, and weight sharing, yet the only baselines are standard dense ViT and GPT-2. The central question — whether learned dynamic routing provides any advantage over hand-designed conditional computation — is untested. A parameter- and compute-matched MoD or Switch Transformer baseline would directly probe whether the extra flexibility of DNAs pays off. This gap weakens the evidence that the routing mechanisms are genuinely useful rather than an elaborate way to replicate what simpler architectures already do.

- **The top-2 DNA language model uses 433M active parameters vs. GPT-2's 406M.** While the gap is small (27M), many of the reported benchmark advantages for top-2 DNA fall within a range that could be explained by the extra active capacity, especially given the absence of variance estimates. The paper acknowledges this via the "non-shared active" column (266M vs. 406M), but the primary comparison is on active params, which favors the DNA model.

### Minor

- **Results are from single runs with no variance estimates.** Given the stochasticity in routing decisions, it is unknown whether the ~0.7–1.0% gaps for vision and the ~0.5–1.3 point differences for language are stable or reflect unlucky/good seeds. Multi-seed experiments with mean±std would substantially strengthen the reliability claims.

- **Compute is measured as "modules used," not FLOPs.** Modules have very different computational costs (attention vs. MLP vs. identity). FLOPs or wall-clock time would provide a cleaner efficiency metric. The current "effective compute nodes" conflates attending to 50 tokens with attending to 2 tokens.

- **The skip rate hyperparameter is not ablated.** For the language compute-efficiency model, only one skip rate (30%) is evaluated, and it degrades performance significantly. A trade-off curve showing accuracy vs. %skipped would give a much clearer picture of what the architecture can achieve.

- **No quantitative measure of interpretability.** The path-specialization analysis (Figs. 3, 8) is entirely qualitative. Correlation with segmentation masks (vision) or clustering metrics compared to embedding-similarity baselines (language) would strengthen the claims substantially.

### Trivial

- The legend order in Fig. 2 (top-left) does not match the curve order, making the plot harder to read.

---

## Nice-to-Haves

- A Mixture-of-Depths or Switch Transformer baseline at matched total parameters and training budget would be the single most useful addition to validate the contribution.
- Ablating the `r` (skip ratio) and `u` (update speed) hyperparameters from Eqs. 2–3 would help understand sensitivity.
- For the vision skip model, edge-detection masks could quantitatively verify the claim that "the model prioritizes boundary patches."

---

## Removed Points

These points from the inputs are flagged for removal — treat with caution.

- **"Vision skip model accuracy is never reported"** — Factually wrong. The accuracy of the top-2 DNA (25% skip) model is reported as 78.8% in Figure 2 (top-left panel and its caption). The harsh critic's central criticism on this point is based on a missed reading of the figure.
- **"HellaSwag loses nearly 12 points (41.8→35.5)"** — The actual drop is 41.8−35.5 = 6.3 points, not "nearly 12." The critic appears to have misread the numbers. The LAMBADA drop (34.0→23.8 = 10.2) is correctly stated, but the inflated HellaSwag number is an error.
- **"Active parameter counts imply the skip model has no inactive parameters — inconsistent"** — The 18M active = 18M total simply means all modules are visited by some token, which is expected for a top-2 routing model. The "25% skip" refers to tokens skipping modules, not modules being unused. The accounting is internally consistent.
- **"Figure 2 top-left legend does not match curve order"** — While this is technically a presentation issue, the curves are clearly labeled with accuracy values in the caption, so the criticism is overstated.
- **"Missing appendix content"** — The parser strips appendix content from all papers. The original submission contains the appendix.

---

## Novel Insights

The most notable synthesis from the reviews is that the paper's strongest contribution (interpretable emergent paths and compute allocation) and its weakest link (incomplete evaluation of the compute efficiency claim) are actually connected: the interpretability analysis would be far more convincing if paired with a quantitative, well-baselined demonstration that the learned routing patterns actually *improve* the accuracy-efficiency trade-off over existing conditional computation methods. The paper shows DNAs *can* learn interpretable patterns, but does not yet show that learning these patterns is *useful* in a way that simpler alternatives (MoD's per-layer binary decisions, MoE's expert selection) cannot match. This is a clear direction for future work rather than a fatal flaw, given the feasibility-study framing.

---

## Suggestions

1. **Fix the compute efficiency claim** to be honest for both domains: state the vision results (1% drop for 25% compute savings) and acknowledge that the language skip model degrades significantly.
2. **Add at least one conditional computing baseline** (e.g., a MoD-style model at matched total parameters and compute budget) to validate that the routing flexibility provides genuine benefits.
3. **Run 3 seeds** for at least the main comparisons (Tables 1 and 3) and report mean±std.
4. **Add a FLOPs-based compute measurement** alongside the module-count-based one.
5. **Add a quantitative interpretability metric** (e.g., correlation with segmentation masks for vision).
6. **Move the "parameter sharing is random in language" finding** (Sec. 4.3) to earlier discussion — it is an honest and important negative result that should not be buried.

---

## Score and Decision

**Round-1 bracket:** [4.0, 6.0] — the paper is clearly above the 3.0-level anchor papers (which have fundamental methodological problems) and below the 8.0-level anchor papers (which are comprehensive, fully-evaluated works).

**Round-2 narrowing:** 

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Understanding Cross-layer Contributions to MoE | BqyPLOkxFY.md | 5.00 | R1 | Similar tier. Both have interesting analyses with methodological gaps. The DNA paper has more novelty but weaker baselines. |
| ProMoE (Routing Matters in MoE) | 1w1jCfYM8P.md | 5.00 | R1 | Similar tier. ProMoE has stronger experiments (multiple sizes, ablations) but less novel conceptual contribution. |
| Composable Sparse Subnetworks | IHwx5ioIP2.md | 5.50 | R2 | Slightly stronger. More thorough evaluation across datasets, though limited to small-scale settings. |
| Expert Divergence Learning | wrqYMYazm0.md | 5.50 | R2 | Slightly stronger. Better-evaluated MoE routing method, though more incremental. |
| Rewiring Experts on the Fly | v5qb8BG18G.md | 4.00 | R1 | Weaker. Accepted but with more significant evaluation gaps. |
| Where do LVLMs Look | OqVbYxDBHV.md | 4.50 | R2 | Similar/weaker. Comparable novelty but rejected due to methodological concerns. |

The paper is most comparable to the 5.00 anchors (MoE routing/analysis papers) in terms of overall quality: genuine contribution, interesting analysis, but notable evaluation gaps. It is slightly below the 5.50 anchors which have more thorough experiments. Given the novelty of the architecture concept and the strength of the interpretability analysis, balanced against the missing baselines and overclaimed compute efficiency statement, the paper sits at the upper end of the 5.0 band.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>