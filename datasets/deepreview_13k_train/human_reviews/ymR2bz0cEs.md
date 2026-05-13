# Interaction-centric Hypersphere Reasoning for Multi-person Video HOI Recognition

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Human-object interaction (HOI) recognition in videos represents a fundamental yet intricate challenge in computer vision, requiring perception and reasoning across both spatial and temporal domains, espically in multi-person scenes. HOI encompasses humans, objects, and the interactions that bind them. These three facets exhibit interconnectedness and exert mutual influence upon one another. However, contemporary video HOI recognition methods focus on the utilization of disentangled representations, neglecting their inherent interdependencies. Our assertions are that these facets are inherently interdependent and that interactions hold essential semantic meaning in HOIs. In light of this, we propose an interaction-centric hypersphere reasoning model for multi-person video HOI recognition. Specifically, we design a context fuser to model the interdependencies among humans, objects and interactions. To encapsulates the semantic essence of video HOIs, our model adopts an interaction-centric hypersphere framework. Furthermore, to enable the model with the capacity for temporal reasoning, we introduce an interaction state reasoner module. Consequently, our model unravels the intricacies of HOI recognition and is felxiable for both multi-person and single-person scenarios. Empirical results on multi-person video HOI dataset MPHOI-72 indicates that our method surpasses state-of-the-art (SOTA) method by more than 15%. At the same time, on single-person datasets Bimanual Actions (single-human two-hand HOI) and CAD-120 (single-human HOI), our method achieves on par or even better results compared with SOTA methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel *Context Fuser* module leveraging the strengths of the CLIP and BLIP models, incorporates an *Interaction State Reasoner* module, and introduces *Interaction Feature Loss* to address the video Human-Object Interaction (HOI) problem.

### Strengths
The experimental results demonstrate superior performance over other methods on MPHOI-72 and CAD-120 benchmarks.

### Weaknesses
1. **Unfair Comparisons and Insufficient Ablation Studies:**
The primary weakness of the proposed method is the unfair comparisons with other video HOI methods and the lack of thorough ablation studies. The Context Fuser employs large Vision-Language Models (VLMs), CLIP and BLIP, pre-trained on big data. While ASSIGAN and 2G-GCN do not. In Table 1, removing Context Fuser results in a notable decline in $F_1@10$. This raises suspicions that the significant performance enhancement could be largely attributed to the text-image alignment capabilities inherent in large VLMs rather than the proposed Context Fuser. The performance is below the benchmark set by Qiao et al., 2020, in the absence of the Context Fuser. The paper lacks critical ablation studies to disentangle the contributions of the VLMs and the proposed method.
2. **Missing References:**
There is a relevant ICLR’23 paper you should refer to, Gao et al., ICLR’23. Gao et al, which also uses large VLMs for the HOI problem. Unlike fixed prompt used in Context Fuser, while Gao et al. delve into learnable prompts.
>Gao, K., Chen, L., Zhang, H., Xiao, J. & Sun, Q. Compositional Prompt Tuning with Motion Cues for Open-vocabulary Video Relation Detection. _ICLR_ (2023).

### Questions
A deeper ablation study focusing on the efficacy of the CLIP and BLIP parts within the Context Fuser is advisable. This would ascertain whether the observed improvements stem from the newly proposed module or merely from the integration of CLIP and BLIP.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an interaction-centric hypersphere reasoning model for multi-person video HOI recognition. To do this, a context fuser is designed to learn the interdependencies among humans, objects, and interactions; a state reasoner model on top of context fuser is used for temporal reasoning; an interaction-centric hypersphere is used to represent the manifold structure of HOIs. 

The model is flexible for multi-person or single-person videos. Experiments show the method outperforms the previous method by 22% F1 score on multi-person dataset, MPHOI-72 and the method performs similarly with existing methods on single-person dataset, Bimanual Actions and CAD-120.

### Strengths
- The paper proposes an interaction-centric hypersphere representation scheme for HOI recognition learning.
- The method achieves SOTA performance with
a huge improvement of more than 22% F1 score over existing methods.

### Weaknesses
 - The main focus of the paper is HOI recognition for multi-person videos. In the experiment, there is only 1 multi-person dataset used for evaluation but 2 single-person datasets. Showing model performance on different multi-person datasets will help strength the claims in the paper.
- After reading the paper, there is still a lack of proof or explanation about why an interaction-centric hypersphere will help in the task theoretically. The ablation study does not show an ablation study on it.

### Questions
- In the method, the context fuser and interaction state reasoner extract CLIP features for the representation. Ablation on the features is necessary to test if the feature is important or over-complex where a simple binary feature is enough. For example, in the interaction state reasoner, the two possible states “continue” and “stop” can be represented by binary labels or simpler features of lower dimensions compared with CLIP.
- In 4.3.1 Model inference, during model inference, the interaction probability is predicted on each frame. It is not clear who is in interaction if there are multiple people in the video. Interaction prediction for each person is more detailed and straightforward.
- Based on the question above, ablation studies with methods of HOI detection on images are necessary. HOI detection can detect interaction for each person. If there are multiple people, the results for comparison from the HOI detection is whether there is any interaction from all people or not.
- In the Conclusion Sec, it mentions that the method outperforms SOTA on the multiple-people dataset but is on par with the single-person dataset. Is it because in the single-person video, there is only one person so the interaction prediction is determined by that single person? But for multi-person videos, the model does not need to predict correctly for each person to get the correct answer for the image.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an interaction-centric hypersphere reasoning model for multi-person video HOI recognition. The design of interaction-centric hypersphere explicitly directs the learning process towards comprehending the HOI manifold structures governed by interaction classes, a hitherto unexplored domain.

### Strengths
The method proposed in the paper is interesting.

### Weaknesses
The experimental evaluation is not comprehensive. 
The presentation for some key concepts and ideas is unclear, which needs extensive improvement.

Presentation:
1. The definition of the task is unclear. What is multi-person video HOI recognition? How to understand multi-person interaction and what is the specific expression? If it is multi-person interaction, what is the difference from the research direction of group action recognition? This work is anchored to explore multi-person interactive action recognition, so please clearly describe the task content and specific input and output.

In addition, regarding the definition of the task of this article, I have some idea until the fourth section. The previous sections do not elaborate on it, which is very good for understanding.

2. Why it is called a hypersphere? What is the meaning of hypersphere and does it have any theoretical implications? Hypergraphs and graphs are different theories. In this paper, what is the difference between the concept of a hypersphere and a sphere?

“The design of interaction-centric hypersphere explicitly directs the learning process towards comprehending the HOI manifold structures governed by interaction classes, a hitherto unexplored domain.” This hypersphere appears to be used to predict interaction probabilities. Please explain how it differs from traditional classifiers? This explanation is necessary since this hypersphere is the key idea. In addition, there is not much comparison, description, and argumentation between manifold structures and hypersphere theories in this paper. On the contrary, other modules explain more, which makes me wonder what is the core of the paper.

3. What are the HOI manifold structure, which has been mentioned several times in this paper? It is hard to understand. Is it related to Riemannian geometry? Please elaborate it. It is better to have a clear explanation.

4. ”To enhance the awareness of complex HOI structures in our representations, we introduce the Context Fuser (CF)...” Is there any connection between complex HOI and multi-person HOI?

5. “To facilitate interaction reasoning, we place the ISR module on top of the context fuser module, yielding entity representations capable of capturing interaction transition dynamics.” Does entity representation represent the characteristics of human and object entities? Or does it represent the transition characteristics of the same person or object between different states?
This sentence confuses me a lot about what exactly it represents.

6. “However, current video HOI recognition methods do not fully explore such inherent structural nature of HOI components. Instead, they often opt for disentangled representations for each component, which may have suboptimal representation capabilities.” It is recommended to visualize the problem to be solved, so that readers can understand it clearly.

7. In Figures 2 and 3, it is better to replace the letters with specific features. Using a large number of letters is too unintuitive and makes it difficult for readers to understand.

8. “We follow 2G-GCN to extract feature of humans and objects from backbone network”.
You used 2G-GCN to capture features, but the input {vt}t=1T seems to be a clip. Is the input of 2G-GCN a video? The output is the characteristics of people and objects in each frame of the video? Do ZH and ZO represent the characteristics of people and objects in each frame, or the characteristics of the entire video? I'm totally confused.

Experiments:
1. Although three datasets are compared, the algorithm is not fully verified. Why the VidHOI dataset is not used for comparison? This is a well-known video-based human-object interaction dataset.

2. There are no comparisons for this hypersphere module in the ablation experiments. It's the key component that needs comparative validation.

### Questions
Presentation:
1. The definition of the task is unclear. What is multi-person video HOI recognition? How to understand multi-person interaction and what is the specific expression? If it is multi-person interaction, what is the difference from the research direction of group action recognition? This work is anchored to explore multi-person interactive action recognition, so please clearly describe the task content and specific input and output.

In addition, regarding the definition of the task of this article, I have some idea until the fourth section. The previous sections do not elaborate on it, which is very good for understanding.

2. Why it is called a hypersphere? What is the meaning of hypersphere and does it have any theoretical implications? Hypergraphs and graphs are different theories. In this paper, what is the difference between the concept of a hypersphere and a sphere?

“The design of interaction-centric hypersphere explicitly directs the learning process towards comprehending the HOI manifold structures governed by interaction classes, a hitherto unexplored domain.” This hypersphere appears to be used to predict interaction probabilities. Please explain how it differs from traditional classifiers? This explanation is necessary since this hypersphere is the key idea. In addition, there is not much comparison, description, and argumentation between manifold structures and hypersphere theories in this paper. On the contrary, other modules explain more, which makes me wonder what is the core of the paper.

3. What are the HOI manifold structure, which has been mentioned several times in this paper? It is hard to understand. Is it related to Riemannian geometry? Please elaborate it. It is better to have a clear explanation.

4. ”To enhance the awareness of complex HOI structures in our representations, we introduce the Context Fuser (CF)...” Is there any connection between complex HOI and multi-person HOI?

5. “To facilitate interaction reasoning, we place the ISR module on top of the context fuser module, yielding entity representations capable of capturing interaction transition dynamics.” Does entity representation represent the characteristics of human and object entities? Or does it represent the transition characteristics of the same person or object between different states?
This sentence confuses me a lot about what exactly it represents.

6. “However, current video HOI recognition methods do not fully explore such inherent structural nature of HOI components. Instead, they often opt for disentangled representations for each component, which may have suboptimal representation capabilities.” It is recommended to visualize the problem to be solved, so that readers can understand it clearly.

7. In Figures 2 and 3, it is better to replace the letters with specific features. Using a large number of letters is too unintuitive and makes it difficult for readers to understand.

8. “We follow 2G-GCN to extract feature of humans and objects from backbone network”.
You used 2G-GCN to capture features, but the input {vt}t=1T seems to be a clip. Is the input of 2G-GCN a video? The output is the characteristics of people and objects in each frame of the video? Do ZH and ZO represent the characteristics of people and objects in each frame, or the characteristics of the entire video? I'm totally confused. 

Experiments:
1. Although three datasets are compared, the algorithm is not fully verified. Why the VidHOI dataset is not used for comparison? This is a well-known video-based human-object interaction dataset.

2. There are no comparisons for this hypersphere module in the ablation experiments. It's the key component that needs comparative validation.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focused on video HOI recognition and proposed a hypersphere-based method to learn the interdependency between humans, objects, and interactions. The authors proposed several modules like CF, ISR, and BiGRU to build a new pipeline to learn complex spatio-temporal video HOIs. On three benchmarks, the proposed method was evaluated and compared with previous works and showed improvements.

### Strengths
+ The complex relations within video HOIs are a meaningful problem for intelligent visual understanding, using hypersphere is an interesting attempt.

+ The whole paper is written well and easy to follow.

### Weaknesses
 - Some design choices were not well illustrated and verified, which will be detailed in the questions.

- Some claims are ambiguous, please give more explanations:

usually lack of ability to capture global context information: which works and why?

ultimately compromising their representational accuracy: what is representational accuracy? Why Euclidean cannot?

### Questions
1. Why choose the hypersphere? Its pros upon Euclidean? Maybe discussions and experiments for support.

2. Each class has its own hypersphere, then how to embed the relations between classes, e.g., holding and grasping? Is the current setting reasonable?

3. How to handle the multi-label classifications given hyperspheres, and the long-tailed bias?

4. Discussion about the temporal action localization or segmentation? And some possible comparison between this line of works?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
