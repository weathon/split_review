---
job_id: 0fc42dea-c965-4d5b-a4e7-bbc534aa0b3f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: sh1hWO9RHo.pdf
paper: What Is Your Agent’s GPA? A Framework for Evaluating Agent Goal-Plan-Action Alignment
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark/evaluation framework for LLM agents, with relevance to agentic AI, planning, tool use, reliability, and evaluation methodology.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, framework description, experiments, quantitative results, and conclusion. While there are important weaknesses in methodology, positioning, and clarity, they do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence of hidden reviewer-targeting text, prompt injection, or concealed instructions intended to manipulate automated reviewing. The appendix includes judge prompts and some formatting corruption, but this appears to be content/reporting noise rather than a covert attempt to influence review.

# Expected Review Outcome:
## Summary
This paper proposes Agent GPA, a trace-based evaluation framework for LLM agents organized around goal, plan, and action, with six specialized LLM judges in the experiments: Logical Consistency, Execution Efficiency, Plan Adherence, Plan Quality, Tool Selection, and Tool Calling, while the core framing emphasizes five metrics. The paper evaluates these judges on TRAIL/GAIA, a small internal data-agent dataset, and a preliminary SWE-bench case study, reporting improved error identification and localization relative to the TRAIL baseline judge, along with moderate-to-strong agreement with human annotations and some repeated-run consistency analyses.

## Strengths
The paper addresses a real problem. A large fraction of current agent evaluation still collapses everything into final-answer correctness or a monolithic trajectory score, which is not very useful for debugging. The proposed decomposition into goal/plan/action-related dimensions is intuitive and practically motivated, and the paper does a decent job explaining why trace-level evaluation matters for maintainability and failure analysis.

The evaluation setup includes several complementary views of judge quality rather than just one headline number. In particular, the paper reports error coverage, localization, agreement with human scores, and repeated-run reliability. This is better than the common pattern of showing only correlation with one annotator or only a few cherry-picked examples.

I appreciated that the paper does not stop at aggregate recall. **Table 3** and **Table 6** are useful because they expose the very uneven precision-recall tradeoffs across the judges. For example, TC is genuinely much more balanced than PQ on caught-error performance, and EE is much stronger than TC for localization recall. This kind of per-judge breakdown is the right level of granularity for a debugging-oriented framework.

The comparison against the provided TRAIL baseline judge in **Table 2** and **Table 5** is one of the stronger empirical parts of the paper. The gap in test-set error coverage, \(267/281\) versus \(151/281\) or \(154/281\), and in localization, \(241/281\) versus \(87/281\) or \(138/281\), suggests that decomposition into specialized judges can indeed help with trace assessment on this benchmark.

The consistency analysis is also a plus. **Figure 2** and **Table 7** make the reliability story more concrete than the typical “we ran the judge multiple times” claim. In particular, the contrast between EE and PQ is informative: EE shows substantially tighter rationale similarity and lower variance, while PQ is visibly noisier. That is a valuable finding in itself because it indicates which evaluation dimensions are currently automatable and which are still unstable.

The paper is generally readable in the main narrative. **Figure 1** communicates the intended conceptual structure reasonably well, especially the distinction between core GPA dimensions and derived judges such as tool selection and tool calling.

## Weaknesses
1. The paper’s central framing is conceptually inconsistent, and that matters because it blurs what exactly the contribution is.  
On **Page 1** and in the abstract, the framework is introduced as having **five** evaluation metrics: Goal Fulfillment, Logical Consistency, Execution Efficiency, Plan Quality, and Plan Adherence. However, by **Pages 4-5**, the experimental framework prominently includes **Tool Selection (TS)** and **Tool Calling (TC)** as additional judges, and all main experimental tables, including **Table 1-6**, evaluate six judges, not five. This is not just cosmetic. If TS and TC are essential for the reported 95% coverage and 86% localization, then the claimed “GPA” decomposition is not actually the full operational story. The contribution oscillates between a five-metric conceptual framework and a six-judge evaluation suite with two auxiliary tool-focused metrics. The authors should make a clean distinction between the ontology of the framework and the deployed judge set, and then report how much the auxiliary judges contribute beyond the core GPA metrics.

2. The novelty is somewhat overstated relative to what is actually implemented.  
At the methodological level, the paper mainly instantiates a set of specialized LLM-as-a-judge prompts, each with custom instructions, few-shot examples, and structured output templates, as described on **Page 5** and in the appendix prompts. That is a reasonable engineering contribution, but the paper repeatedly suggests a broader conceptual advance in agent evaluation. I am not convinced the main technical step goes much beyond decomposition of trajectory evaluation into hand-designed rubrics plus task-specific prompt tuning. The paper does cite TRAIL, MAST, AgentRewardBench, and related LLM-judge work, but it does not convincingly isolate what is new beyond “specialize the judge by subdimension, provide architecture-aware instructions, and verify against annotations.” Given how much performance appears to depend on custom control-flow instructions and development examples, the submission feels more like careful prompt/program design for an evaluator than a new evaluation principle.

3. The empirical evidence is heavily tied to one agent family and one benchmark trace source, which weakens claims of framework generality.  
The main benchmark results on **Pages 5-8** all come from TRAIL/GAIA traces generated by Hugging Face’s Open Deep-Research Agent. The internal dataset has only **17 traces** on **Page 9**, and the SWE-bench section is explicitly framed as a preliminary case study. This means the strongest claims are really about judging traces from a specific manager/search-agent architecture after adding architecture-specific control-flow instructions. That is much narrower than the broad framing of evaluating “agent systems” in general. The paper needs stronger cross-agent evidence, for example across multiple agent architectures with different planning styles, tool APIs, and trace structures. Without that, it is hard to tell whether the framework is robust or simply well-adapted to the idiosyncrasies of one trace format.

4. The comparison to baselines is too narrow, and this materially affects the significance of the results.  
The principal baseline in **Table 2** and **Table 5** is the TRAIL judge, with or without custom architecture description. That is a relevant baseline, but it is also a weak one for supporting broad claims about LLM judge design. The paper does not compare against other plausible alternatives such as a single strong general-purpose judge with the same trace preprocessing budget, a chain-of-thought or planning-enabled judge, or an agentic judge that can inspect traces stepwise. Because of this, the result “specialized judges beat one monolithic baseline judge” is believable but not especially conclusive. It mostly shows that decomposition helps relative to a specific baseline, not that the proposed framework is close to best practice.

5. Several headline claims are stronger than what the actual numbers support.  
For example, the abstract says the framework “provides a systematic way to cover a broad range of agent failures, including all agent errors on the TRAIL/GAIA benchmark dataset.” But **Table 2** shows test-set collective identification of \(267/281 = 95.02\%\), not 100%. The “all 570 errors” claim on **Page 2** and **Page 6** appears to refer to category mapping by at least one judge, not actual automated detection. Those are different things: one says the taxonomy can label every annotated error after human mapping, the other says the LLM judges automatically catch nearly all errors. The paper repeatedly slides between these notions. This overstatement matters because taxonomy completeness is much easier to establish than automated coverage.

6. The human-evaluation methodology is under-specified in places where the details could change the interpretation of the results.  
On **Page 5**, two human annotators map all TRAIL/GAIA errors to GPA dimensions and a third verifies the mappings. Then, for score alignment, one human annotator generates scores per trace and another verifies. But the paper does not clearly report inter-annotator agreement for the core mapping and scoring procedures in the main text, nor does it explain how disagreements were adjudicated beyond brief statements. The appendix later reports some agreement statistics, but the main paper’s conclusions depend critically on the stability of those human labels. If the rubric is subjective, especially for PQ and LC, then human-LLM “agreement” is less informative without stronger human-human calibration in the main presentation.

7. The scoring setup is awkward and may inflate apparent agreement.  
The judges output a 4-point score in \(\{0,1,2,3\}\), but on **Page 6** the paper explicitly says the middle scores are “not delineated,” then reports off-by-one accuracy and a bucketed 3-point accuracy that merges scores 1 and 2. This is a red flag. If the middle categories are intentionally fuzzy and then collapsed, high alignment numbers become much easier to obtain. This is especially visible in **Table 4**, where off-by-one accuracy is near-perfect for many metrics, but the stricter bucketed 3-point accuracy can drop sharply, especially for EE, where test Acc-3pt is only **0.356** despite a test Acc-OB1 of **0.949**. That is not a minor detail; it indicates the score scale is not well calibrated and the stronger alignment narrative depends heavily on lenient metrics.

8. Some metrics seem poorly validated or fundamentally unstable, yet the paper still presents them as part of the main framework.  
The Plan Quality judge is the clearest example. In **Table 3**, PQ has poor test precision and low F1; in **Table 6**, its localization performance is weak; in **Table 7**, it has the worst reliability with \(\alpha = 0.628\) and by far the highest average standard deviation; **Figure 2** also shows that PQ rationales are the least semantically consistent. The text does acknowledge unreliability, but the paper still treats PQ as a first-class metric in the framework narrative. A more honest framing would distinguish mature metrics from provisional ones. Right now the framework is sold as a coherent suite, while the evidence suggests some components are not ready.

9. The mathematical/statistical treatment of reliability is thin, and parts of the notation are confusing.  
On **Page 6**, the consistency section says “for each trace and metric, we collect scores in \([0,1]\) across 5 independent runs,” yet the judges earlier are defined on a **0 to 3** scale. It is not explained whether scores are normalized to \([0,1]\), binarized, or otherwise transformed before computing Krippendorff’s \(\alpha\). This should be stated explicitly, because \(\alpha\) for interval data depends on the scale and treatment of missing values. Likewise, the paper says \(\alpha\) is computed “including traces with \(\ge 2\) valid ratings,” and **Table 7** reports different \(n\) across metrics, but the source of invalid ratings is not explained in the main text. If repeated runs occasionally fail or return unparsable outputs, that is part of the evaluator reliability story and should not be buried. More broadly, claims like “independent runs produced identical scores with substantial inter-rater agreement” on **Page 2** are too strong when **Table 7** clearly shows nontrivial variance and only one metric below 0.7.

10. The GEPA-based optimization section weakens the clean experimental narrative rather than strengthening it.  
On **Pages 8-10**, the paper switches models from Claude-4-Sonnet to Claude-4.5-Sonnet, replaces human review with a meta-judge for scalability, and then reports prompt-optimization gains. This creates a moving-target evaluation. Improvements could come from the different base model, from the meta-judge’s biases, or from the optimization itself. **Table 8** also does not uniformly show gains, and some metrics degrade relative to manual custom prompts. Since this section changes several variables at once, it does not cleanly support the claim that automated prompt optimization improves the GPA judges.

11. The internal dataset evidence is too small and too opaque to carry much weight.  
The ANON-Data-Agent experiment on **Page 9** uses only **17 traces**, only two metrics (LC and EE), and a proprietary setting with limited task description. **Table 10** gives some agreement numbers, but the sample is so small that strong conclusions about production generalization are premature. Also, because the dataset is internal and only lightly described, it is hard to assess distribution, difficulty, or annotation protocol. This section reads more like an anecdotal industrial case study than a rigorous validation.

12. The presentation has noticeable quality-control issues, especially in the appendix, and some of them feed back into scientific clarity.  
There are several formatting and editing problems: inconsistent naming (“Goal-Plan-Action” versus “Goal-Plan-Act” in **Page 10**), “GEPA” versus “GPA” slips, malformed prompt templates in **Pages 21-31**, duplicated/broken blocks around the Tool Calling prompt, and some dangling or corrupted text snippets. Normally I would treat appendix prompt formatting as minor, but here the method is largely prompt-based, so prompt clarity is not peripheral. The appendix currently makes it harder than necessary to understand what exactly was run.

13. The literature positioning is not fully convincing for a paper whose contribution is mainly evaluation methodology.  
The related work covers several relevant agent-evaluation papers, but the paper does not engage deeply with alternative judge architectures or broader critiques of LLM-as-a-judge reliability. Given that the paper’s main move is to decompose and specialize automated judges, it would benefit from a clearer discussion of why specialization is preferable to other approaches such as stronger single judges, planning-based judges, or environment-aware evaluators. Right now the literature review is adequate but not sharp enough to establish that this particular design is the right abstraction rather than one sensible engineering choice.

## Questions
1. The paper alternates between a five-metric framework and a six-judge experimental suite with TS and TC. Can the authors clearly define the object of contribution? Are TS and TC part of GPA proper, or auxiliary extensions? A revised decomposition table, with ablations showing performance of core GPA alone versus GPA+tool judges, would materially improve my confidence.

2. How much of the performance gain over the TRAIL baseline comes from decomposition into specialized judges, versus simply adding architecture-specific control-flow instructions and few-shot examples? A controlled ablation on **Page 5**’s judge construction choices would be very helpful: generic prompt only, +control-flow description, +few-shot examples, +structured output template.

3. Please clarify the scoring and reliability pipeline mathematically. If the raw judge score is \(s \in \{0,1,2,3\}\), what exact transform \(f(s)\) is used before computing the interval Krippendorff’s \(\alpha\) on **Page 6** and **Table 7**? Why are the reported consistency scores described as scores in \([0,1]\)? Also, what causes the metric-dependent \(n\) in **Table 7**?

4. Can the authors report stronger human annotation diagnostics in the main paper, not only in later appendix tables? In particular: human-human agreement for GPA-dimension mapping, inter-annotator agreement for per-trace scores, and the adjudication protocol when annotators disagreed. This is important because the paper’s claims are framed around “agreement with humans.”

5. The bucketed alignment results in **Table 4** raise concerns, especially for EE. Why is test Acc-3pt for EE only **0.356** while Off-by-one accuracy is **0.949**? If the middle categories are intentionally underdefined, should this be treated as evidence that the scalar score itself is not meaningful, and that only binary error detection should be emphasized?

6. For PQ and PA, the paper repeatedly notes low support sizes and unreliable precision. Would the authors consider reframing these as exploratory metrics rather than mature components? Alternatively, can they provide additional evidence on a dataset with many more explicit planning traces?

7. For the GEPA section, could the authors isolate the effect of prompt optimization from the effect of changing both the model and the verification procedure? Right now **Table 8-9** are hard to interpret causally.

8. Since the strongest results are on one trace source, can the authors provide even one additional public benchmark with a meaningfully different agent architecture and trace schema? That would substantially strengthen the generality claim.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work is an evaluation framework for agent traces and does not, in the presented form, raise direct concerns around privacy, discrimination, or harmful deployment beyond the general caveats that apply to LLM-as-a-judge systems.

## Soundness Rating
2: fair. The empirical study has several solid pieces, especially coverage/localization comparisons and some reliability analysis, but the evidence is narrower and less clean than the claims suggest, several metrics are unstable, and key methodological details about scoring, annotation, and judge construction are insufficiently isolated.

## Presentation Rating
2: fair. The main narrative is understandable, and some figures/tables are useful, but the paper suffers from conceptual inconsistency about the metric set, overclaiming in places, and substantial appendix/prompt formatting issues that matter because the method itself is prompt-centric.

## Contribution Rating
2: fair. The paper tackles an important problem and offers a practically useful decomposition for agent-trace evaluation, but the contribution feels more like a careful engineering framework with partial validation than a fully established evaluation methodology of ICLR caliber.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is useful and practically motivated, and parts of the empirical study are genuinely informative, especially the decomposition-vs-baseline comparison. However, there are too many substantive issues around conceptual clarity, novelty over prompt-engineering baselines, limited generalization evidence, unstable metrics such as PQ, and under-specified scoring/annotation methodology for me to support acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially regarding evaluation design, judge validation, and the interpretation of the reported tables and figures, though some uncertainty remains because the paper’s prompt-based implementation details are partly obscured by presentation issues.