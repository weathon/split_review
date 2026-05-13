# MindDETR: Beyond Semantics, Exploring Positional Cues from Brain Activity

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
Decoding visual stimuli from brain recordings offers a unique opportunity to understand how the brain represents the world and seeks to interpret the connection between computer vision models and our visual system. Recent efforts mainly adopt diffusion models to reconstruct images from brain signals. However, while these methods generally capture correct semantic information, they often struggle with precise object localization. Additionally, the commonly used proxy task, image reconstruction from brain signals, mainly measures semantic consistency, to some extent neglecting positional information of the decoded signals. In this work, to encourage more accurate brain signal decoding, we propose to use object detection as the proxy task, aiming at decoding both the semantic and positional cues from brain recordings. Based on this task, we propose MindDETR, a brain recording-based object detection model with the DETR pipeline. After aligning feature representations with a pretrained image-based DETR model, our model demonstrates that accurately brain decoding at both semantic and positional levels is feasible, and our detection-based approach achieves significantly superior results than existing reconstruction-based approaches. This result suggests the effectiveness of applying object detection as a proxy task for brain signal decoding.  Our code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper focuses on the task of brain signal decoding. Instead of adopting generative models to reconstruct images from brain signals, this paper proposes to use object detection as the proxy task, to decode both semantic and positional cues from brain recording. To this end, it presents MindDETR, a brain recording-based object detection model to align feature representations with a pre-trained image-based DETR model. Experiments are conducted to evaluate the effectiveness of the proposed method.

### Strengths
1. The task of this paper is interesting. The paper is well-written and easy to understand.
2. Extensive experiments are conducted on NSD dataset, showing the superiority of the proposed method to other competitors.

### Weaknesses
1. The motivation of this paper is ambiguous to me.
 + Is it proposed to tackle the issue of inaccurate positional features among brain signal decoding (as stated in Sec. 1 and Sec. A.2)? It is a very good question, but instead of solving this issue, this paper raises a new brain decoding task about object detection.
 + Can the proposed proxy task of object detection promote positional awareness during reconstructing visual stimulus from fMRI signals? This paper doesn’t discuss this point.
 + Is it proposed to reveal that the fMRI signals from NSD dataset can do the detection task (claimed as the second contribution in L95)? From the experimental results, the detection performance is not satisfactory (e.g., 8.5 AP_{50} for all objects)

2. The proposed framework primarily uses non-linear functions to map brain signal embedding to image features, to fulfill the task of object detection. From the perspective of computer vision, this is a common operation for feature alignment, especially in the current era of multimodal tasks. IMO, the quality of feature alignment depends on the validity or consistency of two features. Thus, my concern is whether the fMRI signals from NSD datasets are really suitable for object detection or whether brain activity should be collected while asking subjects to do something like object detection. This point is not well discussed or analyzed in depth by the authors, and the experimental results (i.e., metrics for object detection) are not good. I understand that it may be beyond the scope of this paper (more like the field of brain neuroscience), but without this assumption or premise, the significance of this paper is very unclear.

3. The technical novelty of this proposed method is limited. Both the usage of low- and high-level features and the feature alignment via distillation have been proposed by previous literature [A,B,C]. In addition, why does the larger kernel size yield better results? The author didn’t provide any explanation in Sec. 3.3 or 4.4. It is more of an experimental hyper-parameter selection, with no basis.

4. In Tab. 1, the proposed MindDETR achieves better results than MindEye. Could the author briefly describe the implementation of MindEye for object detection, and also state the architectural differences with the proposed method?

5. Are the visualizations in Fig.3 cherry-picked? As seen from Tab. 2, the precision and recall of the proposed method actually are not high. It would be better to provide in-depth discussions of the failure cases.

6. The discussion about Fig. 4 is not convincing. First of all, MindEye is for image reconstruction and MindDETR is for object detection. Two results are not comparable. Second, the proposed MindDETR also shows differences among different subjects, including the position, scale, and confidence of bounding boxes. Especially for multiple objects, the difference between individual results will be more obvious (like Fig.4 (e) and (f)). Besides, the subtitle of ‘Consisteny among different objects’ should be ‘Consistency among different subjects’.

### Questions
Please see the Weaknesses for details.

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
4

### Summary
This paper finds that existing methods struggle to accurately recover object positional information. To address this issue, the authors incorporate an object detection task into brain signal decoding and propose a new method named MindDETR. Experimental results demonstrate the feasibility of performing object detection during brain decoding.

### Strengths
This paper conduct a new task, where conduct object detection based on fMRI signals.

This paper proposed an interesting method, MindDETR, and the performance on object detection beat all the baselines on all kinds of object types.

### Weaknesses
1. First of all, I believe the proxy task of object detection should not be a standalone task; rather, it should serve as an auxiliary task to enhance brain decoding performance. The images in the participant's mind may differ significantly from those they view.

2. Comparing the bounding boxes predicted by MindDETR on ground truth images with those predicted by baseline models on reconstructed images is quite unfair. I suggest that the authors compare the performance of all models (except for the standard object detection model) on reconstructed images using the predicted bounding boxes.

3. In line 310, please explain in detail how object detection is conducted on these reconstructed images. Which object detection model did you use? This clarification may help address any concerns about the fairness of the experimental results.

4. Brain decoding primarily relies on visual regions (ROIs) in the human brain, but I believe object location may depend on certain cognitive regions. I suggest some exploration in this area.

### Questions
Refer to the weaknesses.

### Soundness
3

### Presentation
3

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
This paper presents a new task of object detection using fMRI data acquired while viewing images. The authors distill DETR, a pre-trained model in the object detection field so that the fMRI embedding can be more attentive to position information about the object in the scene. The object detection task header is then used to output the bounding boxes. The methods and evaluations seem sound.

### Strengths
+ Existing brain visual decoding focuses on classification, retrieval, and image reconstruction tasks; this paper focuses on the object detection task for the first time.
+ The experiments in the paper show that the proposed methods are effective and have yielded some results.

### Weaknesses
#### 1. The function of fMRI object detection requires further clarification
Although the authors have mentioned that fMRI target detection is potentially useful for vision-related neuroscience, however, it has only been talked about in general terms without really considering its use. As an innovative paper, it is particularly important to utilize a separate section to **discuss in detail the use of fMRI target detection for neuroscience or brain visual decoding**, which is relevant for judging the value of this paper.

#### 2. Lack analysis for limited performance
The accuracy of fMRI object detection is still low and the authors should further discuss the reasons for this result.

#### 3. Lack of analysis of error cases
Based on the quantitative results of the experiments, there should be many cases of incorrect detection, and the authors should analyze the incorrect cases rather than just showing the correct ones. A systematic analysis of the error cases would have been helpful for subsequent studies.

### Questions
+ Lines 400-406 state the proposed method "can maintain consistency in semantics, location, and quantity in most cases for the brain detection results of different subjects with the same visual stimulus images". I think this conclusion is meaningful, can the authors give quantitative results to further validate this conclusion?
+ Could the authors further provide more visualizations (corresponding to Figures 3, 4, 6) in the Appendix?

### Soundness
3

### Presentation
2

### Contribution
2
