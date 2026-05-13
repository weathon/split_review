# Noise Robust Graph Learning under Feature-Dependent Graph-Noise

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
In real-world scenarios, node features frequently exhibit noise due to various factors, making GNNs vulnerable. Various methods enhance robustness, but they make an unrealistic assumption that the noise in node features is independent of the graph structure of node labels, restricting their practicality. To this end, we introduce more realistic noise scenario, called feature-dependent graph-noise (FDGN), where noisy node features may entail both structure and label noise, and propose a generative model to capture these causal relationships. Our proposed method, PRINGLE, outperforms baselines on commonly used benchmark datasets and newly introduced real-world graph datasets that simulate FDGN in e-commerce systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new setting under graph weakly-supervised learning, named feature-dependent graph-noise, where the noise could be presented on either edge, label, and feature. To counter this proposed noise, authors leveraged the variational autoencoder (VAE) to model the latent variable and capture the causal relationship.

### Strengths
1. Authors adapt a causal prospective to justify the feature-dependent graph-noise, which is intuitive and sensible under mild assumptions.

2. This paper is overall well-presentated, the ideas are easy-to-follow.

3. The proposed metod demonstarates strong performances over multiple settings (graph noise, edge noise, label noise, feature noise).

### Weaknesses
1. The proposed solution lacks technical novelty, using VAE to model the causal relationship and counter noise has already been proposed by [1]. This paper only incrementally adapts that solution on the graph.

2. The proposed solutions lack theoretical support, the derivation on ELBO are well-known results, and the authors are only re-stating them here.

3. The proposed solution seems to have very high complexity (there are three encoder-decoder pairs, and three objectives to compute), therefore an efficiency analysis is needed.

### Questions
not at the moment

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper show that many existing robustness-enhancing methods assume noise in node features is independent of the graph structure or node labels. This is potentially an unrealistic assumption in real-world situations. In response, the authors propose a novel noise scenario called feature-dependent graph-noise (FDGN) and an accompanying generative model to address it.

### Strengths
1. The experiments are extensive. 
2. The performance is good. 
3. A new dataset is introduced.

### Weaknesses
1. The proposed setting is a combination of popular GNN with label noise and [1]. It is better to clarify more application examples in real-world.
2. A lot of GNN with label noise works are missed [2]. 
3. The abstract cannot summarize the methodology, which makes the paper unreadable. 
4. Why the last three losses share the same weights in Eq. 4? 
5. Why the generative methods can release the label noise?

### Questions
See above

### Soundness
3 good

### Presentation
2 fair

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
This paper discovers practical limitations of conventional graph noise in terms of node features, i.e., the noise in node features is independent of the graph structure or node label. To mitigate the limitations of the existing assumption, the paper introduces a more realistic graph noise scenario called feature-dependent graph-noise (FDGN). Technically, the paper devises a deep generative model that directly captures the causal relationships among the variables in the DGP of FDGN and also derives a tractable and feasible learning objective based on variational inference. Empirically, the paper justifies the effectiveness of FDGN by conducting experiments on six datasets with both node classification and link prediction tasks.

### Strengths
The investigated problem of graph noise is essential. The paper breaks the existing assumption of feature noise, which is new to the community.

The paper is solid and extensive from a technical perspective.

The presentation and drawn figures are generally clear and easy to understand.

The paper is also theoretically grounded, with detailed justification elaborated on.

Several technical details, case studies, and evaluation results are also elaborated on in the Appendix.

### Weaknesses
Although some basic examples are given, the practical existence of causal relationships among X, A, and Y, i.e., "$A ← X, Y ← X, Y ← A$," should be further justified and supported by real-world evidence and materials. In other words, the paper should further explain why, in reality, noisy node features may entail both structure and label noise to be more convincing and practically worthy, especially in e-commerce systems. The current examples are not sufficiently detailed to establish the prevalence of this specific causal structure in real-world scenarios. For instance, the paper should elaborate on specific mechanisms in e-commerce where a user's noisy profile directly causes both noisy interactions and miscategorization, rather than just stating it as a possibility.

Further, if "$A ← X, Y ← X, Y ← A$" is true, why does the paper not choose to directly learn a clean latent $Z_X$ but choose to learn two latent variables $Z_A, Z_Y$. The rationale for not directly inferring a latent representation of clean node features, $Z_X$, is not sufficiently justified. Given the proposed causal structure, it seems more direct to infer $Z_X$ and then derive $A$ and $Y$ from it, rather than introducing two separate latent variables. The paper needs to provide a more compelling argument for why this indirect approach is necessary or beneficial.

The overall novelty is neutral. The technical key contributions of the paper are within the proposed causal model and its instantiation with a variational inference network. It skillfully combines both worlds and designs a relatively complex objective based on the KL divergence. However, the core idea of using variational inference for causal modeling is not entirely new, and the specific implementation, while technically sound, does not introduce a groundbreaking methodological advancement. The novelty is primarily in the application of these techniques to the specific problem of feature-dependent graph noise.

The writing can be largely improved. For example, there are too many "i.e., A/X/Y" in Section 3.1, which do not provide any further information but simple notations. Besides, I would suggest the paper analyze the complexity of FDGN and provide running time or training curves. The paper lacks a detailed analysis of the computational complexity of the proposed method. Without this, it is difficult to assess the practicality of the approach, especially for large-scale graphs. Providing running time or training curves would help to understand the scalability of the proposed method. In addition, most of the references are before 2023. I would suggest the paper have a discussion with one work [1] using variation inference for causal learning and one work [2] learning latent variables $Z_A, Z_Y$ for structural denoising, which are technically relevant to the proposed FDGN.

### Questions
Please refer to the above weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of node feature noise in graph learning. In this paper, the author claims that existing methods make an unrealistic assumption that the noise in the node features is independent of the graph structure or node labels, while a more realistic assumption should be that noisy node features may entail both structure and label noise. Under such an assumption, this paper proposes a principled noisy graph learning framework named PRINGLE to address the feature noise problem in graph learning. Experimental results based on several datasets are reported.

### Strengths
-	The problem of feature noise in graph learning is an important problem.
-	To the best of my knowledge, the assumption that noisy node features may entail both structure and label noise is novel, and this paper provides examples and empirical evidence to show that such an assumption is realistic.
-	The proposed PRINGLE method includes a deep generative model that directly models the data-generating process of the feature-dependent graph noise to capture the relationship among the variables that introduce noise. The proposed PRINGLE method generally makes sense.
-	Empirical evidence based on both existing benchmark datasets and newly collected datasets has been provided to show that PRINGLE outperforms state-of-the-art baselines in addressing the feature-dependent graph noise problem.

### Weaknesses
 - Minor issues about the typo: “the graph structure OF node labels” in line 4 of the abstract should be “the graph structure OR node labels”. Besides, in line 5 of page 5, “introduces” should be “introduce”.

- While the paper presents a novel assumption and a principled framework, it would be beneficial to further elaborate on the computational complexity of the proposed PRINGLE method. Specifically, how does the computational cost scale with the size of the graph and the number of features? This is particularly relevant when considering the applicability of PRINGLE to large-scale real-world graphs. Additionally, a more detailed analysis of the sensitivity of the model to different hyperparameter settings would strengthen the evaluation. For instance, how do variations in the parameters of the deep generative model impact the overall performance, and what are the recommended strategies for selecting optimal values?

### Questions
None

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
