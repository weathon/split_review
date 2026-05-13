# Text-to-graph Generation with Conditional Diffusion Models Guided by Graph-aligned LLMs

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Text-to-graph generation, aiming for controlled graph generation based on natural language instructions, holds significant application potentials in real-world scenarios such as drug discoveries. However, existing generative models fail to achieve text-to-graph generation in the following two aspects: i) language model-based generative models struggle with generating complex graph structures, and ii) graph-based generative models mainly focus on unconditional graph generation or conditional generation with simple conditions, falling short in understanding as well as following human instructions. In this paper, we tackle the text-to-graph generation problem by employing graph diffusion models with guidance from large language models (LLMs) for the first time, to the best of our knowledge.  The problem is highly non-trivial with the following challenges: 1) How to align LLMs for understanding the irregular graph structures and the graph properties hidden in human instructions, 2) How to align graph diffusion models for following natural language instructions in order to generate graphs with expected relational semantics from human. To address these challenges, we propose a novel LLM-aligned Graph Diffusion Model (LLM-GDM), which is able to generate graphs based on natural language instructions. In particular, we first propose the self-supervised text-graph alignment to empower LLMs with the ability to accurately understand graph structures and properties by finetuning LLMs with several specially designed alignment tasks involving various graph components such as nodes, edges, and subgraphs. Then, we propose a structure-aware cross-attention mechanism guiding the diffusion model to follow human instructions through inherently capturing the relational semantics among texts and structures. Extensive experiments on both synthetic and real-world molecular datasets demonstrate the effectiveness of our proposed LLM-GDM model over existing baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a novel approach that combines large language models (LLMs) with graph diffusion models for graph construction based on input text. Specifically, the method first pretrains an LLM to learn graph generative features in a self-supervised manner, aimed at predicting structural characteristics of a graph. Once the LLM is pretrained, its parameters are frozen, and it is utilized to generate representations of the conditioning text. A structure-aware cross-attention mechanism then allows a graph transformer to approximate the score function of a graph diffusion model grounded in stochastic differential equations.

### Strengths
- The authors address an interesting problem of text-to-graph construction using an LLM to guide a graph diffusion model. 
- Since the LLM in this method is fixed after pretraining, it doesn’t impose much complexity overhead that makes training the diffusion model more feasible. 
- Authors utilize informative visualizations which help to understand the paper.
- The method shows superior performance in most of the graph generation experiments.

### Weaknesses
 - The objectives used for pretraining the LLM may be too simplistic, as tasks such as predicting the number of nodes, edges, or subgraphs could be reduced to mere counting problems for the model. This focus on counting may not effectively encourage the LLM to learn meaningful semantics, potentially limiting its generalization and robustness. Given that the LLM is responsible for generating informative representations of tokens, the authors could consider incorporating auxiliary objectives that promote understanding of token semantics and their dependencies, such as contrastive learning between connected and unconnected nodes. Specifically, the current pretraining approach might not capture the nuanced relationships between tokens and graph substructures, leading to suboptimal representations for guiding the diffusion process. For example, simply counting the number of cycles or cliques in a graph might not provide sufficient semantic information to effectively guide the generation of complex graph structures.
- In the literature, attention scores typically refer to matrices where the row-wise sums equal 1, making the designation of the matrix $A_{edge, uv}$ as an attention matrix potentially misleading. The authors should either clarify this point or normalize the matrix so that the row sums equal one. Alternatively, using a different term for the matrix could also be a viable option. The lack of normalization could lead to issues in interpreting the attention weights and their impact on the graph generation process. Furthermore, it is unclear how the unnormalized attention scores are used in the subsequent steps of the diffusion model.
- While the graph diffusion process is introduced at the beginning of the "Preliminaries," the subsequent processing steps following the generation of the matrices $X_{cond}$ and $E_{cond, uv}$ in the diffusion workflow are not discussed. Providing a detailed explanation of the steps that follow the construction of these matrices would enhance clarity in the framework and improve the reproducibility of the method. Specifically, it is unclear how these conditional matrices are integrated into the diffusion process and how they influence the generation of the final graph structure. The absence of these details makes it difficult to understand the complete mechanism of the proposed method.
- The authors have not provided their code or sufficient implementation details for the method, raising concerns about the reproducibility of the results. The lack of specific details regarding the architecture, training procedure, and hyperparameter settings makes it challenging for other researchers to replicate the reported results. This lack of transparency is a significant limitation.
- The authors rely on a single molecular dataset as their only real-world dataset for experiments. Including additional experiments on real-world datasets from other domains would provide a better evaluation of the method's generalization, especially since it has been outperformed on this dataset based on three out of six metrics. The limited evaluation on a single dataset raises questions about the robustness and applicability of the method to other types of graphs and text-to-graph tasks.

### Questions
- Regarding Equation 8, the dimensionality of matrix $C$ of token representations must match with nodes feature matrix $X$. However, how the dimensionality of matrix $C$ is set for compatibility with $X$ is not discussed. In other words, there must be a process of detecting tokens related to nodes in the input text so that their embeddings represent the node. Is there an entity recognition step employed before extracting the textual representation? 
- Regarding Equation 12, the edge conditioning matrix $E_{cond, uv}$ is composed of continuous elements meaning that it represents a complete graph. However, usually, molecular graphs are sparse, and making complete graphs increases complexity and would also lead to over-smoothing issues. How do authors encourage the sparsity of the graphs?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the intriguing problem of text-to-graph generation, which involves creating graphs based on natural language instructions and has significant potential applications like drug discovery. The authors point out that existing diffusion-based graph generation models mainly focus on unconditional graph generation and lack the ability to comprehend and follow human instructions. To address this issue, they explore guiding graph diffusion with large language models (LLMs) for text-to-graph generation—an area that has not been thoroughly explored. Their extensive experiments on synthetic and molecular datasets demonstrate the effectiveness of their model.

### Strengths
1. This paper examines the intriguing problem of text-to-graph generation, which involves generating graphs based on natural language instructions.
2.  This paper has some reasonable experiments to show the effectiveness of their method.
3.  Self-supervised finetuning and structure-aware cross attention make sense in the solution.

### Weaknesses
1. ChEBI-20 is the only dataset on which all models were tested for real-world text-guided graph generation. I suggest that the authors include additional real-world datasets to verify the effectiveness of the proposed methods.
2. Missing the discussion of the related works and baselines which also focus on text to molecule generation based on large language models [1]. [2]; Missing the discussion of the related works about text-to-graph diffusion models [3], [4].
3. The experimental results are not promising. In text-guided molecule generation, the proposed method only outperforms the smallest model, MolT5-small, on three metrics. Although the model has a small parameter size, its utility performance is significantly worse than that of current models in this domain, which limits its practical applications. Furthermore, the novelty of the proposed method is not significant, as the latent graph diffusion model and the alignment technique have been explored in previous works [1,2].

### Questions
1. Can the authors talk more about their novelty compared with existing text-to-graph diffusion models as mentioned in the weakness part?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to deal with text-to-graph generation using graph diffusion and LLMs. Specifically, this paper proposes a  LLM-aligned graph diffusion model with two main modules to achieve this goal, self-supervised text-graph alignment and structure-aware cross-attention. Three sets of experiments on different tasks verify the effectiveness of the proposed model. Ablation analysis is also conducted.

### Strengths
1. This paper motivates the problem clearly with clear challenges and proposed solutions. This paper also includes a figure in the Introduction section to aid the description.

2. The Preliminaries section contains background information to make the paper self-contained. Overall, the model architecture is clearly described.

3. Experiments are relatively sufficient to verify the effectivenes of the proposed model, and ablation analysis in also conducted to show the importance of each module.

### Weaknesses
Though this paper uses an interesting method to solve the text-to-graph generation problem, from my point of view there are some unacceptable shortcomings.

1. When we consider the generation problem between text modality and graph modality, we should usually solve both sides of generation, i.e., text-to-graph generation and graph-to-text generation. Existing works [1] of generation between text and graph consider both sides, but the submitted paper models only text-to-graph, but not the other side of generation, which significantly limits the technical contribution.

2. When we do experiments, we encourage authors to repeat the same experiment setting multiple times and report both mean and standard deviation, or conduct significance t-test. However, this paper doesn't have standard deviation or significance t-test, which is difficult for readers to judge how significantly the proposed model outperforms baselines.

3. This paper emphasizes computational costs in the experiments, but there is a lack of computational complexity analysis.

### Questions
1. For Eq. 8, the standard multi-head self-attention in the Transformer paper divides the product of $ Q $ and $ K $ by the squared root of dimension $ \sqrt{d} $, not $ d $. Why do authors divide $ QK^\top $ by $ d $ here?

### Soundness
3

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
The paper focuses on large language model (LLM)-guided diffusion models for graph generation tasks. It first fine-tunes the LLM with a self-supervised task of counting the number of nodes, edges, and subgraphs. Then, it uses the output from the last layer of the LLM as the feature vector for input texts in the diffusion model, where this feature vector guides the generation process. Experiments on synthetic datasets and molecular graphs demonstrate the promise of the proposed method. The work is interesting and could be improved with clearer motivation, refined method design, and enhanced experiments.

### Strengths
- The paper is easy to follow.
- This paper proposes to incorporate large language models (LLMs) and graph diffusion models to tackle the challenge of generating complex graphs for LLMs. By using fine-tuned LLMs to generate informative feature vectors for diffusion models, it bridges the gap between textual information and graph structure, enabling more sophisticated graph reasoning.

### Weaknesses
Motivation:
- The claim (lines 17-18, 77-80) that “Graph-based generative models mainly focus on unconditional graph generation, falling short in understanding as well as following human instructions” is inaccurate. Graph diffusion models have rapidly evolved for conditional generation. The paper mentions two graph diffusion models, GDSS and DiGress, both of which have conditional versions developed in [1,2]. The authors need a more comprehensive survey of recent work advancing conditional graph diffusion models. Specifically, the paper should acknowledge and discuss methods that use node attributes or other forms of conditioning, rather than implying that all graph diffusion models are purely unconditional.
- It is unclear why LLMs are necessary to guide diffusion models. LLMs are primarily designed for generative tasks; however, this paper uses them for embedding. Although this is an interesting direction, it is unclear why a language model specialized in producing embeddings isn’t used instead. Fine-tuning LLMs requires substantial resources, and the motivation for using LLMs in this context is not clearly established. The paper needs to justify the choice of LLMs over other embedding techniques, particularly given the computational overhead.

Method: Graphs have discrete structures, and DiGress has been proposed to enhance GDSS for improved graph modeling. It is unclear whether the proposed method uses Gaussian noise instead of the discrete noise used in DiGress. Additionally, many self-supervised tasks have been proposed in graph learning, but the rationale for the one chosen for text-graph alignment is unclear. For example, why would LLMs already align with graphs simply by counting edges/nodes? This task seems too superficial for an LLM to grasp complex graph structures. The paper should explore more sophisticated self-supervised tasks that can capture the underlying structural properties of graphs, such as subgraph isomorphism or graph edit distance prediction.

Experiments: 
- The work compares the proposed method with a few LLMs but overlooks diffusion models or other generative models designed for graph generation, making the results less convincing. The paper should include comparisons with conditional graph diffusion models and other text-to-graph generation methods to properly benchmark performance.
- The metrics are not convincing. There is no metric reflecting the model's ability to satisfy the requirements specified in the text. The paper needs to define and use metrics that directly measure the alignment between the generated graph and the input text description, such as semantic similarity scores or task-specific metrics.
- The paper lacks a comprehensive comparison with text-to-graph generation baselines and evaluation on more domains of real-world datasets. The paper should evaluate the method on a wider range of datasets, including those with more complex graph structures and text descriptions, to demonstrate its generalizability.

### Questions
- Please address the concerns and answer the questions listed under weaknesses.
- What large language model is used in the proposed method?
- What graph neural network architecture is used in the work?

### Soundness
1

### Presentation
3

### Contribution
2
