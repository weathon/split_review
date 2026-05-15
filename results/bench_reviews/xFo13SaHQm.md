Now I have all the information needed. Let me write the consolidated final review.

## Summary
This paper tackles the copy-paste artifact in identity-consistent image generation—where models overly replicate the reference face rather than generating natural variations. It makes three concrete contributions: (1) **MultiID-2M**, a large-scale dataset of ~500k paired multi-ID images with hundreds of reference images per identity plus 1.5M unpaired images; (2) **MultiID-Bench**, a standardized evaluation benchmark measuring both identity fidelity (Sim(GT)) and copy-paste (CP); and (3) **WithAnyone**, a FLUX-based diffusion model with a paired-training paradigm, GT-aligned ID loss, and an ID contrastive loss with extended negatives. Experiments across 12 baselines show WithAnyone achieves the lowest copy-paste score among face-specific models while maintaining competitive identity similarity, and qualitative results demonstrate improved controllability over expression and pose.

## Strengths
- **Formalizes and quantifies the copy-paste artifact.** The paper identifies a previously vague failure mode, defines it concretely via the CP metric (Eq. 2), and shows empirically (Fig. 5) that most existing methods lie on a trade-off curve between Sim(GT) and CP, with WithAnyone deviating substantially from this curve—achieving high Sim(GT) (0.460) and low CP (0.144) simultaneously on the single-person subset.

- **Constructs a large-scale paired multi-ID dataset (MultiID-2M).** The four-stage pipeline yields ~500k group photos with matched reference images (~3k identities, ~400 refs per identity) and 1.5M unpaired images. This paired data is the enabling resource for the contrastive loss and paired tuning (Phase 3) that reduce copy-paste. The dataset is released open-source, which is a significant practical contribution.

- **MultiID-Bench provides a more principled evaluation protocol.** By using Sim(GT) (similarity to ground-truth) rather than Sim(Ref) as the primary metric, the benchmark penalizes trivial copying while rewarding faithful realization of the prompted scene. The CP metric, despite validity concerns, represents a serious attempt to quantify a previously qualitative phenomenon. The benchmark includes 12 baselines across single- and multi-person subsets.

- **Method design is well-motivated and ablated.** The GT-aligned ID loss (using ground-truth landmarks to avoid noisy extraction) demonstrably improves identity preservation across noise levels (Fig. 7). The four-phase training pipeline (reconstruction → caption → paired tuning → quality) is sensible, and ablation studies (Table 3) confirm the contribution of each component.

## Weaknesses

### Major

- **The CP metric's validity as a measure of "copy-paste" is not fully established.** The metric computes angular distance of the generated embedding toward the reference versus the ground truth, normalized by the GT-reference distance. However, the GT is only one sample from the identity's distribution—a model generating a different but equally plausible variation could be arbitrarily closer to either the reference or the GT by chance. The GT itself scores -0.999 on this metric, which implicitly assumes the ideal generation matches the GT exactly, partly contradicting the paper's own framing that natural variation is legitimate. The paper reports "moderate positive correlation" with human judgments but provides no correlation coefficient, significance test, or confidence interval to substantiate this claim (the details are deferred to Appendix H). Given that CP is central to the paper's headline quantitative comparisons (Tables 1, 2), stronger validation is needed.

- **The claim of "breaking the trade-off" between fidelity and copy-paste is overstated.** The paper uses the phrase "breaking the long-observed trade-off" in both the introduction and conclusion. While Figure 5 does show WithAnyone deviating from the regression curve of prior methods—which is a genuine achievement—the ablation study (Table 3) reveals that the trade-off persists within the method's own components: removing extended negatives drops CP to 0.074 but also drops Sim(GT) to 0.368. The method achieves a better operating point on the trade-off frontier, not a fundamentally different regime. The framing should be adjusted to accurately reflect what the data supports: substantial improvement over prior methods on the combined objective, rather than elimination of the trade-off.

### Minor

- **User study is underreported.** Only 10 participants were recruited, with no inter-rater agreement measure (e.g., Fleiss' kappa), no confidence intervals on the rankings, and no reported correlation statistic between CP scores and human judgments. The correlation claim ("moderate positive correlation") is stated without a coefficient or p-value.

- **GPT-4o baseline comparisons should be more clearly separated.** While the paper acknowledges GPT's prior knowledge of identities in the Table 2 footnote, the reader must manually disentangle which comparisons are fair. The claim "WithAnyone has best performance among face customization models" is stated correctly, but the presentation in Tables 1–2 intermixes general models and face-specific models without a visual separator, which may mislead casual readers.

- **The choice of 50% paired data in Phase 3 is not ablated.** The paper uses 50% paired samples without justifying why this ratio was chosen. A sweep (e.g., 0%, 25%, 50%, 75%) would clarify the sensitivity of copy-paste reduction to this hyperparameter, which is a key design choice.

- **The threshold of 0.4 for identity matching (cosine similarity) is stated without justification.** This threshold determines which identities are considered a match and thus affects the dataset quality, but no sensitivity analysis is provided.

### Trivial

- **The negative pool size of 4096 is stated without analysis of sensitivity.** It would be informative to see how CP and Sim(GT) vary with smaller pools (e.g., 64, 256, 1024), though this does not undermine the core results.

- **The paper uses bold/colored indicators (■, ■, ■) inconsistently in Table 1b (OmniContext):** PuLID and Ours rows both show bold values in columns where PuLID has strictly lower scores than Ours on PF (6.62 vs 7.43) but the formatting is ambiguous.

## Nice-to-Haves
- Extend evaluation to non-celebrity identities (e.g., from FFHQ) for zero-shot generalization testing.
- Provide a scatter plot of individual data points for Sim(GT) vs. CP (not just regression curves) to show variance.
- Report Spearman correlation between CP scores and human rankings with a significance test to strengthen metric credibility.
- Show side-by-side ablations with and without Phase 3 (paired tuning) for the same identity and prompt to visually illustrate copy-paste reduction.

## Removed Points
- **"No statistics on dataset diversity (age, ethnicity, pose variation)"** — removed because the paper references Appendix C for dataset statistics; the parser strips appendices, but they exist in the original submission.
- **"Missing appendix details for user study and dataset"** — same reason; appendix content exists in the original paper.
- **"The GT itself scores -0.999, implying ideal generation should match the GT exactly"** — this is a property of the metric formula, not a flaw; the metric is designed to compare bias toward reference vs. GT, and a GT-self comparison naturally yields -1. This is mathematically expected behavior.

## Novel Insights
The reviews surface an interesting tension: the paper's core contribution is identifying and quantifying a real phenomenon (copy-paste artifacts), but the very metric it proposes to measure this phenomenon inherits a subtle but important structural issue—the assumption that the GT image is the unique correct target, when the paper's own motivation acknowledges that natural variation in identity features is legitimate and desirable. This tension between quantifying faithfulness to the GT while encouraging deviation from the reference is a genuinely hard measurement problem that the paper partially addresses (via user study correlation) but does not fully resolve. The broader implication is that evaluation of identity-consistent generation may need distribution-aware metrics rather than pointwise comparisons against a single GT image.

## Suggestions
1. **Tone down the "breaking the trade-off" language.** Replace with precise claims about achieving a substantially improved operating point on the trade-off frontier, supported by Figure 5.
2. **Validate the CP metric more rigorously.** Report the Spearman correlation (with p-value) between CP scores and human rankings across the 230 user-study cases. If the correlation is modest, be transparent about the metric's limitations.
3. **Add a visual separator in Tables 1–2** between general-purpose models and face-customization models to avoid misleading comparisons, and include a clear statement that GPT-4o comparisons on multi-person subsets are invalid due to prior knowledge.
4. **Ablate the 50% paired-data ratio** in Phase 3 with at least three operating points to justify the choice.
5. **Provide confidence intervals or error bars** for key quantitative results (Sim(GT), CP) where multiple runs are feasible.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| **VIST3A** (kI27Niy4xY.md) | 8.0 (Oral) | Far stronger originality; clean model-stitching contribution. Under review is not at this level. |
| **OmniPortrait** (DVmR3Ij0ap.md) | 5.5 (Poster) | Similar portrait generation area. WithAnyone uses a more modern DiT backbone (FLUX), larger dataset, and more baselines. Comparable or slightly stronger. |
| **SIGMA-Gen** (x2DWTywZ1i.md) | 5.0 (Poster) | Multi-ID generation. SIGMA-Gen uses synthetic data (a weakness noted by reviewers) while WithAnyone uses real data. WithAnyone has larger-scale dataset and more comprehensive evaluation. Comparable. |
| **CoDi** (8pDcEIvmcP.md) | 4.67 (Poster) | Training-free method on outdated SDXL. WithAnyone's contributions (dataset + benchmark + method) are more comprehensive. Stronger paper. |
| **FaceID-6M** (yTq81RcKaw.md) | 3.5 (Reject) | Dataset-only paper; limited technical novelty. WithAnyone has method + benchmark in addition to dataset, making it substantially stronger. |
| **CrossFaceID** (XJ3T70nELl.md) | 2.67 (Reject) | Small dataset (40k), data authorization concerns. WithAnyone is far more comprehensive. |
| **Scaling Laws for DiT** (T985gm4sDA.md) | 5.5 (Poster) | Different area. Hard to compare directly, but the review quality bar for this score band is well-calibrated. |

The paper makes three substantive contributions (dataset, benchmark, method) that together advance the state of the art in multi-identity generation. The weaknesses—overclaimed framing, metric validation gaps, and missing ablations—are real but addressable and do not undermine the core contributions. Compared to accepted anchor papers at the 5.0–5.5 level (SIGMA-Gen, OmniPortrait), this paper holds its ground or exceeds them in terms of contribution breadth and practical impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>