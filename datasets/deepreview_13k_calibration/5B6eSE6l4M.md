# Performance Heterogeneity in Message-Passing and Transformer-based Graph Neural Networks

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 5, 3, 1

## Abstract
Graph Neural Networks have emerged as the most popular architecture for graph-level learning, including graph classification and regression tasks, which frequently arise in areas such as biochemistry and drug discovery. Achieving good performance in practice requires careful model design. Due to gaps in our understanding of the relationship between model and data characteristics, this often requires manual architecture and hyperparameter tuning. This is particularly pronounced in graph-level tasks, due to much higher variation in the input data than in node-level tasks. To work towards closing these gaps, we begin with a systematic analysis of individual performance in graph-level tasks. Our results establish significant performance heterogeneity in both message-passing and transformer-based architectures. We then investigate the interplay of model and data characteristics as drivers of the observed heterogeneity. Our results suggest that graph topology alone cannot explain heterogeneity. Using the Tree Mover’s Distance, which jointly evaluates topological and feature information, we establish a link between class-distance ratios and performance heterogeneity in graph classification. These insights motivate model and data preprocessing choices that account for heterogeneity between graphs. We propose a selective rewiring approach, which only targets graphs whose individual performance benefits from rewiring. We further show that the optimal network depth depends on the graph’s spectrum, which motivates a heuristic for choosing the number of GNN layers. Our experiments  demonstrate the utility of both design choices in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the performance heterogeneity of message-passing and transformer-based architectures in graph-level tasks. Unlike previous studies that focused on node-level tasks, the authors find that graph topology alone does not fully explain heterogeneity. Instead, they establish a connection between class-distance ratios and performance heterogeneity using the Tree Mover's Distance. Building on these observations, the authors propose a selective rewiring approach and a heuristic for determining optimal GNN depths.

### Strengths
- Performance heterogeneity is a well-recognized and valuable research problem in graph learning.
- The proposed selective rewiring approach is promising for addressing performance heterogeneity in graph-level tasks.
- The observation that optimal network depth depends on the graph’s spectrum is intriguing, and the subsequent heuristic method for selecting the number of GNN layers is validated by the experimental results.

### Weaknesses
 - The generalization capability of the proposed selective rewiring approach remains uncertain. While the motivation for this approach is empirically driven, the observations may be biased by the specific graph datasets tested. Would the conclusions hold on challenging open-source benchmarks, such as large-scale datasets in OGB (e.g., ogbg-ppa and ogbg-code2)?
- Given the proposed solutions, how can they be applied to new graph scenarios? For new graph datasets, is there a confidence measure for selective rewiring or heuristic GNN depth prediction?

### Questions
This work addresses an important yet challenging research topic in the graph field. I appreciate the focus on identifying performance heterogeneity in graph-level tasks. However, my primary concern is ensuring the proposed solution’s generalizability. For further details, please refer to the Weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper delves into the phenomenon of performance heterogeneity in graph-level learning, emphasizing how variations in graph topology influence model effectiveness across various architectures. Central to the study is the introduction of heterogeneity profiles, a novel analytical tool designed to systematically evaluate performance disparities across graph-level tasks. These profiles reveal that performance heterogeneity is shaped by factors beyond mere topological characteristics. Building on the analysis of heterogeneity profiles, the research progresses by proposing a selective rewiring strategy. This strategy aims to optimize network architecture based on the spectral properties of graphs, positing that aligning these properties can mitigate the need for extensive hyperparameter tuning by standardizing the optimal depth of GNN layers across different datasets.

### Strengths
1. The introduction of heterogeneity profiles as a tool in graph-level learning to analyze performance across graphs provides a new methodological avenue for studying GNNs.

2. The selective rewiring approach offers a pragmatic solution to a common problem in GNN deployment, potentially simplifying the model training process.

3. The experiments are well-designed, covering multiple datasets and configurations.

### Weaknesses
1. The paper does not provide a detailed description of how hyperparameters were tuned, only presenting the final hyperparameter results. Different hyperparameter settings, including adjustments to hidden dimensions, dropout rates, activation functions, and normalization techniques, could provide a stronger, more robust set of results. Specifically, the lack of detail regarding the search space for each hyperparameter and the optimization strategy (e.g., random search, grid search, Bayesian optimization) makes it difficult to assess the thoroughness of the experimental setup. The absence of ablation studies on these hyperparameters further weakens the analysis, as it remains unclear how sensitive the results are to specific choices.

2. The study lacks a detailed comparison with other state-of-the-art methods that aim to address similar challenges in GNNs. While the paper proposes innovative strategies for improving graph-level task performance, such as selective rewiring and optimized network depth based on heterogeneity profiles, it lacks empirical evidence showing that these approaches achieve state-of-the-art results on 1 or 2 benchmark datasets. This omission could undermine the perceived effectiveness and practical relevance of the proposed methods. The paper should include a comparison against established methods that also focus on graph-level learning, such as those that use attention mechanisms or other advanced architectures, to properly contextualize the performance of the proposed approach.

3. The datasets used in the study are relatively small in scale. Incorporating results from more extensive and challenging datasets, such as those from the OGB, would strengthen the validation of the techniques and enhance the paper’s impact. The current datasets may not fully capture the complexities and variations present in real-world graph data, which could limit the generalizability of the findings. Testing on larger datasets with more diverse graph structures would provide a more rigorous evaluation of the proposed methods.

### Questions
1. How might different settings for parameters affect the conclusions drawn from the study?

2. In line 298, these 'difficult' graphs are nearly identical for GIN and GraphGPS. Given that Figure 3 provides quantitative metrics but does not specify which exact graphs are considered "difficult" across both architectures, could the authors clarify how they determined that the same graphs pose difficulties for both GIN and GraphGPS?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates performance heterogeneity in graph neural networks (GNNs), specifically focusing on message-passing (MPGNNs) and transformer-based architectures. It addresses the challenges in understanding model performance variation on individual graphs within datasets used for graph-level learning. To capture performance variations, the authors introduce heterogeneity profiles and leverage the Tree Mover’s Distance (TMD) to demonstrate that both topological and feature information influence performance heterogeneity. The study explores how class-distance ratios, graph rewiring, and network depth impact heterogeneity, proposing a selective rewiring method and a depth-selection heuristic based on spectral alignment. The experiments validate these techniques, showing improved performance on multiple benchmarks.

### Strengths
- I think the attempted research question is fundamental and important for advancing GNN

- I do like the overall approach which is systematic

### Weaknesses
 - My main concerns with respect to this paper are the contribution and novelty of the methodology and results. More specifically,

a. There is certainly merit in investigating the impact factors for the performance of GNN and I do like a more systematic approach. However, given the fact that GNN can be viewed as a function with the input of both structure and feature, it seems obvious that both feature and structure would affect the output/performance of GNNs. With this said, I am not convinced and not comfortable with the claim that topology is enough to explain node-level tasks (see [1] for an example).

b. One of the claimed contribution is the so-called "heterogeneity profiles". I do not see a detailed introduction or discussion on this technique and why it is novel. Based on the description on Section 3, it seems a standard random experiments/k-fold validation. Please correct me if I am wrong

c. The claimed research question investigates the factors that explain performance heterogeneity. However, the explained framework (tree mover distance) used in the paper is directly adopted from another paper. What is the new insight provided in this paper? In addition, there are many other distance metric such as FID can combine structure and feature. Why not consider those?

d. The paper tries to connect the experimental insight with graph rewiring and over-smoothing. The papers try to connect over-smoothing with the diffusion property of graph structure (fiddle eigenvalue of graph matrix). Despite being somewhat intuitive, it is not a strong explanation for over-smoothing as it is not clear how the diffusive property of graph structure would affect training or generalization. In addition, I think this diffusive property would largely affect node-level tasks. It is not entirely clear to me why this concept is applicable for graph-level tasks. Please explain. While I do think that selective graph rewiring could be a highlight of the paper, the paper does not go into detail in this regard. For example, how do you use the empirical result/theoretical result to obtain the proposed criteria for the selection?

- the presentation and organization of the paper need to be improved. I think the paper right now attempts to connect too many concepts and methods (performance heterogeneity, over-smoothing, graph rewiring e.t.c). I do admire the ambitious goal. However, in the current version of the paper, the connections among these concepts and methods are presented in a rather superficial way (this might be because of the page limit). I do encourage the authors to dive deeper into these connections as they are important for advancing GNN.


### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper investigates the performance variability of GNNs in graph-level tasks.

### Strengths
Identifying the reasons behind the high variance in performance across different models is crucial; however, this work fails to offer new insights into this issue.

### Weaknesses
1. The paper highlights the variance in GNN performance on graph-level tasks; however, I believe this contribution does not offer new insights to the community. It is already well-established that Graph Neural Networks (GNNs) exhibit performance inconsistencies and that the effectiveness of different models often varies across datasets [1, 2].
Furthermore, the paper fails to propose a concrete solution to address this phenomenon. Inconsistencies in evaluation across sections further undermine its findings, as I will elaborate in my next comment.

2.
The authors investigate the inconsistency of performance on graph-level tasks by examining a range of models and datasets. However, the presentation lacks clarity regarding the consistency of their selections. For instance, in Section 3.2, three datasets are analyzed using two GNN architectures—specifically, GCN and GraphGPS. In contrast, Section 3.3 shifts to the Mutag dataset and the GIN model, raising questions about why different datasets and models were chosen for these sections.
Given that the paper's primary contribution aims to highlight an empirical phenomenon, I believe a more comprehensive evaluation is warranted, one that encompasses a broader array of benchmarks and various GNN architectures. Notably, the Mutag and Proteins datasets are recognized for their instability, as documented in previous studies [1]. The MUTAG dataset, in particular, is small and characterized by high variance, which has led to its declining usage in recent research.
Additionally, in Section 4, GPS is not tested at all; instead, GAT is utilized, despite all sections focusing on the same claim of heterogeneity in results. This inconsistency in model evaluation detracts from the paper’s coherence and impact.
The evaluation graph transformers focus solely on one type of graph transformer, GraphGPS, which is inadequate to substantiate the claim that “Our analysis suggests that both message-passing and transformer-based GNNs display performance heterogeneity in classification and regression tasks” (line 102). There exists a diverse range of graph transformers, as highlighted in studies such as [3, 4], which should be considered to strengthen the analysis.

3. The paper suffers from poor writing, featuring numerous grammatical errors and incomplete sentences. For instance, refer to lines 250, 352, 168, 576, and 187. Additionally, some sentences lack clear connections to the surrounding text, such as the statement: "Size generalization in GNNs has been studied in (Yehudai et al., 2021; Maskey et al., 2022; Le & Jegelka, 2024)."
The overall quality of English in the paper is inadequate and unprofessional, significantly detracting from the clarity and credibility of the research.

8. Overall, I find it difficult to see how the content of the paper supports the claims made in the abstract.

### Questions
1. Can you explain the rationale behind the differing datasets and models used in Sections 3.2, 3.3. and 4?
2. While the paper highlights performance inconsistencies in GNNs, it does not present any concrete solutions to address this issue. What are your thoughts on proposing methodologies or frameworks to mitigate these inconsistencies in future work?

### Soundness
1

### Presentation
1

### Contribution
1
