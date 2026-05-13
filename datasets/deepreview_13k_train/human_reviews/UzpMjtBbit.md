# DynamicRTL: RTL Representation Learning for Dynamic Circuit Behavior

- Decision: Reject
- Scores: 5, 6, 3, 3, 6

## Abstract
There is a growing body of work on using Graph Neural Networks (GNNs) to learn representations of circuits, focusing primarily on their static characteristics. However, these models fail to capture critical runtime behavior, which is crucial for tasks like hardware verification and optimization. To address this limitation, we introduce DynamicRTL, a novel GNN-based approach that learns circuit representations by incorporating both static structures and multi-cycle execution behaviors. DynamicRTL leverages an operation-level Control Data Flow Graph (CDFG) to represent Register Transfer Level (RTL) circuits, enabling the model to capture dynamic dependencies and runtime execution. To train and evaluate DynamicRTL, we built the first comprehensive dynamic circuit dataset, comprising over 6,300 Verilog modules and 190,000 simulation traces. Our results demonstrate that DynamicRTL consistently outperforms existing models in branch prediction tasks. Furthermore, its learned representations transfer effectively to related tasks, achieving strong performance in assertion prediction and underscoring its transfer learning capabilities for dynamic circuit tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces DynamicRTL, a novel approach for learning representations of digital circuit behavior that incorporates both static structure and dynamic (runtime) execution characteristics. The proposed work has the following contributions:
1. First Comprehensive Dynamic Circuit Dataset
2. Novel Graph Neural Network Architecture (DR-GNN)
3. Extensive experiments show the effectiveness of proposed method

Overall, this work represents a significant step forward in applying machine learning to hardware design and verification, particularly in understanding how circuits behave during execution rather than just their static characteristics. This could have important applications in hardware verification, optimization, and electronic design automation.

### Strengths
1. This is the first work to create a comprehensive dataset for dynamic circuit behavior.
2. Extensive experiments demonstrate the effectiveness of proposed method.
3. Novel technical approach combining operation-level CDFG with circuit-aware GNN propagation

### Weaknesses
1.  The focuses of proposed work primarily on branch prediction as the main indicator of dynamic behavior. How about other aspects of circuit dynamics such as timing, power consumption, or glitch behavior.
2. It will be better if the authors have some discussion on the limitation of proposed method, especially the effectiveness and efficiency of proposed method for large-scale circuits.

### Questions
Please check weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on improving upon the current state of GNNs for circuit design that depend on the static data of circuits by including dynamic behaviors. The paper creates a large dataset with various designs and simulation traces, then build a dynamic RTL GNN model that is built on the circuit operation-level graph. The paper shows the effectiveness of this representation on branch prediction, then shows that this can be transferred to assertion prediction task.

The paper seems to improve by exploring an underexplored dimension of dynamism in circuit-GNNs. The paper is well organized and shows that it can perform well on a given task + transferred to a downstream task that hints the effectiveness of this new representation and of adding dynamism to the circuit-GNNs.

### Strengths
The paper seems to improve by exploring an underexplored dimension of dynamism in circuit-GNNs. The paper is well organized and shows that it can perform well on a given task + transferred to a downstream task that hints the effectiveness of this new representation and of adding dynamism to the circuit-GNNs.

### Weaknesses
The task that was used seems to be too simple to say that it is effective. Seems like the tasks are simply binary classification tasks which is not sufficient.



### Questions
* Can you provide more details about the test set for the two tasks? For example, size of the dataset, is it balanced, ... Without that information, it is possible for the data to be biased.

* It seems that the number of nodes in the circuit are too small. How does this scale for much larger ones? At what point does the accuracy drop significantly for table 2.

* How is the speed of inference and training?

* For the two tasks, how does it compare to human evaluation or any pre-existing programs?

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
The authors propose a representation learning approach for RTL descriptions of circuits. Unlike prior works that generally learns the static structure of the circuits, this work is capable to cover the dynamic execution features of circuits which change with inputs and circuit states. Specifically, as  the circuit’s functionality is embedded in the attributes of the nodes and their connectivity, the authors model the RTL as an operational-level CDFG and apply GNNs to learn circuit representations. Notably, because some operator nodes in circuits are non-commutative (e.g., subtraction), the authors parameterize the weights of the heterogeneous attention based on different operation types and node positions, enabling effective aggregation of different circuit operations. Finally, the authors verify the proposed GNN model with two downstream tasks.

### Strengths
- This work targets at representation of circuits with dynamic behaviors for the first time.

- This work addresses the over-smoothing problem encountered in the GNN model.

- This work also builds a benchmark for dynamic circuit modeling.

### Weaknesses
1) The dynamic characters of the circuit mentioned in this work mainly include branch and multi-cycle execution. Do they cover all the dynamic features appropriately? It needs to be defined more clearly and formally. For instance, there are many iterative algorithms such as equation solvers implemented with hardware, but the number of iterations depends on the amount of the error and it affects the runtime and power consumption of the circuit substantially. Can it be estimated given the initial inputs using the proposed GNN model?  

2) The experiments are relatively weak. The basic goal of representation of circuits with dynamic characteristics is PPA estimation, but it is not mentioned nor compared to prior works. The proposed downstream tasks are not quite typical tasks. In addition, the circuits used by the authors (with node counts ranging from 10 to 500) are too small which is insufficient to validate the proposed approach.

### Questions
See the weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces DR-GNN, a GNN-based model for learning circuit representations via incorporating dynamic information. Specifically,  DR-GNN integrates static structures with multi-cycle execution dynamics using a Control Data Flow Graph (CDFG) representation of RTL circuits. Trained on a newly developed dataset of over 6,300 Verilog modules and 190,000 simulation traces, DR-GNN achieves promising results on branch prediction tasks compared to conventional GNN models. Additionally, it demonstrates transferability to related tasks like assertion prediction.

### Strengths
- Overall, the paper is well written. All technical steps are easy to follow.
- Learning dynamic circuit representation is both an interesting and important problem.

### Weaknesses
 - Limited Novelty: As the authors noted, the proposed model architecture is largely based on the Heterogeneous Graph Transformer [1], and the use of GRU has also been explored in numerous prior works (e.g., [2]). Therefore, I regret to say that the novelty of this work is insufficient.
- Missing Stronger and More Relevant Baselines: Several recent circuit representation learning methods (e.g., [3-5]) are omitted from the experiments. Notably, [3] also proposes learning different aggregation functions for different node types. Comparing only with basic GNNs like GCN does not fully convince me of the proposed approach's effectiveness.
- Unconvincing Claims: While the authors claim that DR-GNN overcomes the over-smoothing issue, Figure 4 shows a significant drop in accuracy with 30 layers. Additionally, there are numerous prior works addressing over-smoothing [6], yet they are discussed without comparison in this study.
- Limited Reproducibility: The manuscript lacks detailed hyperparameter settings for DR-GNN and baseline GNNs, making it unclear how hyperparameters were tuned. More importantly, since the source code and generated circuit dataset are not provided, it is nearly impossible to reproduce the results presented in this work.

### Questions
- It appears the authors split the circuit dataset into only training and test sets, with no validation set. How was hyperparameter tuning performed in this case?
- What is the variance in accuracy scores reported in Tables 1 and 3?
- How does the model’s accuracy vary across circuit designs with different depths (in contrast to different sizes in Table 2)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The DynamicRTL paper introduces a Graph Neural Network model that captures dynamic behaviors in RTL circuits. Unlike traditional models that focus on static structures, DynamicRTL uses Control Data Flow Graphs (CDFGs) to incorporate both static and dynamic data, enabling more accurate branch execution and assertion predictions. The model achieves good accuracy in branch prediction and demonstrates strong transfer learning potential for tasks like assertion prediction. DynamicRTL offers insights for hardware verification and optimization, setting a new standard for understanding dynamic circuit behaviors.

### Strengths
The DynamicRTL paper introduces an approach that combines static and dynamic circuit information. The model delivers results that outperforming other methods in tasks like branch prediction and assertion prediction, while also contributing a dynamic circuit dataset. The paper is clear in its presentation, offering explanation of the CDFG construction and the DR-GNN model’s architecture. Lastly, DynamicRTL tackles a significant problems for the evolving field of hardware design and electronic design automation (EDA).

### Weaknesses
The weaknesses of the DynamicRTL paper are:
it relies heavily on existing GNN methods and concepts like CDFGs, making it less groundbreaking in terms of underlying technology. 
The model’s generalizability to other circuit types or levels, such as netlists, remains unexplored, and its performance on larger or more complex circuits could be tested more rigorously. 
Additionally, the paper’s significance is limited, as it primarily targets RTL-level circuits, restricting its applicability to broader hardware contexts or higher abstraction levels, such as layout optimization tasks.

### Questions
The paper would benefit from including a brief mention of the results in the abstract to give readers a clearer overview of its performance. Additionally, it would be useful to know how the proposed design compares with existing commercial tools in terms of efficiency and accuracy. Finally, more details on how input sequences are selected for testing would be helpful to understand the robustness of the model in different scenarios.

### Soundness
2

### Presentation
2

### Contribution
2
