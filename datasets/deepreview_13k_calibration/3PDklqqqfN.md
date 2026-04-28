# Multi-Field Adaptive Retrieval

- Decision: Accept
- Avg Score: 7.17
- Scores: 5, 8, 8, 8, 8, 6

## Abstract
Document retrieval for tasks such as search and retrieval-augmented generation typically involves datasets that are \textit{unstructured}: free-form text without explicit internal structure in each document. However, documents can have a \textit{structured} form, consisting of fields such as an article title, message body, or HTML header. To address this gap, we introduce Multi-Field Adaptive Retrieval (\ours), a flexible framework that accommodates any number of and any type of document indices on \textit{structured} data. Our framework consists of two main steps: (1) the decomposition of an existing document into fields, each indexed independently through dense and lexical methods, and (2) learning a model which adaptively predicts the importance of a field by conditioning on the document query, allowing on-the-fly weighting of the most likely field(s). We find that our approach allows for the optimized use of dense versus lexical representations across field types, significantly improves in document ranking over a number of existing retrievers, and achieves state-of-the-art performance for multi-field structured data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper is concerned with the retrieval of documents which are multi-field, i.e, composed of multiple attributes such as title, authors and content. It proposes a method called MFAR which combines the use of different scoring methods, both lexical (word-based) and dense (embedding-based), for each field, allowing the model to adaptively predict the importance of each field for a given query. 

The authors conduct experiments on three datasets (product reviews, scientific papers and biomedical studies) that demonstrate that MFAR outperforms existing retrieval methods, achieving state-of-the-art results in structured data information retrieval. The study explores the benefits of the multi-field approach and the hybrid use of scoring methods to improve retrieval accuracy, showing that, instead of choosing between dense or lexical-based scorers alone, one can combine them in a hybrid fashion. An adaptive weighting technique is provided to combine those scores given a query.

### Strengths
The paper tackles a relevant problem, although the proposal has some limitations discussed below. The paper is well written and easy to understand. Originality is rather limited, since the semi-structured retrieval has been researched for a long time. The significance of the results is also limited because the approach is rather simple, and the experimental evaluation focuses on a recently published benchmark. The paper quality is good to its purposes, despite some adhoc design decisions.

### Weaknesses
It is not clear to me whether the fields may be considered indepent, so that the summation of the field-related scores suffices for determining the overall score. That is, it seems intuitive that there are correlations among the field instances and they may bias the result, as was extensively researched in the information retrieval area.

Another field-related issue is regarding the process of selecting the fields that will be considered in the whole process.

Overall, the proposal is simple and basically consists of combining scoring functions associated with fields, without considering their correlations and other characteristics that may either characterize the task or explain problems or failures. For instance, although the paper focuses on the information carried by the fields, it seems intuitive to mix the aggregated value of the fields with the remaining text, exploiting eventual information there. 

The experimental result also needs to be improved, as detailed next. First of all, the two experimental hypothesis seem to be too simple, thus quite easy to demonstrate. The advantages of using document structure are expected, in particular considering the additional information given to the models. The expected gains of hybrid approaches are also quite predictable. In both cases, it would be interesting to somehow derive upper bounds on the gains, so that the results go beyond benchmark-based evidence. 

On the other hand, it is also necessary to clear outline the limitations of such hybrid approaches and how they may be addressed. I really missed confidence intervals or similar statistical significance metrics on the results. For instance, on Table 2, the results may be too close and, despite the bold highlight, it is not clear how far the results are from the remaining of the baselines.

One terminology issue is regarding the difference between structured and semi-structured and where the paper fits. It seems to me that semi-structured is the proper jargon.

### Questions
Are the scoring dimensions really orthogonal, enabling summation as the summarization metric?

Aren´t there additional baselines and data sets that may be used in the experiments?

### Soundness
3

### Presentation
3

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
The paper presents a framework to improve document retrieval (Multi-Field Adaptive Retrieval, MFAR). Whereas document retrieval typically uses unstructured data for tasks such as retrieval augmented generation, MFAR is designed for structured data where documents have multiple fields (e.g., titles, abstracts, author information). MFAR first decomposes documents into individual fields and then learns a model that adaptively weights fields based on the input query. The framework uses both dense and lexical methods for retrieval, optimizing the combination of these representations per field to improve retrieval performance. Experimens show that MFAR outperforms previous retrieval models in complex document retrieval on the STaRK dataset.

### Strengths
Rereach on structured document retrieval is highly relevant, especially for RAG approaches. The retrieval is well designed, using a hybrid and adpative query scoring mechanism, using both dense and lexical methods as well as a ranking strategy. The evaluation is thorough, and the paper is well-structured and generally well-written.

### Weaknesses
The fine-tuning approach makes the approach specific to a set of fields from a dataset. Information overlap in fields (see lines 416-424) might intruduce some redundancy to the retrieval process.

### Questions
How much robust is the framework to variations in the number of fields, e.g., regarding field information overlap?

### Soundness
3

### Presentation
3

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
This paper exploits the structure in various IR corpora by learning query, corpus, field dependent weights across vector retrieval and token retrieval. The paper compares the methods to a number of strong baselines and analyzes a thorough set of ablation experiments to identify difference makers across different benchmarks. This paper is well written, easy to read and has a comprehensive set of references.

### Strengths
The paper is well motivated and well written. Many documents naturally have structure. Exploiting it should lead to better retrieval quality. However, doing so depends on the query, corpus and kind of retrieval. This paper comes up with an elegant and intuitive formulation to learn all of these weights during training. The baselines are well chosen, ablation experiments are extensive and the references are comprehensive.

### Weaknesses
The main weakness, and kudos to the authors for discussing this, is what they mention in Section 4 "Multi-field vs Single-field": "A side-by-side comparison of the single field models against their multi-field counterparts shows mixed results".  The difference in averages between mFAR_2 and mFAR_all doesn't appear statistically significant. The primary gains (looking at mFAR_2 vs mFAR_all) seem to be in the prime data set which has a lot of fields. Should the paper instead focus on adaptive hybrid retrieval, and choose hybrid retrieval baselines? It's unclear if the adaptive weighting of fields is truly beneficial, given the mixed results, or if the gains are primarily due to the hybrid approach itself. The lack of clear and consistent improvements across all datasets raises concerns about the general applicability of the multi-field approach. The paper should also address the computational overhead of training and inference with multiple fields, as this could be a limiting factor in practical applications. Furthermore, the paper does not explore the potential for negative transfer between fields, which could explain the mixed results.

### Questions
1. Are "Dense only" in Table 4 and "mFAR_dense" in Table 2 the same (the numbers are close but different). Were mFAR_dense and mFAR_lexical trained separately or trained together and one component ablated? 

2. See the weakness section, which I phrased as a question.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is a timely "revisit" of a multi-field retrieval problem with a proposal of multi-field adaptive retrieval that combines sparse-lexical and learned-dense-vector-similarity scores using field-weights, which are learnable and adaptive. Namely, each weight is a neural network incorporating a query representation and a field-specified learned weight vector.

The paper is very nicely written, it has a convincing set of results, as well as thorough literature review.

### Strengths
* The paper revisits an important problem.
* The paper is very well written
* Experimental results are convincing and have quite a few baselines.
* The method is simple and elegant yet effective

### Weaknesses
The only noticeable weakness is the need to compare to a better multi-field BM25 baseline, ideally, where field weights are learned using coordinate ascent (e.g., usling RankLib, or FastRank: https://github.com/jjfiv/fastrank). I do not think, however, that this should be a deal breaker. However, we encourage authors to list this as a limitation of their work.

### Questions
The following questions were fully answered/addressed by the authors:
1. What is exactly used for dense/vector retrieval?
2. How did you decide on selection of top-100 records for each field (L885)?
3. In Eq. 4, what is exactly q in G(q, f, m): I assume it should be a dense query encoder, but it's not clear from the text (at least for me).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Multi-Field Adaptive Retrieval (MFAR), a framework for retrieving structured documents by dynamically weighting document fields based on query relevance. By combining lexical and dense retrieval methods, MFAR improves retrieval accuracy on the STaRK dataset, surpassing state-of-the-art baselines and highlighting the potential of adaptive, hybrid approaches for structured data retrieval.

### Strengths
1. The paper proposes a new approach that incorporates structured document retrieval, where documents contain multi-field information. The proposed method adaptively controls the information by using a weight adjustment strategy based on the query. 
2. The experimental results demonstrate that mFAR framework over various baselines on the STaRK dataset. 
3. The authors present detailed analysis demonstrating why their hybrid approach can outperform baselines through the experiments of both multi-field vs. single-field and hybrid vs. lexical/semantic similarity. 
4. The paper is well-structured, motivated, and written, thus easy to follow.

### Weaknesses
1. Though several recent retrievers [1] and [2] have been proposed, Contriever is used as a representative of dense retrievers without sufficient discussion. I am concerned that the conclusion may change if the authors use the recent retrievers. Especially, since FollowIR is instruction-tuned, it may be more robust against negation in the query, which the authors pointed out as a possible issue of the single-field method. The choice of Contriever, while a reasonable baseline, lacks justification against more recent and potentially more robust models, particularly those designed with instruction-following capabilities that could mitigate issues like negation sensitivity. This raises concerns about the generalizability of the findings.
2. The adaptive weighting mechanism in MFAR relies on training within specific domains and structured datasets, making it potentially sensitive to domain-specific data characteristics. This might lead to suboptimal field selection or scoring when the document structure is inconsistent across the corpus. The reliance on a fixed set of fields and their associated weights, learned from a specific training set, could limit the model's ability to generalize to new datasets with different field structures or even variations within the same domain. This lack of adaptability to structural inconsistencies is a potential limitation.

### Questions
Regarding Weakness 1 in the previous section, did you try to use other dense retrievers and do you have any insights about experiments with better retrievers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a method called Multi-Field Adaptive Retrieval (MFAR), aimed at enhancing retrieval of structured or multi-field documents. The approach decomposes each document into multiple fields, each independently indexed and retrievable through different models. Each field is associated with a learnable embedding, and an adaptive function is trained to predict the importance of each field based on the query and scoring model. The authors validate MFAR's effectiveness through experiments across multiple datasets, comparing it against prior methods.

### Strengths
- S1: This study is the first to demonstrate that multi-field ranking outperforms single-field ranking within the context of dense retrieval. 
- S2: The experiments highlight that hybrid models enhance both single- and multi-field rankings, with certain multi-field scenarios benefitting more from hybrid approaches.
- S3: A thorough ablation study demonstrates the significance of the query-conditioning mechanism in optimizing field weights. Additionally, the qualitative analysis shows the variability in optimal scorers across datasets, showing that there is no universally best approach.
- S4: A detailed case study further illustrates the method’s effectiveness in practical applications.

### Weaknesses
 - W1: Although the paper focuses on multi-field ranking, it does not include classic methods such as BM25F [1], its later extensions [2,3], or the mixture of language models [5], which are commonly applied in table retrieval [6], as part of the baselines. Incorporating at least BM25F or the mixture of language models would add valuable context and enable a more thorough comparison. Specifically, the absence of BM25F, a standard method for multi-field retrieval, makes it difficult to assess the novelty and practical advantages of the proposed approach. The paper should include a comparison with BM25F using optimized field weights, as a naive uniform weighting strategy is not representative of BM25F's potential.
- W2: Query-dependent field weighting has been previously explored, such as in table retrieval methods that incorporate both query-dependent and query-independent features [4]. Testing on table retrieval datasets could offer additional insights, as tables represent another structured, multi-field document type. The current evaluation is limited to datasets that may not fully capture the complexities of multi-field retrieval, particularly in scenarios where field importance varies significantly across queries. Evaluating on table retrieval datasets, which inherently have a structured multi-field nature, would provide a more robust assessment of the method's generalizability.
- W3: The proposed method adaptively determines the importance of each field given a query and scorer; however, it does not select among scorers, instead requiring calculation of all scoring potentials, thereby increasing computational load. This approach, while flexible, introduces unnecessary computational overhead, as it calculates scores for all fields and scorers even when some may be irrelevant for a given query. A mechanism to prune or select relevant scorers would enhance the method's efficiency.

### Questions
n/a

### Soundness
2

### Presentation
3

### Contribution
2
