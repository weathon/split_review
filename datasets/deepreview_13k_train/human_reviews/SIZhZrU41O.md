# Video Diffusion Models Learn the Structure of the Dynamic World

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Diffusion models have demonstrated significant progress in visual perception tasks due to their ability to capture fine-grained, object-centric features through large-scale vision-language pretraining. While their success in image-based tasks is well-established, extending this capability to the domain of video understanding remains a key challenge.  In this work, we explore the potential of diffusion models for video understanding by analyzing the feature representations learned by both image- and video-based diffusion models, alongside non-generative, self-supervised approaches. We propose a unified probing framework to evaluate six models across four core video understanding tasks: action recognition, object discovery, scene understanding, and label propagation. Our findings reveal that video diffusion models consistently rank among the top performers, particularly excelling at modeling temporal dynamics and scene structure. This observation not only sets them apart from image-based diffusion models but also opens a new direction for advancing video understanding, offering a fresh alternative to traditional discriminative pre-training objectives. Interestingly, we demonstrate that higher generation performance does not always correlate with improved performance in downstream tasks, highlighting the importance of careful representation selection. Overall, our results suggest that video diffusion models hold substantial promise for video understanding by effectively capturing both spatial and temporal information, positioning them as strong competitors in this evolving domain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The proposed paper aims to evaluate video diffusion models with respect to their visual perception capabilities. To this end, it analyzes the feature representations learned by image- and video-based diffusion models in context of video understanding tasks like action recognition, object detection, scene understanding, and label propagation on datasets like UCF101, HMDB, MOVi-C, MOVi-E MOT, DAVIS, and JHMDB.

### Strengths
The topic if and how diffusion models are able to capture visual representations is of great interest. The topic is also very timely.

### Weaknesses
 - 1. Comparison to SoTA/RW:
Compared to the original DIFT paper, results in Tab 3. are below state-of-the-art and varying also with respect to DIFT baselines. Namely, DIFT (from Stable Diffusion) reports e.g. PCK@0.1=61.1 for JHMDB (PCK@0.1=60.48 for SD and PCK@0.1=60.52 for SDV in the paper), deviation for DAVIS is even worse.

- 2. Evaluation of video diffusion vs general visual foundation models?:
The evaluation considers three Video diffusion models(SVD, ModelScope, Open-Sora), and four other models (e.g. image diffusion, Dinov2, VJEPA). This is a bit irritating and not clarified in the evaluation table or the discussion. It would be better to account for those scenarios as well in the paper (e.g. by a comparative discussion of different representations based on different pretrainings etc.) 
Further, if the paper would care about video in the first place, why not test against more video models? While VJEPA is one possible backbone, it would be good to have a least a few more representatives like VideoMAEv1 or v2, InternVid, etc. 

- 3. Details about video probing:
The video probing is very superficially described (imho). As this is the most novel part of the paper, spending only 20 lines on this makes it challenging to understand what's really going on. I really tried to consider if the conclusion in the experiments make sense to me, but I always ended up with having the feeling that details are missing. Some were available in the experiments later, but it was hard to get a full picture. The paper should be more self-contained. 

- 4. Feature computation (line 299-303): 
It seems like the block index is chosen per model (which makes sense), but it is unclear based on which criteria. Was this optimized per model per task as shown in Tab. 4?

### Questions
There are some typos, e.g. line 290 "... and report xxx."

While I don't think that this would be a feasible improvement to do for this specific conference (bc it's mainly a new paper), some suggestions for a revision could be (adapted from what the OpenReview LLM proposed based on the weakness section, but nice anyway): 

- 1. Give a detailed background section about the original DIFT paper and directly address these discrepancies  (if there are any). Provide a detailed comparison and explanation for why your results differ, and discuss any implications this may have on your conclusions.

- 2. Clearly categorize the models in their evaluation tables (e.g., video diffusion models vs. other types) and discuss and provide a rationale for including non-video models in the analysis.

- 3. Explain your criteria for selecting the models included in the study, and consider expanding the analysis to include additional, prominent video models.

- 4. Provide a more comprehensive description of the video probing methodology in the main body of the paper. Include specific details on techniques used, implementation methods, and key parameters or settings.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper analyzed the capability of video diffusion model in video understanding tasks. They extracted features from diffusion model, and used these features to perform several video tasks, including action recognition, object discovery, scene understanding, and label propagation. Results show that video diffusion can achieve good results.

### Strengths
-The analyze of video diffusion models on understanding tasks is important.

### Weaknesses
-While the aim of using diffusion model in understanding tasks is appreciated, the designed method is not new compared to diffusion features (DIFT). This work is more like a technical report, and provides little insights.

-From the results on four tasks, I don't think video diffusion models have significant advantages compared to SSL models and image diffusion models, considering that they have been trained on vast videos. In action recognition, SVD actually performs similar to VJEPA. In object discovery, DINOv2 performs much better. In scene segmentation, DINOv2 and ModelScope are the best on two metrics. In label propagation, SVD/ModelScope performs similar to SD. Particularly, since SVD is extended from SD 2.1, while the performance gap between SD and SVD on object discovery, scene understanding, and label propagation is quite minor, considering the enormous training cost of SVD, I don't think it is promising.

--Minor, typo in line 232, zT, \epsilon^v\theta. Line 290, MOT17(), report xxx. Many depulicated sentences, e.g. Line 372-373 and Line 430-431.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
2

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
This paper focuses on analyzing the strengths and limitations of existing video diffusion models for different video understanding tasks. A probing framework is proposed to extract the video feature representations from existing pre-trained models and learn lightweight task heads for different downstream video understanding tasks.  Comprehensive experiments across six models and four downstream video tasks are conducted and some findings are demonstrated.

### Strengths
1) The investigation of different characteristics of image-/video-based diffusions is interesting and meaningful for the video-understanding community;
2) The proposed probing framework is technically sound and the experimental results are comprehensive.
3) The paper is well-written, making it easy to follow and understand.

### Weaknesses
1) Although many findings are demonstrated by the comprehensive results, **the reviewer finds these findings are well-known consensus in the video understanding community**. For example, modeling the human motion or object dynamics is important for analyzing the videos, it is straightforward that most video-based diffusions contribute their models to this problem. Therefore, for instance, the findings "video diffusion models demonstrate exceptional proficiency in capturing motion patterns and temporal dynamics" that the paper try to demonstrate, **cannot provide new insights to the community**;

2) The used video action recognition datasets, i.e., UCF and HMDB, actually do not require modeling too much temporal/dynamic semantics for recognition. To make the demonstration more convincing, the reviewer thinks experiments should be conducted on the action datasets that require effective temporal dynamics modeling (e.g., something v2, Kinetics).

minor issues:
1) the symbol zT in line #231 should be corrected;
2) the sentence in line #289~290 should be revised;

### Questions
please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper explores the adaptation of video diffusion models to fine-grained video understanding tasks, such as action recognition and object discovery. The authors conducted comparative experiments on several different video diffusion models and found that the spatiotemporal modeling of generative models can be effectively applied to video understanding tasks.

### Strengths
- The motivation and writing of this paper are very clear and easy to follow.
- The experiments are quite rich, comparing various feature extractors and multiple different tasks.

### Weaknesses
 - The novelty is somewhat limited, as the method in this paper is inspired by DIFT from the image domain. The extraction of visual features also follows its diffusion feature extraction approach.
- The method section lacks insights, mainly introducing and simply applying others' methods.
- Regarding the features and training methods, most of the approaches in this paper are fixed, i.e., they freeze the backbone and only tune the task head. Exploring features from different layers and fine-tuning more backbone parameters could be valuable and might improve the model's performance.
- Although this paper conducted experiments on multiple tasks, it did not achieve good results for each individual task. This limits the practical applications and impact of the paper.
- There is a lack of citations for some key literature, such as GenRec[1], which also explores the application of video diffusion models in action recognition and examines the performance on K400 and SSv2. In contrast, this paper only validates its results on the smaller datasets UCF and HMDB, which are not representative.

### Questions
See above in weakness .

### Soundness
2

### Presentation
2

### Contribution
2
