# Preventing Model Collapse in Deep Canonical Correlation Analysis by Noise Regularization

- Decision: Reject
- Scores: 3, 3, 6, 1

## Abstract
Multi-View Representation Learning (MVRL) aims to learn a unified representation of an object from multi-view data.
Deep Canonical Correlation Analysis (DCCA) and its variants share simple formulations and demonstrate state-of-the-art performance. However, with extensive experiments, we observe the issue of model collapse, {\em i.e.}, the performance of DCCA-based methods will drop drastically when training proceeds. The model collapse issue could significantly hinder the wide adoption of DCCA-based methods because it is challenging to decide when to early stop. To this end, we develop NR-DCCA, which is equipped with a novel noise regularization approach to prevent model collapse. Theoretical analysis shows that the Correlation Invariant Property is the key to preventing model collapse, and our noise regularization forces the neural network to possess such a property. A framework to construct synthetic data with different common and complementary information is also developed to compare MVRL methods comprehensively. The developed NR-DCCA outperforms baselines stably and consistently in both synthetic and real-world datasets, and the proposed noise regularization approach can also be generalized to other DCCA-based methods such as DGCCA.git}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to deal with the “model collapse” problem of deep canonical correlation analysis. The technical approach is to introduce a noise regularization term.  Basically, the regularization asks that, in each view, the correlation with Gaussian noise before transforming the data and after transforming the data to be similar. Some properties of such regularization under the linear case is studied.

### Strengths
The reviewer does agree with the paper that the DCCA formulation itself does not guarantee meaningful representation learning, as the learned solution may lose information of the data. 
However, this is a well recognized problem and was studied from many aspects in the literature (DCCA was from 2013 and some fixes were proposed in Wang et al 2015 already) - some of them have rigorous and interesting proofs, which this submission lacks.

### Weaknesses
**The mathematical rigor of this submission is questionable.** The so-called “model collapse” seems to have no rigorous definition. There is a mentioning “The correlation between unrelated data increases as the collapsed model transforms any data to a degenerated feature space” in the end of Section 3. This seems to imply that model collapse equals to finding a “degenerated feature space”, which also does not have a rigorous definition.

**The discussion/comparison with existing methods is lacking.** My understanding is that the noise regularization is a heuristic to make the learned representation have relatively large entropy - so that the solution is not “collapsed” or “degenerated”. This is a reasonable heuristic. The paper did not provide any other justifications other than intuition. Note that it is unclear why the proposed method is better at avoiding degenerated solutions compared with many existing methods, e.g., the DCCAE [wang et al 2015], i.e., deep CCA with an autoencoder to maintain the information from data. The paper mentioned that "... Wang et al. (2015) introduces the reconstruction errors of autoencoders to DCCA ... However, the model collapse issue of DCCA-based methods has not been explored and addressed". However, it is clear to me that the autoencoder can effectively avoid degenerate solutions. As there is no formal definition of "model collapse", it is unclear why DCCAE cannot avoid it.

**The key claimed theoretical contribution is questionable.** One of the key claimed contributions is “Rigorous proofs are provided to demonstrate that the full-rank property of the transformation in the CCA method is the key to preventing model collapse, which justifies the developed noise regularization approach from a theoretical perspective. ” There are a series of concerns regarding this claim and its related developments. 

-  First, the major theorem (Theorem 1) is a little hard to comprehend. It says eta_k = 0 if and only if the square matrix W_k has full rank. It is not easy to follow why a square matrix is applied for CCA as CCA almost always uses a “fat matrix” W_k for dimensionality reduction. Hence, it is hard to understand how this theorem is useful in practice. 

-  Second, more importantly, using the linear case to argue for nonlinear cases seems to be far-fetching. Note that even if X_k has zero-mean, there is no guarantee that f(X_k) still has zero mean. This basically breaks the proof of the linear case immediately. Saying that ``rigorous proof for linear cases’’ can be used to justify the nonlinear case is not convincing. 

-  Third, it is hard to understand the relation between “full rank W_k” and “model collapse”, as these terms are never formally defined or linked together. 

-  Fourth, Definition 2 seems to be arbitrary.

### Questions
I do not have questions for the authors.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an algorithm for regularizing the multi-view deep CCA model with noise. Specifically, the algorithm introduces additional loss terms that encourage the correlation between DNN output of signal and noise, to be consistent with linear mapping output of signal and noise.

### Strengths
I like that the authors somewhat carefully designed numerical simulations to test their method.

### Weaknesses
I have several concerns.

1. Important references and discussions are missing. The fact that powerful neural networks could lead to degenerate feature space is known. In the original deep CCA paper [Andrew et al, 2013] there was already ridge regularization of the auto-covariance matrices (see their eqn 5) to avoid degeneracy and improve numerical stability. And that regularization technique was already studied for linear CCA, see
- De Bie and De Moor. On the regularization of canonical correlation analysis, 2003.
and an probabilistic interpretation where a Gaussian observation model leads to regularized covariance matrices
- Bach and Jordan. A Probabilistic Interpretation of Canonical Correlation Analysis. 2005.
While the authors' proposal appears different, it is still important to discuss the connections to existing methods and compare with them, both theoretically and empirically.

2. The intuition behind the proposal is not super clear to me. If the goal is to have full-rank f(X), so that the covariances are better conditioned, the abovementioned covariance regularization approach already achieves the same effect. If I look at Proposition 4, it essentially says CCA is invariant to linear transformations of input; but this is well-known and easy to see from the original formulation, even without complicated linear algebra. The more interesting analysis would be to explain why the correlation between signal and random noise is a good quantity for deep neural networks to mimic; there must be more structure than saying that fk is full-rank in my opinion.

3. The paper is not purely about optimization and numerical stability. And I expect to see different inductive bias from the proposed regularization. There shall be investigation of the feature quality on real-world datasets, as shown by prior deep CCA-based papers.

### Questions
- I hope to see non-trivial analysis regarding the effect of noise regularization.
- I hope to see comparison of feature quality against alternatives.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this study empirically observe a critical issue of model collapse in DCCA-based methods. This phenomenon is characterized by a significant drop in performance as the training progresses. The model collapse issue poses a substantial challenge to the widespread adoption of DCCA-based methods, as it becomes difficult to determine the appropriate stopping point during training. To address this issue, the authors introduce NR-DCCA, which incorporates a novel noise regularization approach designed to prevent model collapse. Furthermore, they provide theoretical insights demonstrating that maintaining the full-rank property is essential for preventing model collapse, and the proposed noise regularization effectively enforces this property within the neural network. Additionally, they develop a framework for generating synthetic data containing various common and complementary information to facilitate a comprehensive comparison of Multiple View Representation Learning (MVRL) methods.

### Strengths
NR-DCCA consistently outperforms the baseline methods in both synthetic and real-world datasets. Moreover, the proposed noise regularization approach can be applied to other DCCA-based methods, such as DGCCA. This paper is well-structured and easy to follow.

### Weaknesses
Some key details are missing. See my comments below.

### Questions
However, the reviewer has several questions:

The proposed method involves adding a regularization term to the loss function. The choice of the optimal value for the hyperparameter α in Equation 6 is crucial. If α is set too large, the model may tend to behave like an identity mapping function, potentially reducing its effectiveness. Conversely, if α is too small, the model may not maintain a "full-rank" property. The authors should provide guidance or suggestions on how to select an appropriate α value.

The reviewer is interested in whether there is any theoretical analysis of the generalization ability of the proposed method. An exploration of how NR-DCCA's performance might extend to new, unseen data or domains would add depth to the paper.

The paper showcases the performance improvement of the proposed method in downstream tasks using off-the-shelf methods like Support Vector Regression (SVR). However, the reviewer is curious about whether there are any significant performance differences when fine-tuning the system using downstream tasks. An analysis of how NR-DCCA performs in this scenario would be informative.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deal with Multi-View Representation Learning and solves a problem which affects Deep Canonical Correlation Analysis (DCCA) approaches, which is the model collapse. Model Collapse occurs when the performance of DCCA-based methods drops with the advancements of the training epochs, and is due to the model correlation among neural networks. 
The authors make a comparison with simple CCA (not deep) approaches, and demonstrate that the main reason for CCA not having the model collapse issue is that the full-rank property holds in its transformation matrix, while the DNNs in DCCA do not possess such property. In particular, CCA searches for as a full-rank matrix, and it is robust to random noise, given the fact that the correlations before and after the (linear ) projection is kept
Therefore, the authors propose a noise regularization to enforce the DNNs to be “full-rank”, tailored for DCCA-based methods, dubbed NR-DCCA. NR-DCCA generates a set of i.i.d Gaussian white noise, with the same shape as the multi-view data Xk. Subsequently, DCCA is enforced to be full rank by adding a Noise regularized loss which requires that the correlation between the raw data and the noise is kept after having embedded the data into a latent space with the deep network, for each of the view.
Experiments on synthetic and real world datasets, against a set of SOTA approaches, show the validity of the simple idea of the authors

### Strengths
The problem is important, since DCCA-based MVRL methods without model collapse are hard to achieve.
A theoretical analysis of the model collapse issue in DCCA-based methods for MVRL is shown 
A novel noise regularization approach is proposed for DCCA
The full-rank property of the CCA method which prevents model collapse is demonstrated, this drives the noise regularization approach from a theoretical perspective.
Experiments demonstrate a good performance. The comparative approaches are appropriate. The resulst tel a clear story, and there are no question marks that arise.

### Weaknesses
I did not find any major lack. I was focusing on the theory, but it seems very clear (yet simple). I was looking for additional, more appealing comparative approaches doing DCCA, but I did not find any. One may argue why the approach has been casted solely for Multi-View Representation Learning, since it could have a broader scope, but this is not a minus. Just a curiosity. 
In general I think that the paper can be squeezed a little, in order to host some of the experiments of the additional material. In particular, I found fascinating the experiment reported in Fig.12, about the the correlation between unrelated data. This is a further proof of the goodness of the idea. I would also report the tsne visualization in the main paper.

### Questions
See my suggestions and curiosity above

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
