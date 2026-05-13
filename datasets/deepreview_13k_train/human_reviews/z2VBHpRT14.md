# SpaceSet: A Large-scale Realistic Space-based Image Dataset for Space Situational Awareness

- Decision: Reject
- Scores: 6, 5, 5, 10

## Abstract
Space situational awareness (SSA) plays an imperative role in maintaining safe space operations, especially given the increasingly congested space traffic around Earth. Space-based SSA offers a flexible and lightweight solution compared to traditional ground-based SSA. With advanced machine learning approaches, space-based SSA can extract features from high-resolution images in space to detect and track resident space objects (RSOs). However, existing spacecraft image datasets, such as SPARK, fall short of providing realistic camera observations, rendering the derived algorithms unsuitable for real SSA systems. In this research, we introduce SpaceSet, a large-scale realistic space-based image dataset for SSA. We consider accurate space orbit dynamics and a physical camera model with various noise distributions, generating images at the photon level. To extend the available observation window, four overlapping cameras are simulated with a fixed rotation angle. SpaceSet includes images of RSOs observed from $19 km$ to $63,000 km$, captured by a tracker operating in LEO, MEO, and GEO orbits over a period of $5,000$ seconds. Each image has a resolution of $4418 \times 4418$ pixels, providing detailed features for developing advanced SSA approaches. We split the dataset into three subsets: SpaceSet-100, SpaceSet-5000, and SpaceSet-full, catering to various image processing applications. The SpaceSet-full corpus includes a comprehensive data-loader with $781.5GB$ of images and $25.9MB$ of ground truth labels. We also benchmark detection and tracking algorithms on the SpaceSet-100 dataset using a specified splitting method to accelerate the training process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a large-scale realistic space-based image dataset for space situational awareness. The dataset contains 20k images with 673 objects. The paper describes the detailed pipeline of data curation and data annotation. Additionally, the authors construct an object detection and tracking benchmark based on the proposed dataset and provide several baseline results.

### Strengths
1. This paper proposes a new large scale dataset for space situational awareness. Comparing to previous public avaiable dataset available in this filed, the proposed dataset is the first realistic image dataset at the photon level.
2. This paper constructs object detection and tracking benchmark on the proposed dataset, and implemented several baselines methods on the dataset.

### Weaknesses
1. Considering the relatively small number of target objects (673) in the dataset, it is crucial for the authors to perform multiple experimental runs for object tracking tasks to obtain statistical mean values and variances. The authors should ensure that the variation in evaluation metrics across different runs (e.g. 3 or 5 runs) remains below a specified threshold (e.g., 0.5) to establish the reliability and stability of the results. The current single-run results may not be representative of the true performance of the evaluated methods, especially for tracking where randomness in initialization and matching can significantly impact the outcome.
2. Given that object scale is a critical factor influencing detection performance, the authors should provide comprehensive statistical analysis of object scales in the dataset, such as the distribution of object sizes (e.g., small, medium, and large objects). This information should include not only the overall distribution but also the distribution within different object classes (e.g., LEO, MEO, GEO). This detailed analysis is essential for understanding the dataset's challenges and for interpreting the performance of different detection and tracking algorithms. Without this, it is difficult to assess if the reported results are due to the algorithms' capabilities or simply the prevalence of certain object scales.

### Questions
1. Please provide multi-run results with mean and variances on the object detection and object tracking benchmarks to ensure the variances of multiple-runs are small.
2. The authors could include baseline results of specialized small object detection methods, such as approaches [1] that have shown promising performance on the VisDrone [2] benchmark.

[1] QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection.

[2] VisDrone-DET2019: The Vision Meets Drone Object Detection in Image Challenge Results.

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
To improve Space Situational Awareness (SSA), the authors introduced SpaceSet, a comprehensive, large-scale dataset of high-resolution spaced-based images, designed to address the limitations of existing simulated datasets. This datasets consists of images generated with accurate orbital dynamics and a physical camera model with various noise distributions, capturing observations from altitudes between 19 km and 63,000 km. In experimental section, the authors provided the object detection and tracking benchmarks. The benchmark indicates that a series of YOLO-8 can show the better performance in the computational overhead and the accuracy.

### Strengths
First of all, the motivation of the paper seems to be meaningful and pragmatic in the perspective of addressing limitations in the existing dataset. 

SpaceSet contains high-resolution scenes and more RSOs than existing datasets and also contains multi-camera images that consider various physical factors including noise, object properties, camera models, and locations.

To validate its effectiveness as a benchmark for object detection and tracking, the authors selected the most widely used models and conducted meaningful experiments.

### Weaknesses
As a benchmark paper, it lacks many details and analysis on dataset itself. Except for data generation, the information such as the properties of RSOs such as size and orientations, the positional distribution of frequently appearing locations in the images, and criterion for image splits is needed. Furthermore, there is a lack of detail regarding the benchmark experiments such as whether all models used input images of the same size or why do existing SOTA object detection and tracking methods not perform as well as expected on SpaceSet-100?

Another concern is the completeness of the paper. Although the completeness is an essential aspect of a paper, this paper contains awkward sentences, typos (e.g., L.140, 210, obit), grammatical errors (e.g., L.216 box are -> is). Regardless of whether these issues hinder understanding of the content, the lack of attention to such things is problematic.

Lastly, the content in A.5 intended to validate the proposed dataset’s effectiveness in real-world data is not clearly conveyed. It would be beneficial to emphasize in the main paper why these metrics provided in Table.8 and 9 are meaningful.

### Questions
I mentioned all comments including reasons and suggestions in the above sections. I recommend that the author will provide all the concerns, and improve the completeness of the paper. If the rebuttal period resolves the above-mentioned concerns, I will gladly raise my score. Also, there are many vague sentences and grammatical errors in the paper. I recommend that the author will revise the paper.

### Soundness
2

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
3

### Summary
This paper introduces SpaceSet, a large-scale, realistic image dataset designed to enhance space situational awareness (SSA) for tracking and monitoring resident space objects (RSOs). Unlike previous datasets, SpaceSet incorporates accurate orbital dynamics and a physical camera model with photon-level noise distributions to produce realistic space-based images. Simulated from multiple orbital perspectives (LEO, MEO, GEO), the dataset covers distances from 19 km to 63,000 km and provides high-resolution images (4418 × 4418 pixels) suitable for advanced SSA methods. It includes three subsets—SpaceSet-100, SpaceSet-5000, and SpaceSet-full—addressing various image processing needs, along with a benchmark evaluation for detection and tracking algorithms.

### Strengths
The main contribution of this paper is a large-scale, realistic image dataset designed to enhance space situational awareness (SSA) for tracking and monitoring resident space objects (RSOs). The dataset has a few merits compared to existing ones:

+ The proposed dataset incorporates realistic orbital dynamics and a camera model with photon-level noise, enhancing its applicability to real-world SSA tasks.

+ The image resolution in the proposed dataset is high (4418 × 4418 pixels). It covers multiple orbital altitudes (LEO, MEO, GEO) and observation distances (19km to 63,000km)

### Weaknesses
My major concern is the limited contribution. A pure dataset contribution may not align with the topic of the ICLR conference (Learning Representations). This paper benchmarks many existing detection and tracking algorithms on the proposed subset (SpaceSet-100). However, no new algorithms regarding learning representations are provided.

Another concern is the dataset setup. I understand the proposed one is already closer to real settings than previous ones, but it is still a synthetic dataset. I wonder what the gap is between the proposed synthetic and realistic settings. For example, the dataset uses a fixed camera setup, four overlapping cameras, and a fixed rotation angle. Is this always the real application scenario? Will any missions require a different number of cameras with other relative pose settings (e.g., unstructured)?

Is there any available real dataset that could be used to evaluate the quality of the synthetic data or the synthetic-to-real generalization ability of an algorithm?

Some illustrations might be clearer. For example, from Fig.1, I cannot figure out why (a) shows the realistic exposure with noise distribution, how exposure is reflected, what the noise distribution is, and why they are realistic. (b) shows a picture from an existing dataset, SPARK, but there isn't an image of the proposed dataset for comparison. (c) is almost black and I do not know where to put my focus.

### Questions
Plz refer to my comments in "Weakness".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
1

### Summary
Given my limited expertise in the field of space observations, I find myself ill-equipped to provide a comprehensive evaluation of this paper. The specific challenges and nuances within this domain are not within my area of specialization. Therefore, I recommend that you consult with a diverse group of reviewers who possess a deeper understanding of space-related research to ensure a thorough and informed assessment of the paper's content and significance.

### Strengths
Given my limited expertise in the field of space observations, I find myself ill-equipped to provide a comprehensive evaluation of this paper. The specific challenges and nuances within this domain are not within my area of specialization. Therefore, I recommend that you consult with a diverse group of reviewers who possess a deeper understanding of space-related research to ensure a thorough and informed assessment of the paper's content and significance.

### Weaknesses
Given my limited expertise in the field of space observations, I find myself ill-equipped to provide a comprehensive evaluation of this paper. The specific challenges and nuances within this domain are not within my area of specialization. Therefore, I recommend that you consult with a diverse group of reviewers who possess a deeper understanding of space-related research to ensure a thorough and informed assessment of the paper's content and significance.

### Questions
Given my limited expertise in the field of space observations, I find myself ill-equipped to provide a comprehensive evaluation of this paper. The specific challenges and nuances within this domain are not within my area of specialization. Therefore, I recommend that you consult with a diverse group of reviewers who possess a deeper understanding of space-related research to ensure a thorough and informed assessment of the paper's content and significance.

### Soundness
4

### Presentation
4

### Contribution
4
