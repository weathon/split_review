# Graph Transformers Dream of Electric Flow

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
\noindent We show theoretically and empirically that the linear Transformer, when applied to graph data, can implement algorithms that solve canonical problems such as electric flow and eigenvector decomposition. The input to the Transformer is simply the graph incidence matrix; no other explicit positional encoding information is provided. We present explicit weight configurations for implementing each such graph algorithm, and we bound the errors of the constructed Transformers by the errors of the underlying algorithms. Our theoretical findings are corroborated by experiments on synthetic data. Additionally, on a real-world molecular regression task, we observe that the linear Transformer is capable of learning a more effective positional encoding than the default one based on Laplacian eigenvectors. Our work is an initial step towards elucidating the inner-workings of the Transformer for graph data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the capabilities of the linear Transformer when applied to graph data, particularly its ability to implement algorithms for core graph tasks without explicit positional encodings. The authors demonstrate that the linear Transformer, which uses the graph incidence matrix as input, can solve canonical problems like electric flow computation and eigenvector decomposition. Key contributions include explicit configurations for weight matrices, error bounds for each task, and empirical results validating theoretical findings on synthetic data.

### Strengths
**Originality**: This paper introduces a novel use of a linear Transformer, to perform core graph algorithms like electric flow and eigenvector decomposition without explicit positional encodings. 

**Quality**: The paper offers rigorous theoretical analysis with explicit weight constructions and error bounds for each algorithm.

**Clarity**: The paper is well-organized, clearly written, and enjoyable to read.

### Weaknesses
1. Since the paper’s contribution is primarily theoretical, providing a proof sketch under the main results would be highly beneficial. Additionally, a more detailed description of the weight matrices, including their sparsity patterns and how they relate to the graph structure, would enhance clarity. Specifically, detailing how the weight matrices are constructed to implement the core graph algorithms would be crucial for reproducibility and understanding.

2. The theoretical results, while interesting, are not particularly surprising given the use of a linear Transformer. The paper does not adequately address the question of whether similar results could be achieved with other architectures, such as GNNs, which are also capable of processing graph data. A more thorough discussion of the architectural choices and their implications for the observed results is needed.

3. The practical impact of the proposed approach is unclear, as the empirical results are limited compared to numerous existing works. For instance, the performance on the ZINC dataset is significantly lower than the state-of-the-art, with an error approximately twice as large. The paper should include a more comprehensive evaluation, comparing against a wider range of baselines and datasets to demonstrate the practical applicability of the linear Transformer for graph-based tasks.

### Questions
Please address the points raised in the previous section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a simplified (linear) Transformer architecture (no softmax activation in self-attention layers) and use it to show (theoretically and empirically) that it can implement graph algorithms. In particular they present a series of lemmas providing bounds in approximating the solution to problems like flow and heat kernel computation, finding resistive embeddings and performing eigenvalue decomposition (assuming specific weight matrices). Their input encodings include the incidence matrix representation of the graph and then the approximate solution will land in a subset of columns in the output encodings' matrix,  after passing through a a number L of transformer layers (where L is decided by the target approximation error). A parameter efficient variant is also presented. The linear transformer is tested on a series of small graph instances of the problems (e.g. of the order of 10 nodes and 20 edges) and for learning a positional encoding (PE) for a molecular regression task.

### Strengths
- The idea is novel and appealing: using a transformer to compute the solution to a graph problem as part of the latent vectors in its node output representations adds another level of applicability of transformers well beyond language understanding or generation.

- Lemmas are well organized, follow similar themes and the narrative is smooth and clear.

### Weaknesses
 - Removing the nonlinear softmax terms from standard transformer architecture, facilitates analysis but severely impacts the power of the model.

- Complexity of the approach is prohibitive: it can be O(n^4) and this explains their experimentation with very small synthetic graphs. Parameter efficient implementation is promising, but still the original idea is far from being scalable and thus practically testable beyond a couple of tens' of graph nodes. The core issue is that the naive implementation requires a parameter count of O(m^2), where m is the number of edges, which can scale to O(n^4) for dense graphs. This makes it impractical for larger graphs, and the experiments are limited to very small graphs, which raises concerns about the generalizability of the approach. While a parameter-efficient version is presented, the practical scalability of the approach remains a major concern, as the theoretical analysis is primarily based on the naive implementation.

### Questions
- How would the analysis be impacted if nonlinearity in self-attention was re-introduced? In order to "understand, at a mechanistic level, how the Transformer processes graph-structured data" (lines 32-33), we are expected to remove only non-essential elements of Transformer architecture (and nonlinearity seems to be a critical one). The linearity in the Transformer, means that if its operations are expanded for a number of layers we'll reduce to a simple matrix operator.

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
4

### Summary
The paper shows that Linear Transformers (and their variant) using the incidence matrix can implement canonical problems, such as electric flow and subspace iteration. While the contribution is mainly theoretical, the authors also empirically validate their findings, and further show that on existing molecular datasets the linear transformer is capable of learning better performing positional encodings than standard laplacian eigenvectors.

### Strengths
The results are interesting. I particularly appreciated the structure of the paper, in which experimental results are shown after their corresponding theoretical claims instead of having them all the end, which highlights the connection between the presented theory and the experimental results.

### Weaknesses
W1. Generally speaking, I think the impact of the paper tends to be a bit limited. This is especially true because the considered architecture (linear Transformers), and in particular its variant which includes an L2 normalization, is not widely used. The main implication I can see is to use the variant of the linear transformer in place of existing predefined positional encodings, and therefore as an additional component of a bigger architecture.

W2. I find a bit confusing that the authors claim that the input to the Transformer is only the graph incidence matrix, without any other positional encoding (Lines 11-13), while for instance for the subspace iteration $\Phi_0$ is required to be some arbitrary column-orthogonal matrix. I think -- depending on the graph -- $\Phi_0$ might need to be a positional encoding to ensure all columns are orthogonal (note that if $\Phi_0$ is a random matrix then it is a positional encoding [Srinivasan and Ribeiro, 2020]). I think the authors need to clarify this point and adjust accordingly in the entire paper.

### Questions
Q1. Can you elaborate on the practical implications of your findings (see W1)?

Q2. I think the eigenvectors you converge to have sign/basis ambiguities derived from the choice of $\Phi_0$. How do you deal with these ambiguities? Do you perform sign flipping at every forward pass?

Q3. I think denoting by $d$ the number of edges (Line 128) is a bit confusing, because $d$ is usually the embedding dimension. Also, in Equation 1, since $j= 1, \ldots, d$ is the first index of $B$, I think $B \in \mathbb{R}^{d \times n }$, but you wrote $B \in \mathbb{R}^{n \times d }$ (Line 132). Please clarify.

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
2

### Summary
The papers show theoretically and empirically that the linear transformer can approximate the hypothesis function space of several graph problem (electric flow and Laplacian eigenvector decomposition). The authors also conduct a real-world experiment on molecular regression, in which positional encoding outputs by transformers are adopted.

### Strengths
* The organisation of the paper is clear, it's easy to understand the main contribution of the paper. And mathematically, it's generally well-written.
* The idea of solving the traditional graph problem with a Transformer is novel. 
* For the proposed lemmas, the paper provides the relevant experiments which are quite nice.

### Weaknesses
 * My main concern is that since the neural network is a universe approximator, it's not surprising that it (in this paper, even it concerns linear Transformer, which is more like in a polynomial function) can solve approximate the hypothesis function space of several graph problems. I wonder how the lemmas shown in the paper can provide us with more useful information. Specifically, while the paper demonstrates that a linear transformer can approximate solutions to graph problems, it does not sufficiently address the practical implications or advantages of using this approach compared to traditional methods. The theoretical results, while mathematically sound, lack a clear connection to real-world performance benefits. It is unclear if the linear transformer offers any computational advantages or if it simply replicates the behavior of existing algorithms with a different architecture.
* The paper lacks a conclusion section.
* The real-world experiment concerns only the Laplacian eigenvector decomposition, it would be nice to have another for the electric flow. Furthermore, the experimental section could be strengthened by including more diverse datasets and a more thorough comparison against established graph algorithms. The current evaluation is limited in scope and does not fully demonstrate the general applicability of the proposed approach.
* While the paper concerns two graph problems: electric flow and Laplacian eigenvector decomposition, why the title mentions only the first one?

### Questions
* While the paper concerns two graph problems: electric flow and Laplacian eigenvector decomposition, why the title mentions only the first one?

### Soundness
3

### Presentation
3

### Contribution
2
