# Grounding by Trying: LLMs with Reinforcement Learning-Enhanced Retrieval

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The hallucinations of large language models (LLMs) are increasingly mitigated by allowing LLMs to search for information and to ground their answers in real sources. Unfortunately, LLMs often struggle with posing the right search queries, especially when dealing with complex or otherwise indirect topics. Observing that LLMs can learn to search for relevant facts by \textit{trying} different queries and learning to up-weight queries that successfully produce relevant results, we introduce \underline{Le}arning to \underline{Re}trieve by \underline{T}rying (LeReT), a reinforcement learning framework that explores search queries and uses preference-based optimization to improve their quality. \methodclass can improve the absolute retrieval accuracy by up to 29\% and the downstream generator evaluations by 17\%. The simplicity and flexibility of \methodclass allows it to be applied to arbitrary off-the-shelf retrievers and makes it a promising technique for improving general LLM pipelines. Project website: \url{http://sherylhsu.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In multi-hop question answering, a model needs to perform multiple retrieval steps before arriving at an answer.  Since the reward (answer) is not known until the last step, this problem lends itself well to reinforcement learning (RL).  The paper proposes to optimize one component (the question generator for retrieval) in the multi-hop QA pipeline using RL.  The method uses direct supervision (gold retrieved docs) to first train a reward function.  Then a diverse set of queries are sampled from the model using varied prompts.  The rewards for these generations are fed into an RL algorithm (IPO) to improve the query generator.  The method improves substantially on pure SFT methods on HotpotQA and HoVer.

### Strengths
* Well written paper, clear presentation
* Results are strong and convincingly support the claim that using RL to improve query generator works better than pure SFT.

### Weaknesses
 * A bit difficult to judge the novelty of the contribution.  Has similar methods been used for single-hop QA or RAG in general?  If so, the novelty here might be marginal, especially since the paper relies on direct supervision for the reward model.
* The two multi-hop datasets used are not natural and somewhat out-of-date.  It would be great to see the methods usefulness on more relevant tasks and benchmarks.  The long-form generation attempt in the appendix is interesting, and could perhaps be developed more and moved into the main text?

### Questions
* Has similar methods been used for single-hop QA or RAG in general?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework called "Learning to Retrieve by Trying" (LeReT), which aims to improve the grounding of large language models (LLMs) through reinforcement learning (RL)-based retrieval. LeReT enables LLMs to generate queries, learn from trial-and-error, and enhance retrieval by using diverse few-shot prompts combined with preference-based reinforcement learning. LeReT's flexibility makes it adaptable across different retrieval systems, with potential applicability in broader retrieval-augmented generation (RAG) contexts.

### Strengths
1. Introduces a unique reinforcement learning framework to improve retrieval accuracy in LLMs, especially for complex multi-hop queries.
2. Demonstrates the effectiveness of iterative training in enhancing the retrieval and grounding abilities of LLMs.
3. Compatible with various retrieval systems, including ColBERTv2 and Azure AI Search, indicating its broad applicability.

### Weaknesses
1. Primarily relies on direct supervision for labeling relevant documents, which may limit its scalability in cases where explicit relevance labels are unavailable. The reliance on explicit labels for each hop in multi-hop retrieval is particularly concerning, as it requires significant annotation effort and may not be feasible for all domains or tasks. This approach also risks overfitting to the specific annotation style and may not generalize well to scenarios where relevance is more nuanced or subjective.

2. Requires extensive computation due to multi-hop retrieval and diverse query sampling, making it resource-intensive. The computational burden is further exacerbated by the need to sample multiple queries and perform retrieval at each hop, which can quickly become prohibitive for large datasets or complex queries. The lack of parallelization in the multi-hop process also limits the potential for speedups.

3. The need for sampling across multiple hops is computationally intensive and less parallelizable, reducing scalability. The sequential nature of multi-hop retrieval, where the output of one hop feeds into the next, inherently limits parallelization. This makes it difficult to leverage modern hardware accelerators and can significantly slow down the training process, especially for longer chains of reasoning.

### Questions
1. While iterative training improves retrieval accuracy, does it potentially overfit the model to specific multi-hop tasks, thereby impacting generalizability in other retrieval-augmented scenarios?
2. What is involved in adapting LeReT to new domains or types of queries that it was not originally trained on?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents LeReT, a framework for improving LLM retrieval and answer grounding using reinforcement learning. It uses prompt-driven diverse query generation, model optimization with preference-based RL, and reward labeling for retrieved documents. Experiments on HotpotQA and HoVer datasets show significant improvements in retrieval and downstream generation compared to baselines. Analysis reveals the importance of diverse few-shot prompting and LeReT's applicability across different retrievers. Limitations include the use of direct supervision, and future work may focus on indirect supervision and tool updating.

### Strengths
- LeReT is applicable to general retrieval-augmented generation (RAG) systems and can adapt to different retrievers.
- LeReT significantly improves retrieval accuracy. Compared to the unadopted Llama and Gemma instruction models, the recall rate increases by 9-22% on HotPotQA and 27-29% on HoVer.
- It can be used iteratively: applying LeReT for two iterations shows that the model performance after the second iteration is better than that of the standard non-iterative LeReT.

### Weaknesses
The novelty assertion of the proposed method lacks clarity. Regarding the related work spanning from line 139 to 148, it remains ambiguous as to how the proposed method differentiates itself from those other methods. I comprehend that the proposed approach employs diverse query generation and IPO for preference learning. However, these seem to be more of incremental enhancements within an existing framework rather than representing a distinct novelty.

Also, the experiments lack comparisons with the most relevant recent works. Only the basic few-shot prompt baseline is compared.

Line 76 "If LLMs can observe the retrieved documents for different search queries, they can learn which queries lead to better outcomes." What supports this claim? And if this is true, then why do you need the direct or indirect supervision to teach LLM "how to query"?

### Questions
- Line 76 "If LLMs can observe the retrieved documents for different search queries, they can learn which queries lead to better outcomes." What supports this claim? And if this is true, then why do you need the direct or indirect supervision to teach LLM "how to query"?

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
4

### Summary
The paper addresses the issue of hallucination in language models by enhancing their capability to generate effective queries for retrieving relevant facts, thereby improving the accuracy of model responses. The proposed approach, LeReT, generates diverse search queries by incorporating few-shot examples. It constructs comparative queries guided by the supervision of retrieval quality and optimizes the model using the IPO algorithm. The study empirically validates the LeReT framework, exploring various methods of collecting retrieval rewards and assessing performance across different retrievers.

### Strengths
1. The motivation that enhancing RAG performance through learning to generate better search queries is clear and reasonable.
2. The experiments present the improvement in both retrieval quality and finally performance, which validate the soundness of proposed algorithm.

### Weaknesses
1. The writing and presentation of results in this work could be enhanced. On line 254, I think it should be, "In this work, we consider XXX."

2. Some baselines (https://aclanthology.org/2023.emnlp-main.585.pdf, https://openreview.net/pdf?id=vDvFT7IX4O, and https://aclanthology.org/2023.acl-long.99.pdf) could be added to both the experiments and the related works sections. Although these works may not directly focus on multi-hop retrieval, they fit broadly within the same topic as this work, i.e., "query expansion." These works focus on generating better search queries to enhance RAG performance.

3. Relying on annotated golden documents, referred to as "direct supervision" in this work, limits the vision of the study. In more general scenarios, collecting "indirect supervision" is more feasible. Moreover, signals from "indirect supervision" are the ultimate indicators for downstream tasks.

### Questions
1. On lines 218–219, are there any concrete examples illustrating the differences between BFRS-generated queries and high-temperature sampling queries?

2. Regarding line 260, what are the examples used in few-shot prompting? Why is few-shot prompting not feasible during testing? Is it due to considerations of inference efficiency?

3. As for section 4.3, are there any details about how rewards are computed?

4. For Iterative-LeReT and the discussion in Section 4.3, this multi-hop search process seems compatible with online RL training, such as using PPO, by incorporating process rewards at each hop and a final reward for the conclusion. Have the authors explored online RL training?

### Soundness
3

### Presentation
2

### Contribution
3
