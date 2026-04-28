# Fake It Till Make It: Federated Learning with Consensus-Oriented Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In federated learning (FL), data heterogeneity is one key bottleneck that causes model divergence and limits performance. Addressing this, existing methods often regard data heterogeneity as an inherent property and propose to mitigate its adverse effects by correcting models. In this paper, we seek to break this inherent property by generating data to complement the original dataset to fundamentally mitigate heterogeneity level. 
As a novel attempt from the perspective of data, we propose federated learning with consensus-oriented generation (\texttt{FedCOG}). \texttt{FedCOG} consists of two key components at the client side: complementary data generation, which generates data extracted from the shared global model to complement the original dataset, and knowledge-distillation-based model training, which distills knowledge from global model to local model based on the generated data to mitigate over-fitting the original heterogeneous dataset.
\texttt{FedCOG} has two critical advantages: 1) it can be a plug-and-play module to further improve the performance of most existing FL methods, and 2) it is naturally compatible with standard FL protocols such as Secure Aggregation since it makes no modification in communication process.
Extensive experiments on classical and real-world FL datasets show that \texttt{FedCOG} consistently outperforms state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on federated learning (FL) in the presence of data heterogeneity. Different from the existing methods which usually consider this data heterogeneity as an inherent property and attempt to mitigate the adverse effects, this paper proposes to handle the heterogeneity by generating new data, called FedCOG. There are two key components in FedCOG, including complementary data generation and knowledge-distillation-based model training. It can be plug-and-play, and naturally compatible with standard federated learning protocols.  Extensive experiments on classical and real-world datasets proved the effectiveness of the proposed method.

### Strengths
1. The proposed method is novel, handling the data heterogeneity from the perspective of the data generation, instead of correcting the model.
2. The proposed method can be a plug-and-play model, and it is naturally compatible with standard FL protocols.

### Weaknesses
1. The motivation for why we need to use data generation, instead of recent popular methods based on model correction, is somewhat not clear. When the training dataset is very large, the proposed method therefore needs to generate a large amount of data in order to achieve alignment, which is costly, then it seems like model correction is a better choice in such a scenario.  
2. As the paper mentioned, the proposed method FedCOG has two advantages, i.e., plug-and-play and compatibility with standard FL protocols, however, the unique advantages of this data generation method, compared to previous model correction methods, are still ambiguous. Could you please elaborate more regarding them?

### Questions
(see above)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed FedCOG, a Federated Learning (FL) algorithm that facilitates learning via augmented data generated from the global model, which is later used for knowledge distillation between the global and client models. This scheme is compatible with most existing FL algorithms. Its effects have been empirically verified on real-world datasets.

### Strengths
\+ This paper tackles a crucial challenge in FL which is Data heterogeneity. Their core idea of data correction for achieving global data consensus is well-motivated.

\+ Data generation by capturing the residual knowledge between the global and the client model is novel.

\+ Sensitivity analysis is well designed and conducted.

\+ This paper is clearly written. Related work is comprehensive.

### Weaknesses
 - Data generation on the client step brings extra computation workload compared with classic FL or FL with data generation on the server side.

- The method seems to be designed purely for vision tasks. Authors could discuss if the proposed method can be extended to scenarios with other input modalities, such as text inputs.

- This paper would further benefit from theoretical derivations to interpret why generated data on the client side helps in improving global model performance.

- Concerns on Experiments: All methods in Table 1 achieve notably lower accuracies than SOTA FL methods. I am concerned that the model arch, communication round, or optimizer setting is not well set up for appropriate comparison.

### Questions
\- Since tackling data heterogeneity is the key of this paper, I suggest authors conduct more experiments on data with Dirichlet distribution by varying the hyper-parameter $\beta$. More results with changing heterogeneities would further validate the effects of the proposed methods.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced a novel consensus scheme based on data generation to solve data heterogeneity problems in federated learning. It achieved a relatively higher accuracy on four public datasets with different degrees of heterogeneity. In the context of each individual client, the present study implemented a methodology wherein the global mode and local model which is extracted from the previous epoch were frozen. The objective was to train the generated data with the aim of optimizing the disparity between predictions made by the global model and those made by the local model, all the while mitigating any potential impact on the overall accuracy of the global model. All goals are evaluated on the generated dataset. Unlike current works focusing on the model, this paper provides a novel perspective from the local dataset. By enhancing the distribution of the local dataset, it claims to achieve better convergence. It achieved relatively higher accuracy on public datasets (FLAIR, Fashion-MNIST, CIFAR-10, and CIFAR-100) with different degrees of heterogeneity compared with federated learning (FL) algorithms like FedProx.

### Strengths
- The novel proposed method has a low overhead on each client, making it easy to apply in general FL tasks.
- Extensive experiments have been done to prove the advantages of the applied method.
- The paper is well organized and it's easy to follow.

### Weaknesses
 - As far as I know, an enormous amount of work has proved that in the vision task, introducing unbalanced label distribution will influence the performance of the global model, and according to the results of the experiments, it's possible that this empirical idea is true. For details, please refer to the detailed comment C1.
- Evaluation is not strong enough; For details, please refer to the detailed comment C1~C3.
- No analysis of convergence is provided. For details, please refer to the detailed comment C3.

Detailed comments:
- C1 In the experiment results, the final accuracy on CIFAR-10 is relatively low, please try some more complicated networks other than the 5-layer CNN. 
- C2 It's possible the network is not converged. To eliminate such a possibility, please provide a graph depicting the trend of convergence with the number of rounds on the server side. 
- C3 What's more, the proposed method only achieved a little improvement in accuracy, it's not sure whether it's caused by insufficient experiments, please repeat and provide mean and standard error for all results.
- C4 We kindly request further experimentations involving the generation of datasets of varying sizes, with corresponding meticulous documentation of the associated overhead. Furthermore, if feasible, we encourage experimentation on datasets comprising high-resolution images uniformly, to enhance the comprehensiveness of the analysis.
- C5 Please add proofs for the convergence analysis. If possible, please add a formal security analysis to your method.

### Questions
1. This paper introduced data distribution from other clients, will this cause privacy leakage, making it easier for the attacker to learn data information from the clients? 

2. Will generating new data for each client be identical to amplifying the global weight update direction collected in the last epoch?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed FedCOG, a synthetic data-assisted federated learning system, to mitigate the data heterogeneity in the training. The design mainly focused on the local training part. In the local training part, FedCOG first generates task-specific and client-specific data, and then uses knowledge distillation to train the local model. The experiment on computer vision benchmark datasets demonstrates that FedCOG performs well compared to existing FL baselines.

### Strengths
1. The proposed method is easy to follow. Different from other synthetic-data based methods, the FedCOG proposed task-specific and client-specific data for generation, which is novel and practical.

2. The paper is well-structured. The experiments include several existing FL baselines. The usage of the real-world FL multilabel dataset FLAIR is very rare in the FL literature.

### Weaknesses
1. I am confused about the data generation part of the reading. To my understanding, FedCOG took a learnable parameter for the data generator. What is the structure of the data generator? Does FedCOG update the weight of the data generator during the training as well? Could the author address more about how the data is generated locally?

2. In the experiment part, what are the sample numbers of the synthetic data in your setup? 

3. The client number is so limited for the experiment related to standard datasets.

4. I am concerned that none of the selected baselines is a synthetic data-based method. I see the paper cites FedGen in the related work section. Why does the author not compare with the recent synthetic data-based methods such as FedGen[1] and DynaFed[2]?

### Questions
1. How would the FedCOG be harmonized with FedProx? I am curious about how the FedCOG does the local proximal term in the KD-based model training?

2. In Table 4, why FedProx took longer local training time compared to the FedCOG?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
