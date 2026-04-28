# Align-VL: Can Being Modest Help in the Alignment of Vision-Language Models?

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Multimodal alignment aims to learn a shared latent space between different modal inputs to establish connections across modalities.
A prime example is Visual Language Models (VLMs), such as CLIP, which benefit from extensive image-text pre-training and excel in image recognition tasks. 
These models are emblematic of successful multimodal alignment.
Subsequent work has successfully aligned multimodal data on limited datasets using feature mixing enhancement methods.
However, these models encounter significant challenges:
{The presence of {ambiguous samples (either partially matched or completely unmatched)} in datasets with weakly associated, low-quality image-text pairs causes models to become overconfident (in training) and confused (in inference), ultimately reducing performance}. Current contrastive learning methods, which rely on single positive pairs, exacerbate this issue by encouraging overconfidence when the model encounters such ambiguous samples.
To overcome these challenges, we developed Align-VL, a multimodal alignment enhancement method that operates on the latent spaces of pre-trained unimodal encoders. This approach adjusts the matching degree of the data and moderates model overconfidence, promoting more appropriate and effective alignments.
Align-VL incorporates {Random Perturbation} and {Embedding Smoothing} strategies to enhance input feature robustness and reduce model overconfidence, improving the model's ability to manage uncertainty and generalize to new data. 
In our experiments, Align-VL outperformed existing state-of-the-art (SoTA) methods in image-text retrieval tasks, demonstrating its superior effectiveness.
Align-VL also offers significant reductions in training time and data requirements compared to methods like CLIP, using substantially fewer GPU days and image-text pairs. 
Code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Align-VL, a novel approach to enhance multimodal alignment in Vision-Language Models (VLMs) by addressing the issues of overconfidence and ambiguous training data pairs. Current VLMs like CLIP encounter performance degradation when trained on weakly associated, low-quality image-text pairs, often becoming overconfident and confused by ambiguous samples. Align-VL introduces two main techniques to tackle these challenges: Random Perturbation and Embedding Smoothing. Random Perturbation introduces noise to both visual and textual embeddings during training to enhance generalization, while Embedding Smoothing reduces model overconfidence by ensuring smoother and less peaked prediction distributions. The paper demonstrates that Align-VL outperforms state-of-the-art (SoTA) methods in image-text retrieval tasks, while significantly reducing data requirements and training time. The proposed method aims to be more computationally efficient by leveraging pre-trained unimodal encoders and improving the quality of multimodal alignment.

### Strengths
- The paper proposes a creative enhancement for vision-language alignment through the use of Random Perturbation and Embedding Smoothing applied to the latent space of pre-trained unimodal encoders. While these techniques were introduced from existing methods in other fields, their combination and application in this context is effective in moderating overconfidence, adding an extra layer of robustness to multimodal systems.
- The paper is clearly written, with well-structured sections that logically present the motivation, proposed methods, and experimental results. The equations and theoretical analysis are well-defined and helpful for understanding the concepts. However, some figures are confusing and could be better explained.

### Weaknesses
 - A key limitation is the lack of evaluation on larger-scale datasets comparable to those used by models like CLIP (e.g., 400 million data pairs). The paper acknowledges this but does not include any further experiments or discussions on large-scale datasets to substantiate the scalability of Align-VL. There are publicly available large-scale text-image datasets, such as the LAION dataset, which could have been used to provide additional insights. Including a discussion on potential challenges or a small-scale simulated analysis could strengthen this point.
- The model evaluation is somewhat limited in scope. First, the authors only used the Flickr dataset for evaluation, which is insufficient to assess the model's general performance across a broader range of data. It would be better to include additional datasets, such as MSCOCO, to provide a more comprehensive evaluation. Second, the evaluation was restricted to the image and text retrieval task. Evaluating the model's performance on other tasks, such as zero-shot classification, would provide a more complete understanding of its capabilities.

### Questions
- The method has not been tested on extremely large datasets. Could the authors elaborate on the potential challenges of scaling Align-VL to datasets with large scale datasets? Also,
- Random Perturbation appears similar to other types of regularization techniques, such as dropout or mixup. How does Align-VL compare to these standard methods? Would substituting Random Perturbation with another noise-based regularization method yield similar results?
- I would like to hear the authors' opinion on whether the proposed method would be effective for training a multimodal model from scratch rather than leveraging pre-trained unimodal encoders.
- Figures are somewhat confusing.
  - In Figure 2, It is confusing what the grey square box, "Negative and "Positive mean. Also, what do blurred embeddings and small grey rectangles mean?
  - In Figure 3, it looks like random perturbation is used only for text embedding and the ES is used only for image embedding. Also, those embeddings from A_x and A_y are fed into contrastive loss without ES. Please clarify it.
- How does the performance differ by the batch size of N because the smoothed target distribution in the Embedding Smoothing is defined with N? It would be great to see an ablation study by N.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is based on CLIP and Fusemix and introduces two techniques: Random Perturbation and Embedding Smoothing. The former adds random noise to the output of the unimodal encoder to enhance feature robustness. The latter transforms CLIP's hard labels into soft labels through a target smoothing operation. Experiments on Flickr 30K demonstrate the effectiveness of both techniques. Additionally, the article discusses the issues of partial matches and unmatched pairs in image-text pair data through statistical experiments.

### Strengths
1. The methods proposed in this paper are easy to implement, and the experiments can be conducted on a single 3090 GPU, making this paper easy to follow.
2. The experimental results on Flickr30K presented in the paper are promising, showing a significant improvement compared to CLIP trained on the same data (see Table 2).

### Weaknesses
1. The experiments presented in the paper are not sufficient and would benefit from the inclusion of additional evaluation datasets and tasks. For instance, incorporating zero-shot image classification results from ImageNet, CUB-200, Oxford Pets, Flowers, and SUN397 could enhance the robustness of the findings.
2. The novelty is limited. Embedding Smoothing closely resembles label smoothing in contrastive learning, while Random Permutation is similar to data augmentation in the feature space.
3. Some figures are not very clear. For example, Fig. 2 should better emphasize the differences between CLIP, FuseMix, and AlignVL.

### Questions
1. Are the proposed methods generally effective across more benchmarks, such as the zero-shot image classification datasets mentioned above, as well as additional image-text retrieval datasets?
2. Would you please provide more discussion on the differences between embedding smoothing and label smoothing?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors identify issues with current VLMs, such as overconfidence and confusion due to ambiguous samples in datasets with weakly associated, low-quality image-text pairs. To address these challenges, the authors propose Align-VL, a method that enhances multimodal alignment by adjusting the matching degree of data and moderating model overconfidence. Align-VL incorporates two strategies: random perturbation and  embedding smoothing. Align-VL leverages pre-trained unimodal encoders and requires substantially fewer computational resources and data compared to methods like CLIP.  Experiments show that Align-VL outperforms state-of-the-art methods in image-text retrieval tasks and significantly reduces training time and data requirements.

### Strengths
1.The descriptions are clear and it is easy to follow.

2. Improvements are achieved on well-known datasets, showing the effectiveness of the proposed method.

### Weaknesses
1. The proposed method introduces new parameters, i.e. sigma and alpha. It is needed to select proper parameters.

2. It seems that how performances are effected with varying sigma and alpha.

### Questions
See Weaknesses.

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
4

### Summary
The paper proposes Align-VL, a vision-language alignment method designed to enhance robustness and manage overconfidence in multimodal models. It incorporates two strategies—Random Perturbation and Embedding Smoothing—to handle uncertainties in image-text datasets, especially when data is ambiguously paired. Align-VL operates on the latent spaces of pre-trained unimodal encoders, aiming to enhance generalization and reduce computational costs.

### Strengths
- This paper highlights the reliance of current contrastive learning methods on single positive pairs, a valuable observation.
- The paper is well-structured and clearly written, making it easy to follow.

### Weaknesses
 - In lines 080 to 082, the claim lacks convincing support. The ALIGN model [1] has shown through training on billions of noisy image-text pairs that dataset scale can compensate for noise and yield state-of-the-art representations, which contradicts the author’s claim. Additional references or empirical studies would strengthen this argument.
- The proposed methods, Random Perturbation and Embedding Smoothing are existing methods and are often used as training engineering techniques, which limits their technical novelty.
- The experiment in Table 1 only evaluates a single dataset and compares one baseline, which provides limited evidence.
- The data quality evaluation uses pre-trained CLIP, which may not be ideal given CLIP's own biases, making this evaluation approach potentially limited for assessing data quality.

### Questions
For specific questions, please refer to the points in the "Weaknesses" section.

### Soundness
2

### Presentation
3

### Contribution
2
