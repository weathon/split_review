# Augmenting Negative Representation for Continual Self-Supervised Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
We introduce a novel and general loss function, called Augmented Negatives (AugNeg), for effective continual self-supervised learning (CSSL). We first argue that the conventional loss form of continual learning which consists of single task-specific loss (for plasticity) and a regularizer (for stability) may not be ideal for contrastive loss based CSSL that focus on representation learning. Our reasoning is that, in contrastive learning based methods, the task-specific loss would suffer from decreasing diversity of negative samples and the regularizer may hinder learning new distinctive representations. To that end, we propose AugNeg that consists of two losses with symmetric dependence on current and past models' negative representations. We argue our model can naturally find good trade-off between the plasticity and stability without any explicit hyperparameter tuning. 
Furthermore, we present that the idea of utilizing augmented negative representations can be applied to CSSL with non-contrastive learning by adding a regularization term.
We validate the effectiveness of our approach through extensive experiments, demonstrating that applying the AugNeg loss achieves superior performance compared to other state-of-the-art CSSL methods, in both contrastive and non-contrastive learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Augmented Negatives (AugNeg), a new approach for continual self-supervised learning (CSSL). It addresses limitations in the conventional loss function by incorporating two losses that balance plasticity and stability. The authors evaluate AugNeg's performance over existing methods in both contrastive and non-contrastive CSSL on CIFAR-100, ImageNet100, and DomainNet on Class-, Data-, and Domain-IL.

### Strengths
The author thoroughly re-examine the drawbacks of the existing algorithm (CaSSLe) and propose a novel loss function.

### Weaknesses
1. More experimental results are expected. CaSSLe performs experiments with all SSL methods mentioned in all CSSL settings. However, the authors only selected two SSL methods, though with exploratory experiments on CIFAR-100, to compare with the baselines. It is worth noting that different SSL methods may have different effects on different CSSL settings and datasets. The goal of various SSL methods is to demonstrate that the loss can universally improve CSSL, given any existing SSL methods and potentially future methods.
2. The presentation of the paper needs to be improved, as most of the captions of the tables and figures do not contain useful information.
3. The loss needs a more intuitive explanation. From the current presentation, it seems like the design lacks meaning and is more of an engineer labor. See the question below.

### Questions
While I can understand that additional embeddings $\mathcal{N}_{t-1}(i)$ are introduced to $\mathcal{L}_1$, I am curious about the effect of this operation in the representation space and the specific property that $\mathcal{L}_1$ aims to encourage. Are the current negative samples in $\mathcal{L}1$ (previous negative samples in $\mathcal{L}2$) so extensively utilized that the inclusion of the negative samples from another source is necessary? If this is indeed the case, could it be attributed to the scale of the dataset? The variable 

$z_{i,t} = Proj(h_{\theta_t}(x_i))$ 

in CaSSLe is designed for the invariant feature of the current and previous tasks. Does this apply to the proposed algorithms as well? In section 3.4, why does the addition of an extra regularization term follow a similar principle to that of the previous section?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work present the improvement to SSL loss function for continual self-supervised learning (CSSL) that consider outputs of the previous model while training for the current task. The proposed loss consists of two terms: plasticity and stability ones, without additional explicit tradeoff between two of them. Proposed method should result in a better plasticity in comparison to existing method, that focus on stability. Experimental section follows one from CaSSLe method [18]. Ablation study is provided.

### Strengths
1. Motivation why use negatives from the previous tasks is well motivated.
1. Proposed method presents some improvement.

### Weaknesses
The main weakness for me of this paper is seeing it for the second time without small changes. I've spent some of my time to help the authors to improve it the last time and they do not even find enough time to do the good text replacement from Sy-con to AugNeg.
Main changes: They've removed one unfavorable plot (CaSSLe was always better on it for two out of three methods) and add Table 2, changed Fig.4, added "SyCON (BYOL)" **(!) (authors own writting)**, and added why the cannot reproduce CaSSLe results (Challenges of reproducing CaSSLe’s results - I've checked the issue page as well, 2% changed at the end in #12).

1. Improvements presented in Table 1 (CSSL baselines) – taking into account the results variability is not always significant (see std. dev. reported there for AugNeg vs CaSSLe).

1. The results for CaSSLe are still lower from ones presented in the original paper. The pointed issue on the github is mainly about BYOL method.

1. For a good comparison in Fig.4 the right figure should be MoCo with just finetuning. We can then compare all three methods better and can be a good sanity check. Right now, what we can say is that AugNeg hurts the performance on the first task a bit (why?) and is better in the following. Do we have the same queue size and all hyper-params here between the methods? (see my questions).

1. There is no clear message why AugNeg works in each of the scenario with each method (MoCo / BYOL).

### Questions
1. Why do not adjust other hyper-parameters, when changing some crucial ones, e.g. batch-size for cassle?

1. Why AugNeg for Domain-IL is 43 (Tab.3) when SyCON for the same seting was 46?

1. Is the MoCo for FT and CaSSLe as well run with extended queue size (to 65K)?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this study, the authors introduce a novel method for continual self-supervised learning, termed "AugNeg". This approach generates an increased number of negative examples, utilizing the encoding derived from the previous model. Demonstrating versatility, the proposed method exhibits enhancements across three distinct settings. Furthermore, the authors integrate this method with non-contrastive learning methods, adapting it into a regularization term.

### Strengths
1. Continual self-supervised learning stands as a promising field of research, offering the substantial benefit of potentially reducing computational resource requirements.
2. The proposed method appears to be soundness. By generating a greater number of negative examples, particularly those derived from the previous model, it is anticipated that the quality of the representations will be enhanced.
3. The structure of this paper is commendably clear and logical, facilitating ease of understanding and follow-through for readers.

### Weaknesses
1. There is a significant discrepancy in performance between the proposed method and standard joint training. It raises the question of whether the proposed method offers any resource savings compared to conventional training approaches. Additionally, it's pertinent to question why a user would choose to sample exclusively from current task data instead of the entire dataset.

2. The primary goal of continual self-supervised learning (CSSL) is to conserve resources, for instance, by reducing the need for large mini-batch sizes. However, it's crucial to determine whether the proposed method maintains its efficacy in datasets with an extensive array of classes, such as ImageNet-1K.

3. Augmentation represents a crucial area of exploration in Self-supervised learning. Given that the authors classify their method as a form of augmentation, it becomes essential to engage in comparisons and discussions with existing augmentation methods [1][2][3].

### Questions
1. In Figure 2, z+,i,t-1 is regarded as an negative example. Is it a typo?  Additionally, with new negative examples, the gradient looks keeping nearly the same direction.

2. Equation 5 is still unclear and requires further elaboration. It looks offsetting to Equation 4.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
