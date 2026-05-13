# GyroAtt: A Gyro Attention Framework for Matrix Manifolds

- Decision: Reject
- Scores: 5, 6, 8, 6

## Abstract
Deep neural networks operating on non-Euclidean geometries, such as Riemannian manifolds, have recently demonstrated impressive performance across various machine-learning applications. Motivated by the success of the attention mechanism, several works have extended it to different geometries. However, existing Riemannian attention methods are mostly designed in an \textit{ad hoc} manner, \textit{i.e.}, tailored to a selected few geometries. Recent studies, on the other hand, show that several matrix manifolds, such as Symmetric Positive Definite (SPD), Symmetric Positive Semi-Definite (SPSD), and Grassmannian manifolds, admit gyro structures, offering a principled way to build Riemannian networks. Inspired by this, we propose a Gyro Attention (GyroAtt) framework over general gyro spaces, applicable to various matrix manifolds. Empirically, we manifest our framework on three gyro structures in the SPD manifold, three in the SPSD manifold, and one in the Grassmannian manifold. Extensive experiments on four electroencephalography (EEG) datasets demonstrate the effectiveness of the proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This article introduces an abstract framework to build attention layers
in various Riemannian manifolds. It generalizes a few previous works
suitable only for particular geometries, namely SPD, SPSD and
Grassmannian manifolds. The proposed layer are validated on somme EEG
classification tasks

### Strengths
A lot of technical work is presented in the article, it shows a mastery
of the mathematical tools and I am always supportive of this kind of
generalization work. The experiments are interesting and shows the
interest of Riemannian networks in particular applications.

### Weaknesses
The writing is still barely understandable, despite some improvements. The authors still try to cram too much content into the 10 pages, leading to a dense and difficult to follow narrative. While some details have been moved to the appendix, the main text still suffers from a lack of clarity and sufficient explanation. The excessive use of abbreviations, even with a provided list, disrupts the flow of reading and requires constant referencing back to the list. The description of the Karcher flow algorithm is still too brief, and its importance is not adequately highlighted in the main text. The line spacing issues, although improved, still contribute to the overall feeling of a rushed and not well-presented work.

It lacks a convincing motivation for the generalization. While the authors claim that it gives a better understanding of the existing layers, this is not clearly demonstrated. It is still unclear if the generalization applied to a particular geometry is strictly equivalent to the specific layer existing in prior work or if it's just similar. The explanation of the gyro homomorphism and its relation to linear layers is still not fully convincing, and a more detailed explanation is needed to justify this claim. The connection between the proposed framework and the existing literature on manifold learning is not clearly established, and a more thorough discussion is needed to highlight the novelty of the approach.

The precise architecture used in the experiments, while improved, still lacks sufficient detail. The description of the implementation details is still too concise, and more information is needed to reproduce the results. Although a figure of the architecture is provided, it does not fully clarify all the critical choices made at the implementation level. The discussion on the influence of the coefficient in the power activation layer, while moved to the appendix, still feels like a distraction from the main focus of the paper. The metric used for SPD experiments in Table 4 is still not clearly stated in the main text, and it is necessary to provide this information for the sake of reproducibility.

### Questions
It lacks a convincing motivation for the generalization. Does it give a
better understanding of the existing layers ? Does it permit to build
new layer for other manifolds ?

It's not clear for me if the generalization applied to a particular
geometry is strictly equivalent to the specific layer existing in prior
work or if it's just similar.

What is the precise architecture used in the experiments ? There is a
short description but more details must be given since a lot of tricky
and critical choices are made at this level. It is not sufficient to put
5 lines in a paragraph called "Implementation details". In addition to a
precise description, a drawing of the architecture is often a good idea.

I am not sure if the long discussion on the influence of the coefficient
in the power activation layer is really necessary. In general it's
certainly interesting but I have the feeling it's not the priority here
due to the lack of space.

What is the metric used for SPD experiments in Table 4 ?

### Soundness
4

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
2

### Summary
The paper presents GyroAtt, a novel attention framework on matrix manifolds that unifies various manifold-based attention mechanisms. The framework generalizes attention operations to gyrovector spaces, incorporating specific implementations for SPD, SPSD, and Grassmannian manifolds. Experiments show competitive performance on EEG datasets compared to traditional methods, demonstrating both the versatility and effectiveness of the GyroAtt framework.

### Strengths
1. The proposed GyroAtt framework provides a unified approach to manifold-based attention mechanisms, which helps in applying attention across various matrix manifolds.
2. The framework’s flexibility is validated by empirical performance across multiple gyro structures, offering a robust approach for EEG data applications.
3. The GyroAtt framework shows strong results on EEG datasets, outperforming or being competitive with existing methods, which is promising for non-Euclidean data.

### Weaknesses
1. Although the framework generalizes attention, it primarily applies existing forms, such as SPD, Grassmannian, and SPSD manifolds, limiting exploration into novel or unknown structures. The framework's reliance on known manifold structures means it does not inherently facilitate the discovery of new geometric representations, which could be a significant limitation for datasets that may benefit from less conventional manifold structures. This constrains the potential for the framework to adapt to data with unique underlying geometries.
2. As noted in Tables 4 and 5, the performance improvements are not consistently significant across datasets, and some results fall within the margin of error. The lack of consistent and statistically significant improvements across all datasets raises concerns about the robustness of the proposed method. The standard deviations reported in the tables suggest that the observed performance differences may not be reliable, which limits the practical impact of the results.

3. There are symbols introduced without clear definitions in the text, like the commutator [A, B] used in line 92 and its meaning only clarified much later in line 146. A glossary or early explanation could improve clarity. The delayed definition of the commutator and other symbols hinders the reader's ability to understand the core concepts of the paper. This lack of immediate clarity can make it difficult to follow the mathematical derivations and the overall logic of the proposed method.

4. Eq. (9) introduces an additional layer to increase model expressivity. Could the authors explain its functional relationship to the Gyro-attention block? Is this added primarily to improve empirical performance, or does it hold a theoretical grounding within the framework? The functional relationship between the additional layer in Eq. (9) and the Gyro-attention block is not clearly explained, leaving ambiguity about its role. It is unclear whether this layer is primarily an empirical adjustment or if it has a deeper theoretical justification within the framework. This lack of clarity makes it difficult to assess the true contribution of this component.

5. Symbols like \downarrow in Theorems 5.1 to 5.4 and parentheses in Equation (16) may be specialized to certain subfields but are not well-defined within the text. Briefly introducing these notations in the initial sections would enhance readability. The use of specialized notations without proper introduction creates a barrier for readers unfamiliar with these conventions. This lack of clarity can hinder the accessibility of the paper and make it difficult for a broader audience to understand the theoretical contributions.

6. In Table 4, GyroAtt-SPSD achieves the best performance, while GyroAtt-SPD is better in Table 5. Could the authors provide an intuitive explanation for why different variants excel on different datasets? The inconsistent performance of GyroAtt-SPSD and GyroAtt-SPD across different datasets suggests that the framework's effectiveness is highly dependent on the specific characteristics of the data. An intuitive explanation for these differences is needed to understand the practical implications of the method.

7. The standard deviations in Tables 4 and 5 suggest that performance differences may not always be statistically significant. The high standard deviations in the results raise concerns about the statistical significance of the reported performance differences. This limits the confidence in the practical impact of the proposed method.

8. Understanding the limitations and computational complexity of GyroAtt would be useful for researchers considering this method for resource-intensive applications. Could the authors include an analysis of these aspects, particularly comparing them with baseline methods? The lack of analysis on the computational complexity of GyroAtt limits the practical applicability of the method, particularly for resource-constrained environments. A comparison with baseline methods would be necessary to assess the trade-offs between performance and computational cost.

### Questions
1. Given that the framework mainly specifies known forms (SPD, Grassmannian, SPSD), can GyroAtt be extended to unknown or less conventional structures? If not, could the authors clarify the contribution of GyroAtt as primarily a unifying formulation rather than a framework for discovering new structures ?

2. There are symbols introduced without clear definitions in the text, like the commutator [A, B] used in line 92 and its meaning only clarified much later in line 146. A glossary or early explanation could improve clarity .

3. Eq. (9) introduces an additional layer to increase model expressivity. Could the authors explain its functional relationship to the Gyro-attention block? Is this added primarily to improve empirical performance, or does it hold a theoretical grounding within the framework?

4. Symbols like \downarrow in Theorems 5.1 to 5.4 and parentheses in Equation (16) may be specialized to certain subfields but are not well-defined within the text. Briefly introducing these notations in the initial sections would enhance readability.

5. In Table 4, GyroAtt-SPSD achieves the best performance, while GyroAtt-SPD is better in Table 5. Could the authors provide an intuitive explanation for why different variants excel on different datasets?

6.  The standard deviations in Tables 4 and 5 suggest that performance differences may not always be statistically significant.

7. Understanding the limitations and computational complexity of GyroAtt would be useful for researchers considering this method for resource-intensive applications. Could the authors include an analysis of these aspects, particularly comparing them with baseline methods?

### Soundness
3

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
5

### Summary
The main contributions of this paper can be summarized as follows:

Proposal of a General Gyro Attention Framework (GyroAtt): This framework extends the classic self-attention mechanism to gyro spaces, making it applicable to various non-Euclidean matrix manifolds, such as Symmetric Positive Definite (SPD), Symmetric Positive Semi-Definite (SPSD), and Grassmann manifolds. GyroAtt unifies the construction of attention mechanisms on these manifolds. Within this framework, the authors introduce gyro homomorphisms and geodesic-based attention mechanisms to enable feature transformations and similarity calculations. The use of geodesic distances for attention scoring and weighted Fréchet mean aggregation ensures that the attention mechanism preserves the manifold's geometric structure.

Validation of the Framework’s Effectiveness Across Multiple Matrix Manifolds: The authors tested the GyroAtt framework on SPD, SPSD, and Grassmann manifolds and conducted experiments on four EEG datasets, demonstrating its excellent performance and adaptability.

### Strengths
The paper is clearly structured, and the mathematical framework and definitions used are rigorous and precise. In terms of methodological design, the GyroAtt framework has strong mathematical generality, overcoming the limitations of specific geometric spaces and being applicable to a variety of non-Euclidean geometries. Additionally, the implementation of GyroAtt makes full use of abstract and concise gyro homomorphisms and geodesic-based attention computation, and employs weighted Fréchet mean for aggregation, achieving a balance of simplicity and mathematical rigor.

This paper represents a continuation and innovation in modeling with gyrovector space on the SPD manifold. This approach is the first to construct an attention networks on the SPD manifold using the gyrovector space approach.

### Weaknesses
Primary Concerns: In the experimental section, the proposed method outperforms almost all existing methods. However, do these results reflect the best performance of the compared models? What parameters and training methods did the authors choose for these models? This question is significant because some alternative tuning may improve the performance of certain baseline models, especially in the case of several deep learning models.

Additionally, it is suggested that the authors provide more focused experimental comparisons with MAtt and GDLNet, rather than general comparisons with other models. These two models also involve optimizations of the attention mechanism on SPD manifolds and are thus the most directly comparable to the proposed method. The current design of the experiments may dilute the focus on these two models.

Possibly the most critical point: The attention structure proposed in this paper is based on scalar multiplication and vector addition in gyrovector space, rather than traditional Euclidean operations. While this network architecture differs fundamentally from the design concepts of existing methods, it also makes it challenging to directly interpret its superior performance through comparisons. Other neural networks on the SPD manifold, while not using the gyrovector space approach, have still effectively designed network structures suited for SPD matrix-valued inputs, processing non-Euclidean data by operating in the tangent space. Although the mapping between the tangent space and the manifold may introduce some error, the overall framework, being based on deep neural networks, has strong robustness that typically adjusts for such discrepancies. Based on your experimental results, there does appear to be an overwhelming performance advantage for the gyrovector space approach. This leaves me feeling puzzled. Hence, could the authors further clarify from a theoretical or practical perspective why the type of your model based on gyrovector space offers performance advantages?

The reason I refer to your results as an 'overwhelming‘ performance advantage is that even a few percentage points of average improvement on the EEG dataset is very substantial. Generally, there are always some subjects who perform poorly, which lowers the overall average. If such an 'overwhelming‘ performance advantage truly exists, then whether we should continue along the current research path focused on SPDNet for model development (such as the Graph-CSPNet and TSMNet mentioned in the paper) is a question worth further discussion. What are your thoughts on this? In terms of computational complexity and scalability, does your method also have advantages over the SPDNet pathway, or are there some potential drawbacks?

### Questions
1. Conduct further ablation studies or direct comparisons focused on GyroAtt, MAtt, and GDLNet, examining their performance and computational efficiency. Highlight key differences in both effectiveness and processing requirements to clarify where each model excels.

2. Provide a detailed analysis comparing the computational complexity and scalability of GyroAtt with SPDNet-based methods (maybe also be called the tangent space approach). Include a theoretical analysis or an empirical study directly comparing gyrovector operations with tangent space operations to illustrate where and why performance gains occur. Perform an ablation study that substitutes gyrovector operations with equivalent Euclidean or tangent space operations to isolate the unique impact of the gyrovector method. 

3. Explain the connection between Equation (7) and the classic attention function. Are there any other possible approaches?

##Open Questions##:

What insights do you have on future research directions, including possible integrations or enhancements of SPDNet-based methods with gyrovector space concepts? Are there suggestions for future research that could merge the strengths of both approaches or further improve GyroAtt?

### Soundness
3

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
4

### Summary
This article presents a framework that unifies attention mechanisms on different manifolds such as the SPD manifold using gyrovector spaces. The main operations of the attention mechanism are focused on feature transformation, attention calculation and aggregation. The key contribution is in the feature transformation part, where they introduce gyro homomorphisms. Relationships between the gyrovector space with other manifolds were implemented. They showed promising results on four EEG datasets.

### Strengths
- The key contribution is the introduction of gyro homomorphisms and its application to different manifolds and metrics. Their work specifically defines seven homomorphisms and their proofs were provided.
- Good results on the experiments.

### Weaknesses
 - Details on the model structure are not clear.

 - The paper focuses on the attention mechanism, but the overall model structure used in the experiments remains unclear. For example, when the network operates on the SPD (GyroAtt-SPD), the attention mechanism appears identical to that in the Matt [1] network. It would be helpful if the authors clarify the reason for performance differences observed in the experiments between these two networks.
- One clear difference is in the activation function. Are there any other similar ones? It would be helpful if the authors include a comparison between their GyroAtt network and other non-Euclidean, attention-based networks used in the experiments. Such comparisons would greatly assist readers in better understanding of the presented results.
- Table 6 shows the model's performance across different power parameters (a parameter of the activation function). To better understand the contribution of the activation function itself, could the authors add a row for each experiment showing results without any activation function?
- At the standard Euclidean attention mechanism, a single head is barely used, as the empirical contribution of using multi-head is well known. Also, can the proposed attention mechanism be easily extended to multi-head configurations in different geometries?

### Questions
- The paper focuses on the attention mechanism, but the overall model structure used in the experiments remains unclear. For example, when the network operates on the SPD (GyroAtt-SPD), the attention mechanism appears identical to that in the Matt [1] network. It would be helpful if the authors clarify the reason for performance differences observed in the experiments between these two networks.
- One clear difference is in the activation function. Are there any other similar ones? It would be helpful if the authors include a comparison between their GyroAtt network and other non-Euclidean, attention-based networks used in the experiments. Such comparisons would greatly assist readers in better understanding of the presented results.
- Table 6 shows the model's performance across different power parameters (a parameter of the activation function). To better understand the contribution of the activation function itself, could the authors add a row for each experiment showing results without any activation function?
- At the standard Euclidean attention mechanism, a single head is barely used, as the empirical contribution of using multi-head is well known. Also, can the proposed attention mechanism be easily extended to multi-head configurations in different geometries? 

[1 ] Yue-Ting Pan, Jing-Lun Chou, and Chun-Shu Wei. MAtt: A manifold attention network for EEG decoding. In NeurIPS, pp.31116–31129, 2022.

### Soundness
3

### Presentation
2

### Contribution
2
