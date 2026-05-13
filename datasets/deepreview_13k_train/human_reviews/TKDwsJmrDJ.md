# Collaborating Heterogeneous Natural Language Processing Tasks via Federated Learning

- Decision: Reject
- Scores: 5, 5, 8, 6

## Abstract
The increasing privacy concerns on personal private text data promote the development of federated learning (FL) in recent years. However, the existing studies on applying FL in NLP are not suitable to coordinate participants with heterogeneous or private learning objectives. In this study, we further broaden the application scope of FL in NLP by proposing an \textsc{Assign-Then-Contrast} (denoted as \ours) framework, which enables clients with heterogeneous NLP tasks to construct an FL course and learn useful knowledge from each other. Specifically, the clients are suggested to first perform local training with the unified tasks assigned by the server rather than using their own learning objectives, which is called the {\sc Assign} training stage. After that, in the {\sc Contrast} training stage, clients train with different local learning objectives and exchange knowledge with other clients who contribute consistent and useful model updates. We conduct extensive experiments on six widely-used datasets covering both Natural Language Understanding (NLU) and Natural Language Generation (NLG) tasks, and the proposed \ours framework achieves significant improvements compared with various baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new technique for applying Federated Learning on sequence modeling tasks (specifically focusing on NLP applications), for coordinating participants with heterogeneous or private learning objectives. The paper proposes the assign and contrast framework, where it relies on a self-supervised learning task for local learning in the assign stage and the use of contrastive learning in the weights averaging stage. The paper introduces a novel framework, and does extensive evaluation on 6 NLP datesets to show the efficacy of the approach.

### Strengths
* The paper does a good job in explaining the related work in the FL space, and motivates a need for their framework to combine heterogenous tasks as opposed to past works with more rigid constraints associated with needing to operate on similar or the same tasks. 

* The assign part of the framework was introduced well, especially by allowing local clients to do self-supervised learning based on labels they already had access to but did not need to share with the global server

* The paper does extensive evaluation and ablation studies to demonstrate the strength of the framework introduced

### Weaknesses
 * The contrast part of the framework lacked rigorous motivation. There was no discussion on the pros and cons of treating the cosine similarity of the model updates as a good measure of grouping the data domains. Are the model updates representative of not only the variety of the data domains but also the heterogeneity of the downstream tasks that are applied on that data? Extensive clustering analysis of model updates would need to be made to motivate this objective. Figure 6 is a step in the right direction, but more rigorous analysis would be useful. Specifically, the paper does not address whether the magnitude of the updates should be considered, or if only the direction is relevant when calculating cosine similarity. Furthermore, it is unclear how the choice of K nearest neighbors affects the overall performance and stability of the contrastive learning stage. The paper should also discuss the potential for negative transfer if clients with dissimilar objectives are grouped together due to noisy or misleading gradient updates.

* Looking at table 2 showed the proposed framework in the top performing range among the competitors, but the improvement in many cases did not seem significant compared to the state of the art. For eg, the Squad and MSQG task top performer had results just 2-3 points below the proposed framework. For all other tasks, the results of all top performers were not significantly different. The paper needs to provide a more nuanced analysis of the performance gains, including statistical significance tests and a discussion of the practical implications of the observed differences. It is also unclear if the proposed method consistently outperforms the baselines across different hyperparameter settings or if the reported results are based on a carefully tuned set of parameters. A sensitivity analysis of the key hyperparameters would be beneficial.

### Questions
* It would be useful to explicitly mention the use of self-supervised learning objectives for the assign portion at the bottom of the introduction section. This would clear up early confusion on how the tasks were assigned without having labels for the local data. Similarly, it would be useful to briefly mention the use of clustering approaches while contrasting.

### Soundness
2 fair

### Presentation
3 good

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
The paper describes a novel framework with heterogeneous/private learning objectives for learning from shared knowledge through federated learning(FL). Participants can build a FL course using the Assign-then-Contrast (ATC) framework without revealing or aligning their own learning objectives. The novelty is that clients can work toward a common goal without sharing their own interests (learning objectives), and by using contrastive learning, they can help clients with similar learning objectives exchange useful information. The server aggregates the trainable parameters of the global model based on the assigned task during each training round. The server aggregates the trainable parameters of the global model based on the assigned task to clients during each training round. When the server assigns tasks to clients, the parameters are updated based on the client's local interest (i.e., when assigned MLM, the encoder is updated and aggregated; and when assigned DR, the updated and aggregated parameters include both the encoder and decoder).

### Strengths
+ Framework is relevant to the ICLR community: it achieves improvements on all the participants compared to ISOLATED (overall 3.66% improvement).
+ The experiments are well planned - randomization, splitting, sufficient datasets, different local task
+ Comparison to baselines including vanilla FL SOTA algorithms (FedAvg, FedAvg-ST, FedProx) and personalized FL (DITTO, FedBN, PerlCFL, SPFL), and isolated local training
+ Reproducibly is enabled with the implementation descriptions and details + code availability willingness
+ Overall noticeable margins of improvement on heterogeneous clients to participate and benefit from an FL course.

### Weaknesses
 + It is still constrained to the global tasks: depending on the server to assign a global task (meaning that participants need to abide by this global task or has to be intrinsically similar)
+ Some novelty is overclaimed, e.g., FL + multi-task [1] (or heterogeneous tasks in the context of this paper),  there is no comparison with this baseline.
+ Some essential questions and concerns on the baselines:
    + The SOTA of the experiments, e.g., IMDB and perhaps others, seems to be different than your experiments (ISOLATED). did you start with a suboptimal setting, e.g., carefully fine-tuned?
+ There is a concern about whether it is worth the margins of improvement provided by Contrastive Learning in the trade of privacy and communication cost. 
    + Additional communication cost between clients means $\Theta (K^2 \cdot D)$, where $K$ is client number and $D$ is data size
    + Privacy can be disclosed to not only the server but also peer clients. Synthetic data is proposed as a way to mitigate the effect, but we want to see more restricted discussion on privacy concerns. Please also consider removing privacy claims if these are not addressed, especially in the abstract and introduction.
    + Willingness of clients' participation: If a global task is imposed by the server and introduced to clients what are the potential drawbacks addressed? i.e. local client training costs (training time and memory cost) and risk (of out of memory) increased.
+ Although there is a marginal improvement it is stated "superior performance". Consider lowering the tone.
+ Many writing issues (see questions).


### Questions
How will this framework tackle backdoor attacks? 

Non-IID could have more discussion, especially the Non-IID introduced by multiple tasks and datasets.

---
[Writing]:

"an FL" -> "a FL"

"learn useful information": One learns from information. Once it's learned, it becomes knowledge.

"unallowable" ?

FL (acronym): once introduced you should stick to it.

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an application of Federated Learning in NLP called Assign-then-Constrast (ATC). This framework facilitates multiple clients (or models) with heterogeneous NLP tasks to not only learn from their own data but also from knowledge of other clients without actual sharing of data amongst different clients.  
The federated learning is achieved through two stages:

Stage 1 - Assign: Involves local training with unified objective assigned to each of the client by the server

Stage 2 - Contrast: Clients train with different local learning objective and exchange knowledge with other clients via an additional contrastive learning loss.

The paper reports evaluation on six datasets and highlights the efficacy of using such a paradigm to train multiple clients. The comparison is against competitive baselines. Additionally, the qualitative analysis and ablation studies show the importance and significance of each of the different stages and modules.

### Strengths
1. Easy to understand paper with comparison against competitive baselines
    
2. Ablation study highlights the importance of each of the component being added.
    
3. State-of-the-art results on multiple tasks learning from shared knowledge by multiple clients.

### Weaknesses
1. Missing details on some important sections. See Questions.
    
2. No statistical significance testing conducted for the results that appear quite incremental compared to the baselines.

### Questions
1. In the introduction, kindly provide a concrete example/use case for federated learning with heterogeneous tasks.
    
2. What does consistent model update mean as given in the abstract?
    
3. Section 3.1: Shed Lighted -> Based on such insights.
    
4. Section 3.2 - Extension with Clustering Algorithms: The gradients change with each iteration, so can the clusters change as well, or is it fixed based on the first iteration?
    
5. Section 3.2 - Extension with Clustering Algorithms - Kindly extend upon the clustering algorithm - provide more details.
    
6. Section 3.3 - 4th paragraph - “To further..” is confusing. Kindly provide concrete examples to highlight this important stage.
    
7. Section 3.3 - Mention that the contrastive learning loss is one of the additional objective other than the client - task specific objective.
    
8. Section 4.2: In FEDAVG what equations govern the federated aggregation? In FEDPROX what is the proximal term
    
9. Table 2: Are these numbers statistically significant? Kindly conduct a significance testing.
    
10. In the related work section, please highlight the importance of ATC for each of the different previous works rather than clubbing them in the end.
    
11. In the conclusion section, kindly mention quantitative results, instead of writing the abstract again.

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper seeks to introduce a framework, which allows for federated learning to take place between end-users who have different learning objectives (e.g. classification versus generation). They propose a 2 step framework, which should protect the privacy of the server (where all of the learning is aggregated as a part of federation learning), as well as the end-users, at the same time as improving performance across varying tasks.

### Strengths
*** Disclaimer *** This paper is very much outside my own specialty, so I've had some trouble understanding the underlying motivations and practical use-cases. That said, my initial review will need to be considered with this context:

Despite being on a topic outside of my wheelhouse, I found this paper mostly quite clear. The authors break down and describe in detail the two steps of their federated learning approach (the "Assign" and "Contrast" components), before conducting baseline experiments, to compare their methods with others in this sub-field. I particularly appreciated the simplicity of experiments (e.g. using simple BERT_tiny models, with simple objectives, on well known datasets, etc., as described in S3.1 and S4.1), so that as an outsider to this sub-field, I could rather focus on the paper's innovation ("Assign then Contrast"). 

For the aforementioned innovation -- I really have a hard time understanding the impact of this new approach, within the sub-field. If most federated learning can indeed only work on homogeneous tasks, then it seems like quite an accomplishment indeed! And although I didn't understand everything, the explanation is thorough enough that it seems this approach could be loosely implemented by others, following the details of the paper. 

Also in the end, I appreciate the discussions, with concrete take-aways and reflections from the analysis, so that I can better understand how something like this could be useful.

### Weaknesses
As an outsider to this specific sub-field it is very hard for me to asses the true weaknesses of the paper. Here, I will attempt to make my best guess:

While the "Contrast" part of the proposed method is focused around preserving privacy, it would have been nice to have some verification of this, as privacy is absolutely central to the proposed model. I genuinely do not work in privacy+fairness, so I do not know if leveraging contrastive learning is sufficient for protecting privacy. Specifically, it's unclear how the contrastive loss function prevents the leakage of sensitive information about individual clients' data distributions. For example, could an adversary infer properties about a client's dataset by observing the learned representations or the gradients shared during the "Contrast" step? Without a formal privacy analysis, it's difficult to ascertain the true privacy guarantees of the proposed method. Furthermore, it would be beneficial to see experiments that directly measure privacy leakage, such as membership inference attacks, to empirically validate the privacy claims.

One last thing -- which is NOT a weakness, but I think addressing this point would be nice:

In the Introduction, the paper introduces the need for improved federated learning by essentially complaining that increased data protections hurt "data owners". This doesn't sound great... I for one am very grateful to have protections on my data, that keep companies from using my data in risky ways! Thus, I would encourage a slight re-framing of the introduction, that doesn't frame end-users rights for data privacy as a burden.  The rest of the paper is much better, in terms of framing for privacy protection, though.

### Questions
Neat project! I only have a few questions for the authors: 

1. Why do you not experiment with more clients? Its unclear to me if these are simulated "clients", or real-life clients. I ask because, for some of the experiments in Table 2, the ATC results are quite close to other tasks, so its unclear to me whether minor improvements are statistically significant with such a small number of clients. Or, perhaps, is a small number of clients intentional? 

2. Verification: in real life, you would never use ATC w/o "Contrast", right? Wouldn't this put customer data at risk? Regarding the point I made in the "Weaknesses" section, is contrastive learning alone enough to safe guard against privacy leakage? 

I am interested in the answers to these questions, but as far as my final score from the manuscript, I am most likely to reference the other reviews and your rebuttals to them, when making my final decision, again because unfortunately this topic is far from my own research topic in NLP.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
