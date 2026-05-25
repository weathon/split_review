Now I have thoroughly read and cross-checked the paper against the reviewer inputs. Let me compose the final consolidated review.

---

## Summary

This paper studies robust decision-making under *partially* calibrated forecasts. It frames the problem as a minimax optimization over outcome distributions consistent with a family of moment constraints (ℋ-calibration). The paper's central theoretical contribution (Theorem 3.1) provides a duality-based characterization of the optimal robust policy for any finite-dimensional ℋ. The headline result (Theorems 4.1–4.2) is that decision calibration—a statistically tractable condition involving only |𝒜| test functions—suffices for the minimax-optimal policy to collapse to the simple plug-in best response, exactly as under (intractable) full calibration. The paper also derives usable robust policies from structural properties of squared-error training (self-orthogonality, Proposition 4.4) and from bin-wise post-hoc calibration (Proposition 4.5), with experiments on two regression datasets.

---

## Strengths

1. **Clean duality-based characterization of the optimal robust policy (Theorem 3.1).** The paper reduces the infinite-dimensional minimax problem to a finite-dimensional concave dual maximization followed by pointwise convex minimization over the outcome simplex. This provides an efficiently computable, general decision rule for any finite set of test functions, going well beyond the full-calibration setting studied in prior work. The two-step interpretation (adversarial tilt then best response) is practically helpful.

2. **Decision calibration suffices for plug-in best-response optimality (Theorems 4.1–4.2).** This is the paper's most surprising and impactful result. It shows that the vastly more tractable notion of decision calibration (with only |𝒜| indicator functions) already forces the minimax-optimal policy to coincide with the plug-in best response. This upgrades prior swap-regret guarantees (Noarov et al., 2023) to a stronger decision-theoretic optimality claim, and provides a crisp target for forecaster design.

3. **Self-orthogonality from squared-loss training yields a "free" calibration guarantee (Proposition 4.4).** The paper identifies that any model with a linear last layer trained to a stationary point of mean squared error automatically satisfies an ℋ-calibration condition. This insight connects the theoretical framework to standard practice without requiring additional post-hoc calibration, making the framework actionable for regression models.

4. **Simple closed-form robust policy for bin-wise calibration (Proposition 4.5).** For coarse partitions of the forecast range, the robust policy reduces to best-responding to bin-conditional means—requiring no per-instance optimization. This bridges the framework to common post-hoc recalibration procedures.

5. **Simultaneous plug-in optimality for multiple downstream decision makers (Corollary 4.3).** Because decision calibration uses only the indicator functions of each decision-maker's best-response regions, a single forecaster can be decision-calibrated for several utility functions simultaneously, with plug-in best-response being minimax optimal for each. This is a practical advantage unavailable with stronger calibration notions.

---

## Weaknesses

### Fatal
None.

### Major

1. **The adversarial evaluation protocol in the experiments is critically underspecified.** Section 5 describes the adversarial distributions only as "altering the test-time outcome distribution in two ways: (i) a worst case tailored to the plug-in policy, and (ii) a worst case induced by the robust dual." No details are given about how these adversaries are constructed—whether via reweighting of the test set, a shift in a specific covariate, an explicit optimization over q∈𝒬, or some other mechanism. The reader cannot assess whether the adversary is actually strong, whether the comparison is informative, or whether it fairly respects the calibration constraints. Since the adversarial evaluation is the core of the empirical section, this methodological gap substantially weakens the validation. The core theory is unaffected, but the empirical support is not presented at a publishable standard of rigor.

2. **Absence of uncertainty quantification in the experimental results.** Table 1 reports only point estimates of mean utility. No error bars, confidence intervals, standard errors, or replication details are provided. The reported differences (e.g., 0.410 vs. 0.402 on Bike Sharing, 0.164 vs. 0.160 on California Housing) cannot be distinguished from sampling noise without variance estimates. This further undermines the empirical contribution.

### Minor

1. **Narrow scope of the experimental evaluation.** The experiments cover only two regression datasets, one model architecture (two-layer MLP), one ℋ-class (self-orthogonality), and one-dimensional outcomes. While the paper's contribution is primarily theoretical and the experiments are presented as a case study, the evaluation would benefit from broader coverage—e.g., multi-class settings, different ℋ-classes, or comparison with baseline robust policies—to demonstrate the framework's generality.

2. **The linear utility assumption is transparent but its relaxation is not developed.** Assumption 2.1 (utility linear in the outcome) is standard in the calibration literature and clearly stated. However, the conclusion's suggestion that non-linear utilities can be "linearized over an appropriate basis" (citing Gopalan et al., 2024b; Lu et al., 2025) is mentioned without analysis of practical feasibility, dimensionality requirements, or computational overhead. The paper is honest about this being future work, but the escape hatch is not sufficiently developed to give confidence that the framework extends gracefully beyond risk-neutral settings.

### Trivial
None.

---

## Nice-to-Haves

- **Analyze the robustness of the sharp transition under approximate decision calibration.** The paper's headline result (Theorems 4.1–4.2) assumes perfect ℋ-calibration. A brief analysis—or even a discussion in the main body—of how quickly the robust policy deviates from the plug-in best response as calibration error grows would strengthen the paper's practical narrative.
- **Provide an explicit optimization problem defining the adversarial distributions in Section 5**, including how the dual formulation (Theorem 3.1) is used to construct them, and report results with standard errors over independent train/calibration/test splits.
- **Position Section 4.2 more explicitly as the operational demonstration of the framework when decision calibration is unavailable**, rather than as a "bonus." The self-orthogonality example (Proposition 4.4) is precisely the regime where Theorem 3.1 is needed—highlighting this framing would sharpen the paper's narrative.

---

## Removed Points

These points were flagged by the harsh critic but are removed with justification:

1. **Approximate calibration as a main-body gap.** The critic argued the paper "provides no guidance" on how the robust rule behaves under approximate calibration. However, the paper explicitly states (line 85) that "in Appendix B we also discuss scenarios in which only approximate ℋ-calibration is available." Since the appendix exists in the original submission, the claim of "no guidance" is inaccurate. The structure of deferring robustness analysis to the appendix is standard for theory papers. *Removed as factually overclaimed.*

2. **Linear utility as a "structural limitation that should temper the paper's claims more."** The paper clearly states Assumption 2.1, explains why it is standard and justified (multi-class settings, risk-neutral expected utility), and acknowledges non-linear utilities as future work. The paper does not overclaim beyond what its assumptions support. The critic's characterization overstates the severity of a clearly scoped assumption. *Demoted to Minor (above) with softened language.*

3. **Figure 1 being "slightly at odds with the sharp-transition thesis."** Figure 1 is a generic schematic of the interpolating property before the paper's results are derived; Figure 2 then illustrates the sharp transition. There is no contradiction—Figure 1 simply shows the space of possibilities, and the paper's contribution is discovering that the interpolation is not smooth. *Removed as a misreading.*

4. **"Small margins" criticism (0.410 vs 0.402).** Whether these margins are "remarkably small" is a subjective assessment. On California Housing, the relative improvements under the plug-in adversary are ~7% (0.155→0.166). The more substantive issue is the lack of error bars, which is retained as a Major weakness above. *Subsumed into the error-bars weakness.*

---

## Novel Insights

Beyond the paper's own contributions, a noteworthy synthesis from the reviews is the *tension between the paper's theoretical sharpness and its practical transparency.* The clean collapse result (Theorems 4.1–4.2) is so crisp that it raises an immediate practical question—how much approximate decision calibration is "close enough" to preserve plug-in optimality?—that the paper does not (and perhaps cannot with current tools) answer with equal sharpness. This tension is not a flaw in the paper but an intellectual opening: future work that characterizes the Lipschitz continuity of the robust policy in the calibration error would complete the picture the paper begins. The paper's self-orthogonality result (Proposition 4.4) is particularly clever because it identifies a calibration guarantee that holds by default for a huge class of models, making the framework immediately applicable without requiring any post-hoc procedure—this bridges theory and practice in a way that is rare in the calibration literature.

---

## Suggestions

- **Rebuild the experimental appendix around a transparent adversarial construction.** Specify the exact optimization problem that defines the worst-case q for each adversary, how the dual variables λ* are computed, and whether the adversary operates via importance reweighting, data resampling, or explicit optimization. Release the code.
- **Add standard errors to Table 1** (e.g., over 5–10 random train/calibration/test splits) to enable assessment of statistical significance.
- **Add a brief paragraph or remark in Section 4.1** discussing the behavior of the robust policy under approximate decision calibration, even if a full analysis is deferred to the appendix. This would help practitioners calibrate their intuition about the sharpness of the transition.
- **Consider adding a multi-class experiment** (e.g., with a decision-calibrated classifier from Noarov et al., 2023) to demonstrate the framework in the setting where decision calibration is known to be achievable.

---

## Score and Decision

**Originality:** High. The minimax perspective on ℋ-calibration and the sharp transition at decision calibration are genuinely novel.  
**Importance of research question:** High. Calibration-based trustworthiness is a central topic, and connecting it to robust decision-making is timely.  
**Claims well supported:** The theoretical claims are well supported by clear proofs (modulo the stripped appendix). The empirical claims are only weakly supported due to the underspecified experimental methodology.  
**Soundness of experiments:** Below bar. The adversarial construction is not described, no uncertainty quantification is provided, and the scope is narrow.  
**Clarity of writing:** Good. The paper is well-structured, notation is consistent, and the conceptual arc is easy to follow.  
**Value to the research community:** High. The theoretical results provide concrete guidance for designing and using partially calibrated forecasters in decision-making contexts.

The paper's theoretical contribution is strong and deserves acceptance. The experimental section falls short of the rigor needed for full empirical validation, but the experiments are presented as supporting case studies rather than as the primary contribution. The core theory stands independently.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>