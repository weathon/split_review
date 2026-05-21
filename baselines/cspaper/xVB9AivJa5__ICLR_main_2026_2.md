---
job_id: 827bcf91-724c-42c8-89d7-e72da884212a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: xVB9AivJa5.pdf
paper: Blueprint-Bench: Evaluating Spatial Reasoning in AI via Apartment Floor Plan Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. This is a benchmark paper for evaluating multimodal and agentic spatial reasoning, which fits ICLR’s datasets/benchmarks and general machine learning scope.

## Minimum Quality
Pass ✅. The paper presents a coherent benchmark contribution with introduction, methodology, evaluation protocol, quantitative results, and conclusion. While the paper does not have a dedicated related work section and the formalization is lighter than ideal, it is complete enough to assess on its merits.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-directed text, or other manipulative content in the provided manuscript.

# Expected Review Outcome:
## Summary
This paper introduces Blueprint-Bench, a benchmark for testing spatial reasoning by asking models to infer a 2D floor plan from multiple interior apartment photographs. The benchmark standardizes outputs into a constrained floor-plan format, extracts room graphs and size rankings from generated images, and scores predictions using a weighted similarity measure over connectivity and room statistics. The paper evaluates several frontier LLMs, image-generation models, and coding agents on 50 apartments, and reports that most systems perform near or below a random baseline while humans remain substantially better.

## Strengths
The paper tackles a genuinely interesting benchmark problem. Reconstructing a coherent floor plan from unordered interior photos is a demanding multimodal reasoning task that is different from standard VQA, captioning, or OCR-heavy benchmarks, and it is relevant to ongoing discussions about what current generalist models can and cannot infer about 3D space from 2D observations.

The standardized output specification in Section 2.1 is a practical design choice. The nine rules make the downstream extraction problem tractable, and this kind of constrained interface is often necessary if one wants robust automatic scoring. In particular, **Figure 1** does a good job of communicating the task and the target representation, and **Figure 4** makes the extraction pipeline much more concrete by showing how room segmentation, room IDs, and detected door connections are derived from a compliant floor-plan image. Those figures materially help the reader understand what is actually being evaluated.

The benchmark compares multiple model families under one task, rather than only comparing LLMs to each other. Including LLMs, image models, agents, a human baseline, and a random baseline gives the paper broader relevance. The comparison in **Figure 7** is especially useful because it prevents the benchmark from becoming an isolated leaderboard without calibration; it shows that the task is solvable by people, but not currently solved by the tested AI systems.

The paper is also refreshingly willing to report a negative result. The empirical message, namely that strong generalist systems still struggle badly on this task, is potentially valuable to the community if the benchmark and scoring protocol are trustworthy.

## Weaknesses
1. **The central evaluation metric is under-validated, and this is the biggest issue in the paper.**  
   The entire benchmark lives or dies by the similarity score in Section 2.3, yet the paper provides only an informal verbal description of the metric and no convincing validation that it aligns with human judgments of floor-plan correctness. The scoring combines six components with fixed weights: 50% edge overlap, 20% degree correlation, 10% density, 10% room count, 5% door count, and 5% door orientation. But these weights appear hand-chosen, and there is no calibration study, no ablation over weights, and no evidence that this weighted sum ranks outputs in a way that matches what humans would consider “more correct.” This matters because the headline claim, that models are near random while humans are much better, depends entirely on this composite score being meaningful.

   The paper should formalize the score explicitly, for example with something like
   \[
   S(\hat{G}, G)=0.5\,s_{\text{edge}}+0.2\,s_{\text{deg}}+0.1\,s_{\text{dens}}+0.1\,s_{\text{rooms}}+0.05\,s_{\text{doors}}+0.05\,s_{\text{orient}},
   \]
   then define each \(s_{\cdot}\) precisely, including range, normalization, and how undefined cases are handled. For instance, what exactly is “degree correlation” when the predicted and true graphs have different numbers of nodes? Pearson correlation on sorted degree sequences, correlation after size-rank matching, or something else? Without this level of precision, the method is not fully reproducible from the main paper, and the scientific interpretation of the scores is shaky.

2. **The room-matching scheme by size rank is fragile and creates cascading penalties that confound the conclusions.**  
   Section 2.4 openly acknowledges that rooms are matched by size rather than semantics, and that a size-ranking error can induce additional penalties in connectivity scoring. This is not a small footnote, it is a structural flaw in the metric. If a model reconstructs the adjacency graph almost perfectly but swaps the order of two similarly sized rooms, the benchmark may score it much worse than its spatial reasoning deserves. The authors themselves effectively admit this when discussing **Figure 7**, where human outputs reportedly had correct connectivity but were still penalized due to size-ranking mistakes. If the human baseline is already being “harshly penalized” by the metric, that is a warning sign that the metric is not cleanly measuring the intended capability.

   Why this matters: if the score entangles graph correctness with size-ordering errors, then the benchmark is not isolating spatial reasoning as clearly as claimed. The paper’s central narrative is “models lack spatial intelligence,” but the actual metric may be partly measuring compliance with a brittle representation choice.

3. **The random baseline, which is central to the narrative in Figures 5 and 7, is not sufficiently specified.**  
   The paper repeatedly states that many models are at or below a random baseline, and **Figure 5** prominently includes a horizontal random-baseline line at 0.279. But the paper does not explain in enough detail how this baseline is generated. Section 2.2 says the authors created a “worst-case baseline by generating typical floor plans using LLMs and image generation models without any image input,” which is not really a standard random baseline. That sounds more like a prompt-based prior baseline or uninformed floor-plan prior, not randomness in the usual statistical sense.

   Several details are missing: How many baseline samples were generated per apartment? Were the same prompts used across models? Were seeds fixed? Was the baseline averaged over models or chosen from one generator? If the “random” line itself comes from strong model priors, then comparing other models against it is conceptually messy. Since much of the paper’s interpretation hinges on “better than random,” the baseline needs to be defined rigorously.

4. **The statistical claims are too loose relative to the evidence shown.**  
   In Section 3 the paper says some models “statistically perform better than the random baseline,” but the evidence shown in **Figure 5** is mean bars with standard-deviation error bars. Standard deviation across apartments/epochs is not a hypothesis test. There is no description of the statistical test used, no confidence intervals, no \(p\)-values, no correction for multiple comparisons, and no explanation of the sampling unit. Is the test over apartments, over repeated generations, or over apartment-generation pairs? Were the generations paired across models on the same apartments? These are not cosmetic omissions. They determine whether the claimed “statistical” superiority is meaningful or just eyeballing overlapping bars.

   Also, averaging “across epochs and apartments” in **Figure 5** raises methodological questions. What exactly is an epoch here, another generation attempt per apartment? If so, repeated samples from the same model-apartment pair are not independent datapoints, and the aggregation should respect that hierarchy.

5. **The experimental protocol is underspecified in ways that make the comparisons hard to interpret and hard to reproduce.**  
   Section 2.2 gives a broad outline, but many key details are missing from the main paper: the exact prompts, whether images are provided in a fixed or randomized order, how many generations are sampled per apartment, model temperatures or decoding parameters, whether there was any prompt tuning per model, how non-compliant outputs were handled, and whether retries were allowed when outputs failed formatting rules. These details matter a lot because the paper itself notes that some models, especially image generators, fail mainly due to instruction-following rather than spatial reasoning.

   This becomes especially important in light of **Figure 6**, which is used to argue that GPT-4o and NanoBanana fail because they do not follow the output specification. If the benchmark is partly testing ability to obey a fairly rigid drawing protocol, then prompt design and post-processing policy have enormous influence on the ranking. The main paper needs to be much more explicit here.

6. **The comparison across model classes is not as apples-to-apples as the paper suggests.**  
   LLMs produce SVG code, image models generate raster images directly, and agents operate with tools and multi-step interaction. These interfaces have very different failure modes. A raster image model can fail because it draws anti-aliased lines or extra furniture; an LLM can fail because SVG syntax is malformed; an agent can fail because its tool loop is inefficient. The benchmark score then collapses all of this into one scalar. That is fine if the claim is “end-to-end ability under a strict interface,” but the paper sometimes makes the stronger claim that it is measuring “spatial intelligence” specifically.

   The problem is visible in **Figure 5** and the discussion around **Figure 6**. Some low scores are attributed to instruction-following failures, not necessarily failures of spatial reasoning. This weakens the causal interpretation of the benchmark outcome. The paper needs to separate, or at least quantify, “format compliance” from “spatial inference given compliant output.”

7. **The dataset is small, private, and only partially calibrated with humans, which limits the benchmark’s scientific value.**  
   The benchmark contains only 50 apartments, and the human baseline in **Figure 7** is from only 12 apartments. For a benchmark paper making broad claims about frontier AI systems, this is quite limited. The paper gives no breakdown of apartment difficulty, no diversity analysis, no inter-annotator or inter-human variability, and no indication of whether some apartments are much easier because the images happen to show strong global cues.

   The privacy rationale for keeping most of the dataset private is understandable, but it weakens reproducibility and independent validation. Since the benchmark’s validity depends heavily on the scoring procedure and data design, the community cannot fully stress-test it if most of the data are unavailable. For a benchmark paper, that is a substantial cost.

8. **The paper does not benchmark against stronger non-generalist baselines, so it is hard to disentangle benchmark difficulty from model unsuitability.**  
   The introduction explicitly mentions systems optimized for floor-plan creation and references prior work, but the experimental section evaluates only generalist LLMs, image models, and coding agents. I understand the authors’ stated goal is to test generalist spatial intelligence rather than task-specialized systems. Still, some stronger baseline is needed to calibrate the task. Even a rough classical or specialized pipeline, or a simple structure-from-motion plus manual heuristics baseline, would help answer whether the benchmark is intrinsically difficult, poorly posed, or simply mismatched to the tested model families.

   Right now the benchmark has human and “random” anchors, but it lacks an intermediate “competent engineered system” anchor. That makes the performance landscape harder to interpret.

9. **Some claims are broader than what the evidence supports.**  
   The paper repeatedly frames the benchmark as revealing a “blind spot” in current AI and as measuring “genuine spatial intelligence.” That is a strong framing. But the actual task bundles many subproblems: multi-view correspondence, scene parsing, scale inference, room segmentation, output-format compliance, and graph extraction robustness. Failing this benchmark certainly suggests a limitation, but the paper overstates how cleanly it isolates a single cognitive construct. A more careful framing would improve the paper.

10. **Presentation is decent at the high level, but the scientific exposition is thinner than it should be for a benchmark paper.**  
   The figures are helpful, especially **Figures 1, 4, 5, 7, and 8**, but several important technical pieces remain informal. For example, **Figure 3** is useful conceptually, showing the floor plan, connectivity graph, and size ordering, but the step from this intuition to the actual score is never formalized rigorously. There is also no results table in the main paper summarizing model means, variances, and significance. Relying only on bar plots makes it harder to inspect exact values and compare models precisely. A benchmark paper would benefit from at least one compact quantitative table with exact scores, compliance rates, and maybe separate metrics for graph accuracy versus format validity.

## Questions
1. Can the authors provide a formal mathematical definition of the full scoring function in the main paper, including exact definitions of each component, normalization, and how node matching is performed when room counts differ?

2. How was the “random baseline” in **Figures 5 and 7** constructed exactly? Please specify prompting, number of samples, model(s) used, whether seeds were varied, and why this should be interpreted as random rather than as an uninformed prior baseline.

3. The paper states that some models are “statistically” above the baseline. What statistical test was used, what was the unit of analysis, and were repeated generations per apartment treated correctly as non-independent?

4. Can the authors report a decomposition of failure modes, for example: (i) output non-compliance, (ii) wrong room count, (iii) wrong graph connectivity, (iv) wrong size ranking? This would help separate instruction-following failures from spatial-reasoning failures.

5. Since Section 2.4 acknowledges that size-rank matching harshly penalizes otherwise good reconstructions, can the authors provide an alternative analysis where connectivity is evaluated under an optimal graph matching or under room-type labels for a subset? Even a small manual study would substantially increase confidence in the metric.

6. Can the authors add exact quantitative values, ideally in a table, for all models shown in **Figures 5 and 7**, including means, uncertainty, and compliance rate with the 9 output rules?

7. Did the prompts, retries, or decoding settings differ across model families? If yes, please report them clearly; if not, please explain why the chosen setup is fair across raster image models, SVG-generating LLMs, and agents.

8. Have the authors tried even one specialized or classical spatial baseline, not because it is the target of the benchmark, but to calibrate benchmark difficulty?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The dataset is described as using apartment interior images and adapted official floor plans from apartment listings, while keeping most of the benchmark private. The paper does not clearly discuss image/floor-plan licensing, permission to redistribute derivative annotations, or whether listing content can be used for a public benchmark and leaderboard. There are also privacy considerations, since apartment interiors and layouts can be sensitive data even if publicly listed at some point. A brief but concrete statement about data sourcing, usage rights, retention, and any filtering of identifying information would strengthen the paper.

## Soundness Rating
2: fair. The benchmark idea is interesting and the empirical observations are plausible, but the central metric and statistical claims are not validated rigorously enough for stronger confidence.

## Presentation Rating
2: fair. The task and figures are easy to grasp, but the paper needs much more precise formalization of the score, clearer experimental details, and exact quantitative reporting beyond plots.

## Contribution Rating
2: fair. The benchmark problem is worthwhile and potentially useful, but the current version does not yet provide a sufficiently validated evaluation protocol to support the strength of its claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The benchmark direction is promising and the negative result is potentially important, but the current paper relies too heavily on an under-validated scoring function and under-specified experimental/statistical methodology.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with benchmark design and multimodal evaluation, though I cannot fully verify all implementation details from the main paper alone.