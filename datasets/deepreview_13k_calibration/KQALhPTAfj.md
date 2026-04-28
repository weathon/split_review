# Navigating Scaling Laws: Accelerating Vision Transformer's Training via Adaptive Strategies

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
In recent years, the state-of-the-art in deep learning has been dominated by very large models that have been pre-trained on vast amounts of data. The paradigm is very simple: Investing more computational resources (optimally) leads to better performance, and even predictably so; neural scaling laws have been derived that accurately forecast the performance of a network for a desired level of compute. This leads to the notion of a "compute-optimal" model, i.e. a model that allocates a given level of compute during training optimally to maximise performance. In this work, we extend the concept of optimality by allowing for an "adaptive" model, i.e. a model that can change its shape during the course of training. By allowing the shape to adapt, we can optimally traverse between the underlying scaling laws, leading to a significant reduction in required compute to reach a given target performance. We focus on vision tasks and the family of Vision Transformers, where the patch size as well as the width naturally serve as adaptive shape parameters. We demonstrate that, guided by scaling laws, we can design compute-optimal adaptive models that beat their "static" counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a “compute-optimal” model, where the characteristics of the network, such as width, depth, and patch size, could be changed/adapted during training. The authors argue that such an “adaptive” model can utilize the scaling property of the neural network, and achieve “optimal” computation status---in a way, it balances the tradeoff between the computation and the performance. The modification of the network mainly focus on ViT, and the authors schedule the width and patch size to reduce training computation resource. Specifically, for both patch size and the network width, the authors apply adapting, scaling, and scheduling strategies. Experiments on ViT of different patch sizes/widths show promising computation reduction.

### Strengths
- The paper focuses on an interesting topic in transformer network (ViT) training---how to tune the parameters---which are image patch size and network width---to achieve "optimal" training with "optimal" training resources.

- The study of previous work is new and very related to the topic.

### Weaknesses
 - The authors have mentioned 3 contributions in the paper. However, these contributions could be summarized as one point---an adaptive strategy to change the patch size and the network width to adapt training.

- Many arguments in the paper lack theoretical connections, and only some empirical results were shown in the paper. I think if the paper focuses on empirical results, more experiments such as different network property changes, and different changes with multiple kinds of properties should be discussed and compared. If the authors keep current experiments, more applications or tasks could be included to further validate the proposed method.

- Following the above discussion, one example is: when adapting patch size, there are no width changes, and when adapting network width, there are no patch size changes. I wondered if the authors could do further experiments on various changes including cross adapting to make the argument stronger.

- Some of the limitations discussed in the paper could actually incorporated in this paper.

### Questions
There are also some ambiguities in the figures/paragraphs. For example, in Figure 3, what do those arrows mean? 

My main concern is discussed above. Please follow this discussion to further improve the paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors introduce a new approach to training deep learning models that we call “adaptive training.” Adaptive training allows the model to change its shape during the course of training, which can lead to significant reductions in the required compute to reach a given target performance.

This work focuses on vision tasks and the family of Vision Transformers (ViTs), where the patch size as well as the width naturally serve as adaptive shape parameters. Authors demonstrate that, guided by scaling laws, one can design compute-optimal adaptive models that outperform their “static” counterparts.

They then propose a simple and effective strategy to traverse scaling laws, opting for the one that leads to the fastest descent, i.e. maximum performance gain for the same amount of compute. The work showcases the efficiency of our approach by optimally scheduling the patch size of a Vision Transformer, leading to significant reductions in the required amount of compute to reach optimal performance. They further confirm the validity of the approach by optimally scheduling the model width of a Vision Transformer.

The work demonstrates that adaptive training is a promising new approach to training deep learning models that can significantly reduce the computational resources required to achieve state-of-the-art performance.

### Strengths
The paper is based on a sound reasoning that having a static architecture while studying scaling laws might not lead to optimal use of compute. This paper proposes an alternative to consider architecture to be elastic which can be modified based on the insights from intermediate scaling laws.

### Weaknesses
Considering patch size and width of the transformer blocks are reasonable first choices to tune flops per training example. It would be interesting to consider other choices and their effects.

### Questions
I would like to see more ablations on other choices of the transformer architecture on their effect on optimal architecture.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The work is motivated by the following observation that the shape of the model remains fixed throughout the training process. Shape in this context refers to hyperparameters of the model that do not degrade performance when changed (such as width, depth and patch size).
- In turn, the paper proposes an adaptive training methodology to achieve equivalent performance for a specific model while using fewer computational resources (termed as FLOPs).
- The algorithm exploits the fact that the scaling laws proposed till now are in the form of a generalized power law. Thus, they compute the inverse function (as the fitted scaling law is bijective) and then compute the set where the shape parameter being tuned achieves the highest gradient. This set provides a scheduler for the shape parameter being tuned across training time.
- The paper leverages existing flexible transformer architectures like FlexVIT to tune shape-parameters like patch size and model width.

### Strengths
- Good motivation to the paper, the method makes intuitive sense to me. The evaluation performed is adequate.
- Excellent results. It appears that substantial improvements in FLOPs is observed compared to the baseline schedulers (fixed) and the FlexVIT scheduling method (which is the architecture they employ).
- The presentation of the work is very good. Visualizations are helpful in understanding the work.

### Weaknesses
 - While the proposed method is interesting and makes intuitive sense, don't such shape parameters exist for transformer models in other modalities. An experiment to show that the scheduler generalizes to text or audio or other modalities would make this work far stronger.
- The work explores the axis being tuned one at a time (patch size or model width). It would be nice to show that the result holds when two shape parameters are scheduled together. Do the authors expect the trend to hold?
- While FLOPs are one measure of computational cost, they do not characterize all aspects of performance [1] (compared to training time, carbon emissions etc). In the context of this work, as the architecture is kept constant, I expect the assumption to hold (FLOPS are a proxy for computational cost), however, it would be good to have further discussion around this point. 
- The work does not provide a discussion/results wrt potentially improved carbon emissions estimates and the overall end-to-end cost of their training procedure (e.g. accounting for their greedy search to get optimal hyper-parameters compared to other baseline methods). Showing just FLOPs presents only one perspective of computational cost.

### Questions
Please clarify the questions and comments listed in Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main argument of the paper is that, by being guided by scaling laws, one can develop compute-optimal adaptive models that surpass the performance of their static counterparts. The paper then proposes an "adaptive" ViT model that can alter its patch size during training. The authors claim the model optimally navigates the underlying scaling laws, thereby reducing the computational resources required to attain a specified performance level.

### Strengths
S1. Relevance: With the increasing computational demands of state-of-the-art models, finding ways to optimize compute resources without compromising performance is very important. This work directly addresses the issue, with a somewhat unique take on the problem. 

S2. Theoretical motivation: The paper's emphasis on neural scaling laws as the guiding principle behind adaptive modeling provides a good basis and motivation for the proposed approach. This grounding might inspire new ideas in this direction.

S3. Empirical results: The proposed adaptive model seems to surpass its static counterpart for most patch sizes which is a promising result. This could make the method useful for practitioners.

### Weaknesses
W1. Novelty: The concept of adaptive models that can modify their shape during training seems very similar to Neural Architecure Search (NAS) which isn't covered at all in the related work or in the comparisons. See [1] for a comprehensive overview of NAS.

W2. Complexity: While adaptive models sound promising, they might introduce additional complexities in terms of training dynamics and hyperparameter tuning. I appreciate that the authors have mentioned some of these issues in the "limitations" section, but I feel a more comprehensive treatment is necessary especially related to how the optimal scheduling will change for other tasks / architectures. Specifically, the paper lacks a detailed analysis of how the patch size transition schedule is determined and whether this schedule is robust to different datasets and model architectures. The current approach appears to rely on a pre-defined schedule based on scaling laws, but the practical implications of this choice need further exploration.

W3. Overfitting concerns: Altering a model's shape during training could lead to overfitting issues. I think the paper should address this concern more explicitly eg. what do the train / test gaps look like for the adaptive model. The paper should include a more detailed analysis of the training and validation curves, specifically highlighting the behavior around the points where the patch size is changed. It's crucial to understand if these transitions cause any sudden changes in the generalization performance of the model.

### Questions
Questions and recommendations:

1. How do NAS approaches relate to neural scaling laws and the method proposed in the paper?
2. At least some comparison to state of the art NAS methods is needed, as this would strengthen the paper's claims and make its contributions clearer.
3. The authors should provide a more in-depth overview of the complexities introduced by adaptive models, potentially with guidelines to address these.
4. Is overfitting an issue? What does the train / test gap look like for the models?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
