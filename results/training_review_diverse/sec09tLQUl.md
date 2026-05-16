Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper investigates the link between memorization and poor generalization on minority groups in the presence of spurious correlations. The authors show that minority-group examples require fewer neurons to flip their predictions (indicating memorization) and that dropping those memorization-critical neurons improves worst-group accuracy. They then introduce FairDropout, which scales example-tied dropout to larger architectures (ResNet-50, BERT) by allocating fixed "memorizing" neurons to each example during training and dropping them at inference. The method is evaluated on five diverse datasets (Waterbirds, CelebA, MetaShift, MultiNLI, MIMIC-CXR) and achieves consistent worst-group accuracy improvements over ERM without requiring group annotations.

## Strengths

1. **Novel application of example-tied dropout to spurious correlation in large models.** The paper is the first to scale the example-tied dropout technique (previously limited to ResNet-9 / MNIST / CIFAR-10 in the label-noise setting of Maini et al. 2023) to ResNet-50 and BERT for the spurious correlation problem. This is clearly stated in Sections 1 and 3.3, which describe how FairDropout extends beyond the original by supporting intermediate-layer and projection-layer placement.

2. **Consistent empirical improvements across diverse modalities.** FairDropout outperforms ERM on all five benchmark datasets and achieves competitive or superior results against methods that do not require group annotations. Gains are substantial on several datasets: MultiNLI (70.3 vs 63.7 ERM), MIMIC-CXR (70.6 vs 59.8 ERM), and CelebA (75.6 vs 64.5 ERM), averaged over 5 runs (Table 1).

3. **Analysis linking memorization to minority-group overfitting.** The paper provides quantitative evidence (Figures 2–3) that minority-group examples require fewer neurons to flip predictions and that dropping those memorization-critical neurons improves worst-group accuracy in ~75% of cases. This goes beyond observing a generalization gap to probing its mechanistic basis.

4. **No group annotations required during training or validation.** The method operates in the most practical setting where group labels are unavailable, unlike GroupDRO, DFR, and many prior methods that need group information at some stage. The paper clearly states this in Sections 3.1 and 4.2.1.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed redirection mechanism is unverified, weakening the paper's explanatory story.** The paper's central argument is: (a) minority examples are memorized in specific neurons → (b) dropping those neurons helps → (c) therefore, allocate *random* memorizing neurons, and the network will learn to use *those* for memorization, then drop them at test time. Step (c) is an untested hypothesis. The paper does not verify that the neurons FairDropout allocates as "memorizing" coincide with the neurons that the Maini et al. analysis would identify as critical for minority-group examples. Without this verification, the improvement could stem from generic regularization (dropping any subset of neurons) rather than the claimed redirection of memorization. The paper partially acknowledges this in Limitations ("this assumption requires further exploration"), but this is the method's core justification.

2. **Missing critical control: comparison to standard/random dropout at the same rate and location.** Without comparing FairDropout to standard dropout (or random neuron dropping of the same proportion at the same layer), the improvement cannot be attributed to the *example-tied* mechanism. A generic dropout or simple regularization effect could explain the results. This control is essential for distinguishing FairDropout's claimed mechanism from a simpler alternative. (The training-mode vs. testing-mode comparison in Figure 4 provides some internal evidence that allocated neurons are causally important, but does not substitute for a direct random-dropout baseline.)

### Minor

3. **The allocation mechanism (role of p_mem) is ambiguously described, harming reproducibility.** The paper states (Section 3.3): "each sample is allocated a memorizing neuron uniformly with probability $p_{\mathrm{mem}}$" and simultaneously "every example allocates the same fixed number of memorizing neurons" and "each image allocates only one memorizing neuron." If every example receives exactly one memorizing neuron, the role of $p_{\mathrm{mem}}$ is unclear—it cannot be a per-example probability. This ambiguity needs to be resolved with a precise algorithmic specification (pseudocode or a clear description of whether $p_{\mathrm{mem}}$ controls the fraction of examples that get a memorizing neuron, the pool size, or something else).

4. **No ablation of the extra linear layer added on BERT.** For BERT, the paper adds a new linear layer before the FairDropout layer (Section 4.2.1). This changes the architecture relative to baselines. No experiment isolates the effect of this added layer from the FairDropout mechanism itself. The reported improvements on MultiNLI could partly come from the architectural change rather than the example-tied dropout.

5. **No hyperparameter sensitivity analysis.** The paper introduces hyperparameters $p_{\mathrm{gen}}$ and $p_{\mathrm{mem}}$ and tunes layer placement per dataset, but reports no sensitivity analysis. The text mentions $p_{\mathrm{gen}}=p_{\mathrm{mem}}=0.2$ for CelebA, but does not show how results vary with these choices or the chosen placements for each dataset. This makes it difficult to assess robustness or provide practical guidance.

6. **Asymmetric baseline reporting.** Baseline results in Table 1 are sourced from Yang et al. (2023) without standard deviations for most entries, while FairDropout results include standard deviations from 5 runs. The paper does not verify that baseline numbers are reproducible in the same environment. This makes statistical comparisons unreliable.

### Trivial

7. **The "first time" claim is slightly overstated.** The paper claims to study the memorization-generalization link "for the first time in the context of spurious correlation." While the specific neuron-level localization technique is novel in this setting, prior work (e.g., Feldman 2020, which the paper cites) has examined memorization in related contexts. The claim should be softened to avoid overclaiming novelty.

## Nice-to-Haves

- A direct comparison to standard dropout and random neuron dropping at matched rates would cleanly separate the example-tied contribution from generic regularization.
- Verification that FairDropout-allocated neurons actually capture minority-group memorization (e.g., by running the Maini et al. analysis on FairDropout-trained models and checking overlap with allocated neurons).
- Sensitivity plots for $p_{\mathrm{gen}}$ and $p_{\mathrm{mem}}$ on at least one dataset.
- Reporting the chosen FairDropout layer positions for each dataset.
- Ablation of the added linear layer on BERT.
- Reproducing at least key baselines under the same evaluation pipeline to enable proper significance comparison.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Prior work on memorization has examined spurious features (Feldman 2020)."** — The paper cites Feldman 2020 in its Limitations section. The claim is about applying the *neuron-localization* technique from Maini et al. to spurious correlations for the first time, which is defensible. Moved because the critic's framing mischaracterizes the specific novelty claim.
- **"The Maini et al. method was designed for label-noise and may not measure the right thing in spurious correlation."** — The paper explicitly frames this as "memorization in the context of spurious correlation" and uses the method as a diagnostic tool. The conceptual adaptation is acknowledged. This is a philosophical concern rather than a concrete flaw in the paper's analysis.
- **"Figure 3 does not control for overlap in neurons dropped across examples."** — This is a minor methodological note about an analysis experiment that is not central to the method. It does not affect the paper's core claims.
- **"Conversion of baseline methods changes their behavior."** — The paper follows the standard benchmark convention (Yang et al., 2023). This is a field-wide practice, not a paper-specific flaw.
- **Pure formatting criticism about "the paper does not report how much the choice of placement affects results" framed as structural issue.** — Kept in Minor as "No hyperparameter sensitivity analysis" with proper framing; the original framing as a structural methodological gap was excessive.

## Novel Insights

None beyond the paper's own contributions. The review surfaces the fundamental gap between the diagnostic analysis (memorization can be localized and dropping those neurons helps) and the proposed intervention (allocate random neurons and drop them), but this is a gap the paper itself could investigate rather than an external insight.

## Suggestions

1. **Verify the redirection mechanism.** Train with FairDropout, run the Maini et al. analysis on the resulting model, and check whether the allocated memorizing neurons for a given minority-group example correspond to the neurons identified as critical for that example's prediction.
2. **Add a random-dropout baseline.** Drop the same proportion of neurons from the same layer(s) uniformly at random. If FairDropout outperforms this baseline, the example-tied allocation is responsible.
3. **Resolve the p_mem ambiguity.** Provide a precise algorithmic description: how many memorizing neurons are assigned per example, whether assignment is probabilistic or deterministic, and what $p_{\mathrm{mem}}$ controls.
4. **Add hyperparameter sensitivity.** Show worst-group accuracy for a grid of $p_{\mathrm{gen}}$ and $p_{\mathrm{mem}}$ on at least one dataset to demonstrate robustness.
5. **Report chosen layer placements per dataset and ablate the BERT projection layer.**

## Score and Decision

**Originality:** Good. Adapting example-tied dropout to spurious correlation is a novel direction, but the novelty is partially contingent on whether the mechanism differs from generic regularization.  
**Importance of research question:** High. Reducing reliance on spurious correlations without group annotations is a practically important problem.  
**Claims support:** Moderate. The empirical results are consistent, but the central mechanistic claim is unsupported and missing controls weaken attribution.  
**Soundness of experiments:** Moderate. The evaluation is broad (5 datasets, multiple modalities) but missing key controls (random dropout) and sensitivity analyses.  
**Clarity of writing:** Adequate but imprecise in the method description (p_mem ambiguity, allocation mechanism).  
**Value to the research community:** Moderate. If the mechanism can be verified, the approach is useful; in its current form, the contributions are promising but inconclusive.

The paper presents an intriguing idea and useful empirical results, but the core mechanism is unverified, and the experimental design lacks the controls needed to attribute improvements to the claimed innovation. The contribution is genuinely novel and the results are promising, but the paper would be significantly strengthened by verifying the redirection mechanism and adding a random-dropout baseline.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>