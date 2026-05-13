# Accelerating Non-IID Federated Learning via Heterogeneity-Guided Client Sampling

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
Statistical heterogeneity of data present at client devices in a federated learning (FL) system renders the training of a global model in such systems difficult. Particularly challenging are the settings where due to communication resource constraints only a small fraction of clients can participate in any given round of FL. Recent approaches to training a global model in FL systems with non-IID data have focused on developing client selection methods that aim to sample clients with more informative updates of the model. However, existing client selection techniques either introduce significant computation overhead or perform well only in the scenarios where clients have data with similar heterogeneity profiles. In this paper, we propose HiCS-FL (Federated Learning via Hierarchical Clustered Sampling), a novel client selection method in which the server estimates statistical heterogeneity of a client's data using the client’s update of the network’s output layer and relies on this information to cluster and sample the clients. We analyze the ability of the proposed techniques to compare heterogeneity of different datasets, and characterize convergence of the training process that deploys the introduced client selection method. Extensive experimental results demonstrate that in non-IID settings HiCS-FL achieves faster convergence than state-of-the-art FL client selection schemes. Notably, HiCS-FL drastically reduces computation cost compared to existing selection schemes and is adaptable to different heterogeneity scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced a novel method of selecting clients in federated learning by clustering clients from their estimated data heterogeneity. Specifically, this paper found the relationship between the last layer's bias and the distribution of all labels in a given client's local data. By applying the Hierarchical Clustered Sampling technique, the server can compute this estimation for all clustered groups from a random sampling. By picking clients with the highest estimation, the server will aggregate clients with more balanced labels without knowing the exact distribution of the local data. This method achieved faster convergence and less overhead in extensive experiments compared with current works (FedProx) in this field on public datasets (FMNIST, CIFAR-10, and CIFAR-100).

### Strengths
++ This paper introduced a novel method to solve client selection problems

++ This paper provided a detailed convergence analysis

### Weaknesses
-- This paper didn't provide enough experiments to support this method. Please add experiments for more complicated networks, current test accuracy is too low to verify the efficiency of the algorithm. Specifically, the experiments are limited to relatively simple models and datasets (FMNIST, CIFAR-10, and CIFAR-100). The performance on these datasets, while showing improvement over baselines, is not sufficiently high to demonstrate the practical applicability of the proposed method in more complex scenarios. The paper should include experiments with deeper networks, such as ResNet architectures, and more challenging datasets to validate the scalability and robustness of the approach.

-- This paper didn't evaluate cases with client inaccessibility issues, though which were mentioned in the abstract. Please provide experiments when a given fraction of clients are unavailable and show the performance of your methods with other STOA methods. The abstract mentions the challenge of limited client participation, but the experiments assume all selected clients are always available. This is not realistic in many real-world federated learning deployments. The paper should include experiments where a certain percentage of selected clients fail to respond or are unavailable during a training round, and compare the performance of the proposed method with STOA methods under these conditions.

-- Writing issues: some part of this paper is a little confusing and there are some typos in certain figures. For example, in Figure 6, the y-axis label is too long, explain it in the caption of the figure.

### Questions
- My greatest concern is that this method may not be extended to cases other than SGD as mentioned in this paper. Even though there are proofs in the appendix, no experiments are provided to deomonstrate that. The appendix mentioned your method could be extended to the non-SGD optimizers. Please provide experiments to benchmark with STOA methods like FedCor with optimizers like Adam. The reason I recommended FedCor is that it doesn't need a loss from all clients and shows good performances in terms of convergence speed and final accuracy.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel client selection approach known as HiCS-FL (Federated Learning via Hierarchical Clustering Sampling). HiCS-FL utilizes client updates sent to the server's network output layer to estimate the statistical heterogeneity of client data. Using this information, it conducts clustering and client sampling. The paper provides an in-depth analysis of HiCS-FL's capability to assess the heterogeneity across various datasets and elucidates the convergence behavior during the deployment of this client selection method.

### Strengths
1. The paper addresses an important problem in the FL setting.

2. The proposed method outperforms some existing methods in the experiment section.

3. The paper is well-written and easy to understand.

### Weaknesses
1. The convergence analysis provided lacks depth and originality. It appears to closely resemble the analysis conducted in prior research on the conventional federated learning (FL) setting. Consequently, it does not offer any unique insights specific to the proposed method.

2. The proposed method needs to address privacy concerns.

3. The comparison methods employed in the study are both limited in scope and outdated. It is strongly recommended that the authors thoroughly explore recent and state-of-the-art methodologies to offer a more comprehensive and up-to-date evaluation of their proposed approach.

### Questions
Please see the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method for federated learning on non-iid data, with a particular focus on client sampling. The proposed method expands upon clustered sampling, making it hierarchical. Existing methods cluster clients into groups based on the similarity of their local updates, selecting one client per group to avoid redundant updates. However, the proposed method differs in several ways. Firstly, the server estimates the heterogeneity of each client's data based on the entropy of soft-max outputs. This estimation characterizes each client group based on average heterogeneity. In the proposed hierarchical scheme, client groups are initially sampled based on their average heterogeneity, with groups demonstrating higher heterogeneity having a greater chance of selection. Following this, clients are sampled from the selected groups based on client weights p_k (batch size). The paper also provides a convergence analysis. Experimental results on three image datasets (FMNIST, CIFAR-10, and CIFAR-100) validate the effectiveness of the proposed method.

### Strengths
**Originality**: The proposed client sampling scheme, which selects client groups based on data heterogeneity and then selects clients based on client weights, is new.

**Quality**: The quality of the proposed work is satisfactory overall, presenting some novel ideas that are quantitatively evaluated on multiple datasets. These ideas have proven to be more effective compared to some other state-of-the-art methods.

**Clarity**: The work's motivation is clear. Sophisticated client sampling is indeed necessary for FL with a large number of clients, where standard random sampling may not always be the optimal solution. The relationship to prior work, especially the clustered sampling strategy (Fraboni et al., 2021), is clearly stated.

**Significance**: The proposed method significantly improves training speed, ranging from 1.63x to 7.3x across multiple datasets.

### Weaknesses
 **Clarity**: The organization of Section 3 could be improved. It currently includes background ideas, existing approaches, and the proposed method, making it difficult to identify the novel aspects of this work. A possible solution could be to split it into two sections: "Preliminaries" and "Proposed Method".

**Applications to other tasks**: The proposed method has only been proven effective on image classification tasks (FMNIST, CIFAR-10, and CIFAR-100). It remains unclear whether the method can be extended to non-classification tasks (e.g., regression) or non-image tasks (e.g., NLP). The method's reliance on softmax outputs for heterogeneity estimation may not be directly transferable to tasks where such an output is not naturally produced. For example, in regression tasks, the output is typically a continuous value, and the concept of entropy of softmax probabilities does not apply.

**Comparisons with other state-of-the-art methods without client sampling**: The significance of the proposed method over existing client sampling-based approaches such as pow-d, CS, and DivFL is clear. However, the necessity for client sampling is not. There are numerous methods addressing non-iidness in FL, not just FedProx, but also Scaffold, Scaffnew, FedNova, FedOpt. The contribution of the proposed method would be clearer if it were compared against these non-sampling-based methods quantitatively in terms of training speeds and communication/computation overheads. Specifically, a comparison against methods that use gradient correction or adaptive optimization techniques would be highly informative, as these methods also aim to address the challenges of non-IID data in federated learning.

### Questions
Based on the weaknesses, I propose the following questions:

- Can the proposed method be evaluated on tasks other than image classification? For example, the Shakespeare (next work prediction) in the LEAF dataset (https://leaf.cmu.edu/) is a task commonly used in FL.
- Can the proposed method be compared with other non-sampling based approaches such as Scaffold, NedNova, or FedOpt that outperformed FedProx?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
