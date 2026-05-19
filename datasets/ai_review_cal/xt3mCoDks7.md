- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5
Now I have all the verification I need. Let me produce the final consolidated review.

## Summary
This paper presents MolJO, a gradient-based framework for structure-based molecule optimization (SBMO) that jointly guides both continuous atom coordinates and discrete atom types within a Bayesian Flow Network (BFN). The key technical contributions are: (1) joint gradient guidance over continuous and discrete modalities via the BFN's continuous posterior space, which overcomes the limitations of prior methods that guide only coordinates (TAGMol); and (2) a backward correction sampling strategy that uses a sliding window to correct past latent states, providing a flexible explore-exploit trade-off. MolJO achieves state-of-the-art results on CrossDocked2020 (Success Rate 51.3%, Vina Dock -9.05, SA 0.78), surpassing previous gradient-based methods by 4× and oracle-based methods, and generalizes to constrained tasks including R-group optimization and scaffold hopping.

## Strengths

- **Joint gradient guidance across continuous coordinates and discrete atom types substantially outperforms single-modality guidance.** Section 4.1 derives guidance over both modalities, and Figure 5 shows that ablating either coordinate or type guidance reduces performance; the full joint model consistently gives better Vina Dock, QED, and SA. This directly addresses the limitation of TAGMol (coordinate-only guidance) and provides a mechanistic explanation for the 4× Success Rate improvement in Table 1.

- **Backward correction strategy improves gradient alignment and boosts both unguided and guided sampling.** Section 4.2 introduces a sliding-window correction (Algorithm 1, lines 7–10) and Figure 2 visualizes how different window sizes \(k\) control gradient alignment. Table 4 quantifies the benefit: backward correction (B.C.) improves Vina Dock, QED, SA, and Success Rate over vanilla sampling and over full correction (k=n=200), with guidance only producing positive gains when backward correction is used.

- **State-of-the-art results on CrossDocked2020 across multiple objectives, with large margins over existing methods.** Table 1 reports that MolJO achieves the best Vina Dock (-9.05), SA (0.78), and Success Rate (51.3%), exceeding the previous best gradient-based method (TAGMol: 12.5%) by 4× and the best oracle-based method (DecompOpt: 44.6%) by 6.7 absolute points.

- **Generalization to constrained tasks (R-group optimization, scaffold hopping) with substantially higher validity and success rate than diffusion baselines.** Table 3 shows MolJO obtains 89.3% validity and 58.5% Success Rate on scaffold hopping, while diffusion baselines (TargetDiff, MolCRAFT) are below 70% validity and 20% Success Rate.

- **Sliding-window formulation unifies and extends existing BFN sampling strategies.** Section 4.2 notes that setting k=1 recovers the original BFN sampling and k=n recovers MolCRAFT's full correction, with intermediate k (e.g., 130) yielding the best performance (Table 4).

- **Thorough ablation studies validate each design choice separately.** Figure 5 ablates joint vs. single-modality guidance; Table 4 ablates backward correction vs. vanilla and full correction. All comparisons use the same base model and evaluation protocol.

## Weaknesses

### Fatal
None.

### Major

- **Missing details on the energy function — a central component of the method.** The paper relies on an energy function \(E(\theta, p, t)\) for gradient guidance (Section 4.1, Algorithm 1) but does not specify: (a) what data it is trained on and whether it uses the same train/validation/test split as the generative model, (b) its neural architecture, (c) the loss function, (d) how time-dependence is incorporated, or (e) any measures taken to avoid data leakage with the generative model. Since the energy function provides the gradients that drive optimization, omitting these details prevents reproducibility and makes it impossible to assess whether the reported gains stem from the guidance framework itself or from an exceptionally well-calibrated predictor. The paper only says it "requires training energy functions as a proxy" (Conclusion), but gives no further specification.

- **No error bars, confidence intervals, or variance reporting for any experimental result.** Table 1, Table 3, and Table 4 all report single-point estimates for Success Rate, Vina Dock, SA, QED, and Diversity. The paper samples only 100 molecules per test protein (line 211), but variance across proteins, random seeds, and sampling stochasticity is not quantified. Without this, it is impossible to determine whether the reported advantages (e.g., Success Rate 51.3% vs. DecompOpt's 44.6%) are statistically robust or within the noise of the evaluation. This is the most significant evidential gap.

- **Key hyperparameters for main experiments are not disclosed.** Algorithm 1 lists guidance scale \(s\) and backward correction steps \(k\) as required inputs, but the main experiments (Table 1, Table 3) never state what values of \(s\) and \(k\) were used. The ablation section reveals that \(k=130\) was tested (Table 4), and it is reasonable to assume this carried over to main experiments, but the paper should state this explicitly. The guidance scale \(s\) is not mentioned at all beyond its definition (line 181).

### Minor

- **The "Me-Better Ratio" metric is touted in the abstract, contributions, and Figure 1 but never formally defined in the main text.** The reader is left to infer its meaning from context. This should be operationalized.

- **The distribution-shift problem of guidance is not acknowledged or addressed.** The energy function is presumably trained on the CrossDocked2020 training set, but during optimization the generative model is pushed to produce molecules with improved predicted properties — likely moving out of the training distribution. The energy function's predictions on such out-of-distribution molecules are unvalidated. The paper should at minimum acknowledge this known limitation and discuss whether any mitigation (uncertainty-aware energy, correlation analysis on held-out data) was considered.

- **No analysis of computational cost.** The paper contrasts gradient guidance favorably against oracle-based methods (which require expensive docking simulations in the loop) but never reports runtime or the cost of training and evaluating the energy function. A simple comparison (e.g., wall-clock time per protein) would strengthen the practicality claim.

- **Proposition 4.4 (equivariance) is stated without justification or proof.** The claim that the guided process preserves SE(3)-equivariance given an equivariant \(\Phi\) and \(E\) is plausible, but the paper provides no argument or citation for why adding gradient guidance to the BFN update preserves equivariance. A brief justification belongs in the main text.

- **The choice \(k=130\) for the backward correction window is reported as "best" but it is unclear whether this was selected on a validation set.** If so, the paper should state that explicitly and report the selection procedure.

### Trivial

- **Remark 4.2 uses dense chain-rule notation (\(g_{y^x} = g_\mu \frac{\rho_i}{\alpha_i}\)) that is difficult to parse.** This could be clarified with a brief intermediate step.
- **Minor garbled artifacts throughout (parser issues, not author errors).**

## Nice-to-Haves
- A correlation analysis between the learned energy function's predicted values and actual Vina scores on held-out data would validate that guidance operates on a trustworthy proxy.
- The backward correction derivation (Eqs. 11–13) could benefit from a brief intuitive explanation of the "additive accuracy" property of BFN for readers less familiar with Graves et al. (2023).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proposition 4.1 stated without proof"** — Removed per hard rule: the parser strips appendix content from all papers; derivations or proofs may have existed there.
- **"Backward correction derivation compact / hard to follow for readers not deeply familiar with Graves et al."** — This is a presentation preference, not a technical flaw, and the paper is already dense content-wise. Removed as a non-substantive nitpick.
- **"Unfair comparison: oracle-based methods use actual docking while MolJO uses learned energy"** — The paper acknowledges this distinction (lines 217-218, row G+O) and the comparison is fair: MolJO without oracles outperforms oracle-based methods, and the oracles-as-postprocessing variant (G+O) further improves results. This asymmetry favors the baseline, not the author's method, so it is removed per the asymmetric fairness rule.
- **Strength Finder's strengths that are generic/superficial** — All strengths listed were specific and evidence-backed, so none removed.
- **"The paper's contribution stands but... the authors should be required to add..."** from the harsh critic's overall assessment — This is evaluative framing, not a weakness per se.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely converge on the same points: the method is technically sound and empirically strong, but the evidential support is weakened by missing error bars and incomplete specification of the energy function. The synthesis does not surface a perspective on the paper that the authors have not already articulated.

## Suggestions

1. **Provide full energy function specification**: Architecture, training data and split, loss function, and how time-dependence is achieved. Even a brief paragraph in the main text or a dedicated appendix section would suffice.

2. **Add error bars for all main results**: Report at least the standard deviation over multiple random seeds or bootstrapped confidence intervals for Success Rate, Vina Dock, SA, QED, and Diversity in Tables 1 and 3.

3. **Disclose hyperparameters for main experiments**: State the guidance scale \(s\) and backward correction window \(k\) used for the results in Table 1 and Table 3, and describe the validation procedure used to select them.

4. **Formally define "Me-Better Ratio"** in the main text (Section 5.1, alongside the other metrics).

5. **Add a brief discussion of the distribution-shift limitation** and any mitigation strategy, or at minimum a caveat that the energy function's OOD reliability has not been independently validated.
