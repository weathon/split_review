# A Soft and Fast Pattern Matcher for Billion-Scale Corpus Searches

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Researchers and practitioners in natural language processing and computational linguistics frequently observe and analyze the real language usage in large-scale corpora.
For that purpose, they often employ off-the-shelf pattern-matching tools, such as grep, and keyword-in-context concordancers, which is widely used in corpus linguistics for gathering examples.
Nonetheless, these existing techniques rely on surface-level string matching, and thus they suffer from the major limitation of not being able to handle orthographic variations and paraphrasing---notable and common phenomena in any natural language.
In addition, existing continuous approaches such as dense vector search tend to be overly coarse, often retrieving texts that are unrelated but share similar topics.
Given these challenges, we propose a novel algorithm that achieves soft (or semantic) yet efficient pattern matching by relaxing a surface-level matching with word embeddings.
Our algorithm is highly scalable with respect to the size of the corpus text utilizing inverted indexes.
We have prepared an efficient implementation, and we provide an accessible web tool.
Our experiments demonstrate that the proposed method
(i) can execute searches on billion-scale corpora in less than a second, which is comparable in speed to surface-level string matching and dense vector search;
(ii) can extract harmful instances that semantically match queries from a large set of English and Japanese Wikipedia articles;
and (iii) can be effectively applied to corpus-linguistic analyses of Latin, a language with highly diverse inflections.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Paper addresses the problem of soft (or semantic) pattern matching over a billion-scale text corpora. Exact matching is often too stringent; on the other hand, naive semantic matching based on computing similarities between word embeddings is much slower, since it requires a lot of floating point operations with high-dimensional vectors instead of fast bitwise comparisons. 

Authors leverage inverted indexes data structure to reduce the amount of required soft matches, and propose an algorithm which requires only a constant amount of soft matches with respect to corpura size. They also conduct two case studies: testing the speed of the proposed implementation on a billion-scale search, and retrieving patterns from a morphologically complex language (Latin). Finally, they provide a demo to interact with the proposed algorithm.

### Strengths
- Paper is very clearly written and easy to follow.

- Main algorithm is simple and straightforward Notably, it requires a constant amount of costly soft word comparisons (which can be ~1000 longer compared to hard comparisons) with respect to corpus size Meanwhile, it still allows for much more flexible matching.

- Provided demo works.

### Weaknesses
1. Description of dense vector search lacks details.
- e.g. in Line 415, what is a “training instance” — a sentence? A paragraph? It's unclear how the text is chunked before being fed into the model. The granularity of these chunks significantly impacts the quality of the embeddings and thus the search results.
- How the training instances and queries were formatted for the model? Does it follow the description at https://huggingface.co/intfloat/multilingual-e5-large? The specific formatting, including any prefixes or special tokens, is crucial for reproducing the results and understanding the model's behavior.
- What was the maximal length of training instances encoded by the model? If maximal length of a training instance is too long for the model, was it truncated or split into chunks? The handling of long sequences is a critical detail that affects both performance and memory usage. Truncation can lead to loss of context, while splitting introduces its own complexities.
- How token embeddings were pooled in a single chunks-level score? Averaging, max pooling, or other methods can lead to different results. The pooling method should be clearly specified.
- What were the HNSW hyperparameters? The performance of HNSW is highly sensitive to parameters like the number of neighbors, the construction parameters, and the search parameters. These should be specified for reproducibility.

2. Table 2 lacks details.
- How many search queries were done (e.g. 1, 100, 1000)? A single query is insufficient to characterize the performance of the system. Multiple queries are needed to obtain a reliable estimate of the average search time.
- How long the queries were (e.g. <20 words)? Query length can significantly impact search time, especially for soft matching. The distribution of query lengths should be reported.
- What are the variation in search time (standard deviation of search time over multiple queries, maximal / minimal search time for a single query)? Reporting only the average search time is not enough. The variability in search time is important to understand the robustness of the system.

3. Approximate string matching baselines were not included (e.g. agrep (Wu & Manber, 1992b;a) or TRE (https://en.wikipedia.org/wiki/TRE_(computing))). While unlike SoftMatcha they can not e.g. find synonyms, they are still useful for finding matches with typos / inflected word forms (which e.g. was part of the goal in “Section 4.3 Case study in computational linguistics — retrieving Latin examples), and it is interesting to compare search speed.
- In Section 2.3 String Matching, lines 200-202 you state that approximate string matching is orthogonal to your work as it focuses on surface-level comparison, while you target semantic-level similarity.
However, in Introduction, lines 076-080 you mention that “...it is often desirable to catch non-standard spellings as well, such as how r u instead of how are you … Additionally, it is desirable to catch different inflected word forms such as sing, sang, sung, signs and singing, which differ only in their morphological features and share the same lemma (base form).”

One big difficulty with assigning an overall score is the fact, that there are basically no metrics in the paper, except for running time. 
For approximate/fuzzy pattern matching algorithms it is interesting to estimate how relevant are the search results, using ranking metrics like mean average precision, or NDCG. However, these require a labeled dataset, which is hard to obtain.

On a qualitative level, this algorithm looks like a noticeable improvement over exact matching, and it might have some benefits compared to dense vector search (e.g. 100% recall in cases where the query exactly matches the pattern, higher speed, simpler implementation). Nonetheless, with more search results there arises a need to rank them. Considering Figure 3: while in some cases the ability to match “July 16, 2015” by the query “March 1, 2016” is useful, in others this might be a completely irrelevant search result.

### Questions
Major:
- There are some questions in Weaknesses section.
- How the sample search results were selected for Table 3?

Minor:
- How to choose alpha?
- How much more search results does SoftMatcha retrieve depending on alpha?
    - How many of additional entries are irrelevant?
    - How to rank additional entries found by Softmatcha?
- For potential future work: is it possible to modify the algorithm to allow flexible order of words in the query, or matching with some words omitted / inserted (e.g. finding “a fantastic jazz musician” by a query “the jazz musician”)? Fixed word order is still quite restrictive, especially for queries containing many words.

Suggestions:

- In footnote 5, page 8 information about Japanese as fifth language in Wikipedia by total amount of articles is outdated — Japanese is now 17th, while Chinese is 10th with almost twice as many total articles. Source: https://wikistats.wmcloud.org/display.php?t=wp. I propose to update the footnote.
- Lines 099-100: “0.1 seconds … without GPU” — I’d propose to add hardware specifications used for speed evaluations (156 cores and 226 Gib of main memory), to make the claim more concrete.

### Soundness
2

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
This paper presents an efficient method for pattern matching over billion-token corpus by combining soft matching via word embeddings and inverted indexes. The method is compared to exact matching and dense vector search as baselines over wikipedia corpora in English and Japanese. They show that the running time of the proposed algorithm is on par with the exact matching but much faster than dense vector search. Through qualitative case analysis, they also show that the algorithm returns relevant results and can be more robust than the other baselines.

### Strengths
The algorithm proposed is straightforward and effective, and it can be quite helpful for quickly locating relevant texts in massive pretraining data. The paper is also well-written and structured clearly, especially the demo interface.

### Weaknesses
The empirical evaluation can be further strengthened. It would be helpful to include analysis that shows 1) how the threshold influences speed and the relevance of the retrieved results. 2) a tradeoff analysis between the efficiency and the qualitative analysis. Table 3 seems to show that SoftMatcha retrieve relevant and robust texts fast. However I wonder if the observed relevancy can be quantified with a information retrieval corpora so that we can understand its relevant performance compared to the baselines.

### Questions
n/a

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
5

### Summary
This paper introduces a pattern-matching algorithm designed to efficiently handle semantic matching across vast text corpora, addressing the limitations of existing methods that struggle with language variations like orthographic diversity and paraphrasing. Unlike conventional string-based approaches, which lack flexibility, the proposed algorithm leverages word embeddings and inverted indexing to perform "soft" matching, enabling it to find meaningfully related phrases without relying on exact string matches. The algorithm operates at a speed comparable to traditional methods, achieving search times of under a second on billion-word corpora. It proves effective in practical applications: identifying harmful content in large English and Japanese datasets, and retrieving linguistically relevant examples in Latin, where morphological variations are common. SoftMatcha, the resulting tool, is accessible via a web interface, making it practical for users in NLP and digital humanities.

### Strengths
The algorithm is optimized for billion-scale corpora, achieving search speeds that are comparable to traditional tools but with a much richer, semantic matching capability. This scalability and speed are significant achievements, especially for applications involving extensive datasets like web-scale corpora.

The paper is well explained and the demo is functional and can be accessed easily. The examples in different languages give a good overview of the applicability potential of the algorithm.

### Weaknesses
An important limitation is the reliance on static embeddings, such as GloVe, which have largely been superseded by contextual embeddings in modern NLP applications. The continued use of GloVe and similar embeddings raises questions about the model's ability to capture context-dependent semantics, which are crucial in diverse language patterns and semantic matching tasks. The paper's illustrative example, where semantically "opposite" concepts (e.g., "lived" vs. "died") are matched, does not illustrate, in my opinion, the advantage of using this soft matching but instead it highlights a potential issue, which derives from the use of "classic" embeddings. "live" and "die" are used in similar contexts, which yields a high similarity according to the embedding spaces of word2vec or GloVe, but they are opposite semantically.

I also think that while the paper contains notable technical contributions, the primary focus on linguistic applications, corpus search, and retrieval, with an emphasis on efficiency, suggests that it may align more closely with the interests of venues like ACL rather than ICLR.

Since the algorithm operates solely on the vocabulary present in the corpus, there is limited discussion on its approach to out-of-vocabulary (OOV) items. This omission raises questions about how the system performs when faced with rare or unseen words and could impact its scalability across languages and domains with rich vocabularies or evolving terminologies.

### Questions
Since the algorithm operates solely on the vocabulary present in the corpus, there is limited discussion on its approach to out-of-vocabulary (OOV) items. This omission raises questions about how the system performs when faced with rare or unseen words and could impact its scalability across languages and domains with rich vocabularies or evolving terminologies.

So my question is: how the matching algorithm deals with OOV words? For instance, if "John" is not in the vocabulary, does it means I can't search for phrases containing "John"?

### Soundness
4

### Presentation
3

### Contribution
2
