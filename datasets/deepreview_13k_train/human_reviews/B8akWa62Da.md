# Bridging General and Personalized Federated Learning through Selective Model Integration

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Personalized federated learning (PFL) achieves high performance by assuming clients only meet test data locally, which does not meet many generic federated learning (GFL) scenarios. In this work, we theoretically show that PMs can be used to enhance GFL with a new learning problem named Selective FL (SFL), which involves optimizing PFL and model selection. However, storing and selecting whole models requires impractical computation and communication costs. To practically solve SFL, inspired by model components that attempt to edit a sub-model for specific purposes, we design an efficient and effective framework named Hot-Pluggable Federated Learning (HPFL). Specifically, clients individually train personalized plug-in modules based on a shared backbone, and upload them with a plug-in marker on the server modular store. In inference stage, an accurate selection algorithm allows clients to identify and retrieve suitable plug-in modules from the modular store to enhance their generalization performance on the target data distribution. Furthermore, we provide differential privacy protection during the selection with theoretical guarantee. Our comprehensive experiments and ablation studies demonstrate that HPFL significantly outperforms state-of-the-art GFL and PFL algorithms. Additionally, we empirically show HPFL's remarkable potential to resolve other practical FL problems such as continual federated learning and discuss its possible applications in one-shot FL, anarchic FL, and FL plug-in market. Our work is the first attempt towards improving GFL performance through a selecting mechanism with personalized plug-ins.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article proposes a new federated learning framework called Hot-Pluggable Federated Learning (HPFL), which aims to solve the performance gap problem between general federated learning (GFL) and personalized federated learning (PFL). Traditional GFL cannot cope with the diversity of data distribution, while PFL is only suitable for scenarios where local data distribution is similar. When the client encounters test data that is different from local data, PFL's personalized model has difficulty maintaining efficient generalization performance. To this end, this paper proposes a new problem framework of Selective Federated Learning (SFL), which enhances the effect of GFL by selecting an appropriate personalized model for each client in the inference stage. The HPFL framework divides the model into shared backbone and personalized plug-in modules. The client trains and uploads plug-ins based on local data. During inference, it can select appropriate plug-ins to adapt to different data distributions, while protecting data privacy through differential privacy.

### Strengths
Originality：The HPFL framework proposed in this paper innovatively introduces a plug-in selection mechanism into federated learning, realizes the bridge between general models and personalized models, and solves the performance balance problem of traditional GFL and PFL. This is a new attempt in federated learning.

Quality：The experimental part is relatively comprehensive, covering a variety of data sets and model verification, and enhancing security through differential privacy. The overall design is rigorous, and the results demonstrate the advantages of HPFL in performance and adaptability.

Clarity：The paper is well-structured, with clear background and problem descriptions, and clear algorithm design, framework details, and experimental procedures, making it easy for readers to understand its core contributions.

Significance：This study proposed a new solution to the adaptability problem of federated learning under heterogeneous data distribution, which has practical application potential and provides a new direction for the future development of federated learning.

### Weaknesses
·Insufficient details of the selection mechanism (page 5, Section 3.3)：HPFL uses multiple distance metrics such as MMD, SVCCA, and CKA to select plug-ins, but the specific algorithm steps and implementation details are rarely described. The article can add mathematical expressions or pseudocodes for some of the selection methods to increase readability and make it easier for readers to understand the robustness of the selection process.

·Selection of comparison methods (page 7&8, Table 2 and Table 3)：The paper compares a variety of GFL and PFL algorithms, but lacks a comparison of newer solutions that focus on heterogeneous data distribution problems. It is recommended to add more to further highlight the advantages of HPFL in performance and adaptability.

### Questions
·How to balance the computational and communication overheads brought by the storage and selection of personalized plug-in modules in the HPFL framework to improve model efficiency?

·Is it possible that differential privacy protection during model selection in this article, or when using other privacy protection methods, may significantly affect model performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a novel framework called Hot-Pluggable Federated Learning (HPFL) that aims to bridge the gap between generic federated learning (GFL) and personalized federated learning (PFL). The authors propose a new learning paradigm, Selective Federated Learning (SFL), which combines model optimization with model selection. HPFL addresses the challenges of storing and selecting whole models by designing an efficient framework that allows clients to train personalized plug-in modules and upload them to a server. During inference, a selection algorithm identifies suitable plug-in modules to enhance performance on target data distributions. The paper also incorporates differential privacy protection during the selection process. Comprehensive experiments demonstrate HPFL's effectiveness in improving GFL performance and its potential in addressing other FL challenges like continual learning and one-shot FL.

### Strengths
1. The authors identify a substantial gap between GFL and PFL, and formulate a new problem SFL to bridge them together to address this performance gap. Both optimization function of GFL and PFL are the special cases of it.

2. The authors propose a general, efficient and effective framework HPFL, which practically solves SFL.

3. Comprehensive experiments and ablation studies on four datasets and three neural networks demonstrate the effectiveness of HPFL.

### Weaknesses
1. It’s adorable that the authors define a paradigm to bridge the gap between GFL and PFL, but the selective method are not novelty enough. For example, [1] allowed each client to choose the appropriate scale model to train. And the training process in HPFL are identical to the split federated learning, the authors only add another select process in inference process. The selection mechanism, relying on MMD, lacks novelty and is not sufficiently justified as a significant contribution beyond existing model selection techniques. The core idea of selecting pre-trained modules based on data similarity is not new, and the paper does not adequately demonstrate how their specific implementation offers a substantial improvement over existing methods.
2. The authors claim that they theoretically show PMs can be used to enhance GFL with a new learning problem named Selective FL (SFL), which involves optimizing PFL and model selection. But only the statement of the loss cannot totally evaluate the effectivess of the SFL. And in the Eq.4, the greater-than sign \geq should be a less-than sign \leq? The better one should gain the less loss? The theoretical analysis relies on a loss function argument, which is insufficient to fully validate the effectiveness of SFL. The paper does not provide a rigorous analysis of the generalization bounds or convergence properties of the proposed method. The theoretical claims are not adequately supported by the provided analysis, and the connection between the theoretical framework and the empirical results is weak.
3. What’s the originality in the analysis of the privacy protection? It seems that add Gaussian noise to the partial model or full model is identical. Thus I think it’s only an existing result. The application of differential privacy (DP) to the markers lacks originality. Adding Gaussian noise to the markers is a standard DP technique, and the paper does not explore any novel ways of applying DP in this context. The privacy analysis does not provide any new insights into the privacy-utility trade-offs in federated learning.
4. The notations needs to be improved. For example, in section 2.4 the definition of Selective FL (SFL) problem, the introducing of auxiliary information is confused. And in Theorem2.3, the function s(\\. ) lacks description. The notation used in the paper is not clear and consistent. The introduction of auxiliary information H in the SFL problem definition is vague and lacks a clear explanation of its role and properties. The selection function s(.) in Theorem 2.3 is not well-defined, making it difficult to understand the theoretical claims.
5. The presentation in experimental section should be improved. For example, the Table 2 is hard to read. It’s confused that the authors not only give the best result in grey, but also some second best result. And why the proposed HPFL does not gain the best result especially compared to the GFL FedSAM?

### Questions
As shown in the Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Hot-Pluggable Federated Learning (HPFL), a framework aimed at bridging the gap between Generic Federated Learning (GFL) and Personalized Federated Learning (PFL) by proposing Selective Federated Learning (SFL). SFL optimizes PFL while allowing for the selection of personalized models (PMs) to enhance generalization performance across diverse test data. In HPFL, clients train personalized plug-in modules based on a shared backbone model, which are then uploaded to a server for selection during inference. This process also incorporates differential privacy to protect user data during the selection phase. Experimental results demonstrate that HPFL significantly outperforms traditional GFL and PFL methods, suggesting its applicability in various federated learning scenarios, including continual learning.

### Strengths
1. The introduction of SFL effectively addresses the limitations of existing PFL methods, allowing for better adaptation to real-world scenarios where test data may differ significantly from local training data.

2. The HPFL framework’s modular approach enables efficient communication and computation, making it suitable for practical applications in federated learning, including scenarios with resource-constrained clients.

### Weaknesses
1. The dependency on a common backbone model may lead to reduced performance if the backbone fails to generalize well across heterogeneous client data distributions. Specifically, the framework does not adequately address the scenario where the backbone model's feature space is not sufficiently representative of the diverse feature distributions present in the client data. This could result in suboptimal plug-in performance, even with fine-tuning, because the initial feature representations are not well-aligned with the local data characteristics.

2. The plug-in selection process during inference could introduce additional computational delays, particularly for clients with limited resources, potentially hindering real-time performance. The selection process involves evaluating multiple plug-in modules, which requires additional computation and memory access. This overhead is especially concerning for edge devices with limited processing capabilities and could lead to unacceptable latency in real-time applications. The paper lacks a detailed analysis of the computational complexity of the selection process and its impact on different client hardware.

3. While the framework claims differential privacy protection, the effectiveness of this mechanism in preventing information leakage during plug-in selection remains to be empirically validated in diverse operational contexts. The paper does not provide a rigorous analysis of the privacy guarantees under various attack models. It is unclear how the differential privacy mechanism would perform against sophisticated adversaries who may attempt to infer sensitive information by analyzing the selection patterns or the perturbed selection scores.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
After authors responses: The rating has been updated considering the authors' inputs and clarifications. I appreciate their efforts in providing those responses.

In order to solve the selective FL (SFL) problem, this paper leverages the model components that attempt to edit a submodel for specific purposes to design a  framework referred to as Hot-Pluggable Federated Learning (HPFL). In HPFL, clients individually train
personalized plug-in modules based on a shared backbone, and upload them with a plug-in marker on the server modular store. During the inference stage, a selection algorithm allows clients to identify and retrieve suitable plug-in modules from the modular store to enhance their generalization performance on the target data distribution. This paper also provides differential privacy protection during
the selection with theoretical guarantee. Key contributions can be summarized as:
-	Identifying a major gap between Generic FL (GFL) and Personalized FL (PFL), and formulate a new problem SFL to bridge this performance 
-	Developing a general, efficient and effective framework HPFL, which practically solves SFL and adding noise on communicated markers to provide differential privacy protection with theoretical guarantee.
-	Experiments on four datasets and three neural networks to demonstrate the effectiveness of HPFL

### Strengths
The paper is well-written. It fairly cites prior works that it built on and shows how it leverages those solutions. It clarifies what is the problem and what are research questions to answer.
After carefully reviewing authors' clarifying points and responses to my concerns and other reviewers, I increased two of my scores.

### Weaknesses
The originality of this paper is not clear. For instance, the following are two major claimed contributions according to the paper “Identifying a major gap between Generic FL (GFL) [e.g.,  (Karimireddy et al., 2019; Woodworth
et al., 2020; Tang et al., 2022b)'s works] and Personalized FL (PFL) [e.g.,  (Li & Wang, 2019; Chen & Chao, 2021; Li et al., 2021c):'s works], and formulate a new problem SFL to bridge this performance; and Developing a general, efficient and effective framework HPFL, which practically solves SFL and adding noise on communicated markers to provide differential privacy protection with theoretical guarantee.”
However, the methodology seems to be a combination of existing works on PFL while leveraging several existing work with minimal advances. It is not clear how the mentioned theorems add value to the literature, for example, this statement is vague and is not adequately explained: “solving SFL means that clients achieve performance in GFL as high as in PFL.”. It is not clear how plug-in marker can contribute to bridging the gap between GFL and PFL? It would be very helpful to explain elaborately. Specifically, please provide a more detailed explanation and concrete example of how the plug-in markers specifically help bridge the gap between GFL and PFL performance.
While using differential privacy can add value to the method, it is not clear whether it can benefit from local DP, central DP, or both?  Please clarify which type(s) of differential privacy (local, central, or both) are used, and to provide a more detailed explanation of how the plug-ins interact with the DP mechanisms and what novel contributions are made in this area. Specifically it could be explained how plug-ins affect DP and what is the contribution in this part of the paper.
Figure 2 should also include results of HPFL. The comparison should be expanded to cover more advanced PFL studies to showcase how HPFL performs compared to those methods. Currently is mainly focuses on basic PFL algorithms for comparison purposes. For instance, some key papers in this domain can help authors to provide a more compelling comparison among proposed method and existing PFL solutions, such as FedAlt/FedSim of Krishna et al, 2022@ICML and for the specific case of PFL with differential privacy, Hu et al, 2020 @ IEEE IoT Journal.

### Questions
Q1. What is the main contribution of the HPFL that makes it outperform existing PFL models? This could be described by adding a table with core update rule of existing PFLs [including more recent studies] and the proposed method;
Q2. What is the difference of plug-in module and vanilla personalized model? Intuitively they seem to be the same and help considering the local model to personalize the local model of each client.;
Q3. What is the novelty of integrating DP in the algorithm? How does it lead to advancing the proposed HPFL solution? Is it HPFL+DP or the integration has some challenges? If so, what are the challenges and how does this paper tackle them? Why can’t we use other privacy preservation mechanisms? ;
Q4. Detailed comparison with two types of studies: i. existing PFL algorithms and comparing with HPFL, ii. Existing privacy preserving algorithms and comparison with DP;
5. How can the plug-in marker contribute to bridging the gap between GFL and PFL?
Q6. Can you please clarify which type(s) of differential privacy (local, central, or both) are used, and to provide a more detailed explanation of how the plug-ins interact with the DP mechanisms and what novel contributions are made in this area?

### Soundness
3

### Presentation
4

### Contribution
3
