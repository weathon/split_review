# On Inductive Biases That Enable Generalization in Diffusion Transformers

- Decision: Reject
- Scores: 3, 6, 8, 3

## Abstract
Recent work studying the generalization of diffusion models with UNet-based denoisers reveals
    inductive biases that can be expressed via geometry-adaptive harmonic bases.
    However, in practice, more recent denoising networks are often based on transformers, \eg, the diffusion transformer (DiT). 
    This raises the question: do transformer-based denoising networks exhibit inductive biases that can also be expressed via geometry-adaptive harmonic bases?
    To our surprise, we find that this is \emph{not} the case. 
    This discrepancy motivates our search for the inductive bias that can lead to good generalization in DiT models.
    Investigating a DiT's pivotal attention modules, we find that locality of attention maps are closely associated with generalization. 
    To verify this finding, we modify the generalization of a DiT by restricting its attention windows. 
    We inject local attention windows to a DiT and observe an improvement in generalization. 
    Furthermore, we empirically find that both the placement and the effective attention size of these local attention windows are crucial factors. 
    Experimental results on the CelebA, ImageNet, and LSUN datasets show that strengthening the inductive bias of a DiT can 
    improve both generalization and generation quality when less training data is available. Source code will be released publicly upon paper publication. Project page: \href{https://dit-generalization.io/}{\tt dit-generalization.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the inductive bias of diffusion transformers. Specifically, the authors start by looking at the difference in the generalization behavior between UNet and DiT. Visualizing the eigenvectors of the harmonic bases, they show that the eigenvectors of smaller eigenvalues of UNet display more interesting patterns than DiT, while the PSNR gap between the training and testing dataset is large for UNet when the number of training data is smaller. Motivated by this difference, they visualize the attention maps of DiT with different training sizes and find out that the attention maps exhibited a more obvious locality pattern when the training size increased. At last, they propose to restrain the attention window size to enhance this locality property of the attention maps during the training. Their results show considerable improvement in the FID score when the training size is smaller.

### Strengths
The paper is well-presented and easy to follow. The authors conduct extensive experiments and show relative improvements in the image generalization quality on CelebA and ImageNet datasets.

Overall, I found the topic of looking into the generalization behavior of diffusion transformers very interesting.

### Weaknesses
1. The focus in the 1st part of the paper seems to disconnect from the rest, especially the method and the experimental results. I don't understand how the proposed method relates to the difference between the patterns of the harmonic bases for UNet and DiT. I am wondering do the authors observe differences in the harmonic bases after they alter the window size of the transformers. 

2. The results are concerning. Though the current results show a considerable amount of improvement with a very limited size of the training data, the downgraded performance when scaling to a larger dataset makes it hard to believe that locality is the right reason behind the good generalization capability. Specifically, the FID score increases with the local attention constraint when the training data is large, which contradicts the claim that locality enhances generalization. This suggests that the observed improvements might be due to other factors or that the locality constraint is only beneficial in a limited data regime.

Typos and the minors:

Line 190: $\sigma_t$ is undefined.

Line 202: I assume you are talking about PSNR instead of PNSR, right?

### Questions
1. Eqn. 4: What does $\hat{x}_0^k$ mean? And what’s the intuition behind setting $K=300$?

2. What is the training time for different training sizes (i.e., N)? What's the norm of the attention maps when you increase the training time? Should this be considered as an impact on the emergence of the locality?

3. If you conduct the experiments in the latent space, have you observed similar results? Related to this, if you conduct the results on a more complex dataset where long-range correlations between objects matter(e.g., COCO-2017), what's your observation?

4. For Figure 4, can you show the results with different thresholds of the colormaps?

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
3

### Summary
In this work, the authors identified that an inductive bias of DiT lies in the locality of attention which contributes to the generalizability of DiT. The local attention windows are proposed to be incorporated to DiT to improve the generalizability accordingly. Experimental results also demonstrated the enhanced performance from the incorporated local attention windows.

### Strengths
1. *Quality*: This work demonstrates good quality on identifying the inductive bias of DiT on generalizability and constructing the local attention map. The preliminary analysis and the model are of coherence and comprehensiveness.

2. *Significance*: Diffusion models have been attracting increasing attention in the recent years. Analysis the generalizability of the prominent diffusion models DiT via inductive biases provides an interesting perspective to improve diffusion models.

### Weaknesses
1. *Presentation*: A minor comment is on the grammar and spelling check of the paper, for example, in Section 1, “Their training involves approximates a distribution…” should be “Their training involves approximating a distribution…”.

2. *Clarity*: What does the Jacobian of a UNet or a DiT mean? Could the authors please articulate how it is computed as in [1] within the main content, for example, Section 2? Hence we can have a better understanding on why the Jacobian eigenvectors can reveal the memorization behavior of Simplified UNets, UNets and DiT. The current explanation lacks sufficient detail to understand the underlying mechanism. Specifically, how are the partial derivatives computed with respect to the input pixels, and what is the dimensionality of the resulting Jacobian matrix? It is also unclear how the eigendecomposition is performed on this high-dimensional matrix, and what the specific interpretation of the resulting eigenvectors and eigenvalues is in the context of image generation.

3. *Novelty*: Although this work is of significance, the analysis perspective and method is still similar to [1]. It would be better to highlight the novelty and contributions of this work compared with [1], especially the differences on the analysis method and techniques. The paper should clearly articulate how the analysis of DiT's attention maps differs from the harmonic analysis in [1], and what new insights are gained from this alternative approach. The connection between local attention and the observed inductive bias should also be more thoroughly explained. Theoretical analysis will be helpful to improve the novelty, as well as the quality.

### Questions
1. Could the experimental results also include the simplified UNet and UNets in improved diffusion models? Hence the comparison can be more comprehensive and promising.

2. It would also enhance the qualitative studies in the experimental results to show the improved generalizability of DiT with local attention windows. The impact of the local attention window size can also be presented.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies generalization of transfomer-based diffusion models (DiT). The authors first make a connection to prior work that discovered that UNet-based diffusion models generalise because of the inductive biases that can be expressed via geometry-adaptive harmonic bases and show that the same analysis is not able to explain the generalisation in DiTs. Authors instead propose that generalisation in DiTs emerges because of the "locality" of the self-attention layers. They first confirm this empirically, by looking into the attention masks at different layers and discover strong local patterns (i.e., pixels mainly attend to their neighbouring pixels). Then they also propose to use the local attention mask (by masking out all the pixels that are outside of the neighbourhood) and show that this can lead to better performance for smaller datasets (both in terms of the PSNR gap and FID).

I like the paper overall and enjoyed reading it. Hence I vote for acceptance. I am not (at all) familiar with the related literature on inductive biases in diffusion models, so my confidence is low (2/3).

### Strengths
- The problem studied (i.e., generalisation of diffusion models) is interesting and highly-relevant. I cannot comment on the novelty aspect since I'm not deeply familiar with this field
- I find the main "theoretical" analysis in the paper interesting, both how they show that the differences with the existing theory for UNets and also how they explain the generalisation of DiTs via the local patterns in the attention masks
- I find the experimental results sufficient for confirming their main hypothesis on the importance of local attention masks

### Weaknesses
 - The paper is not really self-contained. I feel like this could be improved with including the background section where main concepts used throughout the paper are explained. For example, the Jacobian of the denoising network is crucial for the parts of the analysis, however it is never properly introduced. Specifically, the paper delves into the spectral analysis of the Jacobian without defining it clearly. It's unclear whether the Jacobian is with respect to the input image, the network's parameters, or something else entirely. This lack of clarity makes it difficult to fully grasp the theoretical underpinnings of the work. Furthermore, the connection between the Jacobian's spectral properties and the generalization behavior of diffusion models is not explicitly established, leaving the reader to infer the significance of this analysis.


### Questions
- What exactly is the Jacobian you are talking about in Section 2.2? Is it the derivative of the denoising NN w.r.t. its parameters? If so, how do you deal with its dimensionality, since it has dimension of (HW) x M where HxW are the dimensions of the output/image and M is the number of model parameters, right? Also, it is not a diagonal matrix, so do you compute eigen or singular values?
- In line 308 you state you remove the autoencoder, but how do you then go from H x W to (HW) x d, where d is the token dimension?
- Out of curiosity, what is the purpose of black boxes over faces in Figure 1? You are not considering an inpainting task, or?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the generalization mechanisms of diffusion models, comparing the inductive biases of UNet-based and Transformer-based diffusion models (DiTs). The authors find that while geometry-adaptive harmonic bases drive generalization in UNets, DiTs rely on the locality of attention maps. This paper modifies attention window sizes to enhance DiT generalization, especially in settings with limited training data.

### Strengths
This paper considers the locality of attention maps as the key inductive bias that contributes to the generalization of DiTs, which is an interesting perspective. In this way, the authors control generalization of DiTs by local attention window.

### Weaknesses
1.	Findings in this paper need to be further verified. Although Fig. 6 shows that using local attentions in a DiT can improve its generalization (measured by PSNR gap) with limited training data conditions, using a pruned DiTs may also improve its generalization ability. It is a well-known generalization phenomenon that an appropriate ratio between model size/complexity and data quantity achieves a better performance. In this way, decreasing the model size/complexity may be the key reason for improving generalization ability with limited training data conditions, where local attentions is just one way for decreasing model size/complexity.

2.	The contribution is limited. The authors introduce local attention windows to improve the generalization of DiTs, which have been widely used in previous studies [cite1-3]. Furthermore, the authors do not provide a theoretical explanation for why local attention windows improve generalization in DiTs. Therefore, the contribution of this paper is limited.

3.	The experimental results are not convincing. The paper relies heavily on FID scores to evaluate the performance of DiTs. Expanding the evaluation to other relevant metrics, such as CLIP Score [cite4-6], could provide a more comprehensive assessment of the model's capabilities.

4.	The improvements shown in the paper focus on limited training data scenarios, but the impact of the proposed method on other datasets or high-resolution tasks is not thoroughly explored, e.g., MS COCO and PartiPrompts.
5.	I suggest the authors provide more visual comparisons to demonstrate the generalization improvement of DiTs.

### Questions
Please see the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
