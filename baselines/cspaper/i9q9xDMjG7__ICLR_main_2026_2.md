---
job_id: a7cec0fe-5936-4048-bb0e-5e3e0c9ce1ae
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: i9q9xDMjG7.pdf
paper: When to Use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This submission is clearly in scope for ICLR as a datasets-and-benchmarks paper on retrieval-augmented generation, graph-based knowledge representations, and evaluation methodology for LLM systems.

## Minimum Quality
Pass ✅ The paper has the necessary components for a benchmark paper, including abstract, introduction, benchmark design, evaluation methodology, experiments, quantitative results, and conclusion. While there are notable clarity and methodology issues, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence of hidden prompts, concealed instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces GraphRAG-Bench, a benchmark intended to evaluate when graph-based retrieval-augmented generation is actually helpful relative to vanilla RAG. The benchmark contains two corpora, one medical and one literary, four task categories with increasing complexity, and stage-specific evaluation spanning graph construction, retrieval, generation quality, and efficiency. Using this benchmark, the authors compare several GraphRAG systems against standard RAG and draw practical conclusions about when graph structure helps, especially for more complex reasoning and synthesis tasks.

## Strengths
The paper addresses a timely and practically relevant question. A lot of GraphRAG work currently argues for structured retrieval in broad terms, but this paper asks the more useful question, namely when the extra graph machinery is worth using. That framing is valuable for the community.

The benchmark is broader than many prior RAG evaluations in one important sense: it does not collapse everything into a single end metric. The decomposition into graph quality, retrieval quality, generation quality, and efficiency is a real strength. Even if some of the metrics need sharper definition, the paper is directionally correct that evaluating GraphRAG only via final answer accuracy hides where gains or failures come from.

I appreciated the attempt to vary task complexity rather than just dataset identity. Table 1 provides a simple but useful taxonomy from fact retrieval to creative generation, and Appendix Table 8 makes the intended complexity control more concrete through “knowledge breadth” and “reasoning depth.” That is a better design instinct than equating “multi-hop” with genuine reasoning difficulty.

The empirical study is reasonably extensive in model coverage. In the main paper alone, Table 3 and Table 4 compare several representative GraphRAG methods and two RAG baselines on both corpora. The broader pattern in those tables is coherent: vanilla RAG is competitive or stronger on simple retrieval-heavy settings, while some GraphRAG variants, especially HippoRAG2, improve on harder synthesis-oriented tasks. That high-level message is useful and the tables do support it, even if not every causal claim is fully isolated.

The paper includes an efficiency analysis, which many benchmark papers conveniently ignore. Tables 6 and 7 are useful because they make the cost side impossible to miss. For example, the reported prompt sizes for MS-GraphRAG(global) and LightRAG are extremely large relative to vanilla RAG and HippoRAG2. That matters in practice and strengthens the benchmark’s utility.

Figure 1 does a good job of visually contrasting the intended difference between RAG and GraphRAG pipelines. In particular, the emphasis on implicit relations, hierarchical reasoning, and context growth makes the paper’s motivating hypothesis clear before the experiments begin. Figure 5 is also helpful because it ties one of the central empirical claims to graph topology rather than only final answer quality, showing substantial variation in graph density across methods.

The takeaways are practically interpretable. Even though I have issues with how strongly some of them are phrased, the benchmark does lead to actionable conclusions such as “do not assume graph retrieval helps on simple fact lookup” and “context growth is a serious cost bottleneck.” Those are the kinds of conclusions practitioners actually need.

## Weaknesses
I think the paper is useful, but there are several places where the methodology is not yet tight enough for the strength of the claims being made.

1. **The benchmark design still does not cleanly isolate the effect of “using graphs” from many other system-level confounders.**  
   This is the biggest issue for me. The central question of the paper is “when to use graphs in RAG,” but the compared systems differ in much more than graph structure. As shown in Appendix Table 18 and the configuration details on Pages 28 to 31, these methods vary in indexing unit, retrieval granularity, query formulation, prompt format, chunk size, top-$k$, and generation context style. For example, HippoRAG2 uses phrase and passage nodes, MS-GraphRAG(local) retrieves entity, relationship, chunk, and community structures, RAPTOR is tree-based, and vanilla RAG uses plain chunk retrieval. This means the study is really comparing full end-to-end systems, not graph structure as a controlled variable.  
   Why this matters: if one method wins on complex reasoning, that could be due to better prompt construction, larger retrieved context, reranking behavior, passage aggregation, or generation formatting, not necessarily because it used a graph. The paper acknowledges practical comparisons, but some of the broader conclusions, especially in Section 4, are written as if they identify causal benefits of graph structure itself.

2. **Several of the proposed metrics are underspecified mathematically and operationally, which weakens the soundness of the stage-specific evaluation.**  
   The main paper introduces retrieval and generation metrics in Section 3.3, but key pieces are pushed into informal operators. In Appendix F, Equation (3) defines Context Relevance as
   \[
   \textsc{Context Relevance}=\frac{1}{|\mathcal{C}|}\sum_{c\in\mathcal{C}} R(c,Q,\mathcal{E}),
   \]
   and Equation (4) defines Evidence Recall using an indicator over whether a claim is “supported” by retrieved context. Similarly, Equation (7) for faithfulness and Equation (8) for coverage rely on boolean support/matching functions \(S(\cdot)\) and \(M(\cdot)\). But the paper never gives a precise operational definition of these functions in the main text, nor does it explain decision thresholds, annotation protocols, or how agreement/noise is handled.  
   Equation (5) is also problematic in presentation:
   \[
   AC=\alpha\cdot FC+(1-\alpha)\cdot SS,
   \]
   with \(\alpha=0.75\), but \(FC\) and \(SS\) are on potentially different scales unless explicitly normalized. Equation (6) defines
   \[
   FC=2\cdot\frac{\text{TP}}{\text{TP}+\text{FP}+\text{FN}},
   \]
   which is not the standard \(F_1\) form unless justified as a specific Dice-like score. If that is intentional, it should be stated clearly. Right now the metric section mixes formal notation with hidden evaluator heuristics.  
   Why this matters: the paper’s headline contribution is not a new model but a benchmark. For a benchmark paper, the evaluation layer is the method. If the metrics are not sharply specified, the benchmark is harder to trust and harder to reproduce.

3. **The use of LLMs in benchmark construction creates a risk of circularity, and the paper does not quantify annotation quality sufficiently in the main paper.**  
   Section 3.2 and Appendix C describe using GPT-4.1 for logic mining, evidence extraction, question generation, and refinement. Appendix C.5 then says this is supported by advanced models combined with human checking. However, the main paper gives almost no concrete statistics on human validation rate, inter-annotator agreement, correction frequency, or how often automatically generated evidence/questions were discarded. Figure 8 and Figure 10 make clear that the pipeline is heavily prompt-driven, which is fine, but it also increases the need for careful quality auditing.  
   Why this matters: if the benchmark questions and evidence chains are generated and refined by a powerful LLM, then some performance patterns may partially reflect alignment with that construction procedure rather than clean measurement of retrieval and reasoning ability. This is especially relevant for the “creative generation” and “contextual summarize” categories, where the target can be shaped strongly by prompt style.

4. **The task taxonomy is intuitive, but the boundaries between categories are still somewhat soft and partly format-driven.**  
   Table 1 presents four levels: Fact Retrieval, Complex Reasoning, Contextual Summarize, and Creative Generation. The idea is sensible, but some examples blur task type and output format. For instance, creative generation is partially defined by style transformation, and summarization is partially defined by answer length/coherence requirements. Appendix A.5 explicitly argues that task format does not matter as much as retrieval and reasoning complexity, but then the benchmark uses format differences heavily in the upper categories.  
   Figure 2 and Figure 9 are persuasive visually, but they mainly show distributional differences across benchmarks, not validation that the proposed categories correspond to distinct cognitive demands in a robust way. Appendix Table 8 helps, yet even there the monotonicity is not perfect, for example contextual summarization has lower reasoning depth than creative generation but higher breadth, so the categories are still composites rather than clean axes.  
   Why this matters: the paper’s core claim is about “when” graphs help. If task categories entangle reasoning depth, output format, and answer length, it becomes harder to attribute gains to structural reasoning rather than to simply needing more retrieved material for longer outputs.

5. **Some empirical interpretations overreach what the tables directly support.**  
   The text around Table 3 and Table 4 occasionally generalizes more strongly than the numbers justify. For example, Section 4.1 says “GraphRAG models show a clear advantage” in complex reasoning, contextual summarize, and creative generation. That is directionally true for some methods and settings, but the picture is heterogeneous. On the novel dataset in Table 3, HippoRAG2 is strong for complex reasoning and creative generation ACC, but LightRAG is quite weak on creative generation, RAPTOR is weak on complex reasoning ACC, and vanilla RAG remains competitive on some metrics. On the medical dataset, RAG with reranking still has very high coverage for contextual summarization, often above multiple GraphRAG systems.  
   Likewise, in Table 4 the retrieval story is nuanced. Some GraphRAG methods achieve high recall but extremely poor relevance, especially MS-GraphRAG. This suggests that “better graph retrieval” may often mean “retrieve much more,” not necessarily “retrieve more useful.” The paper does mention the recall-relevance trade-off, but the conclusion text is more pro-GraphRAG than the tables justify.

6. **The benchmark is still narrow in corpus diversity for a paper making broad practical recommendations.**  
   The benchmark uses two corpora: NCCN guidelines and pre-20th-century novels, as described in Section 3.2. I understand the rationale, one highly structured and one loosely organized, and this is better than only using Wikipedia-style QA. But the paper’s framing is very broad, almost as if it offers general guidance for GraphRAG deployment. Two corpora, both English and both text-only, are not enough to support strong general claims about enterprise RAG, scientific corpora, legal corpora, web-scale noisy data, or multilingual settings.  
   Why this matters: the practical recommendation “when to use graphs” should be interpreted cautiously outside these settings. The medical corpus is ontology-rich and the novel corpus is narrative-heavy; both are informative, neither is comprehensive.

7. **Presentation quality is hurt by many inconsistencies, typos, and naming errors, some of which interfere with careful reading.**  
   There are repeated naming inconsistencies such as “LeghtRAG” in Table 3 instead of LightRAG, mixed years for HippoRAG2, “Durren Edge” in Table 10, “Surfth et al.” for RAPTOR in Table 9, “LapHRAG” and “mucirRAG” in Appendix Table 18, and formatting issues like missing commas or malformed JSON in configuration blocks. The paper also occasionally makes awkward claims such as “This is intuitive, as these tasks require bridging the complex relations among multiple concepts, which is naturally a graph structure” on Page 8.  
   Figure 3 is conceptually useful, but the surrounding prose sometimes feels like a checklist rather than a precise protocol, and some key methodological details are deferred to appendices in ways that make the main paper harder to assess.  
   Why this matters: for a benchmark paper, presentation is not cosmetic. If names, versions, and configurations are inconsistent, readers will reasonably worry about whether the experiments themselves were equally careful.

8. **Graph quality metrics are too primitive to support the paper’s stronger claims about “quality graphs.”**  
   Section 3.3 uses node count, edge count, average degree, and average clustering coefficient. These are easy to compute, but they do not actually evaluate whether the graph represents the right semantics. Figure 5 and Table 5 show that HippoRAG2 builds much denser graphs, and the paper links that to stronger retrieval/generation. But denser graphs are not necessarily better graphs; they may also contain more noisy or redundant edges. The paper itself later says “build quality graphs, not just large ones” in Figure 7, but the benchmark’s graph-quality measurement does not test semantic correctness, edge precision, relation type quality, path usefulness, or graph faithfulness to source text.  
   Why this matters: otherwise the benchmark risks rewarding graph size/connectivity proxies rather than actual structured knowledge quality.

9. **Efficiency analysis is useful but still incomplete as a cost-benefit study.**  
   Tables 6 and 7 report average token cost and the discussion on Page 9 emphasizes prompt inflation. This is helpful, but latency, indexing cost, and retrieval-time compute are only partially covered in the main paper. Appendix Table 15 includes indexing time and token usage, which arguably belongs in the main paper because some GraphRAG methods are impractical unless offline cost is amortized.  
   Also, the comparison is not normalized by answer quality. A stronger efficiency section would show quality-versus-cost frontiers, for example whether a graph method provides enough gain per token to justify deployment under different budgets.  
   Why this matters: the practical question in the title is not only whether graphs help, but when they are worth using.

10. **The benchmark seems more like an evaluation suite for current systems than a carefully controlled scientific instrument, and the paper does not fully embrace that distinction.**  
   I actually think a realistic systems benchmark is a reasonable contribution. The issue is that the paper sometimes speaks in controlled-science language, for example attributing gains to graph structure or graph density, when the setup is closer to a comparative systems study with multiple changing factors. This mismatch between ambition and evidence is a recurring problem throughout the paper.

## Questions
1. Can the authors provide a clearer statement of the causal scope of their claims? In particular, are the conclusions intended to be about graph structure itself, or about current end-to-end GraphRAG systems as implemented by existing frameworks? A more careful distinction would increase my confidence substantially.

2. Please define the evaluator functions in Appendix F much more concretely. For Equations (3), (4), (7), and (8), what exactly are \(R(c,Q,\mathcal{E})\), \(S(c,\mathcal{C})\), and \(M(e,G)\)? Are these human labels, LLM judgments, string/embedding matches, or hybrid procedures? What prompts, thresholds, and validation checks are used?

3. For Equation (6), is
   \[
   FC=2\cdot\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}+\mathrm{FN}}
   \]
   intended to be a Dice-style similarity? If so, please say that explicitly and justify combining it linearly with cosine similarity in Equation (5). I would like to understand whether both terms are calibrated to comparable ranges.

4. Can the authors provide main-paper statistics on dataset quality control, not only appendix prose? For example: how many candidate questions were generated, how many were discarded after check-and-correct, what fraction required human correction, and what was inter-annotator agreement on evidence validity or answer validity?

5. A stronger ablation would be very helpful: take one strong base retrieval setup and compare text-only retrieval vs graph-enhanced retrieval under matched chunking, top-$k$, prompt budget, and generation model. Without that, it is hard to know whether the benchmark findings are really about graphs or about broader system design choices.

6. In Table 3 and Table 4, some GraphRAG systems have very high recall but catastrophically low relevance, especially MS-GraphRAG on the medical dataset. Can the authors analyze whether this comes mainly from community-level retrieval, prompt length explosion, graph construction noise, or evaluator bias?

7. Figure 5 and Table 5 suggest a link between graph density and downstream performance, but Figure 7 later warns against equating larger graphs with better graphs. Can the authors quantify graph semantic quality, for example edge precision against source evidence or usefulness of retrieved paths, rather than relying mostly on topological summaries?

8. Since the title makes a practical recommendation, could the paper summarize a more explicit deployment rule of thumb, perhaps in the form of a decision table based on question complexity, corpus structure, and budget? Figure 7 points in that direction, but it remains qualitative.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses publicly available text corpora and presents a benchmark rather than a deployed decision system. The medical corpus does raise the usual caution that benchmark results should not be interpreted as evidence for clinical safety, but this is not, in my view, an ethics-review-triggering issue based on the paper itself.

## Soundness Rating
3: good. The experimental effort is substantial and the main empirical patterns are plausible, but the benchmark methodology has important underspecification and confounding issues that prevent a higher score.

## Presentation Rating
2: fair. The overall structure is understandable and several figures are helpful, but the paper has too many inconsistencies, typos, naming/version errors, and underspecified metric definitions for a benchmark paper.

## Contribution Rating
3: good. The paper makes a useful contribution by introducing a benchmark and a practical framing for GraphRAG evaluation, even though the evidence does not fully support the strongest claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The benchmark fills a meaningful gap and the empirical study is useful to the community, especially the task-complexity framing and the efficiency analysis. However, the paper overstates how cleanly it identifies the effect of graphs, and the metric definitions and benchmark construction details need to be tightened considerably.

## Reviewer Confidence
4: confident. I am familiar with RAG/GraphRAG evaluation and checked the technical and empirical details with reasonable care, though some appendix-defined procedures remain too underspecified to verify fully.