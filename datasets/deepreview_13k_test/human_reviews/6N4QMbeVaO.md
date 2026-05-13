# MTSAM: Multi-Task Fine-Tuning for Segment Anything Model

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The Segment Anything Model (SAM), with its remarkable zero-shot capability, has the potential to be a foundation model for multi-task learning. However, adopting SAM to multi-task learning faces two challenges: (a) SAM has difficulty generating task-specific outputs with different channel numbers, and (b) how to fine-tune SAM to adapt multiple downstream tasks simultaneously remains unexplored. To address these two challenges, in this paper, we propose the Multi-Task SAM (MTSAM) framework, which enables SAM to work as a foundation model for multi-task learning. MTSAM modifies SAM's architecture by removing the prompt encoder and implementing task-specific no-mask embeddings and mask decoders, enabling the generation of task-specific outputs. Furthermore, we introduce Tensorized low-Rank Adaptation (ToRA) to perform multi-task fine-tuning on SAM. Specifically, ToRA injects an update parameter tensor into each layer of the encoder in SAM and leverages a low-rank tensor decomposition method to incorporate both task-shared and task-specific information.
Extensive experiments conducted on benchmark datasets substantiate the efficacy of MTSAM in enhancing the performance of multi-task learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes MTSAM (Multi-Task SAM), a framework that extends the Segment Anything Model (SAM) for multi-task learning. SAM's original architecture is limited to single-task applications due to its prompt encoder and uniform output channels. MTSAM addresses these limitations by modifying SAM’s architecture to accommodate task-specific outputs and by introducing Tensorized low-Rank Adaptation (ToRA) for multi-task fine-tuning. ToRA injects a tensor parameter into SAM’s encoder, allowing efficient handling of both shared and task-specific information. Extensive experiments on benchmark datasets (NYUv2, CityScapes, PASCAL-Context) show that MTSAM outperforms existing multi-task learning approaches, both qualitatively and quantitatively, in segmentation, depth estimation, and surface normal prediction.

### Strengths
1) MTSAM successfully extends SAM to a multi-task framework, a novel approach that leverages SAM's strong zero-shot capabilities in a multi-task setting.

2) The proposed ToRA method is parameter-efficient, enabling sublinear parameter growth and effective use of shared information across tasks.

3) The paper provides theoretical justification for ToRA’s superiority over existing methods like LoRA, adding credibility to its parameter efficiency claims.

4) MTSAM outperforms other multi-task learning models across three benchmark datasets, demonstrating its efficacy in varied visual tasks.

### Weaknesses
1) The current work lacks an evaluation of MTSAM’s zero-shot generalization ability, particularly on unseen data distributions. 

2) The experiments do not include a direct comparison with full fine-tuning methods, leaving it unclear whether MTSAM’s parameter-efficient fine-tuning can achieve competitive performance without compromising accuracy.

3) There is a lack of comparative experiments to demonstrate the effectiveness of task embedding. Further experiments are needed to confirm the specific advantages of task embedding in multi-task setups.

### Questions
I don't have particular questions. The concerns can be found on the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose the MTSAM, a multi-task segmentation model, which is based on the architecture of SAM. The researchers change the original prompt encoder and mask encoder of SAM into separate mask decoders for each downstream task, and introduce task embeddings to generate outputs with the corresponding number of channels, enabling the model can be adapted to various tasks. Otherwise, the researchers apply a low-rank tensor decomposition method to fine-tune the image encoder of MTSAM. different tasks. The proposed ToRA can use both task-shared and task-specific information during the multi-task fine-tuning process. The experimental results demonstrate the effectiveness of MTSAM.

### Strengths
There are several strengths of the paper: 
For originality, based on the original model structure of SAM, this work makes a simple, direct but effective modification. Inspired by the previous work, it also proposes the Tora, a novel multi-task PEFT method on the idea of low-rank tensor decomposition. It has made effective innovations on the basis of existing work.
For clarity, the writing of the article is smooth, and the formulas, figures, etc. are clear and unambiguous.
For quality, This work was carried out on the NYUv2, CityScapes, and PASCAL-Context, and the experiments are fairly convincing in terms of the results of the indicators presented.
For significance, this work migrates the excellent performance of SAM to multiple downstream tasks, which has certain significance for the further promotion of SAM.

### Weaknesses
The weakness of this paper lies in the following aspects:
1.The comparative advantages primarily focus on CNN-based methods, without analyzing more advanced approaches like SwinSTL. Additionally, the performance metrics compared to SwinSTL are not significantly superior.
2.The dataset metric configurations differ without adequate explanation. For instance, it is unclear why different evaluation metrics are applied to segmentation tasks across various datasets.
3.The results section insufficiently demonstrates the effectiveness of image multitasking, and the supplementary appendix provides limited image results.

### Questions
1.Could you provide a more detailed analysis of the advantages over advanced methods like SwinSTL? 
2.Can you clarify why different evaluation metrics are used for segmentation tasks or others across various datasets? What criteria were used to select these metrics?
3.Would it be possible to include more comprehensive examples of image multitasking in the results section?

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
3

### Summary
The paper proposes MTSAM, a multi-task learning framework that adapts the Segment Anything Model (SAM) for simultaneous execution of different computer vision tasks. By modifying SAM’s architecture and introducing a novel Tensorized low-Rank Adaptation (ToRA) method, MTSAM aims to optimize SAM's capabilities for multi-task scenarios, addressing task-specific output generation and efficient fine-tuning.

### Strengths
1.	The MTSAM framework successfully extends SAM’s architecture, enabling it to handle multiple downstream tasks, a significant improvement over SAM’s single-task limitations.
2.	ToRA offers a parameter-efficient fine-tuning solution that balances task-specific and shared information, enhancing performance without excessive resource requirements.
3.	Comprehensive experiments across benchmark datasets (NYUv2, CityScapes, and PASCAL-Context) demonstrate MTSAM's superior performance over existing methods in multi-task learning, indicating practical efficacy.
4.	The theoretical analysis of ToRA’s expressive power is well-presented and aligns with empirical findings, adding depth to the framework’s academic contributions.

### Weaknesses
1.	The first and second points in the summary of contribution points appear to be similar, the author is requested to provide good reasons for the significant difference, otherwise it is recommended to merge.
2.	It is hard for me to consider MTSAM as a substantial model innovation improvement, (1) I don't get why the prompt encoder affects the downstream adaptation of the model, (2) the author's improvement of the decoder is more like the integration of multiple decoders for different tasks.
3.	I am interested in ToRA, but the author's description of the details is unclear. (1) How to constrain U1, U2, and U3 to learn task-relevant and task-irrelevant information, respectively? (explain or experiment) (2) Why is the decomposition into U1+U2+U3+G just enough? What happens if there are more or less U's? What if there were G?
4.	The proposed ToRA lacks comparison with other LoRA-based improvement methods.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an interesting idea to make SAM multi-task capable. As mentioned by the authors (L201-204), despite SAM's success, it's end-to-end adaptability is limited by its prompt-guided paradigm. The paper proposes that one can learn multiple mask decoders, one per task, and then have a TORA (Tensorized Low Rank Adaptation) as opposed to say one LoRA per task to capture the task information. In some sense, the main show is actually TORA, for which the authors' motivation that all the tasks share information while having task-specific requirement makes sense. Experiments are sufficient to support the proposal.

### Strengths
- The multi-task challenge with SAM is indeed a real problem that many researchers faced. The original SAM would output multiple potential masks when the prompts are ambiguous which sometimes make it hard for practitioner to adapt it to multiple downstream tasks.
- The main show is TORA which the paper clearly presented why the final formulation is as given. I appreciate this clarity. In fact, I think ToRA can stand as a separate paper exploring its applicability in other problem domains, given that LoRA is a hotly researched topic currently.
- Moreover, ToRA has a lower complexity computational wise. This could be quite valuable when the number of tasks really scale up. I am curious about scaling up the number of tasks. 
- The regularization term in Eq 9 is interesting.

### Weaknesses
- Scaling-up experiments are lacking. Is there any way to see a larger number of tasks beyond 3-4? I really would like to stress test ToRA.
- Are there any out of domain experiments, same task but out of domain datasets?
- Are there any experiments on the speed? ToRA as described has a computational advantage but there does not seem to be any experiments to back that up, unless I missed them.
- Table 3 is slightly disappointing with LoRA-STL (r-32) beating MTSAM on some tasks. Not a show-stopper since overall performance seems ok.
- The qualitative examples need to be better. Resolution is very low and hard to tell. I know cityscapes are like that, but perhaps testing on some higher res samples would be more convincing.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4
