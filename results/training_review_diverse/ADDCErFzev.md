Here is my synthesized final review:

---

## Summary

This paper uses controlled dropout variation across 10 AlexNet models (p=0 to 0.9) to operationalize a continuum between sparse (high-dimensional) and distributed (low-dimensional) population codes. The authors report that dropout systematically reduces representational dimensionality, that lesion robustness peaks at p=0.7 (not at extreme dropout), and that this same p=0.7 model shows the highest emergent representational similarity with human occipitotemporal cortex (OTC) measured via 7T fMRI, alongside the closest match in eigenspectral decay rate. The core thesis is that these converging findings reveal an optimal balance between coding efficiency and robustness that the human visual system may also occupy.

## Strengths

- **Controlled parametric manipulation of a single inductive bias**: All 10 models share the same architecture, training data, and hyperparameters except for dropout rate (Section 2.1). This is a clean design that isolates the effect of dropout on representational geometry and avoids the confounds of comparing across different architectures or training regimes.

- **Non-trivial optimal robustness point**: Lesion robustness increases with dropout up to p=0.7 then declines at higher rates (Figure 2C-D). This U-shaped relationship is not a trivial consequence of dropout training (which would predict monotonic gains) and genuinely suggests that intermediate dropout levels best balance competing pressures. The paper is transparent that lesioning mirrors the training perturbation (Section 2.3).

- **Triple convergence at p=0.7**: Three independent measurements — lesion robustness, RSA alignment with human OTC across 8 NSD subjects, and eigenspectral decay rate — all peak or most closely match the brain at the same dropout level. This specific convergence is the paper's most striking finding and provides meaningful circumstantial evidence for a shared coding principle.

- **High-quality fMRI data and rigorous ROI definition**: The paper leverages the Natural Scenes Dataset (7T, 8 subjects, 515 shared images, 3 repetitions each) with GLMsingle denoising and a well-validated OTC mask, providing a strong empirical target for model-brain comparison.

## Weaknesses

### Fatal
None.

### Major

- **The brain-alignment peak (Figure 3C) lacks statistical validation**: The claim that maximal representational similarity occurs at p=0.7 is central to the paper's argument. However, no confidence intervals, pairwise significance tests, or mixed-effects models accounting for subject variability are reported. Visual inspection of Figure 3C suggests that p=0.5 and p=0.6 may be comparable to p=0.7 for several subjects, and the between-subject spread is large enough to be consistent with a flat or noisy function. Without statistical evidence, this finding remains suggestive rather than conclusive. This weakness is compounded because the paper uses the convergence across findings (lesion + RSA + spectra) as its main rhetorical device — if one leg of the tripod is unstably supported, the whole argument weakens.

- **The causal interpretation is confounded by dropout's multiple effects**: The paper interprets dropout-induced dimensionality reduction as evidence for an efficiency–robustness tradeoff. However, dropout also alters gradient variance during training, forces individual units to be independently useful, and changes the model's effective capacity — any of which could independently produce the observed patterns. The paper acknowledges this in its Limitations (Section 3: "Alternative regularization techniques such as L1 and L2 penalties on the weights could also be explored") but does not run these controls. Without disentangling whether dimensionality *per se* is the causal factor (e.g., via bottleneck layers that directly constrain dimensionality, or via L1/L2 regularization that affects weights differently), the paper's central interpretation remains undersupported.

### Minor

- **Single architecture and single layer**: All experiments use AlexNet and focus on fc6. While the paper acknowledges this limitation, the claim that the results generalize to "biological and machine visual systems" (title and abstract) is premature without at least one additional architecture (e.g., ResNet or a ViT with dropout in its MLP blocks). The brain alignment result could be specific to AlexNet's particular architectural biases.

- **GSN method lacks in-paper validation**: The eigenspectrum analysis (Section 2.5) relies on Generative Modeling of Signal and Noise (GSN), described as "to be fully described and validated in a forthcoming manuscript" (line 138). While the paper provides a mathematical description (Equations 8–10) the method is not validated on synthetic data with known ground-truth spectra, nor are its results compared to the established cvPCA approach (Stringer et al., 2019) on the same dataset. The core spectral match finding (Figure 3E) thus rests on a method whose behavior is not fully characterized in this paper.

- **No multiple training seeds**: All analyses appear to be based on a single training run per dropout level. The dimensionality analysis (Figure 1D) and brain RSA results (Figure 3C) show no error bars reflecting training variability, so it is impossible to assess whether the observed patterns — particularly the subtle differences between neighboring dropout levels — are reproducible or idiosyncratic to the particular weight initialization and training trajectory.

- **Top-5 accuracy only**: The paper reports only top-5 ImageNet accuracy. Top-1 accuracy, precision-recall tradeoffs, or per-class performance would provide a more complete picture of how dropout affects task performance and whether the "preserved performance" claim holds uniformly.

### Trivial
None.

## Nice-to-Haves

- Bootstrapped confidence intervals or a mixed-effects model (dropout level as fixed effect, subject as random intercept) for the RSA results in Figure 3C would substantially strengthen the brain-alignment claim.
- Training models with L1/L2 regularization (or with a bottleneck layer directly controlling dimensionality) and testing whether they reproduce the same lesion-robustness and brain-alignment patterns would help disentangle dimensionality from other dropout effects.
- Validating GSN on synthetic data or reproducing the eigenspectrum analysis with cvPCA would remove reliance on an unpublished method.
- Adding a second architecture (e.g., ResNet-50 with dropout in its fully connected layers) would demonstrate generality.
- Reporting top-1 accuracy in addition to top-5 would provide a more complete picture.

## Removed Points

These points are flagged to be removed — treat them with caution:

- *"The lesion analysis is largely tautological"*: Removed because the paper explicitly acknowledges this relationship (Section 2.3: "In this analysis, we are effectively applying dropout during inference time"). The interesting finding is the non-monotonic peak at p=0.7, which is not predicted by a simple "more training dropout = more inference robustness" account. The reviewer's criticism here largely restates the paper's own framing as if it were a flaw.
- *"The paper dismisses cvPCA without showing GSN yields different results"*: The paper actually discusses cvPCA and explains why GSN is preferable (Section 2.5.1). The absence of an empirical comparison is a valid concern (retained as a Minor weakness above), but the claim that the paper "dismisses" cvPCA is inaccurate.
- *Various formatting and style nitpicks*: Standard removal per instructions.
- *Generic or unsubstantiated "strengths" from the Strength Finder*: Generic claims lacking specific evidence were filtered out.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations (need for statistical testing, confound controls, architectural generality) are standard methodological desiderata rather than novel insights.

## Suggestions

1. **Add statistical evidence for the RSA peak**: This is the most actionable and important fix. Report bootstrapped confidence intervals on the RSA correlations (across subjects, or across image subsets) and a simple mixed-effects model with dropout level as a fixed effect and subject as a random intercept to determine whether p=0.7 is significantly different from its neighbors.

2. **Run at least one control regularization** (e.g., L1 weight decay or a bottleneck layer) to test whether dimensionality, rather than other dropout effects, drives the lesion-robustness and brain-alignment patterns. Even a partial replication would substantially strengthen the causal interpretation.

3. **Validate or supplement GSN**: Either validate the GSN method on simulated data with known ground-truth eigenspectra, or report the eigenspectrum analysis using cvPCA and show the results converge.

4. **Train from multiple seeds** (at least 3) for each dropout level to establish that the observed patterns are reproducible and to enable error bars on all model-level measurements.

## Score and Decision

The paper presents a clever experimental design and an intriguing set of converging findings. However, the lack of statistical validation for the brain-alignment peak, the confounded nature of the main manipulation, and the reliance on an unvalidated method for a core analysis mean that several of the paper's central claims are not yet rigorously supported. The paper would benefit from additional controls and statistical analyses before its conclusions can be fully accepted. Nonetheless, the core approach — systematic dropout variation to probe the sparse-distributed coding continuum — is novel and valuable, and the triple convergence at p=0.7 is sufficiently provocative to warrant publication with the expectation that the authors address the major concerns in a revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>