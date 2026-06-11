Now I have a solid comparison set. Let me finalize the analysis and write the review.

**Bracket analysis:**

Round 1 anchors:
- StkLULT1i1 (5.00, Rejected): Q-Score Matching for diffusion policy — good theory but very weak experiments (only 6 DMC tasks, 2 baselines). DIPOLE is clearly stronger.
- fcJKzwlwcs (4.80, Rejected): SODP diffusion planner — decent method but methodology concerns and limited experiments. DIPOLE is clearly stronger.
- svp1EBA6hA (6.50, Accepted): CTRL — KL-regularized RL for diffusion control, good theory but limited experiments (only image generation, 2 conditions). DIPOLE has broader validation and is comparable-to-superior.

Round 2 anchors:
- HA0oLUvuGI (6.25, Accepted): EFM/QIPO — energy-weighted flow matching for offline RL, novelty questioned by reviewers ("essentially RWR with flow matching"), results not clearly superior. DIPOLE has more distinctive novelty and stronger results.
- xCRr9DrolJ (6.25, Accepted): Score Regularized Policy Optimization — different approach but similar quality level. DIPOLE is comparable.
- ZULjcYLWKe (7.00, Accepted): DMBP — robust offline RL with diffusion. Strong paper. DIPOLE has more novel theoretical contribution (dichotomous decomposition + CFG) and broader experiments but some presentation gaps.

DIPOLE sits between the 6.25 EFM paper (clearly stronger) and the 7.00 DMBP paper (comparable). Accounting for overestimation tendency, I'll place it at **6.5**.

Now let me write the final review with the score.

Final decision: **Accept** (score 6.5).## Summary

This paper proposes DIPOLE, an RL algorithm for diffusion policy optimization that replaces the unstable exponential weighting in standard KL-regularized RL with a sigmoid-weighted reference policy. The key insight is that the optimal policy decomposes into two "dichotomous" policies — one biased toward high-return actions (weighted by σ(βG)) and one toward low-return actions (weighted by 1−σ(βG)) — that can be stably trained with bounded weights in [0,1]. At inference, their score functions are linearly combined à la classifier-free guidance (∇log π* = (1+ω)∇log π⁺ − ω∇log π⁻), with the greediness factor ω controlling the trade-off. The method is evaluated on 39 offline RL tasks (ExORL, OGBench), offline-to-online fine-tuning, and scaled to a 1B-parameter VLA model for autonomous driving on NAVSIM.

## Strengths

- **Novel theoretical decomposition resolving exponential-weight instability.** The greedified KL-regularized objective (Eq. 5) replaces exp(βG) with a sigmoid-weighted reference policy μ·σ(βG)/Z(s). Theorem 1 derives the closed-form solution, and the key algebraic insight — σ/(1−σ) = exp — decomposes the unstable exponential into two bounded components σ(βG) and (1−σ(βG)) in [0,1] (Eqs. 7-8). This enables stable training while preserving theoretical optimality. The derivation from Eq. 5 through Theorem 1 to Eqs. 7-10 is clean and well-paced.

- **Principled connection to classifier-free guidance.** Equation 10 shows ∇log π* = (1+ω)∇log π⁺ − ω∇log π⁻, which is structurally identical to CFG (Ho & Salimans, 2022). This is not a loose analogy — it follows rigorously from the decomposition and provides a theoretically grounded interface (ω) for controlling greediness at inference time. This bridges RL-based policy optimization and diffusion model design in a satisfying way.

- **Strong large-scale validation on NAVSIM.** Table 4 demonstrates DIPOLE scaling to a 1B-parameter VLA model for autonomous driving, improving PDMS from 88.3 (pretrained) to 94.8 on navtest — a 6.5-point gain surpassing all baselines including Hydra-MDP (86.5, CVPR2024 challenge winner). Gains span both safety (NC: 98.0→99.2, TTC: 94.3→95.6) and progress (EP: 82.5→94.2). Figure 2 provides qualitative evidence of the fine-tuned model correcting collision-prone trajectories. DIPOLE also convincingly outperforms DPPO on this benchmark (94.8 vs 89.0).

- **Broad empirical coverage with strong baselines.** Tables 1-2 evaluate across 39 offline tasks (9 ExORL, 30 OGBench) with 8 seeds each, comparing against competitive Gaussian (IQL, ReBRAC) and diffusion/flow policy baselines (IDQL, IFQL, FQL, CFGRL). DIPOLE achieves best or near-best aggregate scores in 5 of 6 OGBench categories and best on 8 of 9 ExORL tasks. Offline-to-online results (Table 3) show gains persist under online fine-tuning (e.g., humanoidmaze-m: 61→97).

- **Ablation isolates training contribution from inference-time tricks.** The DIPOLE w/o rs variant in Table 1 strips away rejection sampling and remains competitive with CFGRL (outperforming it on 5 of 9 ExORL tasks, e.g., Walker-walk 679 vs 608, Quadruped-walk 813 vs 762), directly supporting the claim that the dichotomous training objective itself enables greedy policy extraction beyond what inference-time rejection sampling provides.

## Weaknesses

### Fatal
None.

### Major

- **DDPO/DPPO not evaluated on the RL benchmarks despite being positioned as a primary competing paradigm.** The introduction (lines 21-22) explicitly critiques policy-gradient methods for diffusion (DDPO, DPPO) for their Gaussian-approximation limitations and frames the central research question as building a "more effective and stable RL method for diffusion policy optimization." Yet DDPO/DPPO appear only in the NAVSIM experiment (Table 4). They are absent from the ExORL and OGBench evaluations, where claims about stability and effectiveness relative to policy-gradient alternatives would be most directly tested. Including these baselines — or at minimum a documented attempt with explanation for omission — would substantially strengthen the paper's central claim. The NAVSIM comparison (DIPOLE 94.8 vs DPPO 89.0) provides partial evidence but does not fully substitute for evaluation on the core RL benchmarks.

### Minor

- **Rejection sampling mechanism not described in the main text.** The gap between DIPOLE and DIPOLE w/o rs is substantial (e.g., Walker-walk drops from 910 to 679, Walker-stand from 953 to 793), indicating rejection sampling accounts for a large fraction of performance. Section 3.3 delegates all details to Appendix C/D, but a brief paragraph describing the mechanism and its interaction with the score-combination inference belongs in the main text given its impact.

- **Value function learning approach not stated in main text.** The method hinges on reliable estimates of G(s,a) (set to advantage A(s,a), line 123) for the sigmoid weighting σ(βG). The main text does not specify which algorithm is used for value learning or whether it is trained jointly or separately. A single sentence would resolve this ambiguity.

- **Humanoidmaze-large-navigate results are at floor for all methods.** Scores range from 1 to 11 across methods (Table 2). These tasks appear unsolved by any method, and differences at this performance floor are not meaningful — DIPOLE's 6 is below IFQL's 11. The paper's statement that DIPOLE "achieves better performance compared to other baselines" in "most task categories" (line 174) is technically correct but glosses over the fact that this category shows no meaningful differentiation.

- **Overstated claim about adoption of exp-weighted regression.** Line 72 states "we do not observe the adoption of this scheme in many recent diffusion-based RL methods," yet the paper itself cites Kang et al. (2023) and Zheng et al. (2024) as prior work using this approach (line 58). The framing should acknowledge these prior uses more precisely while explaining what DIPOLE adds beyond them.

- **Computational cost of dual-model training not discussed for RL benchmarks.** The method trains two diffusion models (π⁺ and π⁻), doubling parameter count. The LoRA approach for VLA (Section 3.3) partially mitigates this, but the RL benchmark experiments presumably use full models, and the cost implication is not acknowledged.

### Trivial

- Interaction between β and ω as two greediness controls (β shapes sigmoid steepness, ω controls score mixture) could benefit from a brief conceptual explanation of how a practitioner should choose them.

## Nice-to-Haves

- Ablation studies are relegated to Appendix D.4 (line 207). Given that understanding the roles of β, ω, and rejection sampling is central to evaluating the claims, a summary paragraph in the main text would improve accessibility.
- The navtest gain (+6.5 PDMS) is substantially larger than navtrain (+1.4). Discussion of whether this reflects the pretrained model's difficulty on held-out scenarios or DIPOLE's reduced overfitting would add insight.
- The paper could discuss the interaction between rejection sampling and the ω-based score combination — are they substitutes, complements, or independent mechanisms?

## Removed Points

These points were flagged but removed on verification:

- **"Eq. 5 is essentially a standard KL-regularized objective; paper frames it as fundamentally new"** — REMOVED. The paper explicitly presents Eq. 5 as a "greedified KL-regularized RL objective" and acknowledges it "shares a similar spirit with some offline RL methods" (lines 85-88). The novelty claim is properly scoped to the decomposition, not the objective class.

- **"The comparison with CFGRL is somewhat dismissive"** — REMOVED. This is a stylistic opinion, not a substantive weakness. The paper provides a concrete technical critique (indicator-based weighting lacks theoretical backing and limits greediness).

- **"Section 3.3 is too brief" as a standalone criticism** — REMOVED. Merged into specific missing-content points (rejection sampling, value learning) rather than kept as a generic critique.

- **"Risk of negative policy reinforcing bad behaviors through score-subtraction"** — REMOVED. During inference, the negative policy's score is subtracted (Eq. 10), which should push sampling away from low-return regions. The concern about training-time reinforcement of bad behaviors is speculative and does not follow from the method's design.

- **"The paper should discuss whether rejection sampling is already providing a separate greediness mechanism"** — Partially merged into the rejection sampling minor weakness as a suggested discussion point rather than a standalone criticism.

## Novel Insights

The key novel insight is that by reformulating the KL-regularized RL objective with a sigmoid-weighted reference policy (rather than the standard uniform or behavior-cloning reference), the exponential weighting term that typically causes training instability can be algebraically decomposed into two bounded components — each trainable as a separate, stable diffusion model — and then recombined at inference via score arithmetic that mirrors classifier-free guidance. This bridges RL-based policy optimization and diffusion model design in a way that is both theoretically grounded and practically effective. The connection is not merely analogical; the CFG formula (Eq. 10) falls out directly from the RL derivation in Theorem 1 through the algebraic identity σ/(1−σ) = exp, providing a satisfying unification of two previously separate techniques.

## Suggestions

- Add a brief paragraph to Section 3.3 describing the rejection sampling procedure and its interaction with the ω-based score-combination mechanism.
- Either include DDPO/DPPO baselines on a subset of RL benchmarks (e.g., the 4 offline-to-online tasks) or add an explicit justification for their omission (e.g., known scaling difficulties on these domains).
- Add one sentence in Section 3.3 specifying the value function learning algorithm (e.g., "We use IQL-style expectile regression").
- Tone down the claim on line 72 about "not observing adoption" of exp-weighted regression, and acknowledge the prior work the paper itself cites.
- Add a brief note about the computational cost of training two diffusion models for the RL benchmarks.

## Score and Decision

### Anchor Comparison

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Q-Score Matching | StkLULT1i1 | 5.00 | R1 | DIPOLE clearly stronger — much broader experiments, stronger results |
| SODP | fcJKzwlwcs | 4.80 | R1 | DIPOLE clearly stronger — more novel theory, broader validation |
| CTRL | svp1EBA6hA | 6.50 | R1 | DIPOLE comparable-to-superior — similar theoretical quality, broader experiments |
| EFM/QIPO | HA0oLUvuGI | 6.25 | R2 | DIPOLE clearly stronger — more distinctive novelty, clearer performance gains |
| Score Reg. Policy Opt. | xCRr9DrolJ | 6.25 | R2 | DIPOLE comparable — similar quality tier |
| DMBP | ZULjcYLWKe | 7.00 | R2 | DIPOLE comparable — more novel theory, slightly weaker on presentation completeness |

**Round 1 bracket:** 6.0–7.5. DIPOLE sits well above the rejected 5.0 anchor (Q-Score Matching, weak experiments) and the 4.80 anchor (SODP, methodology concerns), and is comparable to or stronger than the accepted 6.50 CTRL paper.

**Round 2 narrowing:** DIPOLE is clearly stronger than the 6.25 EFM paper (which had novelty concerns raised by reviewers) and comparable to the 7.00 DMBP paper. The major weakness (DDPO/DPPO missing from RL benchmarks) and minor presentation gaps bring it slightly below DMBP's level of completeness. Accounting for the tendency to overestimate, the final score settles at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>