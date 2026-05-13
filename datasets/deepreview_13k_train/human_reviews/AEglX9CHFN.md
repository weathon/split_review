# HG-Adapter: Improving Pre-Trained Heterogeneous Graph Neural Networks with Dual Adapters

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
The ``pre-train, prompt-tuning'' paradigm has demonstrated impressive  performance for tuning pre-trained heterogeneous graph neural networks (HGNNs) by mitigating the gap between pre-trained models and downstream tasks. However, most prompt-tuning-based works may face at least two limitations: (i) the model may be insufficient to fit the graph structures well as they are generally ignored in the prompt-tuning stage, increasing the training error to decrease the generalization ability; and (ii) the model may suffer from the limited labeled data during the prompt-tuning stage, leading to a large generalization gap between the training error and the test error to further affect the model generalization. To alleviate the above limitations, we first derive the generalization error bound for existing prompt-tuning-based methods, and then propose a unified framework that combines two new adapters with potential labeled data extension to improve the generalization of pre-trained HGNN models. 
Specifically, we design dual structure-aware adapters to adaptively fit task-related homogeneous and heterogeneous structural information. We further design a label-propagated contrastive loss and two self-supervised losses to optimize dual adapters and incorporate unlabeled nodes as potential labeled data. Theoretical analysis indicates that the proposed method achieves a lower generalization error bound than existing methods, thus obtaining superior generalization ability. Comprehensive experiments demonstrate the effectiveness and generalization of the proposed method on different downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
A dual-adapter approach has been introduced to graph prompt-tuning methods. The key insight of this work is to leverage dual adapters to capture both node features and graph structures to realize prompt tuning for pre-trained HGNN models. Experimental results on four benchmark datasets were provided in terms of two validation metrics.

### Strengths
- A new dual-adapter approach, applied to different pre-trained HGNN models, has been developed to enrich the current graph prompt tuning methods. 
- Two self-supervised graph learning loss functions have been designed to realize label augmentation, showing a clear improvement in the ablation study given in `Table 2`. 
- The paper provides two orthogonal solutions to improve the generalization error bound, i.e., 1) improving prompt flexibility/complexity by dual adapters and 2) improving data efficiency by designing self-supervised label augmentation.

### Weaknesses
 - **Limited Technical Novelty**: The design of dual adapters and self-supervised losses builds on top of several well-established technologies. Thus, the technical contribution of this work is relatively limited since no new loss functions or adapter architectures have been developed. Specifically, the dual adapter approach seems to be a straightforward application of existing adapter techniques to both node features and graph structure, lacking a novel mechanism for how these adapters interact or are specifically tailored for heterogeneous graphs. Similarly, the self-supervised losses, while effective, appear to be standard contrastive and reconstruction losses, without significant modification or theoretical justification for their use in this context.
- **Unclear Insights for HGNN**: It remains unclear what new insights or hypotheses have been introduced to HGNNs by this work. It seems common to improve the generalization bound by increasing parameters and labels. Are there any specific designs or findings for prompt-tuning of HGNNs? The theoretical results in `Theorem 2.3` and `Theorem 2.4` are relatively weak, where the former only proves the existence of $|\bar{P}_M|$ without giving guidance on how to tune or find this optimal size, while the latter builds on *a very strong assumption* that $|P_A|$ is expected to be closer to $|ar{P}_M|$ without showing evidence. The theorems lack practical implications for guiding the design of the adapters or for understanding the specific challenges of prompt-tuning in heterogeneous graph neural networks. The assumption that $|P_A|$ is closer to $|\bar{P}_M|$ needs more justification, as it's not clear why the proposed dual adapter approach would inherently lead to a parameter space closer to the optimal one.
- **Marginal Improvement**: As shown in `Table 1`, the improvement of the proposed HG-Adapter over existing graph prompt tuning methods, e.g., HGPrompt and HetGPT, is quite marginal and generally less than 1% in three of four datasets. Per the provided theoretical results, can we further improve the performance by increasing the size of dual adapters? It would also be helpful to provide an abolition study on each adapter and give a parameter analysis in terms of adapter size. The lack of substantial performance gains raises questions about the practical significance of the proposed method, especially given the added complexity of the dual adapter approach. The absence of a detailed ablation study on individual adapter components and parameter sensitivity further limits the understanding of the method's behavior and potential for improvement.

### Questions
- Can the authors more clearly articulate the novel aspects of their approach, particularly in combining dual adapters with prompt tuning for heterogeneous graphs? 
- Are there any specific insights or hypotheses about prompt-tuning for HGNNs that motivated the proposed approach? It would also be helpful to explain how to find or approximate the optimal parameter size $|\bar{P}_M|$ and provide empirical evidence or further justification to demonstrate that $|P_A|$ is closer to $|\bar{P}_M|$. 
- Can the performance be further improved by varying the size of the dual adapters? An ablation study showing the impact of each adapter individually is also expected.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, a unified pre-trained and prompt tuning framework is proposed by combining two new adapters with potential labeled data extension to improve the generalization of pre-trained heterogeneous graph neural networks. In the proposed method, dual structure-aware adapters are adopted to fit task-related homogeneous and heterogeneous structural information. Meanwhile, three losses are designed, including a label-propagated contrastive loss and two self-supervised losses. The ablation studies show that each component is very essential in the proposed method.

### Strengths
In the proposed method, dual structure-aware adapters are designed to capture task-related homogeneous and heterogeneous structural information. A label-propagated contrastive loss and two self-supervised losses are proposed to achieve the potential labeled data extension. Meanwhile, a theoretical analysis also has been given to verify the effectiveness of the proposed method.

### Weaknesses
The motivation should be further explained with some toy examples. In the analysis part of challenges, although three limitations are presented, how to demonstrate that their drawbacks really exist in the real-world applications.

The authors have highlighted that “it is the first dedicated attempt to design a unified “pre-train, adapter-tuning” paradigm to improve different pre-trained HGNN models”. While HGPrompt (Yu et al., 2024a) is designed with both pre-training and the prompt-tuning. Hence, I wonder whether the first effort is suitable.

In the experiments, for the method HERO, the improvements are not satisfactory except on Aminer. Hence, I wonder the complexity between HG-Adapter and HetGPT.

Although the proposed method uses the self-supervised technique to improve the confidence of propagated labels, I do not think it can guarantee the accuracy of the propagated labels. Hence, I wonder if the propagated labels are too noisy, whether the proposed method can obtain satisfactory performance.

### Questions
1)	In the main contributions, the authors has highlighted that “it is the first dedicated attempt to design a unified “pre-train, adapter-tuning” paradigm to improve different pre-trained HGNN models”. While HGPrompt (Yu et al., 2024a) is designed with both pre-training and the prompt-tuning. Hence, I wonder whether the first effort is suitable.
2)	In the experiments, for the method HERO, the improvements are not satisfactory except on Aminer. Hence, I wonder the complexity between HG-Adapter and HetGPT.
3)	Although the proposed method uses the self-supervised technique to improve the confidence of propagated labels, I do not think it can guarantee the accuracy of the propagated labels. Hence, I wonder if the propagated labels are too noisy, whether the proposed method can obtain satisfactory performance.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Summary of the paper 

The paper pointed out the major limitations remaining currently in the "pre-train, prompt-tuning" paradigm for heterogeneous graph neural networks (HGNNs), which are :the insufficient adaptation of graph structures during prompt-tuning and the challenges posed by limited labeled data. To mitigate these issues, the authors derived the generalization error bound for existing prompt tuning-based methods, and then proposed a unified framework that combines two new adapters with potential labeled data extension to improve the generalization of pre-trained HGNN models.This novel approach aims to improve the generalization capabilities of pre-trained HGNNs across various downstream tasks.

Contributions 
+ Designing dual structure-aware adapters to capture task-related homogeneous and heterogeneous structural information. Moreover, we design a label-propagated contrastive loss and two self-supervised losses to achieve the potential labeled data extension.
+ Deriving a unified generalization error bound for existing methods based on the training error and the generalization gap. Moreover, we demonstrate that the proposed method achieves a lower generalization error bound than existing prompt-tuning-based methods to improve the generalization ability of pre-trained HGNN models.
+ Validating the superior effectiveness and generalization of the proposed HG Adapter compared to state-of-the-art fine-tuning-based and prompt-tuning-based methods, demonstrating its adaptability to different pre-trained HGNN models by experiments.

Merits
+ Significant shortcomings in existing prompt-tuning approaches were pointed clearly and accurately in this paper , such as the neglect of graph structures and the constraints posed by limited labeled data.
+ Solid theoretical foundation for the proposed framework was provided for the proposed framework in the generalization error bound. And methods are proven and discussed mathematically.  
+  The introduction of dual structure-aware adapters is a noteworthy contribution, as it allows for the adaptive integration of task-related structural information from both homogeneous and heterogeneous graphs.
+ Experiments are comprehensive enough to demonstrate the effectiveness and generalization of the proposed method across different tasks add credibility to the claims made.

Weaknesses:
+ The paper could benefit from clearer explanations of key concepts, particularly around the implementation of the dual structure-aware adapters and the label-propagated contrastive loss.
+ While the empirical results show improvements over existing methods, a more detailed comparative analysis with specific baselines would enhance the reader's understanding of the method's relative performance.
+ The paper would be stronger with a more explicit discussion of the limitations of the proposed method, particularly in relation to scenarios with highly variable graph structures or the quality of unlabeled data.
+  It might be recommendable to talk about future work considerations to make background and trend of the overall research clear.

### Strengths
See Summary

### Weaknesses
The paper could benefit from clearer explanations of key concepts, particularly around the implementation of the dual structure-aware adapters and the label-propagated contrastive loss.

While the empirical results show improvements over existing methods, a more detailed comparative analysis with specific baselines would enhance the reader's understanding of the method's relative performance.

The paper would be stronger with a more explicit discussion of the limitations of the proposed method, particularly in relation to scenarios with highly variable graph structures or the quality of unlabeled data.

It might be recommendable to talk about future work considerations to make background and trend of the overall research clear.

### Questions
See Summary

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper "HG-Adapter: Improving Pre-Trained Heterogeneous Graph Neural Networks with Dual Adapters" introduces a new framework to enhance the generalization of pre-trained heterogeneous graph neural networks (HGNNs). It addresses two key challenges: insufficient focus on graph structures during tuning and a lack of labeled data, leading to a generalization gap. The proposed HG-Adapter employs dual adapters to capture both homogeneous and heterogeneous graph patterns, improving task-specific performance. It also incorporates a label-propagated contrastive loss and self-supervised learning to utilize unlabeled data, effectively expanding the labeled dataset. This helps reduce the generalization error between training and testing phases.

### Strengths
1. The paper introduces a novel approach by using dual adapters to capture both homogeneous and heterogeneous graph structures. This allows for better adaptation to specific graph patterns, improving the model’s generalization capabilities across diverse downstream tasks.

2. By incorporating a label-propagated contrastive loss and self-supervised learning, the paper effectively leverages unlabeled data to extend the training dataset. This approach helps overcome the limitation of scarce labeled data, which is a common challenge in heterogeneous graph neural network applications.

3. The paper provides a solid theoretical foundation by deriving generalization error bounds for prompt-tuning methods. Additionally, it validates the proposed HG-Adapter through extensive experiments, demonstrating superior performance compared to state-of-the-art fine-tuning and prompt-tuning techniques across multiple datasets.

### Weaknesses
1. While the proposed HG-Adapter framework is innovative, its dual adapter system and the integration of multiple losses (label-propagated contrastive loss and self-supervised learning) might make the model computationally expensive and challenging to implement in real-world settings with limited resources. Specifically, the computational overhead of maintaining separate adapters for homogeneous and heterogeneous graph patterns, along with the additional forward and backward passes required for the contrastive and self-supervised losses, could lead to significant increases in training time and memory consumption. This is particularly concerning when dealing with large-scale graphs where computational efficiency is paramount.

2. The experiments in the paper, while comprehensive, may be limited in the diversity of graph types evaluated. A more extensive validation across different types of heterogeneous graphs, particularly in domains beyond those tested (e.g., biological networks, industrial applications), would provide stronger evidence of the model's generalization ability. The current evaluation primarily focuses on academic datasets, which may not fully capture the complexities and nuances of real-world heterogeneous graphs. For example, biological networks often exhibit highly complex relationships and varying node degrees, while industrial applications may involve graphs with specific structural properties that are not present in the tested datasets.

3. Although the framework shows improved performance, its scalability to very large datasets or extremely large graphs is not thoroughly addressed. Given that graph neural networks are often used in scenarios involving large-scale data, the paper could benefit from further analysis on how the model performs with increasing graph size and complexity. The paper lacks a detailed analysis of how the proposed dual adapter system and the associated loss functions scale with the number of nodes and edges in the graph. This is a critical aspect for practical applicability, as many real-world graphs can contain millions or even billions of nodes and edges.

### Questions
please see the weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
