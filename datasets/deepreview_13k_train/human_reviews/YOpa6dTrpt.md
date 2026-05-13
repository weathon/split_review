# Pedestrian Motion Reconstruction: A Large-scale Benchmark via Mixed Reality Rendering with Multiple Perspectives and Modalities

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Reconstructing pedestrian motion from dynamic sensors, with a focus on pedestrian intention, is crucial for advancing autonomous driving safety. However, this task is challenging due to data limitations arising from technical complexities, safety, and cost concerns. We introduce the Pedestrian Motion Reconstruction (PMR) dataset, which focuses on pedestrian intention to reconstruct behavior using multiple perspectives and modalities. PMR is developed from a mixed reality platform that combines real-world realism with the extensive, accurate labels of simulations, thereby reducing costs and risks. It captures the intricate dynamics of pedestrian interactions with objects and vehicles, using different modalities for a comprehensive understanding of human-vehicle interaction. Analyses show that PMR can naturally exhibit pedestrian intent and simulate extreme cases. PMR features a vast collection of data from 54 subjects interacting across 13 urban settings with 7 objects, encompassing 12,138 sequences with diverse weather conditions and vehicle speeds. This data provides a rich foundation for modeling pedestrian intent through multi-view and multi-modal insights. We also conduct comprehensive benchmark assessments across different modalities to thoroughly evaluate pedestrian motion reconstruction methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents the Pedestrian Motion Reconstruction (PMR) dataset, a large-scale, mixed-reality dataset created to support research on pedestrian motion reconstruction, particularly focusing on pedestrian intent and behavior in urban environments. This dataset combines real-world elements with virtual simulations, allowing for extensive data capture with reduced safety and cost risks compared to real-world experiments.

### Strengths
The wide variety of urban setting, and the real data collected also with over 50 VR participants for first person perspective and realistic motions.  It also includes LIDAR. Totaling 12,138 sequences. The validation and the labeling of the dataset is good. All in all makes a very complete contribution.

### Weaknesses
I don't see major weaknesses. However, there could be domain Gaps from the Egocentric Data in PMR as it is collected through VR headsets in a simulated setting, which differs from real-world egocentric videos captured with physical head-mounted cameras. 
I wonder how something like this could be done more similar to Ergo4D.
This domain discrepancy could limit the effectiveness of models trained on PMR for real-world applications, as the simulated egocentric data may not generalize well to real-world environments. This isn't a major flaw, but perhaps limits the impact of the dataset.

### Questions
I would like to see in the discussion how the data could also be used for causal implementations. Beyond just the current dataset. Many simulators recreate events by replicating configuration files. In fact a prior interesting work on a similar space but running on Airsim instead of CARLA, was looking into creating realistic behaviours based on motion capture and personality recreation. 

Wang, Cheng Yao, et al. "CityLifeSim: A High-Fidelity Pedestrian and Vehicle Simulation with Complex Behaviors." 2022 IEEE 2nd International Conference on Intelligent Reality (ICIR). IEEE, 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Pedestrian Motion Reconstruction (PMR) dataset, a large-scale benchmark designed to improve the reconstruction of pedestrian motion and intention for autonomous driving applications. The dataset is generated using a mixed-reality platform that combines real-world realism with simulation-based data collection, reducing costs and safety risks. PMR features multi-modal and multi-perspective data, including third-person RGB videos, LiDAR data, and egocentric perspectives from 54 subjects across 13 urban settings. The dataset provides 12,000+ sequences under various weather conditions and vehicle speeds, capturing complex pedestrian-vehicle interactions, including rare scenarios like collisions. The main contributions include: 1) a mixed-reality platform of collecting real-world like pedestrian motion and corresponding sensor data 2) benchmark evaluations across different modalities such as third-person/first-person RGB and LiDAR for reconstructing pedestrian poses, and 3) insights into pedestrian behavior in dangerous and rare scenarios.

### Strengths
- The proposed mixed-realtiy platform combining real-world MoCap and VR simulation is interesting, and could provide a safe and efficient way to collect real-world pedestrian motion data and rare scenarios.
- It also provides a good benchmark for global human and camera motion estimation, with motion distribution closer to the real-world. Previous dataset often use existing MoCap motion data which often cannot reflect real-world human motion distributions.
- The dataset also includes real-world object interactions and tracking.

### Weaknesses
 - The main tasks of the benchmark seem to focus on human pose estimation, which I think discard most of the scene context such as vehicles, weather, etc. It does not evaluate the main strengths of the dataset, which includes pedestrian vehicle interactions. I think having some pedistrian behavior generation/forecasting tasks would be beneficial since it will measure models’ ability to capture vehicle pedestrain interactions in rare or dangerous scenarios.
- To validate the domain gap between the proposed synthetic dataset and real-world data, the paper should evaluate on its main tasks, human pose estimation. For example, using the proposed dataset as additional training to improve the human pose estimation performance on existing benchmarks (3DPW, EMDB, RICH etc.). It is a bit weird that the paper evaluates the domain gap on a complete different task of 3D object detection. Specifically, the paper should demonstrate how the inclusion of the PMR dataset improves performance on established human pose estimation benchmarks when used as additional training data, rather than simply evaluating on a different task like 3D object detection, which doesn't directly validate the core contribution of the dataset for human motion analysis.
- Finally, it would be nice if the paper can provide videos to showcase the rare cases and highlight the quality of the dataset.

### Questions
- How does the dataset decide which objects should be placed in real-world, and which should be placed in simulation?
- The proposed mixed-reality data capture platform is pretty neat. Any plans to open source it to expand the dataset further?
- What instructions are given to the subject to interact with the VR environment?
- Are there any audios such as traffic sounds provided to the subject to let them behavior more realistically?

Typo:
- l363: “taccount”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a large-scale pedestrian motion reconstruction (PMR) dataset developed using a mixed reality platform. It simulates the authenticity of the real world while reducing the costs and risks associated with dataset creation. The dataset includes third-person perspective RGB videos of moving vehicles, LiDAR data from the vehicles, and self-centered views of pedestrians, along with both unimodal and multimodal pedestrian pose estimation. This dataset contributes to the advancement of the community.

### Strengths
1.	The dataset is designed based on the simulation of pedestrian intentions in the real world and features a pipeline for pedestrian motion capture utilizing VR and MoCap technologies. It replicates various pedestrian actions found in real-world scenarios, providing a reference for dataset collection and production. 
2.	The substantial amount of data offers a rich foundation for modeling pedestrian intentions through multi-view and multimodal insights.
3.	The dataset also simulates the interaction between pedestrians and vehicles under different environmental conditions, which is very suitable for practical applications.

### Weaknesses
1.	I noticed that interactions between pedestrians and objects are quite limited, with a greater focus on pedestrian-vehicle interactions. Did the authors consider including specific scenarios, such as pedestrian conversations, telephone calls, and the use of umbrellas on rainy days? The current dataset seems to lack the richness of everyday human-object interactions beyond simple rigid body contact, which could limit its applicability to more complex real-world scenarios. For example, the absence of interactions involving deformable objects or more intricate manipulation tasks could hinder the development of models that generalize well to diverse environments.
2.	The comparison datasets in the paper are not up-to-date. To strengthen the comparison with datasets gathered from real-world scenarios, you may refer to some of the most recent multimodal human body reconstruction datasets. such as RELI11D(CVPR2024) [1], HiSC4D (TPAMI 2024) [2]. The lack of comparison with state-of-the-art datasets makes it difficult to assess the novelty and contribution of this work. Specifically, the paper should address how the proposed dataset compares in terms of scale, diversity, and modality with recent datasets that include synchronized multi-view RGB, LiDAR, and IMU data.
3.	In the collection pattern of this dataset, the encounters between pedestrians and vehicles in the environment are all predetermined by fixed program designs, which may result in slightly limited comprehensiveness of the dataset. Have the authors considered incorporating randomness in procedural generation techniques to accommodate the diversity of interactions? The current approach may lead to a lack of variability in pedestrian-vehicle interactions, potentially causing the models trained on this dataset to overfit to specific scenarios. The absence of unpredictable events, such as sudden changes in vehicle speed or direction, could limit the dataset's ability to capture the full spectrum of real-world pedestrian behavior.

### Questions
1. There are already numerous existing human motion datasets; could you provide the latest datasets for comparison?
2. The picture annotation text in Figure 6 is blocked by the picture.
3. What is the frequency of camera and Lidar acquisition?
4. The ground truth used in this article is sampled from the mocap system to 120hz, please explain the rationality of the GT.
5. What are the shape distribution and the speed distribution of virtual avatars?

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
The paper introduces the Pedestrian Motion Reconstruction (PMR) dataset, a large-scale benchmark designed to advance autonomous driving safety by focusing on pedestrian intention and behavior. The dataset is created using a mixed reality platform that combines real-world realism with simulation accuracy, capturing pedestrian interactions with objects and vehicles from multiple perspectives and modalities. The PMR dataset includes data from 54 subjects across 13 urban settings with 7 objects, encompassing 12,138 sequences under diverse weather conditions and vehicle speeds. The paper also presents comprehensive benchmark assessments across different modalities to evaluate pedestrian motion reconstruction methods.

### Strengths
1. The PMR dataset is the first of its kind to incorporate multi-perspectives and multi-views for modeling pedestrian intention in diverse outdoor scenes, including rare scenarios like collisions with safety concerns.
2. The dataset provides a rich foundation for modeling pedestrian intent through insights from third-person perspective RGB videos, LiDAR data, and egocentric perspectives.
3. The mixed reality platform reduces data collection costs and risks while ensuring ground-truth alignment with the global coordinate system, capturing pedestrian interactions realistically.
4. The paper conducts thorough evaluations across different modalities, providing a valuable resource for assessing pedestrian motion reconstruction methods.
5. The dataset is publicly available, promoting further research and development in the field.

### Weaknesses
1. While the mixed-reality data offers high-quality labels, there may be a domain gap between simulated and real-world data, which could affect the generalizability of models trained on the PMR dataset. The domain gap not only lies the rendering but also the motion diversity. Specifically, the motion capture system, while precise, may not fully capture the subtle variations in human gait and behavior observed in natural settings. This could lead to models that are overly sensitive to the specific motion patterns present in the dataset and less robust to the variations encountered in real-world pedestrian movements.
2. The reliance on a mixed reality platform with VR headsets, MoCap systems, and the CARLA simulator might limit the reproducibility of the data collection process in other research settings. The complexity of the setup, involving multiple synchronized hardware and software components, makes it challenging for other researchers to replicate the data collection environment. This lack of accessibility could hinder the widespread adoption and further development of models based on this dataset.
3. The dataset is collected from a limited number of subjects, which may not fully represent the global diversity in pedestrian behavior and motion. The limited subject pool could introduce biases in the dataset, as individual variations in gait, reaction times, and interaction styles may not be adequately represented. This could lead to models that perform well on the specific characteristics of the subjects included in the dataset but fail to generalize to the broader population.

### Questions
1. How does the PMR dataset address the domain gap between simulated and real-world data, and what measures are taken to ensure the dataset's applicability to real-world scenarios? The author should discuss more about how could this dataset working together with real captured dataset, for example waymo-open-dataset.
2. What are the limitations of the current data collection process, and how might these be overcome in future work to increase the diversity and representativeness of the dataset?

### Soundness
4

### Presentation
4

### Contribution
4
