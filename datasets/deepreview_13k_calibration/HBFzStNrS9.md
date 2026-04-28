# Unitention: Attend a sample to the dataset

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
We propose an end-to-end trainable module termed Unitention, an abbreviation for universal-individual cross-attention, to improve deep features of a given neural network by attending the feature of a data sample to those of the entire dataset.
This innovation is motivated by two key observations: (i) traditional visual encoding methods, such as Bag of visual Words, encode an image by using a universal dataset-wide codebook, while (ii) deep models typically process every individual data sample in isolation, without explicitly using any universal information.
Our Unitention can bridge this gap by attentively merging universal and individual features, thus complementing and enhancing the given deep model.
We evaluate its efficacy on various classification benchmarks and model architectures.
On ImageNet, Unitention improves the accuracy of different ConvNets and Transformers. In particular, some \knn classifiers with Unitention can even outperform baseline classifiers.
Improvements in fine-grained tasks are more substantial (up to 2.3%).
Further validations on other modalities also confirm Unitention's versatility.
In summary, Unitention reveals the potential of using dataset-level information to enhance deep features.
It opens up a new backbone-independent direction for improving neural networks, orthogonal to the mainstream research on backbone architecture design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to improve the performance of a deep neural network (DNN) by modifying its head structure instead of the backbone structure. Specifically, the authors present a trainable fusion module called Unitention. The basic idea of Unitention is to combine individual feature encoding and universal feature encoding. Specifically, individual feature encoding is just the feature output from a given DNN backbone, while universal feature encoding takes the feature output from this given DNN backbone as the input, and uses a cross-attention module following the self-attention concept in popular transforms to capture sample-to-dataset relations. Then, the output of Unitention is just the sum of the outputs from both individual feature encoding and universal feature encoding. Experiments conducted on image classification (with ImageNet-1K dataset), fine-grained classification (with iNaturalist 2018) and one-dimensional signal classification (with three datasets for device/sensor/medical signals) tasks are provided to show the efficacy of the proposed method.

### Strengths
+ The paper is well written in most parts.

+ The idea of the proposed method is easy to understand.

+ Comparative experiments are performed on three types of benchmarks with different deep neural network architectures including convnets and vision transformers.

+ The proposed method shows improvement to baselines on different datasets.

+ The limitations of the proposed method are also discussed.

### Weaknesses
 - The motivation, the method and related works.

The motivation of this paper is to improve the performance of a deep neural network (DNN) by designing a new head structure, or say enhancing feature encoding for the classification head. 

The authors present Unitention, a trainable fusion module that can be inserted after the backbone structure. The basic idea of Unitention is to combine individual feature encoding and universal feature encoding. Specifically, individual feature encoding is just the feature output from a given DNN backbone, while universal feature encoding takes the feature output from this given DNN backbone as the input, and uses a cross-attention module following the self-attention concept in popular transforms to capture sample-to-dataset relations. Then, the output of Unitention is just the sum of the outputs from both individual feature encoding and universal feature encoding. 

However, the motivation, the idea and the cross-attention design of the proposed Unitention are not new. As a fundamental research topic, there already exist a large number of previous research works that focus on designing a better head structure or enhancing feature encoding for the classification head. Unfortunately, the authors totally ignore this line of research. In what follows, I just list some representative works as well as recent works in this field. 

[1] Mircea Cimpoi, et al. Deep Filter Banks for Texture Recognition and Segmentation. CVPR 2015.

[2] Relja Arandjelovic, et al. NetVLAD: CNN architecture for weakly supervised place recognition. CVPR 2016.

[3] Yang Gao, et al. Compact Bilinear Pooling. CVPR 2016.

[4] Feng Zhu, et al. Learning Spatial Regularization with Image-level Supervisions for Multi-label Image Classification. CVPR 2017.

[5] Mengran Gou, et al. MoNet: Moments Embedding Network. CVPR 2018.

[6] Shilong Liu, et al. Query2label: A simple transformer way to multi-label classification. arXiv preprint arXiv:2107.10834, 2021.

[7] Jiangtao Xie, et al. Sot: Delving deeper into classification head for transformer. arXiv preprint arXiv:2104.10935, 2021.

[8] Ke Zhu, et al. Residual Attention: A Simple but Effective Method for Multi-Label Recognition. CVPR 2021.

[9] Chao Li, et al. NOAH: A New Head Structure To Improve Deep Neural Networks For Image Classification. ICLR 2023 Open Review. 

- The experiments.

As I mentioned above, there already exist a large number of previous research works that focus on designing a better head structure or enhancing feature encoding for the classification head. However, the authors totally ignore them throughout the paper, including in the experimental comparison. Comprehensive comparisons of the proposed method to existing works are necessary.

How about the extra training cost of the proposed method against the baseline?

I would like to the transferring ability of Unitention to downstream tasks as they are more important in real applications.

### Questions
Please refer to my detailed comments in "Weaknesses" for details.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an attention module named Unitention in order to improve the performance of different backbone models with considering the universal information from entire dataset. Unitention takes the output feature vector of a backbone as input and enhances the feature with universal feature from a proposed universal feature bank using cross-attention. The universal feature bank is updated using a momentum mechanism according the classes of input samples. The results show that Unitention demonstrates performance gains on different backbone models and can generalize to multiple modalities.

### Strengths
(1) The proposed method is simple and logical, 

(2) Sufficient experiments with multiple backbones and different modalities are provided. 

(3) This paper is well-written and easy to follow.

### Weaknesses
 (1) Parameters, flops and inference speeds are not provided. It shows that an Unitention module contains multiple FC layers and a feature bank. When applying an attention module to a backbone, it will improve its performance but also increase its parameter and flop usually. The authors should provide the parameters, flops and inference speeds for models with and without Unitention module, so that we can make sure whether Unitention can make a good trade-off between performance and cost. For example, the parameters, flops and inference speeds of ResNet50, ResNet101, ResNet152, ViT-Small, Swin-Tiny with and without Unitention.

(2) The authors considered different models and modalities in the experiments. While Unitention was only tested in single-label global-feature-based classification tasks in the experiments. I think the authors could provide some experimental results of Unitention for different tasks such as multi-label classification to show its generalization ability.

(3) From my point of view, Unitention is an enhanced design of classification head focusing on the information of classes, since it uses feature vectors after the global average pooling operation. I think the authors should compare Unitention with other classification head designs, for example, iSQRT-COV[1]. Or the authors could show that Unitention is complementary with them, which can still demonstrate performance gains on the models with other heads.

### Questions
(1) In the ablation study, how does Unitention update the feature bank when the number of class centers is less than number of classes?

(2) I'm wondering about the performance of Unitention when the feature bank is replaced by trainable parameters. That is, the parameters in the feature bank is updated according to the gradient but not proposed method.

(3) Will the backbones with Unitention still show performance gains when fine-tuned on the downstream tasks such as detection and segmentation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This research introduces a sample-dataset interaction mechanism through cross-attention block, termed Unitention, which contributes to enhance the deep feature for classification. To be specific, the universal distribution for dataset is characterized by a collection of class-specific prototypes, and accumulated in an EMA manner with label annotation. Unitention module is evaluated on multiple architectures.

### Strengths
(+) Adopting the holistic representation to depict the dataset distribution is an interesting exploration. And it maybe inspire to subsequent works.

(+) The universal information and individual information is interacted with a simple-yet-effective cross-attention block.

(+) The proposed method is evaluated on extensive architectures, and obtains healthy gains.

### Weaknesses
(-) The relation between Unitention and codebook/k-NN is somehow overclaimed.

(1) Typically, codebook is constructed using unsupervised methods, often employing K-means. However, in this study, But in this work, it seems that the codebook is dependent on labels. The use of class-specific prototypes, while effective, deviates from the traditional notion of a codebook derived from the data distribution itself, which raises concerns about the method's generality.

(2) Unlike the selection of k-nearest neighbor in k-NN, the unitention module instead aggregates all feature candidates for cross-attention. In fact, it seems that such unitention module does not allow a partial neighbor, i.e., K less than class number, because each candidate responses a specific class. The aggregation of all class prototypes rather than a selection of the most relevant ones, as done in k-NN, might limit the method's ability to focus on the most discriminative information.

Although Unitention shares some commonalities with coding algorithm, it is essential to clearly highlight their differences to prevent misleading readers.


(-) The migration ability for annotated universal bank is limited.
The Universal bank essentially serves as a class prototype, requiring label annotations for aggregation. Such mechanism, which relies on annotation information, faces the challenge when migrating to other downstream task with different categories. The dependence on class-specific prototypes makes the method less adaptable to new tasks where the class distribution might be significantly different or where labels are unavailable. Additionally, such character should be clearly outlined in section 2.2. Moreover, it is advisable to movie the updating principle for universal banks is recommended to section 2.2.

(-) The algorithm is not clearly demonstrated.
As the clarification in paper, the training-free approach is like a variation of k-NN. But how does the classifier come from for test phase? By aggregating training samples? It's unclear how the method transitions from training to inference, especially when the 'training-free' aspect is emphasized. The lack of clarity in how the classifier is formed during the test phase raises questions about the method's practical implementation.

(-) Lack of some empirical studies.

(1) It is recommended to analysis Unitention training/inference efficiency. In particular, the computational and storage demands for the additional 1000xC class-level feature bank. The computational overhead of maintaining and using a large class-level feature bank during both training and inference needs to be thoroughly evaluated, as this could limit the method's applicability in resource-constrained environments.

(2) Lack of the evaluation on other popular vision tasks, e.g., detection or segmentation. The absence of evaluations on tasks like object detection or segmentation limits the understanding of the method's general applicability and its ability to enhance feature representations in more complex scenarios.

### Questions
Other Comments:

Q1: About the hyperparameter analysis on $\tau$. It seems that tuning $\tau$ obtains positive gains with momentum 0.8 setting, i.e. row 7, 9, 10 and 11 in Table 4. Why does fix $\tau$ as 1 finally?

Q2: In Table1, the k-NN accuracy is obtained by the model trained with only k-NN classifier?

Q3: It seems that there is a typo in section 3.2, i.e., BL* in tab:imn -> BL* in tab:1.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a trainable module termed Unitention, an abbreviation for universal-individual cross-attention, to improve deep features of a given neural network by attending the features of a data sample to those of the entire dataset. They are inspired by traditional visual encoding methods, such as bag-of-visual-words, to attend to the entire datasets for visual recognition. The paper validates the effectiveness of this new approach through certain experimental evaluations.

### Strengths
1. The paper proposes an attention mechanism to attend to the entire dataset rather than to individual images for visual recognition,  which is a kind of novel approach.
2. The paper is well-written with good organization.
3. The paper justifies its claim through several good experimental settings. For instance, they performed a training-free study on the attention mechanism to justify their design.
4. They perform detailed experimental evaluation, and the effectiveness of this approach is validated by the improvement of visual recognition performance.

### Weaknesses
While the methods approach the visual recognition problem through a novel perspective, i.e., the contextual information of the dataset, I suspect this is not very fair for the testing scenario, as testing should be performed via individual images, one by one. If one intends to include the contextual information from datasets, one also should not include the extra data in the dataset during the testing phase, otherwise, it is not fair. 
I only have this concern.

### Questions
No other questions, but how is including extra data during the testing phase fair for evaluation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
