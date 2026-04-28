# Efficient Transfer Learning from Arbitrary Pre-Trained Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Transfer learning typically involves loading pre-trained weights as an initialization, followed by fine-tuning on a downstream task. As pre-trained models become ever larger, this procedure is becoming prohibitively expensive, as we are forced to re-use the pre-trained architecture for fine-tuning. This procedure also precludes combining multiple pre-trained models that learn complementary information. Moreover, alternatives such as knowledge distillation do not reflect that we wish to transfer aspects of the pre-trained representation that are most relevant to the downstream task. To address these challenges, we introduce Adaptive Feature Transfer (AFT). Instead of transferring weights, AFT operates purely on features, thereby decoupling the choice of the pre-trained model from the possibly smaller downstream model. AFT (1) enables transfer from multiple pre-trained models, even over multiple modalities, with minimal training overhead and no inference overhead; (2) selectively transfers the information in the pre-trained features most relevant for the downstream task, through a prior that favors low mutual information between the downstream inputs and features given the pre-trained features; (3) performs feature transfer in an efficient kernel formulation that prioritizes the most relevant degrees of freedom. Empirically, AFT delivers a substantial boost in performance across diverse vision, language, and multi-modal datasets, relative to both standard transfer learning and knowledge distillation with the downstream model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Adaptive Feature Transfer (AFT) to extract information from the (multiple) pre-trained model to the downstream model by minimizing the mutual information between pre-trained and downstream features. The paper at the end uses a stronger regularized loss by only minimizing the feature distance in the downstream and pre-trained space to make the training more robust. The results show that AFT outperforms KD on vision and language tasks and architectures.

### Strengths
1. The paper observes that the stronger regularization (using kernels) on the regularization term can further improve the results. 

2. The proposed approach outperforms KD on various tasks and architectures.

### Weaknesses
1. I do not fully understand what is the main difference between AFT with $\rho$ and KD, namely, the equation (7) and (8). Is the main difference that in equation (7) you downsample the pre-trained features and in equation (8) you upsample the downstream features? If yes, is there mathematical proof (or visualization, other experiments, etc) that this difference really makes the model learn the essential information of downstream tasks and discard useless information?

2. Some parts of Section 3.2 are unclear.

(1) There is a missing $\prime$ in the first kernel definition, the definition of applying the kernel function to vector is undefined in equation (9), $X$ and $X^{\prime}$ should be the same according to Algorithm 1 but not mentioned in the text.

(2) Why the $\rho$ in Section 3.2 does not downsample the feature to the shape of the downstream features ($d_{\phi}$)?

(3) How to optimize U to make sure it is orthogonal?

(4) In Algorithm 1, the definition of $\hat{L}(\theta)$ is missing and $\hat{Y}_{batch}$ is not used.

3. The evaluation is conducted only on small subsets of benchmarks. Using more datasets and reporting the average results would make the results more convincing (like datasets used in few-shot experiments in CLIP, GLUE, SuperGLUE, Winogrande, etc).

### Questions
Why choose Eq (7) as the starting point to develop AFT rather than equation (8), as in Figure 4, the results of AFT w/o kernel (optimizing Eq 7 only) are not better than STL (maybe KD either).

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Adaptive Feature Transfer (AFT), a downstream adaptation technique that operates directly on features, thereby decoupling the choice of the pre-trained model architecture from the downstream one. AFT enables combining different pre-trained architectures together during adaptation while distilling only the relevant information for the downstream task to the final model. The algorithm is validated across a diverse set of vision, language and vision-language tasks and compared against knowledge distillation and transfer learning algorithms.

### Strengths
1. The proposed method allows to distill features learned with different architectures on possibly different modalities to any given architecture 
2. The method is validated on both vision, language and vision-language tasks

### Weaknesses
1. The proposed method promises to distill features from **any** set of models to a given model once the downstream task is know. The paper is positioned as a generic method that could be applied to any set of models (possibly containing architectures different to the downstream one). However, while the presented theory to justify the method is sound and generic, the empirical results do not seem to support the claim. For example, in Figure 1 (right) and Figure 2 (b) adding convolutional features to a ViT based downstream model seem to reduce the performance of the model. Why is it the case? To me it seems to suggest that the proposed method is not strong enough to reject some features that will lead to a worse downstream model.
    - If this is the case the current algorithm should be coupled with model selection techniques to pick the best features that are more likely to help (see [1] and reference therein). Can the authors comment on this more?
2. The previous limitation gets even worse when the set of conditioning models gets larger since the signal to noise ratio drops, making extracting the relevant information for the downstream task even harder. I suggest the authors to consider comparing with explicit sparsity inducing methods as the ones proposed in [2] and the references therein.
3. The final algorithm is optimizing theta and rho jointly. However, one would expect \rho being optimized more often than \theta. Typically, this is done with bi-level optimization techniques or simple rewriting \rho in closed form for each given \theta. Did the authors try those more natural alternatives? If \rho is not optimized fast enough the most likely trajectory induced by SGD will be around a stationary point of \rho which leads to a maximally insensitive/uninformative \rho which will be reasonably good on average for many possible \theta, however not optimal for any in particular.

### Questions
1. Why should invariance under orthogonal transformation be of help in the practical optimization optimization objective? Can the authors prove how the optimization landscape will change and get easier to optimize? As of now, this intuitive fact, is left to the ablation studies and only supported by empirical observations.
2. Why not using a different kernel than the linear one? This will make the optimization space much smoother (e.g. by choosing a Gaussian kernel).
3. Visual evaluation on CIFAR100 is quite limited, to increase the impact of the paper on the community I suggest the authors to extend the evaluation to other datasets as the ones used in [1]. 

Minor:
- Some typos and grammatical errors are present in the paper, please proofread the manuscript.
- Can you report in the paper the level of sparsity of the rho projection map? This could help the reader understanding what happens when irrelevant pre-trained models are added to the mix.  
- Make the scatter plots with learn probe accuracy vs test accuracy on the same scale. Is the proposed method worse than directly using a linear classifier on the concatenated features?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Adaptive Feature Transfer (AFT) to transfer from an arbitrary set of pre-trained models into a single downstream model. When fine-tuning the downstream model, AFT introduces an informative prior favoring low mutual information between the downstream inputs and features given the pre-trained features. It then efficiently optimizes it by exploiting a kernel formulation of the objective. This paper conducts experiments on multiple vision, language, and multi-modal datasets, and AFT outperforms standard transfer learning and knowledge distillation methods.

### Strengths
1 This paper explores an interesting problem of efficient transfer learning from arbitrary pre-trained models. 
 
2 The proposed AFT method is efficient and easy to implement. It is evaluated on multiple datasets on various tasks, including vision, language, and multi-modal, and outperforms standard fine-tuning and knowledge distillation methods.
 
3 This paper is clearly written and presented, and the proposed method is easy to follow.

### Weaknesses
1 Compared with the knowledge distillation mentioned in this paper (KD), the authors emphasize the contribution that KD transforms the downstream (student) features, while the proposed AFT transforms the pre-trained (teacher) features. However, in the general feature-based knowledge distillation framework [1], both teacher and student features can be transformed before minimizing their distances. This makes the proposed method a simple variant in the feature-based knowledge distillation framework and thus lack novelty.  

2 Some related works are missing in this paper, including those improving standard transfer learning and those considering transfer learning from multiple pre-trained models. For example, [2] also proposes to match pre-trained features and downstream features during transfer learning. [3] and [4] also consider transfer learning from multiple pre-trained models and propose to use features or knowledge distillation from pre-trained models. More related works in these two topics should be discussed in the paper. In experiments, some of these more advanced transfer learning methods should be compared, instead of only comparing AFT with standard transfer learning or knowledge distillation.

3 Some issues in the experiments. 

(1) It seems that in this paper, the pre-trained models are stronger than downstream models. Figures 2(c) and 3(c) also show that transfer learning by directly using pre-trained models leads to better results than AFT. This makes the problem setting in the experiments less convincing, especially considering that the linear probe from pre-trained models is also efficient.
 
(2) It is good to see experiments from vision, language, and multi-modal tasks, but in each task, only a few datasets are evaluated, and most of them seem to be easy.
 
(3) Transfer learning from multiple models is interesting, but currently, the number of models in the experiments is still small, and the improvements by using more pre-trained models are not clear from the results.

### Questions
1 What are the exact results before normalization in Figure 2(b)?

2 Could the kernel method in Section 3.2 still improve the performance if the downstream datasets have more training data? It would be better to have more experiments on more datasets or situations to validate the efficacy of such a design.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The motivation that inspired the work is important:  the pre-trained models are highly complex and difficult to fine-tune. However when you must train a model on a downstream task it could be that all the features that were learned on the source task are not necessary. So, if one had a way to select which features are relevant, then one could reduce the number of features needed to solve the downstream task and thus deploy smaller models. To address this task, they propose to  impose an L2 regularization which forces to find the most relevant features for the downstream task among all the features of the pre-trained models.

### Strengths
The idea of using the features learned in different models on the same data points and merge them together to represent the input is nice and, to the best of my knowledge, novel. It also makes sense performing an automatic feature selection in that space, in order to select the feature combination which is more informative. The experimental result presented in support of the idea are partially convincing.

### Weaknesses
I understand the attempt of providing a justification of the regularization loss using information theoretical bonds, but the way the authors arrive to the final form of the regularization they use, which is just a kernel version of the L2, eq. 9, is in my opinion unnecessarily involved and might create confusion. I suggest moving the text from eq 2 to eq 9 to the appendix.


MAJOR:  It is  not very clear why this form of R should help avoiding redundancy: the sigmoid function can set to zero irrelevant features, but if several features are simultaneously relevant (but correlated), I expect the solution  will not be sparse, but it will contain weights contributions from all. I suspect that this might lead to overfitting in data-scarce scenarios (see below).  

Given the topic of the article I would have expected a comparison with LORA (https://arxiv.org/abs/2106.), where the features for the downstream task are selected by multiplying the original features by a low rank matrix before downstream fine tuning.



### Questions
Since the focus of the paper is transfer learning, which typically happens towards data-scarce tasks, I would have liked to see if the procedure is robust with respect to aggressive decimation of the target task. What happens if one attempts to use ~100 examples for category, as typical in clinical image analysis applications?

The last paragraph of page 4 is not very clear. The variational parameters are the components of the vector s, which, via the sigmoidal function, set the weight of the corresponding psi component in the rhoPsi kernel?

Minor: when they present the setting on page 3, the labels seem to be linear regression labels, while the experiments are on classification datasets. Please clarify.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
