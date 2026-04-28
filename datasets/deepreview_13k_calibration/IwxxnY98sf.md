# Unsupervised Learning of Categorical Structure

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 5, 5, 6

## Abstract
Humans are known to reason using logic and abstract categories, and yet most state of the art neural models use continuous distributed representations. These representations offer impressive gradient-based learning capabilities, but it is often difficult to know what symbolic algorithm the network might implicitly be implementing, if any. We find that there are representational geometries that naturally suggest a symbolic structure, which can be expressed in terms of binary components. We show that we can recover this structure by fitting the geometry of this binary embedding to the representational geometry of the original objects. After establishing general facts and providing some intuitions, we present two algorithms that work on low-rank or full-rank data, respectively. We assess their reliability on simulated data, and then use them to interpret neural word embeddings, in which we expect a compositional structure.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes novel methods for discovering interpretable categorical structure within continuous data representations. The key idea is to find a binary embedding that preserves the original data geometry while representing data points as combinations of latent concepts. Authors introduce two algorithms: the Binary Auto-Encoder (BAE) for low-rank data, leveraging an approach inspired by Hopfield, and an Iterative Refinement algorithm for full-rank data, where sparsity regularization encourages simpler conceptual structures. Authors then visualizes the learned binary embeddings using novel "analograms." Experiments on simulated data and word embeddings demonstrate the method's ability to uncover meaningful latent concepts and their relationships.

### Strengths
* This paper makes a timely contribution motivated by LLMs' mechanistic interpretability. I learned a lot by how authors frames the problem of symbolic knowledge/algorithm extraction from distributed representation as geometry-preserving binary matrix factorization problem.

* Building on top of existing matrix factorization approaches, this paper proposes two concrete algorithms: (i) Binary Auto-Encoder (BAE)  and (ii) Iterative Refinement algorithm.

* BAE offers a computationally efficient alternative to existing methods, particularly for higher-rank, but still relatively low-rank scenarios. It notably avoids the restrictive Schur independence assumption required by some prior work.

* The Iterative Refinement algorithm provides a solution for the challenging full-rank scenario, which is less explored in prior work on binary matrix factorization.

* It was a smooth read. Presentation of the conceptual and algorithmic contributions are solid, where the "analograms" visualization provides a valuable tool for visualizing the learned binary embeddings.

* Claims are carefully evaluated on both simulated data and real-world word embeddings.

### Weaknesses
Below are some weaknesses. Overall, I appreciated how author themselves have honestly clarified many of the limitations of the proposed approaches in the draft.

* The theoretical justification for sparsity regularization feels a bit weak, given the inherent non-uniqueness and NP-hardness of the problem. Stronger guarantees on solution quality would be valuable. Specifically, while the authors motivate sparsity as a useful inductive bias, the connection to the specific problem of uncovering interpretable categorical structure is not fully established. It's unclear how sparsity directly leads to more meaningful or disentangled concepts, especially given the potential for multiple sparse solutions that may not align with human interpretability. The argument that a smaller solution space implies a better solution is not rigorous enough, and a more formal analysis of the solution space and its properties would be beneficial.

* The Iterative Refinement algorithm, while clever, seems to struggle with larger datasets. That super-polynomial scaling is a real bottleneck, and we're not sure how practical this approach would be in many real-world scenarios. The computational complexity of the algorithm is a significant concern, and the authors should provide a more detailed analysis of its scaling behavior with respect to the number of data points and the dimensionality of the input space. The lack of scalability limits the applicability of the method to smaller datasets, which may not be representative of many real-world problems. Furthermore, the practical limitations of the algorithm should be more clearly stated, including the memory requirements and the time needed to converge on larger datasets.

* Interpreting the discovered concepts feels somewhat subjective and requires manual effort. A more automated approach to interpretation would be beneficial. (This is a broader issue for interpretability approaches though.) The reliance on manual interpretation of the discovered concepts is a significant limitation. While the analograms provide a useful visualization tool, the process of assigning meaningful labels to the discovered binary codes remains subjective and time-consuming. A more automated approach to concept interpretation, perhaps by leveraging external knowledge bases or language models, would be a valuable addition. The current approach requires significant human intervention, which limits the scalability and objectivity of the method.

* A more comprehensive comparison to existing methods would further strengthen the empirical results. The current evaluation lacks a thorough comparison to other state-of-the-art methods for binary matrix factorization and concept discovery. A more comprehensive empirical evaluation, including a wider range of datasets and comparison to existing baselines, would provide a stronger validation of the proposed approach. The authors should also consider comparing their method to other techniques that aim to extract interpretable representations from continuous data, such as sparse autoencoders or concept bottleneck models.

### Questions
* The scalability of Iterative Refinement seems like a real bottleneck. Have you considered any approximations or optimizations to improve its performance on larger datasets? What's the largest dataset you realistically think this algorithm could handle?

* I'd love to see a more thorough comparison with existing methods. Could you add more discussions regarding how your approach compares again recent works, e.g., The Geometry of Categorical and Hierarchical Concepts in Large Language Models by Kiho Park, Yo Joong Choe, Yibo Jiang, Victor Veitch?

* The connection between sparsity and analogram complexity isn't super clear. Have you investigated alternative regularization strategies that more directly target the complexity of the learned graph structure? I wonder if there are cases where sparsity might actually lead to more complex graphs.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores identifying geometry representations to symbolically represent neural models and understand their reasoning patterns. The paper shows that the discovery of latent categories can be presented in a binary matrix factorization set-up, preserving mutual distances. Performance of the proposed framework is tested using low and high-rank representation matrices, showing potential to handle a variety of inputs.

### Strengths
- Detailed theoretical framework supported by experiments on simulated examples and neural word embeddings
- Discussion of performance of proposed method on low-rank and high-rank representations

### Weaknesses
 - Limited discussion of key contributions and problem formulation in the introduction – while this is discussed across other sections in the paper, work would benefit from condensed clear problem formulation, main contributions and applications of the proposed framework
- Notation appears challenging to follow – for example p is used both for probabilities and number of points

### Questions
1. Have you tested your method on embeddings beyond word2vec? It would be good to see how the method generalizes on embeddings for data such as graphs or images
2. In section 2.1, you mention that the problem would be NP-hard to solve where uniqueness does not necessarily hold, could you clarify if this challenge was mitigated with use of CKA objective and proposed regularization?
3. In section 4, it is signaled that the proposed framework has potential to achieve CKA higher than 0.93, have you run experiments which support this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents two related algorithims intended to guide unsupervised category learning. Overall the approach presented here tries to explain high-dimensional embeddings in terms of a linear combination of concept vectors. By taking a sets of concept vectors and embeddings then assigning concepts to each embedding via binary weights. This is done by computing a kernel matrix, comparing each embedding with all the others, and trying to assign categories to each embedding that preserves the similarity structure of the embedding space. That is; two embeddings that are similar should have similar category assignments. To do this process efficiently this work uses gradient based methods. In cases where the embeddings are low rank they search for category vectors that are present in the embedding using a hopfield network. Looking to identify which categorisations of the embeddings are structure preserving. This method is intractable in cases with higher-rank data, as a result they propose a second method that builds all category vectors at once, but looking at a single embedding at a time. By iterating through all the embeddings this iterativley builds category vectors that maximally preserve the similarity structure of the input space. Experiments on artificially generated data shows these methods are relatively good at recovering the undelying strucutre of the space. Additionally these methods are relatively fast when data is low rank with a small number of samples although neither algorithm scales terrifically well with time complexity past 1000 points becoming quite high. A final set of experiments applies these methods to word2vec embeddings, fitting binary concepts to a subset of word2vec, and discussing the potential semantic interpretation of different concepts via qualitative analysis.

### Strengths
Overall this paper is very well written, presenting work on an interesting topic, with well designed visuals. The text tries quite hard to give readers an intuition for why the authors pursue certain lines of enquiry before working through it. The introduction gives sufficient context for the approach, and builds some motivation for the line of work. Additionally experiments are presented on both ariticial and natural data. Allowing the reader to get a sense for exactly how accurate the method presented here is on data with a known underlying structure, before showing that the method still provides interesting results on more complex embeddings.

### Weaknesses
While I would like to be clear that overall I do think this paper is strong, with solid scientific merit, I have a couple of areas of concern. If these are adequately addressed I am open to raising my score.

A) The formalisations are in some places difficult to follow, with certain background literature being under-introduced.

In section 2, equation 2.2 Q is defined as yTy yet I don’t appear to see where y is defined. In other places the notion seems overly verbose and a bit too formal without arming the reader with a sufficiently strong intuition.  I had difficulty understanding equation 4 given the notation and inline explanation. 

Terminologically, centered kernel alignment (CKA) seems central to this work but is mentioned in a single sentence without providing a high-level intuition before introducing it formally. Some discussion of making the similarity of one space align with the similarity of another before talking about Gram matrices would be welcome.

B) The authors discuss embeddings from 4 different perspectives, in terms of real-valued space, kernel space, binary concepts, and geometry. It would be helpful to either make clearer how these relate to each other, or to focus on fewer of them.

In the introduction they note: "These factors were analyzed discretely (is it active or not), but the continuous degrees of ‘active’ can make them a little harder to interpret them as categories or symbols. For that reason, we see advantage in having factors which are categorical by construction.” Later though the analysis of word2vec appears to center around categories with continous degrees of activity. With this section stating "To better understand the discovered concepts we will, ironically, appeal to a continuous projection.” Before visualising and discussing the embeddings in continous space. This does clearly undercut the narrative of the work which asserts binary categorisation to be a useful analytic tool. 

Additionally the section on word2vec makes little discussion of the underlying geometry of the embedding space, despite this being the major focus of the experiments on artificially generated data. I think greater narrative clarity would make the paper much stronger: i.e. making the line of argumentation consistent across the sections, and more clearly relating the artificial and word2vec experiments.

C) While the writing is generally excellent, in many places the style is a bit informal. While accessably written papers are great, there’s a difference between accessability and formality -- some sentences could use tightening.

"In this form the CKA is not nice to optimize, but since our constraining set is a cone it is equivalent to the Frobenius distance between the double-centered matrices.” - What does it mean for something to be ’not nice’ to optimize? How do you know your constraining set is a cone?

"Parsimony is desirable, but there are several ways to define it.” - It would be good to start with introducing parsimony, I assume you mean ’simplicity’ akin to occam’s razor but it would be good to make this explicit.

"Since an exact fit is not always possible (or even desirable), we must define goodness of approximation.” - Why isn’t an exact fit desirable?

D) Novelty and relation to previous work. 

It would be good to clarify that extensive previous work has tried to understand continuous representations in terms of symbols. It seems that the overall approach - approximating embeddings with category vectors - has been tried in previous work quite a bit, and that the novelty here is introducing more scalable methods that can work on higher-rank data. If this is the main contribution it would be great to make that clear at the end of the introduction, although if that is the main contribution that also raises some concern that the methods struggle to scale to 1000 samples. Additionally there is a clear relation between this and tensor product representations which might be worth mentioning.

E) Discussion Narrative.

This is a minor issue, but the discussion opts to introduce the notion of biological plausibility for the first time ("Both algorithms can in principle be implemented by a population of neurons with Hebbian input and recurrent synapses, and though we treat this as a curiosity for now, it raises the question of biological relevance.”). It might be best to either introduce this in the introduction and make it a part of the paper overall, or make the discussion relevant to the current content of the introduction.

### Questions
a) Could you clarify the geometric interpretation of the word2vec embeddings? What is the analogram here, and how does that aid interpretation? While I follow the intuition of aligning kernels between spaces, I struggle to see the broader impact of your geometric analysis of that process.

b) What is the benefit of interpreting embeddings in terms of discrete categories, if interpretation is ultimately a qualitative comparison of the continuous weights associated with those categories? I'm slightly unclear on the utility of the approach here. Is it intended to be useful for interpreting word embeddings (which appears to be a substantial claim of the analysis), if so relevance to other approaches to interpretability would be welcome - and some mention of the computation complexity of running the analysis on a sample of word2vec.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors present a representational decomposition technique to find bases of binary logical components. They describe how to do the technique. They then show that the method can work for a number of geometries in synthetic settings. And lastly they show that the method can be used with word2vec embeddings to some success.

### Strengths
- Decomposing representations into logical components maybe could be promising for generalization?
- The authors showed the technique in both toy settings and more practically relevant settings (word2vec)
- From what I understood, the theoretical backing was sound

### Weaknesses
 - unclear what the author's contributions are. is it the introduction of a new factorization technique?
- unclear why we should care about this factorization technique. the paper needs more focus on relevance.
- the structure of the paper would benefit from more clarity on the high level goals of each section
- I found the majority of the technical details difficult to understand because it sometimes felt like it was unclear how the details fit into the greater picture
- There is a big data dependence issue when creating the kernel matrix
    - what dataset do you use here in practical settings?
    - how can you ensure you're using a relevant dataset for the model you are examining?
    - how can you ensure that the data sufficiently spans the model's representation space?
- if you weight the logical variables, are they not still continuous representations?

### Questions
- What problems do these logical variables solve? How can they be used?
    - is the suggestion that this is a process that occurs in biological systems?
    - do these embeddings somehow improve performance on something?
- There is a big data dependence issue when creating the kernel matrix
    - what dataset do you use here in practical settings?
    - how can you ensure you're using a relevant dataset for the model you are examining?
    - how can you ensure that the data sufficiently spans the model's representation space?
- how does method compare to something like locality sensitive hashing for forming discrete representations?
- why is it necessarily a bad thing that neural systems use continuous representations? In general, I see the opposite complaint more frequently, that artificial networks impose too much slot-like and discrete structure in ways that the human brain does not
- if you weight the logical variables, are they not still continuous representations?

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
2

### Summary
This paper aims to extract binary representations from data, which preserve the latent structure inherent in original data. The authors set up an objective based on centered kernel alignment between the data and binary representations and propose two iterative algorithms for factorizing the data into binary components: one designed for low-rank data and another for full-rank data. They validate their approach with numerical experiments on simulated low-rank data, hybrid low-rank and hierarchical data, and a subset of WordNet, demonstrating the effectiveness of the proposed algorithms.

### Strengths
**S1.** Using the binary matrix factorization to identify geometrical representations seems novel.

**S2.** This paper proposes two algorithms to handle both low-rank and full-rank data, making this framework versatile for various data.

**S3.** This paper demonstrates the efficacy of the proposed methods through several numerical validations. Additionally, it includes analyses of extracted binary representations and an ablation study to test robustness in the presence of noise.

### Weaknesses
 **W1.** The introduction could benefit from further refinement. For example, although the paper introduces two algorithms, there is no clear description of them in this section. Additionally, introducing the concept of binary representation in the third paragraph could help readers grasp the paper's focus more effectively.

**W2.** This paper argues that binary representations can improve the interpretability of neural representations. While this paper provides several analyses of representational quality, whether these representations truly capture the data's latent structure remains ambiguous.

**W3.** Providing a more detailed explanation of the transformation from Equation 2 to Equation 3 would assist readers in understanding the method.

### Questions
**Q1.** From the perspective of representational geometry and sparsity, previous work [1] may be related to this paper. Discussing the relationship between sparsity and representational geometry would provide valuable insights for readers.

**Q2.** In Section 2.2.1, the authors discuss the examples in Figure 3 but do not fully clarify the concept of a hidden node. Could they provide a more detailed explanation of this term?

**Q3.** I am curious whether these algorithms can be used in end-to-end training where each word representation is dynamically changed or if they are applicable solely for post-hoc analysis after training. I would appreciate it if the authors could share their thoughts on this.

[1] Elhage, et al., "Toy Models of Superposition", Transformer Circuits Thread, 2022.

### Soundness
2

### Presentation
2

### Contribution
2
