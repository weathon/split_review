# Are We in (A)Sync?: Guidance for Efficient Federated Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Federated Learning (FL) methods have widely adopted synchronous FL (syncFL), where a server distributes and aggregates the model weights with clients in coordinated rounds. As syncFL suffers from low resource utilization on clients with heterogeneous computing power, asynchronous FL (asyncFL), which allows the server to exchange models with available clients continuously, has been proposed. Despite numerous studies on syncFL and asyncFL, how they differ in training time and resource efficiency is still unclear. Given the training and communication speed of participating clients, we present a formulation of time and resource usage on syncFL and asyncFL. Our formulation weights asyncFL against its inefficiencies stemming from stale model updates, enabling more accurate comparison to syncFL in achieving the same objectives. Unlike previous findings, the formulation reveals that no single approach always works better than the other regarding time and resource usage. Our experiments across five datasets show that the formulation predicts relative time and resource usage of syncFL and asyncFL with up to 5.5$\times$ smaller root-mean-square error (RMSE) compared to the baseline methods. We envision our formulation to guide FL practitioners in making informed decisions between syncFL and asyncFL, depending on their resource constraints.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to show that neither synchronous (syncFL) nor asynchronous (asyncFL) Federated Learning (FL) approaches can be deemed to be definitively superior over the other in regards to reducing time and resource consumption, thus invalidating the previous findings which showed one's superiority over the other.

### Strengths
++ The paper makes a novel observation: the current works that compare syncFL and asyncFL concerning their time and resource consumption contradict each other––some works claim that asyncFL is better than syncFL, and others claim the opposite. The authors settle this argument by making a novel statement that there is no definitive winner among the two. 

++ The authors have thoroughly examined the related works, and identified flaws and contradictions among those works.

++ It introduces novel formulations to determine the time and resource usage till the target accuracy is achieved. The formulation accounts for stale model updates in asyncFL which allows it to outperform baseline models.

### Weaknesses
-- Lack of comparison with state-of-the-art approaches for time & resource measurement and estimation. The paper only compares with the Updates-N baseline methods. This is a significant limitation as it does not contextualize the performance of the proposed formulations against established techniques in the field. The absence of comparisons with more sophisticated prediction models makes it difficult to assess the true novelty and effectiveness of the authors' approach.

-- The abstraction of resource usage in FL is over-simplified since real-world FL systems rely on multiple types of resources with heterogeneous characteristics. The paper's focus on cumulative time for on-device training and model weight communication neglects other critical resources such as energy consumption, network bandwidth, and memory usage. This simplification may not accurately reflect the complexities of real-world FL deployments, where resource constraints can vary significantly across different devices and network conditions.

-- The authors' formulations for time and resource consumption make strong assumptions.  The formulations for time and resource consumption assume that the syncFL and asyncFL reach the target accuracy after p rounds. How do we determine the number (p) of updates until target accuracy is achieved? In addition, the authors' formulation assumes that the time (T = {t_1,t_2,...,t_n}) required by the clients to download, train and upload the model weights are constant across training rounds. The assumption of T being constant across rounds may not reflect reality because a client model can be faster in certain rounds and slower in others. This assumption of constant client times oversimplifies the dynamic nature of real-world FL environments, where client performance can fluctuate due to various factors such as device load and network conditions.

-- In section 4, the authors conclude that, based on their formulations, neither syncFL nor asyncFL can be deemed to be definitively superior to the other. The authors have used their formulation to demonstrate that neither syncFL nor asyncFL can be deemed to be definitively superior to the other. They should verify this using actual time and resource usage values. The conclusion drawn from the formulations alone is insufficient without empirical validation using real-world measurements. The lack of experimental evidence to support this claim weakens the overall argument.


### Questions
1. In section 5, under "Reflecting the Impact of Bias", the authors claim that $10*CV(U)+1$ at $p$ yields an accurate prediction. The authors should justify this in the paper.

2. How do the experiments support the authors' argument–––neither syncFL nor asyncFL can be deemed to be definitively superior to the other? The authors have shown that their approach of determining resource and time utilization for asyncFL closely approximates the actual values, however since this does not establish a connection with previous works that have opposing views, it does not invalidate the previous authors' works which determines that either asyncFL is better than syncFL, or vice versa. Figures 3c and 3d do not justify that the authors' formulations are also accurate when predicting time and resource usage for other aggregation schemes. Those figures do not compare the formulations' predictions of time and resource usage to real ones, instead, they simply show the predictions when using the authors' formulations.

Writing Issues:

* Figure 1 has missing legends, making it incomprehensible to the readers. The figure is critical to the paper as it intends to show that neither syncFL nor asyncFL approaches can be deemed to be definitively superior to the other in regards to reducing time and resource consumption. The authors mention that Figure 1 is a comparison of asyncFL and syncFL in terms of their resource and time utilization, however, it appears that the figure is incomplete and does not compare the two approaches.

* What is D-bar in section 5, under "Contribution Scaling on a Client Dataset"?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
AsyncFL allows the server to exchange models with available clients continuously, enhancing the resource utilization. Given the training and communication speed of participating clients, this paper presents a formulation of time and resource usage on syncFL and asyncFL. The proposed formulation weights asyncFL against its inefficiencies stemming from stale model updates, enabling more accurate comparison to syncFL. This paper reveals that no single approach always works better than the other regarding time and resource usage.

### Strengths
1. The finding that "neither syncFL nor asyncFL universally outperforms the other in terms of time and resource usage" is interesting.
2. The studied problem is timely and may have practical influences.

### Weaknesses
1. Lemma 1, Corollary 1, 2 and Proposition 1 consider the participating time and resource usage. However, they do not consider the model training, loss functions, data heterogeneity, etc. Thus, it is hard to say the proposition can be utilized into FL.
2. Non-IID data distribution widely exists in FL. However, experiments only consider IID data distribution.
3. The presentation of experiment results is not clear. What does the proposed formulation mean when compared with other FL algorithms?

### Questions
See weaknesses.

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
This paper proposes a model to formulate the time consumption and resource usage in asynchronous FL methods and tries to use this model to understand the advantage of the asynchronous FL method compared to the synchronous FL method. The idea is interesting and promising, and the topic is meaningful.

### Strengths
The idea is interesting and promising, and the topic is meaningful. The experiment results show that the proposed formulation well approximates the actual time consumption and resource allocation. Overall, I like the idea of this paper, but wish the authors could clarify my concerns regarding the technical results. I'm willing to improve my score if the authors can address some of my concerns.

### Weaknesses
The technical part of this paper is not well-written and difficult to understand to the reviewer.

1. It's difficult for me to understand the real meaning of $f(T, c, i)$. The authors claimed that $f(T, c, i)$ is the portion of time client $i$ participated in AsyncFL. If the training process takes time $A$ and during the $A$ time interval, client $i$ participated in the training process for $B_i$ time units, then I would think that $f(T,c, i)=B_i/A$. However, with this definition, I cannot understand why in Appendix A, $f(T,2,1)=f(T,2,2)=1$ when $T=$\{$ t_1,t_2$ \}. Moreover, I also don't understand why $f(T,c, i)$ is irrelevant with $k$.

2. The expression of some terminologies is not accurate. For example, the number of updates given by other clients during the training and communication of node $i$ is not precisely the quantity in Eq (4), and the quantity in Eq (4) only tells the of updates given by other clients during the $0$th update and the $1$th update of node $i$.

3. I understand that for simplicity, the authors treat delays or the number of updates as continuous variables, rather than discrete variables. However, since these quantities themselves are discrete, the authors should at least mention this in the paper.

### Questions
The authors also provide a formula for delay prediction (above Eq (5)), which is of interest to many researchers. Therefore, can the authors compare the actual delay distribution with the predicted one by experiments? It would be great if you could provide such a comparison even after the rebuttal and in the final version.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
