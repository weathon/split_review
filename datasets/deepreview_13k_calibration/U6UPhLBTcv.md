# SyGRID: Synthetically Generated Realistic Industrial Dataset

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Industrial automation depends on accurate object recognition and localization tasks, such as depth estimation, instance segmentation, object detection, and 6D pose estimation. 
Despite significant advancements, numerous challenges persist, especially within industrial settings. To address these challenges, we propose 
SyGRID, (Synthetically Generated Realistic Industrial Dataset), a new simulated, realistic dataset specifically designed for industrial use cases. 
Its novelty lies in several aspects: the generated frames are photo-realistic images of objects commonly used in industrial settings, capturing their unique material properties; this includes reflection and refraction under varying environmental light conditions. Moreover, SyGRID includes multi-object and multi-instance cluttered scenes accurately accounting for rigid-body physics. 
Aiming to narrow the currently existing gap between research and industrial applications, we also provide an exhaustive study on different tasks: namely 2D detection, segmentation, depth estimation and 6D pose estimation. These tasks of computer vision are essential for the integration of robotic applications such as grasping.
SyGRID can significantly contribute to industrial tasks, leading to more reliable robotic operations. By providing this dataset, we aim to accelerate advancements in robotic automation, facilitating the alignment of current progress in computer vision with the practical demands of industrial robotic applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new object dataset tailored to industrial scenarios. The dataset is generated using a physically-based renderer (PBR) on 10 distinct objects, considering various materials, lighting conditions, and background textures. The paper also conducts extensive experiments on both simulated and real data to assess the realism of the synthetic dataset.

### Strengths
The paper is well-written, clear, and provides a thorough literature review of previous works related to object datasets. The experiments are comprehensive and sufficiently demonstrate the effectiveness of the proposed simulated data in real-world scenarios.

### Weaknesses
1. A key concern is the limited novelty of the proposed dataset. While the authors emphasize that the dataset includes cluttered scenes, varied lighting conditions, and diverse object materials, these features are already well-supported by modern PBRs [1,2]. Previous works, such as Omni6D [3], have incorporated similar capabilities in the rendering of object datasets. It would be helpful for the authors to further clarify how their dataset differs from prior work in this domain, particularly concerning the specific rendering techniques and material properties that are not already available in existing PBR pipelines. The claim of handling reflective and transparent objects needs more specific details, such as the types of materials and the rendering algorithms used to achieve this, as these are not universally supported in all PBR implementations.

2. The dataset contains only 10 object instances, which is quite limited compared to other object datasets. Industrial environments typically feature a much larger variety of objects. Expanding the dataset to include more object types, and more importantly, a wider range of object categories, would improve its diversity and applicability. The current dataset risks being too specific to the initial use case and not generalizable to broader industrial applications. A more detailed analysis of the object categories and their relevance to a wider range of industrial tasks would be beneficial.

3. Although the dataset features cluttered scenes, it appears that only top-down viewpoints are used to capture the images. Incorporating images from different viewpoints, including oblique and side views, would enhance the dataset’s diversity and better reflect real-world industrial scenarios where cameras are not always positioned directly above the scene. The lack of viewpoint diversity limits the dataset's applicability to scenarios with varying camera angles, which is a common occurrence in industrial settings. Furthermore, the paper does not specify the range of camera distances used, which is a critical parameter for evaluating the robustness of pose estimation algorithms.

### Questions
From a practical perspective, is it realistic to find industrial scenes where transparent objects and tools are piled together? And is it common for different tools to be stacked separately?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new, synthetic dataset tailored for computer vision tasks, such as 2d object detection, segmentation, depth estimation, and 6DOF pose estimation in industrial settings. The dataset aims to bridge the gap between research datasets and real-world industrial environments by providing high-quality, photo-realistic data with challenging features such as reflections, refractions, and highly cluttered multi-object scenes. The dataset is evaluated on real and synthetic data using 2D bounding box detection, instance segmentation, depth estimation, and instance-level 6D pose estimation.

### Strengths
Overall, the paper is clearly written and easy to follow. It introduces prior work on industrial datasets, their strengths and weaknesses, and presents the varying attributes visually through tables. The paper further shows that the presented dataset is more realistic overall compared to prior proposed methods (about on par to YCBV) and, therefore, partially closes the sym-to-real gap.

### Weaknesses
I have multiple questions regarding the proposed dataset's motivation, technical contribution, and real-world usefulness.
1. To me, the dataset seems to be ill-motivated. The dataset focuses solely on applying industrial bin-picking with a very specific (and small) number of objects, severely limiting the applicability of the dataset to real-world scenarios. I am not aware of any application where these exact parts must be picked from an unorganized bin by a robotic manipulator. If such scenarios exist, they should be mentioned in the introduction. If the claim is that the dataset can be used for other applications, I would expect some experiments that analyze the generalization capability of algorithms trained on this dataset in real-world applications. I suggest that the paper contains a more thorough motivation of applications in industry where this dataset can be useful.
2. The motivation for introducing this dataset is to handle "occlusions and highly cluttered scenes" and "different light conditions." I would argue that industrial settings are some of the most controllable environments for robots. Not only can the lighting be fully controlled, but I also have trouble envisioning specific tasks where the robot has to pick these specific arrangements of objects. The paper does not address the fact that in most industrial settings, the objects are presented to the robot in a more structured way, rather than in a cluttered bin.
3. Regarding the results, the paper claims that the main goal is to reduce the sym-to-real gap in performance. However, Table 2 shows that a large gap still exists between the two data distributions. Similarly, the results show that using this data for training results in widely differing performance on real vs synthetic test data (-15 to -20% on segmentation, 10x difference on depth estimation, between 2-6x large rotation error). These differences in performance show to me that the dataset is only partially useful to generalize to real-world data and does not solve the sym-to-real problem. The paper does not provide a clear analysis of why the performance gap is so large, and what aspects of the dataset contribute to this gap. It is unclear if the gap is due to the limited diversity of the synthetic data, or the quality of the real data, or both.
4. It is also questionable how a model trained on this dataset performs on out-of-distribution data. Can these models be used on some of the other datasets (Table 1.)? If so, what is the performance? Specifically, how does the model perform when presented with novel object categories, or different types of clutter? The paper should include experiments that analyze the model's robustness to out-of-distribution data.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces SyGRID, a novel synthetically generated industrial dataset designed to enhance object recognition and localization tasks critical for industrial automation, such as 2D detection, segmentation, depth estimation, and 6D pose estimation. SyGRID’s key contributions include highly realistic, photo-realistic images that simulate industrial environments with challenging elements like material reflections, refractions, and cluttered multi-object scenes modeled with rigid-body physics. By offering a comprehensive dataset tailored for realistic industrial conditions, SyGRID bridges the gap between research and practical applications, enabling advancements in robotic tasks such as grasping, thereby supporting more robust robotic automation in industrial settings.

### Strengths
Realistic industrial dataset is needed for downstream robotic tasks, while this scenario is yet to be well studied and has many challenges, such as the cluttering and transparency of objects. I believe this dataset is practical and will contribute to the development of this field.

### Weaknesses
For presentation, I recommend authors to divide long paragraphs into some short paragraphs, which could largely increase the ease of reading of this paper.

For experiments, as the contribution and final goal is to facilitate downstream robotic manipulation, while this dataset is rendered in simulation, I recommend authors to demonstrate both qualitatively and quantitatively how much this simulation rendered dataset can bridge the sim2real gap of robotic perception and manipulation. Specifically, the evaluation should include metrics that directly assess the performance of models trained on the synthetic data when applied to real-world robotic tasks. This could involve measuring the accuracy of object pose estimation or the success rate of grasping tasks using a physical robot. The current evaluation primarily focuses on performance within the simulation environment, which does not fully validate the dataset's utility for real-world applications.

For dataset, are there diverse objects in a category? Or the diversity only exists in number of categories?

The real-world robotic manipulation video could be polished if the author presents the policy visualization, instead of only the robotic execution.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2
