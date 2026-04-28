# Sparsity beyond TopK: A Novel Cosine Loss for Sparse Binary Representations

- Decision: Reject
- Avg Score: 1.67
- Scores: 3, 1, 1

## Abstract
While binary vectorization and sparse representations have recently emerged as promising strategies for efficient vector storage and mechanistic interpretability, the integration of these two paradigms has till now remained largely unexplored.
In this paper, we introduce an exciting approach for sparse binary representations, leveraging a soft TopK Cosine Loss to facilitate the transition from dense to sparse latent spaces.
Unlike traditional TopK methods which impose rigid sparsity constraints, our approach naturally yields a more flexible distribution of activations, effectively capturing the varying degrees of conceptual depth present in the data.
Furthermore, our cosine loss formulation inherently mitigates the emergence of inactive features, thereby eliminating the need for complex re-activation strategies prevalent in other recent works. 
We validate our method on a large dataset of biomedical concept embeddings, demonstrating enhanced interpretability and significant reductions in storage overhead.
Our present findings highlight the clear potential of cosine-based binary sparsity alignment for developing interpretable and efficient concept representations, positioning our approach as a compelling solution for applications in decision-making systems and compact vector databases.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
- The paper introduces a novel approach called Binary Sparsity Alignment (BSA) that transitions dense embeddings to sparse binary representations using a soft TopK Cosine Loss, enhancing interpretability and reducing storage needs. BSA avoids rigid sparsity constraints and unstable training dynamics, offering a stable and flexible method for sparse binary encoding.

### Strengths
- The research focuses on a narrow topic, specifically Binary Sparsity Alignment, which is rarely addressed by others. This method aims to enhance interpretability while reducing storage requirements.
- The approach is validated using a biomedical dataset, demonstrating effective sparsification with minimal information loss.

### Weaknesses
- The authors cite the paper on contrastive learning of predictive coding; however, the relationship between their work and the contrastive learning perspective (Oord et al., 2018) is not thoroughly discussed.
- Many of the equations presented are not commonly found in other literature, making it challenging for readers to grasp the intended message. The organization of the paper could benefit from improvement.
- The experimental validation is insufficient to support the proposed ideas. Additional experiments and the inclusion of datasets beyond the biomedical context are necessary for a more comprehensive evaluation.

### Questions
- How can your study benefit efficient storage and fast inference? In what situations and environments would this be applicable?
- How does your method enhance interpretability, especially in fields like biomedical concept embeddings, where understanding the underlying data is crucial?
- How can you demonstrate practical benefits while also establishing a theoretical foundation for understanding binary sparsification in the context of contrastive learning? Can you explain this more simply?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper introduces Binary Sparsity Alignment (BSA), a novel method for converting dense embeddings into sparse binary representations using a cosine-based loss function. Unlike traditional approaches that use hard constraints or regularization, BSA treats sparsity as an alignment problem, leading to more stable training and better preservation of semantic information. Testing on biomedical concept embeddings demonstrated that the method achieves 14x compression while maintaining semantic relationships and avoiding common issues like "dead features," all without requiring special feature reactivation strategies that are typically needed in other approaches.

### Strengths
Novel cosine-based loss function for simultaneous sparsification and binarization.

Achieves significant compression (14x reduction).

Stable training without dead features.

Tested successfully on biomedical concept embeddings.

### Weaknesses
There is no evaluation of sparse binary embeddings on downstream tasks regarding performance. At this moment, it is hard to even tell whether the compressed embeddings work. Even worse, there is no baseline comparison.

The results were reported based on only one domain (biomedical concepts).

There is no analysis of training time or computational requirements.

There is no ablation study on hyperparameters like the loss weighting parameter, batch size etc.

The presentation in this paper is poor, the authors did not even write the table in latex, but screenshot some excel sheets.

### Questions
It is unclear how the approach would scale to even larger dimensions?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper presents a method to produce sparse binary embeddings based on a cosine similarity to a top-K sparse embedding. The authors expect that this will allow them to have a soft-sparsity constraint that does not unnecessarily penalize features that might appear in the data. They demonstrate the effectiveness of their sparse binary embedding in an autoencoder. They linearly project the data in a latent space, then apply a signmoid and a rounding to binary outputs, a second  representation were only the top-k values of the sigmoid is set to one and the rest to zero is also returned. Then they use a cosine metric between the output of the sigmoid and the top-k representations, to obtain something like aa soft-top-k penalty for representation. Then they reconstruct the input from that latent space with a linear decoder and optimise the encoder and decoder (both linear) with a a cosine loss between input and reconstruction.    

The method is sensible, although limited in scope - addressing only the issue where top-k would ignore significant features. I am not sure how often that is a problem with top-k sparse representations. Also, if you want to get soft approximations of sparse binary latents, I would expect to see something based on l1 sparsity penalty. I think Mairal and Bach, and the community around them,  about 10-15 years ago did a lot of work around demonstrating that the l1 is convex relaxation of binary sparse coding, and therefore yields an optimal solution. I think there are still open problems with l1 sparse coding, e.g. how do you identify optimal hyper parameters, how do you find an optimal subgradient and things like that. However, that literature around l1 is barely discussed in the paper.

The major problem with the paper is that it proposes a new method, albeit somewhat incremental, and it does not provide an analytical proof of any interesting property nor do the  authors demonstrate its efficacy in an application. Instead only some numerical experiments that resemble sanity checks are presented. For instance that after training the top-k and the binary sparse representation are correlated. This is rather obvious since their cosine similarity was part of the objective function to be optimised.

I would strongly recommend that the authors study the sparse coding literature in greater depth and/or perform more experiments on realistic data with reasonable numerical targets for method validation.

Also, some typos here and there:
Line 309: seems syntactically wrong
Line 281: This approach possesses (not possess)
Line 84: Modern auto encoders often consist of (not in)

### Strengths
New and relatively sensible method. The implementation has been validated with numerical experiments that demonstrate the model works as designed.

### Weaknesses
The paper implies ignorance of a large part of related literature. Going for a cosine similarity between a binary vector with no constraints and a binary vector with top-k constraint is a strange way to relax the hard sparsity condition. The numerical experiments only validate proper function of the implementation, they don't demonstrate an application to a real problem. Also, there is no comparison with alternative sparsity methods

### Questions
Why did you chose to work with a cosine similarity with top-k rather than a norm penalty, e.g. l_1?
Can you compare your work with some other form to sparsify latent representations?
How would your representation work in a real problem, often targeted with sparse representations, e.g. denoising?

### Soundness
1

### Presentation
1

### Contribution
1
