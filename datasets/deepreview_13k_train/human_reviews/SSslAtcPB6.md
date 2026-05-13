# ST-Modulator: Modulating Space-Time Attention for Multi-Grained Video Editing

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Recent advancements in diffusion models have significantly improved video generation and editing capabilities. However, multi-grained video editing, which encompasses class-level, instance-level, and part-level modifications, remains a formidable challenge. The major difficulties in multi-grained editing include semantic misalignment of text-to-region control and feature coupling within the diffusion model. To address these difficulties, we present ST-Modulator, a zero-shot approach that modulates space-time (cross- and self-) attention mechanisms to achieve fine-grained control over video content. We enhance text-to-region control by amplifying each local prompt's attention to its corresponding spatial-disentangled region while minimizing interactions with irrelevant areas in cross-attention. Additionally, we improve feature separation by increasing intra-region awareness and reducing inter-region interference in self-attention. Extensive experiments demonstrate our method achieves state-of-the-art performance in real-world scenarios. More details are available on the project page.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new task called multi-grained video editing, which includes class-level, instance-level, and part-level editing, and proposes a zero-shot approach, ST-Modulator, to address the challenge of distinguishing distinct instances (e.g., "left man" and "right man") by modulating space-time attention mechanisms for precise, fine-grained control over video content—all without additional training.

### Strengths
- The paper is well-written and organized, making complex concepts easy to understand.
- The Spatial-Temporal Layout-Guided Attention method in this paper effectively addresses the challenge of precise, multi-grained video editing by modulating cross- and self-attention. This approach enables accurate text-to-region control and clear feature separation, allowing independent edits to specific subjects while avoiding unintended changes in other areas, especially in complex multi-subject scenes.
- Compared to other approaches, ST-Modulator achieves high computational efficiency, showing lower memory usage and faster processing times.

### Weaknesses
 - Limited focus on background preservation. 
- In Figures 5 and 6, most examples demonstrate edits that include modifications to the background along with the main subjects. Could the authors provide additional examples where the editing focuses solely on specific subjects, allowing the background to remain unchanged? This would help illustrate the method’s capability for selective edits in multi-subject scenes.


### Questions
- For part-level editing, is the method limited to adding objects, or can it also support modifications like changing the color of clothing or the color of an animal?

### Soundness
3

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
This paper presents a zero-shot approach that modulates attention mechanisms to achieve fine-grained control over video content. We enhance text-to-region control by amplifying each local prompt’s attention to its corresponding spatial disentangled region while minimizing interactions with irrelevant areas.  Extensive experiments demonstrate the method achieves state-of-the-art performance in real-world scenarios.

### Strengths
1. This is the first attempt at multi-grained video editing.
2. The results show the SOTA performance on existing benchmarks and real-world videos.
3. The method is intuitive and is easy to follow.

### Weaknesses
1. The readability and presentation of the manuscript need to be enhanced. For example, in Figure 4:
The "I" in "M_i^pos" denotes the i-th frame, whereas the "i" in "cross-attention modulation" appears to refer to the i-th token (e.g., "polar" is the 3rd token?). Readers should not have to guess what these symbols mean; it would be beneficial to clarify these points explicitly.
The "E" in "L × E" is undefined within the context of this paper, and Figure 2 does not utilize this information. Consequently, the shape information in Figure 4 could be omitted to avoid confusion.
It is unclear whether "p" in Figure 4 represents the original attention score. This should be clearly stated to avoid ambiguity.
2. The paper employs an additional model, SAM-Track, to perform instance segmentation, which might be unfair. If this is the case, one could directly use Grounding-DINO in conjunction with SAM-Track to accurately identify the edited area (mask) based on the provided text. Subsequently, methods like prompt-to-prompt or Video-P2P could be employed to control the editing process through attention maps, potentially achieving similar results.
3. A key concept of the paper is to enhance attention scores in relevant areas while suppressing them in irrelevant areas. However, it's worth noting that methods such as prompt-to-prompt already implement mechanisms to either reduce or increase attention scores for editing purposes. This aspect should be discussed more thoroughly to highlight the novelty and added value of the proposed approach.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a new task called multi-grained video editing,  which encompasses class, instance and fine-grained video editing. The empirical study shows that the key obstacles hindering multi-grained editing in diffusion models are text-to-region misalignment and feature coupling.  This work utilizes a pretrained T2I diffusion model to address these problems without any training. More Specifically ,the method modulates cross-attention for text-to-region control and self-attention for feature separation. Effectiveness has been proven by extensive experiments and convincing qualitative results.

### Strengths
1. This paper addresses a highly significant problem of editing granularity in video editing. It proposes a new and interesting task called multi-grained editing, which includes class, instance, and part-level editing. It allows flexible editing at any granularity and breaks the inherent feature coupling within diffusion models.
2. The empirical study is insightful, explaining why diffusion models are limited to class-level video editing.
3. The proposed method is novel and consistent with its motivation. It adjusts cross-attention for accurate attention weight distribution, enables text-to-region control, and modulates self-attention for feature separation. The modulation process is operated in a unified manner, and the overall framework is training-free.
4. The qualitative experiments are impressive, indicating that ST-Modulator surpasses previous approaches in multi-grained editing.

### Weaknesses
1. Since this work proposes a new and interesting task focused on multi-grained editing, a holistic evaluation would be beneficial, such as establishing a benchmark and developing new metrics to evaluate the performance of current methods on multi-grained video editing. The current evaluation relies heavily on qualitative results, which can be subjective and difficult to reproduce. A more rigorous quantitative evaluation, including metrics that assess the accuracy of edits at different granularities (class, instance, and part-level), is needed to fully validate the proposed method.
2. ST-Modulator focuses on editing videos at different spatial granularities, but the temporal length is limited to 16-32 frames.  The paper does not adequately address the limitations of the method in handling longer video sequences. It is unclear whether the proposed approach can maintain temporal consistency and editing accuracy when applied to videos with hundreds of frames, especially given the computational cost of attention mechanisms.
3. What is the difference between multi-grained editing and multi-attribute editing?

### Questions
Please kindly address the questions in the weakness section.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces ST-Modulator, a zero-shot framework for multi-grained video editing, enabling class-level, instance-level, and part-level modifications in diffusion models. To address semantic misalignment and feature coupling issues, ST-Modulator modulates space-time cross- and self-attention, allowing fine-grained text-to-region control and improved feature separation. Experimental results suggest that this approach performs competitively across benchmarks without additional parameter tuning, presenting a promising solution for multi-grained video editing.

### Strengths
- The paper clearly defines the novel task of multi-grained video editing, motivated by practical needs in video editing. By enabling edits at class-level, instance-level, and part-level, it broadens the range of possible video modifications to better meet real-world demands.
- The paper effectively uses visualizations to illustrate key points, such as in the *Analysis of why the diffusion model failed in instance-level video editing.* These visual aids provide intuitive insights into challenges with existing diffusion models and help clarify the motivation behind the proposed approach.
- The proposed Spatial-Temporal Layout-Guided Attention focuses on self-attention and cross-attention mechanisms to address key issues in text-to-region control and inter-region feature separation. This method effectively targets the core issues in multi-grained editing within diffusion models.
- The proposed method does not require parameter tuning, which makes it resource-efficient—a significant advantage for video editing applications where computational cost and tuning complexity are critical factors.

### Weaknesses
1.  **Focus on Image Editing over Video-Specific Needs:** The approach seems more aligned with image editing, as it emphasizes spatial layout control. However, a key distinction in video editing is maintaining inter-frame consistency, which is crucial for coherent video results. While the Spatial-Temporal Layout-Guided Attention is introduced, the temporal aspect appears to receive less emphasis or detailed explanation. Specifically, the paper lacks a thorough analysis of how the proposed attention mechanism ensures temporal coherence across frames, particularly in scenarios with complex object motion or occlusions. The method's effectiveness in maintaining temporal consistency should be explicitly addressed, perhaps through a dedicated ablation study or a more detailed discussion of the temporal modeling aspects of the attention mechanism.

2.  **Lack of Clarification on Additional Control Signals:** The authors mention that the method is compatible with ControlNet conditioning, but it remains unclear if the cases shown in the paper require extra control inputs. There is no ablation study on control conditions to assess the necessity or influence of these signals. This raises questions about fairness in comparisons with other models like ControlVideo, where discrepancies in control conditions might lead to potentially biased results. For instance, it is not clear whether the reported performance gains are solely due to the proposed ST-Modulator or if they are partially attributable to the specific ControlNet conditions used. A detailed analysis of the impact of different ControlNet conditions on the performance of the proposed method is needed to ensure a fair comparison with other methods.

3.  **Dependence on SAM-Track for Segmentation:** The method relies on SAM-Track for instance segmentation, yet no ablation study examines its impact. This dependency raises concerns: it is unclear if the observed performance gain primarily stems from using SAM-Track. For example, using SAM-Track segmentations as conditional input to other video editing models might yield similar improvements, suggesting a need for direct comparisons to validate the unique contributions of the proposed approach. The paper should include experiments that isolate the contribution of the proposed attention mechanism from the segmentation masks provided by SAM-Track. This could involve comparing the performance of the proposed method with and without SAM-Track masks, or using alternative segmentation methods to assess the robustness of the approach.

4.  **Lack of Code or Algorithm Details:** The paper does not provide code or a detailed algorithm description. Open-sourcing the code could help address concerns such as those in Weaknesses 2 and 3 by allowing for transparent validation of the method’s assumptions, control conditions, and segmentation impacts.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
