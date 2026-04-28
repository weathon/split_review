# Segment, Select, Correct: A Framework for Weakly-Supervised Referring Segmentation

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Referring Image Segmentation (RIS) -- the problem of identifying objects in images through natural language sentences -- is a challenging task currently mostly solved through supervised learning. However, while collecting referred annotation masks is a time-consuming process, the few existing weakly-supervised and zero-shot approaches fall significantly short in performance compared to fully-supervised learning ones. To bridge the performance gap without mask annotations, we propose a novel weakly-supervised framework that tackles RIS by decomposing it into three steps: obtaining instance masks for the  object mentioned in the referencing instruction (\textit{segment}), using zero-shot learning to select a potentially correct mask for the given  instruction (\textit{select}), and bootstrapping a model which allows for fixing the mistakes of zero-shot selection (\textit{correct}). In our experiments, using only the first two steps (zero-shot segment and select) outperforms other zero-shot baselines by as much as 16.5\%, while our full method improves upon this much stronger baseline and sets the new state-of-the-art for weakly-supervised RIS, reducing the gap between the weakly-supervised and fully-supervised methods in some cases from around 33\% to as little as 7\%.\blfootnote{$^*$Work primarily done during FE's internship at Five AI Ltd.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a weakly supervised method for referring image segmentation. Starting from class-agnostic object proposals, the proposed method first extracts masks corresponding to the object class which is referenced by the given text, using the open-vocabulary segmentation technique. Then, select the actually referenced mask using the existing zero-shot prompting method. Finally, to refine the obtained mask, the authors propose a correction method by using the assumption that they know if the two references indicate the same object or not. The proposed method obtains better performance than the existing methods.

### Strengths
+ This paper addresses important problem that can effectively reduces the annotation cost for referring image segmentation.

+ The paper is overall well written.

### Weaknesses
- My major concern is that the proposed method is significantly overfitted to specific datasets.

-- First, the correction method in Section 3.3 requires a significantly strong assumption. The authors assume that multiple references tend to indicate a single object (mask), and they know which references actually correspond to the same mask. However, this assumption will not work for another dataset, and especially, knowing whether two references point to the same object or not is infeasible for a weakly supervise setting.

-- If I understood correctly, dataset class projection in Section 3.1 is to determine which class among the 80 classes in COCO corresponds to the key noun. The COCO class list is carefully curated by human, and each of the 80 classes is mutually exclusive. In the real open-world setting, assuming the specific set of classes is infeasible.

- My second concern is the novelty. Methods for obtaining object proposals, and matching those proposals with zero-shot prompting, are already well-explored techniques for the same research field.

- More baselines should be included.

-- GroundingDINO already conducted referring object detection. GroundingDION + SAM can be directly used for referring image segmentation. 

-- For a fairer comparison with Yu et al, FreeSOLO+Select method without Grounding DINO.

-- SAM Proposals (w/o Grounding DINO) + ReverseBlur prompting

### Questions
- Why testB performance is signifcantly lower than that of testA? 

- Excepting the correction method, please include the ablation studies on zero-shot validation and test sets for all datasets.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a weakly supervised framework for the task of referring image segmentation.
It contains three major components:  a segment component obtaining instance masks for the object mentioned in the referencing instruction, a select component using zero-shot learning to select the correct mask for the given instruction, and a correct component bootstrapping a model to fix the mistakes of zero-shot selection.
Further experiments show good performance compared to previous methods.

### Strengths
+ The paper is easy to follow. 
+ The performance is good in zero-shot and weakly supervised setup.

### Weaknesses
- The paper is a good engineering work, but lacks of enough novelty.
- The experiment is incomplete and not convincing.
- It lacks enough ablation studies on the effectiveness of each components used.
- It lacks enough details on the pre-training bootstrapped model.
- It lacks enough reference and comparison to previous methods.

### Questions
What is the major contribution of the proposed framework, since all components are borrowed from existing work?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a framework for weakly supervised referring segmentation. It includes 3 steps, open-vocabulary segmentation, selection based on the CLIP model, and correction with a constrained greedy matching mechanism. The intuition behind the idea is interesting. Very strong performance is also obtained.

### Strengths
+ The use of CLIP for zero-shot matching is sensible. 

+ The overall learning process in step 3 is interesting. It is fully exploiting the dataset information: referring expressions for the same object should lead to the same mask, while  referring expressions for different objects should lead to different mask. 

+ The obtained performance is strong.

### Weaknesses
-  Notations are not well defined, making it really difficult to understand the details some sections. For example,  in {m^c_{i,j,k} }^c, it is really confusing what 'c' means here.  

-  In general, I can appreciate the general idea of the learning mechanism for step 3.  It is really difficult to understand the equation (2) and (3). The reason could be unclear definitions, such as 'c'. Probably there are other undefined notations. 

- Fig.1 fails to provide the basic intuition of the third step, which, in my opinion, is the most valuable part of this paper.

### Questions
- In the ABLATION part, some experiences are based on the training set of the dataset (Table 2 & Table 3). What is the performance on the val and test sets? 

- Stage 3 is designed to correct the mistakes of the zero-shot choice with weak information. Why not use this information directly in stage 2 but take an extra large grounding model from LAVT?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a straightforward pipeline for referring image segmentation through only language sentences. The pipeline is designed to be trained with only images and sentences without masks. To this end, the authors proposed a pipeline of three stages, that is segment, select, and correct, with existing foundation models, such as CLIP, SAM, etc. Experimental results somewhat demonstrate the effectiveness of the proposed method.

### Strengths
The setting is interesting. The proposed pipeline is straightforward and in some perspective shows the power of the combination of existing foundation models.

### Weaknesses
This paper is a bit difficult to read. It abusively uses colorful dots to represent almost everything, including results, modules, and stages, which heavily hinders reading. This proposed pipeline is a straightforward combination of existing foundation models, what's the insight beyond the combination? In addition, some important key details about the correction stage are not clear, which requires further explanation.

### Questions
1. How do you get m^hat and m^c, is the m^hat output of LAVT? In addition, as the authors mentioned in sec3.3, the ZSBootstrap uses LAVT architecture, why the LAVT trained with texts and their pseudo visual masks work better and serve as an error correction model? 

2. What does "grounding" mean exactly? What's the difference between referring instance segmentation and grounding? I found the authors use them two both in the paper. 

3. Since LAVT is already a referring segmentation method, the authors re-trained it. Does that mean stage 1 and 2 are not valuable once the zsbootstrap model is trained?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
