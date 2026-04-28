# Text as Any-Modality for Zero-shot Classification by Consistent Prompt Tuning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
The integration of prompt tuning with multimodal learning has shown significant generalization abilities for various downstream tasks. Despite advancements, existing methods heavily depend on massive modality-specific labeled data (e.g., video, audio, and image), or are customized for a single modality. In this study, we present Text as Any-Modality by Consistent Prompt Tuning (TaAM-CPT), a scalable approach for constructing a general representation model toward unlimited modalities using solely text data. TaAM-CPT comprises modality prompt pools, text construction, and modality-aligned text encoders from pre-trained models, which allows for extending new modalities by adding prompt pools and modality-aligned text encoders. To harmonize the learning across different modalities, TaAM-CPT designs intra- and inter-modal learning objectives, which can capture category details within modalities while maintaining semantic consistency across different modalities. Benefiting from its scalable architecture and pre-trained models, TaAM-CPT can be seamlessly extended to accommodate unlimited modalities. Remarkably, without any modality-specific labeled data, TaAM-CPT achieves leading results on diverse datasets spanning various modalities, including video classification (Kinetic-400/600/700), image classification (MSCOCO, VOC2007, NUSWIDE, VOC2012, Objects365), and audio classification (ESC50, US8K). The code is available at https://anonymous.4open.science/r/TaAM-CPT-0EA6.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on representation in a multimodal setting, introducing a method to build class-specific prompts across three types of inputs: image, video, and audio. The training process is efficient, relying only on a prompt pool as the training parameter and using pretrained models like CLIP, CLAP, and LLM to eliminate the need for complex data collection. However, the experiences discussed in this paper are limited to relatively simple classification problems involving images, videos, and audio. This hinders my ability to fully understand the potential of these methods.

### Strengths
1. This paper focuses on representation in a multimodal setting, which is a interesting and important fields. This paper also utilize important tools of contrastive loss for inter-model learning and ranking loss for intra-model learning.
2. The training process is efficient, relying only on a prompt pool as the training parameter and using pretrained models like CLIP, CLAP, and LLM to eliminate the need for complex data collection.
3. The experiences include both objective metrics and visual figures to help understand the effectiveness of the new methods.

### Weaknesses
The main issue lies in the novelty and practical functionality for this fields:
1. The contrastive loss and ranking loss are not new; they have been applied to multimodal representation learning [1, 2] for some time.
2. The application of this paper is currently limited to relatively simple classification tasks, for which many existing tools perform well. I encourage the authors to include additional tasks, such as conditional image or audio generation using the novaly class.
3. The prompt pool is limited at the beginning, so what if the user wants to add a new concept? Although the pipeline can introduce new concepts, the issue is how quickly this process can be compared to the overall training of the method. I encourage the authors to provide more empirical results or theoretical analysis on the time complexity of adding new concepts in comparison to initial training time.

[1] Wang Z, Zhao Y, Huang H, et al. Connecting multi-modal contrastive representations[J]. Advances in Neural Information Processing Systems, 2023, 36: 22099-22114.

[2] Zheng L, Jing B, Li Z, et al. Heterogeneous contrastive learning for foundation models and beyond[C]//Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2024: 6666-6676.

### Questions
See the weaknesses.

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
The authors explore a generic representation model capable of scaling to an infinite number of modalities without the need for any modality-specific labelled data.TaAM-CPT simplifies the design by characterising any modal category as a randomly initialised vector, and exploits the command tracking capabilities of the LL.M. to allow easy access to textual training data of any category. TaAM-CPT ensures the flexibility to add any category from any modality without retraining the already learned category-specific cues. Additionally, the authors designed a one-way contrast loss, which uses modalities with stronger representational capabilities to guide the learning of those that are weaker.

### Strengths
- The authors present a simplistic approach to prompt building and describe the build process in detail.
- The authors propose a   uni-directional contrastive loss to facilitate intermodal training.
- TaAM-CPT effectively integrates the image/audio/video modalities and achieves competitive performance on classification tasks.

### Weaknesses
- Making prompts requires inserting **{Label}**, does this mean that different pools of prompts need to be designed for different datasets?
- LLM's hallucinations may affect the quality of prompt generation, does TaAM-CPT have a process for quality checking during prompt production?
- TaAM-CPT needs to adjust Inter-modal Learning based on validation performance, but I noticed that some of the dataset's validation set is being used for evaluation, is there an information leak?
- Based on the previous question, should TaAM-CPT be trained individually based on the validation performance of each dataset?
- Section 3.5 mentions that TaAM-CPT improves the inference speed of the model, whether the authors have experimented on objective metrics?
- The authors utilize LLM to generate prompts for auxiliary training. The method can be taken as a distillation from LLM. Whether the authors have compared the performance difference between TaAM-CPT and MLLM?
- In section 4.4, the author discusses the feasibility of TaAM-CPT for infinite modes and categories, but I still have concerns about this. When creating prompts, it is possible to combine 2-3 labels in various ways. In extreme cases, exhaustively permuting a vast number of labels can be very time-consuming and may negatively impact the quality of the model.
- With more modalities and labels, I concern that the burden of training intra- and inter-modalities will increase.

### Questions
See details in Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents TaAM-CPT, a prompt tuning approach for classifying a sample from any modality to a set of predefined categories.
It builds on pre-trained text-modality aligning models such as ViCLIP (text-video), CLIP (text-image) or CLAP (text-audio). 
Keeping these models frozen, TaAM-CPT tunes a set of prompt pools (one prompt pool per modality) to align to text representations directly in the representation space of the pre-trained models. The prompts are trained using a combination of inter-modal uni-directional contrastive loss and intra-modal ranking loss.
The paper reports performance on video classification, image classification and audio classification, but claims to be extendable to any number of other modalities.

### Strengths
Simple approach:
Compared to TaI-DPT (Guo et al., 2023) and follow-up work, the method presented in this paper is simpler as it does not involve complex multi-grained prompts.
TaAM-CPT only uses a single prompt per category per modality which simplifies the approach.

Code availability:
The authors of TaAM-CPT released the code for their implementation which is very valuable for reproducibility.

### Weaknesses
Significance of the quantitative improvement:
The inter-modal unidirectional contrastive learning is the main contribution claimed by this paper. It is ablated in Table 7 and Table 10. But without a statistical analysis of the results it is hard to evaluate the significance of the improvement.
L959: "when all modalities are trained together, the performance of each modality can be further improved." This does not seem to be the case though. 
Comparing to independently training each modality, training all modalities jointly does not seem significantly better (53.8=>53.7, 65.8=>65.2, 92.5=>92.7)

Poor presentation and clarity:
The problem tackled in this paper is not properly introduced. It is not clearly explained what prompt-tuning is and why it is interesting.
There are many important parts of the method that are not properly explained and remain unclear. See "Questions" section for details.

### Questions
Extension to more modalities and labels:
L201: "When a new modality emerges, a new modality-specific prompt pool will be created, avoiding affecting the already learned other prompt pools. When a new label arises, a new class-specific prompt will be also added to each prompt pool, avoiding affecting the existing class-specific prompts either."
The paper claims that the approach is easily extendable to new modalities and new labels, but does not actually experiment with it.
Could the authors further detail what would be the process for adding another modality or a new label? Would it be possible to keep the old prompts frozen and only train the new prompts? Would the performance on the new prompts be as good as if all prompts had been trained from scratch?
How will a new modality encoder with a different output dimension (e.g. 768) be introduced?

Choice of Video as the "Weak" modality:
L213: "Furthermore, we find CLIP (Cherti et al., 2023) and CLAP (Wu et al., 2023b) have superior representation abilities for image and audio, compared to ViCLIP (Wang et al., 2024b) for video, specifically reflected in the zero-shot classification performance."
On which criteria do the authors claim the video modality as "weak"? A poor zero-shot performance does not necessarily mean that the modality is "weak" or difficult to process, it can also mean that the benchmark itself is hard.

Number of labels per query:
In the main paper, the stated number of labels per query is 2 for video and 3 for image and audio:
L187: "{Labels} indicates modality-specific labels, with a maximum of 2 for video modality, 3 for image and audio modalities." 
How were these specific values determined? Why not 3 for video and 4 for image? What would be the impact of only using a single label per query? From Figure 6 it seems like some label combinations lead to captions that do not make much sense.
Moreover, there seem to be a discrepancy in the stated number of labels per query: In the appendix, the stated number of labels per query is 2 for video and audio and 1 to 4 for image:
L913: "For video and audio datasets, we set the number of sampled categories to 2. For image, the number of sampled categories is set to 1, 2, 3, or 4"
Can the authors clarify?

Modality-specific labels:
What if there are common labels across modalities, can the authors confirm that they are not merged together? For example, "crying" could be a video, audio or image label. In that case is it present 3 times in the N labels?

Number of categories:
What is the value of the number of categories (v+a+w=N) used in this paper? How many for video, image and audio? Is it a concatenation of all the labels from benchmark datasets? 

Unclear ablation study for Prompt Design:
The section "D Ablation Study - Prompt Design" is unclear. Can the authors clarify what is being discussed exactly?
It seems to be about the initial prompts dimension and their projection into a lower-dimensional space but the motivation is not explained. 
What does FC stand for? Fully-connected layer? Please remind the reader about the setting adopted by TaAM-CPT in that regard, is it 512-d without transformation?

Minor presentation notes:
In figure 1 and 2, N is used for representing the number of modalities. 
But in the text, N represents the number of categories:
L226: N is the total number of labels across all modalities. 

Minor typos:
L040: "classificatiot"
L145: "a massive of labeled data"
L410: "intergrated"
L464: "110MB parameters"

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces TaAM-CPT, a scalable framework for general representation learning across unlimited modalities using only text data. Unlike existing methods that rely on large amounts of modality-specific labeled data or focus on a single modality, TaAM-CPT leverages prompt tuning, modality-aligned text encoders, and intra- and inter-modal objectives to harmonize learning across different modalities. With its flexible architecture, TaAM-CPT achieves top performance in zero-shot and classification tasks across 13 diverse datasets, spanning video, image, and audio classification, without the need for labeled data specific to each modality.

### Strengths
1. TaAM-CPT supports multiple modalities without needing labeled data, advancing universal representation learning.
2. The model achieves state-of-the-art results across diverse tasks—zero-shot video, image, and audio classification—demonstrating its robust generalization capabilities across various modalities and datasets, a key advantage for multimodal applications.
3. The organization of this paper is logical.

### Weaknesses
1. One of my main concerns is that the proposed TaAM-CPT seems to be a combination of existing techniques, _e.g._, learnable prompts (soft prompts), Inter-/Intra-modal Learning strategies. The authors are expected to provide more discussions to better showcase their novelty and contributions. 
2. In Intra-modal Learning, the authors claim that the proposed method _'simplifies the design of the prompt and reduces the computational cost to half'_ (lines 242-243). However, the experimental section fails to adequately demonstrate the efficiency of the proposed approach. It would be beneficial for the authors to include quantitative metrics such as training cost or parameters to substantiate the robustness and flexibility of their approach.
3. The clarity and simplicity of the paper's writing could be enhanced. Certain sentences were perceived as verbose and challenging to comprehend. Notably, lines 51-53 and Eq. 6 would benefit from refinement to improve their accessibility and ease of understanding.

### Questions
Please refer to the weaknesses, I will raise my score if all concerns are well-addressed.

### Soundness
3

### Presentation
3

### Contribution
3
