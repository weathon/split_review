# Setting the Record Straight on Transformer Oversmoothing

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Transformer-based models have recently become wildly successful across a diverse set of domains. At the same time, recent work has shown empirically and theoretically that Transformers are inherently limited. Specifically, they argue that as model depth increases, Transformers oversmooth, i.e., inputs become more and more similar. A natural question is: How can Transformers achieve these successes given this shortcoming? In this work we test these observations empirically and theoretically and uncover a number of surprising findings. We find that there are cases where feature similarity increases but, contrary to prior results, this is not inevitable, even for existing pre-trained models. Theoretically, we show that smoothing behavior depends on the eigenspectrum of the value and projection weights. We verify this empirically and observe that the sign of layer normalization weights can influence this effect. Our analysis reveals a simple way to parameterize the weights of the Transformer update equations to influence smoothing behavior. We hope that our findings give ML researchers and practitioners additional insight into how to develop future Transformer-based models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates how Transformers oversmooth through the lens of low/high-pass filters and introduces a reparameterization of the product of the output and value projection matrices to avoid oversmoothing. The paper presents conditions in which Transformers are not low-pass filters using analysis of the domination of the eigenvalues of the attention matrix and how at the infinite-layer limit, the feature vectors converge to different solutions based on the domination of these eigenvalues.

### Strengths
1. The paper provides a good analysis of when and how to avoid over-smoothing in Transformers is an important problem since Transformers in practice have many layers.

2. The paper is well-motivated.

### Weaknesses
1. The proposed method for avoiding oversmoothing is based on the claim that H becomes more symmetric as the training progresses. However, it is not confirmed that H eventually becomes a symmetric matrix. Therefore, parameterizing H as a symmetric matrix might restrict the expressive power of the Transformer model as a whole. Specifically, if the true optimal solution for H is not symmetric, forcing it to be symmetric will limit the model's ability to reach that optimum. This constraint could lead to sub-optimal performance, especially in complex tasks where asymmetric interactions might be crucial.

2. There is no definite answer to why the ViT-Ti^- version improves robustness and data efficiency. The intuition provided by the authors is not enough to answer this because robustness and data efficiency are more nuanced than simply choosing higher-frequency features. For instance, robustness to specific corruptions might be linked to learning features that are invariant to those corruptions, which is not necessarily guaranteed by selecting for high-frequency features. Similarly, data efficiency could be related to the model's ability to learn generalizable representations from limited data, which is a more complex issue than simply focusing on high frequencies.

3. The writing of the paper is not polished, which creates confusion in key details of the paper. For example, given the redundancy in the cases in Theorem 1, maybe Theorem 1 could be rewritten to make the main result easier to read. The current presentation makes it difficult to quickly grasp the core message of the theorem, and the multiple cases obscure the main result. A more concise and focused presentation would greatly improve the clarity of the paper.

4. In Table 1, the authors show the distribution of the dominating eigenvalues but do not show whether the features oversmooth when \lambda_1^A dominates. This must be verified because the Theorems presented only work when the attention matrix A is fixed across layers, which does not hold for all practical settings. Therefore, showing the distribution of the dominating eigenvalues without showing how they affect the final features is vacuous. The link between the eigenvalue distribution and the actual feature behavior needs to be explicitly demonstrated, especially given the assumption of a fixed attention matrix is often violated in practice.

### Questions
1. The precise definition of dominating eigenvalues should be given to make Theorem 1 easier to read.

2. “To show a case where over-smoothing is guaranteed, we also define a model diag(ΛH) := −(ψ^2), which we refer to using the superscript +.” I think the authors mean diag(ΛH) := +(ψ^2).

Minor Comments that did not affect the score:

1. It would be good if the authors could compare the runtime of their ViT-Ti^+ with other methods.

2. The authors showed the distribution of dominating eigenvalues of their - version on CIFAR10, but not on ImageNet. It would be interesting to see if the distribution of the dominating eigenvalues is still the same on ImageNet.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the issue of oversmoothing in Transformers, demonstrating that it is not a pervasive problem, as Transformers do not always act as low-pass filters. The authors provide a theoretical analysis to delineate the conditions under which oversmoothing occurs and when it does not. Drawing insights from these findings, they introduce a novel reparameterization technique designed to mitigate oversmoothing. In addition, the authors conducted experiments with the Vision Transformer (VIT) and showcased the effectiveness of their proposed approach in addressing the oversmoothing issue, enabling VIT models to achieve greater depth and better robustness.

### Strengths
1. The authors undertake a comprehensive investigation, encompassing both theoretical and empirical analyses, to gain insights into the oversmoothing phenomenon within Transformers. They give clear explanations regarding the underlying reasons for oversmoothing.

2.  A novel reparameterization technique is introduced as a solution to mitigate the oversmoothing problem.

3. Empirical evaluations validate the efficacy of the proposed approach in addressing oversmoothing, showcasing its ability to deepen Transformers and enhance robustness in Transformer models.

### Weaknesses
The empirical evaluations in this study are exclusively conducted on computer vision tasks. However, there is an expectation for a broader and more diverse range of tasks, including but not limited to natural language processing (NLP) and multimodal tasks, to provide a more comprehensive evaluation of the proposed approach. Specifically, the absence of experiments on sequence-based tasks, which are fundamentally different from image-based tasks, raises concerns about the general applicability of the proposed reparameterization technique. The current evaluation does not sufficiently demonstrate the robustness of the method across different data modalities and task structures. For instance, the oversmoothing phenomenon might manifest differently in sequential data compared to image data, and the proposed solution may not be equally effective in both scenarios. Furthermore, the study lacks an analysis of computational costs associated with the proposed reparameterization, which is crucial for practical applications, especially when considering the increased depth of the models.

### Questions
Can the proposed approach effectively mitigate oversmoothing even when employing an exceptionally high number of layers? 
Additionally, what is the performance impact of this approach on NLP tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the oversmoothing behavior in deep transformer networks. The authors' main focus is in showing under what conditions popular transformer architectures are amenable to oversmoothing and how to mitigate it. The authors mainly analyze residual plus self attention layer using its eigenspectrum. They first show that one eigenvalue will dominate the rest based on phases of H and eigenvalues of A. Depending on the dominating eigenvalue, the representation of the network will converge either to a single vector or a rank one matrix. Theorem-3 further shows that oversmoothing is not inevitable and residual connections and H can counteract it. Finally, the authors show a sufficient condition for counteracting oversmoothing via constraining the eigenspectrum of H to [-1, 0). Experimental results show that proposed solution is effective in counteracting oversmoothing and existing networks do not necessarily oversmooth.

### Strengths
The paper is easy to follow with necessary details given to understand the theory. It extends the available theory and proposes a new perspective on reparameterization. Experimental results support the proposed theory and preventive measures on oversmoothing.

### Weaknesses
While the theory extends previous work in some aspects, it is not clear if this difference is significant. Other preventive measures such as AttnScale/FeatScale from Wang et al. needs comparison and more discussion. Several details are also missing from the paper.

1. Wang et al also examines residual blocks and FFN in addition to the self-attention layer. While they mention the inevitability of high frequency components to be suppressed, their analysis suggest that using residual connections might prevent it from collapsing to zero. In fact, Eq (6) in Theorem-3 suggests that it is possible to prevent decaying of high-frequency components by constraining the $||W_V||_2$ properly so that it is a non-contractive mapping. I think a more detailed comparison to Wang et al is needed to highlight how your analysis differs from low-pass filtering aspect and how your preventive measures are different from constraining $||W_V||_2$ or AttnScale/FeatScale that Wang et al applies.

2. While Figure-2 shows that asymmetry degrades with more epochs, is 0.7 small enough to suggest symmetry, given that it starts at 0.95? What about outliers in the off-diagonal entries? Additionally, can you connect it to the condition number?

3. Can you clarify more on how do you update $\Theta$ in $QR(\Theta)=[V_H, R]$? Do you do QR decomposition after every gradient step or do you use $\Theta R^{-1}=V_H$ where you backpropagate gradients directly to $\Theta$?

4. How does the HFC/LFC evolve in training steps? 

5. At the end of Section 4, page 6, why do you have $V_H^{-1}$ after clip?

6. The same page, last paragraph, I think it should be $diag(\Lambda_H)=\Psi^2$ -- no negative sign.

7. Please define Q in the main statement of Theorem-2.

8. Page 6, "||" is missing in definition of asymmetry.

9. Please describe the metrics for Table-2 and Table-3.

### Questions
Please see above for more details.

1. Can you provide a more detailed comparison with Wang et al? Including more baselines.

2. How should I interpret the asymmetry metric? How does it relate to condition number?

3. Can you give more details on updating QR decomposition?

4. How does HFC/LFC evolve during training?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyses the oversmoothing effect in Transformers. They find that Transformers are not inherently low-pass filters but oversmoothing depends on the eigenspectrum of the update equations. To prove this, the authors analyse a simplified Transformer architecture and incorporate the spectrum of attention and weight matrices. The authors relate their findings to existing pretrained architectures. They finally propose a reparametrization of the Transformer weights that ensures that oversmoothinng does not occur. The implications of such a reparametrization can be detrimental, as preliminary experiments show.

### Strengths
The paper builds on the established and successful framework of Wang et al, that analyses the degree to which a function is a low-pass filter. Doing so:
1. They give new insights on the eigenspectrum of both attention and weight matrices.
2. They find that, surprisingly, the transformer updates do not always lead to a low-pass filter.
3. Motivated by their findings, they propose a new parametrization for the linear layers following the self-attention computation. This leads to a change in the dominating eigenvalues. The authors showcase how these changes can lead to superior performance under cases of severe corruption or for low-data regimes.

### Weaknesses
1. Overall I find the main contributions/results hard to digest. Most of the results seem to be extensions from Wang et al.
2. Oversmoothing is primarily a problem that prohibits/hampers training at initialization (see e.g. Noci et al.). The authors make the same observation, while also noting that trained models exhibit different behavior. In that sense, it would make more sense to show if/how their new parametrization enables training in severe cases of oversmoothing, as e.g. when the networks become much deeper. Although I do find the applications of low-data and corruption interesting, their motivation is less clear. It could be interesting to analyse what is happening during the early phase of training.
3. Oversmoothing is less of a problem in ViT for image classification, compared to other scenarios. In image classification, labels are sparse -- 1 per sequence of tokens -- and some oversmoothing in deeper layers is expected -- in fact modern ViT just use the mean activations of the last layer to make predictions [1]. In that sense, a task in vision or language that requires a higher rank output, requiring a different prediction per token, could be more desirable. 
4. The authors analyse a simplified Transformer architecture, making some non-trivial assumptions along the way. It is not clear how these findings generalize to a more general scenario. In more detail:
- They analyze a 1-head attention layer.
- They assume the same attention and weights are repeated across layers.
- They ignore the existence of LayerNorm.
- Attention weights change depending on the data.

Most notably, Pre-LN architectures [2] have been shown to effectively counteract some of the oversmoothing in Transformers. In the experiment sections, ViTs used by the authors seem to include LN as far as I can tell. The authors should make this clear.

### Questions
1. Can you comment on how your findings will change in the presence of different weights per layer and in the presence of pre-ln layers?
2. If oversmoothing is the problem, what about other ways to mitigate it? I am talking about scaling the residuals (Noci et al, [1, 2]) or initializing the attention layers differently, e.g. [3] or different initializations per layer, e.g. [4]. There is a long list of proposed techniques in the literature from the signal propagation perspective. Since you are proposing a new parametrization, it makes sense to compare what you are achieving compares to what they are trying to achieve. Ensuring that the Transformer is not a low-pass filter, does not necessarily mean that any of the meaningful signal is preserved or that feature learning can take place.
3. Before section 5, should the superscript $^+$ model be initialized as $\text{diag}(\Lambda_H) = + (\psi^2)$?
4. Can you comment on the stability of your new parametrization? Especially what (if any) are the differences in the early stage of training. 

[1] Noci, Lorenzo, et al. "The shaped transformer: Attention models in the infinite depth-and-width limit." arXiv preprint arXiv:2306.17759 (2023).

[2] He, Bobby, et al. "Deep transformers without shortcuts: Modifying self-attention for faithful signal propagation." arXiv preprint arXiv:2302.10322 (2023).

[3] Trockman, Asher, and J. Zico Kolter. "Mimetic Initialization of Self-Attention Layers." arXiv preprint arXiv:2305.09828 (2023).

[4] Zhang, Hongyi, Yann N. Dauphin, and Tengyu Ma. "Fixup initialization: Residual learning without normalization." arXiv preprint arXiv:1901.09321 (2019).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
