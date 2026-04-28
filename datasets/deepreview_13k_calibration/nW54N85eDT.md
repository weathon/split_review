# Predicting User Behaviors with Scene via Dual Sequence Networks

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Modeling sequential user behaviors for future action prediction is crucial in improving user's information retrieval experience. Recent studies highlight the importance of incorporating contextual information to enhance prediction performance. One crucial and typical contextual information is the scene feature which we define it as sub-interfaces within an app, created by designers to provide specific functionalities, such as ''text2product search" and ''live" in e-commence apps. Different scenes exhibit distinct functionalities and usage habits, leading to significant distribution gap in user engagement across them. Popular sequential behavior models either ignore the scene feature or merely use it as attribute embeddings, which could lead to substantial information loss or cannot capture the interplay between scene and item in modeling dynamic user interests. In this work, we propose a novel Dual Sequence Prediction network (DSPnet) to effectively capture the interplay between scene and item sequences for future behavior prediction. DSPnet consists of two parallel networks dedicated to predicting scene and item sequences, and a sequence feature enhancement module to capture the interplay. Further, considering the randomness and noise in learning sequence dynamics, we introduce Conditional Contrastive Regularization (CCR) loss to capture the invariance of similar historical sequences. Theoretical analysis suggests that DSPnet can learn the joint relationships between scene and item sequences, and also show better robustness on real-world user behaviors. Extensive experiments are conducted on one public benchmark and two collected industrial datasets. The codes and collected datasets will be made public soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses the challenge of predicting future user actions by effectively modeling sequential user behaviors with a focus on integrating contextual information, particularly the scene feature. Scene features, designed by app or website developers, significantly influence user engagement and exhibit distinct usage patterns and product themes. Traditional models often overlook the scene feature or treat it superficially, leading to potential information loss and failing to capture the complex interdependencies between scenes and items.

To tackle these issues, the authors propose a Dual Sequence Prediction network (DSPnet), a novel approach that simultaneously predicts scene and item sequences while capturing their inter-dependencies. DSPnet comprises two parallel networks for scene and item predictions and a sequence feature enhancement module to integrate these dependencies. To improve the model's robustness against the randomness and noise inherent in sequence data, the authors introduce a Conditional Contrastive Regularization (CCR) loss, which helps maintain the invariance of similar historical sequences during training.

Theoretical analysis indicates that DSPnet can effectively learn the joint relationships between scene and item sequences, thereby enhancing the accuracy of future behavior prediction. The effectiveness of DSPnet is validated through extensive experiments on a public benchmark dataset and two proprietary industrial datasets. The authors plan to make the source code and datasets publicly available to facilitate further research.

### Strengths
The proposed Dual Sequence Prediction network (DSPnet) method exhibits several strengths:

1. **Innovative Modeling of Inter-Dependencies**: DSPnet captures the inter-dependencies between scene and item sequences, addressing a critical gap in existing sequential behavior modeling methods. By using two parallel networks and a sequence feature enhancement module, it effectively integrates the dynamics of both scenes and items, leading to more accurate and comprehensive behavior predictions.

2. **Theoretical Robustness**: The theoretical analysis demonstrates that training DSPnet is equivalent to maximizing the joint log-likelihood of both scene and item sequences. This ensures that the model can effectively learn and represent the relationships between scenes and items, enhancing its predictive power.

3. **Conditional Contrastive Regularization (CCR)**: The introduction of CCR helps in capturing the invariance of similar historical sequences, which is crucial for dealing with the randomness and noise in user behavior data. CCR uses learned conditional weights to promote similarity among sequences, thereby improving the robustness and generalizability of the model, especially in scenarios with skewed user behaviors.

4. **Rich and Diverse Datasets**: The authors have collected 37 days of sequential user behavior data from their e-commerce app, constructing two industrial datasets. These datasets, along with a public benchmark, provide a rich and diverse set of data for validating the effectiveness of DSPnet. The datasets contain chronological purchase behaviors on nearly thirty million items, addressing the research data gap in this field.

5. **Empirical Validation**: Extensive experiments on three datasets—one public benchmark and two industrial datasets—demonstrate the superior performance of DSPnet compared to state-of-the-art baselines. The results highlight the importance of incorporating scene information in sequential behavior modeling and showcase the practical benefits of the proposed method.

These strengths collectively position DSPnet as a significant advancement in the field of sequential user behavior modeling, offering improved accuracy and robustness in predicting future user actions.

### Weaknesses
 - The paper does not explicitly discuss the potential for integrating Conditional Contrastive Regularization (CCR) with other recommendation models.


### Questions
- Can Conditional Contrastive Regularization (CCR) be integrated with other recommendation models and be effective?

- Please provide an analysis of the model's complexity and efficiency and how to tune the hyperparameters for the training loss?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Dual Sequence Prediction network (DSPnet) to improve future user action prediction by modeling interdependencies between "scene" features (like “text2product search”) and item sequences. This paper claimed that traditional models often overlook these dynamics, leading to potential information loss. DSPnet addresses this by using parallel networks to capture scene and item dependencies and incorporates Conditional Contrastive Regularization (CCR) loss to handle sequence noise. The approach shows enhanced robustness and effectiveness on both public and industrial datasets.

### Strengths
(1) This paper proposes a unique Dual Sequence Prediction network (DSPnet) that explicitly models both scene and item sequences. By focusing on the interdependencies between scenes and items, DSPnet captures a level of contextual nuance that is often overlooked in traditional sequential behavior models. This dual-focus approach is well-aligned with real-world applications where user behaviors are influenced by both the content itself and the surrounding context.
(2) Moreover, the introduction of CCR loss is a good point, as it addresses the noise and randomness inherent in sequential user behaviors. By focusing on the invariance of similar historical sequences, CCR loss enhances the model robustness and improves its ability to generalize to diverse, noisy data. This addition is valuable in real-world applications, where user behavior data can be unpredictable.
(3) The dataset may be valuable for the future research if it will be released as promised.

### Weaknesses
 **Unclear Definition and Scope of "Scene"**: The paper does not clearly define what constitutes a "scene" in the context of user behavior modeling. While scenes are described as features crafted by app or website designers (e.g., “text2product search” and “recommendation”), the criteria for selecting or categorizing these scenes remain ambiguous. It is also unclear how many types of scenes the model considers and whether these categories are generalizable to various platforms or domain-specific. A more precise definition would help readers understand the breadth of the model's applicability and the nature of the contextual features being leveraged. For example, the paper does not specify if scenes are mutually exclusive or if a user action can belong to multiple scenes simultaneously. The granularity of scenes is also unclear; are they broad categories or very specific sub-interfaces? This lack of clarity makes it difficult to assess the practical implementation and generalizability of the proposed approach.

**Limited Comparison with Multi-Behavior Models**: If scenes are understood as representations of multi-behavior patterns, DSPnet could benefit from comparison with established multi-behavior modeling approaches, such as the work by Cho et al. on Dynamic Multi-Behavior Sequence Modeling for Next Item Recommendation (AAAI 2023). Multi-behavior models aim to capture diverse user actions within sequences, which aligns with the paper’s goal to model interdependencies between scenes and items. A direct comparison could illustrate DSPnet’s advantages (or limitations) over these approaches in capturing the nuances of dynamic user behavior. The paper should clarify why existing multi-behavior models are insufficient for the problem being addressed and how the proposed scene-based approach offers a unique advantage beyond simply modeling different types of user actions.

**Lack of Standard Metrics for Evaluation**: In evaluating DSPnet on the OutBrain dataset, the paper does not include Mean Average Precision @12, a widely recognized metric for this dataset. Including this metric would facilitate a more transparent and standardized assessment of DSPnet’s performance, allowing comparisons with other models that have used this benchmark. This would also provide a clearer view of DSPnet's efficacy across different evaluation metrics relevant to the field. The absence of this standard metric makes it difficult to place the results in the context of prior work on the same dataset.

**Omission of Scene Prediction Accuracy**: Although DSPnet is designed to jointly predict both scenes and items, the accuracy of its scene prediction component is not reported. Providing this accuracy would clarify how effectively the model captures the contextual "scene" aspect in addition to item sequence modeling. Without this metric, it is challenging to evaluate the effectiveness of DSPnet’s dual-stream approach in fully capturing the dependencies between scenes and items. The paper should also explore the correlation between scene prediction accuracy and item prediction accuracy to understand if improvements in scene prediction directly translate to better item predictions.

**Limited Citation of Recent Works**: The paper’s references do not include any work from 2024 or later, which may indicate that it has not incorporated the most recent advancements in the field. This omission is notable for an ICLR 2025 submission, as the field of sequential user behavior modeling is rapidly evolving. Including more recent literature would strengthen the theoretical grounding of DSPnet and ensure that it is evaluated within the current landscape of user behavior modeling techniques. Specifically, the paper should address recent advances in transformer-based models and their application to sequential recommendation.

**Commonality of Dual-Stream Architectures**: The paper presents DSPnet’s dual-stream architecture, which separately models scene and item sequences, as a novel approach. However, dual-stream architectures have become relatively common for tasks with multiple related objectives, such as multi-task learning frameworks. The paper would benefit from a deeper exploration of how DSPnet’s dual-stream setup is unique or offers advantages over other dual-stream or multi-task models. Additional insights on why DSPnet’s architecture is particularly suited to user behavior prediction would highlight its contributions more effectively. The paper should also discuss how the proposed dual-stream approach avoids potential issues such as negative transfer between the scene and item prediction tasks.

### Questions
(1) How many types of the scenes does this paper consider?
(2) Please justify the lack of recent works and the comparison with multi-behavior recommendation.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper focuses on using scene/behavior features to enhance sequential recommendation. The authors design a Dual Sequence Prediction network (DSPNet), constructing parallel item sequence encoders along with corresponding scene sequence encoders to form a dual-branch structure. They employ an improved contrastive learning approach to enhance the robustness of both sequence models, utilize adversarial loss for cross-branch alignment, and train the model by combining "next item prediction" with "next corresponding behavior prediction." The effectiveness of the proposed DSPNet is validated on one public dataset and two internal datasets.

### Strengths
1. Using behavior type features as contextual information indeed enhances the effectiveness of sequential recommendation.
2. The paper is well-written and very easy to understand.
3. It includes experiments on industrial-scale datasets.

### Weaknesses
1. **Limited novelty**. The effectiveness of using behavior features as contextual features in personalized recommendations is somewhat a consensus, so emphasizing this appears somewhat trivial. The proposed method is essentially a simple combination of existing practices, including contrastive learning, adversarial training, next-item, and next-scene/behavior prediction, which are lukewarm in this domain. Although a marginal technical contribution is made with conditional weights in contrastive learning, its superiority over standard contrastive loss does not seem supported by the experiments. While some theoretical results are provided, such as Lemma 1 proving that simultaneously predicting the next item and its corresponding scene/behavior minimizes ELBO, this does not appear significant enough to suffice as a novel technical contribution.

2. **Inconsistency between the dual-branch approach and motivation**. Modeling item sequences and scene/behavior sequences with dual branches seems disconnected or even in conflict with the stated motivation. Lines 93-94 mention that item and scene *simultaneously* occur in Figure 1(c), yet the method here appears to overlook this point. This presents a contradiction—how can independent modeling of item and scene sequences ensure their one-to-one correspondence? It is unclear whether the proposed **coarse-grained** sequence-level alignment/fusion is superior to a **fine-grained** alignment/fusion between item-scene/behavior pairs.

3. **Insufficient experimental comparisons**. The paper lacks crucial baselines that would support the superiority of the proposed method, such as: (1) self-supervised sequential recommendation models, like SASRec, S3-Rec [1], ICLRec [2], and DCRec [3]; (2) baselines using scene/behavior features as attributes [4,5]. Additionally, a simple baseline could involve adding scene/behavior embeddings to item embeddings and using straightforward models like SASRec or BERTRec, often considered strong baselines in practice; (3) multi-behavior sequential recommendation models [6-11] and multi-behavior recommendation models [12-15].

4. **Lack of context in related work**. This study's application is highly relevant to multi-behavior recommendations, particularly multi-behavior sequential recommendations [16], yet these works are overlooked without any discussion, reflecting a gap in the paper's background and depth.

### Questions
1. In Table 1, why does BERT4Rec encounter 'OOM' while the other models do not?

2. During inference, how are the metrics calculated? Besides considering the accuracy of item prediction, was the accuracy of behavior prediction also considered?

### Soundness
2

### Presentation
3

### Contribution
2
