# Predicting masked tokens in stochastic locations improves masked image modeling

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
Masked Image Modeling (MIM) is a promising self-supervised learning approach that enables learning from unlabeled images. Despite its recent success, learning good representations through MIM remains challenging because it requires predicting the right semantic content in accurate locations. For example, given an incomplete picture of a dog, we can guess that there is a tail, but we cannot determine its exact location. In this work, we propose to incorporate location uncertainty to MIM by using stochastic positional embeddings (StoP). Specifically, we condition the model on stochastic masked token positions drawn from a gaussian distribution. We show that using StoP reduces overfitting to location features and guides the model toward learning features that are more robust to location uncertainties. Quantitatively, using StoP improves downstream MIM performance on a variety of downstream tasks. For example, linear probing on ImageNet using ViT-B is improved by $+1.7\%$, and by $2.5\%$ for ViT-H using 1\% of the data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes the Stochastic Positionalem beddings (StoP) to MIM in order to perturb the location information of images as a way of regularization. This avoids overfitting the model. The paper motivates and derives the empirical training loss of such perturbation that allows for end to end training by borrowing the well known reparametrization trick. Empirical evidence shows that the proposed method improves the existing SOTA method by evident margin.

### Strengths
The paper has several strengths including:

S1. It introduces Stochastic Positional Embeddings (StoP) for the purpose of adding perturbations to the location information of images within the MIM framework, thus serving as a means of regularization. This measure intuitively can prevent the model from overfitting. 

S2. By employing a reparametrization trick, the paper trivially both justifies and develops the empirical training loss associated with this form of perturbation, enabling end-to-end training. 

S3. Empirical results highlight that this proposed technique significantly enhances the state-of-the-art method, demonstrating a noticeable improvement.

### Weaknesses
However, there are also several concerning points that needs to be addressed:

W1: It is unclear to me why it is necessary to learn optimal $\Sigma$ via additional parameterization. What is the benefits of introducing additional degree of freedom here to learn Sigma? What if we fix Sigma without learning? Isn't it a simpler way to avoid degeneracy of matrix A?  Please explain the motivation. 

W2: I understand that adding stochastic perturbation to position of the images makes sense in regularizing the model. However, why the same spectral decomposition is applied to features s_x (by multiplying with A)? This step also lacks motivation and seems to be heuristic, please clarify on this point, 

W3: What exactly architecture did the paper use to parameterize the matrix $\Sigma$ ? An architecture flow illustration will help better illustrate this mechanism. Currently, I am not sure how the back-propagation of $\Sigma$ flows back to the network  (figure 1 does not have this part ) and how it affects the SSL learning with a positive gain. 

W4: I am not sure of the significance of proposition 1. I do not see why using this optimal predictor can help achieve better generalization ability of the SSL pretraining on downstream tasks.

### Questions
Please see above for the in total 4 questions to be addressed.

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
The paper proposes modeling a distribution over positional embeddings instead of learning/using deterministic ones which is compatible with any Masked Image Modeling (MIM) framework.

### Strengths
Authors propose smart modeling design choice to avoid collapsing model to just learn deterministic embeddings. Experimental evaluation shows consistent improvements compared to deterministic MIM (i.e. I-JEPA) for models of different sizes. Also, ablation study is great, authors ablate and deeply study different aspects of the model.

### Weaknesses
Honestly, I don't see any obvious weaknesses of the work.

### Questions
To strengthen the evaluation, it would be nice to see linear probes/finetuning results on the larger set of downstream datasets. Also, it could be nice to have a model pretrained on a larger dataset rather than Imagenet-1000 as it could lead to stronger model and will enable better transfer to downstream problems which is important to have such representations for the community.

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
This paper proposes stochastic positional embeddings (StoP) to improve masked image modeling (MIM), which incorporates location uncertainty by conditioning the model on stochastic masked token positions drawn from Gaussian distribution. Experimental results demonstrate that using StoP reduces overfitting to location features and guides the model toward learning features that are more robust to location uncertainty, which also leads to better performance on a variety of downstream tasks.

### Strengths
- The idea of stochastic positional embedding proposed here is novel to me
- Experiments are sufficient to support the proposed method, showing that the proposed method can achieve significant improvements on various downstream tasks

### Weaknesses
Several parts of the proposed method are not properly introduced and may cause some confusions, details can be found in Questions part

- I am a bit confused on step 11 in Algorithm 1. As in Figure 2, the context and masked representations are computed by adding their tokens and positional embeddings together. Then for step 11, I suppose $\psi_{B_x}$ should refer to the positional embedding, and $A s_x+b$ should refer to context token? Why do we need an additional linear transformation on $s_x$? Some explanations may be needed for this part. 
- Based on the above concern, I am also confused by later explanations in section 3.2 and 4.3, The authors seem to let $s_{x_i}$ (resp. $n_j$) as context (resp. masked) tokens, and $b$ (resp. $\tilde{m}$) corresponds to the bias for context (resp. masked) tokens. However, I suppose $n_j$ should simply be used to compute stochastic positional embedding as in (2), and $s_{x_i}$ is computed from encoder $f_\theta$ to encode context information. How can they have the same role? 
- Moreover, with the above correspondence, we should have $A s_x+b$ (resp. $An+\tilde{m}$) as context (resp.) tokens, then the positional embedding is simply $\psi_{B_x}$ (resp. $\psi_{B_y}$), and where is the stochasticity? I suppose there might be some misunderstanding. 
- I would also like to see more discussions on the connection between StoP and vanilla MIM. I suppose we can replace step 10 with $\tilde{m} + \psi_{B_y}$, and step 11 with $s_x+\psi_{B_x}$ to reduce to vanilla MIM, is it correct? Such discussions may make it easier to understand the proposed method. 
- While the authors have mentioned the necessity of regularization on A, the regularization with context token is a bit confusing. I note that the authors have conducted additional experiments in section 4.3 that uses L1 regularization on A. Nevertheless, L1 regularization should aim to obtain a sparse matrix A, which seems to contradict with the original aim to avoid zero A. The authors may consider using some other regularization (and also remove A in computing context tokens) and see how such modification works compared to Algorithm 1. The use of the same matrix $A$ for both the projection of the noise vector and the context tokens is also unclear. While it is argued that this prevents $A$ from going to zero, it's not obvious why this is the only way to achieve this. It seems that using a separate matrix $B$ for context projection, such as $m = An + \psi_{B_y} + \tilde{m}$ and $c = BAs_x + b + \psi_{B_x}$, would also achieve the same goal of preventing $A$ from going to zero, as $A=0$ would still result in $BAs_x=0$, and therefore a loss of context. Furthermore, the experiments on regularization are not entirely convincing. It is not clear if the matrix $A$ in StoP is actually regularized towards a sparse matrix. Given the observation that the norm of $A$ decreases with increasing $\sigma$, it would be more appropriate to try $\ell_2$ regularization, which directly regularizes the norm of matrix $A$, instead of $\ell_1$ regularization, to see if that leads to similar improvements.

### Questions
- I am a bit confused on step 11 in Algorithm 1. As in Figure 2, the context and masked representations are computed by adding their tokens and positional embeddings together. Then for step 11, I suppose $\psi_{B_x}$ should refer to the positional embedding, and $A s_x+b$ should refer to context token? Why do we need an additional linear transformation on $s_x$? Some explanations may be needed for this part. 
- Based on the above concern, I am also confused by later explanations in section 3.2 and 4.3, The authors seem to let $s_{x_i}$ (resp. $n_j$) as context (resp. masked) tokens, and $b$ (resp. $\tilde{m}$) corresponds to the bias for context (resp. masked) tokens. However, I suppose $n_j$ should simply be used to compute stochastic positional embedding as in (2), and $s_{x_i}$ is computed from encoder $f_\theta$ to encode context information. How can they have the same role? 
- Moreover, with the above correspondence, we should have $A s_x+b$ (resp. $An+\tilde{m}$) as context (resp.) tokens, then the positional embedding is simply $\psi_{B_x}$ (resp. $\psi_{B_y}$), and where is the stochasticity? I suppose there might be some misunderstanding. 
- I would also like to see more discussions on the connection between StoP and vanilla MIM. I suppose we can replace step 10 with $\tilde{m} + \psi_{B_y}$, and step 11 with $s_x+\psi_{B_x}$ to reduce to vanilla MIM, is it correct? Such discussions may make it easier to understand the proposed method. 
- While the authors have mentioned the necessity of regularization on A, the regularization with context token is a bit confusing. I note that the authors have conducted additional experiments in section 4.3 that uses L1 regularization on A. Nevertheless, L1 regularization should aim to obtain a sparse matrix A, which seems to contradict with the original aim to avoid zero A. The authors may consider using some other regularization (and also remove A in computing context tokens) and see how such modification works compared to Algorithm 1. 

Minor: the authors may also need to pay more attention on notations and typos. An example is on the top of page 5 “Context Encoding”, “Where” is wrongly capitalized (in fact the capitalization is used very arbitrarily and may require a careful proof-reading). Also, the notation through this paper is not consistent, especially for representations $c$ and $m$. Some revisions may be needed as well.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
