# CamoVid60K: A Large-Scale Video Dataset for Moving Camouflaged Animals Understanding

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
We have been witnessing remarkable success led by the power of neural networks driven by a significant scale of training data in handling various computer vision tasks. However, less attention has been paid to monitoring the camouflaged animals, the masters of hiding themselves in the background. Robust and precise segmentation of camouflaged animals is challenging even for domain experts due to their similarity to the environment. Although several efforts have been made in camouflaged animal image segmentation, to the best of our knowledge, limited work exists on camouflaged animal video understanding (CAVU). Biologists often prefer videos for monitoring and understanding animal behaviors, as videos provide redundant information and temporal consistency. However, the scarcity of labeled video data significantly hinders progress in this area. To address these challenges, we present $\textbf{CamoVid60K}$, a diverse, large-scale, and accurately annotated video dataset of camouflaged animals. This dataset comprises $\textbf{218}$ videos with $\textbf{62,774}$ finely annotated frames, covering $\textbf{70}$ animal categories, which $\textit{surpasses}$ all previous datasets in terms of the number of videos/frames and species included. $\textbf{CamoVid60K}$ also offers more diverse downstream tasks in computer vision, such as camouflaged animal classification, detection, and task-specific segmentation (semantic, referring, motion), $\textit{etc}$. We have benchmarked several state-of-the-art algorithms on the proposed $\textbf{CamoVid60K}$ dataset, and the experimental results provide valuable insights for future research directions. Our dataset serves as a $\textit{novel}$ and $\textit{challenging}$ benchmark to stimulate the development of more powerful camouflaged animal video segmentation algorithms, with substantial room for further improvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The paper presents CamoVid60K, a comprehensive video dataset dedicated to studying camouflaged animals. 

- The dataset contains 218 videos, with 62,774 annotated frames, covering 70 animal categories.

- The dataset contains annotations of various forms, for example, bounding box, segmentation masks, classification, and optical flow.

- The authors have also proposed a simple pipeline for camouflaged animal detection and segmentation with the dataset.

### Strengths
- The investigated problem of camouflage animal detection is interesting.

- The contribution of dataset is good, though the construction procedure involves quite some manual effort, thus limiting its scalability.

- The writing is clear, especially on the dataset curation part.

### Weaknesses
 - The dataset is of relative small scale.

- The compared models are quite old, for example, MG was published in 2021, SLT-Net was published in 2022. In addition, as far as I know, MG was trained with self-supervised learning, thus the comparison is not that fair.

- The contribution on the architecture design is minor, and trained on the video dataset with complete supervised learning, which limits the value of proposed method, as it is not scalable, as has been done in previous work, either with synthetic data, or self-supervised learning.

### Questions
Could the authors evaluate more new models ? for example, [1], which has already been cited in the paper.

[1] Xie et al. Segmenting moving objects via an object-centric layered representation, NeurIPS 2022.

And I'm sure there are more new models.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces CamoVid60K, a comprehensive video dataset aimed at enhancing the study of camouflaged animals through improved segmentation and detection in videos. This dataset comprises 218 videos and 62,774 finely annotated frames, covering 70 distinct animal species. The authors detail the construction, annotation process, and the evaluation benchmarks established using state-of-the-art models. CamoVid60K stands out for its exhaustive annotation types—bounding boxes, masks, pseudo-optical flow, and referring expressions—and provides comparisons with existing datasets to illustrate its scale and uniqueness.

### Strengths
1. The dataset fills a clear research gap in video-based camouflaged animal detection and segmentation.

2. Thorough comparison with existing datasets and the benchmarking of state-of-the-art methods highlight the dataset’s relevance and potential for advancing the field.

### Weaknesses
My main concerns is that the paper focuses more on dataset development and benchmarking rather than presenting innovative new algorithms or techniques. Consequently, if the contribution to the field of VCOD is limited to proposing a dataset containing only 60k video frames, it may not be sufficient to consider the overall impact of the paper substantial. Moreover, I have noticed that the dataset proposed by the authors does not seem to facilitate advancements in other fields.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper delves into the realm of understanding camouflaged animals through video analysis, a domain that has traditionally been explored at image and object levels. This study pioneers advancements by focusing on video and pixel-level comprehension. A new dataset sourced from the web is introduced, with annotations primarily derived from off-the-shelf models. The proposed baseline model integrates visual and motion encoders along with a mask decoder, all leveraging existing model architectures. Experimental results demonstrate the efficacy of this streamlined approach compared to state-of-the-art models on the new benchmark presented.

### Strengths
* The investigation into camouflaged animal understanding signifies a challenging and pivotal research avenue deserving increased attention within the academic community. This work represents a progressive step towards broadening the scope of this critical topic to encompass a wider array of species with richer data.
* The authors' dedication to curating a substantially larger dataset than what is currently available is commendable.
* The automated annotation process utilizing off-the-shelf models to identify objects at the image-level and propagate masks throughout the video stream proves to be an efficient pipeline, reducing both time and manual labor.

### Weaknesses
 * The reliance on fully annotating the dataset with off-the-shelf deep learning models raises concerns about the thoroughness of the labeling process. While the authors mention refining outputs, the lack of details on this aspect questions the depth of understanding achieved in camouflaged animal analysis. This raises the issue of whether the combination of existing techniques adequately addresses the challenge at hand, potentially framing it more as an engineering problem rather than a research problem.
* The proposed baseline model provides limited insights to the field. Employing a combination of a visual encoder, motion encoder, and mask decoder, each sourced from established model architectures, which results in strong performance in camouflaged animal understanding, does not strike me as particularly innovative. This approach appears to be widely acknowledged in the realm of pixel-level video comprehension. 
* An essential aspect that requires clarification is how these components are initialized. Whether they are trained from scratch or initialized with pretrained weights can significantly impact the model's performance, especially when working with limited data volumes. Training intricate models like Mask2Former from scratch with a small dataset can pose considerable challenges due to the complexity and the volume of data necessary for effective learning. Besdeis, if pretrained weights are employed in the model, it is crucial for the authors to disclose this information in their study to ensure fairness in comparative evaluations. 
* The paper lacks a thorough exploration of the distinctive challenges inherent in camouflaged animal understanding. Addressing specific challenges tackled by the dataset and the proposed pipeline is essential. While the data sourcing strategy is unique, further differentiation is required for publication.
* The benchmarking methodology appears somewhat lacking, as it only considers methods published before 2022. To establish a more robust benchmark, the inclusion of the latest video object segmentation techniques with superior performance is necessary for a comprehensive evaluation.

### Questions
* The paper mainly focuses on identifying salient objects in scenes. It would be interesting to explore how the model handles situations with multiple instances of camouflaged animals.

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
4

### Summary
The authors have introduced a comprehensive dataset of camouflaged animal videos, which is substantial in scale and includes various types of annotations. This dataset holds the potential to contribute to the tasks of camouflaged animal segmentation and understanding. They have also proposed a pipeline for video camouflaged animal segmentation that integrates existing methods, and conducted experiments on the proposed dataset. This approach demonstrates performance comparable to some existing methods. Additionally, the authors have experimented with other related tasks in camouflaged animal video understanding, yielding some results.

### Strengths
- Building on existing segmentation tasks, the authors introduce the concept of camouflaged scene understanding, and provide a thorough analysis of related work in this field. The proposed camouflaged animal video dataset includes motion annotations and referring expression annotations, contributing to the expansion of research in this domain. The dataset also offers dense annotations for each frame, making it the most annotated dataset in the current field. 
- The article is well-written and presented, with key parts in bold and aesthetically pleasing statistical charts. The supplementary material also has a well-constructed display interface.

### Weaknesses
The main portion of the article focuses on video camouflaged object segmentation, where the novelty and contribution of the work are somewhat questionable.
1. There are concerns about the legitimacy of using existing dataset masks. The proposed dataset includes a significant portion derived from existing datasets, some of which already have mask annotations (e.g., moca-mask). While the video material is sourced from the public domain, the mask annotations belong to the authors of the previous work. Mask propagation from sparse masks to dense masks is not an overly challenging task, as the article mentions using some models for mask propagation. Could the authors clarify whether they used masks annotated by previous authors for propagation, and how exactly they did so? Additionally, I would like to know how many video clips in the dataset were collected by the authors themselves, as this pertains to the dataset's contribution.

2. There is a question about the necessity of dense annotations. I appreciate the authors' effort in data annotation. However, in Section 2.2, they mention that existing datasets' strategy of annotating one frame every five frames results in insufficient data. In practical use, whether for detection or segmentation, the necessity of dense annotations is not evident, and models may struggle to process data at 30 frames per second. The dataset proposed in this paper claims dense annotation as one of its main contributions, but the authors have not provided experiments or literature to demonstrate the usefulness of frame-by-frame annotation, which weakens the paper's innovative support. The authors should supplement relevant experiments, such as comparing the performance of models annotated every five frames versus frame-by-frame.

3. The use of perceptual camouflage score: The article mentions multiple times in Sections 3.1 and the appendix that the authors used the perceptual camouflage score proposed by Lamdouar et al. (2023) to quantify the effectiveness of animals' camouflage and filter candidate videos. While introducing this score for data filtering is innovative, this method requires annotated masks to be used, raising the question of how the authors filtered videos during the data collection phase. In Appendix A.2, the authors mention manually reviewing and initially obtaining 218 videos, with the final dataset also consisting of 218 video segments. Can I infer that no videos were filtered out during the second stage of using the perceptual camouflage score? Furthermore, in Figure 8, nine out of the ten image pairs shown were already present in Lamdouar’s original paper, which raises doubts about the authenticity of the perceptual camouflage score usage. Could the authors provide more evidence to support this?

4. The pipeline proposed in the article lacks strong innovation and contribution. The authors' pipeline uses an existing transformer architecture, but its performance in video camouflaged object detection and segmentation surpasses only unsupervised video methods or methods using only CNNs. This suggests the pipeline's limited novelty and contribution. If the pipeline is intended to be one of the main contributions of the paper, additional comparative experiments on MoCA-Mask are necessary. 

While the paper's aspects on camouflaged animal video understanding are innovative, they lack sufficient discussion and experimental support.

### Questions
Could the authors respond to and revise the issues mentioned in the "Weaknesses" section, particularly the concerns regarding the use of the perceptual camouflage score.

### Soundness
2

### Presentation
3

### Contribution
2
