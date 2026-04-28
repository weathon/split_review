# Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Multi-modal Large Language Models (MLLMs) frequently face challenges from concept drift when dealing with real-world streaming data, wherein distributions change unpredictably. This mainly includes gradual drift due to long-tailed data and sudden drift from Out-Of-Distribution (OOD) data, both of which have increasingly drawn the attention of the research community. While these issues have been extensively studied in the individual domain of vision or language, their impacts on MLLMs in concept drift settings remain largely underexplored. 
    In this paper, we reveal the susceptibility and vulnerability of Vision-Language (VL) models to significant biases arising from gradual drift and sudden drift, particularly in the pre-training. 
    To effectively address these challenges, we propose a unified framework that extends concept drift theory to the multi-modal domain, enhancing the adaptability of the VL model to the distribution unpredictable changes. 
    Additionally, a T-distribution based drift adapter is proposed to effectively mitigate the bias induced by the gradual drift, which also facilitates the model in distinguishing sudden distribution changes through explicit distribution modeling. 
    Extensive experiments demonstrate our method enhances the efficiency and accuracy of image-text alignment in the pre-training of VL models, particularly in the concept drift scenario. Moreover, various downstream tasks exhibit significant improvements in our model's ability to adapt to long-tailed open world. 
    Furthermore, we create a set of multi-modal datasets called OpenMMlo, specifically tailored for the long-tailed open world settings, to validate our findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a T-distribution based drift adapter for the vision language model to reduce the potential impact of concept drift in real-world data streams. Meanwhile, a multi-modal dataset OpenMMlo is built in a long tail open world setting.

### Strengths
1. This model has good performance on both long-tail and OOD datasets.
2. The motivation of the paper is clear and detailed experiments and pictures are provided as support.

### Weaknesses
1. The introduction and evaluation of the image-grounded decoder and text modeling loss are lacking. The author did not introduce and evaluate this module in the methods and experiments. What is the motivation and function of introducing this module?
2. The setup of the experiment is inappropriate. Although OpenMMlo is presented as part of the paper contribution, it is not sufficient to show only the training results of OpenMMlo, which makes comparisons with other methods unfair and meaningless. The authors are encouraged to align the training strategy with the remaining methods, and the current experiments make it impossible to evaluate both the method and the new data set.
3. The resolution used in the paper is 336x336, and the performance of LIVT should be compared with that of the corresponding resolution.
4. Typos in Fig. 1, 'LL' should be 'LT'.

### Questions
1. The current experiment, which introduces additional data, larger resolution, and additional modules, makes it impossible to effectively evaluate the effectiveness of the method, which is my main concern in giving a rating.
2. The text decoder used in the fine-tuning stage is trained from the pretrain stage, so how could the method only fine-tuning using the pretrained CLIP model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the challenges faced by Multi-modal Large Language Models (MLLMs) due to concept drift in real-world streaming data, which includes gradual drift from long-tailed data and sudden drift from Out-Of-Distribution (OOD) data. While previous research has focused on these issues within the separate domains of vision or language, their effects on Vision-Language (VL) models remain underexplored. The authors propose a unified framework that adapts concept drift theory to the multi-modal context, enhancing the adaptability of VL models to unpredictable distribution changes. They introduce a T-distribution based drift adapter to mitigate biases from gradual drift and improve identification of sudden changes. Extensive experiments demonstrate that their approach enhances image-text alignment accuracy during pre-training and improves performance on various downstream tasks. Additionally, the authors create a new multi-modal dataset, OpenMMlo, designed for long-tailed open-world scenarios to validate their findings.

### Strengths
- *Novel Contribution to Concept Drift in MLLMs*: The paper extends concept drift theory to the multi-modal domain, providing a new perspective on how VL models can adapt to unpredictable changes in data distributions, which is a significant advancement in the field.

- *Effective Mitigation Strategies*: The introduction of a T-distribution based drift adapter effectively addresses biases from gradual drift while distinguishing sudden distribution changes, enhancing the robustness and reliability of VL models under concept drift conditions.

- *Empirical Validation and New Dataset*: The extensive experiments demonstrate the proposed method's effectiveness in improving image-text alignment and performance on downstream tasks. The creation of the OpenMMlo dataset specifically tailored for long-tailed open-world settings adds value to the research community by providing a resource for further studies in this area.

### Weaknesses
 - The authors raise important points regarding the presence of long-tail and Out-Of-Distribution (OOD) issues during the pre-training phase of Multi-modal Large Language Models (MLLMs). However, it would be beneficial for them to clarify why these issues are particularly relevant in the context of pre-training.

Specifically, they should address the following questions:

Relevance of Long-Tail and OOD Issues in Pre-Training: Why do long-tail and OOD issues emerge during the pre-training phase? How do these issues affect the learning process of the model, specifically in terms of feature representation and generalization capabilities? For instance, does the model overfit to head classes in long-tailed data, leading to poor performance on tail classes and OOD samples?

Consideration of Sub-Distribution in Training Data: Should the pre-training process explicitly take into account the different sub-distributions present in the training data, such as variations in image styles, lighting conditions, or text writing styles? What implications does this have for the model's performance and adaptability, particularly when encountering data from unseen sub-distributions? How does the proposed method address the challenges posed by these sub-distributions?

Impact of Long-Tail Issues with Large Datasets: Is the long-tail problem still a concern when the pre-training dataset is large? If so, how does the size of the dataset influence the severity of the long-tail issue, and what strategies can be employed to mitigate its effects? For example, does increasing the dataset size simply amplify the bias towards head classes, or does it offer some inherent mitigation? What are the trade-offs between dataset size and the need for specific long-tail mitigation techniques?

- The used intra-class compactness and T-distribution are somewhat similar to those used in [a]. It would be beneficial to provide a more detailed discussion of the connections between them. Specifically, how does the proposed T-distribution based drift adapter differ from the structurally regularized deep clustering approach in terms of its objective function, optimization process, and the specific way it achieves intra-class compactness? A comparative analysis of the mathematical formulations and algorithmic implementations would be beneficial.

[a] Towards Uncovering the Intrinsic Data Structures for Unsupervised Domain Adaptation using Structurally Regularized Deep Clustering. TPAMI, 2022.

- In Figure 1a, it is unclear whether the test sets used to evaluate the BL (Balanced) or LT (Long-Tailed) trained VL (Vision-Language) models are the same. Additionally, it is important to know if these test sets are balanced in terms of class distribution. The answers to these questions could significantly impact the empirical evaluation results and the conclusions drawn from the study. I recommend that the authors clarify this aspect, as it is crucial for understanding the validity and reliability of the comparisons made between the two pretraining setups. Furthermore, it is important to know if the test sets are balanced across classes, or if they reflect the same long-tailed distribution as the training data. If the test sets are balanced, it would be important to understand how the model performs on tail classes specifically.

- In Figure 1a, it is unclear whether the Out-Of-Distribution (OOD) samples are included in the pre-training of the Vision-Language (VL) model or if they are used solely for evaluation purposes. Additionally, the authors should clarify how OOD drift impacts the pre-training of the VL model. Specifically, does the presence of OOD samples during pre-training lead to a degradation in the model's ability to generalize to in-distribution data, or does it enhance its robustness? It would be helpful to understand whether the performance is assessed on both In-Distribution (ID) test samples and OOD samples after incorporating OOD samples into the training process. This clarification is essential for comprehensively evaluating the model's robustness and adaptability in the presence of OOD drift. It is also important to understand if the OOD samples are from a single distribution or multiple distributions, and how this affects the model's performance.

- In Figure 1b, it is unclear whether the Vision-Language (VL) model used for evaluation has been fine-tuned on a downstream class-imbalanced dataset. Additionally, the authors should discuss whether fine-tuning on a balanced dataset can mitigate the side effects of pre-training on an imbalanced dataset. For example, does fine-tuning on a balanced dataset lead to a better performance on tail classes compared to fine-tuning on an imbalanced dataset, and how does this relate to the model's pre-training on imbalanced data?

- The writing and overall flow of the article should be further improved. Enhancing clarity and coherence will help convey the authors' ideas more effectively.

- In Fig. 1a, 'LL' in the green rounded rectangle should be "LT"?

- In Abstract, “distribution unpredictable changes” should be "unpredictable distribution changes”.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Tailed drift and OOD drift are known issues in the vision and language community. While such problems have seen extensive studies on vision and language separately, it has not been studied jointly in multimodal learning. This paper attempts to bridge this gap. The authors show that pretraining on an imbalanced dataset worsens inter and intra-class as well as OOD features in terms of separability. These drifts further degrade performance in FT. A T distribution adapter is subsequently adopted to mitigate both drifts. The authors release a new long-tailed dataset pertaining. Extensive experiments on FT classification and OOD detection demonstrate the effectiveness of the proposed method.

### Strengths
1. the issue caused by tailed drift and OOD drift (concept shift) is illustrated clearly. 
2. The proposed method seems effective across most settings, barring a few in INat which is reasonable.
3. the proposed method is properly theoretically motivated --I checked most math and they seem to be correct.

### Weaknesses
1. The manuscript lacks clarity on how their proposed method or model family compares to popular models like CLIP. The related work section of MLLM only discusses the common MLLMs but fails to draw a clear comparison to the proposed method. Specifically, it's unclear how the proposed T-distribution adapter and training regime differ from CLIP's contrastive learning approach, and whether the observed improvements are due to the adapter itself or other architectural differences. A more detailed comparison, including quantitative results on the same datasets, is needed to contextualize the contribution.
2. There lacks motivation on exactly how the proposed method work and why they are designed in this way. The entire section 2 is on defining concept shift as well as T-distribution adapter how ever it doesn't address the architecture. While the authors mention that "drives the training of all three modules", more details are needed here. I also think the authors should clearly state how each loss is calculated, for example, on which labels are the CE loss calculated. This helps reader understand, compare and contrast the proposed method with existing solutions. For instance, it's not clear how the T-distribution adapter interacts with the cross-entropy loss, and whether it's applied to the image encoder, text encoder, or both. The lack of clarity on the specific loss functions and their application makes it difficult to reproduce or extend the work.
3. What advantage would training on OpenMMlo have compared to training on WIT? Are there any other benefits it brings to the table besides supporting the long-tailed study of this paper? -- since naturally we would want balanced dataset in the real world. The paper should discuss the trade-offs of using a long-tailed dataset for pre-training, especially when balanced datasets are generally preferred for model generalization. It's not clear if the long-tailed nature of OpenMMlo is a deliberate design choice or a limitation of the data collection process, and how this impacts the model's performance on downstream tasks.
4. In the related work section on MLLM, the authors mentions that "However, most of them used the clip pre-trained model, that it is
pre-trained using high-quality and large-scale WIT dataset. And the VL models will also encounter
concept drift caused by data defects in the pre-training, which is the focus of this paper", can you elaborate more on a) would pretraining on WIT mostly already alleviate the said issue and b) what "also encounter concept drift" mean here, odes it refers to pretraining on WIT? The statement about concept drift in pre-training is vague and needs further clarification. It's not clear if the authors are suggesting that WIT itself has concept drift issues, or if the drift arises when transferring to a new dataset. A more precise definition of the concept drift in the context of pre-training is needed.
5. How do you define long-tailed data in image-caption pairs? Since no class label is given here how do we define these concepts? The paper needs to clarify how the long-tailed distribution is defined in the context of image-caption pairs, especially since there are no explicit class labels in the captions. It's unclear if the long-tail refers to the distribution of image categories, the frequency of words in the captions, or some other metric. A clear definition is crucial for understanding the experimental setup and results.
6. The authors mentioned that both gradual and sudden drifts arise from evolving distributions, I wonder if the pre-training experiments are conducted in the manner of different stages?

### Questions
See Weakness. My question mainly lies in the clarity of the proposed method as well as dataset, the experiments are alright. While I believe this manuscript has its clear merit, I feel several confounding parts bar readers from a clear understanding and practitioners from adopting the method. I'm inclined to increase my score if the authors can answer my questions and make good efforts to modify their manuscript.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new unified framework for Multi-modal Large Language Models (MLLMs) to allviate the concept drift. The objective is to enhance MLLMs to enhance classification performance on long-tailed open datasets. The concept drift theory is introduced and extensive experiments demonstrates the method superior performance in downstream tasks. Finally, a multi-modal datasets named OpenMMlo is built for long-tailed open world setting.

### Strengths
The paper is well-structured and easy to follow.

The paper conducts extensive experiments, including long-tailed classification and OOD detection.

The paper's results show substantial improvements over other state-of-the-art (SOTA) baselines.

### Weaknesses
All downstream tasks only test on vision models, lacking exploration of the overall impact of MLLMs on concept drift. It would be better to provide more experiments, such as long-tailed classification and OOD detection, based on VL models.

It would be better to provide more ablations studies of the T-distributed spherical adapter component, it's not clear that which parts adapt to concept drift and be beneficial to downstream tasks.

### Questions
Besides tailed drift and OOD drift, domain shift is also a common problem in open-world environments, especially in the medical field. Can a T-distribution-based drift adapter be robust to domain shift? It would be better to provide experiments to evaluate this on ImageNet-Sketch.

### Soundness
3

### Presentation
3

### Contribution
3
