Here is my final consolidated review:

---

## Summary

This paper proposes modeling temporal difference (TD) errors in deep RL using the generalized Gaussian distribution (GGD) instead of the standard Gaussian assumption. The method introduces a "beta head" to estimate the GGD shape parameter β, a risk-averse weighting scheme ω=Q^β motivated by second-order stochastic dominance, and a batch inverse error variance (BIEV) regularizer that uses TD-error variance rather than value-estimate variance. Experiments with SAC and PPO on MuJoCo and discrete-control tasks show performance improvements over Gaussian-based variance-network baselines.

## Strengths

1. **Empirical demonstration of non‑Gaussian TD errors.** Figure 1 plots fitted GGD PDFs over actual TD errors from SAC training, clearly showing heavy tails and leptokurtosis that the Gaussian assumption cannot capture. This directly motivates the approach and is a concrete empirical finding.

2. **Theoretical guarantee for the GGD-NLL loss.** Theorem 1 proves positive-definiteness of the GGD PDF for β∈(0,2] (the range observed in practice), ensuring the negative log-likelihood is a valid loss function. This is a clean, well-grounded result.

3. **Closed‑form aleatoric uncertainty inversely related to β.** Remark 3.4 provides σ² = α²Γ(3/β)/Γ(1/β), showing that with constant α, aleatoric uncertainty scales inversely with β. This gives a principled basis for the risk-averse weighting scheme.

4. **Stability of β estimation.** Figure 3 shows that the coefficient of variation of β estimates is lower and converges more smoothly than that of variance estimates across multiple environments, supporting the claim that the GGD-based approach yields more stable parameter estimation.

5. **Consistent improvements across SAC and PPO.** Figures 2 and 4 show that GGD-based variants achieve better or comparable sample efficiency and asymptotic performance relative to Gaussian-based counterparts on multiple tasks (HalfCheetah, Hopper, etc.). The benefit holds across both an off-policy Q-based algorithm (SAC) and an on-policy V-based algorithm (PPO).

## Weaknesses

### Fatal
None.

### Major

1. **BIEV claims about kurtosis are not matched by the implementation.** The paper defines the BIEV weight as ω^BIEV_t = 1/V[δ_t] (Eq. 4 / Eq. 6, line 255) — plain sample variance of TD errors. It then discusses the MSE-best biased estimator (MBBE, Proposition 1) that accounts for kurtosis and states "we advocate for the adoption of the MBBE in epistemic uncertainty estimation" (line 277). However, the actual loss function does **not** use the MBBE formula; it uses V[δ_t] without kurtosis adjustment. The contribution list (item 4) claims BIEV accounts for "kurtosis of the estimation error distribution," which is misleading because the kurtosis-aware MBBE estimator is discussed as motivation but never integrated into the loss used in experiments. This creates a gap between what the paper advertises and what it actually evaluates.

2. **Insufficient experimental rigor to support "significant performance improvements."** Results are presented solely as visual learning curves with median and standard deviation over 10 seeds. There are no tabular summaries of final performance, no confidence intervals, no statistical tests, and no quantification of effect sizes. The abstract and contributions claim "significant performance enhancements," but the evidence only supports that the method *tends to improve or match* baselines with varying consistency across environments (clear gains on HalfCheetah and Hopper, marginal on Ant, Walker2D, Humanoid). Without statistical treatment, the strongest warranted claim is that the method helps on some tasks and never substantially hurts — not that improvements are "significant."

### Minor

1. **The connection between second-order stochastic dominance and the risk-averse weighting is heuristic, not a formal derivation.** Theorem 2 establishes that GGDs with larger β have second-order stochastic dominance (i.e., are less spread out). The paper then uses ω=Q^β to give higher weight to samples with larger β. This is a reasonable motivation, but it is not a theorem-derived guarantee that the weighting is optimal or that it minimizes any well-defined risk measure. The paper presents this as "theoretically grounded" (abstract); acknowledging the heuristic nature would better match what is actually delivered.

2. **Improvements are inconsistent across environments.** Some tasks (Ant, Walker2D) show marginal or negligible differences from baselines. The paper acknowledges this ("the impact of BIEV regularization varies by environment") but the overall narrative leans toward claiming universal gains. A more nuanced characterization of where the method helps and why would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- Add a tabular summary of final returns with confidence intervals or interquartile ranges, enabling quantitative comparison.
- Run a statistical significance test (e.g., Mann-Whitney U, bootstrapped CIs) on the final performance across seeds.
- Clarify whether the MBBE estimator was used in any experiments and, if not, state this explicitly and avoid language suggesting it was incorporated.
- Include an ablation that compares the risk-averse weighting scheme (ω=Q^β) against uniform weighting or a simpler alternative (e.g., ω=Q^β with β set to 2, recovering Gaussian weighting) to isolate the effect of the learned β.

## Removed Points

These points were raised by reviewers but removed from the main assessment with justification:

- **"Theoretical grounding for risk-averse weighting is weak / doesn't follow from the theorem"** (Harsh Critic). *Removed because*: the paper's use of the SSD theorem is as a motivation — Theorem 2 shows larger β → less spread, and the weighting ω=Q^β gives higher weight to less-spread samples. This is a straightforward and reasonable heuristic connection. The paper does not claim a formal proof of optimality. The criticism overstates what the paper asserts.
- **"Missing related works"** (implied by harsh critic's scope criticism). *Removed because*: I cannot verify this without external sources; per instructions, this should not be mentioned.
- **Strength Finder claim 4: "The paper explicitly applies [MBBE] to weight samples in the BIEV term."** *Removed because*: this statement is inaccurate — the BIEV term uses plain sample variance V[δ_t], not the MBBE formula. The MBBE is discussed and advocated for but not applied in the loss. The strength itself (Proposition 1's derivation) is valid, but the claim of "explicit application" is not.
- **Generic strengths from Strength Finder** (e.g., "the paper addressed an important problem"). *Removed because*: these are generic, lack concrete evidence specific to this paper, and some conflict with verified weaknesses.
- **Nitpicks about typos/formatting** (parser artifacts). *Removed per instructions*.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the BIEV/MBBE inconsistency.** Either (a) implement the MBBE estimator in the BIEV loss and report its impact in experiments, or (b) remove the MBBE discussion from the BIEV section, clearly state that BIEV uses plain sample variance of TD errors, and tone down claims about accounting for kurtosis. The core innovation of BIEV — replacing V[Q^μ_t] with V[δ_t] — is independently valid and does not require the MBBE rationale.

2. **Add statistical rigor.** Provide a table of mean/median final returns with standard deviations and a simple significance test (or at least bootstrap confidence intervals). Replacing "significant performance improvements" with more precise language ("consistent improvements on several tasks, comparable on others") would better match the evidence.

3. **Temper the theoretical framing of the risk-averse weighting.** Acknowledge that the SSD theorem provides *motivation* for a heuristic weighting based on β, not a formal derivation of optimality.

## Score and Decision

**Originality:** Moderate — applying GGD to TD errors is novel, though the individual components (beta head, variance weighting) build on existing ideas.  
**Importance of question:** Good — improving uncertainty estimation in RL is an important direction.  
**Claims support:** Weak — the claims of "significant" improvements and accounting for kurtosis are not well-supported by the evidence presented.  
**Soundness of experiments:** Adequate but lacking statistical rigor and missing tabular results.  
**Clarity of writing:** Good — the paper is generally well-structured and readable.  
**Value to community:** Moderate — the core idea has potential, but the current presentation overstates what is demonstrated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>