Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated final review.

---

## Summary

This paper proposes Bayesian Tree-Dependent Factorization (BTF), a probabilistic factor model that represents latent factors as nodes in a binary tree, where each factor's loading is a product of sub-loadings (constrained to [0,1]) with right/left child positions indicating positive/negative correlation with the parent. A multi-view extension shares loadings across data modalities. The method is evaluated on simulations and on METABRIC breast cancer gene expression and clinical data, where the authors use gene set enrichment analysis to argue that BTF recovers more biologically meaningful structure than PCA, ICA, and NMF.

## Strengths

- **Novel continuous hierarchical loading composition.** BTF's construction of loadings as products of sub-loadings in a binary tree (Eq. 1, Section 2) is a genuinely novel representation. Unlike eTrees (discrete membership indicators), PCA (orthogonality), or ICA (independence), it provides continuous conditional weights with signed dependencies. This formal innovation is clearly laid out.

- **Detailed, literature-grounded biological analysis of the luminal A subtree.** The analysis in Section 4.3 (Figure 9) traces specific pathway enrichments (estrogen signaling, FOXA1, ECM organization, lipid metabolism) to clinically coherent factor patterns (ER positivity, mucinous tumors, older patients with larger tumors), with each finding cross-referenced to specific literature. This demonstrates that the model can recover known biology, even if the evaluation is qualitative.

- **Honest discussion of limitations.** Section 5 explicitly acknowledges that the binary tree "is unlikely to always reflect the true underlying structure," that depth must be specified a priori, and that the multi-view equal-loadings assumption is strong. This candor is valuable.

## Weaknesses

### Fatal
None.

### Major

- **Key hierarchical baselines are entirely absent from quantitative evaluation.** The introduction/releated work discusses eTrees (Almutairi et al., 2021), hierarchical matrix factorization (Sugahara & Okamoto, 2024; Li et al., 2019), and Tree-Dependent Component Analysis (Bach & Jordan, 2002) as methods that also target hierarchical structure. Yet the real-data comparison (Section 4.2) includes only PCA, ICA, and NMF — none of which model hierarchical structure. TCA only appears in the simulations (and even there, on data generated from BTF's own process). eTrees is never quantitatively compared. The paper claims to address the limitations of these methods but never tests whether BTF actually performs better than them. This is a **structural gap** in the evaluation.

- **The enrichment-based comparison is confounded by the number of factors.** The paper measures "number of unique biological enrichments" (Fig 7, right) to claim BTF outperforms baselines. BTF with 4 subtrees of depth ≥3 (METABRIC model) has many factors (≥28). The paper does not state how many components were used for PCA, ICA, or NMF. More factors provide more opportunities to accumulate enrichments, and no normalization (enrichments per factor) or correction for multiple testing across factors is reported. The headline claim that BTF "outperforms" baselines on real data does not follow from this comparison.

- **Multi-view evaluation establishes only that two views > one view, not that the multi-view formulation is a genuine contribution.** The multi-view experiments (Fig 8, Section 4.3) compare MV-BTF only against SV-BTF. No comparison is made against joint NMF, multi-view CCA, group factor analysis, or any established multi-view method. Showing that using two data modalities provides more signal than one is a trivial finding. The multi-view contribution requires evidence that the specific shared-loading constraint yields benefits over existing multi-view factorization approaches.

- **"Bayesian" framing is misleading given the actual inference procedure.** The paper claims (line 16) that the Bayesian approach allows generating "posterior estimates of uncertainty and likelihood." However, the learning algorithm is ADAM optimization (line 58), which produces MAP point estimates. No variational inference, MCMC sampling, or uncertainty quantification procedure is described or referenced. No posterior intervals, credible regions, or uncertainty estimates are reported anywhere in the paper. The model places priors on parameters, making it Bayesian in the weakest sense, but the advertised posterior inference capability is not delivered.

### Minor

- **Simulations test only self-recovery.** Data in Section 3 is generated from BTF's own generative process (random sub-loadings composed via BTF's product structure). This verifies that ADAM can invert the forward model, but provides limited evidence that BTF discovers structure in data with genuinely different hierarchical properties (e.g., nonlinear dependencies, different tree interaction patterns). A more informative simulation would generate data from a non-BTF hierarchical process and test whether BTF recovers useful structure that simpler methods miss.

- **Model specification contains unresolved ambiguities.** (a) The prior on sub-loadings is written as \(z_{ij} \sim \beta(\beta_0)\) (line 49), which is non-standard — a beta distribution requires two parameters. (b) The covariance \(\Sigma_x\) in the likelihood \(\mathcal{N}(\mu_x, \Sigma_x)\) (line 55) is introduced but never defined; readers must assume isotropic noise (\(\sigma^2 I\)). These do not invalidate the method but hinder reproducibility from the main text alone.

- **Biological interpretation uses PAM50 labels as a structural constraint, but findings are presented without comparison to simpler alternatives.** The METABRIC model fixes subtree loadings to PAM50 subtype indicators (line 114). This is clearly stated, so the critic's claim that it is "framed as unsupervised discovery" overstates the issue — the paper is transparent about it. However, the detailed biological narrative (Section 4.3) is entirely post-hoc, with no comparison showing that PCA or NMF factors under the same subtype-stratified analysis would yield less specific or less coherent enrichments. A comparative qualitative analysis would substantially strengthen the interpretive claims.

- **No ablation separating the effect of hierarchy from non-negativity.** BTF on real data uses non-negativity constraints; NMF is the only non-negative baseline. The paper cannot attribute enrichment gains to the hierarchical structure versus the non-negativity constraint, since BTF without non-negativity is never evaluated (Section 4.2, Fig 7).

### Trivial

- Figure 5 is described in text but the sentence cuts off mid-description at the bottom of page 7 (paragraph ends abruptly after "TCA correctly identified that").
- Notation: the equation on line 55 contains garbled typesetting ("Σ\Σ\left|Z,F\right\rangle").

## Nice-to-Haves

- A sensitivity analysis varying sample size, noise level, and dimensionality in the simulations would strengthen the evidence for BTF's robustness.
- Reporting runtime or convergence behavior would aid practical assessment of the method's scalability.
- Clarifying whether the ADAM optimization maximizes the log-posterior (MAP) or some other objective would resolve the "Bayesian" framing ambiguity.

## Removed Points

These points were raised by the reviewers but are removed per the filtering rules:

1. *"Hyperparameters θ, β₀, σ₀ are not stated"* — The paper refers to the Supplement for hyperparameter choices. Supplements are stripped during PDF extraction; this criticism reflects a parsing artifact, not an author omission. **Removed.**

2. *"Tree depths not stated"* — For simulations, "depth of 3" is clearly stated (Section 3). For METABRIC, "the first 3 levels" is stated (Section 4). The critic misread the paper. **Removed.**

3. *Strength Finder's Strength 5 (explicit handling of identifiability)* — Acknowledging a known problem and proposing a solution is standard practice, not a distinctive strength. **Removed.**

4. *Strength Finder's Strength 6 (systematic comparison)* — Described as "systematic" but conflicts with the verified major weakness about missing hierarchical baselines. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard evaluation gaps (missing baselines, confounded metrics, limited scope of simulations) but do not offer a novel synthesis that the paper's own claims do not already suggest.

## Suggestions

1. **Add hierarchical baselines to the real-data evaluation.** Compare against eTrees and TCA on the METABRIC data, or at minimum provide a simulation where these methods are tested on non-BTF hierarchical data. Without this, the paper's positioning against those methods is unsupported.

2. **Control for the number of components in the enrichment comparison.** Either (a) match the number of PCA/ICA/NMF components to BTF's total factor count, or (b) report enrichments per factor with error bars across random seeds, or (c) both. This is essential to establish that BTF's hierarchy, not simply its larger model capacity, drives the enrichment gains.

3. **Clarify the inference procedure.** If the method performs MAP estimation via ADAM, state this explicitly and remove language about "posterior estimates of uncertainty." If posterior inference is genuinely performed, describe the procedure.

4. **Ablate the hierarchy and non-negativity.** Compare BTF with non-negativity vs. BTF without non-negativity on the real data to separate the effect of the tree structure from the effect of the positivity constraint.

## Score and Decision

The core idea — a continuous hierarchical loading composition via tree-structured products of sub-loadings — is novel and the biological application is well-motivated. However, the evaluation has three major gaps that prevent the paper from meeting the standard for a top venue: (1) the most relevant hierarchical baselines (discussed in the paper itself) are absent from quantitative comparison; (2) the primary real-data metric is confounded by uncontrolled factor count; and (3) the multi-view contribution is only validated against single-view BTF, not against any existing multi-view method. These gaps would require substantial additional experimentation to resolve. The paper also overstates its "Bayesian" capabilities by claiming posterior inference while delivering only ADAM-based point estimates.

With significant revisions addressing these evaluation gaps, this could be a strong contribution. In its current form, the contribution is not adequately established.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>