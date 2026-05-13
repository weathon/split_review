# When Graph Neural Networks Meet Dynamic Mode Decomposition

- Decision: Accept
- Scores: 5, 6, 8, 6, 8

## Abstract
Graph Neural Networks (GNNs) have emerged as fundamental tools for a wide range of prediction tasks on graph-structured data. Recent studies have drawn analogies between GNN feature propagation and diffusion processes, which can be interpreted as dynamical systems. In this paper, we delve deeper into this perspective by connecting the dynamics in GNNs to modern Koopman theory and its numerical method, Dynamic Mode Decomposition (DMD). We illustrate how DMD can estimate a low-rank, finite-dimensional linear operator based on multiple states of the system, effectively approximating potential nonlinear interactions between nodes in the graph. This approach allows us to capture complex dynamics within the graph accurately and efficiently. We theoretically establish a connection between the DMD-estimated operator and the original dynamic operator between system states. Building upon this foundation, we introduce a family of DMD-GNN models that effectively leverage the low-rank eigenfunctions provided by the DMD algorithm. We further discuss the potential of enhancing our approach by incorporating domain-specific constraints such as symmetry into the DMD computation, allowing the corresponding GNN models to respect known physical properties of the underlying system. Our work paves the path for applying advanced dynamical system analysis tools via GNNs. We validate our approach through extensive experiments on various learning tasks, including directed graphs, large-scale graphs, long-range interactions, and spatial-temporal graphs. We also empirically verify that our proposed models can serve as powerful encoders for link prediction tasks. The results demonstrate that our DMD-enhanced GNNs achieve state-of-the-art performance, highlighting the effectiveness of integrating DMD into GNN frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
It presents an approach that integrates Dynamic Mode Decomposition (DMD) with Graph Neural Networks (GNNs), resulting in DMD-GNN models. These models are designed to capture the principal components driving the underlying complex physics on graphs, thereby enhancing feature propagation and reducing computational costs. The paper also explores the potential of incorporating additional constraints on DMD and deploying physics-informed DMD for directed graphs, indicating a range of future research directions at the intersection of DMD and GNNs.

### Strengths
By integrating DMD with GNNs, the paper provides a new perspective for capturing dynamic patterns in graph data, which could be important for understanding dynamic behaviors in complex network structures.

### Weaknesses
The main proof is very similar to the proof in "Data-Driven Linearization of Dynamical Systems." 

Although the paper proposes the DMD-GNN model, it does not explicitly elaborate on the relationship between the Koopman operator and graph neural networks in the first chapters, which may affect the reader's understanding of the theoretical foundation and the perceived innovativeness of the model.

Although the paper points out the DMD-GNN's application in multiple learning tasks, it does not discuss the model's potential and challenges in specific fields (such as bioinformatics, social network analysis, etc.). 

The experimental results are not convincing; for example, in Table 1, some of the best results are close to simple MLP's performance. Besides, it only solves some very traditional classification problems in the experiments.

The analysis of the new approach on graph subclasses (e.g., sparse, dense, small-world, etc.) is insufficient. 

Summary of the Model Procedure: From Line 291 to Line 293 is unclear.

### Questions
Eq(12) and Line 237, which is correct? K = ?

What is the W(l) in Eq(14)?

Line 280: Could you please elaborate on the usage of the rate? 

You explained what o() is in Eq (15), but what is Df(0)?

In Lemma 1, what is X? should be X(l)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the relationship between Graph Neural Networks (GNNs) and Dynamic Mode Decomposition (DMD), proposing DMD-GNN models that enhance GNNs' ability to capture complex interactions in graph data through low-rank approximations of dynamic operators. The authors establish a theoretical connection between GNNs and the Koopman operator via DMD, reducing the number of learnable parameters and computational complexity. Experimental results demonstrate that DMD-GNNs achieve superior performance on various tasks, including node classification and link prediction. This work highlights the potential of integrating DMD techniques into GNN frameworks to improve their performance and applicability.

### Strengths
1. The paper is well written and easy to follow, providing a thorough introduction to the backgrounds of GNNs and DMD. This clarity enhances the reader's understanding of the foundational concepts necessary for grasping the main contributions of the work.
2. Connecting DMD with GNNs is an interesting perspective.
3. The authors support their claims with extensive experiments demonstrating the effectiveness of the DMD-GNN models, including evaluations on directed graphs, large-scale graphs, long-range interactions, and spatial-temporal graphs.

### Weaknesses
1. My main question regarding the paper concerns the motivation: to what extent do the dynamics of GNNs actually influence their performance? Approaching this from the perspective of DMD is interesting, but what specific insights does it offer in understanding GNN performance? It's not clear if the observed performance gains are directly attributable to a better understanding of GNN dynamics or simply an artifact of the low-rank approximation introduced by DMD. The paper needs to more clearly articulate the link between the identified DMD modes and the actual behavior of GNNs, showing how these modes contribute to improved learning. Without this, the motivation remains somewhat abstract.
2. On long-range graph datasets, DMD-GNNs appear to outperform traditional GNNs, but some of the baselines used in the paper seem relatively weak. As far as I know, there is a class of GNNs derived from optimization or energy function approaches that perform reasonably well on such datasets. It would be helpful if the authors could include a few examples of these models for comparison. Specifically, models that explicitly address over-squashing or bottlenecks in long-range graphs, such as those using spectral rewiring or curvature-based methods, should be considered to provide a more rigorous evaluation of the proposed approach.
3. It could benefit from a more thorough comparison with frequency-based analysis methods. Since the modes identified by DMD correspond to specific patterns in dynamical systems—similar to how frequency-based methods assume learned graph signals contain both high-frequency and low-frequency components—exploring the relationship between these approaches could yield unique insights. Although the authors provide some explanations in Section 6, illustrating this comparison with specific datasets would strengthen their argument. A more detailed analysis comparing the learned DMD modes with the spectral characteristics of the graph, and how they relate to the performance of frequency-based GNNs, is needed.

### Questions
I’m confused about the implementation details of the model, as the paper provides limited description in this part. Standard DMD requires explicit eigendecomposition, and I would like to know how $\Psi$ and $\theta$ are determined in Equation 14.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work draws a connection between the feature dynamics in GNNs to DMD (a numerical method for Koopman theory). They use this connection to build a novel GNN architecture, which can be used across tasks --- node classification, node regression, link prediction --- and data settings. They validate this architecture with extensive numerical experiments.

### Strengths
The paper is generally well written. I particularly like the high level layout; the section titles lead the reader along nicely; 'How GNNs Resonates with Dynamic Systems' is a particularly nice one :)

I like that it brings the solidity of DMD and merges it with a learning architecture; which I believe to be mostly original (although out of my expertise). I think it could be useful in real physical systems. I understand the authors use publicly available and widely known datasets out of necessity in proceedings like this, but I would think the work would present even stronger if there were physical systems datasets to validate on. See more on this in 'Questions'.

### Weaknesses
 **Clarity of Derivation for Non-Experts**
I did have a bit of trouble following the derivations in Section 4 and 5; I am not a super GNN expert, nor a dynamics systems expert, so this could be on me. I believe this work will be at a disadvantage in an ICLR-like review process bc it truly lies at the intersection of two fields which are typically distinct. I attempt not to punish this work for this valiant effort/approach, but it would be wise of the authors to attempt to preempt this confusion with generous use of intuitive figures. Perhaps an additional figure outlining arguments section 4. Figure 1 covers some, but not all, of this.

&nbsp;

**Scalablity**
Additionally, the authors claim scalability by showing an experiment on 'OGB-arXiv', but I would like a cleaner argument for scalability. It seems a power (s=2) of the adjacency is used in some experiments. This can present issues for memory and runtime. The use of $A^2$ requires storing a potentially dense matrix, which could be prohibitive for large graphs. Furthermore, the repeated matrix multiplications inherent in the DMD update, even with low-rank approximations, could pose significant computational challenges for very large graphs, especially if the rank $r$ is not sufficiently small relative to the number of nodes.

&nbsp;

**Runtime**
I would also like to see some actual runtime plots/figures/numbers. Don't feel the need to re-run everything to record the times. Just enough to give the reader a sense of scale; what will it cost me (time, memory, etc) to actually run this?

### Questions
**The unique benefit of DMD-GNN**

I am really looking for setting which can show the *unique* benefit of DMD-GNN. The authors have gone through extensive derivations and work to derive DMD-GNN. What can it do that a generic, off-the-shelf, large GNN simply cannot do? What tasks does it make significantly easier (perhaps beyond just the final metric going up a bit). Can the authors think of any applications, and ideally datasets, for this purpose? Perhaps data generated from systems closer to how DMD/Koopman theory is typically used would be a nice direction.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provided a novel connection between dynamical mode decomposition and graph neural network. Starting from considering the feature propagation as a dynamical system, authors took advantages of Koopman theorem and DMD in practice to refine this process. They also provided theoretical analysis to state the properties of the model. The results showed consistent improvement of combining the existing models and the DMD module.

### Strengths
This paper provided enough details and derivation to explain the proposed model.
The results proved that with refined features, GNN performance can be improved. Therefore, physics-informed or biological-plausible systems can be further developed based on this structure.

### Weaknesses
1. Figure 1 is actually confusing as an illustration of the model. The same arrow feels like an input to the next function, and it doesn't really show where DMD module is applied.
2. The motivation of this paper should be expanded. As authors stated at the beginning "a carefully analyzed and refined dynamic can potentially enhance GNN performance by providing deeper insights into feature propagation over graphs", it would be great to see how the features are refined and why it benefits the performance. Specifically, it's unclear how the DMD modes actually refine the feature propagation, and what properties of these modes lead to performance gains. A more detailed explanation of the mechanism is needed.
3. It would be much clearer if authors could highlight the algorithm of the model. The lack of a clear algorithmic description makes it difficult to understand the precise steps involved in applying the DMD module within the GNN framework.

### Questions
1. In Koopman theorem, it states that "a linear process can be found in the infinite-dimensional space", while for the proposed model, the authors used DMD method to imitate this, so only a finite dimensional space is constructed. It means that some information will be ignored. Will this method affect the performance of a more complex dataset? In your experiments, are the ranks different in different datasets? How do you decide the number of filters?

2. In the result table 3, when you compare the results of GCN and DMD-GCN, one can observe that the performance is not improved in all columns. Can you have some additional explanations on what features benefit or "destroy" the model? As I pointed out in the weakness, the model's motivation should be explained by the results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors investigate GNNs from the perspective of Koopman theory. They use dynamic mode decomposition (DMD) to approximate the Koopman operator with a finite dimensional matrix. Based on this they propose Graph Neural Network (GNN) models using the low-rank eigenfunctions given by DMD. They compare their model to state of the art GNNs in extensive experiments on several learning tasks, in which the DMD GNNs achieve competitive results.

### Strengths
1) The background of Koopman theory and DMD is well explained in  section 3 and 4.
2) The authors made extensive experiments and effort to validate their models.
3) To the best of my knowledge the idea presented is novel.

### Weaknesses
Major:

1) While sections 3 and 4 are good to understand, I am not sure, if I understood sections 5 and 6 about the model itself completely. A pseudocode and a more detailed description of Figure 1 could help.
2) The proposed model is not compared to GIN, although it is maximally expressive.
3) In line 425,426 you state that DMD-GNNs “outperform the baseline models across the majority of datasets”, which is formulated too strong, because in most cases the performance increases are only minor and/or not significant.

Ambiguities:

4) The sentence on attention-based GNNs (l. 90-93) is a little bit confusing
5) in line 411, you are listing ACMP as a baseline model but it is not occurring in the tables.
6) APPNP is not cited anywhere and explained what the abbreviation means

Minor:

7) The related work section is very general, the differentiation to previous work is unclear.
8) The equation in line 133 is probably wrong, because it would lead to K = 1. Should probably be the linearity of K_t?
9) Line 237: K = M*F would mean that M = 1? Probably a mistake?
10) Please briefly mention the results of App. C.2.4 in 7.2
11) KNN abbreviation in line 466 was not defined
12) Line 234: The pseudo-inverse of H(l) has already been defined in line 227, and it is not even occurring in Eq. (11)
13) Please divide Figure 2 in a and b
14) Fig. 2 is much too small
15) First sentence in 7.1 is confusing.

Spelling/Grammar:

16) line 146: underlying
17) Headline 4: How GNNs Resonate with Dynamic Systems
18) Table 1: Caption should state that the results are from node classification experiments. Point is missing at the end of the caption.
19) line  523-524, grammatic error

### Questions
a) How many hidden nodes were used in the baseline models for node classification? Can you include a comparison of the number of model parameters?

b) The link prediction VGAE framework is not state-of-the-art, why did you use it and not SEAL?

c). For link prediction you used average accuracy instead of ROC-AUC. Why?

d). Why was ChebNet only used for spatial-temporal dynamics experiments?

e) Why did you use the parameter \xi = 0.85 for homophilic graphs but the sensitivity analysis was perfomed only up to \xi = 0.8?

f). Could it be interesting to use other discretization methods than Euler?

### Soundness
3

### Presentation
3

### Contribution
3
