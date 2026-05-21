Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

**Round 1 bracket:** I placed this paper between weak anchors (avg 2-3, rejected papers with minimal experiments) and strong anchors (avg 8, oral/spotlight papers with extensive validation). The plausible range was 4.0–6.5.

**Round 2 narrowing:** I examined anchors in the 4–6 range. The most relevant are:
- **Make a Donut** (5.25, Reject): LLM-guided planning for deformable manipulation. Has real-robot experiments but unconvincing execution. CoRAL has stronger ablations but sim-only.
- **SC-MLLM** (5.0, Withdrawn): Self-correction with fast/slow systems. Has real-world. CoRAL has more thorough evaluation.
- **LLaRA** (5.25, Accepted Poster): VLA fine-tuning. Has real-world. CoRAL has more novel architecture but lacks real-robot and has the mass inconsistency.

**Final position:** CoRAL is comparable to the 5.0–5.25 papers in most respects but has a significant internal inconsistency in its mass-correction experiment (a central robustness claim). This lowers it to ~4.5 — below the acceptance threshold.

---

## Summary

CoRAL proposes a modular framework for contact-rich robotic manipulation that decouples perception (VLM + FoundationPose) from reasoning (LLM) and integrates them with an MPPI controller, an online adaptation loop, and a memory unit. The LLM generates cost functions and contact strategies, which MPPI optimizes reactively. The system is evaluated on six simulated manipulation tasks against OpenVLA-OFT, π₀.₅, and expert-designed cost baselines, with ablations isolating each component.

## Strengths

1. **Clean role separation validated by ablation.** The Unified VLM variant (collapsing perception and planning into one model) scores 0/10 on most complex tasks (T1, T5, T6), while the full CoRAL succeeds. This provides direct evidence that the modular VLM-for-perception, LLM-for-strategy separation is critical for the paper's task domain. (§4.1.3, Table 1)

2. **LLM-generated contact strategy dramatically improves planning efficiency.** On T6 (Flip with Wall), the LLM-guided strategy is **83.9% faster** (32 vs. 199 steps) and the end-effector travels **63.9% shorter distance** (1.33 m vs. 3.69 m) compared to unguided MPPI sampling. This is a clean, quantitative demonstration of the LLM's symbolic reasoning pruning an otherwise intractable search space. (§4.1.4)

3. **Meaningful baseline comparisons.** CoRAL is compared against two strong end-to-end VLA models (OpenVLA-OFT, π₀.₅) using their official LIBERO checkpoints, plus expert-designed cost baselines (single-stage and FSM). The VLA models achieve 0/10 on T1, T4, T6 while CoRAL succeeds on these tasks, showing the value of the neuro-symbolic approach. (Table 1)

4. **Online adaptation demonstrably helps on multi-stage tasks.** The *w/o Refinement* ablation drops from 4/10 to 0/10 on T1 (Push+Pick Board), confirming that the outer-loop adaptation is essential for long-horizon tasks where initial world-model errors compound. (§4.1.3)

## Weaknesses

### Major

1. **Mass-correction experiment has a critical numerical inconsistency that undermines a core robustness claim.** The text (§4.1.4) states the evaluation world was initialized with a mass of **2.0 kg** (ground truth **0.1 kg**) and friction of 0.9 (ground truth 0.5). However, Figure 4's caption shows the y-axis spanning **0.75–1.00 kg**, with the "Initial Mass" at **1.0 kg** and the "Corrected Mass" converging to **~0.85 kg**. The figure values do not match the text: the initial estimate in the figure is 1.0 kg, not 2.0 kg, and the corrected value of 0.85 kg is an order of magnitude away from the claimed ground truth of 0.1 kg. The paper asserts this "converged remarkably close to their true values," but the data as presented cannot support that claim. Either the text has wrong numbers, the figure is mislabeled, or the adaptation is not working as described. In any case, a key evidence piece for the system's robustness is compromised.

2. **Method specification gap for LLM output parsing.** The paper states the LLM "generates the mathematical structure and relative weights of a cost function" and "is free to introduce any cost terms constructible from the available state, pose, and action variables" (§3.2). However, it never specifies the actual output format (e.g., JSON schema, executable code, parsed natural language template) or how arbitrary cost functions from free text are reliably parsed into the MPPI controller. Equation (2) is an illustrative example, but the claim that the LLM can introduce arbitrary terms requires a concrete description of the parsing mechanism to assess reliability and reproducibility.

### Minor

3. **Ablation comparisons rely on 10 trials with no statistical reporting.** The paper makes strong claims ("memory significantly improved performance," "refinement loop was dramatic," "pose tracking was critical") based on differences such as 2/10 vs. 4/10 (T1, Memory), 5/10 vs. 7/10 (T6, Memory), or 9/10 vs. 10/10 (T3, Memory). With n=10 per condition, these differences are not statistically meaningful — Fisher's exact test gives p > 0.3 for the T1 comparison. No confidence intervals or significance tests are reported. The claims should be tempered to match the evidence, or the number of trials should be increased.

4. **No real-robot validation limits the practical claim for a paper about "contact-rich" manipulation.** The title and framing emphasize contact-rich physical manipulation, and the reactive control augmentation (Eq. 7) is specifically motivated to handle sim-to-real discrepancies. All experiments are conducted purely in simulation. While simulation-only evaluation is acceptable, the paper's strongest claims about robustness and practical applicability would be substantially strengthened by even a single real-robot experiment on a simple contact-rich task.

### Trivial

5. **"Zero-shot" framing is slightly overclaimed.** The initial plan is zero-shot, but the overall system relies on online trial-and-error adaptation (up to 15 retries in the inner loop, plus outer-loop refinement). This is online adaptation through execution feedback, not the typical zero-shot generalization (perform on a new task without any task-specific experience). A qualification like "zero-shot initial planning with online adaptation" would be more precise.

6. **Time column formatting issue in Table 1.** The *w/o Pose Tracking* variant shows dash entries for time on all tasks where success is 0/10, except T2 (9/10) where the time column shows a dash. This is likely a formatting artifact that should be cleaned.

## Nice-to-Haves

- Providing the exact prompt and a concrete example of the LLM's structured output (e.g., the JSON defining a cost function and contact regions for one task) would resolve the method specification gap and improve reproducibility.
- Reporting confidence intervals or increasing trials to 30 per condition would strengthen the ablation conclusions.
- Details on the memory unit's embedding space, retrieval threshold, and similarity metric would clarify when memory helps.

## Removed Points

These points were flagged by the input reviewers but do not meet the standards for inclusion in the final review:

- **Criticism about missing appendix content (proofs, details):** Removed because the parser strips these sections from all papers; they exist in the original submission.
- **Criticism that the paper does not address sim-to-real sufficiently:** The paper explicitly acknowledges this limitation (referenced to App. A.3.2, stripped by parser). This is a known limitation, not a hidden flaw.
- **Criticism about the transition model assumption:** The harsh critic's point about MPPI requiring a known state-transition model *f* is a generic concern about MPPI-based control, not specific to this paper. The paper uses the physics engine as the model, which is standard in simulation-based MPPI work.
- **Strength about "online adaptation recovers from world-model errors and boosts success" (Strength Finder #3):** This strength references the mass-correction experiment, which has the inconsistency documented in Weakness #1. Since the evidence is compromised, the corresponding strength is removed.
- **Criticism about missing confidence intervals for K_f gain matrix:** The gain matrix is a standard component of reactive control; specifying it as a fixed diagonal matrix is common practice. This is a minor implementation detail.
- **Criticism that the Unified VLM ablation may reflect the VLM's inability to output structured plans:** The paper's claim is specifically about role separation — the Unified VLM variant is a deliberate test of that hypothesis. The criticism speculates about alternative explanations without evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the mass-correction experiment.** Align the text and figure numbers. If the true correction is from 1.0 kg to 0.85 kg (as Figure 4 suggests), report that honestly and discuss what it implies about the system's adaptation capability. If the text numbers (2.0 kg → 0.1 kg) are correct, replace the figure. Either way, ensure the evidence and claims match.

2. **Provide concrete LLM output examples.** Show the exact prompt and resulting structured output (e.g., JSON) that defines a cost function and contact regions for at least one task. This would resolve the reproducibility gap and let readers assess the approach's reliability.

3. **Temper the statistical claims.** Replace "significantly improved" with more measured language when reporting 2/10 vs. 4/10 or similar differences. If the authors wish to retain "significant," report a statistical test or confidence interval.

4. **Clarify the "zero-shot" framing.** The paper should explicitly state that the initial plan is generated zero-shot, while the overall system uses online adaptation through trial and error.

## Score and Decision

**Round 1 bracket:** I searched for papers on LLM-based robotic manipulation zero-shot planning across three score bands. The low band (avg < 3.5) returned papers like GRAIL (3.0) and "Exploring and Benchmarking Planning Capabilities of LLMs" (2.0) — papers with minimal experiments or limited contributions. The middle band (3.5–7.5) returned Make a Donut (5.25), SC-MLLM (5.0), LLM+A (4.0), and LLaRA (5.25). The high band (avg > 7.5) returned GenSim (8.0), Data Scaling Laws (8.0), Geometry-aware RL (8.0), and ThinShellLab (8.0) — papers with thorough empirical validation and strong acceptance.

**Round 2 narrowing:** I searched for anchors in the 4–6 and 5–7 ranges. The most directly comparable anchors are Make a Donut (5.25, Reject) — a sim+real LLM-guided planning paper with a similar approach but unconvincing real-robot results — and SC-MLLM (5.0, Withdrawn) — a self-correction framework with real-world experiments. CoRAL has a cleaner ablation study and more complex tasks than these papers, but it also has a more serious internal inconsistency (the mass-correction experiment) and lacks real-robot validation entirely. LLaRA (5.25, Accepted Poster) demonstrates a well-executed pipeline with both simulation and real-world results, though its architectural novelty is lower.

**Final score:** CoRAL is below the acceptance threshold. The paper's core idea is well-motivated, and several ablation results are genuinely informative. However, the mass-correction experiment — a centerpiece of the robustness argument — contains an internal inconsistency between text and figure that makes the evidence uninterpretable as claimed. Combined with the method specification gap, the lack of statistical grounding for the ablation comparisons, and the absence of real-robot validation, the paper's evidence does not support the strength of its claims. A major revision addressing the mass-correction inconsistency, providing concrete LLM output specifications, and adding real-robot experiments could bring this to acceptance level.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>