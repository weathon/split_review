# Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5, 6

## Abstract
The advancement of Large Vision-Language Models (LVLMs) has increasingly highlighted the critical issue of their tendency to hallucinate non-existing objects in the images. 
To address this issue, previous works focused on using specially curated datasets or powerful LLMs (e.g., GPT-3.5) to rectify the outputs of LVLMs. However, these approaches require either expensive training/fine-tuning or API access to advanced LLMs to correct the model's output post-generation.
In this paper, we tackle this challenge by introducing a framework called \textbf{M}itigating hallucin\textbf{A}tion via classifie\textbf{R}-Free gu\textbf{I}da\textbf{N}c\textbf{E} ($\method$), which is both \emph{training-free} and \emph{API-free}, and can effectively and efficiently reduce object hallucinations during the generation process.  
Specifically, $\method$ enriches the visual context of LVLMs by integrating existing open-source vision models, and employs classifier-free guidance to incorporate the additional object grounding features to improve the precision of LVLMs' generations. 
Through comprehensive evaluations across $6$ popular LVLMs with diverse evaluation metrics, we demonstrate the effectiveness of $\method$, which even outperforms existing fine-tuning-based methods. 
Remarkably, it not only reduces hallucinations but also improves the detailedness of LVLMs' generations, as assessed by GPT-4V.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MARINE, a novel framework to reduce hallucinations in Large Vision-Language Models (LVLMs) without requiring additional training or API access. MARINE provides image-grounded guidance by leveraging open-source vision models (like object detectors) to extract object-level information. This approach enhances the accuracy of LVLM-generated content by integrating multiple vision models for reliable object-level guidance. Extensive evaluations on five LVLMs show that MARINE effectively reduces hallucinations and outperforms fine-tuning methods, maintaining the detail and precision of LVLM outputs.

### Strengths
1. MARINE novelly utilizes the strengths of image-grounded visual models (like object detectors) to provide detailed information about the input image, effectively helping to reduce hallucinations in LVLMs. 

2. Extensive evaluations across multiple datasets show that MARINE consistently outperforms baseline methods in mitigating hallucinations, while preserving strong performance across various tasks, including image captioning and visual question answering.

### Weaknesses
1. Would it be possible to revise the input text prompt to "enforce" LVLMs to only describe the significant objects to mitigate hallucination? Would it achieve similar results?  It is recommended to compare to a baseline using carefully engineered prompts aimed at reducing hallucination. This would allow for a more concrete evaluation of MARINE versus prompt engineering approaches.

An example of a prompt is "Describe the visible contents of this image in as much detail as possible without adding any information not clearly visible. Only mention objects, colors, shapes, and textures that can be directly observed in the image, avoiding assumptions about materials, functions, or contexts. If there are any uncertainties about what an object is, describe its visual characteristics (e.g., 'a circular object with a smooth surface') without inferring its purpose or identity. Avoid creative or hypothetical descriptions, and focus on observable details only." Other prompts for a Vision-Language Model (VLM) that minimizes hallucination, focuses on clear, fact-based, and constraint-driven descriptions, are also reasonable.

2. Since the hallucination mitigation is achieved by resembling scores coming from the Guidance Model and LVLM, would it be similar to only conducting an ensemble using different LVLM? I wonder what is the significance and novelty of introducing external image-grounded visual models guidance models. Also, would it achieve similar results by increasing the threshold of object scores so that models won't hallucinate objects with low uncertainty? They can serve as additional baselines to compare with.

### Questions
1. I wonder how much this hallucination problem can be attributed to the visual encoder used by LVLMs. I think MARINE is using other visual models to provide more semantics, or information, in the input prompt, to enhance the downstream tasks to reduce mitigation. Would the results be similar by simply replacing the visual encoder of LVLMs with those image-grounded visual models (like DINO, SAM, or DETR)? The authors could conduct an ablation study comparing MARINE to LVLMs with different visual encoders, including the image-grounded models used in MARINE. This would help isolate the impact of the visual encoder versus the guidance approach.

### Soundness
3

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
This paper proposes MARINE, a training-free and API-free method to address object hallucinations in LVLMs. MARINE integrates an object detector into the pipeline for reliable object identification. The detector's outputs are used as a guidance (a form of controllable generation). The balance between the original LVLM's text generation and the detector's guidance is controlled by a parameter gamma. Compared with baselines, the proposed method shows performance gain on LLM hallucination metrics (CHAIR, POPE).

### Strengths
1. The proposed method combines the complimentary strengths of perception models (object detectors) and generation models. Solving object hallucinations with an object detector is a convincing direction.
2. The proposed method is clean and self-contained. It requires no training and external API calls.
3. Presentation of the paper, including experiments and evaluation is well put together. Comparisons of object detectors and LVLMs, sources of guidances, inference latency analysis make the paper informative and comprehensive.

### Weaknesses
The major concerns are about novelty:

1. The proposed method essentially combines object detection outputs with LVLM generation using a weighted scheme on the token logits. Novelty and technical contribution can be enhanced if more sophisticated methods of bridging the detector and the LLM is proposed. Some rough examples include (1) Does gamma have to be a constant? Any algorithms to dynamically tune gamma based on factors like confidence scores? (2) The detector produces a fixed set of classes. This closed vocabulary nature is different from the LLM. Any thoughts on bridging the vocabulary gap?

2. Using perception models like object detectors to help image-to-text generation were studied in earlier non-LLM methods. Once LVLMs are adapted by the proposed approach, the authors didn't discuss whether the results outperform these specialized models in image captioning and VQA (Table 16). A comparison to related specialized models can better contextualize the results.

### Questions
1. I'm wondering if the proposed method is applied on SOTA models fine-tuned on MSCOCO (not generic VLLMs), will the performance improve. Do the authors have any thoughts on this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the object hallucination problem in LVLMs by utilizing 2D detectors (DETR, RAM++) to provide visual prompts. It proposes that these grounding models provide visual features with higher quality, and combining multiple prompt sources yields better performance.

### Strengths
1. The method description is very clear and easy to understand.
2. Bringing 2D visual feature seems to be a good way to prompt LVLMs to mitigate their inner issues.
3. The results seem to be good.

### Weaknesses
1. While the paper is in very good shape, there are minor errors in writing: in section 4.2, ‘or a rule-based algorithms like XXX’, I think ‘XXX’ might be a typo. Please correct me on this if the authors would like to refer to some work that does not have a reference yet. 
2. Applying 2D features from pre-trained models to prompt downstream tasks (e.g., 3D detection, 2D few-shot detection) is not a completely novel idea. It would be wonderful to see more explanation on this method’s difference from direct prompting.

### Questions
1. Are the pre-trained DETR and RAM++ models being pre-trained before adding to the pipeline? Additionally, does the training vocabulary of DETR and RAM++ influence the performance? Also, I am curious whether the visual prompts are pre-generated prior to the LLM inference or if this 2D prompt-generation time is included in the total inference time.

2. I am also curious about how the performance differs from when using CLIP-extracted features as input prompts compared to DETR and RAM++. Also, there are other 2D feature extractors, including SAM, which has the potential to provide more fine-grained features. 

3. In Table 1, some of the MARINE-Truth’s recall score are significantly lower than MARINE. i.e. the recall score in LLaVA. It will be interesting to see why this is the case since the the access to ground truth guidance is guaranteed.

4. This manuscript mentions two issues in section 4: 1) deficiencies in the visual encoder providing insufficient visual information. 2) misalignment between visual and textual domains. From my current understanding, this work addresses the first issue by providing 2D visual features. It will be nice to see more explanation on whether this method addresses the second issue.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a training-free and API-free framework named MARINE to reduce object hallucinations for LVLMs, with the help of open-source vision models to extract object-level information. Then MARINE integrates information from multiple vision models to refine the visual context provided to the LVLM in a contrastive decoding way. Comprehensive evaluations across multiple LVLMs and datasets demonstrate that MARINE reduces object hallucinations effectively.

### Strengths
1. The paper is well-written and easy to follow. 
2. The core idea of this paper is simple yet effective. 
3. MARINE demonstrates significant improvements over existing methods in reducing hallucinations across various metrics and multiple LVLMs. 
4. MARINE’s design allows integration with different vision models, enhancing its flexibility and robustness in handling diverse contexts.

### Weaknesses
1. In Tables 1 and 2, introducing ground-truth objects (i.e., MARINE-Truth) leads to a significant performance drop in some metrics, which is the exact opposite of the core idea of the paper. Furthermore, the statement in Line 361 ‘The reference method, MARINE-Truth, generally achieves the strongest results.’ is not aligned with the reported results. Please provide a detailed explanation for this discrepancy and clarify why introducing ground-truth objects cause the performance drop. 
2. MARINE’s performance depends on the quality of the external image-grounded models. Limitations in the accuracy of these models may impact MARINE’s effectiveness. 
3. As Table 6 shows, using a single model leads to a significant performance drop, even worse than greedy decoding. This result is counter-intuitive and the authors should do a more in-depth analysis for this phenomenon. Good to provide additional experiments that could help explain this phenomenon as well. 
4. This paper only discusses the additional inference latency of different method in Table 5. However, the additional GPU memory consumption should also be discussed. Please provide GPU memory usage data for each method in a format similar to Table 5,  which would give a more comprehensive view of the computational requirements. 
5. While MARINE effectively mitigates object hallucination, its application is specifically focused on this issue within LVLMs. Extending it to address broader types of hallucinations in general LVLMs remains a challenge.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a training-free method to eliminate hallucinations in Large Vision Language Models (LVLMs) by utilizing guidance prompts generated from grounding models, combined with original inputs, using classifier-free guidance to mitigate model hallucinations.

### Strengths
1. The authors provide code and comparisons for all evaluation outputs, which significantly enhances the work's credibility and technical merit.

2. The proposed method is straightforward, simple, and theoretically well-supported.

3. The experimental section is solid, demonstrating performance improvements across various benchmarks on different models.

### Weaknesses
At this current time, using CFG in VLMs, particularly for hallucination reduction, is not novel. The authors only discuss Visual Contrastive Decoding (VCD) without addressing or comparing with other relevant methods [1][2][3]. While understandable, as most of these methods use CFG with $\gamma>1$, this limitation should be addressed.

### Questions
Regarding the methodology:
As shown in Fig.3, theoretically, $\gamma=1$ already provides sufficient information in most cases. Why is it necessary to balance the original branch? The significance of CFG balance seems unclear. I recommend:
   - Additional experimental validation
   - Presentation of specific cases
   - Clarification of novelty, as if improvements can be achieved simply by adding extra prompt information, the paper's contribution may appear limited

### Soundness
3

### Presentation
3

### Contribution
3
