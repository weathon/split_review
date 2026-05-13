# The Representation Geometry of Features and Hierarchy in Large Language Models

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
The linear representation hypothesis is the informal idea that semantic concepts are encoded as linear directions in the representation spaces of large language models (LLMs). Previous work has shown how to make this notion precise for representing binary concepts that have natural contrasts (e.g., {male, female}) as _directions_ in representation space. However, many natural concepts do not have natural contrasts (e.g., whether the output is about an animal). In this work, we show how to extend the formalization of the linear representation hypothesis to represent features (e.g., is_animal) as _vectors_. This allows us to immediately formalize the representation of categorical concepts as polytopes in the representation space. Further, we use the formalization to prove a relationship between the hierarchical structure of concepts and the geometry of their representations. We validate these theoretical results on the Gemma and LLaMA-3 large language models, estimating representations for 900+ hierarchically related concepts using data from WordNet.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a theoretical and empirical analysis of how concept hierarchies are encoded in the geometry of a pretrained LM's unembedding layer. The theoretical part develops a rigorous formalization of several notions related to the linear representation hypothesis, such as linear representations, vector representations of binary concepts, polytope representations of categorical concepts, and the notion of hierarchy being represented via orthogonality. The empirical part uses this formalism to identify how the conceptual structure of the WordNet hierarchy is reflected in the linear representational geometry of two LMs (Gemma-2B and Llama-3-8B). The empirical results, along with clear visualizations, constitute convincing evidence that the developed theoretical formalism closely tracks the actual representation of a conceptual hierarchy in the (un)embedding layer.

### Strengths
**Originality:** The sequence of definitions (linear representations, vector representations of binary concepts, polytope representations of categorical concepts) culminating in proposed structure of hierarchical orthogonality (Theorem 8) is a novel perspective while at the same time very intuitively appealing. Among the related work I'm familiar with, hierarchical orthogonality is reminiscent of partial orthogonality (Jiang et al., 2023; https://arxiv.org/abs/2310.17611, cited in the submission), but the two notions are distinct enough

**Quality:** The paper is of exemplary quality. The empirical analysis validates all theoretical predictions.

**Clarity:** The paper is exceptionally clear, well-written, and easy to read.

**Significance:** The paper significantly advances our understanding of the unembedding layer, revealing a highly intuitive linear structure in the representational geometry of a conceptual hierarchy. While the analysis in its current form is limited to concepts/features that are expressed as single tokens in the vocabulary of the LM's tokenizer, the formalism of hierarchical orthogonality can potentially provide a theoretical foundation for the analysis of more complex concepts in early-middle layers, which has recently become the focus of work on detokenization/retokenization (https://transformer-circuits.pub/2022/solu/index.html., https://arxiv.org/abs/2305.01610), stages of inference (https://arxiv.org/abs/2406.19384) and the LM's "inner vocabulary" (https://arxiv.org/abs/2410.05864).

### Weaknesses
I don't see any substantive weaknesses. 

An obvious point that might be made here is the limitation (also acknowledged by the authors) that the presented formalism and empirical results are only applicable to the unembedding layer, but in my view the unembedding layer is sufficiently complex and interesting to serve as an object of study in its own right.

### Questions
n/a

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper generalises the idea that binary concepts can be represented as directions of their vectors in a vector space. The authors argue that this idea fails when concepts are not binary, e.g. we have mammals versus birds and each of these has many elements therein. They they construct a new theory that for such manifold concepts one needs a polytope in a vector space. They devise a nice theory,  generalising the notion of linear combinations over binary concepts to these polytopes and experiment with these findings using the vector spaces formed by Gemma and LLaMA.

### Strengths
1- Introducing a nice mathematically solid theory into the vector representations learnt by large language models. 
2- Finding a novel way to represent ontological hierarchies of concepts in the spaces learnt by LLMs. 
3- Solid maths and theory

### Weaknesses
Certain concepts are not well defined:

1- Please provide a clear definition of the unembedding space early in the paper, explaining its role in their theoretical framework. The current description lacks detail, making it difficult to understand how the geometry of this space interacts with the concept polytopes.
2- Please provide concrete examples of concepts that are and are not causally separable, and explain how this distinction is crucial for their theoretical framework. The notion of causally separable introduced in the paper at the moment is vague, many concepts can be imagined to be causally separable. On the other hand, it is not clear at all what is not causally separable? I think the authors want to use this dichotomy to categorize entities under different general labels, but the definition is not helping. For example, is 'red' causally separable from 'apple'? Or is 'running' causally separable from 'jogging'? The lack of clarity here undermines the theoretical claims.
3-  Do please provide a brief explanation of the causal inner product within their paper, highlighting its relevance to their work, rather than relying solely on the external reference. At the moment, the notion of a causal inner product is not clear. The authors refer to the work of Park et al, but I am not sure why and I am not sure what is taken from it. Specifically, how does this inner product differ from a standard Euclidean inner product, and why is this difference crucial for capturing semantic relationships?
4- The dataset on which the theory is testes is rather small (less than 600 nouns and less than 400 verbs). It does provide a proof of concept, but cannot be used as a large scale validation.  I unfortunately do not know what is mainstream in the field. I suggest the authors find a dataset used in knowledge graph literature and test on it.
5- I wonder why the theory has only been tested on nouns and verbs. In other words, it is not clear what exactly are concepts. I would like to suggest the authors explicitly define what they consider to be a "concept" in the context of their work, and discuss whether their theory could be applied to other parts of speech or more abstract concepts. For instance, could the theory be extended to adjectives or adverbs, or even to more abstract notions like 'justice' or 'beauty'?
6- Please discuss how your approach compares to or could be integrated with existing work on knowledge graphs and ontologies, and how this might enhance the applicability of their theory. the paper needs a better theory of concepts to start from and to base itself on. I feel there is a good argument to be made by relating it to knowledge graphs and ontologies rather than working with a subset of WordNet.

### Questions
can you please answer to the points in weaknesses? I would appreciate it.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the representation of semantic concepts in large language models (LLMs), specifically testing and extending the linear representation hypothesis. This hypothesis proposes that semantic features, like gender or categorical distinctions, can be represented linearly in the embedding space. However, existing representations primarily address binary concepts with natural contrasts. This paper broadens this to include hierarchical and categorical concepts, proposing that these can be represented as vectors and polytopes within the representation space. Additionally, the paper formalizes hierarchical relationships as orthogonality between representations and validates these claims on the Gemma and LLaMA-3 models using WordNet-derived hierarchies.

### Strengths
1. Innovative Extension of the Linear Representation Hypothesis: The authors rigorously extend the hypothesis by introducing vector and polytope representations for non-binary, hierarchical concepts. This is particularly valuable because it addresses concepts lacking binary contrasts and presents a way to capture categorical hierarchies in language model embeddings.

2. Mathematical Rigor and Clear Formalization: The introduction of the causal inner product is mathematically grounded, ensuring that causally separable concepts are orthogonal in the transformed space (Equation 2.2). This rigor adds depth to the standard linear representation hypothesis by linking embedding and unembedding spaces without affecting model probabilities (Equation 2.1).
Theorem 4 (on magnitudes of binary representations) and Theorem 8 (on hierarchical orthogonality) are presented with precise definitions and assumptions. The mathematical derivation ensures that vector magnitudes and orthogonal properties align with the semantics of hierarchical structures.

3. Clear and Well-Defined Experimental Setup: The experiments on the WordNet hierarchy using Linear Discriminant Analysis (LDA) are robust. By estimating vector representations for over 900 concepts, the paper empirically tests whether hierarchical concepts are represented orthogonally in the embedding space. Results showing the preservation of hierarchical orthogonality even after shuffling embeddings further validate their claims.

4. Practical Implications: Extending concept representation to polytopes and using orthogonality for hierarchy offers a promising direction for LLM interpretability. The authors’ approach could pave the way for more structured and interpretable embeddings, potentially enhancing downstream tasks such as knowledge extraction and structured generation.

### Weaknesses
1. Clarity on the Choice of Transformation in Causal Inner Product: While the causal inner product transformation (Equation 2.2) is mathematically sound, further clarification on how the invertible matrix and constant vector are determined would strengthen the paper’s rigor. Specifically, elaborating on the practical implications of choosing these parameters and their influence on orthogonal representations in various models could provide more insight for researchers replicating or extending this approach. The paper should detail the specific method used to derive the invertible matrix and constant vector, including any assumptions or approximations made during this process. Furthermore, a discussion on the sensitivity of the results to variations in these parameters would be beneficial, as this could impact the robustness of the observed orthogonal relationships.

2. More Explicit Connection to Hierarchical Concepts: The hierarchical orthogonality introduced in Theorem 8 is foundational to the paper’s approach, yet its practical consequences could be explored more thoroughly. For instance, how does this orthogonality affect the interpretability or utility of representations in hierarchical tasks? Including a discussion of possible applications, such as taxonomy creation or hierarchical clustering, would enrich the paper’s contribution and situate it within the broader field of LLM interpretability. The paper could benefit from a more detailed analysis of how the derived orthogonal representations can be leveraged in downstream hierarchical tasks. This could include examples of how these representations improve performance in tasks like hierarchical classification or how they can be used to construct more interpretable knowledge graphs.

3. Expanding on Limitations and Approximation Issues: The paper notes that exact linear representations may not always emerge during LLM training due to stochasticity in optimization. While this limitation is understandable, the authors could discuss how close approximations might affect the reliability of hierarchical representations, especially under more complex, multi-level hierarchies. This would give readers a clearer view of the limitations of the proposed framework. Specifically, the paper should address the potential for deviations from perfect orthogonality and how these deviations might impact the interpretability of the hierarchical structures. A quantitative analysis of the degree of orthogonality achieved in practice, along with a discussion of the implications of imperfect orthogonality, would provide a more complete picture of the framework's limitations.

### Questions
1. On the Selection of Parameters for the Causal Inner Product: Can you elaborate on how you select the matrix A and the vector gamma in the causal inner product, and whether this choice generalizes across models? Would different values of A significantly alter the representation space, potentially affecting concept separability?

2. Approximation in Magnitude and Orthogonality of Representations: In cases where the representations for binary and hierarchical concepts are not exactly separable, do you have methods to measure or improve the alignment with the proposed theoretical structure (e.g., adjusting vector magnitudes or enforcing orthogonality)?

3. Impact of Hierarchical Orthogonality on Model Behavior: Could you provide more examples or case studies on how hierarchical orthogonality impacts the model’s downstream tasks? For instance, does this structure improve classification accuracy or clustering quality in hierarchical classification tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
As I understand it, the core value proposition of this paper is the report of an empirical observation: that, with respect to a particular inner-product, conceptual representations in transformer-based LLMs are vectorial, and moreover that hierarchical relationships between concepts correspond to orthogonality, while co-hyponymic categorical concepts are organised as simplices, altogether resulting in a direct-sum of polytopes.

The particular (sort/kind of) inner-product used is called "causal" (CIPs), which established in (apparently immediately) prior work by Park et al. CIPs are a piece of conceptual technology, which I understand as follows:
> Assuming an operational/counterfactual notion of concept as a latent variable in a causal chain <Input -> Latent -> Output>...
> Defining causal separability of two concept-variables to be well-definedness of the output on their independent joint distributions...
> An inner product is "causal" when it treats causally separated concept-variables as orthogonal.
> Park et al. gives methods to obtain and compute with such CIPs, and shows how CIPs admit a duality theorem that permits embedding and unembedding spaces to be identified and viewed as isomorphic to some Euclidean space equipped with the usual inner product (in contexts where there are embedding, softmax, and unembedding maps to speak of.)

### Strengths
To me, there are two noteworthy aspects of the empirical claim.

<Emergence> First is that this structure arises emergently and naturally in LLM representations. This would be a scientific contribution to ongoing discourse concerning how and whether LLMs understand [cf. Bender & Koller's "Climbing towards NLU" which casts LLMs as Searle-type non-understanders vs. Sogaard's "Grounding the Vector Space of an Octopus" which surveys evidence that language models obtain geometric models of concepts in their vectorial representations, as the current paper does.]

<Word-Token-Concept> Second is that the claim holds for transformer-based LLMs, where (to my understanding) tokenisation decouples the relationship between words and semantic vectors. Demonstrating empirically that semantic representations not only exist but satisfy geometric constraints according to their natural-language conceptual organisation *at the token level* is big-if-true, even just methodologically.

### Weaknesses
This is a simple and compelling observation, especially in the broader context of approaches to vectorial semantics downstream of Firth's distributional hypothesis, where there are many rhyming ideas in the literature. For example, the usage of an inner-product in a high-dimensional space to test for membership in a vectorial data structure is prefigured by Kanerva's hyperdimensional computing. Hyponymic structure alongside convex simplicial structure is treated mathematically in [Interacting Conceptual Spaces I: Grammatical Composition of Concepts; https://arxiv.org/pdf/1703.08314], and the idea of looking for hypo/hypernymic structural representations in vector spaces is its own cottage industry [as a google search of the terms "hyponymy" and "density matrix" will demonstrate.]

While the authors have taken pains to point out (lines 51, 124, 225, 308) that the current approach is a conceptual advance *due to the consideration of vectors* rather than, e.g. directional cones in prior work, this could be read as a strawman that misrepresents a broader research context of vectorial semantics, and it just doesn't do justice to the empirical claims of the paper. Look, even if I totally discount any claim to conceptual novelty regarding the use of vectorial semantics, I still would consider the paper to be strong on the basis of the empirical observation alone, provided the observation is adequately situated.

Integrating some comparison to approaches in vectorial semantics could be an opportunity to strengthen the conceptual dimension of the paper. As far as I can tell, other vectorial semantics worok typically has a "feature-engineering" rather than exploratory nature, and using the geometry of causal inner products seems to be an effective and relatively novel idea; having these as literature supported claims could potentially broaden the appeal and reach of this work at little cost.

I am currently borderline because I have questions, but I am happy to raise my score if my major questions are addressed: First is what CIPs have to do with LLMs and with the particular empirical observation. Second is how the <Word-Token-Concept> gap was crossed. I'm going to write a little adversarially now, but in hopefully a productive way; I like the paper and would like to strengthen it.

**************

1. Regarding CIPs, their robustness, and their conceptual relevance for the empirical claim at hand.

The content of CIPs was difficult to glean from the materials presented in this paper alone, and I had to refer to the prior work for details. Given the closeness of presentation (down to the choice of variables), I would recommend explicit attribution of credit to the prior work. As a presentational note, just reproducing Thm 3.2 would have gone some way to answering my questions as a reader about why "duality" is used as a term, and why the embedding and unembedding spaces are assumed to be Euclidean and of matching dimension, etc. It is perhaps clearer to indicate that having a CIP is desirable because it enables dual presentation of embeddings and unembeddings, it renders computation of a semantic character as easy as regular Euclidean inner products, and so on.

Here are several cases of conceptual difficulty I had that made it difficult for me to understand what the role of CIP in this story is, and I hope you can help sort me out.

> The definition of CIP from causal separation is potentially too stringent; consider the counterexample case where two co-hyponymic concepts are only defined in the domain of a common hypernym, e.g. "is_bird" and "is_nocturnal" are causally separable properties but only hold in the domain of "is_animal", whereas the current statement requires well-definition of birdness and nocturnality everywhere. So ok, let's say that as a reader I don't trust your first-principles approximation of what a concept is; is it worth spending the time and space to convince me or is that not really important for what needs to be shown here?

> In the mathematical setup of CIP, it is assumed that there is a single euclidean embedding space for text, a matching unembedding space, and a softmax. This is for just the "final token position" (line 107), so I'm assuming an autoregressive transformer, but then there's no further talk of the "internal structure of LLMs" (line 113). This is suspicious to me, because if there's absolutely nothing structurally relevant about the architecture of LLMs to the subsequent analysis of concepts and causal separation and then CIPs, then I can freely swap "LLMs" for anything else? If you're doing something so general-purpose, then I would like to be convinced that CIPs are actually necessary, rather than a contrived thing that the empirical data doesn't really depend upon.

> Where exactly are CIPs used or useful? My best guess so far is that CIPs and their assumptions are required in order to prove Theorem 8, which yields the analytic presentation in Figure 1 as a direct sum of polytopes. However, the polytope-simplices never have their convexity property explored or exploited [cf. Gardenfors "Geometry of Meaning"], and the particular example presented in Figure 1 is a special case where at most one node at every level has children, so I believe a fair equivalent characterisation would also be: "different levels are orthogonal, and co-hyponymic nodes form clusters." I'm not convinced that this is really worth all the baggage of CIP, so where else is it being employed?

2. The Word-Token-Concept gap.

WordNet and vectorial embeddings of words are perfectly good and commonplace. What I was excited to learn about was how you managed to extend this analysis over to the tokens of LLMs. I must have missed something, because the only thing I can see that gives some kind of methological hint as to how this gap was crossed is a sentence in line 955, tucked in the appendix: "Lastly, we use the vector representations estimated by the non-split collection of tokens for Figure 2, (etc.)" I feel like I must have missed it somehow because the omission of this crucial methodology would be such an inconsistency with the attention to detail for the rest of the paper, but I just can't figure out what is being done here to cross-validate findings on WordNet with Gemma and Llama. The mathematical assumptions made only raised more questions (assume final token only for an autoregressive... predictor? autoencoder?).

**************

These two questions are crucial for me because they would make the difference between an uncharitable reading (e.g. CIP is a just-so construct and the empirical work is mostly WordNet with unclear methodology for LLMs), and a very happy one (e.g. CIP is a general-purpose information geometry, and here is a clear and well-motivated demonstration of how this conceptual lens can be applied to find conceptual structure even at the token level of LLMs).

### Questions
I am currently borderline because I have questions, but I am happy to raise my score if my major questions are addressed: First is what CIPs have to do with LLMs and with the particular empirical observation. Second is how the <Word-Token-Concept> gap was crossed. I'm going to write a little adversarially now, but in hopefully a productive way; I like the paper and would like to strengthen it.

**************

1. Regarding CIPs, their robustness, and their conceptual relevance for the empirical claim at hand.

The content of CIPs was difficult to glean from the materials presented in this paper alone, and I had to refer to the prior work for details. Given the closeness of presentation (down to the choice of variables), I would recommend explicit attribution of credit to the prior work. As a presentational note, just reproducing Thm 3.2 would have gone some way to answering my questions as a reader about why "duality" is used as a term, and why the embedding and unembedding spaces are assumed to be Euclidean and of matching dimension, etc. It is perhaps clearer to indicate that having a CIP is desirable because it enables dual presentation of embeddings and unembeddings, it renders computation of a semantic character as easy as regular Euclidean inner products, and so on.

Here are several cases of conceptual difficulty I had that made it difficult for me to understand what the role of CIP in this story is, and I hope you can help sort me out.

> The definition of CIP from causal separation is potentially too stringent; consider the counterexample case where two co-hyponymic concepts are only defined in the domain of a common hypernym, e.g. "is_bird" and "is_nocturnal" are causally separable properties but only hold in the domain of "is_animal", whereas the current statement requires well-definition of birdness and nocturnality everywhere. So ok, let's say that as a reader I don't trust your first-principles approximation of what a concept is; is it worth spending the time and space to convince me or is that not really important for what needs to be shown here?

> In the mathematical setup of CIP, it is assumed that there is a single euclidean embedding space for text, a matching unembedding space, and a softmax. This is for just the "final token position" (line 107), so I'm assuming an autoregressive transformer, but then there's no further talk of the "internal structure of LLMs" (line 113). This is suspicious to me, because if there's absolutely nothing structurally relevant about the architecture of LLMs to the subsequent analysis of concepts and causal separation and then CIPs, then I can freely swap "LLMs" for anything else? If you're doing something so general-purpose, then I would like to be convinced that CIPs are actually necessary, rather than a contrived thing that the empirical data doesn't really depend upon.

> Where exactly are CIPs used or useful? My best guess so far is that CIPs and their assumptions are required in order to prove Theorem 8, which yields the analytic presentation in Figure 1 as a direct sum of polytopes. However, the polytope-simplices never have their convexity property explored or exploited [cf. Gardenfors "Geometry of Meaning"], and the particular example presented in Figure 1 is a special case where at most one node at every level has children, so I believe a fair equivalent characterisation would also be: "different levels are orthogonal, and co-hyponymic nodes form clusters." I'm not convinced that this is really worth all the baggage of CIP, so where else is it being employed?

2. The Word-Token-Concept gap.

WordNet and vectorial embeddings of words are perfectly good and commonplace. What I was excited to learn about was how you managed to extend this analysis over to the tokens of LLMs. I must have missed something, because the only thing I can see that gives some kind of methological hint as to how this gap was crossed is a sentence in line 955, tucked in the appendix: "Lastly, we use the vector representations estimated by the non-split collection of tokens for Figure 2, (etc.)" I feel like I must have missed it somehow because the omission of this crucial methodology would be such an inconsistency with the attention to detail for the rest of the paper, but I just can't figure out what is being done here to cross-validate findings on WordNet with Gemma and Llama. The mathematical assumptions made only raised more questions (assume final token only for an autoregressive... predictor? autoencoder?).

**************

These two questions are crucial for me because they would make the difference between an uncharitable reading (e.g. CIP is a just-so construct and the empirical work is mostly WordNet with unclear methodology for LLMs), and a very happy one (e.g. CIP is a general-purpose information geometry, and here is a clear and well-motivated demonstration of how this conceptual lens can be applied to find conceptual structure even at the token level of LLMs).

### Soundness
2

### Presentation
3

### Contribution
2
