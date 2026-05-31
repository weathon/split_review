Now let me narrow my bracket with more targeted anchors in the 5–7 range.Now I have sufficient anchors to calibrate my score. Let me write the final review.

---

## Summary

Direct Optimal Action Learning (DOAL) is a framework for offline RL policy extraction that computes an "optimized" target action by taking a gradient ascent step from each dataset action using the Q-function gradient, then trains expressive policies (Gaussian, flow, TrigFlow diffusion) to imitate these targets using distribution-native losses (e.g., flow matching). The paper also re-examines the previously neglected trade-off in MaxQ sampling controlled by n\_sample, and introduces a Batch-Normalizing Optimizer that replaces the obscure α coefficient with a more interpretable trust-region parameter δ. Results are reported on OGBench (9 tasks) and D4RL Adroit (6 tasks).

---

## Strengths

- **MaxQ sampling analysis is a genuine and impactful contribution.** Proposition 3 formalizes overestimation bias growth with n\_sample, and the resulting baseline improvement is substantial: MFQL with tuned n\_sample (418 total OGBench) outperforms FQL\* (381) by 37 points without DOAL at all. This finding was previously neglected in the literature and substantively lifts state of the art.

- **DOAL consistently improves over baselines when Q-learning is regularized.** DMFReBRAC achieves 466 vs 425 for MFReBRAC (+41 total OGBench score), and 630 vs 614 on D4RL — genuine improvements on both benchmarks using the same configuration (Table 2). DIFQL similarly outperforms IFQL on OGBench (359 vs 329, Table 1). These are the clearest cases where DOAL's specific contribution (Q-gradient at data action) delivers measurable benefit.

- **Computational efficiency is concretely measured.** Figure 2 demonstrates that DOAL adds only one extra forward + backward Q-call per update, yielding ~2 minutes of overhead on antmaze-large (DIFQL: 31 min vs IFQL: 29 min). Compared to the BPTT baseline (61 min), the practical efficiency advantage is large and empirically verified.

- **Hyperparameter stability of δ over α is empirically demonstrated.** Table 3 shows δ spans 0.03–0.3 across four OGBench environments while the corresponding α spans two orders of magnitude (10–1000). Figure 3 confirms gradient norms are stable throughout 1M training steps.

- **Framework versatility is real, not just claimed.** The authors test three Q-value functions (IQL, Q-learning, ReBRAC) and three policy classes (Gaussian, Flow, TrigFlow diffusion) across two distinct benchmarks, with DOAL variants corresponding to every baseline. This is a broad and carefully organized empirical study.

---

## Weaknesses

### Fatal
None.

### Major

- **DOAL's contribution cannot be cleanly isolated from n\_sample tuning, and improvements are inconsistent across settings.** On D4RL with plain Q-learning, DMFQL (614) underperforms its own baseline MFQL (623) — the DOAL model is worse than the non-DOAL baseline (Table 2). With IQL on D4RL, the paper explicitly states "there is no performance gain from either DOAL model or even ETrigflow." DOAL delivers reliable gains only when combined with regularized Q-learning (ReBRAC) on OGBench. The abstract's claim of "effective and versatile" does not match this conditional picture. While the paper is candid about these results, the introduction does not adequately qualify when DOAL is expected to work and when it is not.

- **Missing ablation on the core design choice.** DOAL's defining feature — evaluating the Q-gradient at data action a rather than at policy output π\_θ(s) — is never isolated in an experiment. There is no comparison between DOAL and a single-sample BRAC approximation that uses the gradient at π\_θ(s) with the same native behavior loss. Without this ablation, it is impossible to know whether performance changes are due to (i) where the gradient is evaluated (the theoretical innovation), (ii) using distribution-native losses instead of MSE, or (iii) some combination. This is a structural gap in supporting the paper's central claim.

### Minor

- **The theoretical framing slightly oversells the design choice as a correction to BRAC.** The paper describes BRAC's gradient evaluation at π\_θ(s) as a "conceptual inconsistency" and presents DOAL as fixing it. However, evaluating the gradient at data action a instead introduces its own asymmetry: for policies far from a early in training, a^target = a + δ/‖∇‖ · ∇\_a Q(s,a)|_{a'=a} may be a poor imitation target for π\_θ. The paper does acknowledge in Footnote 1 that "both [BRAC and DOAL] push the policy to produce higher valued action while being close to the action data point," but the main body still frames DOAL as fixing a flaw rather than as a different reasonable heuristic with its own trade-offs.

- **Batch-Normalizing Optimizer's practical benefit is limited.** Section 5.3 explicitly states: "one can equivalently treating the direct gradient scaling factor as a hyperparameter and avoid the batch-normalization. The performance would be equivalent." The benefit is purely a more interpretable parameter scale, not improved performance. Furthermore, the grid search still uses disjoint value sets across benchmarks ({0.03, 0.1, 0.3} for OGBench vs {0.0003, 0.001, 0.003} for D4RL), limiting how "shareable" δ truly is.

- **Text–formula inconsistency in Section 3.2.** The surrounding text refers to "the expected *squared* magnitude of the update," but Condition 2 and Proposition 2 (Eq. 15) use the L2 norm E[‖g‖\_2] = δ, not the squared norm. This creates ambiguity about what δ physically represents.

### Trivial
None.

---

## Nice-to-Haves

- **Ablation: DOAL (gradient at a) vs. a single-step BRAC approximation (gradient at π\_θ(s)) with the same native behavior loss.** If DOAL outperforms this variant, the formal motivation becomes empirically grounded. If they are similar, the paper should reframe DOAL as a practical simplification rather than a principled correction.

- **Fixed-δ experiment across all OGBench tasks.** If a single δ (e.g., 0.1) achieves competitive performance without per-task tuning, this would directly demonstrate the batch-normalizing optimizer's transferability claim. Currently, δ is selected per task from a 3-value grid.

- **Sanity-check measuring Q-values of a^target vs. a.** A simple check that a^target achieves higher Q(s, a^target) than Q(s, a) on average would confirm the DOAL mechanism is functioning as intended.

- **Discussion of the performance gap vs. ReBRAC(tanh)\* (Table 2: 297 vs. 466).** The paper notes in Section 5.1 that tanh nonlinearity is a key difference but defers this to future work. A brief ablation quantifying this gap would help readers understand how much improvement remains achievable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Table 3 subscript typo (s' vs a').** The table header uses ∇\_{s'} Q (gradient w.r.t. state s') when ∇\_{a'} Q (action) is clearly intended. This is almost certainly a PDF parser artifact — per the review rules, formatting artifacts from PDF extraction are not paper errors and are removed.

- **Proposition 3 formalization concerns (informal proposition on countably many actions).** The critic flagged the Gaussian i.i.d. noise model and countable action space as "unusual." However, the paper explicitly labels this "Informal" and notes it as a proof intuition. This is well within the norms of empirical RL papers providing qualitative formal grounding. Removed.

- **Concern about selection bias from δ grid search** (Section 5.1 candor: "one can not rule out selection bias"). The paper acknowledges this directly and it applies equally to essentially all hyperparameter-tuned baselines. Not specific enough to DOAL to constitute a distinct weakness. Removed.

- **FAC concurrent work comparison.** The paper cites Anonymous (2025) as a concurrent work achieving "very strong performance." Per rules, we do not penalize for not comparing against concurrent submissions. Removed.

- **Concern about antmaze-large high variance** (two seeds with very low performance causing 72→63 drop for DTrigFlow/ETrigFlow). The paper explicitly flags this in Section 5.1 and reports 8-seed averaging. The observation is real but already addressed. Demoted to acknowledged limitation.

- **Generic Strength: "framework addresses an important problem."** Removed as generic; only concrete strengths retained above.

---

## Novel Insights

The most underappreciated observation in this paper is that n\_sample in MaxQ sampling is not merely a computational budget parameter but a substantive algorithmic choice that trades off Q-value coverage against maximization bias — and that prior work has consistently set it too high, compounding overestimation. Proposition 3 provides a formal skeleton for this intuition (the max of n Gaussian samples with noise floor c grows like √(2 log n) regardless of true means), and the empirical payoff from tuning n\_sample is larger than the payoff from DOAL itself in most configurations. This finding could have significant impact on practitioners using any MaxQ-based resampling method in offline RL.

---

## Suggestions

1. **Add the DOAL-vs-gradient-at-π\_θ(s) ablation** using the same native behavior loss. This is the most critical missing experiment.
2. **Revise the abstract and introduction** to qualify that DOAL provides reliable gains only with regularized Q-learning, and that on D4RL with plain Q-learning it underperforms its own baseline.
3. **Fix the "expected squared magnitude" vs "L2 norm" inconsistency** in Section 3.2 Condition 2 and surrounding text.
4. **Report a fixed-δ experiment** (e.g., δ=0.1 for all OGBench tasks) to substantiate the portability of the batch-normalizing optimizer.
5. **Report n\_sample values per task in the main text** (currently deferred to Appendix G), since this is presented as a major new hyperparameter insight.

---

## Calibration Anchors

**Round 1 (bracketing):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| C9BA0T3xhq.md | 2.00 | 1 | Weak offline RL (EIQL) — clearly below DOAL in execution and scope |
| d159zNCmOq.md | 3.40 | 1 | Offline-to-online RL transition — simpler contribution, no flow/diffusion |
| hMjUnF3aQ8.md | 2.00 | 1 | SQT — minimal contribution, prior work duplication |
| HA0oLUvuGI.md | 6.25 | 1 | Energy-weighted flow matching for offline RL — similar topic, clean theory, accepted |
| TeeyHEi25C.md | 6.25 | 1 | Diffusion value functions — similar domain, mixed reviews |
| gEdg9JvO8X.md | 3.67 | 1 | BDQL — simpler approach, rejected, smaller empirical scope |
| StkLULT1i1.md | 5.00 | 1 | Q-Score Matching — similar spirit to DOAL, rejected due to limited experiments |
| 8BAkNCqpGW.md | 8.00 | 1 | Policy gradient for POMDPs — much stronger theory, high score |
| g7ohDlTITL.md | 8.00 | 1 | Riemannian Flow Matching — foundational theory paper, clearly above DOAL |

**Round 1 bracket: 5.0–6.5**

**Round 2 (narrowing within 4.5–7.5):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| xCRr9DrolJ.md | 6.25 | 2 | SRPO — diffusion behavior regularization, cleaner theory, narrower scope, DOAL has broader experiments but messier results; roughly comparable |
| wQCPHxtzGV.md | 4.75 | 2 | RF-POLICY — rectified flow imitation learning, rejected, narrower than DOAL |
| tGQirjzddO.md | 6.33 | 2 | Latent diffusion offline RL — more targeted, accepted, consistent results |
| OATPSB5JK1.md | 6.00 | 2 | LEQ model-based offline RL — more consistent ablations and results, accepted |
| WwCirclMvl.md | 5.67 | 2 | Langevin Monte Carlo offline RL — more theoretical, comparable experimental depth |
| QyVLJ7EnAC.md | 6.40 | 2 | Model-free offline RL with robust Q-learning — consistent results, accepted |

**Round 2 narrowing:** DOAL is stronger than RF-POLICY (4.75) and Q-Score Matching (5.0) due to broader scope and empirical results on two benchmarks beating prior best (FQL). However, DOAL is below LEQ (6.0) and SRPO (6.25) due to the missing core ablation and D4RL inconsistencies with plain Q-learning. The paper sits below the tGQirjzddO/LEQ range (6.0–6.33), which represent accepted papers with more consistent results and complete ablation studies. DOAL's strongest evidence (OGBench with ReBRAC) is compelling, but the absent ablation and mixed D4RL story pull the score toward borderline.

**Final score: 5.5** (between Q-Score Matching at 5.0 and LEQ at 6.0, closer to the lower end given the missing ablation is central to the stated contribution).

---

## Score and Decision

The paper makes a real empirical contribution via the MaxQ n\_sample analysis and demonstrates that a Q-gradient-guided target action framework can work across multiple policy types on OGBench. However, DOAL's core design choice (gradient at data action vs. at policy output) is never experimentally isolated, and the method underperforms its own non-DOAL baseline on D4RL with plain Q-learning. These gaps prevent a confident accept at this stage.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>