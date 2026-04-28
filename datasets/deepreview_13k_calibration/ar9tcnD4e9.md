# Automatic Organization of Neural Modules for Enhanced Collaboration in Neural Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
This work proposes a new perspective on the structure of Neural Networks (NNs). Traditional Neural Networks are typically tree-like structures for convenience, which can be predefined or learned by NAS methods. However, such a structure can not facilitate communications between nodes at the same level or signal transmissions to previous levels. These defects prevent effective collaboration, restricting the capabilities of neural networks. It is well-acknowledged that the biological neural system contains billions of neural units. Their connections are far more complicated than the current NN structure. To enhance the representational ability of neural networks, existing works try to increase the depth of the neural network and introduce more parameters. However, they all have limitations with constrained parameters. In this work, we introduce a synchronous graph-based structure to establish a novel way of organizing the neural units: the Neural Modules. This framework allows any nodes to communicate with each other and encourages neural units to work collectively, demonstrating a departure from the conventional constrained paradigm. Such a structure also provides more candidates for the NAS methods. Furthermore, we also propose an elegant regularization method to organize neural units into multiple independent, balanced neural modules systematically. This would be convenient for handling these neural modules in parallel. Compared to traditional NNs, our method unlocks the potential of NNs from tree-like structures to general graphs and makes NNs be optimized in an almost complete set. Our approach proves adaptable to diverse tasks, offering compatibility across various scenarios. Quantitative experimental results substantiate the potential of our structure, indicating the improvement of NNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the idea of replacing feed-forward neural networks with densely connected networks of neural-units that allow all-to-all communication. It also defines the idea of a "Neural Module", a locally connected subgraph is such all-to-all networks.

### Strengths
This paper does a good job of introducing and motivating the idea of graph-based neural networks and Neural Modules. Presentation of results on multiple datasets helps gain confidence in the ability for this idea to positively impact current research. The work opens up new avenues of research in the fundamental design of neural networks.

### Weaknesses
The paper is missing certain details about the method - such as what algorithm is used to solve the set of simultaneous equations in the forward process, and how neural-modules are identified and factorized.

The paper mentions ability of a neural-graph $\mathcal{G}$ to be separated into Neural Modules for faster computation by allowing parallel computation, but the method for such factorization or parallel computation is never presented. This I believe is the most important detail that this paper should provide as it allows the realization of neural modules effectively making such general neural-graphs computationally feasible.

It is unclear as to how the introduction of regularization in the forward process (Eqn. 6) directly achieves promotion of sparsity in the network. Typically, such regularization is done in the optimization step after computing the gradients (eg. L2 regularization of weights in a feed-forward neural network). Any explaination of this phenomenon, or ablation experiments proving this as a valid approach in comparison to traditional regularization in optimization step, would be helpful.

### Questions
I have 2 major questions that effect my score. In the order of importance:

1. The paper mentions ability of a neural-graph $\mathcal{G}$ to be separated into Neural Modules for faster computation by allowing parallel computation, but the method for such factorization or parallel computation is never presented. This I believe is the most important detail that this paper should provide as it allows the realization of neural modules effectively making such general neural-graphs computationally feasible.
2. It is unclear as to how the introduction of regularization in the forward process (Eqn. 6) directly achieves promotion of sparsity in the network. Typically, such regularization is done in the optimization step after computing the gradients (eg. L2 regularization of weights in a feed-forward neural network). Any explaination of this phenomenon, or ablation experiments proving this as a valid approach in comparison to traditional regularization in optimization step, would be helpful.


**Small suggestions to improve the paper**:
1. Line 209: "Existing numerical methods can effectively solve these above equations." - It would be good to mention which methods you used.
2. Figure 3: The x-axis of all plots is mentioned as "parameter", however it is $\alpha$ for the first 3 plots, and "number of nodes" for the last one. The figure should be updated with correct x-axis labels to help readers. Additionally, the different plots should be labeled as A, B, C, D, so that they can be referred in the text as "Fig. 3A shows ...", instead of "first plot of figure 3 ..."
3. I believe the symbol $f^{-1}$ is incorrectly used in the paper to denote the derivative of the function $f$. This is the symbol is generally used for "inverse function for $f$", and the standard was derivative is $f'$.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper contends that current tree-like/hierarchical structures of neural networks are insufficiently expressive compared to examples of biological neural networks, proposes that networks of arbitrary directed graph structure (where "later" nodes can influence "earlier" ones) might get us access to levels of expressivity not possible with existing structures. However, they recognize that, because this model structure necessitates solving a system of equations in the forward pass, it scales poorly with the size of each system of equations being solved (which in this case is the size of the fully connected subcomponent being solved). Therefore, they formulate a regularizer (which they call NM regularization) which penalizes nodes for being connected to large subcomponents within the graph. This means that nodes will tend to have their edges with larger subgraphs decay to zero, which reduces the size of the subgraphs. They also implement threshold-based sparsification, only including equations in the system of equations to be solved if they have a weight > lambda to the subcomponent

### Strengths
- The paper provides a seemingly practical way of scaling computation graphs without scaling the systems of equations to be solved to an impractical degree, while still staying within the paradigm of soft, gradient-based learning, and not needing to know the network structure ahead of time 
- The paper is well-presented and clear to read

### Weaknesses
 - The paper didn't provide any estimates for how computational cost would scale for more plausibly-sized models (which I think could have been done with some estimates of different regularization parameters and size k without necessarily having to run those experiments)
- The paper did not necessarily make an argument for whether certain _kinds_ of dataset benefit from this problem structure or require it to be solved well, which would make the argument for this computationally costly procedure more compelling. Instead it just tested the approach on some generic ML datasets.
- While there are multiple datasets shown in this paper, it's still not clear whether there are problems that a big enough NN fundamentally will have issues solving, and that a NM will solve successfully. To the point above: can I just train a bigger NN at the same runtime cost to match the performance of a NM. To answer that question, looking more closely at the results, I notice that for two out of the three datasets tested, the 300 node has higher error than the 200 node for NMs, and for all 3 datasets the standard NN has higher error on the 300 node relative to the 200 node. This raises concerns about overfitting, and the simplicity of these datasets, if they are saturating at this small a number of parameters, and makes me worry that these datasets are too simple to provide experimental signal that we should expect to generalize elsewhere

### Questions
- Is there any story for how this could scale to realistic sizes of parameters (as far as I saw 300 parameters was the largest size shown)? 
- What kinds of problems do you believe this technique would be specifically high-value for?

### Soundness
3

### Presentation
3

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
This paper proposes Neural Modules, a graph-based framework for organizing neural units within neural networks that aims to go beyond the traditional constrained structure of neural networks (NNs). Unlike the tree-like structure of traditional NNs which does not allow neurons to establish connections across the same layer, Neural Modules defines a graph-based structure that allows all neural units to communicate with all other units, allowing for more collaborative learning. Performance across three datasets from the UCI data repository are reported, showing that Neural Modules achieves lower error rates compared to other architectures and faster runtime compared to the DEQ model.

### Strengths
1. The discussion about traditional tree-like neural network tructure and the motivation behind redesigning the connectivity pattern behind neurons is well-written and clearly stated. A better organization of neurons could potentially allow for more efficient learning closer to that of real biological neural networks.
2. The methodology provides a formulation for the forward and backward pass of the Neural Modules architecture.
3. The authors show performance comparisons when varying the NM regularization parameter, and show a runtime comparison against one baseline model.

### Weaknesses
1. Performance of Neural Modules with several hundred nodes is reported on several datasets, however there are many other datasets with thousands of input features, requiring more nodes. The results would be stronger with benchmarking results on other datasets with more nodes in the graph, to demonstrate scalability to large graphs of neurons and more diverse datasets.
2. The running time reported for Neural Modules in Figure 3 lacks units, which makes it difficult to gauge what the relative improvement in runtime is against DEQ. Additionally, runtime is not compared to regular NNs, making it unclear if there are runtime disadvantages for Neural Modules versus traditional NNs.
3.  The authors propose NM regularization as a way of introducing sparsity in the connections in the graph to reduce the amount of computation, however it is unclear whether the model can optimally learn connections between nodes given the constraint. Figure 3 shows performance relative to different sparsity levels with 100 nodes on three datasets, however 100 nodes is quite small for many datasets which may have thousands of input features. A scalability test with more input nodes would strengthen the case that the framework is scalable to many nodes in a graph. Regarding the runtime reported in the fourth subplot of Figure 3, it would help to include units and more descriptive axes labels to help interpretation of how much runtime is benefitting from the sparsity constraint.
4. In several sections, there are typos or missing elements; in Figure 3, the subplots are not labeled with dataset labels, making it difficult to tell which dataset performance is being reported on in each subplot. In Section 3, there are some instances of unclear phrasing (e.g. “In real-world applications, efficiency can be optimized.” in Section 3.3).

### Questions
1. In Section 3.1, the authors mention that N0 denotes the “nodes for the first layer and the input variables feed into the first layer.” Does this indicate that N0 is the data which is fed into the first layer? The wording surrounding the usage of the words “input variables” is slightly confusing, however it is clear that the parameters of the model are represented by edges within the structure.
2. How well does this graph-structured processing work on modern GPU infrastructure? An ablation study of the runtime of Neural Modules versus traditional modules would provide more clarity on whether Neural Modules is comparable in runtime to traditional NNs on modern compute hardware.
3. How well does the Neural Modules framework scale to large neural layers with many nodes within a single layer, given that graph connectivity would introduce significant dependencies and computations between individual neurons? The authors propose NM regularization as a way of introducing sparsity in the connections in the graph to reduce the amount of computation, however it is unclear whether the model can optimally learn connections between nodes given the constraint. Figure 3 shows performance relative to different sparsity levels with 100 nodes on three datasets, however 100 nodes is quite small for many datasets which may have thousands of input features. A scalability test with more input nodes would strengthen the case that the framework is scalable to many nodes in a graph. Regarding the runtime reported in the fourth subplot of Figure 3, it would help to include units and more descriptive axes labels to help interpretation of how much runtime is benefitting from the sparsity constraint.
4. In several sections, there are typos or missing elements; in Figure 3, the subplots are not labeled with dataset labels, making it difficult to tell which dataset performance is being reported on in each subplot. In Section 3, there are some instances of unclear phrasing (e.g. “In real-world applications, efficiency can be optimized.” in Section 3.3).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript proposes to organize the neurons in a neural network to a graph-based structure along with an regularization method. While the experimental results demonstrate advancement, the motivation of reorganizing the neural networks from tree-like structure to flat graph structure requires further clarification. The contribution of this work is not convincing since existing works such as reservoir computing have also adopted such structure.

### Strengths
1. The rethinking and redesigning of the neural network structure is in urgent need and the idea of this work originates from real biological neurons.
2. The methods and contends in this paper are easy to follow.
3. Experimental results demonstrate advancement of the proposed framework.

### Weaknesses
1. The motivation of reorganizing the neural networks from tree-like structure to flat graph structure requires further clarification. Specifically, the advantages of a general graph structure over a hierarchical one, in terms of expressiveness and learning capability, are not clearly articulated. The paper needs to provide a more rigorous justification for why moving away from well-established hierarchical structures is beneficial, beyond simply stating it allows for more flexible arrangements. The potential for increased complexity and difficulty in training such a general graph structure also needs to be addressed.
2. The literature review to existing works is not extensive, while the differences with similar works such as reservoir computing have not been explained. The paper should provide a more thorough comparison with reservoir computing, highlighting the key differences in terms of network architecture, training methodology, and performance characteristics. It is not sufficient to simply mention reservoir computing; a detailed analysis of how this work differs is required.
3. The figures are not expressive. The figures lack sufficient detail and clarity to effectively convey the proposed concepts and experimental results. For example, the figures illustrating the graph structure and the neural modules should be more informative, showing the connections, node types, and module boundaries more clearly. The experimental results figures should also be improved to better highlight the key findings and trends.
4. While the parameter \gamma in definition 1 lies within the core of this work, its usage and selection are not detailedly described, which should be explicitly explained in equations or pseudocode. The paper needs to provide a more detailed explanation of how \gamma is used in practice, including how it affects the formation of neural modules and how its value is chosen. The lack of clarity around this parameter makes it difficult to understand and reproduce the proposed method.
5. The proposed NM regularization method requires theoretical verification. While the authors claimed that "a larger value of z would cause the edges connected to these subgraphs to tend toward zero", how to initialize z is not described. The paper needs to provide a theoretical analysis of the proposed regularization method, including a proof of convergence and a discussion of its properties. The initialization of z is also critical and should be clearly defined.
6. The experimental results require detailed description to the experimental environment as in other referenced works. The experimental setup, including the hardware and software used, the specific datasets, and the hyperparameter settings, should be described in detail. This information is crucial for reproducibility and for comparing the results with other works.
7. The results in section 4.2-4.4 are quite foreseeable, which bring minor information to the readers. The experimental results presented in these sections do not provide significant new insights. The paper should focus on more challenging experiments that demonstrate the unique advantages of the proposed method.
8. The contents in appendix are redundant and also bring little information. The appendix should contain supplementary material that is essential for understanding or reproducing the work, such as additional experimental results, detailed proofs, or pseudocode. The current appendix does not provide such valuable information.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
