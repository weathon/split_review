# Federated Learning under Label Shifts with Guarantees

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
We consider the problem of training a global model in a distributed setting and develop an unbiased estimate of the overall *true risk* minimizer of multiple clients under challenging inter-client and intra-client *label shifts* as a stepping stone to provably address distribution shifts in real world. We generalize the family of Maximum Likelihood Label Shift (MLLS) density estimation methods inspired by a board family of Integral Probability Metrics and introduce the Variational Regularized Label Shift (VRLS) family of density ratio estimation methods and show all MLLS methods are special cases of VRLS under specific latent spaces. Our theory shows high-probability estimation error bounds achieved through a versatile regularization term in VRLS. Our extensive numerical experiments demonstrate that VRLS establishes *a new SotA in density ratio estimation*  surpassing all baselines in MNIST, Fashion MNIST, CIFAR-10 datasets and *relaxed label shifts* as a proxy of real-world settings. In distributed settings, our importance-weighted empirical risk minimization with VRLS outperforms federated averaging and other baselines in imbalanced settings under drastic and challenging label shifts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript considers the problem of training a global model in a federated learning setting under challenging inter-client and intra-client label shifts. The authors propose a new method for density ratio estimation and establish a high probability estimation and convergence bounds. Experimental results on MNIST and CIFAR datasets show the effectiveness of the proposed methods.

### Strengths
1. The paper studied a relevant problem in federated learning: a special type of data heterogeneity with client label shift. 
2. The paper is generally well-written and easy to follow.

### Weaknesses
1. I am not sure of the relevance of the statistical results (Theorem 1) and optimization results (Theorem 2) in the context of federated learning (FL). In FL, there is only limited communication and this critical aspect is not categorized by these theorems. I am wondering how many communication rounds the algorithm requires to obtain a statistical and computational guarantee.

2. Experimental results are weak. Tacking data heterogeneity is a well-known problem in federated learning (e.g., FedProx [r1], SCAFFOLD [r2], minibatch SGD [r3], etc.). However, it seems that the authors only consider FedAvg and FedBN as baselines. I suggest the authors also compare against these papers, which were also proposed to learn a global model with client data heterogeneity.

[r1] Li, Tian, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, and Virginia Smith. "Federated optimization in heterogeneous networks." Proceedings of Machine learning and systems 2 (2020): 429-450.


[r2] Karimireddy, Sai Praneeth, Satyen Kale, Mehryar Mohri, Sashank Reddi, Sebastian Stich, and Ananda Theertha Suresh. "Scaffold: Stochastic controlled averaging for federated learning." In International conference on machine learning, pp. 5132-5143. PMLR, 2020.


[r3] Woodworth, Blake E., Kumar Kshitij Patel, and Nati Srebro. "Minibatch vs local sgd for heterogeneous distributed learning." Advances in Neural Information Processing Systems 33 (2020): 6281-6292.


3. The authors did not report the communication round result in the experiments section. It is unclear whether improves over FedAvg or  FedBN when there is only limited communication. There is still a huge gap between the IW-ERM and the upper-bound performance (Table 3).

### Questions
1. Can you elaborate on the communication round results theoretically and empirically?

2. Can you compare against more baselines for tackling data heterogeneity in federated learning?

I am happy to consider increasing the score if these concerns are addressed.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on addressing the label shift problems in both single-client and federated settings. To address the statistical heterogeneity in FL, the authors proposed an importance-weighting ERM method to address joint intra-client and inter-client label shifts. Moreover, the paper offers theoretical generalization guarantees for the proposed density ratio estimation, encompassing adjustments for label shifts across and within clients. Empirical evaluations using the CIFAR-10 and MNIST datasets, along with a series of ablation studies, corroborate the efficacy of the proposed method.

### Strengths
1. This paper pioneers the exploration of label shift challenges within federated learning, introducing a novel framework that distinguishes between inter-client and intra-client variations. This foundational work opens avenues for future scholarly inquiry in this underexplored but critically relevant domain.

2. By establishing a connection with existing label shift literature, such as BBSE and MLLS, the authors have advanced these theories by integrating a regularized objective function. This enhanced formulation not only addresses the label shift in latent space but also embeds regularization within the predictor training phase, allowing for an adaptive response to distribution shifts.

3. The paper excels in its delivery of a straightforward and comprehensible methodology, underpinned by a thorough theoretical analysis across various scenarios. Its clarity and depth offer great insights for practical applications.

### Weaknesses
1. While the authors have conducted experiments across a variety of settings, the scope of their datasets remains limited. To more convincingly demonstrate the robustness and practicality of the proposed method, it would be beneficial to extend these experiments to larger-scale datasets and real-world application scenarios. Specifically, the current evaluation lacks sufficient complexity to fully assess the method's performance under more challenging conditions, such as those with higher dimensionality, more classes, or greater levels of noise. The use of only CIFAR-10 and MNIST, while common, does not fully capture the nuances of real-world data distributions and label shifts.

2. For greater clarity and understanding, a detailed derivation of Equation (Reg-Est) within the main body of the paper would be advantageous. The current presentation of this equation lacks sufficient detail, making it difficult to fully grasp the underlying assumptions and mathematical steps involved. This lack of clarity hinders the reader's ability to critically evaluate the proposed method and potentially build upon it.

### Questions
Please see the comments in the Strengths and Weaknesses sections.

### Soundness
3 good

### Presentation
2 fair

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
This paper studies the label shift adaptation problem under the federated learning setting. There are two parts. For the first part, this paper proposes VRLS, a regularized version of the MLLS method. The authors further show that the optimization problem can be approximately solved by an EM procedure. The second part introduced how to apply the VRLS algorithm to the federated learning setting. Theoretical guarantees on the sample complexity of the density ratio label density ratio estimator and the convergence rate of the IW-ERM algorithm are provided. Extensive experiments are also conducted to evaluate the proposed methods.

### Strengths
The strengths of this paper as as follows:
- Interesting problem formulation: this paper studies the label shift problem under the Federated learning setting. The problem formulation is both interesting and practically relevant.
- Superior empirical performance: this paper proposes a regularized version of the MLLS method. Experiments show that the proposed method achieves superior empirical performance than MLLS method.

### Weaknesses
The weaknesses of the paper are as follows:
- Unclear main focus: While the paper is titled "Federated Learning under Label Shifts with Guarantees," I noticed that a significant portion appears to study the classical label shift problem in supervised learning. In particular, Section 3 only briefly touches upon applying the proposed density ratio estimation to federated learning, but it lacks a detailed algorithm description and a thorough discussion of its contributions. In Section 4, Theorem 1 and Theorem 2 seem to offer limited insight into how the proposed algorithm might effectively tackle the challenges of federated learning. Specifically, Theorem 1 seems to pertain only to a single client, and the presentation of Theorem 2 is somewhat confusing, as discussed in the next point.

- Clarity of Theorem 2: The statement of Theorem 2 strikes me as somewhat informal, particularly due to my uncertainty regarding the definition of the notation $\ell$. In Section 2, it is defined as the loss function on a single sample. In light of this, it's not unclear to me how the theorem relates to the objective Eq.(IW-ERM) that the authors are trying to minimize. Moreover, the proof of Theorem 2 seems to be a straightforward application of (Liu et al., 2023, Theorem 4.1). It's not clear how this theorem perspective helps to enhance our understanding of the federated learning problem.

- Unclear theoretical advantages: As indicated by Eq (3.1) and Eq. (3.2), the proposed method appears similar to MLLS with the difference that the model $\theta^*$, is trained with an additional regularization term. While the experiments demonstrate the benefit of this additional regularization, Theorem 3 shows a similar convergence rate for the proposed VRLS when compared to MLLS. I think the theorem will be more appealing if the authors can provide a more precise explanation of why the regularization helps with the label shift problem.

- Empirical comparison: a closely related work is [1] as cited by the authors, which also considers adding a regularization term to perform for the label density ratio estimation. I think the experiments will be more convincing by also taking [1] as a compared method.

### Questions
1. The connection between the optimization problem in Eq.(Reg-Est) and that shown by Eq.(3.1) and Eq.(3.2) is not immediately clear to me. In Eq.(Reg-Est), the regularization term is incorporated into the training of the density ratio, whereas in Eq.(3.1), it appears to be a part of the loss function to train the classifier $\theta^*$. It would be beneficial if the author could clarify this by providing a more formal statement that establishes the equivalence between these two optimization problems.

2. Could you provide a more comprehensive theoretical explanation of how the proposed help to minimize goal Eq.(IW_ERM) mentioned in Section 2?  (Please refer to the second point of weaknesses for more details.)

3. I think this paper would be more appealing if the authors could show the advantage of the proposed method over MLLS from a theoretical view. (Please refer to the third point of weaknesses for more details.)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
