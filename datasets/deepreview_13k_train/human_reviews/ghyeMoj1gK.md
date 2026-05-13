# Client-centric Federated Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Conventional federated learning (FL) frameworks follow a server-centric model where the server determines session initiation and client participation. We introduce Client-Centric Federated Learning (CCFL), a novel client-centric FL framework that puts clients as the driving role of FL sessions. In CCFL, each client independently and asynchronously updates its model by uploading a locally trained model to the server and receiving a customized model tailored to its local task.  The server maintains a repository of cluster models, iteratively refining them using received client models. Our framework accommodates complex dynamics in clients' data distributions, characterized by time-varying mixtures of cluster distributions, enabling rapid adaptation to new tasks with high performance. We propose novel strategies for accurate server estimation of clients' data distributions. CCFL offers clients complete autonomy for model updates, enhances model accuracy, and significantly reduces client computation, communication, and waiting time. We provide a theoretical analysis of CCFL's convergence. Extensive experiments across various datasets and system settings highlight CCFL's substantial advantages in model performance and computation efficiency over baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new framework in FL where clients determine asynchronous when to update a local trained model to a server. The framework focuses on clustered FL and local distribution shifts in the clients and effects of staleness. Results are presented in comparison ton an Async-FL algorithm on FashionMNIST, CIFAR-100, MiniImagenet

### Strengths
- The idea to have clients control the update process is interesting and novel 
- The solution is sensible and the results are promising

### Weaknesses
 - The technical contributions can be difficult to follow, although the paper seems to suggest their main contribution is to have a client centric update process a lot of the focus is on clustered FL and client level distribution shifts making the exact setting and problem a bit contrived. It would be good to isolate these factors better both in the motivation of the method and in the experiments. Specifically, the paper does not clearly articulate why a client-centric update process necessitates a clustered FL approach. The motivation for using a mixture of distributions that change over time is not well-established, and it's unclear how this relates to real-world scenarios. The experimental setup also conflates these factors, making it difficult to assess the individual impact of each component.
- How does client level distribution shift relate to the area of continual federated learning
- It is difficult to asses if the compared baseline is the most appropriate, the baseline methods should be better motivated. The choice of `FedSoft-Async` as a baseline is not sufficiently justified. It's unclear why this particular adaptation of a synchronous method is the most relevant comparison for an asynchronous, client-driven approach. A more detailed explanation of the baseline's limitations in this specific context is needed.
- There are a lot of hyperparameters, how would these be decided in practice

### Questions
How would this framework perform in a setting without clusters or assumptions of local distribution shifts

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
The paper presents a client-centric framework for federated learning, where a client can decide when to participate in the collaboration and  where the result of an update is a model tailored to the local task. To accomplish this, the server maintains several cluster models, estimates a client's distribution based on available public data, and returns a personalized model based on this distribution. Results are demonstrated on three standard machine learning tasks.

### Strengths
- The philosophical motivation presented by the manuscript is quite compelling: a client-centric federated framework. 
- Handling local client distributions that change over time is an important practical scenario. 
- The paper is overall well written and well presented.

### Weaknesses
 - Although the paper provides a convergence result in Section 4.3, there is no discussion about it. Does this result elucidate anything about the behavior of the algorithm under the given assumptions? I admit I did not check the math carefully. 
- The presented experiments don't account for variance across repetitions. None of the plots have error bars, and the error bars in Table 1 represent variance across clients in one single repetition. This would make the results more robust, particularly when the results are close (e.g., in Table 1, when the number of clusters is 4). 
- There is no discussion on how to choose the number of clusters or where the public cluster data would come from.

### Questions
- I enjoy the client-centric philosophy presented by the paper, but I am not sure if the method truly adheres to this philosophy. I understand this client-centrism is exemplified by the asynchronous nature of the framework, giving clients autonomy over when to send updates to the server. Similarly, the philosophy is reflected by the fact that the updates result in a personalized model for the clients. However, I struggle to reconcile the idea of a client-centric framework with the fact that the server is still a key element and bottleneck in this algorithm. In fact, the paper recognizes that more tasks have been placed on the server compared to previous work (e.g., distribution estimation). This is the main reason for my rating, as I believe the manuscript should either be more careful in addressing this tension, or be more specific in their title/motivation. 
- In the first paragraph of Section 4.2, there is a reference to "aggregation of global models". I assume this refers to the cluster models? This particular term was confusing when I first read the manuscript.
- When explaining the experimental set-up in Section 5.1, there is no detailed description of how the clients' data changes over time. If this is in the appendix, please include a reference. 
- Just to clarify: in Figure 4(a), you know the true distribution of the clients because you track how their data changes through time?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a client-centric FL framework, where the clients have more autonomy.

### Strengths
- The paper is largely well-written (except some math, see below)
- The main sections 4.1 and 4.2 are well-explained, especially the use of Fig 2 helps.
- The experiment section is comprehensive.

### Weaknesses
Minor Issues
- $t_k$ should be defined the first time it is used in "Distributed Estimation" rather than later in "Clusters Updating''
- In Algo 2: Server Update subroutine, should the first condition be $t-\tau > \tau_0$ instead? Client Thread: where is local timestamp $t_m$ updated before sending to the server?
- For the weights $u_{mk}^t$ to sum to 1 in Algo 1, we need $c_1, c_2$ to satisfy $c_1 \sum_i \ell_i + c_2 \sum_i d_{1i} + (1-c_1-c_2) \sum_i d_{2i} = K$. Is it necessarily true that such $c_1,c_2$ will exist?

I have some doubts about the convergence analysis and experiments, see below.

Conclusion:
- What does "fluid dynamics" mean? And fluid dynamics is a completely different field in itself, so I would suggest rephrasing.

My main concern with the work is its practical relevance. The authors claim to put clients at the forefront. But, if the server estimates the distribution of the clients, this is a violation of the client data privacy? How can this be reconciled since privacy is one of the privacy motivations for doing FL in the first place?

Section 1
- Among the 3 properties to encourage client participation, autonomy is well taken. But, lightweight is doubtful - the same comm/computation is needed in FedAvg. Regarding performance enhancement, one could argue that personalized FL can help with that. Please comment.

Section 4.3: several questions about the math here
- Assum. 1: What is $F$? Do you mean $F_k$ for all $k$?
- Assum. 3: what is $f_m^t$? Do you mean the first term in $h_m^t$ in (2)?
- Assum. 4: How can $w_k^*$ be unique if $F_k$ is just assumed smooth (assuming Assum. 1 is about $F_k$)? For that, we need, e.g., strong convexity. But, in Assumption 3, $f_m^t, h_m^t$, both of which depend on loss $l(\cdot)$ have bounded gradients. This is confusing.
- Theorem 1: the authors have not commented on the result. Why is the constant $\epsilon$ needed? Why does the convergence for any $k$ depend on $\sum_i a_i$? Most importantly, can you show explicitly for what choice of the learning rate $\gamma$ can we get convergence, and how do $S_k$ and $H$ affect it?

Experiments:
- Table 1: FedSoft-Async ACC for FMNIST(6). How come cluster accuracy is worse than everything else, even client bfr and local ACC.?
- Section 5.3: since the clients have the 500-2000 data points no matter how many clients are present, and the staleness bound increases with number of client, is the minimal variation with different client counts showing robustness, or an artifact of the experiment design?
- I didn't understand the reason given for worse before client accuracy with small $\rho$. If cluster models are similar, shouldn't it lead to better client accuracy as well?
- The global adjustments are claimed to mitigate adversarial behavior. But, if the server has data from all distributions, won't it recognize adversarial behavior anyway?

### Questions
My main concern with the work is its practical relevance. The authors claim to put clients at the forefront. But, if the server estimates the distribution of the clients, this is a violation of the client data privacy? How can this be reconciled since privacy is one of the privacy motivations for doing FL in the first place?

Section 1
- Among the 3 properties to encourage client participation, autonomy is well taken. But, lightweight is doubtful - the same comm/computation is needed in FedAvg. Regarding performance enhancement, one could argue that personalized FL can help with that. Please comment.

Section 4.3: several questions about the math here
- Assum. 1: What is $F$? Do you mean $F_k$ for all $k$?
- Assum. 3: what is $f_m^t$? Do you mean the first term in $h_m^t$ in (2)?
- Assum. 4: How can $w_k^*$ be unique if $F_k$ is just assumed smooth (assuming Assum. 1 is about $F_k$)? For that, we need, e.g., strong convexity. But, in Assumption 3, $f_m^t, h_m^t$, both of which depend on loss $l(\cdot)$ have bounded gradients. This is confusing.
- Theorem 1: the authors have not commented on the result. Why is the constant $\epsilon$ needed? Why does the convergence for any $k$ depend on $\sum_i a_i$? Most importantly, can you show explicitly for what choice of the learning rate $\gamma$ can we get convergence, and how do $S_k$ and $H$ affect it?

Experiments:
- Table 1: FedSoft-Async ACC for FMNIST(6). How come cluster accuracy is worse than everything else, even client bfr and local ACC.?
- Section 5.3: since the clients have the 500-2000 data points no matter how many clients are present, and the staleness bound increases with number of client, is the minimal variation with different client counts showing robustness, or an artifact of the experiment design?
- I didn't understand the reason given for worse before client accuracy with small $\rho$. If cluster models are similar, shouldn't it lead to better client accuracy as well?
- The global adjustments are claimed to mitigate adversarial behavior. But, if the server has data from all distributions, won't it recognize adversarial behavior anyway?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
