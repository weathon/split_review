Now I have all the verification I need. Let me compile the final consolidated review.

---

## Summary

This paper introduces the first method for conditioning protein backbone diffusion models on dynamical properties — specifically the lowest non-trivial normal mode of oscillation via Normal Mode Analysis (NMA). The key innovation is replacing the intractable conditional score term with a simple analytical loss (NMA-loss), avoiding the need to train an auxiliary eigenvector-predicting network. The framework supports joint conditioning on both dynamics and structure, enabling scaffolding of functional hinge motifs. The method is demonstrated as a plug-and-play modification to the pre-trained Genie model (no retraining), producing novel backbones with targeted hinge dynamics that are partially designable by scTM criteria.

---

## Strengths

1. **First method to condition protein diffusion on dynamical properties.** The paper addresses a genuine gap: existing protein diffusion models condition on structure (motifs, symmetry) but not dynamics, despite the well-known link between low-frequency collective motions and biological function. Evidence: Abstract, contributions list (line 16), and Section 2.2 motivation.

2. **Analytical approximation avoids training a dynamics-conditioning network.** Instead of learning a neural network to predict normal-mode eigenvectors (which is computationally difficult for variable-size matrices), the method approximates \(p(y|x_0)\) via a simple analytical loss and uses reconstruction-guidance-style score decomposition. This makes conditioning computationally feasible and directly transferable to pre-trained models without retraining. Evidence: Section 3.1 (lines 101–102), discussion of prior eigenvector-learning approaches.

3. **Plug-and-play transfer to Genie without retraining.** The framework is applied to the unconditional Genie model by modifying only the sampling process with guidance terms. This demonstrates that dynamics conditioning can be retrofitted onto existing large diffusion models. Evidence: Abstract, Section 4.4 (line 211), Section 5.2 results.

4. **Invariant loss design.** The NMA-loss compares pairwise angles and relative amplitudes of displacement vectors, making it rotation/translation invariant and length-independent — a principled choice given the properties of normal-mode eigenvectors. Evidence: Section 3.2, Equation 15.

5. **SDE-based theoretical justification.** The paper provides a continuous-time score decomposition (Section 3.1) analogous to classifier guidance, showing how the delta approximation and Tweedie's formula lead to the practical loss function. Evidence: Equations 9–14.

6. **Quantitative evidence that conditioning lowers NMA-loss.** Controlled experiments with the GVP model (Figure 2) show that conditioning significantly shifts the NMA-loss distribution toward lower values compared to unconditional sampling. Visual inspection in Figure 3 confirms better alignment of displacement vectors. Evidence: Section 5.1, Figures 2–3.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing structure-only baseline for joint conditioning (hinge targets).** The hinge-target experiments compare joint (dynamics+structure) conditioning against unconditional and dynamics-only conditioning, but *not* against structure-only conditioning. This means the added value of the dynamics term on top of structure conditioning is not isolated. Without this baseline, one cannot determine whether the dynamics conditioning meaningfully lowers NMA-loss beyond what structure conditioning alone would achieve, or whether it degrades designability. The paper claims "dynamics conditioning must be accompanied by structure conditioning" (line 160), which makes the structure-only baseline the most natural control — yet it is absent. This is the single largest evidential gap. (The paper does provide a dynamics-only comparison for scTM, which partially mitigates this, but the critical comparison remains missing.)

2. **GVP model experiments lack designability assessment.** For the random/strain targets (Section 5.1), only structural statistics (bond lengths, \(R_g\), SSE proportions, TM-score novelty) are reported. No sequence-design or inverse-folding step is applied, so there is no evidence that these dynamics-conditioned backbones can fold into stable proteins. The paper's abstract claims "biologically plausible" backbones, yet this is only tested for the Genie hinge experiments. Since the hinge experiments have the baseline problem noted above, the GVP model's designability gap weakens the overall evidence that dynamics conditioning produces useful proteins independent of the Genie architecture.

### Minor

3. **NMA implementation is under-specified, harming reproducibility.** The paper does not state which elastic network model is used (cutoff distance, spring constant, mass assignment), how the Hessian is constructed, which eigenvector extraction routine is called, or how the lowest non-trivial mode is identified (e.g., whether translations/rotations are projected out). These choices directly affect the displacement vectors that enter the NMA-loss. Without this specification, the experiments cannot be reproduced, and it is unclear whether reported loss values reflect genuine dynamics conditioning or artifacts of a particular NMA parameterization. (The authors state code will be made public, which mitigates this somewhat, but the paper itself should document these details.)

4. **Asymmetric filtering and small sample sizes for hinge targets.** Conditional samples are filtered by motif RMSD (<1Å) and chain distance (3.75–3.85Å), retaining only 23–60% of samples and yielding just 27 per target. Unconditional samples are not filtered by the same criteria (they would be eliminated). Consequently, scTM scores are reported only for the filtered conditional set, conflating conditioning effectiveness with filter stringency. Reporting scTM on the unfiltered conditional set (with breakdown by filter pass/fail) would be more informative. The sample size of 27 also means scTM proportions have wide confidence intervals.

5. **Guidance scale sensitivity not discussed.** The guidance scales are reported as "different for each target, and in the order of 2000–3000" (line 211). This is a large range and suggests sensitivity to the target and/or hyperparameter. A brief discussion of how the scale was chosen and whether results are robust to reasonable changes would strengthen the paper.

6. **"Energy" for strain targets is ambiguous.** The paper states strain targets are "10 consecutive residues with the largest summed energy" (line 191) without defining whether this refers to kinetic energy in the mode, strain energy from the Hessian, or some other quantity.

### Trivial

7. **Eigenvector extraction scope.** Clarify whether NMA eigenvectors are extracted from the full protein structure and then sliced to the subset \(\mathcal{C}\), or whether NMA is performed on the subset alone (the latter would be incorrect). The amplitude normalization discussion (Section 3.2) implicitly assumes the former but should state it explicitly.

---

## Nice-to-Haves

- A designability check (ProteinMPNN + ESMFold) on a subset of the GVP model's conditioned samples would substantially strengthen the claim of biological plausibility beyond the Genie experiments.
- A brief note on wall-clock cost added by repeated eigenvector solves during sampling would help readers assess practical applicability.

---

## Removed Points

These points from the reviews were removed with justification:

1. **Criticism that the Section 3.1 derivation is "sloppy" or incorrect.** The critic claims the derivation requires that \(p(\mathbb{E}[x_0|x_t])\) "cancels in the chain rule" in a questionable way. In fact, the derivation is mathematically sound: the \(p(\mathbb{E}[x_0|x_t])\) terms appear in both numerator and denominator of the Bayes rule substitution and cancel directly (Equation 14). The resulting \(-\nabla_{x_t} l(y, v(\mathbb{E}[x_0|x_t]))\) follows straightforwardly. The critic's concern about the "unconditional model's score... not appear[ing]" reflects a misunderstanding of the algebra; the unconditional score correctly enters through the separate \(\nabla_{x_t} \ln p_t(x_t)\) term (Equation 11), not through the conditioning gradient. This is standard reconstruction guidance (Chung et al. 2022a).

2. **Complaint that the amplitude term normalization is problematic because eigenvectors are unit vectors.** The paper already handles this correctly by normalizing by \(||y_D||\) and \(||v(x)||\) — the loss uses *relative* amplitudes, which is the correct approach given that NMA provides only relative amplitude information (as the paper states, citing Bahar et al. 2010).

3. **"Comprehensive evaluation pipeline" strength claim** from the Strength Finder. This claim conflicts with the verified weaknesses (missing structure-only baseline, GVP lacking designability checks). The pipeline is reasonable but not comprehensive enough to warrant this label.

4. **Formatting/style nitpicks and parser artifacts.** These are not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core strengths the paper claims (first dynamics conditioning method, analytical approximation, plug-and-play transfer) and identify evidential gaps but do not reveal unrecognized conceptual observations.

---

## Suggestions

1. **Add structure-only conditioning as a baseline for the hinge-target experiments.** Use the same motif scaffolding method on Genie without the NMA-loss guidance. Compare scTM and NMA-loss across four conditions: unconditional, structure-only, dynamics-only, and joint. This is the single most impactful improvement and would directly validate the claim that dynamics conditioning adds value beyond structure conditioning.

2. **Specify NMA implementation details** in a new paragraph or appendix: elastic network model (cutoff, spring constant, mass model), eigenvector extraction routine, and how the lowest non-trivial mode is identified (projection of translations/rotations).

3. **Run designability checks on a representative subset of GVP model samples** to demonstrate biological plausibility for the dynamics-only conditioning setting.

4. **Report conditional scTM before filtering** (on the full set of generated samples) alongside the filtered results, so readers can assess how much the filter drives the reported designability proportions.

5. **Clarify "energy" for strain targets** and briefly discuss guidance scale selection and sensitivity.

---

## Score and Decision

The paper introduces a genuinely novel and well-motivated idea — conditioning protein diffusion on dynamics — with a clean theoretical framing and a practical, transferable implementation. The core contribution is clear and the problem is important. However, the experimental evaluation has notable gaps: the missing structure-only baseline for joint conditioning prevents isolating the contribution of the dynamics term, and the GVP model experiments stop short of demonstrating designability. These are addressable with additional experiments and documentation. The paper should not be accepted without revision, but the core approach is sufficiently promising that a major revision with the recommended ablations could make it a solid contribution.

**Originality**: High — first to condition protein diffusion on dynamics.  
**Importance**: High — addresses a genuine gap linking dynamics to function.  
**Claims supported**: Partially — core claim (dynamics conditioning works) is supported, but added value over structure conditioning is not isolated.  
**Soundness**: Moderate — main concerns are the missing ablation and under-specified NMA implementation.  
**Clarity**: Good — writing is clear and well-structured.  
**Value to community**: High — opens a new direction and provides a framework that transfers to other models.

MY FINAL SCORE: <pineapple>6.0</pineapple>  
MY FINAL DECISION: <orange>Accept</orange>