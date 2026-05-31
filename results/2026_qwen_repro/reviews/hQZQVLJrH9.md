I now have a solid sense of the paper and anchor comparisons. Let me proceed to write the final review.

## Summary

This paper presents a unified first-order framework connecting activation steering (modifying intermediate-layer activations during inference) and influence functions (estimating the effect of re-weighting training examples on model outputs). The key technical contribution is the **Influence-Aligned Steering (IAS)** construction, which maps any influence-based parameter perturbation to a minimum-norm activation perturbation via Jacobian pseudoinverses, and vice versa. The framework yields a feasibility diagnostic $\gamma(x)$ (the smallest principal angle between parameter and activation Jacobian subspaces), a spectral optimality result for steering direction selection, and Rademacher complexity bounds for low-rank steering interventions. Experimental validation on GPT-2 Medium (detoxification) and ResNet-50 (spectral direction significance) supports the first-order claims.

## Strengths

- **Clean geometric unification with constructive mappings**: Theorem 5.2 ($\Delta h^* = \mathbf{J}_{h \rightarrow y}^\dagger \mathbf{J}_{\theta \rightarrow y} \Delta \theta$) and Theorem 4.2 provide explicit, closed-form bridges between steering and influence. This analytic unification is clean, useful, and has not been done before in this form.
- **Practical feasibility diagnostic $\gamma(x)$**: The alignment cosine $\gamma(x)$ — the cosine of the smallest principal angle between the parameter-Jacobian and activation-Jacobian column spaces — directly bounds the matching error ($\sqrt{1-\gamma^2}$, Theorem 5.1, Eq. 3). This provides a computable geometric certificate that predicts steering feasibility before inference. Figure 2 shows $\gamma$ increasing monotonically with layer depth (0.64→0.94), validating its practical utility.
- **Spectral optimality result**: Theorem 5.3 proves that under an $\ell_2$ budget, the steering direction maximizing first-order logit change is the top eigenvector of a Fisher-influence matrix $\Sigma$, with a scalable power-iteration recipe (Section 5.3). Figure 3 demonstrates statistical significance against random baselines on ResNet-50 ($p=0.00498$).
- **Generalization bounds for low-rank steering**: Theorem 6.1 derives a Rademacher complexity bound showing excess risk from rank-$k$ steering scales as $2\alpha L \sqrt{2k/dn}$, formally quantifying that small-magnitude interventions have benign generalization impact — a property mostly assumed rather than proven in the steering literature.
- **No-free-lunch theorem**: Theorem 6.2 provides a clear impossibility result: when $\gamma(x) \leq \rho < 1$, no activation perturbation can replicate the full effect of a parameter perturbation (ratio bounded by $\rho$), giving practitioners a principled steer-vs-retrain decision rule.

## Weaknesses

### Fatal
None.

### Major

- **IAS underperforms CAA baseline on the primary task (Table 1)**: Table 1 shows IAS achieves higher toxicity (0.0164) and higher perplexity (13701) than CAA (0.0150 and 13291, respectively). The paper positions IAS as providing a "practical workflow" for steering and debugging, yet its core application experiment shows the proposed method is *inferior* to the simple contrastive baseline on both metrics. The authors present these results without discussion or explanation (Section 7.1). IAS is not expected to be a superior *steering* method per se — it is a theoretically grounded mapping — but the empirical narrative needs reframing: the evaluation should measure how well IAS replicates a *known* influence function shift (in logit space), not downstream behavioral improvement where CAA's handcrafted construction may benefit from non-first-order effects. Without this reframing, the evaluation fails to validate the stated motivation.

- **Derivation error in Section 3.2, Equation (2)**: The dual section states $\Delta h^* = \mathbf{J}_{h \rightarrow y}^\top \mathbf{J}_{\theta \rightarrow y} \Delta \theta$, incorrectly omitting the pseudoinverse factor $(\mathbf{J}_{h \rightarrow y} \mathbf{J}_{h \rightarrow y}^\top)^\dagger$ that appears in the immediately preceding $\lambda^*$ expression. The correct formula appears later in Theorem 5.2 ($\Delta h^* = \mathbf{J}_{h \rightarrow y}^\dagger \mathbf{J}_{\theta \rightarrow y} \Delta \theta$), but the inconsistency in Section 3.2 is a genuine derivation error. For practitioners implementing from the paper or students learning from it, this creates confusion. The fix is straightforward but must be addressed.

- **Inadequate statistical reporting across all experiments**: No variance estimates, confidence intervals, or significance tests are provided for any quantitative result. Toxicity scores and perplexity in Table 1 are single-point means over 500 prompts. The cosine similarity of 0.978 in Figure 1 has no confidence interval. The $\gamma$ values in Figure 2 report median but not interquartile range or per-prompt variance. Given that mean differences of 0.0014 (toxicity) and ~410 (PPL) could easily fall within Monte Carlo variance, the absence of any uncertainty quantification undermines confidence in all empirical claims.

- **Slope bias of 1.50 in first-order validation (Figure 1) is inadequately addressed**: The paper highlights the cosine similarity of 0.978 as evidence that the first-order regime holds, but the fitted slope of 1.50 means predicted shifts systematically under-estimate actual shifts by ~50%. This is not a first-order equivalence — it is a linear relationship with a bias. The authors mention this slope but do not explain it or investigate whether it arises from second-order curvature, Jacobian variation across the batch, or a normalization issue. If the first-order prediction can be off by a factor of 1.5, the "small-edit regime" may not be as tight as claimed.

### Minor

- **Corollary 1's $\ell_1$-minimality claim relies on a strong affine independence assumption**: The guarantee that $\|\rho_{\mathbf{s}}\|_1 = |\alpha|$ is the minimal $\ell_1$ measure depends on the influence vectors being affinely independent, which is unlikely in overparameterized networks where gradients are highly collinear (a point the paper itself acknowledges in its assumptions). The claim should be softened to hold under specific rank conditions or in expectation.

- **Scaling claim to billion-parameter models is unsubstantiated**: The paper asserts the workflow "scales to billion-parameter models" (Section 1) but only evaluates on GPT-2 Medium (355M). Computing the Jacobians $\mathbf{J}_{\theta \rightarrow h}$ and Hessian inverse surrogates at scale is nontrivial; no approximation strategy (block-diagonal, iterative solver, KV-cache Jacobian approximation) is discussed to substantiate this claim.

- **ResNet-50 experiment (Section 7.4) has limited baselines**: The spectral direction is compared only against random labels. Showing it beats random vectors is expected and minimally informative. A more meaningful comparison would include guided backpropagation, random projections, or a CAA-analog in vision.

## Nice-to-Haves

- **Demonstrate the $\gamma$-based decision workflow end-to-end**: Section 4.2 claims the workflow enables deciding between steering and weight-space editing, but no experiment shows a case where low $\gamma$ correctly predicts steering failure and the system routes to weight edits. A controlled demonstration — showing a layer with low $\gamma$ where steering fails and weight editing succeeds — would validate the paper's central practical claim.

- **Reframe the evaluation as a controlled fidelity test**: Since IAS is designed to match influence functions in logit space under small edits, the evaluation should measure *how well* steering replicates a known weight perturbation or known data re-weighting effect (e.g., direct logit-shift comparison) rather than using a downstream behavioral metric where nonlinearity, token-level averaging, and reward model miscalibration dilute the signal.

- **Tighten the "primal-dual" narrative**: The geometric framing is clean and useful, but the convex-analysis "dual multiplier" terminology ($\lambda^*$ as a "Fisher-metric certificate") adds rhetorical weight without yielding a computationally distinct algorithm. The presentation would be stronger if it centered squarely on the subspace geometry and principal angles, which is where the actual insight lives.

## Removed Points

- **Harsh critic's claim that Eq. (2) derivation error "propagates a structurally incorrect steering rule"**: The error is real, but Theorem 5.2 immediately corrects it. The issue is presentation/consistency, not a fatal mathematical flaw. Kept as Major above.

- **Harsh critic's "overstatement of duality" claim about novelty**: The paper's "duality" framing is somewhat rhetorical but the paper earns it through closed-form theorems (4.2, 5.2, 6.2). Not a fundamental issue. Moved to a Nice-to-Have about tightening the narrative.

- **Harsh critic's claim about missing modern baselines (RepE, SVD-denoised activation addition)**: CAA is a well-known baseline and appropriate for establishing a floor comparison. The criticism that IAS should beat CAA is misplaced — IAS is a theoretically grounded mapping, not a hand-tuned steering method. That said, keeping the point that CAA beats IAS is a genuine concern (kept in Major above).

- **Harsh critic's claim about "insufficiently rigorous" experimental setup (GPT-2 Medium, layer 8)**: GPT-2 Medium is a standard testbed in activation steering literature (Turner et al., the field's foundational paper, uses GPT-2). This is a reasonable experimental choice.

- **Strength finder's general strength about "importance of the problem"**: Generic and not grounded in specific evidence.

## Novel Insights

The paper's most genuinely insightful contribution is the **$\gamma(x)$ diagnostic as a steer-vs-retrain decision rule**. The geometry is elegant: the smallest principal angle between the activation-Jacobian and parameter-Jacobian column spaces in logit space directly controls the achievable matching fidelity. When $\gamma$ is small, steering is geometry-forbidden from replicating the desired effect, and the paper proves a "no-free-lunch" bound. This turns an abstract subspace alignment question into a practical scalar check that costs the same as computing the IAS vector itself. The insight that a single number — computable in two backward passes — can certify steering feasibility (or rule it out) is the paper's most actionable contribution for practitioners.

## Suggestions

- **Fix Equation (2)**: Replace $\Delta h^* = \mathbf{J}_{h \rightarrow y}^\top \mathbf{J}_{\theta \rightarrow y} \Delta \theta$ with the correct expression $\Delta h^* = (\mathbf{J}_{h \rightarrow y})^\dagger \mathbf{J}_{\theta \rightarrow y} \Delta \theta$, or add a clarifying note that the simplification assumes orthonormal rows of $\mathbf{J}_{h \rightarrow y}$.

- **Report variance and significance**: Include error bars or variance estimates across random seeds or prompt partitions for all quantitative experimental results (Table 1, Figure 1, Figure 2).

- **Explain the slope bias in Figure 1**: Investigate whether the 1.50 slope arises from second-order effects, batch-level Jacobian variation, or normalization, and add a brief discussion.

- **Reframe Table 1 as a fidelity metric**: Complement the behavioral metrics with a direct logit-space comparison (e.g., $\|\Delta y^{\text{IAS}} - \Delta y^{\text{IF}}\| / \|\Delta y^{\text{IF}}\|$) that the method was designed to optimize.

- **Discuss scaling approximation strategies**: Briefly discuss how $\mathbf{J}_{\theta \rightarrow h}$ and Hessian inverse surrogates can be computed or approximated at billion-parameter scale (block-diagonal, Kronecker-factored, iterative solvers).

## Score and Decision

**Round 1 — Bracketing:**
- Weak anchor (3.0–3.4): *FLIA* (fdvSCcB7i8, 3.0) rejects on missing prior work and unclear experiments; *Gradient-based interpretation generalization* (EwAGztBkJ6, 4.0) rejects on contrived motivation and unclear experiments.
- Middle anchor (6.0–7.5): *Activation steering for instruction-following* (wozhdnRCtw, 7.0) accepts with comprehensive experiments; *Unifying mechanistic interpretations* (8xxEBAtD7y, 7.33) accepts on theoretical insights + verification via compact proofs; *Sparse interaction primitives* (3pWSL8My6B, 7.0) accepts with solid theory but debatable practicality.
- Strong anchor (7.5+): *Temporal influence* (uHLgDEgiS5, 8.0), *Sparse feature circuits* (I4e82CIDxv, 8.0) — these have strong theory AND comprehensive experiments across multiple settings.

**Initial bracket: 5.5–7.0.** The paper has strong theoretical contributions (comparable to middle/upper anchors) but weaker empirical validation (IAS underperforms baseline, no variance, slope bias unexplained — comparable to weaker middle anchors).

**Round 2 — Narrowing within (5.0, 7.5):**
- *Instruction-following activation steering* (wozhdnRCtw, 7.0): Accept. Well-tested across 4 models, comprehensive experiments, minor novelty concern. The paper under review has deeper theory but weaker experiments.
- *Unifying mechanistic interpretations* (8xxEBAtD7y, 7.33): Accept. Strong theory + verification method (compact proofs). The paper under review's verification (Figure 1) is weaker — shows correlation with slope bias rather than a rigorous verification.
- *Gradient-based interpretation generalization* (EwAGztBkJ6, 4.0): Reject. Theory is partially derivative, experiments unclear.
- *Where We Have Arrived* (3pWSL8My6B, 7.0): Accept. Theory is strong, assumptions debatable. The paper under review shares this profile — theory is solid but experiments don't fully validate the core claim.

**Comparison:** Relative to *wozhdnRCtw* (7.0): the IAS paper has superior theoretical depth but inferior empirical validation. Relative to *8xxEBAtD7y* (7.33): the IAS paper has narrower scope but less rigorous verification. Relative to *3pWSL8My6B* (7.0): similar profile — interesting theory, debatable empirical support. The IAS paper is roughly comparable to the 6–7 range: theory is at the higher end, experiments at the lower end.

The theory (IAS mapping, $\gamma$ diagnostic, spectral optimality, generalization bounds, no-free-lunch) is genuinely useful and novel. The "practical workflow" framing is overstated because the empirical validation doesn't demonstrate this workflow. But the theoretical contributions stand on their own. The slope bias (1.50) and the IAS-underperforms-CAA finding are legitimate concerns but don't invalidate the first-order theory — they just mean the empirical story needs reframing.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>