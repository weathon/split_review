# EZ-CLIP: EFFICIENT ZERO-SHOT VIDEO ACTION RECOGNITION

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Recent advancements in large-scale pre-training of visual-language models on paired image-text data have demonstrated impressive generalization capabilities for zero-shot tasks. Building on this success, efforts have been made to adapt these image-based visual-language models, such as CLIP, for videos extending their zero-shot capabilities to the video domain. While these adaptations have shown promising results, they come at a significant computational cost and struggle with effectively modeling the crucial temporal aspects inherent to the video domain.

In this study, we present EZ-CLIP, a simple and efficient adaptation of CLIP that addresses these challenges. EZ-CLIP leverages temporal visual prompting for seamless temporal adaptation, requiring no fundamental alterations to the core CLIP architecture while preserving its remarkable generalization abilities. Moreover, we introduce a novel learning objective that guides the temporal visual prompts to focus on capturing motion, thereby enhancing its learning capabilities from video data.

We conducted extensive experiments on five different benchmark datasets, thoroughly evaluating EZ-CLIP for zero-shot learning and base-to-novel video action recognition, and also demonstrating its potential for few-shot generalization. Impressively, with a mere 5.2 million learnable parameters (as opposed to the 71.1 million in the prior best model), EZ-CLIP can be efficiently trained on a single GPU, outperforming existing approaches in several evaluations.

For the latest updates and access to the code, please check the supplementary materials. We will regularly update the code at this link.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the issues of adapting image-based visual-language models to the video domain and proposes solutions. It introduces a prompt-based temporal modeling method to reduce computational complexity when modeling temporal relationships. Additionally, it designs a motion loss to capture the intrinsic relationships between frames, which existing methods often overlook.

### Strengths
+ The paper proposes a prompt-based approach for establishing temporal relationships between different frames in image models.

+ Existing contrastive losses neglect the intrinsic properties of videos. The motion loss is designed to enable the model to learn motion information between frames.

+ The method is simple but has been validated on multiple settings and datasets, achieving state-of-the-art (SOTA) performance.

+ The proposed method outperforms other methods in terms of GFLOPs, throughput, tunable parameters, and total parameters.

### Weaknesses
- The contribution of the paper is limited due to similarities with the Visual Prompt Multi-Modal Tracking [A] approach. Both methods utilize prompts and transformer outputs to generate new prompts interactively. The difference lies in this paper's method of averaging patches from each frame and adding them to the prompt, incorporating information from the current frame. From this perspective, the innovation appears somewhat lacking.

- The paper lacks sufficient ablation experiments, as it only conducts them in the "Base to novel generalization" setting.

- Based on the ablation experiments in Table 4 and Table 5, combined with the results in Table 2, it can be observed that even without the proposed TVP and Motion loss, adding only the adapter achieves better results compared to existing methods. Hence, there are concerns regarding the fairness of the comparison with SOTA methods.

### Questions
- The ablation experiments of LLM were only conducted in the "Base to novel generalization" setting. Were LLM used in other settings? If so, what were the results when LLM was not used?
- The paper mentions the use of text adapter and spatial adapter, citing different papers. However, it is not clear where they are incorporated in Figure 2. Could you clarify where they are added?
- In Table 6, the proposed method has a Tunable params value of only 5.2M. However, the cited Aim's spatial adapter has 3.7M tunable parameters, and LoRA has a minimum of 1.8M. Could you provide the specific breakdown of the tunable parameters for each component?
- For the prompt in this paper, it is added to each layer of the transformer. Has there been an experiment where the prompt is only added to the first layer?
- Motion loss: In Equation (5), the central difference C is computed using the embeddings of the previous and next frames. However, in action recognition tasks, adjacent frames are often very similar. Is this loss calculation effective? Could you explain in detail the role of motion loss?

====================After rebuttal=================
My main concerns about the technical contribution have not been addressed (see my detailed comments). I keep my initial rating.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to adapt CLIP model for video tasks specifically for action recognition in various generalization bench-marking settings. Specifically, two main contributions are proposed to improve CLIP performance on videos. Firstly, temporal visual prompt (TVP) learning is introduced which are learned at the vision encoder. TVP are layer wise prompts that are uniquely added to mean of each frame features and then self-attention mechanism allows the model to learn temporal contexts. Secondly, the authors propose a motion loss, that encourages maximum diversity in terms of variance and pair-wise difference among video frames. This encourages the model to learn distinct embeddings for each frame based on its motion information. 

The performance of model is shown across various generalization benchmark settings which it shows improvements over the prior methods with less compute and trainable parameters. Ablations are conducted to show the effect of each component, which provides a broader perspective on the novelty.

### Strengths
1) The idea of keeping spatial model frozen and using specific modules and loss functions to improve temporal modeling is encouraging. This allows the community to easily analyze the contributions by the proposed component only. This also results in very light weight adaptation which allows the model to be trained on very less compute resources.

2) The proposed techniques including temporal prompt tuning and motion loss are fairly motivated. Their individual importance has been further validated with proper ablation studies.

3) The proposed framework shows reasonable improvements over the prior methods. Further analysis like tsne plots as well as per-class results shows more accurate effect due to the proposed techniques.

4) Paper is easy to read and well written.

### Weaknesses
1) The proposed overall framework seems to be heavily relied on additional training modules and tricks like LLM based prompt ensembling and spatial-language adaptors. However, there is very little detail given on these modules. For example, what kind of adaptors are used, at which place they are incorporated in the model, how many prompts are being used from LLM, illustrations of LLM prompts? It will be better to provide a high level figure diagram which also shows the usage of these additional components.

2) It will be good to see effectiveness of the proposed approach on (i) larger CLIP models like ViT Large or Huge (ii) and on any other CLIP variant (e.g EVA-CLIP) which would confirm the generalization of the proposed approach towards other model scales and recent VL models other than CLIP.

3) I am not completely sure but I think there might be something wrong in the ssv2 results for base-to-novel generalization setting. EZ-CLIP is achieving around 54% and 20.6% accuracy for 16 shots samples. But the same EZ-CLIP is performing relatively poor in few-shot setting where it also uses 16 shot samples. Can the authors revisit the experiments and confirm that they are using the correct split for base-to-novel setting for ssv2? I am afraid it can be the case that complete ssv2 training data is used instead of 16 shots. 
Otherwise the few-shot results should have similar scale results for the proposed approach.

### Questions
Please refer to the weaknesses section for my queries.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces EZ-CLIP, an efficient zero-shot video recognition model, which incorporates temporal visual prompting into the pretrained vision-language model CLIP to capture video motions. During model training, the newly added temporal module is the only component that is learned, making it an efficient approach. Additionally, a motion loss is introduced to enhance diversity and distinctiveness among frames, thus improving model learning. The paper's results on multiple datasets demonstrate its strong performance.

### Strengths
The paper effectively communicates its motivation and methodology. It highlights the key idea of utilizing the image-based visual-language model CLIP and seamlessly integrating temporal visual prompting for video action recognition.

The model's simplicity and clarity make it easily understandable. Moreover, the paper provides compelling evidence of its superiority over alternative methods through results on various benchmarks.

### Weaknesses
1. The authors might overstate the claim that "temporal adaptation techniques require a lot of parameters with fine-tuning of the whole model which is not desirable for preserving generalization capability." Both AIM [1] and ST-Adapter [2] employ a similar learning approach by freezing CLIP parameters and only tuning newly added adapter layers to learn temporal relations within video frames. It's crucial to maintain accuracy in comparative statements.

[1] AIM: Adapting Image Models for Efficient Video Action Recognition, https://arxiv.org/abs/2302.03024

[2] St-adapter: Parameter-efficient image-to-video transfer learning, NeurIPS, 2022

2. The used baseline models are two adapters AIM and LoRA-FA (the last paragraph of Section 3.2). The paper's baseline model utilizes the spatial adapter only, which makes it less comparable to methods like AIM that incorporate both spatial and temporal adapters. Including both spatial and temporal adapters in the baseline would provide a more accurate basis for comparing the proposed temporal visual prompting.

3. Table 5 demonstrates the substantial positive impact of the LLM-generated action class descriptions on action recognition. It suggests that the improved performance of EZ-CLIP may primarily stem from the use of these descriptions rather than the introduction of temporal visual prompting. For example, EZ-CLIP wo LLM-description only achieves 77.3% HM result on UCF-101, while ViFi CLIP which does not use LLM (I checked their paper, if I did not miss something) obtains the higher result of 78.3%. As such, the better performance of EZ-CLIP may mainly come from the utilization of LLM.


4. The proposed EZ-CLIP employs 8 frames for efficiency, while other methods use 32 frames (a 4x difference). As such, the comparison in Table 6 may not be appropriate.

5. It's worth noting that K-600 is an extension of K-400 and shares video categories. This overlap should be taken into account when doing zero-shot learning.

### Questions
Please see my comments in Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
