# ALR$^2$: A Retrieve-then-Reason Framework for Long-context Question Answering

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
The context window of large language models (LLMs) has been extended significantly in recent years. However, while the context length that the LLM can process has grown, the capability of the model to accurately reason over that context degrades noticeably. 
This occurs because modern LLMs often become overwhelmed by the vast amount of information in the context; when answering questions, the model must identify and reason over relevant evidence sparsely distributed throughout the text.
To alleviate the challenge of long-context reasoning, we develop a retrieve-then-reason framework, enabling LLMs to reason over relevant evidence collected during an intermediate retrieval step.
We find that modern LLMs struggle to accurately retrieve
relevant facts and instead, often hallucinate \textit{``retrieved facts''}, resulting in flawed reasoning and the production of incorrect answers. To address these issues, we introduce \textsc{ALR$^2$}, a method that augments the long-context reasoning capability of LLMs via an explicit two-stage procedure, i.e., aligning LLMs with the objectives of both retrieval and reasoning.
We demonstrate the efficacy of \textsc{ALR$^2$} for mitigating performance degradation in long-context reasoning tasks. Through extensive experiments on long-context QA benchmarks, we find our method to outperform competitive baselines by large margins, achieving at least 8.4 and 7.9 EM gains on the long-context versions of HotpotQA and SQuAD datasets, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focus on addressing the challenge of LLMs' degrading performance when reasoning over long contexts. This paper proposes a two-stage retrieve-then-reason approach: first retrieving relevant information from the long context, then reasoning over the retrieved information to produce answers. The model is explicitly trained to align with both retrieval and reasoning objectives, leading to improvements over baselines.

### Strengths
1. The research shows that breaking down long-context reasoning into explicit retrieval and reasoning steps can enhance LLM performance on long document understanding tasks and also provide more transparent reasoning processes. These combined strengths position the paper with higher value.

2. The model can help with hallucination mitigation, where the system dramatically reduces the tendency to generate fictional content by explicitly aligning the LLM with retrieval objectives.

3. The paper is easy to follow and is well-written.

### Weaknesses
1. I believe an important baseline is missing: How is your retrieve-then-reason framework compared to retrieval-augmented generation for LLM baseline methods including DPR (Dense Passage Retrieval), FLARE (Active Retrieval Augmented Generation), RETA-LLM (RETA-LLM: A Retrieval-Augmented Large Language Model Toolkit). Throughout these methods, retrieval can even be performed with a smaller, faster model on a larger context like a database and are applicable to the long-context understanding scenario. 

2. The contribution is limited. As the author indicated in sec 4.2, the retrieve-then-reason framework is very similar to "generate quotes and citations first" framework. Therefore, the innovation of this work seems just to fine-tune the models based on these data.

3. There is lack of a clear explanation for some unexpected parts of the experimental results. For example, the model's performance on squad for some lengths (8k, 16k) in Table 1 is significantly lower than shorter and longer lengths, and I have not seen a clear interpretation for this unusual behavior.

### Questions
1. As mentioned in the first weakness, can you evaluate both efficiency and effectiveness comparison between these methods, and show how in-context retrieve-then-reason can bring extra benefits compared to RAG?

2. The term "Retrieval" in this paper is different from previous work like DPR, where the models do not retrieve in-context but retrieve on an external codebase. Considering this may cause misunderstanding for unfamiliar readers, I suggest considering changing names like "in-context retrieval"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a retrieve-then-reason method to address the issue that LLMs (Large Language Models) struggle to handle long contexts properly, especially in reasoning. This proposed approach improves the handling of long contexts by explicitly retrieving supporting facts from the given long context as well as by aligning LLMs with retrieval and reasoning objectives at the same time.

### Strengths
- The paper is generally well-written, easy to understand, and clearly presented.
- The preliminary study provides interesting insights into where issues arise when LLMs handle long contexts, showing that while retrieval itself is not problematic, the issues occur during reasoning.

### Weaknesses
In my opinion, there seem to be some areas for improvement in the design of the experiments aimed at proving the claims of this paper. If these below points can be clarified through additional responses from the authors, I would be glad to adjust my evaluation accordingly.

1. Details about the experiments are missing. For example, there is insufficient information regarding the hyperparameters used during model training (e.g., learning rate, seed) and the specific training data. It is unclear whether ALR was trained separately on each dataset (e.g., SQuAD, HotpotQA) or trained using both datasets together (according to line 407). If it was the former, which model was used in the experiment described in section 5.2?

2. The experiment setting appears to be incomplete. It seems feasible to apply the RR method (e.g., using multi-turn conversation) to the frontier models utilized in the study (GPT-3.5, GPT-4, GEMINI, CLAUDE-3). Additionally, the benefits of aligning with both objectives are not clearly demonstrated. Why should the LLM be aligned to both objectives? It seems plausible to fine-tune the LLM separately for each objective and then combine the results (e.g., passing the output of the retrieval LLM to the reasoning LLM). An ablation study addressing this approach should be provided.

3. There may not have been a fair comparison with the baselines. It appears that there is a difference in the answer template between the DA prompt (figure 4) and the RR prompt (figure 3), as the "Answer:" is missing in figure 3. Given that LLMs can be sensitive to prompts, this could lead to performance differences. To provide evidence that the comparisons in the experiment were fair, results using the same answer template should be included. Additionally, based on figure 3 and equation (2), it seems that the given long context was used alongside the retrieved facts. A comparison showing the performance when the given long context (i.e., prior chat history) is removed would be necessary for a fair comparison with S2A, which also omits prior records.


### Questions
- Lines 357-359 point out that QF only retrieves 2.2 sentences on average (compared to 7.5 for RR). However, in HotpotQA, it is common for only a small number of supporting facts (1-2) to be necessary [1] (even if 2-6 supporting facts are provided). To assess whether the retrieval was truly effective, could the performance of CMD-R QF also be included in the experiment results of Section 5.1? It is particularly important to include not only the recall score but also precision. Relying solely on the recall score could bias the evaluation toward retrieval methods that select a larger number of facts.

[1] [MuSiQue: Multihop Questions via Single-hop Question Composition] (Trivedi et al., TACL 2022)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents $ALR^2$, a retrieve-and-reason framework for QA over long contexts. $ALR^2$ is trained to first retrieve relevant information from a long context, and then reason over it to arrive at an answer. With Command-R, $ALR^2$ significantly outperforms prompted variants and a model directly trained to generate an answer on HotpotQA and SQuAD (in a variant where gold facts are augmented to create a long context), and generalizes to unseen StrategyQA and TriviaQA datasets.

### Strengths
- The paper deals with an important subject, long-range QA.
- The improvements over a variant trained to directly generate the answer are significant, and improvements generalize to unseen datasets.
- The paper is well-written and easy to follow.

### Weaknesses
 - While the generalization study presented in Section 5.2 is important, it only experiments with datasets that were “modified” to have a long-context, in a method that is similar to those of the training data. I believe the paper could benefit from experimenting with QA datasets that have a long context by design, such as those in the SCROLLS benchmark [1]. Additionally, the paper focuses on reasoning, but experiments with a single multi-hop QA benchmark in each setting (in-domain and out-of-domain).

- The results in Tab.1 only compare against all baselines for the trained Command-R models, and models prompted to directly generate the answer for other models. I believe the paper could benefit from experimenting with another trained LLM with all variants, or at least adding results with the ‘retrieve-then-reason’ prompt with current strong LLMs (e.g., Llama-405B, GPT4-o, Claude-Sonnet-3.5).

- Perhaps I am missing something, but as far as I am aware the idea that a LLM is trained to first retrieve information from a long context and then reason over it has been presented previously, for example by training LLMs as re-rankers (e.g., [2]). While there are differences between these two approaches (in $ALR^2$ the LLM generates relevant sentences instead of ranking), it seems there are also similarities (the LLM first identifies relevant information from a long context). Hence, the paper might benefit from additional experiments or analysis that highlight what leads to the improvements of $ALR^2$ (see questions).

- While the paper is overall well-written, there are a few parts that I think could be further improved. Mainly, the preliminary study provides motivation for the work, but lacks a qualitative analysis, so it was not clear to me why models struggle on Task 3. Additionally, I felt like the discussion in Section 3.5 was a bit misleading, as dense retrievers are often much more efficient than the presented approach.

### Questions
Regarding weakness 1 - do you think there are QA datasets that have long-context by design and might be relevant for evaluation?

Regarding weakness 3 - do you think there are other experiments/ablations that are similar to current methods that can be added? For example, the model can be trained to first re-rank the long context (variants that generate relevant indexes for passages like in RankZephyr or relevant snippets as in the paper can be explored). Additionally, an ablation where the final answer is generated by a short-context QA model can help understand if the full context is necessary for reasoning after the retrieval step, or if only the information in the retrieval step is sufficient to answer the questions.

Additionally, perhaps I missed something, but will the model and data be publicly available? 

Also, I believe the paper could benefit from a discussion regarding reproducibility and an ethics statement.

### Soundness
2

### Presentation
3

### Contribution
2
