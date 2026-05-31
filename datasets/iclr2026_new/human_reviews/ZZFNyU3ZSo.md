## Human Reviewer 1

### Summary
This paper proposes UniMoD (Efficient Unified Multimodal Transformers with Mixture-of-Depths) to address the training efficiency issue in existing unified multimodal transformers. A unified multimodal transformer is a model that integrates and processes both generation and understanding tasks within a single model. The observed training inefficiency stems from token redundancy. The paper empirically demonstrated that token redundancy varies across task type, modality, and layer, and proposed UniMoD as a solution. UniMoD addresses the limitations of applying MoD uniformly to unified multimodal transformers by selectively pruning tokens based on task and layer.

### Strengths
S1. The paper analyzes the existing token redundancy problem and reveals that it varies across tasks and layers. Based on this finding, it proposes a task-aware token pruning method. The causality between the problem and the proposed modules is clear, and its effectiveness is verified.

S2. The proposed method (UniMoD) experimentally shows that it reduces the computational cost of existing methods while maintaining comparable or even superior performance. For example, it reduces training FLOPs by 15% in Show-o and 40% in Emu3.

S3. The paper considers different modeling approaches of transformers (autoregressive/diffusion) for comparison and verifies the generalizability of UniMoD across various settings.

### Weaknesses
W1. Only 2 main models (Show-o and Emu3) are thoroughly evaluated: 1) Show-o: 1.4B params, diffusion + autoregressive, 
2) Emu3: 8.5B params, fully autoregressive. Related work mentions MoMa (Lin et al., 2024b) which also integrates MoE/MoD into Chameleon (a unified model). A more direct comparison or clearer differentiation would be beneficial, although the paper notes MoMa lacked results on generation/most understanding tasks.

W2. The method relies on calculating ARank values beforehand to select layers and estimate pruning ratios. This requires running inference on a base model with sample data, adding a preprocessing step and computational overhead before the efficient training can begin.

W3. The pruning ratios appear to be determined statically based on the initial ARank analysis, rather than being learned dynamically during training (though this is acknowledged as a limitation). Performance might be sensitive to the accuracy of this initial estimation.

W4. Although the paper shows a reduction in FLOPs due to the introduction of the proposed UniMoD, it does not provide an analysis of the exact increase in the number of parameters or the computational overhead caused by introducing the method.

### Questions
Q1. How much computational overhead does the initial ARank calculation add, and how sensitive are the final results to the number and type of samples used for this calculation?

Q2. Could the task-specific routers or pruning ratios be learned dynamically during training, perhaps conditioned on the task type or layer depth, rather than being fixed based on pre-computed ARank values?

Q3. The proposed method was validated by applying pruning to layers with low ARank values. However, it is necessary to show the contrasting effect when pruning is applied to layers with high ARank values. This experiment would clearly demonstrate the causality between ARank, token redundancy, and the proposed method's effectiveness.

Q4. A clear explanation is needed regarding the experiment parameters (pruning layer location and ratio). For example, in the Show-o model's MMU and T2I scaling and pruning ratio selection, were these decisions entirely based on ARank, or were other heuristic criteria also involved?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces UniMoD, an efficient framework for training unified multimodal transformers. It addresses the problem of token redundancy and high computational cost in unified transformers that handle both generation and understanding tasks. By conducting an empirical analysis on attention weights, layer importance, and task interactions, the authors observe that redundancy patterns vary across tasks and layers. UniMoD proposes a task-aware Mixture-of-Depths (MoD) mechanism, equipping each task with its own router to prune redundant tokens adaptively. Experiments on Show-o and Emu3 demonstrate a 15–40% reduction in FLOPs with maintained or improved performance. Moreover, the method generalizes to diffusion-based models such as PixArt and DiT, showing broad applicability.

### Strengths
1. Novelty and Relevance: The paper tackles the important issue of computational efficiency in unified multimodal transformers, introducing a novel task-aware MoD mechanism.
2. Comprehensive Analysis: The empirical studies (attention weights, ARank, layer importance, task competition) are thorough and well-motivated.
3. General Applicability: The approach works for both autoregressive and diffusion-based models.

### Weaknesses
1. Limited Task Diversity: Only two unified models (Show-o, Emu3) are tested; results on larger or more diverse multimodal architectures would strengthen claims.
2. Ablation Details: Although some ablation studies are provided, the analysis of router behavior (e.g., routing distributions, token importance dynamics) could be more in-depth.
3. Limited Discussion on Trade-offs: The paper could elaborate more on how pruning ratios affect different modalities’ representations and downstream tasks.
4. Theoretical Insight: The method is largely empirical; theoretical guarantees or formal efficiency bounds would further solidify its contribution.

### Questions
1. How does UniMoD handle potential conflicts when multiple tasks share overlapping token spaces?
2. How sensitive is performance to router capacity and ARank threshold selection?
3. Does task-aware pruning affect cross-modal alignment quality?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces UniMoD, a task-aware token pruning method engineered to enhance the efficiency of training unified multimodal transformers that share parameters for both generation and understanding tasks. This work finds that directly applying standard token pruning techniques like MoD leads to suboptimal results because token redundancy varies significantly depending on the specific task and across different transformer layers. Proposed UniMoD addresses this issue by implementing a task-aware approach—it converts dense transformer blocks into specialized MoD blocks and employs a separate router for each task, allowing the pruning process to adapt to the distinct token redundancies of each task. Furthermore, the proposed method uses the ARank metric to quantitatively assess token redundancy and determine layer-specific pruning ratios. UniMoD demonstrates significant gains in efficiency, reducing training FLOPs by approximately 15% in the Show-o model, while successfully maintaining or enhancing performance across various benchmarks.

### Strengths
- The paper is generally well written. Especially, the clarity of the problem formulation and literature review effectively sets up this novel approach.
- The paper successfully grounds its motivation in a strong empirical analysis by directly examining attention weight patterns across various tasks and modalities in unified transformers, identifying significant differences in redundancy based on task and layer.
- This observation, combined with the evaluation of layer importance and token redundancy using the ARank metric, effectively explores the potential for task-aware token pruning.

### Weaknesses
- While the detailed analysis is provided, some findings, such as the observation that attention weight patterns differ between tasks (Observation 1) or that token redundancy differs based on modeling methods (Observation 3), might be viewed as expected or previously implied in related transformer studies. 
- Similarly, the finding that early layers are more critical for the final outcome (Observation 2) is a phenomenon often observed in general deep neural networks. 
- Although the application of these analyses specifically to token pruning is novel, the paper's reliance on specific results from the Show-o model (e.g., Observation 5) suggests the specific pattern findings might be somewhat specialized to certain model architectures

### Questions
- What is the performance outcome when the highly task-specific pruning strategy (UniMoD uses task-specific routers and capacities) is applied to a similar task, rather than the exact task it was optimized for?
- Given that the UniMoD achieves a significantly greater FLOPs reduction in the larger Emu3 model (40%) compared to the Show-o model (15%), why is the approach more effective in reducing computation in Emu3, especially when the empirical analysis of attention showed a more pronounced divergence in redundancy patterns in Show-o and JanusFlow?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3