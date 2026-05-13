# DMQR-RAG: Diverse Multi-Query Rewriting in Retrieval-Augmented Generation

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Large language models often encounter challenges with static knowledge and hallucinations, which undermine their reliability. Retrieval-augmented generation (RAG) mitigates these issues by incorporating external information. However, user queries frequently contain noise and intent deviations, necessitating query rewriting to improve the relevance of retrieved documents. In this paper, we introduce DMQR-RAG, a Diverse Multi-Query Rewriting framework designed to improve the performance of both document retrieval and final responses in RAG. Specifically, we investigate how queries with varying information quantities can retrieve a diverse array of documents, presenting four rewriting strategies that operate at different levels of information to enhance the performance of baseline approaches. Additionally, we propose an adaptive strategy selection method that minimizes the number of rewrites while optimizing overall performance. Our methods have been rigorously validated through extensive experiments conducted in both academic and industry settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces DMQR-RAG, a novel multi-query rewriting approach aimed at improving document retrieval diversity and recall within the Retrieval-Augmented Generation (RAG) framework. Unlike prior methods, DMQR-RAG leverages multiple rewriting strategies to ensure diverse document retrieval while maintaining high relevance. This approach aims to refine the transmission of information from queries to documents.

While the proposed method shows promise and demonstrates performance improvements across both academic and industry settings, the paper lacks sufficient technical depth and detail, especially regarding the specifics of the rewriting method. Important methodological details are missing, making it difficult to figure out if the hypotheses about improved retrieval and response generation are fully substantiated in the methodology. This lack of clarity around the technical implementation may hinder reproducibility and raise questions about the robustness of the reported improvements. Despite these limitations, the results presented indicate the potential for DMQR-RAG to set a new standard in multi-query rewriting for RAG, though further clarification and technical elaboration would strengthen the work considerably.

### Strengths
1) The paper is clear and easy to follow.

2) It addresses an important area in RAG, enhancing retrieval through query modeling.

3) Comprehensive Evaluation: Experiments are thorough, including both academic and industrial settings.

### Weaknesses
1.  While Section 2.1 provides an intuitive overview, it lacks specific details on implementing query rewrites. The approach for the three aspects—equality, expansion, and reduction—appears to use a single baseline for each, limiting the exploration of different methodologies. In Section 2.2.2, the selection mechanism determines which rewritings to apply but does not clarify the criteria behind these choices. IMO if only the baselines were used for equality, expansions, and reduction, the technical novelty of this work is limited to asking the LLM to choose between different types of "known" rewriting techniques. 

2. The paper lacks clarity on how query rewrites are actually implemented. For instance, the general query rewrite strategy aims to "extract all keywords from the query q, particularly nouns and subjects." However, the exact process for this extraction is unspecified. Thus I don't understand how the handling of extracted elements and the potential noise in proper noun extraction is dealt with. This gap is imprtant, as extraction methods directly impact retrieval performance and can introduce significant variability.

3. The hypotheses in the paper are not well-supported by evidence. For instance, the statement "By enhancing the diversity of information in the rewritten queries, we increase the likelihood of retrieving a broader range of documents, ultimately improving our chances of obtaining genuinely relevant documents" is attributed to general literature (Maron & Kuhns, 1960; Baeza-Yates et al., 1999; Weikum & Vossen, 2001) rather than research directly focused on natural language query diversity. Some references, such as the Weikum and Vossen citation, are database-focused and do not address natural language queries or retrieval diversity directly. Acc. to me this doesn't add to the argument's relevance and rigor. It is also well known that rewriting adds to the drift in query modelling.  

4. The related work does not include any of the classical or modern information retrieval literature about query modelling. This also shows in the baselines where only LLM-based query rewriting baselines have been considered.

5. The experiments look comprehensive, but the choice of datasets could have been better argued. Most of the QA datasets are multi hop or complex QA tasks which inherently have multiple aspects. It would be interested to test their effectiveness on simpler QA datasets like natural questions or even ranking datasets like MSMarco or TREC-DL. If DMQR-RAG only works for complex questions, then the authors should position their claims accordingly. In that case they should think about other datasets like strategyQA or WikiMultihopQA.

### Questions
1) What are the implementation details of the methods presented in 2.1. Specifically, what novel additions were made to the baselines mentioned in the section explaining equality, expansions, and reduction  ?

2) Did you consider any classical query rewriting methods ?

3) Do your methods work for queries that are not multi hop or are not complex ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes an approach to create diverse rewrites for RQG. The assumption is that different rewrites may account for different types of queries. The rewrites are obtained through different prompts to an LLM. Another phase of adaptive selection strategy is used to select the generated rewrites via a few-short prompt. The experiments performed on 3 datasets show that this approach can outperform the original query and the single rewrites created by other methods. It also slightly outperform the alternative fusion method of different RAGs.

### Strengths
1. The assumption that different rewrites can reflect different aspects of queries is reasonable. The creation of diversified rewrites has not been widely explored in the RAG literature.
2. The strategies used in this paper - prompting an LLM - for different types of rewrites is also reasonable. This is a commonly used strategy in literature.
3. The experiments show interesting results. Although it only outperforms slightly the fusion method, the study shows that creating diverse rewrites is a reasonable alternative to it.
4. The ablation analysis shows the impact of different types of rewrite, as well as of different LLM used.

### Weaknesses
1. The proposed approach is based on a range of the existing ones. The only originality lies in a combination of previous rewrites. The  basic idea is quite similar to the fusion method. It is unclear if conceptually, the proposed method is better than the fusion method (which is still quite simplistic). Overall, the novelty of the approach is limited.
2. In addition, everything is done through prompting. Despite the fact that some improvements have been obtained, it is difficult to understand how the diverse rewrites created have been incorporated in the selection phase. The paper mentions several interesting targeted problems with the single rewrites (noise, etc.), the problems are not further analyzed later. It is simplistic to assume that using relevant prompts would solve the problems. It would be great if these problems are further analyzed in the experiments.
Despite the reasonable assumption made at the beginning of the paper, one can hardly see how the problem has been solved by the two steps of prompting. Therefore, the proposed approach and experiments only provide a quite superficial understanding of the problem.
3. When multiple rewrites are generated through multiple prompts, there is obvious an additional cost. This aspect should be discussed.
4. In the baselines, the prompts are zero-shot prompts, while in the proposed one selection phase, few-shot learning is used. This may give some advantage to the proposed method. It may be fairer to try to use few-shot learning in the baselines.

### Questions
1. How have the proposed method solve the different problems mentioned in the paper? Does it reduce noise? For what queries each type of rewrite is the most useful? Instead of asking an LLM to make the selection, would it be better to train a small selector for it?
2. Have you compared with more sophisticated fusion methods? There are a number of alternative approaches proposed in the IR literature for result fusion. They could be considered as alternatives.
3. The proposed method is related to search result diversification, for which some studies proposed to diversify the search queries. Can the  proposed method be related to these diversification methods?

### Soundness
2

### Presentation
3

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
This paper introduces a strategy for query rewriting, aimed to enhance RAG systems' performance. In particular, this strategy would encourage rewriting the user query into multiple diverse queries by combining 4 different query rewriting strategies. This paper uses a fixed retriever + reranker setting where the retriever is bing search engine and the reranker is BGE-reranker. On three test datasets, this strategy developed by this paper (named DMQR) is comparable (maybe slightly better) to another previously published multi-query rewriting strategy (RAG-Fusion), and outperforms other baselines. This paper further introduce another prompt that allows a subset of query rewriting strategies to be selected based on the specific data point. This adaptive strategy is designed to reduce the amount of distracting documents during retrieval. The paper showed that in some industrial-setting datasets, adaptive DMQR proposed by the paper slightly outperforms RAg-Fusion.

### Strengths
The paper introduces a strategy for rewriting user queries into multiple diverse queries. These diver queries are aimed to retrieve more diverse and comprehensive documents, which would later be used for a generator such as GPT4. In order to reduce the irrelevant documents retrieved by some non-satisfactory rewrites, the paper proposes an adaptive strategy which is a specialized prompt that instruct an LLM to select only the appropriate rewriting strategies based on a specific user query, so data-specific. One of the paper's main strength is that it uses both commercial and open-sourced language model generator such as GPT4 and Llama3-8B, which shows their adaptive DMQR RAG is generalizable to different LLMs as generator. The paper also conduct comprehensive ablation studies to investigate the individual effect of each of the rewriting strategies used in the DMQR. Lastly, the paper was able to show that adaptive DMQR outperform RAG Fusion in industrial setting.

### Weaknesses
1. Lack of originality. I think the idea of combining multiple rewritten queries instead of a single rewritten query has already been proposed in a previous work RAG-Fusion. Therefore, this work is not the first to propose using multiple rewritten queries to improve RAG performance. The authors claim their rewritten strategies are "based on different levels of information", which is vague. In fact, all strategies used in authors' proposed DMQR: removing noise and excessive details from user queries, expanding user queries (i.e. query expansion), and keyword extraction, are fairly natural ideas and many of which I am sure have been explored by previous work before, such as query expansion. This paper fails to engage in a meaningful discussion of of previous work. While it cites a good number of papers in section 2.2.1, it does not discuss what these papers do and how the authors proposed ideas, information equality, expansion and reduction are different from these previous papers. I highly encourage the authors to include a formal related work section. Furthermore, all ideas expressed in this paper, from query rewrite strategies to adaptive selection, are all accomplished by prompt engineering. Prompt engineering itself is not a source of adequate innovation and originality. As it stands right now, I fail to see the true distinctions of this work and previous works, especially RAG Fusion. I would rate the originality of this work to be low, and I am inclined to reject this paper primarily because of this reason.

2. The paper's writing is very unclear, it lacks a related work section that properly acknowledge previous work and explain why the current work is different. It talks about "transmission of information from queries to documents" in the introduction, and never explained the meaning of the sentence. There are too many acronyms which prevents easy understanding. I also believe section 2.1 is completely not necessary.

3. Another concern is that this work only uses bing + BGE-reranker as the sole retriever. While the paper claims this is its advantage, I think it is completely nonsensical to only use one retriever. I also don't understand the claim "without loss of generality", why is this specific bing+ BGE retrieval pipeline can be considered as "without loss of generality"? Later on in the paper, the authors even used different LLMs as generator, showing generalizability of their approach. So why do the authors not wishing to demonstrate generalizability across different retrieval settings? There are many unknown systematic bias introduced with a fixed (and not generalizable) retrieval setting. I would encourage the authors to apply their DMQR strategy on other retrieval settings, including using state-of-the-art semantic embeddings (OpenAI-v3, Grit-LM) and alternative retrieval strategies such as RankGPT and RankLLama. This is one of the major weakness of the paper, failing to show generalizability across retrieval settings.

4. The paper does not provide bootstrapped confidence intervals and p-values, both of which are necessary to examine with statistical rigor if one approach is better than another approach. Another main concern is this, the authors specifically mentioned in their paper that Table 2 shows DMQR is better than RAG-Fusion w.r.t P@5 metric, this feels like selective reporting.

### Questions
1. For all tables, especially table 2, I would suggest authors to bold numbers that are statistically different from the second-best number, otherwise please bold both numbers to avoid confusion. Figure 4 should include error bars, and Figure 4 (c) should include some form of indications for p-value, confidence-level or error bars. 

2. I would like to see a proper discussion that clearly describes the difference of the current paper's DMQR strategy, and other works such as RAG Fusion. I would also like the authors to discuss the four ideas proposed in the paper, general query rewrite, keyword extraction and rewrite, query expansion, query reduction,  and how they relate or differ from previous work. I know for a fact that there are many works on query expansion, so at least that idea is not novel. As I explained before, the lack of proper related work discussion prevents me from seeing the true originality (if there is any) of this paper.

3. I think limiting the setting to only bing + BGE is a potential bias-inducing practice. I would like to see authors compare their method with RAG Fusion while using different retrievers, as mentioned before. 

If my concerns are addressed, I would adjust my scores accordingly.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DMQR-RAG, a Diverse Multi-Query Rewriting framework aimed at enhancing document retrieval and response quality in Retrieval-Augmented Generation (RAG). The authors also present a rewriting strategy selection method that identifies the most suitable approach for each query, thereby improving performance with fewer rewrites. The framework has demonstrated robust performance in both academic and industrial settings.

### Strengths
1. DMQR-RAG has shown effective results.
2. Extensive case studies and ablation experiments were conducted, and the framework was deployed in real-world industrial scenarios.
Weaknesses:

### Weaknesses
1. The technical depth of the four rewriting strategies and the adaptive rewriting selection method is insufficient.
2. The paper appears to contribute primarily a prompt without additional significant contributions.
3. The adaptive rewriting strategy selection significantly increases the number of tokens and inference latency, which are not addressed in the paper. This is due to DMQR-RAG requiring the input of recall results from multiple queries into the LLM's prompt.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
