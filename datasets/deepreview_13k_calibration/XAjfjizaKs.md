# Residual Stream Analysis with Multi-Layer SAEs

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Sparse autoencoders (SAEs) are a promising approach to interpreting the internal representations of transformer language models.
	However, SAEs are usually trained separately on each transformer layer, making it difficult to use them to study how information flows across layers.
	To solve this problem, we introduce the multi-layer SAE (MLSAE): a single SAE trained on the residual stream activation vectors from every transformer layer.
	Given that the residual stream is understood to preserve information across layers, we expected MLSAE latents to `switch on' at a token position and remain active at later layers.
	Interestingly, we find that individual latents are often active at a single layer for a given token or prompt, but this layer may differ for different tokens or prompts.
	We quantify these phenomena by defining a distribution over layers and considering its variance.
	We find that the variance of the distributions of latent activations over layers is about two orders of magnitude greater when aggregating over tokens compared with a single token.
	For larger underlying models, the degree to which latents are active at multiple layers increases, which is consistent with the fact that the residual stream activation vectors at adjacent layers become more similar.
	Finally, we relax the assumption that the residual stream basis is the same at every layer by applying pre-trained tuned-lens transformations, but our findings remain qualitatively similar.
	Our results represent a new approach to understanding how representations change as they flow through transformers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces and analyzes a multi-level sparse autoencoder (MLSAE), which is a sparse autoencoder (SAE) trained on latent representations of the residual stream at all layers. The work experiments with Pythia models on language modeling tasks. The paper further reinforces the technique by adding tuned-lens transformations, allowing analysis of the residual stream even if the information is encoded on different dimensions at different layers. The work then studies the behavior and similarity of representation at different layers in Transformers of varying sizes.
[After the discussion period: I have increased the score from 6 to 8, and increased the confidence from 3 to 4.]

### Strengths
The work experiments with Pythia models (Transformers) of different sizes, making the work highly reproducible. The experiments are sound and most of the doubts I had while reading were answered already in the text. While the paper doesn't offer revolutionary insights on its own, it is an excellent improvement to sparse autoencoders and may be very useful for mechanistic interpretability. The model also tests the relative performance of MLSAE at different expansion factors and sparsity levels and runs good ablations with "tuned lens". While I wondered about some design decisions, in particular "feature-stacked" MLSAE, when reading the paper, the discussion provided in Section 5 answered my potential questions before I even wrote them down. All in all, the writing is excellent, and the experiments look solid and reproducible. In general, I am leaning towards acceptance to the conference, and I am willing to adjust the score during the discussion.

### Weaknesses
1. The biggest weakness that I see is the lack of direct experimental comparison to previous techniques. I'd expect a paper to compare MLSAE and existing SAE techniques, similar to the comparison in Figure 5 of MLSAE w/ and w/o tuned lens. For example, I think it would be possible to show a version of Figure 1 (and almost all other figures, too) using previous SAE techniques, even without training on most of those layers. This would give the reader a qualitative understanding of whether MLSAE provided additional value. Specifically, a comparison should include standard, single-layer SAEs trained independently on each layer and then applied across all layers, which would highlight the multi-layer aspect of MLSAE. The current analysis only compares MLSAE with and without tuned lens, which is insufficient to establish its superiority over existing methods.
2. Similarly, a quantitative measure (e.g., how much different methods agree on a similarity of different representations) could be made. In my eyes, the paper lacks a clear baseline to show improvement over. For instance, a metric like cosine similarity between the latent representations obtained from MLSAE and single-layer SAEs, when applied to the same layer, could be used. Furthermore, the paper could quantify the reconstruction error of single-layer SAEs when applied to layers they were not trained on, compared to MLSAE, to demonstrate the advantage of multi-layer training.
3. The above is especially important as the paper on its own doesn't offer that many additional insights into Transformer - apart from the surprising result of isolated latent activations. The method also is quite simple.
4. I would also like to see an analysis of the method's weaknesses - for example, it seems like it should have a higher computational cost of training, but it is not clear what is the exact impact of that (I assume the impact is quite small). The paper should quantify the training time and memory requirements of MLSAE compared to training multiple single-layer SAEs, especially considering the increased number of activation vectors involved in training MLSAE.

### Questions
Please refer to the weaknesses section, specifically:
* regarding (1 and 2) - can you provide direct comparison to other methods or explain why such comparisons are absent?
* regarding (4)  what is the additional overhead when training/using MLSAE?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method based on sparse autoencoders (SAEs) for recovering features and analyzing the distributions of activations of the same features (SAE latents) across layers in Pythia language transformers of different sizes. The SAE is trained in a manner that treats per-token feature vectors (potentially transformed with tuned lens) from all layers as independent training examples. Hence, the method is named Multi-layer SAE.

Contrary to the authors' hypothesis that features often remain active at later layers once they are activated, the experiments show activations of the latents are often more localized and active at a single layer.

### Strengths
- The paper is well written.
- The experimental evaluation is well done.
- The research area of the paper is mechanistic interpretability, which is a potentially very useful for understanding complex models and important for AI safety.

### Weaknesses
1. Some things might be unclear (on the first reading):
	- this layer may differ for different tokens or prompts -> which layer it is might differ ... ?
	- Under multiple figures: "expected value of the layer" -> "average layer index" or "expected value of the layer index"
	- Eq. (3): The meaning of $\operatorname{Var}$ could be clarified. It is not clear if the variance is computed over the features of a single vector, or over a set of vectors. If it is the latter, it should be clarified that the variance is computed over the set of all feature values across all vectors in the set, treating each feature as an independent sample.
	- In some places, the notation is a bit inconsistent or non-standard.
		- In section 3.1, $\bf x\in\mathbb R^d$, but in Eq. (3), $\bf x$ represents a sequence of vectors $\bf x_\ell$.
		- Eq. (9): $\hat{\bf x}_\ell$ is the same as $\bf x_\ell$. It is a bit confusing that two symbols are used for the same thing.
2. Some training details seem missing: How are layers for mini-batches sampled?
3. It is not very clear to me how the paper is advancing the research in mechanistic interpretability. Perhaps commenting more on what motivated the investigations and what the results suggest for future work directions would be valuable.
4. The paper does not state whether the source code for reproducing the experiments will be published.

There are a few errors:
- L245: "ratio between the model dimension and the number of latents" should be the other way around.
- L353: Should $\mathbb E_T[L\mid J=j]$ be $\mathbb E[L\mid J=j]$ (or, equvalently, $\mathbb E_L[L\mid J=j]$)?

The single-prompt heatmap in Figure 21 appears to show a bimodal distribution of activations over layers for some latents. However, this might be an artifact of the sorting procedure. It is not clear if the sorting is done using the sum of activations over layers or the average activation over layers. If the sorting is based on the sum, then the bimodal appearance is likely an artifact of the sorting procedure. The lack of a colorbar also makes it difficult to interpret the values in the figure accurately.

I apologize for any errors on my part.

### Questions
Questions:
1. How much of computational resources did the experiments require?
2. L301: "we found the mean cosine similarities increased accordingly". This is not true for smaller models. Do you have any intuitions about that?
3. The analysis is normalizing histograms of activations over layers to get distributions. This loses information about relative frequencies of activations of different latents or about the number of layers in which each latent is active. Do you have any comments on this?
4. The paper uses metrics based on variance of the layer index. When looking at a single token, they depend on the number of activated layers as well as their distance. Could measuring the number of activated layers be more useful or easy to interpret for some purposes?
5. What is the intuition behind the hypothesis that features often remain active at later layers once they are activated? Is the hypothesis based on analogous observations when the SAE is trained only on the last layer?

If the questions make sense, I would like the final paper to address them.

Suggestions:
1. Eq (8): Note that the residual connection matters only because of L2 regularization (and because if it effectively changes the initialization).

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
2

### Summary
This study introduces a novel approach called MLSAE for analyzing the evolution of representations across various layers in Transformers. The author presents comprehensive experimental evidence to elucidate the statistical characteristics of representations at different layers. Nonetheless, how these statistical analyses can help the understanding of the inherent mechanisms within Transformers not that clear.

### Strengths
1. This work proposes the MLSAE method to analyze the interpretability of information transmitted through residual flow in Transformers. 
2. The author only uses one SAE in multi-layer Transformers. 
3. The author analyzes the fraction and variance of latents of models of different sizes through detailed experiments.

### Weaknesses
1. As indicated in both the Abstract and Conclusion sections, the author investigates the transformation of representations across various layers within Transformers. However, the analysis is limited to a statistical perspective, focusing solely on the fractions and variances of representations at different layers. The linkage between this statistical overview and a deeper understanding of the underlying mechanisms of Transformers is not explicitly articulated. It remains unclear to me how these statistical descriptions facilitate insight into the working mechanism of Transformers.
2. The motivation for the author's selection of Stacked Autoencoders (SAE) as the dimensionality reduction technique is unclear for me. The advantages of employing an SAE, which necessitates training, over more traditional statistical methods such as Principal Component Analysis (PCA) or t-distributed Stochastic Neighbor Embedding (t-SNE) for analyzing the latent space, are not clearly delineated. This choice warrants further clarification.

### Questions
Please refer to the Weakness Section.

### Soundness
3

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
This paper introduces a novel technique for training a SAE which can be applied to any layer of a model, called a MLSAE, by using training samples drawn from all layers of the model. This is beneficial because it is desirable to be able to see how the active latents change from layer to layer. To address differences in norm between layers, the paper normalizes activations and optionally applies tuned lens to help ensure that activations share the same basis. The paper studies to what extent latents are active across multiple layers as a function of model size, SAE sparsity, and SAE width using Pythia models of various sizes.

### Strengths
The problem of studying SAE latents across multiple layers is an important and understudied problem, and the contribution of training a single SAE on activations from multiple layers is novel. Using TunedLens as a pre-processing step is also novel. The paper is clear and understandable.

### Weaknesses
The paper does not evaluate the quality of the resulting MLSAEs using standard metrics, such as variance explained and cross-entropy loss when the SAE is inserted into the model. It is very easy to train a poor quality SAE, and it is not clear if the MLSAEs in the paper are decent SAEs by these metrics. There is also no performance comparison to a standard single-layer SAEs to see if MLSAEs result in a performance decrease when evaluated on a single layer. The paper only evaluates on Pythia models and topk SAEs - it would be beneficial to study other models and SAE architectures if possible. The paper also lacks a thorough investigation into the potential for redundant latents, especially given the observation that many latents are active at only a single layer. It is unclear if the MLSAE is learning truly distinct features across layers or simply re-learning similar features with slight variations for each layer.

### Questions
- The paper mentions not having a pre-trained TunedLens in some cases - where are these pre-trained TunedLenses from?
- Why does Figure 6 have only Pythia 70m and 160m, and only TunedLens for 70m? The rest of the paper has many more sizes evaluated with and without TunedLens
- I was surprised that in Figure 3 so many latents are active at only a single layer. Is it possible the MLSAE has effectively learned the same latent multiple times for different layers?

### Soundness
3

### Presentation
3

### Contribution
4
