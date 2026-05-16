Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper introduces Octopus, an embodied vision-language model (VLM) that takes egocentric first-person and bird's-eye-view images along with textual task instructions, and outputs both action plans and executable code. The method uses GPT-4 (with access to full symbolic scene state) to generate training data — plans and code — which is then distilled into a VLM (based on Otter/Flamingo architecture with MPT-7B) that operates from vision alone. The pipeline then refines the model via Reinforcement Learning with Environmental Feedback (RLEF), using a text-only reward model trained on step-level and task-level success signals from the simulator. The paper also contributes two simulation environments (OctoGibson, built on OmniGibson, and OctoGTA, built on GTA-V) with 476 and 20 tasks respectively, along with a dataset of vision–code pairs.

---

## Strengths

1. **Unified vision-to-code generation.** Octopus is, to my knowledge, the first embodied VLM that jointly outputs both action plans and executable code from egocentric vision alone. Table 1 clearly positions it against prior work (TAPA, SayPlan, EmbodiedGPT), and the main results (Table 2) show it substantially outperforms blind LLMs (e.g., CodeLLaMA gets 21.1% on seen tasks) and prior VLM planners (EmbodiedGPT gets 36.7%) on task completion in OctoGibson.

2. **Ablation studies validate key design choices.** Figure 5 provides controlled experiments that support the paper's architectural decisions: (a) reducing from 7B to 3B roughly halves task success; (b) freezing all parameters except the connector yields near-zero performance (4/60), whereas full fine-tuning succeeds on many more tasks; (c) randomizing the multi-view image order degrades performance, confirming the model leverages structured visual input.

3. **Automated data-collection pipeline reduces manual annotation.** The paper describes a pipeline (Section 3.2) where GPT-4 generates action plans and code from symbolic environment descriptions, which are paired with egocentric images captured during execution. This enables large-scale supervised training at relatively low human cost.

4. **RLEF shows consistent improvement across all evaluation splits.** While the overall improvement is modest (4/60 tasks), Table 2 shows RLEF improves over SFT on every reported split (seen/unseen, routine/reasoning), suggesting the effect is not driven by idiosyncratic task-level noise.

5. **Open-source commitment.** The abstract states the model, simulator, and dataset will be released, supporting reproducibility and downstream use.

---

## Weaknesses

### Fatal
None.

### Major

1. **Baseline adaptations are underspecified.** Table 2 compares Octopus against TAPA and EmbodiedGPT, but the paper provides no description of how these models were adapted for the OctoGibson environment — e.g., what input they received, how their outputs were post-processed, whether they had access to the same function library, or what prompt templates were used. Without this information, the reader cannot assess whether the baselines were fairly configured or whether the reported performance gap reflects a genuine advantage of Octopus or an artifact of poor baseline adaptation. This undermines the central comparative claim.

2. **Human evaluation component is unsubstantiated.** Table 2 reports "conceptual accuracy of planning as judged by human evaluators" (scores of 0.84, 0.87), but the paper gives no details whatsoever about the evaluation protocol — number of annotators, instructions given, evaluation criteria, or inter-rater agreement. These numbers are presented as quantitative evidence but have no empirical grounding the reader can verify. Either the protocol should be described, or the numbers should be removed.

### Minor

3. **Limited statistical support for RLEF improvement.** The main RLEF result is a 4-task improvement on a 60-task test set (32→36). No confidence intervals, significance tests, or multiple-seed runs are reported. While the improvement is consistent across splits, the small absolute margin and small test set make it impossible to rule out random variation. A bootstrap analysis or repeated runs would strengthen this core claim.

4. **Privileged-information gap in training data is not analyzed.** GPT-4's data-generation process uses full symbolic scene state (scene graph, object relations, inventory), whereas Octopus must infer the same information from egocentric images alone. The paper acknowledges this substitution (Figure 3 caption: "observed objects and relations are substituted by egocentric images") but provides no analysis of when and why vision-based inference diverges from symbolic-state reasoning — e.g., how often failures stem from perceptual ambiguity vs. planning errors. Section 5.3 partially mitigates this by showing Octopus SFT (32/60) slightly exceeds GPT-4 with symbolic input (31/60), but a systematic comparison is missing.

5. **Architecture modifications over Otter/Flamingo are not concretely specified.** Section 4.1 states that "specialized modifications have been made" but then describes standard Otter/Flamingo components (Perceiver Resampler, Cross-Gated Attention) without clearly delineating what, if anything, was changed. The input format (8 FPV + 2 BEV images as a video sequence) is stated, but it is unclear whether any architectural changes were needed to handle this format beyond what Otter already supports.

6. **Text-only reward model discards visual information.** The RLEF reward model is CodeLLaMA-7B with a value head, processing only text. The paper acknowledges this is for "computational efficiency" but does not discuss the risk of reward hacking — i.e., the policy could generate text that scores well without being executable from the actual visual state. No analysis or mitigation is provided.

7. **Key training hyperparameters are missing.** The paper does not report learning rates, batch sizes, number of SFT steps, PPO hyperparameters (KL coefficient β value, number of PPO epochs, reward normalization details), or compute used. These are essential for reproducibility of a method paper.

8. **Post-processing correction extent is unclear.** The paper applies string-similarity matching to replace generic object names with simulator-specific names. The frequency and semantic impact of these corrections are not reported — e.g., does this fix only naming mismatches, or could it change the intended action? The reported task completion numbers may be inflated by how much post-processing corrects.

9. **No failure analysis.** The paper does not categorize what Octopus gets wrong: perception errors (misidentifying objects/relations), planning errors (wrong action sequence), or code execution errors (syntax/runtime failures). This makes it difficult to identify the model's primary bottleneck.

10. **Non-monotonic behavior in ablation not explained.** Figure 5(b) shows that fine-tuning only the connector gets 4/60, connector+decoder gets 5/60, and full model gets 32/60. The jump from 5 to 32 is striking, but the paper does not discuss why the intermediate setting performs so poorly despite having many more parameters than the connector-only setting, or why adding the decoder suddenly unlocks performance when the full vision encoder is also trained.

### Trivial

11. **GTA transferability test is too small.** The few-shot transfer experiment uses only 11 test tasks, with 4 completed. The sample size is insufficient to draw meaningful conclusions about cross-environment generalization.

12. **No limitations section.** The paper lacks a discussion of limitations such as sim-to-real gap, reliance on GPT-4 for data generation, the small number of functions (16 in OctoGibson), and the relatively constrained task scope.

---

## Nice-to-Haves

- A systematic analysis of the vision-to-symbol gap, e.g., comparing Octopus's success on tasks where objects are visually salient vs. occluded or small.
- Confidence intervals via bootstrap resampling for all reported task-completion numbers.
- The GPT-4 system message and environment message templates used for data collection.
- A comparison (or at least discussion) with Voyager, which similarly generates code and uses environmental feedback in Minecraft.
- A breakdown of RLEF improvements by individual task, to show which tasks specifically benefit.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"System-I/System-II analogy is creative but not essential"** — This is a stylistic opinion about presentation, not a weakness of the contribution.
- **"The input format is stated but how multi-image input is tokenized/fed is not specified"** — The paper says it is "treated as a continuous video frame sequence," which is a reasonable description of how the Perceiver Resampler handles multi-image input. This is adequately addressed.
- **Criticisms about missing appendix content** (prompt templates, system messages) — The parser strips appendix content; these may exist in the original submission.
- **"The paper should also cover Y / domain Z"** type demands — These are scope creep unless core to the paper's claim.

---

## Novel Insights

The harsh critic raises a genuinely novel observation: the training pipeline creates an imitation-learning-from-oracle problem where the teacher (GPT-4) has privileged symbolic state that the student (Octopus) must infer from vision. While the paper partially mitigates this by showing Octopus outperforms GPT-4 in the same environment (32 vs 31), the more interesting question is whether the gap manifests differently across task types — e.g., do reasoning tasks that require tracking object relations suffer more from the vision gap than routine tasks? This lens could reframe the paper's contribution as measuring how much of an oracle's symbolic reasoning can be recovered through vision-language distillation, which is a more fundamental question than the paper currently addresses. The text-only reward model exacerbates this concern: RLEF rewards text-based reasoning that may not align with vision-grounded executability.

---

## Suggestions

1. **Describe baseline adaptations in detail** — explicitly state what input TAPA and EmbodiedGPT received, how their outputs were converted to code, and whether they shared the same function library. Consider adding a variant where a strong open VLM (e.g., LLaVA) is given the same images and prompts to generate text for a blind LLM, to isolate the benefit of the specific Octopus architecture.
2. **Add statistical rigor to the RLEF claim** — report bootstrap confidence intervals or results from multiple seeds. Even a simple per-task breakdown of which tasks improve under RLEF would help.
3. **Describe the human evaluation protocol** — number of annotators, instructions, evaluation criteria, and inter-rater agreement must be reported for these scores to be meaningful.
4. **Discuss the vision-to-symbol gap explicitly** in a limitations section, and ideally provide a simple analysis: how often does Octopus fail on tasks where key objects are occluded or visually ambiguous?
5. **Report training hyperparameters** — at minimum: learning rate, batch size, number of SFT steps, KL coefficient β value, and compute used.

---

## Score and Decision

This paper proposes a well-motivated approach to a real problem (embodied code generation from vision), with a plausible training pipeline and reasonable initial results. The main contributions — the unified vision-to-code model, the automated data-collection pipeline, and the RLEF framework — are clearly articulated and represent genuine progress.

However, the paper has significant evidential gaps that prevent full confidence in the claims. The baseline comparisons are not reproducible, the human evaluation scores are unsubstantiated, the RLEF improvement lacks statistical support, and important details (hyperparameters, architecture modifications) are missing. These are fixable with additional analysis and reporting, but as submitted, the experimental evidence is not as strong as the claims.

The paper is a solid *workshop or findability* contribution that could become a strong conference paper with the suggested revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>