# Learning Efficient Positional Encodings with Graph Neural Networks

- Decision: Accept
- Scores: 3, 6, 6, 3, 6

## Abstract
Positional encodings (PEs) are essential for effective graph representation learning because they provide position awareness in inherently position-agnostic transformer architectures and increase the expressive capacity of Graph Neural Networks (GNNs). However, designing powerful and efficient PEs for graphs poses significant challenges due to the absence of canonical node ordering and the scale of the graph. In this work, we identify four key properties that graph PEs should satisfy: stability, expressive power, scalability, and genericness. We find that existing eigenvector-based PE methods often fall short of jointly satisfying these criteria. To address this gap, we introduce PEARL, a novel framework of learnable PEs for graphs. Our primary insight is that message-passing GNNs function as nonlinear mappings of eigenvectors, enabling the design of GNN architectures for generating powerful and efficient PEs. A crucial challenge lies in initializing node attributes in a manner that is both expressive and permutation equivariant. We tackle this by initializing GNNs with random node inputs or standard basis vectors, thereby unlocking the expressive power of message-passing operations, while employing statistical pooling functions to maintain permutation equivariance. Our analysis demonstrates that PEARL approximates equivariant functions of eigenvectors with linear complexity, while rigorously establishing its stability and high expressive power. Experimental evaluations show that PEARL outperforms lightweight versions of eigenvector-based PEs and achieves comparable performance to full eigenvector-based PEs, but with one or two orders of magnitude lower complexity.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose learning positional encodings by using spectral graph filters in the initial layers. They argue that this approach corresponds to learning non-linear functions of the eigenvectors. The spectral GNN is applied to the input graph without using node features; instead, random features are added to the nodes. Although this breaks permutation equivariance, the authors argue that using a sufficient number of samples and specific aggregation functions preserves permutation equivariance. The authors argue that this method is expressive, scalable and stable.

### Strengths
- Most other methods based on eigenvectors require computing the eigenbasis, leading to problems on large graphs. In contrast, the authors argue for a worst-case $N^2$ forward complexity without high preprocessing-complexity.
- The experimental results appear promising.

### Weaknesses
 - The paper is not well-integrated into the existing literature. It is unclear what advantages it offers compared to other methods that count cycles. Although related work is mentioned, the authors do not clearly differentiate their approach or highlight their novel contributions.
- The theoretical results often seem incorrect or lack necessary details. Additionally, many of the results appear to be summaries of theoretical findings from related works. Specific examples are provided in the questions section.
- While the method is more expressive than the 1-WL test, this is not surprising. You can basically do anything to increase beyond 1-WL. For instance, simply adding the number of connected components as a feature would make the model more expressive than 1-WL. It would be beneficial to include quantitative results, such as whether the method is weaker than the 2-FWL test, and to compare it with other methods that have proven counting properties for example.
- A more significant issue is that, although the method is more expressive, it also breaks permutation symmetry. It is well known that adding unique node identifiers can make a model universal but breaks permutation symmetry. 
- In Section 5, it is unclear what is meant by having a basis as an input. Additionally, Remark 5.1 is incorrect. In Huang et al., the $\alpha_i$ are always analytic and are sequence-to-sequence mappings, whereas in this work, they are always real-valued mappings that operate on each eigenvector independently. This makes the approach less expressive, at least in the frequency domain.

- Equation (3) does not accurately represent all possible MPNNs, even when restricting $g$ to be an MLP and $f$ to result from multiplication with a GSO. Specifically, using an MLP from $\mathbb{R}^k$ to $\mathbb{R}^k$ does not trivially extend to a graph signal of dimension $\mathbb{R}^{n \times h}$. It seems that the authors are actually performing matrix multiplications from the right with learnable matrices, and using more than one. Similarly, in Proposition 3.1, the representation in Equation (12) is assumed before the proof begins, which is actually what the authors aim to prove.
- In Proposition 4.3, what is the variable $m$ summing over? The entire proposition lacks clarity, and it appears there is no novelty compared to the existing results from Gama et al.
- The authors claim that Equation (6) is permutation equivariant, which does not seem to be correct. It is only equivariant in expectation, similar to the random positional encodings introduced by Sato et al. (2020).
- What are the contributions to the stability and expressivity analysis? It seems that older results are merely being reused.
- Did the authors follow the standard experimental setup? For example, in the ZINC dataset, it is customary to use a parameter budget of 500K parameters.
- The authors argued that their method is more scalable. Could you a) test on larger graphs, and b) measure the improved speed?

### Questions
- Equation (3) does not accurately represent all possible MPNNs, even when restricting $g$ to be an MLP and $f$ to result from multiplication with a GSO. Specifically, using an MLP from $\mathbb{R}^k$ to $\mathbb{R}^k$ does not trivially extend to a graph signal of dimension $\mathbb{R}^{n \times h}$. It seems that the authors are actually performing matrix multiplications from the right with learnable matrices, and using more than one. Similarly, in Proposition 3.1, the representation in Equation (12) is assumed before the proof begins, which is actually what the authors aim to prove.
- In Proposition 4.3, what is the variable $m$ summing over? The entire proposition lacks clarity, and it appears there is no novelty compared to the existing results from Gama et al.
- The authors claim that Equation (6) is permutation equivariant, which does not seem to be correct. It is only equivariant in expectation, similar to the random positional encodings introduced by Sato et al. (2020).
- What are the contributions to the stability and expressivity analysis? It seems that older results are merely being reused.
- Did the authors follow the standard experimental setup? For example, in the ZINC dataset, it is customary to use a parameter budget of 500K parameters.
- The authors argued that their method is more scalable. Could you a) test on larger graphs, and b) measure the improved speed?

## Additional Comment:

The primary novelty appears to be the use of random features as input for learning positional encodings, instead of typically using eigenvectors. It appears that PEARL is a specific variant of SPE where the equivariant sequence-to-sequence function is replaced by a point-wise function applied to eigenvalues. This point-wise function is simply a learnable polynomial, offering the clear advantage of not requiring eigen decomposition, thus making it faster and more memory-efficient. However, it is unclear whether this approach improves or decreases expressivity or leads to better stability or generalization bounds. Notably, the out-of-distribution (OOD) generalization in the experiments appears to be better for the SPE positional encodings. However, it is not clear why since SPEs are also stable. Finally, I want to direct the authors to "Spatio-Spectral Graph Neural Networks" by Geisler et al., which also uses spectral and spatial layers in GNNs.

Recommendation:
I recommend rejecting the paper in its current form and suggest that the authors improve the clarity of the manuscript (in terms of novely and also writing) and better integrate it into the existing literature.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work aims to propose a new framework for graph positional encoding that is expressive, scalable, stable and generalizable. The proposed framework generates positional encoding as aggregated outputs of GNNs with random or basis inputs, which is then fed into downstream GNNs for performance evaluation. The proposed framework is accompanied with theoretical arguments and empirical verification on graph regression and classification tasks.

### Strengths
1. Good motivations: the topic of graph positional encoding is a significant direction, which requires sufficiency, efficiency and easiness for generalization.
2. The proposed method is easy for plug-in: it proposes positional encodings as aggregation of GNNs' outputs with random/basis inputs, which are quite simple with standard implementation.
3. The empirical performance of the proposed method is comparable with SPE methods in Table 2, but it is much more efficient than SPE in Table 1 for larger graphs.
4. Different choices of input with random or basis are good with a consideration of different scales of problems, with the sample size of random inputs examined in Figure 2.

### Weaknesses
Major:
1. A key assumption is missing in proposition 3.1: GSO $S$ is required to be symmetric if we want to use the decomposition in line 105. So  the random walk matrix in Eq(2) does not satisfy this condition. The use of a spectral decomposition implicitly assumes a symmetric matrix, and this is not generally true for the graph shift operator (GSO) defined by a random walk matrix. This oversight undermines the theoretical justification for the proposed method when applied to non-symmetric GSOs.
2. in line 463, it might be a little sudden to claim ''SPE can be efficiently implemented by B-PEARL with lower computational and memory complexity'': the argument seems coming from the comparison of numbers in Table 2. Although the numbers of SPE and the proposed methods are close, it would be better to conduct more careful analysis to provide such a ''subset'' or ''equivalence'' relationship between the methods, or refer to remark 5.1 for theoretical insights. The claim of superior efficiency requires a more rigorous justification, possibly by analyzing the computational graphs of both methods and demonstrating a clear reduction in operations or memory usage, rather than relying solely on empirical comparisons.
3. in line 60 of introduction, the paper argues '' stability is particularly crucial for out-of-distribution generalization'', which is one of the main motivations for this work. However, such a benefit of size generalization is not provided with enough evidence in this work. Actually in Table 3, the OOD-size performance is not improved by stable methods like SPE and the proposed R-PEARL. The connection between stability and OOD generalization is not clearly demonstrated in the experiments. While the motivation is valid, the empirical results do not consistently support the claim that the proposed method provides better OOD generalization due to its stability, especially when compared to other stable methods like SPE.
4. in line 397, a 9-layer MPNN is used for experiments, which is relatively deep in the practice of GNNs. Could you please reveal how depth will impact the empirical results? Meanwhile, such a deep method with random inputs is quite similar to power iterations for eigenvalues, so some discussion between these might be helpful. The choice of a 9-layer MPNN is not justified, and the impact of depth on the results is unclear. Given the similarity to power iterations, it would be beneficial to discuss the convergence properties of the proposed method in relation to the number of layers and the potential for the method to converge to dominant eigenvectors, which could influence the quality of the positional encoding.

Minor: 
1. in line 133-134, the definition of $F_{l-1}$ is not clearly stated, and it should be $F_l$ for $X^{(l)}$.
2. in line 293, it seems to be ''a consequence of Prop 4.1'' instead of 4.2

### Questions
Please see the above major concerns.

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
Beforehand, I want to say that I am not familiar with this topic.

The paper introduces PEARL, a novel framework for learnable positional encodings (PEs) in graph representation learning. It addresses the limitations of eigenvector-based methods by leveraging message-passing Graph Neural Networks (GNNs) to compute efficient and expressive PEs. The authors propose initializing node attributes with random or basis vectors to ensure both expressiveness and permutation equivariance. The framework is validated through comprehensive theoretical analysis and empirical evaluation, showing significant improvements in scalability and performance compared to existing methods.

### Strengths
1. Innovative Approach: The use of message-passing GNNs as nonlinear mappings of eigenvectors is a novel contribution, enabling efficient computation of PEs.
2. Comprehensive Analysis: The paper rigorously proves the stability, expressiveness, and computational efficiency of PEARL.
3. Empirical Validation: Experimental results demonstrate that PEARL outperforms traditional methods on various graph classification and regression tasks while maintaining lower computational complexity.
4. Scalability: The framework is designed to handle large graphs efficiently, addressing a critical limitation of eigenvector-based methods.
5. Theoretical Contributions: The analysis of sample complexity and stability provides a solid foundation for the proposed approach.

### Weaknesses
1. Limited Discussion on Practical Implications: While the theoretical and empirical results are robust, the paper could benefit from a deeper discussion on the practical applications of PEARL in real-world scenarios. The paper lacks specific examples of how PEARL could be used in different domains, such as drug discovery, social network analysis, or recommendation systems. A more detailed discussion on the types of graphs where PEARL would be most effective, and where it might face limitations, would be beneficial.
2. Complexity of Understanding: The mathematical depth and complexity might pose a barrier to readers unfamiliar with the intricacies of GNNs and spectral graph theory. The paper could benefit from more intuitive explanations of the core concepts, perhaps through the use of illustrative examples or diagrams. The current presentation assumes a high level of prior knowledge, which may limit the accessibility of the work.
3. Comparative Baselines: Although the paper includes several baselines, additional comparisons with more recent or diverse methods could strengthen the empirical validation. Specifically, it would be useful to see comparisons against methods that utilize different types of positional encodings, or those that are specifically designed for large-scale graphs. The current set of baselines, while comprehensive, could be expanded to provide a more complete picture of PEARL's performance.
4. Ablation Studies: While ablation studies are presented, further exploration of the impact of different initialization strategies and pooling functions on performance could provide more insights. For example, the paper could investigate the sensitivity of PEARL to different random initialization schemes, or explore the use of different pooling functions beyond simple mean pooling. A more detailed analysis of these design choices would be valuable.

### Questions
The paper introduces PEARL as a scalable and efficient alternative to eigenvector-based positional encodings. While the theoretical advantages are well articulated, can the authors provide more detailed insights or case studies on how PEARL performs in real-world applications or large-scale industrial settings? Specifically, what types of graphs or domains would benefit the most from the proposed method, and are there any observed limitations in practical deployments?

### Soundness
2

### Presentation
3

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
This work proposes PEARL, using the output of Message Passing Neural Network (MPNN) with noise/basis node feature as input for PE. PEARL's stability, sample complexity, and expressivity are further analysis. Experiments illustrates that PEARL achieves good performance in graph tasks.

### Strengths
1. Good performance on ZINC dataset.
2. Detailed analysis of R-PEARL.

### Weaknesses
1. The abstract states that this work investigates positional encodings (PEs) for graphs based on four key criteria: stability, expressive power, scalability, and genericness. However, the focus is primarily on eigenvector-based PE, and the analysis is limited to the authors' proposed method, R-PEARL, regarding these criteria. A more comprehensive theoretical analysis and comparison with other PEs are needed.
2. The rationale behind using Message Passing Neural Networks (MPNNs) to generate PEs is not clearly explained. Proposition 3.1 appears to be trivial, as graphs (represented by adjacency matrices and node features) can be bijectively mapped to eigenvectors, eigenvalues, and node features. Consequently, all graph functions, including PEs, can be seen as functions of eigenvectors when parameters include both eigenvalues and eigenvectors. Therefore, the justification for choosing MPNNs as eigenvalue function over other graph models is not evident.
3. While the expectation of R-PEARL is equivariant, the actual R-PEARL method is not, due to the involvement of noise.
4. Theorem 4.3 and the claim that "our proposed PE framework is well-suited for large-scale graphs" are questionable. The proof of Theorem 4.3, specifically Formula (45), includes the maximum degree of the graph, which is latter included in $\beta$. Considering $\beta$ as a constant is problematic because large social networks often contain nodes with high degrees, which would require more samples for accurate representation.
5. Most theoretical results (Theorem 4.3, Proposition 4.1, 4.2, 4.3) are direct corollories of previous conclusions.
6. The experimental section is limited to four datasets. To strengthen the validity of the results, additional datasets should be included as in [1].
7. The PE is used in conjunction with a GNN backbone, but the backbone for PEARL appears to be fixed across all experiments. To demonstrate the broad applicability and ensure a fair comparison among different PEs, experiments on PEs with different GNN backbones should be added, as recommended in [2].

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
2

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
The paper deals with learning effective positional encodings for graph structures to be used in conjunction with graph neural networks. Previously, eigenvectors and random features  have been used for such posiitonal encodings. In this paper, the authors first observe that the message passing GNNs are akin to non-linear functions of eighenvectors and therefore can be used to learn positional encodings which can function similarly to eigenvector-based positional encodings. Following this observation, they propose PEARL, a GNN based approach which takes in random feature inputs on the graph (without accompanying node-features) and learns to output encodings which can be interpreted as positional encodings. To preserve permutation invariance upto the expectation, they use multiple IID samples and aggregate with equivarient sample statistics. The authors show that such a approach preserves  stability, improves expressive power, scalability, and genericness. Experiments are presented to validate the approach.

### Strengths
1. The paper addresses an important problem of learning positional encodings on graphs
1. The approach of learning PEs as outputs of GNN with random feature inputs on the graph is well-motivated with the observation discussed that GNNs are non-linear functions of eigenvectors of graph shift operators.
1. The paper is well-written and presentation is good.

### Weaknesses
1. Essentially, the outputs of GNNs on random input features are taken as positional encodings. However, there are no loss functions to bias learning towards such functions. While it is clear the random inputs along with GNN message passing, can encode the relative positional information and the supporting evidence that GNNs compute non-linear maps of eigenvectors of adjacency/laplacians, further regularizing loss functions may be able to make the learning encodings better. One example is enforcing the encodings of each node to be orthogonal to other encodings. This could potentially improve the quality and interpretability of the learned positional encodings, ensuring that each node's representation captures unique and non-redundant information. The lack of such constraints might lead to less efficient or less discriminative encodings.

2. It is not clear to me why eigenvectors need to be used in place of random features for smaller sized graphs. Empirical results to show the difference between eigenvector inputs and random inputs for smaller sized graphs would be beneficial. Specifically, it would be useful to see a comparison of the performance and stability of the learned encodings when using eigenvectors versus random features as input, particularly in scenarios where the graph size is limited. This would help clarify the conditions under which each approach is most effective.

3. Important works are missing in related work and comparison experiments. In experiments, Random GNN [1] and PF-GNN [2] are not compared, which are highly related to using randomization to improve expressive power and in a way, compute positional encodings. The absence of these comparisons makes it difficult to assess the relative advantages and disadvantages of the proposed method compared to existing approaches that also leverage randomization for graph representation learning. A more comprehensive experimental evaluation is needed to properly contextualize the contribution of this work.

4. The paper claims that the proposed approach is more expressive. Then empirical results showing it is needed. For example, identifying graphs  not identifiable by GNNs would be useful. A comparison with random GNN[1] and PFGNN[2] would be beneficial in this respect. Demonstrating the method's ability to distinguish non-isomorphic graphs that are indistinguishable by standard GNNs would provide strong evidence for its claimed expressiveness. This could involve using benchmark datasets specifically designed for testing graph isomorphism capabilities.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
