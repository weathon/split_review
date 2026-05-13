# What Can We Learn from State Space Models for Machine Learning on Graphs?

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Machine learning on graphs has recently found extensive applications across domains. However, the commonly used Message Passing Neural Networks (MPNNs) suffer from limited expressive power and struggle to capture long-range dependencies. Graph transformers offer a strong alternative due to their global attention mechanism, but they come with great computational overheads, especially for large graphs. In recent years, State Space Models (SSMs) have emerged as a compelling approach to replace full attention in transformers to model sequential data. It blends the strengths of RNNs and CNNs, offering a) efficient computation, b) the ability to capture long-range dependencies, and c) good generalization across sequences of various lengths. However, extending SSMs to graph-structured data presents unique challenges due to the lack of canonical node ordering in graphs. In this work, we propose Graph State Space Convolution (GSSC) as a principled extension of SSMs to graph-structured data. By leveraging global permutation-equivariant set aggregation and factorizable graph kernels that rely on relative node distances as the convolution kernels, GSSC preserves all three advantages of SSMs. We demonstrate the provably stronger expressiveness of GSSC than MPNNs in counting graph substructures and show its effectiveness across 11 real-world, widely used benchmark datasets. GSSC achieves the best results on 6 out of 11 datasets with all significant improvements compared to the state-of-the-art baselines and second-best results on the other 5 datasets.
Our findings highlight the potential of GSSC as a powerful and scalable model for graph machine learning. Our code is available at %\url{https://anonymous.4open.science/r/GSSC-5ED8}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work extends the state space models (SSMs) from sequence modeling to the domain of  graph-structured data. By tailoring SSMs for graphs, the proposed model (GSSC)
can capture long-range dependencies and overcome the limitations of Message Passing Neural Networks (MPNNs) while offering efficient computation addressing the quadratic computation of the graph transformers. To preserve the permutation equivariance in the graphs, it outlines a method for designing a permutation-invariant kernel for convolution operations on graphs. Furthermore, it extends to a data-dependent version of the proposed model by defining a selection mechanism for graph-structured data. The proposed model demonstrates provably stronger expressiveness than MPNNs and Graph Spectral Convolution in counting graph substructures.

### Strengths
- The paper provide a method to customize the recursion in the SSMs for graphs,
- It proposes a method for designing a permutation-invariant kernel for efficient global convolution operations on graphs.
- The paper demonstrates provably stronger expressiveness of the proposed model for 3-paths and 3-cycles and also for 4-paths and 4-cycles.

### Weaknesses
1. The distinction between the proposed model (equation 4) and linear graph attention is minimal. It is known, even prior to Dao & Gu (2024), that SSMs can be represented as linear attention. The global convolution representation used here is also an equivalent form of SSMs. Additionally, the use of positional encodings is not novel, as it is a feature used by other works such as GraphGPS, which propose a general framework for transformer-based models and can adopt their approximations like Performer and linear attention. 

2. The presentation requires improvement, and some claims need to be more precise. For example:  
   - a. at line 143, the *Computational efficiency and parallelism*,  The text should clarify that SSMs like S4, when represented as global convolution (equation 2), they can leverage the FFT algorithm to result in parallel and efficient quasi-linear complexity. Parallel scan is used for the recurrence form of equation (1) under certain conditions (employed by data-dependent SSMs like Mamba), which also results in O(n log n) computation but offers parallelization.  
   - b. The statement that the kernel should be factorizable as a dot product to be permutation-invariant (line 127),  needs revision. The dot product between absolute position representations is one way to achieve translation invariance. Reference [2] offers alternative methods, like cross-correlation, to achieve translation invariance in kernels for global convolution using translation-equivariant functions.  
   - c. The factorized form in line 259 is not equivalent to the data-dependent convolution presented in the preceding line.   
   - d. The new positional encodings in equation (6) are positional encodings of all nodes but utilize only the features of node u (as it is a function of $x_u$ only). Lines 267 and 267 need correction to reflect this.   
   - e.The text should elaborate on how $\phi()$ in  in eqn (5)  is modeled to be a permutation equivariant function and capture interactions between frequencies.




3. **Insufficient Empirical Studies**: The literature review lacks citations for many state-of-the-art models, and the experimental section lacks comparisons to them.  
   - Since the proposed model is compared with GSC and Linear Graph Transformers in the paper, it is essential to include their performance comparison in the experimental section (particularly in Table 2 for graph substructure counting, where the proposed model is expected to show superior expressiveness). 
   - Comparisons with newer models like Spatial-Spectral GNN [1] and Polynormer [3] are also necessary. 
   - Additionally, comparisons against other SSM-based models (Graph-Mamba I and II), GSC, Linear Graph Transformers and recent models in Tables 2 and 3 are important to demonstrate the proposed model empirically.

### Questions
1. Please address the aforementioned concerns
2. Some typos:  
   - Equation 5 (line 201): the first term doesn’t require parentheses. 
   - “reply on” -> rely on in line 268 and 346. 
   - There are duplicate references for Behrouz & Hashemi, 2024 


Conclusion:

While the proposed idea is appealing, and I acknowledge its potential impact, I am not sure that the paper is ready for ICLR in its current form. Therefore, I am hesitant to fully support acceptance but I am willing to increase my score if the concerns and questions are addressed.

**References:**    
[1] Geisler, S., Kosmala, A., Herbst, D., & Günnemann, S. (2024). Spatio-Spectral Graph Neural Networks. arXiv preprint arXiv:2405.19121.  
[2] M. Karami, A. Ghodsi, Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling .” In Thirty-eighth Conference on Advances in Neural Information Processing Systems 2024.  
[3] Deng, Chenhui, Zichao Yue, and Zhiru Zhang. "Polynormer: Polynomial-Expressive Graph Transformer in Linear Time." The Twelfth International Conference on Learning Representations.

Update 1: added references

### Soundness
2

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
The paper introduces the Graph State Space Convolution (GSSC) method, an extension of State Space Models (SSMs) to graph data. GSSC utilizes global permutation-equivariant set aggregation and factorizable graph kernels based on relative node distances as its convolution kernels.

### Strengths
I have found the paper well written and self-contained. I think a non-expert could find most of the information in the paper, and I appreciate this aspect.

 Figures 1 and 2, which demonstrate the problem domain and architecture, are interesting and easy to read. I commend the authors for their explicit effort in making these illustrations clear and informative.

The insights are didactical and well communicated. The conclusion given by the experiments looks interesting and valuable for future practitioners, while I think a synthesis would be beneficial for the reader.

### Weaknesses
Despite these merits, I have the following concerns about the paper.

1- While there is a careful analysis of the different design decisions/performance tradeoffs, I feel that there is only a limited understanding about what are the properties of the Architecture that lead to these decisions/performance differences.

2-  Scalability Concerns: The paper acknowledges the challenge of scalability for larger graphs. To address this, the authors could explore methods for optimizing the computational complexity of the GSSC architecture.

3- Weak experimental study:  The paper lacks experimental evaluation of the Graph State Space Convolution (GSSC) method on heterophilic datasets. This omission is significant as such studies are crucial to assess GSSC's performance with heterophilic data and its robustness against issues like over-squashing and over-smoothing, which are common challenges in graph data analysis.

### Questions
(i) For the scalable version of the architecture when you proposed using the first k eigenvectors, how does the method address the issue of missing eigenvectors in the middle and end of the spectrum?

(ii) What are the main challenges in extending GSSC to heterophilic graphs, and do you have any preliminary insights on how these challenges could be addressed?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Machine learning on graphs often uses Message Passing Neural Networks (MPNNs), but these have limited expressive power. Graph State Space Convolution (GSSC) is proposed as a new method that extends State Space Models (SSMs) to graph data, overcoming these limitations and demonstrating superior performance on benchmark datasets. GSSC achieves good results on many datasets and offers a scalable solution for graph machine learning.

### Strengths
1. **Novelty**: Unlike previous methods that design SSM variants on graphs, this paper approaches the problem from the perspective of separable distance kernels on graphs. This idea is both novel and interesting.

2. **Comprehensive Evaluations**: The experimental section of this paper covers synthetic datasets, real datasets, and computational efficiency benchmarks, providing a comprehensive evaluation.

### Weaknesses
1. **Experimental Design**: My main concern is that the model evaluated in the experiments is a hybrid of GSSC and MPNN, without showing the performance of GSSC alone. This makes it difficult to assess the independent contribution of GSSC, affecting the judgment of its effectiveness. I strongly recommend that the authors provide experimental results for the GSSC module alone, which will help readers understand the primary contributions of GSSC.

2. **Baseline Selection**: In Section 5.1, the authors compare only with MPNN, without providing baseline comparisons with SSM or GT, which seems insufficient. Considering the authors claim that GSSC is a replacement module for Transformers, I suggest adding comparisons with other models that include shortest path information (such as high-order MPNN) or global information (such as Graph Transformer). Moreover, the current baselines are mainly single MPNN models, and comparing them with the hybrid model (GSSC+MPNN) seems unfair.

3. **Inconsistency in Model Architecture**: In Section 5.1, the authors use selective GSSC, but it is not used in other benchmarks.If different architectural variants of the model are used in the experiments, I advise clearly indicating this in the tables. Additionally, the authors claim that GSSC without selective is already powerful enough, does this imply that using selective GSSC would be better? If so, it is recommended to provide relevant experimental results to support this argument. If selective GSSC is not used due to other disadvantages (such as computational efficiency), it would be beneficial to discuss this further in the paper. Generally, a unified model architecture is more attractive than one that requires adjustments across different benchmarks.

### Questions
1. Compared to other graph SSM works, this study indeed offers a novel perspective. In your opinion, what advantages does this new viewpoint provide over other methods? How do your experiments support these advantages?

2. The title is "What Can We Learn from State Space Models for Machine Learning on Graphs." Could you elaborate a bit more on other graph SSM models / SSM model on other domins, and compare them with GSSC?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Graph State Space Convolution (GSSC), an extension of state-space models to graph-structured data. The authors emphasize GSSC’s capability for capturing long-range dependencies in linear time and demonstrate competitive performance across several benchmarks.

### Strengths
1. The paper achieves competitive performance compared to SOTA methods.
2. The paper proposes a novel approach in extending state-space models to graphs.
3. The paper provides a plausible framework for capturing long-range dependencies efficiently.

### Weaknesses
My main concerns relate to the complexity claims, specifically:
1. **Layer Complexity vs Expressivity:** The paper states that the complexity of a GSSC layer is “… $O(nmd)$    where $n$ is the number of nodes and $m$, $d$ are hidden and positional encoding dimension.” (239-240) This means that a GSSC layer has $O(|V|)$ complexity   . Consequently, GSSC is in general *incapable of examining every edge in the graph*, unlike MPNNs with $O(|V|+|E|)$ complexity, such as GINE [1]. Although the authors prove that GSSC is “more powerful than MPNNs” *in terms of the WL hierarchy*, the expressivity implications of not being able to examine every edge seems to be overlooked. Even preprocessing the graph to incorporate edge features into nodes, which itself requires $O(|E|)$ time, would still necessitate $m\in O(\frac{|E|}{|V|})$ to store these features without information loss, thus exceeding $O(|V|)$ complexity overall.
2. **Preprocessing Complexity:** The paper claims that finding the top $d$ eigenpairs with Lanczos methods has $O(nd^2)$ complexity (286-287). However, since sparse matrix-vector multiplication with the Laplacian matrix is necessary for Lanczos methods, the complexity per iteration would be at least $O(|E|)$, resulting in an overall complexity of at least $O(d|E|)$ to find $d$ eigenpairs. This exceeds the paper’s claim of $O(nd^2)$ preprocessing, and thus requires clarification.

Despite these concerns, the paper’s main contributions remain valid. I would appreciate if the authors could clarify these points during the rebuttal phase.

[1] https://arxiv.org/abs/1905.12265

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
