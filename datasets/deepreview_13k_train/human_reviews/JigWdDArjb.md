# SAR2Earth: A SAR-to-EO Translation Dataset for Remote Sensing Applications

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
Electro-optical (EO) images are essential to a wide range of remote sensing applications. With the advent of data-driven models, the efficiency of EO image analysis has significantly improved, enabling faster and more effective outcomes in these applications. However, EO images have inherent limitations—they cannot penetrate cloud cover and are unable to capture imagery at night. To overcome these challenges, synthetic aperture radar (SAR) images are employed, as they can operate effectively regardless of weather conditions or time of day. Despite this advantage, SAR images come with their own difficulties: they are affected by speckle noise, complicating analysis, and existing algorithms developed for EO imagery are not directly transferable to SAR data. To address these issues, we introduce SAR2Earth, a benchmark dataset specifically designed for SAR-to-EO translation. By translating SAR images into EO-like representations, SAR2Earth allows the extensive range of algorithms developed for EO imagery to be applied effectively to SAR data. The dataset consists of 18 spatially aligned pairs of SAR and EO images, collected from 8 distinct regions encompassing both urban and rural. We provide comprehensive evaluations, detailed model analyses, and extensive experimental results. All codes and datasets will be made publicly available at https://sar2earth.github.io.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel public benchmark dataset called SAR2Earth which designed for SAR-to-EO translation. Both EO and SAR images have inherent limitations: EO images cannot penetrate cloud cover and capture imagery at night; SAR images are affected by speckle noise and complicating analysis. Meanwhile, existing large foundation models and generalization models trained on EO images do not perform effectively on SAR images. As a result, SAR-to-EO translation methods have been proposed to mind this gap. This paper proposes SAR2Earth dataset with co-registered SAR and EO images, which aims to support further research for SAR-to-EO translation. The intuition is the limitation of available SAR-to-EO datasets. 
The authors propose a SAR-to-EO pipeline and test the SAR2Earth dataset on various image-to-image translation methods with different preprocessing and postprocessing techniques. The experimental results demonstrate the potential value of this benchmark.

### Strengths
•	This paper proposes a comprehensive benchmark dataset called SAR2Earth for SAR-to-EO translation. The SAE2Earth dataset is collected from 8 regions, with rural/urban domains, a wide range of temporal shifts from 1-month to 5-year, and high resolution images ranging from 0.15m to 0.6m.
•	To evaluate the performance of the dataset, this paper proposed a SAR-to-EO pipeline that integrates previous research and provided benchmark results on state-of-the-art image-to-image translation models.
•	The experimental results are comprehensive, detailed, and promising. The proposed public benchmark dataset can support future research in this domain.

### Weaknesses
•	The dataset description lacks specific details like the number of images in the dataset and recommended dataset splits.
•	Compared with section 5, the SAR-to-EO pipeline in section 4 occupies only a small portion of the paper and lacks adequate explanation.
•	As the authors point out, this work did not leverage extra modalities, like OSM-based label maps or metadata. These extra information can provide better understanding for regional characteristics in SAR-to-EO translation.

### Questions
•	Can you provide more information about the SAR2Earth dataset? E.g. a comparison of the number of images with previous datasets.
•	Can you provide more detail in section 4, e.g. a detailed flow chart? This may provide readers with a comprehensive understanding of the pipeline.

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
5

### Summary
This paper introduces SAR2Earth, a deep learning benchmark dataset for SAR to optical translation. It verifies the application of this dataset through various methods and perspectives. The content is comprehensive, and both data and code are openly shared.

### Strengths
This paper constructs a high-resolution (<1m) SAR to optical translation dataset, covering both rural and urban scenes, including large-scale areas—a first in this field. The quality of the data and methods is commendable, with detailed data processing and sufficient experimental comparison. The introduction is clear, outlining the significance of the dataset, the construction process, and various factors influencing SAR to optical translation. This dataset holds significant potential in the SAR to optical translation domain.

### Weaknesses
Although the paper presents a valuable dataset, several shortcomings remain:
1.	The connection between the background introduction and experimental results lacks coherence. The significance of SAR to optical translation is highlighted as solving cloud and fog issues, but the experiments fail to substantiate this claim. While the GeoChat analysis and SAM segmentation results are novel, the GeoChat testing method is questionable and too qualitative. Conversely, the OSM experiment or surface segmentation, which could better demonstrate the conversion's significance, is not included. The experiments should focus on demonstrating the utility of SAR to optical translation in scenarios where optical data is limited due to weather conditions, which is a key motivation for this task. The current experiments do not adequately address this core application.
2.	The dataset review is not comprehensive, and its positioning is unclear. Since 2018, SAR to optical translation has seen significant advancements with many global datasets such as SEN12MS dataset for Sentinel-2, Planet-CR dataset for Planet, and SMILE dataset for Landsat. These were not mentioned. The main contribution of this dataset lies in its sub-meter resolution, which previous global datasets do not offer, enhancing urban (built-up) scene accuracy. The paper needs to explicitly highlight how the sub-meter resolution of this dataset addresses the limitations of existing medium-resolution datasets, particularly in urban environments, and how this impacts the performance of translation models.
3.	The experimental discussion is not sufficiently in-depth. The paper discusses speckle noise but does not address the alignment issues with increased resolution using WGS84. The impact of these alignment errors and their solutions should be discussed, which is not encountered in lower-resolution datasets. Specifically, the paper should investigate the impact of sub-pixel misalignments between the SAR and optical images due to the increased resolution and discuss how these misalignments affect the training and performance of the translation models. Furthermore, the paper should explore methods to mitigate these alignment errors, such as using more sophisticated co-registration techniques beyond simple WGS84 transformations.

### Questions
1.	The title mentions datasets and remote sensing applications, yet experimental applications are not clearly reflected. GeoChat and SAM are not true applications. SAR to optical conversion's main significance lies in interpreting scenes in complex weather, which is only mentioned in the background but not experimentally demonstrated.
2.	The dataset review is not comprehensive, and its positioning is unclear. What are the differences and advantages between your dataset and those medium-resolution global datasets?
3.	Is there a better way to deal with the errors of SAR and optical registration, not just WGS84 registration?
4.	Many existing models are compared in the experiments. Can these models handle noise directly within the network without pre-processing before model training?
5.	The time span between SAR and optical data is lengthy, sometimes exceeding a year. How can this limitation be narrowed? Seasonal differences and surface changes may affect the translation model's accuracy. How can this be mitigated?
6.	Can the model trained on this dataset be directly applied in specific scenarios, or how far is SAR to optical translation from real-world application? Which specific scenarios would benefit most?
7.	GeoChat verification seems biased towards optical images. Would describing SAR images show similar biases?
8.	The migration accuracy for urban and rural scenes is low. Does this issue extend to other scenes? Can dataset expansion and method changes address this?

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
This paper introduces SAR2Earth, a benchmark dataset designed for the translation of synthetic aperture radar (SAR) images into electro-optical (EO) image representations. This dataset addresses the limitations of EO images, which cannot penetrate cloud cover or capture nighttime imagery, by leveraging the all-weather and day-night capabilities of SAR images.

### Strengths
1. This article has strong practical applications and provides a broad platform for future research.
2. Their dataset have considered realistic conditions for practical applications.
3. This paper have provided extensive ablation studies from pre-processing to post-processing techniques.

### Weaknesses
1. As a paper introducing a new dataset, this article provides too few qualitative results.
2. The number of images in the proposed dataset remains unknown, and details such as image numbers, the size of the training and test set are not disclosed.
3. The applications demonstrated in this paper are limited in section 5.6.

### Questions
1. How to ensure the accuracy of the co-registration of SAR and EO? 
2. Why not compared diffusion-based approaches for SAR-to-EO translation? These methods are widely used (Line 134).
3. For SAR-to-EO pipeline proposed in this paper, how can the authenticity of the synthetic EO images be ensured, considering that generative models may introduce artifacts? If the model generates false features, how should they be handled?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Electro-optical (EO) satellite images are used in many important applications of machine learning. But the Earth's surface can be blocked by cloud coverage and is not viewable at night. Synthetic aperture radar (SAR) do not have these two limitations. This paper introduces SAR2Earth, a dataset for SAR-to-EO image translation. It consists of 18 spatially registered pairs of SAR and EO images from 8 different regions. This paper also benchmarks image-to-image translation methods (introduced for natural imagery) on SAR2Earth, showing that the CUT method performs best. This paper qualitatively shows that EO foundation model predictions improve by translating a SAR image to an EO image, then providing the foundation model with this synthetic EO image — compared to directly providing the SAR image.

### Strengths
The paper is well written and presented. Remote sensing is an important application area of ML. The introduced dataset — named SAR2Earth — is valuable to the remote sensing community, as it contains high-resolution SAR-EO pairs sampled from diverse regions and temporal differences. Running many baseline methods on SAR2Earth is a valuable contribution. The examples using SAR to EO translation to create synthetic EO images which are fed to foundation models is also a valuable contribution — and it shows that this research direction complements broader trends in ML.

### Weaknesses
My main concern is that I do not believe this paper is valuable to share with the broader ICLR community. I believe it is more suited to RS-specific journals or workshops. The most similar work to this, that I am ware of, is a CVPR 2024 workshop paper by Low et al., that is cited. SAR2Earth seems to have more regional diversity and this paper performs more extensive (and valuable) experiments. As far as I can tell, Low et al. provide far more SAR-EO pairs than this submission.

Other comments:
- It is hard to tell what the MAE / MSE/ PSNR metrics imply for a remote sensing practitioner. For example, are synthetic images with an MAE of 0.1 still useful? One potential experiment is to find a dataset with SAR-EO pairs, like BigEarthNet or EuroSat (there is a SAR version available). Then translate the SAR image to EO and try classifying it. The performance drops would be very interesting to me. 
- I cannot find a discussion on RS models that were pretrained to ingest SAR. There are many: Presto, CROMA, DOFA, SoftCon, DeCur, etc. If we have foundation models that can ingest SAR, wouldn't it be better to directly provide the SAR image, rather than a synthetic EO image that requires a SAR-to-EO translator?

### Questions
It seems like this dataset only contains 18 SAR-EO pairs, can you confirm this is the case? If so, what is the bottleneck to scale your collection pipeline up to many thousands of pairs?

Please also see questions in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
1
