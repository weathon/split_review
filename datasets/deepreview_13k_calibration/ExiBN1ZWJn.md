# Denoising Graph Dissipation Model Improves Graph Representation Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
Graph-structured data are considered non-Euclidean as they provide superior representations of complex relations or interdependency. Many variants of graph neural networks (GNNs) have emerged for graph representation learning which is essentially equivalent to node feature embedding, since an instance in graph-structured data is an individual node. GNNs obtain node feature embedding with a given graph structure, however, graph representation learning tasks entail underlying factors such as homophilous relation for node classification or structure-based heuristics for link prediction. Existing graph representation learning models have been primarily developed toward focusing on task-specific factors rather than generalizing the underlying factors. We introduce Graph dissipation model that captures latent factors for any given downstream task. Graph dissipation model leverages Laplacian smoothing and subgraph sampling as a noise source in the forward diffusion process, and then learns the latent factors by capturing the intrinsic data distribution within graph structure in the denoising process. We demonstrate the effectiveness of our proposed model in two distinct graph representation learning tasks: link prediction tasks and node classification tasks, highlighting its capability to capture the underlying representational factors in various graph-related tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a graph denoising diffusion model using Laplacian smoothing and edge deletion as the noise source. Authors claimed their new model achieve better and more general graph representation learning.

### Strengths
This is an interesting topic to apply DDPM on graph representation learning. The authors had some good ideas on using Laplacian smoother and a coupled node feature similarity based edge removal schedule to add noises. They claimed this helps learn a more general representation by capturing both the attributes and graph structures.. There are some experiment results to seem to support it.

### Weaknesses
The extension of Rissanen et al., 22' work, using Laplacian smoothing for graphs, was natural and even mentioned in the original paper's discussion section. And the claim of *no work on diffusion models for graph representation learning in both feature and structural aspects* feels like an exaggeration. In Vignac et al. 22' (also cited in the manuscript) uses both node features and structural information.

The experiments are not convincing to support authors' claim on the new GDM. Does it learn both feature and structural level information: table 1 only showed it outperforms SEAL on DDI and underperforms on the other three tasks.

### Questions
1. The authors need more experiments/analysis to support the claim that their model can learn both features/structural information well.
2. It would be more helpful if the authors can explore a bit more on the spectral meanings of Laplacian smoothing aside from information dissipation...the authors did mention it decays the high-frequency components on the spectral domain. Can we expand this more? Do we gain additional insights from using Laplacian smoothing. 
3. I assume GDM was trained on sampled subgraphs (?) but there was no mentioned on how this was done. Does the model only work on smaller graphs? 
4. Minior:

    a). In the abstract, *...model leverages Laplacian smoothing and subgraph sampling as a noise source.* What does subgraph sampling mean here? Edge removal? 

    b). In the abstract, *...Graph dissipation model that captures latent factors for any given downstream task.* need to tune down. 

    c). Some parts of the paper are overly verbose, for example is Corollary 3.1 truly needed? 

    d). typos...for example pg5 *graph-strudtured*, pg8, *iffusion*

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a Graph Dissipation Model (GDM), an innovative framework designed for both link prediction and node classification tasks in graph-structured data. The novelty lies in a coupled diffusion process that merges structure-based and feature-based diffusion mechanisms. Through exhaustive experiments on multiple datasets from the Open Graph Benchmark (OGB), the authors empirically show that GDM outperforms several state-of-the-art methods across different metrics.

### Strengths
Comprehensive Approach - The GDM model is versatile in its application as it targets both link prediction and node classification. This comprehensive scope extends its relevance to a broader set of graph-based tasks, making the paper potentially impactful in the field. 

Strong empirical results - The paper takes advantage of the Open Graph Benchmark, a standard and well-regarded set of datasets, providing a robust testing ground for the GDM. Additionally, the authors compare GDM against a wide variety of existing methods, both classical and state-of-the-art, to establish its superiority. Overall, the proposed method performs favorably compared with other baselines.

### Weaknesses
Omission of graph generation performance - While the paper innovatively adapts the DDPM to graph-based tasks, it focuses solely on node classification and link prediction for evaluation. The absence of comparative performance analysis on graph generation tasks against existing algorithms leaves an important aspect of its applicability unexplored.

Absence of sensitivity analysis - The model introduces several hyperparameters, including weight tuning parameters and the length of diffusion steps. The paper lacks an examination of how variations in these parameters impact the model's performance, making it difficult to fully justify the model's design choices.

Insufficient theoretical underpinning - Despite presenting a novel methodology, the paper falls short in providing an in-depth theoretical discussion to substantiate its claims. Specifically, it asserts that the model "captures latent factors for any given downstream task," but fails to offer comprehensive evidence or discussion that would bolster such a statement.

### Questions
This is a follow up of the weakness one: The paper's title claims "DENOISING GRAPH DISSIPATION MODEL IMPROVES
GRAPH REPRESENTATION LEARNING". Is this claim only valid for the proposed denoising graph dissipation model? Do other DDPM model or more generally other graph generation model help improve graph representation learning? Also, have the authors tried to evaluate the graph generation performance method?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Graph Dissipation model which is a coupled diffusion model operating on node feature and graph structure space simultaneously. The model utilizes the Laplacian smoothing to get the noised node features, promoting the denoising network to capture the structural information during training. The evaluation tasks include link prediction and node classification.

### Strengths
- The paper is well-written and easy to follow.
- Using Laplacian smoothing to diffuse the node features is an interesting operation which sounds technique.
- Experiments support the statements in the paper.

### Weaknesses
 - The novelty of the structure diffusion process with randomly removing edges is limited, which also appears in [3]. Further, this reverse process of the used structure diffusion cannot correspond to the forward process.
- In Eq(9), the Feature prediction loss and structure dissipation loss are both confusing. How to calculate the $q(X_{t-1}|X_{t},X_{0})$ and $q(A_{t-1}|A_{t},A_{0})$? The relationship between ELOB(Eq. (8)) and final loss (Eq 9) should rigorously prove.
- Eq (6) is confusing since the $A_t$ is sampled from eq 5, which is unrelated to $A_{t-1}$. So. How to calculate the elements of $A_t$?
- The experimental results show the proposed method doesn’t achieve competitive performance in Link prediction (https://ogb.stanford.edu/docs/leader_linkprop/). Some important baselines are missing, such as GIN, on the node classification task.

Minor concerns:
- Eq (9) is out of bounds.
- The claim “there has been no work on diffusion models for graph representation learning in both feature and structural aspects” is inappropriate because there exist related works such as MoleculeSDE[1],[2].
- The formula at the bottom of page 3 lacks of the explanation of $x$.
- Eq. (8) should be an inequality.
- Is there  $\zeta $ in Eq(5)?

### Questions
- From the Leaderboards of OGB(https://ogb.stanford.edu/docs/leader_linkprop/), the experimental results of this paper are not very competitive. Why the GDM don’t use a powerful GNN as the denoising network? In my understanding, the Loss $L_{diff}$ can be used in any GNN for graph representation learning.
- What is the relationship between GDM and Digress[1]? The GDM seems to be a specific case of Digress.
- What is the benefit of samping $A_{t}$ from Eq(5) instead of a random transition from $A_{t-1}$ like [2]

[1] DIGRESS: DISCRETE DENOISING DIFFUSION FOR GRAPH GENERATION 

[2] Diffusion Models for Graphs Benefit From Discrete State Spaces

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Existing graph representation learning methods mainly focus on task-specific factors rather than universal factors that can be used for any downstream tasks. This work proposes Graph Dissipation Model (GDM) to learn the latent intrinsic distributions of the graph based on the diffusion models, which enables the learned representations to be utilized for any downstream tasks. To encode both node feature and structural information, GDM introduces a coupled diffusion model framework consisting of a feature diffusion process and a structure diffusion process. Laplacian smoothing is innovatively used as a noise source for the feature diffusion process and edge removal is also defined as a noise source for the structure diffusion process. Experiments on both link prediction and node classification show that GDM achieves comparable performance for existing graph representation learning baselines on both tasks, demonstrating GDM's capability of learning universal factors that can be applied to any downstream tasks.

### Strengths
1. This work proposes GDM, the first diffusion-based graph representation learning model that encodes both node feature and structure information. GDM is able to learn comprehensive and universal latent structures from a graph without explicit bias for specific tasks.

2. The idea of utilizing Laplacian smoothing as a noise source for the feature diffusion process and over-smoothing as a convergence state is novel and interesting. Such a design for blurring node features is also more natural in the graph learning setting.

3. Experiments indicate that GDM achieves comparable performance on the link prediction task compared to baselines, and outperforms baselines on a semi-supervised node classification with few training labels, demonstrating that GDM learns universal graph representations that can be applied to downstream tasks.

### Weaknesses
1. Although GDM aims to learn comprehensive and universal graph representations, Equation 10 in the paper still contains the downstream task loss as a part of the final loss. I wonder if GDM without downstream task loss can learn universal graph representations, or we should regard GDM as a universal framework that can incorporate any downstream task loss. Have the authors done some experiments to evaluate the universal graph representations obtained by GDM without downstream task loss? Specifically, it remains unclear if the learned representations without task-specific loss are truly universal or if the downstream task loss is essential for learning good representations. It would be helpful to see an ablation study that explores the impact of the downstream task loss on the quality of the learned representations.

2. In this work, the authors did not mention the time complexity of GDM and its runtime in experiments. As GDM requires eigendecomposition of the graph Laplacian matrix, I wonder if the authors could further discuss GDM's time complexity and also provide some results of the GDM's runtime compared to other baselines in the link prediction and node classification experiments. The computational cost of eigendecomposition, especially for large graphs, can be significant and should be addressed. A comparison of runtime with baselines would be crucial for understanding the practical applicability of GDM.

3. (Minor) I did not find any supplementary materials discussing the details of the implementation of GDM and the experiments conducted in the paper. There is also no code implementation of GDM to reproduce the experimental results presented in the paper. The lack of implementation details and code makes it difficult to verify the results and reproduce them.

4. (Minor) Typo: In the Implementation Details of Section 5.1, 
"Also we set iffusion state to 3 for OGB-Citation2" $\rightarrow$ "Also we set diffusion state to 3 for OGB-Citation2"

### Questions
1. Please see the questions mentioned in the Weaknesses.

2. As the over-smoothing issue appears after only several Laplacian smoothing operations (i.e., node representations converge to identical after only several steps), it seems the value of time step $t$ can be small if we set the over-smoothing as the convergence state. Therefore, I wonder how to choose a proper $t$ to ensure sufficient diffusion and if the authors have done some experiments on the selection of $t$.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
