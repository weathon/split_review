# The Fundamental Limits of Least-Privilege Learning

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 5, 5, 6

## Abstract
The promise of least-privilege learning -- to find feature representations that are useful for a learning task but prevent inference of any sensitive information unrelated to this task -- is highly appealing. However, so far this concept has only been stated informally. It thus remains an open question whether and how we can achieve this goal.
In this work, we provide the \emph{first formalisation of the least-privilege principle for machine learning} and characterise its feasibility.
We prove that there is a \emph{fundamental trade-off} between a representation's utility for a given task and its leakage beyond the intended task: it is not possible to learn representations that have high utility for the intended task but, at the same time prevent inference of any attribute other than the task label itself. This trade-off holds under realistic assumptions on the data distribution and {regardless} of the technique used to learn the feature mappings that produce these representations.
We empirically validate this result for a wide range of learning techniques, model architectures, and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes inference-time information leakage due to releasing the representations of sensitive input data (compared to only releasing the predicted label). It investigates how this leakage relates to the quality of the representation. For modeling the quality of representation (concerning a downstream prediction task), the authors analyze the mutual information between the representation and the label. For modeling the information leakage from the representation about the sensitive attributes, the authors analyze the Bayesian optimal adversary for attribute inference. The authors prove that whenever the representation enables non-negligible performance for downstream prediction tasks, there must exist attributes that are significantly more leaked through the additional release of representation (compared to only releasing the label) of the sensitive input data. 

To interpret and validate this inherent trade-off, the authors further perform experiments on tabular datasets to quantify the empirical information leakage and model utility. Specifically, information leakage is measured against an empirically instantiated Bayesian optimal adversary using auxiliary data.

### Strengths
- The authors prove an interesting inherent trade-off between the model's utility and the information leakage due to releasing representation (compared to only releasing labels). As an interesting baseline, the authors also discussed the fundamental information leakage of how much the label of input data reveals sensitive attributes.

- Experiments support the proved trade-off, as the authors observe a positive correlation between the number of attributes that incur high information leakage (due to releasing representations) and the model's utility. Interestingly, when the most leaked attributes are censored during the model training and inference phase, the authors observe that the leakage about other attributes increases.

### Weaknesses
 - The model splitting between server and clients analyzed in this paper is counter-intuitive. Namely, the authors assume that clients use only the representation layers of the model, while the server uses only a classification head of the model. Since the classification heads are usually small and easy to train, I do not see the incentive for clients to share input data representations to the server in this setting (for prediction tasks). For example, the clients may download the classification head weights or tune a classification head on local data and compute the labels locally at inference time. This also seems different from Melis et al. 2019, where the clients only compute one embedding layer (rather than a large part of the whole model).

- The definitions and notations lack clarity at times. Most importantly, the information leakage is defined by successful inference of *any* attribute. This may be overly strong as many attributes are less sensitive. I'm wondering whether the proved trade-off in this paper is largely a result of this overly strong definition of information leakage.

- Additionally, the paper's theoretical results hinge on a specific, and potentially unrealistic, definition of representation leakage that considers the maximum possible leakage across all attributes. This worst-case analysis might not reflect realistic scenarios where only a subset of attributes are considered sensitive. The practical impact of the proven trade-off is therefore unclear, as it may not apply when considering more nuanced, attribute-specific leakage metrics. The conceptual representation example, $Z=\arg\max_{y}P(Y=y|X)$, further highlights this issue, as it can achieve Bayes-optimal classification success while potentially leaking less information than other representations, yet it's unclear how this fits within the current theoretical framework.

### Questions
- Could the authors discuss more about the effect of the splitting method, i.e., what parts are deemed as representations, on the theoretical and empirical conclusions? For example, when the client only has access to a small part of the model, would the leakage still be unbalanced on different attributes?

- Could the authors discuss how the theoretical and empirical trade-off (between information leakage and model utility) might change if we only consider a smaller set of attributes (rather than the whole input feature space) as sensitive?

Minor comments regarding clarity:
- What are the transition orders between random variables in the Markov chain $Y - X - W$ defined in Section 2?
- In Figure 4, bottom right plot, what is the meaning of color? Why is the third row from the top colored blue despite its negative value? What does a negative model utility $\tilde{I}_{\infty}(Y, Z)$ mean?
- Assumption A requires a positive posterior but does not require any lower bound for the posterior density. Does it mean the posterior could also be arbitrarily close to a point distribution?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigates the limits to information leakage by considering the least privilege principle. It formalises this notion under strict condition where any attribute other than the task label is deemed as sensitive for leakage. They propose a formal definition of LPP and under strictly positive posterior and the assumption that the label needs to be shared with the service provider, they theorise that there does not exists a a feature map such that both LPP and utility (as defined by mutual information between labels and feature representation) hold simultaneously.  They further support this with pairwise empirical evaluations across 12 attributes where one is considered as label and the other as the adversary’s targeted sensitive attribute. The analysis also compares inference gain under standard and censoring models. 

In my opinion the paper relies on some fundamental assumptions which have been clearly stated
- First, it’s a worst case analysis. This has also been highlighted in the Problem Setup (Section 2) and the text following Corollary 1.
- I think the assumption for label information to be made available is pretty strong from a practical perspective as users may not necessarily need to provide labels to the service provider.
- Unlike unconditional LPP, the LPP is defined with respect to what the authors consider as fundamental limit of leakage from the label.

### Strengths
I found the paper to be generally well written and easy to follow. While I am not familiar with all the current literature in this field, I found that the paper clearly states its worst-case assumptions and conveys its theoretical results with insights.

### Weaknesses
I found the discussion on how users can manage the trade-offs to be quite limited. There is some discussion on DP and its usefulness for training but not test time inference but I think some more discussion on what this theoretical analysis would mean for a user would be useful.

### Questions
Although I am not fully familiar with the related literature on this, I found the paper to be self-contained with insightful discussion. 
I voted for marginal acceptance because of the following, and would appreciate if authors can help clarify

1. Practical implications for users and service providers because of the noted limits
2. Arguments for why sharing label information is a practical worst-case assumption
3. How the work relates to privacy-preserving techniques other than censoring, like de-anonymisation or sharing the information under encryption etc? While I understand this may not be within the scope and/or page limit constraints, I think even qualitative arguments can help position the paper for discussion within the privacy and ML community.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This contribution addresses the concerns of data misuse when offloading model training and inference to a service provider. Collaborative learning and model partitioning are proposed as solutions, where clients share representations of their data instead of the raw data. The principle of least privilege is introduced, which states that the shared representations should only include information relevant to the task at hand. The authors provide the first formalization of the least-privilege principle for machine learning. They prove that there is a trade-off between the utility of the representations and the leakage of information beyond the task. Experiments on image classification demonstrate that representations with good utility also leak more information about the original data than the task label itself. As a result, censoring techniques that hide specific data attributes cannot achieve the goal of least-privilege learning.

### Strengths
This paper reveals the fundamental limits of Least-Privilege learning.

### Weaknesses
1. The presentaion needs improvement.

2. The contribution is limited.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies unintended privacy leakage in collaborative learning. Specifically, the paper proposes to  formalize of the least-privilege principle for machine learning. Via information theory, the paper observes that every task comes with fundamental leakage—a representation shared for a particular task must reveal the information that can be inferred from the task label itself. Such fundamental leakage is also testified in a real-world dataset

### Strengths
+The paper is well-written and easy to follow

+Understanding the fundamental information leakage in collaborative learning is important

### Weaknesses
-The key differences with the existing information-theoretic privacy is unclear

-The observations are only shown on a single dataset

-While the paper uses least-privilege principle to formalize information leakage, I do not know how this largely differentiate other works that use the similar idea (though those works assume a fixed sensitive attribute), e.g., Zhao et al., 2020; Brown et al., 2022 and Salamatian et al., Privacy-Utility Tradeoff and Privacy Funnel. What is the key technical challenge when we do not assume a fixed sensitive attribute, but assume it is a superset of the input?

Theoretically, the paper shows the fundamental leakage and observes this on a dataset. I am curious how common such observation is in more datasets.

The evaluation is only tested on a single attribute inference. How generalizable it is to more attribute inference (e.g., data reconstruction attack)?

### Questions
While the paper uses least-privilege principle to formalize information leakage, I do not know how this largely differentiate other works that use the similar idea (though those works assume a fixed sensitive attribute), e.g., Zhao et al., 2020; Brown et al., 2022 and Salamatian et al., Privacy-Utility Tradeoff and Privacy Funnel. What is the key technical challenge when we do not assume a fixed sensitive attribute, but assume it is a superset of the input?

Theoretically, the paper shows the fundamental leakage and observes this on a dataset. I am curious how common such observation is in more datasets. 

The evaluation is only tested on a single attribute inference. How generalizable it is to more attribute inference (e.g., data reconstruction attack)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the data attribute leakage problem in machine learning models. The core idea of this paper is that any representation that provides utility for prediction always leaks information about properties of the data other than the task. This work gives the definition of the least-privilege principle (LPP) and gives the theory of the trade-off between LPP and utility. The work also demonstrates this trade-off experimentally in an image classification setting.

### Strengths
This work theoretically analyzes the relationship between data attribute leakage and utility, which is important for the security of machine learning. This work also reveals the inherent properties of machine learning models.

### Weaknesses
1. The study of data attribute leakage is an active research field. Some work attempts to mitigate attribute leakage by designing sophisticated algorithms. This paper does not mention and compare cutting-edge defense schemes in the empirical experiment part.

2. More extensive experiments should be used to evaluate the proposed theory. At present, this work is only conducted on a dataset and a neural network model.

### Questions
1.	Advanced defense strategies should be discussed. If advanced defense strategies can solve the problem of data attribute leakage, then the value of this work will be limited. Therefore, could the author provide a more adequate overview of the research area discussed? It’s not just data attribute leaks, it should also include cutting-edge defense methods.
2.	Could the authors conduct empirical experiments on a wider range of datasets and models? For example, conduct experiments on some NLP tasks. More extensive experimental results can more fully verify the proposed theory.
3.	Does the complexity of the feature extractor affect the extent of data attribute leakage?
4.	There are some typographical errors in the paper. For example, formulas (12), (14), and (19) in Appendix A lack punctuation.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
