Now I have enough calibration data. Let me finalize my assessment and write the review.

**Bracket narrowing**: DOAL is stronger than Q-score Matching (5.00) — which had thin experiments — and roughly comparable to SRPO (6.25) in contribution spirit, though SRPO has cleaner theoretical derivation while DOAL has broader experiments. DOAL is clearly weaker than VACO (7.00) and DAC (6.50), which have stronger theoretical frameworks and SOTA comparisons. I place DOAL at **5.5**.

---

## Summary
This paper proposes Direct Optimal Action Learning (DOAL), a framework for extracting policies from Q-value functions in offline RL. Instead of backpropagating through iterative sampling chains (as in BRAC methods), DOAL computes an optimized target action via a single batch-normalized gradient ascent step on the Q-function at each data point and trains the policy to imitate that target using its native distribution loss. The method is evaluated with Gaussian, flow-matching, and diffusion policies across IQL, Q-learning, and regularized Q-learning value functions on OGBench and D4RL benchmarks.

## Strengths
- **Practical hyperparameter contribution (batch-normalizing optimizer):** Proposition 2 derives a batch-normalized action update that controls the expected update magnitude via an interpretable δ, and Table 3 demonstrates δ varies far less across environments (0.03–0.3) than the α hyperparameter in prior work (10–1000). Figure 3 confirms gradient norm stability during training. This is a genuine practical improvement for hyperparameter tuning.

- **MaxQ sampling analysis (Proposition 3):** The paper provides a clear argument that tuning \( n_{\text{sample}} \) in MaxQ sampling involves a trade-off between coverage and maximization bias, and demonstrates that properly tuned \( n_{\text{sample}} \) yields strong baselines that surpass previously published results (e.g., IFQL in Table 1 significantly outperforms the original IFQL* on OGBench).

- **Broad experimental coverage:** The framework is tested across three policy classes (Gaussian, flow, diffusion) and three value-function approaches (IQL, Q-learning, regularized Q-learning) on two benchmarks (OGBench and D4RL). This controlled-study design cleanly isolates the effect of DOAL and provides evidence of its versatility.

- **Computational efficiency demonstrated:** Figure 2 shows DOAL adds only one extra forward and backward Q-network call over the baseline, and the linear relationship between NN calls and wall-clock time supports the claim of low overhead.

## Weaknesses

### Fatal
None.

### Major
- **No comparisons to modern gradient-guided diffusion/flow offline RL methods:** The paper compares DOAL only against its own non-DOAL baselines (IQL, IFQL, TrigFlow, MFQL, MFReBRAC) and published FQL numbers. It acknowledges the existence of methods that also use Q-value gradients for policy learning with diffusion/flow policies (QGPO, EDA, DAC, BDPO, FAC — all listed in Section 6) but provides no numerical comparison to any of them. The ETrigFlow baseline is a one-step BRAC variant implemented by the authors, not a published strong method. Without head-to-head comparisons, it is unclear whether DOAL's approach offers advantages over existing gradient-guided methods or merely improves over weaker predecessors. This limits the significance claim.

- **Weak theoretical connection between Proposition 1 and the actual DOAL objective:** Proposition 1 shows that the BRAC policy gradient is equivalent to the gradient of a squared error toward a target that evaluates \( \nabla_a Q \) at the policy's output \( \pi_\theta(s) \). DOAL instead evaluates \( \nabla_a Q \) at the data action \( a \). The paper acknowledges "Proposition 1 shows BRAC objective and the DOAL objective are *similar but different*" and states "DOAL is a reasonable objective for offline RL in its own right," but provides no derivation or analysis of why this substitution yields policy improvement. The method reduces to an intuitive but heuristic procedure ("take one gradient step from the data action and imitate"), and the theoretical framing via Proposition 1 does not actually support the method as stated.

### Minor
- **D4RL results are inconsistent and often show no gain:** Across D4RL tasks in both Table 1 and Table 2, DOAL-based methods frequently perform worse than or equal to their baselines (e.g., DIOL total 518 vs IQL 520; DMFQL 614 vs MFQL 623 on D4RL). The paper acknowledges this and attributes it to unreliable IQL Q-function gradients, but the fact that DOAL only reliably helps on OGBench and with regularized Q-learning weakens the claim of general versatility. This is partially addressed by the ReBRAC results showing improvement when Q-functions are better regularized, but it remains a limitation.

- **The claim that δ is shared across policies is not fully substantiated in the main text:** The paper states that "for all algorithms in the same task and same value function, the DOAL hyperparameters δ are shared." However, the main text does not report the exact δ values per algorithm per task to verify this (deferred to Appendix G, which is stripped). Table 3 shows δ varies across environments (0.03–0.3) but does not demonstrate sharing across policy types for the same environment.

### Trivial
- Some figures contain parser artifacts (duplicated captions for Figure 1, Figure 2) — this is a formatting issue in the extracted PDF, not a paper problem.
- Section 5.3 begins mid-sentence ("As we are using IQL for value estimation and the same value net in all our experiments...") — the sentence appears truncated.

## Nice-to-Haves
- A controlled ablation comparing the batch-normalizing optimizer against a non-normalized fixed step size (δ′) would strengthen the case for Proposition 2. The paper mentions this is in Appendix F (stripped).
- An experiment explicitly demonstrating that the same δ works across different policy types for a fixed environment would directly support the hyperparameter-sharing claim.
- A systematic discussion of when \( \nabla_a Q \) is unreliable and how practitioners should detect this (the D4RL results suggest this matters in practice).

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic #1 on "backpropagation motivation overstated":** The critic claims the motivation is overstated because IFQL and TrigFlow avoid backpropagation. But the paper's point is about BRAC methods specifically — backpropagation *is* costly for BRAC with iterative sampling policies. The baselines avoid it by not using BRAC during training (they use MaxQ at inference only), which is precisely the paper's comparison point. REMOVED as a misunderstanding.

- **Harsh Critic on "ReBRAC definition confusing":** The ReBRAC definition (Eq. 11) includes a behavior-cloning term in the critic target, which is standard in regularized Q-learning (as in Tarasov et al. 2023). The paper adequately explains this. REMOVED — the definition is clear to readers familiar with the area.

- **Harsh Critic on "missing appendix comparisons":** The critic demands an ablation comparing batch-normalized vs. non-normalized step size, but acknowledges it is "promised in an appendix." Since the appendix is stripped by the parser, this is not a paper problem. REMOVED the demand; noted as a nice-to-have above.

- **Harsh Critic on "totals across diverse tasks with different reward scales":** This is a valid concern about presentation, but the paper follows the same convention as prior work (FQL, Park et al. 2025c) and the per-task scores are fully reported. REMOVED as a significant weakness; it's a minor presentation preference.

- **Strength Finder "Theoretical justification via Proposition 1" retained but qualified:** The Proposition is mathematically correct, but as noted in the Major weaknesses, it does not actually justify the DOAL objective — it justifies a *different* objective (BRAC). The strength is retained but weakened.

- **Strength Finder "Consistent performance gains on OGBench":** Kept, but qualified — the gains are task-dependent and driven by outlier tasks, which is noted in the Minor weaknesses.

- **Harsh Critic #4 merged with Minor weakness about D4RL inconsistency.**

## Novel Insights
The observation that tuning \( n_{\text{sample}} \) in MaxQ sampling involves a fundamental trade-off between coverage and maximization bias (Proposition 3) is genuinely useful and previously underappreciated — prior work either set \( n_{\text{sample}} \) large without tuning or argued larger is always better. The paper's empirical demonstration that properly tuned \( n_{\text{sample}} \) alone yields strong baselines (IFQL surpassing previously published IQL/FQL results on OGBench) is a concrete contribution independent of DOAL.

## Suggestions
- Include at least one head-to-head comparison against a published gradient-guided diffusion/flow method (e.g., DAC or QGPO) on shared benchmarks. This would clarify whether DOAL's simplicity offers a genuine advantage or merely performs comparably.
- Provide a brief formal argument (even if informal) for why using \( \nabla_a Q \) at the data action rather than at the policy output should still yield policy improvement, beyond the intuitive "stay close to data" argument already given.
- Report per-task δ values for each DOAL variant in the main text (or at minimum, clearly state that they are identical across policy types for each task) to support the sharing claim.

## Score and Decision

**Calibration anchors:**
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| BDQL (gEdg9JvO8X) | 3.67 | R1 | DOAL is clearly stronger — broader experiments, better results, clearer contribution |
| Q-score Matching (StkLULT1i1) | 5.00 | R2 | DOAL is stronger — much broader experiments, practical hyperparameter contribution |
| EFM/QIPO (HA0oLUvuGI) | 6.25 | R1/R2 | Comparable topic space; EFM has stronger theory, DOAL has broader empirical coverage. DOAL slightly weaker due to weaker theoretical grounding |
| SRPO (xCRr9DrolJ) | 6.25 | R2 | Similar spirit (extracting policy using Q-guidance without diffusion sampling); SRPO has cleaner derivation, DOAL has broader experiments. DOAL slightly weaker |
| DAC (ldVkAO09Km) | 6.50 | R1 | DAC has stronger theory, SOTA comparisons, cleaner formulation. DOAL is clearly weaker |
| VACO (elTJBP7Fbv) | 7.00 | R2 | VACO has strong theory + SOTA results. DOAL is clearly weaker |

Round 1 bracket: 5.0–6.5. Round 2 narrowed to: DOAL sits between Q-score Matching (5.00) and SRPO/EFM (6.25), closer to the lower end due to (a) weak theoretical connection between Proposition 1 and the actual method, and (b) no comparisons to gradient-guided SOTA methods. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>