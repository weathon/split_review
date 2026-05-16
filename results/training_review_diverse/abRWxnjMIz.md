Now I have a thorough understanding of the paper and can cross-check all reviewer claims against the actual content.

## Summary

This paper introduces and systematically evaluates methods for "scoping" language models — restricting them to answer queries only from specified task categories (e.g., only sentiment analysis) while rejecting all others. The authors adapt Circuit Breakers (CB, Zou et al., 2024) to this task and compare it with system prompting, SFT, DPO, and probing across diverse SNI tasks, adversarial attacks, rejection set diversity, and multiple accept tasks. The main finding is that CB and a novel SFT→CB layering achieve the best balance of robustness and task performance, generalizing from narrow rejection distributions.

## Strengths

1. **Broad empirical comparison across tasks, attacks, and conditions**: The paper systematically compares five methods on three task categories (sentiment analysis, summarization, program execution) under seven adversarial attack types, varying rejection set diversity, and multiple accept tasks (Sections 4.1–4.3). This goes well beyond prior work that evaluates one or two methods on a single task.

2. **Demonstration that CB generalizes from narrow rejection distributions**: Section 4.2 (Figure 3) shows that CB and SFT-CB maintain strong OOD rejection even when trained with only a single reject category, outperforming DPO and probing at low diversity. This is a concrete practical advantage for deployments where limited rejection data is available.

3. **Effective SFT→CB layering**: The simple two-stage training (SFT followed by CB) improves accept task performance while retaining robust rejection. In the Summarization adversarial evaluation (Section 4.1), SFT-CB achieves the best combination of high accept score and high rejection rates across most attack types.

4. **Robustness to a broad set of adversarial attacks**: Seven distinct black-box attacks are evaluated (TAP, multiturn, base-64, prefill, etc.), and CB-based methods are consistently more robust than SFT, DPO, or system prompting. For instance, in Program Execution, CB maintains ~100% rejection on OOD queries under the 2-turn attack while DPO drops to ~50%.

5. **Mechanistic insight via representation analysis**: Section 4.4 shows that SFT and DPO only change representations at the tail end of context, while CB-based methods alter representations across the entire context, providing a plausible explanation for CB's stronger robustness.

## Weaknesses

### Fatal

None.

### Major

1. **Core experiments on a single model only**. All main experiments (adversarial robustness, rejection set diversity, multiple accept tasks) are conducted on Mistral-7B-Instruct-v0.2 alone. The teaser (Figure 1) shows results on Granite, and the paper defers "results for Granite to Figure~\ref{fig:granite}" (line 160), but the central claims about CB's robustness, generalization from narrow rejection sets, etc., are supported only by one model. Scoping behavior depends heavily on base alignment properties, and the paper's own acknowledgment — "Due to the large volume of experiments we are unable to run all models against all permutations" (line 140) — does not mitigate the limitation. Running the main experiments on at least one additional model family is necessary to support the paper's broad conclusions about method performance.

2. **Method-dependent rejection detection creates a systematic measurement bias**. CB-based methods benefit from two detection mechanisms (string matching for "cannot" + repetition detection for broken generation patterns), while other methods rely only on string matching (Section 3.4). If SFT, DPO, or system prompting ever produce repetitive outputs, they would not be counted as rejections. The calibration on 90 samples (30 per accept/reject/OOD) for the repetition detector is too small to ensure comparable operating characteristics across methods, and the paper provides no evidence that non-CB methods never produce repetitive refusal patterns. This directly biases the primary evaluation metric (rejection rate) in CB's favor.

### Minor

3. **No dedicated input classifier baseline**. The introduction (line 15) motivates scoping by noting that "two-stage approaches like relevance classifiers" exist but are brittle, yet the paper never implements one. The Probe baseline operates on internal representations after generation, not as a pre-generation filter on input text. A purpose-built classifier (e.g., a BERT-based task classifier on the input alone) would be a natural and likely strong baseline. Its absence weakens the claim that CB "is more robust than existing methods" since the most obvious competing architectural approach is not compared.

4. **No variance, error bars, or statistical tests reported**. Given the known instability of CB optimization (the paper acknowledges CB "may sometimes be unstable" and has a "sweet spot for performance"), reporting results as point estimates without replication makes it impossible to assess whether observed differences between methods are meaningful. This is especially important for the adversarial evaluation (Section 4.1), where the core comparison depends on fine-grained differences in rejection rates.

5. **Section 4.4 analyses are too brief to be informative**. The claims about precise scoping ("one can scope precisely, e.g. only News summarization instead of all summarization"), effect of data quantity ("as little as 128 instances"), and LoRA rank effects are stated in 1–2 sentences each without quantitative results or figures. The precise scoping claim in particular is asserted with no supporting evidence at all (line 249). For a paper that aims to be comprehensive, these are significant omissions.

6. **No dedicated limitations section**. The Discussion touches on some limitations of CB (instability, issues with large rejection sets), but the paper would benefit from a clear, structured statement of limitations — single-model evaluation, detection bias, framing gap — to help readers interpret the results and understand the scope of the findings.

7. **Connection between representation steering methods and scoping is thin**. The Related Work section discusses Turner et al., Rimsky et al., etc. at length, but these methods do not condition on input and are not used as baselines. The space would be better used discussing the dedicated classifier baseline or more directly relevant refusal methods.

### Trivial

None.

## Nice-to-Haves

- A dedicated input-classifier baseline (BERT-based on input text) would strengthen the comparison, though the paper's focus on single-model solutions makes this optional.
- The precise scoping claim (Section 4.4) should either be backed with evidence or removed.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Gap between motivation and experimental setup" (Harsh Critic Point 4)**: The critic claims the experiments test a different kind of scoping than the motivation. This misunderstands the paper. The motivation gives illustrative examples (poetry, physics, company policies); the experiments operationalize the same concept — restricting a capable model to specific task categories. Scoping between SNI tasks (sentiment analysis vs. summarization) is exactly the right experimental paradigm for studying this capability. The examples in the introduction do not define a different experimental target; they contextualize the problem.
- **"Figures not present" / "Missing appendix"**: Parser artifacts from the extraction process. The figures and appendix exist in the original submission.
- **"Framing gap about sensitive company policies"**: The critic's suggestion that experiments should test proprietary knowledge scenarios is scope creep. The paper studies the general capability of task-level scoping, which is appropriately operationalized with SNI tasks.

## Novel Insights

The most interesting observation from the synthesis of reviews is the fundamental tension between CB's strength (representation-level intervention that generalizes broadly from narrow data) and its weakness (instability under high diversity, detection-dependent evaluation). The SFT→CB layering partially resolves this tension but inherits CB's evaluation biases. A genuinely novel direction that emerges is the question of whether conditional orthogonalization — orthogonalizing one reject task at a time rather than all at once — could preserve CB's generalization at low diversity while avoiding the crash at high diversity. The paper hints at this ("we may need a conditional orthogonalization method to orthogonalize one task at a time") but does not pursue it.

## Suggestions

1. **Run the core adversarial evaluation (Section 4.1) on at least one additional model** — e.g., Llama-3-8B-Instruct or a Granite variant. The teaser already has Granite results, so extending this to the full evaluation would be a natural and high-impact addition.

2. **Unify rejection detection across methods**. Use a separate judge (e.g., a fine-tuned RoBERTa classifier on early tokens, or human annotation on a representative subset) that is applied uniformly to all methods, eliminating the asymmetric advantage from CB's dual-detector setup.

3. **Report confidence intervals or variance across seeds** for the main results (at least 3 seeds). Given CB's acknowledged optimization instability, readers need to know whether reported differences are meaningful.

4. **Add the dedicated input-classifier baseline** (e.g., BERT fine-tuned on task descriptions), even if only for the main adversarial evaluation.

5. **Back the precise scoping claim (line 249) with quantitative evidence** or remove it — an unsupported empirical claim weakens the paper's credibility.

6. **Add a limitations section** clearly stating: (a) single-model evaluation for main experiments, (b) method-dependent rejection detection, (c) absence of a dedicated input classifier baseline.

## Score and Decision

The paper addresses an important and practical problem and provides the first systematic comparison of methods for LM scoping. The finding that CB generalizes from narrow rejection distributions and resists adversarial attacks better than SFT/DPO is genuinely useful. However, two structural issues prevent the current evidence from fully supporting the conclusions: (1) the core experiments are on a single model, and (2) the method-dependent rejection detection asymmetrically favors CB. These are addressable but nontrivial.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>