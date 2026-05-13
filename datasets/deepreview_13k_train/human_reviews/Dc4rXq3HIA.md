# Improving Domain Generalization with Domain Relations

- Decision: Accept
- Scores: 6, 8, 8, 6, 6, 6

## Abstract
Distribution shift presents a significant challenge in machine learning, where models often underperform during the test stage when faced with a different distribution than the one they were trained on. This paper focuses on domain shifts, which occur when the model is applied to new domains that are different from the ones it was trained on, and propose a new approach called \mymodel. Unlike previous methods that aim to learn a single model that is domain invariant, \mymodel\ leverages domain similarities based on domain metadata to learn domain-specific models. Concretely, \mymodel\ learns a set of training-domain-specific functions during the training stage and reweights them based on domain relations during the test stage. These domain relations can be directly obtained and learned from domain metadata. Under mild assumptions, we theoretically prove that using domain relations to reweight training-domain-specific functions achieves stronger out-of-domain generalization compared to the conventional averaging approach. Empirically, we evaluate the effectiveness of \mymodel\ using real-world datasets for tasks such as temperature regression, land use classification, and molecule-protein binding affinity prediction. Our results show that \mymodel\ consistently outperforms state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to solve the multi-source multi-target domain generalization problem using domain relations. The authors claim that existing single domain-invariant or multiple domain-specific models that leverage equal weights on all domains fail to capture appropriate domain-specific correlations. To tackle this problem, the authors extract domain relations from domain meta-data and design a relation-aware consistency regularizer to weight the training domain-specific functions. The weighted functions on source domains are then transferred to predictions on target domains. A theoretical analysis is provided to prove that the proposed approach can perform better than the models using equal domain weights.

### Strengths
1. This paper is clearly written and organized. The underlying idea is straightforward and easy to follow.

2. The authors provide a theoretical analysis that verifies that the proposed relation-aware consistency loss can achieve superior generalization performance compared to the approach of treating all training domains
equally. 

3. The experimental evaluation is comprehensive and thorough. An illustrative toy task is designed to examine the proposed methods and many tables and figures are presented to analyze the results.

### Weaknesses
1. The novelty of the proposed method may be somewhat limited as it bears similarities to ensemble methods, which also involve assigning varying weights to different domains. The essential distinctions between the proposed methods and ensemble methods should be clearly elucidated, and it is important to consider baseline models that incorporate ensemble methods for comparison. Specifically, the paper should clarify how the proposed method differs from simply training multiple models on different domains and then combining their predictions using a weighted average. The use of a shared feature extractor does not automatically differentiate it from all ensemble methods, as some ensemble techniques also employ shared representations or feature learning components. A more rigorous comparison with relevant ensemble techniques, such as those using boosting or bagging, is needed to highlight the unique contributions of this work.

2. The evaluation metrics used in this paper are different from previous works conducted on the TPT-48, FMoW, and ChEMBL-STRING datasets. It is unclear whether the metrics used, such as MSE, are suitable and fair to be used to evaluate domain generalization models. The paper should provide a more detailed justification for the choice of metrics, especially when they deviate from established practices in the field. For example, while MSE might be appropriate for regression tasks, its suitability for evaluating the generalization performance of classification models on datasets like FMoW and ChEMBL-STRING is questionable. The paper should discuss the implications of using these metrics and provide a comparison with commonly used metrics in domain generalization, such as accuracy or F1-score, to ensure the results are comparable and meaningful.

3. As stated by the authors, the theoretical analysis of this paper relies on certain assumptions. It is questioning whether these assumptions reflect the real-world datasets. For example, the assumptions that the domain relations accurately capture the similarity between domains, and that they are determined solely by the distance between domain representations, may not always hold true in real-world datasets. In the proofs of the theorems, the authors only prove that the proposed estimator outperforms the equally weighted estimator in the minimax sense, but not a theoretically global superiority. Moreover, the theorems only reveal that uneven weights can be better than equal weights, which does not entirely support the key ideas of acquiring appropriate weights for different domains. The theoretical analysis should be expanded to address the limitations of these assumptions and provide a more robust justification for the proposed method. For instance, the paper could explore the sensitivity of the theoretical results to violations of the assumptions or provide empirical evidence to support the validity of these assumptions in real-world scenarios. Furthermore, the theoretical results should be strengthened to demonstrate that the proposed weighting scheme is not just better than equal weighting in a minimax sense, but also optimal or near-optimal in a more general sense.

### Questions
Please see the weakness points.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of out-of-domain generalization of discriminative models. The presented approach leverages domain relations and domain-specific meta-data to adapt to new domains at test time. Domain similarities are determined from a combination of a user-defined function and a learned function of the domain meta-data. The domain similarities are used to weight the different neural network heads in a mixture-of-experts fashion. At test time, the domain similarities are used to weight the output of all of the training set domain-specific heads to produce a prediction. Theoretical results provide justification for the proposed approach. Empirical results are shown on open source toy and real-world datasets, including several useful ablations.

### Strengths
* The motivation for the paper is strong, in a relevant area.
* The paper is well-written.
* The empirical results are very strong and well executed, including a large number of baselines. The ablation studies are beneficial, answering fundamental questions about the method.

### Weaknesses
 * The method requires a user-defined domain similarity function based on meta-data. This might not always be available. Additionally, for specific applications, a user might not be able to credibly define such a function. The reliance on a manually defined similarity function introduces a potential source of bias and limits the applicability of the method in scenarios where such meta-data is absent or unreliable. The paper does not adequately address the sensitivity of the method to the choice of this function or provide guidance on how to select or validate it.
* The theoretical work makes (understandably) quite a few strong assumptions that are unlikely to be true in practice. These results could be improved to show how performance is affected by, for example, noisy domain relations. The theoretical analysis assumes a clean, well-defined relationship between domain meta-data and the actual domain shift. This assumption is unrealistic in real-world scenarios where domain shifts can be complex and influenced by factors not captured by the meta-data. The analysis also does not account for the possibility of misaligned or noisy meta-data, which could significantly impact the performance of the proposed method.

### Questions
* Is it possible for the proposed method to utilize negative relationships between domains?
* How will the proposed method behave in a situation where there are no related domains according to the meta-data? Will the method perform as well as a domain-invariant approach? Is this what the consistency loss is for?
* If domain information was unavailable, could a domain discovery method (e.g. clustering) be used to learn domains and domain relations from unlabeled data? In the limit, could the model architecture and inference algorithm be adapted to learn domains and domain relations end-to-end?
* Could this method be used in data impoverished applications to improve performance? 

Minor typos:
* Equations are referenced with "Eqn. equation #", maybe just "(#)" or "Equation (#)"?

### Soundness
3 good

### Presentation
3 good

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
The paper addresses the domain shift problem and proposes a new approach called D3G to this problem. Instead of learning a single model from multiple source domains, the proposed method learns domain-specific models and infer a test domain specific model by exploiting the domain relations. The test domain model is a weighted combination of multiple source domain models whilst the weights are learned from the domain metadata. Theoretic and empirical analyses have been made and experimental results demonstrate the superiority of the proposed approach to many state-of-the-art counterparts.

### Strengths
-- The approach distincts from most existing ones in that it learns domain-specific models instead of a unified model. 

-- The method is clearly presented and theoretic analysis has been made to clarify why it should work for domain generalization.

-- The proposed approach is applicable to many real-world applications as demonstrated in the experiments. The superior performance makes a significant difference to practical problems of this type.

-- Ablation studies have been conducted to demonstrate the effectiveness of each component of the proposed approach.

### Weaknesses
 -- The comparison of the proposed method with ensemble models of existing approaches should have been given.

-- There exist some typos/language issues, e.g., "Eqn. equation x..."; "We using weighted...";

### Questions
1. Does it work when there is no domain metadata available? Can such domain relations be learned from the data themselves?
2. How the domain metadata are used in the comparative methods?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel method called D3G for tackling the issue of domain shifts in real-world machine learning scenarios. The approach leverages the connections between different domains to enhance the model’s robustness and employs a domain-relationship aware weighting system for each test domain.

### Strengths
The authors provide a theoretical proof that using domain relations to reweight a specific function of the training domain can obtain stronger extraterritorial generalization.

### Weaknesses
The novelty is limited, perhaps the authors have not sufficiently explained the differences between their work and existing methods.

The authors state that " Unlike prior works that rely on ensemble models to address the underspecification problem and improve out-of-distribution robustness, our proposed D3G takes a conceptually different approach by constructing domain-specific models." However, the  MoE[1] constructed domain-specific models and they adopted ensemble models to improve out-of-distribution robustness.

The meta-data is key of domain-relation in this work. However, there is no clear definition of meta-data, how to obtain meta-data, and why the meta-data work is lack of detailed elaboration and analysis.

How the consistency loss address the challenge of limited training data in certain domains?

The organizational of the method section needs to be adjusted. The description and calculation of the domain relationship "a" in advance make the method part more clear.

It is recommended to add the venue and year of the comparison method to the table in the experiment section.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new approach for out-of-distribution generalization named as D$^3$G. It leverages domain relations estimated from domain metadata to learn training domain specific models and the ensemble of training-domain-specific functions. Under some assumptions, for example the domain relations can accurately capture the model similarity between domains, the authors proved that the proposed method can generalize better to out-of-domain samples compared to the traditional averaging approach. Empirical results on both synthetic and real-world datasets show that D$^3$G surpassing the performance of traditional averaging methods and some other baseline methods.

### Strengths
- Originality: good. Though learning domain specific classification head has been proposed in exiting works, it is novel to ensemble domain specific classifiers by weights learned from domain meta-data.
- Significance: the proposed method is simple but shown improved performance on several tasks.
- The paper is overall well written and easy to follow.
- Experiment setups are introduced in detail.

### Weaknesses
 - The robustness and generality of the proposed method is unclear. Practically, it is unclear how to design a good similarity definition for metadata of different tasks. The current way of constructing the fixed relations requires specific and expertise knowledge on each task. Nevertheless a learning approach is proposed, the ablation study results in Table 10 show that the learned relations can be less helpful on some tasks.
- The limitations of this work are not fully discussed. For example, the generality of the assumptions in the theoretical analysis part.

### Questions
Please refer to the concerns in the "weaknesses" part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed D3G, which in contrast to previous approaches, utilizes domain metadata to create domain-specific models. During training, it learns domain-specific functions, and during testing, it reweights them based on domain relations, enhancing model adaptability using directly acquired domain metadata.

### Strengths
- The paper is well-written and easy to follow. The authors use appropriate notation and equations where necessary.
- This paper utilizes domain meta-data to extract relations between domains.
- The domain relations are learned rather than fixed.

### Weaknesses
 (1) In section 3.2, it is mentioned that both $m_i$ and $a_{ij}^{g}$ are derived from domain metadata, but the specific relationship or distinction between them is not clearly explained. The experimental results suggest that $a_{ij}^{g}$ is extracted from $m_i$, yet this section lacks explicit clarification. It remains unclear how the domain metadata is processed to obtain $m_i$ and how this relates to the fixed relation $a_{ij}^g$. For example, if $m_i$ represents a feature vector of the domain, how is this vector used to derive the relation $a_{ij}^g$, which seems to be a matrix representing the relationship between domains? The paper should clarify the exact mathematical operations or transformations involved.

(2) It is unclear whether the two layer neural network $g$ should be trained or directly be used from other previous works. It is mentioned that weight vectors $w_r$ are learnable vectors. Are these weights and the neural network trained by the consistency loss? The paper needs to explicitly state whether the parameters of the neural network $g$ are also learned during training, and if so, how they are updated. Specifically, it is not clear if the consistency loss is directly backpropagated through the neural network $g$ to update its weights, or if some other optimization strategy is used.

(3) The consistency loss implies that each head is trained on all the domains with different weights. This is similar to the case where each head is trained on all the domains with a weighted combination of the losses of all the domains. For the predictor $f^{(d)}$, the loss is in this form: $l(\frac{\sum_j^{N^{tr}} a_{dj} f^{(d)}(x^j)}{\sum_j^{N_{tr}} a_{dj}})$. Would this loss also help the learning of domain-specific models? It is not clear if the proposed method offers a significant advantage over simply training each head with a weighted loss across all domains, and the paper should provide a more detailed analysis of the differences.

(4) Suppose that each head is trained on all the domains by the loss function (2). In this case, regardless of the values of $a_{ij}$, if both the supervised loss and consistency loss reach their minimum, then the learning of $a_{ij}$ would be useless. Does the proposed method face this issue? The paper should discuss the potential for the learned domain relations $a_{ij}$ to become trivial if the supervised and consistency losses are minimized, and how the method avoids this scenario. Specifically, it is not clear what prevents the model from converging to a state where all $a_{ij}$ are equal, effectively negating the benefit of learning domain-specific relations.

(5) In the experiment section, one baseline of the proposed method would be training each head on all the training domains by supervised loss and averaging the predictions of these heads as the test prediction. The paper should include this baseline to demonstrate the effectiveness of the proposed method compared to a simpler approach where domain relations are not explicitly learned or used.

### Questions
Please refer to the Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
