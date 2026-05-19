- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8
Now I have all the information needed to write the final consolidated review.

## Summary

This paper introduces a novel approach to molecular docking scoring functions: learning the score as a cross-correlation of SE(3)-equivariant scalar fields (parametrized by E3NNs) so that fast Fourier transforms can exhaustively evaluate rigid-body poses. The core technical contributions are the equivariant scalar field network (ESF) architecture, closed-form Fourier-space evaluation of the fields, a local-to-global spherical harmonic conversion enabling rotational FFTs, and a training objective using conditional log-likelihoods with tractable FFT-based marginalization. Experiments on decoy scoring and rigid conformer docking show competitive accuracy on PDBBind crystal structures, stronger robustness on ESMFold-predicted structures, and substantial runtime speedups in the amortized multi-ligand (PDE10A) setting (45× total inference speedup).

## Strengths

- **First learned scoring function with a cross-correlation functional form enabling FFT-accelerated pose optimization.** The paper defines the score as a cross-correlation of multi-channel protein and ligand scalar fields (Equation 1), which via the convolution theorem allows exhaustive evaluation of translations via FFT (Section 3.2) and rotations via spherical harmonic convolution (Section 3.3). Per-pose scoring reaches 1.0 μs — orders of magnitude below Vina (3.4 ms) and Gnina (13.0 ms) — as shown in the decoy scoring table and the "Typical runtimes" table.

- **Rigorous equivariance guarantees.** Proposition 1 (Section 3.1) proves that if the expansion coefficients transform under Wigner D-matrices, the field is SE(3)-equivariant and the scoring function is invariant. This property is what allows all poses to be evaluated from a single network forward pass, which is essential to the FFT procedures. The ESF architecture achieves 47% success rate (<2 Å RMSD) on ESMFold rigid conformer docking, nearly doubling the 24–28% of Vina and Gnina (docking table).

- **Tractable training objective via FFT-marginalized conditional likelihoods.** Section 3.4 decomposes the pose into conformer, rotation, and translation, then optimizes conditional log-likelihoods (Equations 15–16) where the normalizing integrals are exactly the cross-correlations computable by FFTs. This clever design avoids the intractable partition function while training the model to produce well-calibrated scoring landscapes.

- **Demonstrated amortization benefit on a realistic virtual-screening proxy.** On the PDE10A dataset (77 ligands binding the same pocket), ESF-RF achieves a 45× total runtime speedup (67 s → 1.5 s per complex after protein-level precomputation amortization) while maintaining accuracy comparable to Vina and Gnina (73% vs 74% success rate). The paper also provides a clear taxonomy of four inference modes (TF, RF, TS, RS) with a detailed runtime breakdown table, which is valuable for practitioners.

## Weaknesses

### Fatal

None.

### Major

- **The abstract's "similar but faster" claim is imprecise and overreaches.** The abstract states "Our method attains similar but faster performance on crystal structures compared to the widely-used Vina and Gnina scoring functions." On the PDBBind rigid conformer docking task, ESF variants achieve 70–73% success (<2 Å RMSD) vs 77–79% for Vina and Gnina — slightly worse, not "similar" on an absolute basis. More importantly, the total runtime per complex including precomputations is 67–68 s for ESF-RF compared to 20 s for Vina — **three times slower**, not faster. The speed advantage is real only for per-pose scoring (1.0 μs vs 3.4 ms) or in amortized multi-ligand settings (PDE10A). The paper honestly acknowledges this in the body ("the total runtime is comparable to or slower than the baselines when precomputations are taken into account," line 232), but the abstract and introduction frame the result without these essential qualifications, which is misleading for readers evaluating single-complex docking.

- **The rotational FFT approximation (local-to-global spherical harmonic conversion) is not characterized.** The conversion in Equation 12 is a least-squares approximation with no fidelity analysis. The paper does not report the number of global radial/angular basis functions used, the discretization resolution for precomputing the local-to-global mapping, or the typical reconstruction error. Since the rotational variants (RS, RF) consistently underperform the Cartesian variants (TS, TF) across multiple metrics (Table 1: AUROC 0.87 vs 0.92; Table 2: docking success 71–73% vs 70–72%), the paper attributes this to a "spatially coarser representation" (line 223) without evidence. This gap prevents the reader from distinguishing between fundamental limits of the global basis expansion and correctable implementation choices, weakening the contribution of the rotational FFT workflow — which is the most interesting for virtual screening amortization.

### Minor

- **Missing architectural and hyperparameter details.** The paper does not report the number of radial basis functions $R_j$, the maximum $\ell$ (spherical harmonic band limit), the number of channels $c$, the E3NN depth/width, or training hyperparameters (learning rate, batch size, number of epochs). These details are essential for reproducibility and for understanding the computational-accuracy tradeoffs of the method. A dedicated appendix or subsection is expected; the main text should at minimum summarize the ranges.

- **No statistical significance reported for key comparisons.** The docking success rate differences between ESF and Vina/Gnina (e.g., 73% vs 79% on PDBBind crystal, 47% vs 24–28% on ESMFold) are presented as point estimates without confidence intervals or hypothesis tests. The ESMFold result is large enough to be credible, but the crystal result may or may not be significant with the test set size.

- **No ablation isolating the effect of noise augmentation.** ESF-N (trained with noise) substantially improves ESMFold docking (47% vs 32% for ESF). It is unclear whether this is specifically due to the noise or whether other regularizers (e.g., dropout) would achieve similar gains. An ablation would strengthen the claim that noise is the key factor.

- **The training objective (sum of conditional log-likelihoods for translation and rotation) is not justified** beyond stating "we find that these objectives work well in practice" (line 133). Given that neither conditional likelihood equals the joint likelihood, and that the choice could affect the learned scoring landscape, some analysis or ablation would be helpful.

### Trivial

None.

## Nice-to-Haves

- **Add a scaling experiment on the PDE10A dataset** showing total runtime per complex as the number of ligands is progressively increased (e.g., 1, 10, 100). This would directly demonstrate the amortization curve and give concrete evidence for the claim about large-scale screening, beyond the single 77-ligand data point.
- **Characterize the rotational FFT approximation error** with reconstruction RMSE as a function of the number of global basis functions, number of atoms, and grid extent. An ablation varying the number of global spherical harmonics would clarify whether the RS/RF performance gap is fundamental or fixable.
- **Include the per-complex runtime in the decoy scoring discussion more prominently.** The current per-complex times (ESF-TS: 3.2 s vs Vina: 110 s) are actually more impressive for practical use than the per-pose times and could be featured earlier.

## Removed Points

*These points were flagged for removal; treat them with caution if referenced.*

- **"Decoy generation produces an easy task because most poses are far from native"** — The paper reports a median closest-decoy RMSD of 0.4 Å, which indicates dense sampling near the native pose. The task provides a valid discrimination signal and is not trivially easy.
- **"Table caption garbled ('0.5–0')"** — This is a PDF-to-text parser artifact in the extracted version; the original submission does not have this issue. Removed per formatting/parser artifact rules.
- **"Only 77 ligands on PDE10A; extrapolation to billion-compound libraries is speculative"** — The paper frames this as "could make docking feasible" — appropriately modest language. The dataset is explicitly described as an industrially-sourced proof-of-concept.
- **"Missing comparison to other learning-based FFT docking methods (Padhorny et al., Ding et al.)"** — The paper discusses these works in the Background section (lines 45–47) and correctly positions the gap. A quantitative comparison would require reimplementing those protein–protein methods for the protein–ligand setting, which is outside stated scope.
- **"Per-complex runtime should be featured more prominently"** — The decoy scoring table already includes per-complex runtime (3.2 s vs 110 s). This information is already present in the paper.
- **"Third contribution is vague"** — Minor presentation issue; contribution lists in introduction sections often contain framing language.

## Novel Insights

None beyond the paper's own contributions. The key novel observation — that learning cross-correlation-based scoring functions enables FFT acceleration — is the paper's own central thesis, not something synthesized from the reviews.

## Suggestions

1. **Revise the abstract and conclusion** to qualify the "similar but faster" claim. Replace the blanket statement with something like: "On decoy scoring and amortized multi-ligand docking, our method achieves competitive accuracy with substantial speedups (per-pose: 1 μs vs 3.4 ms for Vina; per-complex on PDE10A: 1.5 s vs 6.1 s). On single-complex PDBBind docking, our method is slightly less accurate (73% vs 79%) and slower in total runtime (67 s vs 20 s) but offers much faster per-optimization-step evaluation (0.5 s vs 20 s)."

2. **Characterize the rotational FFT approximation** by reporting the number of global basis functions, discretization resolution, and reconstruction error. Add an ablation varying the maximum spherical harmonic band limit to separate fundamental from implementation-driven performance gaps.

3. **Report missing architectural details** (number of radial basis functions, maximum ℓ, channel count, E3NN depth/width, training hyperparameters) either in the main text or by noting that they are in the (presumed present) appendix.

4. **Add confidence intervals or bootstrap estimates** for the main comparisons in the decoy scoring and docking tables, especially where ESF and baseline accuracies are close.

5. **Include an ablation** isolating the noise augmentation effect (ESF-N vs ESF with other regularizers) to validate the claim that noise is the key driver of robustness gains.
