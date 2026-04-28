# Alberta Wells Dataset: Pinpointing Oil and Gas Wells from Satellite Imagery

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
\setcounter{footnote}{0} 
Millions of abandoned oil and gas wells are scattered across the world, leaching methane into the atmosphere and toxic compounds into the groundwater.
Many of these locations are unknown, preventing the wells from being plugged and their polluting effects averted. Remote sensing is a relatively unexplored tool for pinpointing abandoned wells at scale.
We introduce the first large-scale benchmark dataset\footnote{Dataset available at: \url{https://zenodo.org/records/13743323}} for this problem, leveraging medium-resolution multi-spectral satellite imagery from Planet Labs.
Our curated dataset comprises over 213,000 wells (abandoned, suspended, and active) from Alberta, a region with especially high well density, sourced from the Alberta Energy Regulator and verified by domain experts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To cope with the problem that the huge amount of abandoned  oil and gas wells are unrecorded, the paper presents  the first large-scale remote sensing dataset for pinpointing onshore  oil and gas wells . The paper also gives  object detection and binary segmentation algorithms for evaluation. For better split the dataset, a training/validation/evaluation dataset splitting algorithm is also designed to make the evaluation reasonable. Some benchmark experiments are also provided in detail. Some limitations are analyzed. The paper is well organized.

### Strengths
1. The first large scale  Wells Dataset is introduced for oil and gas well detection.
2. The dataset construction process is well described which makes the dataset reliabe. Besides, a training/validation/evaluation dataset splititng algorithm based on clustering principle is presented. 
3. Evaluation benchmark algorithms are provided to be baseline for the research in this topic.
4. The limitation of the work is explained in detail.

### Weaknesses
1. The area is limited in Alberta, Canada which makes the dataset lose the universality.
2. The resolution scale is only 3 meters resolution because the dataset was acquired from PlanetScope-4-Band imagery.
3. the baseline algorithms don't utilized some physical information about wells.

### Questions
1. What's the relation of segmentation and detection for wells analysis?
2. Why is the splitting principle using the geographical location?

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
This paper contributes a large-scale dataset comprising over 213,000 wells
from Alberta with their status as abandoned, suspended, and active. The ground truth data is collected from the Alberta Energy Regulator (AER), detailing the wells and their geographic locations. However, this data cannot be used directly due to licensing restrictions or the presence of duplicate entries.  To address this issue, the authors applied a data filtering and quality control approach with domain experts. Afterwards, they created a well-distributed dataset representing various geographical regions by applying a clustering algorithm. For satellite data the Planet labs multispectral imagery and also frame the task of identifying wells applying both object detection and segmentation. Ultimately, the authors generated segmentation maps and object detection annotations for all known wells in the images based on the point labels provided in the AER data.

### Strengths
1. The work overall is of standard quality, including a potentially impactful dataset for an important application that may be of significant contribution to the ML community and preliminary experiments testing well-established baselines on the dataset.
2. The authors create a well-distributed dataset by the clustering Algorithm, which is very clear and well-written.
3. The identification task involves both object detection and object segmentation. This process produces segmentation maps and object detection labels for all known wells in the image using the print labels from the AER data.
4. The dataset may be of use to policymakers and other stakeholders involved in climate
action.

### Weaknesses
 ***Major***

1. The actual contribution of the work is not clearly established. The ground truth dataset is taken from AER ST37, where the there all geolocations are available. The dataset contains only that data; no new data is contributed here. The authors do not provide sufficient justification for why this dataset is needed, given the availability of the source data.
2. The model evaluation lacks in-region and out-of-region performance testing, which is a crucial experiment for remote sensing tasks. The current evaluation does not adequately demonstrate the model's ability to generalize to new geographic areas, which is a critical aspect of real-world applicability.
3. The figure quality is very poor, e.g., Figures 3 and 4. The low resolution and clarity of these figures make it difficult to assess the data and results presented.
4. For object detection, only axis-aligned models are used. The author has not implemented recent models or an oriented bounding box (OBB) approach, such as YOLO-OBB or Faster R-CNN with Rotated Bounding Boxes, which could potentially enhance performance. This limits the potential of the object detection component.
5. Paper writing should be improved.


***Minor***

1. The dataset documentation, AWD_Datasheets_for_Dataset.pdf, follows the NeurIPS 2024 format and includes a footnote stating: "Submitted to the 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks. It violates the rules of the conference.

### Questions
1. How can the author address the challenge of applying the model to a new region where ground truth data is unavailable? This is a concern because Table 4 shows low recall in regional performance. When evaluating the trained model on a new region, there is a high risk that many wells may be missed due to potential changes in pixel density. In such cases, how does the author plan to validate the dataset, given that ground truth data is not publicly accessible?
2. What is the unique utility of this dataset, considering that many standard remote sensing datasets, such as DOTA v2, are already available?

### Soundness
2

### Presentation
2

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
The paper presents a dataset for detecting oil and gas wells from satellite imagery in Alberta, Canada. The dataset contains a large volume of PlanetScope (~ 3 m spatial resolution) images (> 90,000) with over 200,000 curated well labels. Using a 2-step clustering approach, the images were split into a training, validation, and test set. The authors report binary segmentation results for several deep learning models including convolutional neural networks and a vision transformer. Additionally, results from object detection models are reported as an alternative approach. Models achieve good performance on both tasks (IoU values > 0.6).

This dataset lists several contributions compared to existing datasets, including its large scale, the use of high-resolution Planet imagery, and the availability of well type (abandoned, suspended, and active) data. However, large scale mainly refers to data volume and not to geographic diversity. Furthermore, the paper does not demonstrate the usefulness of the well type data. These limitations reduce the contribution of the paper compared to existing datasets.

### Strengths
- The paper is well-structured and easy to read.

- The dataset employs high-resolution PlanetScope imagery which benefits from a high temporal resolution (even better than that of Sentinel-2) compared to the VHR Google Earth imagery used by most existing well datasets. Furthermore, its spatial resolution is better than that of Sentinel-2.

- The data volume, in terms of number of images and well counts, is significantly bigger than that of existing datasets.

- The dataset includes information about well type (active, suspended, and abandoned), unlike existing datasets which supposedly predominantly focus on active wells.

### Weaknesses
 - Despite the high data volume, the study area is limited to Alberta, Canada. In comparison, an existing dataset (NEPU-OWOD V3) features sites across China and California, US. In general, I argue that adding more data for a specific region (although I also acknowledge that Alberta is a large region) is less important than including oil and gas wells from a diverse set of geographic locations to test the generalization ability of models. The importance of this (specifically the robustness of models to geographic distribution shifts) is also one of the key points in Rolf et al. (2024) which the paper cites.

- Although the well type data is a key contribution of the paper, the authors did not include any experiments to demonstrate its usefulness. Furthermore, the dataset splitting does not seem to take well types into account. I suggest adding well type distributions across the sets to Figure 1.

- The authors state that existing datasets predominantly contain active wells, which limits their applicability in the context of identifying abandoned or suspended wells (l86), while also admitting that the physical appearance of different well types is very similar (l133). The latter would mean that models trained on only active wells generalize to all well types, which contradicts the former. Please clarify this (ideally with experimental results).

Minor weaknesses:
- I suggest adding a subfigure to Figure 3, showing the point density of the image locations.
- There are also some typos and minor grammar mistakes (eg l46: "onshore wells oil and gas wells").
- I also suggest labeling the spatial resolution of Planet data as "high-resolution" instead of "medium-resolution", a term that is usually reserved for imagery with spatial resolutions of > 10 m (e.g. Landsat).
- The authors might also want to mention the SpaceNet 7 dataset which features Planet imagery and includes a study site with oil wells (L15-0434E-1218N_1736_3318_13), even though the dataset was developed for multi-temporal urban monitoring.

### Questions
The authors hypothesize that some features, e.g., ground depressions indicating well sites, may be more detectable in the near-infrared band (l323). Have the authors considered running any ablation experiments comparing RGB vs. RGB+NIR?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a large-scale remote sensing multispectral dataset named ALBERTA WELLS, aimed at accurately locating abandoned wells to prevent environmental pollution using remote sensing technology. The dataset, collected using Planet Labs satellites in the Alberta region, encompasses a broad area and a significant number of wells. It provides segmentation and detection annotations using the wells' geographical data and offers a reasonable split into training, validation, and testing sets. The performance of classical architectures on this dataset for segmentation and detection tasks is also provided.

### Strengths
1.	The scale of this dataset significantly surpasses other wells datasets, providing ample training data for deep learning. Given the abundance of oil wells in Alberta, creating a dataset for this region is meaningful. The public availability of this valuable dataset greatly facilitates research into the localization of abandoned oil wells.
2.	The manuscript is clearly written; the dataset-splitting method and benchmark experiments are rational.

### Weaknesses
The main limitations of this work are the inaccuracies in annotations and the insufficiency of the benchmark experiments, detailed as follows:

1.	There are minor suggestions for improvement in the phrasing. For example, line 431 states, "For the binary segmentation task framing, we train both CNN-based and Transformer-based backbones, considering the prevalent imbalance in the image data due to the small size of wells." This description is somewhat vague. If it implies that the backbones were pre-trained, it should be clearly stated which datasets were used for this pre-training. In Section 4, BENCHMARK EXPERIMENTS, it might not be clear to the reader whether the experiments used only the RGB three channels or included the near-infrared to make four channels. Although Section 3 states that the dataset provides four channels, repeating this in the experimental setup could be beneficial.
2.	Tables 4 and 5 display the benchmark performances of various classical semantic segmentation and object detection architectures on this dataset. While this work does not provide experiments with different model sizes (such as small, base, large versions), this might be sufficient for this dataset. However, including the parameter count and computational load of each benchmark model in the tables would add value to the discussion of segmentation and detection results.
3.	The state-of-the-art backbone, ConvNeXt, was omitted in the experiments. Providing its performance in remote sensing image analysis would make the article's benchmark presentation more comprehensive.
4.	In Figure 4, the satellite images reveal that wells may not always be perfectly circular, yet the semantic segmentation annotations are uniformly circular, and the object detection bounding boxes are uniformly square. This may not accurately reflect the real shape of wells, but the article lacks an explanation for this, except for a mention on line 335 about the "teardrop shape typical for well sites." The accuracy of these annotations might be the primary limitation of this dataset.
5.	Line 336 states that wells "typically range from 70 to 120 meters in diameter," indicating that wells in Alberta are relatively uniform in size. In contrast, other datasets, like the Well Pad Dataset, exhibit more significant size variations, which could impact the performance of few- or zero-shot transfer learning, as mentioned on line 503. Discussing regional differences in well characteristics could enhance this section.

### Questions
1.	In the last image of Figure 4, showing multiple wells' bounding boxes, the ground truth for the topmost well overlaps two bounding boxes. What causes this overlap? Is it a shortfall of the quality control strategy introduced in Section 3.1? If so, a detailed discussion in the text would be beneficial. 
2.	Line 338 mentions that, although no relevant experiments were conducted, the data annotation also includes the status of wells (active, suspended, or abandoned). I am curious whether these different statuses manifest distinct characteristics in remote sensing images (e.g., in multispectral bands). If the author could provide insights on this, it could enlighten future work.

### Soundness
3

### Presentation
3

### Contribution
4
