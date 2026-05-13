# Adaptive Invariant Representation Learning for Non-stationary Domain Generalization

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Although recent advances in machine learning have shown its success to learn from independent and identically distributed (IID) data, it is vulnerable to out-of-distribution (OOD) data in an open world. Domain generalization (DG) deals with such an issue and it aims to learn a model from multiple source domains that can be generalized to unseen target domains. Existing studies on DG have largely focused on stationary settings with homogeneous source domains. However, in many applications,  domains may evolve along a specific direction (e.g., time, space). Without accounting for such non-stationary patterns, models trained with existing methods may fail to generalize on OOD data. In this paper, we study domain generalization in non-stationary environment. We first examine the impact of environmental non-stationarity on model performance and establish the theoretical upper bounds for the model error at target domains. Then, we propose a novel algorithm based on invariant representation learning, which leverages the non-stationary pattern to train a model that attains good performance on target domains. Experiments on both synthetic and real data validate the proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Many machine learning algorithms work based on the assumption that training and test data are sampled from IIDs. However, this is commonly violated in real-world cases as the data distribution may shift between train and test times. It has encouraged many researchers to develop techniques such as domain generalization and domain adaptation. However, such methods cannot accommodate the case that the data distribution changes over time based on a mechanism. To tackle such a problem, this paper studies domain generalization in a non-stationary environment, which aims to learn a model from a sequence of source domains that can capture the non-stationary patterns and generalize to unseen target domains. The authors examined the impacts of non-stationary distribution shifts and investigated how the model learned on the source domains performs on the target domains. Experiments were done on simulated, semi-synthetic, and real-world datasets.

### Strengths
- The problem this paper addresses is interesting. Multiple domains evolving over time is a realistic scenario but has hardly been studied before. Also, the authors demonstrated that the existing typical multiple-source DG/DA methods 
- The problem setup is more flexible than those of the related works as it allows the modeling of non-stationary dynamics and can be applied to multiple unseen target domains.
- Well-written and easy to follow.

### Weaknesses
 - Definition of $\Phi$ is a bit ambiguous. In Definition 4.1 and Remark 4.2, $\Phi(\widehat{M})$ consists of an average error of $\widehat{M}$ and on the source domains and error of $\widehat{M}$ on the target domain. It doesn't consider whether each error is low enough but only considers their difference. Thus, based on the definition, $\widehat{M}$ is generalizable even if $\widehat{M}$ has high errors on both source and target domains. I am unsure if such $\widehat{M}$ is generalizable.
- Moreover, Assumption 4.3 tells us that we can find a decent $\widehat{M}$ with a small error on the source domains but seems to tell nothing about the error on the target domain. I am unsure if I understood this statement correctly, but it doesn't seem like Assumption 4.3 implies that the error of $M^{*}$ on the target domain is small. I think this is one of the key statements of this study so it needs to be clarified.
- The authors need to add an uncertainty metric to Table 1.

### Questions
- I appreciate the theoretical analysis and experimental evidence that the authors presented. Could the authors further provide under what condition the proposed approach will have guaranteed improvement compared to either the ERM or some conventional DG method?
- I think the FMoW dataset from the WILDS benchmark aligns with the problem setup in the paper. (The authors already included sufficient experimental results, so I do not request the authors to add an additional dataset.)
- The authors may want to add some dotted lines to Table 1 to differentiate different approaches - ERMs / conventional DA/DGs, ...

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers a non-stationary domain generalization problem.  Authors first establish theoretical upper bounds for the model error at target domain, and then leverage the non-stationary pattern to train a model based using invariant representation learning. Experiments show some improved results over existing methods.

### Strengths
- A more general setting regarding non-stationary DG problem.
- A novel invariant algorithm is proposed based on theoretical bounds.
- Improved empirical results across a wide range of datasets.

### Weaknesses
 - Description of the setting is not clear and the key assumption seems strong.
- Proposed algorithm seems to be ad-hoc and complicated.
- Presentation can be made more concise.

- **Major Concern**: It is stated that "We note that Assumption 4.3 is mild because it is required only for the optimal mechanism M∗ . This assumption implies that there exists at least one hypothesis in M under which the non-stationary patterns learned from source can generalize sufficiently well to the target (with bounded $\Phi$ )."

  - regarding the criterion $\Phi$: I don't think Definition 4.1 necessarily implies a good estimate of the mechanism $M$. That is, $\hat M$ can be bad for all domain pairs, so that each $D$ inside the $|\cdot|$ is large but the difference is small. Perhaps some discussions shall be added here.
  - More importantly, I would like to think that Assumption 4.3 is rather strong. Note that it is NOT equivalent to assuming that there exists  a pattern in the hypothesis space; here it is a "specific" one, which minimizes the divergence of observed datasets, and could provide an almost optimal estimate of an unseen domain. If so, this would be a strong assumption on the relationship of observed domains and unseen domains. Please clarify.

- Minor: Section 5 is hard to follow. Please be more concise.
- Experiments: how many domains are used for training? And what if the domain index is re-ordered?

### Questions
I have some questions regarding the problem setting and assumptions:

- What's the difference between this problem's setting and the IRM's where it is assumed that some invariance exists across domains? I can see that some datasets you use (like RMNIST) falls into the IRM's setting. A related question is, why do you consider learning invariant representations using only two consecutive domains?

-  And do you implicitly assume that the domain indexes and their order are given? If so, I think this setting is limited in this sense.  Note that most benchmark methods do not utilize the order information. Please clarify. 

- **Major Concern**: It is stated that "We note that Assumption 4.3 is mild because it is required only for the optimal mechanism M∗ . This assumption implies that there exists at least one hypothesis in M under which the non-stationary patterns learned from source can generalize sufficiently well to the target (with bounded $\Phi$ )."

  - regarding the criterion $\Phi$: I don't think Definition 4.1 necessarily implies a good estimate of the mechanism $M$. That is, $\hat M$ can be bad for all domain pairs, so that each $D$ inside the $|\cdot|$ is large but the difference is small. Perhaps some discussions shall be added here.
  - More importantly, I would like to think that Assumption 4.3 is rather strong. Note that it is NOT equivalent to assuming that there exists  a pattern in the hypothesis space; here it is a "specific" one, which minimizes the divergence of observed datasets, and could provide an almost optimal estimate of an unseen domain. If so, this would be a strong assumption on the relationship of observed domains and unseen domains. Please clarify.

- Minor: Section 5 is hard to follow. Please be more concise. 
- Experiments: how many domains are used for training? And what if the domain index is re-ordered? 



Overall, I think this paper has some interesting and useful contributions. I am happy to increase my evaluation if authors can address my concerns.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the challenges associated with Domain Generalization (DG) under non-stationary environments. The authors investigate the effects of such non-stationary environments on model performance and provide theoretical upper bounds for errors when models are applied to target domains. To address the identified challenges, they introduce a new algorithm that is rooted in invariant representation learning. This algorithm uses the observed non-stationary patterns to develop a model that is expected to evolve and achieve better performance on target domains. The paper validates the effectiveness of the proposed algorithm through experiments conducted on both synthetic and real-world data.

### Strengths
- The article presents an innovative approach to tackle non-stationary domain generalization, a notable hurdle in practical scenarios. It delivers an extensive analysis of the associated difficulties and meticulously evaluates the impact of environmental changes over time.
- A major academic contribution of this work is the formulation of theoretical upper limits for model error, lending a robust theoretical underpinning to their methodology.
- The effectiveness of their method is validated with both synthetic and real data, showcasing its potential real-world applications.

### Weaknesses
 - The evaluation section lacks significance testing and does not report standard deviations in the results table. Given the close performance across many results, the inclusion of standard deviations is crucial to affirm the method's efficacy.
- The datasets and networks employed in the study are somewhat limited in size. The paper does not address scalability, leaving questions about the method's performance with larger datasets or more complex network architectures.
- While the theoretical analysis provided is compelling, the practical implementation details in Section 5 are complex and challenging to comprehend, even with the pseudo-code. A more detailed and clearer illsutration would greatly enhance understanding.

### Questions
Please refer to the weaknesses mentioned above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the continuous domain generalization problem (also named non-stationary DG setting in the paper), and proposes the  adaptive invariant representation learning algorithm to solve it. The model uses a transformer layer and a LSTM model to capture the evolving patterns between time steps. The experimental results validate the proposed method. However, the non-stationary DG setting is not a new one and there lack some literatures in this paper, and the theoretical analysis seems trivial, which together greatly lower the technical contribution of this work.

### Strengths
After carefully reading this paper, I think the strengths mainly lie in the design of the model.

1. The authors propose a novel model architecture to handle the continuous DG problem, which contains a transformer layer and an LSTM model to capture the time-dependent patterns. 
2. The experimental results are nice to validate the proposed method, which involves many datasets and baselines.

### Weaknesses
 I have several concerns regarding to the theoretical analysis, the model design, and the experimental results.
1. The theoretical analysis is trivial and there is little novelty in it. 
* Firstly, the Theorem 4.5 is a conventional generalization bound via Rademacher Complexity, and the constant term $C$ is the **upper bound** of the loss function, which means the upper bound is quite loose and not quite meaningful to guide the design of methods. That is, if the upper bound is too loose, one could add any term to it that is consistent to the method. Also, the meaning of $K$ is not demonstrated in the paper. 
* Secondly, Proposition 4.6 is also trivial, and the reweighting method that it inspired has little relationship with invariance. 
2. The model design: 
* Firstly, why the alignment of distributions could lead to invariance? The authors did not formally define the invariance property and it seems vague.
* Secondly, it seems that the designed model has a lot of computation burden, could the authors analyze it or provide some empirical analysis/results on this? For example, extra running time.
3. The experiments: the authors did not report the variance of different runs. Further, the validation protocol is not reported.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
