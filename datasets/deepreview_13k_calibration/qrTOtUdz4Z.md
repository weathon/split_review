# Composing Novel Classes: A Concept-Driven Approach to Generalized Category Discovery

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
We tackle the generalized category discovery (GCD) problem, which aims to discover novel classes in unlabeled datasets by leveraging the knowledge of known classes. Previous works utilize the known class knowledge through shared representation spaces. Despite their progress, our analysis experiments show that novel classes can achieve impressive clustering results on the feature space of a known class pre-trained model, suggesting that existing methods may not fully utilize known class knowledge. To address it, we introduce a novel concept learning framework for GCD, named ConceptGCD, that categorizes concepts into two types: derivable and underivable from known class concepts, and adopts a stage-wise learning strategy to learn them separately. Specifically, our framework first extracts known class concepts by a known class pre-trained model and then produces derivable concepts from them by a generator layer with a covariance-augmented loss. Subsequently, we expand the generator layer to learn underivable concepts in a balanced manner ensured by a concept score normalization strategy and integrate a contrastive loss to preserve previously learned concepts. Extensive experiments on various benchmark datasets demonstrate the superiority of our approach over the previous state-of-the-art methods. Code will be available soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the problem of Generalized Category Discovery, which aims to assign unlabeled samples with both known and unknown class clusters. 
To tackle this problem, they propose a concept-based framework, ConceptGCD, which introduces a concept generation module and a novel covariance loss to derive new concepts of novel classes from known classes, and consequently learn independent underivable concepts for novel classes. They evaluate the proposed ConceptGCD on six GCD benchmarks and demonstrate the effectiveness of their method.

### Strengths
S1. They design a novel two-branch concept-based architecture, which introduces a novel shared derivable concept learning branch that consists of a frozen labeled known classes pre-trained encoder to capture concepts of known classes, which are then used to generate the derivable concept of novel classes. With this shared branch, the model can boost the representation learning of unlabeled samples with concepts learned from known classes.

S2. For the final model to be fine-tuned jointly, they expand the derivable concept generate layer to learn more independent concepts of novel classes with proposed knowledge transfer constraint, and a normalization term is introduced to balance the learning process between labeled and unlabeled samples.

S3. They elaborately design a three-stage training strategy for the proposed ConceptGCD to alleviate the influence of the noise introduced by the uncertainty of unlabeled samples.

S4. They provide sufficient analysis of each component of proposed ConceptGCD, includes detailed ablation study on each loss and neuron layer, and visualization of distribution of whole representation space and concept.

### Weaknesses
W1. As mentioned in Line 243, “When the batch size B is sufficiently large, ...”, could you show the performance tendency when batch size is changed, especially when it is small?

W2. The proposed covariance loss is only implied on top-m dimensions of the feature, and there is no explicit constraint for other n-m dimensions of the feature, why do these underivable concepts have no constraint and how does this loss influence these parts of the feature?

W3. The implement detail of the set of negative samples in Line 285, is not expressed in this paper.

W4. Could you try to explain the significant gains achieved in Stanford Cars? and why this dataset is not shown in the T-SNE and the concept visualization?

W5. In Tab. 12, when EL dim = 10.0m the performance remains comparable to EL dim = 5.0m, except for CUB, could you please analyze this phenomenon?

W6. Could you do the mean-variance analysis for the main results to show the stability of the proposed method?

### Questions
Please justify the issues in Weaknesses.

### Soundness
3

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
4

### Summary
This paper addresses the GCD problem by introducing ConceptGCD. The paper mentioned that this framework can enhance class discovery by categorizing concepts as either derivable or underivable from known classes and learning them in stages by using a generator layer with a covariance-augmented loss and a concept score normalization strategy

### Strengths
1. The paper is well-organized and clearly written, making the methodology straightforward to follow.

2. It presents a novel approach, ConceptGCD, which introduces a concept categorization strategy to assist with novel class discovery in generalized category discovery.

### Weaknesses
1. The abstract mentions that "analysis experiments show that novel classes can achieve impressive clustering results on the feature space of a known class pre-trained model," Is the corresponding evidence from Table 1? It's unclear to me, would you give more explanation on it?

2. There is no clear definition or description of "concept"（mentioned in the introduction and method）  and its distinction from class in the paper, nor are "derivable" and "underivable" concepts (mentioned in both introduction and method) adequately defined. I would suggestion to provide detailed definitions and examples of derivable and underivable concepts.

3. The definitions of key variables \( n \) and \( m \) in lines #289-290 are unclear, yet they appear important to the framework. Additionally, there is no ablation study on the impact of \( n \) and \( m \).  Please provide clear definitions of n and m, explain their significance to the framework, and conduct an ablation study to demonstrate their impact on the model's performance.

4. The generator and expansion layers increase the model size, and it is unclear if the performance gains are due to the larger model rather than the proposed method. The baseline models need to be scaled similarly to ensure fair comparisons. I suggest conducting additional experiments with scaled baseline models to isolate the effect of their proposed method from the impact of increased model size.

### Questions
1. Clarification on Line #41-31: The paper states that “sharing encoder makes it challenging to transfer knowledge between labeled and unlabeled data and can be susceptible to the label uncertainty of unlabeled data.” However, crNCD focus on transferring class-relation information between known and novel classes, without suggesting that shared encoders are susceptible to label uncertainty in unlabeled data. Could you clarify this interpretation?

2. Proof of Derivable Concepts’ Utility: The paper claims, “Intuitively, these derivable concepts are one of the key reasons why known class data can help the model learn novel class data in GCD problems.” Could you provide experimental or theoretical proof for this statement? Additionally, the concept is similar to existing works [1,2]; a comparison would strengthen the paper.

[1] Meta Discovery: Learning to Discover Novel Classes Given Very Limited Data
[2] Supervised Knowledge May Hurt Novel Class Discovery Performance

3. Details on the Linear Layer in the Derivable Concept Generator: The paper describes a linear layer and a ReLU layer after the encoder for derivable concept generation, trained with a covariance-augmented loss. How large is this linear layer? Given that larger models typically improve performance, could this impact baseline comparisons?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the task of Generalized Category Discovery (GCD), which aims to group mixed visual data from base and novel classes by leveraging representations learned from semantically related base classes. This task is closely related to open-world semi-supervised learning. In the preliminary study, the authors observed that existing works might not fully leverage the known knowledge (concepts) from base classes. To this end, this paper proposes a novel framework, ConceptGCD, that uses a covariance loss to learn distinctive concepts to facilitate category discovery. The framework is well-designed to allow the model to use both "derivable concepts" to aid novel class discovery while also enabling the model to learn "underivable concepts" that are customized to novel classes. A covariance loss is used to promote diversity in concept learning. The experiments show consistent improvements over the compared methods on both base and novel classes.

### Strengths
- This paper is well-structured.
- The related works are comprehensively discussed.
- Strong performance is achieved across six benchmarks, with the proposed method outperforming previous approaches.
- The comparison of methods is comprehensive.

### Weaknesses
 **Major:**
- The validity of the experiment is questionable: When DINOv1 (self-supervised on ImageNet) is used as the backbone, the novel classes of CIFAR-100-80 and ImageNet-100-50 are not novel. When DINOv2 (trained on curated ImageNet, CUB, StanfordCars, FGVC) is used as the backbone, except for the novel classes of Herbarium19, all the novel classes in the evaluated datasets are not novel. The backbone was self-supervised on all the classes already (seen). Under this experimental setting, are the "Concepts" for base/novel classes learned via the proposed framework or via the backbone pre-training? I have my doubts about this. One suggestion is that it would be beneficial to apply the proposed method on a ResNet model trained from scratch, as this would isolate the influence of backbone pre-training, helping us better understand the effectiveness of the proposed framework.
- The method requires prior knowledge of the number of clusters. Of course, this is a minor concern, as this limitation is common to most GCD works.
- The novelty of the proposed framework is limited: the major contribution is the application of covariance loss in GCD.

**Minor:**
- The English writing should be improved-i.e., “Despite their progress, our analysis experiments show that novel classes can achieve impressive clustering results on the feature space of a known class pre-trained model, suggesting that existing methods may not fully utilize known class knowledge.” (P1#L14): Novel classes should not be the subject for "achieve impressive clustering results." Instead, the correct logic should be: "Impressive clustering results are achieved on novel classes."
- From Fig. 1 and the introduction section, I could not understand: i) what are "derivable concepts"?; ii) how are they generated? This makes the introduction very vague. It would be better to provide the definition or description about the ``concepts'' because the meaning of "concepts" in this paper's context is different from common semantic concepts.
- The motivational insights claimed in the introduction section are not convincing. To confirm the influence of "derivable concepts," further control experiments and qualitative analysis are needed.
- The notation is unclear: 1) At P4#L193-L194, what do $l$ and $l'$ represent? This is only explained on the next page; 2) In Eq.2, $z_{i}$ should be in bold $\mathbf{z}_{i}$ to represent a vector.

### Questions
**Questions:**
- The authors claimed, “Intuitively, these derivable concepts are one of the key reasons why known class data can help the model learn novel class data in GCD problems.” (P1#L50) —> My question is, how is this claim supported or demonstrated? (Such as through previous studies or experiments). NCD/GCD is essentially a clustering problem. The key idea/motivation from DTC [1] is to leverage the representation (prior knowledge) learned from base classes to reduce ambiguity when clustering novel classes. In other words, the “clustering criteria” is defined by the base classes, allowing NCD/GCD methods to group novel data under the criteria defined by the base classes. How do the derivable concepts help in this case, and how do the authors prove it?
- The authors claimed, “This observation suggests that existing approaches may struggle to capture all the derivable concepts useful for knowledge transfer.” (P2#L65) —> Could you please further explain why the results in Table 1 support this claim? Why is the relatively lower performance of SPTNet and crNCD attributed to a "struggle to capture all the derivable concepts"?
- My major question is: How are the "Derivable concepts" defined? From what I understand from the Method section, a "concept" is a scalar value (an element) of an image embedding vector. Why is this defined as a concept?
- Why are the "concepts" denoted as semantic visual cues in Fig. 2? Based on the description in the paper, "a concept" is a scalar value. What makes these concepts represent the semantic visual cues such as "window," "wheel," or "headlight" in Fig. 2?
- Furthermore, since the "concepts" are illustrated in Fig. 2 as visual components (e.g., a wheel), I wonder how the values of "concepts" would change when attributes (e.g., color or shape) change within the same class? To be more specific, for the same car model, the wheel color might change significantly (so-called large intra-class variance challenge in fine-grained visual recognition, e.g., StanfordCars). In this case, how would the "concept" values change?
- Lastly, an open question: The main goal of NCD/GCD is to **discover** novel classes, which are **unknown**. Since novel classes are unknown, how can users/practitioners know the number of novel classes a priori? Could the authors please provide some practical application scenarios that satisfy the GCD setting?

**Some suggestions:**
1. The current paper’s description and definition of "Concepts" are unclear and contain several unverified subjective assumptions, which may confuse readers. The proposed method performs well, so explaining it in a clear, technical manner would make it easier for readers to understand and be convinced. Including too many subjective descriptions without experimental evidence may weaken the credibility of the proposal.
2. The authors could design experiments that do not use DINOv1 or v2 to validate the proposed idea. The absolute performance does not need to be high; the goal is to isolate representations learned from large-scale pretraining and solely validate the effectiveness of the proposed method.
3. More comprehensive motivational experiments should be designed to demonstrate the influence of "concepts."

[1] Kai Han, Andrea Vedaldi, and Andrew Zisserman. Learning to discover novel visual categories via deep transfer clustering. In ICCV, 2019.

### Soundness
2

### Presentation
2

### Contribution
2
