# Equivariant Denoisers Cannot Copy Graphs: Align Your Graph Diffusion Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Graph diffusion models, while dominant in graph generative modeling, remain relatively underexplored for graph-to-graph translation tasks like chemical reaction prediction. We show that standard permutation equivariant denoisers cause severe limitations on such tasks, a problem that we pinpoint to their inability to break symmetries present in the noisy inputs. We then propose to \emph{align} the input and target graphs in order to break the input symmetries, while retaining permutation equivariance in the non-matching portions of the graph. We choose retrosynthesis as an application domain, and  show how alignment takes the performance of a discrete diffusion model from a mere 5\% to a SOTA-matching 54.7\% top-1 accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach to graph-to-graph translation using diffusion models. The authors propose methods to address the inherent limitations of equivariant models in aligning nodes between input and output graphs. The paper introduces several strategies for breaking equivariance and empirically validates their approach on retrosynthesis tasks. While the paper is innovative in addressing this important problem, certain theoretical justifications and experimental evaluations could be strengthened.

### Strengths
- The paper addresses a novel and relevant problem in graph diffusion literature, particularly in breaking symmetries for graph-to-graph translation, which has not been explored in depth.
- The idea of using equivariant models and tackling their limitations is well-motivated, and the theoretical underpinning is clear and compelling.
- The alignment techniques proposed for mapping nodes between input and output graphs are intuitive and demonstrate promising preliminary results, especially compared to unaligned versions.

### Weaknesses
 - The justification for certain design choices, such as using the absorbing state distribution instead of marginal distributions (as in DiGress), is insufficiently explained. A more thorough motivation or comparison would be beneficial. Specifically, the paper does not provide a clear rationale for why the absorbing state transition matrix is preferred over the marginal transition, especially given that the marginal distribution is a more natural choice for diffusion models. The empirical evidence cited is not presented in the paper, making it difficult to assess the validity of this choice.
- Some key claims, particularly in Section 3.2, are vague or lack detailed explanation. For example, the statement regarding the model's capability to handle graph transformations requires clearer elaboration. The claim that the model can handle graph transformations due to the inductive bias of structural similarity is not sufficiently justified. It is unclear how this bias translates into the model's ability to perform complex graph edits, such as bond breaking and formation, which are crucial for tasks like retrosynthesis. The paper needs to provide a more detailed explanation of the mechanisms that enable these transformations.
- The experimental validation, while promising, lacks sufficient quantitative comparisons to existing methods (e.g., RetroBridge). More thorough benchmarking and analysis would strengthen the empirical contribution of the paper. The paper should include a more comprehensive comparison with state-of-the-art methods, particularly in terms of metrics relevant to the specific task of retrosynthesis. The current evaluation does not provide a clear picture of how the proposed method performs relative to existing approaches, making it difficult to assess its practical significance.

### Questions
Please refer to  the weaknesses.

### Soundness
3

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
4

### Summary
The central objective of this paper is to design a discrete denoising diffusion model for graph-to-graph translation, where the task is to train a model to predict a target graph given a source graph and, perhaps surprisingly, a matrix of node mappings between them. The authors use [1] as their design template, though the state transition matrix of the forward process relies on the absorbing state formulation from [2]. In this model, the backward process relies on the denoiser network realized by an equivariant transformer architecture, which, on its own, can take only the target graph as input. The authors' main challenge is augmenting the denoiser by also taking the source graph as input. The authors demonstrate theoretically and empirically that a simple augmentation of the denoiser's input by the source graph is not sufficient even for simply copying graphs, claiming that the equivariance of the denoiser is the main reason for this issue. Therefore, the authors propose to partially relax the equivariance by further extending the denoiser's input with the node mapping matrix, proposing the aligned permutation equivariance. The key idea is to design the underlying transformer architecture such that if the source and target graphs are permuted (by two separate permutation matrices) and the node mapping matrix is permuted accordingly, then the output of the denoiser is equivariant only under the permutations of the target graph. In other words, the output remains sensitive only to the permutation of the target graph. The authors compare the performance of their model with many baseline methods on the task of chemical retrosynthesis, achieving state-of-the-art top-1 accuracy and mean reciprocal rank on the USPTO-50k dataset. Finally, they also show the suitability of their model in the context of the guided and conditional generation of molecular graphs.

### Strengths
The paper presents a comprehensive set of experiments that demonstrate the benefits and the practical utility of the proposed model in the context of guided and conditional generation of molecular graphs. The model achieves state-of-the-art results in chemical retrosynthesis.

The paper concerns an interesting problem, and its central message is important to the community.

Nice and clear illustrations accompany the ideas introduced in the paper.

### Weaknesses
### weaknesses:
The writing deserves improvement. Certain parts of the paper need to be communicated more clearly. The notation sometimes needs to be clarified. These concerns are detailed in the following comments.

Major:

The content from the start of Section 3 up to Section 3.2 qualifies more like a background section. The material is heavily inspired by [1]. Please note that [1] also uses conditioning, though it is not presented in the equations in such an explicit way. It takes more work to recognize the details behind the authors' contributions in the current form. Can the authors clearly delineate which parts are background and which are novel contributions?

In line 124 the authors define $X=P^{Y\rightarrow X}Y$ as $(X^N,X^E)=(P^{Y\rightarrow X}Y^N,P^{Y\rightarrow X}Y^E(P^{Y\rightarrow X})^T)$, and in line 151 define $D_\theta(X,Y)=(D_\theta(X,Y)^N,D_\theta(X,Y)^E)$, saying that $D_\theta(X,Y)^N$ and $D_\theta(X,Y)^E$ output a probability vector for each node and edge, respectively. Now, in line 107, the authors say that $X^N$ and $X^E$ are one-hot encoded (again, it is not suitable to use $\mathbb{R}$ in lines 104 and 105 to define this), then how is it possible that $D_\theta(X,Y)=P^{Y\rightarrow X}Y$? There is no mention that the output of $D_\theta(X,Y)$ is implicitly one-hot encoded. This confusion repeats throughout the text, and clear definitions should stabilize it. The authors should

- clarify when and where $X^N$ and $X^E$ are one-hot encoded or real-valued matrices/tensors,
- explicitly define the output space of $D_\theta(X,Y)$,
- explain how the equality $D_\theta(X,Y)=P^{Y\rightarrow X}Y$ is possible given the different encodings,
- use consistent notation throughout the paper for the spaces these variables belong to.

Minor:

The introduction should better motivate why graph-to-graph translation is important in practical applications.

Line 50: *``a solution aligned''* -> *``a solution: aligned''*

Figure 1: *``w.r.t to''* -> *``w.r.t.''*

In Section 3.3, the authors use phrases such as *``should be possible''*, *``should have learned''*, *``should be the same''*. Why do not use a more certain language? Can the authors please clarify what is or is not true instead of something that should be?

The definition of graph-to-graph translation task deserves improvements. Specifically, if the authors define that the node feature matrix and edge feature tensor belong to the set of reals, why do they redefine them as one-hot vectors in line 107? If they are one-hot, then they are only a subset of reals.

There should be $Y$ on the left side of (2). Consequently, how does this density differ from (3)?

Line 153: *``such that we have a probability vector for each node and edge.''* Probability is not the whole set of reals. It only ranges from 0 to 1.

Line 217: The use of *`respectively'* does not fit the sentence's construction.

Line 243: $\mathbf{X}=\mathbf{P}^{\mathbf{Y}\rightarrow \mathbf{X}}Y$ -> $\mathbf{X}=\mathbf{P}^{\mathbf{Y}\rightarrow \mathbf{X}}\mathbf{Y}$

Line 323: What is DPS?

Line 374: What is MRR? It is first defined in line 402.

The explanation of retrosynthesis in lines 337 and 358 is nearly identical.

Line 337: *``3 parts''* -> *``three parts''*

Table A3 should be in the main text (e.g., Figure 8 can be moved to the appendix).

Figure 3 demonstrates the case for $X_T$, yet there is $D_\theta(X_t,Y)$.

### Questions
Do the authors need the node mapping matrix for this task?

Can the authors explain why the left part of (6) should hold (in light of the above concerns with the output of the denoising network $D_\theta$ and the one-hot encoding of $X$)?

Why do the authors present Theorem 1 for fixed t=T? Is the result for $X_T$ not rather obvious (by definition)?

If the authors use $P^{Y\rightarrow X}$ and $Y$ as input into the denoiser, then these two terms already form the full information about $X$. The authors seem to train the denoiser that always has direct access to $X\_0$ through $P^{Y\rightarrow X}Y$. The consequence of this is that $\tilde{p}\_\theta$ in (3) contains $P^{Y\rightarrow X}$ in the condition, i.e., $\tilde{p}\_\theta(X\_0|X\_t,Y,P^{Y\rightarrow X})=\tilde{p}_\theta(X\_0|X\_t,X\_0)$. This design choice is unsound. Please, can the authors clarify?

Can the authors please provide a more comprehensive explanation of the following comment (starting in line 227): *``This makes it impossible for the model ... some random permutation of $Y$.''*?

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
3

### Summary
The paper presents a novel method to perform graph-to-graph translation using graph diffusion models. The authors show why equivariant models are inherently limited in their ability to perform this task when nodes from the prior distribution need to be aligned with nodes from the output. To that purpose, they demonstrate that an ideal equivariant denoiser cannot correctly copy a graph. Then, they propose several ways to break equivariance for the nodes that should be aligned between the input and the output, and empirically validate their method on the retrosynthesis task.

### Strengths
- To the best of my knowledge, the topic of breaking symmetries to perform graph-to-graph translation has not yet been addressed in the graph diffusion literature.
- The problem of using equivariant models is clearly identified and backed by theoritical evidences.
- The paper proposed several simple ways to solve this problem.

### Weaknesses
- The choice of using the absorbing state distribution over the marginal distributions introduced in DiGress [4] warrants further justification. While the absorbing state model may be simpler, a comparative analysis with marginal transitions, especially considering their successful application in other graph discrete diffusion models, would provide a more comprehensive understanding of the performance implications. It's not immediately clear why the absorbing state was chosen as the primary testing ground, given the potential differences in performance and the established use of marginal distributions in the field [4].

- Statements like "it is easy to see" or "Clearly" should be replaced with rigorous explanations and motivations. For instance, the claim in section 3.2 regarding the model's ability to copy graphs and its extendability to modulations of the task lacks clarity. Is it a prerequisite for the model to copy graphs, or does copying imply the ability to perform modulations? This section needs to be significantly expanded to convey its intended meaning and provide concrete insights.

- Several claims and design choices lack sufficient motivation or justification. The proposed aligning methods, for instance, are not adequately motivated. A more detailed explanation of the rationale behind each method, including node-mapped positional encodings, skip connection denoiser, and input alignment, is needed. The progression from established concepts to these specific methods should be made clearer, highlighting the theoretical underpinnings and potential advantages of each.

- The process of passing Y to the denoiser is not clearly outlined. While the section "Aligning Y in the input" provides some information, a more explicit description of how Y, specifically the node feature matrix Y^N, is integrated into the denoiser's input is necessary. This should include details on the concatenation process and the formation of the edge tensor.

- The dataset construction for retrosynthesis is not sufficiently explained. If the USPTO-50k benchmark is a standard dataset, as mentioned, providing more details about its structure, how it is used in this context, and pointing to a specific reference would greatly improve the paper's reproducibility and clarity.

### Questions
- What is the difference between $D$ and $\tilde p_{\theta}$ ?
- How is $\psi$ generated in section 3.5 ?
- How is Y passed to the denoiser ? I feel it's not clearly outlined anywhere except in the section "Aligning Y in the input"
- I don't get how you build the dataset for retrosynthesis. If it is standard benchmark, could you please provide more explanations or point out to a reference

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an aligned permutation equivariant denoiser for a discrete diffusion model to address the graph translation problem. To align the initial state and target, several techniques, including nodal positional encoding, skip connections, and input alignment, are introduced. The model was validated on retrosynthesis, guided generation, and inpainting tasks.

### Strengths
Aligning initial and target to generate efficiently makes sense and the results are promising compared to unaligned version.

### Weaknesses
Since alignment itself is an empirical approach that has been used previously, the contribution may be limited to explaining why alignment is necessary specifically in a discrete diffusion model with an absorbing state as the prior. When compared to RetroBridge in the retrosynthesis task, it is difficult to find a significant performance gap between the proposed model and RetroBridge. In the cases of guided diffusion and inpainting, only a few figures are provided without numerical comparisons, making precise validation difficult. Furthermore, the ablation study is limited, and it's unclear how much each alignment method contributes to the overall performance. For instance, the benefit of positional encoding compared to skip connections alone is not well established. The paper also does not explore the impact of different transition matrices within the diffusion process, which could influence performance. Finally, the robustness of the method to noisy node mappings is not fully explored, limiting the applicability of the method in real-world scenarios where perfect mappings are unlikely.

### Questions
1. The paper assumes that the prior distribution is absorbing state. Does the proposed model still effective even on the uniform distribution prior?

2. What happens if the node-mapping matrix has uncertainty and is not a binary matrix?

3. How does the performance compare when using only direct skip connections without positional encoding?

4. How does the performance differ from graph translation methods in Related Works, such as G2gt?

### Soundness
3

### Presentation
3

### Contribution
2
