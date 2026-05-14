## Summary

This paper identifies the precise conditions under which normalized training loss curves (TLCs) collapse across LLM scales: the AdamW timescale τ, tokens-per-parameter ratio (TPP), and learning-rate schedule must be matched across model sizes. It introduces **Celerity**, a model family (300M–3.9B parameters) trained at fixed TPP bands with optimally chosen τ, demonstrating tight collapse and competitive compute-efficiency. The paper further shows that collapse residuals enable early detection of training pathologies (detecting a numerical instability at 60% of training in a 1.8B run) and that a parametric surrogate for normalized TLCs, fit at 111M scale, enables early stopping in hyperparameter tuning after only 10–30% of training.

---

## Strengths

- **Identifies the specific, separable control factors governing TLC collapse (τ, TPP, LR schedule) with clean empirical evidence.** Figures 3 and 4 show that varying η, λ, or B produces matching TLC shapes when τ is held constant, and that fixing both TPP and τ yields alignment across a 1000× FLOP range (111M to 3.3B). This is a useful synthesis and extension of prior work by Qiu et al. (2025) and Bergsma et al. (2025a) to practical LLM training regimes with co-scaled width, depth, batch size, and weight decay.

- **Introduces Celerity as the first LLM family with demonstrable TLC collapse across a practical scaling ladder.** The paper trains models at three fixed TPP bands (20, 80, 234) spanning 300M–3.9B parameters, showing tight collapse at 20 and 80 TPP (Figure 6). This directly addresses the call from Qiu et al. (2025) for tests at larger scales with practical parameterizations.

- **Demonstrates practical diagnostic value of collapse residuals via a concrete case study.** The 1.8B run deviation (Figure 1, right) shows that collapse residuals flagged a numerical instability near 60% of training, well before the raw TLC showed any upward trend (~90%). The paper documents the debugging process, attributing the issue to a loss kernel triggered at specific microbatch sizes, and shows the repaired run tracks the reference curve.

- **Proposes and validates a collapse-based early stopping method for hyperparameter tuning.** The procedure aligns partial training curves to a small-scale parametric surrogate to predict final loss. Figure 9 shows that "predicted best" achieves negligible loss gaps when stopping after 10–30% of training for λ sweeps at 1.7B and 3.3B scale, outperforming the "current best" heuristic used in practice.

- **Theoretical grounding through a noisy-quadratic model (Eq. 3).** The paper derives an expression showing that τ controls a bias–variance trade-off: smaller τ → faster initial decay but higher variance floor; larger τ → slower initial decay but lower floor, matching the observed behavior under constant and decaying LR schedules.

---

## Weaknesses

### Fatal
None.

### Major

- **Generalizability of collapse claims is limited to a single architecture family under a specific parameterization.** All experiments use a GPT2-like architecture with ALiBi, SwiGLU, Squared ReLU, and CompleteP/µP. The largest model is 3.9B parameters. The paper frames its findings as applying to "LLM families" and uses language like "full-scale LLMs," but never tests whether collapse holds under different architectural choices (e.g., RoPE, GQA, standard PyTorch init without µP) at comparable or larger scales. The paper acknowledges that Llama-2 does not collapse because its τ and TPP vary, but does not test whether collapse *could* be achieved by setting τ and TPP appropriately in that architecture. This overclaiming weakens the paper's core generality claim. While the 1000× FLOP range (111M to 3.3B) is substantial, whether these findings transfer to 7B+ models with different architectural components remains an open question.

- **Evaluation of Celerity's compute-efficiency is confounded by data quality and a narrow benchmark suite.** Figure 2 plots average accuracy on 7 multiple-choice QA tasks (arc-c, arc-e, boolq, hellaswag, piqa, siqa, winoqrande) against training FLOPs. These tasks do not represent the breadth of LLM capabilities (code generation, math reasoning, open-ended generation). Moreover, Celerity uses a carefully curated data mix emphasizing "educational, math, and coding data throughout training" (Table 6), while comparison models use different, often less curated data mixtures (e.g., SlimPajama, The Pile). The compute-efficiency comparison is therefore confounded by data quality. The paper would benefit from a controlled comparison using the same data or systematically controlling for data quality.

### Minor

- **The parametric surrogate model (Eq. 4) is empirically motivated but lacks principled derivation.** The functional form `((1+ε₁)/(t̂+ε₁))^m + b·(η(t̂)+ε₂)^q` is presented as the result of experimenting with several forms, but no justification is given for why this specific form was chosen over alternatives. The fitting procedure alternates between b-parameters and q-parameters without formal convergence guarantees. While the surrogate demonstrably reduces MAE by two-thirds compared to fixed baselines (Table 12) and transfers to 3.3B, its reliability outside λ sweeps—e.g., for sweeps over LR schedule shapes, batch size, or TPP values outside the training grid—is not validated. The early stopping method depends on this surrogate (Steps 3–5 in Section 5), but the evaluation only covers λ sweeps within the same architecture and data regime.

- **The 234 TPP band shows imperfect collapse.** At 234 TPP, divergences appear late in training for larger models (Figure 1, middle). The paper attributes these to a numerical bug in the 1.8B run and shows the repaired run tracks better, but the 3.9B curve at 234 TPP still shows visible deviation near the end. The paper notes that "loss improves disproportionately on training data, while held-out data remains aligned with projections," which suggests possible overfitting rather than collapse. This is not fully reconciled with the claim that collapse is a signature of compute-efficient training.

- **Limited validation of the early stopping method.** The evaluation in Figure 9 is restricted to λ sweeps at 1.7B/20TPP and 3.3B/30TPP. The method is not tested on sweeps over other hyperparameters (η, B, TPP), different LR schedules, or different architectures. The paper does not compare against standard learning-curve extrapolation baselines (e.g., Domhan et al. 2015, Swersky et al. 2014) or Bayesian optimization, which would help establish that the collapse prior provides a meaningful advantage.

### Trivial
None.

---

## Nice-to-Haves

- **Quantify collapse tightness with a formal metric.** The paper relies on visual inspection of collapse. A quantitative metric (e.g., mean squared deviation across curves normalized by inter-run variation) would strengthen claims about "supercollapse" level alignment at 20 and 80 TPP, and would clarify the degree of residual deviation at 234 TPP.

- **Test on a different architecture (e.g., Llama-2-like with RoPE, GQA, standard init without µP).** This would directly address the main architectural generality concern and would be the most impactful extension of the work.

- **Provide full collapse plot for the repaired 1.8B 234 TPP run** alongside the other Celerity curves, rather than only showing residuals in Figure 1.

- **Report error bars or confidence intervals for the early stopping results** (Figure 9) across multiple seeds or bootstrapped samples.

- **Compare early stopping method to standard baselines** (learning-curve extrapolation, Bayesian optimization) to isolate the value added by the collapse prior.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- *"The noisy quadratic model (Eq. 3) is referenced but not present in the extract; we cannot verify its derivation."* — REMOVED (factually wrong: Eq. 3 is present at line 132 of the paper).
- *"The paper uses the notation τ for 'normalized AdamW timescale' but Bergsma et al. defined it identically; this is fine but should be noted as reuse, not new."* — REMOVED (not a substantive weakness; the paper properly cites Bergsma et al.).
- *"The paper never tests whether collapse can be achieved in Llama-2's architecture by setting τ and TPP appropriately."* — REMOVED (asks the paper to address problems outside its stated scope; the paper uses a GPT2-like architecture with ALiBi, not Llama-2's RoPE/GQA).
- *"The FLOPs computation is not detailed."* — REMOVED (FLOPs accounting for pre-training is standard; the paper specifies how student vs. teacher FLOPs are handled for distilled models and directs to appendix for details).
- *"The trend line ('Celerity Fit') is fit to Celerity points only and then visual inspection suggests Celerity is on the frontier."* — REMOVED (standard practice to fit one's own models; the claim is that Celerity models appear on the Pareto frontier, which is a visual claim supported by the scatter plot).
- *"Missing larger dataset when current size is sufficient"* — REMOVED (generic request).

---

## Novel Insights

The reviews surface one genuinely novel perspective that goes beyond the paper's own contributions: the observation that the collapse phenomenon can be seen as providing an *implicit sanity check on training regime choices* — if your curves don't collapse, something in your scaling recipe (τ, TPP alignment, parameterization) is suboptimal. This reframes collapse not just as a descriptive phenomenon but as a *normative* signal: collapse is what you *should* see when training is well-configured. The diagnostic application (1.8B bug detection) is a concrete instance of this principle in action. The reviews also highlight the natural tension between this normative view and the empirical finding that many successful families (Llama-2) explicitly do *not* collapse — raising the question of whether collapse is necessary for good outcomes or merely sufficient.

---

## Suggestions

1. **Tone down architectural generality claims.** Replace "LLM families" and "full-scale LLMs" with more precise language that acknowledges the single-architecture, single-parameterization experimental basis.
2. **Add a controlled compute-efficiency comparison** where Celerity and a baseline model (e.g., a re-implementation of a public model) are trained on the *same data mix* with the same tokenizer, isolating the effect of the training recipe from data quality.
3. **Broaden the early stopping evaluation** to include sweeps over learning rate and batch size (not just λ), and compare against standard learning-curve extrapolation baselines.
4. **Provide a quantitative collapse metric** (e.g., mean pairwise deviation across curves after normalization) for all three TPP bands, ideally with and without the numerical bug fix, to move beyond visual assessment.
5. **Report error bars** for the early stopping selection gap (Figure 9) across multiple runs or bootstraps.

---

## Score and Decision

**Calibration anchors (all from ICLR 2026):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `NbdCwOgk4m` (Trajectory Invariance) | 4.00 (Reject) | Much weaker: tested on a single 164M model with no cross-scale validation. Our paper has substantially broader empirical support. |
| `o94xgM0sWJ` (Cross-Entropy Scaling Decomposition) | 5.00 (Poster) | Similar in having a strong conceptual contribution but weaker empirical basis. Our paper has more practical applications demonstrated. |
| `qBAV2DEvAC` (Dynamical Scaling Laws) | 5.50 (Poster) | Comparable: both mix theory and experiments across model sizes. Our paper has stronger practical validation (diagnostics, early stopping). |
| `elB9k4nTL1` (CompleteP Extension) | 5.50 (Poster) | Comparable scale of experiments. Both address scaling under µP/CompleteP. Our paper identifies a new phenomenon (collapse) rather than extending an existing parameterization. |
| `T985gm4sDA` (Scaling Laws for DiT) | 5.50 (Poster) | Similar type of contribution (establishing scaling regularities). Our paper has more diverse contributions (phenomenon + applications). |
| `wjaTz8nYjD` (TREC for Data Curriculums) | 6.00 (Poster) | Very similar empirical scope (111M–3.9B models, similar compute). Both identify a phenomenon and show it enables practical applications. Our paper has weaker evaluation breadth. |
| `dSdLqg02tx` (Convex Dominance) | 6.00 (Poster) | Stronger theoretical foundation but similar empirical scale. Our paper has more concrete practical tools (diagnostics, early stopping). |
| `YnJ2s4WeNF` (Downstream Metric Scaling) | 6.00 (Poster) | Stronger in evaluation breadth (models up to 17B, broader benchmarks) but our paper has more mechanistic insight into *why* scaling regularities emerge. |

The paper makes a clear conceptual contribution, supported by reasonably thorough experiments spanning 1000× FLOP range. The diagnostic and early stopping applications are novel and practically relevant. However, the architectural generality is unvalidated (single family, single parameterization, up to 3.9B), the compute-efficiency comparison is confounded by data quality, and the surrogate model is heuristic. Relative to similar-scale empirical papers that received poster acceptance at ICLR 2026 (avg 5.0–6.0), this paper sits in the middle of that band.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>