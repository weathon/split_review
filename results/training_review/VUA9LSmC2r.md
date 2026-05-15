Now I have a complete understanding of both the paper and the reviews. Let me synthesize the final consolidated review.

## Summary

This paper introduces Octopus, an embodied vision-language model that takes egocentric visual input (8 first-person + 2 bird's-eye-view images) and textual task objectives to generate both high-level plans and executable code. The model is trained via supervised fine-tuning on data collected by GPT-4 exploring the OctoVerse environments (OctoGibson and OctoGTA), then further fine-tuned with Reinforcement Learning with Environmental Feedback (RLEF) using a text-only reward model trained on execution traces. The authors release the model, simulator, and dataset.

## Strengths

- **First unified VLM for joint plan-and-code generation from egocentric vision**: Octopus is positioned as the first embodied VLM that directly generates both action plans and executable code from egocentric visual input, contrasting with prior work like TAPA/SayPlan (plans only, with separate vision modules) and EmbodiedGPT (planning then policy mapping). Table 1 and Section 2.1 clearly delineate this distinction.

- **RLEF consistently improves over SFT across settings**: Table 2 shows that Octopus RLEF outperforms Octopus SFT across all evaluation splits. The gains on unseen reasoning tasks are notably substantial (from ~47% to ~67% task completion per the critic's numbers), providing evidence that the environmental feedback loop contributes beyond the initial supervised training.

- **Two customized simulation environments with open-source release**: The construction of OctoGibson (476 tasks, 16 functions) and OctoGTA (20 tasks, 11 functions) represents a concrete resource for the community. The paper's commitment to open-sourcing the architecture, simulator, and dataset supports reproducibility and future work.

- **Ablation studies validate key design choices**: Figure 5 systematically ablates model size (7B vs. 3B), training components (connector-only vs. connector+decoder vs. full), and visual input structure. The sharp performance drop when randomizing visual input order (Figure 5c) confirms that the model leverages structured visual information rather than relying on spurious correlations.

## Weaknesses

### Fatal
None.

### Major

- **The teacher-student modality mismatch is underexplored and raises unanswered questions about visual grounding.** GPT-4 generates the training data using privileged structured environmental information — exact scene graphs, observed objects, observed relations, and inventory (Section 3.2, lines 89-93). While the paper states that "observed objects and relations are substituted by egocentric images to serve as the training input" (Figure 3 caption, line 80), it provides no analysis of whether the information required to produce correct plans and code is actually extractable from those images under real visual conditions (occlusion, lighting, distance, object similarity). **This matters because** the core claim is that Octopus "proficiently decipher[s] an agent's egocentric vision" — but without any failure analysis that traces errors back to visual misidentification vs. planning errors, and without any experiment that controls for what information is visually available, the paper cannot distinguish between genuine visual grounding and the model learning to exploit visual features that correlate with privileged information it never actually "sees." This gap is partially mitigated by the visual ablation (Figure 5c) showing that structured visual input matters, but this does not substitute for direct visual grounding analysis.

- **Experimental rigor is insufficient to fully support the conclusions.** Several specific issues compound this concern:
  - **(a) Baseline specifications are inadequate.** Baselines like "TAPA (adapted)" and "EmbodiedGPT" appear in Table 2 without any description of how they were adapted to OctoGibson, what hyperparameters were used, or whether they received the same post-processing for object name mapping that Octopus uses. Without this information, readers cannot assess whether the comparison is fair.
  - **(b) Human evaluation methodology is absent.** The second value in Table 2 cells is described as "the conceptual accuracy of the model's planning as judged by human evaluators," but the paper provides no rubric, no number of evaluators, no inter-rater reliability measure, and no discussion of how the scores were obtained. This renders the human evaluation component uninterpretable.
  - **(c) No confidence intervals or statistical tests.** With only 60 evaluation tasks (45 seen, 15 unseen; 45 routine, 15 reasoning), the ablation study (Figure 5) reports raw task counts (e.g., 4, 5 out of 60) without any variance estimation. Differences between conditions could reflect noise, and the paper does not address this.
  - **(d) Task breakdown overlap is ambiguous.** The paper states "60 evaluation tasks, with 45 from the seen environment, and 15 that are unseen... We also have 45 routine tasks and 15 require reasoning" (line 163). The overlap between the seen/unseen and routine/reasoning splits is not clarified — are the unseen tasks exclusively reasoning, or is there a mix? This makes interpreting the per-split results in Table 2 difficult.

### Minor

- **The RLEF reward model is text-only, creating a disconnect from the visual task.** The reward model (CodeLLaMA-7B with value head) is designed to "accept only textual modality" for "computational efficiency" (Section 4.3, line 143). It scores state transitions \(\mathbf{T}_i^* \rightarrow \mathbf{T}_r^{\{i,j\}}\) based solely on the task description and generated code text, without access to the visual input that conditions the policy. **Why this is minor rather than major**: The reward model is trained on actual execution traces from the simulator (Section 3.3), so it learns which textual code responses lead to task success or failure in the environment. The policy model *does* see visual input when generating code, and the reward model scores code based on whether it succeeds when executed — implicitly capturing whether the code was appropriate for the visual scene (since visually infeasible code would fail in the simulator). However, this indirect signal is a limitation worth noting, and the paper would be strengthened by either a vision-language reward model or a discussion of how the text-only bottleneck affects the RL signal.

- **RLEF improvements are modest on several splits and significance is unreported.** While RLEF shows meaningful gains on unseen reasoning tasks, the improvements on seen routine tasks appear small (e.g., the critic cites 0.62→0.69). Without confidence intervals or statistical tests, it is unclear whether these smaller deltas represent genuine improvement or noise.

- **Transfer to GTA is reported at 4/11 tasks (36%) without a lower bound.** The paper describes this as "commendable" but does not report what random performance or a zeroshot GPT-4+vision baseline would achieve on these tasks, making the result difficult to interpret.

- **The GPT-4V comparison is anecdotal.** Section 5.3 acknowledges "we couldn't extensively test GPT-4V due to API limitations" and presents only "one sample case." This is essentially no evidence for comparing against the strongest available VLM baseline.

### Trivial

- Table 2 cells with two values are described only in the caption; the table itself could benefit from explicit column headers or visual distinction between the two metrics (task completion rate and human-evaluated plan accuracy).

## Nice-to-Haves

- A controlled experiment comparing the current pipeline (GPT-4 with privileged info as teacher) against one where the teacher is also vision-only (e.g., using GPT-4V to generate training data from the same egocentric images) would directly address the modality gap concern.
- Failure case analysis with the actual visual input shown (FPV + BEV images) would clarify whether errors stem from visual misidentification, planning gaps, or code execution bugs.
- A vision-language reward model, even as a small-scale ablation, would help quantify the impact of the text-only reward bottleneck.

## Removed Points

These points from the reviewer inputs were flagged for removal; treat them with caution:

- **"Teacher-student modality mismatch invalidates the training pipeline"** — Removed from Fatal tier because it overstates severity. The paper *does* train Octopus on vision→code pairs (images are substituted for text, line 80), and the model achieves non-trivial task completion. The concern is valid but as a major weakness (underexplored), not a fatal design flaw.
- **"RLEF reward model cannot evaluate visual reasoning"** — Removed as stated; reclassified as minor because the reward model scores code based on actual execution outcomes, which implicitly capture visual correctness through simulator feedback. The policy sees visual input; the reward model evaluates the textual code against whether it succeeded when executed.
- **"Randomizing vision sequence is obvious/expected"** — Removed. The ablation serves a legitimate purpose: confirming the model actively uses structured visual ordering rather than treating visual input as an unordered bag of features.
- **"Missing Code as Policies in related work"** — Removed; the paper's scope is embodied VLMs, and Code as Policies uses separate vision modules, which the paper explicitly contrasts against.
- **"Formatting/style nitpicks"** — Removed per hard rules.
- **"Missing appendix content / proofs"** — Removed per hard rules (parser strips appendix content from all submissions).

## Novel Insights

The reviews reveal an interesting tension in the paper's contribution. On one hand, the idea of using a teacher LLM with privileged information to generate training data that is then "downgraded" to vision-only for the student is a pragmatic approach to data collection in embodied AI. On the other hand, the reviews correctly identify that the paper provides no empirical analysis of whether the teacher's privileged knowledge "leaks" into the student's training data in ways that make the student appear more capable than it truly is. The most striking insight from the cross-referencing is that the two reviews disagree fundamentally on severity — the harsh critic sees the modality gap as fatal, but the paper's own ablation results (especially Figure 5c, where randomizing visual input causes a sharp drop) suggest the model genuinely uses visual structure, which partially rebuts the strongest criticism. The real missing piece is a failure-mode analysis that would resolve this disagreement empirically.

## Suggestions

1. **Add a visual-grounding analysis**: Examine a sample of failure cases and classify each as visual (object not visible in images), planning (wrong action sequence despite correct visual identification), or execution (API misuse). This directly addresses the modality gap concern.

2. **Add confidence intervals or bootstrapped estimates** for all reported task completion rates, given the small evaluation set (60 tasks).

3. **Provide full baseline details**: Describe how TAPA and EmbodiedGPT were adapted to OctoGibson, including whether they received the same post-processing for object name matching.

4. **Document the human evaluation methodology**: Specify the number of evaluators, whether they were experts or crowd workers, the exact rubric, and inter-rater agreement statistics.

5. **Clarify the task split overlap**: Explicitly state how many of the 15 unseen tasks are routine vs. reasoning.

## Score and Decision

The paper tackles a timely and interesting problem and makes genuine contributions: a new unified VLM for embodied code generation, two customized simulation environments, and an open-source release plan. The RLEF approach shows consistent improvements, and the ablation studies are well-designed. However, the paper's central claim of visual proficiency is weakened by the underexplored teacher-student modality gap, and the experimental evaluation lacks the rigor needed to fully substantiate the conclusions (absent baseline details, no human evaluation methodology, no statistical confidence measures, and an anecdotal GPT-4V comparison). These are significant but addressable weaknesses — they do not invalidate the paper's contributions but do substantially limit how strongly the results can be interpreted. The paper would benefit from a major revision focused on visual grounding analysis and experimental rigor.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>