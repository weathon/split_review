---
job_id: ef417f0a-62dc-4abb-9857-e6b5a6f5d9fb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: OUQ8kLRK3m.pdf
paper: Truly Assessing Fluid Intelligence of Large Language Models Through Dynamic Reasoning Evaluation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly in scope for ICLR as a datasets/benchmarks submission on evaluating reasoning and generalization in LLMs, with direct relevance to machine learning, language models, cognitive evaluation, and benchmark design.

## Minimum Quality
Pass ✅. The paper contains the expected core components for a benchmark paper, including abstract, introduction, related work, method, experiments, results, and conclusion; despite substantial weaknesses in methodology and positioning, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden reviewer-targeting instructions, prompt injection attempts, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes DRE-Bench, a dynamically generated benchmark for evaluating the fluid intelligence of large language models through abstract reasoning tasks. The benchmark organizes 36 tasks into four cognition-inspired levels, uses code-based generator-solver pairs to produce task variants with varying complexity, and evaluates a range of general and reasoning-oriented LLMs, along with a human study, to analyze accuracy, stability, and sensitivity to factors such as in-context examples, visual inputs, and inference time.

## Strengths
The paper targets an important and timely problem. The community does need better ways to separate memorization or benchmark contamination from actual rule generalization, especially for reasoning-heavy models. The emphasis on dynamic task generation rather than a fixed static benchmark is a meaningful design choice for this goal.

The benchmark is organized around a clear hierarchy, and this is one of the better aspects of the submission. **Figure 2 (Page 4)** gives a fairly intuitive overview of the four levels, Attribute, Spatial, Sequential, and Conceptual, and the examples do help the reader understand how complexity is supposed to increase within and across levels. Even if I am not fully convinced by the cognitive claims, the task taxonomy itself is reasonably interpretable and more structured than many ad hoc collections of ARC-like tasks.

The code-based generation pipeline is a practical strength. The generator-solver framing described in **Figure 3 (Page 5)** is sensible for constructing verifiable abstract reasoning instances at scale. Compared with purely LLM-generated natural-language test items, having explicit solvers does improve controllability and makes exact-match evaluation possible.

The empirical section is broad in scope. The paper evaluates several proprietary and open models, includes human comparison, studies dynamic complexity trends, and adds ablations on in-context examples, visual inputs, and inference time. For a benchmark paper, breadth matters, and the submission does attempt a reasonably comprehensive first pass.

Some of the descriptive findings are interesting, even when the interpretation is overstated. In **Table 1 (Page 6)**, the cross-level degradation is quite stark, especially on Level 4, and the contrast between stronger reasoning models and standard LLMs is visible on several mid-level tasks. Likewise, **Table 2 (Page 9)** is useful because it shows that naively adding visual renderings of the grid tasks does not consistently help GPT-4o or Claude-3.7, which is a nontrivial empirical observation.

The dynamic evaluation plots are useful for diagnosing failure modes rather than just reporting a single average. **Figure 4 (Pages 7-8)** does a good job illustrating that some tasks degrade smoothly with complexity while others collapse abruptly. This kind of visualization is more informative than one scalar benchmark score, and it aligns well with the paper’s stated motivation.

## Weaknesses
I have several substantial concerns. The paper has an appealing high-level pitch, but the central claims are stronger than what the evidence actually supports.

1. **The benchmark-to-“fluid intelligence” leap is much too strong, and the paper repeatedly overclaims what its tasks measure.**  
   The title and abstract frame the work as “truly assessing fluid intelligence,” and the conclusion again states that current LLMs remain far from “true fluid intelligence.” But what is actually introduced is a benchmark of code-generated grid reasoning tasks with a hand-designed hierarchy. That is not the same thing. The paper cites psychology, especially Primi (2001), but it does not establish that solving or failing these 36 tasks is a valid operationalization of fluid intelligence in the strong sense used throughout the paper.  
   This matters because the main selling point is not merely “a new abstract reasoning benchmark,” but “a benchmark that meaningfully measures fluid intelligence.” Right now, the evidence supports the former much more than the latter. The human study on **Page 7** shows decreasing human accuracy with level, which is directionally consistent, but that does not validate the much stronger construct claim that these tasks faithfully quantify fluid intelligence for LLMs. A benchmark can be useful without making such sweeping cognitive claims; the paper would be stronger if it narrowed those claims.

2. **The cognitive hierarchy is asserted more than validated, and the mapping from tasks to levels feels hand-crafted rather than demonstrated.**  
   In **Section 3.1 (Pages 4-5)**, the four levels are presented as cognition-inspired, but there is little methodological detail on how specific tasks were assigned to levels or why these exact task families instantiate those levels in a unique or justified way. For example, Level 4 is described as “Conceptual” and includes gravity, reflection, and expansion, but these tasks appear to mix abstract reasoning with domain-specific intuitive physics. That may be a useful challenge set, but it muddies the interpretation: are models failing because they lack abstract fluid reasoning, because they lack grounded physical priors, because the task format is brittle, or because the generators produce edge cases that are unlike how such concepts are usually learned?  
   **Figure 2 (Page 4)** is visually helpful, but it also makes this concern concrete: the progression from size/count/shape to move/rotation/symmetry is relatively natural, while the jump from sequential grid procedures to physical concepts is much less clearly on the same latent axis. The hierarchy may be plausible, but it is not convincingly validated.

3. **The benchmark composition is small and imbalanced relative to the strength of the claims.**  
   The paper says DRE-Bench consists of 36 tasks and about 4K cases. **Appendix Table 4 (Page 15)** shows substantial imbalance across task families, such as 1500 Moving examples versus only 50 Expansion examples and 63 Gravity examples. This imbalance is important because the paper frequently reports averages by level or by task family as if they were comparably stable. Small and uneven sample counts make some conclusions fragile, particularly for Level 4 where the reported accuracies are near zero and task coverage is limited.  
   This also affects comparisons in **Table 1 (Page 6)**. When entire conclusions hinge on average performance at a level, uneven task cardinality and difficulty can distort those averages. The paper should at minimum discuss whether averages are micro- or macro-aggregated and how imbalance affects them. Right now that is unclear.

4. **The experimental protocol is underspecified in several places, which undermines confidence in the reported numbers.**  
   In **Section 4.1 (Page 6)** the authors say each variable contains 12 samples for each value on average and results are averaged over three trials, but several essential details are missing from the main paper. It is not clear how many total samples per model per task were used in the main results, whether the same randomly generated instances were shared across models, whether seeds were fixed across trials, whether prompts were identical across models except for API formatting constraints, how outputs were parsed and normalized into grids, and how invalid outputs were handled.  
   These details matter a lot in a benchmark paper because exact-match grid evaluation is brittle. A model can conceptually solve a task and still fail due to formatting noise. The appendix hints at auxiliary metrics, but the main claims are based on exact accuracy, so the main text should be more explicit about parsing and failure handling.

5. **The “100% reliability” claim for generated samples is not adequately supported in the main paper.**  
   On **Page 4**, the paper states: “Our data generation process is code-verifiable, ensuring 100% reliability of the generated samples.” That is a very strong statement. A generator-solver pair can ensure internal consistency, but it does not by itself guarantee that the task is well-posed, free of shortcuts, uniquely solvable from the provided demonstrations, or semantically aligned with the intended latent rule. A buggy but self-consistent generator-solver pair would also pass such a check.  
   The pipeline in **Figure 3 (Page 5)** includes human inspection, but the paper does not quantify inter-annotator agreement, failure rates of generated candidate programs, or any audit of ambiguity/degeneracy across tasks. “Code-verifiable” is a useful property; “100% reliable” is an overstatement. This is not a cosmetic issue, because the trustworthiness of the benchmark is the core contribution.

6. **Several conclusions are drawn from weak or incomplete statistical treatment.**  
   The paper makes repeated statements about “stability,” “variance,” and model intelligence rankings, including the leaderboard in **Figure 1(c) (Page 2)** and the scatter plots in **Figure 5 (Page 8)**. But the main paper never formally defines how variance is computed. Is it variance across dynamic variable values, random seeds, tasks within a level, or the three repeated runs? Those are very different objects statistically.  
   This matters because the paper uses this variance axis to support claims about robustness and generalization. Without a clear definition, these plots are difficult to interpret rigorously. The issue is particularly visible in **Figure 5**, where points are summarized as “higher accuracy and greater stability” when closer to the upper-left, but the reader is left guessing what exactly the variance summarizes. A benchmark paper needs sharper metric definitions, even if no theorem is involved.

7. **The human study is not a clean apples-to-apples comparison, and the ethics statement is internally inconsistent with the experiments.**  
   On **Page 7**, the authors report a human study with 40 professional annotators, salaries, age ranges, and a released questionnaire. But the **Ethics Statement (Page 10)** says, “The study involves no human subjects, no experiments on vulnerable populations, and no interventions requiring IRB approval.” This is simply not consistent with the paper’s own content. The study clearly involves human participants. Whether IRB approval was required depends on institutional policy, but saying “no human subjects” is wrong on the face of the manuscript.  
   Beyond the ethics inconsistency, the human comparison itself is confounded. The appendix describes UI assistance for humans, including row/column numbers and pre-initialized output grids (**Pages 23-25**), which may be reasonable, but the comparison is then not directly matched to the model interface. Humans also solved a 10% subset rather than the full benchmark. None of this invalidates the study, but it means the strong human-vs-model comparisons in **Table 1 (Page 6)** should be interpreted more cautiously.

8. **The main quantitative table reveals task-specific anomalies that the paper does not explain.**  
   **Table 1 (Page 6)** contains some surprisingly extreme patterns that deserve deeper analysis. For example, symmetry is very low for almost all models, even for o1 and DeepSeek-R1, while rotation can be relatively high. Level-4 performance is nearly zero across most models, with occasional isolated nonzero values such as o3-mini on mechanics. There are also very odd patterns in Level 3, such as strong planning relative to sort for some models.  
   These are not necessarily wrong, but they suggest that task implementation details may dominate the benchmark. A strong benchmark paper should spend more time debugging its own task families, rather than immediately interpreting everything as evidence of lacking fluid intelligence. **Table 3 (Page 9)** provides one case study on directional asymmetry, which is useful, but the paper needs more of this level of diagnosis for the headline results.

9. **The visual-information ablation is too narrow to support the broader conclusion that vision does not help abstract reasoning here.**  
   **Table 2 (Page 9)** only covers GPT-4o and Claude-3.7, and only with two prompt styles and two image packaging schemes. That is enough for a pilot result, but not enough for a general takeaway like “adding visual information has little positive impact.” There are many possible reasons for the null result, including poor serialization of the visual examples, suboptimal prompting, limited image resolution semantics, or the models preferring text for these synthetic grids.  
   The finding is still worth reporting, but the paper should present it as a constrained observation under this setup, not a general statement about visual information and abstract reasoning.

10. **The paper’s literature positioning is incomplete for the strength of its claims about abstract reasoning and cognition.**  
   The related work covers ARC-style and dynamic evaluation papers, but the paper does not sufficiently engage with adjacent work on dissociating language and cognition, abstract reasoning benchmarks beyond ARC-like grids, or analyses that question whether benchmark success reflects reasoning versus format mastery. Because the manuscript explicitly makes claims about fluid intelligence and human-like cognition, this broader positioning is not optional.  
   This omission matters because it leaves the contribution looking more isolated than it is. The paper would benefit from a more careful discussion of what DRE-Bench measures relative to other attempts to isolate abstract reasoning, rather than implying it is the first benchmark to meaningfully approach this question.

11. **Presentation quality is uneven, with multiple wording, naming, and consistency issues that make the paper feel less polished than it should be.**  
   There are quite a few examples: “Arthur” and “Spiral” appear in **Appendix Table 5 (Page 17)** where they should presumably be “Attribute” and “Spatial”; model names are inconsistent in **Table 7 (Page 19)**; “OpenAI’s o1” and “OpenAI-o1” are used interchangeably; some references are malformed or duplicated on **Pages 13-14**; and the paper occasionally overstates conclusions in a way that outpaces the actual evidence.  
   These issues are fixable, but in a benchmark paper, presentation and precision are part of the scientific contribution. Ambiguity in labels, aggregation, and metric definitions reduces usability for others.

12. **The benchmark may still be too close to a specialized grid-reasoning evaluation to support the broader generalization claims.**  
   Even if dynamic generation reduces contamination, the task format remains highly stylized: small colored grids, exact symbolic transformations, and few-shot I/O induction. That is a useful subdomain, but the paper often writes as if success or failure here says a lot about “true human-like fluid intelligence” in general. This is too broad. At best, the paper provides evidence about one family of abstract rule induction tasks in an ARC-like format.  
   The distinction matters because benchmark conclusions should match benchmark scope. The paper would be more credible if it framed DRE-Bench as a targeted probe of dynamic abstract rule generalization, not as a near-definitive test of fluid intelligence.

## Questions
1. The biggest issue for me is construct validity. What concrete evidence can the authors provide, beyond the observed human accuracy decline with level, that the four levels in **Section 3.1** are measuring a coherent cognitive hierarchy rather than a hand-designed ordering of task families? For example, can the authors report correlations between human solving time, human error rates, and level/complexity using only the main-paper tasks, or provide an analysis showing that alternative task orderings fit the data worse?

2. Please define precisely how the “variance” or “stability” metric is computed in **Figure 1(c)** and **Figure 5**. Is it variance over complexity values, seeds, samples, tasks, or repeated runs? A formal definition would substantially increase my confidence in the interpretation of those plots.

3. For **Table 1**, are the reported level averages macro-averages across tasks, micro-averages across all examples, or something else? Given the imbalance visible in the dataset counts, this choice matters a lot. Please clarify the aggregation and, ideally, provide both versions.

4. The “100% reliability” claim in **Section 2.2** seems too strong. Can the authors clarify what exactly is guaranteed by the generator-solver verification? Does it guarantee only solver consistency, or also uniqueness of the latent rule from the demonstrations, absence of ambiguity, and semantic correctness relative to the intended task description? A breakdown of failure modes found during manual inspection would help.

5. In **Section 4.1**, please specify the evaluation pipeline in more detail: how were outputs parsed into grids, how were malformed responses handled, were the same seeds shared across all models, and were task instances fixed in advance? These details are central for a benchmark paper.

6. The human study raises both methodology and ethics questions. Please clarify how the human interface differs from the model setup, why those differences were chosen, and whether the comparison in **Table 1** should be interpreted as direct or only approximate. Also, the ethics statement should be corrected to reflect that human participants were involved.

7. Some results in **Table 1** and **Table 3** suggest strong task idiosyncrasies, especially symmetry, sort, and Level-4 mechanics. Can the authors provide a deeper error analysis explaining why these tasks behave so differently? If these anomalies stem from benchmark design quirks, that would affect the interpretation of the benchmark as measuring general reasoning.

8. The visual ablation in **Table 2** uses only two multimodal models. Would the authors be willing to weaken the claim accordingly, or provide stronger evidence that the null effect is not merely an artifact of prompt formatting and image packaging?

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper includes a human study with 40 paid participants, age ranges, questionnaire design, and interface details, described in **Section 4.2 (Page 7)** and **Appendix E.9 (Pages 22-25)**. However, the **Ethics Statement on Page 10** explicitly says, “The study involves no human subjects,” which is inconsistent with the manuscript itself. This should be corrected, and the authors should clearly state whether institutional review, consent procedures, and compensation practices were evaluated under applicable local policies. I do not view this as evidence of misconduct, but it is a real responsible-research issue that should be addressed.

## Soundness Rating
2: fair. The benchmark idea is plausible and the experiments are broad, but several central claims, especially around fluid intelligence, construct validity, metric definition, and benchmark reliability, are not adequately supported in the main paper.

## Presentation Rating
2: fair. The paper is readable at a high level and figures such as **Figure 2** and **Figure 3** help, but important details are missing, aggregation/metric definitions are unclear, and there are multiple consistency and wording issues.

## Contribution Rating
2: fair. The dynamic benchmark setup and code-verifiable generation are useful contributions, but the benchmark scope is narrower than the paper claims, and the validation is not yet strong enough for a more positive score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and has the bones of a useful benchmark, but in its current form it overclaims, under-validates the cognitive interpretation, and leaves too many methodological details unresolved for me to support acceptance.

## Reviewer Confidence
4: confident. I am familiar with LLM reasoning benchmarks and abstract reasoning evaluation, and I checked the main paper carefully; while some concerns could be clarified in rebuttal, the current manuscript leaves substantial unresolved issues.