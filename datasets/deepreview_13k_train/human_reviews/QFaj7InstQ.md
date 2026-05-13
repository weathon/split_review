# Item Language Model

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
Embeddings are extensively used in many domains to represent information about domain entities in a compressed manner. In recommendation systems, these embeddings are trained to extract meaningful information about an item/user from collaborative filtering data consisting users ratings or implicit feedback on items. These behavioral embeddings are usually not trained on data from language domain, but they encode very useful behavioral information which cannot be described using language. In contrast, in large language models (LLM) this collaborative data and behavioral entities(users/items) are not well represented as they are not textual and are specific to the recommendation system/product. Bridging this gap between behavioral understanding and language understanding can enable new item and language interleaved tasks. In our work we show how we can efficiently adapt rich behavioral embeddings as an additional behavioral input representation in pre-trained LLMs. To achieve this we adapt Querying Transformer technique with a new item contrastive loss and show improved item-text joint understanding in PALM2. Finally, we also demonstrate improved capabilities in recommendation domain over using the behavioral embeddings directly as input to PALM2.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents the Item Language Model (ILM), a framework that bridges the gap between behavioral understanding in recommendation systems and language understanding in Large Language Models (LLMs). The ILM framework adapts a Querying Transformer (QFormer) with a new item-item contrastive loss to improve item-text joint understanding. Experiments validate the effectiveness of the proposed method compared with the ELM baseline.

### Strengths
1. Writing. The whole paper is written well and easy to follow.

2. Empirical Results. The paper provides strong empirical evidence that combining semantic and behavioral embeddings in the ILM framework leads to improved performance on semantic consistency tasks.

3. General Applicability. The technique is domain-agnostic and can be applied to any domain with rich embedding representations, making it widely applicable.

### Weaknesses
1. Limited Novelty. The proposed method is mainly based on BLIP-2, with two additional contrastive losses. However, such kind of contrastive loss is already widely adopted in many self-supervised learning methods for recommendation [1,2]. In a nutshell, the proposed method seems to be a straightforward application of BLIP-2 on recommendation-language pre-training tasks with marginal novelties.

2. Insufficient Experiments. There is only one baseline in the experiments, i.e., the ELM model. There are many recent works in pre-training collaborative-language models [3,4,5,6]. The authors need to compare the performance of their proposed approach with these models, as well as with collaborative models such as SASRec, DIN, FM, or DCN V2. It would be great to evaluate the performance on widely used metrics such as AUC of ROC, Recall or nDCG. Besides, the authors need to justify why QFormer was chosen as the backbone.

3. Insufficient Analysis. There is no in-depth analysis on a) Why does the proposed method work? Does it improve the alignment or uniformity of the representations? [7] b) How does each loss contribute to the performance lift? Could the authors provide an ablation study? c) What's the insight or takeaway of this paper?

### Questions
1. Why choose QFormer as the backbone architecture? Do the proposed losses generalize well to other backbones? If so, could you provide additional experiments on other backbones? If not, why?

2. Three of the losses are already mentioned in the BLIP-2 paper, the only additional contribution is the user-item and Item-Item contrastive loss, which are also widely adopted in many existing works. Could the authors provide an ablation study as well as an in-depth study of this loss? 

3. Could the authors provide the main insight of this work? What should the readers learn from this work?

### Soundness
2

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
4

### Summary
The author proposes the Item-Language Model framework, aiming to bridge the gap between item semantic understanding and user behavior learning in recommender systems. By using the Querying Transformer model with generation tasks, the ILM framework can effectively represents the textual and behavior knowledge for better recommendation.

### Strengths
- Although it is not the first language-recommendation alignment paper, the authors propose a new direction to integrate these two types of knowledge.
- The ILM-Qformer architecture is superior to a simple MLP model, reflecting the value of QFormer.
- Comprehensive experiments demonstrate the effectiveness of the ILM framework.

### Weaknesses
 - Is it practical in the industrial scenario where the number of items and users will reach 1 million or even billion? If not, how to solve this problem?
- There are several related works, including:
  - Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation
  - EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration
  - Learnable Tokenizer for LLM-based Generative Recommendation
  - STORE: Streamlining Semantic Tokenization and Generative Recommendation with A Single LLM
What are the difference between ILM and these works? Any experimental comparison?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

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
The paper proposes Item Language Model (ILM), a framework to bridge behavioral embeddings from recommendation systems with language understanding in Large Language Models (LLMs). The key innovation is adapting a Querying Transformer (QFormer) with a novel item-item contrastive loss to enable interleaved processing of behavioral and textual information. The framework allows unified handling of recommendation items and text for various language generation tasks.

### Strengths
1. The paper addresses a significant gap between behavioral understanding in recommendation systems and language understanding in LLMs. The proposed solution of using QFormer with item-item contrastive learning presents an innovative approach to bridging this modality gap.
2. The addition of item-item contrastive loss to the QFormer architecture is well-justified and demonstrates clear benefits in preserving behavioral information while adapting to the language domain.
3. The ablation studies effectively demonstrate the value of each component, particularly showing how the combination of semantic and behavioral embeddings outperforms using either alone. The comparison across different architectural choices (MLP vs. QFormer vs. QFormer with pre-training) provides empirical support.

### Weaknesses
1. The author should further discuss the comparison with existing recommendation systems based on large language models, such as LC-Rec [1] considering compressing product descriptions into a vector input into the large model, BinLLM [2] compressing the user product collaborative signal into an encoded input into the large model, which can also bridge the gap between semantic and recommendation collaborative signals in the large model.

2. This is a paper for recommender systems, the author does not seem to have compared the model with a large number of recommendation algorithms, such as classic collaborative filtering, LightGCN, NGCF, or with recommendation algorithms based on large language models, such as LC-Rec, BinLLM, etc. Suggest the author to conduct a more detailed baseline comparison and analysis.

3. The author does not seem to have conducted an analysis of time complexity or the time consumed in inferring user intended products, which reduces the likelihood of using this model in industry.

4. Using the method designed in the article, generate an 8-bit code for each item. Will there be similar products with the same code, which may lead to conflicts in item IDs.

5. The structure and sentences of the paper can be appropriately modified and adjusted to enhance the logic and clarity. Some typos in the paper need to be corrected, such as the missing punctuation mark at the end of the formula sentence in 3.2, some Table reference errors in Appendix.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes an item language model, which aims to narrow the gap between semantic information in LLMs and behavioral information in embeddings of CF models. Specifically, the authors adopt a Querying Transformer as an adaptor to build the bridge from collaborative information to textual information that could be handled by LLMs. Moreover, they also provide an item-item CL loss for better training. The proposed framework is adopted on PALM-2 and have been evaluated on 24 tasks from ELM, showing superior results compared to ELM.

### Strengths
1)	This work adopts Querying Transformer with an additional item-item CL loss to fuse the behavioral embeddings into the language model semantic space, which is sound and effective.
2)	The writing is clear and well organized.
3)	The authors give in-depth model analyses in Appendix.

### Weaknesses
1) The main weakness of this work locates in the experiments. In Table2, comparing ILM-Semantic with ILM-Combined, we only find that there is only marginal improvement in the semantic-behavioral combined strategy. Is this improvement significant (maybe a significance test is needed)? Moreover, it also implies that the behavioral information is not that beneficial for the tasks in ELM (which are mostly language modeling related tasks). The lack of a clear, statistically significant advantage for the combined approach raises questions about the true value of incorporating behavioral data for these specific tasks. It's crucial to determine if the observed improvements are more than just random fluctuations.
2) The technical novelty is rather limited, since both the Querying Transformer and the item-item CL are not novel. The application of these techniques, while potentially effective, does not represent a significant advancement in methodology. The core components of the proposed method are adaptations of existing techniques, which limits the overall novelty of the work.
3) The central goal of this work is to discover the best method to fuse behavioral and semantic representations for items in LLMs. However, there are lots of works that have proposed different ways to build item representations in LLM4Rec, which could be discussed in this work. The absence of a thorough discussion of existing methods in the LLM4Rec domain is a notable gap. A comprehensive comparison with other approaches would help to contextualize the contribution of this work and highlight its unique aspects, if any.
4) The authors have shown the results of sequential recommendation in Appendix. We find that the proposed framework cannot outperform OpenP5 in SR tasks. Hence, the possible application scope of ILM is limited (in this work, only the 24 tasks in ELM, which is niche). The limited performance in sequential recommendation tasks, as demonstrated in the appendix, suggests that the proposed framework may not be broadly applicable across various recommendation scenarios. The focus on ELM tasks, while valid, restricts the scope of the evaluation and raises questions about the generalizability of the findings.
5) Further analyses on the Querying Transformer should be given in the main content. For example, the ablation study of different losses should be given (besides IT, IIC, UIC). Moreover, from Table 4 we can find that the benefits of IIC and UIC are also marginal (significance test is needed), which also implies that these two losses are not that beneficial. Similar experiments are also suggested to be conducted in the main evaluation tasks. The lack of detailed ablation studies in the main content, particularly regarding the different loss functions, makes it difficult to assess the individual contributions of each component. The marginal gains observed with IIC and UIC further emphasize the need for more rigorous analysis.
6) Typos, e.g., Page8, fullyfullyfinetune -> fullyfinetune.

### Questions
1) In Figure 3, why does the result drop so dramatically at 8? The optimal query length will be impacted by which factors (e.g., data size)?

### Soundness
3

### Presentation
2

### Contribution
2
