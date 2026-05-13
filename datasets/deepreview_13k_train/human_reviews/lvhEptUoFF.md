# Recursive Abstractive Processing for Retrieval in Dynamic Datasets

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Recent retrieval-augmented models enhance basic methods by building a hierarchical structure over retrieved text chunks through recursive embedding, clustering, and summarization.
The most relevant information is then retrieved from both the original text and generated summaries. 
However, such approaches face limitations with dynamic datasets, where adding or removing documents over time complicates the updating of hierarchical representations formed through clustering.
We propose a new algorithm to efficiently maintain the recursive-abstractive tree structure in dynamic datasets, without compromising performance.
Additionally, we introduce a novel post-retrieval method that applies query-focused recursive abstractive processing to substantially improve context quality. 
Our method overcomes the limitations of other approaches by functioning as a black-box post-retrieval layer compatible with any retrieval algorithm.
Both algorithms are validated through extensive experiments on real-world datasets, demonstrating their effectiveness in handling dynamic data and improving retrieval performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the dynamic document challenge problem in RAG for recursive abstractive indexing of a corpus. Specifically, to efficiently maintain the recursive abstractive indexing tree, the authors propose adRAP,  an algorithm which only partially update indexing trees when new documents are added. Furthermore, a post-retrieval summarization algorithm is also proposed -- postQFRAP, which builds an online query-focused recursive-abstractive tree for more relevant context selection. Experimental results show that the proposed method can achieve competitive performance with fully offline tree indexing algorithms such as RAPTOR baseline.

### Strengths
In general, document updating is a very common problem in document indexing, therefore it is useful to develop online indexing algorithms which can effectively address the dynamic dataset problem. And online clustering algorithms are reasonable solutions for this problem.

### Weaknesses
My main concerns about this paper are as follows:
1. The contribution is incremental, the proposed method is an extension of previous recursive abstractive indexing algorithms;
2. The two contributions, adRAP and postQFRAP, are separated. adRAP addresses the dynamic dataset problem and postQFRAP addresses the online organization problem of retrieved documents. The paper should focus on one main contribution;
3. The proposed adRAP algorithm is just an online clustering algorithm with tree structure updating strategy. Therefore I think the authors should explain and compare different online clustering algorithms. In my opinion, the proposed  problem can be better addressed using the theory-guided Chinese restaurant process, rather than the current ad hoc clustering algorithm.
4. The baselines are too weak. I think the authors should also compare different online clustering algorithms, and different online search result organization algorithms in current RAG studies.
5. The current presentation of experimental results is hard to follow and analyze.

### Questions
See Weaknesses in above.

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
3

### Summary
This paper aims at handling dynamic data and improving retrieval performance for RAG applications. It proposes adRAP, an extension of an existing work (RAPTOR), to efficiently approximate clustering when documents are added or removed. It also proposes postQFRAP, a post-retrieval algorithm that applies query-focused and recursive-abstractive processing to refine large contexts.

### Strengths
1. The method presented by the authors is mathematically interesting and seems sound (equation 3).

2. I like the pseudo-code written by the authors, which improves clarity of the paper.

### Weaknesses
1. I am not sure whether dynamic data for RAG is a high-impact research problem. First of all, building a tree for the entire dataset is a one-shot process, so I think the efficiency bottleneck is the inference speed. Secondly, if we just add a small number of documents, we can simply assign those documents to existing clusters (your way of adapting RAPTOR) or create a new cluster to hold these newly added documents. I guess the performance will not be affected significantly due to the small number of documents added (your experiment demonstrates this point). If we expect that most of the queries are related to the small number of documents we add, I think we can just restart RAPTOR and build a tree dedicated for our updated dataset. If we want to add a lot of documents, you mention that a full tree recomputation is still needed. So I am not sure the contribution of this paper. 

2. For postQFRAP, you claim to build a tree for all retrieved chunks, which sounds quite inefficient. As multiple summarization calls are required to build a tree for each query, this design annihilates your original purpose of being efficient for a small number of dynamic data. The computational cost of building a tree structure on the fly for each query, especially with multiple summarization calls, seems to negate any efficiency gains from the adRAP method, particularly when compared to methods that pre-process the data. This approach introduces a significant overhead at query time, which is a critical performance bottleneck for RAG systems.

3. Performance is weak. As discussed in the previous two points, it seems that "adRAP + postQFRAP" has similar performance as RAPTOR. Efficiency-wise, I am not sure whether it would be more efficient to use "adRAP + postQFRAP", as I mention above that you are using a more inefficient retrieval method than methods mentioned in RAPTOR (e.g., SBERT and DPR). The most salient improvement I see is "adRAP exceeds RAPTOR in metrics such as comprehensiveness, diversity, and empowerment" on QuALITY as described in line 443, but I am not sure whether the improvement comes from adRAP or postQFRAP.

4. It is questionable whether the proposed method can be applied on other state-of-the-art baselines such as GraphRAG ("From Local to Global: A Graph RAG Approach to Query-Focused Summarization"), so the impact of this paper might be very limited.

5. Experiment is limited. There is no ablation study about the effectiveness and efficiency of either adRAP or postQFRAP.

6. Writing is verbose in some parts of the paper. For example, section 3 is too long with many unnecessary details, since you are essentially providing the background of RAG and existing work in around 2 pages. There are many basic things out there that can be omitted (e.g., the EM algorithm). I suggest to simplify this section, and you just need to cite the related work with short explanation. Another option is to put those details into appendix. On the other hand, I suggest to put more words for the last paragraph of section 1 to improve clarity (otherwise, reviewers need to read the whole paper to be able to tell). For example, how much does "postQFRAP effectively enhances retrieval quality"? Are you using state-of-the-art baselines? What are those "real-world datasets"?

### Questions
1. Have you done any detailed analysis about the overall efficiency between "adRAP + postQFRAP" and RAPTOR when you only aim to add a small number of documents?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
RAPTOR is inefficient in dynamic setting where index needs to be frequently updated as it requires recomputing clusters and summaries in the hierarchical tree. To address this limitation, this paper proposes ADRAP and POSTQFRAP algorithms. ADRAP is used to update the tree without full recomputation by recalculating clusters and regenerating summaries only for nodes directly affected by the addition or removal of documents. POSTQFRAP retrieves a larger pool of documents and builds recursive-abstractive tree. It uses query-focussed summarization when building summary nodes.

Authors evaluate both methods on MultiHop, QASPER and QuALITY datasets. Authors used following metrics for evaluation: 1. answered question, 2. context relevance, 3. Human coherence metrics. In addition, authors used win-rate on comprehensiveness, diversity, empowerment, and directness.

### Strengths
- ADRAP addresses the most important limitation of the RAPTOR method. It is computationally efficient. As shown by Table 10, it's faster and requires fewer summarization calls than recomputing entire tree with RAPTOR.

- Both models have performance close to RAPTOR.

### Weaknesses
 - Evaluation Metrics: 

Authors have used indirect metrics for evaluations. LLM Judge is not the most reliable evaluation protocol if it is possible to perform direct comparisons. You should consider standard metrics like accuracy (QuALITY)/ F1 (QASPER) for better understanding. The reliance on LLM-based evaluation introduces subjectivity and potential bias, making it difficult to ascertain the true performance of the proposed methods. Furthermore, the lack of direct metrics makes it challenging to compare the results with existing literature that utilizes standard evaluation protocols.

- Baselines:

ADRAP- It would be useful to include two baselines 1. where we do not update the RAPTOR tree and just retrieve from old RAPTOR tree and new documents, 2. construct a new raptor tree only on new documents and retrieve from new + old raptor trees. The absence of these baselines makes it difficult to isolate the benefits of the proposed update mechanism. Without comparing against a naive retrieval approach and a partial rebuild approach, it is hard to determine whether the complexity of ADRAP is justified. postQFRAP- a version of the model without explicit clustering (e.g., Tree Summarize, Create and Refine, Accumulateresponse synthesizers in LlamaIndex). The lack of comparison against simpler summarization techniques makes it difficult to assess the contribution of the query-focused summarization and recursive-abstractive tree building.

- Datasets:

Both QuALITY and QASPER datasets include question that can be answered by a single document. Do you think they make a suitable dataset for your evaluation? Original RAPTOR work built one tree per document and answer questions based on that. However the benefit of your approach only comes when we know that building one tree for all documents is required. Otherwise, we can just build one tree per document and retrieve from that. 
In my opinion, you should consider evaluating your approach on complex questions that require multi-document evidence. The datasets used do not fully capture the intended use case of the proposed methods, which are designed for scenarios requiring multi-document reasoning. The single-document nature of many questions in the chosen datasets limits the ability to demonstrate the advantages of the hierarchical summarization and retrieval approach.

### Questions
- Why didn't you use standard metrics for evaluation? MultiHOP can be objectively answered, and there are established metrics/ evaluation protocol for other two datasets as well. 

- Refer to question about datasets in Weakness.

### Soundness
2

### Presentation
2

### Contribution
1
