Now I have thoroughly reviewed the paper. Let me compose the final review.

## Summary

This paper applies manifold learning tools—intrinsic dimension (ID) and mean absolute principal curvature (MAPC)—to analyze the internal representations of transformer-based time series forecasting (TSF) models. Studying Autoformer and FEDformer across seven datasets and four forecast horizons, the authors find a two-phase geometric profile (encoding: flat/decreasing ID and MAPC; decoding: increasing), a positive correlation between final-layer MAPC and test MSE (opposite to classification CNNs), and rapid convergence of geometric profiles during training. The work extends prior manifold analysis of classification CNNs to TSF regression models.

## Strengths

- **Novel two-phase geometric profile discovery**: The paper identifies a distinctive encoding/decoding geometric pattern for TSF transformers—ID and MAPC decrease or stay flat during encoding then increase during decoding (Figures 3–4). This contrasts with the "hunchback" profile reported for classification CNNs and is a substantive finding that could inform architecture design if validated more broadly.

- **Systematic experimental design within scope**: The study covers two architectures, seven datasets, four forecast horizons, and 10 random seeds per configuration (Section 3, paragraph "Data collection"), providing robust within-model estimates of ID and MAPC profiles. The coverage of 500K-sample ID estimation and 100K-sample curvature estimation demonstrates thoroughness.

- **Cross-dataset geometric similarity reflecting known data relationships**: The observation that weather and ETT datasets share similar MAPC profiles while electricity and traffic share a different profile is a coherent finding with external grounding (Section 4.1), suggesting the geometric features capture meaningful dataset structure rather than being mere artifacts.

- **Rapid convergence finding**: The observation that untrained models converge to their final geometric profiles within ~5 epochs (Figure 6) is an interesting empirical result with connections to neural tangent kernel literature.

## Weaknesses

### Fatal
None.

### Major

- **MAPC–MSE correlation claim is statistically unsupportable as presented**: The correlation between final-layer MAPC and test MSE (Table 1, Section 4.2) is computed from four data points per dataset (one per forecast horizon), with correlations ranging from 0.46 to 0.97. With N=4, even a correlation of 0.97 barely reaches p<0.05, and values like 0.46 are entirely indistinguishable from noise. The paper averages these to "0.76 and 0.70" but averaging correlations across datasets with 4 points each disguises extreme instability. The strong practical claim that MAPC "allows one to compare models without access to the test set" (abstract, line 24; Section 4.2) is not demonstrated: a post-hoc correlation on the same set of trained models does not establish predictive utility for new model configurations. To make this claim actionable, the authors would need to show MAPC on training data can predict test MSE for unseen model configurations—a fundamentally different and much stronger test.

- **Overstated generalizability of claims about "deep transformer models"**: The title, abstract, and discussion consistently refer to "deep transformer models" and "transformer forecasting manifolds," but only two architecturally similar models are analyzed. Autoformer and FEDformer share the same encoder-decoder-decomposition backbone and differ primarily in their attention mechanism. Finding similar geometric profiles across two models from the same architectural family is nearly tautological. Without analyzing at least one decomposition-free transformer (e.g., PatchTST, iTransformer) or a non-transformer deep TSF model (e.g., N-BEATS, DLinear), the paper cannot distinguish findings specific to the decomposition-based encoder-decoder design from findings generic to transformers, or findings generic to any deep TSF model. This directly undermines the broad framing.

- **Defining transformer components (attention layers) are excluded from analysis**: The paper analyzes only the decomposition block path (the "red trajectory" in Figure 1), skipping all attention modules. The stated justification is that "the Fourier Cross-correlation layer of the FEDformer model outputs almost identical values for all samples in the series, yielding zero curvature estimates" (Section 3). This justifies skipping FEDformer's attention but not Autoformer's auto-correlation attention, which operates differently. Self-attention and cross-attention are precisely what distinguish transformers from other architectures. By analyzing only the decomposition pathway, the paper studies a decomposition-based autoencoder, not "transformers" in any architecturally meaningful sense. The paper should at minimum analyze Autoformer's attention outputs; if these also yield degenerate curvature, that itself would be a meaningful finding.

### Minor

- **"Similar geometric profiles" is not formally quantified**: The paper repeatedly describes ID/MAPC profiles as "similar" across models and datasets, but similarity is assessed only visually. A formal similarity metric (e.g., dynamic time warping, profile correlation) would strengthen the claim. The qualitative descriptions also gloss over real differences: FEDformer's ID shows V-shapes for electricity/traffic but step patterns for weather/ETTm1 (Section 4.1)—calling these "similar" requires more justification than visual inspection.

- **Post-hoc dismissal of the ETT "hunchback" pattern**: The paper acknowledges that ETT datasets show a hunchback ID profile (which would contradict the main finding) and dismisses it as an artifact of "seven features" (Section 4.1). This is post-hoc reasoning that immunizes the claim against disconfirmation. If low-dimensional datasets produce different profiles, that itself is a finding worth discussing rather than dismissing.

- **"Rapid convergence" is not rigorously quantified**: The claim that convergence occurs "within approximately five epochs" (Section 4.3) is based on visual comparison in Figure 6 without a formal convergence threshold or quantitative metric.

- **Classification vs. regression comparison confounds multiple variables**: The contrast with CNN classification models (Ansuini et al., Kaufman et al.) confounds architecture type (CNN vs. transformer), task type (classification vs. regression), and data modality (images vs. time series). The claimed "fundamental difference between classification and regression" cannot be isolated from these confounds.

### Trivial
None.

## Nice-to-Haves

- Additional transformer architectures (e.g., PatchTST, iTransformer) and at least one non-transformer deep TSF baseline (e.g., DLinear) to distinguish transformer-specific from task-specific geometric behavior.
- Formal statistical validation of the MAPC–MSE relationship using more model configurations (varying depth, width, dropout, training data) to generate sufficient independent observations for meaningful correlation analysis.
- Analysis of Autoformer's auto-correlation attention to determine whether the attention mechanism produces degenerate or informative geometric signatures.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Availability/reproducibility of cited models and benchmarks**: Removed per hard rule—cited entities are assumed to exist.
- **Missing appendix or proofs**: Removed—parser strips appendix sections; these exist in the original submission.
- **Formatting/typo nitpicks**: Removed per hard rule—these are parser artifacts.
- **Undisclosed hyperparameters**: Removed as a minor reproducibility nitpick—the paper specifies seeds (10), sample sizes (500K for ID, 100K for CAML), and standard benchmark settings.
- **Demand for user studies or theoretical proofs for what is an empirical analysis paper**: Removed as scope creep—the paper's contribution is empirical, and demanding proofs or user studies would be outside its community norms.
- **Strength finder claims that "this paper addresses an important problem"**: Removed as generic/superficial. The importance of understanding TSF models is assumed, not a specific contribution.
- **Strength finder claim about "opposite-direction correlation compared to classification"**: This is partially retained but recontextualized—the direction difference is noted, but the strength of the finding is diminished by the statistical concerns above.

## Novel Insights

The most genuinely novel finding is the two-phase geometric profile (flat/decreasing during encoding, increasing during decoding) that contrasts with classification CNNs' "hunchback" pattern. If this pattern holds across diverse architectures, it would suggest that regression/forecasting networks learn fundamentally different representational geometries than classification networks—a claim that, while currently confounded by architecture and modality differences, motivates clear follow-up work. The rapid convergence observation (~5 epochs) also merits further study, as it connects to the neural tangent kernel line of inquiry.

## Suggestions

- Narrow the framing to explicitly scope claims to "decomposition-based encoder-decoder TSF architectures" (Autoformer and FEDformer) rather than "deep transformer models." This aligns claims with evidence and still represents a valuable contribution.
- For the MAPC–MSE correlation, either (a) pool data across datasets after appropriate normalization and report a single correlation with adequate N, or (b) train multiple model variants (varying hyperparameters) per dataset to generate enough independent data points for meaningful per-dataset correlations. In either case, remove or heavily qualify the "compare models without access to the test set" claim until predictive (not post-hoc) utility is demonstrated.
- Analyze at least Autoformer's attention outputs. If they too yield degenerate curvature, report this as a finding rather than a footnote.

## Score and Decision

The paper asks a genuinely interesting question—what do TSF transformers learn internally, viewed through manifold geometry? The two-phase profile and cross-dataset similarity findings are real contributions. However, the central correlational claim (MAPC enables model comparison without test data) is statistically unsupportable with 4 data points per dataset, and the broad "deep transformer" framing is not matched by the evidence from two closely related architectures, especially since the defining transformer component (attention) is excluded from analysis. These major weaknesses significantly undermine the paper's core contributions in their current form.

**Originality**: Moderate. Extending manifold analysis from CNNs to TSF transformers is a reasonable step, but the methodology is directly borrowed from prior work (Ansuini et al., Kaufman et al.).

**Importance of question**: High. Understanding TSF model internals is valuable.

**Claims support**: Weak. Overclaimed relative to evidence on two key fronts (MAPC correlation, generalizability to "transformers").

**Experimental soundness**: Moderate within scope, but the scope is too narrow for the claims made.

**Clarity**: Good. Well-structured paper with clear methodology.

**Community value**: Moderate. Findings could inform architecture design if validated more broadly.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>