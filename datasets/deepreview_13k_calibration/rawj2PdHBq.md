# Can Medical Vision-Language Pre-training Succeed with Purely Synthetic Data?

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Medical Vision-Language Pre-training (MedVLP) has made significant progress in enabling zero-shot tasks for medical image understanding. However, training MedVLP models typically requires large-scale datasets with paired, high-quality image-text data, which are scarce in the medical domain. Recent advancements in Large Language Models (LLMs) and diffusion models have made it possible to generate large-scale synthetic image-text pairs. This raises the question: \textit{\textbf{Can MedVLP succeed using purely synthetic data?}} To address this, we use off-the-shelf generative models to create synthetic radiology reports and paired Chest X-ray (CXR) images, and propose an automated pipeline to build a diverse, high-quality synthetic dataset, enabling a rigorous study that isolates model and training settings, focusing entirely from the data perspective.
Our results show that MedVLP models trained \textit{exclusively on synthetic data} outperform those trained on real data by \textbf{3.8\%} in averaged AUC on zero-shot classification. Moreover, using a combination of synthetic and real data leads to a further improvement of \textbf{9.07\%}. Additionally, MedVLP models trained on synthetic or mixed data consistently outperform those trained on real data in zero-shot grounding, as well as in fine-tuned classification and segmentation tasks.
Our analysis suggests MedVLP trained on well-designed synthetic data can outperform models trained on real datasets, which may be limited by low-quality samples and long-tailed distributions\footnote{All data and code will be released upon acceptance.}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a thorough evaluation of the medical visual language model with synthetic data. It is proven that training MedVLM with synthetic data and a carefully designed data generation pipeline can significantly boost the model's performance in multiple downstream tasks. The proposed chest X-ray generation pipeline can generate high-fidelity image-report pairs with the given entity. With proper design, the synthetic data can avoid the data quality issues within the real-world data such as long-tailed distribution, and incorrect or low-quality images.

### Strengths
1. The proposed image-report generation pipeline uses entities extracted from the real-world report. By sampling these entities with a balanced prior, the synthetic dataset ensures a more balanced distribution compared with real-world data. This has proven to be helpful in the downstream evaluations.
2. This work has conducted a very thorough evaluation with carefully designed experiment settings. It has evaluated the pre-trained model with different training data on multiple downstream, OOD datasets under different settings. It has also evaluated the influence of using different report generation models and text-guided image generation models, which further validate the design of the proposed pipeline.
3. The paper is well-written and easy to follow, and all the technical details are very clear.

### Weaknesses
1. One of the major concerns of this paper is the entity sampling process during report generation. According to the paper, the only constraint on this process is the balanced distribution constraint. However, it is possible that the method samples contradictive entities. For example, “decreased in size” and “increased in size” are two of the top 50 entities in the abnormality entities according to Figure 6. They naturally contradict, but it is possible that the model samples both entities during report generation. Moreover, The quality of the extracted entity is also not very satisfying. There are multiple repeated, or less meaningful entities in the top 200 examples according to the appendix. What makes it worse is that the only quality control on report generation is the evaluation of whether the sampled entity exists or not, rather than if they are reasonable as set. Also, enforcing all the sampled entities to be present in the “Impression” section does not make much sense as well. The “Impression” section in the real-world report may not always contain all the findings. So the quality of the generated report is very concerning without further evaluation, especially considering that there are no example reports provided here. Though it indeed improved the performance.
2. Another secondary concern is about the image quality generated from the synthetic reports. Though the author used a SoTA CXR generative model validated by “clinical experts”, the concerns about generated image correctness still remain, especially considering there might be self-contradicting/incorrect synthetic reports. As a universal concern about the medical image generation method, the method adopted here has no control over the anatomy structure, which means it could generate unrealistic CXR and therefore pollute the downstream training process. 
3. Additionally, there are some implementation details missing in the paper. a) The actual value of $k$, $m$, and the sampling threshold $\tau_{max}$ were not mentioned in the paper or appendix, which is very critical to understanding the method. b) There is no specific description of the pre-training setting with mixed data, where the dataset size is doubled, It is unknown if the training time is also doubled or not.
4. Considering that the paper itself focuses on evaluating the influence of synthetic data on MedVLM, 2 baseline methods are not very convincing. Except for the methods mentioned in the paper that are not suitable, the reviewer would still recommend evaluating more baselines like naive CLIP and MGCA[a]. It is necessary to conduct further evaluation to validate the conclusion of this paper.
5. There are some small typos in the paper such as a) Some of the results in Table 3 row 3 (ConVIRT-MIX) are bolded incorrectly. b) The “Medical Image Fine-tuned Classification” section in section A.2 was aligned incorrectly as well. c) Also, it would be better if the author could annotate the exact numbers in Figure 3. The current version is not very clear, especially in the bottom right figure.

### Questions
While the improvement shown in the paper is quite impressive and the reviewer actually agreed with the authors about the major conclusion, there are still some major concerns about the proposed data synthetic pipeline, as mentioned above. Also, the reviewer has the following questions:

1. The reviewer wonders if it is possible to conduct any form of data quality evaluation on the synthetic data. Even if the experiment results prove that using the synthetic data has greatly improved the performance, it remains unknown if the incorrect synthetic data has injected incorrect knowledge into the model, considering the loose data generation process.
2. Can the author provide some examples of the generated data in the appendix or supplement? The current paper has no example of the generated data, which makes it less convincing.
3. The reviewer also wonders how well the models may perform if they were trained with the **cleaned** MIMIC-CXR as mentioned in the paper. It seems that this cleaned version of MIMIC-CXR is only used for filtering out low-quality synthetic images.

The reviewer sincerely looks forward to hearing from the author during the rebuttal and would be happy to discuss the concerns mentioned above.

### Soundness
2

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
5

### Summary
This paper details a pipeline for generating fully synthetic datasets with the downstream objective of pretraining large vision-language models (VLMs). The synthetic datasets are generated semi-automatically by producing a set of entities using RaTE, a named entity recognition algorithm, which are sampled to produce a subset of findings per sample and are then used to generate a textual report. The textual report is iterated with LLMs to ensure congruence with the initial subset of entities, and is then used for the generation of synthetic images using a text-to-image algorithm. A series of datasets are created using this methodology, which are then explored in a battery of different evaluation strategies for zero-shot classification & segmentation via grounding and further fine-tuning with real data to improve initial VLM performance. The extensive numerical results show consistent performance improvement in VLM when training with mixed real and synthetic data.

### Strengths
•	Fully synthetic image generation might open the door to more balanced datasets for training larger vision models, which is a challenging topic in medical image analysis.
•	The evaluation presented is extensive and covers many different aspects of image analysis in the medical domain
•	The work delves into recent trends in AI, where pre-trained services are connected to create outcomes beyond their original intended usage (i.e., using pretrained LLMs, NER algorithms, and TTI synthesis…).
•	The emphasis on only using open-source models is commendable.

### Weaknesses
•	The evaluation as expressed in the document is rather confusing, where in many cases it’s not clear which is the evaluation/test set used to derive a set of results (e.g., Table 4, Fig 3).


•	There is a lack of a discussion section, which affects the completeness of the work. It would be preferred to move certain aspects of the methodology (and even some results!) to the appendix (e.g., the specific prompts used to identify and filter low-quality images) and create a proper discussion. The reason behind this is because there are some aspects of this work which puzzle the reader (e.g., the low F1 scores in most zero-shot evaluation techniques) that could/should be addresed in the discussion.


•	Section 3.2. could be worded better, so that it’s clear that a single sample contains both anatomical and clinical entities. I found it slightly confusing


•	There are many aspects of this work that would need remediation or discussion. In no particular order: 

1.	In the “analysis” section, there is no description of which test set is employed, so these performance reports are difficult to interpret, validate and compare. 

2.	Section 5 should be merged with 4.2. to create a singular “results” section.

3.	Why do you claim “Some methods also leverage external datasets to boost performance, raising concerns about generalizability”? No metric has been provided. 

4.	Why do you claim that “Our results confirm that many images in the dataset exhibit these issues” in section 3.1.? No metric has been provided. 

5.	Much of the evaluation focuses on classification – what are we to gain using a VLM as opposed to a self-supervised CXR model like Rad-DiNO? 

6.	You’ve identified 150k+ entities, but the synth dataset is 200k. This would lead to the generation of a very low number of samples-per-entity. This can also lead to illogical combinations (e.g., pneumothorax in rib) which AFAIK are not accounted for. 

7.	The generation efforts described in 3.2. look quite compute-intensive. It’s not essential for the work but I’d be interested to have some approximate time taken to generate a single sample (i.e., text generation + filtering and QA + IMPRESSION generation + TTI). 

8.	This methodology could easily lead to collapse because of feeding an algorithm with synth data, see 10.1038/s41586-024-07566-y

9.	The F1 and Dice/IoU scores are quite low in most zero-shot evaluation techniques (tables 1 and 2). It could use some discussion/comparison to other vanilla VLMs and non-VLMs (e.g., zero-shot segmentation with Rad-DiNO). Moreover, the IoU increase wrt the real baseline is not super significant.

10.	It’s not clear how exactly the models are fine-tuned in Section 4.2. What’s the pretraining dataset? Which is the dataset used for fine-tuning?

11.	There’s no comparison to other concept generation or filtering techniques, which is the main contribution of your work. You provide a large amount of experimental runs for downstream applications but the bulk of your work is the synthetic data generation pipeline. Although this is understandable because a paper has to be constrained somehow, some mention in discussion/future steps would be required.

12.	Section 5 contains claims that have not been formally and are hipotheses, e.g.: “likely due to the persistent long-tailed distribution, as the synthetic reports are generated based on real images” or “as synthetic images can be curated using our image filtering procedure to ensure high quality, avoiding issues commonly found in real datasets”.

### Questions
See weakness part and please answer the listed question and concerns

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Given that recent large visual language models require extensive medical data and often rely on synthetic data, the authors question whether synthetic data alone could meet these needs effectively. Through experiments conducted on a synthetic chest X-ray dataset, they found that the synthetic data outperformed real data.

### Strengths
- The authors developed SYNCXR, a large-scale synthetic X-ray dataset, demonstrating that models trained on this dataset could achieve improved performance. 
- They also identified common issues prevalent in real-world datasets, such as MIMIC-CXR.

### Weaknesses
 - Concerns with the Experiment and Scope: The focus of this study should be limited to evaluating whether a synthetic CXR dataset can enhance VLM training. Currently, the authors have not included experiments involving other modalities, which limits the broader applicability of the findings.
- RadGraph and RaTE Discussion: I recommend addressing the limitations of RadGraph and the rationale behind RaTE in the related work section, rather than in the main text, as it detracts from the primary focus.
- Novelty and Methodological Concerns: This work primarily takes an engineering approach to address a specific task, lacking novel theoretical contributions or robust validation. For instance, the authors did not provide a mathematical explanation as to whether synthetic data can lead to improved representation learning, nor did they validate the generated data with real clinicians. While model-based validation is acceptable, practical relevance in radiology requires clinician verification.
- For medical image segmentation, the authors should include qualitative comparisons across methods to strengthen their claims, especially as the current quantitative results are presented as single-digit figures, which may be insufficient to persuade readers.
- Additional experiments are recommended to expand the study’s scope, including evaluations across other modalities, tasks beyond visual language pretraining, and models that confidently showcase quantitative results.
- There is a typo in line 233.

### Questions
- The authors noted that 1,448 + 5,512 samples were removed from the MIMIC-CXR dataset; however, this constitutes only about 3% of the entire dataset, raising questions about the necessity of this step. Could the authors provide evidence demonstrating that excluding these ~7,000 samples significantly benefits MedVLP training?
- Incorporating more modalities and tasks would strengthen the argument that synthetic datasets can offer substantial benefits across a broader range of applications.

### Soundness
2

### Presentation
3

### Contribution
2
