# Selective Concept Bottleneck Models Without Predefined Concepts

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
There has been considerable recent interest in interpretable concept-based models such as Concept Bottleneck Models (CBMs), which first predict human-interpretable concepts and then map them to output classes. To reduce reliance on human-annotated concepts, recent works have converted pretrained black-box models into interpretable CBMs post-hoc. However, these approaches predefine a set of concepts, assuming which concepts a black-box model encodes in its representations. In this work, we eliminate this assumption by leveraging unsupervised concept discovery to automatically extract concepts without human annotations or a predefined set of concepts. We further introduce an input-dependent concept selection mechanism that ensures only a small subset of concepts is used across all classes. We show that our approach improves downstream performance and narrows the performance gap to black-box models, while using significantly fewer concepts in the classification. Finally, we demonstrate how large vision-language models can intervene on the final model weights to correct model errors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Selective CBMs (UCBMs in the paper) - a novel mechanism that converts any pre-trained model into a CBM. CBMs have been trained using concept annotations in the bottleneck layer which is a significant drawback. To solve this, authors take inspiration from Post-hoc CBMs [1] wherein the concepts are "discovered" in the latent (feature) space and then can be combined together in an interpretable manner to make the final label prediction. UCBMs first decompose (non-understandable) features into an interpretable set of concept representations using a sparse matrix [This is where the problem is formulated as a dictionary learning objective]. Next, the concepts learned are assigned scores based on cosine similarity with the features - giving them weights corresponding to their impact on prediction. The final weight matrix W is also regularized to be sparse. In addition, input-dependent concept selection has been proposed to only select a few concepts as multiple works show that only a few concepts are responsible for prediction. Experiments are performed on ImageNet, CUB, and Places365 wherein UCBM beats [1]. Lastly, the authors demonstrate that UCBMs are intervenable.

[1] POST-HOC CONCEPT BOTTLENECK MODELS, Yuksekgonul et al.

### Strengths
1. The paper is well-written and easy to understand. The proposed method is pretty straightforward and builds on top of known and effective approaches.
2. The Human user-study design is well-documented and clear validating some of the author claims regarding the qualitative analysis of concepts detected.
3. Code is readily available to replicate the results.

### Weaknesses
1. Lack of novelty: In my opinion, UCBM makes two distinct assumptions. First (well-grounded) - concepts form the basis of the latent space and can be linearly decomposed into concepts using a sparse matrix which has been well studied in [2,3]. Second, the novel concept selection module has been utilized in [4,5,6] wherein an auxiliary branch is utilized to directly predict 'the most important' concepts for predictions. This severely limits the novelty of the proposed modules.
2. Interpretability of $C$'s: I have some doubts over the effectiveness of the concepts $C$ as an interpretable unit. As shown in [7], even feature activations can be an effective interpretability metric if properly tuned. Refer Fig 6 in [7] where the most activating prototypes are aligned. In contrast to [1] UCBM has no pre-selected prototypes making the interpretation of each concept in $C$ ambiguous and up to the user's choice.
2a. Weakness 2 makes me apprehensive about the results in Table-1. UCBM w/o concept selection is basically a Black-box model with some added sparsity regularization and the supposed presence of "interpretable" concepts. In my opinion, "w/o concept selection" row is not a significant metric to judge the efficacy of this approach.
3. As the work focuses on unsupervised concept discovery, some experiments with models such as SENN [7] or similar approaches should be performed. One metric that could have demonstrated good concept decomposition is the diversity between each c ($\in$ C) and how different they are to each other.
4. Lacking Experiments:  The experiments have only been performed on 3 datasets with only CNN model architectures. As a truly generic approach, experiments on ViT-based architectures should also be performed.
5. Doubts over utilizing similarity between activations and concepts as scores: What does a high or low score imply? Let's say the similarity value is 1, does it imply that the activation is in itself interpretable? I fail to understand why such a measure should be used and cannot learned automatically.



[2] Interpretable Basis Decomposition for Visual Explanation, Zhou et al., ECCV

[3] Uncovering Unique Concept Vectors through Latent Space Decomposition, Grazini et al., TMLR

[4] Learning Bottleneck Concepts in Image Classification, Wang et al., CVPR

[5] A Framework for Learning Ante-hoc Explainable Models via Concepts, Sarkar et al., CVPR

[6] Self-explaining Neural Architecture for Generalizable Concept Learning, Sinha et al., IJCAI

[7] Towards Robust Interpretability with Self-Explaining Neural Networks,  Alvarez-Melis et al. NeurIPS

### Questions
See Weakness and also:

1. Why is the paper titled "Selective"? I would recommend changing the title of the paper or the UCBM acronym itself to align with each other. The title states the word "Selective" but it has never been used again in the paper itself.
 
2. CBMs are known to be fragile and can cause "leakage". Does UCBM also face similar problems? Were any experiments performed in this direction?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes learning post-hoc Concept Bottleneck Models (CBMs) in an unsupervised manner. Understanding and improving CBMs is important for improving the interpretability of classification models. This paper uses an unsupervised non-negative matrix factorization to decompose the feature vectors into concept vectors, proposes an input-dependent alignment score selection, and finally learns a sparse linear layer for class prediction from the alignment score.  Experiments and visualizations demonstrate the superior performance of the proposed method on Imagenet, CUB and Places365 dataset.

### Strengths
1. Unlike previous methods, UCBMs do not assume a set of concepts learned by black-box models. Instead, the concept vectors are discovered by non-negative matrix factorization in an unsupervised manner.
2. The idea of input-dependant sparsity constraint is interesting and non-trivial, and the paper explores multiple candidate functions.
3. The paper demonstrates applications of the proposed method by correcting errors in model predictions by updating weights of the sparse linear layer using VLM's.

### Weaknesses
1. The proposed method has limited novelty. This paper uses an existing matrix decomposition method called CRAFT for feature generation, and the novelty of this paper is limited to proposing input-dependant selection applied before learning the sparse linear layer.
2. The paper lacks comparisons with the newer methods in terms of performance and sparsity[1,2,3]. Particularly, this work should be compared to [2], which trains a learnable dictionary to approximate the embedding space of VLMs in a supervised manner without using a pre-defined concept set.
3. The paper lacks results on CIFAR-10 and CIFAR-100 datasets and shows results on just three datasets. To demonstrate the applicability of this method in wide scenarios, the results should be provided on additional datasets, including Actions: UCF-101, Textures: DTD, and Skin tumors: HAM10000 following [2].
4. The paper does not provide any quantitative results on the quality of descriptions assigned with VLMs.

[1] An Yan, Yu Wang, Yiwu Zhong, Chengyu Dong, Zexue He, Yujie Lu, William Yang Wang,
Jingbo Shang, and Julian McAuley. Learning concise and descriptive attributes for visual
recognition. In ICCV, 2023.

[2] Yue Yang, Artemis Panagopoulou, Shenghao Zhou, Daniel Jin, Chris Callison-Burch, and Mark
Yatskar. Language in a bottle: Language model guided concept bottlenecks for interpretable
image classification. In CVPR, 2023.

[3] Srivastava, Divyansh, Ge Yan, and Tsui-Wei Weng. "VLG-CBM: Training Concept Bottleneck Models with Vision-Language Guidance." arXiv preprint arXiv:2408.01432 (2024).

### Questions
Please see weaknesses

### Soundness
3

### Presentation
3

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
This paper proposed a novel type of CBM called UCBM, which utilizes concept discovery methods to discover concepts learnt by pretrained, black-box models and convert them into CBM. Additionally, a novel input-dependent concept selection mechanism is proposed to dynamically retain a sparse set for prediction.

### Strengths
* The paper proposed an unsupervised concept discovery mechanism for CBMs, which is novel in the field of CBM. The method does not need pre-defined concept sets. 
* The paper designed an input-dependent concept selection mechanism to increase sparsity of model decision. Empirical results show improved prediction accuracy with sparse activated concepts.

### Weaknesses
1. The idea of input-dependent concept selection is not novel: For example, [1] introduced a binary latent indicator to dynamically select activating concepts according to input embedding and mask out other concepts. A thorough discussion on the difference between proposed method and previous work and empirical comparison on performance will be needed to clarify the contribution of this work. 
2. The concepts discovered is represented visually instead of textually. From my view, textual concept representation is an important feature of CBMs as it provides more concise and user-friendly description. I agree that the introduction of unsupervised concept discovery into CBM is interesting but the missing of text representation limits the novelty. 

[1] Panousis, Konstantinos Panagiotis, Dino Ienco, and Diego Marcos. "Sparse linear concept discovery models." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Questions
1. In user study, how is the most activating image crops of UCBM's concepts labeled? (Line 1277) If they are labelled by human, I think this setting is not very scalable. Adding experiments on (1) explanations with no text labels are displayed (2) explanations with text labels generated by large vision-language models (e.g. in Appendix I) will help understand the dependency of proposed approach on human labeling.
2. In line 431, "we ran a grid search on the training set ofImageNet to find optimal weighing factors βi ∈ [0, 1] for each proposed change ∆Wi". Shall it be "weighting factors"? How is the weight adjusted according to the factor and how is the grid search conducted? Also, since the process is automated, adding more quantitative results, e.g. edit success rate will help reader better evaluate the effectiveness of proposed editing method.

### Soundness
3

### Presentation
2

### Contribution
2
