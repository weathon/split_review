# Persistent Similarity in Internal Representations of Large Language Models

- Decision: Reject
- Scores: 3, 6, 3, 5, 5

## Abstract
Understanding the decision-making processes of large language models (LLMs) is critical given their widespread applications. Towards this goal, describing the topological and geometrical properties of internal representations has recently provided valuable insights. For a more comprehensive characterization of these inherently complex spaces, we present a novel framework based on zigzag persistence, a method in topological data analysis (TDA) well-suited for describing data undergoing dynamic transformations across layers. Within this framework, we introduce persistence similarity, a new topological descriptor that quantifies the persistence and transformation of topological features such as $p$-cycles throughout the model layers. Unlike traditional similarity measures, our approach captures the entire evolutionary trajectory of these features, providing deeper insights into the internal workings of LLMs. As a practical application, we leverage persistence similarity to identify and prune layers, demonstrating comparable performance to state-of-the-art methods across several benchmark datasets. Additionally, our analysis reveals similar topological behaviors across various models and hyperparameter settings, suggesting a universal structure in LLM internal representations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel topological data analysis method based on zigzag persistence, which describes data undergoing dynamic transformations across layers within the large language models. The proposed persistence similarity is used to quantify the persistence and transformation of topological features throughout the model layers and provide insights to prune redundant architecture modules without significantly degrading performance. Experimental results indicate that the behavior of persistent topological features and their similarities are consistent across different models, layers, and choices of hyperparameters of the framework, suggesting a certain degree of universality in the topological structure of LLM representations.

### Strengths
- The paper is clearly written, making complex concepts accessible to the reader.
- The application of zigzag filtration to the internal representation of LLM is novel and insightful. 
- The approach to zigzag persistence is firmly rooted in theoretical foundations, providing a robust framework that enhances its applicability and relevance in the field.

### Weaknesses
 - The zigzag filtration, and persistence images are previously well-defined and existing. This raises concerns about the originality and depth of the theoretical and technical contributions presented in the paper.
- The performance gains over existing pruning methods, as shown in Table 1, appear marginal. Including a significance test would enhance the robustness of these findings. Specifically, the lack of statistical significance makes it difficult to ascertain whether the observed differences are due to the proposed method or random variation. The paper should include a rigorous statistical analysis, such as a t-test or ANOVA, to validate the performance claims.
- While the paper provides a geometric interpretation of the topological features, it is not clear how these features can be directly interpreted in the context of language models. The paper could benefit from a more in-depth discussion on the interpretability and implications of the observed topological properties. For example, what specific linguistic or semantic properties do the persistent homology features correspond to? Without this connection, the practical utility of the topological analysis remains unclear.
- The zigzag algorithm is computationally expensive, especially for large datasets and high-dimensional representations. The paper should discuss strategies to optimize the algorithm's performance and make it more scalable. The authors should provide a detailed analysis of the computational complexity of their approach, including both time and memory requirements, and compare it to existing methods. Furthermore, they should explore techniques such as approximation algorithms or parallel computing to mitigate the computational burden.

### Questions
- Figure 5 is somewhat unclear. Are the 10% (orange) segments included within the 20% (yellow) segments in most cases? The authors might consider a more effective visualization method to enhance clarity.
- Since other similarity measures can also characterize layer-wise behavior, what specific advantages does the proposed persistence similarity offer over these existing methods?
- What is the computational complexity of the proposed persistence similarity in comparison to other existing methods? 
- Can the authors provide insights or a high-level intuition regarding the consistent patterns observed in Figure 4?

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
2

### Summary
This paper uses zigzag persistence, an approach from TDA, to analyze the hidden representations of LLMs. With these tools, they track the evolution of topological properties of LLM hidden representations across layers. They make numerical observations such as increased persistence of topological features formed in later layers, and high similarity between representations in later layers. As an application, they prune layers based on persistence similarity.

### Strengths
1. Generally good and clear explanation of the requisite background and method.
2. Experiments show some insights into several open-weight language models of interest, across datasets that people care about (both for computing the metrics, and for testing downstream accuracy after pruning).

### Weaknesses
1. Besides the layer pruning application, the qualitative and quantitative insights from these topological features are not particularly interpretable or grounded. We can measure how the number of $k$-cycles evolves, but there are no interpretable quantities that come out of this, besides similarities between layers. To alleviate this, perhaps further discussion of motivation and related work (why should people use TDA tools to analyze internal representations), or interpretability work (what kind of 1-cycles form, and on what kind of data) could be interesting.
2. Utility in one downstream application (layer pruning) is questionable (the simpler methods from prior work do solidly and are not consistently outperformed).
3. The use of zigzag persistence in layer pruning only depends on the similarity matrix formed by the method. Other simple baselines could be considered for making similarity matrices.

### Questions
1. Have you looked at how topological features vary across different data samples / domains? For instance, are there any interesting data features that form between representations of tokens from certain programming languages?
2. Could you provide a bit more information on where the embeddings are extracted from (this is currently described in Section 4.1 as "each prompt is processed so that the last token is extracted at each normalization layer and the final normalization applied to the output layer.") Do you take the embedding before or after the normalization layer? Also, does this mean you take two embeddings from each block (one from the attention normalization, one from the MLP normalization)? Also, some discussion on how this compares to how other works extract LLM hidden representations  would be nice.

### Soundness
3

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
The paper uses zigzag persistence to empirically study LLMs.

### Strengths
Section 3 rigorously introduced the zigzag persistence.

### Weaknesses
The major problem of this paper is the lack of a problem. In fact, the word "problem" was not found in the whole paper at all.

Lines 520-521: "Our approach aims to provide a high-level geometrical and topological description of positional and relational changes across layers".

If this phrase in the conclusions should be considered a problem statement, then almost any empirical study using geometry and topology can fit this description.

Section 3 "Method" describes over 3 pages the known facts about zigzag persistence without even mentioning LLMs from the title of the paper.

The world "layer" appears in the paper 50+ times without a proper definition. Initially, this word is used in the context of neural networks but section 3 seems to assume that a layer is a cloud of unordered points in R^d, which is a standard input for computing persistence in TDA.

The "persistence similarity" introduced in (5) raises many concerns. First, the concept of "persistent similarity" appeared in the literature, e.g. https://www.intlpress.com/site/pub/pages/journals/items/cis/content/vols/0018/0004/a004/, but no past work on such similarity was cited.

More importantly, the denominator in (5) can vanish, which makes the persistence similarity S_p undefined. In this definition, it is still unclear if l_1,l_2 denote layers or point clouds because min/max of l_1,l_2 seem to be real numbers. If a layer is indeed a point cloud, the first metric axiom surely fails for l_1 and its translated image l_2, which have the same persistence.

Even if we consider point clouds under isometry, because persistence is an isometry invariant of a point cloud for standard filtrations of complexes, the first metric axiom also fails for infinitely many non-isometric point clouds, see J Applied Comp Topology 2024. Computational geometry has known much stronger isometry invariants of unordered point clouds for more than 20 years, see Boutin and Kemper, 2004.

Lines 402-403: "Note that the plot is not symmetric by definition (cfr. equation 5)".

Does it mean that the symmetry axiom fails?

The triangle axiom also seems unlikely to hold, so a proof is needed. If a distance fails the triangle axiom with any positive error, then results of clustering are not trustworthy as proved in https://ieeexplore.ieee.org/abstract/document/10574843? 

The form on "soundness" asked to evaluate "the technical claims, experimental and research methodology and on whether the central claims of the paper are adequately supported with evidence".

No technical claims were found, no words "claim", "proposition", "theorem" in the paper. Here are the comments on informal claims about contributions.

Lines 74-76: "We propose a new metric to measure which topological features persist across the layers of an LLM."

If persistence similarity is called a metric, proofs of metric axioms are expected. The original persistence already measures "which topological features persist".

Lines 77-79: "By identifying layers with high persistence similarity, we prune redundant layers without significantly degrading performance".

The adjective "redundant" appears in the paper without explanation. If performance refers to percentages in Table 1, they degrade by 10%. Is it not significant?

Lines 80-82: "Our findings indicate that the behavior of persistent topological features and their similarities are consistent across different models, layers, and choices of hyperparameters of the framework".

To make this claim meaningful, the words "consistent" and "consistency" should be properly defined.

### Questions
Lines 523-524: "This approach allows for effective model pruning by identifying and removing redundant layers without significantly compromising performance" 

All accuracies in Table 1 are between about 40% and 70%. Are these numbers enough to guarantee safety in real applications?    

How are outputs of LLMs converted into point clouds in the experiments? What is the meaning of persistence in terms of word tokens or other language-related concepts?

Should the review mention the previous work explaining LLMs as stochastic parrots at https://dl.acm.org/doi/abs/10.1145/3442188.3445922 and in stronger terms at https://link.springer.com/article/10.1007/s10676-024-09775-5?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel TDA-based method for measuring LLM similarity.  Zigzag-persistence is introduced to take account of the properties of the LLM graph structure. As part of the evaluation, it has been applied to Pruning to check its effectiveness.

### Strengths
- This paper introduces a new idea to introduce Zigzag-persistentce by considering the layer structure.
- It has been applied to pruining to check its effectiveness.

### Weaknesses
 - Methods that regard Neural Networks as graphs and apply TDA have been proposed in [1], for example. This is the usual persistent homology, but the use of zigzag persistence for graph structures has been verified in [2],[3] and elsewhere. The structure focusing on the LAYER structure has some aspects of novelty, but it seems to be a simple conventional combination idea and the degree of novelty is weak.

- It is difficult to see what the similarity of the models is intended to achieve. The proposed method is similarity of the graph structure and may be similar for different models. The paper evaluates the similarity in application to pruning to demonstrate its validity. However, it is difficult to accept from the experimental results alone that the proposed method is a superior similarity simply because the implications that the similarity indicates are not clear. As a method for measuring the degree of change, such as model modifications, such as pruning, it is intuitively effective. However, as no uses have been indicated, the current situation is that there is only evidence for it as a pruning method. If the claim is that it is a superior pruning method, it should be clearly stated as such. In addition, if the pruning method is slaughtered and claimed, it should be compared with a generally sufficient advanced puruning method, for example [4],[5].

### Questions
- Clarify the claim point(s) for which the novelty of the contribution in this paper is sufficient.
- Please clearly indicate in what sense the similarity of the proposal is valid, what use scenarios are covered (other than pruning) and whether it is sufficient evidence for this.


Why are the titles on the system different from the titles in the PDF?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new framework based on zigzag persistence to analyze internal
representations in LLMs by characterizing the birth and death of topological features within the
model’s layers.   it provides a fine-grained geometric analysis of the internal representations through TDA.  Distinct from traditional methods that solely compare representations at individual layers, the proposed method  captures their entire evolutionary path, providing a richer understanding of how these features evolve and contribute to the model’s decision-making processes

### Strengths
Originality:
The idea of applying topological data analysis to LLM  is novel and interesting
Clarity:
The paper is well-written and easy to follow.
Significance:
The proposed Persistence Similarity and zigzag algorithm have rigorous mathematical formulation and are easy to compute. The experiment in Section 4.3 is promising. Author compares the performance of layer pruning Persistence Similarity and other common llm layer pruning methods and the proposed method performs well in most cases under 10% pruning rate.

### Weaknesses
Major concerns:
1. The discussion in Section 4 did not clearly explain the sensitivity of the proposed method when pruning LLM layers.  The result shown in Fig 5 indicates that, across different models, our metric consistently identifies the deep layers as “redundant”. Additionally, in the results from Table 1, the proposed metric does not show an advantage at a 20% sparsity level, which further heightens my concerns. Specifically, the consistent identification of deep layers as redundant across diverse models suggests a potential lack of sensitivity to model-specific nuances. The pruning results at 20% sparsity, where the method fails to outperform common techniques, raise questions about the practical utility of the proposed metric, particularly in scenarios requiring more aggressive pruning.

2. The authors mention, "Due to the autoregressive nature of these models, the representation of the last token in a sequence captures information about the entire sequence and is the only token used for predicting the next." I disagree with this assumption; predicting the next token is clearly based on all preceding tokens. Therefore, I would like to see an analysis of certain special tokens, such as the EOS and BOS tokens.

3.  Can Persistence Similarity and the zigzag algorithm help explain the varied responses of LLMs across different abilities or areas of knowledge? The pruning experiments presented in the paper are limited to base models. Could you provide an analysis of the instruction-following abilities of chat models or their capabilities in math and code?

### Questions
Overall, I believe this paper is likely to present a novel perspective on understanding LLMs. 
However, the experimental section is overly limited. I look forward to discussing these questions further in the weaknesses section. Addressing them may help improve the overall score.

### Soundness
3

### Presentation
4

### Contribution
3
