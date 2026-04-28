# Multimodal Variational Disentangled  Knowledge Alignment for Cross-domain Recommendation

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Multimodal recommendation systems have been widely used in e-commerce and short video platforms. Due to the large differences in data volume and data distribution in different business scenarios, cross-domain recommendation is studied to improve the effect of target domain by using rich source domain data. Some studies use encoders to represent domain information and design knowledge alignment to achieve cross-domain knowledge transfer. However, simple information representation and alignment methods are easily affected by noisy information and lead to negative transfer problems. The distribution of features in different domains also has a large deviation, which affects the effective transfer of knowledge. Therefore, we propose a Variational Disentangled Cross-domain Knowledge Alignment Method (VDKA) for multimodal recommendation. Specifically, we propose a variational multimodal graph attention encoder, which consists of variational autoencoder and graph attention encoder. Variational encoder can learn domain sharing and domain specific representations under multimodal data utilization. Then we introduce variational optimization objectives and disentangled representation objectives to improve the accuracy of domain representation. Furthermore, in order to solve the problem of domain knowledge distribution drift, adversarial learning is designed to realize cross-domain knowledge alignment. We conducted comprehensive experiments on four real-world multimodal data sets, and the experimental results show that our proposed VDKA method outperforms other state-of-the-art models. Ablation experiments have verified the effectiveness of our various designs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a variational disentangled cross-domain knowledge alignment method(VDKA) for multimodal recommendation. Specifically,  a variational multimodal graph attention encoder learns domain-sharing and domain-specific representations, and adversarial learning is designed to realize cross-domain knowledge alignment. Experiments on multiple real-world datasets show VDKA  outperforms all baseline models selected by authors.

### Strengths
1. Concise language, easy to understand and read.
2. Cross-domain multimodal recommendation is a interesting and promising topic.
3. A novel and seemingly feasible solution is proposed and extensive experiments are conducted on two datasets.

### Weaknesses
1. The motivation is weak, and the problems to tackle in this paper are not clear. Since the method mostly focuses on cross-domain recommendation, why must the authors use multimodal data?  There is almost no contribution for multimodal design.
2. The paper simply lists related works. There is no discussion on the differences between this work and literature, making its position unclear.
3. The designed methods are widely adopted in general domain adaptation, with small technical contributions.
4. The experiments are only conducted on two small datasets, hard to show the generality of the method. Also, there is no mean and variance or significance test.
5. The method uses multimodal information and cross-domain information, but the baselines only use one of them, which may be also unfair. It should be clearly stated the adopted information.

### Questions
1.In the sensitivity analysis, the model performance has ups and downs instead of rising and then stopping or no obvious change as described in the paper. How to explain this phenomenon? In addition, when taking two extreme values (0.2 and 1.0), the performance difference on some datasets(such as lambda in book-domian) is very small. How to explain this?

### Soundness
2 fair

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
This paper introduces variational multimodal graph attention encoder and variational disentangled cross-domain knowledge alignment method (VDKA). The graph attention encoder extracts node representations for each modality and then fuses them. The basic objective is to predict positive interaction of users and items.  The VAE encodes these user representations into domain-specific and domain-shared latent representations. The paper proposes intra-domain and inter-domain information bottleneck regularizations methods to get disentangled representations. The paper also proposes the cross domain knowledge alignment method to solve the problem of native semantic space heterogeneity of the two shared latent representations.

### Strengths
1. The paper nicely applied many methods to solve the multimodal multi-domain recommendation task and achieved best performance.
2. The paper conducted ablation experiments to verify each proposed method.
3. The paper shows low distribution discrepancy of VDKA compared to the previous models.

### Weaknesses
1. Applying the graph attention networks, multi-modal fusion, VAE, and disentangled representation is not novel.  I found similar disentangled representation methods  in https://arxiv.org/abs/2012.04251 and DisenCDR.
2. The explanation of the knowledge alignment method is unclear.

### Questions
1. What is the "covariate drift hypothesis"?
2. What is the definition of the output of G_d(z)?
3. Why is there no item (v) in the input of G_y in equation (10) as far as I understand that G_y is the binary classifier of positive interaction between user and item?
4. How to optimize the three parameters in equation (9) exactly?
5. In equation (11), why only L_A has minus coefficient? It is awkward that L_A is loss function and we want to maximize it. I'm so confused about whether we want to maximize equation (10) or not.
6. Are \lambda in equation (10) and (11) is same?
7. Does equation (10) mean that we want to minimize the loss of domain classifier while maximizing L_y? Why do we maximize the L_y?

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a variational disentangled cross-domain knowledge alignment method for cross-domain recommendation. The domain-shared and domain-specific representations are learned through variational auto-encoders and adversarial training. Conducted experiments show the proposed method has better performance than compared baselines.

### Strengths
1. The paper is clearly written and easy to understand.
2. The proposed method sounds reasonable.
3. Experiments show clearly better results than baselines.

### Weaknesses
1. The motivation is weak, and the problems to tackle in this paper are not clear. Since the method mostly focuses on cross-domain recommendation, why must the authors use multimodal data?  There is almost no contribution for multimodal design.
2. The paper simply lists related works. There is no discussion on the differences between this work and literature, making its position unclear.
3. The designed methods are widely adopted in general domain adaptation, with small technical contributions.
4. The experiments are only conducted on two small datasets, hard to show the generality of the method. Also, there is no mean and variance or significance test.
5. The method uses multimodal information and cross-domain information, but the baselines only use one of them, which may be also unfair. It should be clearly stated the adopted information.

### Questions
Please see the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
