# Learngene Tells You How to Customize: Task-Aware Parameter Prediction at Flexible Scales

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Reducing serving costs and latency is a fundamental challenge for deploying large-scale models in business applications. To cope with this demand, the Learngene framework encapsulates shareable information from large models into a compact unit called a learngene. This unit serves to initialize downstream models, enabling them to inherit the knowledge from the large model efficiently, hopefully diminishing deployment expenses. However, existing learngene methods are constrained by their strong dependence on the architecture of large model and overlook the features of target tasks, resulting in suboptimal adaptability of downstream models to deployment requirements. In this paper, we present Task-Aware Learngene (TAL), a novel method based on graph hypernetworks that predicts model parameters conditioned on desired model scales and task-specific characteristics. Extensive experiments demonstrate that TAL effectively scales model initialization parameters, selectively utilizes shareable information pertinent to target tasks, and consistently outperforms random initialization and existing parameter prediction methods. Furthermore, TAL exhibits promising transfer learning capabilities for unseen tasks, underscoring its effectiveness in condensing large model knowledge while being aware of downstream requirements.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new parameter prediction method based on Graph HyperNetworks (GHNs), called Task-Aware Learngene (TAL). The proposed method aims to address the shortcomings of traditional Learngene methods in adapting to flexible scales and task-specific requirements. By incorporating task-specific information and model scale information, TAL predicts the initial parameters for downstream models, thereby enhancing the efficiency and adaptability of model initialization. Experimental results demonstrate that TAL significantly outperforms existing parameter initialization methods, such as random initialization and LoGAH, across various tasks.

### Strengths
1. TAL utilizes task-specific features and flexible model scaling for parameter prediction, thereby achieving efficient initialization for different tasks, which significantly enhances the adaptability and performance of the model across various downstream tasks.
2. By using Graph HyperNetworks to encode structural information, TAL can generate downstream models of different scales based on requirements, supporting model flexibility and task customization, which is particularly effective in resource-constrained environments.
3. The paper conducted extensive experiments on multiple datasets (e.g., ImageNet-1K and Decathlon) to validate the effectiveness of TAL.

### Weaknesses
1. While the TAL mechanism improves model flexibility and performance, it also significantly increases the computational and resource costs in multi-task scenarios.

2. The comparative experiments in the paper mainly focus on vision tasks, lacking experiments in other domains. Demonstrating similar performance improvements in other fields would enhance the generalizability and persuasiveness of the method.

3. The paper lacks an in-depth discussion on the setting of sampling weights in multi-task training.

4. The method and experiments are inconsitent in motivation. Specifically, the method aims to enhance the expression of gene data, which are more likely to be sequence and graph structure, while the evaluation focus on images that are not corresponds to structure modeling.

5. The core technique is derived from graph hypernetworks directly. However, it lacks of the novel contribution for customize graph hypernetwork for the main task in this work.

### Questions
Q1: Could the authors provide a more detailed analysis of the computational cost of TAL during both the training and inference phases, and compare it to other baseline methods such as LoGAH or Random Initialization? Specifically, how much additional training time and resource consumption does TAL require compared to these methods, and how does this translate into efficiency gains for downstream tasks?

Q2: Can TAL mitigate the inherent conflicts among different tasks?

### Soundness
2

### Presentation
3

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
Existing learngene methods often rely solely on large model architectures, overlooking the specific features of target tasks. This paper introduces a task-aware framework, TAL, which utilizes a graph hypernetwork to predict model parameters while considering both model scale and task-specific information. TAL functions as an end-to-end framework, learning representations and transferring shared knowledge to enable effective parameter initialization. Empirical results show that TAL effectively predicts parameters, with the predicted parameters providing a stronger initialization than previous methods.

### Strengths
**Originality:** The authors propose a novel task-aware parameter prediction framework that effectively integrates task-specific information, enabling the predicted parameters to serve as a more effective initialization point.

**Quality:** The experimental results need a better structure to clearly demonstrate the framework’s effectiveness. The heavy use of abbreviations makes the results challenging to read and confuse readers.

**Clarity:** The overall writing of the paper lacks clarity and hard to read, which makes it difficult to understand the proposed approach and its contributions. See below.

### Weaknesses
 **Reducing Serving Cost:** The abstract mentions reducing serving costs and latency, but the experiments lack clarity on how the TAL framework actually predicts a smaller parameter set to create a more compact model, which would reduce serving costs and latency. The paper does not provide a clear evaluation of the model size reduction achieved by TAL, nor does it quantify the resulting decrease in serving costs or latency. This makes it difficult to assess the practical benefits of the proposed approach in real-world deployment scenarios.

**Learngene Concept:** The concept of "learngene" remains unclear and appears insufficiently differentiated from the standard pretraining-then-finetuning approach. The description in the introduction does not fully convey the concept, and even with Figure 1, it is challenging to understand what a "learngene" is. It is unclear how the 'learngene' is extracted from the pretrained model and how it differs from simply using a subset of the pretrained model's parameters. The paper needs to clarify the specific mechanisms for creating and utilizing the 'learngene'.

**Preliminaries:** The background on Graph HyperNetworks (GHN) is unclear. Lines 128–132 seem just a general training process. Besides, GHN is trained on M different architectures and N data samples, but the nature of these training data samples is not explained. The preliminaries section could be improved by clarifying the input and output formats needed to train a GHN and standardizing the notation. Specifically, the paper should detail the structure of the graph used in GHN, including the node and edge features, and how these features are derived from the model architectures. The lack of clarity on the training data for the GHN makes it difficult to reproduce the results.

**Model Scales:** The paper makes a significant claim about handling different model scales in the introduction, but there is little detail or experimental evidence on this. It remains unclear how TAL predicts or adjusts parameters for models of varying scales. The paper should provide a detailed explanation of how the TAL framework adapts to different model sizes, including the specific mechanisms for adjusting the predicted parameters based on the target model scale. The experiments should also explicitly demonstrate the performance of TAL across a range of model sizes, not just a few examples.

**Presentation:** The experimental results need a clearer, more structured presentation. For instance, starting with an overview of the experiments would provide context, followed by details on the setup, datasets, and baselines. Most importantly, each experiment should include an explanation of its objectives and expected outcomes, helping to guide readers through the data. This approach would make it easier to interpret the results and understand how the numbers and tables support the authors' claims. Besides, the abbreviation should be used properly.

### Questions
**Computation Graphs:** The term "Computation Graphs" is introduced but confusing me. Can the authors provide examples?

**Training TAL on a Large Dataset:** It is unclear what a "large dataset" here means. Does this refer to a pretraining dataset containing diverse domains and concepts, or something else?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Authors introduce Task-Aware Learngene (TAL), a framework for predicting model parameters based on task-specific characteristics and desired model scales. TAL is an incremental improvement on top of previous methods like LoGAH and authors demonstrated better results compared to LoGAH in some cases. The motivation for this is to achieve efficient knowledge transfer and adaptability to descendant models of different scales. The paper highlights the importance of high-quality initialization in improving descendant model performance.


---- Replying here as the review period has ended -- Time: Dec 3, 4:15PM PST

Thanks authors for replying to my questions. I have reviewed the answers and gone through other reviewer comments and discussions. I would like to keep my rating primarily because it's still not clear the solid reasoning/ understanding around how  "Task Aware" idea is helping improve representations. More insight into that will definitely help strengthen the paper. Would recommend following up on that in next iteration. Thank you! Good luck

### Strengths
Novelty in terms of proposing task and scale specific initialization: TAL introduces a unique approach for multi-task parameter prediction that adjusts model parameters to specific tasks and scales. The use of task-specific computational graphs in the Learngene module is innovative and contributes a fresh angle to multi-task learning and model initialization.

Broad Applicability/ Significance: TAL’s ability to initialize models for varied tasks and handle models of differing scales suggests it could become a valuable tool in multi-task learning and transfer learning research. It addresses an important problem if solved could lead to massive efficiency wins in efficiently transfering knowledge from foundation models to downstream applications.

Extensive experiments and comparison to LoGAH: Authors have done extensive experiments across multiple tasks and shown improvements compared to LoGAH versions. The low dimensional representation of computation graphs generated by TAL for various tasks are quite interesting.

### Weaknesses
Limited contribution: It does look like a minor incremental work over existing hypernetwork methods GHN-2, LoGAH where in the main different is adding task-specific layers/information. It is also not very clear from the paper what is the specific "task-specific" information that is added to the learngene that helps improve the downstream model performance. 

Explanation of results/experiments: Table 2 and Table 3 has lot of experiments comparing TAL with LoGAH and showing several cases of improvements. The improvements range from slight to large improvements and in some cases negative improvements. Authors can dig deeper into what's the underlying reasoning behind this improvement/regressions. 

Shallow Analysis of Catastrophic Forgetting: The paper mentions TAL addresses catastrophic forgetting, but it lacks specific experiments or metrics to evaluate this claim. There is little evidence showing that TAL explicitly mitigates forgetting across tasks in sequential or continual learning contexts.

### Questions
More details around the TSL and Task HyperNet layers. What's the specific input to this? How does this help achieve better representation of the computation graph, etc. In cases where the downstream multi task performance regressed, what might have caused this to happen. Adding discussions around these can further strengthen the paper. Looking forward to hear back from authors around these topics.

### Soundness
3

### Presentation
2

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
This paper introduces an approach to address the cost and complexity of deploying large-scale models for various downstream tasks by creating a framework called Task-Aware Learngene (TAL). TAL builds on the learngene concept, which encapsulates transferable information from a large model into a compact, reusable unit. Unlike previous methods, TAL utilizes graph hypernetworks to predict model parameters that are both task-aware and scalable, thus enabling models to inherit large model knowledge with better adaptability and lower deployment costs. Through experiments, TAL shows good performance in initializing models compared to traditional methods like LoGAH, demonstrating improved accuracy across various datasets, quicker convergence, and adaptability to unseen tasks.

### Strengths
TAL provides a cost-effective means to transfer knowledge by creating a compact learngene unit, making it easier to deploy models with limited resources. 
The task-specific customization through TAL’s graph hypernetwork enables the model to adapt to different downstream tasks, outperforming existing methods by a margin on unseen tasks.
TAL supports flexibility in model scaling, allowing the adjustment of model parameters based on specific task requirements. This scalability is particularly valuable for application scenarios.
TAL's initialization outperforms other methods like LoGAH across datasets, as evidenced by experiments showing TAL’s capability to provide higher-quality initialization parameters.

### Weaknesses
 Overall, I personally like the idea of model customization with dynamic architectures and task-specific parameters. I have some concerns mainly regarding the experiments part.

The related works need improvement. Clearly stating the differences and contributions make the paper review evaluation better.

The baselines are limited. Comparing the latest one is good but diverse baselines from different aspects make the results stronger.

The datasets can be somewhat out-of-dated. Considering using challenging datasets would make the results and conclusions stronger, especially in an era of foundation models.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
