Now I have a thorough understanding of the paper and reviews. Let me compile the final consolidated review.

## Summary

This paper proposes ACC-Debate, an actor-critic framework for jointly training two LLMs (an actor that produces answers and a critic that provides feedback) to collaboratively solve tasks through multi-round debate. The key methodological innovation is "guided-debate" trajectory generation — an off-policy scheme that steers debate toward/away from the correct answer to efficiently create contrastive preference pairs for DPO training. Empirically, ACC-Debate and its two-round variant ACC-Debate+ achieve top accuracy in 12 of 15 model-benchmark combinations across three model families (Llama-3-8B, Mistral-7B, Gemma-2-2B) and five benchmarks, with gains of up to 8–12 percentage points over prior debate methods like DebateGPT.

## Strengths

- **First joint training framework for multi-agent debate teams.** Prior work treats debate as an emergent behavior of off-the-shelf LLMs or uses debate only to generate data for single-model fine-tuning (DebateGPT). ACC-Debate directly optimizes both agents for collaborative multi-round problem-solving via iterative best-response and DPO (Section 4, Eq. 3–5). This is a principled advance over prompting-only or single-agent training approaches.

- **Consistent and substantial empirical gains.** In Table 1, ACC-Debate/ACC-Debate+ achieves the highest accuracy in 12 of 15 settings. Notable examples: Llama-3 on BoolQ jumps from 0.815 (DebateGPT) to 0.894, Mistral on MMLU from 0.577 to 0.672, and Mistral on BBH from 0.48 to 0.601. These gains hold across three different base model families, showing robustness.

- **Evidence that training enhances collaborative dynamics beyond individual accuracy.** Figure 2 shows ACC-Debate+ has the largest percent improvement from round 0 to round 5 across all three model families, while methods like SoM, SFT, and DebateGPT show little or negligible per-round improvement. Table 2 further shows that even pairing a trained actor with an *untrained* critic already surpasses full-debate baselines, and performance further improves when both agents are trained. The qualitative example (Figure 3) demonstrates that the trained critic shifts from being overly agreeable to providing substantive disagreement.

- **Efficient preference data generation.** The guided-debate scheme (Algorithm 1) addresses a practical bottleneck: when models perform poorly, purely on-policy sampling may yield too few high-value positive examples. Steering toward/away from the correct answer and thresholding by Δ efficiently creates contrastive pairs without massive computational overhead.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of training to *collaborative* dynamics vs. individual improvement is not fully disentangled.** The paper's narrative emphasizes that ACC-Debate trains models to *collaborate* better, but the training pipeline also substantially improves the actor's single-turn (round 0) accuracy. For example, on Llama-3 BoolQ, ACC-Debate achieves 0.887 at round 5, but its round‑0 accuracy (before any debate) already surpasses the SFT model's round‑5 performance. Table 2 confirms that a trained actor with an untrained critic (no collaborative training on the critic side) already outperforms DebateGPT on several datasets. The paper *partially* addresses this via Figure 2 (percent improvement from round 0), which shows ACC-Debate+ has larger *relative* improvement, suggesting real collaborative gain. However, because the round‑0 baselines differ across methods, Figure 2 does not cleanly isolate collaboration from starting-point advantage. A control experiment matching round‑0 accuracy across conditions would substantially strengthen the claim. As it stands, the empirical evidence is consistent with the paper's interpretation but does not conclusively rule out the alternative explanation that much of the gain comes from a better single‑turn actor. **Why it matters:** The paper's central framing is about training for *collaboration*. While the method clearly works (this is not disputed), the mechanism is less certain than the paper suggests.

### Minor

- **The one-step rollout reward estimate is myopic.** The DPO loss is summed over rounds, but the reward estimate \(r(z^{(t)}, x, y)\) is estimated via a single additional round of debate rather than a full rollout to round T. The paper acknowledges this as a heuristic, but it would be useful to know whether the preference ordering is stable under longer rollouts. This does not undermine the results but limits insight into the training signal quality.

- **Analysis of the threshold ε and guided-debate data quality is missing.** The paper uses threshold ε to filter trajectory pairs but provides no analysis of what fraction of examples pass the threshold, how sensitive results are to ε, or how well the off-policy guided trajectories resemble the model's natural debate distribution. The paper discusses the trade-off conceptually but does not quantify it.

- **No analysis of why ACC-Debate+ sometimes degrades performance.** The paper notes (Section 5.1) that a second round of training can hurt performance (e.g., Gemma-2 on several tasks) and recommends using a hold-out set to detect this, but does not investigate *why* this occurs — e.g., whether reward trends diverge, the critic overfits, or the iterative best-response scheme oscillates.

- **Error analysis of failure cases is absent.** For instance, on Gemma‑2 MMLU, ACC-Debate scores 0.51 vs. DebateGPT's 0.582 — a significant deficit. Understanding *why* ACC-Debate fails in this case could illuminate method limitations and guide future improvements.

- **Computational cost is not discussed.** The paper does not report training overhead (number of DPO steps, model-hours, or how the offline trajectory generation cost compares to SFT), making it hard for practitioners to assess the practical trade-off.

### Trivial
None.

## Nice-to-Haves

- **Quantify the critic's behavioral change beyond a single example.** Figure 3 shows one compelling qualitative example of the trained critic disagreeing substantively. Measuring this systematically (e.g., frequency of disagreement markers, token count of feedback, delta between critic's own opinion and actor's answer) across the test set and correlating with accuracy would provide direct mechanistic evidence for the collaborative claim.

- **Compare against inference-time-modified baselines.** Several debate works (e.g., Liang et al., Khan et al.) modify prompts during inference to encourage disagreement without training. Comparing ACC-Debate against a "best-prompted" version of the base model (e.g., explicitly instructing the critic to disagree) would provide a stronger test of whether the benefit comes from training or from increased disagreement generally.

- **Control experiment matching round‑0 accuracy.** Fine-tuning an SFT actor to match ACC-Debate's round‑0 accuracy and then measuring per-round improvement would cleanly separate individual gains from collaborative gains.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing training setup details (learning rate, batch size, DPO steps)"** — Removed per hard rules: these details are standard supplement content, and the parser strips the appendix. The paper references "see section \ref{SUP:preference} of the supplement" indicating these details exist in the original submission.

- **"Clarity on Eq. (1) and (2) notation"** — Removed as a pure formatting/presentation nitpick that does not affect the paper's substance.

- **"Lack of inference-time modification baselines"** — Moved to Nice-to-Haves rather than treated as a core weakness, since the paper's baselines (SoM, Persona, DebateTune, SFT, DebateGPT) are the standard comparators in the field and its own choices are defensible.

- **"Distribution shift between guided and natural trajectories"** — Moved to Minor (threshold analysis) rather than treated as a core weakness since the paper explicitly acknowledges and motivates the off-policy nature (lines 197–198).

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's *framing* (training for collaboration) and the evidence that much of the gain may come from improved individual reasoning. Table 2's finding that a trained actor + untrained critic already beats full-debate baselines, combined with Figure 2's improvement plot, suggests an intriguing division of labor: ACC-Debate's training may primarily teach the actor to be a better *independent* reasoner that is also receptive to feedback, while the critic learns to be less agreeable — but the actor improvement alone accounts for a large fraction of the total gain. This points toward a potentially simpler hypothesis worth testing: whether training only the actor (with a fixed, disagreeable critic prompt) could capture most of the benefit at lower cost.

## Suggestions

1. **Disentangle individual vs. collaborative gains.** At minimum, reframe the narrative in Sections 1 and 5.2 to explicitly separate the two sources of improvement (better single-turn reasoning vs. better collaboration). The ideal fix is the control experiment matching round‑0 accuracy, but even a more cautious framing would address the concern.  
2. **Systematically measure critic behavioral changes** across the full test set (not just one example) to provide quantitative support for the claim that training alters collaborative behavior.  
3. **Report the fraction of examples passing the ε threshold** and perform a sensitivity analysis on ε to ground the guided-debate design choice.  
4. **Investigate why ACC-Debate+ degrades** on some settings and analyze Gemma-2 MMLU as a representative failure case.  
5. **Document computational cost** (training FLOPs/model-hours relative to SFT) to help readers assess practical viability.

## Score and Decision

The paper presents a novel, well-motivated training framework for multi-agent debate and demonstrates clear and substantial empirical gains over state-of-the-art methods across diverse benchmarks and model families. The main weakness — that the collaborative mechanism is not fully disentangled from individual improvement — is genuine but does not invalidate the core contribution: ACC-Debate works better than prior methods. The paper acknowledges this confound and provides partial evidence (Figure 2, Table 2) supporting a collaborative benefit. The remaining weaknesses (missing analyses of the threshold, failure cases, computational cost) are standard depth desiderata that most papers at this venue would benefit from addressing. The contribution is solid and represents a genuine advance in the multi-agent debate literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>