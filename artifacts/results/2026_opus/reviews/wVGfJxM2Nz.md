Now I have enough calibration to write the final review.

## Summary
The paper is a position-style empirical case study arguing that geometry-aware models generalize better with fewer parameters than structure-naive baselines. It examines two case studies: (i) Riemannian-Adam optimization on the SPD manifold for a 2-state linear state-space identification of a heat-transfer system, and (ii) an existing Symplectic Hamiltonian Neural Network (SHNN) applied to the 18-D FPUT-α chain, compared against RF/XGBoost/LSTM/NeuralODE baselines.

## Strengths
- **Headline result on FPUT is genuinely strong:** Table 2 shows a 1,441-parameter SHNN attains rollout MSE 5.28e-09 and drift RMS 3.98e-04, versus the best LSTM (97,074 params, 67× larger) at rollout MSE 1.69e-06 and drift RMS 5.91 — multiple orders of magnitude better on both metrics, supporting the "smaller is better with structure" claim.
- **Model-size sweep reveals a real saturation effect for naive baselines:** Figure 3 (center) shows NeuralODE and LSTM rollout MSE plateau as parameter count grows, while SHNN remains flat and low. This is concrete evidence that "scale up" is not a substitute for the inductive bias.
- **Energy-drift RMS is a useful, mechanistic diagnostic:** Section 3.2 defines drift_RMS over 1,000-step rollouts; combined with Figure 4 (trajectory crossings of energy level sets), the paper gives a clear mechanistic narrative for *why* naive models fail at long horizons.
- **Riemannian-update LSSM does generalize OOD better than its Euclidean twin:** In Table 1, RieOpt beats EucOpt and structure-naive baselines on the Chicago test set (T_ext1: 1.36 vs. 3.35 (EucOpt), 40.1 (LSTM), 22.3 (XGBoost)), which supports the dissipative-case claim on the OOD axis.

## Weaknesses

### Fatal
None. The core empirical claim — that structure-aware models generalize better at smaller sizes — is supported by the FPUT numbers, even if the supporting story has gaps.

### Major
- **The geometric scaffolding for the dissipative case is shaky on the paper's own equations.** §2.1.1 argues $\Phi_A = e^{A\tau}$ lives in $\mathrm{Sym}_n^+$ because $A \in \mathrm{Sym}_n$, but the $A$ written explicitly in Eq. 2 is *not* symmetric in general — the off-diagonals are $U_{ext1,ext2}/C_{ext1}$ and $U_{ext1,ext2}/C_{ext2}$, which are equal only when $C_{ext1}=C_{ext2}$. The paper hedges with "in several instances," but does not state whether the experiment is one of them. Compounding this, the text in §2.1.1 conflates SPD-ness with discrete-time stability: SPD requires positive eigenvalues but the discrete-time stability condition is $|\mu_i|<1$, so SPD is neither necessary nor sufficient for stability. The text "$e^{A\tau}$ is a bilinear map ... wrapping the stable eigenvalues located in the left half-plane (Re$(\lambda_i)<0$) within the unit circle in the s-plane where Re$(\lambda_i)>0$" is internally contradictory (s-plane / z-plane are conflated). Net effect: the geometric justification for the SPD constraint in the dissipative experiment is not what the paper claims it is. The constraint may still work as a regularizer for *near*-symmetric problems, but framing it as "structure-preserving" is overreach.
- **The dissipative comparison is not the comparison that supports the thesis.** RF/XGBoost/LSTM are generic time-series learners, not parametric ODE-style models, so the gap to the LSSM in Chicago is largely the parametric-vs-nonparametric gap, not the SPD-vs-not gap. The RieOpt vs. EucOpt contrast in Table 1 is the *controlled* comparison and shows a real but more modest improvement (e.g., London T_ext1: 0.40 vs. 1.28; Chicago T_ext1: 1.36 vs. 3.35). The Cholesky $LL^\top$ parameterization explicitly mentioned in §2.1.2 as an alternative is not evaluated, even though it is the natural ablation that would isolate the role of the Riemannian update from the role of merely enforcing SPD structure.
- **The FPUT result does not isolate the symplectic-integrator contribution.** The SHNN combines (a) a scalar Hamiltonian parameterization with (b) a symplectic time discretization. The cleanest comparison — HNN with the same scalar-Hamiltonian parameterization but a non-symplectic integrator (e.g., RK4), or SHNN's symplectic step swapped for RK4 — is not run. Without it, the orders-of-magnitude drift advantage cannot be cleanly attributed to symplectic structure vs. the Hamiltonian parameterization itself. Given that the paper's headline finding rests on this result, the missing ablation is a real evidential gap.
- **Single-seed reporting throughout.** No variance, repeats, or confidence intervals are given for Table 1 or Table 2. This is genuinely problematic for the NeuralODE column in particular: drift swings from 1.79 (L=1, W=72) to 377.5 (L=1, W=36) to 1802.7 (L=2, W=36) — a three-order-of-magnitude jump across nearby configurations strongly suggesting training-stability artifacts rather than a meaningful trend. The paper presents these as "the answer."

### Minor
- **Contribution is narrower than the framing.** Stripped of geometric exposition, the paper is: apply RAdam to a 2×2 SPD-constrained LSSM, plus apply an existing SHNN (David & Méhats 2023) to FPUT. The "smaller structure-aware models generalize better" thesis is already supported by the works cited (Greydanus 2019; David & Méhats 2023; Jin 2020). No new architecture, theorem, dataset, or clearly novel regime is introduced.
- **PINN baseline is absent despite the motivation.** §1.1 frames the paper against PINN-style "structure-through-loss" approaches, but no PINN is included in either experiment.
- **§3.1.1 narrative glosses over a real Table 1 datum.** XGBoost on London T_ext2 (1.06e-01) is better than RieOpt (5.07e-01), yet the text broadly characterizes the structure-naive baselines as "unstable." The honest read is: structure-naive models are competitive or better in-distribution; structure-aware models are much better out-of-distribution. This is still a defensible story; it just isn't the one the text tells.
- **Eq. 7 likely has a transcription slip:** the second term reads $\Phi_B T_i$ where Eq. 4 dictates $\Phi_B U_i$. Worth checking.

### Trivial
- "Further expansion of 16" in §3.1 references a nonexistent equation.
- Eq. 10 writes both $q_0=q_N=0$ and $q_0=q_{M+1}=0$ in adjacent lines; consistent given $M=N-1$ but reads as carelessness.

## Nice-to-Haves
- A data-efficiency curve (varying training trajectory length or subsample fraction) on either system would do far more to support the "smaller models" thesis than the current single parameter-count snapshot across non-apples-to-apples model classes.
- A roll-out-horizon sweep would let the symplectic integrator's contribution emerge cleanly: the symplectic advantage *should* grow with horizon, and showing that curve crossing is more convincing than a point estimate at 1,000 steps.
- Replace breadth with depth: one system class, the full family of structural priors (SPD-constrained, Cholesky-LL^T, unconstrained Euclidean, plus PINN-style loss penalty), and varying initialization-error magnitude. That isolates the geometric prior from the model class.
- A short discussion of when SPD is and is not the right structural prior for the dissipative LSSM (i.e., when $C_{ext1} \approx C_{ext2}$, so $A$ is near-symmetric) would make the §2.1 framing honest and would not weaken the empirical story.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"NeuralODE numbers may reflect unstable training"** (Harsh critic) — already covered under "single-seed throughout"; kept once, merged.
- **Strength: "The paper validates on two fundamentally different physical regimes — dissipative and conservative"** (Strength Finder) — superficial breadth framing that the harsh critic correctly identifies as a weakness (one example each side, no depth). The two-example breadth conflicts with the missing controlled comparisons; removed per the rule that weaknesses override conflicting strengths.

## Novel Insights
None beyond the paper's own contributions. The "smaller structure-aware models generalize better than scaled-up naive models" message is already established in the literature the paper cites (Greydanus 2019; David & Méhats 2023; Jin 2020).

## Suggestions
- Add the HNN-without-symplectic-integrator ablation on FPUT; this is the experiment that would turn the §3.2 result from a re-demonstration into a contribution.
- Run multi-seed (5–10) for at least the key cells of Tables 1 and 2 and report variance, especially given the NeuralODE column's three-order-of-magnitude swings.
- Either restrict §2.1.1's geometric claims to the symmetric-$A$ case ($C_{ext1}=C_{ext2}$) and clearly state that the experiment satisfies it, or reframe the SPD constraint as a *regularizer for near-symmetric problems* rather than as structure preservation. Fix the s-plane/z-plane and "bilinear map" misstatements in §2.1.1.
- Add a Cholesky $LL^\top$ ablation (the paper itself proposes it in §2.1.2 and does not run it).
- Add a PINN baseline to close the loop with the §1.1 framing.
- Acknowledge in §3.1.1 that in-distribution the gradient-boosted models are competitive; the structure-aware advantage is specifically OOD.

---

**Axis assessment.** *Originality*: low — both methods (Riemannian-Adam SPD optimization and SHNN) are taken off the shelf. *Importance*: the question (when does structure beat scale?) is important. *Claim support*: partial — the FPUT claim is well supported in magnitude though missing the key ablation; the dissipative claim has shaky geometric scaffolding and the wrong controlled comparison. *Soundness*: the FPUT case is sound empirically; the dissipative case has a conceptual gap in §2.1.1. *Clarity*: generally readable but sloppy in the dissipative theory section (Eq. 7 typo, missing eq. 16, s/z-plane confusion). *Value to community*: limited — a re-demonstration of established phenomena without a new method, theorem, or carefully isolated empirical regime.

**Calibration anchors retrieved.**

| Path | Avg | Round | Comparison to paper under review |
|---|---|---|---|
| `NRRHkJE03w.md` (Beyond Dynamics) | 3.00 | R1 | Read in full. Confusing presentation, unclear contribution. Paper under review is clearer but contribution is similarly limited; comparable. |
| `kkVTeMvC9D.md` (Training Jacobian) | 3.40 | R1 | Listed only. Off-topic empirical study; similar weakness profile (descriptive, not novel). |
| `oMfZUSbVwf.md` (NN parameter symmetries) | 3.00 | R1 | Listed only. Different topic. |
| `uL1H29dM0c.md` (Metriplectic) | 7.00 | R1 | Listed only. Genuinely novel architecture with theory; clearly stronger than paper under review. |
| `U1DjXQeJRx.md` (Poisson-Dirac NNs) | 6.60 | R1 | Listed only. Novel framework; clearly stronger. |
| `XqDM97DtMf.md` (Embedded Dissipativity) | 4.67 | R1 | Read in full. Proposes a novel Lyapunov-projection architecture with formal guarantees; mixed reviews. Stronger than paper under review since it offers a new method. |
| `03EkqSCKuO.md` (Port-Hamiltonian DGN) | 7.00 | R1 | Listed only. Novel architecture for graph networks; clearly stronger. |
| `Xo0Q1N7CGk.md` (Conformal Isometry) | 8.00 | R1 | Listed only. Substantive theory + numerics; far stronger. |
| `JWtrk7mprJ.md` (Deep GPs on Manifolds) | 7.60 | R1 | Listed only. Novel models with broad applicability; far stronger. |
| `g7ohDlTITL.md` (Riemannian Flow Matching) | 8.00 | R1 | Listed only. Novel framework; far stronger. |
| `60FseFP084.md` (SPONs) | 4.25 | R2 | Read in full. Novel FEM-based operator-learning architecture; reviewers ding it on experimental breadth. Has more methodological novelty than paper under review — stronger. |
| `ZujMVRn7Md.md` (ODNN) | 4.25 | R2 | Listed only. Novel orthogonal constraint architecture; stronger than paper under review on novelty. |
| `sSWiZr8QU7.md` (Gray-box) | 4.00 | R2 | Listed only. Comparable scope/contribution. |
| `gz8Rr1iuDK.md` (Geometric+Physical Constraints PDE) | 4.00 | R2 | Read in full. Systematic two-experiment ablation of constraint types; has more rigorous experimental design than paper under review. Slightly stronger. |
| `AZGIwqCyYY.md` (Cross-domain Hamiltonian) | 5.75 | R2 | Listed only. Novel meta-learning extension; clearly stronger. |
| `QXQiq8JVOB.md` (Hamiltonian mechanics ResNets) | 5.25 | R2 | Listed only. Novel theory; stronger. |
| `KEpR8hFzvO.md` (Conservation-law NOs) | 5.00 | R2 | Listed only. Novel architecture with theory; stronger. |

**Round-1 bracket:** between 3 and 5 — weaker than all >5 anchors (which propose new methods/theory), comparable to or weaker than 4.0–4.7 anchors which propose new architectures with mixed reviews.

**Round-2 narrowing:** all four R2 anchors I read in detail (gz8Rr1iuDK at 4.0, 60FseFP084 at 4.25, XqDM97DtMf at 4.67) introduce a *new method/architecture* and were rejected primarily on experimental scope and clarity. The paper under review introduces no new method — it applies existing RAdam on SPD and an existing SHNN. Combined with (a) the genuine geometric-framing problems in §2.1.1, (b) the dissipative comparison not isolating the claimed cause, (c) the missing HNN-without-symplectic ablation, and (d) single-seed reporting, it sits *below* the 4.0–4.25 cluster but is rescued slightly above the 3.0 floor by the clean, clearly-presented, and quantitatively-strong FPUT result. Settles at 3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>