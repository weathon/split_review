# Out of Sight: A Framework for Egocentric Active Speaker Detection

- Decision: Reject
- Scores: 6, 6, 3, 1

## Abstract
Current methods for Active Speaker Detection (ASD) have achieved remarkable performance in commercial movies and social media videos. However, the recent release of the Ego4D dataset has shown the limitations of contemporary ASD
methods when applied in the egocentric domain. In addition to the inherent challenges of egocentric data, egocentric video brings a novel prediction target to the ASD task, namely the camera wearer’s speech activity. We propose a comprehensive approach to ASD in the egocentric domain that can model all the prediction targets (visible speakers, camera wearer, and global speech activity). Moreover, our proposal is fully instantiated inside a multimodal transformer module, thereby allowing it to operate in an end-to-end fashion over diverse modality encoders. Through extensive experimentation, we show that this flexible attention mechanism allows us to correctly model and estimate the speech activity of all the visible and unseen persons in a scene. Our proposal (ASD-Mixer) achieves state-
of-the-art performance in the challenging Ego4D Dataset, outperforming previous state-of-the-art by at last 4.41%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Paper proposed a novel approach for the Active Speaker Detection (ASD) problem in egocentric data (esp. First Person Video (FSD)). This problem is relatively unexplored. The challenges for ASD in FPV is mainly to the "invisibility" of the camera wearer in the video which the SOTA ASD algorithms cannot handle correctly.

The proposed method uses multimodality to overcome this challenge via 3 building blocks: (i) Modality Encoder; (ii) Mutlimodal Mixer; (iii) Speech Decoder.

Experiments were performed to compare against SOTA ASD in FPV methods for the Ego4D dataset.

### Strengths
1. Paper's position that ASD in FPV is less research and proposed a novel method to overcome the specific issue for this problem is well explained and motivated.

2. Proposed method is somewhat novel and logical.

3. Experimental results are quite strong.

### Weaknesses
1. Problem statement is somewhat niche.
2. Novelty of proposed solution is limited as it's a special case of multimodality matching. The unseen visual features are replaced with a special token (c).

### Questions
No question.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes O2S, a framework for egocentric active speaker detection. Most active speaker detection literatures fall in commercial movies and social media videos, while egocentric videos are less investigated. O2S consists of three stages: 1) An audio encoder and a video encoder are employed to obtain audio features and visual face features. 2) A transformer serves as multimodal mixer to aggregate information from audio and video. 3) Another transformer serves as speech decoder to predict speech event for each face feature, audio feature, and an additional feature for the invisible camerawearer. There are some additional changes made for egocentric videos. First, face positions are added in the visual feature. Second, as egocentric videos may present many blurred faces due to fast motion, noisy faces are less contributed to the loss. Experiments are conducted on the Ego4D dataset for two tasks: Active Speaker Detection of visible targets
(vASD) and egocentric Active Speaker Detection (eASD).

### Strengths
1. The proposed O2S achieves the state-of-the-art performance on the Ego4D for both vASD and eASD.
2. The proposed method is a reasonable solution for egocentric active speaker detection.
3. The paper presentation and writing are very clear.

### Weaknesses
1. The authors should highlight the main differences between the proposed method and the previous 3rd person view active speaker detection methods. This is important to show the contribution of this proposed method.
2. I think Visual Token Representation and Weighted Visual Loss are the two unique contributions for the egocentric scenario. However, these two contributions are not significant. This brings back to the first concern: the authors should highlight the main differences compared to previous works especially on the main architecture.
3. Although the whole pipeline is reasonable, it is complicated. Does it need to first use a face detector to detect faces? In the main architecture of O2S, there are CNNs for encoding video and audio, and then there are transformers for mixing video and audio and decoding them. Why not encode and mix video and audio in just a single transformer? In my view, all the three stages can be simplified in one single transformer in principle.

### Questions
"In other words, the active speaker is more likely to appear near the center of the frame" I agree in most cases the active speaker appear around the center. But in some cases, the camerawearer may not look at the speaker or only turn eyeballs to look at the speaker. It may be more accurate to incorporate eye gaze location in the Visual Token Representation. After all, the XR device should already detected eye gaze.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method for active speaker detection of egocentric videos. Unlike existing works that focus on YouTube or broadcast videos, ASD for egocentric videos brings additional challenges such as head movement and camera wearer's speech. The paper proposes a 3-stage architecture consisting of (1) modality encoders, (2) multimodal mixer, (3) speech decoder. In particular, a learnable token helps to model speech from the camera wearer. Short- and long-term architectures enable effective multi-modal fusion and extended temporal modelling. The authors use additional tricks like weighted visual loss and position of face in order to improve performance. The method is evaluated on the recent Ego4D dataset which contains various egocentric videos including human speech.

### Strengths
- The method is well-engineered and achieves a strong performance. 
- Techniques such as face position and weighted loss paper is well tailored to this dataset.

### Weaknesses
- The performance exceeds existing works, but the gap between the proposed method and LoCoNet is not too significant, given that this paper is specifically tailored to this dataset.
- The methods used such as "face position" and "weighted loss paper" are the sources of most of the improvement compared to LoCoNet, but these tricks might be overfitting to the biases that exist specifically in this dataset. Does the method still generalise to existing non-egocentric ASD datasets, such as AVA-ASD or ASW?
- Most similar literature to this is (Jiang et al., 2022) but there is very little comparison to this work in the paper.
- I am not sure if "active speaker detection" is an appropriate term for the overall task. vASD in this paper is usually called ASD in other literature, and the ASD usually does not encompass what is called eASD in this paper. A similar work (Jiang et al., 2022) does not refer to this task as ASD.
- Regardless of the term used, I am not sure if the proposed combined problem (eASD+vASD) is useful, in between vASD and AV speaker diarisation. The camera wearer is a specific identity, whereas we do not consider the identity information of the visible speakers.

Regarding clarity/writing:
- The authors use abbreviations egoASD/egoVAD in page 6, but these are not explained or used anywhere else. 
- What is meant by "visible" and "unseen" exactly? Why not "seen" and "unseen" or "visible" and "invisible" for example?
- Is "at last 4.41%" at the end of abstract is the intended expression?
- "fine grain..." in the introduction should be "fine-grained..."
- Sec 3.2 refers to "Token Supervision" without section number, but this only appears much later making it confusing.

### Questions
- Please see questions in 'weaknesses'.
- Does the proposed method work well when there are multiple off-screen speakers? For example, it is realistic to have off-screen speakers next to the camera wearer in a meeting.
- Do the authors use the pre-trained weights for LoCoNet, or is it re-trained on the same dataset?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a transformer-based approach, Out of Sight, that can model all the speaking activities from three prediction targets (visible speakers, camera wearer, and global background speech). The proposed method consists of 3 building blocks: Encoder, Multimodal Mixer, and Decoder. The encoder is a series of convolutional networks that embeds the visual and audio features. The multimodal mixer performs cross-modal attention and aggregates relevant information from audio-visual modalities. The decoder maps all types of tokens (audio, visual, and camera wearer) into a common representation space and predicts the final prediction. To further improve the performance, it uses a technique of long-term feature modeling by incorporating an extended temporal sampling.

### Strengths
- The proposed architecture is very simple and easy to understand.
- It can be used to predict all the speaking targets (visible speakers, camera wearer, and global background speech) using a single architecture.

### Weaknesses
First of all, it looks like the authors provide inconsistent comparisons.
- In Table 1, the authors report vASD mAP scores on the Ego4D’s validation set. The problem is that they report mAP\@0.5 (which is different from mAP) for previous methods when they report mAP only for their method. When we compute the mAP score, we only use the ground-truth face bounding boxes. However, computing mAP\@0.5 involves comparing IoU between the face bounding-box detections and the ground-truth, therefore mAP\@0.5 is estimated much lower than mAP.
- The authors didn’t report the vASD mAP of Min et al. Min (2022) although they report eASD mAP of it. This kind of partial reporting might make their method look more powerful, but doesn’t seem appropriate.
- Reporting unfair and inconsistent comparisons confuses the readers and the whole computer vision community. I believe the authors should be more accurate in describing their validation scheme and the validation strategy of the Ego4D paper.

Second, the proposed method and the results are not state-of-the-art.
- SPELL (2022) and STHG (2023) achieve 71.3% vASD mAP and 75.7% vASD mAP on Ego4D’s validation set, respectively, which significantly outperform the proposed method. Furthermore, STHG (2023) achieves 85.6% eASD mAP, which also outperforms the proposed method in this paper. Please refer to the challenge reports and recognize them. It is recommended by the Ego4D organizers to properly acknowledge their technical reports.

Moreover, the proposed method has some weaknesses in its form.
- For the weighted visual loss, the user needs to pre-compute a weight factor. The weight factor needs to be fine-tuned for each dataset (because it is data-dependent), which is ineffective and seems ad hoc.
- There are many other hyper-parameters that need to be fine-tuned for each dataset: $\alpha$, $k$, $n$, $\beta$, which makes the overall method complicated and hard to optimize and utilize.

[SPELL (2022)] Intel Labs at Ego4D Challenge 2022: A Better Baseline for Audio-Visual Diarization

[STHG (2023)] STHG: Spatial-Temporal Heterogeneous Graph Learning for Advanced Audio-Visual Diarization

### Questions
What are the FLOPS and memory requirements for the proposed method? What is the throughput? Most of the previous state-of-the-art approaches are very efficient in terms of FLOPS and memory, and I wonder if the proposed method is comparable.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
