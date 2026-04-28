# What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Language models deployed in the wild make errors. 
However, simply updating the model with the corrected error instances causes catastrophic forgetting---the updated model makes errors on instances learned during the instruction tuning or upstream training phase. 
Randomly replaying upstream data yields unsatisfactory performance and often comes with high variance and poor controllability. %Precisely identifying forgotten examples is computationally intractable with a large upstream dataset.
To this end, 
we try to forecast upstream examples that will be forgotten due to a model update for improved controllability of the replay process and interpretability. 
We train forecasting models given a collection of online learned examples and corresponding forgotten upstream pre-training examples.
We propose a partially interpretable forecasting model based on the observation that changes in pre-softmax logit scores of pretraining examples resemble that of online learned examples, which performs decently on BART but fails on T5 models. We further show a black-box classifier based on inner products of example representations achieves better forecasting performance over a series of setups. Finally, we show that we reduce forgetting of upstream pretraining examples by replaying examples that are forecasted to be forgotten, demonstrating the practical utility of forecasting example forgetting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to predict what kind of information is forgotten when further training language models.
In particular, it proposes a partially inter-pretable forecasting model based on the observation that changes in pre-softmax logit scores of pre-training examples resemble that of online learning examples. Further a black-box classifier based on inner products has improved the forecasting performance. Based on the forecasting model, using examples that are forcasted to be forgotten to train the model can mitigate the forgetting issue.

### Strengths
1. The idea of predicting forgotten examples are novel.
2. The method is quite easy to understand and implement.
3. Solving the forgetting issue has practical application values in pretrained language models.

### Weaknesses
1. The experiment results reveal that the improvement over the baseline is quite marginal.
2. A more insightful experiments could be done to analyze why some examples are more import than others when training the model in terms of forgetting.
3. The relation between the further-training and forgetting is not quite clearly explained.

### Questions
1. Are the predicted samples sensitive to the training order of the same set of samples?
2. How the forgotten samples are related to the training data, learning rate, etc?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In a continual learning framework focused on LM’s the authors study the problem of  predicting which samples from the upstream data a model is likely to forget after it has been trained on new data.  This is then also used to improve the samples selected for replay from upstream data (focusing on the ones to be forgotten).

### Strengths
- The authors focus on a timely and relevant setting of continual learning for LMs
- The approach is computationally efficient and reasonably well motivated
- The authors point out an interesting phenomenon of logit change
- Results of using forecasting for augmenting replay seem to be promising

### Weaknesses
- The experiments can benefit from some quantitative results about the computational efficiency, for example in Table 4 what is the overhead of the approach compared to replay w/random
- The authors describe several prior works on forecasting (albeit not in the LM space) it would be interesting to experimentally compare these methods to the proposals

### Questions
It would be interesting to know if the method and observations are applicable to classification problems or other continual learning domains

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the challenge of catastrophic forgetting in language models during continual refinement. They introduce a framework to predict which pretraining examples will be forgotten when a model is fine-tuned on new tasks. They propose some baselines and new approaches based on estimating logit change in pretraining sample when a model is finetuned on a new sample. Empirically, the proposed approach work only in one setting on BART models and fails on FLAN-T5 models (more commonly used and large scale).

### Strengths
- Problem statement is well motivated
- Thorough experimentation with proper baselines considered 
- The paper builds up and formalizes an interesting problem which is going to be studied a lot in near future.

### Weaknesses
- Writing is quite poor for the methods section. Even after repeated reading, I could not understand how exactly $h$ is being learned for the trainable logit based forecasting. How does one train a LM which maps inputs to h(x), where h(x) is supposed to model the gradient of the model at x wrt $\theta$. I cannot find any details about this or some reference about this. 
- Authors should clarify in Table 1 that they are predicting a minority class of forgotten examples in a binary classification setting. Hence F1 scores lower than 50% still make sense. In general, the writeup is quite poor. 
- Poor empirical results on real large scale models : The proposed approach is heavily reliant on order 1 approximations of training dynamics, which do not hold true of large models as seen empirically. There are quite marginal gains of vanilla baseline of frequency based forgetting prediction on FLAN. Although I do thank the authors for acknowledging this fact, it still remains a major concern about efficacy and practicality of proposed approaches in the paper.

### Questions
See weakness section

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for mitigating catastrophic forgetting in instruction tuned language models, by building an interpretable forecasting model that predicts which training examples will be forgotten during model refinement, and replaying these examples. The authors compare a logit-based approach, which predicts how token logits on a pretraining example change before and after the model sees the online learning example, and a representation-based approach, which directly predicts whether the online learning example will cause a pretraining example to become erroneous using the latent representations of each example. Although the logit-based approach is more directly interpretable, the representation-based approach is robustly stronger at forecasting as well as mitigating forgetting across various settings (tuning heads only vs. LORA vs. all weights, different types of models).

### Strengths
This presents a novel and simple approach to tackle catastrophic forgetting, with clear problem formulation and strong motivation (Fig. 1-2 are very good). The paper is easy to read and clearly presented. The authors perform very thorough and thoughtful experiments that convincingly support their proposed method.

### Weaknesses
The computational efficiency discussion is very good, but I think reporting actual runtimes for some example settings would also be helpful. E.g. tuning the head only should be faster than the whole model, so I think the asymptotic complexity only tells half the story. It will also help practitioners consider how feasible this method is for their own application.

### Questions
Not sure if I missed this but why do the authors hypothesize the logit-based approach is less effective on FLAN vs BART?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
