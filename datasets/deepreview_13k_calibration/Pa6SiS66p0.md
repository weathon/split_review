# Beyond Unimodal Learning: The Importance of Integrating Multiple Modalities for Lifelong Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
While humans excel at continual learning (CL), deep neural networks (DNNs) exhibit catastrophic forgetting. A salient feature of the brain that allows effective CL is that it utilizes multiple modalities for learning and inference, which is underexplored in DNNs. Therefore, we study the role and interactions of multiple modalities in mitigating forgetting and introduce a benchmark for multimodal continual learning. Our findings demonstrate that leveraging multiple views and complementary information from multiple modalities enables the model to learn more accurate and robust representations. This makes the model less vulnerable to modality-specific regularities and considerably mitigates forgetting. Furthermore, we observe that individual modalities exhibit varying degrees of robustness to distribution shift. Finally, we propose a method for integrating and aligning the information from different modalities by utilizing the relational structural similarities between the data points in each modality. Our method sets a strong baseline that enables both single- and multimodal inference. Our study provides a promising case for further exploring the role of multiple modalities in enabling CL and provides a standard benchmark for future research.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a multi-modal continual learning benchmark.  Further, this paper also provides a simple baseline by incorporating the knowledge contained in different modalities to achieve better multi-modal continual learning with less forgetting on previously learned tasks. Experiments on a visual and audio modality continual learning dataset show the effectiveness of the proposed method compared to standard experience replay.

### Strengths
* The paper is easy to follow.

* This paper provides a baseline of multi-modal continual learning and benchmark.

### Weaknesses
 * The proposed method is straightforward with experience replay and those techniques are commonly used in existing multimodal learning and continual learning literature. 


* The memory buffer includes multi-modal examples from previous tasks.  The authors store the same number of data for single-modality and multi-modality. It would be better to compare different modality methods in terms of the same memory storage since multi-modality memory data requires more storage to store multi-modality data.


* The baseline is too weak, only the standard experience replay is compared. It would be better to compare to more recent state-of-art baselines in experience replay.  


* Furthermore, there are other categories of CL methods, including regularization-based methods and architecture-based methods. It would be better to also compare those methods in the experiment. 


* The experiments are only performed on visual and audio modality. It would be better to provide experiment and benchmark on other modalities as well, e.g., language.

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new benchmark based on the VGGSound dataset for multimodal (visual-audio) continual learning (CL). 

The authors show complementary aspects with the results of analyses on the dataset to highlight the advantageous points of integrating multiple modalities of visual and audio. 

Also, the paper presents a method for integrating and aligning information from multiple modalities using relational structural similarities, which seems to induce more robust representations to reduce catastrophic forgetting in deep neural networks.

### Strengths
- The authors introduce novel benchmark datasets for multimodal CL on vision and audio. If publicly available, it would be valuable and helpful for our communities to provide one of the standardized frameworks for evaluating the performance of models and facilitating fair comparisons between different methods in visual-audio multimodal CL settings.


- The paper presents empirical evidence supporting the complementary benefits of integrating multiple modalities of vision and audio. It seems to have better representations to be robust to reduce catastrophic forgetting.

### Weaknesses
 - The paper shows the main experimental results of the proposed method, SAMM (Semantic-aware multimodal method), in Table 1~2. I think that the performances of other methods reported in major references such as [Buzzega et al., NIPS20] or [Arani et al., PAMI 2022] seem to be compared. Since lack of comparison, it is NOT clear to figure out the effectiveness and uniqueness of the proposed method among other methods.

- The paper does NOT provide enough information (including data composition, details on evaluation, and experimental settings) to reproduce the results in the experiments, even though Appendix A.2~A.4 presents some information. For example, the specific splits of the VGGSound dataset used for the continual learning tasks are not clearly defined, nor are the exact hyperparameters used for training each model. The absence of these crucial details makes it difficult to independently verify the reported results and assess the robustness of the proposed method.

- It seems weak as a paper to propose a new dataset. Because it needs to provide baseline performances to show the characteristics of the dataset. On the other hand, it seems weak as a paper to propose a novel method for continual learning for visual-audio multimodal settings since it does not clearly validate the pros and cons of the proposed method. The paper does not sufficiently explore the limitations of the proposed SAMM method, such as its sensitivity to hyperparameter choices or its performance under different task sequences. A more thorough analysis of these aspects is needed to fully understand the method's strengths and weaknesses.


-- Minor
- 5th line on page 5, models a capture --> models to capture?
- caption in Figure 4, leverages leverage --> leverages?
- lines in Figure 3, it would be better to draw with line styles (solid, dotted, ... ). It is not easy to discriminate in gray-color printing.

### Questions
- Is there any reason to compare with only ER?

- What is the motivation to introduce relational structural similarity into the proposed models?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an under-explored problem --- leveraging multiple modalities for lifelong learning. Towards this end, the authors (1) provide a benchmark for this task, sourced from VGGSound; (2) conduct a case study demonstrating the advantages of using multiple modalities over a single modality; (3) develop an approach to leverage relational structural information in each modality for better integration of multimodal information.

### Strengths
+ The proposed benchmark covers three CL scenarios and can be beneficial to the community. 
+ The analysis in Section 3 makes sense and provides empirical evidence for the superiority of multiple modalities over single modality in CL.
+ The paper has good motivation and is well organized.

### Weaknesses
My major concern with this paper is the lack of comparison and experiments. The evaluation seems a bit weak to me as all the experiments are conducted on VGGSound only, and the baseline Experience Replay for comparison with the proposed approach is from 2018. I wonder if the authors could apply some more recent unimodal CL approaches ([1][2] etc.) to the problem.

[1] SS-IL: separated softmax for incremental learning   
[2] Class-incremental learning by knowledge distillation with adaptive feature consolidation.

---
Also, in terms of comparison with multimodal CL approaches:
+ (1) Could the authors further clarify why the proposed approach can not be applied to vision-language? What is the advantage of the proposed benchmark compared with [3], besides the modality difference? 
+ (2) I understand that [4] is published after the submission ddl, but it would be good if the authors could comment a few sentences about the differences with them in the rebuttal.  

[3] Climb: A continual learning benchmark for vision-and-language tasks.  
[4] Audio-Visual Class-Incremental Learning

---
For the semantic-aware feature alignment, I wonder if the authors can provide some visualization examples to demonstrate that the model indeed learns the desired modality-specific features, such as Figure 4 in [5].

[5] The Modality Focusing Hypothesis: Towards Understanding Crossmodal Knowledge Distillation

---
Typo, Figure 4 caption, "leverage leverages"

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
