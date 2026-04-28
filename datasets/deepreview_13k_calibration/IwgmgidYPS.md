# MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
This paper introduces MedTrinity-25M, a comprehensive, large-scale multimodal dataset for medicine, covering over 25 million images across 10 modalities, with multigranular annotations for more than 65 diseases. These enriched annotations encompass both global textual information, such as disease/lesion type, modality, region-specific descriptions, and inter-regional relationships, as well as detailed local annotations for regions of interest (ROIs), including bounding boxes, segmentation masks. Unlike existing approach which is limited by the availability of image-text pairs, we have developed the first automated pipeline that scales up multimodal data by generating multigranular visual and texual annotations (in the form of image-ROI-description triplets) without the need for any paired text descriptions. Specifically, data from over 90 different sources have been collected, preprocessed, and grounded using domain-specific expert models to identify ROIs related to abnormal regions. 
We then build a comprehensive knowledge base and prompt multimodal large language models to perform retrieval-augmented generation with the identified ROIs as guidance, resulting in multigranular texual descriptions. 
Compared to existing datasets, MedTrinity-25M provides the most enriched annotations, supporting a comprehensive range of multimodal tasks such as captioning and report generation, as well as vision-centric tasks like classification and segmentation.
Pretraining on \datasetnamefull, our model achieves state-of-the-art performance on VQA-RAD and PathVQA, surpassing both multimodal large language models and other representative SoTA approaches.
This dataset can also be utilized to support large-scale pre-training of multimodal medical AI models, contributing to the development of future foundation models in the medical domain.
The dataset is publicly available at~\url{https://yunfeixie233.io/MedTrinity-25M/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces MedTrinity-25M, a comprehensive and large-scale multimodal dataset for medicine, covering over 25 million images across 10 modalities with detailed annotations for more than 65 diseases. The dataset provides the most enriched annotations for various multimodal tasks, such as captioning, classification, and segmentation, and supports the pre-training of advanced multimodal medical AI models, achieving state-of-the-art performance.

### Strengths
1.	The paper introduces MedTrinity-25M, the largest multimodal medical dataset to date, featuring multigranular annotations and containing over 25 million triplets (image-ROI-description). The development of an automated data annotation pipeline significantly scales up medical image-text data.
2.	With the support of MedTrinity-25M, the pretrained CLIP and LLaVA models demonstrate better performance compared to previous methods.
3.	The release of this dataset contributes to the medical AI community, providing researchers and practitioners with a valuable resource for advancing multimodal tasks and improving healthcare applications.

### Weaknesses
1.  The quality of the generated image-text data may not be sufficiently high. It is advisable to review the questions associated with this data. In the image-captioning constructed from MedTrinity-25M, we found that many basic imaging modalities were incorrectly identified. For instance, in the CT-RATE data used as the source, over 60,000 images were misidentified as MRI, more than 90,000 as X-ray, and even a small number were identified as endoscopy. Below, we provide some captions to illustrate this phenomenon present in MedTrinity-25M.
"""
{"image_path":"seg_train_126_a_2-right lung.nii-34.jpg","id":"b573995e-2d11-11ef-bbea-f02f74942466","caption":"The image is a magnetic resonance imaging (MRI) scan of the thoracic region, showing the heart, part of the lung, and the spine. The heart is centrally located with the lung on either side and the spine running vertically in the background. The region of interest, located in the left-center at the bottom of the image, appears to have a different texture and intensity compared to the surrounding tissue, suggesting a possible abnormality. This region's relative position is towards the lower left side of the image, adjacent to the lower part of the lung. The content within this region may indicate a disease process, which could be related to or affecting the adjacent lung tissue. Given the proximity to the lung, it is possible that the abnormality could be influencing or being influenced by the pulmonary structures.","source":"ct_rate"}
{"image_path":"seg_train_126_a_2-right lung.nii-11.jpg","id":"b57345c6-2d11-11ef-a899-f02f74942466","caption":"The image is a magnetic resonance imaging (MRI) scan of the thoracic region, showing the heart, part of the lung, and the spine. The heart is centrally located with the lung on either side and the spine visible posteriorly. The region of interest, located in the lower-middle left-center of the image, shows an area with altered signal intensity, which is indicative of a pathological condition. This area is situated within the lung tissue and is characterized by a texture and signal intensity that differ from the surrounding healthy lung tissue, suggesting the presence of a disease process such as consolidation, infection, or a mass.\n\nThe region of interest may be related to the surrounding lung tissue in that it could represent a localized disease process affecting the lung, potentially leading to or resulting from changes in the adjacent lung parenchyma. Given the nature of MRI imaging and the appearance of the region, it is possible that this area could be associated with a process such as inflammation, demyelination, or a neoplastic growth, which may have implications for the function of the adjacent lung tissue.","source":"ct_rate"}
{"image_path":"seg_train_14684_a_1-covid-19 infection.nii-76.jpg","id":"a77ee972-2d78-11ef-bdc4-f02f74942576","caption":"The image is a radiographic scan, likely a chest X-ray, showing the thoracic region with the trachea and main bronchi appearing open, indicating no occlusive pathology. The lungs exhibit minimal emphysematous changes, and there are pleuroparenchymal sequelae changes at the apex of both lungs. Additionally, there are linear atelectasis in the middle lobe of the right lung and the lingular segment of the left lung upper lobe. The heart contour and size are normal, and there are no pleural or pericardial effusions. The mediastinal structures are not optimally evaluated due to the absence of contrast material, and the mediastinal main vascular structures are of normal width. No enlarged lymph nodes or pathological wall thickness increase are observed in the esophagus. The thoracic vertebral corpus shows normal heights, alignment, and densities, with osteophytes at the vertebral corpus corners, and the neural foramina are open.\n\nThe region of interest, located centrally and in the upper-middle area of the image, occupying approximately 0.3% of the area, corresponds to the lung apices where pleuroparenchymal sequelae changes are noted. These changes are characterized by alterations in lung parenchyma texture, which may appear as irregularities or areas of increased density compared to the surrounding lung tissue.\n\nThe pleuroparenchymal sequelae changes in the lung apices may be related to the emphysematous changes in the lungs, as both conditions can result from chronic inflammatory processes, suggesting a possible pathophysiological connection between the two findings.","source":"ct_rate"}
{"image_path":"seg_train_9381_a_2-covid-19 infection.nii-145.jpg","id":"9880af92-2c1e-11ef-b9dd-f02f74942466","caption":"The image is a chest X-ray showing a cross-sectional view of the thoracic cavity, including the lungs, heart, and part of the spine. A region of interest is located at the periphery of the thoracic cavity, likely within the lung tissue, which appears as a darker area compared to the surrounding lung parenchyma. The region of interest, which is abnormal, shows an area of increased opacity that suggests the presence of a pathological condition, possibly a mass or lesion within the lung tissue. This abnormal area is indicative of a disease process, which could be related to the surrounding lung tissue either as a primary pathology or as a secondary effect of a systemic condition affecting the lung. The abnormality's proximity to other structures within the thoracic cavity, such as the pleura or lung tissue could imply a relationship where the disease process in the region of interest may have originated from or is affecting adjacent areas, potentially impacting nearby structures due to its location within the thoracic cavity.","source":"ct_rate"}
{"image_path":"seg_train_7973_a_1-right lung.nii-84.jpg","id":"88af61aa-2d11-11ef-959e-f02f74942466","caption":"The image is a sagittal section of an endoscopic view of the thoracic region, showing the spine, part of the lung, and the surrounding thoracic structures. A region of interest is located at the lower-middle part of the image, horizontally left-center, occupying approximately 0.6% of the area. The region of interest, located in the lower-middle left-center of the image, displays an abnormality in the lung tissue, which appears to be a small, localized area with a different texture and possibly altered density compared to the surrounding lung parenchyma, suggesting a pathological change. This abnormality could be related to the adjacent lung tissue, potentially indicating a localized disease process or lesion that may be affecting or resulting from the surrounding lung tissue, given the proximity and the nature of the disease knowledge provided.","source":"ct_rate"}
"""
Moreover, there are also issues with modality misidentification in the image-captioning derived from the quilt-1m dataset. For example, pathology images were misidentified as X-ray and MRI, as follow, 
"""
{"image_path":"G-tdJ0oZxJ4_image_e74e3372-a40e-40e3-ac06-e3d53eeab845.jpg","id":"f5ce616b-89ca-41f6-b820-b480bb3327af","caption":"The image is a magnetic resonance imaging (MRI) scan of the lung, showing a cross-sectional view of the thoracic cavity. A region of interest is located at the top of the image, which appears to be in the upper part of the lung field, likely within the upper lobe, given the position of the lung's anatomy. The region of interest, which is abnormal, exhibits an unusual appearance compared to the surrounding lung tissue, possibly indicating a neoplastic process. This abnormality is characterized by a difference in texture and density, which may suggest a pathological change, such as a mass or lesion within the lung tissue. The affected area's relationship to the rest of the lung tissue could imply a localized pathological process that may be the primary site of the disease, potentially impacting or being impacted by adjacent lung structures due to its proximity to other regions, although the exact relationship depends on the nature of the pathology and its progression.","source":"quilt_1m"}
{"image_path":"895313503048712192_0.jpg","id":"0b53a8c8-5661-449a-b39a-f92887fceb86","caption":"The image is a magnetic resonance imaging (MRI) scan of the brain, showing a cross-sectional view that includes brain tissue with various shades of gray indicating different structures and densities. A region of interest is located at left-center part of the image, which appears to be in the cerebral hemisphere, likely within the white matter of the brain. The region of interest exhibits an abnormality that differs in texture and possibly size from the surrounding brain tissue, suggesting the presence of a pathological change. This abnormal area could be related to the surrounding brain structures, potentially affecting or being affected by them due to its proximity and the nature of brain tissue, which may indicate a pathological process such as a tumor, edema, or other brain abnormalities. The abnormality's characteristics, such as altered signal intensity, could be indicative of the disease process affecting the brain tissue's function or structure.","source":"quilt_1m"} 
{"image_path":"962043872649011205_0.jpg","id":"f94e8ba4-7ddf-450e-9616-d4681e9dcf02","caption":"The image is a chest X-ray image of a 15-year-old boy's hand, showing the left side of the image is a chest X-ray showing the hand's anatomy, including the bones of the hand, with the focus on the epiphysis and possibly the bones of the hand's proximal and distal parts such as the clavicles, ribs, clavicles, and parts of the spine, which are essential for various activities like running, throwing, and punching, along with the presence of the epiphyseal plate and the development of the trapezius, which are crucial for a 15-year-old boy's hand, suggesting a focus on the skeletal structure and function of the hand, including the development of the hand's bones such as the clavicles and the development of the wrist bones, which are crucial for various activities like walking, running, and running, as well as the development of the wrist bones of the hand, which are essential for a growing hand and are indicative of a developing hand and are crucial for a growing hand and are typically found in activities such as playing with play and sports, suggesting a comprehensive evaluation of the hand's anatomy and function.","source":"quilt_1m"}
{"image_path":"1301506707483439105_1.jpg","id":"7b0161c9-1451-4f27-9278-aff87726bacb","caption":"The image is a lateral chest X-ray image of a 15-year-old boy's hand, showcasing the epiphysis of the wrist bones, which are the bones of the hand, including the radius of the wrist bones, clavicles and the bones of the hand's growth plate are visible, such as the clavicles, ribs, and vertebrae are the primary focus of the image is a close-up view of a lateral chest X-ray image, showcasing the epiphysis of the hand's anatomy, which are essential for various stages of development and growth patterns. The image is a detailed X-ray of the hand's anatomy, displaying the epiphyseal growth plate and development of the wrist bones of a 15-year-old boy's hand, with the bones of the epiphyseal plate visible in the image are the primary organ of interest, which includes the epiphyseal plate and epiphyseal plate, as well as the epiphyseal plate's development is crucial for diagnosing the stage of developmental stage of the wrist bones, typically found in the wrist bones of a 15-year-old boy's hand, which is crucial for understanding the zone of developmental development, and the image is likely to be a lateral chest X-ray image showing the epiphyseal plate's development is crucial for diagnosing the stage of developmental stage of the wrist, with the epiphyseal plate being the primary focus of the image.","source":"quilt_1m"}.
2.	The experiments lack comprehensiveness. The comparison of multimodal large models is limited to VQA-RAD, SLAKE, and PathVQA. A broader range of specialized benchmarks, such as the health subset of MMMU, could provide a more robust comparison of the multimodal large models’ performance.

### Questions
1.	The data construction pipeline consists of two main steps: first, generating 200,000 multigranular textual descriptions via GPT-4V, and then fine-tuning LLaVA with this dataset. In my opinion, the performance of the trained model LLaVA-MedCap is significantly influenced by the quality of the data generated by GPT-4V. However, in Table 3, GPT-4V's performance falls far short of LLaVA-Tri. Why did you choose to use GPT-4V to generate the supervised fine-tuning data for the fine-tuning process? In my recent review of the publicly released MedTrinity-25M data, I found that many of the generated data instances were of average quality, with even simple modalities being incorrect.
2.	In Section 4.1, it is stated that “The model is fine-tuned for three epochs on each VQA dataset and evaluated accordingly.” However, this evaluation setup is not fair when comparing with the methods presented in the table. Some results in Table 3 appear to be directly extracted from llava-med’s table, but these methods were not fine-tuned on the training set of the VQA benchmark. In contrast, the accuracy of the chosen llava-med method was achieved after fine-tuning for 15 epochs on the corresponding VQA benchmark training set, making this comparison inappropriate.
Currently, the evaluation paradigm for multimodal large models (MLLM) typically involves assessing the model directly on multiple benchmarks after two stages of pretraining and supervised fine-tuning. Therefore, I suggested distinguishing the results presented: there should be a comparison of the results not fine-tuned on the corresponding training set against the models that were not fine-tuned. Additionally, when comparing with methods fine-tuned on the corresponding training set, the number of fine-tuning epochs (including for the comparison methods) should be clearly indicated. If possible, please also conduct an ablation study regarding the number of fine-tuning epochs.
3.	In Table 3, comparing CLIP-like models with LLaVA, a multimodal large model, seems inappropriate. It would be better to categorize them into two groups: one for CLIP models and another for MLLM.
4.	The evaluation details in Table 3&4 are not clearly explained. What do "open" and "close" specifically refer to?  Please add a brief explanation of the "open" and "close" terms in the table caption or in the text describing the results.

### Soundness
2

### Presentation
2

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
The paper presents MedTrinity-25M, a large-scale multimodal medical dataset with 25 million images across 10 modalities and detailed annotations for over 65 diseases. Enhanced by automated multigranular annotations, it supports tasks like image captioning and report generation. The LLaVA-Tri model, pre-trained on MedTrinity-25M, achieved state-of-the-art results on multiple medical VQA benchmarks.

### Strengths
1. The dataset uses an automated process with medical knowledge retrieval and domain-specific models, greatly reducing manual labeling needs.
2. With over 25 million image-ROI-description triplets, the dataset supports classification, segmentation, report generation, and spans multiple medical domains.
3. The LLaVA-Tri model, pre-trained on MedTrinity-25M, performs exceptionally well across multiple benchmarks, showcasing the dataset’s potential to enhance medical AI applications.

### Weaknesses
 1. Although the labeling process is automated, its reliance on domain-specific models may limit scalability when handling new modalities or emerging diseases. The use of specialized models, while potentially offering higher accuracy for known domains, introduces a bottleneck for adapting to novel image types or pathologies. This is particularly concerning given the rapid pace of medical imaging advancements and the emergence of new diseases.
2. The accuracy of automated labeling may fall short of expert-labeled datasets, potentially impacting performance in critical medical applications. How can a high standard of automated labeling be ensured? The automated process, while efficient, may introduce inaccuracies or inconsistencies in annotations, especially in complex or ambiguous cases. This could lead to a dataset that, while large, is not as reliable as one curated by human experts, potentially limiting its use in high-stakes medical scenarios.
3. With data from over 30 sources, potential biases in image quality, demographics, or disease distribution call for a deeper integration analysis. The heterogeneity of the data sources could introduce significant biases that are not easily detectable. Variations in image acquisition protocols, patient demographics, and the prevalence of certain diseases across different sources could skew the dataset and limit the generalizability of models trained on it. A thorough analysis of these potential biases is crucial.
4. Performance depends on external medical knowledge bases, risking inconsistency if not updated, and the LLaVA-Tri comparison may be biased due to overlap with MedTrinity-25M's data sources. The reliance on external knowledge bases introduces a dependency that could lead to inconsistencies if the knowledge bases are not regularly updated or if there are discrepancies between different sources. Furthermore, the possibility of data leakage between the training set and the evaluation benchmarks, especially given the large number of data sources, raises concerns about the validity of the reported performance.

### Questions
1. Given the reliance on automated processes and external knowledge sources, how is labeling consistency ensured in the data generation process? Additionally, has it been validated by human experts?
2. Has a comparison with expert-labeled datasets been considered to further quantify the quality of automated labeling?
3. How does the dataset address potential biases in source data? For example, is there a mechanism to prevent overrepresentation of certain demographics?
4. What is the expandability of the labeling process for new, unrepresented modalities or diseases? Does it offer strong scalability?
5. Although LLaVA-Tri achieved good performance on RAD, PathVQA, and SLAKE, how do the authors ensure that MedTrinity-25M does not contain data from these datasets? If these datasets were included, the model may have seen the questions and answers during training, leading to artificially high accuracy.

### Soundness
3

### Presentation
3

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
This paper presents MedTrinity-25M, a large-scale multimodal medical dataset comprising over 25 million images across 10 imaging modalities with fine-grained annotations for more than 65 diseases. MedTrinity-25M is developed through an automated pipeline introduced by the authors. Leveraging this dataset, the authors pre-train a vision-language model, named LLaVA-Tri, which achieves superior performance on three MedVQA benchmarks compared to other vision-language models.

### Strengths
1.	The proposed MedTrinity-25M dataset is the largest multimodal medical dataset to date, substantially increasing the scale of accessible training data for medical vision-language tasks.
2.	MedTrinity-25M includes structured, multigranular annotations for each image, offering a level of detail superior to other medical vision-language datasets.

### Weaknesses
1.	The multigranular text descriptions in MedTrinity-25M are generated by the proposed automated pipeline, raising concerns about the accuracy of the generated text. As indicated in Table 2, an expert-based evaluation of 200 random samples resulted in an accuracy score of 85%.
2.	Several key details regarding the automated pipeline remain insufficiently discussed. Specific questions are listed under “Questions”.
3.	The pre-trained model LLaVA-Tri is evaluated solely on the MedVQA task alongside other vision-language models, overlooking its potential application to other important medical vision-language tasks, such as visual report generation.

### Questions
1.	In the initial step of data processing (coarse caption generation via metadata integration), what approach is taken if the metadata lacks organ or disease labels?
2.	Section 3.2.2 states that all textual descriptions in MedTrinity-25M are generated using LLaVA-Medcap, a model fine-tuned on data generated by GPT-4V and the proposed pipeline. Why was GPT-4V specifically chosen? As shown in Table 3, several other medical VLMs, such as the VL Encoder-Decoder and LLaVA-Med, appear to perform better than GPT-4V.
3.	For images without bounding boxes or masks from the original data source, how does the pipeline generate the ROI using expert models? Is ROI generation based on organ or disease labels, and how accurate are the generated ROIs? Additionally, if an image contains multiple ROI regions, how is this managed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces MedTrinity-25M, a large-scale multimodal medical dataset comprising over 25 million images across 10 imaging modalities and covering more than 65 diseases. The dataset features multigranular annotations that include both global information and local information. The authors develop an automated pipeline that generates image-ROI-description triplets without the need for paired textual descriptions. This pipeline utilizes domain-specific expert models to identify ROIs and prompts multimodal large language models (MLLMs) to produce detailed annotations through retrieval-augmented generation (RAG).

### Strengths
- Dataset Comprehensiveness: The dataset is exceptionally extensive, encompassing a wide array of imaging modalities, diseases, and anatomical structures. This diversity significantly enhances its comprehensiveness and utility for various medical AI applications.
- Construction Pipeline through Advanced Models: The utilization of domain-specific expert models and multimodal large language models (MLLMs) for annotation substantially enriches the dataset. This approach adds multigranular details that improve the quality and depth of the annotations, making the dataset more valuable for training sophisticated models.

### Weaknesses
 - Limited Applicability for Visual Data without ROIs: The proposed pipeline relies heavily on regions of interest (ROIs) for constructing multimodal data pairs. For visual data that lack explicit ROI annotations, it is unclear how the pipeline can be effectively applied. This limitation may restrict the dataset's usability across the full spectrum of medical images, particularly those where ROI determination is challenging or subjective.
- Impact of Multigranular Information Not Fully Explored: While Tables 3 and 4 validate the effectiveness of the benchmark in general terms, the paper does not specifically assess how the inclusion of multigranular information, such as ROIs, influences the performance of medical MLLMs. Given that ROI is a pivotal component of the dataset, a focused evaluation comparing models trained with and without multigranular information would strengthen the claims about its benefits.
- Insufficient Discussion of Related Benchmarks: The paper lacks a thorough discussion of existing med-MLLM benchmarks that involve multigranular information. Notably, works like "GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI" and "A Spectrum Evaluation Benchmark for Medical Multi-Modal Large Language Models" are not cited or compared against. Including a comparative analysis would provide context and clarify how MedTrinity-25M advances the field relative to existing resources.
- Lack of Evaluation on Multigranular-Specific Tasks: The dataset is primarily used for training and is evaluated only on VQA-RAD, SLAKE, and PathVQA. These evaluations may not fully capture the effectiveness of the dataset's multigranular annotations since they do not specifically target tasks designed to leverage such detailed information. This omission raises questions about the practical benefits of the multigranular data provided.
- Challenges with Unique Medical Image Descriptions in RAG: The Retrieval-Augmented Generation (RAG) technique used for annotation relies on a general medical knowledge base. However, medical images often have unique features and presentations, even within the same disease category. For example, Atelectasis can manifest differently in chest X-rays depending on the affected lobe. The paper does not address how the RAG system accounts for these unique variations when the initial visual datasets typically offer only generic classification labels. This could impact the accuracy and specificity of the generated annotations.

### Questions
- Handling of Visual Data Without ROIs: For medical images that lack explicit ROI annotations, how does your pipeline construct the corresponding multimodal data pairs? Is there a mechanism to generate or infer ROIs in such cases, or is the pipeline limited to images where ROIs are predefined?
- Assessing the Impact of Multigranular Information on Med-MLLMs: Considering that ROIs and multigranular annotations are central to your dataset, have you conducted experiments to evaluate how these features specifically affect the performance of medical MLLMs? Can you provide insights or results that demonstrate the advantages of including multigranular information in model training?
- Comparison with Existing Multigranular Benchmarks: Could you elaborate on how MedTrinity-25M compares with existing benchmarks that involve multigranular information? What distinguishes your dataset from these, and how does it contribute uniquely to the advancement of general medical AI?
- Evaluation on Multigranular-Specific Tasks: Given that the dataset is evaluated only on VQA-RAD, SLAKE, and PathVQA, which may not fully utilize multigranular annotations, do you have plans to test your dataset on tasks specifically designed for multigranular information? How can you demonstrate the effectiveness of your dataset's detailed annotations in improving model performance on such tasks?
- Addressing Unique Medical Image Presentations in RAG: Medical images often present unique and variable features even when categorized under the same disease label. How does your RAG approach handle the specificity and variability of individual medical image descriptions? For instance, with conditions like Atelectasis that can manifest differently in imaging, how does the system ensure that the generated annotations accurately reflect these variations?

### Soundness
3

### Presentation
2

### Contribution
2
