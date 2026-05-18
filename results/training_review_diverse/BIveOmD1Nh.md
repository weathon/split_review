Here is my final consolidated review after carefully verifying all claims against the paper.

---

## Summary

This paper proposes a novel learned scoring function for molecular docking defined as the cross-correlation of SE(3)-equivariant scalar fields (parameterized by E3NNs) independently computed for the protein and ligand. Because the score takes the form of a cross-correlation, it can be optimized over rigid-body translations and rotations using fast Fourier transforms, yielding substantial speedups — particularly when precomputations are amortized across multiple ligands binding to the same protein pocket. The method is evaluated on decoy pose scoring and rigid conformer docking, showing competitive accuracy to Vina/Gnina on crystal structures and significantly better robustness on ESMFold predicted structures, with up to 45× total runtime reduction in a virtual screening scenario.

## Strengths

1. **Novel and principled formulation.** The paper is the first to propose *learning* a protein–ligand scoring function whose functional form is explicitly a cross-correlation of scalar fields, directly enabling FFT-based optimization. This departs from both physics-inspired scoring functions and pose-wise deep learning models. The theoretical derivation connecting E3NN-equivariant fields, spherical harmonic expansions, and closed-form Fourier-space expressions (Eq. 4–10) is clean and rigorous.

2. **Strong empirical demonstration of the accuracy–speed tradeoff, especially on predicted structures.** On ESMFold structures, ESF-N achieves nearly double the success rate of Vina/Gnina in rigid conformer docking (47% vs 24%/28% <2 Å RMSD, Table 2) and substantially lower top-ranked RMSD in decoy scoring (1.38 Å vs 2.43 Å/2.19 Å, Table 1). On the PDE10A dataset with a common pocket, ESF-N-RF achieves comparable accuracy to Vina (70% vs 74% <2 Å) while reducing total inference time from 67 s to 1.5 s — a 45× speedup through amortization (Table 2).

3. **Systematic characterization of amortization opportunities.** Table 1 breaks down computation frequencies and runtimes across four inference modes (TF, RF, TS, RS), making it concrete where and how precomputation is reused (e.g., 65 ms per protein structure, 4.3 ms per ligand conformer, 1.0 μs per pose for TS). This level of detail grounds the amortization claims and informs practitioners where the method fits workflow-wise.

4. **Tractable training via conditional log-likelihoods with FFT marginalization.** The training objective (Eq. 11–12) leverages the FFT cross-correlation to compute the otherwise intractable marginal likelihoods over translations and rotations in closed form, enabling direct optimization of an energy-based model without MCMC. This is a clever algorithmic insight specific to the proposed architecture.

## Weaknesses

### Fatal
None.

### Major

1. **The rotational FFT pipeline relies on an uncontrolled approximation whose effect on docking accuracy is unquantified.** The conversion from atom-centered local expansions (Eq. 3) to a global spherical harmonic expansion (Eq. 7) uses a least-squares projection (Eq. 11). The authors correctly note that "it is generally not possible to express the ligand or protein scalar field as defined in Equation 3 using the form in Equation 7" and attribute the worse performance of RS vs TS to "the spatially coarser representation." However, the paper never directly measures the projection error (e.g., RMSD between exact and projected fields on held-out grid points, or correlation between exact and projected scores on decoy poses). Since the rotational FFT (RF) pipeline — which is the key to the amortization advantage on the PDE10A dataset — depends on this approximation, its severity matters. If the projection error shifts the scoring function maximum by >1 Å RMSD, RF may be fundamentally unreliable as an optimization procedure. The TS vs RS comparison is evidence that the approximation has a cost, but it does not quantify how large that cost is or whether it affects the ranked-ordering of poses. **Why it matters:** Without this characterization, readers cannot assess whether the rotational FFT is a genuine contribution or an expedient whose drawbacks are hidden.

### Minor

1. **The training objective is a heuristic, and the paper's validation of it is indirect.** The authors optimize the sum of two conditional log-likelihoods (Eq. 11–12) and explicitly state that "neither technically corresponds to the joint log-likelihood of the pose." The paper claims the objective "works well in practice," but the only evidence is the downstream docking/scoring metrics. What is missing is a direct check: does the learned scoring function actually rank the true pose first on training examples? Are the conditional densities peaked at the correct values? An ablation comparing against a simpler contrastive loss (e.g., hinge loss pushing true pose scores above perturbed pose scores by a margin) would demonstrate whether the complexity of the conditional likelihood formulation is necessary. **Why it matters:** If the scoring function is not properly concentrated around true poses, the FFT optimization — however fast — optimizes a misaligned target. The downstream results suggest this is not catastrophic, but a targeted validation would eliminate the concern.

2. **No error bars or dispersion measures on any reported metric.** All results are medians over test complexes without interquartile ranges, bootstrap confidence intervals, or any measure of variability. Given the moderate test set sizes (PDBBind test split, 77 PDE10A complexes), readers cannot gauge the reliability of the observed improvements or whether differences between methods are meaningful. **Why it matters:** This is a standard expectation for comparative benchmarking; its absence weakens the quantitative claims.

3. **The ESMFold structure quality is not characterized.** The paper uses ESMFold structures from the DiffDock dataset but never reports the RMSD between the ESMFold and crystal structures. The "robustness" claim is anchored to a single predictor at an unknown accuracy level. Reporting the distribution of backbone RMSD between ESMFold and crystal would contextualize the robustness results and let readers judge at what level of structure degradation the method's advantage kicks in.

4. **The alpha-carbon-only protein representation is a significant design choice with limited justification.** The protein scalar field is built from alpha-carbon coordinates only (Section 3.1), which is a departure from all-atom baselines like Vina and Gnina. The paper explains that "our scalar fields only indirectly depend on the sidechains via residue-level coefficients" — but this is a post-hoc explanation, not an ablation. An experiment adding sidechain atoms (or at least sidechain centroids) to the protein scalar field would clarify whether the robustness on predicted structures is a feature of the scalar-field approach or merely a consequence of ignoring noisy sidechains. **Why it matters:** The comparison to Vina/Gnina on crystal structures is asymmetric: baselines use all atoms while ESF uses only alpha-carbons. An ablation would show whether this gap is intrinsic to the method or fixable.

### Trivial
None.

## Nice-to-Haves

- A direct measurement of the local-to-global projection error (e.g., field reconstruction error on a held-out grid) would resolve the main uncertainty about the rotational FFT.
- Reporting the number of angular/radial basis functions ($\ell_{\max}$, $N_{\text{global}}$, $N_{\text{local}}$, $N_{\text{grid}}$) and the rotational sampling resolution would aid reproducibility.
- A harder decoy set (e.g., generated by docking other ligands or systematic scanning) would provide a more stringent test of discriminative power.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that the decoy set is too easy (median closest decoy 0.4 Å).** Removed because the reviewer misunderstands the task: having decoys very close to native (0.4 Å median) makes fine-grained pose discrimination harder, not easier. The AUROC threshold at 2 Å measures the ability to separate near-native from clearly wrong poses, not coarse ranking.

2. **Criticism about TF vs RF being "inconsistent."** Removed because similar performance across two different optimization modes is evidence of robustness, not inconsistency. The paper transparently reports both and notes TS outperforms RS for a known reason (coarser global expansion).

3. **Criticism about the "amortized" terminology being non-standard.** Removed because the paper's usage — precomputations done once per protein and reused across ligands — is standard and clearly defined. The paper describes exactly what is being amortized and at what levels.

4. **Criticism about missing grid resolutions, RBF details, and hyperparameters.** Removed per rule: the appendix (which the parser strips from these review materials) likely contains these details. The parser-stripped content cannot be verified as absent from the original submission.

5. **Criticism about the training objective lacking any empirical check.** Weakened from "there is no empirical check" to the more accurate statement above. The paper's entire experimental section (Tables 1–2) is an empirical check of the scoring function, which implicitly validates the training objective. The remaining concern is that a more targeted ablation is missing.

6. **Portion of the alpha-carbon criticism claiming "unfair comparison."** Removed per rule: the asymmetry in this comparison favors the baselines (Vina/Gnina use all atoms), not the author's method. The authors are intentionally operating at a disadvantage to prove a stronger point about robustness. The underlying concern about the design choice not being ablated is retained as a minor weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one insight not fully developed in the paper: the relationship between the spatial resolution of the scalar field representation and the tradeoff between accuracy and speed is the central lever of the method. The paper shows that TS (Cartesian grid) outperforms RS (global spherical harmonic expansion) on all metrics, confirming that the local-to-global projection sacrifices fidelity. But this same projection is what enables the rotational FFT and the major amortization gains. A systematic characterization of this resolution–speed Pareto frontier — varying the number of global basis functions and measuring both projection error and runtime — would be a natural extension that could turn the rotational FFT from a "plausible but uncharacterized" component into a principled one.

## Suggestions

1. **Characterize the projection error.** Compute the RMSD between the exact scalar field (Eq. 3) and the projected field (Eq. 7) on a held-out grid of points as a function of $N_{\text{global}}$ and $\ell_{\max}$. Correlate this error with the gap between TF and RF/RF docking performance to establish whether the projection is the bottleneck.

2. **Add an ablation of the training objective.** Train the same architecture with a hinge loss that directly maximizes the score margin between the true pose and random perturbations. If performance matches the conditional-likelihood objective, the simpler loss suffices; if not, the complexity is justified.

3. **Report error bars.** Add interquartile ranges or bootstrap confidence intervals for the main metrics in Tables 1 and 2. This would allow readers to assess the significance of the differences between methods.

4. **Report ESMFold vs crystal backbone RMSD.** This simple statistic would contextualize the robustness claims and help readers understand at what level of structure degradation the method's advantage manifests.

## Score and Decision

The paper presents a genuinely novel approach to ML-accelerated molecular docking, with a clean theoretical foundation, strong empirical results on predicted structures, and a clear runtime advantage demonstrated through amortization. The three weaknesses identified are real but none are fatal: the rotational FFT approximation is acknowledged by the authors and partially evidenced by TS vs RS comparisons; the training objective is validated by the overall experimental results; and the alpha-carbon design choice is defensible with the provided rationale. The paper would benefit from additional quantification and ablations, but its core contribution — learning cross-correlation-based scoring functions for FFT-accelerated docking — is sound and valuable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>