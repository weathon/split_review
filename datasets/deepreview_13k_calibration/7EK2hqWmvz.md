# RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
Deploying large language model inference remains challenging due to their high computational overhead.
Early exiting optimizes model inference by adaptively reducing the number of inference layers.
Existing methods typically train internal classifiers to determine whether to exit at intermediate layers.
However, such classifier-based early exiting frameworks require significant effort to train the classifiers while can only achieve comparable performance at best.
To address these limitations, this paper proposes RAEE, a robust \textbf{R}etrieval-\textbf{A}ugmented \textbf{E}arly \textbf{E}xiting framework for efficient inference.
First, this paper demonstrates that the early exiting problem can be modeled as a distribution prediction problem, where the distribution is approximated using similar data’s exiting information.
Then, this paper details the process of collecting exiting information to build the retrieval database.
Finally, based on the pre-built retrieval database, RAEE leverages the retrieved similar data's exiting information to guide the backbone model to exit at the layer, which is predicted by the approximated distribution.
Experimental results demonstrate that the proposed RAEE can significantly accelerate inference.
More importantly, RAEE can also achieve a robust zero-shot performance on 8 downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work uses retrieval to improve performance on training-free early exit frameworks. The motivation for doing so is observing that similar data should have similar early exit patterns. Experimental results show that this method is significantly better than existing training-free early exit methods.

### Strengths
- Good empirical results on downstream tasks when compared to prior work (table 1)
- Compares inference times as well (figure 3)
- Provides a clear overview and motivation for the problem

### Weaknesses
 - While the paper mentions that out-of-domain performance is out of scope, I think this is a very important problem because many models today train on non-public data and in the real world we do not always have accompanying train sets to user inference. While it may be out of scope to completely understand out-of-domain performance, I would like to see the authors do some analysis, such as examining performance changes as a function of distance between test example and the nearest neighbors.
- Another interesting experiment for the above is using the LM train set (e.g. C4 for T5) instead of GLUE train sets for the database.
- Give that you have the test labels, can you do additional analysis to compare RAEE with other methods to see how often it exits at the correct layer? This can also clarify questions about inference times
- Figure captions could be improved

### Questions
See potential experiments or analyses mentioned in weaknesses

### Soundness
3

### Presentation
2

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
This paper aims to enhancing the efficiency of large language model inference by adaptively exiting the model at earlier layers. The authors model the early exit problem as a distribution prediction issue, and then use exit information from similar data to approximate the distribution. They outline the methodology for constructing a retrieval database with exit information and propose the RAEE framework, which leverages the pre-built retrieval database to predict the exit layer based on the exit information from the top-k nearest neighbors. Experimental results across eight downstream tasks demonstrate that RAEE improves inference speed while maintaining robust zero-shot performance, outperforming other early exit frameworks.

### Strengths
1. The paper provides a novel combined method to decide the exit layer.
2. The paper is well written and easy to follow.
3. The proposed method is reasonable. Experiments support their claims. The performance can be improved in most scenarios.

### Weaknesses
1. The paper does not clearly position itself with respect to existing retrieval-augmented methods that used to accelerate the model’s inference. A more thorough literature review is needed to highlight how RAEE differs from and improves upon prior work. Specifically, the paper lacks a detailed discussion on how its retrieval mechanism compares to other methods that leverage retrieval for efficient inference, such as those that use nearest neighbor search or knowledge distillation with retrieved examples. The novelty of the retrieval database construction and its impact on performance should be more clearly articulated in relation to existing techniques.
2. While the data presented in figure3 is comprehensive, I noticed that the visual presentation, specifically the subscripts, could be enhanced for better readability and aesthetic appeal.

### Questions
1. It has been observed that modeling the early exit problem as a distribution prediction issue is not a novel approach, as similar concepts have been explored in prior works. Could the authors elaborate on the specific novelties of their proposed RAEE framework compared to existing methods?(eg. Predictive Exit: Prediction of Fine-Grained Early Exits for Computation- and
Energy-Efficient Inference)
2. Table 4 indicates that the performance of RAEE improves with a larger retrieval database. How does the authors plan to balance the trade-off between database size, storage requirements, and inference efficiency, especially for resource-constrained environments?
3. In Table 1, why were only 2-3 other methods compared for a specific single backbone(why weren't some methods compared) ?
4. The paper uses a threshold of 0.9, but it's unclear how sensitive RAEE is to it. An analysis of how changes in these parameters affect performance would be useful.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenge of high computational demands in large language model inference. It focuses on reducing the number of inference layers required by exploiting early exits. Instead of early-exiting by training internal classifiers to decide if the model can exit after fewer layers, the authors propose RAEE, a Retrieval-Augmented Early Exit framework. RAEE treats early exit as a distribution prediction problem, where exit decisions are informed by similar data examples stored in a retrieval database (Cache). This approach allows the model to decide on exiting based on prior information from similar data, leading to faster and more efficient inference.

### Strengths
**Method**

- The method is interesting, and there is a clear performance improvement. Creating a database to decide what layer to use sounds promising. I would push that idea to create a more general dataset rather than tailor it to each specific target dataset.

### Weaknesses
 **Motivation.**

- Although I understand that the inference time could be reduced by early exiting, one of the main reasons for the high computational demand for Transformer LLMs is the KV cache. In this regard, solutions like PagedAttention [1] show a 3.5x and 24x higher throughput using LLaMA. My concern is that this paper claims to accelerate the model inference. However, it doesn't compare with those types of approaches. If the motivation of this work is to deploy LLM on resource-constrained devices, the memory aspect is key. Moreover, Figure 3 shows that the method did not always get better inference latency compared to the base method T5-L, RoBERTa/ElasticBERT or the selected baselines (AdaInfer, SLEB).

- In my opinion, the work is more interesting regarding performance improvement than latency reduction (Table 2). The results show a clear diversity in the layers. It seems that some layers are better than others for some datasets. Thus, section 4.3 needs to be explored deeply. I expected to see some statistics about the layers used the most for each dataset and what type of tasks/questions/data are better answered for the early or later layer. This raises the question of whether the retriever database could be more general to the input data type.

---
**Experiments.**
- Even though the GLUE benchmark is well-known by the NLP community, it would be good to explain it further, emphasizing the evaluation metrics and clarifying if the tasks are classification or generation.

- To better contextualize the method RAEE with the LLMs used in the comparison, it would be great to see the performance of HashEE/CALM/SLEB on each LLM. (Figure3)

- Section 4.3 requires much more analysis to understand the sentence L407-408 better. 
> - What layers are the most used? 
> - Is there some correlation between the type of data vs early exit or type of task vs early exit?


---
 **Presentation.**

- Some parts of the text are difficult to follow. 
 
- Figures and plots require better captions. Figure 1 is quite intuitive, but explaining each component in the caption would be ideal. Figure 2 is confusing: the caption doesn't explain the difference between (a) and (b). Also, the explanation between L131 and L142 is confusing. In general, captions for figures and tables are very superficial.

- Citations. Line 124 could cite Tip-Adapter as a training-free adaptation that uses a cache for image classification. In the same line (124), what are the existing retrieval databases that use clustering and/or product quantization?

### Questions
- If you could assess the concerns above.
- When two or more layers have the same maximal probability RAEE selects the earliest L255. I'm wondering if this is a good option. How many cases exist with the same maximal probability in each dataset? How many times RAEE choose the earliest and make mistakes? If it would use a later, could it get a correct performance?
- How much memory is added if we want to deploy this method on resource-constrained devices?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new early exit approach that predicts a probability distribution over the set of layers in the model in which distribution is approximated using similar data. Specifically, it utilizes the embedding of the incoming samples and creates an embedding space where the number of spaces is equal to number of layers in the model. The decision of which space an incoming sample belongs is made based on  the possible layers it can make an exit from. During inference, an incoming sample is first checked against the top-k nearest neighbors and the sample is assigned an exiting layer based on the estimated probability distribution using the top-k neighbors.

### Strengths
1. The paper is well written.

2. Paper uses multiple backbone models making the claims strong.

3. The paper claims to reduce the latency overheads which is an important problem for the community.

### Weaknesses
1. **Novelty:**  The paper lacks novelty as the main claim is it is learning the distribution of incoming samples using the embeddings of the samples. This is already done in DIMEE [1] work, however the objectives of both the works are different, the method to solve the problem are very similar. 

2. **Lack of proper baselines:** There are multiple existing works [2], [3]. [4], [5] that also learn the probability distribution over the exit points but the paper have neither cited them nor compared against them that reduces the overall impact of the paper. Since the final objective of the paper is to learn a distribution, there should be a comparison with existing distribution predicting methods.

3. **Overclaim:** The paper has a major claim that it can outperform under zero-shot setting but it requires the labels to create the retrieval database. Also, there will be large impact if the domain of the test dataset changes which is not explored in this paper.

4. **Lack of explanation:** As per as I believe, the better results of RAEE are due to the fact that it uses learned final layer classifier to map the hidden representations from intermediate layers to class probabilities similar to [5], however, other baselines use different classifiers at each layer that are randomly initialized hence the loss in performance. This is an apple to orange comparison, even the baselines should be tested with learned final layer classifier for fair comparison.

5. **Clustering figure:** I believe there should be an additional t-SNE plot in the paper showing that how the clusters are formed based on the exit points as shown in the DIMEE paper.

**Missing references:** There are a lot of missing references

1. DIMEE: https://arxiv.org/abs/2410.05338

2. JEI-DNN: https://openreview.net/pdf?id=jX2DT7qDam (ICLR 2024)

3. ZTW: https://proceedings.neurips.cc/paper/2021/file/149ef6419512be56a93169cd5e6fa8fd-Paper.pdf (NIPS 2021)

4. PALBERT: https://proceedings.neurips.cc/paper_files/paper/2022/file/5a9c1af5f76da0bd37903b6f23e96c74-Paper-Conference.pdf (NIPS)

5. MSDNet: https://arxiv.org/abs/1703.09844

6. CeeBERT: https://aclanthology.org/2024.findings-acl.101/ (ACL 2024)

7. ETFEE Yixin Ji, Jikai Wang, Juntao Li, Qiang Chen, Wenliang Chen, and Min Zhang. 2023. Early exit with disentangled representation and equiangular tight frame. In Findings of the Association for Computational Linguistics: ACL 2023, pages 14128–14142.

### Questions
See weaknesses:

Also, Early Exits are not pruning based methods, instead they fall into class of dynamic inference methods as pruning reduces the weights. Here none of the weights are reduced instead the model decides which layer it should not use although it has an option to use them which is not the case with pruning.

### Soundness
2

### Presentation
2

### Contribution
2
