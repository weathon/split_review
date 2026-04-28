# Distributed In-Context Learning under Non-IID Among Clients

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Advancements in large language models (LLMs) have shown their effectiveness in multiple complicated natural language reasoning tasks. 
    A key challenge remains in adapting these models efficiently to new or unfamiliar tasks. 
    In-context learning (ICL) provides a promising solution for few-shot adaptation by retrieving a set of data points relevant to a query, called in-context examples (ICE), from a 
    training dataset and providing them during the inference as context. 
    Most existing studies utilize a centralized 
    training dataset, yet many real-world datasets may be distributed among multiple clients, and remote data retrieval can be associated with costs. 
    Especially when the client data are non-identical independent distributions (non-IID), retrieving from clients a proper set of ICEs needed for a test query presents critical challenges. 
    In this paper, we first show that in this challenging setting, test queries will have different preferences among clients because of non-IIDness, and equal contribution often leads to suboptimal performance.
    We then introduce a novel approach to tackle the distributed non-IID ICL problem when a data usage budget is present.
    The principle is that each client's proper contribution (budget) should be designed according to the preference of each query for that client.
    Our approach uses a data-driven manner to allocate a budget for each client, tailored to each test query. 
    Through extensive empirical studies on diverse datasets, our framework demonstrates superior performance relative to competing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the challenge of distributed non-IID in-context learning (ICL) for LLMs, where data is spread across clients with differing distributions. The paper first shows that uniform in-context examples would fail on non-IID situations. Then the authors propose a method to optimize the allocation of a limited in-context examples (ICEs) budget by training a budget allocator. This allocator predicts query-specific budgets for each client, addressing the inefficiencies of uniform allocation under non-IID settings. The method outperforms baseline approaches like random and uniform budgets in experiments, improving ICL performance on distributed datasets.

### Strengths
1. This paper highlights the important yet underexplored problem of distributed non-IID in-context learning (ICL), offering fresh insights into a new problem.
2. The paper presents some valuable experimental results demonstrating the poor performance of distributed non-IID ICL under simple uniform budget allocation, effectively validating the significance of the problem.
3. The method proposed in this paper have improved the performance in a simple while effective way.

### Weaknesses
1. The paper does not provide concrete examples of distributed non-IID ICL scenarios. So i don't get that given the server can request budgeted samples from each client, why can't these samples be used to simulate a comprehensive, unbiased retrieval pool for inference?

2. The training dataset for the allocator is constructed by retrieving k samples per query from each client, combining these 𝐶×𝑘
samples to simulate a unified dataset. However, this simulation raises questions. If the simulation is reasonable (e.g., with large 𝑘), why not directly perform retrieval from this simulated dataset instead of training an allocator? If the simulation is unreasonable, can this dataset still be valid for training the allocator?

3. In Figure 8, the proxy size appears to have minimal influence, which is surprising. Since the allocator is trained using questions from the proxy dataset, a poor match between the proxy and test set questions should bias the collected data and hinder the training of a good allocator. However, this surprising result lacks a detailed explanation.

4. The conclusion in Section 3-Observations that query embeddings can determine budget assignments is based on observed clustering patterns in oracle budgets corresponding to different queries. This conclusion may be too strong, as other factors, such as the specific distribution of client data, might play a criticle role. For instance, in the experiments, non-IID clients are constructed based on classes, and these class-based distributions likely influence budget assignments significantly.

5. The experiments simulate non-IID clients based on data classes. Could an LLM directly infer which classes are relevant for a query and decide sample allocations accordingly? Since the allocator effectively behaves like a classifier for assigning budgets based on query classes, a straightforward rule-based budget allocation using known client classes might perform comparably.

6. There are multiple spelling mistakes in the paper. For instance, in Section 2.2, the first two sentences describing the pipeline use k_c with seemingly different meanings, leading to confusion.

### Questions
1. Why not evaluate using inherently distributed non-IID datasets? Is there an available one or not?
2. How are proxy datasets constructed, and do they ensure coverage of all clients? The description suggests the proxy set is sampled directly from the test set, but what real-world scenario does this correspond to, and how would such a proxy dataset be realistically constructed? Can you provide specific examples of a proxy dataset in real-world application?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of distributed in-context learning under non-identically distributed (non-IID) data across multiple clients. It trains a budget allocator to dynamically allocates the number of in-context examples (ICE) retrieved from each client based on the relevance of query. Specifically, it trains a multi-layer perceptron (MLP) for each client to approximate the oracle budget, derived from a server-side proxy dataset, enabling efficient and targeted ICE retrieval per query. This paper additionally explores paraphrasing techniques to ensure data privacy in distributed contexts. Empirical results across multiple datasets show that this approach outperforms several baselines.

### Strengths
1. Distributed ICL under non-IID conditions is an interesting problem and aligns well with real-world scenarios. This paper explore the challenges under this setting, providing some meaningful insights.
2. The proposed method is simple yet effective across several benchmarks, with low training overhead.

### Weaknesses
1. In real-world scenarios, data distribution differences can manifest in multiple aspects, such as text length, style, etc., but this paper only focus on Non-IIDess at the class level. I strongly recommend the author to take more aspects into considerations. Specifically, the paper should explore how variations in text length, writing style, and vocabulary across different clients impact the performance of the proposed method. For instance, clients might have data with significantly different average sentence lengths or use different linguistic styles (e.g., formal vs. informal). These factors could introduce biases in the in-context learning process, and the paper should investigate the robustness of the proposed approach under such conditions.
2. Since the training of allocator does not require the label of examples, the experiments should not be limited to classfication tasks. The effectiveness of allocator on generation tasks remains to be validated. The paper should extend its evaluation to generation tasks, such as text summarization or machine translation, to demonstrate the general applicability of the proposed budget allocation method. It is important to investigate whether the learned budget allocator can effectively select relevant in-context examples for generation tasks, where the notion of relevance might differ from classification tasks. For example, in summarization, the allocator should be able to identify examples that provide relevant content and style for generating a summary.
3. The partition for non-IIDness in the main experiments is unreasonable. According to Table 7, for binary classification task like Subj and MR, each client only having access to data under one class is too extreme and can easily lead to biased predictions. This extreme non-IID setting does not reflect realistic scenarios where clients typically have access to data from multiple classes, albeit with varying distributions. The paper should consider more realistic non-IID settings, such as Dirichlet distribution-based partitioning, where each client has access to data from all classes but with different class proportions. This would provide a more comprehensive evaluation of the proposed method's performance under more practical conditions.

### Questions
The training of the allocator relies on a proxy dataset. In practice, the distribution of test data is usually unknown and obtaining a proxy dataset with the same distribution is unrealistic. What if the distribution of the proxy dataset differs from that of the test set?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims at addressing the issue of non-iid distributed  in-context examples (ICE) for in context learning. The authors 
introduce an approach to tackle the distributed non-IID ICL problem by calculate the budget for different clients on the number of ICEs for different clients. The principle is that each client’s proper contribution (budget) should be designed according to the preference of each query for that client. This is done by the server who
will gather the optimal budget statistics using an existing proxy dataset on the server side. Basically, the idea is straightforward with limited novelty. The paper is well structured and the experiments are thorough. However, as mentioned, the novelty and technical depth is limited.

### Strengths
Pros:
1). The paper is well structured 

2). The experiments are thorough.

### Weaknesses
Cons:

1). The novelty and technical depth is limited. The core idea is the server 
will gather the optimal budget statistics using an existing proxy dataset on the server side. This however is pretty straightforward.

2). I think the work is highly related to the distributed RAG work. THe authors are suggested to include the discussion of the difference of existing distributed RAG works and compare with these approaches if possible.

3). The paper only uses small open-sourced LLMs, such as GPT-Neo-1.3B GPT-Neo-2.7B Llama-2-7B. Is that possible to provide results using larger ones, such 70B LLama-3.1 and other close-sourced ones, such as Claude 3.5 and GPT-4o?

### Questions
as shown in the weakness.

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
This paper proposed a solution to ICL when non-iid data exist across clients. The authors identify that traditional ICL assumes a centralized and uniform dataset that might not hold in real-world use cases (distributed), where each client's data might vary significantly. Thi could lead to suboptimal results by uniformly retrieving ICEs. In this paper the authors propose a framework that trains a budget allocator to determine the optimal number of ICEs to retrieve from each client based on their data's relevance to the query. The allocator uses a server-side proxy dataset to guide budget assignment per query - and this adjusts the contributions from each client and therefore more relevant context for inference. The experiments in this paper cover various LLM architectures over a series of classification tasks and demonstrate that this method improves ICL performance over existing distributed strategies (especially in non-iid scenarios)

### Strengths
This paper identifies a real-world complexity which is the non-iidess of the dta settings during ICL. It introduced a budge allocator that dynamically selects the most relevant ICEs from each client based on their own queries, which leads to improvement over uniform or random ICE distributions.  It also includes a privacy-preserving option using paraphrasing and demonstrates consistent performance gains over such privacy-preserving setting.

### Weaknesses
1. I feel the task covered in the study is quite limited to classification tasks. It would benefit from proving the effectivenss across other more complex tasks that are more context-heavy such as RAG and multihop reasoning. 
2. The paraphrasing based method to secure privacy during data retrieval - seems to have limited evaluation and more robust evaluation against other privacy-preserving techniques needs to be done to support the claim
3. The proposed solution relies on the assumption that a high quality, representative proxy dataset presents at server-side. Although experiments have shown the method stability data size. it would be nice to see furtehr experiments on how the proxy data quality or distribution affects performance or alternative methods to reduce such dependency.

### Questions
1. In a real world use case, even when sharing a similar task, the clients might have totally different prompts in terms of structure, length, and specific requirements. Will this affect retrieval effectiveness since it heavily depends on the similarity between query and training examples? 
2.  Could the authors provide more details on the proxy dataset used to train the budget allocator? Specifically, how is the proxy dataset selected, and how does it ensure adequate representation of non-IID distributions across diverse client tasks?
3. The paper references federated learning in related works, have you done any comparisons with FL methods that tackle non-IID distribution, especially regarding data and budget efficiency
4.  How sensitive is the budget allocator to differences across task types? Does the allocator need to be re-trained for different tasks?
5. Table 3 shows the result from Llama-2-7B but line 502 says Gemma-2B was used
6. Missing reference for ICL annotation selection under limited budget - "Mavromatis et al. Which examples to annotate for in-context learning? towards effective and efficient selection"

### Soundness
3

### Presentation
3

### Contribution
2
