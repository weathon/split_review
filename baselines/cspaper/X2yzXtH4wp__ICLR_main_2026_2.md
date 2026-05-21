---
job_id: d06ac5bd-308a-41c3-9fbd-1beec60486aa
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: X2yzXtH4wp.pdf
paper: Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark and empirical study of interactive LLM agents for software engineering, with direct relevance to language agents, safety, evaluation, and datasets/benchmarks.

## Minimum Quality
Pass ✅. The submission contains the expected research components, including abstract, introduction, method, experiments, results, related work, and conclusion/limitations, and it presents a coherent empirical study with substantial quantitative and qualitative analysis.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence of hidden prompts, concealed instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies how LLM-based coding agents handle underspecified software engineering tasks. The authors introduce Ambig-SWE, an interactive variant of SWE-Bench Verified with synthetically underspecified issue descriptions, and evaluate models along three axes: detecting underspecification, asking clarification questions, and leveraging the obtained information to solve the task. Across several open and proprietary models, the paper compares non-interactive, interactive, and fully specified settings, and analyzes interaction behavior using both task success and question-quality measures.

## Strengths
The paper tackles a practically important problem. A lot of coding-agent evaluations quietly assume the user prompt is already complete, while real issue descriptions are often not. Framing the problem around underspecification, rather than only pure code synthesis, is useful and timely.

I liked the decomposition into three capabilities, detection, question asking, and utilization. This gives the paper more structure than a single end-to-end benchmark number. The split across RQ1, RQ2, and RQ3 makes it easier to see where different models fail.

The experimental setup is reasonably broad in terms of model coverage, with both proprietary and open-weight systems and several capability levels. This makes the comparisons informative, especially because the paper does not reduce everything to one headline number.

**Figure 2** is a strong presentation element. It clearly communicates the three evaluation settings, Full, Hidden, and Interaction, and makes the benchmark construction easy to understand. For a benchmark paper, that kind of setup figure matters, and here it helps anchor the later results.

**Figure 3** supports one of the paper’s central claims well, namely that interaction improves performance over the underspecified non-interactive setting. The monotonic pattern from Hidden to Interaction to Full is visible across all evaluated models, which makes the main empirical story easy to verify. Even though I have concerns about confounds in the setup, the figure does establish that the phenomenon being studied is real in the authors’ environment.

The qualitative examples are useful rather than decorative. **Figure 4** concretely shows the difference between broad, poorly targeted questions and more actionable ones. That is much better than simply claiming that some models ask better questions. Similarly, the examples in **Table 7** give a readable sense of what “good” and “bad” clarification behavior looks like.

The paper includes several results tables that do real analytical work. **Table 2** is particularly informative because it shows that underspecification detection is not just a matter of “more prompting helps”; the response to prompt strength is highly model dependent, and in some cases pathological. **Table 1** is also valuable because it goes beyond average success rate and examines the role of navigational information, which helps unpack what kinds of questions are actually useful.

The paper is generally clear and readable. For an empirical benchmark-style paper with multiple settings and measures, the exposition is mostly successful.

## Weaknesses
My main concern is ecological validity of the benchmark construction. On **Page 3, Section 2.1**, the underspecified issues are generated synthetically using GPT-4o by “preserv[ing] specific terminology” while removing detail. The authors do acknowledge differences from naturally underspecified issues, and **Table 5** in the appendix gives examples, but in the main paper this still leaves a substantial gap between the benchmark and the phenomenon it aims to model. The distributional comparison is helpful, yet the conclusion is basically that the synthetic issues are more aggressively stripped of technical detail, especially code snippets and error messages. That matters because an agent’s clarification strategy may look very different on natural, messy, partially informative user reports than on systematically compressed summaries. In other words, the benchmark may be measuring recovery from deliberate information deletion more than handling realistic underspecification.

A second issue is that the comparisons across settings are not as clean as the paper sometimes suggests. In **Section 3.1 on Page 5**, the Interaction condition is not merely “Hidden plus optional user access.” It also changes the prompt substantially, including an instruction that interaction is compulsory, encourages asking questions early, and restricts interaction to at most three times. Meanwhile, the Full condition includes extra hints from SWE-Bench discussions, as described in **Appendix A.2.1**, and the user proxy in the Interaction setting also has access to hints and file locations (**Page 4, Section 2.3**, and **Appendix A.2.2**). So the setting differences mix at least three factors: information availability, prompting/scaffolding, and procedural constraints. This weakens causal claims about “the value of interaction” as an isolated ingredient.

Relatedly, there is a fairness/confounding issue in the model-specific evaluation protocol. The paper states on **Page 5** that Claude Sonnet 4 and Qwen 3 Coder are given up to 100 turns, while the default is 30. In **Appendix A.7**, Qwen 3 Coder is additionally given a modified interaction prompt with a mandatory clarification phase because otherwise it often bypasses interaction. I appreciate the authors being transparent, but this means the cross-model comparisons in RQ1 are not fully apples-to-apples. For Qwen in particular, the evaluated system is not simply “the same agent with the same scaffold on a different base model.” Since one of the main conclusions is about differences in interaction behavior across models, the extra scaffold modifications matter a lot.

The underspecification detection evaluation in **Section 4** is interesting, but methodologically it is somewhat underdefined and arguably conflates detection with prompt compliance. The operationalization seems to be: present either a Full or Hidden issue, vary the interaction prompt, and infer detection quality from whether the model chooses to interact. But with the Neutral/Moderate/Strong prompts in **Table 2**, a substantial portion of the measured behavior is instruction following rather than latent recognition of missing information. This is especially obvious in cases like Llama, where FPR becomes extreme under stronger prompting, and Qwen, where FNR stays at 1.00. That does show something useful about deployed behavior, but it is not a clean measurement of detection ability in the cognitive sense claimed by the section title. Also, the paper later notes in **Section 7** that detection is measured only within the first three turns, which is a consequential design choice but not foregrounded enough when interpreting the results.

The question-quality analysis in **Section 5** is only partially convincing. The core quantitative metric is embedding cosine distance between pre- and post-interaction text, defined in **Equation (1)** in the appendix. But the mathematical formulation is fairly shallow for the importance placed on it. First, the notation is sloppy: \(P=\{p_1,\ldots,p_N\}\) and \(Q=\{q_1,\ldots,q_N\}\) are called “embedding vectors,” yet are written as sets; this is minor mathematically, but it reflects a loose treatment of the metric. More importantly, cosine distance between the summarized task and “cumulative knowledge after interaction” is not obviously aligned with task-relevant information gain. The paper itself implicitly admits this in **Figure 7**, where an alternative recovery metric is discussed as being misaligned because not all information is equally useful. But the same critique applies, to a lesser extent, to the chosen metric as well. Without stronger validation that this score correlates with actionable clarification quality, conclusions like “Qwen extracts the most information” should be treated cautiously.

The statistical reporting is thinner than I would want for a benchmark paper making comparative claims. **Figure 3** reports resolve rates, but there are no confidence intervals or error bars, and the main text emphasizes pairwise Wilcoxon tests whose p-values are only shown in **Table 4** in the appendix. For a dataset of 500 issues, some uncertainty quantification and effect-size discussion should be in the main paper, especially since many conclusions are comparative and model-specific. Similarly, the analysis in **Table 1** is observational: “resolve with navigational info” versus “without” is based on model-chosen behavior, not randomized assignment. The text sometimes reads as if navigational information itself caused the performance change, but selection effects are likely strong here. Models may ask for file locations precisely on tasks they already find harder or easier.

I also think the paper overstates certain interpretations of efficiency. In **Section 3.2**, the paper argues that interaction improves effectiveness but not efficiency because some models use similar or more action steps. That is plausible, but the evidence presented in the main paper is limited to average step counts for a couple of models. Efficiency in this setting is multidimensional, involving wall-clock cost, token usage, number of tool invocations, and user burden. The current discussion is interesting but a bit too sweeping for the amount of evidence provided.

Finally, the paper’s positioning against prior work is decent, but the novelty is more in benchmark framing and analysis than in method. That is fine for a benchmark paper, but it raises the standard for experimental control and dataset validity. Right now, the paper lands as a useful benchmark-style study with real insights, but not yet as a definitive evaluation of underspecification handling in coding agents.

## Questions
1. The biggest thing that would raise my confidence is a cleaner ablation of the interaction scaffold. Can the authors separate the effect of additional information access from the effect of changed prompting and compulsory questioning? For example, what happens with a matched prompt where the agent is told interaction is available but not compulsory?

2. Can the authors report more clearly how much of the RQ1 gain remains when budgets are matched across models and settings, especially for the models given 100 steps? Right now it is hard to disentangle model capability from extra trajectory budget.

3. For **Table 1**, can the authors clarify whether the observed difference between “Resolve w/ Info” and “Resolve w/o Info” is being interpreted causally or descriptively? If possible, a controlled experiment where navigational information is randomized would make the claim much stronger.

4. On the synthetic summaries: did the authors perform any human validation that the generated Hidden issues are genuinely unsolvable without clarification, rather than merely harder? Even a modest manual audit in the main paper would strengthen the benchmark substantially.

5. For the detection task in **Table 2**, what exactly counts as an interaction event for computing FPR/FNR? Is a single clarification question enough, and are tool-based probes or self-talk excluded? Please define the metric more formally.

6. For the question-quality metric based on cosine distance, can the authors show stronger validation that it aligns with task-relevant information gain? For instance, is it correlated with downstream resolve rate after controlling for number of questions? As written, the metric is plausible but not fully convincing.

7. The paper notes in **Section 7** that detection is only measured within the first three turns. Could the authors provide the sensitivity of results to this choice? Some models may reasonably inspect the repo before realizing the issue is underspecified.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the paper itself. The work evaluates coding agents in a sandboxed benchmark and does not appear to involve human subjects or release sensitive data in the main paper.

## Soundness Rating
3: good. The central empirical claim, that interaction helps on underspecified coding tasks, is supported, but several methodological confounds limit the strength of the more detailed comparative conclusions.

## Presentation Rating
3: good. The paper is generally clear, well organized, and supported by effective figures and tables, though some evaluation definitions and metric formulations need sharper specification.

## Contribution Rating
3: good. The benchmark framing and decomposition into detection, clarification, and utilization are useful contributions, but the reliance on synthetic underspecification and scaffold confounds reduce the strength of the overall contribution.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper studies an important failure mode of coding agents, offers a useful evaluation decomposition, and presents informative empirical results. I am positive on the value of the benchmark and analysis, but I have real reservations about ecological validity and experimental disentanglement, so this is not an enthusiastic accept.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the empirical design, figures, tables, and the quantitative metric definitions carefully, though some implementation-level details would still benefit from author clarification.