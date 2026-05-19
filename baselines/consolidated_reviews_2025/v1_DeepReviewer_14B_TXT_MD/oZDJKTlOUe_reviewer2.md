### Summary

This paper proposes a post-hoc approach to address the object hallucination issue in large vision-language models. The proposed method is based on a rigorous statistical analysis of the key factors underlying object hallucination, including co-occurrence, uncertainty, and object position. The authors also provide a theoretical explanation to support their method. The experimental results demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical explanation to support their method, which makes the paper more convincing.
3. The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the availability of accurate descriptions, which may not always be the case in real-world scenarios.
2. The proposed method may not be effective for all types of hallucinations, such as those related to object attributes or relationships.

### Suggestions

The paper's reliance on accurate initial descriptions is a significant limitation that needs to be addressed more thoroughly. While the authors focus on object hallucination, the method's dependence on a perfect ground truth caption limits its applicability in scenarios where such captions are not available or are themselves noisy. The paper should include a more detailed discussion of how the method would perform with imperfect initial descriptions, perhaps by introducing controlled levels of noise or errors into the input captions and evaluating the robustness of the proposed approach. Furthermore, the authors should consider exploring methods to generate or refine the initial descriptions, potentially using techniques like iterative refinement or incorporating external knowledge sources to improve the quality of the input data. This would make the method more practical for real-world applications where perfect captions are rarely available.

Additionally, the paper should delve deeper into the limitations of the proposed method regarding different types of hallucinations. While the authors acknowledge that their method primarily targets object hallucination, they should provide a more comprehensive analysis of why it might not be effective for attribute or relationship hallucinations. For example, the method's reliance on object detection and noun identification might not be sufficient to address errors in object attributes or relationships, which often require a deeper understanding of the scene context. The authors could explore how the method could be extended to address these other types of hallucinations, perhaps by incorporating techniques that explicitly model object relationships or attribute information. This could involve using graph-based representations or attention mechanisms to capture the dependencies between objects and their attributes. A more detailed analysis of the method's limitations and potential extensions would significantly strengthen the paper.

Finally, the paper should include a more detailed analysis of the computational cost and scalability of the proposed method. While the authors mention that the method is lightweight, they should provide a more quantitative analysis of the computational resources required for training and inference. This should include the memory footprint, the number of parameters, and the inference time. Furthermore, the authors should discuss the scalability of the method to larger datasets and more complex models. This is particularly important for real-world applications where computational resources are often limited. A thorough analysis of the computational aspects of the method would make the paper more practical and useful for a wider audience.

### Questions

1. How does the proposed method perform on other types of hallucinations, such as those related to object attributes or relationships?
2. How does the proposed method compare to other methods for addressing object hallucination in large vision-language models?
3. How does the proposed method perform on different datasets and models?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
