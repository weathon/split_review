# Concept Matching: Clustering-based Federated Continual Learning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Federated Continual Learning (FCL) has emerged as a promising paradigm that combines Federated Learning (FL) and Continual Learning (CL). To achieve good model accuracy, FCL needs to tackle catastrophic forgetting due to concept drift over time in CL, and to overcome the potential interference among clients in FL. We propose Concept Matching (CM), a clustering-based framework for FCL to address these challenges. The CM framework groups the client models into concept model clusters, and then builds different global models to capture different concepts in FL over time. In each round, the server sends the global concept models to the clients. To avoid catastrophic forgetting, each client selects the concept model best-matching the concept of the current data for further fine-tuning. To avoid interference among client models with different concepts, the server clusters the models representing the same concept, aggregates the model weights in each cluster, and updates the global concept model with the cluster model of the same concept. Since the server does not know the concepts captured by the aggregated cluster models, we propose a novel server concept matching algorithm that effectively updates a global concept model with a matching cluster model. The CM framework provides flexibility to use different clustering, aggregation, and concept matching algorithms. The evaluation demonstrates that CM outperforms state-of-the-art systems and scales well with the number of clients and the model size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to overcome the two issues of catastrophic forgetting and the potential interference among clients in Federated Continual Learning (FCL), the authors proposed a clustering-based framework, called Concept Matching. At each time step, the CM framework first assigns a concept model for each client as initialization in the fine-tuning process. Then the client models trained with local data, are clustered into some groups, which are used to update those concept models via the designed server concept matching approach in Algorithm 1. Finally, the updated concept models are for the next time step.

### Strengths
The proposed concept matching framework has used different clustering, aggregation, and concept matching algorithms, which can effectively improve performance compared with the state-of-the-art systems in Federated Continual Learning.

### Weaknesses
1. In terms of equations, many equations are not written clearly and normatively. Specifically, Eq.(2) is wrong where k* has missed n in Eq.(2), and the argmin operation of the loss function is not presented. Aggregate function in Eq.(4) is not expressed. \Theta and \omega are not unified in \Theta^t={\omega_1,\omega_2,...,\omega_J}.
2. In terms of the writing, this submission has not been written well. What is the meaning of the concept in the image experiment of this paper? This abstract vocabulary has not been explained clearly. More reasons for experiments should be analyzed. Many equations are not clear. In Algorithm 1, the \omega_j and \omega_k are repetitive in the inner and outer loop. 
3. In terms of experiments, the experiments are also insufficient. It is very important to discuss the number of concept models and clustered groups, as well as their relationship from the perspective of theory or experiment, which can help readers understand the importance of clustering for FCL. The authors are suggested to provide more analysis and reasons about all experiments, such as performance differences based on various distance functions, clustering methods, etc. 
4. The authors claim that two issues in Federated Continual Learning (FCL), catastrophic forgetting and interference among clients, can be greatly diminished. It will be better to prove that claim through conducting some experiments. 
5. The novelty is limited, as there are some Federated Learning (FL) works adopting the clustering method. however, the authors apply the clustering method to FCL at a single time step, which does not reflect the unique design of CL.

### Questions
Shown in the above Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a Concept Matching (CM) method for Federated Continual Learning (FCL). The main innovation of this article lies in maintaining global concept models for matching on the server . At training step, each client selectively updates the weights of its corresponding model. These updated weights are then clustered on the server side to differentiate between different tasks and reassign them to their respective matches. From a technical perspective, the approach presented in this paper is straightforward. Experimental results indicate that the proposed method outperforms the benchmark.

### Strengths
1. Federated Continual Learning is a genuine real-world problem that exists in practical scenarios.
2. The experimental results clearly demonstrate the effectiveness of the proposed method within the experimental setting provided by the authors.
3. The algorithm framework proposed in the paper is presented in a concise and easily understandable manner.

### Weaknesses
1.The problem background is unreasonable and does not align with practical needs. The requirement for each client to train with different datasets each time is not realistic in real-world scenarios. The assumption that each client will encounter completely distinct tasks in every training round is a strong and often unrealistic constraint. In most practical federated learning scenarios, clients will experience a mix of new and old data distributions, not a complete shift to a new task each time.

2.The method lacks innovation and can be seen as a mere patchwork of existing client aggregation approaches. The core idea of clustering client updates on the server and reassigning them to different models is reminiscent of existing techniques in personalized federated learning and meta-learning. The paper does not clearly articulate how the proposed concept matching mechanism significantly differs from these prior methods, or how it addresses the specific challenges of continual learning in a federated setting beyond what existing methods already accomplish.

3.The experimental comparisons lack persuasiveness as the baselines should be diverse in their configurations. The current baselines do not adequately cover the spectrum of possible approaches. For example, a comparison against a naive federated learning approach where all clients train on all data, even if not a continual learning setting, would provide a clearer understanding of the benefits of the proposed method. Additionally, the baselines should include methods that use different strategies for client aggregation and model updates, not just variations of the same basic approach.

### Questions
1.In the paper, there is a lack of explanation regarding the calculation of distlist[k] in line 9 of Algorithm 1. The author should provide further clarification on this point to enhance the understanding of the algorithm.

2.The model's implicit assumption that the number of concepts is smaller than the number of global concept models introduces a limitation. When there is a large number of concepts, it becomes evident that the algorithm's maintained models may encounter difficulties in effectively handling this situation. This limitation is a result of the algorithm's design.

3.The overall design of the model lacks novelty, as there are many similar methods available. The author simply transfers existing methods from other domains to the problem of federated continual learning without introducing any substantial innovation.

4.The experiments should be more comprehensive and diversified. It is recommended to include baselines that cover scenarios where all the data is combined or where all the data is separated. This will ensure a fair comparison and prevent experiments from being solely designed to favor the proposed method.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors investigate a continual learning setting in a federated learning framework. They propose concept matching as a method to avoid the catastrophic forgetting problem in continual learning under the assumptions of a federated framework, i.e., that only model weights can be shared between clients and server. The concept matching algorithm:
-starts by sending a set of K concept-specific models to each client
-the client evaluates each model and fine-tunes the locally best-performing model
-the locally fine-tuned models are sent back to the server
-the server clusters the models into J clusters within which models are aggregated 
-the server matches the J aggregated models with the initial K models to only update the matched ones
-the next round commences

### Strengths
The continual learning setting is relevant for many real-world applications. Investigating the interaction with restrictions from federated frameworks is valuable. 

The authors provide some limited theoretical intuition for their algorithm and empirical evidence that it works.

### Weaknesses
The algorithm requires each client to evaluate each model at every round. How does this impact run time? 

The experiments are based on a single "super" dataset which is of a relatively modest input scale. 

The experiments do not seem to have been run multiple times with different random seeds.

### Questions
What happens if some concept models never get updated? 

It would be helpful to have explicit definitions of concept and concept model in the introduction.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on federated continual learning (FCL) and proposes Concept Matching (CM), a clustering-based FCL framework. CM learns different global models for different concepts and designs server/client matching to identify target concept models for local optimization and global aggregation.

### Strengths
S1. The idea of learning a model set for clients to select in FL setting is novel.

S2. The introduction of two main challenges in FCL is clear.

### Weaknesses
W1. There are some more related works [1, 2] about clustered federated learning not included in this paper.

W2. The authors cite several related works about FCL but compare only one of them in experiments.

W3. This paper claims that CM can handle both class-incremental and task-incremental FCL but the experiments only include class-incremental setting.

### Questions
Q1. Are there experimental results on the datasets of FedWeIT under its setting?

Q2. How to select the correct concept model during inference/test as there are no data labels on the testset for Client Concept Matching?

Q3. Can we regard it as privacy risk to update and upload only selected concept models after local training?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
