### Summary

The paper proposes OC-STORM, an object-centric model-based reinforcement learning (MBRL) pipeline designed to improve sample efficiency in visually complex environments. The method integrates recent advances in object segmentation and detection to address the limitations of traditional reconstruction-based MBRL methods, which often overlook decision-relevant details. The authors demonstrate the effectiveness of OC-STORM through experiments on Atari games and the visually complex game Hollow Knight, showing that it outperforms conventional MBRL approaches in many cases.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach by integrating object-centric learning with MBRL, which is a significant step towards improving the sample efficiency of reinforcement learning in complex visual environments.
- The authors provide a comprehensive evaluation of OC-STORM on both Atari games and Hollow Knight, demonstrating its practical value and adaptability to different environments.
- The paper is well-written and clearly structured, making it easy to follow the methodology and understand the results.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on Cutie for object segmentation, which may introduce biases or limitations depending on the quality of the segmentation. The paper does not provide a detailed analysis of how segmentation errors propagate through the system and affect the overall performance. For instance, if Cutie fails to consistently identify the same object across frames, the learned dynamics model could be significantly impaired, leading to suboptimal policy learning. This is particularly concerning in complex environments where object occlusion or rapid movement is common.
- The paper mentions that the method requires a few-shot annotation, which might not be feasible or scalable for all real-world applications. The reliance on manual annotation, even if few-shot, limits the applicability of the method in scenarios where such annotations are difficult or impossible to obtain. Furthermore, the paper does not explore the sensitivity of the method to the quality or quantity of these annotations, which is a critical factor for practical deployment.

### Suggestions

The authors should investigate the impact of segmentation errors on the performance of OC-STORM more thoroughly. This could involve introducing controlled levels of noise or inaccuracies in the segmentation masks and observing how the agent's performance degrades. A detailed analysis of the types of segmentation errors that are most detrimental to the learning process would be valuable. For example, does inconsistent tracking of the same object have a greater impact than inaccurate segmentation boundaries? Furthermore, the authors should explore methods to make the system more robust to segmentation errors, such as incorporating uncertainty estimates from the segmentation model into the dynamics model or using techniques like data augmentation to improve the model's ability to handle noisy inputs. This would provide a more comprehensive understanding of the method's limitations and potential for real-world application.

To address the annotation requirement, the authors should explore methods to reduce or eliminate the need for manual annotations. One approach could be to investigate unsupervised or self-supervised object discovery techniques that can identify relevant objects without explicit labels. This could involve adapting existing methods from the computer vision literature or developing new techniques specifically tailored to the reinforcement learning setting. Another direction could be to explore methods for learning object representations from interaction data, where the agent learns to identify and track objects based on their influence on the environment. This would make the method more scalable and applicable to a wider range of real-world scenarios. The authors should also investigate the sensitivity of the method to the number and quality of annotations, providing guidelines for when and how annotations should be used.

Finally, the authors should consider expanding the evaluation of OC-STORM to more complex and diverse environments. While the Atari games and Hollow Knight provide a good starting point, testing the method on more challenging tasks with more complex object interactions and dynamics would provide a more comprehensive evaluation of its capabilities. This could include environments with more realistic physics, more complex object relationships, or more diverse visual appearances. Such evaluations would help to better understand the strengths and limitations of the method and identify areas for future improvement. Additionally, comparing the performance of OC-STORM with other state-of-the-art model-based reinforcement learning methods on these more complex environments would provide a more rigorous assessment of its effectiveness.

### Questions

- How does the choice of the object-centric representation affect the performance of OC-STORM? Are there any specific types of objects or environments where the method performs particularly well or poorly?
- What are the computational requirements of OC-STORM compared to traditional MBRL methods? Is the method scalable to more complex environments or tasks?
- How does OC-STORM handle environments with a large number of objects or complex object interactions? Are there any limitations in terms of the number of objects or the complexity of the environment that the method can handle effectively?

### Rating

6

### Confidence

3

**********
