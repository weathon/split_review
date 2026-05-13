# SiReRAG: Indexing Similar and Related Information for Multihop Reasoning

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
Indexing is an important step towards strong performance in retrieval-augmented generation (RAG) systems. However, existing methods organize data based on either semantic similarity (similarity) or related information (relatedness), but do not cover both perspectives comprehensively. 
Our analysis reveals that modeling only one perspective results in insufficient knowledge synthesis, leading to suboptimal performance on complex tasks requiring multihop reasoning.
In this paper, we propose \model{}, a novel RAG indexing approach that explicitly considers both similar and related information. 
On the similarity side, we follow existing work and explore some variances to construct a similarity tree based on recursive summarization.
On the relatedness side, \model{} extracts propositions and entities from texts, groups propositions via shared entities, and generates recursive summaries to construct a relatedness tree. We index and flatten both similarity and relatedness trees into a unified retrieval pool. Our experiments demonstrate that \model{} consistently outperforms state-of-the-art indexing methods on three multihop datasets (MuSiQue,  2WikiMultiHopQA, and HotpotQA), with an average 1.9\% improvement in F1 scores. As a reasonably efficient solution, \model{} enhances existing reranking methods significantly, with up to 7.8\% improvement in average F1 scores.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SiReRAG, which proposes to consider both similar and relatedness information when creating retrieval indices that address queries with multi-hop reasoning. The paper gives motivations to demonstrate the bottleneck of solely modelling relatedness or similar information only. For similar information, the paper constructs a similarity tree based on recursive summarization, while for relatedness, SiReRAG extracts propositions and entities from text, and groups them via shared entities to construct a relatedness tree. Experimental results show SiReRAG considerably improves over other baselines like HippoRAG, GraphRAG and RAPTOR when evaluated on various multi-hop QA datasets.

### Strengths
1)	The approach shows considerable performance improvements over RAPTOR on a variety of multi-hop QA datasets.

2)	The experimental ablation settings are thorough and show the benefit of different design choices made by the authors for the SiReRAG approach.

### Weaknesses
1) The paper does read like incremental work over RAPTOR, and it is hard to be convinced that the paper has enough novelty for acceptance at ICLR.

2) Some important baselines such as the closed book approach, i.e. directly getting the final answer from the LLM without any retrieval, or iterative retrieval, such as Self-Ask [1] or DSPy [2] are missing. Also, the authors should include these baselines when doing the inference latency comparison.

3) The writing needs to be improved in Sections 1 and 3 of the paper since it’s not easy to grasp the main intuitions or motivations of SiReRAG. 

### Questions
1)	The motivation example in Figure 1 is a bit misleading. The authors suggest that the question “Who is the father of the artist who painted Head I?” has three hops of reasoning, whereas it only requires two hops, i.e. finding the artist in 1st hop and then identifying the author in the 2nd hop. This example can be a bit confusing to the reader on what the overall motivation of the approach is.

2)	It is very surprising to see almost similar performance for models of highly different capabilities such as GPT-3.5-turbo and GPT-4o. The authors should provide more insight/analysis on why this is happening? Also, what is the performance when the LLM used is an open-source model such Llama-3 8B.

3)	It would be interesting if the authors could show performance separately based on the number of reasoning hops present in the question. Also, does the approach show any benefits over RAPTOR for single hop/simple queries?

4)	The authors should also evaluate more recent multi-hop QA datasets, such as FanOutQA or FreshQA. All the datasets considered are pre-2022, raising concerns about leakage into LLM pretraining data. 

5)	The authors should also consider adding a few qualitative analysis examples that demonstrate how and “why” (i.e. which part of the method helps) SiReRAG improved over RAPTOR due to incorporating the relatedness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents SiReRAG: a new indexing and retrieval technique that takes into account both "semantic similarity" and "entity relatedness" for answering complex multi-hop queries.

The suggested technique is built mostly on top of another technique called RAPTOR (which indexes text chunks on similarity only), but augments it by: first, extracting entity-level facts or propositions s (which are single facts/statements about entities), using LLMs like chatGPT or LLama-instruct, then applying the RAPTOR pipeline to extracted propositions to create relatedness trees akin to the original RAPTOR similarity trees. The final method merges the output from the two trees (one from original RAPTOR built on text chunks, and another from RAPTOR built on extracted and aggregated propositions).

The paper includes comprehensive evaluations and shows significant improvement over baseline methods that use only similarity or relatedness features.

### Strengths
Originality: The work presented in SiReRAG is original in the sense it combines ideas from two existing methods/philosophies about indexing, similarity and entity-relatedness into one solution.

Quality: The thought process and reasoning of the paper is mostly intuitive and simple (merge two ideas that have been shown to improve performance), the experimental section supports this reasoning and is somewhat comprehensive with high quality and well-studied datasets. 

Clarity: The paper is mostly well-written and easy to follow, with certain exceptions are included in the Weaknesses sections. The claims of the authors about coverage of relatedness or similarity only in table 1 serves as a good benchmark and motivation for the work.

Significance: I consider this method to be an incremental addition on top of RAPTOR, The main metrics reported show significant improvement over the baseline methods that use only one signal.

### Weaknesses
- The paper is not very clear regarding how to merge the result from the two trees (similarity and relatedness trees), specifically how the retrieval scores from the two trees are combined or if a re-ranking is performed after the initial retrieval. The description of the merging process lacks sufficient detail, making it difficult to understand the exact mechanism by which the final set of candidates is selected.

- The metric "time per retrieval pool size" which is used to quantify the time of the SiReRAG vs other baselines method seems very contrived and not at all relevant, since it seems to say more about the number of candidates (the denominator) than about the time spent answering a query. Which means that the number of candidates generated by this method can be an order of magnitude more than the baseline methods in some cases, which can be prohibitive in many use-cases. The paper does not adequately address the computational cost associated with the increased pool size, which is a critical factor for practical applications.

- The main body of the paper has only two examples, without much detail: I recommend adding a full simple example for how the relatedness tree would look for a simple paragraph, as it's more difficult to visualize the entity-related tree as opposed to the similarity/summary between text chunks. The lack of detailed examples makes it challenging to grasp the practical implications and behavior of the relatedness tree construction and its integration with the similarity tree.

- The suggested method ends up performing badly on the more structured datasets (2Wiki): this indicates that the way it's encoding the relatedness is not representative enough to capture the structure of the graph/triples/facts. The method's failure on structured data highlights a limitation in its ability to effectively leverage relational information, suggesting that the current encoding approach may not be suitable for all types of knowledge sources.

### Questions
- The reasoning behind why HippoRAG does significantly better for 2Wiki dataset is not very clear in my opinion: I think what might be happening here is the following: when the RAPTOR text clustering pipeline is applied to the extracted entity-relatedness propositions, it treats the full propositions as text, completely ignoring the underlying structure of the proposition/fact (which is usually of the form Subject/Predicate/Object). That destroys certain information from the triple. My guess is that if we modify the RAPTOR encoder to encoder these features separately (e.g. with SPO markers tokens or with different encoders altogether), then we could see that we're able to encode the triple structure better, and we might be able to recover that difference.

- It would be very informative to share more information about the average number of candidates considered by the method compared to the baseline methods per query. This would show the computational increase compared to the baseline.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the retrieval component of the retrieval-augmented generation. It argues that existing RAG methods tend to focus exclusively on semantic similarity or relational links, leading to suboptimal performance in complex, multi-hop reasoning tasks. The paper motivates this with a coverage study to show that similarity or relatedness can only return a few correct entity connections, and the return results are half overlapped. The paper proposes SIRERAG, which is designed to optimize information retrieval by indexing data based on similarity and relatedness. The index is based on a similarity and relatedness tree using a a method similar to RAPTOR's.

Experiments with three datasets (MuSiQue, 2WikiMultiHopQA, and HotpotQA) showed improvements in EM and F1 scores compared to previous indexing methods, which include similarity or relatedness. The gain in performance had a slight negative impact on the inference time compared to a similarity-only method due to a larger retrieval pool size. Further analyses showed that the relatedness tree was indeed helpful.

### Strengths
1. The paper's main idea is well-motivated and supported by its preliminary experiments (Table 1). I found that its arguments were well-articulated and supported by existing literature, yet the hard evidence provided in Table 1 was a helpful addition.
2. The paper acknowledged an alternative approach in some steps and some results to reject the alternatives (Sections 4.1 and 4.3).
3. The method proposed in the paper consistently improved over three multi-hop reasoning datasets (Tables 4 and 6). In addition, ablation analysis also justified the need for the relatedness tree (Table 5).
4. The paper included an inference time experiment, showing that inference time increased with pool size.

### Weaknesses
1. Although not related directly to the paper, the paper should still acknowledge the state-of-the-art multi-hop reasoning method such as [Open-RAG](https://openragmoe.github.io/).
2. Section 4.3, which described an alternative method rather than the main method, did not explain flattened indexing well. Figure 2 showed an "+" sign but was not technical enough to confirm what was being done. Specifically, it's unclear how the nodes from different trees are combined and if there is any weighting or prioritization applied during the flattening process. The description lacks detail on how the unified retrieval pool is constructed from the similarity and relatedness trees.
3. A few prompts were not provided, such as the summary prompt (maybe similar to RAPTOR?), the topic extraction prompt (Section 3), and the hierarchy prompt (Section 4.1). The absence of these prompts makes it difficult to reproduce the results and understand the exact implementation details of the proposed method. The prompts are crucial for understanding the behavior of the system, especially in the summarization and hierarchical structure generation.
4. Some missing details of the baseline might be crucial to interpret the results (see Questions)

### Questions
1. It is unclear whether you re-ran the baseline or obtained the results from the original papers. I could not find the exact numbers reported elsewhere in Table 4.
2. What was the retrieval size of the baselines?
3. Overall, I found that TPRS was not meaningful. Wasn't it simply a result of whether the documents were short or long?

------
After the discussion, the score was raised from 6 to 8.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Indexing is critical for IR or RAG systems. In this paper, the authors propose a RAG indexing method which considers both semantic similarity and relatedness for better retrieval, named SIRERAG. Specifically, for similarity-based indexing this paper constructs a similarity tree via recursive summarization, and for relatedness this paper constructs a relatedness tree via entity and proposition extraction and grouping. Experimental results show some performance improvement on multi-hop QA datasets over previous similarity-based baselines and relatedness-based baselines.

### Strengths
In general, I think it is helpful to leverage multiple types of relevance for better retrieval results, and the experimental results also verify its effectiveness. It is also helpful to investigate and identify that similarity-only is not enough for complex QA tasks (although this is not a new discovery as many previous studies in traditional IR studies).

### Weaknesses
1. Because the similarity-based indexing component just follows RAPTOR (Sarthi et al., 2024), I think the main contribution of this paper maybe the relatedness-based indexing component.  Unfortunately, I found the relatedness-based indexing algorithm is ad hoc. Firstly, the relatedness are modeled using entity-specific propositions, which I think is over-specialized to multi-hop QA tasks(where the hop is just entity-entity associations and this is why the proposed method can achieve performance improvements). However, I think entity-specific propositions may not a good decision for many other complex reasoning tasks, and the authors should explain and verify the effectiveness and generality in more tasks. Secondly, I found there are many heuristic decisions, such as how to filter proportions, how to resolve entity references, etc.
2. The similarity and relatedness trees are constructed and used independently, which I think is  straightforward, it is important to consider the interaction between different relevance scores.
3. There are many multi-hop QA baselines, such as iterative RAG-based, agent-based, etc. The authors should compare them for more convincing experimental results.
4. The writings of this paper should be improved.

### Questions
1. The experimental results on other multi-hop reasoning tasks.
2. The performance using other relatedness-based trees (e.g., entity-based, or entity pair-based)

### Soundness
2

### Presentation
2

### Contribution
2
