# Probabilistic Sampling-Enhanced Temporal-Spatial GCN: A Scalable Framework for Transaction Anomaly Detection in Ethereum Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 1, 5, 5, 5

## Abstract
The rapid evolution of the Ethereum network necessitates sophisticated techniques to ensure its robustness against potential threats and to maintain transparency. While Graph Neural Networks (GNNs) have pioneered anomaly detection in such platforms, capturing the intricacies of both spatial and temporal transactional patterns has remained a challenge. This study presents a fusion of Graph Convolutional Networks (GCNs) with Temporal Random Walks (TRW) enhanced by probabilistic sampling to bridge this gap. Our approach, unlike traditional GCNs, leverages the strengths of TRW to discern complex temporal sequences in Ethereum transactions, thereby providing a more nuanced transaction anomaly detection mechanism. Preliminary evaluations demonstrate that our TRW-GCN framework substantially advances the performance metrics over conventional GCNs in detecting anomalies and transaction bursts. This research not only underscores the potential of temporal cues in Ethereum transactional data but also offers a scalable and effective methodology for ensuring the security and transparency of decentralized platforms. By harnessing both spatial relationships and time-based transactional sequences as node features, our model introduces an additional layer of granularity, making the detection process more robust and less prone to false positives. This work lays the foundation for future research aimed at optimizing and enhancing the transparency of blockchain technologies, and serves as a testament to the significance of considering both time and space dimensions in the ever-evolving landscape of the decentralized platforms.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose the usage of temporal random walks (TRW) with probabilistic sampling enhancement for anomaly detection in Ethereum network data. The method augments the GCN convolution operation with the TRW information. The authors then used classical anomaly detection algorithms (like isolation forest) to detect the anomalies on the GCN embeddings.

### Strengths
- Unsupervised anomaly detection is an interesting area that requires more study.
- The method incorporates temporal information into GCN models.
- Practical application on Ethereum networks, which may be extended to other financial transaction cases.

### Weaknesses
1) The paper feels incomplete and not ready for me. There are multiple sections of the paper that are incomplete, for example:
    - "Proof" in  Section 2.3. What theorem to prove, and where is the proof?
    - "caption." in Section 3.
2) The whole paper feels like a conjecture rather than proven or discovered findings. For example, the use of "Theorem (Hypotehetical)" in Section 3.4. What does that mean? Are they proven theorems or just hypotheses?. Another example is the use of "Potential Conclusions" in Section 1.
3) The authors do not use proper baselines in the experiments. There are multiple GNN-based anomaly detection algorithms that have been proposed in the literature. None of them appeared in the experiment.
4) The evaluation metrics used by the authors are not appropriate for comparison. The number of nodes flagged as anomalous cannot be used as a fair metric in anomaly detection. A model may flag many nodes as anomalies, but they could be just false positive detections.

### Questions
Please answer my questions in the previous section.

### Soundness
1 poor

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper underscores the potential of temporal cues in Ethereum transactional data
but also offers a scalable and effective methodology for ensuring the security and
transparency of decentralized platforms.

Revisions needed as follows:

a) Gaps in literature should be mentioned

b) Readability improved

c) Equations should be numbered

d) Figure 1 and 2 text is too small, impossible to read

e) The proofs are too short and it was tough to gauge if they were sound or not as presented. 

f) No tabular data was presented.

### Strengths
This paper underscores the potential of temporal cues in Ethereum transactional data
but also offers a scalable and effective methodology for ensuring the security and
transparency of decentralized platforms.

### Weaknesses
 a) Gaps in literature should be mentioned

b) Readability improved

c) Equations should be numbered

d) Figure 1 and 2 text is too small, impossible to read

e) The proofs are too short and it was tough to gauge if they were sound or not as presented. 

f) No tabular data was presented.

### Questions
Why are the proofs so short?

Why is no tabular data presented?

What is the overall novelty compared to current state of the art?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel framework, called Probabilistic Sampling-Enhanced Temporal-Spatial Graph Convolutional Network (TRW-GCN) for anomaly detection in Ethereum networks. The paper highlights the importance of considering both time and space dimensions in anomaly detection and offers a scalable and effective methodology for ensuring the security and transparency of decentralized platforms. The experimental results demonstrate the superiority of the TRW-GCN framework in detecting anomalies and transaction bursts compared to traditional GCNs. 
The main contributions of this paper are as follows:

1.The paper introduces several innovative aspects. Firstly, it combines Temporal Random Walks (TRW) with Graph Convolutional Networks (GCNs) to capture temporal patterns in Ethereum transactions, enhancing anomaly detection. 
2.Secondly, the authors leverage probabilistic sampling methods to address the challenge of training GCNs on large-scale graphs, improving computational efficiency and scalability. 
3.Lastly, the integration of both spatial relationships and time-based transactional sequences as node features adds an additional layer of granularity to the detection process, making it more robust and less prone to false positives.

### Strengths
Strengths:

1.Integration of TRW with GCNs: The paper introduces a novel approach that combines TRW with GCNs, enhancing the model's ability to detect anomalies and transaction bursts influenced by recent events.
2.Consideration of spatial and temporal dimensions: By incorporating both spatial relationships and time-based transactional sequences as node features, the proposed model provides a comprehensive approach to anomaly detection in Ethereum networks.
3.Scalability and efficiency: The paper addresses the challenge of training GCNs on large-scale graphs by leveraging probabilistic sampling methods, improving computational efficiency and scalability.

### Weaknesses
Weaknesses:
1. My main concern is that the contribution may be not enough for this conference. Although the application is novel, the idea of using temporal information to build graphs (and weighted adjacency matrix) is not new in pattern recognition and machine learning areas. In addition, the proposed method seems straightforward.
2. Lack of ablation experiment: While the paper presents the theoretical benefits of the TRW-GCN framework, there is a need for empirical evaluation to demonstrate its tangible benefits. Comparing the performance of GCN with and without TRW on a temporal dataset would provide more evidence of the model's effectiveness.
3. Lack of intuitive visualization of experimental results: The paper presents experimental results to demonstrate the superiority of the TRW-GCN framework, but the visualizations and figures provided are not clear and do not effectively convey the findings. The authors should consider improving the clarity and quality of the figures to make the experimental results more intuitive and easier to interpret.

### Questions
None.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study proposed an approach for capturing both spatial and temporal transactional patterns in Ethereum network anomaly detection. Specifically, the paper introduces temporal random walks (TRWs) in graph convolutional networks (GCNs), which may help discern complex temporal sequences in Ethereum transactions as an anomaly detection mechanism.

### Strengths
+ The study focuses on an interesting and important topic.
+ The consideration of temporal features is inspiring.

### Weaknesses
 + The presentation and writing of the paper need improvement

Overall, the paper is not well-written with a somewhat unclear presentation and lacks critical details. It is necessary to describe the main contributions of the study and clearly explain how the existing challenges are addressed. Furthermore, as a key technology involved in this research, TRW should be introduced with more details, such as what specific temporal features are used and how they interact with spatial features, if applicable. Additionally, it is not clear which 7 features are extracted and why they were selected. Were they chosen based on findings from other existing studies? An example to demonstrate a sample and how the spatial and temporal patterns are involved would be helpful.

+ Regarding the ground truth

After reading the Empirical Analysis section, it feels that the anomaly detection results are not validated against any ground truth. In other words, it is unclear whether the detected anomalies represent actual threats. Furthermore, from the description stating, "by changing the threshold, far more anomalies could be detected," it appears that the accuracy of anomaly detection depends on the chosen threshold. This raises the question of how to determine the threshold in practical applications.

+ Lack of comparison with existing approaches

As mentioned in the Introduction section, there are numerous related studies that employ various sampling methods. Liu et al. (2023) is introduced as an approach that "combines historical information over time". However, none of these approaches is considered as a benchmark method. It would be better and necessary to provide more experimental results demonstrating that the proposed approach offers a superior solution.

### Questions
+ How to determine the threshold in practice?
+ Is the experimental result validated against any ground truth, and if there is ground truth, how is it obtained?
+ Are there any existing studies could be compared as benchmarks? If there are no proper related studies, please explain why.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
