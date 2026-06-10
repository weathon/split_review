## Summary

Manifold Diffusion Fields (MDF) extends diffusion-based generative modeling of continuous functions from Euclidean domains to Riemannian manifolds by replacing the standard Fourier positional encoding used in DPF (Diffusion Probabilistic Fields) with eigenfunctions of the Laplace-Beltrami Operator (LBO). The resulting model learns distributions over fields \(f: \mathcal{M} \to \mathcal{Y}\) without requiring access to an analytical Riemannian metric, working instead with discrete approximations (meshes, graphs, pointclouds). MDF is evaluated on three fixed-manifold settings (wave, bunny, human) with increasing curvature, on the sphere (ERA5 climate), and on molecular conformer generation (GEOM-QM9), where it matches or beats domain-specific methods without using geometric inductive biases.

## Strengths

- **Invariance to rigid and isometric transformations, convincingly demonstrated.** The paper provides striking empirical evidence (Table 4, lines 226–238): training MDF on one manifold \(\mathcal{M}\) and evaluating on an isometric transformation \(\mathcal{M}_{\text{iso}}\) yields COV = 0.595, identical to the same-manifold setting, while the ambient-space baseline DPF collapses from 0.547 to 0.003. This cleanly isolates the advantage of an intrinsic coordinate system over an extrinsic one and is the paper's single strongest piece of evidence.

- **Competitive molecular conformer results without domain-specific inductive biases.** On GEOM-QM9 (Table 5, lines 333–355), MDF matches or surpasses specialized methods (Torsional Diffusion, GeoMol) that explicitly model torsional angles and bond geometry. MDF achieves Recall AMR mean = 0.124 (vs. 0.178 for Torsional Diffusion) and Precision AMR mean = 0.169 (vs. 0.221 for Torsional Diffusion) while making no geometric assumptions about molecular structure — a meaningful demonstration that a general manifold-function generative model can compete with heavily engineered approaches on a real scientific task.

- **Robustness across different Laplacian discretizations.** The paper tests MDF with graph, cotangent, and pointcloud Laplacians on the same manifold (Table 6, lines 296–310). Performance varies only modestly (e.g., COV for GMM ranges from 0.575 to 0.588; for MNIST from 0.551 to 0.571), confirming the method is not brittle to how the LBO is computed — important for practical deployment across meshes, graphs, and pointclouds.

- **Architecture-agnostic formulation.** Three different score-network architectures (PerceiverIO, Transformer Encoder-Decoder, MLP-mixer) achieve similar COV/MMD under matched parameter counts (Table 7, lines 1007–1023), confirming that gains come from the intrinsic coordinate representation rather than a specific architectural choice.

## Weaknesses

### Major

- **No statistical significance reported for close comparisons, where it matters.** None of the main results in Tables 1–3 include confidence intervals or error bars. This is a genuine gap because several comparisons are close or mixed. On the wave manifold (lowest curvature), DPF achieves better GMM MMD (0.01339 vs. 0.01405) and better CelebA-HQ COV (0.361 vs. 0.354). While the paper acknowledges MDF "tends to outperform" DPF and the pattern becomes systematic as curvature increases, without variance estimates the reader cannot assess whether the wave-manifold results reflect genuine limitations or statistical noise. The only variance reported in the paper (Appendix A.6.1, line 1043, three seeds on bunny GMM at coarse resolution) shows MMD = 0.00843 ± 0.00372 — a coefficient of variation of ~44%. If similar variance applies to the main tables, several close comparisons could be statistically indistinguishable. This weakens the headline claims.

### Minor

- **The k=2 molecular conformer ablation raises unexplained questions.** In Table 5, MDF with just \(k=2\) eigenfunctions achieves Precision AMR mean = 0.211 (median = 0.138), which is *better* than \(k=16\) (0.220, 0.151) and competitive with \(k=28\) (0.169, 0.101) on precision. Recall coverage is essentially flat from \(k=2\) through \(k=28\) (~93–95%). This non-monotonic behavior is surprising — molecules with 10–40 atoms would seem to require more than 2 eigenfunctions to distinguish atomic positions. The paper states "interestingly, with as few as \(k=2\) eigenfunctions MDF is able to generate consistent accurate conformations" (line 354) but does not analyze why, nor whether the model is exploiting a shortcut (e.g., that most conformers cluster around a limited set of geometries distinguishable with very coarse coordinates). This matters because if MDF is not actually leveraging the manifold structure for conformers, the argument that the method works *because of* its intrinsic coordinate system is weaker than claimed.

- **PDE conditional inference demonstration is thin.** The PDE experiment (Appendix A.7, lines 1129–1148) uses a single PDE (heat equation), a single manifold (bunny at 602 vertices), a single diffusivity value, and reports MSE = 4.77e-3 without any baselines. The paper correctly frames this as a demonstration, but it does not provide evidence of generalizability. This limits the strength of the claim (line 27) that "Results on climate modeling datasets and PDE problems show the practicality of MDF in scientific domains."

- **Novelty relative to DPF is modest, though honestly presented.** The paper transparently inherits the context/query set formulation, the denoising loss, the ancestral sampling scheme, and the PerceiverIO-based score network from DPF (line 75). The core methodological change is the substitution of LBO eigenfunctions for Fourier positional encodings. This substitution is principled and consequential, as the experiments show, but the paper's framing (e.g., "first principled approach") should be read as a generalization of an existing framework to a new domain rather than a fundamentally new generative paradigm. This is an honest characterization of the contribution's scope rather than a flaw.

### Trivial

- **Context set sampling fraction not specified.** Algorithm 2 states the context set is a "random subset" of the query set but does not specify the size or fraction. The hyperparameter table (Table 8) lists context/query sizes as "variable" for GEOM-QM9 without further detail. This is a minor clarity issue.

## Nice-to-Haves

- A controlled ablation comparing MDF with LBO eigenfunctions vs. MDF with ambient Fourier features (within the same architecture) would isolate the effect of the coordinate system more cleanly than comparing against a separate DPF implementation.
- Reporting training costs of baselines (DPF, GASP) under the same setup would contextualize whether MDF's gains come at a higher computational price.
- The ERA5/sphere experiment could be strengthened by also comparing to DPF, since the sphere is a tractable special case.
- Analysis of why \(k=2\) suffices for molecular conformers would remove a puzzling loose end.

## Removed Points

- **"Missing related works (neural processes)"**: The paper explicitly discusses neural processes (line 41). Also, the instructions forbid mentioning missing related works.
- **"Asymmetric DPF comparison is unfair"**: The comparison is between intrinsic vs. extrinsic coordinates — which is the paper's thesis. The paper equates hyperparameters between methods and the comparison is properly scoped. The framing does not overstate the findings.
- **"LBO sign ambiguity deserves more discussion"**: The paper already acknowledges this limitation (line 1080) and reports that it was not an issue empirically. The criticism adds no new information.
- **"ERA5 is a missed opportunity for broader evaluation"**: The paper compares to GASP, the relevant baseline for this dataset. Scope creep.
- **Generic formatting/style criticisms** (not present in the critic but removed per instructions).

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface concerns about statistical rigor and the unexplained \(k=2\) conformer behavior that the paper should address, but do not introduce a fundamentally new lens on the work.

## Suggestions

1. **Add confidence intervals or error bars** to the main results in Tables 1–3. At minimum, report results across multiple seeds for the close comparisons (wave manifold). This is the most impactful improvement the authors could make.
2. **Analyze the \(k=2\) conformer result.** Provide an explanation (or additional analysis) for why very few eigenfunctions suffice for molecular conformers, to rule out the possibility that the model is learning a shortcut rather than leveraging manifold structure.
3. **Add a within-architecture ablation**: compare MDF with LBO eigenfunctions vs. MDF with ambient Fourier features using the same architecture and hyperparameters, to isolate the contribution of the coordinate system.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>