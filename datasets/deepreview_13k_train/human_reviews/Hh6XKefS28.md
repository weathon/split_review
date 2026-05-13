# Croppable Knowledge Graph Embedding

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Knowledge Graph Embedding (KGE) is a common method for Knowledge Graphs (KGs) to serve various artificial intelligence tasks. The suitable dimensions of the embeddings depend on the storage and computing conditions of the specific application scenarios. Once a new dimension is required, a new KGE model needs to be trained from scratch, which greatly increases the training cost and limits the efficiency and flexibility of KGE in serving various scenarios. In this work, we propose a novel KGE training framework MED, through which we could train once to get a croppable KGE model applicable to multiple scenarios with different dimensional requirements, sub-models of the required dimensions can be cropped out of it and used directly without any additional training. In MED, we propose a mutual learning mechanism to improve the low-dimensional sub-models performance and make the high-dimensional sub-models retain the capacity that low-dimensional sub-models have, an evolutionary improvement mechanism to promote the high-dimensional sub-models to master the knowledge that the low-dimensional sub-models can not learn, and a dynamic loss weight to balance the multiple losses adaptively. Experiments on 4 KGE models over 4 standard KG completion datasets, 3 real application scenarios over a real-world large-scale KG, and the experiments of extending MED to the language model BERT show the effectiveness, high efficiency, and flexible extensibility of MED. The code and data are available at https://anonymous.4open.science/r/MED-DBFC.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Knowledge Graph Embeddings (KGEs) project entities and relationships into a continuous vector space and are widely applied in tasks like link prediction. Typically, increasing the embedding dimension enhances performance, yet device capabilities and storage limitations often dictate the feasible dimensionality. This paper tackles this issue by introducing a novel training framework, named MED, designed to train adaptable KGEs that work across various dimensions suitable for different scenarios.
The MED framework includes several modules: a mutual learning mechanism, an evolutionary improvement mechanism, and dynamic weight loss. In the mutual learning mechanism, the smaller-dimension model acts as a teacher to the higher-dimension model (the student), helping the student model retain knowledge from the higher-dimensional embeddings. To further refine the higher-dimension model by addressing what the teacher model has missed, the evolutionary improvement mechanism leverages hard labels and a weighted loss approach. Dynamic loss weighting is achieved through a weighted combination of these losses.
The proposed MED method has been evaluated on multiple datasets and compared with various embedding techniques, including distillation-based approaches. Results demonstrate the effectiveness of MED in improving performance across different embedding dimensions.

### Strengths
– The core idea and motivation of the paper are sound, and such approaches are essential to support real-world applications.

– The experiments have been done across a wide range of datasets from smaller ones to large one (SKG). In addition, the authors show their approach is general and can be extended to other machine learning models such as BERT. Thus the model may have a high impact beyond KGE models.

– In very low dimension, e.g., 10d the method shows superior performance comparing to other models.

– the approach seems to be more efficient than previous approaches, e.g., knowledge distillation.

### Weaknesses
– In high dimension, the results are not better than other models in most cases.

– The technical contribution of the paper is not very significant. The main loss is combination of two existing losses. Moreover, the equation 4 is the same as equation 5 in the RotatE paper (the only difference is that equation 4 is used for two model, please add citation).

### Questions
Which patterns are learnt in high dimension that cannot be learned in low dimension?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of efficiently adapting Knowledge Graph Embedding (KGE) models to various dimensional requirements without retraining from scratch. It introduces a novel KGE training framework called MED, which allows for the extraction of sub-models with specific dimensions from a single trained model, utilizing a mutual learning mechanism and adaptive loss weights. The results demonstrate that MED enhances performance across multiple KGE models and application scenarios, providing greater efficiency and flexibility compared to traditional methods.

### Strengths
1. The proposed method aims to train once to get a croppable KGE model applicable to multiple scenarios with different dimensional requirements, which is an interesting topic.
2. The authors improve the low-dimensional sub-model's performance and make the high-dimensional sub-models retain the capacity that low-dimensional sub-models have, which seems reasonable.

### Weaknesses
1. The paper is not organized clearly, which is not friendly for understanding. For example, there is a lack of preliminary details on how the previous knowledge distillation methods do.

2. The novelty of this paper seems limited since knowledge distillation has already been used in the previous work [1].
[1] Lifelong embedding learning and transfer for growing knowledge graphs

3. The paper lacks the analysis of time complexity as well as space complexity, which is necessary to study the efficiency of the model. 
4. The authors do not compare the model with other SOTA KGE methods, e.g.,[1][2][3]. The performance of, MRR of these models in FB15K-237 is 0.36 while that of the proposed paper is 0.323. In this way, the performance of the proposed paper is not significant and the authors may better give a reasonable explanation.
[1] Compounding Geometric Operations for Knowledge Graph Completion
[2] Geometry interaction knowledge graph embeddings
[3] KRACL: Contrastive Learning with Graph Context Modeling for Sparse Knowledge Graph Completion

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a croppable knowledge graph embedding training framework MED. This MED is consisting of three modules. The first mutual learning mechanism is mutual learning mechanism that is used to make the two submodels learn from each other. The second evolutionary improvement focuses on enabling the high-dimensional submodel can get the knowledge that low-dimensional model cannot predict correctly. The final mechanism is the dynamic loss weight for balancing the multiple losses of submodels.

### Strengths
Strengths:

1.	This paper presents an interesting problem that is how to train a croppable KGE so that more different dimensions can be cropped from the embeddings. The whole idea is clear and easy to follow in this paper.

2.	A framework MED is proposed for serving the purpose of croppable embeddings. This framework is consisting of multiple sub-models. The low dimensional models are similar to our original KGE. Authors want to improve the performance as much as possible. The high dimensional models are more different because they need to master the knowledge that low-dimensional sub models cannot learn well. Here the “master” is not easy to understand. It is designed for high-dimensional model can make a better prediction based on the prediction of low-dimensional model based on the evolutionary improvement mechanism.

### Weaknesses
Weaknesses:

1.	The ablation studies are needed for this paper. The MED includes three modules: mutual learning mechanism, evolutionary improvement mechanism and a dynamic loss weight. It is very important to evaluate the effectiveness of each module and discuss if there is any alternative solution here. For instance, can we just duplicate a model that dimension d is small num n times and use the evolutionary improvement mechanism to tune them for satisfying the target that high-dimensional models need to master the knowledge that low-dimensional model cannot predict.

2.	It is not clear about how to choose the dimension size of each sub-model and define the number of sub-models. 

3.	For the mutual learning mechanism, the purpose is to make two models learn from each other, while the evolutionary improvement mechanism is to make high dimensional model learns more knowledge that low-dimensional model cannot predict. Will the purposes of these two losses opposite？

### Questions
Please check the weaknesses and answer the questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In conventional KGE approaches, each change in embedding dimensions necessitates retraining the entire model from the beginning. This paper aims to train a single KGE model that can be "cropped" into sub-models of various dimensions without additional training, thus reducing the overhead and enhancing the flexibility of KGE applications.

### Strengths
1.The idea of the croppable KGE is interesting and makes sense. 
2.The manuscript is well-organized and easy to follow
3.Authors provide extensive experimental results, especially on real-world applications and LMs

### Weaknesses
1.The authors claim one of major contributions is that “the training efficiency of MED is far higher than that of independently training multiple KGE models of different sizes or obtaining them by knowledge distillation.” This comparison seems unfair because the multiple models in MED are parameter sharing. I expect to see some impressive techniques to reduce redundant gradient calculations, instead of a rough procedure of iterative model-pair training. This makes the technical contribution limited.

2.In experimental settings, configuring 64 sub-models represents a significant investment in resources. However, in practical applications, training such a large number of models with varying dimensions is often unnecessary. Typically, it is adequate to develop models for a few key dimension settings that cater to the requirements of servers, PCs, and mobile devices. While increasing the number of sub-models might enhance training performance, this approach can be excessively time-consuming and resource-intensive in real-world scenarios. Therefore, it would be more convincing to evaluate the effectiveness and efficiency of the multi-submodel MED by comparing it against the traditional method of training three specifically dimensioned models tailored to the aforementioned application settings.

3.In MED, there are many learnable weights. It would be useful to know about the robustness of the training and the time it takes for the training to converge. Providing a curve showing how the training loss/metric changes over time would be even more informative.

4.Compared to training 64 sub-models, I am curious about the performance when training different numbers of sub-models. (No need to provide comprehensive results in the rebuttal phase.)

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
