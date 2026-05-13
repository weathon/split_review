# ReSimAD: Zero-Shot 3D Domain Transfer for Autonomous Driving with Source Reconstruction and Target Simulation

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Domain shifts such as sensor type changes and geographical situation variations are prevalent in Autonomous Driving (AD), which poses a challenge since AD model relying on the previous domain knowledge can be hardly directly deployed to a new domain without additional costs. In this paper, we provide a new perspective and approach of alleviating the domain shifts, by proposing a Reconstruction-Simulation-Perception (ReSimAD) scheme. Specifically, the implicit reconstruction process is based on the knowledge from the previous old domain, aiming to convert the domain-related knowledge into domain-invariant representations, \textit{e.g.}, 3D scene-level meshes. Besides, the point clouds simulation process of multiple new domains is conditioned on the above reconstructed 3D meshes, where the target-domain-like simulation samples can be obtained, thus reducing the cost of collecting and annotating new-domain data for the subsequent perception process. For experiments, we consider different cross-domain situations such as Waymo-to-KITTI, Waymo-to-nuScenes, Waymo-to-ONCE, \textit{etc}, to verify the \textbf{zero-shot} target-domain perception using ReSimAD. Results demonstrate that our method is beneficial to boost the domain generalization ability, even promising for 3D pre-training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes RESIMAD, which aims to base source 3D reconstruction for target-domain point clouds data generation. Specifically, using implicit neural fields with accumulated point clouds per sequence, a high-quality source-domain 3D mesh could be extracted as background of AD scenes. Foreground synthetic assets like vehicles are added within simulation guided by source GT information. Therefore, target-domain point clouds could be further extracted directly or rectified with domain-specific sensor specs. Experiments compared against UDA baseline and pre-training effectiveness demonstrate the potential usage of RESIMAD.

### Strengths
- The overall paper is well motivated and easy to follow. The RESIMAD pipeline of is composed of three key components and clearly discussed with adequate implementation description.

- The experiments on several Waymo to other datasets setup shows the effectiveness of RESIMAD.

### Weaknesses
1. Effectiveness on larger detection models. One potential benefit of a ‘reconstruction, simulation and perception’ pipeline is that numerous data could be generated/rendered. As only a typical point RCNN baseline model is chosen for evaluation, it would further highlight the advantages of such methods considering more powerful and data-hungry models (e.g., ViT, DETR like detection models). It is unclear if the proposed method's benefits would scale to more complex architectures that are known to be more sensitive to data variations and volume.

2. Only ‘zero-shot’ performance is given. It would still be valuable to see whether RESIMAD could benefit from increasingly more target-domain information, from sensor specs (almost zero shot), to few-shot set-up or even with more target samples available). The current evaluation does not explore the potential of the method in scenarios where some target domain data is available, which is a common practical scenario.

Above tow points also applies to the pre-training experiment in Table3.

3. Comparison against more recent DA/UDA methods. UDA is a popular topic attracting much attentions, it is expected to compare against more recent SOTA DA/UDA approaches to further support the evaluation. The current comparison is limited and does not fully contextualize the performance of RESIMAD against the state-of-the-art in domain adaptation.

4. Although an almost ‘zero-shot’/unsupervised DA could be achieved, such zero-shot performance, I would say, requires the underlying similarity of driving scenarios and a large amount of geometric observations (to form background 3d meshes). I am wondering if the source domain shifts from Waymo to nuScenes or KITTI, will the proposed method still able to work well? The dependence on similar driving scenarios and extensive geometric data raises questions about the generalizability of the approach to more diverse environments.

5. Related to last point, one of my main concern is that the acquisition of 3D meshes. It may require a lot of computational costs and multi-lidar sensor specs for pre-training (per-scene optimization of LINR) to get relatively complete and accurate 3d meshs? The computational demands and sensor requirements for 3D mesh acquisition are not fully addressed, raising concerns about the practicality and scalability of the method.

### Questions
Please see the weaknesses section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is a system paper. The authors study a weakened domain generalization setting for 3d object detection from lidar point clouds. For example, training only on Waymo dataset and only accessing the target domain's lidar statistics, the setting pursues good performance on nuScenes. Since information about the target domain is not completely unknown, this is a weakened domain generalization setting. The proposal is to reconstruct the mesh using aggregated LIDAR (or RGB? as NeuS is mentioned). Then the background mesh is put into Carla and car assets are placed according to object size matching. The lidar signal is simulated using the composed scene in Carla. Then the authors train detectors using these simulated data and show the results out-perform the UDA baseline.

### Strengths
+ The idea generally makes sense and the authors benchmark it in a large-scale, showing meaningful margins.

### Weaknesses
 - The biggest issue is a lack of clarify, for both the mesh reconstruction and the sampling part:
* The reconstruction does not define input, output and losses formally. The only equation is depth rendering. Aggregated lidar piont clouds are used for training? (this is highlighted in bold texts) The authors mention NeuS and I am not sure whether RGB rendering losses are used. 
* Lidar rendering is difficult and there are some sphiscated methods to simulate second-returns [A]. Again the lidar rendering part does not contain any formal mathematical exposition so I cannot understand what the lidar rendering formulation is.
Since two major algorithmic parts are not understandable, I am rating presentation as poor.

- Let alone the presentation issue about algorithms, I will just assume that these two parts invoke some black-box functions and only consider the system. In this regard, I find the mesh of poor quality. This is understandable as recent papers from my group can only reconstruct meshes from lidar with similar quality. Having that said, I cannot understand why points generated from them are meaningful for detection. The authors should present a systematic evalution for mesh quality (Table.6 does not make sense to me) and rendered point cloud quality. Some comparisons are also needed, e.g., comparing with point clouds rendered from VDBF?
This concern makes me rate soundness as fair.

Minor but still confusing issues:
- Fig.2 is confusing. I cannot understand what the differences are except for the figure color.
- Table.1 gives literally no additional information since target domains are already mentioned in texts. And Waymo is also target domain？

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces 3d domain transfer pipeline, ReSimAD.
It focuses on bridging the gap between old autonomous driving datasets and newly collected real-life datasets.
The pipeline is threefold, 1) point-to-mesh implicit reconstruction, 2) mesh-to-point rendering, and 3) zero-shot perception process.
First two stages are designed to simulate target domain's LiDAR configuration using source domains. For better granulity compared to using raw sparse LiDAR points, it utilizes implicit SDF representation.
The last stage is to use the simulated dataset for 3D detection method and perform zero-shot inference on the real dataset.

### Strengths
This paper suggests dataset generation/simulation pipeline that may enrich/adjust old annotated dataset to the new target domain.

### Weaknesses
1. Poor presentation
Overall, the placement of figures and tables is not aligned with the text, thereby the whole paper is difficult to follow.

2. Technical novelty & Writing
The paper mainly focuses on the dataset simulation process using old annotated dataset.
Therefore, the most of the methodology is restricted to step-by-step instructions, rather than providing theoretical insights or verifications.
I believe the paper's contribution on introducing new dataset simulation pipeline does not exceeds its lack of technical novelty.

3. Questionable dataset selection
Since Waymo dataset is more recent and contains more LiDAR sensors all around the vehicle, compared to nescenes or KITTI, wouldn't it be more plausible to simulate Waymo from KITTI, rather than KITTI from Waymo, to be more in coherence with the paper's motivation?
It seems like the pipeline only focuses on interchanging sensor configuration, using the richest point cloud information. Please elaborate.

On the minor note, I believe that this paper is more related to computer vision or robotics field than machine learning.

### Questions
Addressed in weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces ReSimAD, a unified reconstruction-simulation-perception paradigm that addresses the domain shift issue when 3D detectors face cross-domain performance degradation in the field of autonomous driving.
The experimental results conducted on multiple 3D detectors and datasets verify that the proposed paradigm can maintain cross-domain performance in the simulated target domain. In addition, it can also assist and accelerate model training optimization, which has a certain application value.

### Strengths
Regarding the phenomenon of cross-domain performance degradation in 3D detectors in the field of autonomous driving, this paper proposes a paradigm of reconstruction-simulation-perception from the perspective of data sources. This paradigm can alleviate or partially solve the problem of cross-data domain discrepancies. The proposed approach, named ReSimAD, has significant research value.

### Weaknesses
1) The readability of the paper needs improvement, such as the illustrations, explanations, and better formatting.
2) Some necessary elaborations and supporting evidence need to be added.



### Questions
1)	Figure 1 and 3 can be made more illustrative of the proposed paradigm.
2)	The formatting of the paper needs adjustment, for example, ensure that figures and corresponding sections are not too far apart.
3)	To eliminate artifacts in Point-to-mesh Implicit Reconstruction, it should be further explained how the authors performed point cloud registration when consolidating all frames from the corresponding sequence.
4)	The interpretation of "Closed Gap" in Table 2 and its analysis are not provided in the paper.
5)	The paper does not mention the significance or the specific impact of "the matching of vehicle traffic flow density" mentioned in Section 4 (Mesh-to-point Rendering).
6)	In Table 5, what is the reason of the significant gap between using zero-shot and oracle methods? The details regarding the sample quantity and other experimental settings can be supplemented in the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
