# Large-scale and Fine-grained Vision-language Pre-training for Enhanced CT Image Understanding

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Artificial intelligence (AI) shows great potential in assisting radiologists to improve the efficiency and accuracy of medical image interpretation and diagnosis. However, a versatile AI model requires large-scale data and comprehensive annotations, which are often impractical in medical settings. Recent studies leverage radiology reports as a naturally high-quality supervision for medical images, using contrastive language-image pre-training (CLIP) to develop language-informed models for radiological image interpretation. Nonetheless, these approaches typically contrast entire images with reports, neglecting the local associations between imaging regions and report sentences, which may undermine model performance and interoperability. In this paper, we propose a fine-grained vision-language model (fVLM) for anatomy-level CT image interpretation. Specifically, we explicitly match anatomical regions of CT images with corresponding descriptions in radiology reports and perform contrastive pre-training for each anatomy individually. Fine-grained alignment, however, faces considerable false-negative challenges, mainly from the abundance of anatomy-level healthy samples and similarly diseased abnormalities, leading to ambiguous patient-level pairings. To tackle this issue, we propose identifying false negatives of both normal and abnormal samples and calibrating contrastive learning from patient-level to disease-aware pairing. We curated the largest CT dataset to date, comprising imaging and report data from 69,086 patients, and conducted a comprehensive evaluation of 54 major and important disease (including several most deadly cancers) diagnosis tasks across 15 main anatomies. Experimental results demonstrate the substantial potential of fVLM in versatile medical image interpretation. In the zero-shot classification task, we achieved an average AUC of 81.3% on 54 diagnosis tasks, surpassing CLIP and supervised methods by 12.9% and 8.0%, respectively. Additionally, on the publicly available CT-RATE and Rad-ChestCT benchmarks, our fVLM outperformed the current state-of-the-art methods with absolute AUC gains of 7.4% and 4.8%, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a fine-grained vision-language model (fVLM) to improve CT image interpretation by associating specific anatomical regions in CT scans with corresponding descriptions in radiology reports, addressing limitations of global image-report contrastive methods. It introduces a large dataset, MedVL-CT69K, encompassing 272,124 CT scans and achieves state-of-the-art performance. Key contributions include anatomy-level contrastive learning and a method to handle false negatives.

### Strengths
1. Fine-Grained Anatomy-Level Alignment: The paper introduces a novel, fine-grained vision-language model (fVLM) that aligns anatomical regions in CT images with corresponding report descriptions.
2. Large and Comprehensive Dataset: Experiments were conducted on a range of datasets including the largest CT dataset to date (MedVL-CT69K)
3. Effectively tackling shortcomings of their method by introducing the dual false-negative reduction approach.

### Weaknesses
1. Experiments are incomplete: Table 1 doesn't include a performance evaluation of the methods from Table 3, namely CT-CLIP, CT-VocabFine, CT-LiPro. Table 3 doesn't include performance evaluation of the methods from Table 1. In both cases it's not argued why those experiments were not conducted. For Table 1, and Table 2 it's also unclear how the 2D approaches were adapted for 3D and how their evaluation was then done. Additionally, the evaluation metrics in Table 1 and Table 3 differ. Why? Furthermore, the performance comparison in Table 2 should also include comparisons to other CT-CLIP approaches, not only natural image counterparts (he it's again not clear how the 2D models were adapted to 3D).  
2. Report generation uses only a single NLU metric. Other NLU metrics such as ROUGE would be interesting. Furthermore, using the GREEN metric[1] or RadFact[2] for evaluation would allow assessing clinical relevance.
3. T-SNE visualization: An (additional) comparison of the embeddings to CT-CLIP would be be interesting to see if they have the same clustering behavior. 
4. Ablations study on masking missing: The masking approach is not well investigate and no ablation studies are done. One intuitive baseline would be the anatomical cropping of the image. What's the advantage of the masking approach? 
5. The authors approach only works for CT scans, since it relies on anatomy segmentations from TotalSegmentator. Furthermore, only on the classes which are available in TotalSegmentator.

### Questions
1. What's the authors reproducibility statement? Will the dataset, code and weights be released? Especially publishing the dataset would be of great value for the community.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work discusses the fine-grained alignment issue for vision-language clip-like pretraining for CT and reports. To improve the granularity of alignment the authors propose to pre-segment key anatomical structures in CT using a public segmentation model (Totalsegmenter), and to pre-segment descriptions corresponding to individual anatomical structures in the free-text report using an open-access LLM (Qwen). This allows fine-grained contrastive learning at the anatomical structure level. Considerations are made to avoid pushing representations of the same organ/condition away. Improved performances are shown for zero-shot abnormality detection compared with several existing approaches.

### Strengths
The idea of increasing the granularity of contrastive learning by data pre-segmentation using public tools is neat, simple, and straightforward. 

The paper is written with sufficient clarity, where the insights behind each design and the implementations details are well-presented. 

Improved performance on zero-shot abnormality detection is shown compared with some existing works.

### Weaknesses
For a comprehensive assessment of report generation some essential scores are missing, such as BLEU 1-3, ROUGE-L, and METEOR. Also, comparisons with vision encoders from peer vision-language pre-training for CT works may be needed. This is my major concern as the authors have claimed improved performance on report generation task.

Despite improved granularity, attributing sentences of reports `mentioning` a structure to the image feature of that structure may sometimes be misleading especially when manual verification/correction is not accessible. E.g., in practice pancreatitis is often associated with the entire abdomen instead of the pancreas alone and neighboring structures. The authors are encouraged to comment on this.

### Questions
A high-level question: The capability of open-source image segmentation tools (totalsegmenter and/or SAM family) and open-source LLM advance fiercely -- does it imply that the utility of (un-/weakly-supervised) vision-language pretraining for CT will gradually phase out? One may directly construct semantic labels from text reports using strong enough LLM tools and turn the problem back to large scale supervised learning. I am curious to hear the authors’ insight.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present an vision-language model for  anatomy-aware medical report generation, adressing the task of false negative reduction.  A large (private) dataset is curated and good performances on public datasets are presented.

### Strengths
* The study addresses an interesting multi-modal learning problem from the medical domain
* The presented false negative reduction is a meaningful integration to vision-language model report generation
* The results are promising indicating the relevance of this addition

### Weaknesses
 * The methodology is not quite clear
* There is no codebase, preproduction may be a challenge.

* Image Encoder Setup: The authors mention using a ViT base model with MAE pretraining on ImageNet-1K and a patch size of 16 x 16 x 32 (referenced in A.2). However, it’s unclear how they process 3D volumes with 3D patch embeddings through a 2D ViT model. Although they provide details on the training procedure, the overall model architecture remains vague. Given the lack of source code, a clearer description of the model's structure is crucial. Can the authors improve?
* Comparison with 2D CLIP Methods: The comparisons made with 2D CLIP methods in Table 1 are not fully explained. Specifically, it's unclear how they adapted these methods to a 3D context and how the training was conducted. Please clarify.
* Evaluation with CT-CLIP: In Table 3, the comparison with CT-CLIP models is ambiguous. Did the authors fine-tune a pre-trained model (based on their in-house data) on CT-RATE, or was there a different approach taken?
* t-SNE Consistency: To enhance the consistency of the embedding spaces shown in Fig. 7, the authors could consider setting a random seed before calculating the t-SNE embeddings.
* HU Value Clipping: The authors chose to clip HU values between -300 and 400, which raises a question: Does this range cover all abnormalities? For instance, lung-related abnormalities are typically closer to -1000 (representing air), while bone-related abnormalities can reach values close to 1000. Since they utilized both non-contrast and contrast-enhanced CT scans (arterial, venous, and delayed phases), did they apply this same HU preprocessing across all scans? Additionally, did the authors use this range for the CT-RATE training ablations (which is different than the original CT-RATE paper)? Please clarify.

### Questions
* Image Encoder Setup: The authors mention using a ViT base model with MAE pretraining on ImageNet-1K and a patch size of 16 x 16 x 32 (referenced in A.2). However, it’s unclear how they process 3D volumes with 3D patch embeddings through a 2D ViT model. Although they provide details on the training procedure, the overall model architecture remains vague. Given the lack of source code, a clearer description of the model's structure is crucial. Can the authors improve?
* Comparison with 2D CLIP Methods: The comparisons made with 2D CLIP methods in Table 1 are not fully explained. Specifically, it's unclear how they adapted these methods to a 3D context and how the training was conducted. Please clarify.
* Evaluation with CT-CLIP: In Table 3, the comparison with CT-CLIP models is ambiguous. Did the authors fine-tune a pre-trained model (based on their in-house data) on CT-RATE, or was there a different approach taken?
* t-SNE Consistency: To enhance the consistency of the embedding spaces shown in Fig. 7, the authors could consider setting a random seed before calculating the t-SNE embeddings.
* HU Value Clipping: The authors chose to clip HU values between -300 and 400, which raises a question: Does this range cover all abnormalities? For instance, lung-related abnormalities are typically closer to -1000 (representing air), while bone-related abnormalities can reach values close to 1000. Since they utilized both non-contrast and contrast-enhanced CT scans (arterial, venous, and delayed phases), did they apply this same HU preprocessing across all scans? Additionally, did the authors use this range for the CT-RATE training ablations (which is different than the original CT-RATE paper)? Please clarify.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents fVLM, a fine-grained vision-language model for CT image interpretation. The key innovation is to perform anatomy-level contrastive learning between CT scans and radiology reports. The authors introduce a dual false negative reduction approach and curate a large dataset (MedVL-CT69K) with 69,086 patients. The model achieves strong zero-shot performance across 54 disease diagnosis tasks and outperforms existing methods on public benchmarks.

### Strengths
1. Anatomy-level fine-grained alignment for the complex report generation task/ diagnosis task is a great idea. 
2. The paper collects large-scale datasets with expert annotations, which is time-consuming and expensive in the medical domain.
2. The paper is well-structured, with extensive results (including ablation studies and visualizations) showing clear improvements over baselines.

### Weaknesses
The evaluation metrics for the report generation task are limited to basic metrics (BLEU-4) and diagnostic accuracy. The paper should include medical-specific metrics like RadCliQ, RaTESCore, or GREEN that better capture clinical relevance and factual consistency.

### Questions
1. Will the MedVL-CT69K dataset or the pre-trained model checkpoint be open-sourced? Additionally, why are there different numbers of diseases annotated in the validation (36) and test (54) sets? 
2. While Figure 7 shows more compact embedding clusters for positive cases compared to CLIP, there seems to be limited separation between positive and negative cases. 
3. It would be great if the radar plot could link with positive case numbers and normal/abnormal ratios.  This would help readers better understand the model's performance across different conditions and data distributions. Also more analysis on long-tailed disease.
4. The scaling law curve is interesting, 272,124 CT scans from 69,086 unique patients are the largest CT dataset till now, but still far away from data saturation. Do you do the data selection (try to include more abnormal patients) when collecting the dataset? Will the scaling law related to data distribution?

### Soundness
4

### Presentation
3

### Contribution
3
