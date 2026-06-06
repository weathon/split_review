## Summary
MolMiner is an autoregressive, fragment-based molecular generative model that conditions on up to twelve physicochemical properties, incorporates dynamic 3D geometry via forcefield relaxation during inference, uses symmetry-aware fragment attachment via Morgan fingerprint canonicalization, and employs order-agnostic rollouts. The paper also proposes Wasserstein-based distributional evaluation and calibration plots as improved benchmarking tools for both unconditional and conditional generation.

---

## Strengths

- **Calibration-based evaluation methodology**: The use of Wasserstein distances (Table 1) and calibration plots (Figure 2) with mean ± 1σ bands for continuous properties and confusion matrices for discrete ones provides a substantially richer evaluation signal than standard validity/diversity metrics. This is a genuine methodological contribution that could benefit the broader community.

- **Symmetry-aware attachment standardization**: Section 3.2 presents a concrete, systematic procedure for resolving fragment attachment ambiguities using Morgan fingerprints and cyclic permutation matching. This is a specific, well-motivated engineering contribution that prior fragment-based models (e.g., MoLeR) did not clearly address.

- **Practical partial-conditioning interface**: The GMM-based mechanism (Section 3.6) for completing unspecified properties from the empirical training distribution is a useful user-facing feature, enabling chemists to specify only known constraints rather than requiring full 12-dimensional input.

- **Order-agnostic rollouts with demonstrated regularization benefit**: Section 4.1 confirms that rollout resampling reduces overfitting. This is stated as empirically confirmed through ablation (though results are in Appendix A.3).

- **Single model supporting the widest reported simultaneous conditioning**: Conditioning on twelve properties in one model—including both continuous (logP, SAS, TPSA, MR, etc.) and discrete (ring count, chiral centers, rotatable bonds) targets—represents a broader conditioning scope than previous reported systems.

---

## Weaknesses

### Fatal
None. No individual flaw conclusively invalidates the method.

### Major

- **The "simultaneous" multi-property conditioning claim is not experimentally validated as simultaneous.** Section 4.3 describes the evaluation protocol explicitly: "For each of the twelve physicochemical and structural properties, we uniformly sample target values across the range μ ± 2σ... The remaining eleven properties are sampled conditionally from the GMM prior." This means each calibration plot in Figure 2 tests *one* property's range while the other eleven are drawn from the prior—not jointly specified by the user. The paper nonetheless claims in Section 4.3 that the protocol "evaluates...its capacity for simultaneous, multi-property control," which is a non sequitur: marginal calibration plots do not demonstrate joint satisfaction of multiple simultaneously specified constraints. A model could achieve good per-property marginal calibration while failing when multiple properties are jointly constrained, since cross-property trade-offs and conflicts are never evaluated. The paper's abstract and conclusion claim "simultaneous conditioning across as many as twelve molecular properties" and "a significant advance in controllable molecular design," but the evidence base is marginal (one-at-a-time) rather than simultaneous. This is the core claimed contribution, and it is not demonstrated.

- **Absence of any baseline for the main contribution.** The conditional generation evaluation (Figure 2) has no comparison to any other method. No prior model is shown to be worse on calibration, no ablated variant without key modules is shown. The unconditional benchmark (Table 1) compares only to HierVAE (one baseline), and conditional generation—the paper's primary contribution—has no competitive reference point whatsoever. Without a baseline, it is impossible to judge whether MolMiner's conditional accuracy is strong, adequate, or marginal in absolute terms.

- **Train/inference geometry mismatch undermines the 3D-awareness learning claim.** Section 3.3 states explicitly: "During training, rollouts are precomputed... This allows efficient learning without the need for force field optimization during training epochs. In contrast, during generation, the molecule is built incrementally, with geometry relaxed after each attachment step via a classical force field." The geometric attention bias (Eq. 2) and the "distances to attachment point" input are derived from static pre-computed training geometries, while at inference the model receives progressively force-field-relaxed intermediate geometries it has never encountered during training. The paper frames this dynamic inference geometry as a core learned capability ("ensures that predictions are conditioned on realistic intermediate structures"), but the training signal comes from a different geometric distribution. This inconsistency is not acknowledged in the limitations section and no ablation compares inference with vs. without per-step forcefield relaxation to test whether the 3D component contributes positively.

### Minor

- **Unconditional performance gap mischaracterized.** Table 1 shows MolMinerD vs. HierVAE: molecular weight (47 vs. 15, ~3×), TPSA (7.6 vs. 2.3, ~3.3×), MR (11.9 vs. 3.8, ~3.1×). The paper characterizes these as "modest differences across most properties." Factors of 3× on three structurally important properties (molecular size and polarity proxies) are not modest. The early-termination hypothesis stated in Section 5 is a plausible explanation but is presented without supporting ablation—no size distribution analysis, no termination probability analysis by step, no remediation attempt.

- **QED control failure acknowledged but not bounded or explained.** Section 4.3 states "QED is a notable exception, where control accuracy degrades," but no quantification is given of how badly QED is controlled, no mechanism is proposed, and no comparison indicates whether this is a negligible or disqualifying failure for typical use cases.

### Trivial

- Ablation evidence for geometry-aware attention, rollout resampling, and conditioning richness—three central design choices—is deferred entirely to Appendix A.3 with only a three-sentence summary in Section 4.1. This reduces in-paper verifiability of the design rationale.

---

## Nice-to-Haves

- Construct a multi-property joint evaluation: specify 3, 6, and 12 properties simultaneously, generate molecules, and measure what fraction of prompted properties are jointly satisfied within ±0.5σ. This directly tests the "simultaneous" claim and would substantially strengthen or honestly qualify the main contribution.
- Provide an ablation that compares inference with vs. without per-step forcefield relaxation on any metric. This would directly test whether the dynamic geometry component contributes meaningfully over static training geometry.
- Analyze generated molecule size distributions and per-step termination probabilities to verify or refute the early-termination hypothesis, and attempt a straightforward fix (e.g., down-weighting termination during training).
- Even a simple nearest-neighbor retrieval from the training set given property targets would provide a reference point for conditional calibration quality.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Harsh Critic: "Simultaneous claim is architecturally unverified as a fatal flaw."** Retained as Major (not Fatal), since the method does use a 12D conditioning vector at all times and the architecture is not fundamentally broken—the gap is evidential, not structural.

- **Harsh Critic: Abstract novelty claim is unverifiable without external comparison.** Removed—we cannot verify related-work coverage without external sources, and the paper appropriately hedges with "to our knowledge."

- **Harsh Critic: Jensen bound gap discussion.** The lower bound via Jensen is standard in order-agnostic generation (following Hoogeboom et al., 2022a cited in the paper). The variance of the gap is a theoretical curiosity but not a substantive flaw for an empirical systems paper. Removed.

- **Harsh Critic: MolLeR exclusion is "concerning."** The paper explicitly states MolLeR completed only two mini-epochs in seven days and shows poor results consistent with known VAE prior/posterior mismatch issues; it includes results in Appendix A.9. Exclusion from the main table with documented reasoning is reasonable. Removed.

- **Harsh Critic: Evaluation on in-distribution targets only.** Testing within ±2σ of training distribution is standard practice and not a flaw in a primary evaluation; OOD extrapolation is a useful future direction. Moved to Nice-to-Haves.

- **Strength Finder: "First model to unify dynamic geometry, symmetry handling, order-agnostic generation, and high-dimensional conditioning."** Generic novelty framing—kept as a characterization only, not an independent strength.

- **Strength Finder: Potential to accelerate drug discovery and sustainable energy.** Generic impact statement with no specific evidence in the paper. Removed.

---

## Novel Insights

The train/inference geometry distribution mismatch (precomputed static geometries during training vs. progressively force-field-relaxed geometries at inference) is an underappreciated structural inconsistency in the 3D-aware molecular generation literature broadly, not just in MolMiner. If the model learns to use 3D biases primarily as a noisy signal it partially ignores—because training geometries don't correspond to realistic partial-molecule geometries—this could explain why purely geometric attention biases have limited benefit in practice. An ablation isolating this would be informative beyond this paper.

---

## Suggestions

1. Run a joint evaluation where 3, 6, and 12 user-specified properties are simultaneously set, and report the fraction of jointly satisfied constraints. This is the single most important experiment for validating the paper's main claim.
2. Add at least one conditional generation baseline—even a simple GMM retrieval or a model conditioned on fewer properties—to give the calibration plots a reference point.
3. Add an ablation: inference with vs. without per-step forcefield relaxation, measured on any quality metric. This tests whether 3D-awareness is doing useful work despite the training mismatch.
4. Analyze generated molecule size distributions vs. training data and per-step termination rates to empirically validate or refute the early-termination hypothesis.
5. Rephrase "modest differences" in the unconditional benchmark to accurately reflect 3× gaps on TPSA, MR, and molecular weight.

---

## Score and Decision

**Originality:** The components (fragment generation, order-agnostic rollouts, 3D attention bias, property conditioning) each have clear precedents; the contribution is their integration plus the symmetry protocol and evaluation methodology. Moderate originality.

**Importance of research question:** Multi-property controllable molecular generation is genuinely important for HTS pipelines. High importance.

**Claims well supported:** The primary claim—"simultaneous" multi-property control—is not demonstrated as simultaneous. The calibration plots show per-property marginal control only. Unconditional performance is substantially below the sole baseline. Claims partially but not adequately supported.

**Soundness of experiments:** Single baseline (unconditional only), no conditional baselines, train/inference geometry mismatch unaddressed, no joint conditioning evaluation. Experiment design is insufficient for the claims.

**Clarity of writing:** The paper is clearly written, contributions are enumerated, methodology sections are well-structured.

**Value to the research community:** The evaluation methodology (Wasserstein distances, calibration plots) and symmetry-handling protocol have standalone value. The system as claimed—if the joint conditioning gap were validated—would have significant practical value, but that remains undemonstrated.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>