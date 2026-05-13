# Periodic and Random Sparsity for Multivariate Long-Term Time-Series Forecasting

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
For years, Transformers have achieved remarkable success in various domains such as language and image processing. Due to their capabilities to capture long-term relationships, they are expected to give potential benefits in multivariate long-term time-series forecasting. Recent works have proposed segment-based Transformers, where each token is represented by a group of consecutive observations rather than a single one. However, the quadratic complexity of self-attention leads to intractable costs under high granularity and large feature size. In response, we propose Efficient Segment-based Sparse Transformer (ESSformer), which incorporates two sparse attention modules tailored for segment-based Transformers. To efficiently capture temporal dependencies, ESSformer utilizes Periodic Attention (PeriA), which learns  interactions between periodically distant segments. Furthermore, inter-feature dependencies are captured via Random-Partition Attention (R-PartA) and ensembling, which leads to additional cost reduction. Our empirical studies on real-world datasets show that ESSformer surpasses the forecasting capabilities of various baselines while reducing the quadratic complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a transformer approach for multivariate timeseries forecasting. To improve the efficiency for segment transformers authors propose two new self-attention modules. First module applies block-diagonal and stride dilated attention to capture temporal relationships. Second module partitions features into disjoint groups and applies attention within each group. Empirically, authors show that the combination of the two modules leads to better performance and higher efficiency.

### Strengths
I found the paper to be well written and easy to follow. The two introduced attention blocks are interesting and while numerous papers have been published on attention, I believe this work is novel. Authors provide extensive empirical evaluation showing superior performance over a number of leading baselines. Furthermore, extensive ablation study is conducted demonstrating the contribution of each introduced module and the efficiency gains in computation.

### Weaknesses
The R-PartA introduces randomness into the grouping of the features. To overcome this during inference authors run multiple passes through the model and ensemble the results. This can create an unfair advantage as ensembles nearly always improve performance and often significantly, Figure 5 further validates it. I think the results reported in Table 1 should not be ensembled and I suspect that this would significantly reduce the performance improvements.

### Questions
What is the average rank of ESSformer (Table 1) if the ensembling is not used?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is paper presents a new Transformer variant for multivariate long-term time series forecasting. In particular, it proposes to decompose tokenized long time series into blocks over both temporal and feature dimensions. For temporal contextualization, dense attention within each block is followed by dilated attention across blocks; for feature contextualization, the partitioning is done randomly and dense attention is applied within each random group only. In this way, the complexity of self-attention is reduced while the random partitioning in features introduces implicit data augmentation to boost the performance.

### Strengths
1. The paper is well-written with clarity in the presentation of the well-motivated main ideas;
2. The empirical studies are extensive with strong results. 
3. Abundant analyses are provided to support the effectiveness of the proposed methods.

### Weaknesses
1. The novelty of such a Transformer variant is rather limited given the mediocre empirical improvement. 
2. The name of the proposed method is somewhat misleading. For example, "periodic and random sparsity" in the title is not accurate as sparsity only applies to temporal dimension and random only applies to feature dimension, while these highlights are placed side-by-side. Moreover, the term "periodic" is confusing since it has nothing to do with the intrinsic periodicity of time series, as the block size $P$ is empirically selected.
3. The theoretical analysis on complexity needs to be elaborated.

### Questions
1. Why is the complexity of R-PartA reduced to be $\mathcal{O}(DS_G)$?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a new time series forecasting method called Efficient Segment-base Sparse Transformer with two attention modules called PeriA and R-PartA. PeriA reduces the computational cost by taking advantage of the attention score matrix capturing temporal dependencies that tend to mix representations of periodically spaced tokens. R-PartA randomly partitions the given features into equal size groups and it seems to work well.

### Strengths
1. This article is exquisitely crafted, using precise and appropriate language while being rich in meticulous details, allowing readers to gain a deep understanding of the content. In terms of exposition, the article is both comprehensive and succinct, making it easily comprehensible without feeling overly lengthy or cluttered. Furthermore, the article also incorporates beautiful illustrations that are not only aesthetically pleasing but also vividly complement and enrich the content.  
2. The article extensively experimented with the proposed model structure across seven datasets and outperformed the selected baseline.  
3. The article not only conducted a theoretical analysis of the model's complexity but also presented a comparison of FLOPs and memory usage.

### Weaknesses
1. The effectiveness of the proposed two sparse attention modules in the model can be questionable. In the Method section (Section 3), I found that ESSformer is not a purely Transformer-based model because it includes an MLP encapsulating two attention modules at each layer of the model. Excluding these two structures, ESSformer appears to be a simplified version of TSMixer, which is already effective enough. The results of ablation experiments are also unsatisfactory, as the predictive performance of the ablated models closely resembles that of the non-ablated models. Additionally, in Table 1, we observe that the performance difference between ESSformer and TSMixer is not significant.  
2. The reason why randomly partitioning features seems to work could be simply because it involves using a reduced set of features for prediction. The author's perspective is that R-PartA works by diversifying the training set by allowing partial feature interactions, and the model is capable of "overcoming feature dropping" (as discussed in Section 4.3). However, for time series forecasting tasks, the results of univariate time series predicted univariate time series are often superior to multivariate time series predicted univariate time series. Also, the more features are used, the more challenging the prediction becomes, leading to poorer model performance in terms of metrics, so there is no "overcoming feature dropping".  
3. In the complexity section, the author does not compare all the experimentally selected baseline models in Table 1, including some Transformer-based models such as PatchTST. This omission is somewhat perplexing.

### Questions
I hope the author will address the questions raised in the Weaknesses section in their response.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of time-series forecasting using transformer models. The paper tries to improve the efficiency of the existing segment-based transformer model by two aspects: 1) the paper proposes the periodic attention block where data points in the same segments are first processed using self-attention and then only the data points with the same periodic indexed are processed together using a second self-attention. 2) The paper uses a random attention block on the feature where the features are firstly randomly partitioned into blocks and self-attention is applied accordingly based on the partitioning structure. The paper shows improved performance on the majority of time series forecasting task with improved efficiency.

### Strengths
The paper proposes two kinds of novel attention block mechanisms which are very intuitive and have strong empirical performance.

### Weaknesses
1. It seems that to make the periodic attention work, the model needs to know the right periodic interval of the time series. In some cases, this could be easy as we know the data is collected hourly/daily/etc but in the more general setting it may require to infer the actual periodic behaviors of the data stream. Moreover, there could be multiple and potentially overlapping periodic intervals encoded in the data stream. Extending the given approach to such a more general setting seems not trivial. The current approach appears to rely on a single, pre-defined period, which may not capture the full complexity of real-world time series data that often exhibit multiple periodicities or non-stationary periodic patterns. For example, a time series might have both daily and weekly seasonality, and the proposed method would need to be adapted to handle such cases effectively. Furthermore, the method does not address how to deal with time series where the periodic behavior might change over time, which is a common occurrence in many real-world scenarios.

2. More studies on why the random partition attention works are necessary. It's not clear to decide on the number of groups and how many instances are required for the ensemble during inference to get the best performance. Are there some metrics we can check before/during training to get the right number of groups? Furthermore, how do they relate? I.e., if we change the number of groups when partitioning, how should the number of instances in the ensemble be adjusted accordingly? The paper lacks a clear explanation of the underlying mechanism that makes random partitioning effective. It is unclear how the random partitioning of features leads to improved performance, and what properties of the data or the model make this approach beneficial. Without a deeper understanding of this mechanism, it is difficult to determine the optimal hyperparameters for the random partition attention, such as the number of groups and the number of instances for ensembling. The paper should provide more insights into the relationship between these hyperparameters and the performance of the model.

### Questions
Please see the weaknesses part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
