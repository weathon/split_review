- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5
Now I have a thorough understanding of the paper and the reviewer inputs. Let me compose the final consolidated review.

## Summary

This paper introduces LLM-AAI, a framework for evaluating physical common-sense reasoning in LLMs by embedding them as agents in the Animal-AI 3D environment (a Unity-based virtual laboratory with tasks drawn from comparative psychology). The authors present initial empirical results comparing three state-of-the-art multimodal LLMs (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) against human children (ages 6–10, N=59) and top RL competition entrants on 40 tasks from the Animal-AI Testbed, testing capabilities ranging from food retrieval to object permanence and causal reasoning.

## Strengths

- **Novel framework for embodied LLM evaluation in a 3D environment with cognitive science grounding.** The LLM-AAI framework fills a genuine gap: prior work evaluated LLMs on static text/image benchmarks of physical reasoning, or deployed them in virtual environments (Minecraft, VirtualHome) without a framework designed for *evaluation* against cognitive benchmarks. The connection to the Animal-AI Testbed—a suite of tasks validated in comparative and developmental psychology—is well-motivated (Sec. 3.1, 4.1).

- **Direct comparison across LLMs, human children, and RL agents on identical tasks.** The paper tests three LLM families, 59 children, and top-10 competition agents on exactly the same 40 tasks (Sec. 4.3, Fig. 1–2). This cross-population comparison is enabled by the framework and is a genuine methodological strength.

- **Principled integration of ReAct prompting for embodied control.** The use of `Think`, `Go`, and `Turn` commands following the ReAct framework (Yao et al. 2022) is a sensible design choice that balances the need for structured reasoning traces against the constraints of API-based interaction (Sec. 4.2.1, lines 75–80).

- **Systematic investigation of in-context learning.** Experiment 2 tests whether providing an "expert example" (supervised in-context learning) improves performance on Levels 1–3, with results showing model-specific effects (e.g., GPT-4o improved on Levels 2 and 3; Claude showed mixed effects; Gemini declined). This is a controlled manipulation that yields meaningful differential results (Sec. 4.2.2, Fig. 2).

- **Honest and thorough limitations section.** The paper dedicates significant space (Sec. 6.1–6.5) to discussing sensing limitations, control coarseness, capability confounds, cost constraints, and the path toward cognitively-driven evaluation. The authors acknowledge that the control scheme may dominate the cognitive challenge on some tasks, and that the 30-script cap penalizes LLMs relative to children and RL agents.

- **Explicit reproducibility measures.** Model checkpoints, environment version (AAI 3.1.3), and prompt appendices are specified (Sec. 8). This supports reproducibility despite the use of closed-source models.

## Weaknesses

### Fatal
None.

### Major

- **The abstract and central framing overstate what the empirical results can tell us about physical common-sense reasoning, given the confounded comparison.** The paper acknowledges in its Limitations (Sec. 6.2–6.3) that the LLM control scheme is "a relatively coarse way of controlling an agent" and that "the challenge of controlling the agent in the environment is so large that this dominates the cognitive challenge on some tasks." However, the abstract states the headline finding as "LLMs are currently outperformed by human children on these tasks" without caveating that the comparison involves fundamentally different control regimes (continuous per-timestep control for children vs. a coarse scripting language with no visual feedback during script execution for LLMs). The conclusion hedges slightly ("may lack the physical common-sense reasoning capabilities of humans"), but the aggregate effect—particularly in the abstract—creates the impression that the paper has demonstrated a physical-reasoning deficit in LLMs, when the confound between reasoning and motor control through the scripting interface cannot be resolved from the current design. This is fixable: the framing should lead with the framework contribution and treat the empirical results strictly as a proof-of-concept demonstration that LLMs *can* complete these tasks through this interface, with performance gaps being suggestive but not diagnostic of physical reasoning ability.

### Minor

- **No uncertainty quantification for LLM results.** The paper reports LLM proportions only as single values (e.g., 8/12 trials passed per level) with no confidence intervals or trial-level variance, while showing interquartile ranges for children and competition agents. The paper's justification ("the LLMs are repetitions of the same individual, and so are aggregated into a single value") conflates population variance with measurement uncertainty. With n=12 binary outcomes per level, binomial confidence intervals are straightforward to compute and would meaningfully inform the reader about the reliability of the observed proportions (e.g., 8/12 corresponds to a 95% CI of roughly [35%, 87%]). This omission weakens the reader's ability to assess whether observed differences between models, or between LLMs and children, are reliable (Sec. 5.1, Fig. 1 caption).

- **The claimed "construct validity" of the LLM-AAI framework is asserted rather than demonstrated for the LLM translation of the tasks.** The Animal-AI Testbed has established validity in comparative psychology as administered to animals and humans with appropriate controls (continuous visual feedback, natural action spaces). However, when administered via LLM-AAI, the task changes: the agent receives a single post-hoc 2D image, must process it through a VLM, and must express actions in a formal scripting language. These transformations introduce failure modes (depth estimation errors, mis-quantification of distances, prompt misinterpretation) that are not separated from true physical reasoning failures. The paper claims the approach is "construct valid" (lines 19–21, 165) without providing evidence that the LLM-AAI administration preserves the construct validity of the original tests. A control experiment—e.g., asking the LLM to answer static questions about the same scenes, or comparing performance with ground-truth vs. visual inputs—would address this gap.

- **Floor effects in Levels 8–10 make the comparison uninformative for those levels.** The paper notes this (line 129: "these all occur at a very low success rate, so there may be a floor effect"), but the statement "LLMs are comparable in performance with competition agents in Levels 3, 8, 9 and 10" (line 129) is misleading when "comparable" means both are at or near zero. This does not threaten the main finding but the language should be more precise.

### Trivial

- **It is unclear whether `Think` commands count toward the 30-action-script limit.** The paper states LLMs are "restricted to using, at most, 30 action-scripts, and therefore API calls, per episode" (line 173). If `Think` is counted, this severely limits the number of reasoning steps the LLM can take. This should be clarified.

## Nice-to-Haves

- **Add a sanity-check experiment that isolates the control confound.** Present the LLM with static snapshots of the same scenes and ask it to describe the correct sequence of actions in natural language (without executing them). Compare success rates to the embodied condition. This would help separate "knowing what to do" from "being able to do it through the scripting interface."
- **Analyze the 30-script-limit as a failure mode.** Report how often episodes ended due to hitting the script limit vs. other failures (timeout, death, reward collection). This would help quantify how much the limit constrains performance.
- **Consider a formal statistical comparison to children** (e.g., Fisher's exact test per level) to strengthen the claim that children outperform, rather than relying solely on visual comparison.
- **Discuss potential degradation from growing context windows.** As conversation history accumulates, LLMs may "forget" early observations or be confused by accumulated text—this is a known failure mode for LLM agents and could differentially affect longer episodes (note: the paper mentions token cost in limitations but does not analyze forgetting).

## Removed Points

These points from the inputs were removed or downgraded with justification:

- **Critic's characterization of the control confound as "structural" and "invalidating the primary claim"**: Overly severe. The paper acknowledges this limitation honestly (Sec. 6.2–6.3), and the primary contribution is the framework itself, not the empirical headline. The empirical results are presented as an "initial assessment." The issue is real but is a *framing/calibration* problem, not a fatal one. Retained as Major (not Fatal) with the specific criticism focused on the abstract's lack of caveats.
- **"No significance tests" criticism**: The paper visually compares proportions, which is reasonable for an exploratory study with n=12 per level. Formal hypothesis tests would be desirable but their absence is not a major flaw. Moved to Nice-to-Haves.
- **"Missing discussion of why Experiment 2 showed null results"**: The paper describes the model-specific effects (lines 135–137), which is adequate discussion for a null result. The suggestion to analyze *why* is a nice-to-have extension.
- **"Small sample size" criticism (40 tasks, 3 trials each)**: The paper's sample size matches the prior study with children (Voudouris et al. 2022) and is appropriate for a proof-of-concept. This is not a genuine weakness.
- **"Ablation of image resolution"**: This is a request for additional experiments, not a weakness of what is presented. Moved to Nice-to-Haves.
- **Various format/style nitpicks and generic "areas of concern"**: Removed per filtering rules.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's stated four desiderata (ecological validity, construct validity, non-static, precise target) and the actual demonstration of the third and fourth in the LLM-AAI setting. While the paper convincingly argues that the *Animal-AI Testbed* satisfies these criteria as originally administered, the LLM-AAI translation introduces confounds (sensing lag, coarse control, script limits) that partially undermine the ecological and construct validity of the *LLM version* of the tests. This gap between claimed and demonstrated validity for the new interface is the paper's central tension and the key area for improvement. The fact that all three LLMs showed some non-trivial success on Levels 1–3 despite these constraints is noteworthy and suggests the framework is viable for future, more controlled evaluations.

## Suggestions

1. **Recalibrate the abstract** to lead with the framework contribution and present the empirical results as a proof-of-concept with caveats about the control confound, rather than as a headline finding about LLMs lacking physical common-sense.
2. **Add binomial confidence intervals** to the LLM results in Figures 1–2. With n=12 binary trials per level, this is trivially computed and would substantially improve interpretability.
3. **Clarify the construct validity claim** by adding a paragraph (or a brief control experiment) that acknowledges the gap between the original task validation and the LLM-AAI implementation, and discusses what the specific confounds mean for interpreting results.
4. **Clarify whether `Think` counts toward the 30-action-script limit** and discuss the implications.
5. **Replace "comparable" with "at floor"** when discussing Levels 8–10, where both LLMs and competition agents perform near zero.
