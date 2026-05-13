# FRAPPE: Fast RAG-Inspired Prompt Evaporator

- Decision: Reject
- Scores: 3, 5, 3, 3, 5

## Abstract
Large Language Models (LLMs) have demonstrated remarkable performance in various tasks such as multi-document QA, summarization, and text classification. This has been achieved in part by recent advancements in prompt engineering and in-context learning (ICL), enabling LLMs to consume tens of thousands of input tokens as the supported context for the given query. However, this creates higher computational costs, longer latency, and potential performance degradation. To address these issues, we propose a task-agnostic and efficient approach called “Fast RAG Inspired Prompt Evaporator”, or FRAPPE, to significantly reduce LLMs’ latency, memory requirement, and computation by compressing input tokens. Unlike many other proposed approaches for prompt compression, our method does not rely on any large model for computing conditional probabilities, and data preparation is fast with negligible memory requirements. In particular, our approach first pre-processes the input data, categorizes and ranks phrases based on their informativeness, and finally selects the highest-ranked phrases to generate highly compressed and extractive input. We show the efficacy of our approach through a comprehensive set of experiments on public datasets and benchmarks. For instance, on the summarization task of the MeetingBank dataset, at a compression rate of 70%, our proposed approach achieves performance similar to the full context while performing compression up to 4 times faster than the contemporary state of the art compression algorithms.  We extend FRAPPE to create the Context-Aware FRAPPE algorithm, which incorporates task-specific information when ranking phrases, which further improves performance of downstream tasks using compressed text.  Additionally, we demonstrate that the use of FRAPPE can reduce toxicity by close to 50% relative to the original text by removing extraneous vitriolic phrases, in contrast to other compression methods, which often increase toxicity.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new approach to improve efficiency in retrieval augmented generation (RAG), by compressing its input context. The proposed method goes through multiple stages of compressing, removing phrases that belongs to pre-determined sets of unnecessary words (3.1, 3.2). Then, in the last step, they form a graph with phrases in the document, and use TextRank algorithm to identify salient phrases. The proposed, unsupervised approach shows up speed gain compared to the baselines. However, I have some issues with their experimental setups and writing.  Please see the weaknesses section.

### Strengths
The proposed method is simple and efficient. 
The proposed approach is evaluated against many tasks and LLMs and show decent gains compared to the baselines.

### Weaknesses
The writing of the paper is not rigorous or clear. 
* For example, in line 218, what is \bar{\tau_r}? Variables should be introduced more carefully. (I know \bar{\tau} is introduced in 147 but the subscript was not introduced). 
* In the introduction, the discussion about toxicity comes out of the blue in the last bullet, very difficult to understand.

Questions / issues about the experimental setups: 
* Why not include other baselines such as ICAE? The current choice of baselines should be justified more carefully (and described).  
* Does this approach work with variable compression rate (seems most results are on 70% compression rate? - which, means you are removing only 30% of the tokens?)
* How is Time measured in the result tables? Why not report the time for uncompressed method?
* How much is getting reduced at each step? It'd be good to report them, to see which of the steps are actually impactful. We need ablation study on step 3.1, 3.2, 3.3. 
* The toxicity section (Section 6) is hard to follow.  Also why selective-Context method not presented here as a baseline here?

### Questions
* It’d be helpful to explain *why* the memory requirement is big for the other methods (394-395).
* What was actual hyper parameter value that is chosen (lambda 1, lambda 2) for each experiment?
* Citation formats need a pass (e.g., line 133, “Pan…” should be \citet. Same in line 256). 
* Line 92 “ATo” -> “To”
* Line 288-90, it’d be good to elaborate a bit on the choice of LLMs, whether they are open-sourced or API driven, etc. 
* Second paragraph of related work would benefit from some cutting. The first half lack citations, thus making claims without supporting them (e.g., how does prompt compression leads to improved performances?) 
* Missing related work:
    * RECOMP https://arxiv.org/abs/2310.04408

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a context compression method, aiming to improve compute and memory efficiency for LLMs. The proposed method -- FRAPPE -- chunks input text into phrases and removes two types of phrases (1) redundant phrases which are pre-defined and (2) non-salient phrases, which are determined by similarity with other phrases, calculated with a sentence embedding models. Experiments are conducted on multiple dataset and models, and compared against previously proposed context compression methods. The authors further proposed an extension to FRAPPE -- which takes similarity with the query into account and demonstrates improved performance.

### Strengths
* The paper proposes a task-agnostic method to perform context compression, which is an active research area to improve inference time efficiency of LLMs.
* The proposed method connects to previously proposed unsupervised summarization methods (e.g. PacSum) which is interesting.

### Weaknesses
The clarity of the paper, as well as experiment set-up could be improved. Please see questions below.

**Experiments / ablation set-up**:
* How much does the two stages of filtering each contribute to the performance / efficiency trade-off? It would be helpful to conduct an ablation study on this. I am mostly wondering if it is possible to remove stage 1, or incorporate the constraint into the centrality calculation which could make the method cleaner.
* What is the uncompressed results for ShareGPT (for Table 1)?
* To contextualize the metrics / results, it might also be helpful to report a baseline which randomly decide whether to keep a phase or not (but retaining the same number of tokens).


**Clarification questions**:
* It is unclear to me how exactly does the context-aware FRAPPE method work. It'd be helpful to flash out the algorithm in equations / pseudo-code.

* I am finding the motivation of the detoxification experiments confusing -- is the idea that after compressing the context, the model is less likely to generate toxic content? It seems like toxicity is evaluated on the compressed context, instead of the generated text conditioned on the compressed context. Please clarify the hypothesis / goal for the detoxification experiments.

### Questions
**Experiments / ablation set-up**:
* How much does the two stages of filtering each contribute to the performance / efficiency trade-off? It would be helpful to conduct an ablation study on this. I am mostly wondering if it is possible to remove stage 1, or incorporate the constraint into the centrality calculation which could make the method cleaner.
* What is the uncompressed results for ShareGPT (for Table 1)?
* To contextualize the metrics / results, it might also be helpful to report a baseline which randomly decide whether to keep a phase or not (but retaining the same number of tokens).


**Clarification questions**:
* It is unclear to me how exactly does the context-aware FRAPPE method work. It'd be helpful to flash out the algorithm in equations / pseudo-code.

* I am finding the motivation of the detoxification experiments confusing -- is the idea that after compressing the context, the model is less likely to generate toxic content? It seems like toxicity is evaluated on the compressed context, instead of the generated text conditioned on the compressed context. Please clarify the hypothesis / goal for the detoxification experiments.

**Suggestions on related work**: There has been previously proposed methods which encode input context in chunks and use embedding models to derive similarity and decide which context to use ([0] and [1]). Although the methods are different from FRAPPE, they are definitely relevant.


[0] https://arxiv.org/abs/2310.04408
[1] https://arxiv.org/pdf/2310.03025

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a prompt compression pipeline to remove redundant and unimportant content, reducing LLM latency and memory consumption. The pipeline includes three components responsible for text chunking, redundancy removal, and text compression. The authors tested this approach on tasks such as summarization, question answering, in-context reasoning, and code completion, demonstrating that the proposed FRAPPE model achieves improved latency performance.

### Strengths
1. The paper compares several of the latest approaches across different downstream NLP tasks, demonstrating latency advantages.
2. The collected expressions, utterances, and other resources from GPT-4 could benefit the research community if published.

### Weaknesses
1. The compression rate was fixed at 0.7 across all model comparisons, with no results reported for other compression rates. This makes it unclear whether the proposed approach consistently outperforms others at varying rates, which diminishes the contribution of this work.

2. The paper lacks a baseline comparison with simple sentence compression methods such as [1]. This LSTM-based approach is lightweight and may also offer speed advantages. 

3. The toxicity study using this proposed method does not enhance the speed or performance of this work. Toxicity reduction relies mainly on the safety training strategy of the LLMs, ensuring that even if the input contains toxic content, the output remains free of it. Thus, I would not regard toxicity reducation as a plus of this work.

### Questions
1. in some cases, I observed that your proposed compression method is even better than uncompression method, such as Arxiv Articles results in Table 1. I thought that compression means somehow some salient information is remove Could you provide an explanation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a multi-stage, task-agnostic prompt compression methods to improve LLMs runtime latency and memory footprint. The proposed approach chunks context into text pieces and removed filler phrases and projects the text phrases into embedding space, ranked the phrases to keep only the most relevant ones using asymmetric centrality measure. The proposed approach could achieve a compression rate of 70%. Comparing with several other baseline methods, the approach achieves comparable or better accuracy performance and much lower latency. The authors also proposed context-aware setting to deal with high compression resulting loss of information related to query.

### Strengths
1. The proposed method is very empirical and is backed up by solid experiment results. The compression rate is high and performance on QA tasks looks very solid. 
2. The authors take consideration of all kinds of issues in real application, e.g. they considered the possibility of high compression might lead to removing relevant info with respect to query, thus proposed context-aware solution.

### Weaknesses
1. Context compression/pruning comes with context info loss. It would be great if the authors could provide robustness analysis of the proposed approach. The concern is about the approach to remove filler words (such as articles) and chunking mentioned in the paper seems quite arbitrary. For instance, for questions like "If each child receives a cookie, how many cookies are needed for 10 children?", answering this kind of simple math question with removed articles might create ambiguous question, thus lead to incorrect answer. The paper lacks a systematic analysis of how these preprocessing steps impact performance across different question types and complexities. Specifically, it would be beneficial to see a breakdown of performance on questions that rely heavily on specific articles or prepositions for correct interpretation, compared to those that are less sensitive to such removals. Furthermore, the chunking strategy, while seemingly straightforward, could introduce issues by breaking up semantically related phrases, and this needs more rigorous evaluation.
2. The idea is very straightforward and intuitive, but it's very empirical as well. For instance, the idea with removing `Phatic Expressions` and `Contrastive (e.g. "but" as given in the paper)` is that it won't provide much help on answering the question. However, for some application like sentiment analysis, it would provide some value. Can we remove these info based on things such as mutual information etc? Or even simpler, it might be better just merge the two phases into one and using the proposed `asymmetric centrality` to remove the irrelevant info. It would be good to provide such experiments. Overall, the first step here gives the impression that we fallback to traditional NLP pipeline rather than leveraging LLMs' capability. The paper does not explore alternative methods for identifying and removing irrelevant information, such as using attention mechanisms or other learned representations, which could potentially be more robust and adaptable than the current rule-based approach. The reliance on a fixed set of filler words and expressions might not generalize well across different domains or languages, and this limitation should be addressed.

### Questions
1. If we remove articles in the context, would that be an issue for tasks such as GSM8K since it might be helpful to answer the questions? One example is `If each child receives a cookie, how many cookies are needed for 10 children?`
2. I assume when we do context pruning, we have to set a hyperparameter as the threshold, it would control the balance between info loss and compression rate. Would that be possible to show such tradeoff in the system? Latency could serve as an proxy, but would compression rate be more intuitive?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes "Fast RAG Inspired Prompt Evaporator", or FRAPPE for short, which compresses the prompt to LLMs. It first processes the data to categorize and rank the phrases based on their informativeness. Only the phrases with the highest ranks will be selected as input for LLMs. FRAPPE achieves similar performance as the full-context baseline while greatly reducing the inference cost.

### Strengths
1. FRAPPE uses a suite of efficient and effective solutions to remove redundant phrases, including four categories: phatic expressions, filler utterances, connectives, and stop words. Each category is addressed with different methods, including the usage of neural-network-based similarity measurement.
2. The phrase ranking of FRAPPE deploys a graph-based ranking algorithm to identify the informative phrases. 
3. FRAPPE can work in both task-agnostic and task-aware modes, giving more flexibility to users.
4. The performance of FRAPPE is superior to its baseline method LlmLingua.

### Weaknesses
1. One issue behind phrase-based compression is that it may break the meaning of a paragraph. The removal of some short phrases may completely change the meaning of a passage.
2. The compression method reduces the context length for LLM inference. However, its practical usage can be limited. On the one hand, the major overhead of LLMs, i.e. the inference cost for proprietary LLMs or the computation of local LLMs, is on generation instead of pre-filling. On the other hand, the compression rate of FRAPPE is low. A compression rate of 70% may not compensate for the performance loss or the extra step of the compression algorithm.
3. The compression rate is low. FRAPPE only removes phrases and is unable to merge phrases or shorten the text, e.g. making a shorter summary, thus its theoretical compression rate is bounded.
4. Measuring the latency of LLM APIs is less effective than directly measuring the runtime of local LLMs. The author should consider running inference with open-source LLMs if computation is allowed.

### Questions
1. Using the rule-based system to identify phrases can be fast but will result in long phrases. Have you ever considered using syntactic parsing to get a finer-grained unit?
2. Fig 4 in the appendix is a good explanation of the whole method but is rendered in low resolution. The authors should consider making it a vector graph.

### Soundness
3

### Presentation
4

### Contribution
3
