# SeLoRA: Self-Expanding Low-Rank Adaptation of Latent Diffusion Model for Medical Image Synthesis

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
The persistent challenge of medical image synthesis posed by the scarcity of annotated data and the need to synthesize `missing modalities' for multi-modal analysis, underscored the imperative development of effective synthesis methods. Recently, the combination of Low-Rank Adaptation (LoRA) with latent diffusion models (LDMs) has emerged as a viable approach for efficiently adapting pre-trained large language models, in the medical field. However, the direct application of LoRA assumes uniform ranking across all linear layers, overlooking the significance of different weight matrices, and leading to sub-optimal outcomes. Prior works on \emph{LoRA} prioritize the reduction of trainable parameters, and there exists an opportunity to further tailor this adaptation process to the intricate demands of medical image synthesis. In response, we present \emph{SeLoRA}, a Self-Expanding Low-Rank Adaptation Module, that dynamically expands its ranking across layers during training, strategically placing additional ranks on crucial layers, to allow the model to elevate synthesis quality where it matters most. The proposed method not only enables LDMs to fine-tune on medical data efficiently but also empowers the model to achieve improved image quality with minimal ranking. The code of our \emph{SeLoRA} method is publicly available on \url{https://anonymous.4open.science/r/SeLoRA-980D}.
\keywords{Text-to-Image Synthesis  \and Low-Rank Adaptation \and Parameter-efficient.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces SeLoRA (Self-Expanding Low-Rank Adaptation), an extension of the LoRA (Low-Rank Adaptation) technique, designed for the fine-tuning of large diffusion models specifically in medical image synthesis. The core idea is to dynamically expand the rank of low-rank matrices during training, based on a criterion derived from Fisher information. This adaptation is applied selectively across different layers, allowing for a more effective distribution of ranks that aligns with each layer's significance in the model, particularly within the denoising U-Net of the Stable Diffusion framework.

### Strengths
1. The paper is well-organized and easy to follow.

2. The idea of adaptive computation rank selection is interesting and highly relevant for using pre-trained models for downstream tasks in a memory efficient fashion

### Weaknesses
 - While the paper mainly focusses on making a more efficient LoRA design as claimed by authors, there is no Analysis of Training Efficiency in the paper.

- Lack of detailed explanation of the procedure of selecting hyper-parameters needed.

- In figure 7, why are the other methods not generating similar xray images? As per my understanding, they should at-least make a similar image like figure 8. 

- The proposed method is just compared to methods with rank pruning methods (dylora and adalora), could you mention why there is no comparing with adaptive rank selection papers? as they seem to be a similar approach to your paper.

### Questions
- How is the proposed method compared to other baselines in terms of max training GPU memory, training speed, and
training time costs? An analysis of these criteria would strengthen the paper.

- The paper mentions thresholds (λ and t) for triggering rank expansion. How sensitive is the method to these hyper-parameters?

- In figure 7, why are the other methods not generating similar xray images? As per my understanding, they should at-least make a similar image like figure 8. 

- The proposed method is just compared to methods with rank pruning methods (dylora and adalora), could you mention why there is no comparing with adaptive rank selection papers? as they seem to be a similar approach to your paper.

### Soundness
2

### Presentation
2

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
This paper proposes a new parameter-efficient fine-tuning method SeLoRA (Self-Expanding Low-Rank Adaptation) for adapting Stable Diffusion to generate chest x-ray images. The main contribution of the paper lies in dynamically expanding the rank of LoRA during the training process, allowing it to adapt the rank according to the importance of different layers and thereby improving the quality of the synthesized images. The novelty of this approach is in using Fisher Information to guide the rank expansion, avoiding the limitations of the traditional LoRA method, which uses a "uniform rank," especially when dealing with models (like Stable Diffusion) that have diverse weight matrix shapes. The paper demonstrates the effectiveness of SeLoRA on two chest x-ray datasets and provides detailed comparative experiments with other LoRA variants.

### Strengths
1. 
The papers proposes SeLoRA, a dynamic rank-expanding method using Fisher Information to guide rank expansion during fine-tuning large models with LoRA. This is novel and more applicable to models with diverse weight matrix shapes.
2.
Experimental results demonstrate the effectiveness of the proposed method.
3. 
The paper is well-organized.

### Weaknesses
1.
The contribution is vague. As a paper focusing on adaptive parameter efficient fine-tuning methods, the paper utilizes LoRA to adapt Stable Diffusion for Chest X-ray synthesis, limiting its technical contribution. For a paper dedicated to adapting foundation model like Stable Diffusion for Chest X-ray (medical image) synthesis, the exploration is also limited and does not compare with previous work (e.g. Chambon et al., 2022a;b). Through visual comparison with image displays in Chambon et al., 2022a;b, the proposed method seems at a disadvantage.
2.
Experiments are conducted on relatively small datasets. Large image-report paired Chest X-ray datasets exist (e.g. MIMIC-CXR). Is this because of the heavy burden of large model like Stable Diffusion, or may be also related to the proposed method? Can the authors provide training time comparisons between SeLoRA and the compared methods? Also, as the test set of IU X-RAY and Montgomery County CXR dataset has only contains 100~200 images, the validation of the effectiveness of the method is weak.
3.
Evaluation and explanation are insufficient. Using a CLIP model trained purely on natural images and a maximum text token length of 76 to compute CLIP-score may not faithfully reflect how good the text-image alignment is for Chest x-ray images.
The training/validation/testing split is strange, could the author explain why the test set only contain 4% of the data? Are Table 1 values computed with valid data or test data? This is unclear. The paper also lacks in-depth discussion of the distribution of final rank (Figure 4,5,6) and why other LoRA methods fail on Montgomery county CXR data (Figure7). How accurate can the model generate an image given the disease or abnormal findings in the text prompt? This may be revealed using pretrained Chest X-ray classification models or manually inspect a small subset of generated results.

Other non-important issues:
4.
the paper title is about "medical image syntheis”; but it only focuses on chest x-ray image.
5.
The formula derivation in section3.3 is unclear.
6.
The Stable Diffusion model is trained to generate a resolution of 512x512, using a resolution of 224x224 may limit the performance.

### Questions
Please answer the questions mentioned in the above 'weakness' section.

### Soundness
2

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
The paper present SeLoRA, a Self-Expanding Low-Rank Adaptation module, that dynamically expands its ranking across layers during training. The proposed method increases the rank from 1 gradually. FI-Ratio and parameter \lambda were used to determine when to expanding the rank.  The experiment is performed with stable diffusion and X-ray dataset and synthesis the X-ray image with text prompt.

### Strengths
The paper introduces a parameter-efficient method to e fine-tune stable diffusion models for generating X-ray images based on text (radiology) prompts. And the proposed method can progressive expansion in the rank of LoRA. FI-Ratio is used to guiding SeLoRA to expand its rank. The rank of different layers was given. The experiment shows the result is promisingly.

### Weaknesses
1. Computational overhead. While SeLoRA reduces the number of trainable parameters, its dynamic rank expansion mechanism introduces additional computational complexity. Computing Fisher information increases the overhead, which may become significant for larger datasets or more complex models. The overhead of computing the Fisher information, specifically, involves calculating gradients and performing element-wise squaring, which, while seemingly simple, can add non-negligible computational cost, especially when performed frequently across multiple layers and during iterative training processes. The frequency of rank updates, determined by the parameter \lambda, also impacts this overhead, as more frequent updates lead to more frequent Fisher information calculations. 
2. Limited dataset evaluation. Experiments were limited to two 2D X-ray datasets, with no evaluation of SeLoRA’s performance on other modalities, such as MRI or CT scans. Further validation on additional modalities would help confirm the generalizability of the method. The lack of evaluation on diverse medical imaging modalities limits the assessment of the method's robustness and applicability in real-world clinical settings. Different modalities have distinct characteristics and noise profiles, and performance on one modality does not guarantee similar performance on others. 
3. Visual result is limited. The visual result is not satisfactory, such as in Figure 8, the contrast and details are not good. The generated images lack the fine details and contrast necessary for accurate clinical interpretation, which is a critical requirement for medical imaging applications. The low contrast and lack of detail could be due to limitations in the training data, the model architecture, or the training process itself. The visual quality needs to be improved to ensure the generated images are clinically relevant.

### Questions
1. Computational complexity analysis A comparison of training time, memory usage and FLOPs between SeLoRA, LoRA, and other variants is needed to quantify the computational trade-offs introduced by dynamic rank expansion.
2. Evaluation on a wider range of datasets Evaluating SeLoRA on larger datasets, such as MIMIC-CXR (containing approximately 377,000 images), would provide more insights into its scalability. Future work could also validate SeLoRA on MRI, CT, or ultrasound datasets, as testing on diverse datasets would better demonstrate its robustness and versatility.
3. Incorporating related work. The idea of dynamically adjusting the rank of the LoRA matrix in SeLoRA is conceptually similar to the recently proposed ALoRA (NAACL 2024). However, the two methods differ in implementation: ALoRA utilizes pruning and redistribution strategies, while SeLoRA relies on Fisher information as the adjustment criterion. Insights from ALoRA could provide valuable inspiration for future improvements of SeLoRA.
4. Evaluation with medical doctor may help verify the experiment results.
Other questions
1. Unconventional split of the IU X-Ray dataset. The 80:16:4 split results in a relatively small test set, which could compromise the robustness of the evaluation. A more conventional split (e.g., 80:10:10) might provide more reliable insights.
2. Small sample size in the Montgomery County CXR dataset. With only 138 samples, the Montgomery County dataset is too small for deep learning applications, which may impact the stability and generalizability of the model’s results

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Self-Expanding Low-Rank Adaptation (SeLoRA), akin to LoRA’s structure but distinguished by the dynamic growth of ranks guided by Fisher information during training.   This enables SeLoRA to flexibly adapt to the inherent characteristics of each layer, guaranteeing enhanced medical image synthesis quality while minimizing challenges related to rank adjustments.

### Strengths
* Originality: good originality, combining self-expanding and LoRA to make LoRA self-adapt to the different needs of layers.

* Quality: simple but effective method. Performance validated in the scope of medical image synthesis.

* Clarity: clear figures and method presentation.

* Significance: Data scarcity is very common in the medical AI field, and a strong LoRA variant is important to the community. IF the proposed method is effective and generalizable in the general scenes, it could be significant in efficient learning.

### Weaknesses
 * The paper proves the proposed method is significantly outstanding in the medical image synthesis scene (IU X-RAY dataset and CXR dataset). Would it work well in other tasks, like perceptual tasks or other synthesis tasks?

* Time cost is an important metric for the self-expand algorithm. The paper lacks a discussion of the efficiency of the algorithm and the experimental comparison with other LoRA methods.

### Questions
Included in the Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3
