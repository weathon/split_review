# Relevance-Based Embeddings for Efficient Relevance Retrieval

- Decision: Reject
- Scores: 3, 5, 8, 5, 3

## Abstract
In many machine learning applications, the most relevant items for a particular query should be efficiently extracted. The relevance function is usually an expensive similarity model making the exhaustive search infeasible. A typical solution to this problem is to train another model that separately embeds queries and items to a vector space, where similarity is defined via the dot product or cosine similarity. This allows one to search the most relevant objects through fast approximate nearest neighbors search at the cost of some reduction in quality. To compensate for this reduction, the found candidates are re-ranked by the expensive similarity model. In this paper, we investigate an alternative approach that utilizes the relevances of the expensive model to make relevance-based embeddings (RBE). The idea is to describe each query (item) by its relevance for a set of support items (queries) and use these new representations to obtain query (item) embeddings. We theoretically prove that relevance-based embeddings are powerful enough to approximate any complex similarity model (under mild conditions). An important ingredient of RBE is the choice of support items. We investigate several strategies and demonstrate that significant improvements can be obtained compared to random choice. Our experiments on diverse datasets illustrate the power of relevance-based embeddings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors developed an algorithm which learns to embed queries using query relevance based on fixed set of randomly chosen set. In my opinion this area is well studied, and authors have missed whole genre of research on memory-based architectures.
- End-To-End Memory Networks, NIPS 2015.
- OAK: Enriching Document Representations using Auxiliary Knowledge for Extreme Classification, ICML 2024

### Strengths
I do not see any major contributions by this paper.

### Weaknesses
 Authors developed an algorithm which learns to embed queries using query relevance based on fixed set of randomly chosen set. In my opinion this area is well studied, and authors have missed whole genre of research on memory-based architectures.
- End-To-End Memory Networks, NIPS 2015.
- OAK: Enriching Document Representations using Auxiliary Knowledge for Extreme Classification, ICML 2024

### soundness:
 2

### presentation:
 3

### contribution:
 1

### strengths:
 I do not see any major contributions by this paper.

### weaknesses:
 Authors need to work on literature review, they have missed important area of work called memory networks, this area also relies on fixed set of vectors to augment query and generate query representation. This makes baselines and comparison incomplete.

### questions:
 Kindly compare with the memory network literature and its state of the art. Also compare with retrieval augmented retrieval approaches like OAK for comprehensive comparision.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
Kindly compare with the memory network literature and its state of the art. Also compare with retrieval augmented retrieval approaches like OAK for comprehensive comparision.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper analyzes and improves AnnCUR, which is a published method to obtain and use a cross-encoder for retrieval (not just for reranking but as the main retrieval model). AnnCUR obtains query embeddings for a query by using a randomly selected support set of items and computing the query's relevance with each of those items (by using a cross-encoder). The authors of this paper propose relevance-based embeddings (RBE) which improves upon AnnCUR by better selecting a specific support set of items and by adding trainable parameters.

### Strengths
The strengths are as follows:
- From the experiments it looks the proposed method always outperforms the baseline AnnCUR. 
- For selecting the support items, the authors tested many simple heuristics and a theoretically justified approach.

### Weaknesses
Here are some weaknesses:
- There is no timing information for how long it takes to run any of the method variants or the baselines. 
- It's not clear what the architecture of the lightweight neural networks for RBE is? How many parameters are in this neural network?
- The writing is not ver clear. Here are some specific issues:
  - It's not clear what the main difference between the result in Theorem 3.1 and Theorem 3.2 is.
  - It's not clear how the theory in the first part informs the method in the second part.
  - Lots of terms are undefined. What is $n$ on line 272? What is $\hat{R}$? Explicitly specify what $X$ and $K$ are in tables 4 and 5.  
  - The notation in section defining the metric HitRate(P,T) is also very hard to read.
- How does this method perform on other retrieval benchmarks like BEIR and NQ?

### Questions
Here are some questions:
- Will the RecSys and RecSys2 datasets be publicly released?
- Why is RBE so much better on Recsys2 when compared to any other dataset?
- The CUR approximation requires computing the matrix $R(I, Q_{train})$. This is very expensive. RBE doesn't need to compute this matrix, right? Does that mean RBE can scale to larger datasets?
- For the l2-greedy approach isn't it very expensive to optimize over all possible choices of $S_I$. How long does this take in practice?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors propose an improvement over AnnCUR, which matrix factorization is replaced with neural embeddings. Authors also prove that the proposed model family extends AnnCUR and can approximate any continuous function on the joint (compact topological) space of items and queries. Authors also provide an empirical study of how anchor items and queries should be chosen. A good variety of methods are explored: four reasonably strong heuristics as well as a more theoretically well-justified method. Authors experiment with a standard dataset used in the baseline (ZeShEL) as well as standard retrieval dataset (MS MARCO) and datasets from real-world production systems. Experimental results show that beyond certain budget, the proposed method outperforms dual encoder and a strong AnnCUR implementation.

### Strengths
Originality: Authors extend AnnCUR into neural embedding models. The extension of matrix factorization into neural embeddings has been extensively studied in the last 10 years and seen a good success, which makes the proposed approach well-motivated.

Quality: Authors make both theoretical and empirical contributions. With theoretical work, authors provide a universal approximation guarantee for AnnCUR, and then further proves a stronger result for the proposed RBE method. The proof is done at very abstract level (compact topological space of items and queries) and can be instantiated for a wide variety of settings. Authors also provide strong empirical evidences by 1) considering strong baseline methods on both anchor selection and embedding models, 2) experiment across diverse datasets, not only ZeShEL used in the previous work, but also MS MARCO as well as recommender tasks from production systems.

Significance: Author's extension of AnnCUR will open up wide possibilities, as the framework is generic and can accommodate arbitrary neural networks. Subsequent work may study further extend the work by studying variations of neural architecture choices.

Clarity: High-level implications of the theory are well-described, although some abstraction would benefit from more elaboration (see Weaknesses section). The proposed algorithmic framework is also well-motivated by discussing limitations of the AnnCUR baseline.

### Weaknesses
It is unclear how well the algorithm scales to larger number of items. Datasets used in experiments have relatively small number of items (at the scale of 10K) with the exception of Military and QA. Comparisons against baseline embedding algorithms are only done in RecSys datasets, which have small number of items. My concern is that as the number of items grows, the larger number of anchors should be chosen. This will in turn make the method less practical compared to simpler dual encoder methods. Even with only 10K-scale RecSys datasets, dual encoders outperform at 100 top items budget. Authors don't seem to be using knowledge distillation to further improve dual encoders, which is a standard technique; when knowledge distillation is used, the benefit of the proposed method would only show up for even larger compute budgets, which may not be practical in many applications. If the comparison between DE and RBE shall be run on datasets with larger number of items, this will strengthen the paper even if RBE doesn't outperform, because this informs readers when to use RBE and when not to. Even better, the scaling study of DE and RBE with respect to the number of items would provide an even stronger guideline for practitioners.

While I value that mathematical guarantees are proved at the quite abstract level, there are opportunities to improve the communication of the abstraction. More specifically, rather than simply saying $I$ and $Q$ are assumed to be compact topological spaces, it would be great to explain what does it mean that the space of queries and items are compact topological spaces. For example, interesting instantiations of the abstraction shall also be discussed, for example, popular Euclidean embeddings of $\mathbb{R}^d$ queries and items embeddings. Such elaborations will help practitioners to understand how they shall leverage the proposed abstract framework in their modeling efforts.

### Questions
In Line 166: Authors suggest CUR requires $O(M \cdot |Q_{train}|)$ calls to cross-encoder, but I believe it only requires $O(S_I \cdot |Q_{train}| +  S_Q \cdot M)$ calls because C and R matrices are randomly selected rows & columns? I can see $O(S_I \cdot |Q_{train}|)$  part can be reduced to $O(S_I \cdot N)$ in RBE, so I see there can be an improvement of efficiency, but it doesn't seem to be as drastic difference as authors argue.

Exactly in what sense is Theorem 3.2 stronger than Theorem 3.1: is it that $R$ is only expected to be continuous and $R^4$ doesn't need to be integrable anymore? Authors mention the guarantee is stronger, but doesn't explicitly mention in what sense it is stronger, hence it would be useful to elaborate.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores relevance-based embeddings (RBE), by utilizing the support items and support queries to construct relevance vectors upon which the embeddings are trained. This paper tries to provide rigorous proof to show that the functions $f_I$ and $f_Q$ (that are used to transform the relevance vectors) can be arbitrary under certain conditions. Building on the previous method of AnnCUR, this paper proposes some heuristics for selecting support items and queries. Experiments shows that the proposed approach can improve model performance compared to the dual encoder method.

### Strengths
1. A generalization of AnnCUR's approach to using support items has been introduced.  
2. Heuristics are provided to select support items. Their effectiveness has been validated by experimental results.  
3. Detailed explanation of the method and the experiments.

### Weaknesses
1. The motivation behind CUR decomposition is to enhance performance while maintaining the model's efficiency as much as possible. Therefore, providing the actual runtime of the relevant models in the experiments is essential. Currently, only some analysis is included. Specifically, the paper should report the wall-clock time for training and inference, not just the number of CE calls. The overhead of computing relevance vectors, even if done with a cheaper model, needs to be quantified in real time. This is crucial for understanding the practical applicability of the method.

2. Presentation: the method descriptions in Table 1 and separating the l2-greedy approach from other methods may lead to misunderstandings. The descriptions in Table 1 lack sufficient detail to fully understand the differences between the methods. For instance, the exact procedure for constructing the relevance vectors using different selection heuristics is not clearly defined. Separating the l2-greedy approach may suggest it is fundamentally different, when it is just a specific heuristic. This can confuse the reader.

3. Some experimental settings need to be explained more clearly. For example, why the AXN model was chosen? as well as how the dimensions in θI were set, etc. (though these functions are proven to be arbitrary). The choice of AXN needs more justification, especially if it is not a standard baseline. Also, while the functions are proven arbitrary, the practical choice of dimensions for θI can impact performance and should be discussed. The paper should also explain how these dimensions were chosen and if any hyperparameter tuning was performed.

### Questions
1. What are the time consumed by each model in Tables 3, 4, 5, and 6? The RBE method requires SI CE calls for each inference, which may represent a significant overhead compared to other methods.    
2. I am not quite understand the statement “DE uses |SI| more CE calls for the re-ranking” in line 470. Does the Dual Encoder actually use CE calls? Also, how many CE calls does AXNDE make? Why adding 100 items is considered a fair comparison? Will these additional 100 items be re-ranked using the cross-encoder model? If it's simply expanding the evaluation range, it seems that the choice of 100 as the number is not reasonable.   
3. Why does Table 1 use the QA.small dataset while Table 2 uses the QA dataset?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to distill an expensive neural model into multiple query-side and item-side embeddings, or "relevance embeddings", utilizing a retrieve-and-rerank setup. The author shows that the proposed neural similarity model have good approximation properties (when relying on universal approximation properties of the MLPs used in (2)).  The authors additionally conduct experiments showing how to improve embedding selection on top of a baseline selection strategy in (Morozov & Babenko, 2019; Yadav et al., 2022).

### Strengths
* Constructing relevance function and its approximations is an important topic and applicable to multiple areas like search, language modeling and recommendations.
* The authors demonstrate improvements vs support embedding selection strategies used in prior work, i.e., AnnCUR (Morozov & Babenko, 2019; Yadav et al., 2022).
* The experiments were conducted on diverse datasets in entity linkage, question answering, and recommendation systems.

### Weaknesses
W1. The concept of "relevance-based embedding" seems identical to the multi-embeddings/multi-vector line of research done in prior work (eg MIND, ColBERT, Multi-CLS BERT), which the submitted paper neither compared with or even cited.  Moreover, the paper's main conclusion reached in Section 3 seems identical to multiple recent work based on multi-embeddings. A few relevant examples include: 

* (RecSys) Li et al. Multi-Interest Network with Dynamic Routing for Recommendation at Tmall. 2019. Cen et al. Controllable Multi-Interest Framework for Recommendation. KDD'20. Ding et al. Efficient Retrieval with Learned Similarities. 2024.

* (NLP) Khattab et al. ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. SIGIR'20. Santhanam et al. ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction. NAACL'22. Chang et al. Multi-CLS BERT: An Efficient Alternative to Traditional Ensembling. ACL'23.  Dhulipala et al. MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings. 2024.

* The paper's main theoretical result in Section 3 - "in any relevance function can be well estimated using only such individual vectors" (based on multiple embeddings) is in principle similar to the conclusion reached by Ding et al. in Efficient Retrieval with Learned Similarities. 2024, which also proves that multi-embeddings can be used to approximate arbitrary relevance functions, albeit with different proof construction and a slightly different neural architecture. Additionally, Dhulipala et al. MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings. 2024 also shows for a widely used relevance function in COLBERT, a single very high-dimensional vector can be constructed to approximate the relevance function, and should also be discussed as related work.

W2. Evaluations in the paper are performed against non-standard and/or relatively weak baselines.
* ZESHEL (5 out of 9 scenarios reported) is not commonly used in relevance retrieval scenarios for either RecSys or NLP (see example papers above).
* RecSys (3 out of 9 scenarios reported) are a) based on proprietary, non-reproducible datasets, and b) the teacher model (gradient boosting model) is not considered state-of-the-art for recommendation systems.
    * Published recommendation literatures over the last 1-2 years have used cross encoders (acknowledged by authors in intro L47-48), deep stacked networks (eg Wang et al. HoME: Hierarchy of Multi-Gate Experts for Multi-Task Learning at Kuaishou. 2024), and/or generative approaches (eg Zhuo et al. Learning Optimal Tree Models Under Beam Search. ICML'20., Gao et al. Deep Retrieval: Learning A Retrievable Structure for Large-Scale Recommendations. 2020)
     * Additionally the experiment setup used goes against authors' own claim in abstract "... The relevance function is usually an expensive neural similarity model"
* QuestionAnswering (last 1 of the 9 scenarios) - the paper similarly failed to compare with recent state-of-the-art approaches on MS MACRO, including Cao et al. Autoregressive Entity Retrieval. ICLR'21. Ni et al. Sentence-T5: Scalable Sentence Encoders from Pre-trained Text-to-Text Models. ACL'22., Ni et al. Large Dual Encoders Are Generalizable Retrievers. EMNLP'22., Wang et al. Neural Corpus Indexer for Document Retrieval. NeurIPS'22., Sun et al. Learning to Tokenize for Generative Retrieval. NeurIPS'23. etc.). In fact, the baseline authors used is from 2019.

Overall, more solid experiments on standard datasets are needed to justify whether the baselines used are still relevant and to contextualize the contributions in this paper.

W3. Random choice is a weak baseline for multi-embeddings given most prior work in this area already utilize co-trained query- and item- vectors. See references in W1.

W4. To achieve universal approximation property of MLPs (used in Section 3), we need a very wide hidden layer. More experiments are needed to justify how to trade off quality vs efficiency of the proposed approach for retrieval in practical scenarios, against standard baselines.

### Questions
My main suggestion is to a) properly contextualize this work w.r.t. prior work on multi-embedding / multi-vector retrieval (W1), and b) conduct experiments against recent baselines on more commonly used benchmark datasets (W2) and in particular add efficiency experiments (W4). Happy to revise the score if a) and b) are addressed sufficiently.

### Soundness
2

### Presentation
1

### Contribution
2
