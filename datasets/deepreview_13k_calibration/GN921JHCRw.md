# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Retrieval-augmented language models can better adapt to changes in world state and incorporate long-tail knowledge.  However, most existing methods retrieve only short contiguous chunks from a retrieval corpus, limiting holistic understanding of the overall document context. We introduce the novel approach of recursively embedding, clustering, and summarizing chunks of text, constructing a tree with differing levels of summarization from the bottom up. At inference time, our RAPTOR model retrieves from this tree, integrating information across lengthy documents at different levels of abstraction. Controlled experiments show that retrieval with recursive summaries offers significant improvements over traditional retrieval-augmented LMs on several tasks. On question-answering tasks that involve complex, multi-step reasoning, we show state-of-the-art results; for example, by coupling RAPTOR retrieval with the use of GPT-4, we can improve the best performance on the QuALITY benchmark by 20\% in absolute accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an approach to generate recursive summaries for closed-book QA tasks such as NarrativeQA, Qasper, and Quality. The summaries compress multiple documents, which are clustered according to GMM. Then, at test time, the summaries and original passages are retrieved from to perform the task in a RAG-like fashion.

### Strengths
1. Strong results compared to multiple baselines, but some choice of baselines are poorly justified and claims of SOTA are not correct.

2. An interesting approach to generate a set of summaries to retrieve from. The nature of the summaries is probably the main value here, especially given that the tree structure of the summaries are mostly ignored. Further, despite other complains for easy scalability, probably this approach will not immediately scale for larger retrieval datasets. Perhaps the focus should be for closed book QA.

3. Results reported on three datasets of varying domains using both closed and open source LMs.

### Weaknesses
1. There is very little analysis of the summarized outputs. The analysis included in the main text, Table 6, is difficult to understand and does not reveal much about the content of the summaries. Based on an in-line example, it seems the benefit of this approach may be the abstractive nature of the summaries, and it would be helpful to verify further whether this is the case or some other property is helping.

2a. The baselines in table 1 and 2 are not well justified. It seems like BM25 and DPR do not use the tree structure, also, SBERT can be applied without tree structure.

2b. There are multiple claims of state of the art that are not accurate. In zeroscrolls, flan-ul2 is reported to get 56.9F1 on Qasper. GPT-4 gets 89.2 on Quality in the same paper.

3. The paper is hard to read at times. Details about beam search are confusing (e.g. do we return all the visited docs, or a single sequence of them?).

### Questions
Q1: Did you consider using a hierarchical clustering algorithm like agglomerative clustering?

Q2: Why use GMM? In practice, do you assign passages/summaries to more than one cluster?

Q3: Is 4 percent hallucination considered standard? What amount of hallucination have other LLM-based summarization systems experienced?

Q4: Is the example for hallucination in the appendix the full length? I am surprised to see the summary and child node are almost the same size.

Q5: Is the cumulative cosine score used to select the next top-k nodes in beam search approach? If not, then perhaps it makes sense to rename this---the approach does not seem very beam search like.

Q6: When using beam search, will there always be k * d nodes kept? Or is it only d nodes, where you choose the sequence of nodes with the highest cumulative score?

Q7: Why did you need to create your own story? Can you share more details about how the 2600 word story is created?

Q8: Can you provide more details about the difference between collapsed and beam in Figure 3? Does collapsed tend to choose more summaries than beam? Why is top-3 not centered over the 1000 x-ticker? How should we interpret the context length x-axis wrt beam?

Presentation

When referencing the appendix, perhaps specify where in the appendix (i.e. which appendix section).

It is deceptive and not clear to describe RAPTOR as scaling linearly. The actual complexity is closer to O(n * k) where N is the number of tokens and k is the number of layers. It only appears linear because you are using a small k. I suggest to refine the writing to mention it "scales linearly in practice" or something along those lines.

Can make it more clear whether using dev or test data. Also, if using dev data to claim state-of-the-art, then perhaps provide some clarification why test is not being used.

Related Work

Sun et al 2021. Do Long-Range Language Models Actually Use Long-Range Context?---This work pre-dates Liu et al and effectively shows transformers do not handle large contexts effectively.

Since your approach is meant to make up for shortcomings of chunked passages, then you may be interested in "decontextualization". For example, see: https://arxiv.org/abs/2305.14772

Gao et al 2023. Enabling Large Language Models to Generate Text with Citations---This recent work uses summaries in retrieval augmented generation.

Min et al 2021. Joint Passage Ranking for Diverse Multi-Answer Retrieval---This work does tree-based retrieval for open-domain QA.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method called RAPTOR that retrieves chunks and summaries from tree-structured automatically created clusters based on the representation of SBERT. Since the clusters have a hierarchy, RAPTOR can consider high-level and low-level details of texts. To deal with the variable depth of the hierarchy, the cluster size is automatically decided by Gaussian Mixture with Bayesian Information Criterion (BIC) like x-means. The authors summarize each cluster by GPT-3.5-turbo from its elements, chunks, or summaries. When retrieving these chunks and summaries, the authors use two different methods. The first method, beam search, conducts a layer-wise traversal of the clusters beginning at the root nodes. The second method, collapsed tree, considers all nodes in the tree simultaneously. Experimental results show that RAPTOR improves the performance in various QA datasets.

### Strengths
- The proposed method RAPTOR can indirectly retrieve long texts by tracking tree-structured automatically created clusters.
- RAPTOR can decide the number of clusters automatically, and thus, it doesn't require manual tuning for creating the tree-structured clusters.
- RAPTOR can achieve better performances in QA compared with commonly used retrievers.

### Weaknesses
 - Considering the information loss by summarization, the benefit of RAPTOR against enumerating possible concatenation of chunks is uncertain.
- Even if clustering is automatically done, how to segment texts into chunks is still left as a problem.
- When comparing model performances, the parameter sizes of models should be the same or similar. However, the paper compares models with totally different parameters. This is problematic from the viewpoint of fairness.
- How many retrieved instances are used for baseline models needs to be described in detail. Thus, judging the fairness of the comparison in the experiment is difficult.

### Questions
- How did you segment texts into chunks? If you use obvious segments in text like paragraphs, please state it clearly.
- How did you generate summaries by GPT-3.5-turbo? You should show the actually used prompt.
- What kind of embedding did you use for retrieving chunks and clusters? Did you use the centroids for each cluster or embedding of the summaries? Also, are these calculated by SBERT similar to the clustering step?
- This is related to the above weakness part. How many retrieved instances are used for baseline models?
- In the part, "Comparison to State-of-the-art Systems", you compared your RAPTOR with GPT-4 to LongT5 that has 3B of parameters and its variant, ColtT5. Considering that the detailed parameter size of GPT-4 is not released and the size of the baselines' parameters, this comparison is not fair. Did you adopt RAPTOR to LongT5 or ColtT5?
- Similar to the previous question, in Table 5, you should have adopted RAPTOR to the model with almost the same parameter size as that of baselines.

I can update my score based on your response.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new information retrieval mechanism for retrieval augmented generation (RAG). Traditionally, retrieval in RAG is done rather flatly by indexing text-chunks and then retrieving top-k. In the new approach, the authors create a hierarchical encoding. They do this by: 

1. Encoding original text-chunks. 
2. Clustering the (encoding,text-chunk) pairs. 
3. Summarizing the clustered text-chunks into a single text-chunk.
4. Encoding the summary text-chunks to get new (encoding,text-chunk) pairs .
5. Going to step 2 and repeating the process until the root encoding is created.  

They also propose two ways to query/retrieve from the hierarchical encoding - one method involving plain top-k retrieval from flattened tree, and another method starts from the root encoding and explores the tree of encodings via beam search. In both cases, information at various levels of granularity can be retrieved.

### Strengths
1. Overall an elegant, well-motivated, and seemingly novel (to my knowledge) approach. It can set up a new paradigm baseline for RAG that can incite future research on refining the general idea.

2. Decent performance compared to other paradigmatic approaches for retrieval such as DPR.

### Weaknesses
1. One limitation seems to be that the approach requires recursive summarization with an LLM which can add to computational expense (could be also good to share the trade-off).


2. While I get the theoretical intuition of clustering (to prevent information loss, by clustering more homogenous content for summarization), it would have been nice to have an empirical demonstration of the effectiveness of clustering. A possible ablation could be: what if we took a balanced tree-style encoding/summarization and simply recursively encoded contiguous chunks (instead of clustering)?


3. There is some precedence for using hierarchical retrieval (even though there are crucial differences) [1,2] that could be cited and discussed for better contextualization in the literature.

### Questions
1. It could be good to add a pseudo-code for beam tree-based retrieval and collapsed-tree-based retrieval. 
2. The 20% accuracy boost claim (while technically correct) may be a bit misleading given prior works do not use GPT4 (if I understand correctly). So most of the boost most likely comes from GPT4 rather than RAPTOR.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the context of reML, this paper proposes to extend the support documents by generating summaries at different level of granularity (full document to the original text). Summaries are based on a clustered set of chunks of text within a UMAP representation space (which is the novelty in this paper), and the process is recursive. This new set of passages is used as a new dataset, with two strategies for searching: either considering each passage independently, or using a hierarchy to bias the search. The latter strategy is working much worse, and hence the authors focus on the first. The model perform experiments with this strategy, using GPT-3.5/4 to generate the final answer, and comparing to other summarization-based approaches on NarrativeQA, Qasper and QuALITY - and improve the results on the three datasets (especially QuALITY).

### Strengths
While the model novelty is low -- instead of using contiguous segments for summarization, the authors propose to segments cluster by similarity -- this simple idea improves results on three different datasets. The different experiments conducted show that the hierarchy is only useful because it produces summaries at different granularity levels (but it does not help in searching for the right passages).

### Weaknesses
It would be good to see the performance using open-domain pre-trained models (e.g. LLAMA or other ones), to ensure a more reproducible research.

There is no experiment on the impact of the clustering algorithm (what is the difference when not using UMAP? when using more or less neighbors?). Specifically, how does the choice of clustering algorithm affect the hierarchical structure and subsequent retrieval performance? Exploring this aspect could provide valuable insights into the robustness and generalizability of the proposed method.

### Questions
- Please give examples of generated summaries.

- It would be great to have some insight on the impact of the clustering algorithm, and how the performance degrades with summary quality

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
