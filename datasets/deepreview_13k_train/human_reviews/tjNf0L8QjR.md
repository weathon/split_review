# An Image is Worth More Than 16x16 Patches: Exploring Transformers on Individual Pixels

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
This work does not introduce a new method. Instead, we present an interesting finding that questions the necessity of the inductive bias -- \emph{locality} in modern computer vision architectures. Concretely, we find that vanilla Transformers can operate by directly treating each individual pixel as a token and achieve highly performant results. This is substantially different from the popular design in Vision Transformer, which maintains the inductive bias from ConvNets towards local neighborhoods (\eg by treating each 16$\times$16 patch as a token). We mainly showcase the effectiveness of pixels-as-tokens across three well-studied tasks in computer vision: supervised learning for object classification, self-supervised learning via masked autoencoding, and image generation with diffusion models. Although directly operating on individual pixels is less computationally practical, we believe the community must be aware of this surprising piece of knowledge when devising the next generation of neural architectures for computer vision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The study investigates whether the inductive bias of locality is necessary for modern computer vision models. It explores the effectiveness of using vanilla Transformers to directly treat each individual pixel as a token for various computer vision tasks. The findings show that pixel-based Transformers can perform competitively in supervised and self-supervised learning, as well as image generation, challenging the belief that locality is essential. The research examines how removing locality impacts architectures like Vision Transformers (ViT) and compares results with patch-based models. Although computationally intensive, the study demonstrates that locality-free Transformers can still learn effective visual representations, which may inform future neural network designs.

### Strengths
1. This paper is well-written.
2. The topic is of great interest to the computer vision community.
3. The experiments are extensive.

### Weaknesses
In general, I agree to recommend the acceptance of this paper. However, I think it is a borderline paper, due to the following reasons.
1. The finding is not surprising: removing the locality of visual backbones, and the models still work, at least to some extent. I think this conclusion can be expected by most of the researchers within the community (btw, I appreciate the efforts of authors to make these observations clear).
2. As also recognized by the authors, the practicality of this conclusion is questionable, given its limited computation efficiency.
3. The down-sampling algorithm (e.g., bicubic resampling) has already introduced some inductive biases of locality. It can be seen as a convolutional layer with fixed kernels. This effect may be particularly notable when the resolution is relatively small (e.g., 28x28 on ImageNet).

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a study of locality in ViT, through decreasing the patch size down to 1x1. The paper shows that smaller patch will always get better performance and 1x1, which does not encode locality in each patch, gets the best performance. The work contributes to understandings of whether locality / patchification is necessary. The authors conduct experiments on supervised learning, self-supervised learning, and image generation. The results validate the hypotheses and statements.

### Strengths
+ The paper is well-written and has great clarity on motivation and experiment designs.
+ The authors extensively test the model on various tasks and benchmarks.
+ It's interesting to see that the patchification design to be explicitly re-checked.

### Weaknesses
- The work focuses on using smaller side of ViTs. I wonder if scaling up, does 1x1 patch still help in performance? Could it be that for ViT/L or ViT/H the patchification does not matter that much among 1x1, 2x2, or 4x4? It would be beneficial to see experiments on larger ViT models to confirm if the observed trend holds, as the relative importance of patch size might diminish with increased model capacity. Specifically, the impact of 1x1 patches on ViT-L or ViT-H should be investigated to ensure the findings generalize beyond smaller models.

- This paper proposes a finding, but it seems no good solution is available for now. The growth of #tokens is quadratic, 512 x 512 will give you 262144, and 1048576 for 1024 x1024. Further more, video will even give more tokens. Flash Attention and other efficient version will still have a tough time taking these many tokens as inputs. The practical implications of the quadratic increase in token count with smaller patch sizes need more discussion. While the paper acknowledges this, it would be beneficial to explore potential mitigation strategies or alternative architectures that can handle such a large number of tokens more efficiently. The computational cost associated with 1x1 patches needs to be addressed more thoroughly.

- The authors discuss a series of related works. Another important and emerging line of work that uses grouping operation is missing though. Images as set of points is strongly relevant work that breaks the image into 1x1 pixel representation and uses fixed centers clustering / pooling for representation learning. The slot attention-based backbone, although do not use 1x1 patches, made the grouping operator (instead of key-axis attention in ViT) work on ImageNet scale and should also be discussed. Do the authors think grouping can be a more handy way for forming "flexible and irregular-shaped patches" automatically, and enjoy the sweet spot of lower computation while having smaller patch sizes?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work poses an intriguing question regarding locality-free modeling of images using Transformers. The new modeling perspective centered on the locality-free concept presents an interesting direction for applying Transformers in computer vision, given their success in machine translation tasks. The study conducts extensive experiments across various scale tasks, revealing consistent and general observations. These findings lead to broader conclusions regarding the effectiveness of locality-free modeling under certain conditions.

### Strengths
1. The questions raised are interesting. The locality-free concept is essential for bridging the gap between computer vision and natural language processing when language models are adopted to solve visual recognition tasks.
2. The observations are compelling and support the general conclusions on the potentials of locality-free modeling under certain conditions. The study performs extensive experiments across various scales, revealing consistent and widespread findings.
3. The experiments are well designed to demonstrate the potential of locality-free modeling for images.

### Weaknesses
The conditions underlying the observations and conclusions require greater emphasis and detail. While "locality-free" suggests that input patches or tokens can be fragmented, it is still essential to preserve the relationships among adjacent input vectors or scalars. Developing a dictionary or tokenizer for image pixels is challenging, which hinders the advancement of locality-free models. The conclusions presented summarize valuable insights, but many of these observations, especially pixel-based modeling, probably have been considered during the design of Vision Transformers (ViTs). The limitations in their efficient training contribute to their performance issues. It is also quite challenging to represent image pixels semantically in a linguistic manner. If the authors could propose an effective training scheme or a pixel dictionary design for locality-free approaches, this work would become even more insightful and beneficial.

### Questions
The concept of locality-free in this work is conditional and needs to be clearly differentiated from random pixel-level training. All discussions regarding locality-free should specify these conditions; otherwise, the statements may be too bold. While the paper identifies a problem, it does not explore potential solutions or the feasibility of addressing them. The authors should address these questions during the rebuttal to improve the rating score.

### Soundness
4

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
5

### Summary
The paper studies the role of locality biases in Vision Transformers (ViTs) by examining whether treating individual pixels as tokens (1x1 patches)—rather than conventional 16×16 patches—is sufficient for computer vision tasks (image classification or generation). 

This pixel-based approach yields 2 benefits:
1. Reduced Vocabulary Size: By treating each pixel as an independent token, the "vocabulary" size (i.e., unique values the model must handle) becomes more manageable.
2. Model Agnosticism to Locality Bias: The pixel-based Transformer performs competitively across various tasks, such as image classification, self-supervised learning, and image generation, suggesting that locality may not be as essential for vision tasks for ViT as previously thought.

The authors evaluate this approach on tasks like classification (CIFAR-100, ImageNet), self-supervised learning, and image generation through diffusion models. They find that the pixel-based Transformer achieves results comparable to patch-based ViTs, though with higher computational costs due to increased sequence lengths.

While the paper is well-written, it falls short in addressing the practical implications of using 1x1 patches beyond merely demonstrating feasibility. (i.e. other than knowing that we can use 1x1 patches, what is the value of using 1x1 in practice?). I am hesitant to recommend this paper for NeurIPS.

### Strengths
* Clear and Detailed Writing: The paper is well-organized, with clear explanations of the rationale behind pixel-based tokenization, the potential benefits, and the authors are upfront about the trade-offs involved. I only suggest a few writing modifications below.

* Thorough Experimental Evaluation: The paper includes a comprehensive set of experiments across multiple tasks—classification, self-supervised learning, and image generation, although adding more baselines will make the evaluation more complete and convincing.

### Weaknesses
 * The empirical results in Table 3 for Case Study #1 show only marginal performance improvements when using 1×1 tokens on datasets like ImageNet and Oxford-102-Flower. The evaluation would be more convincing if results were presented for all four size variants (ViT-T/S/B/L) and included a 16×16 baseline for comparison. Specifically, the reported gains of 0.1-0.4% on ImageNet are not substantial enough to justify the increased computational cost of using 1x1 tokens without a more comprehensive analysis across different model sizes. The lack of a direct comparison with a 16x16 patch baseline also makes it difficult to assess the true impact of the 1x1 token approach.
* In Case Study #2, there is a lack of detailed information on the setup and evaluation. It’s unclear what new value or insights this setup offers beyond those in Case Study #1. This section appears to have been completed in a rush. For example, the specific training parameters, the architecture of the self-supervised model, and the evaluation metrics are not clearly defined, making it difficult to reproduce or interpret the results. The absence of a clear motivation for this case study further weakens its contribution to the paper.
* In Table 5, there is no clear advantage in using 1×1 tokens over 2×2 tokens. Results might benefit from additional baselines, such as 4×4 or 8×8 tokens. The current results do not provide a strong argument for the superiority of 1x1 tokens, and the lack of comparison with other patch sizes leaves the reader wondering if the observed performance is simply a result of the specific experimental setup. A more thorough exploration of different patch sizes would be necessary to draw more robust conclusions.
* In Figure 3, qualitative examples for the 1×1 approach are shown without comparable examples from baseline methods. Including baseline results would provide a more effective comparison. The lack of a direct visual comparison makes it difficult to assess the quality of the generated images and to determine if the 1x1 approach offers any tangible benefits over existing methods. The visual comparison should include images generated using the same prompts and random seeds to ensure a fair comparison.
* While the authors are upfront about the inefficiency of using 1x1 patches, I am unsure about the practical value of using 1x1 patches (though vocab size benefit was mentioned). The overall takeaway for me is: “We can use 1x1 rather than 2x2 and we still get good performance” but the answer why this finding matters is not clearly explained. The paper does not convincingly demonstrate a practical use case where the benefits of 1x1 patches outweigh their computational cost, thus limiting the impact of this finding.

### Questions
Rather than questions, I have a few suggestions to improve writing.

L411 Intrestingly, -> Interestingly

L201: in range [0,255],  the vocab size is 256^3 not 255^3. Please revise all the writing to ensure the correct information.

L44-46: The authors should clarify **why** translation equivariance still exists in ViT. Translation equivariance in neural networks, particularly in convolutional neural networks (CNNs), is the property where shifting the input (e.g., an image) results in a corresponding shift in the output features. This means the network recognizes that the content has moved spatially without altering the actual information content, which is useful for tasks like object detection and localization.

In transformers, translation equivariance is not naturally present. Transformers process input sequences as tokens, where each token attends to all other tokens through self-attention. transformers don’t inherently “understand” spatial shifts in the same way that CNNs do because each token’s positional information is encoded separately, often through positional embeddings.

All my concerns are written in Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
