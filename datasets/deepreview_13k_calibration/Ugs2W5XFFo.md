# Information Theoretic Text-to-Image Alignment

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Diffusion models for \gls{T2I} conditional generation have seen tremendous success recently. Despite their success, accurately capturing user intentions with these models still requires a laborious trial and error process. This challenge is commonly identified as a model alignment problem, an issue that has attracted considerable attention by the research community. 
Instead of relying on fine-grained linguistic analyses of prompts, human annotation, or auxiliary vision-language models to steer image generation, in this work we present a novel method that relies on an information-theoretic alignment measure. In a nutshell, our method uses self-supervised fine-tuning and relies on point-wise mutual information between prompts and images to define a synthetic training set to induce model alignment.
Our comparative analysis shows that our method is on-par or superior to the state-of-the-art, yet requires nothing but a pre-trained denoising network to estimate \acrshort{MI} and a lightweight fine-tuning strategy. %to substantially improve \acrshort{T2I} model alignment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a self-supervised approach using Mutual Information (MI) for model alignment, requiring only the pre-trained T2I model and a simple fine-tuning process, outperforming current state-of-the-art methods.

### Strengths
1. The proposed method does not require additional image datasets for training.
2. The idea is relatively novel.

### Weaknesses
1. Comparison methods, "Attend and Excite (A&E) (Chefer et al., 2023b), Structured Diffusion Guidance(SDG) (Feng et al., 2023b) and Semantic-aware Classifier-Free Guidance (SCG) (Shen et al., 2024)"  mentioned in line 329, is implemented on SD1.4, but the proposed work is implemented on SD 2.1, which is powerful than SD1.4 and may introducing evaluation bias.
2. The experiments, the train set, and the test set are split from the same dataset, but this may exist some correlations, what's the results on out-of-distribution prompts?
3. Although mutual information provides a theoretical explanation, it essentially uses classifier guidance as a loss for fine-tuning. Given that this approach is so simple, has there been any similar attempt in previous work?

### Questions
Referring Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Mutual Information (MI) to guide model alignment, which uses self-supervised fine-tuning manner. It relies on a point-wise MI estimation between prompts and images to create a synthetic fine-tuning set for improving model alignment.

### Strengths
- The idea of introducing  self-supervised fine-tuning manner is interesting.

- Mutual Information in the pipeline is simple and effective.

- It seems is a plug-and-play module, which is useful for most T2I models.

### Weaknesses
 - More detailed ablations are needed. The authors employ MI as the metric to select fine-tuning samples, which eliminates the extra usage of other models. However, what if we use SOTA VQA models as the metric? Intuitively, SOTA VQA models are more precise than the MI metric.

- An inherent drawback of MI is that it can measure how much help comes from the prompt but cannot guide in the right direction. For example, in cases of color misalignment, how should we deal with this issue?

### Questions
Please see the waeakness.

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
4

### Summary
The proposed MI-TUNE introduces a self-supervised fine-tuning approach to enhance text-to-image alignment in diffusion models. At its core, the method leverages Mutual Information (MI) between text prompts and their corresponding generated images to improve model alignment, eliminating the need for human annotation. The method generates multiple images per prompt, selects the top-K aligned ones based on MI estimation, and uses these for fine-tuning.

### Strengths
1. The main problem "Is mutual information meaningful for alignment?" is compelling and necessary, showing the potential of MI as a new direction for text-image alignment
2. The paper is well-organized and easy to follow.
3. The proposed fine-tuning approach is intersting and seems to have predictive power.

### Weaknesses
1. MI scores are missing from comparison tables and images despite being central to the method.
2. Figure 1 only demonstrates MI effectiveness on simple category prompts (color, texture, shape), lacking validation on more challenging cases like spatial relationships or complex compositions

### Questions
1. How were the 700 prompts selected for the MI quantitative analysis?

### Soundness
2

### Presentation
2

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
This paper proposes MI-TUNE, a finetuning strategy for T2I models. This strategy introduces mutual information calculation into the T2I model tuning process to guide model alignment. In brief, the tuning method uses self-supervised fine-tuning and relies on a point-wise MI estimation between prompts and images to create a synthetic fine-tuning set for improving model alignment. This paper claims to be the first to introduce mutual-information calculation into T2I model training, leading to effective guidance for model alignment. The MI index is also measured and compared with well-established metrics and user study to prove the rationality. The experiments on MI are performed and evaluated on T2I-CompBench and user studies.

### Strengths
1.	This paper claims to be the first to introduce the mutual information (MI) for T2I model training alignment. And the MI is proven to be effective on model alignment and strongly agrees with well-established metrics.
2.	MI-TUNE results on several measurements (BLIP-VQA, HPS and Human) on image features reveals state-of-the-art performance.
3.	The paper also provides the proof for MI index to have a valid point-wise manner. Introducing mutual information into T2I model tuning is interesting, it may benefit the generative model training.
4.	The paper is easy to follow with algorithm and pseudo code provided.

### Weaknesses
1.	Note that the paper mainly focuses on SD-based (SD 2.1, SDXL) models. These models are mostly the same styles, e.g., similar network structures and traditional denoising training strategies. Is there any possibility that the MI tuning incorporated with flow-based models like DiT-based models (SD3, Pixart series or so). And it is interesting to see if the proposed MI tuning behaves different with different types of models. Specifically, the reliance on DDPM-style denoising for MI estimation is a potential limitation. The method's applicability to rectified flow models, which do not have the same iterative denoising process, is unclear. This raises concerns about the generalizability of the proposed approach. The paper should address how the MI estimation would be adapted to models that do not rely on a score function derived from a diffusion process.
2.	The evaluations on MI mainly focus on only simple semantic concepts like color, shape and texture. Is MI-tuning sensitive to object numbers or so? The evaluation lacks a comprehensive analysis of the model's ability to handle more complex scenarios, such as varying object counts or intricate spatial relationships. The T2I-CompBench, while useful, may not fully capture the nuances of real-world prompts. It is crucial to assess how the MI-tuning behaves with more complex prompts that involve multiple objects and their interactions. The paper should include experiments that test the model's sensitivity to object numbers and complex spatial arrangements.
3.	The paper fixes the denoising steps to 50 when inferencing an image, are there any differences in performance of MI-tuning when using different steps except 50? The choice of 50 denoising steps is not sufficiently justified. The impact of varying the number of denoising steps on the MI estimation and the overall performance of the model needs to be explored. It is important to understand whether the MI-tuning is robust to changes in the denoising process or if it is highly sensitive to this parameter. The paper should include an ablation study on the number of denoising steps to demonstrate the robustness of the method.
4.	In quantitative analysis of Sect. 3.1, the paper mentions that the point-wise MI ranks images and select 1st, 25th and 50th as the representative images. Why the three images are representative? This needs more detailed explanations. Also, the reason of the selection needs quantitative analysis. The selection of the 1st, 25th, and 50th ranked images lacks a clear rationale. The paper should provide a more detailed analysis of the distribution of MI scores and justify why these specific ranks are representative of the overall performance. A quantitative analysis of the score distribution is needed to support the choice of these representative images.
5.	Some of the ablations mentioned in previous sections are hard to locate in the following contents, the writing can be improved in this part.

### Questions
Please see the weakness part. How about the performance of MI Tuning on DiT based models or Flow-based model, since the flow-based model reveals stronger generation capability comparing to traditional DDPM training. If MI tuning strategy fails to have good performance on flow-based training, the impact may be weaker.

### Soundness
3

### Presentation
3

### Contribution
3
