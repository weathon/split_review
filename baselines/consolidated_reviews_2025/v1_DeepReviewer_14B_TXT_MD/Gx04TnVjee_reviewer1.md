### Summary

This paper aims to manipulate multi-entity 3D motions in video generation. To achieve this, the authors introduce 3DTrajMaster, a robust controller that regulates multi-entity dynamics in 3D space, given user-desired 6DoF pose sequences of entities. At the core of the approach is a plug-and-play 3D-motion grounded object injector that fuses multiple input entities with their respective 3D trajectories through a gated self-attention mechanism. Furthermore, the authors exploit an injector architecture to preserve the video diffusion prior, which is crucial for generalization ability. To mitigate video quality degradation, a domain adaptor during training and an annealed sampling strategy during inference are utilized. Additionally, to address the lack of suitable training data, the authors construct a 360°-Motion Dataset, which correlates collected 3D human and animal assets with GPT-generated trajectory and then captures their motion with 12 evenly-surround cameras on diverse 3D UE platforms. Extensive experiments show that 3DTrajMaster sets a new state-of-the-art in both accuracy and generalization for controlling multi-entity 3D motions.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The task is interesting and the problem is well-formulated.
3. The proposed 3DTrajMaster can customize object location and orientation in 3D space.
4. The experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only tested for 3 entities, and the authors have mentioned that the proposed method has limitations when the number of entities is larger than 3. This is a significant limitation, as many real-world scenarios involve more than three interacting entities. The paper does not provide a clear path for scaling the method to handle more complex scenes with a higher number of entities. The performance bottleneck when increasing the number of entities should be analyzed in more detail, including memory usage and computational complexity.

2. The proposed method needs a good quality 6DoF location and rotation sequences, and it is not easy to obtain such sequences in real-world scenarios. The method's reliance on accurate 6DoF pose data limits its applicability in practical settings where such data is not readily available or is noisy. The paper does not discuss the sensitivity of the method to errors or uncertainties in the input pose sequences. Furthermore, the process of obtaining these sequences, even if possible, is not trivial and requires specialized equipment or techniques, which are not widely accessible.

### Suggestions

The authors should investigate methods to improve the scalability of their approach to handle a larger number of entities. This could involve exploring more efficient attention mechanisms or alternative architectures that do not suffer from the same computational limitations as transformer-based models when the number of inputs increases. For example, techniques like sparse attention or hierarchical modeling could be considered to reduce the computational cost and memory footprint. Additionally, the authors should provide a more detailed analysis of the performance degradation as the number of entities increases, including metrics such as memory usage and inference time. This analysis should identify the specific bottlenecks that limit the scalability of the method and suggest potential solutions for overcoming these limitations. It would also be beneficial to explore the possibility of using approximate nearest neighbor search or other techniques to reduce the computational cost of the attention mechanism when dealing with a large number of entities.

To address the limitation of requiring accurate 6DoF pose sequences, the authors should explore methods to make their approach more robust to noisy or incomplete pose data. This could involve incorporating techniques from robust estimation or data augmentation to train the model to handle uncertainties in the input pose sequences. Furthermore, the authors should investigate the possibility of using alternative motion representations that are less sensitive to noise or easier to obtain in real-world scenarios. For example, using skeletal animations or motion capture data could be a more practical approach for capturing complex motions. The authors should also consider developing a method to estimate the 6DoF pose sequences from raw video data, which would eliminate the need for manual annotation or specialized equipment. This could involve integrating a pose estimation module into their framework, which could be trained jointly with the rest of the model.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and suggest potential avenues for future research. This discussion should include a thorough analysis of the assumptions made by the method and the scenarios where it is likely to fail. The authors should also explore the possibility of extending their approach to handle more complex interactions between entities, such as collisions or physical contact. This could involve incorporating physics-based constraints into the model or using a more sophisticated motion representation that can capture these interactions. The authors should also consider the ethical implications of their work, particularly in the context of generating realistic videos of human or animal motion.

### Questions

Please see the weakness.

### Rating

6

### Confidence

4

**********
