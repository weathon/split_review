# Functional Classification Under Local Differential Privacy with Model Reversal and Model Average

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Local differential privacy (LDP) has been a focal point in data privacy research, yet its application in the field of functional data classification remains underexplored. To address this gap, we present a novel approach that tackles the challenge of infinite dimensionality in functional classification under LDP constraints. The main idea is to leverage the inherent property of functional data---which allows it to be approximated by a linear combination of basis functions---to reduce the dimensionality of data and facilitate the process of model training under LDP constraints. Specifically, we propose algorithms for constructing functional classifiers designed for both single-server and heterogeneous multi-server environments under LDP. In single-server scenarios, we introduce an innovative allocation strategy where fewer samples are used for training multiple weak classifiers, while the majority are used to evaluate their performance. This enables the construction of a robust classifier with enhanced performance by model averaging. We also introduce a novel technique, ``model reversal", which effectively enhances the performance of weak classifiers. In multi-server contexts, we employ federated learning and enable each server to benefit from shared knowledge to improve the performance of each server's classifier. Experimental results demonstrate that our algorithms significantly boost the performance of functional classifiers under LDP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of (binary) classification for functional data, under local differential privacy.

Their approach is as follows: First they project the functional data onto a finite subspace and express it in a finite basis. This would make the data look like a point in $\mathbb{R}^d$. In order to reduce sensitivity, they apply either the $\tanh$ or the $\min$-$\max$ transformation to each point to make each coordinate bounded. This would give us bounded sensitivity. After that they train a classifier on the privatized transformation of the data.

In order to mitigate the effect of the noise they use a boosting technique, specifically they use model averaging: they divide the users into two groups, one for training and one for validation, and divide each of those two into $B$ parts. Then they design $B$ weak classifiers, one for each part of the training set and the evaluate them on the corresponding part from the validation set. Each validation user then outputs the result of the validation, with a randomized response mechanism to ensure privacy. If the answer from the aggregation of randomized response is less than 50% accurate, we negate the sign of the classifier to obtain a better classifier (Model Reversal). In order to design a final classifier using the $B$ weak classifiers and the validation outputs, they use the validation outputs to design a set of weights, and then to create the final classifier, they take a weighted average of the $B$ weak classifiers (Model Averaging).

They also provide a similar technique for combining the results of $K$ servers.

They run several experiments to compare the performance of their model against the naive model that uses all of the training data to train a single classifier and compare different threshold levels for Model Averaging.

### Strengths
I think this is the first paper that considers the problem of functional classification under local differential privacy.

From their experiments it seems like the accuracy of their approach is better than the naive baselines by 10 to 20 percent. The naive baselines include: all of the data is used to train one model, or we're doing model averaging but all of the weights are equal.

### Weaknesses
My main concern is limited novelty in the techniques. Apart from the part initial dimensionality reduction and encoding part, which are standard techniques, I think the rest of the techniques are independent of the functional classification setting specifically. Overall, it seems like once we're done with dimensionality reduction and encoding everything is the same as in $\mathbb{R}^d$.

The effect of model reversal in the experiments seems pretty small.

### Questions
It is mentioned that the ignored residual function contributes to privacy protection. I think that requires more explanation.

I think the budgeting for privacy at the top of page 4 is wrong. When running the Laplace mechanism and assuming sensitivity is some $\Delta$ you need to sample noise from $\mathcal{L}(\frac{\Delta}{\epsilon})^{\otimes d}$. You don't need to add a multiplicative $d$ for each dimension.

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies functional classification under local DP constraints. Specifically, the paper proposes a privatization step for each client using a projection-based dimensionality reduction technique. Then this paper also proposes a model average and a model reversal method to enhance the performance of the classifier. Finally, this paper also studies the same problem under heterogeneous multi-server setting.

### Strengths
1. This paper is the first to study functional classification with LDP constraints.
2. The proposed method is simple and practical.

### Weaknesses
1. It would be better if the authors could add some intuition and discussion about the result in Theorem 2 and 3. Specifically, the current presentation lacks a clear explanation of why the derived bounds are meaningful in the context of functional classification under local differential privacy (LDP). The practical implications of these theorems are not immediately obvious, and a more detailed discussion of how these results translate to real-world performance would be beneficial. For instance, what are the key factors that influence the variance of the accuracy estimate, and how can these factors be controlled in practice?
2. The proposed method is built on the dimension reduction scheme and laplace mechanism which does not seem to be very novel. While the combination of these techniques might be novel in this specific context, the paper does not adequately address the limitations of using these well-established methods. For example, the choice of dimensionality reduction technique can significantly impact the performance of the classifier, and the paper does not provide sufficient justification for the specific choice made. Furthermore, the Laplace mechanism, while simple, might not be optimal in terms of utility-privacy trade-off compared to other more advanced mechanisms.

### Questions
Please see weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Functional data is infinite-dimensional data which can be approximated by a linear combination of basis functions; this paper explores how to classify functional data under the constraint of local differential privacy (LDP). The authors demonstrate how to construct “weak” functional data classifiers under LDP, and then demonstrate how to boost the weak classifiers’ performance using model averaging (which combines the weak classifiers) and the novel technique of “model reversal” (which flips the signs of a weak classifier’s coefficients). The authors combine these techniques into algorithms for both single-server and multi-server (i.e., federated learning) settings.

### Strengths
1. The problem setting as well as the proposed algorithms are quite novel. In particular, I think that the idea of model reversal is kind of fun and creative.

2. The experimental results also seem to show that using the proposed methods does improve classification accuracy.

### Weaknesses
1. The setting seems obscure and not very well-motivated. I don’t really understand the significance of functional data and where it’s found in real-world applications.

2. I’m not fully convinced by the empirical evaluation. The experimental results show that the proposed techniques improve classification performance, but at the same time the baselines don’t set a particularly high bar to beat. While I understand that a little-explored setting won’t have much previous work to compare to, it is still hard to judge the importance of the methods without them. And touching back on Weakness #1, the experiments are all conducted on a synthetic dataset and so it’s unclear how well the methods will generalize to real-world data.

### Questions
1. Would it be possible to give more details on the practicality of functional data? For example, are there realistic datasets that are considered to be “functional data” and how do the properties of functional data translate to the real world?

2. Is there a formal definition for a “weak classifier”?

3. The functional data classifiers are constructed under LDP, and then it seems to me that the LDP setting is kind of irrelevant to the rest of the paper (or at least, to the model average and model reversal techniques). Similarly for the functional data setting, after dimensionality reduction and re-scaling. Do MA and MR actually have anything to do specifically with LDP (or with functional data), or are they general techniques that could be used to improve the performance of any collection of weak classifiers?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors have provided a method for adding noise to functional classifiers to satisfy Local Differential Privacy (LDP). In the context of federated learning, the authors introduce the idea of using more clients to evaluate the performance of weak classifiers and propose the concept of model reversal, which involves inverting the parameters of models with poor accuracy. Additionally, the authors propose a federated learning approach for the heterogeneous multi-server setting under LDP.

### Strengths
1.The paper introduces a novel approach to functional data classification under Local Differential Privacy (LDP), a topic that has not been extensively explored in the existing literature.  
2.The introduction of model reversal is particularly innovative, as it provides a unique solution to enhance the performance of weak classifiers by inverting their parameters when their accuracy is below a certain threshold.

### Weaknesses
1.Differential Privacy (DP) has already proven to be sufficiently effective in protecting individual privacy, for instance, in defending against membership inference attacks. Moreover, there are numerous existing methods within DP for adding noise to functional input data, where the idea of projecting onto a set of finite bases is also quite common. From this perspective, the innovation of projection might not be high enough, and the necessity of employing Local Differential Privacy (LDP) remains to be further examined.At the same time, the performance degradation caused by residuals has not been analyzed theoretically. The expressive power of a finite basis is quite limited, and for some functions, their residuals could be fatal.

2.Regarding the ideas of model average and model reversal proposed by the authors, compared to traditional ensemble techniques, model average utilizes more clients in the evaluation process, aiming to select better weak classifiers. For each poor classifier, a model reversal approach is employed for improvement. However, since only a small number of clients are used to train the parameters, the classifiers might generally perform poorly; model reversal can enhance the performance of the learners, but it may not necessarily improve them to a satisfactory level. Theorem three provides an expected conclusion, but it does not directly lead to a high-probability bound; the theoretical analysis of model reversal is still lacking.

### Questions
1..Are there specific scenarios or use cases where LDP provides a clear advantage over DP in functional data classification?

2.The idea of projecting data onto a finite basis is quite common in the realm of DP. Could you clarify how your approach innovates or differs significantly from existing methods?

3.The theoretical analysis of model reversal seems to be lacking. Could you provide more details or elaborate on the theoretical foundations of this technique?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
