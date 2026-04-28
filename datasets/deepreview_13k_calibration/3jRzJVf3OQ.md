# Quantum entanglement for attention models

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Attention mechanisms in deep learning establish relationships between different positions within a sequence, enabling models like Transformers to generate effective outputs by focusing on relevant input segments and their relations. The performance of Transformers is highly dependent on the chosen attention mechanism, with various approaches balancing trade-offs between computational cost, memory efficiency, and generalization ability based on the task.

Quantum machine learning models possess the potential to outperform their classical counterparts in specialized settings. This makes exploring the benefits of quantum resources within classical machine learning models a promising research direction. The role of entanglement in quantum machine learning, whether in fully quantum or as subroutines in classical-quantum hybrid models, remains poorly understood. In this work, we investigate whether quantum entanglement, when used as a resource, can improve the performance of the attention layer in Transformers.
We introduce an entanglement-based attention layer within a classical Transformer architecture and numerically identify scenarios where this hybrid approach proves advantageous. Our experiments on simple standard classification tasks in both vision and NLP domains reveal that the entanglement-based attention layer outperforms classical attention, showing superior generalization on quantum-generated datasets and in settings with limited training data for classical datasets. Additionally, it demonstrates a smaller generalization gap across all tested datasets. Our work contributes towards exploring the power of quantum resources as a subroutine in the classical-quantum hybrid setting to further enhance classical models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper incorporates quantum entanglement into the attention mechanism of a Transformer encoder by using a measure of entanglement to compute the attention matrix.

### Strengths
Novelty:  The paper proposes entanglement based attention and novel methodology for computing attention. Three measures of entanglement(Entanglement entropy, SWAP test and concurrence)  are used for measuring the entanglement between the queries and the value vectors. The proposed method is evaluated in both classical and quantum datasets.  The proposed model was compared with scaled-dot-product attention and another quantum attention method QSANN model for various vision and NLP datasets. 
Soundness: The paper is well written. The paper claimed that the quantum entanglement based attention is having a better generalization gap across all datasets. The experimental results of the paper supports this claim. Experiments were conducted extensively on various  NLP and vision  datasets with clear figures and tables. 
Significance: With limited number of works done on quantum computing w.r.t Transformers, this work has relevance and future applications
Relation to prior works: The previous related works are discussed comprehensively in this paper. 
Reproducibility: The authors have provided the source code of the experiments

### Weaknesses
Clarity:  In section 4.3, the authors have defined various methods of entanglement. But how these methods are applied in regard to self attention is not clear. The authors have stated the methods used for computing key, query quantum states and attentions, but exactly how it is done on mathematical terms is not defined. A mathematical expression of  the measures of entanglement for computing the attention, would have made it clearer.  Specifically, the paper lacks a clear explanation of how the quantum feature map (QFM) and parameterized quantum circuit (PQC) transform the input embeddings into quantum states suitable for entanglement measurement. The description of how the entanglement measures (Entanglement entropy, SWAP test and concurrence) are actually used to compute the attention weights is vague. For example, it is not clear if the entanglement measure is directly used as the attention weight or if it undergoes further processing. In Figure 5, there is no explanation of how the parameterized quantum circuit is generated. The specific structure of the PQC, including the types of quantum gates used and their arrangement, is not detailed, making it difficult to understand the exact quantum operations performed. 

The  transformer model consists of only  two sequential attention layers. Eventhough the performance of the model with varying data sizes were studied, the performance of the model with varying model sizes have not been studied. Is the model underperforming on larger datasets because of smaller model size? The paper does not explore the impact of model depth on performance, which is a crucial aspect of transformer architectures. It is unclear if the limited number of layers is a bottleneck, especially for more complex datasets. A study on how performance scales with model size would be beneficial. 

A qualitative analysis of the behavior of attention maps and the interactions between various positions, if included, would have given a better understanding of the model. The paper lacks any visualization or analysis of the attention maps. Understanding which parts of the input the model focuses on is crucial for interpreting its behavior and validating the effectiveness of the proposed entanglement-based attention mechanism. Without this, it's hard to assess whether the model is learning meaningful relationships between the input tokens.

### Questions
The model (entanglement entropy) is giving 100% test accuracy on the MC dataset in Table 1. Is there any explanation for this?
In table 1, in the QSANN model, when only CLS token was used the test accuracy dropped from 100 to 56%. What could have been the possible reason?
Why was the comparison only with QSANN model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates the potential of quantum entanglement for attention in Transformers. Authors use the entanglement of quantum states as a co-relation criterion for the Attention layer in the Transformer. The method is evaluated on both language tasks, vision tasks, and quantum datasets. Experiments show the potential of quantum entanglement attention to have better generalization ability.

### Strengths
- The paper is easy to follow.
- Introducing quantum in classical computers is meaningful and interesting.

### Weaknesses
 - Dataset used for experiments is too small. The transformer is a large-scale model that requests large-scale data to learn meaningful features. Besides, quantum entanglement attention shows its outperformance from Figure 2 when the size of the dataset is less than 1000, which is not practical.
- The paper claims that quantum entanglement attention has better generalization ability, which is the difference between train and test accuracy. However, as stated above, the transformer is a large-scale model that requests large-scale data, which means the transformer would easily overfit in small datasets. This has resulted in poor accuracy of transformers on small datasets. For example, in CV tasks, transformers generally require 200-300 epochs on ImageNet to match the accuracy of CNN (which also requires the corresponding number of epochs), while in CIFAR datasets, transformers require 7200 epochs to match the accuracy of CNN, which only requires 200 epochs.
- It's vital to visualize or analyze the attention of quantum and classical. If the elements of quantum attention matrix is all same, the transformer treats all token equally, which means the transformer model is about to degenerate into an MLP which could generalize better than transformer when dataset is small. It's hard to conclude that the benefit is coming from quantum entanglement operation.


- The details of the transformer model should have a description. What's the dimension of the transformer? How many blocks do you stack?  
- The details of datasets for experiments should have a more clear description, e.g., MC and RP datasets.
- The details of training should have a description. How many epochs? How do you train the transformer?
- The illustrations in the paper should be improved. The current illustration is confusing and the content is not clear, especially Fig 1.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an approach that integrates quantum entanglement into the attention mechanism of Transformer models, proposing an entanglement-based attention layer. By encoding query and key vectors as quantum states, entangling them through a parameterized quantum circuit (PQC), and using entanglement entropy to calculate attention coefficients, the method aims to enhance Transformer performance on specific tasks. Experimental results demonstrate that this quantum-based attention layer outperforms classical attention on smaller classical datasets and quantum-generated datasets, showing a superior generalization gap and reduced tendency to overfit. The work provides valuable insights into leveraging quantum properties within classical machine learning frameworks, especially for data-limited applications, and contributes to the emerging field of quantum-inspired hybrid models. This research lays the groundwork for further exploration of quantum resources as subroutines in machine learning models, particularly Transformers, offering new possibilities for performance improvements in specialized scenarios.

### Strengths
This paper presents an innovative approach that integrates quantum entanglement into the Transformer’s attention mechanism, using entanglement entropy to calculate attention coefficients. The method demonstrates improved generalization and reduced overfitting on small classical and quantum-generated datasets, providing a robust evaluation against classical and other quantum attention models. This work contributes to quantum-classical hybrid models, showing potential in data-limited applications and opening avenues for further exploration in quantum-enhanced machine learning.

### Weaknesses
1. The paper does not address the impact of noise on the proposed quantum model, which is crucial given the current limitations of noisy intermediate-scale quantum (NISQ) hardware. Quantum systems are inherently sensitive to noise, and without examining how noise affects the model’s performance, it is unclear whether the proposed entanglement-based attention mechanism can be effectively implemented on real hardware. Specifically, the paper lacks any discussion of how decoherence, gate errors, or measurement inaccuracies might degrade the performance of the parameterized quantum circuits used for entanglement generation and entropy calculation. To improve the practical relevance, I recommend adding noise simulations or discussing how hardware noise, such as bit-flip errors or phase damping, might affect entanglement performance in attention mechanisms, which would make the work more applicable to real-world quantum devices.

2. Although the authors introduce entanglement entropy for the attention mechanism, the paper lacks a rigorous theoretical foundation to explain why entanglement specifically improves generalization in small-data scenarios. There is little discussion on the advantages of Hilbert space representations (related to quantum feature mapping, QFM) or why quantum entanglement should provide performance benefits over classical models, especially from a quantum information perspective. The paper does not delve into the properties of the quantum feature map used to encode the input data, nor does it explain how the entanglement entropy captures relevant features for the attention mechanism. I recommend that future work include a deeper theoretical exploration of the role of quantum entanglement in attention mechanisms. This could involve discussing Hilbert space properties, parameter efficiency, and the specific benefits of quantum versus classical models, to clarify the approach’s underlying strengths and limitations.

3. The paper does not provide a detailed comparison of parameters between the quantum and classical models, which could help clarify the computational trade-offs of the proposed approach. Including a summary table of model configurations and hyperparameters would enhance transparency, allowing readers to better understand the computational costs associated with each method. For example, the number of qubits, the depth of the parameterized quantum circuits, and the number of classical parameters in the embedding layers should be explicitly stated and compared against the number of parameters in the classical attention mechanism.

4. The paper only compares its entanglement-based attention mechanism with a simplified Transformer model. It would be helpful to compare against other classical models, such as MLPs, to demonstrate the quantum model’s relative performance more comprehensively. This would help establish whether the observed performance gains are specifically due to the quantum attention mechanism or if similar performance could be achieved with simpler classical architectures.

5. The paper does not reference several recent works that are highly relevant to quantum self-attention and Transformer models. Key papers, such as Shi et al. (2023), Shi et al. (2022), and Di Sipio et al. (2022), explore similar mechanisms and should be cited for completeness. These references would provide additional context and underscore where this work contributes new insights to the existing literature.

### Questions
1. Given that current quantum hardware is noise-prone, how do the authors envision the entanglement-based attention mechanism performing in noisy conditions? Are there plans to test this model in simulated noisy environments or on NISQ devices to verify its stability?

2. Although this paper proposes using entanglement entropy for a quantum implementation of the attention mechanism, it lacks an in-depth analysis of the theoretical foundation and effectiveness of this approach. It is recommended that the authors enhance the theoretical exploration of the role of quantum entanglement in the attention mechanism, especially by explaining from a quantum information perspective why it performs exceptionally well on certain tasks. Additionally, a discussion on the theoretical basis and advantages of Hilbert space (related to the Quantum Feature Map, QFM) and the parameter efficiency of quantum models compared to classical models would be beneficial.

3. Can the authors include a table comparing the parameters and architectures of the quantum and classical models to clarify any computational trade-offs? This would help readers understand the efficiency and scalability implications of the proposed approach.

4. Have the authors considered evaluating the entanglement-based attention mechanism against other classical models, such as MLPs, to provide a broader baseline comparison? This could clarify whether the quantum approach offers unique benefits over simpler classical architectures.

5. Several relevant works on quantum self-attention and quantum Transformer models are missing from the current paper. Could the authors consider adding the following references to provide additional context and background on prior work in this area?

Shi, Shangshang, et al. "A natural NISQ model of quantum self-attention mechanism." *arXiv preprint arXiv:2305.15680* (2023).
Shi, Jinjing, et al. "QSAN: A near-term achievable quantum self-attention network." *arXiv preprint arXiv:2207.07563* (2022).
Di Sipio, Riccardo, et al. "The dawn of quantum natural language processing." *ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*. IEEE, 2022.

### Soundness
2

### Presentation
2

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
This paper presents an entanglement-based attention layer integrated into a classical Transformer, where the traditional dot product operation between query and key vector pairs is replaced by a quantum feature map circuit and an entanglement measurement. Leveraging quantum circuits introduces quantum entanglement into the attention mechanism. Numerical experiments indicate that entanglement entropy outperforms other entanglement metrics, and the entanglement-based layer demonstrates advantages over its classical counterpart in classification tasks within vision and NLP domains. For both quantum-generated and classical datasets, the model shows improvements in classification accuracy and a reduced generalization gap.

### Strengths
1. The attention mechanism is a cornerstone of modern machine learning, and the potential enhancements offered by quantum computing are compelling.
2. Exploring the synergy between quantum computing capabilities and entanglement is valuable, and this paper provides promising numerical evidence.
3. The quantum circuits are relatively simple and could likely be implemented in near-term quantum computers.

### Weaknesses
1. Circuit size: The model proposed in this paper involves a simulated quantum circuit with only 6 qubits; meanwhile, the quantum circuit in Figure 5 is too simple, introducing only local entanglement. Experiments with more qubits (such as 10~20) could significantly improve the soundness of the paper.

2. Motivations: The introduction talks a lot about well-known concepts, but the motivations or insights to replace the dot product with entanglement in the attention mechanism are not sufficiently discussed.

3. Efficiency: My understanding is that the entanglement measurement needs to be performed as many times as the number of attention coefficient matrix elements, which is quite inefficient. The algorithmic/time complexity should be explicitly discussed in this paper.

4. Missing details: There is no specific explanation for the query state and key state; are they row or column vectors of Q and K? Detailed circuit implementations should be provided. Also, the complexities of the different entanglement measurements are not compared in Section 4.3.

5. Concerns about model performance. The numerical results in Figure 2 suggest that the classical model performs better as the sample size increases, potentially diminishing the practical value of this model. I wonder if the small size of the quantum circuit limits performance when using large sample sizes. The training curves are not stable, which could be improved by adjusting hyperparameters. Is there any reason behind the instability of the training curve?

6. Citation mistakes. The introduction refers to 'Systematic benchmarking of existing quantum approaches suggests that entanglement may not play a significant role' but cites no paper. In Section 4.1, QFM methods are reviewed but not proposed by Khan et al. (2024). In Section 4.3, Quantum State Tomography lacks citation, where a typo occurs (FST).

### Questions
A few concerning points are listed as follows, and I hope the authors could clarify these before I change my mind in this paper's decision.

1. How about the scalability/complexity of this model, or, what is the scaling with respect to the vector size?

2. Can it show more concrete relations between quantum entanglement and enhancement, to evaluate whether stronger entanglement leads to stronger model performance?

3. If the quantum circuit size becomes larger, will the quantum model keep its advantage on classical datasets as in Figure 2?

4. There have been existing papers differently adapting attention mechanisms, such as Cherrat and Kerenidis (Quantum 2024), Ren-Xin Zhao (IEEE Trans. Pattern Anal. Mach. Intell. 2024), and Khatri (arXiv:2406.04305). What is your advantage or novelty compared to their works?

5. Could you please provide a resource analysis including time complexity, qubit number, or number of measurements...

6. Please clarify several concepts, including "learning rate scheduler", "data reuploading layers" In Appendix A. 

7. What is the number of trainable parameters in this model?

### Soundness
2

### Presentation
2

### Contribution
2
