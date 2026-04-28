# SegLLM: Multi-round Reasoning Segmentation with Large Language Model

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We present SegLLM, a novel multi-round interactive reasoning segmentation model that enhances LLM-based segmentation by exploiting conversational memory of both visual and textual outputs. By leveraging a mask-aware multimodal LLM, SegLLM re-integrates previous segmentation results into its input stream, enabling it to reason about complex user intentions and segment objects in relation to previously identified entities, including positional, interactional, and hierarchical relationships, across multiple interactions. This capability allows SegLLM to respond to visual and text queries in a chat-like manner. Evaluated on the newly curated MRSeg benchmark, SegLLM outperforms existing methods in multi-round interactive reasoning segmentation by over 20%. In addition, SegLLM obtains a 5.5% improvement in cIoU for standard single-round referring segmentation and a 4.5% increase in Acc@0.5 for referring expression comprehension.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes SegLLM a new Multimodal Language Model capable of performing multi-turn segmentation tasks based on language inputs. The paper introduces two new mechanisms to ease the multi-turn segmentation by allowing the LLM to get mask and bounding box tokens as inputs. This mechanisms allows the LLM to understand multi-turn instructions that can refer to previously predicted masks. Along with the method, the paper is paired with a new dataset to train multi-turn segmentation tasks. The dataset was created automatically by using current single-turn datasets and leveraging the capabilities of Language Models to adjust input prompts.
The results show that SegLLM is capable of solving multi-turn segmentation better than other alternatives, while also improving at single-turn segmentation benchmarks.

### Strengths
The paper is really well presented and written. The ideas are clear and the problem that the paper is trying to solve is clear from the get go. 
The method is also clear and simple to understand, while still being technically sound. The validation of the method using the self-created dataset and benchmark is also a great contribution for the community. The ablation studies are solid and conclusive and validate the design choices.

### Weaknesses
1. Methods like LISA employ LoRA for fine-tuning; does this paper adopt a similar approach? If not, could the observed performance improvement over LISA be attributed to a more advanced fine-tuning strategy? Specifically, the paper should detail the fine-tuning process, including the learning rate, batch size, and number of epochs. It is crucial to understand if the performance gain is due to architectural innovations or simply a more optimized training regime. A comparison of training parameters with LISA would be beneficial.
2. The paper lacks an ablation study with masks and bounding boxes separately as inputs, and it is unclear whether using points or drawing trajectories as prompts would be viable. The absence of such an ablation makes it difficult to assess the individual contribution of each input modality. For example, it's unclear if the model benefits more from the precise boundary information provided by masks or the more general region information from bounding boxes. Furthermore, the paper should explore the model's response to point prompts, which are common in interactive segmentation, and trajectory prompts, which could offer a more intuitive way for users to guide the segmentation process. 
3. There are minor errors in the text, such as on lines 427–428 and line 470.

### Questions
There are a few aspects of the paper that were not entirely clear to me, and I would appreciate some clarifications:

1. **Metric for Multi-turn Segmentation**:
   - Is the goal of multi-turn segmentation to segment only the object referred to in the final turn, or is the model expected to get each intermediate step correct as well?
   - Additionally, does each turn in the multi-turn setup refer to only one instance at a time?

2. **Evaluation of Baselines on MR-RefCOCO Dataset**:
   - How were the baselines evaluated on the proposed MR-RefCOCO dataset? I did not see details on whether the baselines were trained using the same training split as SegLLM.
   - If the training split was not used to refine these methods, could this weaken the strength of some conclusions? For instance, if SegLLM’s robustness to query diversity is largely due to the dataset rather than the model itself, wouldn't training LISA on this dataset also equip it with similar robustness?
   - This additional context would also clarify the performance gap observed between previous methods and the proposed one.

3. **Ablation Study Execution**:
   - Although the ablation study results look good numerically, I find some of the details around execution unclear. For example, how does SegLLM perform multi-turn segmentation without the module that enables it to "see" previously segmented masks?
   - Without access to these masks, how would the model handle queries that refer back to prior segmentations? More details on how the model operates without these critical components would make this section much clearer.

4. **Multi-turn Segmentation by Other Methods**:
   - Related to the previous question, how do other methods in this study perform the task without mechanisms to refer to previously segmented masks?
   - Do you feed an image back into the model with the segmented instance painted in? If so, could you provide more details on this approach?


I would love to hear these clarifications from the authors. I believe the paper is already very good, and making it crystal clear for the reader would make it a great work.

### Soundness
3

### Presentation
4

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
This paper introduces SegLLM, an advanced multi-round interactive segmentation model that improves LLM-based segmentation by incorporating conversational memory of past visual and textual outputs. Utilizing a mask-aware multimodal LLM, SegLLM refines its inputs with previous segmentation results, allowing it to handle complex queries about object relationships across multiple interactions. Testing shows SegLLM outperforms existing methods in both interactive and single-round segmentation tasks.

### Strengths
1. This paper proposes a multi-round reasoning segmentation task, which extends the boundaries of traditional reasoning segmentation and introduces new avenues for exploration within the community.
2. The paper presents the SegLLM model, which supports both bounding box and mask inputs, expanding the capabilities of large segmentation models. For the multi-round reasoning segmentation task, the authors carefully designed special tokens and a corresponding mask decoder. These modifications, in my view, represent an extension of the LISA paradigm with practical significance.
3. The paper constructs a multi-round reasoning segmentation dataset, drawing from diverse sources and following a well-designed pipeline, thus advancing research in this area through a robust data contribution.
4. The experiments are thorough, showcasing the task’s difficulty while effectively validating the proposed modules.

### Weaknesses
1. Methods like LISA employ LoRA for fine-tuning; does this paper adopt a similar approach? If not, could the observed performance improvement over LISA be attributed to a more advanced fine-tuning strategy?
2. The paper lacks an ablation study with masks and bounding boxes separately as inputs, and it is unclear whether using points or drawing trajectories as prompts would be viable.
3. There are minor errors in the text, such as on lines 427–428 and line 470.

### Questions
Will the code, dataset, and details on data processing be made open-source?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces SegLLM, an advanced interactive reasoning segmentation model that leverages **multi-round dialogue capabilities** in Large Language Models. SegLLM outperforms existing models by enhancing interactional reasoning and memory retention, demonstrated on a new benchmark, MRSeg, with substantial gains in accuracy metrics.

### Strengths
1. This paper proposes a novel integration of mask-aware LLMs for segmentation, enabling iterative, memory-based multi-round interactions.

2. SegLLM outperforms state-of-the-art segmentation models like LISA with significant performance margins across single and multi-round tasks.

3. Paper provides a comprehensive MRSeg dataset, structured for interactional and hierarchical segmentation tasks.

4. Paper demonstrates robustness against diverse question templates, improving the practical applicability of multi-modal conversational AI.

### Weaknesses
1. Using vision prompts for referring segmentation is a good approach. However, I would like to see a more comprehensive ablation study in Table 7 of the main paper, exploring the effects of different types of vision prompts, such as using only the mask encoder or only the bounding box encoder.

2. It would be valuable to understand the performance impact of directly using the `[SEG]` token from the previous round as the visual prompt for the current round. This approach might reduce the computational overhead introduced by the mask and bounding box encoders.

Minor Comment: Typically, table captions are placed at the top rather than the bottom of the table.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
