# REPOFILTER: Adaptive Retrieval Context Trimming for Repository-Level Code Completion

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5

## Abstract
Retrieval-Augmented Generation (RAG) has recently emerged as a promising approach for repository-level code completion by integrating cross-file knowledge with in-file preceding code to provide comprehensive contexts for generation. To better understand the contribution of the retrieved cross-file contexts, we introduce a likelihood-based metric to evaluate the impact of each retrieved code chunk on the completion. Our analysis reveals that, despite retrieving numerous chunks, only a small subset positively contributes to the target completion, while some chunks even degrade performance. To address this issue, we leverage this metric to construct a repository-level dataset where each retrieved chunk is labeled as positive, neutral, or negative based on its relevance to the target completion. We then propose an adaptive retrieval context trimming framework, REPOFILTER, trained on this dataset to mitigate the harmful effects of negative retrieved contexts in RAG-based code completion. Extensive evaluation on the RepoEval and CrossCodeLongEval benchmarks demonstrates that REPOFILTER consistently improves completion accuracy compared to approaches without filtering operations across various tasks. Additionally, REPOFILTER significantly reduces the length of the input prompt, enhancing computational efficiency while exhibiting strong generalizability across different models. These results underscore the potential of REPOFILTER to enhance the accuracy, efficiency, and attributability of RAG-based repository-level code completion.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a new likelihood based metric to evaluate the effect of retrieved cross-file chunks on code completion tasks. Using this, it was found that the majority of retrieved chunks negatively or neutrally affect code completion performance. So, the authors finetune LLMs to pre-emptively determine the utility of retrieved code chunks on code completion tasks and demonstrate that this can dramatically improve code completion performance while significantly reducing the sequence length of supplemental contexts introduced after cross-file retrieval.

### Strengths
**Useful novel contributions.** The paper introduces a new method to filter retrieved cross-file chunks. Further, the authors demonstrate how their filtering strategy can be used as a plug-in approach for larger models, demonstrating generalization of utility. This approach also leads to remarkable improvements on cross-file tasks and will be of great value to researchers who are focusing on improving Code LLM performance on repository-level code completion.

**Well-written paper.** The paper is well-written and offers great insights - from motivating the need for a cross-file chunk filter to ablations around various design choices - making it a great contribution to the community.

### Weaknesses
 **Missing details.** There are a number of missing details from the paper (or maybe I missed them) that need further clarification:

- Line 183: How were these thresholds set? How important are these and what is the effect of changing these thresholds? Specifically, what is the sensitivity of the final performance to the precise values of these thresholds? It would be useful to see an ablation study that explores a range of threshold values and their impact on the performance of the RepoFilter.
- From line 239, it appears that the model is never shown the `<neg>` token. Is this case? If so, how does the model generate the `<neg>` token? This is a critical detail that needs to be clarified, as it is not immediately obvious how the model learns to produce a token it has not seen during training. The mechanism for generating this token needs to be explicitly stated.
- It appears that there is a discrepancy between the descriptions of polarity token generation in Algorithm 1 and lines 343-349. If the polarity token is the one with maximum probability, what is the role of thresholding? The manuscript needs to be consistent in its description of the polarity token generation process. The role of the threshold needs to be clearly defined in relation to the maximum probability token.

**Data leakage concerns.** The authors have used the Stack dataset to finetune StarCoder models and evaluate on CrossCodeEval. These are both sourced from GitHub repositories and potentially have overlaps. I recommend taking special care for deduplication of training data against evaluation datasets to address leakage concerns. This is a critical point that needs to be addressed to ensure the validity of the results. The authors should provide a clear explanation of how they have addressed this issue, including specific steps taken to deduplicate the datasets.

**Problem scope clarifications.** It would be useful to clarify the scope of problem being solved or contextualize it among other problems. For example, what is the difference between training RepoFilter and a new retriever or reranker with the same labels? This is unclear and left me confused about the advantage of training a filter over training a new retriever on the same data. The authors need to clearly articulate the unique contributions of their approach compared to existing methods.

**Additional experiments.** This is not a major concern. I would be interested in seeing more experiments that evaluate the RepoFilter system in isolation and not through the downstream task evaluation. Specifically, what are the precision/recall metrics of the RepoFilter for scoring the `<pos>, <neu>, <neg>` tokens? This would provide a more granular understanding of the performance of the RepoFilter and its ability to correctly classify code chunks.

### Questions
See notes above. I have framed some of the concerns raised in a question format here.

1. Were some steps taken to ensure that there is no leakage between the RepoFilter training and the benchmark datasets?
2. How does RepoFilter differ or do better than training a new retriever with the RepoFilter training data?
3. What are the precision/recall metrics of the RepoFilter for scoring the `<pos>, <neu>, <neg>` tokens?
4. Can you clearly outline the training and inference algorithms for the polarity tokens? In the current manuscript, it appears a bit confused.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces REPOFILTER, a framework designed to improve repository-level code completion by filtering irrelevant or negative cross-file contexts in retrieval-augmented generation (RAG) setups. REPOFILTER evaluates the impact of retrieved code chunks using a likelihood-based metric, classifying chunks as positive, neutral, or negative. Extensive experiments on the RepoEval and CrossCodeLongEval benchmarks demonstrate that REPOFILTER enhances completion accuracy while reducing the length of input prompts, improving efficiency without compromising performance.

However, in my opinion, this paper has no essential innovation compared to Self-RAG. It just adjusts the quantitative standard of classification indicators and replaces model evaluation by training a probabilistic parameter classifier. However, due to the lack of baseline comparison, I cannot believe that the method in this paper has achieved SOTA. Moreover, in essence, the training method in this paper increases the training cost and introduces generalization considerations. At the same time, it may not be significantly improved compared to the existing SOTA RAG framework in terms of interpretability and effect. Therefore, the contribution of this paper is missing, and it is more like an engineering skills report in the SE field.

### Strengths
1. **Clear Motivation**: The paper identifies a critical limitation in RAG-based repository-level code completion: the inclusion of extraneous or detrimental code chunks in the retrieval process. The authors present an argument for REPOFILTER’s filtering mechanism.

2. **Likelihood-Based Polarity Metric**: The proposed likelihood-based metric is innovative and provides a quantitative approach to evaluate the relevance of each retrieved chunk. This metric adds rigor to the filtering process, ensuring that retained chunks positively influence completion accuracy, which is a practical and scalable solution.

3. **Experimental Results and Efficiency Gains**: REPOFILTER consistently outperforms full retrieval and even adaptive retrieval strategies such as RepoFormer, achieving improvements in completion accuracy on the RepoEval and CrossCodeLongEval benchmarks.

### Weaknesses
1. **Limited Evaluation on Diverse Repositories**: While the experimental results on Python repositories are robust, the paper could further strengthen its generalizability claims by evaluating REPOFILTER on repositories in other languages. This would demonstrate the approach’s adaptability to different programming contexts and enhance its appeal to a broader range of applications.

2. **Detailed Explanation of the Adaptive Mechanism**: Although the framework’s adaptive nature is a strong feature, some aspects of its implementation, particularly the proof of hypothesis, could benefit from additional clarification. A more detailed explanation of the decision-making process for context sufficiency and information would help in understanding the effectiveness and robustness of the adaptive retrieval mechanism.

3. **Dependency on Accurate Likelihood Estimation**: The effectiveness of REPOFILTER’s polarity classification relies heavily on accurate likelihood estimations. Situations where this estimation might fail, such as repositories with highly unconventional or complex code patterns, are not discussed. This could potentially limit the framework’s performance in non-standard or heterogeneous coding environments.

### Questions
1. **Provide Qualitative Examples**: Adding examples of how positive, neutral, and negative chunks impact the completion process would provide readers with a more intuitive understanding of the framework. A case study or visualizations comparing outputs with and without REPOFILTER’s filtering would be beneficial. Also which qualitative code characteristics the code classification via this uninterpretability approach tends to favor should be discussed.

2. **Extended Analysis of Filtering Mechanism**: While REPOFILTER achieves efficiency by trimming context lengths, further analysis on cases where the model incorrectly labels chunks (e.g., a neutral chunk classified as negative) would add depth to the evaluation. This could be presented as an ablation study or error analysis.

3. **Broader Contextual Relevance Discussion**: The paper briefly discusses filtering strategies in the context of other RAG tasks. Expanding this section to consider REPOFILTER’s potential impact on domains like documentation generation or bug fixing. Besides, the baselines of related works and RAG methods for comparison are too inadequate.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new RAG fine-tuning method called RepoFilter, designed to enhance retrieval quality for code completion tasks. The core idea is to train the model to predict two specialized tokens: a polarity token after each retrieved chunk, indicating the chunk's helpfulness for completion, and an adaptive retrieval token to signal whether further retrieval is necessary. At training time, the authors use the likelihood gain on ground-truth tokens to label retrieved chunks with polarity tokens, creating full training examples in a single pass. During inference, the LM filters out any chunks classified as neutral or negative. A key finding is that most retrieved chunks are either neutral or detrimental to code completion, underscoring the need for effective filtering strategies. The evaluation demonstrates that RepoFilter achieves up to a 3% improvement in exact match over standard RAG models and significantly reduces prompt length, improving computational efficiency without sacrificing accuracy.

### Strengths
**Motivated and Simple Technique**: The approach is well-motivated, leveraging easy-to-implement mechanisms for filtering retrieval contexts.

**Performance and Efficiency Gains**: RepoFilter delivers substantial performance, with a 3% exact match increase over baseline RAG models and prompt length reductions of over 80% in some cases. This filtering approach enhances computational efficiency while maintaining accuracy.

**Low Computational Overhead**: The technique requires minimal additional computation from the LM (just two extra decoded tokens per chunk) while keeping the retrieval context concise and relevant.

**Generalizability**: RepoFilter performs well across various benchmarks and RAG strategies, demonstrating compatibility with larger models like GPT-3.5 when applied as a plug-and-play retrieval context selector.

### Weaknesses
* It’s unclear if the baselines in this work were RAG fine-tuned. If the baseline models were not fine-tuned with RAG using a standard loss $L = -\log P_G (Y | C_{in}, C_{out})$ defined on middle tokens, the comparison may be unfair. Such a loss typically encourages the model to ignore irrelevant chunks, so it's plausible that there would be no additional benefit to explicitly teaching the LM model to label each chunk. Furthermore, the lack of improvement when fine-tuning StarCoder on all retrieved chunks is surprising, given that it was not originally RAG fine-tuned. This suggests that the fine-tuning process itself might have limitations, or that the model is not effectively learning to utilize the retrieved context even with the standard loss function.
* Instead of using the likelihood gain for filtering, prior research has shown that likelihood gain can be a strong signal for training a more effective retriever (e.g., the perplexity distillation loss in [1]). This work does not compare its approach to such techniques, which could offer a more meaningful baseline. The current approach focuses on filtering after retrieval, but it could be beneficial to explore how likelihood gain can be used to improve the retrieval process itself, potentially leading to a more efficient and effective overall system. This would provide a more comprehensive understanding of how different components of the RAG pipeline can be optimized.


### Questions
* Are the three baseline techniques RAG fine-tuned for this task? Models like StarCoderBase and CodeLlama are generally not RAG fine-tuned, limiting their ability to handle retrieved chunks effectively without additional training. However, RepoFilter does perform RAG fine-tuning (as described in Section 4.1). If the other baselines are not fine-tuned, the evaluation might be unfair.

* The performance of a large model like GPT-3.5-turbo on left-to-right generation tasks is surprisingly low in Table 4--I would expect it to be at least better at the left-to-right generation task. Have the authors explored the reasons behind this underperformance?

* Can the approach be further simplified to avoid using constrained decoding at inference? Have the authors explored alternative formats, like an end-of-chunk special token before polarity tokens?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present REPOFILTER, a method for repository-level code completion and infilling. The motivation lies in addressing limitations of retrieval-augmented generation (RAG) approaches, which often misidentify positive retrieved code chunks, leading to decreased performance, longer prompts, and increased latency. REPOFILTER introduces a novel training objective designed to predict the polarity of a retrieved code chunk, retaining only positive code chunks that enhance code completion accuracy. Experiments on RepoEval and CCLongEval datasets across various completion levels (line, chunk, function) demonstrate the effectiveness of this approach.

### Strengths
- **Clarity**: The paper is well-written and accessible, facilitating comprehension of the proposed method.

- **Novelty**: REPOFILTER addresses a critical gap in repository-level code completion by introducing a streamlined, effective approach. The method’s training is straightforward, cost-efficient, and potentially generalizable.

- **Comprehensiveness**: The authors conduct extensive evaluations on two widely used benchmarks, RepoEval and CCLongEval, covering diverse completion scenarios (line/API/chunk/function completion and left-to-right/fill-in-the-middle tasks). The analysis and ablation studies offer insights into hyperparameter settings and alternative experimental configurations.

### Weaknesses
 - **Limited Exploration of Combinatorial Effects**: The authors treat the polarity of each code chunk individually based on its log-likelihood with the ground truth, overlooking potential interdependencies among retrieved code chunks. It would be valuable to consider whether combining two or more neutral/negtive code chunks might yield a positive impact on code completion accuracy. The current approach does not explore how the model might leverage synergistic effects between chunks, potentially missing opportunities for improved performance. For instance, two individually unhelpful chunks might, when combined, provide necessary context or a more complete picture of the code's functionality. This limitation could be addressed by exploring methods that consider the joint information content of multiple chunks, rather than treating them as independent entities.
- **Potential Hyperparameter Tuning Bias**: In Section 6.5, the authors justify selecting a threshold of 0.3 for `<MC>` and `<pos>`, with ablation studies verifying this choice. However, these studies are conducted on the RepoEval API subset, which overlaps with the main test data. Tuning hyperparameters on test data risks introducing bias. I recommend using a separate validation dataset for tuning and then reporting test performance with the final hyperparameter choices. The risk of overfitting to the test data is significant, potentially leading to inflated performance metrics that do not generalize well to unseen data. This issue is particularly concerning given the relatively small size of the RepoEval API subset.
- **Unstable Evaluation for Chunk and Function-Level Completion**: Evaluation based on text similarity metrics like EM or ES may be unreliable for longer code completions, as seen in Table 1. Here, CodeLlama-13B-REPOFILTER outperforms CodeLlama-13B-RepoFormer in ES but not in unit test execution, and the same holds for CodeLlama-7B-RepoFormer versus CodeLlama-7B-REPOFILTER. Robust metrics better suited to larger code segments are needed for reliable assessment. The discrepancy between text similarity and execution-based metrics highlights the limitations of relying solely on surface-level similarity for evaluating code generation quality. This is especially true for longer code segments where functional correctness is more critical than exact string matching. The current evaluation approach may not accurately reflect the practical utility of the generated code.
- **Minor Issue**:
    - In Section 5.2, where the RepoEval dataset is introduced, the authors mention 32 repositories. This number appears to be incorrect and should be double-checked.

### Questions
1. **Masking Non-Contextual Information**: At the end of Section 4.1, the authors state, "To prevent the model from merely replicating non-contextual information, we mask both the in-file and cross-file contexts during loss calculation." Could the authors elaborate on why replication occurs without masking?
2. **Thresholding for Informativeness**: In Section 5.1, the authors use an ES threshold of 0.5 to determine informativeness for completion. Given that ES may not be strongly correlated with informativeness, would it be possible to add qualitative examples illustrating informative cross-file chunks above and below this threshold?
3. **Query Construction for Infill Tasks**: Could the authors clarify how they construct retrieval queries in the infill setting? Specifically, does the query contain only preceding code or also include code following the target line/chunk? Further elaboration on how the infill setting enhances REPOFILTER’s performance, as suggested in Section 6.1, would improve clarity.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a three-step framework: **retrieval**, **filtering**, and **generation**, to enhance the accuracy of repository-level code completion. The authors introduce two special tokens, **<MC>** and **<EC>**, during the generation process to determine whether cross-file context retrieval is necessary.

Additionally, a likelihood-based metric is employed to assess whether the retrieved context is **positive**, **negative**, or **neutral** for the current completion task. Harmful cross-file context is filtered out before the model proceeds with code completion, ensuring sufficient relevant information. 

The effectiveness of the proposed framework is validated through extensive experiments on the **RepoEval** and **CrossCodeLongEval** benchmarks using language models like **StarCoderBase**, **CodeLlama**.

### Strengths
1. **Cross-file Code Completion Framework**: The authors propose a repository-level code completion framework based on a **retrieval-filtering-generation** process, which improves completion accuracy by filtering out harmful cross-file contexts retrieved during the process.

2. **Effective Methods**: Experimental results show that this framework not only improves code completion accuracy but also reduces input length compared to other baseline methods.

3. **Holistic Experimental Results**: The authors conducted comprehensive experiments, including ablation studies, on multiple benchmarks to validate the effectiveness of their approach.

### Weaknesses
 1. **Lack of Baselines**: The authors only compare their approach with RepoFormer, without considering the No-Retrieve and Full-Retrieve settings. I suggest adding more baselines based on RAG methods, such as RepoCoder, RepoHyper, RepoFuse, DraCo, CoCoGen, and HCP, for a more comprehensive comparison.

 2. **Time Overhead**: While most repository-level code completion works do not consider or report time overhead, many real-world scenarios require low latency for code completion results. I noticed that REPOFILTER evaluates the polarity of each retrieved chunk and, when the polarity is <pos>, it further checks whether the next token is <MC> or <EC>. This might introduce additional time overhead. I recommend that the authors provide data on the total time cost for a single completion task.

 3. **New Code LLMs**: Although the results on StarCoder and CodeLlama are promising, these models have been available for some time. Newer code models, such as StarCoder2, CodeGemma, DeepSeek-Coder-V2, and Qwen2.5-Coder, now natively support repository-level code completion. I recommend leveraging these newer models and conducting related experiments.

 4. **Writing**: I suggest that the authors summarize their contributions in bullet points at the end of the Introduction. This will provide readers with a clearer and more direct understanding of the key contributions of the work.

### Questions
1. **Regarding Time Overhead**： See Weaknesses 2.

### Soundness
3

### Presentation
2

### Contribution
3
