# Wiki Entity Summarization Benchmark

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
\dm{Entity summarization aims to compute concise summaries for entities in knowledge graphs. 
Existing datasets and benchmarks are often limited to a few hundred entities and discard graph structure in source knowledge graphs. This limitation is particularly pronounced when it comes to ground-truth summaries, where there exist only a few labeled summaries for evaluation and training. 
 We propose \ourdataset (Wiki Entity Summarization Benchmark), a comprehensive \emph{benchmark} comprising of entities, their summaries, and their connections. Additionally, \ourdataset features a dataset \emph{generator} to test entity summarization algorithms in different areas of the knowledge graph. 
 Importantly, our approach combines graph algorithms and NLP models, as well as different data sources such that \ourdataset does not require human annotation, rendering the approach cost-effective and generalizable to multiple domains. Finally, \ourdataset is scalable and capable of capturing the complexities of knowledge graphs in terms of topology and semantics. %This benchmark is instrumental in advancing research in semantic data and knowledge graphs, particularly in managing large datasets. 
\ourdataset features existing \emph{datasets} for comparison. Empirical studies of entity summarization methods confirm the usefulness of our benchmark.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a benchmark dataset for Wiki entity summarization called WikES with the help of random walks.

### Strengths
--> The authors introduce a benchmark dataset for entity summarization over wikidata.

### Weaknesses
--> Why the automated mapping from Wikipedia to Wikidata allows for better summarization over entities as stated in "Wikidata to automatically map entities from Wikipedia to Wikidata. This automation allows us to efficiently generate summaries for any number of entities"
--> The motivation behind choosing these 4 algorithms for comparison is missing.
--> A thorough comparison with all the benchmark datasets given in the related work is missing. 
--> The main contribution on why this benchmark dataset is needed should be motivated more clearly.
--> The overall results in table two are very low, what would be the reason behind that?

### Questions
--> Why the automated mapping from Wikipedia to Wikidata allows for better summarization over entities as stated in "Wikidata to automatically map entities from Wikipedia to Wikidata. This automation allows us to efficiently generate summaries for any number of entities"
--> Why did authors only choose these algorithms for comparison?
--> Why these algorithms are not also tested on all the benchmark datasets which are given in the related work?

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
This paper introduces a new entity summarization(ES) benchmark, called WIKES, sourced from Wikidata and Wikipedia. Compared existing ES benchmarks, WIKES is generated automatically without relying on human labeling. WIKES also contains complex topology and semantics of the knowledge graph by including 2-hop connected sub-graphs  and diverse topics.

### Strengths
1. The new benchmark WIKES is the first ES benchmark that does not require human annotation. And the generation method could be easily applied to generate other ES datasets with diverse topics and scales. 
2. WIKES is the largest ES benchmark compared to existing benchmarks, which make it possible to explore the effectiveness of the ES methods over large scale datasets. 
3. Some results on the smallest datasets of WIKES  are presented, giving baseline results for further researches.

### Weaknesses
 1. Relying Wikipedia’s abstract to generate the ES datasets is cost-efficient and novel. But this makes the entity summarization generated based on the abstract  text rather than the triples of the entities in the knowledge graph. This might cause the entity summarization in WIKES not the gold entity summarization of the entities. 
 2. The DistillBERT is used to annotate the property that should be included in the summarization. The correctness of the final property is not evaluated, which is important to the quality of the WIKES in terms of entity summarization. 
 3. The datasets evaluation is not comprehensive. For example, 
    (1). Figure 3 only shows the F1 evaluation on WIkiProFem, part of the WIKES benchmark. The F1 score on other subdatasets are not presented. 
    (2). Table 2 shows that results of entity summarization methods on the smallest WIKES datasets. But the midium and the large WIKES datasets are not tested. It is not clear what would be the performance of current summarization methods on these two datasets. 
 4. The dataset quality are not analyzed, for example, the correctness and diversity that are important for ES benchmark. 
 5. Minor points and typos: 
   (1). In line 119, there is an extra question mark after “(version 3.9)”. 
   (2). The citation format in the main text seems not correct.

### Questions
1. Have you evaluated the correctness of property identification results based on the DistillBERT in terms of entity summarization? 
2. Why the left side of the Equation (2) equal to the right side? 
3. How would the minRW, maxRW, and minRW affect the random walk results for graphs in different scales? Especially how they would affect the quality of the entity summarization datasets? 
4. What is the meaning of Real-first and Real in the Figure 3? They are not explained in the main text.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduced a novel large-scale benchmark, named as WIKES, for entity summarization (ES) in knowledge graphs. Existing benchmarks are limited in size and often rely on expensive and time-consuming manual annotations. In contrast, WIKES aims to overcome these limitations by using Wikipedia abstracts and knowledge graph structures from Wikidata to automatically generate high-quality entity summaries without the need for manual annotators.
This paper proposed a dataset generation algorithm by combining graph algorithms with natural language processing models. The automatic processing makes the dataset be scalable and suitable for multiple domains.
Finally, this paper  offers a comprehensive evaluation of several entity summarization methods, including both unsupervised (e.g., PageRank, RELIN, LinkSum) and supervised models (e.g., GATES). It highlights that unsupervised methods, particularly graph-based approaches, often outperform supervised models in large-scale knowledge graphs.

### Strengths
S1: The WIKES benchmark is scalable, leveraging automatic summary generation from Wikipedia and Wikidata without relying on costly manual annotations, making it applicable to large datasets across various domains. The use of random walk-based subgraph extraction ensures that the structure of knowledge graphs is preserved, capturing both topological and semantic complexities of entities while maintaining computational efficiency.

S2: This paper provides a thorough evaluation of multiple graph-based entity summarization methods (e.g., PageRank, RELIN, GATES), allowing for direct comparison of unsupervised and supervised approaches, highlighting the advantages of graph-based methods.

S3: The overall presentation is good and the authors provided source code for review.

### Weaknesses
W1: The summarization methods are limited to graph-based summarization techniques. The authors may need to evaluate some text generation methods. A broader comparison with recent NLP-based summarization techniques could add more depth.

W2: The paper focuses on scalability but only evaluating the small version of their dataset. The methods without efficiency concerns could be used to conduct evaluation on the large version to show the effectiveness of the proposed dataset.

W3: The random walk-based graph expansion approach may not always capture the most semantically relevant information for all types of entities. While the two-hop neighborhood approach is computationally efficient, it may miss out on key relationships that are further away in the graph but still contextually important for the entity. The authors could have considered a dynamic approach, where the hop count is adjustable based on the entity or relationship type.

W4: The authors could provide some qualitative examples of the generated summaries of model like LinkSum in Appendix .

### Questions
Q1: In your paper, entity summarization is derived from Wikipedia abstracts and infoboxes, primarily using extraction-based methods. However, you did not explore any text generation or abstractive summarization models (such as GPT or T5) to create summaries from the knowledge graph or the Wikipedia text. Given the recent advancements in text generation, have you considered evaluating the performance of generative models for entity summarization, especially in cases where the structured data might be sparse or incomplete? What are the potential reasons for not including these methods in your benchmark?

Typos:
- Line 34, Entity summarization (ES) => Entity Summarization (ES)
- Line 119 “(version 3.9) ? and”
- Line 122 “INFO” may need to be bold.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a method to automatically create a dataset for evaluating entity summarization. Compared with existing datasets, with this new approach:
- larger datasets can be programmatically generated,
- mutli-hop (empirically 2-hop in the paper) relations are allowed,
- a connected subgraph is guaranteed to be sampled.

### Strengths
S1. A programmatically generatable benchmark for entity summarization. Can be larger and better than existing ones. It represents a useful contribution to the community. I like it.

S2. Generally reasonable approach to benchmark generation. The generated gold-standard summaries are likely to have high quality, despite lacking verification.

S3. Well-written paper. Very easy to read.

### Weaknesses
W1. Missing some important technical details and experiments related to the quality of the automatically generated gold-standard summaries.
- Line 175-176, how did you identify 'mentions' of Wikidata items in a Wikipedia page? If only relying on hyperlinks, recall could be low. Essentially it is an entity linking problem. I would like to see more details about its implementation. I also want to see a technical comparison of your approach with https://doi.org/10.1016/j.ipm.2013.12.001 which also relies on Wikipedia abstract to create gold-standard entity summaries.
- The above-mentioned entity linking, and your heuristic relation selection method, both can be inaccurate. Have you conducted experiments to evaluate the quality of your generated gold-standard summaries?
- Line 138-140, according to this problem definition, do you consider or ignore literals?

W2. While your sampled graphs can be arbitrarily large, it seems that your gold-standard summaries are limited in the following aspects.
- I am not sure whether generating a larger graph is really helpful for the entity summarization task. According to Table 1(b)(c)(d), while graphs differ in size, the number of gold-standard summaries remains almost unchanged, about 500 entities, if I understood correctly. You criticized existing benchmarks for their small size in terms of the number of entities with gold-standard summaries (e.g., 175 in ESBM), but your datasets are not significantly larger.
- All these ~500 entities are instances of person, while there are many other types of entities in DBpedia/Wikidata and in previous benchmarks like ESBM. Why did you limit your datasets to person entities? It introduces a bias.
- Only entities with English labels are considered. This is acceptable, but not necessary IMO.

### Questions
Apart from my questions in Weaknesses, I have the following further questions/comments.

Q1. For relation selection, you compared relation embedding with abstract embedding. The latter covers a very large piece of text. How about comparing with the embedding of the sentence where the relation value is mentioned?

Q2. Line 321-323, I did not understand why the bias comes from the small size and/or the incomplete edges of the sampled graphs. An extended explanation would be appreciated.

Q3. LinkSum performed best in your experiments. Is it possible that its good performance came from its use of Backlinks, which coincides with your approach to generating gold-standard summaries (based on entities mentioned in Wikipedia abstracts)? It may represent a bias of your ground truth.

### Soundness
3

### Presentation
4

### Contribution
3
