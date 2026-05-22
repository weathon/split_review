Now I have all the calibration data I need. Let me write the consolidated review.

---

## Summary

This paper proposes STNAdam, a stochastic optimizer for "nonconvex + weakly-convex" composite optimization problems. The key algorithmic novelty is a "two-track iteration framework" that maintains an extrapolation trajectory alongside a regular update trajectory, combining Nesterov momentum with Adam-style adaptive conditioning. The authors provide a convergence analysis under the Kurdyka-Łojasiewicz property with dynamic hyper-parameters, and present empirical results on low-light image enhancement (LIE).

## Strengths

1. **Genuinely novel algorithmic design (two-track framework).** The two-track iteration idea — maintaining separate extrapolation and regular update sequences driven by momentum and adaptivity — is a clear departure from existing single-track accelerated Adam variants (NAdam, SNAdam). Algorithm 1 and the trajectory comparison in Figure 1(d) make this distinction explicit. The paper integrates this design with three concrete gradient estimators (SGD, SAGA, SARAH) and provides specific update formulas for each.

2. **General almost-sure convergence theory under KL property with flexible estimator support.** Theorem 1 establishes that the sequence converges almost surely to a stationary point, and the analysis accommodates any variance-reduced gradient estimator (SVRG, SAGA, SARAH, SPIDER) through the conditions in Lemma 1. Theorem 2 gives explicit rates for three regimes of the KL exponent ($\vartheta \in (0,\frac12]$, $(\frac12,1)$, and $=0$), which is a more detailed rate characterization than is common for adaptive stochastic methods with momentum.

3. **Empirical advantage of STNAdam over single-track baselines on LIE.** In Table 2, STNAdam-SARAH (PSNR 22.26) substantially outperforms the single-track SNAdam (PSNR 17.14) on the LOL dataset when all are applied to the same optimization problem (14). STNAdam-SAGA (PSNR 21.05) and STNAdam-SGD (PSNR 18.06) also outperform SNAdam. This provides evidence that the two-track design yields better optimization outcomes than single-track counterparts on this task.

## Weaknesses

### Major

1. **Unexplained timing measurements that undermine credibility.** The "Time(s)" column in Tables 2 and 3 reports values like 2.64×10⁻⁵ s (~26 microseconds) per sample for processing an entire image through an optimization algorithm with proximal gradient steps. The paper provides no explanation of what this timing measures (per-image? per-iteration? per-patch?), on what hardware, or how many runs were averaged. Even a single forward-backward pass through a small neural network or a proximal gradient iteration on a 600×400 image would take orders of magnitude longer than 26 μs. Without clarification, these numbers suggest either a reporting error or evaluation at an unrealistically small scale, which casts doubt on all quantitative results.

2. **Reference inconsistencies for key baselines.** The paper uses the name "SAdam" inconsistently: the Related Work section attributes SAdam to Le-Duc et al. (2024) and Wang et al. (2019), but the table heading and contribution section cite it as "(Kingma & Ba, 2014)" — Kingma & Ba is the plain Adam paper. Similarly, the Related Work states that Reddi et al. (2019) named SNAdam, while the table and contribution section cite SNAdam as "(Xie et al., 2024)" — but the text says Xie et al. proposed "SAdan," not SNAdam. These inconsistencies make it unclear which algorithms were actually used as baselines, which is a serious concern for a paper claiming empirical superiority.

3. **No ablation or sensitivity analysis for the claimed advantages.** The experimental section reports only final metric values. There are no convergence curves, no ablation studies isolating the effect of the two-track design from the variance reduction or momentum components, no sensitivity analysis for the randomly-selected parameters ($\gamma_{k+1}, \lambda_{k+1}, \alpha_{k+1}$), and no multiple-seed trials with error bars. Without these, it is impossible to attribute the empirical gains to the two-track mechanism specifically rather than to hyperparameter choices or other implementation details.

4. **The claim "removing hand-tuning" is misleading.** The hyper-parameter intervals in (6)–(8) depend on global constants $L$ (Lipschitz modulus of $\nabla f$), $\tau$ (weak convexity modulus), and estimator-dependent constants $V_1, V_T, \rho$ that are unknown in practice. The user must still estimate or bound these constants to define the intervals. This replaces one set of hand-tuned hyperparameters with another set of opaque problem-dependent constants, not "removes" hand-tuning.

### Minor

5. **Missing Step 4 in the analysis.** Section 3 jumps from "Step 3" (Lemma 5, Theorem 1) directly to "Step 5" (Theorem 2). While this is likely a formatting artifact from rearranged content, it suggests the theoretical narrative was assembled from fragments and reduces confidence in the presentation.

6. **Lemma 1 conditions are stated but not verified for any concrete estimator.** Lemma 1 defines abstract conditions (MSE bound, geometric decay, convergence) for a "variance-reduced gradient estimator," and the paper claims these hold for SVRG, SAGA, SARAH, SPIDER. But it provides no verification — not even a sketch or a citation showing why any specific estimator satisfies (3)–(5). The theoretical results that build on Lemma 1 are therefore conditional on unverified assumptions.

7. **The two-track motivation is imprecise.** The paper explains the two-track design as aiming to "promote the formation of a larger update neighborhood, while exploring a better iteration direction continuously." This intuition is not made precise — the paper never formalizes what "larger update neighborhood" means or why two tracks achieve it while single-track extrapolation (as in NAG or NAdam) does not. Figure 1 is a cartoon with undefined notation (e.g., arrows labeled $\hat{m}^{k+1}, \tilde{m}^{k+1}$) that does not cleanly map to Algorithm 1.

8. **Joint denoising experiment (Table 3) is too narrow.** It tests only 2 images against 3 baselines. This is insufficient to support any general claim about denoising performance.

### Trivial

9. The analysis mentions SVRG and SPIDER as supported estimators but only evaluates SGD, SAGA, and SARAH.
10. The proximal gradient operator notation $\mathcal{P}_g(x, y, t)$ is nonstandard — the usual proximal operator takes a step size, not a separate linear term and step size — though the definition is provided in Remark 1(i).

## Nice-to-Haves

- Compare against a broader set of adaptive first-order optimizers (AdamW, AMSGrad, AdaBelief) to better contextualize performance.
- Add a controlled synthetic experiment where the ground-truth optimum is known, to isolate the effect of the two-track mechanism from model-specific factors.
- Include convergence curves (objective value vs. iterations) alongside final metric tables.

## Removed Points

These points were flagged during review but are removed with justification:

- **"Experimental comparison is fundamentally invalid (mixing LIE methods with optimizers)"** — The harsh critic called this "apples-to-oranges" and said the comparison is uninformative. However, the paper clearly separates its claims: Contribution (iii) says "favorable practical performance" against both single-track optimizers *and* customized LIE methods. The paper includes a valid optimizer comparison (SGD, SAdam, SNAdam vs. STNAdam variants on the same problem (14)) *alongside* a practical comparison against LIE-specific methods. The latter is a standard way to show a full-pipeline advantage in applied optimization papers. It does not invalidate the optimizer comparison. The weakness is softened to a suggestion for clearer separation in presentation, not a fundamental flaw.

- **"Time(s) orders of magnitude too fast for neural network processing"** — The paper states it "adopts the training framework of Retinex-Net" and references the appendix for details. The appendix (removed from this review) may specify that the timing is per-patch or per-iteration on a small subproblem. The criticism of "implausible" timing is valid as a *presentation* issue (the main text should explain the timing) but is not a proof of error. Retained as a major weakness in modified form.

- **"The analysis cannot be assessed for correctness"** — This is true of most papers that defer proofs to an appendix; it is not a specific weakness.

- **"Not enough baselines like AdamW, NAdam, AMSGrad"** — This is a generic nice-to-have, not a weakness.

- **"The LIE problem-specific constants make the intervals impractical"** — This overlaps with weakness #4 above and is merged there.

- All pure formatting/style nitpicks.

- All reproducibility nitpicks about undisclosed hyperparameters or trivial implementation details.

## Novel Insights

None beyond the paper's own contributions. The main insight — that coupling two intertwined iteration trajectories (one extrapolation, one regular update) with adaptive momentum can yield better optimization than single-track variants — is the paper's own claim, not something that emerged from the reviews.

## Suggestions

1. **Clarify what "Time(s)" measures.** Specify: per-image, per-iteration, or per-patch timing; on what hardware; averaged over how many runs. If the timing is for a small patch, state this explicitly in the main text.

2. **Fix the reference inconsistencies.** Ensure SAdam and SNAdam are attributed to the correct papers. Clarify which "SAdam" is used — the stochastic Adam from Kingma & Ba, or the strongly-convex variant from Le-Duc et al.

3. **Add convergence curves and an ablation study.** Show objective value vs. iterations for at least STNAdam-SARAH vs. SNAdam vs. SGD. Run an ablation that disables the two-track mechanism (reverting to single-track NAdam-style updates) to isolate the contribution of the two-track design.

4. **Soften the "removing hand-tuning" claim.** Acknowledge that the parameter intervals depend on problem-dependent constants ($L, \tau$) and estimator-specific constants ($V_1, V_T, \rho$), and describe how a practitioner might estimate or bound these in practice.

5. **Verify Lemma 1 conditions for at least one estimator (e.g., SARAH).** Even a brief sketch in the main text or a reference to an existing proof would substantially strengthen the theoretical contribution.

6. **Fix the Step 3 → Step 5 jump.** Either renumber or add a (possibly empty) Step 4.

## Calibration

**Round 1 bracket**: [4.0, 5.5]. The paper is clearly stronger than rejected anchors below 3.5 (thin contributions) but notably weaker than accepted anchors around 6.0–6.75 (which have clearer motivation, convincing experiments, and polished presentation).

**Round 2 narrowing**: The rejected paper at avg 4.25 (*Adam under Non-uniform Smoothness*) had proof gaps and "no substantial contribution" criticism; STNAdam has more algorithmic novelty. The rejected paper at avg 5.0 (*SGDM Bounds*) was criticized for marginal improvement and outdated methods; STNAdam has a more original algorithm but worse experimental validation. The accepted paper at avg 6.0 (*Double Momentum SGD*) had strong theory and clear experiments. STNAdam falls below this level due to unexplained timing data, reference inconsistencies, and lack of ablation evidence.

**Final score**: 4.5. The algorithmic idea is genuinely novel and the theory is broad, but the experimental validation has credibility issues (timing numbers) and the presentation has multiple inconsistencies that prevent acceptance in the current form.

### Anchor Papers Retrieved

| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| 5nldnvvHfw | 2.50 | Bracket | Much weaker — thin contribution, rejected |
| cya3eEczAx | 1.67 | Bracket | Much weaker — thin contribution, rejected |
| 1NYhrZynvC | 2.50 | Bracket | Much weaker — thin contribution, rejected |
| Og7ZZd7hDm | 3.25 | Bracket | Weaker — novelty concerns, rejected |
| mEBSeSk49H | 4.25 | Bracket & Narrow | Comparable — STNAdam has more algorithmic novelty but worse experiments |
| n3TkrH7fEr | 6.25 | Bracket | Stronger — tighter analysis, accepted |
| YwJkv2YqBq | 6.75 | Bracket & Narrow | Stronger — clearer motivation and presentation, accepted |
| Fj6Yv5rPRe | 4.25 | Bracket & Narrow | Comparable — STNAdam has more algorithmic novelty |
| x45vUUY4nT | 5.00 | Narrow | Marginally stronger — better writing but also rejected |
| gBT6rAEqvx | 3.80 | Narrow | Weaker — rejected |
| CIqjp9yTDq | 6.25 | Narrow | Stronger — clearer experiments, accepted |
| zCZnEXF3bN | 6.00 | Narrow | Stronger — better theory-practice match, accepted |

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>