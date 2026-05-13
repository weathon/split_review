# AdaRC: Mitigating Graph Structure Shifts during Test-Time

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Powerful as they are, graph neural networks (GNNs) are known to be vulnerable to distribution shifts. Recently, test-time adaptation (TTA) has attracted attention due to its ability to adapt a pre-trained model to a target domain, without re-accessing the source domain. However, existing TTA algorithms are primarily designed for attribute shifts in vision tasks, where samples are independent. These methods perform poorly on graph data that experience structure shifts, where node connectivity differs between source and target graphs. We attribute this performance gap to the distinct impact of node attribute shifts versus graph structure shifts: the latter significantly degrades the quality of node representations and blurs the boundaries between different node categories. To address structure shifts in graphs, we propose {\algname}, an innovative framework designed for effective and efficient adaptation to structure shifts by adjusting the {\gammanicknames} in GNNs. To enhance the representation quality, we design a prediction-informed clustering loss to encourage the formation of distinct clusters for different node categories. Additionally, {\algname} seamlessly integrates with existing TTA algorithms, allowing it to handle attribute shifts effectively while improving overall performance under combined structure and attribute shifts. We validate the effectiveness of {\algname} on both synthetic and real-world datasets, demonstrating its robustness across various combinations of structure and attribute shifts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of structure shifts in Graph Neural Networks at test time.  The authors claim that existing test-time adaptation methods are primarily designed for attribute shifts rather than structure shifts. Based on theoretical analysis, they propose a framework called AdaRC, which aggregates hop parameters to restore good node representation, alleviating the negative impact of structure shifts. They also employ pseudo-class labels to optimize the hop-aggregation parameters.

### Strengths
1. The paper points out the problem of structure shifts, which is indeed overlooked in previous research on TTA, or not focused explicitly at least. 

2. The proposed AdaRC framework provides a simple yet effective solution for graphs with structure shifts at test time. It is compatible with existing Test-Time Adaptation algorithms, which allows better adaption.

3. The authors conduct a detailed theoretical analysis of the impact of structure shifts on a single-layer GCN on a CSBM-generated graph.

### Weaknesses
1. The theoretical analysis focuses on single-layer GCNs and CSBM-generated graphs, which represent a simplified model where structure shifts are easily identified. However, the evolving real-world graph structures are far more complex. It is unclear whether the findings on this simplified model still hold for real-world graphs, particularly in domains where the task accuracy is not high. Specifically, the analysis does not consider the impact of more complex structural variations such as changes in clustering coefficients or community structures, which are often present in real-world graphs and can significantly affect the performance of multi-layer GNNs. The theoretical analysis should be expanded to include these more complex scenarios.

2. The experimental results, which show promising performance, are primarily based on synthetic datasets or real-world datasets with synthetic structure shifts. The verification that the structure shifts existence in the real-world graphs should be included. The paper lacks a thorough analysis of whether the observed performance gains are due to the method's ability to adapt to real-world structure shifts or simply to the artificially introduced shifts. It is crucial to demonstrate that the method is effective in real-world scenarios where structure shifts are not explicitly controlled.

3. The experimental setup for real-world datasets lacks transparency. The paper mentions injecting structure shifts by deleting a subset of homophilic edges. However, it did not specify the quantity of this deletion and the selection criteria. The lack of detail makes it difficult to reproduce the experiments and assess the robustness of the method. Furthermore, it is unclear how the degree of homophily was measured and what impact the edge deletion had on the overall graph structure. A more detailed explanation of the edge deletion process is needed, including the specific metrics used to quantify the changes.

4. The paper presents full results for only one GNN backbone. Presenting results for different GNN backbones, especially fundamental ones, would provide a more comprehensive understanding of AdaRC's effectiveness and applicability across various architectures. The current evaluation limits the generalizability of the findings. It is important to demonstrate that the proposed method is not specific to a particular GNN architecture and can be effectively applied to other commonly used architectures.

### Questions
1. AdaRC is a plug-and-play method, have you explored scenarios where it might conflict with other TTA methods? For instance, if a TTA method focuses on adapting to changes in node features while AdaRC adjusts to structure shifts, could their optimization goals lead them in opposite directions?

2. On Twitch-E and OGB-Arxiv, AdaRC shows only minor improvements without artificially injected structure shifts. Does this suggest that the impact of structure shift might be less significant in these real-world datasets?  Could this be because the type of structure shift addressed by AdaRC is less prevalent in these contexts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes the AdaRC framework, a test-time adaptation approach for graph neural networks (GNNs). At the core of AdaRC is a prediction-informed clustering (PIC) loss, designed to seamlessly integrate with existing methods. Experimental results demonstrate the effectiveness of PIC in enhancing GNN performance.

### Strengths
The paper analyzes the performance gap in a simple single-layer Graph Convolutional Network (GCN) using graphs generated from the Community Structure Benchmark Model (CSBM). It effectively investigates the impacts of attribute shifts and structural shifts on performance.

The proposed PIC loss is both simple and effective, allowing for seamless integration with existing frameworks and methods. Its effectiveness is validated through experimental results.

### Weaknesses
It is worth noting that, as I am not deeply familiar with this specific area, my comments here may lack technical depth. I will rely on the insights from other expert reviewers and will focus primarily on their evaluations. Here, a few potential concerns include:

- The performance improvements on the Twitch-E and OGB-Arxiv datasets appear marginal. Could the authors provide further analysis to clarify the reasons behind these limited gains?

- The gains achieved seem to vary significantly across different methods and backbone models. For instance, the Tent method demonstrates the highest improvements. Could the authors offer insights into why this variation occurs?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes AdaRC, a novel framework aimed at improving graph neural networks (GNNs) under distribution shifts, particularly those involving changes in graph structure. Traditional test-time adaptation (TTA) methods are typically designed to handle shifts in node attributes, but they perform poorly with structure shifts, where connectivity patterns vary significantly between training and test data. AdaRC addresses this gap by dynamically adjusting the hop-aggregation parameters in GNNs, effectively enhancing node representation quality under structure shifts. Additionally, a prediction-informed clustering (PIC) loss is introduced to encourage clear separations between node categories, further improving adaptation. Extensive experiments demonstrate AdaRC's compatibility with existing TTA methods, yielding notable performance improvements on both synthetic and real-world datasets.

### Strengths
- AdaRC introduces a new approach to handling structure shifts by adapting hop-aggregation parameters, which allows the model to improve node representation quality in ways traditional TTA methods cannot.

- The experimental evaluation is comprehensive, covering both synthetic and real-world datasets, and demonstrates substantial improvements in accuracy and robustness across different shifts, particularly structure shifts.

- The theoretical insights into the impact of structure and attribute shifts are clearly explained, and the figures and visualizations effectively illustrate the method's impact.

### Weaknesses
 - While the PIC loss offers advantages, its application may face scalability challenges with very large graphs due to the computational overhead introduced by clustering operations. The method's efficiency under extreme graph sizes could be explored further.

- AdaRC's performance relies on the optimization of hop-aggregation parameters, which may not generalize across all GNN architectures without tuning. This reliance might limit its applicability for varied and complex GNN models.

- AdaRC has been evaluated on static graphs with controlled shifts. Its applicability to dynamic graphs, where structure shifts occur over time, is not explored, which could be crucial for certain real-time applications.

- The performance of AdaRC's clustering approach may be sensitive to the quality of initial predictions, particularly in cases where pseudo-labeling accuracy is low, potentially affecting the model’s stability in scenarios with noisy initial data.

### Questions
- Can AdaRC be adapted to handle continuously evolving graphs where node connectivity changes over time?

- How does the computational efficiency of AdaRC scale when applied to graphs with millions of nodes?

- Could PIC loss performance be enhanced by integrating more robust initialization methods for pseudo-labeling in low-confidence scenarios?

- Does the framework support automated tuning of hop-aggregation parameters across different GNN architectures, or would manual tuning be required for optimal results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method to mitigate the impact of structure shifts on graph neural networks (GNNs) during test-time adaptation (TTA). The core innovation lies in the introduction of the prediction-informed clustering (PIC) loss to enhance node representation quality during TTA, alongside adjusting hop-aggregation parameters to handle structure shifts. The approach is designed to be compatible with existing TTA algorithms and shows promising results.

### Strengths
1. The introduction of the PIC loss to improve node representation quality without labels is a promising approach. This loss function helps better separate classes by minimizing intra-class variance and maximizing inter-class variance, providing a reliable alternative to traditional entropy-based methods.

2. AdaRC is a plug&play framework that can be seamlessly integrated into existing TTA algorithms, making the approach highly extensible.

### Weaknesses
1. The authors mention that traditional TTA methods rely on the quality of node representations, but there are also existing works in graph TTA and DA that similarly address the impact of structure shifts. It is recommended to further discuss the differences and advantages of AdaRC in comparison to these methods, particularly in handling heterophilic graphs or complex structure shifts. Specifically, a more detailed comparison is needed that clarifies how AdaRC's approach to adapting hop-aggregation parameters differs from methods that directly manipulate the graph structure or node features during adaptation. It would be beneficial to discuss the computational trade-offs and performance differences, especially in scenarios with varying degrees of homophily and different types of structural perturbations.

2. In Section 3.2, the authors discuss the distinct impacts of attribute and structure shifts; however, using a single-layer GCN as an example may not be sufficient. Given that adjusting hop-aggregation parameters typically involves integrating multi-layer GCNs and broader neighborhood information, it would be beneficial to explore the impact of multi-layer GCNs in the model. The analysis should consider how the proposed method scales to deeper GNN architectures and how the learned hop-aggregation parameters interact with the multi-layer aggregation process. Furthermore, it is important to analyze whether the effectiveness of AdaRC is consistent across different depths of GNNs, as deeper networks can be more sensitive to structural variations.

3. Given that the process of using the PIC loss to update hop-aggregation parameters intuitively focuses on optimizing the distinction of node representations (i.e., separating node attribute boundaries), it is recommended to further explore the specific mechanisms by which various structural shifts affect GNN performance. This would help to enhance the theoretical depth and rigor of the analysis. A deeper investigation into how different types of structural shifts (e.g., changes in clustering coefficients, degree distribution, or community structure) impact the node representations and the effectiveness of the PIC loss is needed. It is not clear how the method would perform under more complex structural shifts that are not easily captured by homophily or degree changes.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
[Update]
Thanks for the authors'  feedback. My concerns have been addressed. I raised my vote accordingly.

The authors present a method called AdaRC, which is designed to improve the accuracy of Graph Neural Networks (GNNs) under testing time graph structure shifting conditions. It achieves this by adapting GNN architectures in real-time based on the changing graph structure during testing.  The key idea is to introduce a prediction-informed clustering loss which leads to a better learned node representation. The authors demonstrate the superiority of AdaRC algorithm on several popular benchmark datasets with comparisons to popular baseline methods.

### Strengths
* Propose a novel loss (PIC loss) to improve the robustness of learned graph embedding when structure shifting is presented.
* The algorithm comes with theoretical guarantees, although I did not check the correctness of the proof.
* Experiments on both controlled synthetic datasets and real-world datasets show the effectiveness of the proposed algorithm.

### Weaknesses
 * The paper is not easy to follow, especially for readers without years of experiences in graph neural networks. It would be nice if the authors could provide high level intuitions behind their algorithms, before giving mathematical statements.

* To my best guess, the proposed method is not data driven. The algorithm relies on several theoretical assumptions in order to extract an invariant node embedding on the shifted graph structure. The major concern is that, such assumptions may not hold in real-world tasks. It is also hard to verify whether the assumptions hold or not for a given task. This greatly limits the practical value of the algorithm.

### Questions
* If the graph structure is shifting in real-time, that is, there is no stable distribution in testing time, will the proposed algorithm still work well?

### Soundness
3

### Presentation
2

### Contribution
2
