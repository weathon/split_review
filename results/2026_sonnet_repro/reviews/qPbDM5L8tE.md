Now let me search for calibration anchors to score the paper.Based on Round 1, the paper appears to sit between 3.5 and 5.5. Let me narrow within this bracket.Now I have enough information to write the final consolidated review. Let me compile everything.

---

## Summary

CoRAL is a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation. It integrates FoundationPose for 6-DoF pose tracking, GPT-4o (as both VLM and LLM) for physical parameter estimation and MPPI cost function generation, and a RAG-based memory unit for experience reuse. The system is evaluated in simulation (ROBOSUITE/MuJoCo) across six manipulation tasks, with an ablation study demonstrating the contribution of each component.

---

## Strengths

- **The LLM-to-MPPI cost grounding is a genuine architectural contribution.** Rather than feeding LLM outputs to a downstream learned policy, CoRAL has the LLM directly formulate the mathematical structure and weights of the MPPI cost function (Eq. 2). This neuro-symbolic coupling is a concrete and meaningful departure from prior work and is the paper's clearest design novelty.

- **Ablation study demonstrates that role separation is necessary for robust performance.** The *CoRAL (Unified VLM)* variant, which consolidates perception and planning into a single prompt, fails catastrophically on nearly all complex tasks (0/10 on T1, T4, T5, T6; 2/10 on T2), while the full system succeeds. Even granting ambiguity about whether FoundationPose is removed in this condition, the performance gulf is striking and worth reporting.

- **The online refinement outer loop is shown to be indispensable.** Removing refinement collapses T1 success from 4/10 to 0/10 and T3 from 10/10 to 3/10, confirming that the closed-loop adaptation — not just the initial LLM plan — drives success on hard tasks. The prose explanation of how friction misjudgment is diagnosed and corrected (Section 4.1.3) is coherent and informative.

- **Contact strategy guidance measurably prunes the MPPI search space.** On the Flip with Wall task (T6), guided contact sampling produced a trajectory that was substantially shorter and more direct than unguided random sampling (Section 4.1.4). Though this comparison comes from a single trajectory pair, the directional result is visually compelling and consistent with the broader success-rate data.

- **Comparison to human-designed cost functions gives meaningful context.** By including both a single-stage and FSM expert baseline, the paper provides an intelligible performance ceiling against which CoRAL's automatic cost generation can be situated.

---

## Weaknesses

### Fatal
None that fully invalidates every contribution, but the following Major issue threatens the most novel claim of the paper.

### Major

- **The Figure 4 narrative and the figure itself are mutually inconsistent by roughly an order of magnitude.** Section 4.1.4 states: "we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)." However, Figure 4 shows a y-axis spanning 0.75–1.00 kg, with the corrected mass beginning at 1.00 kg and converging to ~0.85 kg. Neither the starting value (1.0 vs. 2.0 kg), the true value (~0.85 vs. 0.1 kg), nor the claim of "converging remarkably close to their true values" is consistent with what the graph actually displays. The section also describes a *friction* adaptation (0.9 vs. 0.5 ground truth) but Figure 4 shows only mass, with no friction trace. This section is explicitly described as the key demonstration of "online correction of physical parameters," called "a cornerstone for deploying robots in unknown environments." Because this is the paper's most novel empirical claim — distinct from the ablation study which covers already-established components — the internal contradiction significantly undermines confidence in this result. This must be corrected, not merely clarified.

- **The "Unified VLM" ablation is potentially confounded with the "w/o Pose Tracking" ablation, making the claimed conclusion unverifiable.** The paper argues (Section 4.1.3): "separating the role of a VLM for perception from a dedicated LLM for strategy formulation is crucial." But the paper never explicitly states whether FoundationPose is retained in the Unified VLM condition. If the unified single-prompt condition also bypasses FoundationPose (as seems likely, since the unified model takes over all perception), then the Unified VLM failure (0/10 on T1, T5, T6) cannot be attributed to role conflation alone — it may be driven by the loss of precise pose tracking, which the *w/o Pose Tracking* ablation independently shows is catastrophic. The paper presents these as separate ablations, but does not confirm the critical detail of whether FoundationPose is active in the Unified VLM condition.

- **Contact strategy comparison in Section 4.1.4 draws strong quantitative conclusions from a single trial.** The "83.9% faster" and "63.9% shorter path" figures are presented as quantitative findings but are derived from a single trajectory pair ("the guided trajectory vs. the unguided trajectory"), not averaged across multiple trials. These numbers should not be treated as population estimates.

### Minor

- **Success rate differences of 1–2 successes over 10 trials are presented as causal component contributions without statistical hedging.** Key findings — memory boosting T1 from 2/10 to 4/10, memory boosting T6 from 5/10 to 7/10 — are stated as clean demonstrations of component benefit. With n=10 and no confidence intervals, these differences are within plausible noise. The directional claims may well be correct, but the paper's certainty in presenting them is not warranted by the data.

- **The contribution bullet about memory enabling "generalization across diverse manipulation scenarios" (Section 1, bullet 4) overstates what is demonstrated.** The memory evaluation tests retrieval within a single task family with randomized parameters; it does not demonstrate cross-task or cross-scenario transfer. The word "generalization" should be qualified.

- **The reactive control term (Eq. 7) leaves $x_{des}$ undefined.** The paper says "the error term is calculated from real-time sensors (e.g., force/torque, proprioception)" but never defines what the desired state $x_{des}$ refers to in the MPPI context (next waypoint, goal, or something else). The gain matrix $K_f$ is also uncharacterized.

### Trivial
- The memory module (Section 3.2) states retrieval occurs via "LLM embeds the current task into a latent semantic space" but does not specify whether embedding is over textual task descriptions, parameter vectors θ, or a combination. For a component producing measurable success-rate improvements, more specificity is warranted.

---

## Nice-to-Haves

- A controlled parameter adaptation experiment (varying the magnitude of initial parameter error systematically and measuring success rate as a function of that error, with and without the adaptation loop) would convert the Section 4.1.4 narrative from an anecdote into a quantified capability evaluation — and it would directly resolve the Figure 4 concern by providing reproducible supporting data.
- Reporting control loop frequency and LLM API latency would sharpen the practicality claims; the paper acknowledges "computational latency" as a limitation but provides no numbers.
- A real-robot demonstration on even one task would substantially strengthen the paper's significance claims.
- Logging a representative sample of actual LLM-generated cost functions and showing that weight choices correlate with task-specific physical requirements (e.g., higher $w_c$ for contact tasks) would directly validate the mechanism rather than just the outcome.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Harsh critic: "VLA baseline comparison is uninformative"** — *Partially removed / demoted.* The paper explicitly frames the comparison as zero-shot: "This setup tests CoRAL's zero-shot capabilities against powerful policies." The VLA models do succeed on simpler tasks (T2: 10/10 for OpenVLA-OFT), demonstrating that their failure on contact-rich tasks is domain-specific, not general. The comparison validly shows that end-to-end policies trained on demonstration data cannot zero-shot generalize to contact dynamics. The comparison is admittedly not symmetric (CoRAL is purpose-built for this domain), but the paper does not overclaim otherwise. This criticism is largely category-driven noise and is removed. The VLA baseline comparison is positioned accurately.

- **Strength Finder: "Online refinement loop enables recovery from incorrect physical assumptions, converging near their true values (Figure 4)"** — *Removed from strengths* because Figure 4 directly contradicts the claimed convergence to ground truth. This strength conflicts with the verified Major weakness; the weakness wins.

- **Strength Finder: "The framework provides human-interpretable failure diagnostics" (Section 4.1.4)** — *Removed.* The example of natural-language diagnosis is described but points to "Appendix ??" (a parser-stripped broken reference). The capability is stated but not concretely demonstrated in the main paper. Too speculative to stand as a strength without verifiable content.

---

## Novel Insights

The paper's most genuinely novel conceptual contribution is the elevation of the LLM from a sub-goal generator or action selector to a cost function architect: the LLM determines the *mathematical structure* of the MPPI optimization problem itself (which cost terms exist and what their relative weights are), not just where to move. This is a sharper form of LLM-grounded planning than preceding VLM-in-MPC approaches. The ablation study, despite its confound concern, provides suggestive evidence that this separation is load-bearing. If the Figure 4 discrepancy is resolved and the adaptation claim is placed on firmer experimental ground, the system has a coherent core worth building on.

---

## Suggestions

1. Reproduce the mass and friction adaptation experiment from scratch, starting at the claimed 2.0 kg initial mass and 0.9 friction, and replace Figure 4 with graphs for both parameters showing convergence (or failure to converge) to ground truth. If the experiment was run differently than described, revise Section 4.1.4 to match the actual experimental conditions.
2. Clarify explicitly whether FoundationPose is active in the *Unified VLM* condition; if it is not, add a separate ablation that isolates role conflation while retaining FoundationPose.
3. Increase trials to 20–30 per condition, or add standard error bars, especially for components where the measured benefit is 1–2 successes in 10 trials.
4. Replace the single-trial trajectory comparison in Section 4.1.4 with a multi-trial average.
5. Define $x_{des}$ in Eq. 7 and specify the implementation of the RAG embedding mechanism in Section 3.2.

---

## Score and Decision

**Round 1 bracket:** The paper sits between 3.5 and 5.5 based on the initial search. The most topically similar anchors are LLM-for-contact-rich-manipulation papers (WtHKqtHVXo, avg 4.0, rejected) and LLM-hierarchical-planning papers (iTsHStJKcm, avg 5.25, rejected; qGL6fE1lqd, avg 4.4, rejected).

**Round 2 narrowing:**
- **WtHKqtHVXo (4.0, rejected):** That paper also uses LLMs for contact-rich manipulation but lacks ablations, memory modules, and has weaker experimental coverage. CoRAL is clearly more complete in architecture and evaluation. CoRAL is better.
- **iTsHStJKcm (5.25, rejected):** That paper integrates LLM hierarchical planning with closed-loop MPC, includes real-world results, and is assessed as borderline. CoRAL lacks real-world validation but has a more coherent and novel cost-formulation architecture. However, CoRAL's critical Figure 4 discrepancy is a genuine quality problem that iTsHStJKcm doesn't have. CoRAL is roughly comparable, slightly worse.
- **qGL6fE1lqd (4.4, rejected):** Physical reasoning with LLMs and world models, simulation only. Somewhat comparable scope to CoRAL. CoRAL has more targeted manipulation experiments but a cleaner story.
- **p01BR4njlY (5.75, accepted):** Notably better in terms of evidence quality and completeness. CoRAL is below this.

CoRAL sits closer to the 4.0–4.5 range. The Figure 4 discrepancy is a real quality problem for the paper's most novel claim, the ablation conflation concern is meaningful, and the paper is simulation-only with n=10 trials. It is clearly better than the weakest anchors (3.0–3.5), comfortably above WtHKqtHVXo (4.0), and somewhat below iTsHStJKcm (5.25). Given the confirmed Figure 4 inconsistency specifically attacking the paper's headline adaptation novelty claim, the final score is **4.5**.

**Axes summary:**
- *Originality:* Moderate-good. The LLM-as-cost-architect framing is a genuine step forward from prior LLM-in-MPC work.
- *Importance of research question:* High. Contact-rich zero-shot manipulation is a relevant and difficult problem.
- *Claim support:* Weak for the key adaptation claim (Figure 4 contradiction), moderate for ablation claims.
- *Soundness of experiments:* Limited. Simulation-only, n=10, no confidence intervals, single-trial trajectory comparisons.
- *Clarity of writing:* Good. The architecture is clearly described; the figure inconsistency is the main clarity failure.
- *Value to research community:* Moderate. The approach is interesting and the ablation structure is informative; the Figure 4 inconsistency must be resolved before the paper achieves its full impact.

**All retrieved anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| oyXoGJQlUf.md (GRAIL) | 3.0 | R1 | Weaker scope; CoRAL is more complete |
| EODzbQ2Gy4.md (Diff-Transfer) | 3.4 | R1 | Different topic; weaker |
| I0To0G5J7g.md (Online Self-Improvement) | 6.25 | R1 | Better real-world validation; much stronger |
| wl1Kup6oES.md (Appearance to Motion) | 3.0 | R1 | Different topic; weaker |
| c0chJTSbci.md (Zero-Shot Diffusion Manip.) | 6.25 | R1/R2 | Real-world + stronger evidence; stronger than CoRAL |
| WtHKqtHVXo.md (LLM Contact-Rich Policy Code) | 4.0 | R1/R2 | CoRAL is more complete; CoRAL is better |
| iTsHStJKcm.md (Make a Donut) | 5.25 | R1/R2 | Similar tier; CoRAL comparable but simulation-only and Figure 4 issue |
| cbVnJa4l2o.md (LLM+A) | 4.0 | R1 | Simpler approach; comparable tier |
| qGL6fE1lqd.md (LLMPhy) | 4.4 | R2 | Similar scope; roughly comparable |
| s3sJenvY5H.md (Generative Robotic Sims) | 4.75 | R2 | Different focus; somewhat comparable |
| p01BR4njlY.md (Solving New Tasks) | 5.75 | R2 | More complete evidence; stronger than CoRAL |
| fZZ4ubttru.md (GenBot) | 5.5 | R2 | More complete generative approach; stronger |
| NxoFmGgWC9.md (Video Generative Pre-training) | 5.5 | R2 | Different topic; stronger |

**Round 1 bracket:** 3.5–5.5  
**Round 2 anchor range used:** 4.0–5.25 (WtHKqtHVXo, iTsHStJKcm, qGL6fE1lqd)  
**Final position:** CoRAL is above WtHKqtHVXo (4.0) but below iTsHStJKcm (5.25), with the Figure 4 discrepancy as the deciding drag.  
**Final score: 4.5 — Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>