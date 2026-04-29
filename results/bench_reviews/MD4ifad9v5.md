## Summary
The paper proposes a construction of adaptive higher-order reversible integrators for neural ODE-style deep learning. Its central technical step is showing that two half-steps of ALF, denoted ALF2, are second-order accurate in both state and velocity, enabling Yoshida symmetric composition to build fourth- and higher even-order reversible architectures; experiments compare a fourth-order instance, Y4, against ALF on several dynamical-system learning tasks.

## Strengths
- **Concrete and technically meaningful construction of higher-order reversible methods.** Theorem 3.1 states that composing two ALF half-steps gives second-order accuracy in both \(z\) and \(v\), despite standard ALF being described as order \((2,1)\). This is the key observation that permits use of classical symmetric composition methods.
- **Systematic rather than ad hoc extension to higher order.** Section 3 applies Yoshida composition with explicit coefficients \(a=\frac{1}{2-2^{1/(2k+1)}}\), \(b=1-2a\), and invokes Theorem 3.2 to obtain order \(2k+2\) reversible methods from an order-\(2k\) reversible base method. This is a clean route to arbitrary even-order reversible integrators, not merely a single new layer.
- **The experiments do show consistent speedups over ALF in the tested settings.** The Kepler experiment reports that Y4 reaches loss \(10^{-8}\) at least four times faster than ALF; the coupled Duffing oscillator experiment reports nearly a factor-two speedup to loss \(10^{-4}\); the neural-network-parametrized oscillator and discretized wave equation experiments also report faster wall-clock convergence for Y4.
- **The experimental tasks are relevant to the intended application area.** The paper tests scalar parameter identification, a 20-dimensional coupled oscillator with 65 unknown parameters, a neural-network-parametrized force/potential model with 51,500 parameters, and a discretized wave equation. This is a reasonable initial set of dynamical-system learning examples.
- **The paper usefully distinguishes neural-network reversibility from numerical time symmetry.** Section 2.3 explains that reversible networks require an explicit backward map, while symmetric numerical integrators invert by replacing \(h\) with \(-h\). This distinction is important for understanding why symmetric-composition theory is relevant here.

## Weaknesses

### Fatal
None.

### Major
- **The adaptive-gradient semantics are not sufficiently established.** The paper motivates reversible networks partly as a way to avoid the incorrect-gradient issue of continuous adjoints, but the adaptive stepping paragraph says that “the computational graph and all the variables needed for the step size computations” are deleted and “only the value of the accepted new step size \(h_j\) is saved.” This means the backward pass differentiates through a trajectory with the accepted mesh frozen, not necessarily through the full adaptive solver as a function of parameters, because the accepted step sizes themselves depend on the forward trajectory and therefore on the trainable parameters. The paper needs to state precisely what objective is being differentiated and whether gradients through the step-size controller / accept-reject mechanism are intentionally ignored. This is central because the claimed benefit is not merely reversibility, but memory-efficient training with adaptive time stepping.
- **The memory-efficiency claim is central but not empirically demonstrated.** The title, abstract, and conclusion emphasize memory-efficient deep learning and claim that reversibility avoids high memory requirements. However, Section 4 reports only wall-clock time to reach loss thresholds; it does not report peak memory, memory-vs-depth scaling, or comparison to standard backpropagation, checkpointing, adjoint methods, ALF/MALI, or reversible Heun. The theory supports storing step sizes rather than high-dimensional states, but the paper’s empirical claim that the architecture “demonstrate[s] lower memory costs” is not actually tested.
- **The empirical comparison is too narrow for the broader efficiency/scalability claims.** The experiments compare Y4 almost entirely against ALF. That is a useful baseline, since ALF is the base low-order adaptive reversible method, but it only supports the limited conclusion that Y4 is faster than ALF on these examples. It does not establish competitiveness with checkpointed high-order adaptive solvers, reversible Heun, continuous adjoint/checkpointed Runge–Kutta methods, or other high-order composition methods. Because Y4 uses multiple ALF2 substeps per macro-step, wall-clock time alone is also hard to interpret without function-evaluation counts, accepted/rejected step counts, tolerances, and per-epoch solver behavior.
- **The applicability of Yoshida composition is materially limited by negative substeps, and the paper underplays this limitation.** Section 3 correctly notes in Remark 3.3 that Yoshida composition uses negative time steps and that this can be problematic for dissipative equations such as the heat equation. This is not just a small implementation caveat: it limits the method’s applicability to some important PDE-derived dynamical systems and weakens the broad claims about scalability to PDE discretizations unless the scope is narrowed or a stability analysis / alternative positive-coefficient construction is provided.

### Minor
- **The “memory independent of depth” phrasing is too strong for adaptive solvers.** Section 2.3 explicitly says the time steps \(t_0,\ldots,t_N\) must be stored, and Section 3 says the accepted step sizes \(h_1,\ldots,h_N\) are saved. This is much cheaper than storing high-dimensional activations, but the memory is not literally independent of the number of accepted steps.
- **The experiments report training-loss thresholds but not parameter or model-identification accuracy.** In the Kepler and Duffing settings, the stated goal is accurate parameter identification, yet the reported metric is time to a trajectory-loss threshold. Reporting \(|\hat{\alpha}-\alpha|\), final parameter errors, or parameter error versus tolerance would better support the claim that higher-order integration improves identification accuracy.
- **The claim of applicability to high-dimensional PDE-governed systems is only weakly supported.** The discretized wave-equation example is relevant, but its state dimension is 40 and it is not a stress test of high-dimensional PDE learning. It also avoids the dissipative/parabolic regimes where negative substeps are most concerning. The result is a useful proof of concept, but not enough to substantiate broad scalability claims.
- **The adaptive algorithm is underspecified in the main text.** The paper does not clearly describe the error estimator, accept/reject policy, handling of rejected steps, tolerance choices, or exactly what is stored and replayed. This matters because the paper’s novelty is specifically adaptive high-order reversibility.

### Trivial
None.

## Nice-to-Haves
- Report loss and parameter/model error versus number of RHS evaluations, not only wall-clock time.
- Include accepted/rejected step counts and step-size histories to support the claim that Y4 is faster because it can take larger steps.
- Add a direct gradient check comparing the reversible adaptive backward pass against full backpropagation through the same discretized computation, finite differences, or checkpointed autodiff.
- Test or discuss a dissipative/parabolic system more carefully, or explicitly state that the current construction is best suited to dynamics where negative substeps are stable.
- Include qualitative rollouts or generalization tests on unseen initial conditions for the neural-network-parametrized systems.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Missing appendix/proof complaints.** Any criticism that the proof of Theorem 3.1 or appendix material is absent should be removed because the extracted PDF may omit appendices and proof details; the paper text explicitly indicates that computations/proof material exist.
- **Formatting, garbled text, table-image, and parsing artifacts.** The extracted file contains broken text and image placeholders for tables, but these are parser artifacts and should not be counted against the submission.
- **Missing related-work complaints.** Critiques based on absent external references are removed because we cannot verify the completeness of the related-work landscape here.
- **Generic “important problem” strength.** The statement that adaptive reversible neural ODEs are an important problem is true but generic; it is not counted as a core strength unless tied to the specific ALF2/Yoshida contribution.
- **Overly broad demand for every possible downstream application.** Experiments on normalizing flows, image processing, or stochastic differential equations would be interesting, but they are outside the paper’s stated primary focus on dynamical-system learning.

## Novel Insights
The paper’s genuinely novel insight is that ALF’s apparent first-order behavior in the auxiliary velocity does not preclude higher-order reversible construction: by grouping two half-steps into ALF2, the authors recover a second-order symmetric base method in the augmented variables and can then apply classical composition theory. The main unresolved tension is that this elegant numerical-analysis construction is stronger than the empirical and algorithmic validation currently provided: the paper convincingly motivates a higher-order reversible integrator, but does not yet fully establish the adaptive-gradient correctness, memory savings, or broad practical superiority claimed around it.

## Suggestions
- Precisely define the differentiated objective under adaptive stepping: frozen accepted mesh vs. full adaptive solver including step-size controller.
- Add a gradient-correctness experiment comparing the proposed reversible backward pass to full autodiff/checkpointed autodiff on small problems.
- Measure peak memory and memory scaling with number of steps/depth against backpropagation, checkpointing, ALF/MALI, reversible Heun, and a checkpointed high-order adaptive solver.
- Report solver-level statistics: RHS evaluations, accepted/rejected steps, tolerances, average step sizes, and per-epoch cost.
- Narrow claims about high-dimensional PDE scalability unless larger PDE experiments or a stability analysis for negative Yoshida substeps are added.
- Report parameter-identification errors in the Kepler and Duffing experiments, not just trajectory-loss thresholds.

## Score and Decision
**Originality:** Good. The ALF2 observation plus Yoshida composition is a concrete and nontrivial numerical-method contribution for reversible neural ODE architectures.  
**Importance:** Moderate to high for the niche of memory-efficient neural ODE training and dynamical-system identification.  
**Support for claims:** Mixed. The construction is plausible and the ALF comparison is positive, but the paper overclaims memory efficiency, adaptive-gradient correctness, and scalability beyond what is shown.  
**Experimental soundness:** Limited. The experiments are relevant but narrow, use mostly one baseline, omit memory measurements, and lack solver-level diagnostics.  
**Clarity:** The high-level idea is understandable, but the adaptive-stepping algorithm and gradient semantics need much more precision.  
**Value to the community:** Promising, especially for researchers working on reversible/adaptive neural ODE solvers, but the current submission needs stronger validation and narrower claims.

### Calibration anchors used
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AoraWUmpLU.md` — Avg 8.00. A much stronger Neural ODE theory paper with rigorous convergence analysis and supporting experiments; the present paper is below this because its central adaptive-gradient and empirical-memory claims are not comparably established.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1PXEY7ofFX.md` — Avg 7.20. A strong numerical-solver paper praised for practical acceleration and empirical quality; the present paper has a nice construction but weaker baseline coverage and diagnostics.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/trV41CpAK4.md` — Avg 6.50. A Neural ODE acceleration paper with clear function-evaluation reductions and broader empirical speedups; the present paper is below it because it lacks comparable efficiency accounting and memory measurements.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qA4foxO5Gf.md` — Avg 6.25. A principled numerical-integrator acceleration paper; the present paper is somewhat similar in spirit but less empirically complete.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/y33lDRBgWI.md` — Avg 6.00. A memory-efficient adjoint/backpropagation paper accepted despite limitations; the present paper is below or around this level because its memory claim is not empirically demonstrated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E34AlVLN0v.md` — Avg 6.00. A sequential-model acceleration paper; useful as a high/medium anchor, but less directly comparable than the Neural ODE anchors.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IWpLQfZ8Xg.md` — Avg 6.00. Solid theory with limited empirical scope; comparable pattern, though the present paper’s central empirical memory claim is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Pin2kdWloe.md` — Avg 5.75. Theory-driven work with concerns about generality/overstatement; close to the present paper’s profile.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3J7foqnJkA.md` — Avg 5.67. Interesting theory plus useful experiments but limited scope; similar borderline region.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4KKqHIb4iG.md` — Avg 5.60. Borderline neural PDE/ODE-solver training work with validation/soundness concerns; similar in broad area but likely less technically crisp.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Z1m5uqUpO9.md` — Avg 5.50. Theoretical framework with narrow validation; similar in the sense that useful ideas are weakened by limited evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aJl5aK9n7e.md` — Avg 5.25. Theory and experiments with concerns about scope and overclaiming; comparable but less topical.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/90QOM1xB88.md` — Avg 5.00. Numerical-integrator paper praised for some theory/performance but weakened by unclear results and assumptions; close to the score I assign here.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/97dJ3Jp5P4.md` — Avg 4.75. Memory-efficient reversible-network gradient paper with interesting ideas but weak practical/memory argument and limited baselines; very relevant, and the present paper is slightly stronger technically but has similar validation gaps.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/X3IcgZEUEi.md` — Avg 4.75. ODE parameter-identification efficiency paper with unclear formulation and weak validation; the present paper is stronger due to a clearer numerical construction.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/spwklWgmWJ.md` — Avg 4.75. Theoretically interesting but weak practical memory-efficiency evidence; a close weakness-pattern anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EUe0yA2pAw.md` — Avg 4.67. Reversible/memory-saving transformer paper with practical concerns; relevant as a memory-efficiency overclaim anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WtNgFrPn8y.md` — Avg 4.25. Theory plus limited empirical comparison; the present paper is stronger and more coherent.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/17ZbByq95E.md` — Avg 3.75. Memory-efficient backpropagation paper weakened by limited novelty and narrow evaluation; the present paper is above this due to a more substantive numerical-method contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tnSj6FdN8w.md` — Avg 3.50. Neural time-integrator paper judged incremental and lacking theory/experiments; the present paper is clearly stronger because it has a specific reversible higher-order construction.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YAvEKf1KUd.md` — Avg 3.50. Low-novelty Neural ODE/DAE paper with simple case studies and weak baselines; the present paper is above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CNPLXcMcSP.md` — Avg 3.50. Theoretical acceleration idea with essentially absent empirical validation; the present paper has more concrete experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vnp2LtLlQg.md` — Avg 3.00. Novel but poorly validated memory/efficiency method; the present paper is substantially stronger.

Relative to these anchors, this paper sits above the clearly weak numerical-integrator/memory-efficiency papers around 3–4 because it has a real mathematical construction and consistent ALF speedups. However, it is below the accepted Neural ODE/numerical-solver papers around 6–7 because its central memory and adaptive-gradient claims are under-validated and its baseline set is too narrow. I therefore assign a borderline but negative score.

## Score and Decision
Score: **5.0 / 10**  
Decision: **Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>