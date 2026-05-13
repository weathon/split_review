# Learning Visual Prompts for Guiding the Attention of Vision Transformers

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Visual prompting infuses visual information into the input image to adapt models toward specific predictions and tasks. Recently, manually crafted markers such as red circles are shown to guide the model to attend to a target region on the image. However, these markers only work on models trained with data containing those markers. Moreover, finding these prompts requires guesswork or prior knowledge of the domain on which the model is trained. This work circumvents manual design constraints by proposing to learn the visual prompts for guiding the attention of vision transformers. The learned visual prompt, added to any input image would redirect the attention of the pre-trained vision transformer to its spatial location on the image. Specifically, the prompt is learned in a self-supervised manner without requiring annotations and without fine-tuning the vision transformer. Our experiments demonstrate the effectiveness of the proposed optimization-based visual prompting strategy across various pre-trained vision encoders.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses solely on learning prompts through self-supervised learning, which can be added to any input image to redirect the attention of the pre-trained ViT to its location. It achieves this by minimizing the KL divergence between the attention of the CLS token and the target distribution.

### Strengths
- The paper is easy to follow and understand.
- This method can be applied to different pre-trained ViT, regardless of their pre-training supervision methods, and does not require annotation or fine-tuning of the ViT.

### Weaknesses
 - The paper lacks essential details and descriptions, which may lead readers unfamiliar with the preceding work to struggle with understanding what is being tested or implemented. For example, the methodology for testing on the CUB dataset is not clearly outlined, and the significance of "K2N" on line 478, which stands for keypoint to name, is not explained.
- Building on the concept that a "red circle" can direct CLIP's attention to a specific area, as demonstrated in prior work by Shtedritski et al. (2023), the paper's technical contribution is limited, and its effectiveness is also open to debate:
    1. It primarily applies the phenomenon of the "red circle" to other pre-trained Vision Transformers through learnable prompts. However, the experiments involving language-supervised methods lack baselines for the "red circle" and cropping techniques. Moreover, the performance comparison with the "red circle" from the referenced paper [https://arxiv.org/pdf/2304.06712] appears to show a decline rather than an improvement.
    2. In the DINOv2 experiments, the paper shows examples from MMVP for illustration but does not provide quantitative metrics.
    3. The paper combines the phenomenon of the "red circle" with visual prompt learning, which is incremental. Moreover, its effectiveness has not been well demonstrated.
- The application scenarios are limited: the phenomenon of the "red circle" is quite interesting and helps us better understand CLIP. This paper focuses on applying this phenomenon to more pre-trained Vision Transformers. However, the method of using circles necessitates manually annotating areas of interest on images, making it impractical for large datasets. Consequently, effectively applying this phenomenon to downstream tasks is challenging. If possible, it should be stated how the proposed method can be applied to downstream tasks.
- There is a lack of suitable baselines and quantitative comparisons. In the absence of an appropriate baseline, it is challenging to demonstrate that the proposed method improves upon previous approaches. Since the paper’s contribution is to extend this phenomenon to other ViTs, it is essential to conduct controlled ablation experiments on the MMVP-VLM dataset to show that the proposed method is more effective than the simple "red circle" approach.
- Minor: The presentation of the figures needs improvement; for instance, in Figure 7, the text for location 2 3 is obscured.

### Questions
Please refer to the Weaknesses section for further details.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a self-supervised learning approach for generating visual prompts that guide the attention mechanism of Vision Transformers (ViT). The method utilizes a neural network prior and optimizes the prompt pixels through backpropagation to enhance attention at corresponding positions in the visual encoder. The approach is evaluated on the CUB and RefCOCO datasets, showing improved performance compared to baseline methods.

### Strengths
1. The approach is model-agnostic and does not require fine-tuning, making it versatile across different models.  
2. The method demonstrates strong generalization capabilities across various models and datasets.  
3. The presentation is clear and easy to understand.

### Weaknesses
1. The paper lacks sufficient justification for the advantages of the approach compared to directly collecting and fine-tuning with annotated visual prompt data, particularly in terms of performance and efficiency benefits.  
2. There are some typos: some citation formats need correction; Table 2 shows inconsistent decimal places across the results; the ordering in Figures 4 and 5 appears to be incorrect.

### Questions
1. When applying multiple visual prompts simultaneously, do the attention maps exhibit similar patterns of change as observed with single prompts?  
2. How does the performance compare quantitatively to using a simple red circular frame as a visual prompt?  
3. Could you consider using attention gain as a training objective to enhance the model's ability to follow visual prompts with LoRA (a efficient training method)? This could provide an interesting baseline comparison.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a self-supervised optimization approach for designing visual prompts to guide the attention of vision transformers (ViTs) toward specific regions in an image. Instead of manually creating visual markers, the method involves learning visual prompts specific to each vision encoder, enhancing its focus without altering its architecture. Experiments on CLIP, DINOv2, and other ViTs show that these prompts effectively influence attention distribution, improving model performance on tasks like keypoint naming and object recognition.

### Strengths
The approach appears to be adaptable, allowing self-supervised learning of visual prompts for various vision encoders without needing labeled data. This flexibility is particularly valuable for adapting vision transformers across tasks and models without costly retraining or fine-tuning.

### Weaknesses
There are a few concerns for the algorithmic design: 1. Although the method is intended as a self-supervised approach, its performance is primarily evaluated using annotated datasets like CUB (for keypoint detection) and RefCOCO (for object localization), where specific body parts or objects are pre-labeled. This reliance contrasts with the self-supervised nature of the learning process, potentially limiting practical utility. For instance, if access to labeled datasets is restricted or unavailable in a particular domain, the evaluation and validation of the learned prompts could become challenging, affecting the applicability of the approach in real-world, unlabeled environments. 2. The evaluation is performed on datasets with relatively controlled settings (e.g., images with birds or single annotated objects). In more complex, natural scenes where multiple objects and overlapping contexts are present, the effectiveness of learned prompts could degrade. Without sufficient evaluation on diverse, unlabeled datasets, there’s a risk that the method may not generalize effectively to scenarios with complex visual contexts. This gap highlights a limitation in validating the approach’s robustness and universality outside curated datasets. 3. The learned prompts are customized for individual transformer-based architectures (e.g., CLIP, DINOv2), which may not translate effectively to other model types or even to transformers with slight architectural variations. This specificity can limit cross-model generalization, requiring separate training of prompts for each new architecture. For broader applicability, it would be beneficial to explore if and how prompts could be designed with more universal features or optimized independently of model architecture.

### Questions
In light of these weaknesses, I would suggest the authors address the following: 1. How does the method perform on real-world datasets with complex and diverse scenes? The paper’s focus on curated datasets like CUB and RefCOCO raises questions about robustness on uncurated, real-world datasets with more complex scenes. Such environments may demand attention guidance that adapts beyond controlled settings, so further validation in these contexts would be beneficial. 2. Could the approach be generalized to non-transformer vision models? As the study is limited to transformer-based models like CLIP and DINOv2, testing with other architectures (e.g., CNNs) could clarify whether the learned visual prompts are uniquely suited to transformers or if they have broader applicability across different model types. 3. How can we ensure the accuracy of attention guidance? Since the model’s "attention" relies on pre-trained representations, this approach may lack robustness across different test set distributions (e.g., open-set scenarios). The work’s effectiveness hinges on accurate attention to guide model behavior, but if the attention is inconsistent, it could potentially mislead the model, impacting performance.

### Soundness
2

### Presentation
3

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
This paper explored the possibility of guiding the attention mechanism to focus more on a region of interest by introducing visual cues to the input while avoiding intervention on the internals of the ViT. However, I have some concerns as follows:

### Strengths
1. The structure of this paper is complete.
2. The content of this paper is easy to follow.

### Weaknesses
1. The Introduction is confusing. There is no logical relationship between the three paragraphs of the introduction, and it is unclear what the author is trying to do within the three paragraphs. How do existing methods do it? What problems do they have? What is the difference between the proposed method and the above methods? What is different and innovative about the proposed method?
2. In related work, what is the relationship between the three parts of the introduction? What problems do existing methods have that should be further elaborated?
3. The proposed method is too simple. It feels like a patchwork of existing methods. Compared with existing methods, I don’t know where the core innovation of the proposed method is.
4. The experimental results are unreliable. First, there is a lack of comparison with the most advanced methods. Second, the analysis is insufficient for ablation studies. It is unclear why each of the proposed components can bring performance improvements.

### Questions
See the comments below.

### Soundness
2

### Presentation
2

### Contribution
2
