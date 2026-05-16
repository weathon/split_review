Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final consolidated review.

---

## Summary

This paper conducts a systematic empirical study of the feature learning strength γ (the output scaling parameter in μP) across architectures (MLPs, CNNs, ResNets, Vision Transformers) in the online training setting. It maps the γ–η phase portrait, identifies scaling laws for the learning rate (η* ∝ γ² for γ≪1, η* ∝ γ^{2/L} for γ≫1), catalogs dynamical phenomena (catapults, silent alignment, stepwise loss drops, progressive sharpening), and shows that large-γ networks can match or exceed γ=1 performance given sufficient training and proper η scaling. A minimal linear-network model analytically reproduces all observed scaling exponents.

## Strengths

1. **Systematic identification of scaling regimes in the γ–η plane across diverse architectures.** The paper sweeps γ and η over many orders of magnitude for MLPs, CNNs, ResNets, and ViTs, revealing a consistent phase portrait with the distinctive "triangle of optimizability" at large γ (Figures 1c,d). The predicted scalings η* ∝ γ² (lazy) and η* ∝ γ^{2/L} (ultra-rich) are observed as the boundaries of the convergent region, and this depth-dependent large-γ scaling is a novel finding not previously highlighted.

2. **Theoretical derivation of all observed scalings from a minimal linear model.** Section 5 derives η_min, η_crit, and η_max for both MSE and cross-entropy loss from a single-parameter deep linear network (Table 1). The model reproduces the full phase portrait and explains the origin of the depth-dependent η_max ∝ γ^{2/L} scaling via the Hessian at the minimizer (Equation 3). This connects the empirical observations to first principles.

3. **Discovery and catalog of ultra-rich (γ≫1) regime dynamics.** The paper documents silent alignment, stepwise loss drops, and progressive sharpening at large γ (Figures 2a, 4b, Section 3.3) and shows these phenomena — previously studied only in simpler settings — occur in realistic deep networks. The finding that early-time dynamics become γ-invariant under τ = ηt/γ rescaling provides testable predictions for theories of feature learning.

4. **Demonstration that large γ yields competitive performance in the online setting.** Figure 2b shows that with proper learning-rate scaling and sufficient training time, larger-γ networks match or exceed γ=1 generalization. This contrasts with offline results (Petrini et al. 2022) and isolates the effect of γ on optimization from dataset-repetition confounds.

5. **Consistency across architectures and datasets.** The main findings replicate across MLPs, CNNs, ResNet-18, and Vision Transformers on MNIST-1M, CIFAR-5M, and TinyImageNet. The use of large synthetic/curated datasets to approximate the online setting is methodologically sound.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Scaling-law claims rely on qualitative visual evidence rather than quantitative extraction.** The paper's central empirical claim — the scaling exponents η* ∝ γ² and η* ∝ γ^{2/L} — is supported by dashed lines overlaid on accuracy heatmaps (Figures 1c,d) and by the theoretical derivation (Section 5). However, the empirical boundaries are not quantitatively extracted: there is no thresholding of accuracy to define the convergent region, no power-law fitting to the boundaries, and no reported exponents with confidence intervals. While the visual match is compelling and the theory provides the exponents, this gap between the qualitative empirical demonstration and the precise quantitative claims reduces the paper's rigor. The authors could substantially strengthen the paper by extracting boundaries via accuracy thresholding and fitting power laws.

    *Versus the overly strong version in the harsh review*: I keep this as Minor rather than Major because (i) the theoretical derivation independently provides the exponents, (ii) the visual match in the phase portraits is clear, and (iii) the paper is primarily an empirical catalog, not a precision measurement paper. It is a real limitation but not one that invalidates the core contribution.

2. **"Optimal" vs. "maximal" learning rate terminology is ambiguous.** The abstract and introduction use η* ("optimal learning rate"), but the technical discussion in Sections 3.1 and 5 focuses on η_max (the maximum convergent learning rate derived from Hessian eigenvalues). The phase portraits show accuracy, so the "optimal" η would be the best-performing one, which may not coincide with η_max. The paper should clarify whether the scaling laws apply to the maximal convergent η, the best-performing η, or both, and whether these are empirically the same.

3. **The time-rescaling claim (τ = ηt/γ) is asserted but not demonstrated in a figure.** Line 248 states that "upon rescaling time as τ = ηt/γ, the early time dynamics coincide," and line 398 derives this from the linear model. However, no multi-γ collapse plot is shown in the main paper. A figure overlaying loss or alignment curves for several γ values before and after rescaling would directly support this claim and is straightforward to produce.

4. **Function-comparison evidence is thin.** Section 3.4 claims that large-γ networks learn "the same function" and that representations agree under time rescaling. The evidence consists of a single scatter plot (Figure 5a) comparing network outputs and an end-of-training CKA plot (Figure 5b). The scatter plot's caption mentions "pairs of networks" but the text describes comparing "two distinct networks A and B" — it is unclear how many pairs, seeds, or γ values are compared. The CKA figure shows only end-of-training values, yet the text mentions that "after adopting a suitable time rescaling, the alignment scores for a variety of networks across γ agree" — the time-rescaled version is not shown. This claim would be much stronger with systematic pairwise comparisons across multiple seeds and γ values, and with a time-rescaled collapse plot for CKA.

5. **Inconsistency between described η sweep range and actual plotted range.** Line 151 states sweeping η from 10¹² down to 10⁻¹², which the reviewer notes is implausibly large. In context, the sweep starts at the high end and stops upon finding the first convergent η, so the actual η values used in training are far smaller — but this procedural detail is easy to misread. The paper should clarify the actual η ranges that were used in the reported experiments.

### Trivial

None.

## Nice-to-Haves

- **Add a summary table** (beyond Table 1) comparing predicted and observed scaling exponents for η_min, η_crit, η_max for both losses across all architectures. This would clarify the connection between theory and experiment.
- **Quantify the scaling exponents** by extracting the convergent-region boundaries from the phase plots and fitting power laws with error bars. See Weakness #1 above.
- **Add a multi-γ collapse plot** for the τ = ηt/γ time rescaling to visually demonstrate the claimed invariance.
- **Brief discussion of batch-size scaling** and how it might interact with the γ–η phase portrait.
- **Practical guidance paragraph** on how practitioners should tune γ and η (e.g., "set γ large, then tune η via η ∝ γ^{2/L}").

## Removed Points

- **ViT lazy-limit claim unsupported in main text**: This criticism questions evidence that lives in the appendix, which was stripped by the parser. The rule explicitly requires removing weaknesses about missing appendix content. The original submission contains this evidence.

- **Figure 3a caption truncated**: Parser artifact — the original submission has the complete caption. Removed per rule about formatting/parser artifacts.

- **"implausible" η range (10¹² to 10⁻¹²)**: The reviewer misread the methodology. The sweep proceeds *downward* until convergence is found, so the extreme η values are starting points, not training values for all configurations. The text describes the procedure clearly.

- **Comments about missing related works**: Removed per rule (cannot verify existence of missing references without external sources).

- **Reproducibility nitpicks / missing implementation details**: Removed per rule (trivial implementation details impractical for a submission).

- **Generic or superficial strengths from Strength Finder**: None were generic enough to drop; all cited specific content.

- **Strength about "large-γ networks converge to similar functions" retained despite Weakness #4**: The strength notes the claim, while the weakness notes the evidence is thin. These are not contradictory — the paper does indeed make this claim and present some evidence; the weakness merely argues the evidence is insufficient. Keeping both is appropriate.

## Novel Insights

Beyond the paper's own contributions, the most insightful observation from reviewing this work is how the combination of broad empirical sweeps and a minimal theoretical model generates a complete picture that neither approach alone would provide. The empirical phase portraits show the phenomena exist in realistic networks, while the linear model shows the scaling exponents arise from elementary Hessian and gradient-flow calculations, establishing that depth-dependent scaling (γ^{2/L}) is a generic feature of learning in deep networks — not a quirk of nonlinear activations or wide architectures. The tension with offline results (Petrini et al.) further highlights that the γ dependence of generalization is fundamentally tied to the data regime, a point with practical implications for hyperparameter tuning in large-scale models where data repetition is minimal.

## Suggestions

1. **Clarify the η*/η_max distinction.** Either use η_max throughout when discussing the boundary scalings derived from Hessian analysis, or explicitly state whether η* (optimal for accuracy) empirically coincides with η_max and provide evidence.

2. **Add a quantitative boundary extraction.** Threshold the accuracy maps in Figures 1c,d (e.g., where accuracy drops below 90% of maximum) and fit power laws to the resulting boundaries, reporting exponents with standard errors. This would convert the scaling claims from visual to quantitative.

3. **Provide the τ = ηt/γ collapse plot.** Overlay loss curves for γ ∈ {10, 100, 1000} before and after rescaling on the same axes. This single figure would substantively support a claim made in multiple places.

4. **Strengthen the function comparison analysis.** Show pairwise function correlations or CKA values across multiple seeds and γ values (e.g., γ ∈ {0.01, 1, 10, 100}) with error bars, demonstrating that within-regime agreement exceeds cross-regime agreement statistically.

## Score and Decision

This paper makes a real contribution: it provides the first systematic mapping of the γ–η phase diagram across architectures in the online setting, identifies novel depth-dependent scaling laws, catalogs rich dynamical phenomena, and explains them with a minimal model. The weaknesses are real but addressable: the scaling claims would benefit from quantitative boundary extraction, the time-rescaling claim needs a collapse plot, and the function comparison analysis is thin. None of these undermine the core contribution.

The paper is clearly written, the experiments are thorough (spanning MLPs, CNNs, ResNets, ViTs on multiple large datasets), the theoretical model is elegant, and the findings have practical implications for hyperparameter tuning in large-scale models.

Score: 7.0 — A solid paper with clear contributions and addressable weaknesses.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>