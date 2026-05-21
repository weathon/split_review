---
job_id: 722d9c08-ac16-490d-88ae-4f8b004374cd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: MrJoBgN1VO.pdf
paper: GeoGramBench: Benchmarking the Geometric Program Reasoning in Modern LLMs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This is clearly within ICLR scope as a datasets/benchmarks paper for LLM reasoning, with emphasis on symbolic-to-spatial reasoning, evaluation methodology, and geometric program understanding.

## Minimum Quality
Pass ✅ The paper contains the expected structure for a benchmark paper, including abstract, introduction, related work, task definition, benchmark construction, experiments, results/analysis, and conclusion. While I have several substantive criticisms about experimental methodology, positioning, and presentation, I do not see a desk-reject-level flaw such as missing core sections, fatal invalidity, or non-scientific content.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence of hidden prompts, manipulative instructions to automated reviewers, or suspicious injected text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper introduces GeoGramBench, a benchmark of 500 geometry problems containing procedural drawing code, intended to evaluate what the authors call the Program-to-Geometry task, namely translating code such as Asymptote or Matplotlib-style drawing instructions into internal geometric understanding and then solving the associated problem. The benchmark is organized into a three-level taxonomy, Primitive Recognition, Local Relation Composition, and Global Abstract Integration, and the paper reports evaluations of 19 LLMs together with qualitative behavior analysis and a discussion of answer-leakage mitigation during dataset construction.

## Strengths
The paper targets a capability that is genuinely under-evaluated in current LLM benchmarks, namely reasoning from procedural graphics code rather than from natural language alone or from rendered diagrams. That framing is useful, and the task definition in Section 3 gives the benchmark a reasonably clear identity.

The dataset construction effort appears substantial. Section 4 describes a pipeline from 905K candidate problems down to 500 curated items, with manual verification, decontamination, and explicit answer-leakage mitigation. For a benchmark paper, this attention to dataset hygiene is important, and Figure 3 is a good, concrete illustration of why this domain has a special leakage problem. In particular, the distinction between direct leakage and indirect leakage is practical and should be useful beyond this dataset.

The taxonomy is intuitively meaningful even if I am not fully convinced by its validation. The three levels correspond to increasingly demanding forms of geometric scene construction, and Figure 4 helps make this progression tangible. The examples shown there do a decent job of conveying what the authors mean by “Primitive,” “Compositional,” and “Abstract,” rather than leaving the categories purely verbal.

The empirical evaluation is broad in terms of model coverage. Table 1 includes a large set of closed-source and open-source models, and the per-subtype breakdown is potentially informative. The central takeaway, that performance collapses on the Abstract tier, is a useful empirical result for the community, especially because the drop is seen across families rather than for only one or two models.

I also appreciated the attempt to go beyond a single leaderboard table. Figure 2, Figure 6, and the appendix analyses try to connect aggregate performance with failure modes and possible explanations. Figure 6 is particularly useful as an illustrative example of the claimed phenomenon that models can parse local code fragments but still fail to maintain a coherent global spatial representation.

The paper is also reasonably reproducible for a benchmark paper. The authors state the data source pipeline, model prompting protocol, and sampling setup, and they provide qualitative examples and subtype statistics. Even though I have concerns about some evaluation choices, the overall experimental setup is described clearly enough to understand what was done.

## Weaknesses
I think the paper is promising and relevant, but in its current form there are several issues that prevent me from viewing it as a clearly strong ICLR benchmark paper.

1. **The evaluation protocol in Section 5.1 is methodologically underspecified, and the chosen metric is unusual enough that it materially affects how Table 1 should be interpreted.**  
   The authors state, on Page 7, “For each problem instance, we sample 8 responses using temperature 0.6, and report final accuracy as the mean over these 8 outputs.” This is not the standard notion of benchmark accuracy. Formally, if the $i$-th problem has sample-level correctness indicators $c_{i1},\dots,c_{i8}\in\{0,1\}$, then the paper appears to report
   \[
   \mathrm{Acc}=\frac{1}{N}\sum_{i=1}^N \frac{1}{8}\sum_{j=1}^8 c_{ij},
   \]
   which is expected sample correctness, not single-run accuracy, majority-vote accuracy, or pass@8. These are very different evaluation targets. A model with one correct sample out of eight gets credit $0.125$ under this metric, while under majority vote it gets $0$, and under pass@8 it gets $1$. Without reporting at least one deterministic metric or a self-consistency aggregation baseline, the headline numbers in Table 1 are difficult to compare to prior benchmark work. This matters scientifically because the paper’s central claims are comparative, and the choice of metric can alter both rankings and the severity of the reported failure modes.

2. **Table 1 contains serious consistency problems, which undermine confidence in the reported results.**  
   This is not a minor formatting nit. Several entries in Table 1 appear numerically incompatible with the level-wise averages. For example, for GPT-5 the table lists Primitive = 98.44, Compositional = 84.19, Abstract = 50.20, but ALL = 88.67. A weighted average over the category totals in Table 2, namely 102 Primitive, 279 Compositional, and 119 Abstract items, should be far lower than 88.67. Even a simple convex-combination sanity check shows the overall score cannot exceed the largest category average. Similar issues appear for multiple rows. There are also naming inconsistencies such as “GPT-c3-mini”, “GPT-c1”, “Respnke-Shutter-32B”, and “cl-1-32B”, which make it hard to know exactly which models were evaluated. Since Table 1 is the main quantitative evidence of the paper, these inconsistencies are a substantial problem, not a cosmetic one.

3. **The validation of the proposed taxonomy is not very convincing, and Figure 2 does less than the paper claims.**  
   Section 3.2 argues that geometric complexity, rather than reasoning complexity, is the primary axis for Program-to-Geometry tasks. However, the evidence is based mainly on QwQ-32B on the MATH-500 subset, as described around Figure 2. This is a thin basis for validating a benchmark taxonomy that is then applied to all 500 problems and all 19 models. The claim would be stronger if the same trend were shown across multiple model families, with confidence intervals, and perhaps with inter-annotator agreement for the taxonomy labels. As presented, Figure 2 is suggestive, but it does not really establish that the three proposed levels are the right abstraction, nor that “reasoning complexity is largely irrelevant” for code-based geometry problems.

4. **The benchmark’s construction and labeling pipeline relies heavily on GPT-4o-assisted filtering and classification, but the paper does not quantify annotation reliability.**  
   Sections 4.2 and 4.5 say GPT-4o was used for prompt-based classification and for category assignment, followed by human review. But there is no report of agreement statistics, adjudication rules, or how often the model’s initial label was changed by human experts. Since the main contribution is a benchmark, this missing information matters a lot. If the taxonomy labels are noisy, then the core claim that performance sharply declines with geometric complexity becomes less reliable. Likewise, the subtype labels in Figure 5 and Table 1 are used diagnostically, but there is no evidence about consistency of those annotations.

5. **The paper overstates some of its positioning and novelty claims relative to what is actually demonstrated.**  
   The conclusion says GeoGramBench is “the first large-scale benchmark” for this task, and earlier sections frame the contribution as establishing a new evaluation axis. The task framing is useful, but 500 examples is moderate rather than large-scale by current benchmark standards, especially when 108 of them come from augmentation in Section 4.4. More importantly, the paper does not compare against any non-LLM geometry solver or hybrid symbolic baseline, so the empirical framing is narrower than the text suggests. A benchmark about procedural geometry reasoning would be much stronger if it included at least one explicit symbolic, parser-based, or geometry-solver baseline, even if weak, to clarify whether the difficulty is due to LLM limitations specifically or to the task itself.

6. **The behavior analysis in Section 6 is interesting but too anecdotal to support several of the paper’s stronger interpretive claims.**  
   The paper repeatedly argues that models can parse local primitives but fail at global integration, and that chain-of-thought does not effectively update internal geometric representations. Figure 6 is a useful example, and Figures 11 and 12 in the appendix illustrate failure cases, but these are still hand-picked examples. The text on Page 9 explicitly says the analysis is based on “representative examples rather than exhaustive annotation.” That is fair, but then the conclusions should be phrased more cautiously. As written, the paper comes close to making cognitive claims about “internal geometric representations” without systematic evidence. The hypothesis in Figure 13 is reasonable as speculation, but it is not empirically established by the current analysis.

7. **There is a mismatch between some qualitative claims and the quantitative evidence presented in the main paper.**  
   For example, in Section 6, RQ1 concludes that “most of the models achieve 60% accuracy on the Primitive Recognition level,” which is true numerically, but the interpretation that this demonstrates effective construction of basic geometric scenes is too strong. Primitive-level success could still come from local code-token heuristics, direct numerical extraction, or shallow algebraic shortcuts, especially given that the benchmark still contains many coordinate-based constructions. The paper acknowledges answer leakage, but it does not provide a post-mitigation audit quantifying how many items remain solvable through straightforward coordinate manipulation without meaningful diagram abstraction. This matters because the central scientific claim is about spatial abstraction, not just solving geometry questions that happen to contain code.

8. **The paper does not sufficiently disentangle code understanding from downstream mathematical reasoning.**  
   The benchmark combines parsing procedural code and solving the math problem, but the evaluation is based only on final numeric answers. If a model fails, we do not know whether it failed to interpret the code, failed to infer the geometry, or simply failed at algebraic manipulation afterward. This is acknowledged indirectly in the paper’s narrative, but not addressed experimentally. For a benchmark that aims to isolate Program-to-Geometry competence, some intermediate supervision or diagnostic subtask would be very valuable, such as predicting explicit primitives, relations, or a normalized scene graph. As it stands, the benchmark is useful, but it does not cleanly measure the thing it claims to measure.

9. **The paper’s comparison regarding drawing-language invariance is too weak to support the broad claim in Appendix A.**  
   Figure 7 uses only QwQ-32B and only 47 problems translated from Asymptote to Matplotlib. That is a very small basis for the sentence that the principal bottleneck is not the choice of drawing language. It is a reasonable preliminary observation, but it should be framed as such. Different syntactic conventions, API idioms, and latent training exposure could matter much more for other models or other DSLs.

10. **There are literature-positioning gaps for a benchmark paper centered on geometric code reasoning.**  
   The related work covers visual geometry reasoning and SVG understanding, which is helpful. However, the paper would be better positioned if it discussed more directly adjacent efforts on programmatic geometry or formal geometry reasoning. In particular, a comparison to work like TurtleBench would help clarify the distinction between code-to-geometry understanding and geometry-to-code generation or visual-program reasoning. Likewise, classical formal geometry reasoning systems such as Inter-GPS are relevant as contrastive baselines or at least as positioning, especially since this paper is effectively probing the interface between symbolic geometry structure and problem solving. Their absence leaves the related-work story somewhat incomplete.

11. **Presentation quality is uneven, with multiple signs of rushed preparation in the main tables, model names, and prose.**  
   Beyond the Table 1 numerical inconsistencies already mentioned, there are many wording issues, typos, and odd nomenclature choices. Examples include “we expanded these investigations on a broader range of models further corroborate these observations” on Page 1-2, and several malformed model names in Table 1. These may sound minor, but in a benchmark paper they matter because readers need to trust dataset labels, splits, and evaluation identities exactly. The current presentation invites avoidable doubt.

12. **Some ethical and legal aspects are dismissed too quickly.**  
   The ethics statement says the authors are not aware of legal compliance concerns, but the dataset is constructed from multiple public sources and includes manual transcription/adaptation from MathVerse diagrams into Matplotlib code. That may well be fine, but the paper should explicitly state the redistribution and licensing status of the resulting benchmark, especially because benchmark release is part of the contribution. This is not a fatal issue, but “no concerns” feels too absolute.

## Questions
1. In Section 5.1, what exactly is the reported metric? Is Table 1 reporting mean sample correctness across 8 stochastic generations, majority vote over 8 generations, pass@8, or something else? Please define the estimator formally. If you used
   \[
   \frac{1}{N}\sum_i \frac{1}{8}\sum_j c_{ij},
   \]
   please also report single-sample greedy accuracy and/or majority-vote accuracy, since those are much easier to interpret as benchmark numbers.

2. Please audit and correct Table 1. Several “ALL” entries appear mathematically inconsistent with the category-level averages, and some model names are not standard or are garbled. This is important enough that it could change my confidence in the empirical section.

3. How often did human annotators override GPT-4o in the taxonomy assignment and subtype classification pipelines? Please report some measure of annotation reliability, such as inter-annotator agreement, adjudication frequency, or at least the fraction of items relabeled after human review.

4. Can you provide a stronger validation of the three-level taxonomy than Figure 2? For example, showing the same trend across multiple models, or correlating human difficulty judgments with your categories, would substantially increase confidence that the taxonomy is not mostly post hoc.

5. Did you test any non-LLM or hybrid baselines, for example explicit geometry solvers, symbolic parsers, or rule-based extraction of coordinates/relations from code? Even a weak baseline would help separate “LLMs are bad at this” from “this is intrinsically hard for any purely text-based system.”

6. Have you analyzed how many benchmark items remain solvable by straightforward coordinate extraction or simple algebraic reasoning over the code, even after leakage mitigation? A small manual audit would already help support the claim that the benchmark really targets geometric abstraction rather than code-level arithmetic.

7. The behavior-analysis claims in Section 6 would be much stronger with some systematic annotation. Did you consider labeling a subset of failures by error type, such as primitive misparse, orientation confusion, local relation error, global integration failure, or final algebra error? Even a 50-100 item study could materially improve the paper.

8. For the drawing-language comparison in Figure 7, can you clarify whether the Matplotlib translations preserve identical geometric semantics and whether multiple annotators verified them? Also, do you have any evidence beyond QwQ-32B that the conclusion generalizes across models?

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)

## Details Of Ethics Concerns
The concern is modest rather than severe, but I do think the paper should be more explicit here. Section 4 says the benchmark is constructed from public datasets including NuminaMath, HARP, OmniMATH, AIME24, MATH-500, and adapted MathVerse items. The Ethics Statement on Page 10 says there are no legal compliance concerns, yet the paper appears to redistribute transformed problems and manually transcribed diagram code derived from external benchmark content. For a dataset-release paper, it would be better to state the licensing or redistribution status of each source explicitly, especially for the adapted MathVerse subset discussed in Section 4.4.

## Soundness Rating
2: fair. The paper’s main empirical claims are plausible and the benchmark effort is real, but the evaluation metric is underspecified, the main results table appears internally inconsistent, and several interpretive claims are stronger than the evidence provided.

## Presentation Rating
2: fair. The paper is readable overall and the figures are helpful, but the presentation has too many numerical inconsistencies, naming issues, and imprecise methodological descriptions for a benchmark paper.

## Contribution Rating
3: good. Despite the issues above, I do think the paper identifies a meaningful evaluation gap and offers a benchmark that many researchers would likely find useful.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The benchmark direction is relevant and the dataset appears useful, but the paper needs a more rigorous and cleaner empirical presentation, especially around Table 1, metric definition, taxonomy validation, and benchmark positioning.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main methodological and empirical details carefully, though I am less certain about the full space of adjacent benchmark literature.