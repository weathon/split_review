# Embedding-Converter: A Unified Framework for Cross-Model Embedding Transformation

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 5, 3

## Abstract
Embeddings, numerical representations of data like text and images, are fundamental to machine learning. However, the continuous emergence of new embedding models poses a challenge: migrating to these potentially superior models often requires computationally expensive re-embedding of entire datasets even without guarantees of improvement. This paper introduces Embedding-Converter, a unified framework and a novel paradigm for efficiently converting embeddings between different models, eliminating the need for costly re-embedding. In real-world scenarios, the proposed method yields O(100) times faster and cheaper computation of embeddings with new models. Our experiments demonstrate that Embedding-Converter not only facilitates seamless transitions to new models but can even surpass the source model's performance, approaching that of the target model. This enables efficient evaluation of new embedding models and promotes wider adoption by reducing the overhead associated with model switching. Moreover, Embedding-Converter addresses latency constraints by enabling the use of smaller models for online tasks while leveraging larger models for offline processing. By encouraging users to release converters alongside new embedding models, Embedding-Converter fosters a more dynamic and user-friendly paradigm for embedding model development and deployment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors focus on a specific use case of using embeddings generated from a pretrained LLM and transfer them to different target LLM. Typically, doing this would need reembedding the entire corpus using the target model. This paper present a way to eschew this re-embedding process by introducing a small converter (another Neural network) to learn mappings from the source model embedding space to the target model’s embedding space. Re-training on large internet-scale datasets requires an extensive amount of compute resources and time, and for production-scale systems that need to regularly update their models to SOTA. This can be an expensive process from both an effort and cost standpoint. The authors introduce an intermediate network (referred to as a converter in the manuscript) to learn the mapping between the embedding spaces of the models. They train this network by optimizing for similar pair-wise distances between points in their respective embedding spaces.

### Strengths
* The use case the paper tackles is interesting and relevant in the context of the growing use of pre-trained LLMs. The solution proposed is simple to understand and implement.

* The authors try to make their contributions to the setup quite generic and extensible to various models in the wild.

* The computation speedups achieved over the baselines are substantial, making this use case and strategy worth exploring.

### Weaknesses
 * Even though the solution proposed does not require to re embedding with the target models, it still requires training a converter (and subsequently evaluating it/ performing hyperparameter searches) every time a new target model is introduced. In most practical scenarios, the datasets change across time just as much if not more than the embedding models. Changes to the dataset would need re-embedding and thus the proposed solution might have lower utility.

* Relevance of Relative Scores : It is not clear if the performance gains using the converter are actually reflective of the target model embeddings being better than the source model. For instance, in both in-domain and out-of-domain experiments presented, there are datasets for which the target embedding performance is better than the source embedding performance, however the converter embeddings have an even worse performance (for instance see DBPedia openaismall -> gecko004 in  Table 1), not indicative of the fact that the target embeddings are actually better than the source. This raises questions on how well do the converted embeddings reflect the relative performance of the source and target models - “It offers a preliminary performance guarantee when migrating to a new embedding model” - Sec 4.4. Furthermore, there are very few experiments where the retrieval performance of the source model embeddings is superior to that of the target (perhaps due to reasons mentioned in the next point), making it more difficult to assess the validity of the aforementioned claim.

* Fair Baseline Comparisons? Performance is measured using query embeddings generated using the target model across all scenarios - “queries are consistently encoded using the target model across all conditions” - Sec 4.2. This does not sound like a fair comparison to me - using target model query embeddings to evaluate the source model performance which uses a different embedding scheme altogether.
For  2 in-domain datasets, retrieval performance of the converter-embeddings is even better than the target embedding performance. Some explanation or insights into this behavior would be interesting perhaps.

* Potential Bias : Model selection and hyperparameter tuning was done based on retrieval performance rather than something related to the criterion which the converter was trained to maximize. Some details on how the validation set was constructed would be helpful here.

* No confidence intervals reported - (can use multiple seeds to initialize the converter model weights or use bootstrapping and provide error bars).

* Additional hyperparameter details like values of alpha and beta for some source-target model pairs could have provided additional insights to the reader.

* Not clear if the global loss in Eqn 2 is applied to all NC2 pairs in the training set,

### Questions
* A fairer comparison to baseline models? 

* It would be informative to report error bars to note significance of results obtained, either a theoretical justification or at least a more thorough empirical evaluation of relative scores to establish their validity - for instance including more scenarios where the source model has a better performance than the target model and showing the claim on relative scores still holds.

### Soundness
2

### Presentation
3

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
This paper proposes to translate the text embeddings of different embedding models, such as gecko003 of Google to openai-3-small. To facilitate training of such a translator, the authors propose a few loss functions: 1. regression loss to force the translated source embedding to be close to the target embedding, 2. global similarity loss, to retain the similarities of the source space in the translated space, 3. local similarity loss, which is similar to global similarity loss, but is done in a neighborhood of a selected piece of text t. The authors verified that the translated embeddings usually perform better than source embeddings, but slightly worse than target embeddings.

### Strengths
1. This work explores an interesting direction of pursuing compatibility between different embedding models. Although cross-embedder retrieval itself is not so strongly motivating, I believe it's important to have such embedding translators that bridge different models.
2. The 3 loss functions proposed seem to be reasonable.

### Weaknesses
My major concerns are 1) a few important details are missing, and 2) issues on experiments:
1. Some important technical details are missing. For example, in the global and local similarity losses, what is the Dist() used? Is this cosine?
2. How to get the k-nearest neighbors of a text piece t, $NN_k(t)$? Do we need to iterate the corpus and find similar embeddings? Could we simply perturb the embeddings of t to get its neighbors?
3. What are the number of parameters of the embedding converter?

Experimental issues:

4. Different embedding models should have drastically different topological structures of embedding spaces. Therefore, it would pose a severe challenge for such embedding translators. Although the authors have evaluated in experiments that Embedding-Converter performs well between source and target embedders, the evaluated embedding models are basically only 2 types: gecko (003 and 004, which I presume should be topologically homogeneous to each other) and openai-3-small. It's more convincing if more embedding models are evaluated to show that the architecture of Embedding-Converter is valid for other challenging pairs of embedders.
5. The reported retrieval performance of openai-3-small seems to be lower than reported in [a]. In Fig. 8(b) of [a], openai-3-small seems to score around 0.537 (no numerical values are reported, but on the chart it's well centered between 0.525 and 0.55), however Table 1 of this paper reports 0.5209. 
6. Matryoshka-Adaptor [a] is not compared as a baseline, which is quite relevant. EDIT: I noticed that due to the review policy, arxiv papers released after 1st July don't have to be compared. However, if authors could make such comparisons, it would be a strong boost to the convincingness of this paper.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces the concept of an embedding converter: a model that transforms the embedding space between two embedding models. The motivation stems from the existence and continual development of multiple embedding models that produce incompatible embeddings. This often necessitates re-running a new embedding model (re-indexing) on all data after a model update, which can be costly. With the proposed Embedding Converter—a lightweight model—an already indexed dataset can be inexpensively transformed to be compatible with a target model’s embeddings. This approach can also facilitate deploying two models (a large model to index the corpus, and a lightweight model + embedding converter for real-time querying). Empirical results demonstrate the effectiveness of the proposed method for both in-domain and out-of-domain data across various model update scenarios.

### Strengths
- The paper is well-written and mostly easy to follow.
- The motivation and setup are reasonable and valuable, particularly for practitioners dealing with embedding models and large-scale retrieval systems.
- Empirical results demonstrate the efficacy of the proposed method on different datasets, tasks, and model update scenarios.
- The use case for latency reduction (using a light model + embedding converter) is a practical and useful proposal.

### Weaknesses
 - While the motivation, method, and experimental setup in the paper are sound, the paper unfortunately overlooks an important and relevant domain of related work: model compatibility. The exact motivation, problem setup, and solution discussed in the paper have been the focus of model compatibility studies (e.g., see [1-4]). In particular, both [3] and [4] propose learning a simple MLP-based transformation function from the embedding space of a source model to that of a target model, and they address additional aspects (e.g., the availability of extra information, the potential for partial reindexing of the corpus with the new model) that are not covered in this work. All relevant model compatibility literature, including the mentioned studies, is absent from the current manuscript and should be discussed. The contribution of the proposed method, compared to the existing works cited above, is limited to addressing new domains/tasks.

- Section 3.2 (Loss functions):
  - For the relation-based losses, such as $L_{global}$ in equation (2), do we consider all pairs $(t_1, t_2)$ in the training dataset? Since the number of pairs scales quadratically, this approach is computationally expensive. Further clarification on this point—specifically, whether pairs are formed only within a batch (and, if so, the effect of batch size)—should be discussed.
  - In the analysis of loss functions, relevant works from the knowledge distillation literature should be reviewed. For instance, [5] proposes losses to capture relations between features, similar to what is proposed in this paper.

- One missing empirical analysis for the proposed method, also discussed in model compatibility literature, is the setup with multiple updates. All results provided in the paper consider a single update from source to target. The performance of the embedding converter should be discussed in scenarios with a chain of updates: $v1 \rightarrow v2 \rightarrow v3 \rightarrow v4 \rightarrow \dots$ .

### Questions
- Lines 276-277: It is stated that “queries are consistently encoded using the target model (gecko004) across all conditions.” Is this true for all columns in Table 1? For example, when the corpus is indexed by the gecko003 model, can the query be encoded by gecko004 (as in the column in Table 1 with 0.5067 average performance)? Since the embeddings of these models are not comparable, clarification is needed.
- In Table 5: What is the definition of global/local distance? Are these essentially average values of the loss functions defined in equations (2) and (3)? It might be helpful to indicate in the table that “lower is better.”
- In Table 5: What does “baseline” refer to? Is it the use of an identity embedding converter?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This paper introduces a unified framework called "Embedding-Converter" aimed at efficiently converting embeddings between different models, addressing the high cost associated with re-computing entire dataset embeddings when switching or upgrading models. The main contributions include:

Framework Design: The Embedding-Converter acts as a "translator for embedding spaces," enabling seamless conversion of embeddings between various models, thus eliminating the need to regenerate embeddings. This allows for quick and low-cost model switching or version upgrades and is applicable to different types of data across tasks and domains.

Performance Validation: Through experiments, Embedding-Converter achieves performance close to the target model on large datasets and, in some tasks, even surpasses the source model's performance. The method saves over 100 times in computational cost and time compared to traditional methods, highlighting its potential in model migration.

Multi-Task Extension: Embedding-Converter is not only suitable for retrieval tasks but also performs well in other tasks like text classification and semantic similarity, demonstrating its broad applicability.

Efficiency and Flexibility: This framework supports efficient vector transformation in high-dimensional spaces, preserving local and global structures among embeddings, enabling a smooth transition during model migration.

### Strengths
Reduction in Cost and Time for Model Migration: Traditional methods require re-embedding entire datasets when switching embedding models, which is costly and time-consuming, especially for large datasets. Embedding-Converter allows efficient conversion of embeddings between models, eliminating the need for re-embedding and reducing the cost and time of model migration by over 100 times. This efficiency is crucial for applications requiring frequent model updates.

Support for Cross-Model and Cross-Version Conversion: This framework can convert embeddings not only between different versions of the same model (e.g., Google’s Gecko003 to Gecko004) but also between entirely different models (e.g., from an OpenAI model to a Google model). This flexibility enables users to switch to the best-performing model for their task without re-computation.

High-Quality Embedding Conversion: Experiments show that Embedding-Converter generates converted embeddings that perform close to or even better than the source model on multiple downstream tasks, while also maintaining target model performance. By leveraging various loss functions, such as global and local similarity losses, the framework ensures that the converted embeddings structurally align well with the target model.

Broad Applicability Across Tasks: Besides retrieval tasks, the framework also excels in text classification and semantic similarity tasks, demonstrating its versatility. This suggests that Embedding-Converter can adapt to various data types and tasks, with the potential for cross-domain applications.

Reduced Latency and Improved Real-Time Performance: Embedding-Converter can convert query embeddings in low-latency scenarios, allowing users to employ larger models for dataset embeddings and smaller models for real-time queries, significantly improving both the speed and accuracy of real-time tasks.

### Weaknesses
I am not familiar with this direction.

### Questions
N/A

I will see the comments of other reviewers.

### Soundness
2

### Presentation
2

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
The paper addresses a practical industrial problem - how to quickly determine if a new embedding model is better when we have an existing pipeline built on a specific embedding model.
The paper proposes a straightforward approach - training a converter between embedding spaces and observing the effects in the pipeline.

### Strengths
The paper raises a valuable question with significant industrial relevance.

### Weaknesses
 * The paper's approach is rather direct and simple, lacking deeper analysis of the problem. For instance, it doesn't explore whether mapping from higher to lower dimensional embeddings is equivalent to mapping from lower to higher dimensions. Furthermore, the method does not consider the potential information loss or distortion that may occur during the conversion process, particularly when dealing with significant dimensionality changes. The paper also does not investigate the impact of different conversion architectures (e.g., linear vs. non-linear transformations) on the final performance.
* The paper fails to establish clear criteria for evaluating new embeddings - the performance after conversion may be inconsistent with direct usage of new embeddings, potentially being better or worse, and lacks a golden standard for assessment. The paper does not address the potential for the conversion process to introduce biases or artifacts that could skew the evaluation results. It also does not consider the sensitivity of the evaluation metrics to the converted embeddings, which could lead to misleading conclusions about the efficacy of the new embeddings.
* The study lacks experiments on mapping from stronger embeddings to weaker ones. This is a significant oversight, as it limits the generalizability of the findings. The paper should explore scenarios where the source embeddings are known to be more informative than the target embeddings, to assess the limitations of the proposed conversion method.

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
2
