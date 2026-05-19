## Summary
This paper addresses the overlooked problem of SVG code readability in automatic vector graphics generation. It proposes three readability desiderata (Good Structure, Appropriate Element Use, Redundant Element Removal), three corresponding evaluation metrics (SPI, ESS, RQ), and three differentiable proxy losses (ℒ<sub>SC</sub>, ℒ<sub>EA</sub>, ℒ<sub>RR</sub>) designed to optimize readability during training. The method is evaluated on font reconstruction (SVG-Fonts dataset) and via a GPT-3.5 understandability study on the SHAPES dataset.

## Strengths
- **First systematic treatment of SVG readability**. Section 2.1 defines three concrete desiderata (Good Structure, Appropriate Element Use, Redundant Element Removal) for SVG code readability. Prior work like Im2Vec and DeepVecFont focused entirely on visual accuracy, so this provides a missing foundation for an underexplored problem.

- **Three dedicated differentiable proxy losses with ablation evidence**. Section 3.2 introduces ℒ<sub>SC</sub>, ℒ<sub>EA</sub>, and ℒ<sub>RR</sub> as differentiable surrogates for the three readability aspects. The ablation study (Table 3) shows that adding each loss progressively improves its corresponding metric (SPI, ESS, RQ) while leaving other metrics relatively stable, confirming each loss drives its intended effect. This provides clear evidence that the losses are functional.

- **Honest treatment of the accuracy–readability trade-off in the body**. Section 4.3 explicitly titles a paragraph "Compromise in Accuracy" and acknowledges the accuracy drop (SSIM, L1, s-IoU), framing the results as a "balanced trade-off" rather than an unqualified improvement. This transparency in the experimental discussion is a mark of scientific integrity.

- **Quantitative readability metrics that operationalize the desiderata**. SPI, ESS, and RQ (Section 2.2) give concrete, computable measures for aspects of readability that previously had no standardized quantification. Table 2 provides a cross-method numerical comparison of readability that prior work did not offer.

## Weaknesses
### Fatal

None. The core contribution (identifying readability as a problem and proposing metrics/losses) is genuine, and the paper's approach is coherent.

### Major

- **Abstract claim contradicts the paper's own results.** The abstract states that SVG generators show "significant improvements in code readability **without compromising visual accuracy**" (line 4). Yet Section 4.3 explicitly acknowledges a "Compromise in Accuracy" where SSIM drops to 0.746 vs. 0.878 (Im2vec) and 0.895 (Multi-Implicits), and describes the results as a "balanced trade-off." The abstract's categorical denial of any compromise is a structural misrepresentation of the paper's empirical contribution. If the paper's honest finding is a *trade-off*, the abstract must say so.

- **No external validation that the readability metrics correspond to anything practically meaningful.** The metrics (SPI, ESS, RQ) are defined by the authors, and the proxy losses are explicitly designed as differentiable versions of those same metrics. The ablation study therefore shows that optimizing for a metric improves that metric — which is expected but nearly circular. No human study, established code-readability rubric, or downstream task demonstrates that improvements in SPI/ESS/RQ actually make SVG code easier to understand, edit, or debug. Without external grounding, the reader cannot judge whether the metrics capture genuine readability or merely measurable correlates that may not matter in practice.

- **The GPT-3.5 understandability study is critically under-described, making it impossible to evaluate.** The paper does not specify: (a) whether the font-trained VAE was fine-tuned on SHAPES, retrained from scratch, or applied zero-shot; (b) the exact prompts given to GPT-3.5; (c) the number of test questions; (d) any measure of variance or confidence. The paper states the model "predefin[es] the number of simple shapes in accordance with the characteristics of the test images" but does not describe this mechanism. These omissions prevent the reader from reproducing or even properly interpreting the results. The claim that GPT-3.5 "demonstrates exceptional performance" is unsubstantiated without these details.

### Minor

- **Several implementation details needed for reproducibility are missing.** The VAE encoder architecture, number of latent dimensions, decoder output structure (how many primitives per SVG, how parameters are generated), and whether the number of elements is fixed or dynamic are not specified. The differentiable rasterizer (Diffvg vs. LIVE) is not identified. These are not hyperparameter nitpicks — they are architectural choices central to understanding and reproducing the method.

- **The redundancy reduction loss (ℒ<sub>RR</sub>) uses a hard threshold T without guidance on how to set it.** The threshold T determines which elements are penalized (line 200), yet the paper offers no analysis of how T affects performance or how practitioners should choose it. The loss form max(0, T−||∂R||) also penalizes small-gradient elements, which could suppress genuinely small but necessary elements — a concern the paper acknowledges (line 207) but does not analyze.

- **ESS complexity weights are assigned without justification.** The complexity scores (1 for `<rect>`, `<circle>`, `<line>`; 3 for `<path>`) are presented as an illustrative example (line 83: "we could assign"), but the paper uses these specific values without sensitivity analysis or justification for the particular 1:3 ratio.

- **No variance or confidence intervals reported.** Quantitative results (Tables 1–4) are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given the modest dataset sizes (1425 test fonts), statistical uncertainty could be meaningful.

- **RQ computation (ΔR) is underspecified.** The paper defines RQ (line 103) based on ΔR(eᵢ) — "the change in rendering when an element eᵢ is omitted" — but does not specify what distance function is used (per-pixel L2? SSIM? something else?), making the metric imprecise.

### Trivial

None.

## Suggestions
1. **Fix the abstract.** Replace "without compromising visual accuracy" with language that honestly reflects the accuracy–readability trade-off demonstrated in the experiments (e.g., "while accepting a modest reduction in visual accuracy").
2. **Validate the metrics with human judges.** Even a small user study (10–20 participants ranking SVG snippets) would ground SPI, ESS, and RQ as meaningful proxies for readability rather than self-referential constructs.
3. **Fully specify the GPT-3.5 experiment.** Clarify how the model was applied to SHAPES (fine-tuned? zero-shot?), provide the prompts used, report the number of questions, and include qualitative examples of successes and failures.
4. **Report variance.** Add standard deviations or confidence intervals to all quantitative tables.
5. **Add a limitations section** discussing when the approach might fail (e.g., images requiring complex paths, photographs, organic shapes) and acknowledging the heuristic nature of the proxy losses.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
