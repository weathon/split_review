# On Exploring Visual Attention Shrinking for Accelerating VLMs for Video Understanding

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Vision-language models (VLMs) have shown promise in a variety of challenging video comprehension tasks. VLMs typically extract frames from the source video and take the corresponding encoded visual tokens as input. A rapid increase in the number of visual tokens, e.g., when handling lengthy videos, can swiftly lead to a long-context dilemma during the inference process of VLMs, posing an efficiency challenge for real-world applications. Given that significant redundant and task-irrelevant information may exist in the visual tokens across both spatial and temporal axes, we advocate removing less important visual tokens during the prefilling phase of the inference procedure to improve the computation and storage efficiency of VLMs. We first identify an interesting phenomenon termed as \emph{Visual Attention Shrinking (VAS)}, wherein certain visual tokens receive progressively diminishing attention during the processing stages of the model. This implies that the model itself knows what to care about and what to discard. With this understanding, we develop a robust algorithm to detect attention shrinking at each layer of the model using states from preceding layers. Based on the detection results, we perform token removal in both temporal and spatial axes. Our approach does not require parameterized modifications to the original VLM and is compatible with the prevalent KV cache strategy. Through extensive experiments across different VLMs, our approach witnesses an average speedup of $1.98\times$ in generating the first response token, utilizing only 47.2% of the visual tokens, without compromising the task performance. Additionally, when applied to the huge VILA1.5-40B, our method can achieve up to $4.16\times$ speedup compared to the vanilla model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a method to improve the efficiency of vision-language models for video tasks by reducing redundant visual tokens during inference. The authors introduce an algorithm to detect and remove low-importance tokens along spatial and temporal dimensions. Their approach requires no parameter changes, is compatible with KV caching, and achieves substantial speedups, using only 47.2% of tokens without degrading task performance, especially benefiting large models like VILA1.5-40B.

### Strengths
1. Tuning-free and plug-and-play: Being tuning-free and plug-and-play, The proposed method can be seamlessly integrated with existing VLMs without the need for extensive modifications or retraining, facilitating broader adoption.
2. Efficient Token Usage. Removing less important visual tokens during inference is an intuitive motivation.
3. Well-structured presentation. The presentation of this paper is clear and easy to understand.

### Weaknesses
1. Lack sufficient experimental support. It would be beneficial to include evaluations on other challenging video benchmarks, such as long video datasets, to validate effectiveness and enable a more comprehensive comparison.
2. Limited novelty. The concept of removing redundant tokens based on attention scores is not entirely new and has been explored in other VLM and transformer-based model optimizations. This approach may not offer a substantial advancement beyond existing methods.

Minor issues: These are some typos in the paper, such as Line 464 and the captions of Table 1.

### Questions
See weaknesses.

### Soundness
2

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
3

### Summary
This paper introduces a dynamic token removal method based on the phenomenon of Visual Attention Shrinking (VAS), which identifies less important visual tokens during inference. The algorithm operates without modifying the original VLM and is compatible with KV cache strategies.

### Strengths
The paper introduces the phenomenon of Visual Attention Shrinking (VAS) and develops a dynamic token removal algorithm based on this phenomenon, providing a new approach to improve the inference efficiency of video VLMs.
The proposed algorithm does not require parameterized modifications to the original VLM and is compatible with the prevalent KV cache strategy, demonstrating good generality.
The proposed method can perform token removal in both temporal and spatial dimensions, enhancing inference speed.

### Weaknesses
The paper primarily demonstrates the effectiveness of VAS through experimental results, but it lacks more intuitive visual analyses. It is recommended to use visualization tools (such as heatmaps, attention maps, etc.) to clearly illustrate the changes in attention distribution of the model before and after token removal, as well as the impact on the model's inference process.

The proposed method does not perform as well on certain specific tasks (such as Egoschema and MLVU) and fails to adequately explore the reasons for this. Specifically, the performance drop on Egoschema with the PLLaVA-7B model is significant and requires further investigation into why the token reduction strategy exacerbates this issue. For MLVU, the paper should provide a more detailed analysis of why the method underperforms compared to other token reduction techniques, particularly when applied to the LongVA model. It's not sufficient to simply state that it's a challenging dataset; the interaction between the proposed method and the model's architecture needs to be better understood.

### Questions
The paper mentions that the token reduction algorithm performs token reduction at certain layers, but what is the basis for selecting which layers to apply token reduction?
Can the dynamic visual token reduction algorithm you proposed be extended to other types of multimodal data beyond video?

### Soundness
3

### Presentation
3

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
This paper identifies an interesting phenomenon termed as Visual Attention Shrinking (VAS), wherein certain visual tokens receive progressively diminishing attention during the processing stages of the model, and develop a robust algorithm to detect attention shrinking at each layer of the model using states from preceding layers.

The contributions are summaried as follows:
1. observe an interesting phenomenon called Visual Attention Shrinking.
2.  develop an algorithm that utilizes the attention states from previous layers to robustly detect attention shrinking, and continuously removes visual tokens based on the detection results. 
3. extensive experiments on various VLMs, across multiple video benchmarks, validate the effectiveness of propsoed method.

### Strengths
1. The phenomenon of Visual Attention Shrinking where some frames or positions consistently exhibit a downward trend in attention scores, is interesting.
2. In the current field of video VLM, a large number of visual tokens are commonly used to represent videos. It is very meaningful to explore token reduction in this field.
3. The experiments are comprehensive, including multiple Benchmarks and video VLM models, and the method shows a significant acceleration for the models.

### Weaknesses
1. In certain settings, the proposed method experiences a higher drop in performance, such as with LongVA-7B and VILA1.5-40B.
2. Although the article focuses on accelerating the inference of video VLM models, it lacks substantial design specific to video.
3. My primary concern is that the model's performance may significantly degrade if we opt for KV cache rather than recalculating VAS with each Q&A round. 
4. In Table 3, the 'Spatial average' toy method is only 0.2 points lower than 'VAS'. What would the corresponding results be if VAS were applied solely in the Spatial or Temporal dimension?

### Questions
1.  Is the shape of $T$  $m$ or $n$? If it is $m$, then in Line 8 of Algorithm 1, $T$ should be summed over dimension 1. It appears there is a conflict between Line 8 and Line 10 in Algorithm 1.
2. How about multi-turn conversations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The large number of visual tokens creates significant inconvenience for both the training and inference of large multimodal models (LMMs). Therefore, reducing and removing unnecessary visual tokens is an important direction for development. This paper observes that certain visual tokens receive progressively less attention during the processing stages of the model. Based on this observation, token removal is performed along the temporal and spatial axes without requiring architectural modifications. This strategy can reduce the number of visual tokens by approximately 50%, with almost no performance degradation, while significantly speeding up inference.

### Strengths
1. The efficiency and performance of the proposed method are competitive compared to ToMe and FastV.

2. This is an architecture-agnostic approach, meaning it can be widely applied to various LMMs.

3. Although the pipeline figure in the paper is somewhat confusing, the textual organization is well-structured and makes it understandable.

4. In addition to the basic experiments, the authors included some observations (such as Figure 2) and ablation studies (Tables 3 and 4) to make the work more comprehensive.

5. The motivation of the paper is reasonable, and I believe this is indeed an urgent issue that needs to be addressed in LMMs.

### Weaknesses
1. The proposed VAS method does not actually show a sufficiently significant performance difference compared to ToMe [1] and FastV [2]. As shown in Figure 1, when VAS is applied to PLLaVA-7B, the performance on MVBench, VideoMME, and MLVU does not demonstrate a notable advantage (e.g., 46.6 vs 46.9, 48.5 vs 49.0). Furthermore, when VAS is applied to LongVA-7B, it consistently falls behind ToMe across all benchmarks. The performance deltas are marginal, raising questions about the practical benefits of the proposed method over existing techniques. A more rigorous analysis of performance gains, especially in scenarios where computational resources are severely constrained, is needed to justify the method's utility.

2. There are many instances of "Failed" in Table 1, and the authors lack a reasonable explanation for this. The only mention of it is in Section 4.2.2, where it is briefly noted that "FastV’s aggressive reduction approach proves to be overly drastic, often resulting in model abnormal responses." However, this is merely a superficial description of the phenomenon. The authors should provide a more in-depth analysis of why these failures occur, including potential reasons related to model architecture, training data, or specific token reduction strategies. It would be beneficial to understand the types of failures observed (e.g., repetitive outputs, nonsensical responses) and how they correlate with the degree of token reduction.

3. The authors lack a direct comparison of the proposed VAS method with prior works, such as ToMe [1] and FastV [2], in terms of motivation and technique. Compared to FastV [2], both methods evaluate the importance of visual tokens based on attention weights, identifying tokens that can be discarded without sacrificing model performance. Both approaches use gradual token reduction strategies, ensuring that important tokens are preserved during the early stages of inference to prevent the loss of critical information. The authors need to clearly differentiate their approach from existing methods, highlighting the unique aspects of their technique and the specific advantages it offers. A more detailed discussion of the similarities and differences in the underlying mechanisms is necessary.

4. The authors lack citations and discussions of other works focused on token merging, such as LlamaVid [3] and MovieChat [4], among others. Additionally, the authors' discussion of Chat-UniVi is inaccurate. The claims that it "attempted to adjust the architecture of the visual encoder" and "introduced additional training requirements" do not align with the original paper's descriptions. The omission of relevant work and the misrepresentation of existing methods undermine the novelty and contribution of the proposed approach. A more comprehensive literature review is essential to place the work in the proper context.

5. Although the authors emphasize "lengthy videos" in the abstract, the experiments lack analysis and emphasis on VAS's performance and observations in long video sequences. For example, does attention dispersion become more severe with longer sequences? It would have been better if the authors had conducted more detailed observations on benchmarks like MovieChat-1K [4] or LongVideoBench [6]. The lack of specific experiments and analysis on long video sequences is a significant oversight, given the focus on this aspect in the abstract. The authors should provide empirical evidence to support their claims regarding the method's effectiveness on long videos.

### Questions
Please revise the Weaknesses section point by point. This is a paper with great potential. If the authors can provide additional responses to certain issues, discuss related work more thoroughly, and include more experiments and observations, I would be very happy to raise my score. Additionally, please redraw Figure 1, as it took me twice the time to understand what VAS is actually doing!

### Soundness
2

### Presentation
2

### Contribution
3
