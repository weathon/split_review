# On the Joint Interaction of Models, Data, and Features

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Learning features from data is one of the defining characteristics of deep learning, but our theoretical understanding of the role features play in deep learning is still rudimentary. \yj{To address this gap,} we introduce a new tool, the \emph{interaction tensor}, for empirically \yj{analyzing} the interaction between data and model through features. With the interaction tensor, we make \yj{several key} observations about how features are distributed in data and how models with different random seeds learn different features. \yj{Based on these observations, we propose a conceptual framework for feature learning. Under this framework, the expected accuracy for a single hypothesis and agreement for a pair of hypotheses can both be derived in closed-form.} We demonstrate that the proposed framework can explain empirically observed phenomena, including the recently discovered Generalization Disagreement Equality (GDE) that allows for estimating the generalization error with only unlabeled data. \yj{Further, our theory also provides explicit construction of natural data distributions that break the GDE.} Thus, we believe this work provides valuable new insight into our understanding of feature learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the interaction tensor which is a binary 3-dimensional tensor T describing the presence of certain features in both model and data point, i.e., if $T_{tmn} = 1$ implies that $t_{th}$ feature is present in both $m_{th}$ model and $n_{th}$ data point. The construction of the interaction tensor is based on the correlation analysis between PCA-reduced features of penultimate layers of the collection of models on the given dataset. Authors utilize this interaction tensor to empirically analyze properties of feature learning and propose a feature learning model based on their observations. Using this feature learning model they focus on analysing recently proposed Generalization Disagreement Equality and given which conditions GDE can arise.

### Strengths
Understanding how models learn is an important topic in modern deep learning. Authors build the new framework to describe feature learning from the different perspective which allows to describe recently observed phenomenas. I think that this new perspective provides a valuable contribution to the community and can facilitate further developments in this area. In addition, I personally liked the construction of a natural dataset on which deep ensemble is not well-calibrated in-distribution and where GDE fails.

### Weaknesses
Honestly, I don't see obvious weaknesses of the proposed framework and study.

### Questions
1. Given that construction of interaction tensor depends on thresholding ($\gamma_{corr}$ and $\gamma_{data}$), how important are these hyperparameters? How to properly set them?
2. Currently theoretical framework analyzes binary classification, does the analysis extend to multi-class classification?
3. Does the framework allow for introducing distribution shifts and etc?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the interaction between data and model through feature to understand deep learning from the feature learning perspective. Based on their observations, they propose a framework to characterize the quality and process of feature learning, with theoretical support. Some empirical results are provided to validate their approach.
.

### Strengths
1) To catch on feature learning process during deep learning is a key problem in community.
2) Paper provides a practical framework with solid theoretical analysis. 
3) Empirical results on different datasets are provided. And clear experimental details are listed.

### Weaknesses
Figure 1 is a bit vague. It is recommended to replace it with a clearer version.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the interaction tensor, for empirically analyzing the interaction between data and model through features. Based on some observations using this tensor, they propose a very simple toy model (a combinatorial model) for feature learning. They show that this model also exhibits Generalization Disagreement Equality (GDE). Finally, the authors use their model to provide data distributions that break GDE in real world experiments.

### Strengths
- The problem of feature learning is quite important and there has been a lot of attempts for gaining a better theoretical understanding of it in recent years.

- The authors are able to come up with a toy model that shows GDE which is a very important phenomenon (and it does need the explicit assumption of calibration).

- The model that the authors propose is simple and it can be analyzed fully.

- The paper is very well-written.

### Weaknesses
 - I definitely agree with "the empirical phenomena of deep learning can be understood at many different layers of
abstraction". However, I think the model proposed in this paper is too simplistic. The implicit biases of deep learning are core to some of the merging phenomenon that we see these days and the models that the authors propose fails to capture that. I also think that a good toy model should leave the door open to generalizations and getting closer to real world practice (for example, for the random features model of deep learning, there is a very obvious way to move towards making it more realistic). But the models that the authors propose is too abstract and it is not clear what simplifications are made to the real problem to arrive at the proposed model.

- Although the model is based on some observations using the interaction tensor, I still find the model to be not very well motivated. Any insights on how this can relate to the training of deep nets?

- It is not very clear how the authors set the hyperparameters in their model (e.g., the thresholds).

- The notations are a bit confusing (i, j, k, etc.). I suggest authors avoid using these generic letters. Also, the paper will benefit greatly from a figure that summarizes all the notations (p_d, p_r, etc.). It will also help explain the method.

- The authors "prove" GDE in their model without the explicit assumption of calibration. But the model is very abstract/high-level and I'm not sure if the assumptions that they make are stronger or weaker than calibration.

- The theoretical understanding of feature learning is not as rudimentary as the authors claim. For example,

[1] Alex Damian, Jason Lee, and Mahdi Soltanolkotabi. Neural networks can learn representations with gradient descent, 2022.

[2] Zhichao Wang, Andrew Engel, Anand Sarwate, Ioana Dumitriu, and Tony Chiang. Spectral evolution and invariance in linear-width neural networks, 2022.

[3] Eshaan Nichani, Alex Damian, and Jason D Lee. Provable guarantees for nonlinear feature learning in three-layer neural networks, 2023.


[4] Yatin Dandi, Florent Krzakala, Bruno Loureiro, Luca Pesce, and Ludovic Stephan. Learning two-layer neural networks, one (giant) step at a time, 2023.

[5] Behrad Moniri, Donghwan Lee, Hamed Hassani, and Edgar Dobriban, A theory of non-linear feature learning with one gradient step in two-layer neural networks, 2023.

### Questions
- Looking at figure 3 (a) and 3 (c), it seems that the observations made from them are not that significant. Am I missing something? How does the choice of the thresholds affect your observations?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel framework for analyzing feature learning in deep NNs, from the perspective of observed phenomena occurring in trained networks. The learnt features in a trained model are defined as the principal components of the last layer's activations, and the proposed interaction tensor examines these feature representations of a dataset for a set of models. The interaction tensor is used to empirically validate several common-sense intuitions, such as feature distribution being long-tailed, which then leads to a further abstracted framework for combinatorial-style analysis. This framework is able to theoretically demonstrate empirical phenomena from the observations as well as prior works such as GDE.

### Strengths
- Due to the increasingly complex nature of deep networks, the concept of studying feature learning's observed phenomena like a natural science is a useful supplement to more derivation-based frameworks such as NTK
- The combinatoric analysis is a creative and original perspective for studying feature learning. While the simplifications might seem a little overly-simplistic at first, the experiments in section 6 and observations in section 4 serve as adequate motivation
- The resulting findings of the framework not only validate but add nuance to understanding of prior phenomena such as GDE

### Weaknesses
 - Like any theoretical framework, many assumptions went into the combinatorial analysis. In particular, this framework assumes features and datapoints are each either dominant *or* rare, a dominant/rare datapoint always has the same number of dominant/rare features, etc. This binary simplification, while useful for initial analysis, may not fully capture the nuanced interactions between features and data points in real-world scenarios. For instance, the assumption that a dominant datapoint always activates the same number of dominant features and vice versa is a strong constraint that could limit the framework's applicability to more complex datasets.
- The framework is less useful for understanding the learning process of networks, such as why some runs might collapse while others successfully learn the desired features. The analysis focuses on the post-training state, neglecting the dynamic evolution of feature representations during training. This limits its ability to explain phenomena like mode collapse or the emergence of specific feature hierarchies.
- Some minor typos: section 5, data generating process paragraph's second-to-last sentence samples $n_r$ rare, not dominant, features. Appendix C, equation line 34 the two $\not = \emptyset $ could maybe instead be $= \emptyset$

### Questions
- While simplifying features and datapoints to be either dominant *or* rare is good enough for the section 6 experiments, have you considered modeling the rare-dominant variation as a spectrum instead of a binary? For instance, looking at figure 2b, I'm not sure where I would want to draw a line to separate the rare from the dominant features. Even putting the line somewhere around x=6.5, there is still a relatively large deal of variation of frequency of occurrence in both the rare and the dominant feature types

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
