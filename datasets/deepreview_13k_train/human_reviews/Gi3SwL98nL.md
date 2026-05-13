# Leveraging LLM Embeddings for Cross Dataset Label Alignment and Zero Shot Music Emotion Prediction

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
In this work, we present a novel method for music emotion recognition that leverages Large Language Model (LLM) embeddings for label alignment across multiple datasets and zero-shot prediction on novel categories. First, we compute LLM embeddings for emotion labels and apply non-parametric clustering to group similar labels, across multiple datasets containing disjoint labels. We use these cluster centers to map music features (MERT) to the LLM embedding space. To further enhance the model, we introduce an alignment regularization that enables dissociation of MERT embeddings from different clusters. This further enhances the model's ability to better adaptation to unseen datasets. We demonstrate the effectiveness of our approach by performing zero-shot inference on a new dataset, showcasing its ability to generalize to unseen labels without additional training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors use sentence embedding (from Sentence-BERT) and MERT to get the embedding of music emotion label and music respectively, and try to align the label and music embeddings through triplet loss and alignment regularization to achieve emotion classification and zero-shot emotion classification. The authors demonstrated the benefit by using sentence embedding, and also the alignment regularization over baseline.

### Strengths
Overall, the ablation studies are self-consistent and supportive to the claims. The improvement on the zero-shot recognition capability via alignment regularization is simple yet effective, which can also be applied to other domains.

### Weaknesses
Here are my major concerns.

1. The word LLM used here is a bit misleading to me. If I read the "LLM" used in this work properly, it seems to be a sentence transformer that was modified from BERT by using siamese and triplet network for training which can help derive semantically embedding for sentences that can used to calculate cosine-similarity. The LLM here is not the causal large-scale LLM like GPT.
If BERT-style models are non-causal LLM, if the authors want to claim large-scale LLM can generally bring in huge benefits to this problem especially in generalization to unseen labels, I would encourage the authors to break down between causal and non-causal style models. 
Especially, some LLMs do not natively output semantic embedding, the authors may want to describe how they do that generally, and also do comparison among different LLMs with different training strategies and model size.

2. The baseline design does not make too much sense to me. From baseline 2 to baseline 1, there are at least two variables, one is the authors use more datasets, and the other is introducing the LLM embedding clustering. Can we have a baseline with LLM that's just based on one single dataset?

3. Do different clustering methods matter? This is not studied and mentioned.

4. The authors described a specific way to extract representations from MERT (e.g., 3/6/9/12 layers). The authors should explain the motivations. As you eventually go to a follow-up linear projection layer, why not use all layers?

5. Overall, the algorithm makes sense but does not show a lot of novelty. One major attracting point is the claim that using embeddings from LLM will help, but the results to support that claim are not strong enough. This also relates to my major concern point 1.

### Questions
How zero-shot is achieved is still not clear to me. Will the authors re-do clustering using new unseen labels? Or will the model just map to existing defined centroids? 
Equations are not properly labeled, so it also becomes difficult to refer to equations.

### Soundness
3

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
5

### Summary
The paper introduced a method to conduct zero-shot emotion recognition from music audio. The authors basically followed the well-known zero-shot learning framework. First, label's language embedding is extracted. Second, label embeddings are clustered. Third, audio encoder is learned to match with the clustered label embeddings. Finally, in the inference stage, they conducted zero-shot prediction using unseen label's embedding (or non-parametric clusters). In this work, the authors used LLM embeddings as a labels' language embedding extractor, and MERT audio encoder, Mean Shift clustering, triplet loss and regularization techniques are used. Overall, the paper is easy-to-read. However, the lessons the readers can acquire from the paper is limited in terms of the novelty of the technique, the experimental result, and analysis of the phenomenon.

### Strengths
The paper is well-written and easy-to-read. Experimental design seems to be correct and the results seem convincing.

### Weaknesses
If we see the result tables (2,3,4), the authors basically trained the model with certain datasets and evaluated the trained model on the dataset that are not used in the training phase. However, I think this is not enough for measuring the zero-shot ability. In MTG-Jamendo, CAL500, and Emotify datasets are distinct in terms of the data instances, however, I think there exist some overlaps in the labels between the datasets. Therefore, what the authors mainly measured through the experiments was instance-level or dataset-level zero-shot prediction capability however, this experimental design may have not considered the zero-shot learning ability on the unseen label thoroughly. Also, the used datasets are mostly multi-labeled emotion datasets, so applying zero-shot learning experimental design that were developed in single-labeled task may not be enough for measuring multi-label zero-shot learning experiments.

### Questions
I think if the authors would want to emphasize on the proposed methodology, then the experimental design should be enhanced with more diverse datasets with more strict seen / unseen dataset separation. Also, if the main contribution is on the proposed methodology, then maybe including more tasks and datasets might make the paper more solid, such as zero-shot music tagging, audio tagging, etc. Or, if the main contribution is on zero-shot emotion prediction task itself, then more in-depth experimental design on emotional label might be helpful to highlight the authors contributions. For example, analysis over certain emotion tags that are used in multiple datasets, such as how this emotion tag is used slightly differently over each datasets, and how the proposed method bridge this difference well. Case studies over emotion labels would also be beneficial.

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
4

### Summary
The paper presents an approach to use large language model embeddings for label alignments across multiple datasets to perform emotion recognition in music. The paper reports improved performance as a consequence of applying the proposed approach as compared to not using it, and also demonstrated generalization of the proposed approach's efficacy through zero shot learning experiments.

The paper is well motivated, clearly drafted, and provides sufficient background information on prior art. The contributions of the work are clearly outlined. However, there are certain information that are missing which can help to make the work more easily accessible to the reader. Detailed comments and questions are shared below.

### Strengths
The article presents an approach to leverage large language model embeddings obtained from labels to generate music emotion clusters for the task of recognizing perceptual emotions from music samples. The proposed approach can be used to perform zero shot learning that can facilitate cross-corpus evaluation. The work is well motivated, the proposed approach is interesting and results show promise.

### Weaknesses
The paper lacks certain details which makes it difficult to assess the novelty and the strength of the proposed approach. Some technical contents are missing which can benefit the paper by making it more easily accessible to the reader.

(1) The data description section can benefit from additional details, for example how was the training-validation-test splits obtained?

(2) Providing additional technical details for example how many clusters were used and how the number of clusters was determined will be helpful. Also, it will be informative to share how the performance of the system may vary based on the number of clusters selected? Given that the approach is based on learned emotion clusters from LLM embeddings obtained from the data labels, it will be quite useful for the reader to be aware of some of the decisions that were made while processing the LLM embeddings.

### Questions
Here are some detailed questions and comments, which if addressed, can help the paper to be more useful and accessible to the reader:

(1) Section 3.3.1: line 192: "We select the 3rd, 6th, 9th, and12th layers from MERT ..." > what is the rationale behind selecting these specific layers from MERT? If this based on any prior research then providing that reference will be useful. Otherwise, it will be helpful to provide some rationale behind the selection. If the decision was made through empirically studies, please add that information into the paper.


(2) Section 4.1: How were the train-dev-test splits obtained? There are multiple datasets explored in this work, it will be helpful to provide how the data-splits were done and if possible point to some resources that provide such information, that way the results shared in this work can be reproduced.

(4) It is not clear what is used to generate the LLM embeddings. In case of Emotify data, how were the top 3 labels converted to LLM embeddings? It will be helpful if the authors can elaborate more on the steps that were taken to transforming the labels to LLM embeddings and then to emotion clusters. Figure 1 is definitely helpful, but more explanation in section 3 will be helpful.

(5) Section 4.4, page 8, line 408 > a macro-F1 score of 0.078 is fairly low, it will be helpful to explain why the authors specified “strong macro F1 scores”. It will be helpful to provide prior reported results on these datasets to provide some clarity regarding how well the performance shared in this paper perform with respect to prior art.

(6) Section 4.4, page 8, lines 412-414 > Is it possible that these observations indicate that perhaps there may be some over fitting happening during the model training, as a consequence of limited data?

(7) Page 9, table 3: t seems from table 3 that the authors considered clustering across 2-datasets, one rational follow up question would be: what happens when the same is performed across all the three datasets?

### Soundness
3

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
3

### Summary
The paper proposes a novel approach to music emotion recognition (MER) by utilizing Large Language Model (LLM) embeddings for label alignment across disparate datasets and enabling zero-shot emotion prediction. The core idea involves computing LLM embeddings for emotion labels from different datasets, clustering these embeddings to form a common representation space, and mapping music features derived from the MERT model into this space. The paper introduces an alignment regularization to enhance the model's generalization to unseen data. The proposed method is validated through extensive experiments on three music emotion datasets: MTG-Jamendo, CAL500, and Emotify, demonstrating substantial improvements in zero-shot inference performance.

### Strengths
- The use of LLM embeddings for aligning emotion labels across different music datasets is interesting due to its ability to generalize to previously unseen emotion labels
- The experimental results show that the proposed alignment regularization and clustering techniques improve zero-shot performance compared to existing methods

### Weaknesses
 - The introduction lacks a proper literature review. For example, the claim that "the majority of studies have focused on training and testing with a single dataset" is inaccurate. Since 2022, many audio-language papers (e.g., LTU, CLAP, GAMA) and music-language models (e.g., MuLan, MuLaP) have been trained on multiple emotion recognition datasets.
- The choice of methods, such as the specific LLM used for embeddings, Mean Shift clustering, and the alignment regularization formulation, lacks theoretical support or empirical justification. The paper would benefit from a deeper discussion on why these choices were made and how they compare to alternatives like k-means clustering, l2 regularization, etc.
- The baselines used for comparison are relatively simple. The paper does not include comparisons with multi-task learning, transfer learning techniques, or zero-shot models that could also address cross-dataset generalization. Recent works, for instance, train on valence, arousal, dominance, and other emotion views to avoid dealing with different emotion labels across datasets. Another approach is SSL training across datasets, followed by linear probing on target datasets. For zero-shot approaches, models like CLAP, LTU, and GAMA can support any emotion classes, providing alternative ways to overcome predefined class limitations. Including these baselines would help contextualize the proposed method and offer further analysis on where it outperforms or underperforms existing methods.
- While alignment regularization improves zero-shot performance, it seems to degrade cross-dataset generalization. The paper should provide a more detailed analysis of the trade-offs involved and whether the zero-shot improvement outweighs the generalization loss.

### Questions
- It would be beneficial to discuss why previous multi-dataset approaches may fall short and how this work addresses those gaps, expanding on the point mentioned in introduction
- Did the authors have a rationale for selecting specific methods of mean-shift clustering? If so, can the authors add it here and include it in the paper. Adding empirical comparisons, such as how Mean Shift performs relative to k-means or other clustering methods, would help support the hypothesis the authors have
- Can the authors consider adding general baselines that utilize multi-task learning across emotion dimensions, self-supervised learning (SSL) across datasets followed by linear probing, or zero-shot models like CLAP, LTU, and GAMA, which support arbitrary emotion classes? This would provide a clearer picture of the proposed method's strengths and limitations compared to existing techniques and reveal its competitiveness when emotion labels vary across datasets.

### Soundness
3

### Presentation
3

### Contribution
2
