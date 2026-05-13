# HIERARCHICAL EQUIVARIANT GRAPH GENERATION

- Decision: Reject
- Scores: 6, 5, 6, 5, 6

## Abstract
Deep learning, and more specifically denoising models, have significantly improved graph generative modeling. However, challenges remain in capturing global graph properties from local interactions, ensuring scalability, and maintaining node permutation equivariance. While existing equivariant models address node permutation issues, they struggle with scalability, often requiring dense graph representations that scale with $\mathcal{O}(n^2)$.

To overcome these challenges, we introduce a novel coarsening-lifting method that generates sparse spanning supergraphs, preserving global graph properties. These supergraphs serve as both conditioning structures and sparse message-passing layouts for generative models. Leveraging this method with discrete diffusion, we model graphs hierarchically, enabling efficient generation of large graphs.

Our approach, to the best of our knowledge, is the first hierarchical equivariant generative model for graphs. We demonstrate its performance introducing new evaluation datasets with larger graphs and more instances than traditional benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors of this paper introduce a hierarchical approach for graph generation using graph coarsening and discrete diffusion. The authors introduce a novel "coarsening-lifting" method that creates spanning supergraphs to model global graph properties at each hierarchical level, improving scalability and capturing global structure. They evaluate their method against other graph generative models and achieve promising results on multiple datasets.

### Strengths
- One of the strongest points of the paper is the scalability of the proposed methods. Usually, graph generators struggle with large graphs, as they have quadratic complexity. By leveraging sparse supergraphs for message-passing, the model reduces this complexity, achieving lower generation time for the graphs.

-   The experimental results are strong, outperforming previous several state-of-the-art methods. The model demonstrates better performance, faster graph generation, and lower memory consumption, which is especially apparent with larger datasets.

- Hierarchical graph generation is an interesting and important research direction, as it can better capture the hierarchical patterns in various graph datasets.

### Weaknesses
 - A weak point of the paper is that it doesn’t sufficiently motivate the hierarchical generation approach beyond its computational efficiency. While reducing computation costs is a valuable advantage, hierarchical generation could offer additional benefits, such as enhanced model interpretability or improved capture of multi-scale graph structures. The paper would be stronger if it discussed these potential benefits in more detail, especially how hierarchical modeling might help in applications with hierarchical graph patterns.

- Even if the paper acknowledges the lack of conditional generation, I think it is important to include some preliminary results or ideas on how to extend the current method with conditioning. In practical applications, generating graphs conditioned on specific properties (e.g., molecule properties) is often necessary.

- Another weak point is the lack of visualizations for the generated graphs. Visual comparisons between generated and real graphs would further improve the evaluation process. Graph visualizations could also help illustrate how well the hierarchical coarsening-lifting process preserves essential features at each level.

- The training time is missing for the results, and only the generation time is included.

### Questions
- Could the authors elaborate on the use for hierarchical generation, aside from computational cost reduction? Specifically, how the proposed method can better model and generate graph structures with hierarchical patterns? 

- How the authors would extend their method to conditional graph generation?

-  Could the authors provide visual comparisons between generated and real graphs?

-  Could the authors provide training time for their method and the baselines across different datasets?

### Soundness
3

### Presentation
2

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
The paper introduces a hierarchical equivariant generative model for graphs using a graph coarsening-lifting method and discrete diffusion. This approach aims to address challenges including scalability and node permutation equivariance. The authors claim significant improvements in generating large-scale graphs with efficient training and inference. Empirical validation is provided through experiments on standard benchmarks and newly proposed large datasets.

### Strengths
The proposed coarsening-lifting method preserves global graph properties, enabling efficient generation of large graphs while maintaining node permutation equivariance. The empirical results demonstrate the method’s strong performance on various datasets, including newly introduced large-scale graph datasets.

### Weaknesses
1. While the hierarchical framework is compelling, training separate generative models at multiple levels increases overall complexity and may pose challenges in terms of training and hyperparameter tuning. The partitioning method also relies on training a GNN and there are no experiments verifying if this is more effective than simpler partitioning methods.
2. The descriptions of the proposed method seem quite vague and informal, which make the paper generally hard to follow. For example, how to formally define global graph information, why equivariant models can not capture that, what is the formal definition of spanning supergraph (definition in proposition 1 looks like a tautology, i.e. for any graphs $G$ and $G'$ we have $G = G' + (G\backslash G')$), etc.
3. There is no ablation study on individual components of the proposed method (such as the architectural choices, the partitioning method) or discussion about hyperparameters (such as how $L$ and diffusion steps affect the performance and efficiency).
4. The novelty seems limited given existing permutation equivariant discrete generative models for graphs [1,2]. The authors might want to provide more detailed comparisons.

### Questions
See above

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
The paper propose a hierachical graph generation models. The idea is to train a partition model to partition graphs into a multiple components, where each component corresponds to a super node. The partition model helps identify components that edges mostly reside within. Then a diffusion model is applied on the components individually to avoid considering all N^2 node pair when formulating the generative models. The method claims to improve sampling speed since the number of variables to be modeled decreases.

### Strengths
1. The propose method has great intuition and the methods used to address graph shrinking are reasonable and convincing

2. The derivation is rigorous and I didn't spot any obvious error.

3. Experiment result seems to be superior over baselines.

### Weaknesses
1. The illustrative figures are a little confusing, I am not sure how the graph is lifted during the generation. Clarity need to be improved.

2. Followup question on 1. In the paper it mentions the modeling only happens intra-cluster edges, are you not considering inter-cluster edges? If so, what's the limitation of the assumption.

3. Typo in line 456: DGSS -> GDSS.

4. Metrics used in experiments are outdated, for example, MMD from GraphRNN are still used in here. I suggest using more metrics that better reflects the generated graph statistics.

### Questions
See weakness.

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
The paper presents a new approach to graph generation based on discrete diffusion. The method addresses two challenges in graph generative modeling, (1) scalability (2) equivariance. To address these challenges, the authors propose an equivariant coarsening-lifting technique to create sparse spanning supergraphs, which they claim maintain global graph properties. This hierarchical model enables efficient generation of large graphs, and the authors validate their approach by comparing it to existing models across multiple datasets, showing improvements in both performance and speed.

### Strengths
1. The usage of a coarsening/lifting technique combined with the hierarchical generation process (in an equivariant manner) is innovative in my opinion.
2. The proposed technique demonstrates competitive results compared to baseline methods.
3. The authors introduce new datasets for larger graphs.
4. The authors provide code to reproduce their results.

### Weaknesses
1. The presentation lacks clarity, making it difficult to understand how the model operates -- see questions below.
2. The method requires training a series of generative models, one per coarsen level. This is a weakness in my opinion, since there might be graphs that require a lot of coarsen levels.
3. Although the model shows good results on large graphs, the comparisons with baseline models are somewhat limited by generation speed constraints, leading to fewer generated samples. 
4. The authors use a specific coarsening/lifting technique in their method, which might be a bottleneck in generating certain graphs. See question 2.

### Questions
1. Do the authors have any insights on how graph size affects the performance of generation? Specifically, is it more challenging to approximate the probability distribution for larger graphs compared to smaller ones?
2. Do the authors know how to quantify the bottleneck that comes from the fact that a particular coarsening/lifting procedure is used?
3. Does the number of nodes remain fixed throughout the entire training/sampling process? From my understanding, the diffusion process is trained independently at each coarsening level. At what point during training/generation does the number of nodes change?
4. What is the number of coarse levels (L) used in the experiments, and how does it affect performance?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript outlines a new approach to graph generative modeling by addressing challenges such as scalability and maintaining node permutation equivariance. Specifically, current denoising models for graph generation face issues in capturing global graph properties from local interactions. Additionally, while existing equivariant models manage node permutation issues, they often struggle with scalability, particularly when dense graph representations with O(n^2) complexity are involved. To overcome these shortcomings, the authors introduce a novel coarsening-lifting method that generates sparse spanning supergraphs. These supergraphs help in preserving global graph properties and are used as both conditioning structures and sparse layouts for MPNN in generative models. By combining this method with discrete diffusion, the model handles graphs hierarchically, improving the efficiency of generating large graphs.

### Strengths
This manuscript proposed a novel hierarchical graph generation method. Firstly, it proposes the gamma-min partitioning method to generate the coarse supergraph G, and then spann the G to a spanning-garph H. With the guidance from G and H, the authors employed the diffusion model for generation. In the experiment, this work was comprehensively evaluated on multiple synthetic and real datasets.

### Weaknesses
1. This manuscript proposes a hierarchical equivariant graph generation model. Specifically, the generated object is a 2D graph, and the equivariance is guaranteed on the permutation group by using MPNN as the basic building block. However, equivariance is not a major contribution of this work, so it is somewhat overemphasized in the title of the manuscript. Moreover, it is suggested to illustrate the generated object at first.
2. The manuscript is lengthy, and the experiments are comprehensive. However, some sections do not have a critical correlation with the proposed method, such as the invariance and equivariance (which are not the main contributions and stem from the properties of MPNN itself) and the spectral properties (a long analysis with proof but not directly applied to the generation). The spectral analysis, while mathematically rigorous, does not provide clear practical benefits or insights directly applicable to the graph generation process. The connection between the spectral properties and the actual generation performance remains unclear.
3. In contrast to the equivariant property, the generation model lacks sufficient detail. The authors should describe the generation model more clearly, including how the graph is encoded, how the constraints of $G$ and $H$ are applied to the diffusion layer, and what the loss function is. Specifically, the method should clarify how the coarsened graph $G$ and the spanned graph $H$ are used to guide the generation process. The encoding of these graphs and their influence on the diffusion process are not sufficiently detailed, making it difficult to understand the core mechanisms of the proposed approach. Furthermore, the specific loss function used to train the model is not explicitly stated, which is crucial for reproducibility and understanding the model's optimization process.

### Questions
1. In this manuscript, the proposed method focuses only on 2D graphs, and the equivariance correspondingly pertains only to permutations. It is confusing when reading the introduction without a clear definition of the graph category.
2. The graph coarsening process, in some ways, appears similar to node clustering. If I cluster the nodes with their neighbors first (or just combined with some neighbors as the supernode), would that lead to similar results compared to the proposed coarsening method? Maybe some ablation experiments will prove that.
3. In Equation (2), the definition of $W$ should be clarified.
4. It is recommended to adjust the content of the manuscript, delete some unnecessary sections amd introduce more details about the generation model, such as how the guidance of the coarsened and spanned graph is employed, and how the model is supervised.
5. It is suggested to present the related work first before introducing your method.

### Soundness
3

### Presentation
2

### Contribution
3
