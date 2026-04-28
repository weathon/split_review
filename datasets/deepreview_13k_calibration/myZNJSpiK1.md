# CoVT-CXR: Building Chain of Visual Thought for Interpretable Chest X-Ray Diagnosis

- Decision: Reject
- Avg Score: 6.75
- Scores: 5, 8, 6, 8

## Abstract
Though clinical report generation demonstrates the potential to improve the efficiency of radiologist workflow and benefits the under-served regions, automated analysis of radiographs suffers from un-interpretable progress and inaccurate results. To this end, we propose a novel Chain-of-Visual-Thought (CoVT) to emulate doctors' multi-modal reasoning, enabling more interpretable and accurate CXR diagnostic predictions with explicit multi-step intermediate guidance. Specifically, we mimic the multi-modal multi-step reasoning procedure of the doctors by breaking down clinical reports into individual descriptions and connecting each rationale to corresponding visual prompts—like masks, landmarks, linestrips, and bounding boxes—to illuminate the visual reasoning behind radiographs. By further dividing this association into cross-modal sub-tasks, CoVT is able to exploit a multi-stage fine-tuning protocol to gradually develop the chain-of-reasoning capability. To support this approach, we introduce CoVT-CXR, the first detailed-aligned, multi-step cross-modal dataset for diagnostic tasks, featuring about 3M instruction-following data points for pretraining and around 30K reasoning sequences for fine-tuning, sourced from 6K patient cases and annotated by 32 medical trainees using our tailored tool. Our CoVT-CXR covers more than 20 diseases, requiring 1 to 12 reasoning steps for diagnoses. Through a series of experiments on our CoVT-CXR, we demonstrate the advantages of the CoVT method over baseline approaches, validate the quality of our annotated data, and highlight the positive impacts of CoVT-CXR on various clinical-related tasks. Our CoVT model, annotation tool, and CoVT-CXR dataset will be fully available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a multi-step instruction tuning framework for generating radiology reports and performing visual question answering (VQA) for chest radiographs (CXRs). To train and fine-tune their models, they also introduce an annotated subset of the MIMIC-CXR dataset which aims to decompose radiology reports into individual statements (they call this dataset CoVT-CXR). Each statement has an accompanying co-ordinate location, semantic description (such as ‘left 7th rib’), and a textual description of the relevant reasoning required to produce the statement of interest. The author evaluate their framework for VQA and report generation against a number of closed-source models such as GPT-4o and some open-source frameworks such as LLaVa-1.5.

### Strengths
- The paper notes an appropriate lack of 'interpretable' medical datasets, and this is true for multi-modal radiological datasets. The introduction of CoVT-CXR would be a welcome resource for a number of researchers in the medical AI field.
- The 5-stage 'step decomposition' framing is intuitive and easy to both motivate and understand.
- The authors attempt a number of ablation experiments to demonstrate both the utility of multi-step reasoning, and the fact that additional traces are associated with improved performance.

### Weaknesses
I have a number of questions and comments that relate to the quality of this work. 
- Whilst the CoVT-CXR dataset does sound useful, it is not possible for me to review any example instances of it. The authors explain all code and the dataset will be released upon acceptance. However, as the dataset is framed as a core contribution, it would be more useful If reviewers could review both an anonymous codebase of their experiments AND at least some instance of the proposed CoVT-CXR dataset. 
- This approach appears to be inference-heavy. Visual and textual information may need to be passed to the model upwards of 12 times to perform inference for a statement $\mathcal{S}$ (as per the abstract - Line 26). Could the authors comment on this? If this is a limitation, it should probably be acknowledged in the main script.
- If the dataset required 32 medical professionals and a bespoke labelling platform, it is unlikely to be a scalable data labelling approach. What it I wanted to do this for brain MRIs, for instance? Unless the authors have a different view, this should also probably be acknowledged as a limitation.  
- How did you deal with incomplete or incorrect ground-truth radiology reports in MIMIC-CXR?
- How were the 112 semantic classes defined?
- Segmentation strategy is quite unclear from lines 271-275. Are you using pretrained segmentation models with prompt engineering to ‘enable zero-short capability for medical images’, or are you fine-tuning models with CXRs, or something else? → if using a generic segmentation model, how do you account for poor segmentation results? 
- How exactly does the framework autonomously identify the report all relevant targets within the images (line 325)? If inference is performed multiple times, can we not end up with the same statement being produced more than once? An explanation is not clear in the manuscript.
- The authors do not compare their framework to Llava-Med, MAIRA-1/2, CheXAgent, etc. I.e., there are no comparisons with VLMs specialized for medical tasks/CXRs specifically. 
- Only lexical metrics are used for eval. These do not appropriately capture meaning as they treat all terms equally (please see https://arxiv.org/pdf/2406.04449 for more detail) — what about RGER, Chexbert, RadFact, etc? These are well known clinical evaluation metrics that are reported in most radiology report generation research.
- Unfortunately, for both ROUGE and meteor metrics (reported lexical metrics), results are somewhat underwhelming. For instance Phi-3V outperforms the proposed CoVT when finetuned. LLaVA-1.5 (not LLaVa-med) matches or outperforms CoVT for both VQA and report generation when fine-tuned. 
- Line 490: Authors claim that incorporating more intermediate steps significantly improves the average sampling probability of ground truth tokens, which enhances the likelihood of generating accurate reports. Could it not simply be the case that incorporating more intermediate steps simply exposes the model to more “ground-truth” tokens, and is thus not a function of improved reasoning per se, but rather something more like oversampling these tokens and therefore generating them more frequently? It would be useful to have clinical metrics rather than purely lexical ones to help make this claim.

### Questions
Please refer to the weaknesses above. 

In addition to the above points, the paper appears to have not been appropriately spelling- or format-checked in many places. Here is a non-exhaustive list: 

Paragraph 2: 
are over-demanding for massive data → demand massive data. 
learning process compared to human → learning process compared to humans.

Fig 1: 
There is a mild enlargement of the cardiac silhouette is present → Mild enlargement of the cardiac silhouette is present

Line 92-93: 
generic as there are all structures and major types of pulmonary pathologies included → generic as all [anatomical] structures and major pulmonary pathologies are included.

Fig 2: 
for one “S” in red? What is “S” explicitly here? Presumably a sentence/segment → if so, is every sentence of every report annotated in this way?
 
Line 131-132: 
shed lights → shed light

Line 150: 
report segment → report segments

line 152: 
corrdinate space → co-ordinate space 

Fig 4 T1 panel: 
<classe> → <classes>

Line 380: 
as shown in 5. → as shown in Fig. 5.

Lines 471-472: 
formatting error — clash between text and Table 3 caption - likely due to vspace adjustment.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work contributes a new public dataset of chest X-ray interpretation (and the chain of thought used) designed for use training Visual LLMs to perform radiology tasks. A model is trained with this data and performance is evaluated against current visual LLMs.

### Strengths
This work presents improved performance compared to zero shot of existing VLM models.

The ablation studies are well done. They present evidence demonstrating multi step reasoning improves model performance compared to a step for medical analysis tasks.

### Weaknesses
The dataset appears through, designed by clinical experts, and cast as well studied ML tasks such as segmentation and question answering.

The evaluation metrics used are generally for machine translation and don't capture how useful the reports are, only that they contain similar words. A solution would be a human evaluation for some set of tasks with quantitative feedback.

### Questions
It would be nice to have more insight into the topics, pathologies, and tasks included in the dataset. Such as a table showing these categories and the counts of samples associated with them. This would help to identify what is in-domain for the model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is a dataset and benchmark paper that incorporates the idea of a 'chain of thought' into constructing the Chest X-ray dataset. This paper offers a unique insight; instead of training end-to-end medical VLM models as most works tend to do, it proposes that just like clinicians make diagnoses based on observations and changes in thought, this process should be incorporated into the dataset. Overall, I believe this paper could be helpful to many audiences. However, there are two issues with this paper: more standard models should be used to compare with CoVT, and using only general evaluation metrics is not sufficient for medical report generation for VQA. I initially gave the paper a weak acceptance, but I might change my score based on whether the paper can provide more evaluation results, especially on medically factually related accuracy scores.

### Strengths
1. *Novel Insight*: It offers a unique insight by proposing that just like clinicians make diagnoses based on observations and changes in thought, this process should be integrated into the dataset.

2. *Comprehensiveness of the Dataset*: The dataset is extensively annotated by over 30 annotators. The medical questions cover a wide range of diseases, enhancing its applicability and relevance.

3. *Claimed Transparency*: Although not available yet, the authors commit to releasing both the model and the annotation tool, along with the related codes. This promised transparency is commendable and aligns with open science principles.

### Weaknesses
1. *More model evaluation*: The use of LLaVA-1.5 is noted, but LLaVA-1.6 offers significant improvements that could enhance model performance. I recommend upgrading to this latest version for fine-tuning. Additionally, exploring models like Flamingo may further improve results.
2. *Evaluation Metrics*: The evaluation metrics used—BLEU, ROUGE, METEOR, and CIDEr—are standard for many natural language processing tasks; however, they are not ideally suited for evaluating medical Visual Question Answering (VQA) or the factual accuracy in medical reports. These metrics often fail to capture the semantic accuracy required in medical contexts. It is critical to implement more specialized metrics that can assess the medical factual accuracy and the clinical relevance of the answers provided by the system.

### Questions
1. *Model Comparison*: Do you think it is a fair comparison to have an encoder trained on medical data while a model like LLaVA uses an encoder trained on everyday images?

2. *Image encoder*: The SSL method (VAE) you used is somewhat outdated. Are there specific reasons for not using more up-to-date methods like Dino_v2? I'm not suggesting that what you did is incorrect or insufficient; I just want to understand why you chose this particular SSL method.

3. *Multi-Stage Fine Tuning*: The approach you took to multi-stage fine tuning is interesting. Do you have any evidence supporting that what you did is necessary?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors propose a chain-of-thought approach to automated radiology report generation. They propose a data labeling strategy and tool to support this approach, generate a new set of chain-of-thought labels for a subset of the MIMIC-CXR dataset, and propose a new training strategy to utilize their chain-of-thought labels.

### Strengths
-	A new dataset has been developed that should be valuable to the community. This dataset contains fine-grained, chain-of-thought reasoning labels that mimic how radiology reports are generated by humans. This dataset generation is a manually intensive process that will likely support future research.
-	An open-source tool to generate additional chain-of-thought labels was developed and provided, which is another valuable addition to the community. 
-	In addition to generating more correct answers, the proposed method also generates more interpretable answers, which is a critical need in this domain.

### Weaknesses
-	The authors reference an Appendix many times, but there is no Appendix.
-	The baselines in the evaluation are not medical-specific models. There have been many models proposed for radiology report generation which have been trained on medical images/text, however the authors opt to use natural image/text baselines, which is an unfair comparison. For example, instead of comparing against Llava-med or llava-rad, they compare against llava; instead of comparing against med-gemini, they compare against gemini. Similarly, they exclude models specifically trained for radiology report generation, such as maira-1 or any of the numerous other proposed radiology report generators. As a result, I do not find the empirical results convincing. 
-	The paper is difficult to read and follow. In particular, I have a difficult time following how the dataset was created and the contents of the dataset. What are the 112 semantic classes? How were these chosen? What is a “intermediate text description”? Is there any standardization on what an “intermediate text description” comprises? The murkiness of this dataset development description makes it difficult to understand how valuable the dataset will be to others or how one would go about extending the dataset. 
-	Additionally, the total size of the dataset is relatively small (6k cases), and the test dataset is very small (400 cases). While I understand this is because of the manual effort required to create a chain-of-thought dataset, it does limit its upper bound on performance. I am doubtful of how well this dataset size could be increased in the future, as the chain-of-thought labelling process is not very well described. Further, if the authors could discuss how this dataset could be used in tandem with other non-chain-of-thought datasets, that would be useful. 
-	In the Data Curation: Motivation section and later in Section 3.1, the authors authoritatively describe a process that doctors (the authors imply all doctors) use to read chest x-rays. There are no references in this section, aside from a footnote pointing to “geekymedics” and “radiologymasterclass” websites. I find this support weak; either the language in this section should be made less strong, or additional support is needed as to how the authors determined this CXR reading process. 
-	Limitations and Future Work should be discussed.

In summary, I find the dataset and approach interesting and useful for the community. While the baseline comparisons leave me unsure of how well the proposed method actually works and the writing needs revision for clarity, I still find this dataset and general approach to be a valuable contribution and lean toward acceptance.

### Questions
Above.

### Soundness
3

### Presentation
2

### Contribution
3
