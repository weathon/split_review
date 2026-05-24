Now I have all the information I need. Let me construct the final review.

## Summary

This paper introduces Direct Optimal Action Learning (DOAL), a framework that replaces end-to-end backpropagation through iterative sampling (BPTT) in offline RL with a two-step process: (1) compute an "optimized" target action by taking a gradient step on the Q-function from the data action, normalized by a batch-statistics trust-region parameter δ; (2) train the policy using its native behavior-clone loss (MSE, flow matching, or diffusion loss) to imitate this target. The paper also contributes a batch-normalizing optimizer that replaces the hard-to-tune α in BRAC with a more interpretable δ, and an analysis of the MaxQ sampling trade-off. The method is evaluated across three value functions (IQL, Q-learning, ReBRAC) and three policy classes (Gaussian, flow, diffusion) on OGBench and D4RL.

## Strengths

1. **Practical framework that cleanly avoids BPTT overhead.** DOAL decouples the Q-gradient computation from the policy training by constructing a differentiable target action from the data point, then using the policy's native loss (flow matching, diffusion) for imitation. This sidesteps the computational cost and memory overhead of backpropagating through iterative sampling chains. The runtime analysis (Figure 2) confirms that DOAL adds only one extra forward+backward call over baselines (DMFQL: 18 total NN calls vs MFQL-BPTT: 37; 37 min vs 61 min actual time).

2. **Batch-normalizing optimizer demonstrably simplifies hyperparameter search (Table 3).** The paper observes that α in BRAC-style objectives varies by two orders of magnitude (10–1000) across OGBench tasks, while the proposed δ varies only within (0.03, 0.1). The theoretical connection (Proposition 2) linking δ to an expected update magnitude is clean, and the empirical evidence in Table 3 directly supports the claim that δ is more interpretable and easier to tune.

3. **Comprehensive evaluation across value functions and policy classes.** The paper tests 3 value functions (IQL, Q-learning, ReBRAC) × 3 policy families (Gaussian, flow, diffusion) on 9 OGBench tasks and 6 D4RL Adroit tasks, totaling 15 diverse environments. This breadth strengthens the claim of versatility and allows the paper to identify the key dependence on Q-function regularity.

4. **Clean baseline subsumption (Figure 4).** Setting δ=0 recovers the non-DOAL baseline exactly (DMFQL → MFQL, DMFReBRAC → MFReBRAC), showing that DOAL generalizes its counterparts without harming performance when the gradient signal is unhelpful.

5. **MaxQ sampling analysis (Proposition 3) is a useful insight.** The informal proposition about overestimation bias growing with n_sample is well-motivated, and the practical recommendation to tune n_sample (rather than defaulting to a large fixed value) improves the baselines meaningfully — IFQL goes from 218 to 329 total on OGBench by tuning n_sample alone.

## Weaknesses

### Fatal
None.

### Major

1. **DOAL's core theoretical motivation is unquantified and applies only to a restricted setting.** Proposition 1 shows that for a *deterministic* policy with an *MSE* BC loss, the gradient of the BRAC objective equals the gradient of a squared-error loss w.r.t. a target action that evaluates $∇_aQ$ at the *policy output*. DOAL then replaces this with $∇_aQ$ at the *data action*. The paper correctly calls these "similar but different" (Section 3.1) and includes a footnote explicitly disclaiming equivalence. However, (a) the approximation error between the two targets is never analyzed — no bound, no empirical correlation study, no condition under which the substitution is justified; (b) Proposition 1 does not cover the flow-matching or diffusion losses actually used in the main experiments (Eqs. 3, 6), where the BC loss is velocity matching or denoising MSE, not the simple MSE of the proposition. The paper acknowledges this implicitly ("DOAL is a reasonable objective in its own right") but the claimed connection to BRAC — which frames the method's motivation in the title and abstract — remains an unverified approximation.

2. **Empirical improvements are inconsistent and concentrated in a narrow regime.** On OGBench with IQL (Table 1), DOAL's total improvements over tuned baselines are modest (DIOL: 276 vs IQL(Gauss) 191; DIFQL: 359 vs IFQL 329; DTrigFlow: 368 vs TrigFlow 361), and the gains are largely driven by a few tasks (scene-play: 12→37 under Gaussian; puzzle-4x4: 5→40 under Gaussian). Many tasks show negligible change or regression (antmaze-large-navigate: 72→63 for DTrigFlow). On D4RL with IQL (Table 1), DOAL produces *no* improvement at all — totals are essentially within noise (520 vs 518; 592 vs 584; 584 vs 577). Under Q-learning (Table 2), DOAL improves on OGBench (DMFQL 443 vs MFQL 418) but regresses on D4RL (614 vs 623). The most consistent gains come only with regularized Q-learning (DMFReBRAC 466 vs MFReBRAC 425 on OGBench; 630 vs 614 on D4RL). The paper is transparent about this pattern, but the abstract calls DOAL "effective" and "versatile" without qualification, which overstates the evidence.

3. **Missing control experiment: direct gradient ascent training without the imitation-learning step.** DOAL's design has two components: computing a gradient-optimized target and then imitating it via BC loss. The paper does not isolate the contribution of the imitation step from simply using the same gradient signal to train the policy directly (e.g., via reparameterization for Gaussian, or via the one-step approximations used by EDP/FQL for diffusion). ETrigFlow (Table 1) is a one-step BRAC approximation but uses a different formulation (sampling from corrupted $a_t$). Without a control that uses the same one-step gradient *as a training signal* without the BC-imitation step, it is unclear whether the imitation learning design is beneficial or whether the gains come from the gradient signal itself.

### Minor

1. **Claim that δ is "shareable across policies" is not explicitly validated.** The abstract states δ is "shareable across policies," and the paper says "for all algorithms in the same task and same value function, the DOAL hyperparameters δ are shared" (Section 1). However, Table 3 only shows δ values for *different environments*, not for different algorithms (IQL vs Q-learning vs ReBRAC) on the *same* task. The claim about cross-algorithm sharing would require explicit demonstration (e.g., using the same δ for DIOL and DIFQL on antmaze-large), which is absent from the main evaluation.

2. **Failure analysis on D4RL with IQL is speculative.** The paper attributes DOAL's lack of improvement on D4RL with IQL to "unreliability of IQL learned function gradient" (Section 5.1). This is a plausible explanation, but no quantitative evidence is provided — e.g., comparing gradient norms or target action OOD-fraction across IQL and Q-learning Q-functions. The argument would be strengthened by such analysis, or by acknowledging that the explanation is a hypothesis.

3. **Batch-normalization is shown to be equivalent to a fixed per-task scaling factor.** The paper notes (Section 5.3, Figure 3) that gradient norms are stable during training, meaning the batch-normalized update $a + \frac{δ}{\mathbb{E}[\|∇Q\|]} ∇Q$ is essentially equivalent to $a + η∇Q$ with a fixed per-task η. The advantage is that δ varies less across tasks than η would, but the claim that batch normalization is "a mechanism" rather than a reparameterization is modest. This is correctly acknowledged but the framing could be sharper.

### Trivial
- In Table 1, several standard deviations appear suspiciously rounded (e.g., ±24, ±23, ±28 across many cells), suggesting they may be rounded computed values or there is a formatting issue.
- In Table 2, the subscript "hyst" for MFQL appears to be a typo for "bptt".

## Nice-to-Haves

1. An analysis (theoretical or empirical) of when $∇_aQ(s,a)$ at the data action is a good approximation to $∇_aQ(s,π_θ(s))$ — e.g., a bound in terms of $\|π_θ(s)-a\|$ or an empirical correlation plot across training.
2. A control experiment directly training the policy to maximize Q via reparameterization (for Gaussian) or one-step approximations (for flow/diffusion), without the BC imitation step, to isolate the benefit of DOAL's design.
3. Explicit demonstration of the "shared δ" claim by showing that the same δ works for IQL-based and Q-learning-based DOAL variants on at least one shared task (e.g., antmaze-large).

## Removed Points

The following points from the reviewers are removed for the stated reasons:

- **Harsh Critic: "[Proposition 1] does not even directly apply" to flow/diffusion policies**: The paper acknowledges this via footnote 1 and the statement that "DOAL is a reasonable objective in its own right." The connection is approximate and the paper does not claim exact equivalence. The point is retained in Major weakness #1 but the framing is softened from "overstated" to "unquantified."
- **Harsh Critic: "The paper should more clearly state that this is an approximation"**: The paper already states (Section 3.1) "BRAC objective and the DOAL objective are similar but different" and includes footnote 1 clarifying no equivalence claim. The paper is sufficiently clear.
- **Harsh Critic: "The comparison is structured in a way that may inflate DOAL's relative performance"** — the claim about unfair baselines: The baselines (IFQL, TrigFlow with MaxQ) are strong, well-tuned baselines. The comparison is fair because DOAL keeps the same policy class and value function, differing only in accessing $∇_aQ$. The missing control (direct gradient training) is retained as a Major weakness but not framed as inflating results.
- **Harsh Critic: "DOAL is 'sample-efficient, effective, versatile' but undercut by failure on D4RL with IQL"**: The paper qualifies its claims in the body ("on Adroit tasks, improvement can be achieved when the Q value learning is regularized"). The abstract's unqualified claims are addressed in Major weakness #2.
- **Harsh Critic's section-by-section notes about presentation**: These are formatting/style preferences without concrete evidence of errors.
- **Strength Finder's generic strengths ("addressed an important problem," "timely contribution")**: These lack specific content anchored to the paper's actual results.

## Novel Insights

The central insight — that the BRAC gradient can be reinterpreted as an imitation-learning target, and that the Q-gradient can be evaluated at the data action rather than the policy output to decouple computation — is the paper's genuine contribution. The batch-normalizing optimizer insight (δ directly controls expected update magnitude and varies less across tasks than α) is a practical engineering contribution that is well-supported by Table 3 and Figure 3. The observation that MaxQ sampling's n_sample needs to be tuned (Proposition 3) is a useful practical finding that improves the baselines substantially. However, none of these insights individually transforms the field; they are incremental but solid contributions to the practical engineering of diffusion/flow policies for offline RL.

## Suggestions

1. Recalibrate the abstract's claims to match the evidence: DOAL is "effective" primarily with regularized Q-functions and on OGBench, not universally.
2. Add a bounded analysis of the approximation error between DOAL and BRAC targets, or at minimum an empirical correlation study showing when the two gradients are aligned during training.
3. Add a control experiment that trains a Gaussian policy directly via $π_θ(s) ← π_θ(s) + η∇_aQ(s, π_θ(s))$ (without BC imitation) to isolate the benefit of the imitation step.
4. Provide explicit evidence for the "shared δ" claim by running IQL-based and Q-learning-based DOAL with the same δ on at least one shared task.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Queried "offline reinforcement learning policy extraction diffusion flow models" in three bands.

- **Low band (avg < 3.5):** Retrieved 4 anchors at avg 3.00 (rejected). These papers are substantially weaker than the paper under review, which has a clear practical framework and extensive experiments.
- **Mid band (3.5–7.5):** Retrieved anchors including SRPO (6.25, Accept), DAC (6.50, Accept), RF-Policy (4.75, Reject), Energy-Weighted FM (6.25, Accept), AlignIQL (5.33, Reject), Efficient Offline RL (5.00, Reject).
- **High band (avg > 7.5):** Retrieved anchors at 7.6–8.0 (all Accept). These papers have stronger theoretical contributions or more definitive empirical results, placing them clearly above this paper.

**Round 1 Bracket:** 4.5–6.5

**Round 2 (Narrowing):** Queried for "offline RL behavior regularized actor critic policy extraction gradient" and "offline RL action optimization target matching imitation learning" within (4.5, 7.5).

- **SRPO (6.25, Accept):** Similar topic (efficient diffusion policy via behavior score regularization). SRPO has cleaner theory but less comprehensive evaluation. This paper is comparable but with weaker theoretical grounding.
- **Energy-Weighted FM (6.25, Accept):** Flow matching + offline RL. This paper has less theoretical depth but broader empirical coverage. Comparable overall.
- **DAC (6.50, Accept):** Diffusion policies with Q-guidance. Stronger empirical results; this paper is slightly weaker.
- **AlignIQL (5.33, Reject):** Related work on IQL policy extraction. This paper has a more original contribution (DOAL framework vs constrained optimization view).
- **Efficient Offline RL (5.00, Reject):** Modest contribution around critic pretraining. This paper has a more substantial contribution.

**Final Score Determination:** The paper is stronger than AlignIQL (5.33) and Efficient Offline RL (5.00), comparable to Energy-Weighted FM (6.25) and SRPO (6.25) in overall ambition but weaker in theoretical depth and empirical consistency. It is below DAC (6.50) in empirical strength. Given the uneven empirical results, unquantified theoretical approximation, and missing control experiments, the paper sits at 5.5 — a solid contribution with clear value but significant limitations in the strength of evidence.

**All anchors considered across rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| mc97L2QVIa | 3.00 | R1 | Much weaker — basic offline MARL approach |
| cXxfVkRCHJ | 3.00 | R1 | Much weaker — offline-to-online augmentation |
| VCscggkg2t | 3.00 | R1 | Much weaker — GFlowNet for goal-conditioned RL |
| 4u0ruVk749 | 3.00 | R1 | Much weaker — treatment effect estimation |
| TeeyHEi25C | 6.25 | R1 | Stronger theoretical framing; this paper has broader eval |
| gEdg9JvO8X | 3.67 | R1 | Weaker — BDQL on-policy approach |
| wQCPHxtzGV | 4.75 | R1 | Weaker — rectified flow for IL only |
| HA0oLUvuGI | 6.25 | R1/R2 | Comparable level; cleaner theory, narrower scope |
| 8BAkNCqpGW | 8.00 | R1 | Much stronger — confounded POMDP theory |
| uKZdlihDDn | 7.60 | R1 | Much stronger — fluid simulation diffusion |
| EO8xpnW7aX | 8.00 | R1 | Much stronger — discrete permutation diffusion |
| kJFIH23hXb | 8.00 | R1 | Much stronger — protein generation |
| oWKPZ1Hcsm | 5.00 | R2 | Weaker — critic pretraining, less novel |
| ldVkAO09Km | 6.50 | R2 | Stronger — DAC with cleaner theory and stronger results |
| xCRr9DrolJ | 6.25 | R2 | Comparable — SRPO, similar topic, cleaner theory |
| nrRkAAAufl | 6.50 | R2 | Different topic (safe RL) |
| 7fxzVTSgZC | 6.25 | R2 | Different topic (offline IL without auxiliary data) |
| 9TL99KnTv5 | 5.00 | R2 | Weaker — AILOT, less comprehensive |
| N2Kdq5biZx | 5.33 | R2 | Weaker — offline-to-online planning |
| MNyOI3C7YB | 7.00 | R2 | Stronger — SEABO offline IL |
| A0DI5v6m8O | 5.50 | R3 | Comparable — black-box gradient matching, similar score |
| 3Xfa63ggsq | 5.33 | R3 | Weaker — AlignIQL, related but less contribution |
| gCZyD7WD0w | 5.50 | R3 | Different topic (fine-tuning) |
| 7zY781bMDO | 6.00 | R3 | Different topic (trajectory stitching, theory paper) |
| 1Akd36hG9z | 5.33 | R3 | Weaker — optimal supported dataset generation |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>