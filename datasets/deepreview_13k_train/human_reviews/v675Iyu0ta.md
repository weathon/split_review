# Interpretability Illusions in the Generalization of Simplified Models

- Decision: Reject
- Scores: 5, 8, 6, 6, 3

## Abstract
\looseness=-1
A common method to study deep learning systems is to use simpliﬁed model representations---for example, using singular value decomposition to visualize the model’s hidden states in a lower dimensional space. 
This approach assumes that the results of these simpliﬁcations are faithful to the original model. 
Here, we illustrate an important caveat to this assumption: even if the simpliﬁed representations can accurately approximate the full model on the training set, they may fail to accurately capture the model’s behavior out of distribution.
We illustrate this by training Transformer models on controlled datasets with systematic generalization splits, including the Dyck balanced-parenthesis languages and a code completion task.
We simplify these models using tools like dimensionality reduction and clustering, and then explicitly test how these simpliﬁed proxies match the behavior of the original model.
We find consistent generalization gaps: cases in which the simplified proxies are more faithful to the original model on the in-distribution evaluations and less faithful on various tests of systematic generalization.
This includes cases where the original model generalizes systematically but the simplified proxies fail, and cases where the simplified proxies generalize better.
Together, our results raise questions about the extent to which mechanistic interpretations derived using tools like SVD can reliably predict what a model will do in novel situations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study focuses on the question whether a simplified model (e.g., models obtained from dimensionality reduction or clustering) can still faithfully mimic the behavior of the original model on out-of-distribution data. This study conducts experiments on synthetic datasets constructed using the Dyck balanced-parenthesis language and shows that simplified models are less faithful on out-of-distribution data compared to in-distribution data and can under- or overestimate the generalization ability of the original model.

### Strengths
The paper focuses on a very important question, that is, whether the explanation model/proxy is faithful to the original model. Or more precisely, whether the explanation model can mimic the original model’s behavior on different data distributions. Some existing explanation methods, such as distilling the target model into a decision tree, cannot guarantee the faithfulness on out-of-distribution data (e.g., masked input samples). Therefore, it is of significant value to delve into this issue.

### Weaknesses
1.	I’m not familiar with the Dyck balanced-parenthesis language used in this paper, so I feel a bit confused and overwhelmed reading Section 2.1. It would be a great help if the authors can give some toy examples when introducing the Dyck languages.
2.	The phrase “simplified models” can be misleading in this paper’s context. I was thinking of methods such as knowledge distillation or network pruning when I first see the phrase “simplified models”. However, what the paper mainly focuses on are dimensionality reduction and clustering methods. It is encouraged to use a more precise word other than “simplified”.

3.	I'm still confused about how one would consider a testing set *in-distribution* or *out-of-distribution*. I think one important claim of the paper is that "simplified models" (models obtained from dimensionality reduction or clustering) may well capture the original model's behavior on in-distribution data, but fail to do so on out-of-distribution data. To validate this claim, a clear definition (or a dichotomy) of in-distribution data and out-of-distribution data is needed. The claim that "some aspect of the data can be considered 'out-of-distribution' and some can be considered 'in-distribution' "makes the boundary between *in-distribution* or *out-of-distribution* testing sets even more ambiguous. It seems like there is actually **no** in-distribution testing set in the experiments. If the testing set named **IID** is also considered out-of-distribution, then does it mean that only the training set is considered *in-distribution*, but all other testing sets are considered *out-of-distribution*? If so, I think it is more interesting to consider **both an in-distribution testing set and an out-of-distribution testing set**. For example, in image classification, if a training set consists of dog images with a grass background, an in-distribution testing set could consist of other dog images with a grass background, while an out-of-distribution testing set consists of dog images with a water background. This would be a more compelling experimental setting.

4.	About the validation of the claim that "the simplified model underestimate/overestimate the generalization ability of the original model". The authors seem to make the following explanation: because the original model achieves near-perfect accuracy on out-of-distribution testing sets, and the output of the simplified model deviates heavily from that of the original model on these testing sets, one can conclude that the simplified model does not perform well on these testing sets, which means they "underestimate" the generalization ability. However, this chain of logic is quite indirect and awkward. I would suggest conducting a direct experiment to validate this claim.

### Questions
I have several confusions when reading the paper, and hope these can be resolved by the authors’ rebuttal.

1.	In Section 2.1, the authors construct different testing datasets (named as **IID, Seen struct, Unseen struct (len <= 32), Unseen struct (len > 32), and Unseen depth**, respectively) to evaluate the model’s generalization ability. I wonder which of these testing datasets are considered in-distribution datasets, and which are out-of-distribution datasets? It seems not clear from the paper.
2.	After reading Section 5.1, I’m still confused about how to interpret the results in Figure 4. I only see as the number of components or the number of clusters increase, the simplified model becomes more similar to the original model (the JSD between the attentions decreases, while the ratio for predicting the same token increases). However, I’m not sure how one can conclude that there is a generalization gap between the simplified model and the original model. I’m also not sure how one can conclude that the simplified model underestimate/overestimate the generalization ability of the original model. Is it more appropriate to compare the prediction accuracy of the simplified model with that of the original model on both in-distribution and out-of-distribution data?

Furthermore, combined with Question 1, if the testing set named **IID** is considered in-distribution, and the testing set named **Unseen struct (len>32)** is considered out-of-distribution, then why are the curves on these two testing sets so similar to each other?

### Soundness
2 fair

### Presentation
2 fair

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
The paper provides a case study of using simplified model to interpret a trained transformer model on an algorithmic task. It's shown that using dimension reduction or clustering to simplify the model down to a proxy model may yield interpretability illusion. In particular, the simplified proxy model is not faithful in out-of-distribution settings, and cannot be used to reliably predict the original model's OOD error.

### Strengths
The paper is focused on a classic formal language task (Dyck grammer) and provides a convincing case study of interpretability illusion in Transformer language model. I think the main observation from the paper is interesting and quite relevant. 

The distributions are novel, as prior work in mechanistic interpretability mostly gives positive results. 

I think the main result is surprising, where the simplified model generalizes less well to OOD data than the full model, where intuitions from learning theory would suggest the opposite.

The paper is well-written and the illustrations are clear.  It also gives a good survey of related work.

### Weaknesses
While the paper delivers a strong conceptual message, at a technical level, it is a single case study on a somewhat toy algorithmic task. That is, the scope of the work is a bit limited. I personally would be interested in a broader study on similar formal language tasks (for example, on other languages expressed by finite-state automata https://arxiv.org/abs/2210.10749).

The paper would also be stronger if it looks into why the simplified model generalizes less well to the depth split. Figure 6 is an interesting observation. What is really being truncated by SVD (which plays a role for OOD generalization)? Is there any mechanistic story here?

Minor suggestions
---

Figure 2(a)(b) should be accompanied by a color scale. Does yellow indicate 1 and green indicate something less than 1?

Also, for Figure 2(a) and related experiments, if you don’t prepend the START symbol, what would the attention pattern look like? Does that affect any of your results here?

“Second, the value embeddings encode more information than is strictly needed to compute depth, which might suggest that the model is using some other algorithm” — Can you expand on this? What is the extra information, if you have looked into it all?

### Questions
I have asked a few questions above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an analysis of transformer models trained on the Dyck languages. To do so, the models are simplified and analyzed with data-dependent and data-independent tools, highlighting a discrepancy between the behaviour of original models and simplified models on out-of-distribution data.

### Strengths
The paper provides several methods to analyse transformers trained on the Dyck language, investigating whether simplified versions of the model are faithful to the original one on out-of-distribution test sets.

### Weaknesses
Being unfamiliar with the literature, it is hard for me to understand the point of the analysis, and it is hard to tell whether that is due to a poor presentation or due to my lack of understanding. However, what I find a weakness of the paper is the fact that the analysis is not paired with proposed improvements or solutions. For example, what do the results from the paper entail? Is it that transformer models are not suitable for learning language models? Or is it that using model simplifications, while facilitating the analysis of some properties of the model, leads to a mismatch with the original model on out-of-distribution samples? If so, what would be a better way to analyze transformer models, to avoid the found shortcomings of current methods?

### Questions
In addition to the questions in Weaknesses:

- What conclusions can be drawn from Deep Learning practitioners? Are transformers reliable for learning languages?
- Does the analysis extend also to similar models or other datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper describes how much the simplified transformer models represent the behaviour of the original ones.

The authors consider a use case of Dyck balanced-parenthesis languages and show that while the simplified proxies, using hard (one-hot) attention, show alignment with the behaviour of the original models, they do not match the behaviour out-of-distribution. They use the evaluation methodology as per Murthy et al (2023) which involves predicting closing brackets at least ten positions away from the corresponding opening brackets and evaluating the  highest-likelihood prediction accuracy.

### Strengths
Pros:
- (Originality) The originality of the paper stems from analysing the claims of interpretability

- (Significance) It is important to see the detailed analysis of limitations of simplified models on a simple example which would highlight the deficiencies of such models.

- (Quality) The paper thoroughly addresses reproducibility

- (Clarity) The paper is clearly written (however, see Q1-Q3)

### Weaknesses
Cons:

- (Elements of significance) Given that the analysis focuses on Dyck balanced-parenthesis languages, it is largely limited and arguably backs up the intuitive claim that the simplified models do not fully represent the behaviour of the original models; however, I still think that it  is still significant because we have such evidence described in detail as it helps inform large-scale model interpretability studies



### Questions
1. In Figure 6, it seems like for the longer key depths, the predictions diverge more. Would the authors be able to emphasise more whether it is always the case and if there are any solid reasons behind this particular behaviour?

2. In Figure 1 description it is stated that ‘On the depth generalization split, the models achieve approximately 80% accuracy.’ Is it 80% or around 75% as can be seen in the purple curve on the image? (It does not affect any conclusion, just found that I could not fully explain this discrepancy)

3. “However, the error patterns diverge on depths greater than ten, suggesting that the lower-dimension model can explain why the original model makes mistakes in some in-domain cases, but not out-of-domain” To what extent does it  happen consistently across different training trajectories of the stochastic gradient descent and/or across different datasets? In other words, plausible it sounds, would the same tendency repeat if we change the data or train the model again?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper offers an analysis of the extrapolation performance of several simplified representation methods used to understand the information processing of deep architectures. The analysis is solely focused on Transformers trained on Dyck-k languages, which consists of strings of matched brackets of k different types. These models are tested in and out of distribution by manipulating the maximum hierarchical depth and other parameters. The study considers two simplified models: PCA and k-means clustering of the key and query embeddings of the transformer layers. The authors conclude that these simple methods offer a good description of the model in-sample, but fail to explain the behavior of the model out-of-sample.

### Strengths
- The paper is well written and it contains several interesting considerations on the nature and interpretation of transformers.
- The problem area is vitally important to the implementation of AI in real-world applications, and the focus on out-of-sample performance is interesting and well motivated.
- The experimental analysis is detailed and rigorous.

### Weaknesses
The focus of the experimental analysis is too narrow. The introduction section does a good job in outlining the research goals, but this aim is then overly specialized to a specific class of models trained on a toy problem. It is therefore very difficult to extrapolate the conclusions of the paper outside of its narrow domain, which in itself is not very useful for the broader literature. The use of Dyck-k languages, while providing a controlled environment, severely limits the applicability of the findings to more complex, real-world scenarios. The analysis is limited to Transformers, and even within that class, only to models trained on these artificial languages. This makes it unclear whether the observed discrepancies between simplified representations and actual model behavior would generalize to other architectures or tasks. The paper does not explore the impact of different training regimes, such as varying the size of the training dataset or the optimization algorithm, which could significantly affect the extrapolation performance of the simplified models. The study also lacks an analysis of the sensitivity of the results to the specific parameters of the PCA and k-means clustering methods, such as the number of components or clusters used.

### Questions
- Can you include the analysis of other datasets and architectures? I do appreciate your work on toy-languages. However, I would like to see these insights to be applied  to models trained on naturalistic data.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
