# Vision-RWKV: Efficient and Scalable Visual Perception with RWKV-Like Architectures

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
\blfootnote{* Equal contribution; \  \Letter~Corresponding author (wangwenhai362@gmail.com)}
Transformers have revolutionized computer vision and natural language processing, but their high computational complexity limits their application in high-resolution image processing and long-context analysis. 
This paper introduces Vision-RWKV (VRWKV), a model adap-ted from the RWKV model used in the NLP field with necessary modifications for vision tasks. 
Similar to the Vision Transformer (ViT), our model is designed to efficiently handle sparse inputs and demonstrate robust global processing capabilities, while also scaling up effectively, accommodating both large-scale parameters and extensive datasets. 
Its distinctive advantage lies in its reduced spatial aggregation complexity, which renders it exceptionally adept at processing high-resolution images seamlessly, eliminating the necessity for windowing operations.
Our evaluations demonstrate that VRWKV surpasses ViT's performance in image classification and has significantly faster speeds and lower memory usage processing high-resolution inputs. In dense prediction tasks, it outperforms window-based models, maintaining comparable speeds. These results highlight VRWKV's potential as a more efficient alternative for visual perception tasks.
  \keywords{RWKV \and Visual Perception \and Linear Attention}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces a new network architecture, VISION-RWKV, a vision-adapted version of the RWKV network from the NLP community, which employs an RNN-based linear attention mechanism. The authors have made necessary adaptations to the RWKV to better suit visual tasks, recognizing the differences between vision and language processing tasks.

### Strengths
1.The paper is well-written and easy to follow;

2.Extensive empirical evidence supports the effectiveness of the model, indicating its practical application potential;

3.The adaptation of RWKV for visual tasks goes beyond mere transfer, incorporating modifications that enhance its suitability for image processing.

### Weaknesses
Major：Although the paper discusses RWKV and mamba as prominent RNN-based linear attention models transitioning from NLP to computer vision, it lacks a direct comparison with the mamba (vision) model. Such a comparison would be valuable for assessing the respective strengths and weaknesses of each model in the field of computer vision.

Minor：From an innovation perspective, the approach of adapting other domains' mature architectures to computer vision, similar to what was done post-transformer, appears somewhat incremental.

### Questions
see weaknesses

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors propose an approach that adapts NLP models for RWKV to vision tasks, termed as V-RWKV. Their proposed method could be looked upon as a cost effective solution than ViTs. They propose Quad-directional Shift and change the causal attention to bidirectional one towards learning locl concepts that are more relevant in vision rather than simple text. They evaluate their approach on the image classification, object detection and semantic segmentation tasks.

### Strengths
- Comprehensive results across three tasks.
- Interesting direction to replace ViTs with other efficient techniques that provide on-par or better performance.

### Weaknesses
 - The gains in efficiency seem to be relatively minor, i.e., it is not an order of magnitude which still brings the question whether it is worth exploring these type of models to replace ViTs to begin with or not.

 For example, in Table 2 ViT-L vs. VRWKV-L 191.1 vs 189.5G FLOPS and parameters at 309.5M vs. 334.9M respectively. I think the reduction in FLOPS when scaling to Large variant seems to be around 3G. Similarly in Table 4, FLOPS 446.8 vs. 421.9G with the expense of an increase in the number of parameters. I am not expert in such type of methods focused on improving efficiency but I do not see the results are impressive enough to show the benefit from the V-RWKV design, especially that it is increasing the parameters.



### Questions
Clarifying the practical benefit from their proposed approach and why not simply use vanilla ViTs considering the current gains are not that considerable when looking at Tables 2 and 4. Hence, the reason I am leaning towards a marginal reject but since the method seems to provide interesting direction and their results for detection seems sufficiently good I am not going lower.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors describe a Vision-RWKV architecture that employs novel techniques like bi-directional RWKV, quad token shifting method Q-shift etc. These techniques helps Vision-RWKV  architecture surpass window-based ViTs and comparable to global attention ViTs along with lower FLOPs, lower GPU memory cost and faster processing as shown in Figure 1. Although the MAE finetuning is not as straightforward as typical finetuning on downstream task, overall this paper has a good contribution for the vision research community.

### Strengths
- Novel contribution for quad-directional token shifting called Q-shift. This essentially increases the models range of semantic understanding
- Authors expanded causal RWKV to a bidirectional global RWKV. They modified the exponent in the RWKV attention that leads to transforming the absolution positional bias to relative bias.
- Well written paper with through experimentation including MAE pretraining

### Weaknesses
 - The authors implemented a bidirectional shift operation that removed the vertical shift in Q-shift, thereby enabling for MAE pretraining. IMO this is a source of complexity. As a result, MAE finetuning needs to be done in Q-shift manner

### Questions
- Can you please clarify what you meant in line 527-528 by task fine-tuning using Q-shift manner?

### Soundness
3

### Presentation
3

### Contribution
3
