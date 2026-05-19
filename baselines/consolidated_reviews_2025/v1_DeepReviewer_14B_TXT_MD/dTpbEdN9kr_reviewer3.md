### Summary

The paper proposes three methods for human motion generation based on diffusion priors. The first method, DoubleTake, tackles the challenge of long sequence generation by concatenating short sequences. The second method, ComMDM, shows steps toward two-person generation by learning a communication block to coordinate interaction between two motions. The third method, DiffusionBlending, enables flexible and efficient fine-grained joint and trajectory-level control and editing. The paper evaluates the composition methods using an off-the-shelf motion diffusion model and compares the results to dedicated models trained for these specific tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes three novel methods for human motion generation based on diffusion priors, which show promising results in long sequence generation, two-person generation, and fine-grained control.
- The paper is well-written and easy to follow, with clear explanations of the proposed methods and their evaluation.
- The paper provides a comprehensive evaluation of the proposed methods, comparing them to dedicated models trained for specific tasks and showing that they outperform these models in many cases.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed methods, which could help readers better understand their potential drawbacks and areas for improvement.
- The paper does not discuss the computational cost of the proposed methods, which could be an important factor in their practical application.
- The paper does not provide a detailed comparison of the proposed methods with other state-of-the-art methods in the field, which could help readers better understand their relative strengths and weaknesses.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed methods. For instance, while the DoubleTake method is presented as a solution for long sequence generation, it's unclear how it handles potential inconsistencies or artifacts that might arise from concatenating shorter, independently generated sequences. A detailed analysis of failure cases, such as abrupt transitions or repetitive motion patterns, would be valuable. Furthermore, the ComMDM method, while showing promise for two-person motion generation, needs a more in-depth discussion of its ability to handle complex interactions and occlusions. It would be beneficial to explore scenarios where the communication block might fail to coordinate motion effectively, leading to unrealistic or unnatural interactions. Finally, the DiffusionBlending method, while offering fine-grained control, should be analyzed for its sensitivity to the choice of blending parameters and its ability to maintain physical plausibility under extreme control conditions. A more rigorous analysis of these limitations would significantly strengthen the paper.

In addition to the limitations, a more detailed discussion of the computational cost of the proposed methods is needed. The paper should provide a breakdown of the computational resources required for each method, including training time, inference time, and memory usage. This analysis should consider the impact of different parameters, such as the length of the generated sequences and the number of persons involved. For example, how does the computational cost of DoubleTake scale with the length of the generated sequence? How does the computational cost of ComMDM scale with the number of persons? A comparison of the computational cost of the proposed methods with existing approaches would also be beneficial. This would allow readers to better assess the practical applicability of the proposed methods and their trade-offs between performance and computational resources. Furthermore, the paper should discuss the potential for optimizing the computational cost of the proposed methods, such as through parallelization or model compression techniques.

Finally, the paper should include a more comprehensive comparison of the proposed methods with other state-of-the-art methods in the field. While the paper compares the proposed methods to dedicated models trained for specific tasks, it lacks a broader comparison with other relevant approaches. For example, how do the proposed methods compare to other diffusion-based motion generation methods? How do they compare to other methods for long sequence generation, two-person generation, and fine-grained control? A more detailed comparison would help readers better understand the relative strengths and weaknesses of the proposed methods and their position within the broader landscape of motion generation research. This comparison should include both quantitative and qualitative evaluations, highlighting the specific advantages and disadvantages of each method. Furthermore, the paper should discuss the potential for combining the proposed methods with other existing techniques to further improve performance.

### Questions

- Can you provide more details on the limitations of the proposed methods and potential areas for improvement?
- How does the computational cost of the proposed methods compare to existing approaches in the field?
- How do the proposed methods compare to other state-of-the-art methods in the field, and what are their relative strengths and weaknesses?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
