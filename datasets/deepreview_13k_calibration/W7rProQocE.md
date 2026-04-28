# GrEASE: Generalizable Spectral Embedding with an Application to UMAP

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Spectral Embedding (SE) is a popular method for dimensionality reduction, applicable across diverse domains. Nevertheless, its current implementations face three prominent drawbacks which curtail its broader applicability: generalizability (i.e., out-of-sample extension), scalability, and eigenvectors separation. In this paper, we introduce $\textit{GrEASE}$: Generalizable and Efficient Approximate Spectral Embedding, a novel deep-learning approach designed to address these limitations. GrEASE incorporates an efficient post-processing step to achieve eigenvectors separation, while ensuring both generalizability and scalability, allowing for the computation of the Laplacian’s eigenvectors on unseen data. This method expands the applicability of SE to a wider range of tasks and can enhance its performance in existing applications. We empirically demonstrate GrEASE's ability to consistently approximate and generalize SE, while ensuring scalability. Additionally, we show how GrEASE can be leveraged to enhance existing methods. Specifically, we focus on UMAP, a leading visualization technique, and introduce $\textit{NUMAP}$, a generalizable version of UMAP powered by GrEASE. Our code will be publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a post-processing step named GrEASE (Generalizable and Efficient Approximate Spectral Embedding) to handle three drawbacks in spectral embedding including generalizability, scalability, and eigenvectors separation.

### Strengths
To handle the three limitations of spectral embedding, the authors design a Generalizable and Efficient Approximate Spectral Embedding (GrEASE) method. Meanwhile, it also is extended to UMAP visualization. Besides, the presentation of the paper is good and clear to follow.

### Weaknesses
1) The main contribution seems to add the post-processing step of the SpectralNet. It still needs to rely on SpectralNet to solve the generalizability and scalability problems.
2) There are some problems with the proposed method including the correctness, persuasiveness, and presentation.
3) In experiments, the experiments are unclear and the evaluation is not persuasive.
4) There are some typo errors.

### Questions
In this paper, the authors propose a post-processing step named GrEASE and extend it to the UMAP visualization. Here are some comments:
1) As shown in introduction, the main contribution seems to add the post-processing step of the SpectralNet. It still needs to rely on SpectralNet to solve the generalizability and scalability problems. Although it can be extended to UMAP, the contribution is not enough. 
2) The spectral embedding is a representation learning method. Thus, the authors could discuss the extension of the proposed method on main representation learning such as GNN or transformer.
3) In section 4.1, what are matrix Q and V? What is the dimension of V? Is it a QR decomposition of U? The authors should discuss this equation and motivation in more detail.
4) In section 4.2, why does the proposed method solve the k+1 eigenfunctions at first, instead of directly solving k eigenfunctions? 
5) In line 453, what is the true vector? And how to obtain them for evaluation?
6) The representation learning method generally is evaluated on downstream tasks. Thus, the authors should add experiments about this like SpectralNet evaluated on clustering.
7) In Table 4, the batch size is so large. Thus, I'm concerned about the stability of the model. The authors should analyze this convergence.
8) There are some typo errors including missing definitions of the symbols and missing sequence numbers of the equations.

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
4

### Summary
This paper addresses limitations in Spectral Embedding (SE), a popular non-linear dimensionality reduction technique widely used in applications like visualization (e.g., UMAP), Graph Neural Networks (GNNs), and protein analysis. SE’s strengths lie in its ability to preserve global data structure through projections onto eigenvectors of the Laplacian matrix. However, SE faces three main challenges in modern applications: generalizability (handling new data points without re-computation), scalability (processing large datasets efficiently), and eigenvector separation (directly extracting leading eigenvectors).

The authors build on SpectralNet to introduce GrEASE (Generalizable and Efficient Approximate Spectral Embedding), which achieves scalability, generalizability, and eigenvector separation, enhancing SE’s utility across diverse applications. They further present NUMAP, a novel adaptation combining SE initialization with UMAP’s loss function, achieving results similar to standard UMAP while also generalizing to new data. NUMAP addresses limitations in Parametric UMAP (P. UMAP), which lacks global structure preservation.

The contributions may include:

1. GrEASE, a generalizable SE method with eigenvector separation.
    
2. A foundation for new SE applications and enhancements.
    
3. NUMAP, an adaptation of GrEASE for generalizable UMAP.

4. A new evaluation method for dimensionality reduction, enabling better assessment of global structure preservation.

### Strengths
1. The introduction of NUMAP as a generalizable alternative to UMAP, which preserves the global structure while allowing for out-of-sample extension, showcases creative integration of SE principles with modern visualization techniques, addressing limitations in Parametric UMAP (P. UMAP).

2. The authors address common challenges in SE with rigorous methodological enhancements, particularly with the post-processing approach for eigenvector separation, which ensures that GrEASE provides accurate and interpretable embeddings.

3. The proposed evaluation metric for global structure preservation could also become a valuable tool for assessing future dimensionality reduction techniques.

### Weaknesses
1.  While the paper introduces GrEASE as an enhancement to SE, the experimental comparisons focus mainly on classical SE methods and UMAP adaptations, with limited exploration of other state-of-the-art generalizable embedding methods or scalable techniques that target similar applications, such as LargeVis or PaCMAP.

2. The experiments mainly rely on synthetic and operational datasets, which may not fully capture the complexity or variability encountered in real-world applications where SE is commonly applied, such as social network analysis or biomedical data.



### Questions
In additional to the above comments, this reviewer does have the following specific questions on technical details.

1. Minimising R_L(U) is actually a Grassmann manifold optimization problem. The paper could elaborates on this further.  Lemma 1 is in fact an explicit fact on the Grassman manifold.

2. Between Line 249 and 251, not sure why suddenly talk about Laplace-Beltrami operator.  In the paper context, Laplacian matrix is sufficient enough.

3. In line 262, can you please more specifc on the meaning of "it becomes apparent that the SE was seldom attained."?

4. I would like to see an exact definition of the separation of the eigenvectors.

5. In line 294, why you say "Q is a property of ..."?

6.  Line 298:  Can you give a proof that the eigenvalues of \tilde{\Lambda} are the eigenvalues of L", particularly when  \tilde{\Lambda} comes from the average of batch operations?

7. Can algorithm 2 be moved into the main text?

8. In Algorithm 1 (line 754), which Sec. 3.2.  I did not find out loss function.

9. Algorithm 2 is not clearly defined.  After getting Q, how is this converted to the algorithm output F_{\theta}? Do you mean F_{\theta} = VQ, while V comes from the network output?

Overall, the paper should be carefully revised to make it more specific and concise.  For example, I would like to see paragraph between 294 and 298) to be replaced with mathematical description.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new method that aims to achieve a three-fold contribution to the field of dimensionality reduction: (1) parametric embedding, (2) eigenvector separability, and (3) output of eigenbasis.

They combine this approach with UMAP, leading to another method called NUMAP.

### Strengths
The authors provide a good framework in which to embed their own work.

The related work section seems extensive.

The appendix appears extensive.

From their claims it seems promising that a new approach can strike a balance between the three described SE goals.

### Weaknesses
If, as described in ll. 341ff, the representation is learned from the UMAP embedding space via a parametric network, then it is unclear how this approach can have more scalability than parametric UMAP (which only does the first part), which the authors claim in their introduction.

I am surprised to see that the time for computing the spectral embedding via the eigensolvers AMG and LOBPCG are so slow.  Could this perhaps be related to the construction of the kNN graph?  If so, it would be better to either exclude the graph contstruction or to use the same graph building as UMAP does (which uses an approximate version via annoy or pynndescent).

Overall, it feels like it's more of a minor extension of Shaham et al. (2018) and it is not sufficiently clear why the improvements are significant enough.  This also relates to a comparison that is mostly only done to parametric UMAP, raising concerns about the tanglible improvements over prior work.

The choice of using the Grassmann score seems unusual.  Why are other approaches like correlation between high-dimensional and low-dimensional points not considered?  Especially since it's the main metric that they show improvements on, it feels like it is not discussed enough in the main text.

### Questions
- Why is outputting the basis relevant?  The authors give a few citations, but it would be good to highlight that in their own words.
- Why are the visualizations in 5b only compared to parametric UMAP?  It would be good to see how other approaches fare on the data.
- Please make sure that the scatter plot visualizations have a 1:1 aspect ratio.  They look very distorted in e.g. Fig. 7, I am unsure whether this is then also distorted in the main body figures.
- The embeddings in Fig. 4 are not labeled.
- Since the authors talk a lot about scalability, it would be nice to see some large-scale real-world datasets 
- What is meant by UMAPs contrastive loss (l. 343)?  UMAP uses a binary cross-entropy loss.
- It would be good to make the evaluation more consistent.  Sometimes only GS and kNN are reported, and sometimes the silhouette score.  It would be beneficial to include all of the metrics and summarize them in one place.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers a parameterized technique for computing the spectral embedding (SE) of a dataset. They note that parameterized methods exist for finding an embedding with respect to spectral clustering (namely, SpectralNet). Therefore, the authors propose a modification to this technique which ensures that the eigenvectors of the Laplacian are correctly distinguishable in the obtained embedding. The authors show this to be the case experimentally and propose a metric -- the Grassmann score -- with which they measure the resulting embeddings.

### Strengths
I agree with and commend this paper's stated goals -- improving data visualization techniques' scalability and generalizability is a useful direction which aligns well with this conference's scope. Furthermore, I believe that parameterized methods for data visualization are under-studied and that there are interesting objectives which can be optimized in this space.

Additionally, I am interested in understanding how to produce UMAP outputs and what the properties of these outputs are. To this end, I believe the idea of the Grassmann score for measuring the quality of an embedding is an interesting one. I have long considered that the usage of kNN scores is insufficient for measuring data-visualization quality.

### Weaknesses
Unfortunately, the weaknesses in this paper significantly outweigh its strengths. These are organized into the following three themes: the premise of the paper, the experiments, and the technical clarity.

## Premise

Unless I am missing something, this paper's primary technical contribution is to apply a change-of-basis to the output of SpectralNet. This... does not feel like a sufficient contribution for ICLR. Furthermore, it is wholly unclear to me why this change-of-basis is even necessary. Yes -- the authors show that SpectralNet's outputs are not unique up to orthogonal transformation. And yes -- these embeddings might not correspond to the exact eigenvectors of the Laplacian. However, I fail to see how this is cause for any concern or, indeed, why this is something that needs to be remedied.

As far as I understand, the embeddings from SpectralNet and the embeddings from GrEASE are the exact same output except that GrEASE takes the points and rotates them. If we are simply rotating the outputs of SpectralNet, then how does this have any impact on downstream uses of the embeddings? For example, whether this rotation was applied clearly makes no difference if we then use the embedding as an initialization for UMAP (as is the primary use-case in the paper) or for spectral clustering (the most common use for spectral embeddings). Thus, I find it difficult to understand the primary motivation for this technical contribution in the first place. Please correct me if I have misunderstood something.

## Experiments

Part of the confusion surrounding the motivation comes down to the experiments: it seems that the authors have chosen experiments which emphasize that GrEASE finds the exact eigenvectors of the Laplacian but have not run experiments to explain why this was necessary to do. For example, the usage of the Grassmann score to measure distance between the Laplacian vectors and the identified vectors shows that GrEASE is better at identifying the eigenvectors of the Laplacian. However, this experiment does little to explain *why* this is helpful. Instead, the only evidence of GrEASE's improved embeddings seems to be Figure 1, where results are shown on three toy datasets. The sparsity of the dataset choices and the lack of quantitative measures however does not make Figure 1 sufficient evidence to justify the fact that GrEASE was necessary (additionally, there is no code attached so the experiments are not reproducible).

Instead, I would be more interested in an in-depth evaluation of the outputs of GrEASE. The authors have proposed a dimensionality reduction technique for getting a spectral embedding and yet we do not see a single spectral embedding in the paper. What do the GrEASE outputs look like? How do they compare against standard Laplacian Eigenmaps or spectral embeddings? Similarly, the paper is in need of a comparison between SpectralNet and GrEASE outputs. If the authors are crafting their submission around modifications to SpectralNet, then a comprehensive evaluation of why this was necessary is in order. Are GrEASE outputs significantly different from SpectralNet ones? An experimental verification of the issues of SpectralNet outputs would be helpful in explaining why GrEASE was necessary.

## Technical Clarity

These issues are exacerbated by the writing of the paper. While the text is often easy to read from a stylistic perspective, the technical substance is imprecise and the reader must make guesses about what the authors mean.

The most pertinent example of this is the term "eigenvector separation," which is used throughout the paper. This is not a term that I am familiar with and it took until page 5 that I even had a guess as to what was meant by it (I believe it means that the spectral embedding is aligned with the eigenvectors rather than some linear combination of them). Since this is a key notion behind the paper, it requires a clear, unambiguous definition.

In addition to this, it seems that the term "spectral embedding" is used in a specific way which feels different from my expectation. I would expect the spectral embedding to be the $n \times k$ matrix of leading eigenvectors of the Laplacian *or any orthogonal transformation of this matrix*. Indeed, the orthogonal transformation is arbitrary with respect to the relevant use-cases of spectral embeddings such as spectral clustering and UMAP. Thus, the implication in lines 239-240 that "this does not lead to the [spectral embedding]" feels unsubstantiated.

The writing has several smaller cases of impreciseness. For example, the first sentences of the intro state that SEs are used in GNNs and GCNs? I don't believe this to be true. Additionally, the Grassmann Score is left completely undefined and I have no idea how one calculates it. Furthermore, the applications seem incomplete. It is currently completely unclear to me how GrEASE relates to Diffusion Maps. Separately, if one wished to approximate the Fiedler vector, then this is a well-studied problem and there are fast methods for doing it such as [1]. Lastly, I strongly disagree that the complexity is linear in the number of samples (line 315). For one thing, I'm not sure what is meant by "samples" here. More importantly, however, I think Figure 2 is comparing apples to oranges. GrEASE works by running mini-batches and averaging their outputs. However, it seems the competitors are running on all $n$ inputs? Also, are these all on GPU or are we comparing CPU times to GPU times? Does the runtime include training time? How many batches were run? If the code was available, these things would be easier to check.

### Questions
My primary question is for the authors to explain why GrEASE is necessary as a substitute for SpectralNet. Specifically,
- What happens if we use SpectralNet outputs as the input to Parametric UMAP (rather than GrEASE outputs)? I suspect that this will perform equivalently to NUMAP and would require thorough, reproducible experiments to convince me otherwise. If SpectralNet and GrEASE perform the same as an input to UMAP, this would contradict the primary motivation of the paper that the eigenvector separation is indeed necessary.
- How do GrEASE and SpectralNet outputs differ? How do they compare to standard Laplacian Eigenmaps/spectral embeddings?
- How does GrEASE help in getting generalizable diffusion maps? This is completely unclear to me.

### Soundness
1

### Presentation
2

### Contribution
1
