# Making Transformer Decoders Better Differentiable Indexers

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Retrieval aims to find the top-k items most relevant to a query/user from a large dataset. Traditional retrieval models represent queries/users and items as embedding vectors and use Approximate Nearest Neighbor (ANN) search for retrieval. Recently, researchers have proposed a generative-based retrieval method that represents items as token sequences and uses a decoder model for autoregressive training. Compared to traditional methods, this approach uses more complex models and integrates index structure during training, leading to better performance. However, these methods remain two-stage processes, where index construction is separate from the retrieval model, limiting the model's overall capacity. Additionally, existing methods construct indices by clustering pre-trained item representations in Euclidean space. However, real-world scenarios are more complex, making this approach less accurate. To address these issues, we propose a \underline{U}nified framework for \underline{R}etrieval and \underline{I}ndexing, termed \textbf{URI}. URI ensures strong consistency between index construction and the retrieval model, typically a Transformer decoder. URI simultaneously builds the index and trains the decoder, constructing the index through the decoder itself. It no longer relies on one-sided item representations in Euclidean space but constructs the index within the interactive space between queries and items. Experimental comparisons on three real-world datasets show that URI significantly outperforms existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes URI, a variant of generative retrieval methods which learns the retrieval model and index construction jointly. Besides, this paper also proposes averaged partition entropy (APE) as a measure for index construction quality. In URI, the same decoder is used to generate tokens for both query and items and is trained in a using an EM algorithm. In E-step, the model is optimized through minimizing the cross entropy loss.  In M-step, To avoid model collapse while minimizing APE, two loss functions apart from the cross entropy loss are introduced to encourage that the token distribution w.r.t. each item follows a peak distribution while the expected token distribution w.r.t. the whole item space follows a uniform distribution. Finally, an additional dual encoder model is trained to identify the topk items as the final retrieved result. Experiments on KuaiSAR and Amazon Beauty/Toys/Games demonstrates the effectiveness of URI compared to other generative retrieval methods.

### Strengths
1. Learning to construct index jointly with retrieval models is an important problem for generative retrieval. The proposed method is well motivated.
2. Performance is impressive, especially on the KuaiSAR dataset.

### Weaknesses
1. Writing can be further improved, especially the experiment section. The difference between URI and GR methods w/ URI index is unclear in Table 1. The analysis of token consistency is hard to understand and it will be better to demonstrate their differences to original URI through notations.
2. Insufficient analysis and comparison on other generative methods (e.g., ASI [1] and GenRet [2] ) that learns both retrieval models and indexing jointly. 
3. The assumption of Theorem 1 seems very strong and there lacks empirical analysis on real-world dataset to verify the rationality. 
4. The comparison in experiments is not unfair. The candidate size of URI is larger than other GR methods which requires the mapping between the token representation and the item is bijective while URI allows each leaf node contains more than 1 items. Besides, URI is equipped with an additional ranker.

### Questions
My major concerns are listed in the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces URI (Unified Retrieval and Indexing), a framework for generative retrieval that integrates index construction with Transformer Decoder training. URI enhances consistency between the index and retrieval model. The authors also introduce Average Partition Entropy (APE), a model-independent metric for evaluating generative indices after index construction. Targeting this metric, they also propose an optimization algorithm with a theoretical explanation. Experiments confirm the effectiveness of the proposed method.

### Strengths
- The motivation is clear. The authors argue that recent methods separate index construction from retrieval  in traditional and generative models, which limits the overall performance. Thus, this paper attempts to unify index construction and retrieval.
- This paper provides a theoretical guarantee of the proposed greedy algorithm.
- The experiments on multiple benchmark datasets validate the effectiveness of the proposed method compared with the baseline models.

### Weaknesses
 - The authors overlook recent retrieval work such as [1,2]. The authors are encouraged to discuss them in the related work.
- Since the final goal of the proposed method has many hyper-parameters in (11), more sensitivity analysis also is crucial. Specifically, the interaction between k and l, and their impact on the final performance should be analyzed in more detail. The current analysis in Section 5.4 is not sufficient to show how these parameters affect the overall performance of the model. For example, how does the performance change when k is large and l is small, and vice versa?
- Theorem 1 lacks the corresponding empirical results, so more evidence is needed. The theoretical guarantee is not directly linked to the actual performance of the algorithm. It would be beneficial to show how the greedy algorithm's behavior aligns with the theoretical claim in practice, and whether the 95% allocation translates to a significant performance gain.
- Including both index construction and retrieval in the unified framework may increase computation and storage overhead, affecting efficiency. Therefore, an efficacy analysis (e.g., memory usage, training/inference time, and FLOPs) is necessary. The analysis should also consider the scalability of the proposed method with respect to the size of the dataset and the index.

### Questions
Please see the above weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes URI (Unified framework for Retrieval and Indexing), a novel approach that unifies index construction and retrieval model training for generative retrieval systems. The key innovation is using the same Transformer decoder both as the retriever and the indexer, constructing the index simultaneously with model training rather than as a separate pre-processing step. The paper introduces Average Partition Entropy (APE) as a new metric for evaluating generative indices and provides theoretical analysis using EM algorithm to justify their approach. The authors demonstrate URI's effectiveness through experiments on three real-world datasets.

### Strengths
- The paper identifies clear limitations in existing two-stage approaches where index construction is separated from retrieval model training. 
- The approach of using the decoder itself as an indexer is creative and original and introduction of APE as an evaluation metric is well-justified and useful
- Addresses fundamental limitations in generative retrieval systems leads to potentially applicable across various retrieval tasks
- Could influence future work in information retrieval and recommender systems

### Weaknesses
Limited Empirical Analysis
- While experiments are conducted on three datasets, more details about these datasets would be helpful
- Ablation studies could better isolate the impact of different components
- Comparison with more baseline methods would strengthen the evaluation

Scalability Concerns
- The paper doesn't thoroughly discuss computational complexity
- Practical considerations for large-scale deployment are not addressed
- Memory requirements for the unified approach could be significant

### Questions
- How does the computational complexity of URI compare to traditional two-stage approaches? Is there a significant overhead in training time or memory usage?
- How sensitive is the method to the choice of initial conditions? Does the unified training require special initialization strategies?
- Could the authors provide more details about how URI handles cold-start scenarios where new items or queries are added to the system?
- How does URI perform in scenarios with highly imbalanced data distributions? Are there any special considerations or modifications needed?
- The theoretical analysis assumes certain statistical conditions - how often are these conditions met in practice? What happens when they are not met?
- Could the authors elaborate on potential extensions of URI to handle dynamic indices that need to be updated over time?

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
3

### Summary
The paper tackles item (document) retrieval problem, i.e., the algorithm should return the indices (and scores) of most relevant items given a query. In particular, the paper focuses on generative (decoder) based subset of algorithms. Current decoder-based methods follow a two-step procedure where first the index is learned over pre-trained features (e.g., DSI) and then the model is trained to generate in this space. The paper argues that the aforementioned procedure can be sub-optimal, and it proposes URI (a unified framework for generative retrieval) that simultaneously learns the index as well as the decoder. 

The model is trained in a layer-by-layer manner (in contrast to existing ones). The first layer is trained by optimizing $\mathcal{L_{E step}} + \mathcal{L_{M step}} $ - the similarity between corresponding queries and items is optimized while avoiding index collapse. The buckets are then assigned for each item via balanced assignment. First layer tokens are then passed onto second layer which is trained via an additional memory reinforcement loss term to avoid forgetting. Finally, a ranker is trained that assigns score to query item pairs on the basis of inner product between pooled embeddings.  

The results are reported on KuaiSAR, Amazon Beauty and NQ-320K datasets with focus on demonstraing the benefit of URI index as compared to the baselines (DSI, NCI, TIGER etc.,).

### Strengths
1. The paper is decently written and easy to follow.
2. The paper reports numbers on KuaiSAR, Amazon Beauty and NQ-320K datasets and it compares against leading methods including DSI and NCI. 
3. The proposed method yields good benefits when the index of baselines is replaced with the proposed URI based index as well as in terms of overall numbers. For e.g., the performance of DSI and NCI improved by ~3% on the NQ-320K datasets. The benefits are even starker on the KuaiSAR dataset where the overall performance improved by upto 14% as compared to the baselines.  
4. The paper analyses the impact of URI index as compared to other popular indices including kMeans and VQ-VAE. The APE values are reported in Table 2. The benefits of layer wise training (token consistency), Adaptive weights ($\mathcal{L}_{balance\ w}$) and hard negative mining (during ranking). 
5. The paper provides hyper-parameter details in 5.4.

### Weaknesses
1. The results section compares against various methods including DR, DSI and NCI. It shows the impact of changing the original index with URI index alongside the overall comparison. However, the overall numbers don't seem to be for the best version of respective algorithms. It is perhaps done for consistency across algorithms? For e.g., the R@20 for NQ-320K can be in range of 0.56 - 0.89 for methods including ANCE, DSI, and NCI whereas URI is 0.057 (?). Please see https://arxiv.org/pdf/2206.02743. Please clarify if I am misinterpreting something.
2. The paper is missing the training and inference times of the proposed method. These stats will provide a fair comparison against the baselines (in addition to already included theoretical complexity).

### Questions
1. Please look into the points above concerning end-to-end baselines and training/inference time. 
2. The final scores are computed via a re-ranker that uses the inner product (on pooled query and doc embeddings). It may be worthwhile to try out a cross-encoder based re-ranker. 
3. Can you please comment on scalability of URI? How does the performance change with increase in number of docs / items?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an end-to-end retriever and index, It simultaneously clusters query and relevant items and ensure that they both follow similar distribution over cluster nodes at each level. The URI (proposed approach) ensures that clusters are balanced and accurate.

### Strengths
This paper proposes an end-to-end retriever and indexer.
Results are state of the art

### Weaknesses
 - This paper looks a lot like EHI: End-to-end Learning of Hierarchical Index for Efficient Dense Retrieval with similar loss functions, TMLR 2024
- Results on standard bier benchmark datasets are missing
- In real world scenario new items are always popping in and out of existence, how does URI deals with zero shot items

### Questions
Please see the weakness section and answer the following:
- How does method compares with EHI, what are the similarity and differences between EHI and URI
- APE is standard practice to measure cluster quality why is it a contribution in your paper. (See ECLARE)
- Add comparison on BIER benchmark datasets

ECLARE: Extreme Classification with Label Graph Correlations, WWW 2021.

### Soundness
2

### Presentation
2

### Contribution
2
