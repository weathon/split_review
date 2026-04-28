# Weakly-supervised 3D Referring Expression Segmentation

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 5, 3

## Abstract
3D Referring Expression Segmentation (3D-RES) aims to generate precise segmentation masks for targets based on free-form text descriptions. Despite significant advancements, current methods still rely on costly point-level mask-description pair annotations. In this paper, we introduce the Multi-Expert Network (MEN), a novel weakly supervised framework that utilizes the multimodal alignment of vision-language models across various semantic cues to reveal the relationships between descriptions and 3D instances. The primary challenges lie in effectively extracting and matching visual and textual context, while eliminating potential distractions. To address this, we propose the Multi-Expert Mining (MEM) and Multi-Expert Aggregation (MEA) modules. The MEM module employs multiple experts to extract semantic cues from full-context, attribute, and category dimensions. The MEA module mathematically consolidates the outputs of these experts, automatically assigning greater weight to more accurate ones, thus improving target selection accuracy and robustness. Extensive experiments on the ScanRefer and Multi3DRefer benchmarks demonstrate the effectiveness of our method in addressing the challenges of weakly supervised 3D-RES.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a weakly supervised 3D-RES task and the Multi-Expert Network (MEN), an innovative framework that aims to mitigate the reliance on costly annotations by leveraging diverse complementary visual-language cues. MEN consists of two core modules: the Multi-Expert Mining (MEM) module and the Multi-Expert Aggregation (MEA) module. The MEM module employs multiple visual-language experts to independently mine distinct visual and linguistic cues, aligning visual and textual contexts from three complementary perspectives. Meanwhile, the MEA module synthesizes the outputs of these experts through a distribution-based fusion approach, adaptively assigning appropriate fusion weights to enhance integration. Extensive experiments on the ScanRefer and Multi3DRefer datasets underscore the efficacy of this approach for the weakly supervised 3D-RES task.

### Strengths
1、	The high cost of obtaining annotations in the 3D domain has been a significant barrier to progress in related fields. Thus, this work’s proposal of a new weakly supervised 3D-RES task, aiming to reduce dependency on 3D annotations, is highly valuable and offers a fresh direction for advancing the community's development.

2、	Additionally, this paper introduces a novel weakly supervised 3D-RES framework, MEN, to address the weakly supervised 3D-RES task, providing a strong baseline. The incorporation of a multi-expert fusion approach into the 3D-RES task is also innovative and noteworthy.

3、	The proposed MEM module in this paper effectively explores different visual-language relationships by leveraging three complementary cues: Full-context, Attribute, and Category.

### Weaknesses
1、	Lines 202-205 lack a detailed and clear description of visibility. Additionally, some symbol notations in the text are ambiguous; for instance, the "textual full-context feature" mentioned in line 215 is referred to as "2D-fine text features" in line 199. The description of visibility should specify how the projected points are determined and what criteria are used to consider a point as visible, especially given potential occlusions or partial views. Furthermore, the inconsistent terminology between "textual full-context feature" and "2D-fine text features" suggests a lack of precision in defining the feature extraction process, which could confuse readers about the exact nature of the input to the model.

2、	The proposed method demonstrates high performance on traditional 3D-RES tasks; however, it exhibits lower performance on certain metrics in the 3D-GRES task, particularly in zero-target scenarios. What factors contribute to this underperformance, and are there potential improvements that could be implemented? The paper should delve deeper into the reasons for this performance disparity, analyzing whether the model's architecture or training process is less effective in handling zero-target cases. It is crucial to understand if the issue stems from the model's inability to distinguish between background and zero-target instances or if the fusion mechanism is not adequately handling the absence of a target.

3、	This two-stage paradigm is influenced by the proposals generated in the first stage. Therefore, how would the overall performance of the network change if a different instance segmentation model were utilized in the first stage? The paper should provide a more detailed analysis of how the quality of instance segmentation proposals affects the final 3D-RES performance. It is important to understand the sensitivity of the proposed method to the quality of the initial proposals, as this could limit its applicability in scenarios where high-quality instance segmentation is not readily available.

4、	Furthermore, I would like to see the performance upper bound of the network when errors from the first-stage segmentation model are excluded. This would help to understand the inherent limitations of the proposed method, independent of the performance of the instance segmentation model. It's crucial to determine how much room there is for improvement in the 3D-RES task itself, assuming perfect instance segmentation.

### Questions
1、	This paper utilizes an off-the-shelf natural language parser to extract attribute-level text, which can be understood as a standard approach. However, I am quite curious whether employing a powerful large language model (LLM) to construct attribute phrases as text inputs for the attribute experts could further enhance the model's performance.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Multi-Expert Network (MEN), a weakly supervised framework for 3D Referring Expression Segmentation (3D-RES) that reduces dependency on costly annotations. MEN uses two modules: Multi-Expert Mining (MEM) to extract semantic cues from various dimensions and Multi-Expert Aggregation (MEA) to consolidate these cues.

### Strengths
Experimental results demonstrate MEN’s effectiveness in accurately segmenting 3D objects based on text descriptions, even with limited supervision, outperforming some fully supervised 3D-RES methods.

### Weaknesses
1. The paper lacks a discussion of related works, specifically on open-vocabulary 3D segmentation. Open-vocabulary 3D segmentation techniques utilize open-vocabulary queries (such as class labels or text queries) to segment 3D objects. These approaches can be adapted for weakly supervised 3D referring segmentation by replacing open-vocabulary queries with referring expressions. For example, methods [A-C] could be applied to weakly-supervised 3D segmentation tasks similar to those proposed in this paper, as their models operate without manual 3D annotations or can produce 3D segmentation results in a zero-shot manner. Including these methods in the related work discussion or comparing them in the experiments would strengthen the paper.
2. Methods [A-C] are capable of handling weakly-supervised 3D referring segmentation.
3. The writing is hard to follow, particularly in Lines 294-323. For instance, the phrase in Line 299, “Then &(P1, …, Pn) exists,” lacks clarity, making its intent unclear. Furthermore, Eq. (13) includes a parameter $\sigma_x$, which is missing in Eq. (14).
4. The symbols in Eq. (11) are inconsistent with those in Figure 2. Eq (11) uses $\cdot$ to denote matrix multiplication, but Figure 2 uses $\otimes$.

Minor issue: 
Incorrect description in Figure 4(a): It appears that the target in Figure 4(a) is a table, not a couch, yet the descriptions for (a) and (b) are identical.

### Questions
In the category expert, if the class label can be directly extracted from the input text, why is a classifier needed for the text as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a weakly supervised 3D-RES task and introduces the Multi-Expert Network (MEN), a framework that leverages multiple cues for referring expression reasoning, reducing reliance on expensive mask-description pair annotations. The framework includes the Multi-Expert Mining (MEM) module, which aligns visual and textual contexts from three complementary cues, and the Multi-Expert Aggregation (MEA) module, which consolidates expert knowledge while filtering out interference to emphasize the target instance. Extensive experiments on the ScanRefer and Multi3DRefer datasets validate the effectiveness of our approach in addressing weakly-supervised 3D-RES.

### Strengths
1. Proposes a novel weakly supervised approach to handle 3D RES.
2. The paper is well-written and easy to understand.
3. Demonstrates impressive results across multiple metrics in the weakly supervised setting.

### Weaknesses
1. This pipeline processes each frame separately, however, target objects and anchors are not always present within the same frame due to the limited field of view. This slightly goes against the authors' statement in Lines 189-191: “The full-context expert focuses on... understanding the spatial relationships and the surrounding environment of the target.” The method's reliance on single-frame processing limits its ability to leverage temporal context and handle cases where the target and anchor are not simultaneously visible, potentially hindering its performance in complex scenes.
2. The proposed pipeline appears to struggle with cases containing zero targets, even in scenarios without distractors, as shown in Table 2. The method's inability to reliably identify zero-target scenarios, even in the absence of distractors, suggests a fundamental limitation in its object detection or reasoning capabilities, which could be due to the lack of explicit negative examples during training.
3. The ablation study in Table 3 is limited to evaluating the performance of individual modules. Specifically, it would be helpful to see the performance of samples in the "Unique" category. The absence of a detailed breakdown of performance on the "Unique" category limits the ability to understand the specific strengths and weaknesses of each module when dealing with single-instance target scenarios, making it difficult to assess the overall contribution of each component.

### Questions
1. How can one ensure that the methods effectively address the issues outlined in Weakness #1?
2. Have you considered adding a confidence threshold to allow the pipeline to handle scenarios with zero targets?
3. Could you provide the ablation studies mentioned in Weakness #3?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new weakly supervised 3D Referring Expression Segmentation task, along with a baseline method, named Multi-Expert Network (MEN), designed to address this task. The proposed task can potentially eliminate the need for laborious point-level mask annotations. The proposed method includes two main components: a Multi-Expert Mining module, which leverages various experts to extract and align visual and textual features from multiple complementary cues, and a Multi-Expert Aggregation module, which integrates the knowledge acquired from these experts.

### Strengths
1. The proposed 3D-RES task is well motivated.
2. The proposed MEN method is reasonable and all proposed modules are thoroughly ablated.

### Weaknesses
1. The proposed method employs SoftGroup as its instance segmentation backbone. However, since this model was trained on ScanNet data, there is a significant data leakage issue, as both evaluation datasets (ScanRefer and Multi3DRefer) were built using ScanNet. Despite this favorable evaluation setting, the method's performance remains substantially lower than fully supervised approaches. The performance would likely deteriorate further when applied to other datasets. Given that such a method is primarily intended for use in unseen environments, the poor generalization capability presents a major concern and undermines the core motivation of this work. An ablation using an alternative backbone trained on different data may help to alleviate this concern.
2. Based on Table 1, distilling MEN to fully-supervised methods does not improve performance in the "Multiple" and "Overall" settings. This outcome suggests that the segmentation masks obtained through this method are noisy and struggle to differentiate between multiple objects, rendering the supervision signal less effective. Table 2 further supports this observation, showing poor performance in both zero-target and multiple-target cases. These limitations imply that the model may lack the ability to accurately interpret referring expressions to distinguish between multiple objects. This raises the question of whether there is any difference between using referring expressions and class labels for training this model. An ablation study on this would help to clear the confusion.
3. The proposed method, while a commendable effort by the author, lacks elegance. It primarily represents a complex engineering solution that combines various existing approaches and models.
4. Typo: 
> 1. Line 201: Dimension of RGB-D should not be 3xWxH.
> 2. Line 255: textaul -> textual.
5. Paper has organizational issues. Many core details are not mentioned or put in the appendix.
6. The model cannot properly handle spatial relationships between objects. It processes frames one at a time and fails when objects referenced in the text appear in different frames. The authors' claim that this only affects 5% of cases is based on an extremely small number of examples (100) from their dataset. In real-world settings, where objects naturally appear across different viewpoints and spatial relationships are crucial, this architectural limitation would severely impact performance.

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
