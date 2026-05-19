### Summary

This paper introduces 3DTrajMaster, a framework for precise 3D motion control in multi-entity video generation. Unlike previous methods limited to 2D control, 3DTrajMaster uses 6DoF pose sequences to manipulate object motions in 3D space. The system includes a 3D-motion grounded object injector that maintains video quality and realism. To support this, the authors created a 360°-Motion Dataset with diverse 3D assets and trajectories. Experiments show that 3DTrajMaster achieves high accuracy and generalization in 3D motion control, offering fine-grained customization for applications like virtual cinematography and gaming.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors propose a novel task that is interesting and worth exploring.
2. The authors propose a new dataset which is valuable.
3. The authors conduct extensive experiments to prove the effectiveness of their method.

### Weaknesses

#### Some Related Works


#### comment

1. The method requires 3D trajectories as input, which may necessitate manual annotation or complex preprocessing, limiting its practicality.
2. The paper lacks a user study to assess the visual quality of the generated videos. I am curious about the perception of the denoising results by humans.
3. The generated videos are relatively short, and the objects do not rotate or move significantly, which may limit the model's ability to handle more complex scenarios. The lack of significant object rotation and movement makes it difficult to assess the model's robustness in more dynamic environments.
4. The paper does not provide sufficient details about the training of the LoRA adaptor, including the specific dataset used and the training process. This lack of detail makes it difficult to reproduce the results or understand the limitations of the domain adaptation.
5. The paper does not provide enough details about the text-to-video backbone model used in the experiments, including its architecture and training data. This lack of information makes it difficult to assess the generalizability of the proposed method to other video generation models.
6. The paper does not explore the scalability of the proposed method to handle more entities, and it is unclear how the method would perform with more complex interactions between multiple entities. The current experiments are limited to a small number of entities, and it is not clear how the method would scale to more complex scenes.
7. The paper does not provide a clear explanation of how the Plücker embeddings are used in the method, and it is unclear why they are not used for object trajectories, given their use for camera trajectory representation. The lack of discussion about the potential benefits of using Plücker embeddings for object trajectories is a significant omission.

### Suggestions

The paper introduces an interesting task of 3D motion control in multi-entity video generation, but several aspects need further clarification and improvement. First, the practicality of the method is limited by the requirement of 3D trajectories as input. While the authors argue that this is similar to other controllable generation methods, the complexity of obtaining these trajectories, especially for non-rigid objects, is a significant hurdle. The authors should explore methods to automatically generate or estimate these trajectories from simpler inputs, such as 2D paths or rough sketches, to make the method more accessible. Additionally, the paper should include a more detailed analysis of the sensitivity of the method to the accuracy of the input trajectories. It is important to understand how errors in the input trajectories affect the quality of the generated videos. This analysis would provide valuable insights into the robustness of the method and its applicability in real-world scenarios.

Second, the evaluation of the generated videos is insufficient. While quantitative metrics are provided, the lack of a user study to assess the visual quality is a major weakness. Human perception is the ultimate judge of video quality, and the authors should conduct a user study to evaluate the realism and coherence of the generated videos. This study should include a diverse set of participants and a well-defined evaluation protocol. Furthermore, the authors should provide more detailed qualitative results, including videos with more complex object interactions and movements. The current results are limited to relatively simple scenarios, and it is unclear how the method would perform in more challenging situations. The authors should also explore the limitations of the method in terms of the types of objects and motions that can be generated. This would provide a more complete picture of the capabilities and limitations of the proposed approach.

Finally, the paper lacks sufficient details about the implementation and training of the proposed method. The authors should provide more information about the text-to-video backbone model, including its architecture and training data. This information is crucial for understanding the generalizability of the method to other video generation models. The paper should also provide more details about the training of the LoRA adaptor, including the specific dataset used and the training process. This lack of detail makes it difficult to reproduce the results or understand the limitations of the domain adaptation. The authors should also discuss the potential benefits of using Plücker embeddings for object trajectories, given their use for camera trajectory representation. The lack of discussion about the potential benefits of using Plücker embeddings for object trajectories is a significant omission. Addressing these points would significantly improve the clarity and reproducibility of the paper.

### Questions

1. The authors claim that 2D control signals cannot fully express the inherent 3D nature of motion, but they do not provide a detailed comparison between 2D and 3D control signals. I would like to see a more detailed comparison between the two, including specific examples of scenarios where 2D control signals fail and 3D control signals succeed. Additionally, I would like to know if the authors have explored the possibility of using 2D control signals as a fallback option when 3D trajectories are not available.
2. The paper does not mention the use of Plücker embeddings in CameraCtrl, VD3D, and SyncamMaster, which are used for camera trajectory representation. I would like to know why the authors did not use Plücker embeddings for object trajectories, and if they have considered this possibility.
3. The paper does not provide sufficient details about the training of the LoRA adaptor, including the specific dataset used and the training process. I would like to know more about the training data and process for the LoRA adaptor.
4. The paper does not provide enough details about the text-to-video backbone model used in the experiments, including its architecture and training data. I would like to know more about the text-to-video backbone model used in the experiments.
5. The paper does not explore the scalability of the proposed method to handle more entities, and it is unclear how the method would perform with more complex interactions between multiple entities. I would like to know if the authors have considered this issue and if they have any plans to address it in future work.

### Rating

6

### Confidence

4

**********
