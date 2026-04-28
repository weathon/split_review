# BoneMet: An Open Large-Scale Multi-Modal Murine Dataset for Breast Tumor Bone Metastasis Diagnosis and Prognosis

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Breast tumor bone metastasis (BTBM) affects women’s health globally, calling for the development of effective solutions for its diagnosis and prognosis. While the deep learning has exhibited impressive capacities across various healthcare domains, their applicability to managing BTBM diseases is consistently hindered by the lack of an open, large-scale, deep learning-ready dataset. As such, we introduce the Bone Metastasis (BoneMet) dataset, the first large-scale, publicly available, high-resolution medical resource specifically targeting BTBM for disease diagnosis, prognosis, and treatment management. It offers over 50 terabytes of multi-modal medical data, including 2D X-ray images, 3D CT scans, and detailed biological data (e.g., medical records and bone quantitative analysis), collected from thousands of mice spanning from 2019 to 2024. Our BoneMet dataset is well-organized into six components, i.e., Rotation-X-Ray, Recon-CT, Seg-CT, Regist-CT, RoI-CT, and MiceMediRec. Thanks to its extensive data samples and our tireless efforts of image processing, organization and data labeling, BoneMet can be readily adopted to build versatile, large-scale AI models for managing BTBM diseases, which have been validated by our extensive experiments via various deep learning solutions. To facilitate its easy access and wide dissemination, we have created the BoneMet package, providing three APIs that enable researchers to (i)flexibly process and download the BoneMet data filtered by specific time frames;and (ii) develop and train large-scale AI models for precise BTBM diagnosis and prognosis. The BoneMet dataset is officially available on Hugging Face Datasets at https://huggingface.co/datasets/BoneMet/BoneMet. The BoneMet package is available on the Python Package Index (PyPI) at https://pypi.org/project/BoneMet. Code and tutorials are available at https://github.com/BoneMet/BoneMet.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript presents a pioneering large-scale, high-resolution multimodal dataset focused on breast tumor bone metastasis. The dataset encompasses over 50 TB of comprehensive resources across multiple modalities, including 2D X-ray imaging, 3D CT scans, and detailed biological data. The authors have implemented robust accessibility measures through PyPI, Huggingface, and GitHub APIs, ensuring broad availability to the research community.

### Strengths
1.	The dataset represents the first over 50 terabytes-scale multimodal data resources
2.	The implementation of multiple standardized APIs ensures seamless accessibility and integration capabilities
3.	The methodology section provides comprehensive documentation of data collection protocols and analytical procedures
4.	The extensive experimental validation demonstrates the dataset's utility for advanced deep learning applications

### Weaknesses
1.	The experimental design exhibits inconsistencies in model selection and parameter settings, potentially impacting comparative analyses, see question 1
2.	Several, but not limited to, technical inaccuracies require attention: "detials" should be "details" on line 454, and "BigThansfer" should be "BigTransfer" in Figure 5
3.	The translational aspects between murine models and human applications require stronger substantiation, particularly given the introduction's emphasis on human breast cancer implications

### Questions
1.	What scientific rationale guided the decision to utilize Swin-base for comparison with ViT, rather than employing ViT with STA for a more direct comparative analysis?
2.	How do the findings from murine breast cancer models specifically inform and advance our understanding of human breast cancer pathophysiology and treatment approaches?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel large-scale dataset (named BoneMet) of Breast tumor bone metastasis for disease diagnosis, prognosis, and treatment management. It consists of six components: Rotational X-Ray Imagery, Reconstructed CT Imagery, Segmented CT Imagery, Registered CT Imagery, Region of Interest CT Imagery, and Mice Medical Records. Besides, the author conducted a series of experiments on the BoneMet dataset by developing various deep learning models to exhibit its applicability and efficiency in managing BTBM disease. The enormous open-source dataset has significant implications for the development of new algorithms in this field beyond doubt.

### Strengths
(1) The motivation of this study is clear and the background is well presented in the manuscript.
The main contribution of this work is to release a large-scale breast tumor bone metastasis dataset BoneMet, for the research community. Upon the subsets of the BoneMet, the researchers are allowed to develop some novel approaches to solve the task of breast tumor bone metastasis diagnosis and prognosis, and thus facilitating the automated analysis for breast tumor bone metastasis.
(2) Apart from the information of the collected dataset, the authors also developed several deep learning models to validate the applicability and efficacy of BoneMet.
(3) Dataset, code and tutorials are made available for free use.

### Weaknesses
(1) The technical contributions of this study are quite marginal, as most of the deep learning models are built upon existing methods.
(2) Some details about the dataset preparation and experiments are missing.
(3) Some settings and analyses in the experiment may not support the objectives.
(4) The quality of the labels, particularly the pixel-wise annotation of the bone, might be questionable.

### Questions
1. Authors describe that Seg-CT and Recon-CT are independent. What is the difference between 3D CT scans in Recon-CT and Seg-CT? What is the meaning of the adjective 'segmented'?
2. Line 341 "Second, we observe a significant training-test accuracy gap of 20.4% with ViT (w/o STA), indicating a pronounced overfitting issue inherent to the ViT architecture."
I think ViT, as a visual backbone network, is less overfitting compared to other structures such as CNN. In addition, is the decrease in accuracy necessarily overfitting?
3. Section 3.1, the purpose and analysis of experiments is confusing. Why comparing two ViT models could demonstrate the applicability of the Rotation-X-Ray dataset to manage BTBM disease? What is the relation between the effectiveness of
STA and the applicability of the Rotation-X-Ray dataset? All subsections 3.2-4 have similar questions.
4. The experiment did not report data partitioning.
5. Table 2 reported metrics on the training and testing data. Is there any evaluation/dev data?
6. The experiment reported many indicator values, but their actual clinical significance has not been evaluated. For example, what are the Precision/Recall/F1-Score/Accuracy of clinical experts on the BTBM diagnosis? Besides, the 3D-GAN, T-VAE, and ST-VAE methods achieve SSIM values of 0.767, 0.817, and 0.860. So, what role can they play in clinical practice?
7. The authors used many existing softwares as the processing tools to generate the sub-datasets of BoneMet. Please provide the corresponding reference and specify whether it is free of charge or not. Also, please accurately explain in which case the datasets are processed by the Seg-API, Regist-API and RoI-API that were developed by the authors.
8. Are Pre-Op and Post-Op refer to pre-operation and post-operation? Please give the full spelling.
9. For RoI-CT, the tibiae ROI is assigned with different pixel values. As shown in Figure 4, for each CT example, is the processed CT image contains the values of 180, 240, 60 and 0 only? If yes, the original CT turns to a segmentation mask instead, and lots of information would be lost.
10. In the whole preparation procedure, it seems that the manual annotation of the organs or tumors is not involved, except for the manual cropping of fibular by  CTAn®. How could we ensure the effectiveness of the existing software?
11. In Table 1, the column "Spatial Resolution" might be accurately filled out as most of them indicate the organs. Please revise it.
12. Some details about the BoneMet dataset are missing. For instance, the number of mice is not introduced. Besides, in Table 1, the images/records are classified into two categories, i.e., positive and negative. Is the label assigned at the slice level or animal level? Besides, we noticed that the numbers of Seg-CT are larger than those of Recon-CT, which makes it confusing, as the Seg-CT is obtained from Recon-CT.
13. I also have concerns about the MiceMediRec dataset. It mainly consists of the medical record and quantitative analysis results of 3D CT images, simulation and mechanical testing. The authors list only a part of the features in Table S2 in the supplementary file. However, all feature should be provided. The off-the-shelf software, such as CTAn®, was used to generate the quantitative parameters, which took about half an hour for each case of animal. In Section 3.3, the multi-modal prognostic assessment model first leveraged the GAN to produce the CT scan of the future point and use the quantitative data in the MiceMediRec dataset as the ground truth label to validate the predicted reaction force values. However, the details about how to obtain the predicted reaction force values are not clear.
14. In my opinion, multi-modal learning might refer to a way to integrate the information of multi-source data to build a model. However, the application in Section 3.3 just used CT data as model input. Please consider revising it.

### Soundness
2

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
This paper introduces BoneMet, the first large-scale, open dataset specifically designed for BTBM research. This dataset offers over 50 terabytes of high-resolution, multi-modal data, including 2D X-rays, 3D CT scans, and comprehensive biological records collected from thousands of mice. Structured into six components, the dataset may be suitable for a range of AI tasks focused on BTBM diagnosis, prognosis, and treatment. The authors also conducted extensive experiments to demonstrate the usability of this dataset. The dataset, APIs for flexible data processing and retrieval, accompanying code, and tutorials are freely available. To some extent, this dataset makes a valuable contribution to this field.

### Strengths
1.This paper presents a large-scale, open dataset for the diagnosis and prognosis of breast tumor bone metastasis (BTBM), with a total volume of over 50 terabytes, encompassing various modalities. To some extent, this dataset makes a valuable contribution to this field.
2.The authors have developed a specialized toolkit for accessing and processing the dataset, facilitating its use for researchers in the field.
3.The authors conducted detailed experiments that demonstrate the usability of this dataset for some tasks related to BTBM diagnosis and prognosis.

### Weaknesses
1.This dataset is derived from mice, and there are certain differences between mouse skeletons and human skeletons. Can models trained on this dataset be effectively transferred to the diagnosis and prognosis of human BTBM? If applicable, how is the performance? If not, what clinical value does this dataset or model hold?
2.The authors do not provide sufficient details regarding the experimental setup, particularly how the data was partitioned. The experiments appear to be internal validations conducted solely within the dataset, with no external validation on other datasets. This raises concerns about the generalization ability of the models trained on this dataset. Therefore, it remains uncertain whether this dataset can be used to build versatile large-scale AI models or foundational models.

### Questions
refer to the weaknesses.

### Soundness
3

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
In this study, the authors integrated a publicly available large-scale Bone Metastasis (BoneMet) dataset with multimodal medical data, including 2D X-ray images, 3D CT scans, and comprehensive biological data. The primary objective of this database is to facilitate the diagnosis, prognosis, and treatment management of bone metastasis associated with breast tumors.

### Strengths
The paper is well-organized and clearly written.

Our collected dataset is open, large-scale, and consists of multi-modal resources including 2D X-ray images, 3D CT scans, and medical records and quantitative analysis.

The author provides a tool on the Python Package Index (PyPI) for assisting researchers and practitioners.

The authors have conducted multiple benchmarks, such as BTBM Diagnosis to exemplify the utilisation of the collated dataset.

### Weaknesses
In the abstract, the author states, “Breast tumor bone metastasis (BTBM) affects women’s health globally, necessitating the development of effective solutions for its diagnosis and prognosis.” However, the dataset collected was derived from mice rather than human patients.

The author should perform a comprehensive comparison between the BoneMet dataset and previously available datasets, including those derived from human subjects, to elucidate the differences and scales involved.

Additionally, the methods employed in each benchmark were limited. The author should justify the selection of the included methods over others.

### Questions
This paper comprises two main components: the dataset and the benchmark. Both sections could benefit from additional details and comparisons.

The authors should evaluate and clarify how the collected data can directly benefit human health. For example, they could discuss the potential for training models on their dataset and subsequently transfer the obtained model to human datasets.

Furthermore, the figures in the manuscript require better organization, as the text is currently too small for effective readability.

### Soundness
2

### Presentation
3

### Contribution
2
