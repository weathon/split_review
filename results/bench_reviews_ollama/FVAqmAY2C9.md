## Summary
The paper proposes Gaussian Earth Mover's Distance (GEMD) for few-shot learning, replacing DeepEMD's costly LP-based discrete EMD with the closed-form Wasserstein-2 distance between Gaussian feature descriptors. Two variants are presented: a metric-based GEMD-M that uses the closed-form Bures–Wasserstein distance for nearest-neighbor classification, and a transfer-learning GEMD-T that introduces a parametric EMD via learnable orthogonal matrices, implementable as an FC layer + softmax. Experiments on Meta-Dataset and three smaller benchmarks claim 2.3%/1.3% gains over prior SOTA in SDL/MDL settings and ~6× speedups over DeepEMD.

## Strengths
- **Closed-form Gaussian EMD as a principled drop-in for DeepEMD's LP.** Prop. 1 / Eq. (4) replaces QPTH/Sinkhorn with a closed-form distance, and Tab. 3e cleanly establishes the speed/accuracy trade-off (GEMD-T is ~6× faster than DeepEMD with materially higher accuracy under matched backbones).
- **Well-isolated improvement over the KL-Gaussian baseline (ADM).** Under matched pre-training, GEMD-M improves over ADM in both Tabs. 1 and 2, supporting Wasserstein over KL for Gaussian descriptors in FSL — this is a meaningful, scope-appropriate result.
- **Practical, GPU-friendly implementation.** Newton–Schulz for matrix square roots and the retraction-free landing algorithm for orthogonal updates are reasonable choices, and the ablations on iteration count $r$ (Tab. 3b) and feature dim $p$ (Tab. 3a) give the reader actionable knobs.

## Weaknesses

### Fatal
None — the GEMD-M contribution stands on its own merits even if other claims weaken.

### Major
- **GEMD-T's claim to be a "parametric EMD" is not supported by the math in Eq. (8).** Prop. 2 expresses Wasserstein-2 as a minimization over orthogonal $U$ of $\|\Sigma_X^{1/2}U - \Sigma_Y^{1/2}\|_F^2$. Eq. (8) replaces $\Sigma_Y^{1/2}$ with an *unconstrained* learnable $W_k$ (no PSD/square-root constraint), drops the constants $\|\Sigma_X^{1/2}\|_F^2 + \|W_k\|_F^2$, and uses $\mathrm{tr}((\Sigma_X^{1/2}U_k) W_k)$ as a *similarity to maximize* inside a softmax. The objective being optimized is not a Wasserstein distance — it's a structured linear classifier over $(\mathrm{vec}(\Sigma_X^{1/2}U), \mu_X)$ with an orthogonality regularizer. Tab. 3c reinforces this: class-share $U$ wins, which is the *opposite* of Prop. 2's per-pair prescription. Since GEMD-T provides the headline gains, the framing "first parametric EMD for Gaussians in deep learning" (Sec. 1 contribution 2; Sec. 4.3 last paragraph) materially overclaims; the contribution is better described as an EMD-inspired classifier head.
- **The +2.3%/+1.3% SOTA gains are confounded by an upgraded pipeline that competitors were not re-run under.** The authors' RFS, ADM, DeepEMD rows use self-distillation pre-training + last-stage DS removal; Tab. 3d alone shows DS removal yields 1.4–1.6%. TSA's row is taken from its paper rather than re-run on the matched backbone. The cleanly controlled comparisons (GEMD-T vs RFS/ADM/DeepEMD under matched pre-training) are convincing, but the "beats prior SOTA by 2.3%/1.3%" framing requires a re-run of TSA (and ideally 2LM+TSA) with self-distilled + DS-removed ResNet-18 to be defensible.

### Minor
- **No confidence intervals on Meta-Dataset.** Standard protocol reports 95% CIs over 600 episodes per dataset; many per-dataset deltas in Tabs. 1–2 are sub-1% and average-rank computations are sensitive to a few close calls. Reporting CIs would mark which dataset-level wins are statistically distinguishable.
- **"Not elucidated previously in deep learning" (Sec. 1; Sec. 4.2; Sec. 2 last paragraph) overstates the novelty of the matching-flow interpretation.** The Gaussian-coupling form is the Dowson–Landau / Olkin–Pukelsheim transport plan and is cited as such (Prop. 1 is attributed). The intuitive-interpretation contribution is presentational rather than technical and should be framed that way.
- **Per-domain In-D / Out-D averages on Meta-Dataset are not reported,** only "Average All" / "Average Rank." These splits are standard and would let the reader see whether gains are concentrated in-domain or generalize across domains.
- **NS preconditioning by $\mathrm{tr}(\Sigma)$ rather than operator/Frobenius norm.** NS convergence requires spectral radius $<1$; tr-normalization is a sufficient bound only in benign conditioning regimes. Tab. 3b's slight degradation at large $r$ for GEMD-T is consistent with marginal convergence, and a brief diagnostic (e.g., fraction of iterates within the precondition) would substantiate the choice.

### Trivial
- The "matching flow" $f_{XY}^*$ density form in Eq. (5) is degenerate (concentrates on an affine subspace under the deterministic optimal coupling); the visualization in Fig. 1b is illustrative only and never used downstream. Worth a clarifying sentence.
- Sec. 4.2 invokes the Riemannian geometry of the Gaussian manifold but support-set prototypes average $\Sigma_k$ in ambient Euclidean space rather than along the Bures–Wasserstein geodesic — a small inconsistency between motivation and practice.

## Nice-to-Haves
- A constrained "true-EMD" variant of GEMD-T (e.g., parameterize $W_k$ as the NS square root of a learned PSD $M_k$, keep the constants, flip the sign) tested head-to-head with the current Eq. (8). If matched, the EMD framing is vindicated; if not, GEMD-T's gain comes from being a free classifier head and the paper should say so honestly.
- A direct analysis of what the learned $U_k, W_k, v_k$ encode (is $W_k$ close to any PSD matrix? is $U_k$ close to the polar factor of $\Sigma_X^{1/2}W_k$?).
- Visualization of optimal Gaussian matching flows on actual Meta-Dataset image pairs — the paper promises this interpretive payoff in Fig. 1b but only delivers a schematic.
- Demonstrating on the few-shot action recognition / image retrieval tasks promised in the conclusion would justify the broader-applicability claim.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *(Harsh critic) Parser-mangled landing-algorithm symbols inline in Sec. 4.4.* Removed: formatting/parser artifact, not an author error.
- *(Harsh critic) "Many `wins` ... are likely within CI of competing methods."* Speculative without independent CI estimates; the underlying call for CIs is kept above as a minor weakness, but this particular framing is conjecture.
- *(Strength finder) "GPU-friendly parallelism enables a first such learnable EMD in deep learning."* This strength conflicts with the verified Major weakness about Eq. (8) not preserving EMD structure; the parallelism aspect is real but the "first parametric EMD" framing isn't.
- *(Strength finder) Generic praise about "careful ablation of design choices."* Too generic to keep as a standalone strength; the specific ablations (NS iterations, DR dim, DS removal) are already implied by other kept strengths.

## Novel Insights
None beyond the paper's own contributions. The strongest reviewer-introduced observation — that Eq. (8) is structurally a linear classifier rather than a Wasserstein metric and that Tab. 3c's class-share winner corroborates this — is a clarifying critique of the paper's own framing rather than an independent insight.

## Suggestions
- Reframe GEMD-T as an "EMD-inspired structured classifier" or run the constrained variant described above; in either case, soften "first parametric EMD" claims.
- Re-run TSA (and 2LM+TSA where feasible) under the self-distilled + DS-removed ResNet-18 pipeline, and report a matched-backbone comparison alongside the current numbers.
- Add 95% CIs over 600 episodes per dataset and per-domain In-D / Out-D averages on Meta-Dataset.
- Add a brief NS-convergence diagnostic under tr-normalization for the largest $p$ used.
- Replace Euclidean averaging of $\Sigma_k$ for class prototypes with Bures–Wasserstein barycenters for consistency with the manifold motivation.

---

**Axis-by-axis assessment.** *Originality:* moderate — applying the closed-form Bures–Wasserstein distance to FSL is a sensible, focused contribution but the underlying identity is classical, and the "parametric EMD" angle is overclaimed. *Importance:* moderate — DeepEMD's cost is a real bottleneck and a closed-form replacement is useful. *Claim support:* mixed — the GEMD-M-vs-ADM/DeepEMD comparison and the speed claim are well supported; the SOTA-by-2.3%/1.3% claim is not adequately controlled. *Soundness of experiments:* mostly sound under matched pre-training, but the head-to-head with TSA is uncontrolled and CIs are absent. *Clarity:* generally clear; the GEMD-T derivation glosses over which constants/constraints are dropped from Prop. 2. *Value to the community:* a useful engineering recipe (closed-form Gaussian EMD + NS + landing) and a credible improvement over DeepEMD/ADM at matched settings; the parametric-EMD framing should be tempered.

## Score and Decision
The paper has a real, well-supported core (GEMD-M as a closed-form, faster, more accurate replacement for DeepEMD/ADM under matched pre-training), but its two most prominent advertised contributions — that GEMD-T is a *parametric EMD* and that it sets new SOTA by 2.3%/1.3% — are respectively a structural mischaracterization of the loss and a confounded comparison. These are addressable in revision (re-run TSA on the matched backbone; reframe or constrain GEMD-T), but in the current form the headline framing exceeds what the math and experiments establish.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>