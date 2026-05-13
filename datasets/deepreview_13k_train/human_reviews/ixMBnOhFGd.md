# SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Large Language Models (LLMs) have demonstrated improved generation performance by incorporating externally retrieved knowledge, a process known as retrieval-augmented generation (RAG). Despite the potential of this approach, existing studies evaluate RAG effectiveness by 1) assessing retrieval and generation components jointly, which obscures retrieval's distinct contribution, or 2) examining retrievers using traditional metrics such as NDCG, which creates a gap in understanding retrieval's true utility in the overall generation process.  To address the above limitations, in this work, we introduce an automatic evaluation method that measures retrieval quality through the lens of information gain within the RAG framework. Specifically, we propose *Semantic Perplexity (SePer)*, a metric that captures the LLM's internal belief about the correctness of the retrieved information. We quantify the utility of retrieval by the extent to which it reduces semantic perplexity post-retrieval. Extensive experiments demonstrate that SePer not only aligns closely with human preferences but also offers a more precise and efficient evaluation of retrieval utility across diverse RAG scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a measure of semantic perplexity reduction (SePer) to evaluate the utility of retrieved documents in RAG. The measure reflects the change in the probability of the ground truth answer when given the retrieved document. The authors evaluate the correlation of this measure with respect to machine and human judgments, showing higher correlation than other measures.SePer is then used to evaluate the effect of different factors: model size, number of retrieved document, prompt compression and document reranking.
The experiments suggest that SePer can be used to estimate whether a retrieved document is useful.

### Strengths
1. The paper uses a well motivated idea to measure the utility of a retrieved document. Similar idea has been used in IR literature quite a long time ago, but it is rarely used in recent studies. Reusing this idea with the current approaches to RAG is interesting.
2. The demonstration that SePer could be a reasonable measure for document utility is interesting (however, some unclarities - see weaknesses).

### Weaknesses
1. While the general idea is well motivated, its demonstration and tests have could be described more clearly. Some unclear presentation hampers the understanding. For example, the tables and figures are usually not well explained. E.g. In Table 1, it is unclear what the numbers correspond to. SePer reduction is a central concept of the paper. However, there is not a clear definition of it. One may guess that it corresponds to Equation 9 (?), but a clear explanation would help.
2. Some important details are not well described in the paper. For example, reranker is a means to improve RAG. However, it is unclear how reranking is done. The single sentence that explains it is unclear. The method used for prompt compression may also be more detailed.
3. The evaluation is limited to testing if SePer correlates to human judgments and how different factors influence SePer measure. It would be interesting to design a method to use SePer in RAG, e.g. to select retrieved documents according to SePer. This would be a more direct evaluation of the utility of SePer.
4. The paper bears some similarity to Farquhar et al. (2024). This has not been explicitly stated in the paper.

### Questions
1. How could SePer be used concretely in RAG?
2. SePer is compared to retrieval annotations to estimate its correlation to the latter. Would it be possible to test if SePer correlates well with the final answer generation, i.e. when a document with higher SePer is provided to the generation process, the generated answer tends to be better?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a method for estimating the value of a document in a RAG setting according to its ability to reduce semantic perplexity in the downstream model. The method is compared to ground truth utility and human preferences using measured correlation.  The method is further studied in the context as an evaluation metric.

### Strengths
* **Interesting new work in relevance estimation.** Determining the relevance of an item for RAG is an exciting new area of research that moves beyond classical notions of relevance from information retrieval.

### Weaknesses
 * **Metric validation.** When proposing a new metric, various criteria must be met. These include validity (e.g., construct, content, convergent, discriminate), reliability, and sensitivity.  Although Section 4.1 provides some evidence of validity, we need more analysis to understand if this would be a strong metric (e.g., reliability, sensitivity).  The remaining experiments in Section 5 are difficult to connect and are relatively informal.  The authors are strongly encouraged to review the literature in metric design, some of which are listed below,
   * Abigail Z. Jacobs and Hanna Wallach. Measurement and fairness. In Proceedings of the 2021 acm conference on fairness, accountability, and transparency, FAccT '21, 375--385, New York, NY, USA, 2021. , Association for Computing Machinery.
   * Claudia Wagner, Markus Strohmaier, Alexandra Olteanu, Emre Kıcıman, Noshir Contractor, and Tina Eliassi-Rad. Measuring algorithmically infused societies. Nature, 595(7866):197--204, 2021.
   * Ziang Xiao, Susu Zhang, Vivian Lai, and Q. Vera Liao. Evaluating evaluation metrics: a framework for analyzing NLG evaluation metrics using measurement theory. In Houda Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the 2023 conference on empirical methods in natural language processing, 10967--10982, Singapore, December 2023. , Association for Computational Linguistics.
* **Related work in information retrieval.** The authors seem to dismiss much of the information retrieval work that looks at the cognitive process of searching and its connection to relevance.  Since they do cite earlier work (e..g, [Cooper 1973]), I believe this should be considered.  Please look into work from Belkin and related,
   * Nicholas Belkin. Anomalous states of knowledge as a basis for information retrieval. Canadian Journal of Information Science, page 133-143, 11 1980.
   * N. J. Belkin, R. N. Oddy, and H. M. Brooks. Ask for information retrieval: part i. background and theory. Journal of Documentation, 38(2):61-71, June 1982.
   * N. J. Belkin, R. N. Oddy, and H. M. Brooks. Ask for information retrieval: part ii. results of a design study.. Journal of Documentation, 38(3):145-64, September 1982.
* **Writing.** This is minor but the authors should consider improving the flow and exposition in the writing.  There seems to be little justification for the Properties in Section 3.2, which could benefit from discussion or citation.  The RQs in Section 5 are introduced also without much discussion of why they are important.

### Questions
The authors have addressed the above weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new measure, SePer, to measure the retrieval utility through the lens of semantic perplexity reduction.  The authors point out the current problems at evaluating RAG effectiveness: assessing retrieval and generation components jointly, which obscures retrievals distinct contribution, or examining retrievers using traditional metrics such as NDCG. To address these limitations, the authors introduce an automatic evaluation method that measures retrieval quality through the lens of information gain within the RAG framework, by proposing Semantic Perplexity (SePer) that captures the LLM’s internal belief about the correctness of the retrieved information. The measure quantifies the utility of retrieval by the extent to which it reduces semantic perplexity post-retrieval. Extensive experiments demonstrate that SePer not only aligns closely with human preferences but also offers a more precise and efficient evaluation of retrieval utility across diverse RAG scenarios.

### Strengths
1.	Overall, the motivation of the paper is justified, and the paper is clearly written.  

2.	The idea of introducing a new measure, SePer, to evaluate the effectiveness of retrieval in RAG is justified and it seems to be necessary and innovative.

3.	Evaluation of retrieval utility based on shifts in LLMs’ knowledge distributions sounds reasonable.

4.	The experiments show that the new measure not only aligns closer with human annotations but also is more consistent with inference-time situations.

5.	Both theoretical analysis and extensive experiments demonstrate that SePer provides a more accurate, fine-grained, and efficient evaluation of retrieval utility. It is also generalizable across a broad range of RAG scenarios.

### Weaknesses
1.	The design is mainly based on the entailment model and semantic clustering.  Moreover, the semantic clustering is also based on the entailment threshold, as show in its algorithm: Grouping responses rj into clusters C = {Ck} such that E(ri, rj) ≥ τ within each cluster.  Thus, the entailment model becomes the most critical factor in this measurement.  I am not sure if further discussion is needed with different entailment inference methods and different thresholds and see how they may impact the effectiveness of the SePer measure.  I feel some discussion is needed. Specifically, the paper should explore how different entailment models (e.g., using different pre-trained models or fine-tuning strategies) affect the resulting SePer scores. Furthermore, the sensitivity of the clustering algorithm to the entailment threshold τ needs to be investigated. It's unclear how the choice of τ impacts the granularity of the semantic clusters and, consequently, the final SePer score. A more robust analysis should be conducted to determine the optimal range for τ and how it should be chosen for different datasets or tasks.

2.	The design does not conduct any concrete semantic analysis on different kinds of queries and texts to be retrieved.   It seems such study and discussion could be useful to deepen the understanding although this study (simply) tested on multiple datasets as shown in Table 2. The paper lacks a detailed analysis of how SePer performs across various query types (e.g., factual, comparative, definitional) and document types (e.g., short snippets, long articles, structured data). A more granular analysis is needed to understand the strengths and weaknesses of SePer in different retrieval scenarios. For example, does SePer perform equally well when retrieving information for complex reasoning queries compared to simple fact-based questions? Does the length and complexity of the retrieved documents affect the SePer score? These questions need to be addressed with concrete examples and analysis.

3.	There are quite a few typos in the paper.  For example, “a efficient” should be “an efficient” on lines 349 and 404;line 351: “It’s high correlation score in matching responses and answers also set a solid step …” should be  “Its high correlation scores in matching responses and answers also set a solid step …”; line 399 “results are shown in 3” should be “results are shown in Figure 3”, and others.

### Questions
The points outlined in the “weakness” should be clarified in the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes SePer, an automatic evaluation metric to measure the benefit of retrieval. SePer first samples multiple responses of the input query, clusters them based on the semantic meanings, and estimates the belief distribution conditioned on the current input. It computes the CE between this belief distribution and ground truth as the final information gain. Experimental results demonstrate that SePer can evaluate retrieval utility and align with human preference.

### Strengths
- The method is well-formulated and written.

- SePer has a high correlation with human annotations, which is valuable for content evaluation.

### Weaknesses
 - The assumption that retrieval utility is uniformly distributed across different reasoning steps may not hold true universally, potentially oversimplifying complex retrieval interactions.

- The need for extensive Monte Carlo sampling and clustering in semantic space may not be feasible for all applications, particularly those with limited resources.

- My major concern is about the experiment section. The selected metrics are evaluating semantic similarity instead of information gain or retrieval utility. Comparing SePer with the baselines does not necessarily mean that it is more competitive in measuring knowledge gain. Answers with high certainty but poor information (e.g., "I don't know") can still achieve high metric scores. The experimental results demonstrate that SePer is more about answer quality than information gain.

### Questions
- How much does it cost to run SePer during evaluation? The introduction claims that SePer is efficient but there isn't any cost analysis.

### Soundness
3

### Presentation
3

### Contribution
3
