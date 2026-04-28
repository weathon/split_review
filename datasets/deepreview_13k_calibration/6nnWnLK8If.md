# Dataset for Image-based Analysis of Mineral Fertilizer Granules

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
In the context of the mineral fertilizer industry, a crucial sector for global food production, which faces challenges in production efficiency and fast quality control, this work introduces the Mineral Fertilizer Dataset (MFD), a novel annotated segmentation dataset comprising 1,608 images and 125,648 instances of various fertilizer granules with different colors. Addressing the lack of datasets in this field, the MFD supports both semantic and instance segmentation tasks, with segmentation masks that facilitate the computation of the equivalent area diameter of granules. Periodic checks of the area equivalent diameter based on customer specifications are essential to prevent potential defects, such as caking and dustiness, in the produced fertilizer granules. Baseline models based on Feature Pyramid Network (FPN), UNet, and MANet were trained for semantic segmentation, while baseline models based on Mask R-CNN, YOLOv8, YOLOv9, and Mask2Former were trained for instance segmentation. Our experiments demonstrate the efficacy of these models, as well as the robustness of the trained models in identifying fertilizer granules of different colors not included in our dataset, fertilizer granules under 365 nm ultraviolet light, as well as other granular objects such as Polyethylene Terephthalate (PET) pellets, corn, beans, and even pharmaceutical tablets. This dataset, along with its benchmark results on existing semantic and instance segmentation algorithms, aims to facilitate further advancements in computer vision applications for quality control in the fertilizer industry and related sectors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents the Mineral Fertilizer Dataset (MFD), created specifically for the segmentation of fertilizer granules. The dataset contains 1,608 annotated images of four types of mineral fertilizer granules: KCl, NH₄NO₃, DAP, and NPK. The authors assess the performance of classical semantic and instance segmentation techniques using the MFD, highlighting its applicability for fertilizer granule segmentation tasks.

### Strengths
The constructed dataset offers a novel approach to evaluating the quality of mineral fertilizer products. The granule annotation process is both logical and compelling. The benchmark results can provide good guidance to researchers in the related fields.

### Weaknesses
While the paper provides a benchmark evaluation of several classical semantic and instance segmentation techniques on the MFD, it lacks a significant technical contribution to the field. Given the unique features of the dataset, the authors could consider proposing a tailored model to achieve better segmentation performance. The current approach uses standard architectures like FPN, Unet, and MANet, without any modifications to leverage the specific characteristics of fertilizer granules, such as their texture, shape, and color variations. A novel architecture or loss function that is specifically designed for this task could have significantly enhanced the paper's contribution.

The authors claim that the MFD dataset is designed for quality control in the fertilizer industry. However, it would be helpful to demonstrate how the segmentation results directly contribute to the quality evaluation process. For example, how do the segmentation metrics (e.g., accuracy, IoU) correlate with key quality control parameters in fertilizer production, such as granule size distribution or shape uniformity? The paper does not provide a clear link between segmentation performance and practical quality control metrics. It is unclear how the segmentation masks are used to derive meaningful quality control parameters like area equivalent diameter, circularity, or aspect ratio, which are crucial for assessing granule quality. Additional explanations are also needed to clarify the displayed experimental results.

The experiments conducted on extended datasets with similar morphological characteristics lack sufficient detail. A detailed table or description specifying the models used to segment beans, seeds, and tablets, along with their corresponding performance metrics, would strengthen the extended experiments. The paper mentions using similar models, but does not provide specific details on the architectures, training parameters, or performance metrics achieved on these datasets. This lack of detail makes it difficult to assess the generalizability of the proposed approach. Furthermore, the paper does not discuss the specific challenges encountered when applying the models to these different datasets, such as variations in lighting, background, or object density.

Although the dataset may be valuable for the fertilizer industry, the paper lacks a clear discussion of novel ideas or distinguishing contributions. It would be beneficial to explicitly state the novel contributions or to draw a more direct comparison between this dataset and approach and existing methods in the fields of industrial quality control or granular material analysis. The paper does not adequately position the MFD dataset within the broader context of existing datasets for granular material analysis or industrial quality control. A more thorough comparison with existing datasets, highlighting the unique aspects of MFD and its potential advantages, would strengthen the paper's contribution.

### Questions
1. The authors state in the Abstract, "our experiments demonstrate ... the robustness of the trained models in identifying fertilizer granules of different colors not included in our dataset." However, this claim is not supported in the experiment section. Which experiment validates this statement? Given that the segmentation networks used are classical ones, like FPN, Unet, and MANet, what exactly do the authors mean by this claim?

2. In Line 85, the authors mention that isolating individual granules from the overall mask makes the method more acceptable for the fertilizer industry. Why would this isolation process improve industry acceptance?

3. What does the x-axis of the Violin plot in Figure 3 represent for each type of fertilizer granule?

4. In Figure 4, why are only a few KCl granules annotated?

5. What is the intended explanation in Lines 262–268?

6. Which models were employed to segment objects with similar morphology, as shown in Figures 9 through 12?

### Soundness
3

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
3

### Summary
The paper introduces the Mineral Fertilizer Dataset (MFD), a novel annotated segmentation dataset designed for image-based analysis of mineral fertilizer granules. Aiming to address the lack of datasets in the fertilizer industry for improving production efficiency and quality control, MFD includes 1,608 images and 125,648 labeled instances, supporting both semantic and instance segmentation. Baseline models were trained on MFD demonstrate strong efficacy and robustness.

### Strengths
1. The Mineral Fertilizer Dataset (MFD) uniquely contributes to the field by explicitly addressing the image-based segmentation of mineral fertilizer granules. This dataset tackles real challenges in the fertilizer industry, where resources for quality control and production efficiency datasets are limited.
2. The paper benchmarks multiple models—FPN, UNet, and MANet for semantic segmentation, and Mask R-CNN, YOLOv8, YOLOv9, and Mask2Former, for instance, segmentation—offering a thorough evaluation across a range of segmentation techniques.
3. The paper provides a detailed overview of the dataset construction process, covering image capture, annotation, and preprocessing steps. It also clearly describes the experimental setup, model selection, and evaluation metrics, ensuring transparency and reproducibility.

### Weaknesses
1. This paper does not include a comparative analysis with prior work in this field or similar fields. It would be beneficial to discuss what datasets have been used in previous studies on fertilizer granules or related domains and how the Mineral Fertilizer Dataset (MFD) compares in terms of uniqueness or advantages.
2. This paper lacks a detailed analysis of the dataset's diversity, specifically regarding whether it covers all common types of fertilizer granules and whether these granule types are representative of real-world production. 
3. The dataset lacks detailed documentation and user instructions. Information such as the composition of each data element, annotation standards, and a clear breakdown of dataset attributes would make the dataset more accessible and manageable for other researchers.
4. While the paper claims that the dataset and models support real-time and robust applications, it does not provide experimental data to substantiate these claims.

### Questions
1. Could the authors provide a comparison between the Mineral Fertilizer Dataset (MFD) and other datasets commonly used in related fields?
2. The paper mentions several types of fertilizer granules but does not specify whether these types cover the full range of granules commonly used in the fertilizer industry. Are there any significant granule types not included in MFD, and if so, how might this affect the dataset’s applicability?
3. Could the authors consider adding a detailed usage guide to help future users better understand and adopt the dataset?
4. Could the authors perform or further discuss tests measuring inference speed across different devices or environments? 
5. Could the authors provide experimental results using the same image resolution for all models?
6. Could the authors clarify the criteria for selecting the specific segmentation models in the benchmark?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a mineral fertilizer segmentation dataset, featuring real-world scenes with particles of various colors. It makes up for the lack of relevant datasets in the fertilizer industry.And it constructs benchmark test results based on some instance segmentation models and semantic segmentation models, which to a certain extent promotes the development of quality control technology in the fertilizer industry.

### Strengths
This paper proposes a mineral fertilizer segmentation dataset, which consists of mineral fertilizer particles of different colors in real scenes, which to a certain extent promotes the development of quality control technology in related industries.

### Weaknesses
1. The article lacks innovation. The author only uses some benchmark models for testing on the constructed dataset and does not propose new methods to test on the dataset. The lack of technological innovation also makes the paper look more like an experimental report.
2. In the introduction, the author did not describe the innovation of this paper in points, which is not intuitive enough. In terms of expression, the author did not explain some specific contents clearly, such as how the "self-developed algorithm" is implemented and what are the specific "some OpenCV operations".

### Questions
1. The technical innovation is extremely limited. This article only uses some benchmark models for testing on the proposed dataset, and does not make any technical optimization for this field. If there is any technical optimization for this field, it is recommended to add relevant content.
2. For the annotation of the dataset, how does the algorithm developed by the author achieve block uniqueness? What does the author mean by some OpenCV (Bradski, 2000) operations in the article?
3. For the evaluation of the dataset, can you provide more model evaluation effects and some additional indicators to more comprehensively evaluate the quality of the dataset?
4. The article is not well organized in terms of language. It uses conjunctions such as first, second, and at last to describe things in one paragraph, which can easily lead people to mistake it for being AI-generated. Please modify the overall expression of the article.
5. This dataset has only four categories. Can it represent most scenarios in this field?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces the Mineral Fertilizer Dataset (MFD), a novel annotated segmentation dataset containing 1,608 images and 125,648 instances of various fertilizer granules with different colors, aimed at supporting semantic and instance segmentation tasks in the mineral fertilizer industry. The authors trained baseline models such as FPN, UNet, MANet for semantic segmentation, and Mask R-CNN, YOLOv8, YOLOv9, and Mask2Former for instance segmentation, demonstrating the dataset's utility and the models' efficacy in identifying fertilizer granules and other granular objects. The contribution lies in providing a benchmark for computer vision applications in quality control for the fertilizer industry and related sectors.

### Strengths
The introduction of the Mineral Fertilizer Dataset (MFD) fills a significant gap in the field by providing a specialized dataset for image-based analysis of fertilizer granules, which was previously lacking.

### Weaknesses
The paper's writing is very catastrophic.
The dataset is not very valuable.

### Questions
refer weakness.

### Soundness
2

### Presentation
1

### Contribution
2
