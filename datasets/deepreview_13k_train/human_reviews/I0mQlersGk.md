# SGHormerVQ: Bridging Graph Transformers and Spiking Neural Networks via Spiking Vector Quantization

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Graph Transformers (GTs), which simultaneously integrate message passing and self-attention mechanisms, have achieved promising empirical results in some graph prediction tasks. Although these approaches show the potential of Transformers in capturing long-range graph topology information, issues concerning the quadratic complexity and high computing energy consumption severely impair the scalability of GTs on large-scale graphs. Recently, as brain-inspired neural networks, Spiking Neural Networks (SNNs) provide an energy-saving deep learning option with lower computational and storage overhead via their unique spike-based event-driven biological neurons. Inspired by these characteristics, we propose SGHormerVQ, which bridges efficient Graph Transformers and spiking neural networks via spiking vector quantization. Spiking vector quantization generates implied codebooks with smaller sizes and higher codebook usage to assist self-attention blocks in performing efficient global information aggregation. SGHormerVQ effectively alleviates the reliance on complex machinery (distance measure, auxiliary loss, etc.) and the \textit{codebook collapse} present in previous vector quantization-based GNNs. In experiments, we compare SGHormerVQ with other state-of-the-art baselines on node classification datasets ranging from small to large. Experimental results show that SGHormerVQ has achieved competitive performances on most datasets while maintaining up to 518× faster inference speed compared to other GTs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors proposed SGHormerVQ, which is a graph transformer with spiking neural networks. SGHormersVQ utilizes spiking vector quantization with a codebook. According to the authors’ experiments, they could achieve 518x faster inference speed compared to other models.

### Strengths
- Through experiments and competitive results
- Incorporating graph Transformer and spiking neural networks through spiking vector quantization

### Weaknesses
This study presents a method to combine spiking neural networks and graph Transformers through spiking vector quantization to reduce the computational complexity, but it seems that the vector quantization technique using codebook has serious concerns in terms of soundness.

This study utilizes a method to reduce the computational complexity of self-attention through vector quantization using a codebook. Vector quantization is implemented using spiking neurons as quantization functions. This causes the codebook to change dynamically, which is expressed in the manuscript as the term “implicit codebook.” However, this is actually just a spike train, which is the activation value of a spiking neuron, and it is difficult to apply a quantization technique that uses a codebook because it changes dynamically. The core issue is that the 'implicit codebook' is not a fixed set of vectors; it is a dynamically changing set of spike counts derived from the spiking neuron activations. This dynamic nature undermines the fundamental principle of vector quantization, which relies on a static codebook to map input vectors to a reduced set of representative vectors.

In addition, in general, in order to improve efficiency due to quantization, the representation space of the codebook should be narrower than the representation space of the activation. However, in this study, since these two are used identically, it is correct to say that there is no improvement due to the codebook. In this paper, vector quantization using an implicit codebook simply processes information with spike activation. It is unreasonable to view the improvement as being due to a codebook vector quantization. The main reason for the improvement is believed to be due to the characteristics of spiking neural networks that process information with binary spikes. The authors need to clarify this. The claim that the method achieves efficiency gains through vector quantization is misleading because the 'codebook' is not a pre-defined, static set of vectors but rather a dynamically generated set of spike counts. This means the method is essentially performing a form of binarization or discretization, rather than true vector quantization.

Furthermore, a significant portion of the manuscript is devoted to explaining existing research. It is necessary to concisely revise it and devote more parts to explaining the proposed model. Overall, it is recommended that the authors revise the manuscript.

- Miscellaneous
  - Redundant definition of abbreviations - SNNs, GT, SVQ
  - Used before abbreviations are defined - GNNs (line 107)
  - Used undefined abbreviations - EMA (line 148)

### Questions
- Why is the title SGHormerVQ?
- What algorithm was used for learning?
- What surrogate function was used?
- What is the effect of the norm function in Equation 11?
- What is R in g{V,e,X} → g{V,e,R} in Figure 2?
- What does U in Equation 13 represent? It is a one-hot matrix, so what information does it contain?
- Line 305: “we construct random features” → What does it mean?
- Is SVQ the only part that uses spiking neurons? It seems that information is not processed by spikes in other parts. Then, how can this model work on neuromorphic hardware?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a spike-based graph transformer model SGHormerVQ with spiking vector quantization for graph node classification. It builds on transformer with vector quantization and proposes to leverage spiking vector quantization to replace the pre-defined and fixed codebook. Experiments on various datasets demonstrate the competitive performance and faster inference speed of the proposed method.

### Strengths
1. This paper proposes a new spiking vector quantization for efficient graph transformers.

2. The proposed model achieves competitive or superior node classification performance with much faster inference speed than graph transformer baselines.

### Weaknesses
1. The motivation for *spiking* vector quantization is not clear enough.

- If it aims at the potential energy efficiency of SNNs, there is no discussion on the issue of deployment on neuromorphic hardware, because SNNs rely on it to obtain real energy efficiency and hardly have efficiency on GPU. Since spiking vector quantization is only a small part of the model and other parts like normalization, MPNN, and self-attention are real-valued artificial neural networks, the model is not a pure SNN model and has problems for deployment. It is also not proper to mark the model as spike-based since some major parts are not spike-based.

- If it just wants to solve the problems of VQ on GPU, why consider spiking neurons? The process is similar to previous random feature propagation, what if directly use it without the spiking function? No experiment demonstrates any advantage of considering the spiking property.

2. The claim “518$\times$ faster inference speed compared to other GTs” is not proper since SGFormer has a similar inference time. It is also unclear why inference speed is largely improved.

3. For the proposed model, spiking vector quantization seems to adapt previous random feature propagation to the spiking function setting for implicit codebook, and codebook guided self-attention also follows previous works. Can the authors distinguish the contributions of this work more clearly?

4. There is no theoretical analysis for the proposed method.

### Questions
For SNNs, spiking is only one of the properties. Very early works focused on analyzing their stronger computational power induced by the temporal dimension of spiking time [1], and recent works have introduced this thought to graph AI tasks [2]. This paper only considers rate coding that loses a lot of information of spike trains. Is it possible to introduce these spiking time information to better enhance the codebook coding?

[1] Networks of spiking neurons: the third generation of neural network models. Neural Networks, 1997.

[2] Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning. ICML 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Authors propose SGHormerVQ, a graph transformer model that combines Graph Transformers (GTs) with Spiking Neural Networks (SNNs) through Spiking Vector Quantization (SVQ). SGHormerVQ leverages the spiking mechanism of SNNs to encode compact, low-precision spiking vectors that efficiently capture global graph information. The model was evaluated on multiple node classification datasets, demonstrating superior performance and computational efficiency over various state-of-the-art baselines, with up to a 518x increase in inference speed on some datasets.

### Strengths
1.SGHormerVQ introduces SNNs into graph transformers and uses SVQ to address issues of high computational complexity and resource demands in graph data processing. This interdisciplinary model design showcases a novel application of SNNs in graph structures.
2.The paper provides thorough experimental comparisons with various advanced models, and detailed ablation studies support the design decisions behind SGHormerVQ.imited Applicability: The model performs less effectively on datasets with high node degrees (e.g., ogbn-products), suggesting that SVQ may suffer from information loss in highly connected graphs.
Lack of Technical Detail: The practical impact of SVQ and CGSA on computational complexity, hardware requirements, and performance trade-offs is not sufficiently analyzed, potentially limiting the model's real-world applicability.
Unclear Advantage of Innovation: The paper could better articulate the distinct advantages of SVQ over traditional quantization methods, especially regarding its unique application in SNN-based quantization.

### Weaknesses
1.limited Applicability: The model performs less effectively on datasets with high node degrees (e.g., ogbn-products), suggesting that SVQ may suffer from information loss in highly connected graphs.
2.Lack of Technical Detail: The practical impact of SVQ and CGSA on computational complexity, hardware requirements, and performance trade-offs is not sufficiently analyzed, potentially limiting the model's real-world applicability.
3.Unclear Advantage of Innovation: The paper could better articulate the distinct advantages of SVQ over traditional quantization methods, especially regarding its unique application in SNN-based quantization.
4.The authors should set up ablation experiments to verify the model improvement on the speed of inference.
5.The description of how the node information of a graph is converted into a codebook is poor.

### Questions
Same as Weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SGHormerVQ, a Graph Transformer model that integrates spiking neural networks through spiking vector quantization (SVQ) to enhance efficiency in graph learning tasks. By using spiking neurons as quantizers, SGHormerVQ achieves faster inference and reduces computational overhead while maintaining competitive performance on node classification benchmarks.

### Strengths
The paper is very well-written and looks into an important research question.

### Weaknesses
1. I am not sure what is the key novelty of the work - it seems the authors have just used Spiking Vector Quantization (which is itself not a new concept) for spiking graph transformers (also not new)

2. The experimental section is very weak as most of the datasets used for the results are very simple datasets.

3. The paper gives a lot of context and discusses a lot about the prior works. i would recommend to push them to the supplementary section and add more experimental results to show where this model actually works and where it fails- as that is not really clear from the experiments

### Questions
1. I am confused by the statement "SGHormerVQ with better performance infers faster thanotherGTs by up to 518x" as the Fig 4 shows that it has higher latency than the standard GAT with slightly higher accuracy? Also, the authors only show this for the simplest dataset (Physics dataset) - I would recommend the authors to also show the latency results for the more complex datasets. Also, how are you getting the latency numbers? Is it just the average for all the inferences in the test set?

2. I would recommend the authors to give a detailed analysis of energy and memory usage would give solid proof of the paper's efficiency claims.The authors could measure the average number of spikes per inference and that would be a good measure for the memory reductions, especially compared to standard Graph Transformers and SNN-based models. 

3. I would also recommend the authors further break down the SVQ module to explore the effects of specific components (e.g., varying quantization levels, spike neuron types, or normalization techniques) could highlight why SVQ is particularly effective and reveal which configurations yield optimal performance.

4. I am curious - does the degree of homophily play a role in the SVQ?

### Soundness
2

### Presentation
4

### Contribution
2
