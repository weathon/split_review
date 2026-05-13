# A Graph Enhanced Symbolic Discovery Framework For Efficient Circuit Synthesis

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
The efficiency of Circuit Synthesis (CS) has become one of the key bottlenecks in chip design. To prompt efficient CS, previous studies propose using a key scoring function to predict and prune a large number of ineffective nodes of the CS heuristics. 
However, the existing scoring functions struggle to balance inference efficiency, interpretability, and
generalization performance, which severely hinders their application to modern CS tools. To address this challenge, we propose a novel data-driven circuit symbolic learning framework, namely CMO, to learn lightweight, interpretable, and generalizable scoring functions.
The major challenge of developing CMO is to discover symbolic functions that can well generalize to unseen circuits, i.e., the circuit symbolic generalization problem. Thus, the major technical contribution of CMO is the novel $\textit{Graph Enhanced Symbolic Discovery} $ framework, which distills dark knowledge from a well-designed graph neural network (GNN) to enhance the generalization capability of the learned symbolic functions. To the best of our knowledge, CMO is $\textit{the first}$ graph-enhanced approach for discovering lightweight and interpretable symbolic functions that can well generalize to unseen circuits in CS. Experiments on three challenging circuit benchmarks show that the $\textit{interpretable}$ symbolic functions learned by CMO outperform previous state-of-the-art (SOTA) GPU-based and human-designed approaches in terms of $\textit{inference efficiency}$ and $\textit{generalization capability}$. Moreover, we integrate CMO with the Mfs2 heuristic---one of the most time-consuming CS heuristics. 
The empirical results demonstrate that CMO significantly improves its efficiency while keeping comparable optimization performance when executed on a CPU-based machine, achieving up to 2.5$\times$ faster runtime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This authors propose a novel data-driven circuit symbolic learning framework, CMO. It learns a symbolic scoring function balancing inference efficiency, interpretability, and generalization performance. While existing approaches often struggle with these trade-offs in modern circuit synthesis (CS) tools, CMO demonstrates superior capability in discovering lightweight and interpretable symbolic functions from a decomposed symbolic space. The major technical contribution of CMO is the Graph Enhanced Symbolic Discovery (GESD) framework, which employs a specially designed Graph Neural Network (GNN) to guide the generation of symbolic trees. CMO is the first graph-enhanced approach for discovering lightweight and interpretable symbolic functions that effectively generalize to unseen circuits in CS.

### Strengths
1. Overall, the proposed work is well-structured with a profound related work.
2. This paper proposes a novel circuit symbolic learning framework to learn efficient, interpretable, and generalizable symbolic functions that are reliable and simple to deploy in modern CS tools.
3. CMO is the first graph-enhanced approach for discovering lightweight and interpretable symbolic functions that can well generalize to unseen circuits in CS.  
4. Extensive experimental results show the effectiveness of the proposed CMO over existing works.

### Weaknesses
The link between the two methods in sections 4.1 and 4.2 needs to be further elucidated, and it is not currently possible to visualize in the text the specific interrelationships between the two methods. For example, what is the role of si in section 4.1 in section 4.2 and what is the flow of the calculations for si.

### Questions
Please check weakness

### Soundness
4

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
This paper studies the problem of circuit synthesis (CS) via graph-based methods that can generalize to unseen circuits. The proposed method, CMO, combines symbolic function learning with Graph Neural Networks.

### Strengths
1. The paper is well-written with good introduction to the domain especially for ML-audience less familiar with hardware design.
2. Choice of benchmarks and state-the-art heuristics seem to be solid with comprehensive evaluation.
3. The proposed method achieves significant speedup while maintaining optimization performance on real circuits.

### Weaknesses
1. Theoretical justification and analysis are lacking – It seems combining GNN, MCTS, symbolic learning etc. leads to better results on these CS benchmarks, yet some deeper explanation and analysis can be provided to make the paper stronger. Specifically, the paper does not sufficiently explain why this particular combination of methods is effective, nor does it provide a theoretical framework that justifies the observed performance gains. For instance, how does the inductive bias of the GNN interact with the search strategy of MCTS and the generalization of symbolic learning? A more rigorous analysis is needed to understand the underlying mechanisms.
2. Some of the writings can be improved, e.g. “However, this approach cannot capture effective information from specific circuit distribution for higher generalization performance” – Is it due to the human-designed nature and lack of adoption of machine learning from existing data? This statement is vague and could be clarified by explicitly stating the limitations of human-designed heuristics in capturing complex circuit distributions, and how machine learning can address these limitations by learning from data. The paper should elaborate on the specific aspects of circuit distributions that are difficult for human-designed methods to capture, and how the proposed method overcomes these challenges.
3. Some technical errors, e.g. “Specifically, we use mean absolute error and focal loss” yet the equation (4) is an MSE loss. This discrepancy between the text and the equation introduces confusion. It is important to ensure consistency in the description of the loss function used. The paper should also clarify why a specific loss function is chosen over other alternatives and justify the choice.
4. More circuit dataset descriptions, e.g. graph sizes, and graph visualizations would provide a more solid background for ML audience. The paper lacks sufficient details about the circuit datasets used, including the distribution of graph sizes, the complexity of the circuits, and the specific characteristics of the graphs. Visualizations of the circuit graphs would also be helpful for the ML audience to understand the structure of the data and the challenges of the task. The paper should provide statistical details such as the number of nodes, edges, and depth of the graphs, as well as visualizations of representative circuits.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method called CMO to develop lightweight and generalizable scoring functions for ranking nodes in an AIG, aiming to enhance the efficiency and performance of logic optimization. The method is clearly introduced. The paper trains a GNN and uses an MCTS-based symbolic regression method to generate symbolic scoring functions, ensuring both inference efficiency and generalization. However, some experimental details remain unclear.

### Strengths
The method is clearly introduced, with comprehensive experiments demonstrating the effectiveness and performance of CMO.

### Weaknesses
### Topic
The term "circuit synthesis" is not well-defined in the field of EDA, which may cause confusion. Based on the related works and experiments, this paper appears to focus on logic optimization. The distinction between these terms is crucial; circuit synthesis typically encompasses a broader range of tasks, including high-level synthesis and technology mapping, while logic optimization specifically deals with the manipulation of Boolean logic representations. The paper's use of "circuit synthesis" could mislead readers into thinking the scope is wider than it actually is.

### Datasets
The labels of circuit datasets should be clarified. When mentioning node-level transformation, does it mean it is effective for the current step of logic optimization or for overall performance? Effectiveness in the current step may not translate to overall performance in logic optimization. The paper needs to specify if the labels indicate immediate local improvement (e.g., reduction in node count within a small subgraph) or if they are correlated with the final optimized circuit's quality. Furthermore, the method used to determine the effectiveness of a node-level transformation needs to be explicitly defined. Is it based on a heuristic, or is it an oracle-based approach?

### Experiments
The experiment part is somewhat confusing. The focus of logic optimization should be on time cost and node reduction during the online phase. The offline phase appears more like an ablation study. Experiments on generalization should be highlighted in the main part of the manuscript. Experiment 4 should showcase generalization compared to other baselines like COG, but why other SR methods? Is this an ablation study of the SR method used? The paper needs to clarify the purpose of each experiment and how it contributes to the overall claim. The distinction between offline and online phases should be made clearer, and the metrics used in each phase should be explicitly stated. The choice of baselines for comparison also needs to be justified, especially why other symbolic regression (SR) methods are included in Experiment 4 instead of more relevant logic optimization baselines.

### Generalization
EPFL, IWLS, and an industrial-level dataset from Huawei HiSilicon are used to train the GNN. Are the datasets mixed to train a single GNN, or are three separate GNNs trained for each dataset? The paper should clearly state the training methodology, including whether the datasets are used in a mixed or separate manner. If separate GNNs are trained, the paper should specify the rationale behind this choice and how it impacts the generalization claims. If the datasets are mixed, the paper should explain how the different characteristics of each dataset are addressed during training.

### Questions
1. Can CMO generalize to other logic optimization methods like Rewrite?
2. Can a GNN trained on one dataset generalize to another dataset?
3. How are the training dataset labels obtained?
4. The presentation of experiments is confusing. Please clarify which is the main experiment and which are ablation studies.

### Soundness
3

### Presentation
2

### Contribution
2
