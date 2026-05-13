# Memorization Capacity of Multi-Head Attention in Transformers

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Transformers have become the go-to architecture for language and vision tasks, yet their theoretical properties, especially memorization capacity, remain elusive. This paper investigates the memorization abilities of multi-head attention mechanisms, examining how many example sequences they can memorize, as a function of the number of heads and sequence length. Motivated by experimental findings on vision transformers, we introduce novel assumptions about the linear independence of input data, distinct from the commonly used general-position assumption. Under these assumptions, we demonstrate that an attention layer with $H$ heads, dimension $d$, and context size $n < d,$ featuring $\Theta(Hd^2)$ parameters, can memorize $\Omega(Hn)$ examples. Our analysis sheds light on how different attention heads handle various example sequences, aided by the softmax operator's saturation property. We validate our findings through experiments on synthetic data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the memorization capabilities of multi-head attention mechanisms, a core component of transformer architectures widely used for language and vision tasks. The study aims to understand how effectively these mechanisms can remember example sequences, depending on the number of attention heads and the lengths of the sequences. The research introduces new assumptions about the linear independence of input data, which differ from previous models, and under these conditions, it's shown that an attention layer with a certain number of heads and parameters can memorize a proportional number of examples. The paper further discusses how different attention heads process different sequences and how the softmax function contributes to this capability. These theoretical findings are supported by experimental results using synthetic data.

### Strengths
- The paper makes theoretical contributions by exploring the memorization capacity of transformers, an area that is not yet fully understood. This contributes to a deeper understanding of transformer architectures.
- The paper introduces new assumptions about the linear independence of input data, distinct from commonly used assumptions. This novel approach provides a fresh perspective on analyzing transformer models. 
- The findings are validated through experiments on synthetic data. This empirical approach strengthens the theoretical claims made in the paper.
- The paper includes a detailed analysis of assumptions, theoretical proofs, and experimental validation, making it a comprehensive study.

### Weaknesses
 - Limited Empirical Testing: While the paper includes synthetic experiments, real-world data experiments might be needed to fully understand the practical implications of the findings. The synthetic data experiments, while useful for isolating specific effects, may not capture the complexities and nuances of real-world datasets, particularly those found in NLP and computer vision tasks. The paper would benefit from a more thorough investigation into how the theoretical memorization capacity translates to performance on benchmark datasets.
- Focus on Single-Layer MHA Module: The study primarily focuses on a single-layer Multi-head Attention (MHA) module. Expanding the analysis to multi-layered architectures could provide more comprehensive insights. The current analysis does not address how the memorization capacity scales with the depth of the network, which is a crucial factor in the performance of deep learning models. The interactions between multiple MHA layers, and how they might affect the overall memorization capacity, are not explored.
- Potential for Broader Impact Analysis: The paper could benefit from a more in-depth discussion on how these findings impact current transformer-based models in various applications, like natural language processing or computer vision. The paper does not sufficiently discuss the implications of the theoretical results for practical model design. For example, it would be beneficial to discuss how the findings could guide the selection of the number of attention heads or the dimensionality of the key, query, and value vectors in real-world applications.

### Questions
- Could you explain the rationale behind the specific assumptions made regarding the linear independence of input data? How do these assumptions align with real-world data scenarios in transformer applications?
- How do your findings contribute to the ongoing discussion in machine learning between model generalization and memorization, particularly in the context of overfitting?
- How do your derivation connect to the Hopfield Network as one classical memory network that has recently been proven to be connected to the Transformer network [1]?

[1] Ramsauer, Hubert, et al. "Hopfield networks is all you need." arXiv preprint arXiv:2008.02217 (2020).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a lower bound on the memorization capacity of MHA layers under a rather mild linear independence assumption. Based on two input-data assumptions, the authors theoretically and experimentally prove that (1) When fixing dimension d, increasing the number of heads H improves memorization. (2) When further fixing the number of heads H, increasing the context size n improves memorization. (3) When fixing d, n, increasing dh only helps up to dh < n, there is no memorization gain beyond that.

### Strengths
1.	The paper is well-organized and the proof makes sense.
2.	The two input-data assumptions are milder than the General Position assumptions. Although it is impossible to fully verify its generalizability, the author demonstrated the reasonableness of the assumptions through sampling testing, which interests me.
3.	The conclusion “When fixing d, n, increasing dh only helps up to dh < n, and there is no memorization gain beyond that” is enlightening and I believe it can bring more valuable thinking and discussion to the community.

### Weaknesses
1.	It might be significantly different between the image patch tokens (ViT) and the language tokens. Can the author's experimental verification of those assumptions be verified on NLP tasks?

### Questions
1.	The authors demonstrate that Assumption 2 typically holds in practice due to positional encoding. Does the assumption still hold when the positional encoding is learnable?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
this paper investigates the memorization abilities of MHA of transformers with theorectical analysis. Based on two new proposed assumptions, the authors find a lower bound on the memorization capacity of attention layers. The paper tested the rationality of the assumptions and validate the theorectial findings with synthetic experiments.

### Strengths
1. The assumptions in this paper are more relaxed The authors  verified the rationality of the assumptions on real data.
2. The exploration of memorization capacity of transformers is meaningful for more advanced go-to architecture, while the memorization abilities of attention modules is quite interesting. 
3. The paper is well-written.

### Weaknesses
1. One of my main concern is the illustration or definition of "memorization" in this paper. The inputs of attention include both the key matrix and the query vector. In a common understanding, attention plays a role to capture knowledge from the context according to the "attention" on other tokens for each token.  So what does attention memorize? I think the paper should make it clearer before or after the theorectical analysis, or even verify the memorized knowledge with some visualization. Specifically, it's unclear if the memorization refers to the ability to perfectly reconstruct the training data outputs, or if it's about learning a more generalizable mapping. The paper needs to clarify whether the attention mechanism is memorizing specific input-output pairs or learning some underlying relationship, and how this relates to the typical understanding of attention as a contextualization mechanism. A visualization of what is being memorized, perhaps by analyzing the attention weights or the output vectors, would greatly enhance the understanding of the paper's claims.
2. Analysis and comparison with existing works are insufficient, for example,  <<Transformer Feed-Forward Layers Are Key-Value Memories>>. How are the memories different between this paper and the reference? There are also some works about transformer   interpretability and model editing. Do the observations in these related works support the findings in this paper? I think the authors should give more analysis, rather than demonstrating the their propsed theorem only. The paper should delve deeper into how its findings relate to the broader landscape of transformer research. For instance, how does the memorization capacity of attention layers compare to that of feed-forward layers? Are there any implications for model editing or interpretability techniques? A more thorough discussion of these connections would significantly strengthen the paper's contribution.

### Questions
refer to the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors prove a lower bound on the memorization capacity of a multi-head attention layer under a new set of input-data assumptions that relax General Position assumptions previously used in similar work. The main result is that memorization increases linearly with the number of heads, monotonically with the context size, and monotonically with the head dimension as long as it is smaller than the context size. The result validates some of the common practical choices of hyperparameters. The authors verify their data assumptions empirically by checking for linear independence of context vectors and approximately testing the Kruskal Rank. They also present a synthetic experiment that confirms their theoretical findings.

### Strengths
The paper presents an important result on the memorization capacity of a multi-head attention layer using an original set of data assumptions that are shown to hold in practice. The result is verified through a properly designed experiment. The paper is well written and structured, and the logic of the argument is easy to follow. The figures are of high quality and they help to get the message across. While I haven't checked the proof in detail, the main steps seem to be sound.

### Weaknesses
It would be great to provide code for your synthetic experiments and input-data assumption validation to increase reproducibility.

It is unclear how good the approximation of the Kruskal Rank computation is. The paper mentions that computing Kruskal Rank is NP-Hard, but it does not provide any quantitative analysis of the approximation error. This makes it difficult to assess the practical implications of the theoretical results. 

It is also not clear how the specific data assumptions were derived. While the authors mention that the assumptions are inspired by previous work and practical considerations, more details on the thought process would be beneficial. Specifically, it would be helpful to understand if the assumptions were tailored to fit the proof technique, or if they were derived independently based on empirical observations.

Finally, while the authors discuss the potential for extending the proof technique to multi-layer attention networks, they do not provide any concrete results or insights. It would be helpful to understand the fundamental obstacles that prevent such an extension.

### Questions
How good is the approximation of the Kruskal Rank computation?

How did you come up with this particular set of data assumptions? Was this dictated by the proof technique you wanted to apply?

Can your proof technique be applied to prove a similar result beyond a single attention layer or is there some fundamental obstacle?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
