# SaTran: An efficient Transformer exploiting Spatiotemporal Redundancies for Satellite Image Time Series Representation Learning

- Decision: Reject
- Scores: 3, 5, 5, 5, 5

## Abstract
Earth observation applications like crop yield prediction, solar energy prediction, land cover classification, etc., need large size Satellite Image Time Series (SITS) leading to huge computational requirements. A couple of BERT-based models exist which work at pixel level unable to exploit spatial correlation among pixels and also require ground truth at pixel granularity during fine-tuning, rendering them infeasible for prediction tasks. The  models based on Vision Transformer factorize spatial and time dimensions and first process images and then time series of image embeddings. However, in many cases, SITS require simultaneous analysis of both dimensions. We present a transformer, SaTran, which focuses on non-redundant patch tubes to overcome the limitations listed above. Transformers developed for RGB videos are found lacking when applied to SITS data characterized by the presence of patches with spatiotemporal redundancy persisting throughout the time series. SITS data also has patches where temporal redundancy lasts only for a few timestamps. The salient features of SaTran include: 1) an automatic patch tube selection mechanism which ignores spatiotemporally redundant patches; 2) exploitation of spatial correlation between pixels by the processing of patch tubes and handling of their temporal redundancy using tube masking; 3) two-fold handling of redundancy and distributed application of VideoMAE enables space and time efficient processing of large size SITS; and 4) learning end task agnostic representation of entire time series. Extensive experimentation shows that SaTran outperforms competing models and exhibit state-of-the-art performance for various earth observation applications. The code is available on (.. will be given after acceptance..).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
SATRAN: An Efficient Transformer for Satellite Image Time Series Representation Learning by Exploiting Spatiotemporal Redundancies. This conference paper proposes SATRAN which is a novel Transformer-based model designed to efficiently learn representations from satellite image time series by leveraging spatial and temporal redundancies. The approach aims to address challenges in Earth observation applications where ground truth is often unavailable at pixel-level, necessitating aggregation of predictions for larger geographical units. However, there are some issues:

### Strengths
This conference paper proposes SATRAN which is a novel Transformer-based model designed to efficiently learn representations from satellite image time series by leveraging spatial and temporal redundancies. The approach aims to address challenges in Earth observation applications where ground truth is often unavailable at pixel-level, necessitating aggregation of predictions for larger geographical units.

### Weaknesses
1.	In terms of writing, the fifth paragraph of the introduction has poor writing cohesion.
2.	Figure 2 is blurry and cannot clearly reflect the innovation points.
3.	Tables 1 and 2 of the experiment do not clearly express the effect.
4.	The innovation of the model is not sufficient, and the source of ROI selection is not indicated in the text.
5.	Table 3 shows the efficiency of the model. Regarding the column of GPU, is it the same GPU that is used?
6.	Insufficient method details: Although SATRAN is an efficient Transformer model that exploits spatiotemporal redundancies, it does not specify in detail how it specifically achieves this. There is no detailed elaboration on the architecture of SATRAN, how to identify and reduce spatiotemporal redundancies, and how these designs improve the efficiency and performance of the model.

### Questions
1.	In terms of writing, the fifth paragraph of the introduction has poor writing cohesion.
2.	Figure 2 is blurry and cannot clearly reflect the innovation points.
3.	Tables 1 and 2 of the experiment do not clearly express the effect.
4.	The innovation of the model is not sufficient, and the source of ROI selection is not indicated in the text.
5.	Table 3 shows the efficiency of the model. Regarding the column of GPU, is it the same GPU that is used?
6.	Insufficient method details: Although SATRAN is an efficient Transformer model that exploits spatiotemporal redundancies, it does not specify in detail how it specifically achieves this. There is no detailed elaboration on the architecture of SATRAN, how to identify and reduce spatiotemporal redundancies, and how these designs improve the efficiency and performance of the model.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduced SaTran, a new, cost and time-efficient transformer for large-size SITS to learn their generic representation for earth observation tasks. This method are many issues that need to be addressed.

### Strengths
The practical application value is very excellent.

### Weaknesses
1.The authors claim to have introduced SaTran, a novel, cost- and time-efficient transformer, but I did not see a detailed analysis of its architecture. Specifically, the paper lacks a clear explanation of how the proposed method differs from existing transformer architectures in terms of the core mechanisms for processing satellite image time series (SITS) data. The description of the architecture should include details on the specific layers, their configurations, and how they are optimized for SITS data.
2.The presented SaTran architecture appears to be merely a block version of a standard Transformer, showing no significant innovations or improvements. The paper does not provide sufficient evidence to support the claim of novelty. For example, it's unclear how the patch selection and temporal handling mechanisms are implemented and how they contribute to the claimed efficiency gains compared to a standard transformer with similar block structures. I encourage the authors to provide a more detailed explanation of the specific architectural modifications and their impact on performance.
3.The authors only compared one algorithm from 2023; they should include a comparison algorithm from 2024 as well. The lack of comparison with more recent state-of-the-art methods makes it difficult to assess the true performance and novelty of the proposed approach. It is essential to benchmark against the most relevant and recent algorithms to demonstrate the advancement of the proposed method.

### Questions
An analysis of the innovative aspects of the presented SaTran architecture.

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
3

### Summary
SaTran is an efficient Transformer model designed for satellite image time series. It reduces computational burden by mining spatiotemporal redundancies and extracts generalized features for Earth observation tasks. The model features a unique automatic Patch Tube selection function that discards unnecessary patches and optimizes temporal redundancy handling through Tube Masking techniques. By integrating distributed VideoMAE, SaTran enhances the efficiency of processing large-scale Satellite Image Time Series (SITS) data. Experimental results demonstrate that SaTran outperforms traditional models in prediction tasks such as crop yield and snow cover, offering lower resource consumption and providing an efficient new approach for high-resolution satellite image analysis.

### Strengths
SaTran improves the efficiency of processing Satellite Image Time Series (SITS) data by focusing on non-redundant patch tubes, which reduces computational demands. The model enhances representation learning through automatic selection of patch tubes and the use of tube masking techniques to address spatial and temporal redundancies. Additionally, SaTran learns task-agnostic representations across the entire time series, thereby increasing the model's generalizability.

### Weaknesses
The paper mentions that the SaTran model requires tuning hyperparameters, such as patch size, number of channels, and traversal ratio, for different satellite datasets. This may indicate that the model has a high dependency on specific datasets, which could limit its generalization ability. Furthermore, the paper primarily focuses on MODIS and Landsat-8 satellite data, and the model's generalization capability on data from other satellite systems remains unclear. The paper also lacks a thorough discussion on how the model adapts to the ever-changing real-world data, especially considering the need for manual parameter adjustments for each dataset. This raises concerns about the practical applicability of the model in diverse and dynamic environments.

### Questions
1. The paper mentions that the SaTran model requires tuning hyperparameters, such as patch size, number of channels, and traversal ratio, for different satellite datasets. Does this indicate that the model has a high dependency on specific datasets, thereby limiting its generalization ability?
2. The paper primarily focuses on MODIS and Landsat-8 satellite data. Will the model's performance be affected when applied to data from other satellite systems?
3. How robust is the model when faced with outliers, noisy data, or incomplete datasets?
4. The comparative methods in the paper are mainly from 2021 and 2022. Are there any more novel methods available?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The identifies spatiotemporal redundancy of SITS data as a distinctive attribute and proposes a transformer architecture that selects non redundant such patches for efficiently processing large samples.

### Strengths
The proposed network is a transformer the can efficiently process large SITS and is capable of both classification and regression tasks. The network increases the maximum size of SITS data that can be processed reducing memory about 50% compared to previous research.

The paper argues that the spatiotemporal redundancy of SITS data is an attribute that current architectures do not optimize for and proposes a method for selecting k-top patches of spatiotemporal tubes that enable good performance at a reduced cost. It is shown to perform above  previous research in MODIS and Landsat data.

The literature review is well writen and comprehensive.

Experiments clearly show improved performance of the proposed framework over several previous SOTA studies.

### Weaknesses
While I believe that the method is sensible and has value, the paper does little in presenting the method in detail. Method part also includes too few citations that could clear out details in formulation or implementation. As its stands now the method cannot be reproduced from information in the main paper alone which is my major concern. Details such as the k-top selection algorithm are not exposed in detail. I believe releasing the code is absolutely necessary for understanding and replicating this work.

From my understanding tube selection constraints the network to global prediction problems and blocks support for dense prediction which is a crucial aspect of remote sensing applications. As such it cannot be used as a general framework for remote sensing.

More details should be given about comparison with other methods and how they were implemented in the data used as none of these works were proposed for the type of data used here and were reimplemented in this study.

Some additional points: 
It is not clear what is the argument made at l.69-75 regarding the size of satellite vs NLP data and how it relates with the proposed method.
In l.172-178 it is discussed how TSViT is not capable of prediction at SITS level, this is not factual as the original study presented such applications. 
In l.195-200 the argument made about redundancies in RGB video data. I disagree with the authors assessment about video data being less spatiotemporally redundant compared to SITS data, especially considering the high frame rate of video data. 
More comments or citation should be given about design components such as trans-convolutional layers.

### Questions
Is dense prediction supported by SaTran?

What is the effect of pretraining on reported performances? What is the performance of the proposed method w/o pretraining?

Can the number of k selected patches be adjusted during inference for a speed-accuracy tradeoff?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents SaTran, an efficient transformer model for Satellite Image Time Series (SITS) representation learning. SaTran aims to improve performance in earth observation tasks (e.g., crop yield prediction, snow cover prediction) by selectively processing non-redundant “patch tubes” within SITS data, thus exploiting spatiotemporal redundancies to reduce computational load. The model incorporates a dual redundancy-handling mechanism, including an automatic patch selection process and the use of VideoMAE to manage temporal redundancy.

### Strengths
1. The proposed redundancy-handling mechanism is helpful for processing high-dimensional SITS data, reducing computational demands in a practical way.

2. The model is evaluated across multiple earth observation tasks, showing its potential in fields like crop yield prediction and snow cover prediction.

### Weaknesses
1. The core ideas of ignoring redundant patches/regions and using masking seem to be inspired from prior works like AdaViT, DynamicViT, VideoMAE, etc. While combining these concepts for satellite data is a reasonable next step, the technical novelty does not seem significantly high. The authors should more clearly articulate the key novel aspects beyond just applying existing techniques to a new domain.

2. The description of the model architecture and modules like PatchTubeSelect, TemporalRedundancyHandler, etc. lack sufficient technical details and clarity. More mathematical formulations and algorithmic specifics are needed. The pre-training tasks also seem relatively straightforward adaptations of prior works.

3. The comparison with state-of-the-art models, such as VSViT and BERT-based models, is limited, which makes it difficult to establish SaTran’s advantages convincingly. A more comprehensive comparison with a broader range of advanced models, combined with ablation studies on different components of SaTran, would be necessary to validate the effectiveness of each element. Furthermore, a deeper analysis of the experimental results is essential to fully demonstrate the impact of the proposed improvements. Such an in-depth evaluation would provide a more persuasive case for SaTran’s effectiveness and contributions.

### Questions
1. How well does the model scale to satellite image time series datasets of higher resolutions and larger time spans? What is the generalization capability of the model to data from other satellite systems (e.g. Sentinel-2)? Would extensive fine-tuning be required?
2.  What are the quantitative improvements in memory usage and runtime compared to existing video transformer baselines? Please provide some concrete numerical evidence.
Does SaTran exhibit better computational scaling characteristics as the dataset size grows larger?
3. How does the attention mechanism for detecting redundant patch tubes work? What features is it based on to determine redundancy?
4. Is SaTran’s redundancy-handling mechanism effective for other types of earth observation tasks?
5. Is there any theoretical foundation supporting the dual redundancy-handling mechanism (especially the use of VideoMAE) that would confirm it reduces computational load without compromising performance?
---
 Some typos: 
1）The writing can be improved for clarity in several sections. There are quite a few grammatical/spelling errors as well.

2）The literature review in Sec. 2. seems incomplete and misses some relevant recent works.

3）Several references within the text are missing from the bibliography section.

### Soundness
3

### Presentation
2

### Contribution
2
