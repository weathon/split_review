# Interpreting Equivariant Representations

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Latent representations are used extensively for downstream tasks, such as visualization, interpolation or feature extraction of deep learning models. Invariant and equivariant neural networks are powerful and well-established models for enforcing inductive biases. In this paper, we demonstrate that the inductive bias imposed on the by an equivariant model must also be taken into account when using latent representations. We show how not accounting for the inductive biases leads to decreased performance on downstream tasks, and vice versa, how accounting for inductive biases can be done effectively by using an invariant projection of the latent representations. We propose principles for how to choose such a projection, and show the impact of using these principles in two common examples: First, we study a permutation equivariant variational auto-encoder trained for molecule graph generation; here we show that invariant projections can be designed that incur no loss of information in the resulting invariant representation. Next, we study a rotation-equivariant representation used for image classification. Here, we illustrate how random invariant projections can be used to obtain an invariant representation with a high degree of retained information. In both cases, the analysis of invariant latent representations proves superior to their equivariant counterparts. Finally, we illustrate that the phenomena documented here for equivariant neural networks have counterparts in standard neural networks where invariance is encouraged via augmentation. Thus, while these ambiguities may be known by experienced developers of equivariant models, we make both the knowledge as well as effective tools to handle the ambiguities available to the broader community.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that using equivariant representations for downstream analysis can be misleading since they can assign distinct representations to inputs that only differ by some group action. To fix this they propose projecting the equivariant representations with an invariant projection which then ensures that the projected representation preserves invariances. There are however challenges in designing such an invariant projection since it must also retain information. This paper proposes such transformations and shows that they can lead to more reliable interpretation of representations. The efficacy of the proposed method is shown on a molecule graph generation VAE and an MNIST classifier.

### Strengths
1. The paper thoroughly explains why distances in an equivariant representation space can be misleading
2. The paper explains why an invariant transform is the right way to analyze equivariant representations
3. The paper also explores different possible invariant transforms that can better analyze representations while retaining information
4. The theory is corroborated with experimental results

### Weaknesses
1. I had a hard time reading and contextualizing this paper. For example, I'm not fully sure I understand why one would use equivariant representations when the inputs do not follow the G-equivariance of the representations. For eg, if x and g.x are similar inputs, then an equivariant representation is perhaps not the correct one to analyze such data in the first place. Why wouldn't one, instead just choose some mapping f that is invariant?

2. I did not fully understand Section 4, it read more like a related work section and felt out of place.

3. It was never clear to me what "analysis of representation" meant throughout the paper. All the results indicate that "analysis" means visualization of the representations in a 2D space. Is that the only "analysis" where equivariant representations would show deceiving results? It would help with readability to clarify what kinds of analyses are hard with equivariant representations.

4. Isn't the interpolation experiment self-satisfying? You already claim that after the invariant transform the representation space is convex and thus interpolation makes total sense (and thus the nicer results in Fig 4), whereas this is not the case for equivariant representations (thus results are all over for these in Fig 4). I'm not quite sure what was the purpose of this experiment. Was it to empirically validate the theory?

5. Overall, the paper was a tough read for me. It would be very helpful to start by contextualizing a use case where equivariant representations might need a downstream analysis where equivariance can be misleading, this would help motivate the paper better.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes that latent equivariant representations should not be used naively and that invariant representations should be used. Equivariant representations should be projected in an invariant manner. The authors show empirically on a permutation equivariant graph VAE and a SO(2) invariant classifier on MNIST that invariant representations are more interpretable.

### Strengths
The authors provide a clear background to equivariant and invariant representations.

Figure 3 helps visualize the interpolation in latent space and helps the reader analyze the interpretability.

### Weaknesses
The fundamental argument of the paper seems to be that existing visualization methods cannot handle quotient spaces correctly. If I remember correctly, doesn’t UMAP map the data to a lower-dimensional manifold embedded in higher-dimensional space? Why would UMAP not be able to handle quotient spaces?

It’s unclear to me that invariant representations would be more interpretable than equivariant ones. Since equivariant representations inherently generalize invariant representations, why would invariant representations increase interpretability?

### Questions
See weaknesses.

Typo: Abstract Line 4: “inductive bias imposed on the by an equivariant”

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies the problem of directly using equivariant latent representations for subsequent visualization tasks without considering the associated inductive bias of equivariance. The authors suggest employing an invariant projection of the latent representations in Euclidean space, enabling the application of conventional visualization tools to this transformed latent space.

To validate their approach, the authors present two illustrative examples. In the first scenario, they explore permutation equivariant autoencoders applied to graph data. Through this investigation, they find an isometric cross-section, ensuring the preservation of orbit distances in the space of the latent representation.

In the second scenario, the focus shifts to rotation-equivariant representations for the task of image classification. In this example, finding an isometric cross-section proves challenging. To address this, the authors propose to use random projections, showcasing their effectiveness through practical demonstrations.

### Strengths
- The motivation behind this work is solid. The majority of visualization tools operate in a Euclidean space, and the use of an equivariant representation is indeed problematic. This particular issue has not been extensively examined in existing literature, highlighting the novelty of this study.
- The paper is well-written. The writing strikes a balance between intuition and rigorousness. The presentation is well-paced and the figures for results are clear.
- The selected examples effectively substantiate the authors' assertions and are very interesting.

### Weaknesses
See questions.

### Questions
- Are there other significant examples where an isometric cross-section can be found? Or is the latent graph representation a very unique example? If that is the case, maybe the paper should focus more on the random projection approach because it has more applications.
- Is there any theoretical results to prove that random projections approximately find isometric cross-section? If this is not true, Sec 3.1 and Sec 3.2 feel like two completely unrelated methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
