# AutoG: Towards automatic graph construction from tabular data

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent years have witnessed significant advancements in graph machine learning, with its applications spanning numerous domains. However, the focus has predominantly been on developing powerful models, often overlooking a crucial initial step: constructing suitable graphs from common data formats, such as tabular data.
This construction process is fundamental to applying graph-based models, yet it remains largely understudied and lacks formalization.
Our research aims to address this gap by formalizing the graph construction problem and proposing an effective solution. We identify two critical challenges to achieve this goal: 1. The absence of dedicated benchmarks to formalize and evaluate the effectiveness of graph construction methods, and 2. Existing automatic construction methods can only be applied to some specific cases, while tedious human engineering is required to generate high-quality schemas. 
To tackle these challenges, we present a two-fold contribution.
First, we introduce a benchmark to formalize and evaluate graph construction methods. 
Second, we propose an LLM-based solution, AutoG, automatically generating high-quality graph structures without human intervention.
The experimental results demonstrate that the quality of constructed graphs is critical to downstream task performance, and AutoG can generate high-quality graphs that rival those produced by human experts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method to convert table data into a graph by leveraging a large language model (LLM). 
The primary features are as follows:
- Detailed design of LLM prompts.
- Comprehensive definition of basic actions (Section 4.2).
- Quantitative oracle using GML, potentially effective for this task (Section 4.3).

### Strengths
- S1: The proposal introduces a carefully devised LLM prompt (Appendix D)
- S2: The evaluation experiments show that the proposal significantly outperforms existing techniques and achieves results close to those of manual graph generation.
- S3: Section 3.1 identifies C4 (graph variations) , which is indeed an important challenge.
- S4: Generating co-author relationships as edges is definitely effective for node classification of homophily graphs.

### Weaknesses
 - W1: The problem definition is not explicitly stated.

- W2: Although the proposal utilizes carefully designed LLM prompts, it relies on standard techniques in LLMs like few-shot learning and chain of thought (CoT), making the novelty unclear.

- W3: While the quantitative oracle evaluating GML with a validation set seems effective, Table 4 suggests the oracle may not be essential. The GML results are highly dependent on the choice of label selection (e.g., venue vs. year), making the conclusion "LLMs can generate good candidates merely based on prior knowledge" is not reasonable. We encourage the authors more detailed discussions here.

- W4: Concerning the five challenges in Section 3.1, if the schema is normalized, issues like C2 and C3 (1NF) seem unlikely to arise. Additionally, the proposal only addresses node classification and does not handle tasks like link prediction or node clustering, so C5 appears to be an overstatement.

- W5: There is a lack of evaluation on speed improvements. Section 4.2 claims the high cost of JTD, and Section 4.3 mentions a design for potential speed-ups, making such an evaluation essential.

### Questions
Questions
- Is the problem defined as follows?  The input: relational data, GML for downstream tasks, and records and class labels for training and validation data. output: transformed graph data from the relational data.

Comments
- The term "RGAT" may be incorrect and should be "GAT." The cited paper (Veličković et al., 2017) refers to GAT.
- Using GML models suited for homophilic graphs (e.g., RGCN, GAT) as an oracle may be unsuitable for tasks on heterophilic graphs. This issue could be addressed by selecting GML models tailored to heterophilic graphs as the oracle.

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
The authors provide a method for automatically converting relational tables into a knowledge graph. They forego manual engineering by using an LLM approach. First, the LLM is instructed to create a schema, restricted by calling certain functions. Then, an oracle is used to provide feedback for this schema generation. That feedback is then again used by the generator.

### Strengths
* The general observation is an important one: the conversion of tabular data into graph form cannot be taken for granted. Existing graph benchmarks based on tables avoid the hard cases.
* The setup with an LLM to generate candidates is pretty nice. Restricting its generation freedom using function calls is a good idea as well.

### Weaknesses
 * It remains unclear how well this method performs on the long tail. The evaluation is averaging over many cases, but the results might be dwarfed by very common ones.
* The paper only considers very well behaving rectangular tables (relational database style), with column names and all. Even the data types are given. There is also a lot of web tables around with large datasets available. One could certainly question whether te chosen setting is realistic, now.
* The datasets are pretty small.
* Citations for relational graph learning are to 2023< papers, while this has been studies for 10+ years.
* It is not clearly argued why relational graphs are most suitable. Other formalisms like hyper-relational ones might be more appropriate.
* I suggest removing the claim of surpassing human experts. It is not clear whether all schemas from the experts are  such that they were made as an ideal schema for a GNN architecture / the specific task.

minor:
*  treate each ->  treated each

### Questions
* Recently, Alivanistos, et al. (2024) presented "The Effect of Knowledge Graph Schema on Classifying Future Research Suggestions". That work suggests that the classification performance depends on the chosen schema. Is this the same you observed in the current work? Should one consider existing schemas or let the model figure this creation out as well?
* Much of the idea is clearly supported by argument, the choice of the oracle as a discriminator and the heuristics one gets out of that are rather arbitrary. It is not clear whether these are the best options. How do you know?
* You only use RGCN and GAT, both of which are rather GNN based learning methods. Would you expect other methods to behave similarly? Why?

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
This paper focuses on the impact of automatic graph construction from input tabular data on downstream Graph Machine Learning (GML) tasks. It introduces a benchmark for evaluating graph construction and proposes AutoG, an automated graph construction method.

### Strengths
1. In the field of GML methods for tabular data, this paper is the first to concern graph construction evaluation, and introduces a benchmark for it.
2. The authors identify five key challenges in converting tabular data into graphs and proposed AutoG, an agent-based approach. They design actions for the large language model (LLM) to utilize its prior knowledge for augmenting graph construction. Additionally, they implement a feedback mechanism to calibrate the LLM's output based on the validation performance of downstream GML tasks.
3. The paper is well-structured, clearly expressed, and includes detailed information.

### Weaknesses
My main concern is with the "metrics used in the proposed benchmark for evaluating the conversion of tabular data into graphs (T2G)." As stated in line 216, the authors use the performance of fixed GML models (RGCN, RGAT) trained on the generated graphs for quantitative evaluation. However, as a benchmark for T2G, it should be independent of specific downstream GML methods. Thus, the evaluation is limited to these two models and lacks generalizability to all GML models. Until it is demonstrated that the conclusions from RGCN and RGAT apply to all GML models, both the benchmark and the experimental findings in this paper remain constrained. The use of only RGCN and RGAT as evaluation anchors is problematic because these models might not capture the full spectrum of graph properties that other GML models could leverage. For example, Graph Transformers or models using message passing with different aggregation functions might be sensitive to different graph characteristics. This narrow evaluation scope could lead to a benchmark that favors graph structures optimized for RGCN and RGAT, rather than a more generally applicable graph representation.

Furthermore, the paper does not explore the potential for the constructed graphs to be evaluated based on intrinsic graph properties, such as homophily, clustering coefficients, or degree distributions. These metrics could provide a more direct measure of the quality of the graph structure, independent of any specific downstream task. The lack of such analysis makes it difficult to understand the characteristics of the generated graphs and how they might impact the performance of various GML models. The current evaluation approach conflates the quality of the graph with the performance of specific models, making it hard to isolate the impact of the T2G method itself.

### Questions
1. Can you prove that the conclusions from RGCN and RGAT apply to all GML models?
2. Have you considered proposing a better metric to evaluate the constructed graph itself? Furthermore, if the constructed graph is closely tied to specific downstream tasks, does that suggest that T2G might be more suitable as a data augmentation module to be explored with specific GML models, rather than as a standalone benchmark?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a benchmark for constructing graphs from tabular data as well as an LLM-based method that generates graph schemas without human intervention.

### Strengths
(S1) The paper proposes a direction to tackle the interesting problem of transforming tables into graphs.

(S2) The benchmark datasets are a valuable addition to the community.

(S3) The paper performs several experiments to show the effectiveness of the method on various data.

### Weaknesses
 (W1) The paper does not consider a rich database literature in mining functional dependencies [1,2] and data profiling [3] that automatically extracts dependencies among table columns. These methods can be used to generate more refined schemas that can solve some of the challenges expressed in Section 3.1. This method should be part of the experimental evaluation.

(W2) After having mined uniqueness constraints and functional dependency, one can apply conventional data normalization to further remedy the problems highlighted in challenges C2, and C3. From this standpoint, it is not clear why a mine-and-normal step would not solve most of the issues.

(W4) The benchmark only contains fairly small datasets with, at most 8 tables, for example, PTE has 38 tables (https://relational-data.org/dataset/PTE). There are also several datasets here: https://relational-data.org/

(W5) Another challenge, not specifically addressed by the current paper, is missing values and NULL values. Can the proposed method cope with those? If not, why?

(W6) Clarity: The paper is, in many parts hard to follow. Here are some examples

- Figure 2: It is not clear what flexible design is and what the prompt looks like
- at least two columns as FK and no PK: provide an example
- chain of augmentation: please state what it is
- validation set performance: explain

(W7) 488: How does the method ensure that the test data is not included in the pre-training of the LLM? Do you have access to the training data?

(W8) The paper relies on LLMs that are subject to changes. Does it mean that one has to adapt the method to a different LLM every time?

(M1) I encourage the authors to use citations from published sources while in the current draft, several citations are from arXiv

(M2) Typos:

- 133: Treate
- 277: LLM generates / tends → LLMs generate / tend
- 282: single-steply

(M3) In modelling the graph $G={V, E}$ it seems that the nodes are just a set of types as $\mathcal{V}=\bigcup_{v\in V} \mathcal{V}^v$. This definition does not seem standard for Heterogeneous graphs. There should be a set of nodes, each with a type (or a set of types) and a set of edges among the nodes.

### Questions
The authors should carefully address the concern about the relationships with previous database research (W1, W2) and the assumptions of the method (W5). Moreover, the inclusion of a larger, more challenging set of datasets would also be encouraged (W4).

### Soundness
2

### Presentation
2

### Contribution
2
