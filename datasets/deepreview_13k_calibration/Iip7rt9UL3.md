# Lightweight, Pre-trained Transformers for Remote Sensing Timeseries

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
Machine learning methods for satellite data have a range of societally relevant applications, but labels used to train models can be difficult or impossible to acquire. Self-supervision is a natural solution in settings with limited labeled data, but current self-supervised models for satellite data fail to take advantage of the characteristics of that data, including the temporal dimension (which is critical for many applications, such as monitoring crop growth) and availability of data from many complementary sensors (which can significantly improve a model's predictive performance). We present Presto (the \textbf{P}retrained \textbf{Re}mote \textbf{S}ensing \textbf{T}ransf\textbf{o}rmer), a model pre-trained on remote sensing pixel-timeseries data. By designing Presto specifically for remote sensing data, we can create a significantly smaller but performant model. Presto excels at a wide variety of globally distributed remote sensing tasks and performs competitively with much larger models while requiring far less compute. Presto can be used for transfer learning or as a feature extractor for simple models, enabling efficient deployment at scale.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this article authors proposed Pretrained Remote Sensing Transformer (Presto) a transformer architecture pretrained with remote sensing timeseries imagery. This model can generate pixel-wise feature representation from timeseries imagery from different remote sensing imagery sensors. Presto is pre-trained using a proposed self-supervised objective that leverages the structure and consistency of multi-sensor data. The article argues that Presto achieve competitive or superior performance on multiple geospatial ml downstream tasks like land cover mapping, crop type identification, and fuel moisture estimation, compared to larger models trained from scratch. Authors also comapre performance with other existing self-supervised methods.

### Strengths
* The article is well written, techincally sound, and easy to follow.
* **Reproducibility**. Code have been made available and it is easy to reproduce results. This is also very important to motivate adoption from the community.
* **Generizability**. Presto works well for multiple application tasks and was tested in multiple geographic locations.

### Weaknesses
 * **Resolution constraints**. Most downstream tasks Presto is tested on use coarse resolution. It would be nice to test the effect of encoding different resolution imagery during pretraining. Specifically, the impact of pre-training with higher resolution imagery on downstream tasks that also use higher resolution data should be explored. The current evaluation does not fully demonstrate the model's capability to handle fine-grained spatial information.
* **Small performance gains**. The performance improvement for some of the tasks tested compared to simple baselines is limited. While the model achieves competitive results, the practical significance of these gains, especially considering the increased complexity of a transformer architecture, needs further justification. The marginal improvements in some cases might not warrant the computational overhead.
* **Set of downstream tasks tested**. It is worrisome to me that most self-supervised methods test their proposed approach againg a different set of downstream task maiking it hard to actually compare apporaches. There are multiple other self-supervised approaches that could be used as comparison. The lack of a standardized benchmark makes it difficult to assess the true advancement of this method compared to the broader field.

### Questions
1. Do you have intuition on why the improvement from Presto on TreeSatAi is much larger on S1 than S2 on Teble 4. 
2. Figure 2 would benefit by explaining which channel are missing which channels were masked.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a self-supervised pre-training method for remote sensing pixel timeseries based on masked autoencoders. The pre-trained a Transformer backbone, which is either finetuned or used as a feature extractor in downstream tasks, is shown to have strong performance while having a small parameter count.

### Strengths
The paper deals with an important issue which is model pretraining using remote sensing data. For remote sensing applications of machine learning there exist plentiful unlabelled data directly from satellite while getting ground truths can be challenging, as a result labelled datasets for remote sensing are typically small and taking advantage of large scale unlabelled data through pretraining could bring significant benefits. As discussed, the masked autoencoder framework is by design suitable for dealing with missing data which is a desirable property for remote sensing applications.

### Weaknesses
I believe there are several issues with this paper that need to be addressed by the authors.

1) The application of Transformers to remote sensing should be discussed in more detail, e.g. [1] for pixel timeseries classification and [2] image timeseries classification and segmentation (despite operating on image timeseries base their model design on similar points as bullet points 1, 2 mentioned in the introduction).

2) I believe the importance attributed to small model size is not as significant for the intended use case as it is presented in the paper. While it is always desirable to reduce model size and FLOPS as this reduces both latency, use of computing resources and their environmental footprint, models operating on satellite images will typically run on servers, and there is a limit to the number of inference runs imposed by the size of the area of interest. The revisit time of satellites (5 days for S2) provides a window for inference to run over large areas even with commodity hardware. This is in contrast to models operating on edge devices or models potentially receiving a very large number of calls on servers, e.g. chatbots, in which small model size can be crucial for deployment. If the authors have some specific use cases under consideration these should be presented and the argument should be made why a small model is needed. Also, one of the main findings of deep learning research, the fact the large overparameterized models outperform smaller ones even for small scale datasets, has not been successfully applied to satellite image timeseries in which performance typically drops after a certain model size. On that last part, an ablation in terms of model size would be interesting to showcase how the proposed framework scales.

3) While the authors recognise the need for methods particularly designed for remote sensing data, other than the domain specific inputs,  the proposed method itself does not account for such characteristics, utilising a pre existing framework (MAE) and architectures (Transformers) without significant modifications. 

4) a) In 2.2 the details of tokenization are not clear. Different channel groups are separately encoded to a common latent space of size d_e but it is not clear if these encodings are concatenated channel wise (Fig.1 suggests so, in this case the encoding size of each group should be mentionned) or side by side (E \in R^{T |Cdyn| + |Cstatic| x d_e} suggests so). Also, the paper mentions the use of different learnable encodings for different channel groups, why are these needed if channels have fixed positions over the input? This part needs to be explained better for understanding.

5) Evaluation: a) Several deep learning works for remote sensing are presented in page 1 but these are not used as baselines in experiments despite being shown to outperform non deep learning baselines in original studies. As an absolute minimum, the Presto encoder architecture (Transformer) should be trained from random initialization on all downstream tasks to isolate the effect of pre-training. This is the most important point of critisism i have.
b) In Table 1 random timesteps appears to have practically the same performance as all transformations combined. 
c) Section 3.2 discusses performance in image based tasks despite the model not containing mechanisms for spatial modelling, it basically operates as a deep fully connected network on single pixel features. It has to be clarified what can be derived from such a comparison. In Table 4 it appears that both baselines outperform Presto. In Table 5 experiments it is shown that Presto outperfroms baselines specifically trained on spatial data which is very surprising given that Presto has no understanding of spatial relations and that the MAE family of models are very similar in terms of their pre-training objective. This most probably can be attributed to the fact that there is a train/test input size discrepancy for the baselines. Given that both models operate out of domain not a lot can be derived from this comparison. If the argument is related with the need for reduced algorithmic complexity then this not a fair comparison for the baselines which could be trained at smaller resolutions and be better and less expensive to compute at the same time. Overall, I dont believe that reduced algorithmic complexity can justify the use of a non spatial model in these spatial modelling tasks (see point 2). e) Experimental results should include more performance metrics including pixel based and class based metrics. I propose to move tables from supplementary material to main paper. Also, several captions need to provide more details to make them complete for understanding (Table 1: class or pixel based metric, Tables 4, 5: what are top, bottom?).

### Questions
1) Will the pretraining data be shared as part of the submission to help replication?
2) How does a Transformer trained from scratch in downstream tasks compare with the pre-trained model?
3) Regarding Image based tasks, the reasons why a pixel-timeseries model outperfroms spatial-only models in Table 5 should be analysed. a) What is the baseline performance and FLOPS when trained at test resolution? and what is the performance using 224x224 inputs?
b) Do both baselines and Presto use the same input data or is Presto informed with additional details about location, elevation?  
4) How does Presto scale with model size/pretrain-data/finetune-data size?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a lightweight, pre-trained transformer model called Presto for analyzing remote sensing data. The authors highlight the challenge of acquiring labeled data for training remote sensing models and the need for self-supervised learning approaches. Presto is designed to leverage the temporal dimension and data from multiple sensors in remote sensing data. The model is pre-trained on a diverse range of Earth observation products and achieves competitive performance with state-of-the-art models while requiring significantly less computing. The main contributions of the paper are the introduction of Presto, its competitive performance across various tasks and geographies, and its efficiency in terms of model size and computational requirements.

### Strengths
1. Comprehensive Pretraining Data: The paper mentions that Presto is pre-trained on a diverse range of directly sensed and derived Earth observation products, which can significantly improve model performance. This comprehensive pretraining data helps the model capture a wide range of features and patterns in remote sensing data.

2. Competitive Performance: The paper highlights that Presto achieves state-of-the-art results in a wide variety of globally distributed evaluation tasks. It outperforms benchmark models in many cases, even when used as a feature extractor. This indicates that Presto is effective in capturing relevant information from remote sensing data and producing accurate predictions.

3. Lightweight and Efficient: Presto is described as a lightweight model that meets the computational efficiency requirements of remote sensing settings. It has a small compute footprint, making it accessible and deployable in compute-constrained environments. This efficiency is achieved without compromising performance, as Presto performs consistently well across tasks.

4. Self-Supervised Learning Approach: The paper emphasizes the use of self-supervised learning, which allows for training the model on publicly available data. By leveraging self-supervised learning, the model can learn meaningful representations from the data without relying on extensive labeled datasets.

5. Wide Range of Geographies: Presto is shown to perform well across a range of geographies, spanning four continents and 38 countries. This indicates that the model is robust and generalizable, making it suitable for analyzing remote sensing data from various regions around the world.

### Weaknesses
1. Limited Spatial Context: Presto is designed to process pixel-time series data and does not process very high-resolution imagery natively. This limitation may impact its performance on tasks where spatial information is crucial, such as scene classification challenges. Image-based models that can distinguish the shape of relevant pixels may be better suited for such tasks. Specifically, the model's architecture, which focuses on temporal sequences of individual pixels, inherently limits its ability to capture spatial relationships between neighboring pixels, which are often critical for tasks like identifying specific land cover types or urban structures.
2. Lossy Aggregation of Spatial Information: The paper mentions that Presto uses a crude token-aggregation method to represent images, which may result in a loss of spatial information. This lossy aggregation method can penalize Presto's performance on tasks that heavily rely on the occurrence of objects in subregions of the image. For example, the model might struggle to differentiate between a forest and a group of trees if the spatial arrangement is not well-preserved during the tokenization process. This is because the aggregation might average out the unique spatial patterns that define these different classes. Future work is planned to address this difficulty with Presto.
3. Plateauing Performance with Increasing Input Resolution: The performance of Presto on the EuroSat dataset reaches a plateau as the input resolution increases. This plateauing is mainly caused by a failure to accurately predict specific classes, such as the Highway and River classes. This suggests that Presto may struggle with accurately classifying images where the relevant pixels for a class are a minority of the pixels in the image. For example, a highway might only occupy a small linear portion of an image, and the model's inability to focus on these small but critical areas limits its performance. The model seems to struggle with classes that are spatially sparse or have a high degree of spatial variability within the same class.
4. Lack of Discussion on Specific Limitations: While the paper briefly mentions limitations related to spatial context and lossy aggregation of spatial information, it does not provide an in-depth discussion of these limitations. Further exploration and mitigation techniques for these limitations are mentioned as future work. A more detailed discussion of these limitations would provide a clearer understanding of the model's constraints. For instance, a more thorough analysis of the specific types of spatial patterns that the model struggles with, and a quantitative assessment of the information loss during the aggregation process, would be beneficial.

### Questions
a. How does Presto handle missing or unreliable labels in remote sensing datasets? Are there any specific techniques or strategies employed to mitigate the impact of limited labeled data?  
b. Can Presto effectively handle tasks that require a high level of spatial context, such as scene classification challenges? If not, are there any plans to address this limitation in future work?  
c. How does Presto perform when the input resolution increases? Are there any specific challenges or limitations observed in accurately predicting specific classes at higher resolutions?  
d. Are there any privacy concerns associated with the use of Presto for collecting information about individuals who are unaware that data is being collected? How can these concerns be addressed when deploying Presto in collaboration with local communities and stakeholders?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce the Pretrained Remote Sensing Transformer (Presto) to address challenges in parsing remote sensing data with machine learning, emphasizing the unique temporal and sensor diversity attributes of this data. Presto diverges from traditional self-supervised learning approaches, which often treat remote sensing similarly to natural imagery. Presto is designed to be adaptable across various Earth observation sensors, remains robust despite missing data, and showcases computational efficiency, particularly when compared to models like ViT or ResNet.

### Strengths
##### S1: Tailored for Remote Sensing Data: 
Unlike other models that treat remote sensing data akin to natural imagery, Presto is explicitly designed for remote sensing's unique characteristics, such as the importance of the temporal dimension and the variety of sensors involved.

##### S2: Computational Efficiency: 
Presto, despite its competitive performance, has a significantly smaller model size compared to ViT or ResNet models. This makes it suitable for real-world deployment, especially when processing large volumes of data to make geospatial predictions.

##### S3: The paper is well-written and organized

The paper presents its results in a clear and organized, making it accessible and informative for readers.

### Weaknesses
##### W1: Understanding the proposed method: 

While the proposed methods are effective and efficient, I'd expect more discussions or derivation to illustrate the reason to give insights to understand the framework better. Specifically, the paper lacks a detailed explanation of how the learned encodings for different sensors are implemented and how they contribute to the model's ability to handle multi-modal data. The masking strategy, while mentioned, could benefit from a more in-depth discussion of its impact on the model's ability to capture temporal dependencies and handle missing data. A more thorough explanation of the architectural choices, such as the specific type of transformer used and the rationale behind the chosen dimensionality, would also be beneficial.


##### W2: Literature reviews and comparison of related work: 

Presto is designed to ingest 10m/px resolution imagery and designed to fuse temporal information. I'd suggest authors have further literature review or experiences. For example, for pre-training and downstream tasks, there is a dataset like Extended AgVision[1] with 10m/px resolution and labeled/unlabeled imageries on large scales. For comparison, authors could compare with the backbones of pretrained from seasonal contrast [2] that authors have discussed in the paper. I'd suggested authors give a more comprehensive review and comparison in the related work and experiments section.

### Questions
The main questions are listed in Weaknesses. I'd raise my score if they were appropriately addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
