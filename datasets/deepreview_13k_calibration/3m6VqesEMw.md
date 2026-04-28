# T$^3$-S2S: Training-free Triplet Tuning for Sketch to Scene Generation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
Scene generation is crucial to many computer graphics applications. Recent advances in generative AI have streamlined sketch-to-image workflows, easing the workload for artists and designers in creating scene concept art. However, these methods often struggle with complex scenes with multiple detailed objects, sometimes missing small or uncommon instances.
In this paper, we propose a Training-free Triplet Tuning for Sketch-to-Scene (T$^3$-S2S) generation after reviewing the entire cross-attention mechanism. This scheme revitalizes the existing ControlNet model, enabling effective handling of multi-instance generations, involving prompt balance, characteristics prominence, and dense tuning. 
Specifically, this approach enhances keyword representation via the prompt balance module, reducing the risk of missing critical instances. It also includes a characteristics prominence module that highlights TopK indices in each channel, ensuring essential features are better represented based on token sketches. Additionally, it employs dense tuning to refine contour details in the attention map, compensating for instance-related regions.
Experiments validate that our triplet tuning approach substantially improves the performance of existing sketch-to-image models. It consistently generates detailed, multi-instance 2D images, closely adhering to the input prompts and enhancing visual quality in complex multi-instance scenes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a Training-free Triplet Tuning (T³-S2S) method for sketch-to-scene generation, aiming to enhance the quality of generated scenes from sketches without additional training. The authors identify challenges in existing diffusion models related to imbalanced prompt energy and value homogeneity in the cross-attention mechanism, which lead to missing or coupled instances in complex scenes. To address these issues, they introduce two strategies: Prompt Balance and Characteristics Prominence. Additionally, they incorporate Dense Tuning from Dense Diffusion to refine attention maps. The proposed method is evaluated qualitatively on game scene generation tasks, demonstrating improvements in generating detailed, multi-instance scenes that align with input sketches and prompts.

### Strengths
1. The proposed Prompt Balance and Characteristics Prominence strategies contribute to enhancing the quality of generated scenes, particularly in handling complex scenes with multiple instances.
2. The method is relatively simple and does not require additional training, making it efficient and practical.

### Weaknesses
1. The proposed Prompt Balance and Characteristics Prominence strategies appear to be incremental improvements on existing techniques such as TopK methods. Dense Tuning is adapted from Dense Diffusion. Therefore, the paper may lean more towards engineering optimization rather than presenting significant novel techniques.
2. The experimental comparisons use models based on different versions of Stable Diffusion, with the proposed method and T2I Adapter using SDXL (a more advanced model), while Dense Diffusion is based on SD v1.5. Since SDXL offers higher generation quality than SD1.5, this results in an unfair comparison. Considering that this work draws inspiration from Dense Diffusion, it would be more appropriate to either adapt Dense Diffusion to SDXL or apply the proposed method to SD1.5 to ensure a fair evaluation.
3. The experiments focus primarily on game scenes, with limited variety in the types of scenes presented. Some examples are repeated in the paper, and the lack of diverse examples may not fully demonstrate the method's generalizability to other contexts. 
4. The paper focuses heavily on qualitative analysis and lacks quantitative experiments. 
5. Line 360 and 361: citations of SDXL and ControlNet are incorrect.

### Questions
1. I wonder whether the proposed method is effective for other types of scenes. Exploring and presenting results on different scene categories would be beneficial.
2. I suggest to incorporate user studies to enhance the robustness of the experimental validation.
3. The appendix seems to be directly attached after the references. It might be more appropriate to format the appendix according to the conference guidelines, ensuring it is properly integrated or submitted as a supplementary document as required.

### Soundness
3

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
5

### Summary
This article primarily focuses on the task of sketch-to-scene generation. Specifically, for complex scenes with multiple detailed objects, previous methods sometimes miss small or uncommon instances. Addressing this issue, the article proposes a training-free triplet adjustment method for sketch-to-scene generation. This method can be directly applied to existing SDXL and ControlNet models, enabling them to effectively tackle the multi-instance generation problem, including prompt balancing, feature highlighting, and dense adjustment. The proposal is made after reviewing the entire cross-attention mechanism. This solution revitalizes the existing ControlNet model, allowing it to effectively handle multi-instance generation, involving prompt balancing, feature highlighting, and dense adjustment. Experiments demonstrate that this triplet adjustment method enhances the performance of existing sketch-to-image models, enabling the generation of detailed, multi-instance 2D images that closely follow input prompts and enhance visual quality in complex multi-instance scenes.

### Strengths
1. This article addresses a very meaningful area, utilizing the approach of scene generation through sketches.

2. The method requires no training and can be seamlessly integrated into existing controllable generation models, thereby enhancing the models' generative performance.

### Weaknesses
1. The experimental content of this article is somewhat lacking in depth. From the presented experimental results, it only includes the generation of isometric view of game scene using colored sketch lines as control inputs. This raises the question of whether the method proposed in this article has universal applicability to scene sketch generation tasks. The experiments are limited to a very specific domain (game scene generation) and a specific style (isometric view), which does not sufficiently demonstrate the method's robustness across diverse scene types and viewpoints. Furthermore, the use of colored lines, while helpful for distinguishing instances, does not reflect the typical input for sketch-to-scene generation, which is usually black and white. This limits the practical applicability of the method in real-world scenarios where users typically provide hand-drawn sketches.

2. According to the description in this article, this training-free method at the feature level should be universally applicable to various controllable generation models. The method proposed in this article is based on ControlNet, but the article does not sufficiently discuss whether this approach would still be effective when integrated into other controllable generation models. The paper claims that the proposed triplet adjustment method is universally applicable to different controllable generation models, yet it only provides experimental results for ControlNet. The lack of experiments on other architectures, such as T2I-Adapter, makes it difficult to assess the generalizability of the method. The paper should provide more evidence to support its claim of universal applicability.

### Questions
1. Since this method can enhance the performance of existing controllable generation models without the need for training, is it possible to include experimental analyses based on more diverse existing models, such as the T2I-Adapter (https://arxiv.org/abs/2302.08453)   that the article compares?
If additional experiments could be added to demonstrate this, it would better showcase the universal applicability of the method proposed in the article, significantly enhancing its contribution.

2. Can the method proposed in this article be applied to a wider range of scenarios? From the experimental results presented in the article, it seems that simply altering the prompt should be sufficient to produce a more diverse array of scene images. I hope to see more experimental outcomes. Is it possible to incorporate a wider variety of input types (for example, black and white hand-drawn sketches)? Can the output be expanded to include a richer variety of scene images (for example, real-world images), not just limited to the isometric view of game scenes?
Particularly, the experimental results in Figure 6 of the article suggest that the method's control over the style of generated images should stem solely from the specific input prompt "Isometric view of game scene." Therefore, if the article could showcase more use cases across a variety of application scenarios, it would greatly increase the value of the method proposed in the article.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper identifies a phenomenon in sketch-to-scene generation where certain instance are not effectively represented in complex, multi-instance scenes. The authors attribute this issue to the imbalance of prompt energy and the homogeneity of value matrices. To address these challenges, the paper proposes a method that incorporates prompt balance, characteristic prominence, and dense tuning for sketch-to-image generation in complex scenes.

### Strengths
1. The paper provides a thorough analysis of text embeddings and the value matrices in cross-attention, revealing the issues of prompt energy imbalance and value matrix homogeneity.

2. The proposed method seemly  addresses the challenges associated with sketch-to-scene generation involving multiple subjects.

### Weaknesses
My primary concern lies with the clarity of the writing and the evaluation methodology:

1. The writing lacks clarity and the notation system is somewhat confusing.
2. Although the method does not require training, the optimization during inference may increase time demands, yet the paper does not report specific inference times.
3. The results are solely qualitative, lacking quantitative comparisons. The effectiveness of the proposed modules is not validated with measurable metrics, raising concerns about potential cherry-picking in qualitative assessments. While it may be challenging to establish reasonable quantitative benchmarks for this task, there even is no mention of conducting user studies to support the findings.

### Questions
see weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an approach, termed Triplet Tuning for Sketch-to-Scene (T3-S2S), a training-free method designed to enhance T2I generation capabilities in multi-instance scenarios, effectively mitigating challenges such as instance omission. The T3-S2S method introduces a prompt balance mechanism to automatically balance the energy of each instance within text embeddings and incorporates a characteristics prominence mechanism that strengthens cross-attention by highlighting Top-K indices within each channel, ensuring that essential features are more robustly represented based on token sketches. Methodologically, T3-S2S demonstrates certain innovations compared to previous approaches, and the results presented by the authors indicate that this method indeed yields notable improvements. Therefore, at this stage, I would rate this paper as [weak accept]. However, I believe the current experimental results are still insufficient; please see the question section for details. I look forward to the authors' responses.

### Strengths
Methodologically, T3-S2S demonstrates certain innovations compared to previous approaches, and the results presented by the authors indicate that this method indeed yields notable improvements.

### Weaknesses
I believe the current experimental results are still insufficient. First, the paper does not include comparisons with state-of-the-art (SOTA) methods on popular benchmarks. Additionally, it lacks quantitative comparison results, which are essential for a comprehensive evaluation of the method’s effectiveness.

### Questions
(1) The prompt balance mechanism could also be applied to text-to-image models. I recommend testing the effectiveness of the prompt balance mechanism on some multi-instance text-to-image benchmarks. Specifically, you could compare it with training-free optimization algorithms designed for multi-instance T2I scenarios, such as AAE [1] and StructureDiff [2].

(2) When performing the characteristics prominence mechanism, the paper states that the optimal setting for K is 2. When the number of instances exceeds K, how does your characteristics prominence mechanism ensure that each instance is effectively enhanced? More specifically, how does it handle multiple instances that belong to the same category but have different fine-grained attributes? For example, when dealing with five cats—one red, one blue, one green, one black, and one white.

(3) I have some questions regarding specific details. When performing characteristics prominence, should the operation be applied on cross_attention(I, T) or on I + cross_attention(I, T), where I is the image feature and T is the text embedding?

(4) I believe further experiments on widely used multi-instance generation benchmarks are necessary to better demonstrate the effectiveness of your method.

[1] Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models.

[2] TRAINING-FREE STRUCTURED DIFFUSION GUIDANCE FOR COMPOSITIONAL TEXT-TO-IMAGE SYNTHESIS.

### Soundness
2

### Presentation
2

### Contribution
2
