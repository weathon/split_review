### Summary

The paper introduces the task of generating realistic and diverse 3D hand trajectories from single images, which could be used for various applications in robotics, augmented reality, and computer vision. The authors propose a pipeline that extracts features from the input image and uses a conditional diffusion model to generate the hand trajectories. They also introduce a task-specific metric to evaluate the performance of the proposed method and conduct extensive experiments to demonstrate its effectiveness.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a new and challenging task of generating 3D hand trajectories from single images, which is an important problem in the field of human motion generation.
2. The authors propose a novel pipeline to extract relevant features from the input image and use a conditional diffusion model to generate the hand trajectories.
3. The paper introduces a new task-specific metric to evaluate the performance of the proposed method, which is more comprehensive than existing metrics.
4. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method, including comparisons with state-of-the-art baselines and ablation studies.
5. The paper also evaluates the generated hand trajectories in a physics simulation setting, showing that they can successfully complete the intended actions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for why this task is important and what are the potential applications of this task. The authors should provide more context and motivation for this task.
2. The paper does not compare the proposed method with existing methods for hand motion generation, such as [1,2,3,4,5]. The authors should compare the proposed method with these methods to demonstrate its effectiveness.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. The authors should discuss the potential failure cases of the proposed method and the limitations of the dataset used in the paper.

### Suggestions

The authors should provide a more thorough discussion of the practical applications of generating 3D hand trajectories from single images. While the paper mentions robotics, augmented reality, and computer vision, it lacks specific examples of how this task would be used in these domains. For instance, in robotics, how would this method be used to enable a robot to interact with objects in a more natural and intuitive way? In augmented reality, what kind of virtual objects would benefit from realistic hand trajectories, and how would the proposed method be used to ensure seamless interactions? Providing concrete examples would significantly strengthen the motivation for this research. Furthermore, the authors should discuss the limitations of the proposed method in more detail. For example, how does the method perform when the input image is of poor quality or when the hand is occluded? What are the potential failure cases of the method, and how could these be addressed in future work? A more detailed analysis of the limitations would provide a more balanced view of the proposed method and help guide future research in this area.

The paper needs a more comprehensive comparison with existing methods for hand motion generation. The authors should compare their method with state-of-the-art methods that generate hand motion from various types of input data, such as skeleton data, video data, or text descriptions. This comparison should not only focus on quantitative metrics but also include a qualitative analysis of the generated hand trajectories. For example, how do the generated trajectories compare to human-drawn trajectories in terms of realism and diversity? The authors should also discuss the advantages and disadvantages of their method compared to existing approaches. This would help to better position the proposed method within the broader context of the field and highlight its unique contributions. The authors should also consider including a discussion of the computational cost of their method compared to existing methods.

Finally, the authors should provide a more detailed analysis of the limitations of the dataset used in the paper. The authors mention that the dataset contains manipulations with already empty objects, which can lead to generated trajectories that outperform ground-truth trajectories. However, they do not discuss other potential limitations of the dataset, such as the diversity of hand motions and the number of objects included in the dataset. A more detailed analysis of the dataset would help to better understand the scope and limitations of the proposed method. The authors should also discuss how the dataset could be expanded to include more diverse and challenging scenarios. This would help to improve the generalizability of the proposed method and make it more applicable to real-world scenarios.

### Questions

1. What are the potential applications of this task?
2. How does the proposed method compare with existing methods for hand motion generation?
3. What are the limitations of the proposed method?

### Rating

5

### Confidence

4

**********
