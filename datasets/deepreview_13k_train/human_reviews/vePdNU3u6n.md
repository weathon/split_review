# Towards Robust and Efficient Cloud-Edge Elastic Model Adaptation via Selective Entropy Distillation

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
The conventional deep learning paradigm often involves training a deep model on a server and then deploying the model or its distilled ones to resource-limited edge devices. Usually, the models shall remain fixed once deployed (at least for some period) due to the potential high cost of model adaptation for both the server and edge sides. However, in many real-world scenarios, the test environments may change dynamically (known as distribution shifts), which often results in degraded performance. Thus, one has to adapt the edge models promptly to attain promising performance. Moreover, with the increasing data collected at the edge, this paradigm also fails to further adapt the cloud model for better performance. To address these, we encounter two primary challenges: 1) the edge model has limited computation power and may only support forward propagation; 2) the data transmission budget between cloud and edge devices is limited in latency-sensitive scenarios. In this paper, we establish a Cloud-Edge Elastic Model Adaptation (\methodname) paradigm in which the edge models only need to perform forward propagation and the edge models can be adapted online. In our \methodname, to reduce the communication burden, we devise two criteria to exclude unnecessary samples from uploading to the cloud, \ie, dynamic unreliable and low-informative sample exclusion. Based on the uploaded samples, we update and distribute the affine parameters of normalization layers by distilling from the stronger foundation model to the edge model with a sample replay strategy. Extensive experimental results on ImageNet-C and ImageNet-R verify the effectiveness of our \methodname.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel learning paradigm aimed at enhancing the adaptability of cloud-edge models to address challenges posed by out-of-distribution test samples in real-world scenarios. The proposed approach is both practical and holds substantial significance. Specifically, to reduce communication overhead, the authors have incorporated a dynamic sample filtering strategy, allowing for the identification and exclusion of unreliable and low-informative samples. Furthermore, to further augment the edge model's capabilities and fully capitalize on the abundant cloud resources, the authors have integrated a substantial foundational model to serve as a guiding teacher for the edge model. Extensive experimental results on ImageNet-C and ImageNet-R datasets serves to underscore the efficacy of the presented method.

### Strengths
1.	The proposed collaborative cloud-edge model adaptation (CEMA) paradigm addresses a highly practical problem in the realm of cloud-edge model deployment, emphasizing the challenges of distribution shifts and the limited resources of the edge devices.
2.	The proposed CEMA paradigm is a pioneering achievement in the field. It effectively divides adaptation tasks and distributes them between the cloud and edge devices, resulting in optimized resource utilization and the assurance of robust performance. 
3.	The experimental results demonstrate that the proposed method not only achieves the highest level of out-of-distribution performance but also reduces communication costs by an impressive 60% when compared to SOTAs on the ImageNet-C and ImageNet-R benchmarks.
4.	The paper is well-written and easy to follow. Furthermore, it is accompanied by illustrative figures that enhance its overall readability.

### Weaknesses
1.	In Section Identification on low-informative samples, the author claims that ‘We emphasize that uploading samples does not block the edge from inferring on next incoming samples. In other words, the processes of inference and uploading can be executed simultaneously.’. How do the authors decide which test samples use which updated model to make a prediction? Specifically, if the edge model is updated in the cloud based on a batch of uploaded samples, it's unclear how the edge device ensures that subsequent incoming samples are processed using the most recent model parameters, especially considering the potential for network latency and asynchronous updates. More explanations are required.
2.	In Equation (6), the foundation model assigns pseudo labels to the uploaded samples. Simultaneously, the authors employ entropy to update the model, introducing another pseudo label (the maximum value). It is unclear how these two pseudo-labeling mechanisms interact, and if they might lead to conflicting gradients during training. Furthermore, the justification for using entropy minimization alongside pseudo-labeling is not fully explained. What consequences might arise if the entropy loss is eliminated, and how would this impact the model's ability to generalize to out-of-distribution samples?
3.	In Algorithm 1, line 3, ‘Calculate S(X) via Eqn. (x)’, It is confused what is Eqn.(x).

### Questions
See weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a Cloud-Edge Model Adaptation (CEMA) paradigm for dynamic model adaptation. This approach delegates adaptation workloads to the cloud, thereby reducing the burden on edge devices. To minimize communication overhead, CEMA excludes unreliable high-entropy and low-informative low-entropy samples from uploading to the cloud. The model leverages knowledge distillation from the foundation model to guide the edge model, and a replay buffer is employed to enhance data utilization efficiency. Experimental results demonstrate a 60% reduction in communication costs compared to state-of-the-art methods on ImageNet-C.

### Strengths
* This paper introduces the Cloud-Edge Model Adaptation (CEMA) paradigm, which addresses the dynamic model adaptation problem in a novel way.

* The paper is of high quality, the language is clear, the structure is clean, the related work review in the appendix is adequate (including a valuable comparative analysis with various methods), and the figures are clear and easy to follow.

* The manuscript is very clear in the explanations and the methodology. 

* As a practical method for model adaptation, I think this paper is of great chance to benefit the community, especially in real-world scenarios.

### Weaknesses
The overall framework appears to be somewhat straightforward as it contains multiple steps. The selection scheme used in the paper is relatively simple, as mentioned in Q1.  Additionally, the selection scheme is designed to exclude data that is either entirely out-of-distribution or absolutely in-distribution. There could be alternative methods to identify these two types of data beyond logits. The reliance on entropy of logits as a measure of uncertainty is also a potential weakness, as neural networks are known to exhibit overconfidence, which could lead to misidentification of informative samples. Furthermore, the paper does not explore the impact of different entropy thresholds on the performance of the model, which could be a critical factor in real-world applications. The lack of a detailed analysis of the computational overhead of the proposed method, especially the cloud-based adaptation, is also a concern.

### Questions
Q1. The authors employ the entropy of the logits to assess uncertainty and selectively upload test samples, excluding both unreliable and low-informative ones. However, recent research has pointed out that neural networks can exhibit overconfidence. In such cases, can the uncertainty of a sample still be accurately evaluated based on the logits?

Q2. The sample selection process involves dynamically adjusting the threshold and incorporating more samples into training. This idea seems to be similar to self-paced learning. Can the authors elaborate on the relationship between self-paced learning and their sample-selection scheme?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a Cloud-Edge Model Adaptation (CEMA) paradigm that executes dynamic model adaptation, which puts all adaptation workloads to the cloud and only requires vanilla inference in edges. A replay-based entropy distillation method is also proposed to improve the adaptation performance of the edge model. Extensive experiments show that CEMA achieve SOTA performance with lower communication cost.

### Strengths
1. The proposed cloud-edge model adaptation (CEMA) framework seems novel to me.

2. The CEMA paradigm only requires the edges to perform forward computation, which is important considering that backpropagation on edge is difficult.

3. The proposed dynamic unreliable and low-informative sample exclusion are simple but effective.

4. Extensive experiments and ablation studies are provided. There are large performance improvements over previous methods.

### Weaknesses
1. The proposed method is only evaluated on classification tasks. Could the proposed method be extended to other tasks such as object detection?



### Questions
1. From table 15, it seems that the performance improves as the replay buffer increase. Why not use all the uploaded samples for adaptation?

2. What's the performance if no teacher model is used?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on adapting deep learning models for edge devices with limited resources in dynamic environments. Traditional approaches involve deploying fixed models, which can result in reduced performance as scenarios change. This paper devises the Cloud-Edge Model Adaptation (CEMA) paradigm, in which the edge models only need to perform forward propagation and the edge models can be adapted online, by performing a data filtering strategy to allow high-quality data to be uploaded to the cloud and a replay-based entropy distillation.

### Strengths
1. This paper is well-written, easy to follow.
2. Manage what data to train is a sound approach to reduce training efficiency.
3. Experiments are comprehensive.

### Weaknesses
From algorithmic perspective (low-informative data identification), the novelty is limited. There should be existing papers studied how to filter out low-informative data. These can be added into the paper related works and experiments to compare. The use of entropy as a measure of informativeness, while computationally efficient, is a relatively simple approach. More sophisticated methods, such as those based on gradient norms or uncertainty sampling, could potentially offer better performance and should be considered or at least discussed in the related works. The paper also lacks a thorough analysis of the computational overhead associated with the proposed data filtering strategy. While the authors claim it reduces data transmission, the computational cost of calculating entropy on the edge device and the potential impact on latency should be evaluated and discussed.

### Questions
1. In equation 6, is fθ(x) and the pseudo labels yˆ  the same thing or different?
2. To use KL divergence loss and CE loss together is interesting. I wonder how the hyperparameter alpha and beta change in different dynamic scenarios.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
