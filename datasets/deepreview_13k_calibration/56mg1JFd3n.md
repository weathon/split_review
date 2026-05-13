# Writing in the Margins: Better Inference Patterns for Long-Context Retrieval

- Decision: Reject
- Avg Score: 6.00
- Scores: 10, 3, 5, 6

## Abstract
In this paper, we introduce Writing in the Margins (WiM), a new inference pattern for Large Language Models designed to optimize the handling of long input sequences in retrieval-oriented tasks. This approach leverages the chunked prefill of the key-value cache to perform segment-wise inference, which enables efficient processing of extensive contexts along with the generation and classification of intermediate information (``margins'') that guide the model towards specific tasks. This method increases computational overhead marginally while significantly enhancing the performance of off-the-shelf models without the need for fine-tuning. Specifically, we observe that WiM provides an average enhancement of $7.5\%$ in accuracy for reasoning skills (HotpotQA, MultiHop-RAG) and more than a $30.0\%$ increase in the F1-score for aggregation tasks (CWE). Additionally, we show how the proposed pattern fits into an interactive retrieval design that provides end-users with ongoing updates about the progress of context processing, and pinpoints the integration of relevant information into the final response.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper introduces a new inference methodology called "writing in margins" for long context tasks. The method builds upon the chunked prefill strategy (commonly used while dealing with long contexts to avoid the quadratic growth of memory), dividing long input contexts into manageable segments and generates "margins" or intermediate summaries for each chunk. 
The margins are then classified by the same LLM as useful or not-useful and useful margins are kept as part of the context and used during decoding step. 
The approach seems to significantly help LLM (especially smaller LLMs) in better accuracy during decoding.

### Strengths
The paper provides a number of thought provoking outcomes.
1) It showcases how adding a simple strategy of adding notes or summaries in the "margins" after each prefilled chunk can assist in improving LLM reasoning and retrieval capabilities. 
2) The notes written by the LLM can potentially be used to improve explainability of the final decoded output. This is dependent on whether the question asked for the margin generation is useful. In the paper the authors ask the LLM whether the context is relevant to the query (and to provide a summary).
3) The approach is general purpose, it can be applied to any LLM without the need for finetuning which is a big win. 

Overall, strong contribution.

### Weaknesses
1) Latency - while the authors mention that latency is slightly increased, an ablation study for this would be welcome. Since the paper uses 2 steps for each chunk - margin generation and then margin classification, you are effectively doing 2 decoding steps for the model with each chunk. This will add latency, especially if the summaries generated are long.

2) comparison against finetuned models - the paper mentions that this technique the models to perform well on tasks (long context) without the need to finetune the model (similar to rag). It would be good to include a model finetuned for the task and using the standard Long Context LLM decoding approach.

### Questions
1) One approach the authors could explore would be to use a separate smaller LLM as classifier. Using the base model (which can be very large) adds latency.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors present a method for improving the representation of chunked text in a prompt by computing query-specific representations (margin notes) for each chunk. They hypothesize that this expanded and query-specific text allows for more efficient and effective decoding. To test this, the authors apply their method to several baseline models across three tasks: multi-hop reasoning, single-hop retrieval, and aggregation.  Post-hoc analysis involves an ablation study.

### Strengths
* **Interesting approach to query-specific representation expansion.**  Bootstrapping decision-making with model information (e.g., writing the margins) is a compelling way for a model to guide itself toward a better response. 
* **Focus on effectiveness and efficiency.** The authors discuss both the effectiveness of their method and how it can improve the efficiency during decoding.  
* **Extensive experimentation.** Notwithstanding concerns (below), testing the approach on multiple settings and across multiple models is a rigorous way to test a model.  The authors could have improved the discussion on how performance varies and what that implies about the proposed method.

### Weaknesses
 * **No formal statement of hypotheses.** This is perhaps implicit, but given the number of experiments, it is essential to be explicit about the precise hypotheses the experiments test.  As best I can tell, one hypothesis is that treatment with margin notes will be better than treatment with other methods (LLM and RAG baselines) across a fixed condition (e.g., length variant, task).  There are some allusions to other hypotheses (e.g., comparisons across columns), but that's less clear.  This is important because of the next point.
* **No formal hypothesis tests.** There are a lot of numbers in Table 4+.  Results in bold seem to be the max within some context.  However, it's not clear if any of these differences are (a) statistically significant and/or (b) if those tests have accounted for multiple comparisons (since these datasets are being reused...a lot).  Without this, it's difficult to understand the robustness of these results.  In order to address this, you can consult the literature on significance testing (Cohen's "Empirical Methods for Artificial Intelligence" is good; tutorials from the RecSys/information retrieval communities are also good) and correcting for multiple comparisons (see those tutorials from the RecSys/information retrieval communities).
* **Writing falls off at the end.** Starting with the ablation experiments (Section 5), the flow and writing of the paper weaken.  Why do these ablation experiments make sense?  What are the implications?  What is the argument of Section 6?  How are all of these things connected to the core hypothesis of the paper?

### Questions
* The main results in Table 4 present many metric values repeatedly measured using a fixed dataset and multiple algorithms.  No statistical significance tests are shown.  This severely compromises the integrity of the results. Were these tests conducted—with appropriate corrections for multiple comparisons—but not reported?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose and investigate the usage of intermediate information (margins) for improving long-context retrieval. They compare different small and medium-size LLMs as well as a RAG like system and find improvements over these baselines in many cases.

### Strengths
- interesting and original idea
- comparison with several base lines
- improvements over these baselines

### Weaknesses
 - comparison and discussion not complete, as larger models (which show less improvements) and more sophisticated RAG systems are not included


### Questions
1. Larger models seem to profit less from WiM (table 4), and you do not include models larger than 70B. Would models larger than 70B still see improvements with WiM? Can you discuss this in more detail?
2. RAG is best with SQuAD in many cases, and almost always better than WiM. You argue that with multihop Q&A this is no longer the case (as shown in table 4), but isn't this only true for your RAG implementation / approximation, and more sophisticated RAG systems would improve this score?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a new inference pattern called "Writing in the Margins" (WiM) that addresses the challenges of processing long input contexts in retrieval-oriented tasks. WiM leverages the chunked prefill mechanism in large language models to generate intermediate "margin notes" that summarize relevant information for the given query. These margin notes are then incorporated into the final response, leading to significant performance boosts on benchmarks like HotpotQA and Common Words Extraction compared to vanilla long-context models and retrieval-augmented approaches. The paper also discusses how WiM can enhance the transparency and interactivity of the retrieval process by providing users with real-time insights into the model's reasoning.

### Strengths
* The authors introduce a novel inference pattern called "Writing in the Margins" (WiM) that leverages the chunked prefill mechanism in large language models to generate intermediate "margin notes" that can guide the final prediction. This is a clever way to address the challenges of long-context processing in retrieval-oriented tasks.

* The results show that WiM can significantly boost the performance of off-the-shelf models across a range of long-context benchmarks, including multi-hop reasoning and aggregation. This demonstrates the effectiveness of the proposed approach.

### Weaknesses
 * The experimental setup could be expanded to include more baselines, such as state-of-the-art models specifically designed for long-context processing to better assess the relative performance of WiM.

* While the results are strong, the paper could benefit from a deeper analysis of why WiM works well for some tasks (e.g., multi-hop, aggregation) but not as consistently for others (e.g., single-hop QA). Understanding the underlying mechanisms behind these performance differences would strengthen the contributions.

### Questions
Please refer to the "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3
