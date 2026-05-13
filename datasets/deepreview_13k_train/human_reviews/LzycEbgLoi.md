# 3D-CT-GPT++: Enhancing 3D Radiology Report Generation with Direct Preference Optimization and Large Vision-Language Models

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Automatically generating radiology reports from three-dimensional medical images, such as 3D CT scans, plays a crucial role in modern diagnostics. Current approaches for generating 3D reports often adopt video processing methods, which struggle to effectively capture the relationships along the Z-axis. Additionally, multimodal large language model-based methods for generating 3D image reports face significant limitations, particularly in terms of the image encoder’s ability to represent 3D structures and the hallucinations that arise in generated content. To address these challenges, we propose the 3D-CT-GPT++ model. This model integrates the optimized 3D image encoder CTViT-V, specifically designed for chest CT scans, and builds upon the LLaVA-1.5 architecture. Furthermore, we introduce \textit{Direct Preference Optimization (DPO)}, where GPT-4 is used to score the outputs of our fully fine-tuned (SFT) model, creating a preference dataset for subsequent DPO training. DPO significantly reduces hallucinations in the report generation process, ensuring the generated reports are more aligned with clinical needs. We fine-tuned the model on both high-quality private and public datasets to ensure clinical relevance. Extensive experiments were conducted using standard natural language generation (NLG) evaluation metrics, including BLEU, METEOR, ROUGE-L, and GREEN, to assess the report generation performance. Experimental results demonstrate that 3D-CT-GPT++ significantly outperforms existing methods in terms of accuracy, fluency, clinical factual consistency, and clinical relevance, advancing the automation of 3D medical report generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces 3D-CT-GPT++, a novel model for radiology report generation that leverages an optimized 3D image encoder (CTViT-V) specifically designed for chest CT scans. They apply Direct Preference Optimization to reduce hallucinations and increase factfulness. They show that 3D-CT-GPT++ outperforms existing methods.

### Strengths
1. The paper presents a novel CTViT-V encoder, specifically optimized for 3D CT images, addressing the challenges of spatial coherence and slice dependency, which could contribute to improved clinical relevance and accuracy​
2. The use of GPT-4 for preference optimization provides a scalable, cost-effective alternative to human feedback, potentially reducing hallucinations and aligning generated reports more closely with clinical needs​
3. Despite limitations in using NLG metrics, the proposed model outperforms existing benchmarks in BLEU, ROUGE, and METEOR scores

### Weaknesses
1. The evaluation relies on standard NLG metrics like BLEU and ROUGE, which do not capture clinical relevance or diagnostic utility. Using the GREEN metric[1] or RadFact[2] for evaluation would allow assessing clinical relevance
2. The authors propose a multi-stage training process. The community would benefit from more ablation and more details for each stage: 
2.1 For Stage 1 and 2 it would be interesting to see how their CTViT-V encoder performs in comparison to other 3D CT image encoder, such as CTViT and CT-CLIP. 
2.2 Stage 2 pre-training is not well described. It's not clear how the custom-built dataset looks like, nor how the interactive approach was performed. 
2.3. Ablation study scoring LLMs would be interesting to see how sensitive the performance is to the chosen LLM. 
2.4. Ablation study on 3D-CT-GPT++(LoRA+DPO) missing, especially since 3D-CT-GPT++(LoRA) achieves higher performance than 3D-CT-GPT++(SFT)
3. The experiments are not reproducible due to the reliance on private dataset in many steps. It's not clear to me, why the authors didn't conduct their experiment on the public CT-RATE dataset. 
4. Comparison to Existing Models: The literature results are not comparable to the fine-tuned 3D-CT-GPT(++) results since the literature results are without finetuning on the dataset, therefore it's hard to judge the works improvements over other methods.

### Questions
1. What are the various reconstructions techniques described in 3.4 Dataset, which expands the dataset? (line 320-322)
2. The authors use a subsection of the CT-RATE dataset, it's not described how they do this subselection and what's the motivation behind it. Why don't they use the whole dataset? 
2. Are you planning to open source the training code/weights? 
3. Will the authors publish the Dataset-XY?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach to automatically generate radiology reports from 3D medical images such as 3D CT scans. Traditional methods mostly use video processing technology, which is difficult to effectively capture the relationship between images along the z axis, and multimodal large language models have limitations in representing 3D structures and avoiding the illusion of generating content. To address these issues, the authors proposed the 3D Structure-CT-GPT ++ model, which integrates an optimized 3D image encoder CTViT-V designed for chest CT scanning and is based on the LAVA-1.5 architecture. Furthermore, this work introduces Direct Preference Optimization (DPO), which uses GPT-4 to score model outputs to reduce hallucinations and ensure reports are more aligned with clinical needs. The model was fine-tuned in two high quality conditions.

### Strengths
1. This work proposes the 3D-CT-GPT++ model, which integrates an optimized 3D image encoder specifically designed for chest CT scans. This novel approach addresses the limitations of existing methods in representing 3D structures and reducing hallucinations in generated content.
2. This paper is well-organized and clearly presents the problem, methodology, experimental setup, and results. The use of appendices provides additional details, enhancing the readability of the paper.

### Weaknesses
1. The format of references needs to be uniform. Some citations lack journal names. Such as "Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023a.", "Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023b.". In addition, on line 320 of page 6, the CT-RATE dataset is missing references. Authors need to carefully check and format the references.

2. 3D-CT-GPT++ models use complex architectures such as CTViT-V encoders, which can lead to high demands on computational resources and time. The authors mention that they reduce the computational overhead associated with processing high-resolution 3D volumes. However, the design of specific methods to reduce computing costs is not described in detail. The authors are advised to elaborate further on the design used to improve computational efficiency. It is better to show the computational cost through quantitative comparisons of computational requirements (e.g., GPU memory usage, training time) between the proposed model and baseline approaches. 

3. To further enhance the clinical relevance of the generated reports, the authors could consider incorporating additional clinical context or patient-specific information into the model.

### Questions
1. What strategies were used to mitigate potential biases in the generated medical reports?
2. How does the integration of the optimized 3D image encoder improve the representation of chest CT scans compared to traditional 2D image encoders?

### Soundness
3

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
The paper titled "3D-CT-GPT++: Enhancing 3D Radiology Report Generation with Direct Preference Optimization and Large Vision-Language Models" presents a novel approach for automating radiology report generation from 3D CT scans, addressing key challenges in current methods. Traditional models, often adapted from video processing, struggle to maintain spatial consistency along the Z-axis and are prone to inaccuracies ("hallucinations") in generated content. 

An optimized 3D image encoder, CTViT-V, is designed to improve spatial and temporal feature extraction specific to 3D CT images. This encoder integrates a slice Transformer and relative position encoding to better capture global dependencies across CT slices.

Built upon the LLaVA-1.5 architecture, the model efficiently processes 3D CT data and enhances the generation of radiology reports, providing a more accurate and context-aware representation.

To mitigate hallucinations without the high costs associated with Reinforcement Learning from Human Feedback, DPO is employed. GPT-4 scores model outputs, creating a preference dataset that aligns generated reports with clinical relevance and accuracy.

### Strengths
The work is original in both its application and the methodology employed for 3D CT scan analysis. Unlike many radiology models that focus on 2D images, this paper tackles the more complex problem of 3D report generation, which requires understanding inter-slice dependencies across the Z-axis. The introduction of Direct Preference Optimization (DPO) for reducing hallucinations in generated reports is particularly innovative. Instead of relying on human feedback, which is costly and often impractical for large-scale applications, DPO utilizes GPT-4 for automated scoring, presenting a scalable approach to aligning model output with clinical relevance. Furthermore, the integration of the CTViT-V encoder optimized for 3D imaging enhances both spatial and temporal feature extraction, making this an effective and creative combination of existing model architectures adapted for a challenging domain.

The model's ability to handle 3D CT data and generate clinically relevant radiology reports holds significant potential for the medical field, especially in reducing radiologists’ workload. Addressing hallucinations in generated reports is a critical advancement, as inaccurate information in medical reports can lead to severe consequences. By demonstrating substantial improvement over existing models and applying DPO to radiology for the first time, this work positions itself as a valuable contribution. The approach’s scalability, thanks to automated feedback from GPT-4, enhances its significance by making it feasible for broad deployment in clinical settings. Future extensions to other imaging modalities, such as MRI and X-ray, as discussed in the conclusion, underscore its adaptability and potential long-term impact.

### Weaknesses
Lack of Detailed Hyperparameter Configuration: More information about the choices made for hyperparameter training configurations would be beneficial. This detail could help with model reproducibility and provide clarity on the specific adjustments that impact performance.

Comparison with 2D Models: Although the paper focuses on introducing a 3D model, it would be helpful to include a comparative analysis with existing 2D models for similar tasks. This comparison could better highlight the specific advantages and limitations of the proposed 3D approach.

### Questions
Could you provide more details on the hyperparameter choices and training configurations? For instance, what specific hyperparameters were optimized, and how were they chosen or tuned?

Given the focus on a 3D model, did you evaluate any baseline comparisons with existing 2D models for similar tasks?

How does DPO specifically reduce hallucinations compared to Reinforcement Learning from Human Feedback (RLHF)? Are there examples where RLHF failed but DPO succeeded?

### Soundness
3

### Presentation
3

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
This paper proposes the 3D-CT-GPT++ model. 
The main contributions include 3D image encoder CTViT-V, report generation model 3D-CT-GPT++, and the Direct Preference Optimization(DPO) technique.

### Strengths
Originality: The original method combines contrastive learning for image encoder pretraining, spatial transformer+slice transformer for 3D vision encoding, LLaVA architecture to support report generation from images, and DPO technique to optimize the quality of generation.

Quality: A complete framework, sufficient workload on method design, and effective performance

Clarity: Clear figures and writing about methods

Significance: Limited technological progress

### Weaknesses
 * Bad figure quality: Misalignment of line; Overlap of text and border; Case is not unified.

* Unclear experiment setting. The main text of the paper just describes the source and preprocessing of datasets, without mentioning the training and evaluation setting of datasets which is essential for the experiment section.

* Unfair comparison.  RadFM and M3D results in Table 1 are based on a different evaluation setting. The notation of "Literature Results" is not enough to describe the relationship.

* Computational overhead reduction of CTViT-V is listed as one of the major contributions, but there is no evaluation of it.

* Compared to the entire 3D ViT of M3D, what is the advantages of 2D slice encoding + Z-fusion?

### Questions
Weaknesses have contained the part of questions. Please consider them seriously.

### Soundness
3

### Presentation
2

### Contribution
3
