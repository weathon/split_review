Now I have a comprehensive understanding of the paper and the calibration landscape. Let me write the final consolidated review.

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison to SIGMADOCK |
|--------|------|-----------|-------|------------------------|
| VFDiff | /home/wg25r/split_review/datasets/deepreview_13k_calibration/5YLsnsjgeC.md | 6.0 | 1,2 | Rejected for being too similar to IPDiff. SIGMADOCK has much stronger novelty and evaluation. |
| DiffDock-Pocket | /home/wg25r/split_review/datasets/deepreview_13k_calibration/1IaoWBqB6K.md | 5.0 | 2 | Incremental DiffDock extension. SIGMADOCK more novel with stronger results. |
| IPDiff | /home/wg25r/split_review/datasets/deepreview_13k_calibration/qH9nrMNTIW.md | 6.25 | 2 | Accepted but limited to CrossDocked2020. SIGMADOCK evaluates on PoseBusters + Astex with richer analysis. |
| GroupBind | /home/wg25r/split_review/datasets/deepreview_13k_calibration/zDC3iCBxJb.md | 6.75 | 2 | Accepted, novel idea but no PoseBusters evaluation. SIGMADOCK has stronger evaluation. |
| FABFlex | /home/wg25r/split_review/datasets/deepreview_13k_calibration/iezDdA9oeB.md | 7.0 | 2 | Accepted, regression-based approach, criticized as incremental over FABind. SIGMADOCK more novel. |
| ShEPhERD | /home/wg25r/split_review/datasets/deepreview_13k_calibration/KSLkFYHlYg.md | 8.0 | 1 | Accepted, SE(3)-equivariant diffusion for bioisosteric design. Different task, comparable quality. |
| FlexDock | /home/wg25r/split_review/datasets/deepreview_13k_calibration/gHLWTzKiZV.md | 8.0 | 1,2 | Accepted, strong UF Matching theory, 73% PB-valid. SIGMADOCK achieves 79.9% with rigid docking. |

**Final bracket**: SIGMADOCK clearly above 6.0 and comparable to 7.0-8.0 papers. Score: **7.5**.


## Summary

SIGMADOCK introduces a fragment-based SE(3) diffusion model for molecular docking. The key idea is to decompose ligands into rigid molecular fragments (by breaking rotatable bonds), then define a diffusion process over SE(3) transformations of each fragment. The paper contributes a fragmentation reduction scheme (FR3D), soft triangulation constraints to preserve bond geometry across fragments, and an EquiformerV2-based architecture adapted for fragment reasoning. Empirically, SIGMADOCK achieves 79.9% Top-1 PB-valid on PoseBusters, substantially surpassing prior deep learning methods (DiffDock: 38.0%) and matching AlphaFold3-level performance with far less training data and compute.

## Strengths

1. **State-of-the-art empirical results on rigorous benchmarks.** Figure 4 (left) reports 79.9% Top-1 PB-valid on PoseBusters and 90.6% on Astex under the standard PB train-test split. This is a 6.3× improvement over DiffDock (38.0%) and, as the paper documents, the first deep learning method to surpass classical physics-based docking on this split. These results are credible and well-documented.

2. **Genuine generalization demonstrated, not memorization.** Figure 4 (right) shows Top-1 PB-valid rates of 51% for proteins with ≤0% sequence similarity, 53% for 30-95%, and 53% for 95-100%. The flat performance across similarity splits, combined with the co-factor analysis (Table 2: 84.2% RMSD<2 on complexes with no co-factors vs. 58.8% on natural ligands), provides strong evidence that the model learns physicochemical principles rather than memorizing training complexes.

3. **Well-structured ablation study isolating key components.** Table 1 shows that removing triangulation conditioning drops PB-valid from 79.9% to 67.1%, removing fragment merging drops it to 73.7%, and removing protein-ligand interactions drops it to 76.3%. These controlled experiments (configurations A-C are retrained from scratch) convincingly demonstrate the contribution of each proposed inductive bias.

4. **Theoretical grounding for the fragment-based approach.** Theorem 1 identifies that torsional models produce non-product induced measures in Cartesian space while fragment models factorize. Theorem 2 proves invariance to local coordinate orientation choice — a non-trivial technical issue resolved via Newton-Euler equations. These theoretical contributions, while compactly stated, genuinely motivate the design.

5. **Data efficiency relative to co-folding methods.** Table 4 shows SIGMADOCK achieves 79.9% avg PB-valid vs. 80.2% for AF3, while training on only ~19k complexes (PDBBind v2020) versus AF3's substantially larger and more diverse dataset, with 50× faster sampling and lower train-test leakage (Appendix J). This is a meaningful demonstration of principled inductive biases reducing the need for scale.

6. **Robustness to pocket definition.** Table 3 shows performance remains stable (80.5%→77.3% PB-valid) when increasing pocket diameter from 5Å to 6Å, and only drops to 68.2% at 7Å (outside training support of mean 5Å + σ=1Å). This addresses a practical concern for real-world deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim that fragment-based diffusion is superior to torsional diffusion is not tested in a controlled manner.** The paper motivates its method as solving known problems of torsional models (ill-conditioned learning, non-product induced measures), but then compares against DiffDock — a torsional model with a different architecture, training data, and inference pipeline. No ablation replaces the fragment parametrization with a torsional parametrization while keeping the EquiformerV2 backbone, training set, and ranking heuristic fixed. Without this control, the large gains (79.9% vs. 38.0%) cannot be definitively attributed to the fragment formulation rather than to architecture improvements, the ranking heuristic, or data augmentation. The ablation study (Table 1) isolates the contribution of triangulation, merging, and PL interactions, but none of these directly tests the core fragment-vs-torsion hypothesis. This does not invalidate the paper's results — the SIGMADOCK system clearly works well — but it leaves the primary methodological argument partially unsubstantiated.

### Minor

2. **The ranking heuristic used to select the best pose from 40 seeds is underspecified.** Section 2.5 states: "evaluating both the (pseudo) binding energy of the generated protein-ligand system, as well as a set of physicochemical checks (such as, bond angles, bond lengths, internal energy)." The nature of the "pseudo binding energy" is not described — whether it is a classical scoring function (e.g., Vina), a learned model, or another form. The ablation (Table 1: "(-) Energy Scoring" drops from 79.9% to 66.1%) shows the heuristic is critical to the headline result. Details likely reside in the stripped appendix, but the main text is insufficient for independent assessment. The paper would benefit from a clear statement of the exact energy function and checks used.

3. **No error bars or uncertainty quantification on any reported metric.** All success rates in Figure 4 and Tables 1-4 are point estimates. Given the stochastic diffusion process and the use of 40 seeds per complex, there is likely variance across different random seeds or training runs. While single-run evaluation is standard practice in this field, the absence of any uncertainty measure makes it impossible to assess whether differences in ablations (e.g., 67.1% vs. 73.7%) are meaningful or noise. This is a replicability concern for the ablation comparisons specifically.

4. **The theoretical motivation (Theorem 1) is stated but not connected to empirical evidence of improved learnability.** Theorem 1 argues that torsional models produce "highly entangled, non-product induced measures" while fragment models yield product measures. This is an intuitive geometric claim, but the paper does not empirically validate that this translates to easier learning — e.g., via training loss curves, gradient norm comparisons, or sample quality as a function of ligand flexibility. The theory remains motivational rather than explanatory of the observed gains.

### Trivial
- The paper claims "50× faster sampling than AF3" but does not provide a runtime comparison against DiffDock or other deep learning docking methods, which are the more direct competitors on the re-docking task.

## Nice-to-Haves

- A controlled experiment replacing the fragment parametrization with a torsional parametrization (SE(3) + torsional angles) within the same architecture, training data, and ranking heuristic would cleanly test the paper's central hypothesis. Implementing this is substantial engineering but would significantly strengthen the contribution.
- Reporting training/inference wall-clock times compared to DiffDock and other re-docking baselines would substantiate efficiency claims.
- Providing confidence intervals (e.g., bootstrap over the test set or multiple training seeds) on the main numbers would improve scientific rigor.

## Removed Points

- **"Theorem 1 is not formally stated or proved in main text"**: Stating a theorem in the main text and providing its proof in the appendix (Appendix C.2) is standard practice at ICLR. This is not a weakness.
- **"Comparison to physics-based methods is under-contextualised (Vina tuning)"**: The paper systematically analyzes Vina with multiple pocket definitions (Table 3, showing 57.2% vs. 56.0% with different autobox settings). This adequately addresses the concern.
- **"PDBBind is not a docking method"**: The critic misreads the figure — PDBBind entries are used as a baseline representing "just use the crystallographic training pose" which is standard in the docking literature. Not a valid criticism.
- **"Runtime comparison needed against DiffDock"**: The paper explicitly claims "50× faster than AF3" (a co-folding competitor), not against DiffDock. The critic extrapolated an unwarranted claim.
- **"Missing related works"**: Cannot be verified without external sources.
- **"Pure formatting/style nitpicks"** and **"typos/grammar"**: These are parser artifacts, not author errors.
- **"Co-factor subsets show 41.2% failure rate"**: The paper acknowledges this limitation and correctly attributes it to the model deliberately excluding co-factors. This is honest reporting, not a weakness.

## Novel Insights

The reviews collectively surface one important observation not fully articulated in the paper: the ablation "G: Sampling from M_b" achieves 86.4% RMSD<2 (Table 1), which is substantially higher than the default 80.5%. This suggests that a significant portion of the remaining error stems from the conformer initialization (RDKit ETKDGv3) rather than the diffusion model itself. This insight points to a clear improvement path: better conformer generators — even those trained on bound-state data — could directly improve SIGMADOCK's performance. The paper acknowledges this honestly but does not highlight the implication that the diffusion model's ceiling may be higher than the reported results suggest.

## Suggestions

1. Provide a clear specification of the ranking heuristic in the main paper (or a self-contained appendix section): what exact energy function is used, whether it requires any trained parameters, and exactly which physicochemical checks are applied. This is critical for reproducibility.
2. Add a controlled torsional ablation — even if it underperforms — to directly substantiate the central claim about fragment-based vs. torsional diffusion. This would be the single highest-leverage improvement.
3. Report bootstrapped confidence intervals on Top-1 success rates, at minimum for the ablation study, to give readers a sense of statistical significance.

## Score and Decision

**Round 1 bracket**: Initial bracketing placed SIGMADOCK between the weak band (~3.0) and the strong band (~8.0). The paper is clearly far above the 3.0-level (which contains rejected papers with generic or incremental contributions). Initial bracket: 5.0–8.0.

**Round 2 narrowing**: Compared against DiffDock-Pocket (5.0, rejected — incremental), IPDiff (6.25, accepted — limited benchmarks), GroupBind (6.75, accepted — no PoseBusters), VFDiff (6.0, rejected — insufficient novelty), FABFlex (7.0, accepted — incremental over FABind), and FlexDock (8.0, accepted — strong theory). SIGMADOCK is clearly more novel than the 5.0–6.0 papers and has stronger evaluation than several accepted papers in the 6.25–7.0 range. Its evaluation depth (PoseBusters + Astex + co-factor + pocket sensitivity + AF3 comparison) exceeds that of most comparable works. The weaknesses (missing controlled torsional ablation, underspecified ranking heuristic) are real but not fatal — they do not undermine the empirical results. The paper is comparable to FlexDock (8.0) and ShEPhERD (8.0) in overall quality but has somewhat more substantial weaknesses than those top papers.

**Final score**: 7.5.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>