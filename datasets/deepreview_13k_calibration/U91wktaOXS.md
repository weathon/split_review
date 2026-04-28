# Improving Editability in Compositional Image Diffusion with Layer-wise Memory

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
-

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a framework for compositional image generation that enables sequential object placement through mask-based editing with three main components: layer-wise memory, background consistency guidance, and multi-query disentangled cross-attention. The layer-wise memory stores latent representations and prompt embeddings from previous denoising steps, while background consistency guidance helps maintain background stability during object addition through latent blending. The multi-query disentangled cross-attention mechanism handles the integration of new objects with existing content by managing attention between current and previous objects' regions. The method builds upon the PIXART-\alpha architecture and requires no additional training, operating as a sampler that processes objects sequentially according to specified mask orders. The authors also propose a new benchmark dataset focused on evaluating semantic alignment and spatial accuracy in order-aware image generation scenarios.

### Strengths
The topic is interesting. 

From the evaluation, the method achieves the best performance among competitors and the visual results look good.

### Weaknesses
1. Lack of technical novelty. The method’s core components appear to be straightforward combinations of existing techniques. For example, layer-wise memory is essentially a buffer that stores everything they might potentially need. Background Consistency Guidance (BCG) is essentially a masked blending of the latents. And Multi-Query Disentanglement (MQD) uses standard cross-attention mechanisms guided by masks. It is hard to tell the lessons we can learn from the paper.

2. The paper didn’t report their resource usage, such as GPU memory, RAM, or disk storage for their layer-wise memory and the whole model. As the method has minimal takeaways, it is important to show other benefits of the approach. However, instantly one can tell the method is constrained by memory and computation, limiting the real applicability. A scalability/stress test may be needed, say performing over 10 edits. 

3. The improvements over previous methods are small. Numbers in Tab. 1 are only slightly better than previous approaches. And I don’t observe a clear advantage of the method over others in Fig. 5.

4. Paper writing can be improved. For example, to be more concise, the paragraph right before Sec. 3.3 doesn’t seem to be necessary since the following technique is presented right afterwards. There are a few small typos which can be easily fixed through a paper revision. For example, standig in L053 -> standing, train-free in L323 -> training-free

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a interactive framework for layout control generation that supports comprehensive layouts with denoted instance orders. It includes Background Consistency Guidance and Multi-Query Disentanglement to maintain the background and harmonization of whole image. It also introduces a new comprehensive benchmark for evaluating mask order-aware arrangements in generated images.

### Strengths
1. The proposed interactive framework can support comprehensive layouts. It includes Background Consistency Guidance and Multi-Query Disentanglement, which help to maintain the latent of the previous editing step and improve harmonization of whole image.
2. The experiments verify the effectiveness of the method, which surpasses the baseline methods.

### Weaknesses
1. Iterative image editing for multiple objects takes longer time, which limits its application. It needs a comparison with baseline methods.
2. It lacks the qualitative results of the ablation study, including BCG and QD.
3. It also lacks the qualitative comparisions with LayoutGuidance and NoiseCollage.

### Questions
As seen in weaknesses.

### Soundness
2

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
The manuscript proposes a new image editing pipeline that decomposes a complex editing task into multiple simpler task units. Each task unit can be regarded as a text-guided single-object image inpainting task. Background Consistency Guidance (BCG) and Multi-Query Disentanglement (Multi-QD) are proposed for the progressive editing process. The experimental results show that the proposed method achieved better outcomes in complex image editing tasks.

### Strengths
1. The idea that decomposes a complex editing task into multiple simpler task units makes sense. Both the quantitative and visual results demonstrate that the proposed approach offers superior robustness and editing accuracy in more complex editing tasks.
2. The ablation study in Table 2 clearly demonstrates the effectiveness of each proposed module.

### Weaknesses
1. Is the process of task decomposition manually designed? It seems that P_l is currently sorted based on depth information, but it's difficult to determine the order of each element solely based on the editing prompts. Does the order of P_l affect the robustness of the results? It would be better for the authors to discuss the effects of different orders of P_l.
2. In addition to metrics like clip-score, it's necessary to include a user study in the experimental results. Is Table 3 a user study? If so, please describe the evaluation details, such as how many cases were evaluated, how many users participated, etc.
3. Is it possible for the editing objects to expand beyond noun concepts to include different aspects, such as style, color, expressions, actions, and so on?

### Questions
Please see weakness

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
4

### Summary
The paper's key strength is the seamless integration of Layer-wise Memory and Multi-Query Disentanglement (MQD), which together enhance the editability of compositional image diffusion. This synergy allows for the natural incorporation of new objects while maintaining background consistency, significantly improving the generation of complex image compositions. Alongside, a new benchmark dataset is proposed for assessing semantic alignment and interactivity in image editing.

### Strengths
1 The introduction of layer-wise memory to store and recall latents and embeddings from previous steps allows for precise control over object placement and background consistency in iterative image editing.
2 The creation of a new benchmark dataset focused on spatial accuracy and mask order is a valuable contribution, as it addresses the limitations of previous benchmarks by evaluating semantic alignment and interactivity in image generation.

### Weaknesses
1 The paper mentions that generating multiple objects takes longer, depending on the number of objects. This indicates a potential limitation in terms of efficiency, especially for scenes with a high number of objects or complex interactions.
2 While the layer-wise memory is a strength, it also introduces additional complexity to the model. There is a risk that this could lead to increased computational costs or difficulties in scaling to very large scenes with many layers.
3 The paper does not detail how the model would accurately parse complex, multi-object natural language prompts to determine object layering, particularly when the number of objects and their spatial relationships are intricate, posing challenges for scalability and accuracy in processing such prompts.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2
