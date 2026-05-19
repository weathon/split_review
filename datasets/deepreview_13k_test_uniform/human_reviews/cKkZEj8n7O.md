# Generalization Error Minimized Deep Learning

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Despite the vast applications and rapid development of deep learning (DL), understanding and improving the generalization ability of deep neural networks (DNNs) remains a fundamental challenge. To tackle this challenge, in this paper, we first establish a novel bias-variance decomposition framework to analyze the generalization error of DNNs. Based on our new generalization error formula, we then present a new form of DL dubbed generalization error minimized (GEM) DL by jointly minimizing the conventional optimization target and an analytical proxy for the generalization error. Extensive experimental results show that in comparison with DNNs trained within the standard DL, GEM DNNs have smaller generalization errors and better generalization ability, thereby improving DNN prediction accuracy. Notably, GEM DL can increase prediction accuracy by as much as 13.19% on ImageNet in the presence of data distribution shift between training and testing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new algorithm of DNN training named generalization error minimized (GEM). It is motivated by theoretical analyses of reducing the generalization error. Targeting on minimizing a squared generalization error, the authors derive that the squared expected test loss and expected squared test loss are the two key components for reducing generalization error. GEM is designed based on this theoretical result. Experiments CIFAR-100 and ImageNet confirm the effectiveness of GEM against ERM and DOM. Additional experiments of test data shift, few-shot learning and imbalanced classification also show GEM surpasses ERM.

### Strengths
1. This paper proposes a new algorithm of DNN training derived from generalization error minimization. 
2. The algorithm is easy to implement and doesn’t require heavy computations. 
3. GEM shows clear benefits in small datasets.

### Weaknesses
1. The theoretical part is a bit tricky to me. Eventually the generalization error is reduced to be two loss terms only relying on test data as shown in Eq (15). Then the algorithm is implemented by simply replacing the test data with training data or processed training data. For the latter case, the difference between training and test data must be known in advance, which is not very realistic. Also, the theoretical result is based on the particular form of squared generalization error, which is different from the common definition of generalization error (training loss - test loss). The motivation of using the squared form of generalization error should be explained.
2. The optimal choices of beta and lambda are quite different for different datasets. This increases the complexity in applying the proposed loss in real applications. In the experiments, how did you decide the optimal choices?
3. For the evaluation of Case-2, how is ERM implemented? I think it’s not fair to compare GEM with a vanilla ERM trained on clean data if the test data shift is supposed to be known. Simply data augmentation (e.g., image compression or Gaussian Blur) should work better. 
4. For few-shot learning settings, transfer learning is a common technique to address the issue of data limitation. Training from scratch is far from state-of-the-art. It’s interesting to see whether GEM also improves the accuracy when a pre-trained model is utilized for few-shot learning.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework that integrates a 'novel' bias-variance decomposition of generalization error into the training objective for deep neural networks (DNNs). The proposed framework aims to improve the model's generalization by jointly optimizing the traditional ERM loss and a theoretically-inspired proxy for generalization error, yielding gains in accuracy  across various image classification scenarios.

### Strengths
1- The paper is extremely well-written and structured. 
2-  Generalization in deep learning is a very important problem. The proposed generalization decomposition is simple, yet sound and interesting.

### Weaknesses
W1- From a theoretical perspective, the generalization decomposition is quite straight-forward for me. So the main contribution here lies in leveraging the theoretical bound to propose a practical proxy of generalization. Regarding this proposed proxy, I have some concerns (See the question bellow) regarding the link between the theory and practice.

W2- The experiments focused only on image classification tasks with CNN-based structure with NLL loss. I would like to have seen a more diversified  experiments, e.g.,  transformer-based models. regression tasks, NLP, to better evaluate the utility of the proposed approach. 

I will reconsider my score if the authors can address my concerns in the questions section.

### Questions
**Theory**

In eq 11, the first two terms use the test data (True population). The third term is based on the training data and the forth uses both distribution. In the remaining part of the paper (after eq 11 Section 4.1), the authors argue that we can neglect the last two terms and keep only the first 2 (defined using the population data T ). However, in the experiment section, the proposed generalization proxy is based on the training data D and not on independent data). This poses several contradictions: 

Q-1: The proposed proxy does not minimize  $\text{Var}(\Omega(T, \hat{\theta}) | \hat{\theta}) + K^2(\hat{\theta})$. In fact, as it is based on the training data, what it really minimizes is $\text{Var}(\Omega(D, ) | \hat{\theta}) + KJ^2(\hat{\theta})$, which contradicts the argument made by the author (between eq11 and 13) that these two terms should be ignored. 

Q-2:  With the proposed proxy setup, T and $\hat{\theta}$ are no longer independent. In fact $\hat{\theta}$ is optimized using T. Hence, Eq 4 and onwards are no longer valid. 

Q-3: One potential way to solve this in my opinion is to define the proxy using an auxiliary validation set, i.e., in equation 19, the first term is defined using the training data while the second and third are computed using an independent validation data. 


**Experiments**

Q-4: Even that the link between the theory and the generalization proxy is not valid or weak (Q1-3 above), I think that the proposed regularizer can still be useful. However. the empirical validation in this paper is not enough to evaluate that. Have the authors tried their regularizer with other architectures beside CNN and NLL loss, e.g., transformer?

Q-5. Empirically, the authors compare only with DOM. However, several other theoretically-sound approaches have been proposed in the literature that can reduce overfitting, e.g., dropout [1-2], Mixup [3-4], feature diversity [5-7], etc. 


[1] Srivastava, Nitish, et al. "Dropout: a simple way to prevent neural networks from overfitting." The journal of machine learning research 15.1 (2014): 1929-1958. \
[2] Wan, Li, et al. "Regularization of neural networks using dropconnect." International conference on machine learning. PMLR, 2013.  \
[3] Zhang, Hongyi. "mixup: Beyond empirical risk minimization." arXiv preprint arXiv:1710.09412 (2017). \
[4] Zhang, Linjun, et al. "How does mixup help with robustness and generalization?."  Neurips (2020). \
[5] Laakom, Firas, et al. "WLD-reg: A data-dependent within-layer diversity regularizer." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 7. 2023. \
[6] Laakom, Firas, et al. "Learning distinct features helps, provably." ECML, 2023. 
[7] Cogswell, Michael, et al. "Reducing overfitting in deep networks by decorrelating representations." ICLR 2016

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces generalization error minimized (GEM) deep learning, a method that optimizes the standard minimization objective coupled with a “generalization” proxy target. The authors first decompose the conditional generalization error into three terms: Conditional testing variance, Conditional training variance and bias between the expected training and testing performance. The authors then discuss two cases: Case 1 when the training and test distribution are similar and Case 2 where the train and test distribution are dissimilar. In case 1, the GEM objective boils down to the linear combination of cross entropy (CE) loss, square of the CE loss and the second moment of the CE loss. Results with GEM in image classification task on CIFAR, ImageNet with ResNet, MobileNetV2 and other backbones shows that GEM performs better than ERM.

### Strengths
The authors show experimental results on a wide range of settings include few-shot setup, imbalanced learning in the context of image classification. The results on various datasets and settings show that GEM performs better than ERM in most of the scenarios.

### Weaknesses
1. I am not convinced the by the Case 2 argument. In most cases, the distribution (U, V) can not be obtained by processing (X, Y). For example, consider the case of subgroup shift (Waterbirds, Celeb-A) or OOD datasets (ImageNet-Sketch, ImageNet-R etc). 
2. The authors should also report performance on various OOD datasets atleast in the case of ImageNet (for e.g ImageNet-A, ImageNet-Sketch to name a few)
3. It would be great if the authors can also show a toy experiment with a synthetic data and how the solution learned by GEM and ERM differs

### Questions
1. Is label smoothing used in both ERM and GEM? If yes, what is the alpha value? The pseudocode in Appendix A.2 mentions label smoothing. 
2. In case of Case 2, the authors should compare against a method that computes CE loss w.r.t $\hat{X}$ and original CE loss and not the general ERM.
3. Could the authors provide the detailed hyperparameter and regularization configurations in each of the setups. In L524-529, the authors mention that many regularization techniques are already included in the baseline method. I could not find the relevant details anywhere in the paper.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new algorithm called generalization error minimized deep learning (GEM DL). The algorithm builds upon a bias-variance decomposition for the generalization error. The decomposition then inspires a new form of regularization term to be added to the objective function. The authors empirically show models trained using the new algorithm experience better generalization performance compared to the naive empirical risk minimization.

### Strengths
- The paper studies a very interesting topic to the research community.
- Overall, the type of experimentations that are done to evaluate the effectiveness of the proposed objective function are good. There are however issues within the experiments which I’ll detail in the weaknesses section.

### Weaknesses
- Overall, the paper is difficult to read. There are various vague expressions/statements throughout the paper. Starting from the abstract, what is meant by “a new form of deep learning”? Or in the introduction “training/testing performance”? This ambiguity makes it difficult to follow the authors' approach, especially when specific details are introduced before fundamental concepts are defined. Further contributing to the confusion, Section 3.1 refers to "average loss" as "performance", which contradicts the conventional understanding of these terms.
- The motivation for introducing new definitions of generalization error and conditional generalization error remains unclear. The authors should clarify why they deviate from established definitions used in theoretical and empirical research. A detailed comparison between their proposed definitions (Equations 2 and 3) and conventional ones is necessary, highlighting the differences and justifications for these changes. Also, the definition in Equation 2 is more the “generalization gap” rather than the “generalization error”.
- Ultimately, the proposed optimization method reduces to adding a regularization term to the training loss (or empirical risk minimization objective function).  Therefore, comparisons with benchmark regularization algorithms are crucial. However, the empirical results are limited in this regard, with only one benchmark included. Moreover, this chosen competitor exhibits lower performance than baseline ERM on the ImageNet dataset (Table 2), suggesting it may not be a suitable benchmark for state-of-the-art comparisons.  Furthermore, most of the experiments omit this competitor entirely, presenting only comparisons to ERM, which is insufficient. Even if considered a "plug-and-play" method, the proposed algorithm should be compared against other techniques that incorporate regularization terms into the objective function.
- The application of the proposed method in Case 2 relies on a questionable assumption: knowledge of the distribution shift that will occur in the test case. In practice, both the type and amount of shift are often unknown a priori, raising concerns about the method's practicality in out-of-distribution scenarios. This limitation is evident in Figure 1, where the applied GEMs are pre-designed for the specific type of distribution shift. Moreover, when the amount of shift is unknown and an incorrect hyperparameter is estimated (e.g., overestimating the blurring amount with sigma=3 in Figure 1.b), performance deteriorates significantly compared to baseline ERM. This experiment highlights the method's sensitivity to accurate estimations of the distribution shift.


More minor weaknesses/comments:
- The statement "since  ˆθ depends only on D and the training process, it follows that T and ˆθ are independent" is inaccurate. Model parameters depend not only on the training data itself but also on the underlying training data distribution, which may not be independent of the test data distribution. The authors need to clarify the distinction between the independence of random sampling used to collect training and test data, and the potential dependence between the underlying distributions from which these samples are drawn.
- The proposed method is adding two more hyper-parameters to the learning method, which would require additional hyper-parameter selection, making the method less practically appealing. 
- There are no standard deviation bars in any of the figures throughout the paper. This is particularly problematic in Figure 4 where there are lots of small variations.

### Questions
- In Section 3.1, the defined generalization error appears to be its out-of-distribution variant. The authors should clarify the rationale behind using this specific setting and explain why they refer to this generalization gap as a "new generalization error." What novelty does it introduce? Additionally, the presence of a squared term within the generalization error definition requires justification.

### Soundness
1

### Presentation
2

### Contribution
1
