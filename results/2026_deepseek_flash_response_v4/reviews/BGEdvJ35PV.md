## Summary

This paper proposes DIST, a plug-in corrective sampling module for diffusion-based 3D molecular generation. The core insight is that molecular data distributions exhibit a "dense-concentrated structure" (DC-structure) — narrow, densely packed probability peaks separated by near-zero-density regions — which makes standard reverse inference fragile because small denoising errors can overshoot valid peaks. DIST mitigates this by, at an intermediate timestep, evaluating batches of candidate trajectories via a pilot scoring mechanism, discarding those that have drifted off-distribution, and continuing reverse inference only from retained samples. Experiments on QM9 and GEOM-Drugs with three backbone models (EDM, GeoLDM, RADM) show consistent quality improvements.

## Strengths

1. **Formal characterization of molecular distribution geometry (Definition 3.1, Equations 6–7):** The paper provides a precise mathematical definition of DC-structure as a mixture of narrow Gaussian peaks with separation constraints, and derives an explicit overshoot condition (β\_t·Δ/σ\_\*² > cσ\_\*) linking the narrowness of molecular peaks to the fragility of reverse inference. This goes beyond qualitative descriptions in prior work and yields a testable prediction.

2. **Consistent and substantial empirical gains across diverse backbone architectures (Table 2):** DIST improves molecule stability on QM9 by +7.9 pp (EDM: 82.0%→89.9%), +4.0 pp (GeoLDM: 89.4%→93.4%), and +4.1 pp (RADM: 87.3%→91.4%) with standard deviations reported over three runs. The gains hold across GNN-based equivariant, Transformer-based non-equivariant, and latent-space models, supporting the claim that DC-structure issues are cross-architectural.

3. **Theoretical framework for corrective sampling (Corollary 3.1, Proposition 3.1):** The TV-contraction bound formally justifies that improving the intermediate distribution q\_t directly improves the final distribution q\_0. The Selective Reverse Error Bound provides a theoretical guarantee that the corrected distribution q\_t^c converges toward p\_t under the DC-structure assumptions.

4. **Ablation providing practical guidance (Table 4):** Systematic variation of pilot subset sizes (30, 50, 100) shows monotonic quality gains with budget, with strong performance even at the smallest budget (99.2% Atom Sta, 89.5% Mol Sta), giving practitioners a concrete efficiency-quality trade-off.

## Weaknesses

### Fatal

None.

### Major

1. **The pilot scoring function s\_j is not specified in the main text.** The paper defines DIST around a "model-side pilot score s\_j" (Eq. 9, line 150) but only lists examples (round-trip residual, self-consistency, ensemble variance, chemistry-based penalty) without stating which was actually used in any experiment. Since s\_j is the core of the filtering mechanism, this makes the method irreproducible from the main text and prevents the reader from interpreting what the ablations in Tables 3–4 actually mean (Are improvements from filtering invalid geometries? From selecting chemically valid fragments? From an oracle validity check?). The paper references Appendix F for detailed settings, but the main text should at minimum identify the scoring function type.

2. **The efficiency claim in the main text is misleading because it excludes pilot costs.** The formula in Section 4.3 (line 221) — (T−t)/|B| + t — counts only the parallelized batch steps from T to t plus the remaining steps for accepted trajectories. It does not account for the cost of running full reverse inference on pilot subsets from each batch (described in Section 3.2). With pilot size 50 per batch and moderate rejection rates, the pilots could add substantial overhead. The paper references Appendix G.1 for detailed quantification, but the main text's "nearly half the standard number of timesteps" claim (Abstract, Section 4.3) is presented without caveats, creating an unsupported impression of the true computational savings.

3. **Missing baselines that would isolate DIST's effect from extra compute.** The evaluation compares backbone vs. backbone+DIST. There is no comparison against: (a) the backbone with more sampling steps (e.g., 2000 steps), (b) the backbone with rejection sampling on final molecules, or (c) DIST with a random (non-informative) scoring function to show that the selection mechanism itself — not merely discarding samples — drives improvement. Without these, it is unclear how much of the gain comes from DIST's steering mechanism versus additional compute or simple filtering.

### Minor

1. **Corollary 3.1 is a standard contraction property of any Markov kernel.** The bound ‖q₀ − p₀‖\_TV ≤ κ ‖q\_t − p\_t‖\_TV holds for any ideal reverse kernel K\_{t→0} regardless of molecular structure. It correctly motivates why bringing q\_t closer to p\_t helps, but does not provide molecular-specific insight. The paper's more distinctive theoretical contribution is the overshoot analysis (Equations 6–7), not this corollary.

2. **The method description could clarify the role of pilots.** The paper states that pilots run "full reverse inference" from timestep t to 0 (line 176). Since the pilots generate complete molecules, a reader may wonder whether the correction genuinely alters remaining denoising steps or retroactively selects good pilot runs. (In fact, the main trajectories continue from t to 0 independently of the pilots, so the correction is genuine intermediate filtering.) A brief clarifying sentence would resolve this.

### Trivial

None.

## Nice-to-Haves

- Report total wall-clock time or total FLOPs for DIST vs. baselines, broken into pilot cost, batch inference cost, and filtering cost, rather than relying solely on the derived "average timestep" metric.
- Add a random-score ablation in Table 4 to demonstrate that DIST's selection mechanism adds value beyond simply discarding a fraction of batches.
- Show that the corrected intermediate distribution q\_t^c is measurably closer to p\_t than the uncorrected q\_t (e.g., via a validity classifier on intermediate states).

## Removed Points

These points from the inputs were removed with justification:

- **"Temporal ambiguity / retroactive selection" (Harsh Critic Critical Issue 4):** The paper's description is coherent — pilots assess quality via full reverse, then main trajectories of kept batches continue from t to 0. The correction is genuine intermediate filtering, not retroactive selection. A softened version is retained as Minor weakness 2.
- **"Table 1 criticism (starts from clean data):** The paper transparently describes the diagnostic setup (z\_t ~ p(z\_t|x)). The criticism misinterprets the table's purpose.
- **"DC-structure overlaps with prior work":** The paper acknowledges related work; the overlap claim is too vague without specific evidence.
- **"Definition 3.1 parameters not used quantitatively":** Factually incorrect — σ\_\* and Δ are used directly in the overshoot analysis (Equations 6–7).
- **Generic strengths from Strength Finder** (e.g., "paper addresses an important problem"): Removed per filtering rules. Only concrete, evidence-backed strengths retained.

## Novel Insights

The key tension across the reviews is between the paper's genuinely novel core (DC-structure formalization with a concrete overshoot condition, plus consistent cross-architecture empirical gains) and the incomplete presentation of the method's central mechanism (the scoring function) and an overclaimed efficiency benefit. Neither reviewer disputes the quality improvements; the debate is about reproducibility and attribution. The paper would benefit most from specifying s\_j, correcting the efficiency accounting, and adding the simplest baselines (random filter, more sampling steps) to pin down what DIST actually contributes. The comparison with "Correcting Flows with Marginal Matching" (5.25) is instructive — that paper proposed a similar inference-time correction idea but on images, and shared similar presentation and attribution weaknesses. DIST has stronger empirical grounding (3 backbones × 2 datasets, consistent gains) but worse specification of its core mechanism.

## Suggestions

1. Specify the scoring function s\_j used in all experiments directly in Section 3.2 or Section 4.1 — this is the single highest-leverage fix.
2. Revise the efficiency calculation to include pilot costs, or at minimum add a caveat in the main text that the reported timestep counts undercount total compute.
3. Add compute-matched baselines (more sampling steps, rejection sampling) to strengthen attribution of gains to DIST's mechanism rather than extra compute.
4. Add a clarifying sentence in Section 3.2 that main trajectories continue from t to 0 independently of the pilots (pilots are diagnostic only).

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DynamicsDiffusion | kKXIYUi8ff.md | 3.00 | R1 | Weaker — molecular dynamics generation, poorly motivated |
| Ligand Conformation | m9zWBn1Y2j.md | 3.00 | R1 | Weaker — different task, limited scope |
| TorSeq | G536mmC2HL.md | 3.00 | R1 | Weaker — torsion modeling, less ambitious |
| **Lift Your Molecules (SyCO)** | **uNomADvF3s.md** | **6.50** | **R1** | **Stronger — comprehensive, well-presented, minor evidence gaps** |
| **EQGAT-diff (Navigating Design)** | **kzGuiRXZrQ.md** | **5.75** | **R1** | **Similar — accepted, limited novelty but solid experiments; DIST has more novelty but worse reproducibility** |
| Subgraph Diffusion | 9g8h5HwZMy.md | 5.00 | R1 | Similar — rejected, some novelty but evaluation gaps |
| Megalodon (Modular Co-Design) | 9UoBuhVNh6.md | 6.33 | R1 | Stronger — SOTA transformer model, more comprehensive |
| Generator Matching | RuP17cJtZo.md | 8.00 | R1 | Stronger — broader impact, cleaner theory |
| Shortcut Models | OlzB6LnXcS.md | 8.00 | R1 | Stronger — one-step diffusion, broad applicability |

**Round 2 (Narrowing within bracket 4–6.5):**
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| **Correcting Flows with Marginal Matching** | **kRjLBXWn1T.md** | **5.25** | **R2** | **Similar — inference-time correction, comparable strength; DIST has stronger empirical grounding but worse method specification** |
| MoreRed (Molecule Relaxation) | rwmWd2rjP1.md | 4.75 | R2 | Weaker — questionable evaluation, limited generality |
| Dynamics-Informed Protein Design | jZPqf2G9Sw.md | 5.50 | R2 | Similar — novel conditioning approach, modest gains |
| Improved Order Analysis (EI) | 90QOM1xB88.md | 5.00 | R2 | Similar — niche contribution, mixed reviews |
| E(3) chirality | mXHTifc1Fn.md | 6.75 | R2 | Stronger — clear theoretical result, well-received |
| DiffCSP++ (Crystal Generation) | jkvZ7v4OmP.md | 7.33 | R2 | Stronger — cleaner method, better presentation |

**Bracket established in Round 1:** 4–6.5

**Narrowing in Round 2:** Comparison with "Correcting Flows with Marginal Matching" (5.25) and EQGAT-diff (5.75) anchors the paper near the 5.0–5.5 range. The paper has genuine novelty (DC-structure + overshoot analysis) and strong empirical consistency (3 backbones, 2 datasets), but is held back by the unspecified scoring function (reproducibility gap) and misleading efficiency claim. It is weaker than SyCO (6.50) and the E(3) chirality paper (6.75) due to these gaps, but stronger than MoreRed (4.75) and comparable to Correcting Flows (5.25) and EQGAT-diff (5.75). Given the fixable nature of the major weaknesses but their current presence, the paper sits at the lower end of the comparable range.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>