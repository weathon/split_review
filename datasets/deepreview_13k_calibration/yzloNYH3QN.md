# Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Information retrieval (IR) systems have played a vital role in modern digital life and have cemented their continued usefulness in this new era of generative AI via retrieval-augmented generation.
With strong language processing capabilities and remarkable versatility, large language models (LLMs) have become popular choices for zero-shot re-ranking in IR systems. 
So far, LLM-based re-ranking methods rely on strong generative capabilities, which restricts their use to either specialized or powerful proprietary models.
Given these restrictions, we ask: \textit{is autoregressive generation necessary and optimal for LLMs to perform re-ranking?}
We hypothesize that there are abundant signals relevant to re-ranking within LLMs that might not be used to their full potential via generation.
To more  directly leverage such signals, we propose \textit{in-context re-ranking} (ICR), a novel method  that leverages the change in attention pattern caused by the search query for accurate and efficient re-ranking.
To mitigate the intrinsic biases in LLMs, we propose a calibration method using a content-free query.
Due to the absence of generation, ICR only requires two ($O(1)$) forward passes to re-rank $N$ documents, making it substantially more efficient than generative re-ranking methods that require at least $O(N)$ forward passes.
Our novel design also enables ICR to be applied to any LLM without specialized training while guaranteeing a well-formed ranking.
Extensive experiments with two popular open-weight LLMs on standard single-hop and multi-hop information retrieval benchmarks show that ICR outperforms RankGPT while cutting the latency by more than 60\% in practice.
Through detailed analyses, we show that ICR's performance is specially strong on tasks that require more complex re-ranking signals, such as handling \textit{contextualization} and \textit{contradiction} between the query and passages, as well as \textit{information integration} across multiple passages.
Our findings call for further exploration on novel ways of utilizing open-weight LLMs beyond text generation.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors focus on adopting large language models (LLMs) as zero-shot rerankers. I believe this is crucial because if we also need to train the LLMs as rerankers, there would be no difference from the previous framework. The authors propose leveraging the intrinsic attention scores to aggregate into a document score, along with a standard debias score. ***The authors claim that the proposed method operates in O(1) LLM forward passes (This is a point I am skeptical about and would like the authors to clarify in their discussion).*** I will first assign a threshold score and then adjust it based on the authors' rebuttal.

### Strengths
1. The writing of this paper is well-crafted, allowing readers with relevant backgrounds to quickly follow and provide feedback.
2. The proposed method is versatile and applicable, making it suitable for use with open-source LLMs.

### Weaknesses
1. The claim of O(1) LLM forward passes raises significant questions. Please refer to my Question 1 for a detailed explanation, as this will determine the overall quality of the paper.
2. A limitation of this method is that ordinary users cannot implement it using advanced commercial large language models, especially when compared to RankGPT. However, I believe this is due to commercial factors rather than technical ones.
3. When only comparing against a single baseline, RankGPT, the classic datasets TREC 19 and 20 are notably missing.

### Questions
1. A listwise LLM-based ranker typically requires O(N) forward calls because it often assumes that the number of candidate documents, N, is too large, exceeding the LLM's context limit. This necessitates the use of a sliding window for multiple forward passes. Given the same number of documents, how does the proposed ICR achieve this with only two forward passes? If RankGPT requires O(N), I believe the proposed ICR would also require O(N) with the same LLM.
2. Since RankGPT is the only used baseline, the TREC 19 and 20 datasets tested in the RankGPT paper should also be included in the experiments.
3. ICR utilizes attention scores from all transformer layers. Could you provide results from an ablation study showing the outcome when using only the attention scores from the final layer?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel re-ranking method based on LLMs called ICR. ICR first aggregates the attention weights received by each document token from all query tokens. To mitigate intrinsic biases of LLMs, ICR calibrates the ranking scores by subtracting the attention scores obtained by using a content-free query. ICR is evaluated on both single-hop and multi_-hop re-ranking tasks using open-source LLMs, Mistral and LLaMA 3.1.

### Strengths
1. The problem is important, and the overall writting is clear. 
2. The proposed method is easy to follow and demonstrates effectiveness on two public LLMs.

### Weaknesses
My primary concern is the insufficient comparison with other methods and a lack of depth in experimental analysis.

1）Although the paper compares ICR with RankGPT, highlighting improvements, it would be strengthened by comparisons with more methods, especially other zero-shot listwise methods.

[1]  RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models.

[2] A Setwise Approach for Effective and Highly Efficient Zero-shot Ranking with Large Language Models.

2） The paper could benefit from additional analysis to deepen the understanding of ICR’s behavior. First, for open-source LLMs, it would be helpful to provide a clear comparison between ICR and fine-tuning (FT) methods, highlighting the performance gap and cases where fine-tuning might be preferable. Second, the paper does not analyze the sensitivity of the proposed algorithm to changes in the input document order. It would be valuable to examine how much the re-ranking results fluctuate when the order of input documents is adjusted.

### Questions
1. The analysis in Figure 4 lacks details on how results would change if the document input order were adjusted. Additionally, if the document set contains similar documents, would these similar documents receive higher weights?

2. In Section 3.3, how does the method address biases introduced by documents of varying lengths?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed in-context re-ranking (ICR), an efficient re-ranking method based on the attention distributions of LLMs. This method can achieve better performance compared to RankGPT while maintaining lower latency.

### Strengths
The motivation is "whether autoregressive generation necessary and optimal for LLMs to perform re-ranking?", which is quite interesting and worth discussing. 
The proposed method is technical sound and is effective on various datasets of re-ranking tasks. 
The paper is well-written and easy to follow.
The experiments and discussions are thorough.

### Weaknesses
The paper lacks more high-level intuition and explanations especially about why the proposed method works intuitively. 
What are the advantages and disadvantages of the proposed methods intuitively.
Why the proposed method works well although the model's instruction following ability is poor?

The claim of reducing time complexity from O(N) to O(1) needs careful consideration. The method still requires processing each document through the attention mechanism, which suggests a linear dependence on the number of documents, N. The authors need to clarify how they achieve constant time complexity, as it appears to be misleading. The current explanation of sharing KV cache does not address this concern fully.


### Questions
1. In line 216, "We use N/A as a calibration query". I was wondering why use this as the special token, how about NA or None or blank space or <>? Could these be alternatives?
2. In line 226-227, "the final ranking score sd_i, which measures the change of attention weights that each document receives when the query changes from the content-free calibration query to the actual query". I was wondering whether sd_i can be considered as distance between the actual query and calibration query? It would be better to have more high-level intuition and explanation about this.
3. In line 233-234, "since we place the query tokens at the end of the re-ranking prompt, ICR can share the KV cache of document tokens when computing s_{di, Q} and s_{di, Qcal}". I was wondering why the shared KV cache is in effective when you put query tokens at end? I didn't get the point here.
4. In line 297, "ICR's performance advantage is more prominent on Mistral, which has weaker instruction-following capabilities...". I was wondering what's the advantages of the proposed method when instruction following is involved? Whether the proposed method can better leverage important information in the query? I'm looking forward to more explanation here.
5. In ablation study/discussion, I'd love to see how the overall distribution looks like in terms of calibration scores.

### Soundness
3

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
4

### Summary
This paper proposes an unsupervised ranking method that leverages the attention scores of query tokens over each document token. Extensive experiments, including nine single-hop and three multi-hop datasets, were conducted to prove the improvements over unsupervised baseline RankGPT. Ablation studies were conducted to prove the effectiveness of calibration and aggregation.

### Strengths
1. This paper is well-written and easy to follow.
2. Extensive experiments, including nine single-hop and three multi-hop datasets, were conducted to prove the improvements over unsupervised baseline RankGPT
3. Ablation studies were conducted to prove the effectiveness of calibration and aggregation. 
4. Clear analyses were presented to help explain why calibration helps and what re-ranking signals the proposed method captures.

### Weaknesses
1) Missing important unsupervised baseline UPR:

Sachan, Devendra Singh, et al. "Improving passage retrieval with zero-shot question generation." arXiv preprint arXiv:2204.07496 (2022).

UPR ranks documents based on the log-likelihood of generating the ground-truth query given the document. Although it is less efficient than ICR, UPR operates in an unsupervised manner and should be compared with ICR.

2) The impact of document order has not been studied. ICR ranks all documents within the context, but the paper does not specify how documents are concatenated. Are they randomly shuffled before concatenation? To what extent does document order impact ranking performance?

3) For single-hop evaluations, only the weaker BM25 retriever is applied. It remains unclear whether ICR can enhance the performance of stronger retrievers.

### Questions
1) UPR is a popular unsupervised reranking method that ranks documents based on the log-likelihood of generating a query from the input document. How does ICR's performance compare to that of UPR?

Sachan, Devendra Singh, et al. "Improving passage retrieval with zero-shot question generation." arXiv preprint arXiv:2204.07496 (2022).

2) Are the documents randomly shuffled before concatenation? To what extent does document order impact ranking performance?

3) Why is the top 20 instead of the top 100 utilized for multi-hop evaluations?

### Soundness
3

### Presentation
3

### Contribution
3
