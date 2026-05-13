# OLGA: One-cLass Graph Autoencoder

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
One-class learning (OCL) comprises a set of techniques applied when real-world problems have a single class of interest. The usual procedure for OCL is learning a hypersphere that comprises instances of this class and, ideally, repels unseen instances from any other classes. Besides, several OCL algorithms for graphs have been proposed since graph representation learning has succeeded in various fields. These methods may use a two-step strategy, initially representing the graph and, in a second step, classifying its nodes. On the other hand, end-to-end methods learn the node representations while classifying the nodes in one learning process. We highlight three main gaps in the literature on OCL for graphs: (i) non-customized representations for OCL; (ii) the lack of constraints on hypersphere parameters learning; and (iii) the methods' lack of interpretability and visualization. We propose \textbf{\underline{O}}ne-c\textbf{\underline{L}}ass \textbf{\underline{G}}raph \textbf{\underline{A}}utoencoder (OLGA). OLGA is end-to-end and learns the representations for the graph nodes while encapsulating the interest instances by combining two loss functions. We propose a new hypersphere loss function to encapsulate the interest instances. OLGA combines this new hypersphere loss with the graph autoencoder reconstruction loss to improve model learning. OLGA achieved state-of-the-art results and outperformed six other methods with a statistically significant difference from five methods. Moreover, OLGA learns low-dimensional representations maintaining the classification performance with an interpretable model representation learning and results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents OLGA, a new method for one-class learning on graphs. OLGA uses a graph autoencoder and a novel hypersphere loss function to learn node representations and classify them as interest or non-interest. OLGA also learns low-dimensional representations that enable interpretability and visualization of the learning process and the data. The paper evaluates OLGA on eight datasets from various domains and sources, and shows that it outperforms six other methods.

### Strengths
1. The manuscript introduces a novel end-to-end method for one-class learning on graphs called OLGA, which combines a graph autoencoder and a hypersphere loss function.
2. The manuscript proposes a new hypersphere loss function that encourages the interest instances to approach the center of the hypersphere.
3. The manuscript evaluates OLGA on eight datasets from various domains and sources, and shows that it outperforms six other methods.

### Weaknesses
1. The motivation for using GAE is not well explained. Specifically, it's unclear how the graph autoencoder's reconstruction loss directly addresses the challenges of one-class learning on graphs, such as learning from limited positive examples and distinguishing between in-class and out-of-class nodes. The paper should elaborate on the specific properties of the GAE that make it suitable for this task, beyond simply stating it's a constraint. A more detailed discussion should be added explaining how the GAE loss helps to solve the three gaps introduced in the abstract.
2. It is unclear how the function in Eq.5 is derived. The paper provides the function, but lacks a clear explanation of the mathematical reasoning behind it. The choice of this specific function and its relation to the hypersphere loss should be justified.
3. For the two reconstruction losses, A contains topology information of unlabeled nodes, setting a reconstruction loss on A^u could be repetitive and meaningless. The authors should give more explanation on why the reconstruction loss is applied to both labeled and unlabeled nodes, and what specific information each loss is intended to capture. The current explanation is insufficient to justify the use of two separate reconstruction losses.
4. The writing should be improved. Many discussions are hard to understand, lacking clarity and precision. The paper needs a thorough revision to ensure that the concepts and methods are presented in a clear and accessible manner.
5. A mathematical problem formulation would be helpful. The paper lacks a formal definition of the one-class learning problem on graphs, making it difficult to understand the objective and the proposed solution in a rigorous way.

### Questions
NA

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors concentrate on One-Class Learning (OCL) with the aim of addressing three specific limitations. They introduce an innovative one-class graph autoencoder named OLGA, which serves as an end-to-end graph learning framework. Additionally, the authors propose two distinct loss functions to encapsulate the interesting instances.

### Strengths
1.The author provides a statement about OCL.
2.The author identifies and discusses three issues in OCL.

### Weaknesses
1. In the introduction, the author claims, "Existing methods often assume high-dimensional latent spaces, which can hamper interpretability." However, this statement lacks a basis in terms of theoretical or experimental analysis. As a result, the subsequent experimental results do not provide evidence that high-dimensional features are significantly worse or even better than low-dimensional features, such as OCGAN, OCGAT, and OCSA. This raises doubts about the accuracy of the author's description.

2. There is a scarcity of comparative methods in the paper, and recent research is underrepresented. Out of the six comparative methods, three are derived from the same paper.

3. The third motivation point mentions "the methods' lack of interpretability and visualization." Nevertheless, the paper itself lacks corresponding theoretical explanations.

4. The paper lacks a complexity analysis of the proposed method, both theoretically and experimentally.

5. In Formula 8, there are three hyperparameters. Unfortunately, the paper does not include a sensitivity analysis for these parameters, making it difficult to intuitively gauge the effectiveness of the design module.

6. The innovation of the author's method appears limited, as it seems to be based on GAE and two MSE losses.

### Questions
See Weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors introduce OLGA, an end-to-end One-class Graph Autoencoder that combines a novel hypersphere loss function with a graph autoencoder reconstruction loss to encapsulate interest instances and achieve state-of-the-art results, outperforming several methods.

### Strengths
- One-class learning is a very fundamental problem for graph-related problems, and exploring one-class learning on graphs is a very interesting topic.
- The paper is well-organized and easy to be understood.

### Weaknesses
 - Adding a diagram in the introduction to illustrate the significance and importance of one-class learning on graphs would be beneficial.
- The lack of innovation is a concern, as the author has primarily combined two conventional and commonly used loss functions. The hypersphere loss, while encouraging examples towards the center, lacks a novel approach in its formulation. Specifically, it does not address the potential for collapsing all embeddings to a single point, which is a common issue with such losses. The combination of the hypersphere loss with the graph autoencoder reconstruction loss, while potentially useful, does not present a significant conceptual leap, and the paper does not provide a strong justification for why this specific combination is superior to other possible combinations.
- I suggest the author provide detailed statistics about the dataset, including the number of nodes, edges, and the distribution of node features, to allow for a more thorough understanding of the experimental setup.
- The authors could provide an anonymous GitHub link to ensure the reproducibility of the paper, including the code and the specific hyperparameter settings used for each experiment.
- Due to the popularity of large language models, it is advisable for the authors to consider using Large Language Models (LLMs) or other encoders to initialize text representations for comparison. The current approach may not be leveraging the most advanced techniques for feature initialization, which could impact the overall performance of the proposed method.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed that a reconstruction-based loss function can improve one-class learning models in determining whether an instance belongs to the target class or not. The proposed method introduced in this study is termed "One-Class Graph Autoencoder" (OLGA).

### Strengths
1. When combining different loss functions,   this paper considers the scale regularization.
2. The paper conducts a comprehensive review of the relevant literature.

### Weaknesses
1. Many claims in the article have not been reasonably explained.

     a. The rationale behind the benefits of low-dimensional node representations within the OCL context for enhancing model interpretability is not adequately elucidated. The paper vaguely mentions interpretability but does not detail how lower dimensions directly translate to better understanding of the learned representations, especially considering that graph data is inherently high-dimensional. The paper should clarify the specific mechanisms through which lower dimensions aid in interpreting node embeddings and how these interpretations can be used in practice.

     b. The reason behinds the integration of the autoencoder framework into one-class classification models is not well illustrated. In page 5, authors wrote "If we only use the L1, all instances will converge towards the center, regardless of whether they are interest nodes, as the GNN aggregates representations at each iteration. Therefore, we propose multi-task learning with additional loss functions to assist our main task solved by L1, combining the loss functions." Such explanation is too high-level, and the underlying mechanism why autoencoder is beneficial to one-class classification is still unclear. The explanation does not sufficiently justify why an autoencoder is the appropriate choice for preventing collapse, rather than other regularization techniques. A more thorough analysis of why the reconstruction loss is beneficial in this context is needed, perhaps by detailing how it prevents the trivial solution of mapping all inputs to the same point.

      c. The paper presents the challenge of combining GAEs and hypersphere loss functions, which it appears to resolve by simply combining these functions without a detailed explanation of the challenges involved. The paper should delve into the specific conflicts that arise when optimizing these loss functions simultaneously. For example, how does the optimization landscape change when both losses are present? What are the potential gradient conflicts and how does the proposed method address these conflicts beyond simply stating that they are combined?

      d. The paper attempts to address the hypersphere collapse problem in one-class classification using low-dimensional representations, but this paper does not sufficiently discuss the advantages of lower dimensions compared with existing solutions. Furthermore, the explanation of why lower dimensions enhance interpretability remains unclear. The paper should provide a comparative analysis of how its low-dimensional approach compares to other methods that address hypersphere collapse, such as those using margin-based losses or alternative regularization techniques. The paper should also elaborate on how low-dimensional representations are directly linked to improved interpretability, providing concrete examples of how these representations can be visualized and understood.

2. The writing of the article is not professional enough. In introduction, author wrote "encapsulating the interest class around a single point in the learned space with a minimum-radius hypersphere can yield erroneous results for unseen data".   However,  this paper does not respond it in the introduction section, even in the paragraph discussing the proposed method OLGA.
3. The choice of comparison algorithms in the paper is not sufficiently novel. For example, the OCSAGE method, which uses GraphSAGE, was introduced in 2018, and deep one-class classification was also proposed in the same year. This lack of innovative comparison algorithms diminishes the paper's contribution.
4. In the reference literature, there are too few articles from conferences such as ICLR, NeurIPS, and ICML. A more comprehensive reference selection from these esteemed conferences would enhance the paper's credibility.

### Questions
Please refer to the weakness section.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
