# In-Context Learning of Representations

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Recent work demonstrates that structured patterns in pretraining data influence how representations of different concepts are organized in a large language model’s (LLM) internals, with such representations then driving downstream abilities. Given the open-ended nature of LLMs, e.g., their ability to in-context learn novel tasks, we ask whether models can flexibly alter their semantically grounded organization of concepts. Specifically, if we provide in-context exemplars wherein a concept plays a different role than what the pretraining data suggests, can models infer these novel semantics and reorganize representations in accordance with them? To answer this question, we define a toy “graph tracing” task wherein the nodes of the graph are referenced via concepts seen during training (e.g., apple, bird, etc.), and the connectivity of the graph is defined via some predefined structure (e.g., a square grid). Given exemplars that indicate traces of random walks on the graph, we analyze intermediate representations of the model and find that as the amount of context is scaled, there is a sudden re-organization of representations according to the graph’s structure. Further, we find that when reference concepts have correlations in their semantics (e.g., Monday, Tuesday, etc.), the context-specified graph structure is still present in the representations, but is unable to dominate the pretrained structure. To explain these results, we analogize our task to energy minimization for a predefined graph topology, which shows getting non-trivial performance on the task requires for the model to infer a connected component. Overall, our findings indicate context-size may be an underappreciated scaling axis that can flexibly re-organize model representations, unlocking novel capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates how LLMs form representations for novel concepts during in-context learning. Authors design a synthetic graph navigation task where the model has to learn from random walks between graph nodes are referenced as words from the training set (e.g. “apple”), meaning that the model has to learn a new representation for these words to accurately predict the next node in the graph traversal. They refer to this problem as “in-context graph tracing”.

Authors then study the hidden representations formed by LLMs as they learn this task in-context, visualizing their first few principial components. They find that, after a certain number of examples, the model abruptly re-organizes the representation space in a way that facilitates the graph traversal task, as learned from the context. They also find cases where the in-context learned representations do not dominate  the first principal components, but they are still present in subsequent components (e.g. 3rd and 4th in Figure 3). Finally, authors demonstrate a connection between the process of in-context learning of node representations and a form of graph energy minimization.

### Strengths
- The paper investigates an interesting phenomena that may further our understanding of how LLMs learn in-context;
- The paper includes a simple and easy-to-reproduce experiment that can facilitate future analysis of LLM representations;
- The paper is generally well-written, if a bit unconventionally structured. It follows the natural flow of an investigation into how representations change during in-context learning;
- Authors go to reasonable length to ablate alternative hypotheses in their analysis.

### Weaknesses
 - The paper focuses primarily on just a single model: Llama 3 8B. It is possible that some of the authors findings reflect not the general ability of LLMs, but an artifact of Llama 3 models, or a property of models of this particular size. The paper would arguably be improved if authors verify their findings on other models: both of different size (e.g. 1B / 70B / 405B), different family (gemma, qwen, mistral, opt, etc) and of different type (e.g. instruct vs non-instruct). Failing that, authors could at least clarify this as potential limitation.

- The part where authors argue that the in-context learning is linked to Dirichlet energy minimization is interesting, but (arguably) a bit contrived. As authors explain, energy minimization would be solved simply by assigning all nodes to the same embedding. Perhaps it would be best to further explore the analogy with graph embedding learning as a possible alternative? (e.g. distance-preserving embeddings or similar)

- While I don't count this as a significant weakness, the paper could arguably be improved by further exploring *what* in the model causes the abrupt shift in representations. (e.g. is there any connection with induction heads, transformer circuits, or any other mechanism that could be responsible for the change).

### Questions
### Questions:

Note that these questions are mostly asked out of curiosity and do not affect my overall recommendation.

1. Authors found that there is a shift in concept representations after the model has seen enough context. **Could this mean that the model does not 'understand' early examples in real few-shot learning tasks?** For instance, could it mean that the model would not be able to reason about information if it requires understanding the sequences it 'read' before the change in representations? If yes, would it mean that the model would benefit from repeating the early in-context examples again, once the model 'understands' them?

2. What happens to the representation shift if you increase the number of concepts? Is there a point by which the model is no longer able to shift the structure properly to match the in-context 'meanings'?

### Minor:

L186 task-specific? (more popular with a dash)

L269 “Given that we empirically do not observe this to be the case, we can safely assume this trivial solution does not arise in our experiments.” - slightly odd phrasing - you make an observation about your experiments that implies an assumption about the same experiments? Perhaps it would be best to paraphrase / clarify the footnote.

### Soundness
3

### Presentation
4

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
This work designs a synthetic task to determine to what extent LLM  representations reflect in-context semantics rather than those observed during pre-training. 

To do this they generate a graph structure, where nodes consist of tokens that are highly likely to be observed during pre-training, but with novel dependencies defined by the structure. They then generate sequences following a random walk across the graph, which are fed into the LLM 'in-context' (i.e. without weight updates). They then show that the LLM can learn to organise its representations such that they mimic the underlying graph structure.

The task is to some extent adversarial, because the context neighbourhoods defined by the graph differ from the standard semantics of the tokens.

Evidence presented is both qualitative (using PCA) and quantitative (various measures for how well representations conform to the graph structure).

### Strengths
The paper is excellently written, and the figures clearly get the central findings across the reader, making it a pleasure to read. The experimental design is original, elegant and well crafted in order to probe the hypothesis. Finally, the findings provide an interesting insight in the abilities of LLMs to zeroshot generalise to novel connective structures.

### Weaknesses
The work relies quite heavily on PCA, which the authors admit can be somewhat misleading, though they provide theoretical justifications for why this reliance is valid.

On a higher level I am not quite sure whether the finding is particularly surprising. Natural language is supposed to have similar causal relationships modelled by dependency parses, and LLMs are capable of modelling it successfully. Moreover, they are supposedly able to learn to translate hitherto unseen languages entirely in context, which constitutes a much more complex graph than the ones assessed in this paper. As a result I am not certain that the findings expose a new capability. However, as stated in the strengths section the paper provides a very nice framework for understanding this capability which should bias towards acceptance.

### Questions
Have you or do you plan to extend your investigation to more complicated structures? The ones presented in the paper are fairly simple and it would be interesting if there are certain forms that are harder to represent.

### Soundness
3

### Presentation
4

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
The paper studies how the different representations are organized in a large language model’s internals. It reveals the sudden reorganization of representations as the context length increases.

### Strengths
1. The problem is interesting and important. 
2. The experiment results are interesting.

### Weaknesses
1. Lack of quantitative metrics of “the representations mirror the grid/ring structure” in Section 2: It is unclear how the PCA plot relates to the conclusions that the representations reflect the graph structure. The results in Section 4 may be helpful but require more discussion. Specifically, the connection between the visual patterns in the PCA plots and the underlying graph structure is not rigorously established. The authors need to provide a more concrete justification for interpreting the PCA visualizations as direct evidence of graph structure learning. For example, how do the specific eigenvectors of the PCA relate to the adjacency matrix or Laplacian of the graph? Without this, the PCA plots remain qualitative observations rather than quantitative evidence.
2. The use of PCA: The PCA is useful for visualization but is not convincing enough to draw rigorous conclusions. Without the manually added vertices in Figures 1(c), 2(c), and 3(c), the results are not interpretable. The reliance on manually added vertices to interpret the PCA plots is a significant weakness. The authors should demonstrate that the observed structures are inherent to the model's representations and not artifacts of the visualization process. A more robust approach would be to use quantitative metrics to directly measure the alignment between the model's representations and the graph structure, without relying on visual interpretation of PCA plots. The PCA plots should be considered a tool for visualization, not the primary source of evidence.
3. Equ. (4) is the probability of seeing one node with each token randomly sampled with replacement. It does not match the data generating procedure with the first token randomly sampled, and the remaining tokens are generated through random walk. The mismatch between the data generation process and the probability calculation in Equation (4) undermines the theoretical analysis. The authors should either modify the equation to accurately reflect the random walk process or provide a clear justification for why the current equation is still valid. The analysis should be based on the actual data generating process, not a simplified version.
4. I do not find the percolation theory fits here. Although Figure 8(b) indicates a strong result, it is unclear how y and x connect to the percolation theory. The connection between the observed transition in Figure 8(b) and percolation theory is not clearly established. The authors should provide a more detailed explanation of how the concepts of connectivity and critical thresholds in percolation theory relate to the in-context learning task. The current argument lacks a clear mechanistic link between the model's behavior and the theoretical framework of percolation.

### Questions
1. What is the layer of the figure 1(c)
2. In Section 3.1, it is claimed that a window of $N_w=200$ preceding tokens is included in the computation of representations. This number is greater than the minimal context length of Figure 2(b), which is 100.
3. How does Figure 3(c) prove that the LLM learns the in-context non-semantic structure?
4. The percolation relates to the thresholds of having an infinite connected path. Can authors explain more explicitly about its relation to the problem considered in the paper?

### Soundness
2

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
This paper explores how in-context learning in large language models allows a reorganization of representations to fit novel task-specific semantics. The authors propose to override the pre-trained meaning of the words, thus the internal organization of the LLM representations with a semantic extracted from the neighbor relationships of names placed at the nodes of a graph. 

The authors show that the LLM can internalize the graph structure learned in-context for sufficiently long input sequence sampled from the graph. They also connect their findings to energy minimization in graph and percolation theories, offering insight into how models might adapt internal representations based on in-context structure.

### Strengths
1. The paper presents a new task framework to study in-context reorganization in LLMs. It connects empirical observations with a theoretical foundation, connecting context-scaling with energy minimization. 

2. The graph tracing task using well-defined structures (grid, ring) is an effective method for observing changes in LLM representations in a controlled way.

3. The paper is well-written and relatively easy to follow; the main goal is clearly stated, and the set of experiments are spot-on

### Weaknesses
The findings are based only on the analysis of llama3 representations, so extending the experiment to at least another model class would be easy.

The constructed task is somewhat artificial, and it is not immediately clear how we can extend these findings in the domain of natural language.

### Questions
Have you tried to see if your finding holds also on models other than Llama?

l371, 372 Have you tried to check empirically if the coordinates z2 and z3 are aligned with the principal axis you find with PCA?

What does DGP stand for in line 249?

### Soundness
3

### Presentation
3

### Contribution
2
