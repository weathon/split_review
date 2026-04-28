# MSfusion: Enabling Collaborative Training of Large Models over Resource-Constraint Participants

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6

## Abstract
Training large models like GPT-3 requires a large amount of data, as well as abundant computation resources. While collaborative learning (e.g., federated learning) provides a promising paradigm to harness collective data from many participants, performing training for large models remains a major challenge for participants with limited resources. We introduce MSfusion, an effective and efficient collaborative learning framework, tailored for training large models on resource-constraint devices through model splitting. Specifically, a double shifting model splitting scheme is designed such that in each training round, each participant is assigned a subset of model parameters to train over local data, and aggregates with sub-models of other peers on common parameters. While model splitting significantly reduces the computation and communication costs of individual participants, additional novel designs on adaptive model overlapping and contrastive loss functions help MSfusion to maintain training effectiveness, against model shift across participants. Extensive experiments on image and NLP datasets illustrate significant advantages of MSfusion in performance and efficiency for training large models, and its strong scalability: computation cost of each participant reduces significantly as the number of participants increases.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Summary*
This work focuses on collaborative learning of large models over resource-constrained
participants. The authors propose a new model splitting strategy that assigns a submodel of the
full global model to each participant. They further introduce adaptive model overlapping and
contrastive loss functions, achieving effective and efficient training. The evaluation is conducted
over 3 image datasets (i.e., CIFAR10, CIFAR 100, and TinyImageNet) and 1 natural language
dataset (i.e., WikiText2) using ResNet18 and Transformer-based network.

### Strengths
1. The submodel splitting strategy is a natural way to reduce the computation cost and has
been well studied in the federated learning context. The key contribution of this work is the
design of adaptive model overlapping and contrastive loss functions to help maintain
training effectiveness against model shift across participants.
2. The convergence of the proposed algorithm is analyzed in smooth and strongly convex case.

### Weaknesses
1. The technical contribution of this paper is limited. Except introducing a double shifting
model splitting scheme, the proposed design has no significant difference from existing
partial training work as reviewed in Section 2.3.
2. The convex assumption over the loss function (i.e., Assumption 1) for convergence analysis is
quite strong.
3. The experiments cannot support the previous design and analysis sections. While the
previous design sections are claimed to study the collaborative training of large language
models (e.g., GPT-3 in Abstract), the evaluation diverges to computer vision tasks and only
take one natural language dataset for evaluation.
4. Some important evaluation details are missing, including the detailed parameter size and the
number of layers of the transformer model, as well as the size of participants and the
dataset partition for the experiment over WikiText2.

### Questions
From Table 1, why the baselines of HeteroFL and FedRolex perform so badly over WikiText2?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims at a collaborative training framework of large models for resource-constrained participants. To solve this problem, model splitting and contrastive loss functions are adopted. The research problem is interesting and important, and technical solution is reasonable and easy to follow. However, there is a gap between the research background and the experimental setup. The most serious issue is that the models used in the experiments of the paper cannot be called as large models. Besides, both of the two adopted techniques, i.e., model splitting and contrastive loss have been widely explored in many existing federated learning approaches, leading to novelty concerns.

### Strengths
1.	The research problem mentioned in Introduction is interesting and important.
2.	The overall structure and writing of the paper are well-organized and clear, enhancing the readability and understanding of the content.
3.	The adopted techniques are reasonable.

### Weaknesses
1.  Lacks of novel contribution. The proposed framework leverages adaptive model overlapping and contrastive loss function. These two proposed techniques, i.e., model splitting and contrastive loss have been investigated by many existing researches, while I do not find sufficient discussion on the related works. To have a clear view on the contribution, it is reasonable to have a comparison between the proposed approach and [1][2]. Specifically, the paper needs to clearly articulate how the proposed model splitting differs from existing split learning approaches, particularly in the context of decentralized training. The use of contrastive loss also needs more justification, given its prevalence in federated learning, and the authors should detail how their specific contrastive loss formulation addresses the unique challenges of their framework beyond existing uses.
2.  There is a gap between the experimental setup and the research background of the paper. From the title and abstract of the paper, I was looking forward to seeing collaborative training of large models, especially since the first sentence of the abstract mentioned models like GPT-3. However, I was surprised to find in the experimental setup that the visual tasks were performed using ResNet-18, and the model used for text-related tasks was not explicitly mentioned. But based on the calculated FLOPS in Table 1, I can infer that the parameter size of this model is far less than 1B. I am curious if a model with such parameter size can be considered a large model. If the authors decide to claim this framework is designed for Large Model, I highly recommend to conduct experiments on real large models such as models with at least billion-sized parameters. The current experiments do not adequately validate the claims made about the framework's applicability to large models.
3.  Insufficient baselines. The authors claim that the proposed framework is compared with partial training-based approaches, however, there are some well-recognized approaches missed, e.g., [1][3]. The selection of baselines seems arbitrary, and the paper would benefit from a more comprehensive comparison with state-of-the-art methods in federated learning and distributed training, especially those that also employ partial training or model splitting techniques. A more thorough comparison is needed to properly contextualize the performance of the proposed framework.
4.  Lacks of theoretical analysis. Considering the there is a proposed loss function in the framework, it is better to have a theoretical convergence analysis on the framework. The absence of a theoretical convergence analysis is a significant weakness. The paper should provide a rigorous analysis of the convergence properties of the proposed loss function, including conditions under which convergence is guaranteed and the rate of convergence. This is crucial for understanding the stability and reliability of the framework.
5.  There are some typos, e.g., " for TinyImageNet experiments for WikiText2 experiments is 800" in section A.2.2.

### Questions
Please see the weakness above.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents MSfusion, a collaborative learning framework that enables the training of large models on resource-constrained devices through model splitting. With its double shifting model splitting scheme, adaptive model overlapping, and contrastive loss functions, MSfusion maintains training effectiveness while significantly reducing computation and communication costs. The paper provides a mathematical reasoning for DSS and introduces the definition of an unbiased compressor. The authors also discuss the practical application of MSfusion in real-world scenarios where multiple companies with resource-limited servers and private data can collaborate to train high-performance large models. Overall, MSfusion offers a promising solution to the challenge of training large models on resource-constrained devices.

### Strengths
- The paper focuses on the significant task of collaborative training, which plays a vital role in various scenarios, particularly in training large models. The authors provide a clear motivation for their work, emphasizing the challenges faced when training resource-intensive models on devices with limited resources, and the necessity of collaborative learning frameworks. The practical application of MSfusion is also discussed, highlighting real-world scenarios where multiple companies with resource-limited servers and private data can collaborate to train high-performance large models.
- A highly effective collaborative training framework, MSfusion, is proposed in the paper, offering both computational efficiency and high performance. MSfusion leverages model splitting to enable effective and efficient training of large models across participants with resource constraints. The paper introduces the double shifting model splitting scheme, adaptive model overlapping, and contrastive loss functions to maintain training effectiveness while significantly reducing computation and communication costs. The authors provide a detailed description of the MSfusion framework, including the training process, communication protocol, and model aggregation method.
- The proposed approach is validated through experiments on various tasks. The authors conduct experiments on several datasets, such as CIFAR-10, CIFAR-100, and TinyImageNet, to evaluate the performance and efficiency of MSfusion. The results demonstrate that MSfusion achieves comparable or even superior performance compared to state-of-the-art methods, while substantially reducing computation and communication costs. The authors also perform ablation studies to analyze the contribution of each component of MSfusion to its overall performance.
- The paper includes in-depth theoretical analysis to support the proposed framework. This analysis encompasses the mathematical reasoning for the double shifting model splitting scheme and the definition of an unbiased compressor. The authors provide mathematical reasoning for DSS, which serves as a crucial component of MSfusion. Additionally, they introduce the definition of an unbiased compressor, which is employed to compress the model updates before transmission, thereby reducing communication costs. Theoretical analysis is provided to support the effectiveness of these components and their contribution to the overall performance of MSfusion.

### Weaknesses
 - The performance gap between the ablated models and the proposed model is not very large. This does not support the importance of the proposed contrastive learning objective and the dynamic overlapping method.
- The association between the proposed collaborative training framework and the contrastive learning objective could be further discussed.  This additional loss seems independent from the proposed collaborative training method. Also, this contrastive learning method itself may benefit other distributed learning frameworks, or the backbone model itself.

### Questions
I would expect more discussion on the results of the ablation study, and the proposed cross-sub-model contrastive learning, as specified in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
