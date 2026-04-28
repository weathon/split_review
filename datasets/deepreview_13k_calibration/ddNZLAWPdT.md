# Robust Decentralized VFL Over Dynamic Device Environment

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Robust collaborative learning on a network of edge devices, for vertically split datasets, is challenging because edge devices may fail due to environment conditions or events such as extreme weather. The current Vertical Federated learning (VFL) approaches assume a centralized learning setup or assume the active party or server cannot fail. To address these limitations, we first formalize the problem of VFL under dynamic network conditions such as faults (named DN-VFL). Then, we develop a novel DN-VFL method called **M**ultiple **A**ggregation with **G**ossip Rounds and **S**imulated Faults (MAGS) that synthesizes faults via dropout, replication, and
gossiping to improve robustness significantly over baselines. We also theoretically analyze our proposed approaches to explain why they enhance robustness. Extensive empirical results validate that MAGS is robust across a range of fault rates—including extreme fault rates—compared to prior VFL approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers the problem of collaborative inference in vertical federated learning (VFL). In VFL, all clients have the same datapoints, but different subsets of features for each datapoint. Faults in VFL can disrupt both training and inference due to the need for client communication during inference. This work formalizes the problem statement of faults in VFL -- both during the computation in a node, and during communications between nodes.

### Strengths
The paper proposes the notion of dynamic risk, where the expectation of loss is also computed over the stochasticity of faults. In the proposed algorithm, the language model heads of the models at each node are trained by simulating faults via dropouts -- which introduces robustness to faults during test time. The work also proposes several heuristics such as multiple VFL, where the data aggregator is replicated to prevent catastrophic faults with a single point-of-failure. Moreover, gossip rounds o ensemble the predictions from multiple data aggregators reducing the prediction variance across devices. (Unlike vanilla VFL, in DN-VFL, the clients are allowed to act as data aggregators and communicate with each other). Inference is done in two steps: Firstly, each client makes a prediction. This is followed by an "entity" collection these predictions, and subsequently making a final prediction. 

This approach seems like a sound and well-defined approach to the problem of faults in VFL.

### Weaknesses
My major concern (which prevents me from giving a higher score) is that it is not completely clear to me what are the technical challenges that were overcome and novelty of the proposed approach. It majorly seems like some orthogonal approaches are combined to give the proposed approach. While this is not a negative thing per se, it would be highly appreciated if some discussions were added regarding the choices made, which will help clarify some things. For example:

1. Multiple data aggregators have been used in prior works with conventional federated learning too. It falls under the umbrella of "semi-decentralized federated learning" Prior works consider communication failures between data aggregators as well. Is there any reason why it was not considered in this work? This can perhaps be mitigated by using multiple rounds of gossip, and/or optimizing the collaboration weights during the data aggregation process. It's unclear why the specific challenges of communication failures between aggregators in a VFL setting are not explicitly addressed, given that this is a known issue in semi-decentralized FL. The paper should clarify if the gossip mechanism is sufficient to handle these failures, or if additional mechanisms are needed.

2. It was not clear to me -- is the idea of training classifier heads with dropout to simulate test-time faults novel to this paper, and has not been considered in prior work? If so, how scalable is this approach, i.e., is it possible to train the classifier heads for robustness by simulating faults on very large networks (or must it be done in a clustered fashion)? The use of dropout to simulate faults, while intuitive, needs further justification. Specifically, how well does dropout during training truly capture the complexities of real-world faults in a distributed VFL system? It would be beneficial to see an analysis of the correlation between dropout-induced errors and actual fault scenarios. Furthermore, the scalability of this approach should be discussed in more detail, particularly concerning the computational overhead of training with simulated faults on large networks.

### Questions
In addition, I have some more clarification questions:

1. Proposition statements need to be more precise -- eg., in Prop. 1, what is "aggregator specific risk"?

2. More implementation details are needed -- what is the predictor used at each client?

I would be more than happy to reconsider my score contingent on other reviews, and the authors' responses (especially the concerns in the Weaknesses section).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies decentralized vertical federated learning over a dynamic device environment, which the authors define as faults in changing client graphs. The authors develop a novel DN-VFL that brings together dropout, replication, and gossiping and show its outperformance over baselines via empirical results.

### Strengths
* The paper identifies an important issue in the VFL setup, where fault can occur when the clients or the communications betwwen different clients stochastically drop out.
* The paper provides extensive experiments on different datasets.
* The design of algorithms is intuitive, and the derivations seem correct.

### Weaknesses
 * The most obvious weakness is the presentation of the paper. The authors should try to shorten the overview of each section and go straight to the point. For example, the overview of Section 3 is just a wordy replication of what is coming next. It might be helpful to use bullet points to highlight the contributions.
* The related work is not thorough enough. Except asynchronous decentralized learning, the authors have to consider a topic called client unavailability problem in federated learning, where clients may (stochastically) drop out, e.g., in [1,2,3]. Specifically, they should talk about the connections and differences between them and this work.
* There are many contents that seem to be out of the space in Section 2. For instance, different client selection strategies have been talked about in great detail, which should belong to the development of algorithms instead.
* Following the problem formulation, there is no motivating example to illustrate that a dynamic network can lead to significant performance degradation to the classic VFL algorithms. Although it might be intuitive to conjecture that is the case, evidence is needed.
* Some of the definitions are missing. In Section 3.1, the authors talk about adopting Communication-wise Dropout. Yet, no formal definitions are given. 
* It is hard to parse the different components directly from Algorithm 1. No elaborations on Algorithm 1 have been given; neither do the authors talk about the connections in Sections 3.2 and 3.3.
* The most confounding part is that the authors greatly emphasize the case when there are no active aggregators. In that case, a trivial solution is to skip and move on to the next round. In addition, Proposition 1 is a lower bound, meaning that the second term, which depends on the probability of an empty active client set, can be ignored.
* In Proposition 2, it is also unclear what the dynamic risk of an ensemble leads to in the sense that no matching upper bound for risk with faults is proved.

### Questions
* Can the authors provide numerical or theoretical justifications that the dynamic device environment will lead to detrimental effects?
* What is the difference between Definition 2 and Definition 3? It seems that Definition 3 subsumes Definition 2 although with different probabilities.
* Which definition (2 or 3) do the authors consider when proving their theoretical results?
* Can the authors provide formal definitions of communication-wise dropout?
* Can the authors outline the connections between the pseudocode Algorithm 1 and their development of methods?
* Regarding experiment setups, the authors compare their serverless methods with VFL methods with a server while also including baseline communication networks. Can authors elaborate on the experiment setup for VFL methods with a server?
* Why are there NAN results in Table 3 and Table 8 (in Appendix) for VFL and PD-VFL? Can the authors elaborate the difficulty in not being able to produce meaningful results for VFL and PD-VFL?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper attempts to improve the robustness of the (Vertical) Federated Learning framework, where data features are spread across different clients. It proposes a method called MAGS (Multiple Aggregation with Gossip Rounds and Simulated Faults) to overcome scenarios of device failures and communication reliability.  The authors propose combining three strategies to enhance fault tolerance and resilience: (1) fault simulations (dropout) during training, (2) aggregation redundancy using multiple clients as data aggregators, and (3) Gossip rounds for reducing prediction variability and improving resiliency.

The authors claim to formalize the integration of these strategies into a framework that they define as Dynamic Network Vertical Federated Learning (DN-VFL). They introduce a dynamic risk metric to assess model performance and propose three propositions. Proposition 1 establishes a lower bound on the dynamic risk of their approach. Proposition 2 highlights the benefits of averaging prediction using gossip rounds by comparing the risk of ensembled predictions across multiple clients versus that of a single prediction by an individual client. Proposition 3 claims to establish a bound on the difference between the ensemble and the local predictions.

Empirical experiments were conducted on various datasets, including MNIST and StarCraftMNIST, among several others. A key aspect of these studies was to evaluate the performance of the MAGS approach under device and communication faults. The authors compared performance with the Vanilla VFL approach and VFL variations, including party-wise and communication-wise dropouts. Consensus algorithms were also studied.

### Strengths
The paper attempts to formalize the combination of three strategies, which have traditionally been used in isolation, to improve the robustness of the VFL framework. The authors formalize some aspects of their approach and performs a reasonably comprehensive experimental study.

### Weaknesses
My primary concern with this work is that, by allowing peer-to-peer communication between devices, the framework diverges from the original design and motivation of Vertical Federated Learning. VFL was specifically devised for environments where direct communication between parties is impractical or restricted due to privacy, regulatory, or technical limitations. By introducing peer-to-peer communication through gossip rounds, client-based aggregation, and ensembling, the proposed framework theoretically violates the foundational principles of federated learning. In fact, the framework now resembles a multi-agent system, which allows direct interactions among agents to achieve consensus.  This seems to be a topic that is closely related and yet there is no mention of it in the literature review.  Can the authors explain how their MAGS framework maintains the privacy guarantees of VFL while introducing peer-to-peer communication? Are there specific use cases where this trade-off is justified?

Proposition 1 highlights risk reduction when using multiple aggregators, which seems to be an intuitive results considering that the MAGS framework increases redundancy. Similarly, Proposition 2 highlights a reduction in variance which is a natural byproduct of ensembling. Proposition 3 also seems to be a simple and direct adaptation of a well-known consensus result in distributed averaging. Could the authors clarify how these propositions provide new insights or guarantees specific to the DN-VFL setting that are not immediately obvious from existing results in other domains?

### Questions
Can the authors explain how their MAGS framework maintains the privacy guarantees of VFL while introducing peer-to-peer communication? Are there specific use cases where this trade-off is justified?

Could the authors clarify how these propositions provide new insights or guarantees specific to the DN-VFL setting that are not immediately obvious from existing results in other domains?

Could the authors explain how MAGS differs from a multi-agent system (MAS)? While MAS commonly involves multiple agents collaborating for decision-making, similar configurations can also be applied to Machine Learning. Can authors discuss any specific advantages that MAGS might have over traditional MAS approaches in this context? Alternatively, are there any VFL-specific constraints that MAGS addresses that a general MAS approach might not?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The algorithm presented in this paper is designed to address the robustness of Vertical Federated Learning (VFL) in dynamic network environments, especially when devices may fail due to faults caused by environmental factors or extreme weather. The algorithm is called MAGS (Multiple Aggregation with Gossip Rounds and Simulated Faults), which improves robustness by simulating faults during training, replicating the data aggregator, and utilizing gossip propagation rounds.

### Strengths
The MAGS algorithm proposed in this paper is mainly compared with several existing Vertical Federation Learning (VFL) methods, including traditional VFL, PD-VFL, MVFL and its variants such as MVFL-G4 and CD-MVFL-G4. These methods have different capabilities in dealing with device failures, especially in distributed environments such as edge computing where devices may fail due to a variety of reasons (such as extreme weather, power problems, etc.) to fail, which in turn affects the reliability and performance of the whole system. MAGS enables the system to maintain good performance in spite of high equipment failure rates by simulating failures and multiple rounds of rumor propagation.

### Weaknesses
The algorithm proposed in this paper has several disadvantages or limitations that need further clarification. The first one is due to the fact that MAGS needs to perform additional rounds of rumor propagation, which may incur more computational and communication overhead. Specifically, the multi-round gossip protocol, while potentially beneficial for robustness, introduces a significant communication burden, especially in scenarios with a large number of devices or limited bandwidth. The paper does not provide a detailed analysis of this overhead, making it difficult to assess the practical scalability of the approach. In addition, there seems to be a limitation in the applicability of the MAGS algorithm, based on this paper it is known that although MAGS excels in dealing with high failure rates, it may not be advantageous compared to other VFL methods in the case of lower failure rates. How can a better algorithm be chosen for a specific equipment failure rate in a practical application? It seems that this paper does not provide quantitative selection criteria. The lack of clear guidelines for choosing between MAGS and other VFL methods based on the expected failure rate is a significant limitation, hindering its practical adoption.

### Questions
1.In Algorithm 1 proposed in this paper, the message interaction between clients is based on the multi-round Gossip protocol. However it seems that Algorithm 1 will put higher requirements on communication and computation resource consumption compared to the single round Gossip usually used in decentralized optimization. Can the authors avoid using the multi-round Gossip protocol? 
2.Another important topic of concern to the reviewer is that the paper does not quantitatively analyze the effect of the number of Gossip rounds on the performance of the algorithm under different network structures. It makes the results of this paper lack theoretical interpretability. In addition, can the authors further explore how to automatically adjust the optimal number of Gossip rounds according to different network structures?
3.Could the authors describe the differences and connections between the two types of failures leading to dynamic networks considered in the paper and the Byzantine attacks (malicious server) and denial-of-service attacks (communication link corruption) that are common in centralized or decentralized federated learning literature?
4.The MAGS approach is presented in the paper and its superiority is shown in the experiments. However, the theoretical analysis section could be more detailed as to why the MAGS approach improves robustness. It is recommended to add a mathematical derivation of the convergence analysis of the MAGS algorithm and how the algorithm enhances robustness by simulating faults, replicating data aggregators, and gossip propagation.
5.The effect of network structure on performance can be further explained, especially how MAGS performs under different network topologies, such as complete graph, ring, star, etc., and whether the parameters or design ideas need to be adjusted.
6.In accordance with this paper, MVFL is the optimal model when trained in a fault-free scenario. This means that in scenarios where high failure rates are not anticipated, MAGS may not be the most efficient approach. Can the authors discuss the reasons for that phenomenon? Can the algorithm be modified so that it achieves optimal performance under different failure rate conditions?

### Soundness
3

### Presentation
3

### Contribution
2
