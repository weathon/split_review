# Make the Pertinent Salient: Task-Relevant Reconstruction for Visual Control with Distractions

- Decision: Reject
- Scores: 5, 6, 6, 5, 5

## Abstract
Recent advancements in Model-Based Reinforcement Learning (MBRL) have made it a powerful tool for visual control tasks.
Despite improved data efficiency, it remains challenging to train MBRL agents with generalizable perception.
Training in the presence of visual distractions is particularly difficult due to the high variation they introduce to representation learning.
Building on \dreamer, a popular MBRL method, we propose a simple yet effective auxiliary task to facilitate representation learning in distracting environments.  % latent-state
Under the assumption that task-relevant components of image observations are straightforward to identify with prior knowledge in a given task, we use a segmentation mask on image observations to only reconstruct task-relevant components.
In doing so, we greatly reduce the complexity of representation learning by removing the need to encode task-irrelevant objects in the latent representation.
Our method, Segmentation Dreamer~(\methodshort), can be used either with ground-truth masks easily accessible in simulation or by leveraging potentially imperfect segmentation foundation models.
The latter is further improved by selectively applying the reconstruction loss to avoid providing misleading learning signals due to mask prediction errors.
In modified DeepMind Control suite (DMC) and \metaw{} tasks with added visual distractions, \methodshort{} achieves significantly better sample efficiency and greater final performance than prior work.
We find that \methodshort{} is especially helpful in sparse reward tasks otherwise unsolvable by prior work, enabling the training of visually robust agents without the need for extensive reward engineering.  % in DMC

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Segmentation Dreamer, a model-based reinforcement learning method that extends the Dreamer framework by introducing an auxiliary task focused on predicting task-related segmentation masks. Specifically, the reconstruction task in Dreamer is modified to work with images that contain task-relevant parts, rather than reconstructing the entire image. The authors evaluate the method on two RL benchmarks: DeepMind Control and Meta-World, demonstrating its effectiveness in these environments.

### Strengths
1. Clear Presentation: The paper is well-written, with clear and easy-to-understand figures, text, and mathematical formulations. The explanation of the model and its components is thorough, making it accessible to both newcomers and experienced researchers in the field.

2. Intuitive Idea: The core idea of the paper—introducing task-relevant segmentation as an auxiliary task—is intuitively appealing. It draws inspiration from human perception, where individuals tend to focus on the most relevant parts of their environment when performing a specific task. This concept feels natural and aligns with cognitive science.

3. Solid Experimental Comparison: The authors conduct experiments for comparing with some strong baselines, and provide detailed ablations for SD's designs.

### Weaknesses
1. Limited Scope of Contribution: One of the main weaknesses of the paper is that the contribution feels somewhat narrow. While the introduction of task-relevant segmentation masks is an interesting idea, it could potentially have a broader application beyond Dreamer or visual distraction tasks. Other model-based RL frameworks, such as transformer-based models (e.g., Trajectory Transformer), also use reconstruction as an auxiliary task, meaning the innovation may not be entirely novel. The applicability of this approach to other RL models and tasks remains underexplored, which limits its perceived impact.

2. Stability Concerns in Meta-World: The experimental results on Meta-World show large reward variance, which raises concerns about the stability of the model. This suggests that the proposed approach may struggle with robustness, particularly in more complex or dynamic environments. A deeper analysis of the reasons for this instability and potential solutions would strengthen the paper.

3. Limited Scope of Experiments: The experiments are conducted on relatively simple and controlled environments (DMC and Meta-World), which might not fully capture the complexity and variability of real-world tasks. The lack of experiments in more complex or high-dimensional settings limits the generalizability of the findings. It would be helpful to see how the method performs on more challenging tasks or in real-world applications where the environment is less predictable.

### Questions
How to ensure that the segmentation masks correctly identify task-relevant parts of the image, especially when the foundation model (used for segmentation) does not inherently understand what is important for the task. In some cases, the background details may be crucial for the task, and it is not clear how the model can distinguish between what is task-relevant and what is not. How can you ensure that the masking process does not remove essential information, especially in environments where the task might require nuanced understanding of the background or context? In other words, how can the sparse rewards guide good segmentation masks prediction, when they are not enough at guiding good policies?

The variance in the rewards observed in the Meta-World experiments could be indicative of instability in the model. Can the authors provide more insights into why this happens and how this issue might be mitigated? For example, are there any hyperparameters or training strategies that could be tuned to improve stability across environments?

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
4

### Summary
This paper addresses the challenge of training Model-Based Reinforcement Learning (MBRL) agents in visually distracting environments, where standard approaches struggle with representation learning due to high visual variability. Building on the DREAMER framework, the authors propose Segmentation Dreamer (SD), an auxiliary task that uses segmentation masks to focus representation learning on task-relevant elements, thereby simplifying latent encoding by excluding irrelevant objects. In experiments with visually complex tasks, SD significantly improves sample efficiency, performance, and robustness, particularly in sparse reward scenarios, enabling effective agent training without extensive reward engineering.

### Strengths
* This paper is well-written and easy to follow. The idea of using the segmentation to capture the task-relavent information is reasonable.

* The literature review is sufficient and the authors have adequately discussed the major difference between the proposed method and existing works.

* The evaluations of the proposed method are comprehensive. The authors compare the proposed methods with several state-of-the-art algorithms and evaluations are conducted on two benchmarks.

### Weaknesses
 * Although the authors conduct experiments on several benchmarks, I still have concerns about the generalization ability. In DMControl tasks, the agent’s visual state consistently appears at the center of the image, and the fixed camera makes segmenting the agent's body relatively straightforward. Could the authors provide additional visualized results for Meta-World and other more complex tasks? For instance, how would segmentation handle the robotic arm and objects in these more challenging scenarios?

* The segmentation process will inevitably introduce additional computational overhead during the model training. For example, the proposed method need masks of the agent body, which is obtained from a fine-tuned SAM model.

### Questions
1. How does the quality of the mask affect the results of the proposed method? The authors propose a selective L2 loss during training. Can the authors provide results about using native L2 loss and selective L2 loss for training respectively?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Segmentation Dreamer (SD), an approach to learn task relevant features in model-based RL framework by using segmentation mask from prior domain knowledge as an auxiliary objective. The proposed approach only reconstruct task relevant components instead of entire original image to avoid noisy learning signals from distractions. Additionally a selective l2 loss is proposed to handle error predictions from segmentation masks. Experiments are performed on visual control benchmarks including DMC and Meta-World with visual distractions by replacing them with diverse background scenes. Experiments demonstrate that SD outperforms Dreamer and other baselines in better sample efficiency and convergence performance. Ablations show effectiveness of each component, specifically focusing on segmentation quality and usefulness of proposed selective l2 loss.

### Strengths
1. Paper is well-written, offering clarity and easy to understand
2. The motivation of only reconstructing task-relevant parts in image is reasonable. The proposed approach can handle potential error of adapting pre-trained segmentation model to visual RL domains
3. Extensive experiments including baseline comparisons and ablation analysis demonstrate benefits of proposed approach in improving sample-efficiency

### Weaknesses
1. This framework requires significant prior knowledge about which part is task-relevant in the image. This may limit the scope of potential usage of the proposed approach, where domain knowledge may be ambiguous or hard to obtain. The reliance on pre-defined segmentation masks introduces a strong assumption that may not hold in many real-world scenarios, particularly those with complex or dynamically changing environments where identifying task-relevant features is not straightforward. For example, in a cluttered scene, it might be difficult to determine which objects are truly relevant to the task without extensive manual annotation or a highly sophisticated understanding of the task itself.
2. Since only parts of image is reconstructed specified by mask, this problem setting is simpler than the original, which may be hard to directly compare to other baselines. By focusing only on task-relevant regions, the method avoids learning representations for the full visual input, potentially limiting its ability to generalize to scenarios where the task-irrelevant components might contain useful contextual information or where the task definition changes slightly. The simplification could also lead to overfitting to the specific segmentation masks used during training, making the model brittle to variations in the environment.
3. Experiments are limited to performance of visual control tasks; we do not know how good pre-trained segmentation models are adapted to downstream domains. The evaluation does not thoroughly investigate the performance of the segmentation model itself after fine-tuning on the RL tasks. It is unclear how well these adapted segmentation models generalize to new, unseen environments or tasks that differ from the training scenarios. The paper lacks a detailed analysis of the segmentation quality and its impact on the overall performance of the RL agent, which is crucial for understanding the limitations and potential failure modes of the proposed approach.

### Questions
1. Since segmentation quality is important to task performance (Figure 3b), what will happen if more samples, than 1 or 5-10, are used in fine-tuning pre-trained segmentation models to downstream domains? Will the proposed selective l2 loss become less important if segmentation model improves with more training samples?
2. How is binary mask predictor head trained, i.e. what is loss function objective here? What will happen if binary mask decoder is trained but selective l2 loss is not used in learning world model, i.e. is the mask prediction task or addressing segmentation model errors more important in this framework?
3. In terms of $mask_\mathbf{SD}$ and $mask_\mathbf{FM}$, could authors visualize how these segmentations look like in order to understand what are similarity and differences in predictions from adapting pre-trained models and those from the process of learning world models?

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
5

### Summary
The paper introduces an approach to enhance MBRL in environments with visual distractions. Building upon the DREAMER framework, the authors propose a method called Segmentation Dreamer (SD). This method utilizes segmentation masks to focus on task-relevant components of the visual input, reducing the complexity of representation learning. To address the limitations of predicted masks, the authors introduce a selective L2 loss function.

### Strengths
To address the limitations of predicted masks, the authors propose a selective L2 loss function.
This is a thoughtful addition to improve the robustness of the model to segmentation errors.

### Weaknesses
1. While the paper presents an integration of segmentation masks into MBRL, it lacks a thorough comparison with existing works that also combine foundation models with RL. A more detailed analysis against these related works would strengthen the paper's claims and provide a clearer picture of the method's advantages and potential limitations[1, 2]. Specifically, the paper should clarify how its approach differs from methods that use segmentation as a preprocessing step, and how it handles scenarios where segmentation models fail or produce noisy masks. A quantitative comparison, beyond the ablation study, would be beneficial to demonstrate the robustness of the proposed method compared to these alternatives.
2. The generalizability of the approach across a wider range of real-world scenarios beyond the controlled environments should be considered. In real-world scenarios, distractions may closely resemble task-relevant features, potentially occluding critical information. The paper could benefit from evaluating the method in more realistic settings with complex distractions[3, 4]. For example, the paper could evaluate the method in environments where the distractors have similar textures or colors as the task-relevant objects, or where the distractors are dynamic and occlude the target object for extended periods. The current evaluation is limited to relatively simple distractors and does not fully explore the limitations of the approach.
3. The paper addresses some limitations, particularly regarding the dependence on accurate segmentation masks. However, a more detailed discussion on potential model biases, especially how segmentation errors might affect performance in untested environments, would be beneficial. The paper should discuss how the selective L2 loss mitigates the impact of segmentation errors, but it should also analyze the potential for the model to learn to rely on incorrect segmentation masks, leading to poor generalization in scenarios where the segmentation model performs poorly.

### Questions
1. Could the authors elaborate on how their approach of integrating segmentation masks into MBRL differs from and improves upon existing methods that combine foundation models with RL?
2. What are the authors' thoughts on the generalizability of their method to real-world tasks where distractions are inherently complex and closely intertwined with task-relevant features? 
3. Can the authors discuss potential biases in their model that may arise from errors in segmentation masks? What strategies could mitigate the impact of segmentation errors in untested environments?
4. In environments where distractions and task-relevant features are dynamic, how does the method ensure consistent performance?
5. Is there a mechanism for the model to adapt to new environments or changing task dynamics without complete retraining?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Segmentation Dreamer (SD), which improves Model-Based Reinforcement Learning (MBRL) in visually distracting environments. It focuses on task-relevant components using segmentation masks, and achieves better sample efficiency and performance, especially in sparse reward settings and when exposed to significant visual distractions.

### Strengths
Originality: Propose selective L2 loss to handle not perfect segmentation input
Quality: A good approach to introduce segmentation model to help MBRL 
Clarity: Visualizations easy to read
Significance: Deal with distraction in RL policy deployment, which is important

### Weaknesses
The main weakness is that proposed algorithm mainly tested with visual distraction with swapped 2D background shift. This set of benchmarks are surrogate to real domain shifts but the segmentation model directly aims to remove that. Thereby, it would be hard to generalize to other cases such as change of viewing angle, color, lighting, texture etc.

### Questions
Can you also compare against other methods also utilizing  segmentation model? e.g., using SAM to get relevant part and feed that to some RL algorithm?  

Can you discuss how would some extension of the proposed method handle cases such as change of viewing angle, color, lighting, texture etc.?

### Soundness
3

### Presentation
3

### Contribution
2
