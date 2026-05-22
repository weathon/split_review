Now I have all the information I need. Let me compose the final consolidated review.

**Calibration Summary:**

Round 1 bracketing placed this paper between the weak band (1–3.5) and the middle band (3.5–7.5). The paper's algorithmic novelty and theoretical ambition lift it above papers scoring ≤3, but the significant practical gaps prevent it from reaching the upper-middle band. Round 2 narrowed to anchors in 4–6 range. Comparing:
- **DIAaRdL2Ra** (avg 5.0, Adafactor convergence): Similar paper type (Adam variant + theory + experiments). The Adafactor paper had restrictive assumptions but the theory was self-contained. STNAdam has a more novel algorithmic contribution but a worse practical gap (underspecified intervals), so slightly below.
- **nE1l0vpQDP** (avg 4.5, AdaGrad-Norm implicit bias): Theory-heavy with limited experiments. STNAdam has more experiments but the AdaGrad-Norm paper's theory is fully specified. Comparable overall.
- **TBJCtWTvXJ** (avg 6.2, SoftSignSGD): Stronger experiments across multiple tasks, far exceeding STNAdam's evaluation scope. STNAdam is clearly below this.
- **mEBSeSk49H** (avg 4.25, Adam under non-uniform smoothness): Similar theory+experiments profile, with proof correctness concerns. STNAdam is comparable.

Final score: **4.0**. The paper has genuine novelty (two-track framework, KL-based analysis for Adam variant) but the hyperparameter scheduling cannot be implemented from the information provided (intervals depend on constants V₁, V_T, ρ, M, s that are never concretely specified), the experiments are confined to a single task/dataset with no ablation of the core two-track idea, and there are smaller inconsistencies (abstract/theorem mismatch on convergence mode, SGD tested outside theory's scope, citation inconsistencies).

---

## Summary

This paper proposes STNAdam, a stochastic Adam variant with a novel two-track iteration framework that maintains two intertwined trajectories — an extrapolation track and a regular update track — governed by Nesterov momentum and Adam-style adaptive conditioning. The authors provide convergence analysis under the Kurdyka-Łojasiewicz property (Theorems 1–2) and present experiments on low-light image enhancement (LIE) on the LOL dataset, claiming superiority over single-track optimizers (SGD, Adam, SNAdam) and several specialized LIE algorithms.

## Strengths

1. **Novel algorithmic architecture.** The two-track iteration framework (Algorithm 1, Step 5) is genuinely different from existing single-track Adam variants (NAdam, SNAdam). Maintaining an extrapolation trajectory $\{\bar{x}^k\}$ alongside the regular update trajectory $\{x^k\}$ and having them interact through a coupled proximal-gradient step is a creative design, conceptually distinct from standard Nesterov acceleration. This is evident in Figure 1(d) and the update formulas.

2. **Ambitious convergence theory under the KL framework.** The paper establishes convergence to a stationary point and explicit rates (sublinear/linear depending on KL exponent) for the "nonconvex + weakly-convex" composite problem class (1). The analysis allows the gradient estimator to be *any* variance-reduced estimator satisfying Lemma 1 (SVRG, SAGA, SARAH, SPIDER), which is more general than typical Adam analyses tied to a specific estimator. The energy function (9) and the eight-term descent in Lemma 2 show nontrivial theoretical work.

3. **The idea of iterate-dependent hyperparameter scheduling.** The parameters $\gamma_{k+1}, \lambda_{k+1}, \alpha_{k+1}$ are designed to be selected within closed-form intervals (6)–(8) that depend on the current adaptive learning rate $\hat{\pi}_{k+1}$. Remark 3 attempts to verify positivity of the lower bounds. This is a principled approach that, if fully specified, could reduce manual tuning.

## Weaknesses

### Major

1. **The hyperparameter scheduling intervals cannot be instantiated from the information provided.** The intervals (6)–(8) depend on constants $V_1, V_\Upsilon, \rho$ (from Lemma 1) and $M, s$ (from the energy function (9)). Lemma 1 only states that these constants *exist* for variance-reduced estimators — it does not give their values for any specific estimator or problem. The term $M$ is described as a "parameter within some certain intervals," and $s$ is an arbitrary Young's inequality parameter. A practitioner cannot compute, e.g., $\underline{\gamma} = 1 - \frac{\sqrt{2}\sqrt{(1-\mu^2)^2[(1-2\mu^2)M-4s(V_1+V_T/\rho)]-4}}{16}$ without concrete values. The paper claims this scheduling "removes hand-tuning," but the constants themselves would need to be hand-tuned or derived from problem data — a step the paper does not perform or illustrate on any example. This undermines the practical contribution and makes the algorithm underspecified.

2. **Empirical evaluation is too narrow to support the claimed superiority.** The experiments are confined to a single task (LIE) and a single dataset (LOL). Only three image metrics are reported without variance or statistical significance (single runs). There is **no ablation** isolating the two-track mechanism — e.g., a comparison of STNAdam against a version that uses the same momentum and adaptive learning rate but without the second track. This makes it impossible to attribute the reported gains to the two-track design vs. other algorithmic choices. Modern Adam variants like AdamW, NAdam, and AdaBelief are not compared. The "time(s)" column reports per-update times (~10⁻⁵ s) that are implausibly small for any realistic image size, suggesting tiny patches or few iterations, but no details (image size, patch size, number of iterations) are provided to interpret these numbers.

3. **SGD is tested but lies outside the theoretical framework.** Lemma 1 defines variance-reduced gradient estimators through conditions (3)–(5) including a geometric decay condition (5). The paper explicitly states "it is well known that SGD does not exhibit variance reduction" (line 128), yet STNAdam-SGD is tested in Table 2 and Remark 2 labels it as an STNAdam variant. The theory section assumes the gradient estimator satisfies Lemma 1 (see Lemma 2 heading: "with variance-reduced gradient estimator"). SGD does not satisfy the geometric decay condition (5). The paper does not acknowledge this gap or clarify that the SGD results are outside the theory's scope, creating ambiguity about what the experiments demonstrate.

### Minor

4. **Mismatch between abstract and theorem statements.** The abstract claims "almost surely converges to a stationary point," but Theorems 1 and 2 state convergence *in expectation* (e.g., Theorem 1(ii): "The sequence $\{\bar{x}^k\}$ converges to a stationary point of $\Phi$ *in expectation*"). While some almost-sure results appear in Lemma 4 (summability of $\|\bar{x}^k - \bar{x}^{k-1}\|^2$ a.s.), the convergence to a stationary point is stated as in-expectation, not almost sure. This mismatch should be corrected.

5. **Citation inconsistency for SAdam and SNAdam.** In the introduction, SAdam is attributed to Wang et al. (2019) and Le-Duc et al. (2024), but in the experiments (line 285) SAdam is cited as "(Kingma & Ba, 2014)" — which is the original Adam paper, not SAdam. SNAdam is attributed to Reddi et al. (2019) in the introduction (line 37) but to Xie et al. (2024) in the experiments. This needs clarification.

6. **Minor notation inconsistency.** Line 178 references "$\tilde{\omega}^{k+1}$" (omega) when discussing the second-order decay factor from Table 1, but Table 1 uses $\tilde{\varpi}^{k+1}$ (varpi). These are the same variable but denoted differently.

### Trivial

7. Some grammatical issues and awkward phrasings throughout (e.g., "arbitrary a variance-reduced gradient estimator" → "an arbitrary variance-reduced gradient estimator").

## Nice-to-Haves

- Provide a concrete worked example (synthetic or otherwise) where the constants $V_1, V_\Upsilon, \rho, M, s$ are computed or bounded, demonstrating that the intervals (6)–(8) can actually be used.
- Add an ablation comparing STNAdam to a single-track variant that shares all other design choices, to isolate the effect of the two-track mechanism.
- Test on at least one other problem type from the paper's target class (e.g., sparse logistic regression with MCP/SCAD regularization) to show generality beyond LIE.
- Report error bars or confidence intervals over multiple runs.
- Compare with modern Adam variants (AdamW, NAdam, AdaBelief) in the experiments.
- Clarify the relationship between the two tracks and standard Nesterov acceleration, providing intuition for why two tracks are beneficial over a single Nesterov-accelerated track.

## Removed Points

These points were flagged by the harsh critic but are removed or downgraded per the filtering rules:

- *"The method description is unclear and the two-track motivation is vague"* — Partially removed. While the paper could provide more intuition, Algorithm 1 and Figure 1(d) give a concrete description. The two-track idea is conceptually clear even if the motivation could be elaborated. This is weakened to a nice-to-have (elaboration on intuition).
- *"The convergence analysis does not apply to the SGD estimator used in the experiments"* — Downgraded from fatal to Major. The paper is transparent that SGD is not variance-reduced; the issue is the lack of acknowledgment that SGD results fall outside the theory's scope, not a claim that the theory covers SGD.
- *"The abstract states 'almost surely converges' but Theorem 1 only shows convergence in expectation"* — Kept as Minor. This is a real claim mismatch but not fatal.
- *"Lemma 1's proof is not in the main text"* — Removed. The paper states the proof is "analogous" to earlier works; proofs in appendices are standard.
- *"No comparison to modern Adam variants (AdamW, NAdam, AdaBelief)"* — Demoted to nice-to-have. The paper compares against the most standard baselines (SGD, Adam, SNAdam) plus specialized LIE methods; adding more baselines would strengthen but is not required.
- *"Weakness about unfair comparison"* — Not applicable; the paper compares fairly.
- *"Pure formatting/style nitpicks"* — Removed per filtering rules.
- *"Missing reproducibility details (image size, iterations, batch size)"* — Weakened to a suggestion. These details are standard for an appendix, which is stripped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the constants.** Provide concrete values or bounding procedures for $V_1, V_\Upsilon, \rho, M, s$ for at least one estimator (e.g., SAGA or SARAH) on the LIE problem, or provide a general method to compute them from problem parameters ($L, \tau$) alone. Without this, the scheduling scheme is a theoretical construct that cannot be applied.

2. **Broaden the experiments** to include at least one additional problem type (e.g., a nonconvex regularized regression with MCP/SCAD) and an ablation that removes the second track to isolate the two-track contribution.

3. **Align the abstract with the theorems.** Either strengthen Theorems 1–2 to prove almost-sure convergence or soften the abstract to "converges in expectation."

4. **Fix the citation inconsistencies** for SAdam and SNAdam, and address the notation discrepancy in line 178.

## Score and Decision

**Round-1 bracket:** Between ~3.5 and ~6.0 (above papers scoring ≤3 with major fatal flaws, below papers with strong experiments at 6+).  
**Round-2 anchors consulted:** Adafactor convergence (5.0), Adam under non-uniform smoothness (4.25), Online learning meets Adam (4.25), AdaGrad-Norm implicit bias (4.5), SoftSignSGD (6.2), Parameter-free AdaGrad/Adam (4.0).  
**Final positioning:** The paper's algorithmic novelty and theoretical ambition are real, but the underspecified hyperparameter scheduling (a structural practical gap), the narrow evaluation (single task/dataset, no ablation of the core idea), and the theory-experiment disconnect for SGD place it below the Adafactor paper (5.0) and closer to the 4.0–4.5 range. The paper is comparable in overall quality to the AdaGrad-Norm implicit bias paper (4.5) but with a larger practical gap, leading to a score of **4.0**.

The paper contains a genuinely novel algorithmic idea and nontrivial theory, but the core claim of "dynamic scheduling removing hand-tuning" is unsupported because the scheduling intervals depend on uninstantiated constants. The experimental validation is too narrow to substantiate the claimed superiority. A substantial revision addressing these gaps is needed before the paper could be considered for acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>