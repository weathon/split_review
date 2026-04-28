# INDOOR-3.6M : A Multi-Modal Image Dataset for Indoor Geolocation

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 5, 3, 3

## Abstract
Indoor image geolocation, the task of determining the location of an indoor scene
based on visual content, presents unique challenges due to the constrained and
repetitive nature of indoor spaces. Current geolocation methods, while advanced
in outdoor contexts, struggle to perform accurately in indoor environments due to
the lack of diverse and representative indoor datasets. To address this gap, we in-
troduce INDOOR-3.6M, a large-scale dataset of geotagged indoor imagery span-
ning various residential, commercial, and public spaces from around the world.
In addition to the dataset, we propose a new sampling methodology to ensure ge-
ographic diversity and balance. We also introduce INDOOR-15K, a benchmark
for evaluating indoor-specific geolocation models. Finally, we demonstrate the
dataset’s utility by finetuning GeoCLIP using our dataset, which shows significant
improvements over the GeoCLIP baseline on our test set and other benchmark test
sets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces INDOOR-3.6M, a large-scale dataset of geotagged indoor imagery for indoor geolocation tasks. Recognizing the limitations of existing geolocation models in indoor environments, the authors propose a new sampling methodology to ensure geographic diversity and balance in their dataset. They also introduce INDOOR-15K, a benchmark dataset specifically designed for evaluating indoor geolocation models. Lastly, they showcase the dataset's utility by introducing IndoorGeoCLIP, a fine-tuned version of the GeoCLIP model, which demonstrates superior performance compared to the baseline GeoCLIP on their test set.

### Strengths
- This paper addresses a relevant gap in image geolocation by creating a dataset specifically for indoor environments. Existing datasets primarily focus on outdoor scenes, making them unsuitable for the unique challenges of indoor geolocation. The creation of the dataset, along with the development of a specialized indoor geolocation benchmark (INDOOR-15K) are novel contributions. 

- The dataset seems carefully curated and includes metadata, such as scene classification and object segmentation, which add to its potential applications. The use of the Places365 ResNet indoor/outdoor image classifier to filter images is good. Further, the effort to mitigate data leakage concerns by selecting images captured after 2017 for the INDOOR-15K benchmark demonstrates a commitment to quality and reliable evaluation.

- The paper is well-written and structured logically, making it easy to understand. The authors clearly articulate the challenges of indoor geolocation and provide a good overview of existing datasets and their limitations. 

- The INDOOR-3.6M dataset has the potential for numerous interesting applications. The most direct is the development and evaluation of more robust and accurate indoor geolocation models. The dataset can also facilitate research in related areas, such as indoor navigation, scene understanding, and place recognition.

### Weaknesses
 - While the paper introduces IndoorGeoCLIP as a specialized model fine-tuned on their dataset, the evaluation is limited. Exploring and comparing the performance of other state-of-the-art geolocation models or techniques on INDOOR-15K would strengthen the analysis. Additionally, the authors could include a more in-depth error analysis to identify the specific challenges posed by indoor geolocation, and what it can be used for, to guide future research.

- The paper primarily focuses on creating and describing the dataset. It lacks a thorough demonstration of the dataset's usefulness beyond the fine-tuning of GeoCLIP. Further experiments and analyses showcasing the dataset's application in tasks like place recognition, or indoor navigation would strengthen the paper significantly.

- The reliance on URLs to online sources for data access could lead to unreliable data availability, where links might become broken over time, limiting the dataset's long-term usability. The authors should consider providing alternative access methods, such as potentially mirroring the links.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces INDOOR-3.6M, a large dataset specifically for indoor image geolocation, addressing the challenges posed by indoor environments that lack the rich landmarks of outdoor spaces. INDOOR-3.6M includes 3.6 million globally diverse, geotagged indoor images, accompanied by metadata for enhanced model training. Alongside this, the authors provide INDOOR-15K, a benchmark dataset for evaluating indoor-specific geolocation models, and propose a sampling strategy to ensure balanced geographic diversity. They also propose a sampling method, which combines population density and land area to ensure balanced geographic representation within the INDOOR-15K benchmark dataset.

### Strengths
- The presentation is well-structured, making the paper clear and easy to understand.
- Unlike other datasets, the proposed dataset is easily accessible and distributable, as demonstrated in the supplementary materials.
- The proposed dataset fills a critical gap in the research community, providing much-needed resources for indoor geolocation tasks.

### Weaknesses
 - In line 231, the paper mentions collecting images from the internet that contain latitude and longitude coordinates. Is there a human review mechanism to ensure the accuracy and reliability of the geographic information in these images? Additionally, even if the images themselves are under a CC license, is there a protocol to blur potential privacy-sensitive information within the images, such as faces, intimate clothing, etc.?
- Could the release of this dataset lead to illegal applications, such as using images (e.g., from social media) to obtain the user locations (even if they don’t want others to know their location), thereby introducing security risks?
- In line 490, the proposed dataset only provides URLs. These URLs may become inaccessible over time, especially for sites where links frequently change, such as booking websites (with some hotels even removing pages). How does the dataset plan to address the potential issue of broken or inaccessible URLs? The MD5 checksum is insufficient to address the issue of data unavailability, as it only verifies the integrity of downloaded images, not their continued existence. The potential for data loss due to link rot is a significant concern for long-term dataset viability and reproducibility.
- Is it reasonable to determine geographic information solely from images? Have experiments been conducted for more complex cases? For example, (1) many hotel chains use standardized decor, so to what extent can images alone reliably confirm the location of, say, the same hotel brand in the U.S. versus China? (2) Different individuals may have distinct decor and layout styles that may be more indicative of personal taste than geographic location. For instance, a Chinese staff working in the U.S. might have a TV studio with a Chinese interior style. To what extent can models accurately recognize the geographic location in such cases?
- The paper lacks a detailed description and explanation of the proposed IndoorGeoCLIP model. Are the authors only fine-tuning the existing GeoCLIP model using their proposed dataset? If so, this contribution might be seen as insufficiently significant and could be considered merely a necessary experiment to support the dataset.
- The experiments seem insufficient. The authors should consider using more existing methods to evaluate the proposed Indoor15K benchmark; currently, Table 3 includes only GeoCLIP, which seems inadequate. Additionally, in Table 3, wouldn’t it be more intuitive to label IndoorGeoCLIP directly as “GeoCLIP (fine-tuning)”?
- I acknowledge the authors’ introduction of an interesting sampling strategy, but they have not demonstrated its advantages through appropriate ablation studies. I also believe this sampling method could be beneficial for other geolocation datasets (both indoor and outdoor), and further verification of its performance and feasibility would be valuable.
- In the supplementary material, the download_images.py code essentially functions as an automated data-scraping script that downloads images through URLs. It raises the question of whether the authors have obtained proper authorization from all websites involved in the dataset to conduct automated data scraping.

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
3

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
This works introduce a new large-scale dataset to train and evaluate the tasks of global locations prediction from images. The train set consist of 3.6M image-text pairs collected from the internet on a global scale. The test set is constructed by sampling the images using the population and the land area of each contry. Finetuning the previous sota, GeoCLIP, on the proposed dataset achieves much better geolocation accuracy on the indoor scenes.

### Strengths
+ This paper propose a new geolocation dataset dedicating for indoor scenes. The evaluation results shows that the previous sota can perform even better on the indoor scenes after finetuning on the proposed dataset.
+ The discussions of many aspects of the geolocation tasks and the challenge of collecting the dataset is comprehensive.

### Weaknesses
The significance is somewhat unclear to me:
- Regarding dataset scale, it's unclear from Table1 that if the proposed dataset provide more indoor data than some of the other much larger scale mixed dataset like YFCC100M.
- The accuracy improvement for indoor geolocation task is limited to the proposed dataset. Can the fine-tuned models achieve better accuracy on the indoor subset of the other datasets?
- What is the accuracy merit by the proposed dataset additional to the existing resource? Say if we train on a combined indoor data from existing datasets (e.g., Im2GPS, YFCC100M, MP-16, Hotels50k), what is the additional accuracy boost by adding the proposed INDOOR-3.6M?

The sampling strategy in Sec.4.1 looks ad-hoc to me:
- The sampling weight of each contry is determine by the weighted sum of it's population and land area. How the final weight (population * 0.3 + area * 0.7) determined? As it listed as one of the main contribution, I expect more insights. Perhaps an analysis of the accuracy on different contries by varying the weighting can show some support for the goal of the sampling.
- The sampling weight seems to assume that the scene visual diversity of the contries are linearly propotion to the population and land area. Is there any support for this assumption? Perhaps some measure using CLIP distance can provide some insight.



### Questions
In Table1, what is the column "Benchmark" actually stand for? Is it saying that if the dataset has a train/test split?

Why the correctness of the city/contry/continent prediction is determined by a distance threshold (Table 2 and 3)?

Scene labels, segmentations, and object detection results are provided by the dataset. What is the purpose of them? Are they serve as some additional conditions for the geolocation task?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel image geolocation dataset tailored for indoor scenes, addressing the limitations of existing datasets and establishing a benchmark for evaluating indoor image geolocation algorithms. Specifically: 
1. The paper presents a dataset that covers a wide variety of indoor scenes and includes rich multimodal metadata, which is expected to advance the field of indoor image geolocation;
2. The paper proposes an innovative sampling method to obtain geographically representative samples from datasets with geographic bias; 
3. The paper provides a standardized evaluation framework for fair assessment and comparison of research progress in indoor geolocation research.

### Strengths
i) The dataset is collected from three different sources, covering a variety of indoor scenes, thus filling the gap in indoor image geolocation datasets and providing rich multimodal information;
ii) A sampling method that integrates population density and land area is proposed to ensure that the distribution of GPS points across regions is geographically representative;
iii) A new benchmark dataset specifically for indoor geolocation is introduced to address the limitation of existing benchmark datasets, which primarily focus on outdoor environments.

### Weaknesses
(1) The contribution of the dataset does not seem particularly prominent, especially regarding the limitations of existing datasets mentioned in the Introduction (such as insufficient diversity, imbalanced distribution, and blurred boundaries between indoor and outdoor environments), which have not been significantly addressed;  
(2) Compared to some of the datasets in Table 1, the proposed dataset does not show a clear advantage in terms of scale.  Additionally,  I would like to know the amount of indoor scene data within mixed-scene datasets (e.g., YFCC100M). It seems feasible to separate indoor and outdoor images in such datasets using image classification methods.
(3) The experiments in Table 3 do not adequately demonstrate the superiority of the proposed dataset for this task. It is recommended to supplement the results by providing the performance of IndoorGeoCLIP on the three datasets listed in Table 2, to further substantiate the advantages of the proposed dataset.

### Questions
1.The paper demonstrates the performance of the IndoorGeoCLIP model on various levels of geolocation tasks (such as street-level, city-level, and country-level), but it lacks comparative experiments with other classic indoor geolocation methods, making it difficult to comprehensively validate the superiority of IndoorGeoCLIP.  Explicitly, 
i) Lack of Baseline Model Comparisons: Apart from GeoCLIP, the experiments lack comparisons with other geolocation models, making it insufficient to illustrate the relative advantages of IndoorGeoCLIP in indoor scenes.
ii ) Insufficient Ablation Studies: The experiments only show the performance changes of the GeoCLIP model before and after fine-tuning, without conducting ablation analyses on the contributions of the dataset's multimodal features (such as textual and visual data) to geolocation.
2. Some of the images lack sufficient clarity.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new dataset for indoor geolocation and proposes a sampling method to obtain a test set. Additionally, it demonstrates the fine-tuning of GeoCLIP on the proposed dataset.

### Strengths
1) Authors focus on a meaningful and niche (relative to large-scale outdoor scenarios) problem.
2) Building datasets is almost always beneficial, especially large-scale datasets.

### Weaknesses
1) The writing of this article needs to be improved, and the logic within each section is somewhat confusing. For example, the turn on L49 is not rigorous and only shows that you know little about the datasets for other tasks.
2) The article lacks citations for many key statements.
L41: such as seasonal changes, time of day, weather conditions, and human-induced modifications.
3) As I said in the “Strengths”, indoor geolocation (localization) is a meaningful research topic. However, the author lacks a rigorous literature review. I can name many famous indoor localization datasets without thinking: Baidu Mall(CVPR'17), InLoc(CVPR'18), NL-Indoor(CVPR'21). (Although the task objectives of these datasets are different from yours, I think they should be discussed.)
4) The experiments based on the proposed dataset are very limited and do not demonstrate the significance of the dataset.
5) Although you crawled the text descriptions of images, the word "multimodal" in the title is hardly seen again in the paper.

### Questions
None.

### Soundness
2

### Presentation
1

### Contribution
3
