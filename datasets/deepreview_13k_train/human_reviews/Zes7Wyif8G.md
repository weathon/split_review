# KLay: Accelerating Neurosymbolic AI

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
A popular approach to neurosymbolic AI involves mapping logic formulas to arithmetic circuits (computation graphs consisting of sums and products) and passing the outputs of a neural network through these circuits. This approach enforces symbolic constraints onto a neural network in a principled and end-to-end differentiable way. Unfortunately, arithmetic circuits are challenging to run on modern AI accelerators as they exhibit a high degree of irregular sparsity.
To address this limitation, we introduce knowledge layers (\klay), a new data structure to represent arithmetic circuits that can be efficiently parallelized on GPUs.
Moreover, we contribute two algorithms used in the translation of traditional circuit representations to \klay and a further algorithm that exploits parallelization opportunities during circuit evaluations.
We empirically show that \klay achieves speedups of multiple orders of magnitude over the state of the art, thereby paving the way towards scaling neurosymbolic AI to larger real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new data structure, called knowledge layers (KLay), that allows the efficient parallelization of arithmetic circuits, which appear to be a major computational bottleneck in a specific type of neuro-symbolic AI approach.

### Strengths
First, the paper tackles an important challenge in neuro-symbolic AI, where scalability is still one of the major roadblocks for their general application. The achieved speed-ups of the proposed KLay on both CPU and GPU seem very promising.  Finally, the paper is well-written, and the methods are explained intuitively thanks to the use of appropriate figures and examples. This makes the paper accessible despite the methodology being quite involved.

### Weaknesses
1) Although the paper indicated in 3rd paragraph that it focused on a "particular flavor of neurosymbolic AI", i.e., a neural network feeding into probabilistic inference based on arithmetic circuits, it would be beneficial to reflect it explicitly in other parts, e.g., in the abstract, or a more specific title (Accelerating Arithmetic Circuits in Neurosymbolic AI), to be able to attract the right audience.

2) The actual "interface" and details between the neural network and the used arithmetic circuits remain largely a secret for readers(of course there are pointers to prior arts). It would be beneficial to open up and explain how exactly a neural network is interfaced to the arithmetic circuits, what are the assumptions and domain knowledge etc. at least for one of the tasks (e.g. MNIST addition) in an appendix.

3) Unclear impact on end-to-end neuro-symbolic approaches. While the introduction clearly states the dominance of the “symbolic” part, this dominance is not obvious in the experimental results. To my understanding, only the MNIST addition dataset tests the end-to-end timing results (including "neural"+"symbolic"). What are the contributions of the individual blocks? It would be great to quantify. Moreover, this is an example where the “neural” part is rather lightweight (simple digit recognition). How would this relation between “neural” and “symbolic” would look like in other tasks?

4) Explosion in the number of KLay Nodes on “Sudoku” and “HMLC”. On these two datasets, the number of KLay nodes increases by 1.5-2.7x. What is the reason for the increase? Could you please elaborate on it?

5) Insufficient introduction of datasets. It would be good to introduce all the datasets in the appendix so that the paper becomes more self-contained. In particular, the number of instances in Figure 6 is not introduced. Are they variables, clauses, or their combination? The mentioned range over 5 orders of magnitude is not visible in Figure 6.

### Questions
Answering the following questions/remarks could further improve the paper: 

1) Unclear impact on end-to-end neuro-symbolic approaches. While the introduction clearly states the dominance of the “symbolic” part, this dominance is not obvious in the experimental results. To my understanding, only the MNIST addition dataset tests the end-to-end timing results (including "neural"+"symbolic"). What are the contributions of the individual blocks? It would be great to quantify. Moreover, this is an example where the “neural” part is rather lightweight (simple digit recognition). How would this relation between “neural” and “symbolic” would look like in other tasks?
 
2) Explosion in the number of KLay Nodes on “Sudoku” and “HMLC”. On these two datasets, the number of KLay nodes increases by 1.5-2.7x. What is the reason for the increase? Could you please elaborate on it?
 
3) Insufficient introduction of datasets. It would be good to introduce all the datasets in the appendix so that the paper becomes more self-contained. In particular, the number of instances in Figure 6 is not introduced. Are they variables, clauses, or their combination? The mentioned range over 5 orders of magnitude is not visible in Figure 6.

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
3

### Summary
In this paper, the authors introduce a new data structure called knowledge layers (KLAY) designed to enhance the parallelization of Boolean circuit computation in neurosymbolic AI. They propose organizing d-DNNF circuits into layers and applying Merkle hashing for node deduplication, subsequently reducing circuit evaluation to indexing and scattering operations. Empirical results demonstrate that KLAY achieves speedups of several orders of magnitude compared to related works, providing a significantly more efficient implementation on GPUs.

### Strengths
1. The utilization of modern AI accelerators is crucial for advancing the field of neurosymbolic AI, enabling the development of large-scale models and tackling more complex problems that have been previously out of reach.
2. The ability to enable parallel computation on GPUs results in speedups of multiple orders of magnitude over current state-of-the-art approaches.

### Weaknesses
1. The background introduction to neurosymbolic AI is somewhat lacking, providing insufficient context. 
2. The experimental comparisons with state-of-the-art methods appear limited in scope compared to those discussed in related works.


### Questions
1. Although the title of Section 2 is "A Brief Primer on Neurosymbolic AI," it does not adequately explain the concept. It focuses primarily on the use of Boolean circuits in neurosymbolic AI and the challenges associated with their execution on GPUs. The significance and value of the work need to be more emphasized.
2. In Figure 6, there is a noticeable increase in slope when the number of instances exceeds 100. Does this behavior align with the authors' expectations regarding the linear time complexity of the algorithm?
3. In Table 1, a batch size of 1 is used. Is this a standard measurement practice? Could this choice potentially disadvantage non-parallel methods due to lower resource utilization?

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
The authors propose KLay, a data structure that enable parallel computing on irregular operations in knowledge layers of neurosymbolic AI.

### Strengths
The problem the authors formulated is clear.

### Weaknesses
The problem the authors formulated is clear.

The motivation needs further justification.



### Questions
I appreciate the authors effort in advancing neurosymbolic AI, and I personally am educated a lot from this work. Below are some questions, mainly regarding the motivation. 

1. "arithmetic circuits are ill-suited to be evaluated on AI accelerators..." Additional to GPUs/TPUs, AI accelerators also use ASICs and FPGAs as platforms, which are known to be capable of handling irregular operations. It would be insightful if the authors could discuss why arithmetic circuits are not suitable on these platforms. 

2. Could you please clarify if the neural networks are indeed separate from the arithmetic circuit? My understanding is that the leaf node values represent probabilities obtained from neural networks, and the subsequent operations involve arithmetic computations from the leaf nodes to the root node. Would it be practical to transfer the probability data to CPUs for post-order tree traversal after the neural network computations are performed on GPUs?

3. Could the authors provide insights into how the workload and time consumption of the arithmetic circuit compare to the upstream neural networks? Is there a typical percentage that represents this comparison?

4. Could the authors clarify if this approach can be considered an efficient method for parallel post-order tree traversal? If so, how does it compare to other efficient parallel algorithms for post-order tree traversal, if any exist?

5. Do current AI models possess the capabilities that neurosymbolic AI offers? What are the advantages compared to modern AI models do the authors anticipate that neurosymbolic AI can achieve? It would be very helpful if examples can be provided.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to tackle a numerical problem in the field of neurosymbolic AI. It allows to represent arithmetic circuits, used to model symbolic constraints, as a new kind of data structure, knowledge layers (KLay), on which computations can be performed more efficiently. Notably, computations on KLay can be performed in parallel, and thus exploit the full potential of AI accelerators such as GPUs. Empirical results show the superiority of these layers over existing methods in terms of computational speed.

### Strengths
+ The paper tackles an apparently difficult problem, which other authors had claimed is impossible to solve
+ It paves the way for a broader deployment of neurosymbolic AI models on standard deep learning hardwares such as GPU or TPU, while efficiently exploiting their potential
+ Empirical results are displayed in a clear way, showing the effective superiority of the proposed method over existing ones

### Weaknesses
No weekness to mention

### Questions
How are the KLay optimized ? Is optimization performed on the arithmetic circuits (that are emphasized as differentiable in the text) before representing them as KLay ? Could the authors address this question more explicitly would benefit to the completeness of the analysis.

### Soundness
4

### Presentation
3

### Contribution
3
