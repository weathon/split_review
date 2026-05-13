# Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
While large language models (LLMs) have integrated images, adapting them to graphs remains challenging, limiting their applications in materials and drug design. This difficulty stems from the need for coherent autoregressive generation across texts and graphs. To address this, we introduce Llamole, the first multimodal LLM capable of interleaved text and graph generation, enabling molecular inverse design with retrosynthetic planning.
Llamole integrates a base LLM with the Graph Diffusion Transformer and Graph Neural Networks for multi-conditional molecular generation and reaction inference within texts, while the LLM, with enhanced molecular understanding, flexibly controls activation among the different graph modules. 
Additionally, Llamole integrates A* search with LLM-based cost functions for efficient retrosynthetic planning. We create benchmarking datasets and conduct extensive experiments to evaluate Llamole against in-context learning and supervised fine-tuning. Llamole significantly outperforms 14 adapted LLMs across 12 metrics for controllable molecular design and retrosynthetic planning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper propose a multimodal large language model framework to jointly model molecules and texts for drug discovery and retrosynthesis planning tasks, which is motivated by the fact that the joint modeling of texts and molecules remain challenging.  To address this, the framework combines an existing LLM with two pre-trained graph encoders: one for conditional molecule generation and another for predicting reaction templates for retrosynthesis planning. The paper further proposes to apply A* search to ensure the target product could be synthesized from reactants that are purchasabe on the market. To summarize, the goal of this paper is to propose a MLLM-based framework that is able to build a pipeline from drug design to retrosynthesis planning for the discovered molecules. To evaluate the proposed framework, the paper proposes a dataset to benchmark in such task. From the empirical experiments, the paper argues that the proposed framw3ork Llamole outperforms the baselines of ICL or SFT with only LLMs, as well as GraphGA. The paper also justifies their deisgn of the framework based on ablation studies.

### Strengths
1. The idea proposed in the paper on jointly model texts and molecules with MLLM for inverse molecular deisgn and retrosynthesis planning pipeline is novel. The created dataset could also contribute to the area;
2. From the experiments the proposed framework shows strong performance.
3. The paper is clearly written for readers to understand the proposed method.

### Weaknesses
The baselines selected in the experiments are mainly LLMs with ICL or SFT. The only baseline with similar purpose is GraphGA. It would be interested to see the comaprisons of more baselines of the combination of existing inverse molecular design [1] and retrosynthesis planning [2,3] methods.

1. Weiss, Tomer, et al. "Guided diffusion for inverse molecular design." Nature Computational Science 3.10 (2023): 873-882.
2. Zeng, Tao, et al. "Developing BioNavi for Hybrid Retrosynthesis Planning." JACS Au 4.7 (2024): 2492-2502.
3. Han, Peng, et al. "Gnn-retro: Retrosynthetic planning with graph neural networks." Proceedings of the AAAI conference on artificial intelligence. Vol. 36. No. 4. 2022

### Questions
What is the computational cost and inference time of the proposed methods, compared to GraphGA?

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
5

### Summary
The paper introduces Llamole, a novel multimodal large language model (MLLM) designed for inverse molecular design. It is capable of autoregressive generation of interleaved text and graphs, which is a significant advancement in the field. Llamole integrates a base LLM with a Graph Diffusion Transformer and GNN model to enable molecular generation and molecular inference within textual contexts. Additionally, it incorporates an A* search algorithm with LLM-based cost functions for efficient retrosynthetic planning. The authors have further created benchmarking datasets, MolQA and MolPair, and conducted extensive experiments comparing Llamole against various state-of-the-art LLMs, demonstrating its superiority in controllable molecular design and retrosynthetic planning.

### Strengths
- The paper presents an autoregressive MLLM capable of understanding and generating interleaved text and graphs, which has the potential to be applied to a wide range of molecule-text downstream tasks.
- The authors have collected and processed new datasets, MolQA and MolPair, which allow for more complex molecule-text downstream evaluations. These datasets will be valuable resources for future research in the field if they can be made open-source.
- The experiments in controllable molecule generation are particularly compelling.
- The integration of the A* search algorithm with LLM-based cost functions is a practical and effective approach to retrosynthetic planning

### Weaknesses
 - The framework of this work (Figure 3) is somewhat difficult to understand due to its tight layout and restricted color use. - Rearranging the layout and using a more varied color scheme could improve the clarity of the framework.
- The first claim about this paper's contribution is a bit vague. Although this model is indeed a novel MLLM (Multimodal LLM), there are already some existing MLLMs for molecular generation and understanding. The key innovation of this work lies in the autoregressive generation of interleaved text and graphs with GNN and Graph Diffusion Transformer. This should be emphasized in the introduction and preliminaries to distinguish it from existing work.
- As mentioned above, there are existing MLLM methods tailored for molecule-text related tasks, some of which can be scaled up to 7B or higher parameter levels. These models have made a great contribution to molecule discovery and should be included in the introduction (Figure 1), preliminaries, and experiment sections of this paper.
- This work conducts experiments majorly on the two new datasets proposed in this paper. While the comprehensiveness of the newly proposed datasets is commendable, additional comparisons on existing datasets such as MoleculeNet or USPTO retrosynthesis datasets would lead to better comparison with previous approaches.

### Questions
I've expressed all my concerns in the weaknesses session.

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
2

### Summary
The paper introduces Llamole, a novel multimodal large language model (MLLM) designed for inverse molecular design that integrates graph and text generation capabilities for retrosynthetic planning. Llamole combines a base LLM with specialized graph modules (Graph Diffusion Transformer and Graph Neural Networks) to perform multi-conditional molecular generation and reaction inference within a unified framework. The model also incorporates A* search with LLM-based cost functions to enhance retrosynthetic planning efficiency. Extensive experiments demonstrate that Llamole outperforms other adapted LLMs on several benchmarks, establishing its effectiveness in controllable molecular design and retrosynthetic planning.

### Strengths
1. Novel Multimodal Integration: The integration of graph-based models with a base LLM to handle both text and graph data is innovative, addressing the limitations of LLMs in generating coherent molecular structures and enabling interleaved text and graph generation.

2. Efficient Retrosynthetic Planning: The use of A* search combined with LLM-derived cost functions significantly improves the efficiency of retrosynthetic planning, offering a practical solution for synthesizable molecular design.

3. Good Performance: Llamole achieves substantial improvements over baseline methods across multiple metrics, demonstrating its superiority in both molecular design and planning tasks.

### Weaknesses
1. Theoretical Justification: The paper lacks a strong theoretical explanation for why the Llamole approach works effectively for inverse molecular design. While the empirical results are compelling, a deeper theoretical discussion would enhance the understanding of its effectiveness. Specifically, the paper does not delve into the underlying mechanisms that enable the graph diffusion transformer and graph neural networks to effectively interact with the base LLM. It remains unclear how the latent spaces of these different models are aligned and how the information flow is optimized for multi-conditional molecular generation. A more rigorous analysis of the information-theoretic properties of the model would be beneficial.

2. Scalability Concerns: The computational cost and scalability of Llamole are not thoroughly discussed. The practicality of deploying such a large-scale multimodal model in real-world scenarios remains unclear, especially given the integration of multiple complex components. The paper should include a more detailed breakdown of the computational resources required for training and inference, including memory usage, training time, and energy consumption. It is also unclear how the model's performance scales with the size of the molecular database and the complexity of the target molecules. The paper should also address the potential bottlenecks in the model architecture that might limit its scalability.

3. Comparative Analysis Gaps: The paper does not compare Llamole with some recent multimodal approaches that also attempt to bridge the gap between graph and text modalities, which would provide a more comprehensive evaluation. The paper should have included a comparison with models that use similar techniques for graph-text interaction, such as those based on graph attention networks or message passing neural networks. Furthermore, the paper should have explored the performance of Llamole on a wider range of molecular design tasks, including those that involve more complex chemical reactions and molecular structures. The lack of comparison with other state-of-the-art methods makes it difficult to assess the true novelty and effectiveness of the proposed approach.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Summary: In this paper, the authors address an important task of multi-modal molecule design using LLMs. In particular, they have integrated pre-trained Graph Models with pre-trained auto-regressive LLM and fine-tuned them using multi-modal data (Text+Graph) to enable interleaved generate Multi-modal output (text, molecules, and graph). Moreover, they have incorporated retrosynthetic planning during generation, where they integrate A* search to efficiently identify synthesis pathways for the designed molecule.

### Strengths
- The paper is very well written. The problem statement is well-motivated. The authors did a comprehensive review of prior work on LLMs for Molecule Synthesis.
- The authors proposed the first multi-modal LLM for molecular design. They proposed a novel idea to integrate Graph encoders with pre-trained LLMs and unified cross-entropy loss into the autoregressive modeling of LLMs. 
- They curated a dataset and developed fine-tuning guidelines for benchmarking multimodal molecular design.
- Authors conduct extensive experiments with popular benchmark datasets and compare them with state-of-the-art models to show the effectiveness of their proposed model.
- Authors conduct ablation studies to show the utility of different components of their model.
- Source code is  provided

### Weaknesses
 - Can the model handle any random format of the question, or is the format specified in Fig-2 predetermined?
- What is the minimum information required by LLMole to generate an appropriate molecular structure?
- To what extent does the information requested in the text match the generated material, and are there any qualitative results available for this?
- For property prediction for Drugs and Materials, Can the model handle unseen datasets for property prediction in drugs and materials? Could the authors provide some insights on this?

### Questions
Check the Weaknesses

### Soundness
4

### Presentation
4

### Contribution
3
