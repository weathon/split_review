# Which Tasks Should Be Compressed Together? A Causal Discovery Approach for Efficient Multi-Task Representation Compression

- Decision: Accept
- Avg Score: 5.33
- Scores: 8, 5, 3

## Abstract
Conventional image compression methods are inadequate for intelligent analysis, as they overemphasize pixel-level precision while neglecting semantic significance and the interaction among multiple tasks.  This paper introduces a Taskonomy-Aware Multi-Task Compression framework comprising (1) inter-coherent task grouping, which organizes synergistic tasks into shared representations to improve multi-task accuracy and reduce encoding volume, and (2) a conditional entropy-based directed acyclic graph (DAG) that captures causal dependencies among grouped representations. By leveraging parent representations as contextual priors for child representations, the framework effectively utilizes cross-task information to improve entropy model accuracy. Experiments on diverse vision tasks, including Keypoint 2D, Depth Zbuffer, Semantic Segmentation, Surface Normal, Edge Texture, and Autoencoder, demonstrate significant bitrate-performance gains, validating the method’s capability to reduce system entropy uncertainty. These findings underscore the potential of leveraging representation disentanglement, synergy, and causal modelling for compact representation learning, enabling efficient multi-task compression in intelligent systems. Code will be available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors focus on learning methods for image compression. To this end, they propose a method that optimizes image compression for a number of different downstream visual tasks. They consider the potential redundancy of encodings for similar groups of visual tasks, and they utilize directed acyclic graphics to learn causal relationships between tasks. This approach leads to a better multi-task representation. They evaluate their approach on a number of different visual tasks and demonstrate convincing quantitative results.

### Strengths
1. The problem has multiple applications and is very sensible. Image compression has direct implications, and it is sensible to think image compression in terms of its final use (object detection, classification, etc) as opposed to only pixel reconstruction.

2. The proposed approach has a strong mathematical foundation and makes intuitive sense (conditional entropy should help resolve redundancy between certain tasks). 

3. Quantitative results are thorough and show promise.

### Weaknesses
1. I believe the description of the DAG learning should have more detail. Specifically, some of the details of the DAG based algorithm (described in the appendix as Algorithms 1 and 2) should be incorporated into the main paper. 

2. There are some typos and grammatical errors.

### Questions
1. Would it be possible to incorporate more details of the graph learning into the main paper?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework, Taskonomy-Aware Multiple Task Compression (TAMC), for lossy compression where the distortion is defined by multiple downstream tasks. First, TAMC  groups tasks into clusters where tasks within a cluster are mutually supportive and a share representation is learned for each cluster. Then, it leverages causal discovery to identify dependencies between groups. This results in a directed acyclic graph (DAG), which can be used for further compression of the representation.  Experiments on the Taskonomy dataset demonstrate that TAMC achieves superior bitrate reduction and task performance compared to baseline compression methods.

### Strengths
The paper discusses an important but less studied aspect of representation learning - how to leverage different supervised signals to learn a better representation, where "better" is defined as lower bitrate with higher downstream performance. This principle is sound. The experimental results demonstrate that the proposed framework achieves better performance comparing to end-to-end compression methods using the same bitrate.

### Weaknesses
 **Clarity**: the description of the framework lacks clarity. Given that the paper proposes a fairly complex system, clarity is even more important for the readers to understand. For example, although there is a space constraint, the description of step 3 (taskonomy-based compression) is too brief. Other more specific questions are raised below.

**Lack of ablations**: there are at least 2 ablations the authors could provide. 1. an end-to-end compression with multiple supervised tasks as auxiliary tasks; 2. single task groups, where instead of grouping tasks together in phase 1, simply treat each task as a group and carry out the rest of the learning.

### Questions
1. Could you state the number of parameter sets used and explain how they are allocated across groups and individual tasks? The paper seems to suggest it's per group, but it also needs a set of task parameters per task for computing the pairwise gradient coherence.
2. How is the forecast loss in Eq.3 used? 
3. Line 287, could you clarify if task order impacts the cost calculation and, if so, how do you address this potential variability in their method?
4. Is there any constraint on the subsets used for set cover?
4. Is it better or worse when the same task is not allowed to appear in different clusters? 
5. How is bitrate controlled in the proposed framework? How do you determine $\lambda_i$ for each task?
6. Is the causal discovery step required? Could the minimum description length principle be used for causal discovery and, thus, unifying step 2 and 3 as finding a DAG structure that minimizes the bit-rate?
7. Could you provide a complexity analysis showing how computational requirements change as the number of tasks increases?
8. A simple baseline would be multi-task learning naively combined with end-to-end compression, i.e. without the grouping, just use them auxiliary tasks with well-tuned weights. Why would you not include such a baseline? How would this baseline compare theoretically to the proposed method?
9. Figure 3, could you add a legend for what the color shade represent?  Could you define the "Anchor" baseline in the figure caption or main text?
10. How does the method perform compare to more familiar baselines such as VQGAN?
11. Github link is not provided?
12. L137 typo "Hu"?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose a data compression technique using representations that can be applied to multi-tasking in computer vision. They propose a methodology for task-aware representation learning by using multi-task learning approaches and grouping similar tasks based on the alignment of gradient vectors during the training phase. To efficiently utilize the learned representations, they calculate the causal relationships between task groups using conditional entropy and construct a directed acyclic graph (DAG). The proposed method was validated using the Taskonomy dataset, and the baselines included traditional data compression methods (e.g., JPEG, WEBP) as well as some recent methods (e.g., ELIC, MLIC++, etc.). The authors confirmed the robustness of the proposed method at relatively lower bit-rates compared to the baselines across multiple tasks.

### Strengths
- Hierarchical structure of multiple tasks: The authors propose a methodology that learns a universal representation for computer vision tasks by utilizing techniques from multi-task learning and uses these representations to form a hierarchical structure of the tasks. I believe this methodology could aid research on general representations in areas beyond data compression.
- Robustness of the trained representation: At lower bit-rates, the performance on downstream tasks consistently outperforms trained compression methods (such as MLIC++, ELIC).
- Ablation with random graphs: The authors compared the performance of the proposed causal DAG structure, which exploits causal relationships, with that of a random graph structure to verify its effectiveness. This demonstrates the existence of inter-task relationships and shows that efficient learning and inference, which take these relationships into account, have a considerable impact on performance.

### Weaknesses
 - Lack of clarity, not well-organized components: The figures in the paper are generally not well-organized, and the font size within the figures is excessively small, causing visibility issues. In particular, in Figure 2, the font size within the figure is less than half the line height. Even if it results in a reduction of the amount of information in each figure, it seems necessary to increase visibility by focusing on the most important information.
- Relatively low data decoding accuracy: As mentioned by the authors, the results in subsection 4.3.2 show that the proposed method performs similarly or relatively worse than existing methods in terms of image compression. In order to show that this difference is not a significant problem for the application of the method, it seems necessary to qualitatively compare the decoded images, at least with some examples.
- No results with time and space complexity: One of the critical aspects of a data compression algorithm is minimizing the time and space cost of its execution. Since this work focuses on data compression techniques using multi-task learning methods rather than representation learning methods, I believe it is necessary to analyze such costs to justify the applicability of the proposed method.
- Lack of baselines for comparison: While I think it seems meaningful that the paper uses traditional data compression techniques (e.g., JPEG, WEBP) as baselines, there is still a lack of comparison with more recent trainable methods. Even if the compared baselines are considered state-of-the-art models, I believe that additional comparisons are necessary to clarify the consistent robustness of the proposed method compared to other approaches.
- To summarize, the paper lacks completeness in explaining the methodology and convincing the readers through the results, and the experiments are not sufficiently thorough. Regarding the experiments, it may be helpful for the authors to refer to the analytical techniques used in the MLIC++ paper [1], which they have cited as a key reference. Through a comprehensive revision of the content and additional analyses, the paper’s clarity can be improved, and its novelty can be further emphasized.

### Questions
- Although the paper states that tasks were grouped based on gradient coherence, the justification for task grouping is not clearly stated in LN 470. Could the task grouping process be further explained?
- In Appendix A.5.2, the authors state that they select the parent node for a chosen child based on the node with the highest mutual information and claim that this is equivalent to the optimal choice for conditional entropy. While this claim seems correct, in the partial ordering of Algorithm 5, the child node is not explicitly defined, so the claim does not appear to be directly related to the implementation of the proposed method. It seems there might be an implicit assumption that the task with the larger entropy in its representation distribution is assigned the parent node. Would this be an accurate interpretation?
- It is mentioned that the total bit-rate of task-wise representations was used as a regularization for model training, but there is not enough explanation regarding the bit-rate for each task in the trained models. It would be helpful to include information on the observed bit-rates for each task and to explain how these bit-rates may be related to the tasks.
- Although theoretical approaches are mentioned in Appendix A.5.4 and A.5.5, they do not seem to be fully utilized or proven within the logic of the paper. Is there a plan to elaborate on these? In addition, could further explanations be provided in relation to the above Weaknesses and Questions?
- (minor) Uniform upper and lower case conventions in subsection titles (especially in Section 5)
- (minor) Typo in Equation 3 (\theta_s -> \theta_s^t)
- (minor) Typos in Algorithm 1, 2 in Appendix (end for"\n"return)

### Soundness
2

### Presentation
1

### Contribution
3
