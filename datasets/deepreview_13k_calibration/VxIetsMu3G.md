# Understanding the Benefits of SimCLR Pre-Training in Two-Layer Convolutional Neural Networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
SimCLR is one of the most popular contrastive learning methods for vision tasks. It pre-trains deep neural networks based on a large amount of unlabeled data by teaching the model to distinguish between positive and negative pairs of augmented images. It is believed that SimCLR can pre-train a deep neural network to learn efficient representations that can lead to a better performance of future supervised fine-tuning. Despite its effectiveness, our theoretical understanding of the underlying mechanisms of SimCLR is still limited. In this paper, we theoretically introduce a case study of the SimCLR method. Specifically, we consider training a two-layer convolutional neural network (CNN) to learn a toy image data model. We show that, under certain conditions on the number of labeled data, SimCLR pre-training combined with supervised fine-tuning achieves almost optimal test loss. Notably, the label complexity for SimCLR pre-training is far less demanding compared to direct training on supervised data. Our analysis sheds light on the benefits of SimCLR in learning with fewer labels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a theoretical analysis of SimCLR pretraining, focusing on training a two-layer convolutional neural network to learn a signal-noise model, as explored in recent works like Cao et al., 2022. The authors derive conditions under which SimCLR pretraining and finetuning can achieve near-optimal test loss. Their findings indicate that SimCLR pretraining, followed by finetuning, can reach nearly optimal error rates with fewer labeled data than required for supervised learning.

### Strengths
- The theoretical results and proof techniques are novel. In particular, the connection between SimCLR and the matrix power method is especially interesting.

### Weaknesses
- Unlike other works focused on similar data distributions and network architectures, such as Cao et al., 2022, and Kou et al., 2023, the authors provide only a sufficient condition on the amount of unlabeled data, whereas previous studies offer tight necessary and sufficient conditions. I agree that providing only a sufficient amount of pretraining data effectively demonstrates SimCLR’s advantage over supervised learning. However, I believe that characterizing tight necessary and sufficient conditions would be valuable, as it may facilitate comparisons with other pretraining methods in future work.
- The data augmentation techniques introduced in the problem setting is too unrealistic. While I understand that defining data augmentation in an abstract manner within a signal-noise model is necessary, changing only the noise patch to new i.i.d. noise seems overly simplistic. This approach leads to augmented data from different pretraining samples with the same (unseen) label following the same distribution, which differs from practical scenarios. I believe a more practical definition for data augmentation could be used—such as applying a linear transformation to the noise patch.
- There are limited practical insights provided regarding the theoretical findings (see Question 1).

### Questions
- Could you provide some practical insights into the theoretical findings? Specifically, can the main proof technique—interpreting SimCLR as a matrix power method and characterizing top eigenvectors—be translated to real scenarios to offer intuition on why SimCLR is effective?
- Can the same proof technique be extended to ReLU networks and the 0-1 test loss considered in Kou et al.2023?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper extends a prior analysis of Cao et al. (2022) (regarding supervised learning) with a particular focus of SimCLR self-supervised learning. Specifically, it revisits a toy binary classification problem designed by Cao et al. (2022), and consider a SimCLR training using a bespoke 2-layer convolutional neural network. As the result, the paper theoretically show that fine-tuning a SimCLR pre-trained two-layer convolutional neural network requires significantly less label complexity compared to the supervised counterpart (of Cao et al. (2022)) to achieve low training/test losses, in a sense that the complexity is independent to the signal-to-noise ratio of the data at fine-tuning stage provided that it is sufficiently accounted at the pre-training stage. Although the main body of the paper is focused on theoretical results, some supporting experimental results are also provided, e.g., on synthetic data and MNIST, in Appendix.  

Cao et al., Benign overfitting in two-layer convolutional neural networks, NeurIPS 2022.

### Strengths
- The paper is well-motivated and clearly written.
- The paper presents solid theoretical results, which indeed provide insight about SimCLR.
- The area of study, i.e., theoretical understanding of recent contrastive learning methods, is still a timely topic in my opinion.
- Although not present in the main text, the paper also provides empirical supports as well.

### Weaknesses
 - To my knowledge, there have been several works that study contrastive learning in theoretical aspects, although I could not find a discussion about them from the paper: e.g., [Bansal et al., 2021; HaoChen et al., 2021; Tan et al., 2024]. I think the paper should incorporate any discussions about such a line of research. For example, I am curious whether the paper’s observation about SimCLR as a matrix power method can be related to the spectral view of contrastive learning [HaoChen et al., 2021].
- I generally feel a lack of discussion about how the theory presented in this paper can be related to the real-world use of SimCLR. I think this is because the paper omits enough context about how can we really ensure that the simplifying assumptions made here are mild enough, so that it can be eventually connected to the real-world. Specifically, the analysis relies on a simplified two-layer CNN architecture and a specific data model with a clear signal-to-noise ratio, which may not accurately reflect the complexities of real-world datasets and more complex architectures. The paper should address the limitations of these assumptions and discuss the potential impact on the practical applicability of the theoretical results.
- The main body of the paper is quite theory-biased, and allocates its significant portion with the proof sketch. This may narrow down the potential audience, and I personally think the authors might consider to give more highlight on their empirical results as well as the theoretical ones.

### Questions
- Is there any potential that the analysis presented in this paper can be generalized to more complex architecture?
- The overall setup assumes that the labeled data at fine-tuning stage is sampled from the same distribution where the pre-training data is sampled, considering a pure unsupervised learning scenario. But one important aspect of SimCLR like training is in its transferrability; as such, could the analysis can be generalized in any way if we relax the assumption of the labeled data to another distribution? For example, I am curious if the analysis could be extended when the labeled data is more noisy that the pre-training data.
- In my understanding, Theorem 4.3 implies that one still require the unlabeled sample size for SimCLR, $n_0$, at the similar rate of those for supervised learning to optimize the loss. But could this result be due to that the data considered is too easy to discriminate, even without labels, and perhaps the complexity of SimCLR can be much worse under a more challenging data assumption?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors present a theoretical analysis to establish the benefits of SimCLR pretraining for downstream finetuning of classification tasks. Their analysis is based on several assumptions, including isotropic Gaussian distributions of the representations, the signal-to-noise ratio (SNR) of the training and testing data as well as number of labeled data. Focusing on a two-layer convolutional neural network (CNN) setting, the authors provide detailed proofs and explanations to support their main argument: SimCLR pretraining provably guarantees convergence of the training loss and enhances test-time robustness.

### Strengths
The paper is clearly and coherently written, allowing readers to easily follow the presented ideas. Despite being based on several simplified assumptions, the analysis and proofs provided are detailed and reasonable, making the work theoretically sound in the setting of a two-layer CNN.

### Weaknesses
There are several weaknesses in the paper that require clarification from the authors:

1) The paper aims to understand how SSL methods like SimCLR benefit downstream fine-tuning. However, the literature review provided is insufficient to comprehensively cover this topic, which has been widely studied both theoretically and empirically. A more thorough literature review on SSL's impact on fine-tuning performance is necessary.
2) The problem setting of 2-layer CNN presented appears overly simplified, potentially deviating from the practical deep learning problems that commonly employ SSL methods such as SimCLR. While deriving theoretical guarantees for modern architectures like transformers is challenging, a more realistic framing of the problem would better justify its relevance and importance. Specifically, the analysis focuses on a very narrow setting of two-layer CNNs, which may not generalize to deeper networks or other architectures commonly used in SSL. The theoretical results are derived under strong assumptions, such as isotropic Gaussian distributions of the representations, which may not hold in practice. This limits the applicability of the theoretical findings to real-world scenarios.
3) The experiments in the appendix seem questionable in terms of their validity and relevance to the stated problem. Typically, SimCLR pretraining leverages large-scale unlabeled datasets. However, the experiments employ only 250 and 200 unlabeled data points for the synthetic data experiment and real data experiment, respectively. These small dataset sizes are atypical for SimCLR pretraining and may not represent the true behaviors of SimCLR pretraining combined with downstream fine-tuning tasks. Furthermore, the experimental setup lacks details on the specific hyperparameters used for SimCLR pretraining and fine-tuning, making it difficult to reproduce or validate the results. The choice of synthetic data also raises concerns about the generalizability of the findings to more complex, real-world datasets.

### Questions
1. How would the theorem transfer to more modern backbone architectures such as ViT? Can you provide more experiment ablation on more architectures?
2. Can you provide more ablation on the SNR rate and the number of the unlabeld data / labeled data?
3. What happens if the representation does not follow isotropic Gaussian distribution? Typically SimCLR type of loss results in non-isotropic representations, in that case, does the theorem still hold just by simply replacing the variance term in the SNR equation with the maximum variance across different embedding dimensions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This theoretical paper presents new contributions aimed at enhancing our understanding of how pre-training schemes improve fine-tuning performance. It introduces some theoretical results about SimCLR, one of the most popular contrastive learning methods for vision tasks. The paper demonstrates that, under specific conditions regarding the amount of labeled data, SimCLR pre-training coupled with supervised fine-tuning can achieve nearly optimal test loss. The main theoretical results are presented in Theorem 4.2 and 4.3. The paper and its appendix contain the proofs of these theorems. The paper also contains many novel analysis tools that enable the study of the SimCLR algorithm. The theoretical results are valid in a specific setting (simple binary classification task and a two-layers ConvNet), which is not a standard setting and may limit the potential impact of the contributions.

### Strengths
- This paper introduces new theoretical contributions to understand the advantage of SimCLR pre-training in fine-tuning stage. The paper demonstrates that, under specific conditions regarding the amount of labeled data, SimCLR pre-training coupled with supervised fine-tuning can achieve nearly optimal test loss for two-layers ConvNets. Under certain conditions related to the quantity of labeled and unlabeled data, as well as the signal-to-noise ratio (SNR), the convergence of training loss and a low test loss are assured. These theoretical results indicate that SimCLR pre-training during the fine-tuning stage can reduce label complexity, leading to a lower test loss.
- The paper and its appendix contain the proofs of the theorems 4.2 and 4.3, which are the main results of this paper.
- The paper contains many novel analysis tools that enable the study of the SimCLR algorithm. 
- The appendix contains some experiments on synthetic and MNIST datasets to confirm the theoretical results.

### Weaknesses
 **Impact of the contributions.** The paper studied a very specific setting: simple binary classification task and a two-layers ConvNet with $RELU^q$ output activation. In practice, this setting is not used often. For instance, SimCLR paper uses a ResNet-50 and was used on multiple multiclass classification benchmarks. There is a big gap between the theoretical setting used in this paper and the practical setting, so it is difficult to understand the potential impact of this paper contributions. It may be difficult to do, but it would be interesting to relax some of the assumptions to be able to get theoretical for a family of models which include ResNet-50.


**Lack of justification/motivation.** The paper has many assumptions that are not well motivated, or claims that are not well justified. Here are a few examples:
- L162: "this data model is particularly suitable to study SimCLR, which is originally proposed for vision tasks." This claim appears to lack sufficient justification. It may be beneficial to include an analysis to support this claim.
- L153: The patches are represented as vector rather than matrix in Definition 3.1. It seems to ignore the 2d nature of the patches. It could be valuable to justify this choice.
- L215: The paper focuses on two-layers ConvNet with $ReLU^q$ activation function with q > 2. This type of activation is not the most popular choice so it could be interesting to explain this choice.
- The assumptions regarding data augmentation for pre-training are not clearly stated.
- Definition 3.1 does not explain the assumptions on $\mu$


**Clarity.** The presentation and clarity of the paper could be enhanced. The paper includes a considerable number of notations, which can make it challenging to keep track of them all. Some notations appear to be undefined, while others are introduced later in the text, making it difficult to fully understand them until the subsequent paragraphs are read. Here are a few examples:
- $\Omega$ symbol is used L84, but it is defined at L106
- $W$ is used at L171 but it does not seem to be defined.
- $w_r$ is used at L172 but it is defined at L196
- $[F(W, x)]_r$ is used at L172 but it does not seem to be defined.
- $[n_0]$ is used L184 but it does not seem to be defined.
- L200: some variables like the unlabeled dataset are used to compute the loss, but they are not shown as input: $L(W, S_{unlabeled})$
- L158: The third bullet point in Definition 3.1 is not clear. It looks like a something is missing.


**Things to improve the paper that did not impact the score:**
- A lot of equations do not have number so it is difficult to reference them in the review.

### Questions
The questions are arranged in order of importance, with the first question being the most important.

- The paper should discuss the scope of the contributions, as the theoretical setting seems quite different from the practical setting. In particular, is it possible to remove or relax some assumptions to include a larger family of models? 
- L279: "we remark that most of these assumptions are non-essential." It seems to be counter-intuitive to make some assumptions that are non-essential. How do the theoretical results change if these non-essential assumptions are removed? 
- What are the assumptions about the data augmentation? 
- Why does the paper focus $ReLU^q$ activation function for the theoretical analysis? Is it possible to include other activation functions? 
- What are the assumptions about $\mu$? Can $\mu$ be the zero/null vector?

### Soundness
3

### Presentation
2

### Contribution
3
