# DV-3DLane: End-to-end Multi-modal 3D Lane Detection with Dual-view Representation

- Decision: Accept
- Avg Score: 4.40
- Scores: 6, 6, 6, 3, 1

## Abstract
Accurate 3D lane estimation is crucial for ensuring safety in autonomous driving. 
However, prevailing monocular techniques suffer from depth loss and lighting variations, hampering accurate 3D lane detection. 
In contrast, LiDAR points offer geometric cues and enable precise localization. 
In this paper, we present~\modelname, a novel end-to-end {\textbf{D}ual}-{\textbf{V}iew} multi-modal \textbf{3D} \textbf{Lane} detection framework that synergizes the strengths of both images and LiDAR points. 
We propose to learn multi-modal features in dual-view spaces, \ie, \textit{perspective view} (\uv) and \textit{bird's-eye-view} (\bev), effectively leveraging the modal-specific information.
To achieve this, we introduce three designs:
\textbf{1)} A bidirectional feature fusion strategy that integrates multi-modal features into each view space, exploiting their unique strengths.
\textbf{2)} A unified query generation approach that leverages lane-aware knowledge from both \uv and \bev spaces to generate queries. 
\textbf{3)} A 3D dual-view deformable attention mechanism, which aggregates discriminative features from both \uv and \bev spaces into queries for accurate 3D lane detection.  
Extensive experiments on the public benchmark, OpenLane, demonstrate the efficacy and efficiency of~\modelname. It achieves state-of-the-art performance, with a remarkable \textbf{11.2} gain in F1 score and a substantial \textbf{53.5\%} reduction in errors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a LiDAR Camera 3D-Lane detection model. This model consists of 4 main blocks: 1) two backbones (image in camera view (CV) and LiDAR (BEV) in bird-eye-view) linked by a bidirectional feature fusion, 2) a dual view query generation with clustering between BEV and CV queries, 3) a decoder with query clustering that produce point queries and 4) a 3D dual-view deformable attention producing a 3D lane prediction. The experimental part shows that the proposed model outperforms SOTA, including the last ICCV2023 papers.

### Strengths
One original contribution is the bidirectional feature fusion module used to train the backbones in both BEV and CV leveraging for each view information from both sensors. The experimental part shows that this mechanism increases the F1 score about 2%. 
Another important part of the pipeline is a Unified Query Generation process that win less than 1% F1 score. 
The authors a 3D Dual-view Deformable Attention model that slightly improves the F1 score of the model. 
Regarding the ablation study, the sensor fusion win more than 10% regarding the LiDAR only and about 20% regarding only the camera. 
Experiments have been achieved on the public dataset OpenLane. The proposed model outperforms SOTA.

### Weaknesses
there are no really weakness in the paper. 
I should be interesting to experiment your models on other datasets like  OpenLane-Huawei: a dataset with more horizontal lines.

minor typo : 

instruction <-> introduction
Increase or remove line (d) of fig 7. (figures are too small)

### Questions
Did you try to experiment your models on other datasets like  OpenLane-Huawei: a dataset with more horizontal lines?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper target 3D lane detection problem by proposing a dual view representation method utilizing both camera and Lidar as input. Their proposed method has achieve remarkable improvement over prior work with high efficiency.

### Strengths
1. Compared to prior work that mostly use only camera and feature learning in either Perspective View or Bird Eye View, this work fill the gap by fully investigate feature interaction of both sensor(Lidar+Camera) in both view(PV+BEV). And shows the superiority of their method by showing large improvement over prior work. 
2. The work is very well written, clearly introduce all related work as well as their problems, and how this work target those problem by proposing new solutions. 
3. This work include detail ablation study, make it clear to see the improvement over each step.

### Weaknesses
1. There’re some inconsistent in the evaluation result: 1). Although this method have explicitly filling the gap of missing Lidar modality in prior work, it might not seem as an apple to apple comparison in the table. In table 1 1.5m, compare with prior SOTA LATR, the proposed method didn’t achieve overwhelming improvement despite using one extra modality(Lidar). Does that mean the improvement in this range had been saturated to some extent? Also DV-3Dlane use a weaker backbone(ResNet-18/34) compare to ResNet50 LATR, make it even harder to see the full potential of proposed method compare to prior art. 2). Why Use OpenLane1000 in table 1(main experiment) but OpenLane300 for the ablation? Make it incomparable with result in Table1. 
2. For onboard application, it might not always viable, to access both Lidar and Camera information for joint feature, does this method also provide implications for camera only/Lidar only methods? Maybe it’s more clear in ablation study if we could compare Table1 and Table2 directly. A follow up question, if camera-only ablation is possible, could it also show result on Apollo dataset? This is the dataset most commonly used in prior work. 
3. For Figure1, please also consider adding more methods to be more completed, for instance light weight model like GenLane.
4. What is the ‘lane-aware prior knowledge’ in the abstract? I feel like ‘prior knowledge’ it is not discussed in the main text. Please explain or consider rephrase it.

### Questions
Please refer to weakness. In general I feel like this paper is well written, happy to raise my score if question addressed.
Some related papers from prior venue is not properly cited, please consider citing the following works

@inproceedings{liu2022learning,
  title={Learning to predict 3d lane shape and camera pose from a single image via geometry constraints},
  author={Liu, Ruijin and Chen, Dapeng and Liu, Tie and Xiong, Zhiliang and Yuan, Zejian},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={36},
  number={2},
  pages={1765--1772},
  year={2022}
}

@inproceedings{yao2023sparse,
  title={Sparse Point Guided 3D Lane Detection},
  author={Yao, Chengtang and Yu, Lidong and Wu, Yuwei and Jia, Yunde},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={8363--8372},
  year={2023}
}

@inproceedings{li2022reconstruct,
  title={Reconstruct from top view: A 3d lane detection approach based on geometry structure prior},
  author={Li, Chenguang and Shi, Jia and Wang, Ya and Cheng, Guangliang},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={4370--4379},
  year={2022}
}

@inproceedings{ai2023ws,
  title={WS-3D-Lane: Weakly Supervised 3D Lane Detection With 2D Lane Labels},
  author={Ai, Jianyong and Ding, Wenbo and Zhao, Jiuhua and Zhong, Jiachen},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
  pages={5595--5601},
  year={2023},
  organization={IEEE}
}

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel 3D lane detection algorithm that exploits a dual-view representation. The proposed algorithm consists of bi-directional feature fusion to aggregate view-specific features, unified query generation that focuses on coherent lane features, and 3D dual-view deformable attention to associate information across the viewpoints. The authors provided outperformed experimental results on OpenLane dataset.

### Strengths
- Achieved the best performance on a 3D lane detection benchmark
- Leveraged multi-modal features to generate a unified query for 3D lane detection

### Weaknesses
 - It appears that the 3D DV deformable attention mechanism lifts PV features to 3D using known camera parameters. Also, when the authors concatenate DV features, they depend on these camera parameters. Have the authors attempted to test the tolerance of calibration parameters to noise?
- Since the evaluation was only performed on OpenLane, it is difficult to check the generalizability of the proposed method.

### Questions
.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a multi-modal 3D lane detection method. A bidirectional feature fusion approach is proposed to incorporate multi-modal features into each view space. A unified query generation module is adopted that provides lane-aware prior knowledge from both views. A 3D dual-view deformable attention mechanism that combines discriminative features from both PV and BEV into queries for precise 3D lane detection. Comprehensive experiments on the public benchmark, OpenLane, prove the efficacy and efficiency of DV-3DLane.

### Strengths
*  The performance of this article exceeded that of existing methods. A significant increase was also achieved in the multimodal feature fusion at the backbone level. 
*  The paper is well written and easy to follow.

### Weaknesses
 *  Most methods in Table 1 are based on camera. As can be seen from the results in Table 3, the performance of camera-only is not competitive. Multimodal inputs should be introduced to some methods for a comparative performance evaluation. Otherwise, presenting multimodal fusion as a key contribution is somewhat insufficient.

* In Table 4, the performance of the queries generated based on PV and BEV is not as high as random queries, indicating that the adaptive generation of queries doesn't work. Although the queries after clustering have achieved performance improvement, it remains to be seen whether this improvement is brought about by the extra network. 

* The feature fusion in the backbone and decoder is quite tricky, making it difficult to be viewed as a major contribution point.

### Questions
*  The main performance improvement primarily comes from multi-modalities, but multi-modalities inherently achieve higher points than a single modality. Therefore, it would be best to prove that the multi-modal performance of existing methods is inferior to this paper. The camera result is not much competitiveness, especially when compared to some recent methods, such as Group Lane.
*  Using Deformable attention to aggregate multi-modal features lacks innovation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper covers lane detection task using attention mechanism from multi-modal queries of vision and LiDAR.

### Strengths
* Really novel idea that does this task of lane detection using query clustering from multiple perspective. 
* SOTA results, and code should be available online soon 
* Takes care of runtime optimization as well.

### Weaknesses
NA

### Questions
NA

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
