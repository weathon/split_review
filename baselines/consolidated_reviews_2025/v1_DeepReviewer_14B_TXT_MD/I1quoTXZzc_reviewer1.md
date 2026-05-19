### Summary

This paper proposes energy-based concept bottleneck models that consider the joint energy of input, concept, and class label. The authors claim that this approach addresses limitations of existing CBMs by providing higher accuracy and richer concept interpretations.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a novel approach to address the limitations of existing CBMs by considering the joint energy of input, concept, and class label.

2. The authors provide a theoretical analysis of their method and derive a set of algorithms to compute different conditional probabilities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's contribution seems incremental, combining energy-based models and CBMs, without addressing the fundamental limitations of CBMs. The core idea of using an energy-based model to jointly model input, concepts, and class labels, while novel, doesn't fundamentally overcome the inherent challenges of CBMs, such as the reliance on pre-defined concepts and the potential for information loss during the bottleneck process. The approach appears to be a straightforward application of energy-based modeling to the CBM framework, rather than a transformative solution.

2. The authors claim that their ECBMs can provide concept-based interpretations that align well with human intuition. However, this claim is not supported by any empirical evidence or user studies. The paper lacks any qualitative analysis or user study to demonstrate that the concept-based interpretations provided by the ECBM are indeed intuitive or useful for humans. The absence of such evidence makes this claim unsubstantiated.

3. The paper does not provide a detailed analysis of the computational complexity and scalability of their approach. The energy-based formulation, particularly the joint energy function, can be computationally expensive to train and evaluate. The paper lacks a discussion of the computational cost associated with the proposed method, including the time and memory requirements for training and inference, and how these scale with the number of concepts and data points.

4. The paper's experiments are limited to a few small datasets and do not demonstrate the generalizability of their approach to other domains or tasks. The evaluation is limited to a few attribute-based datasets, which may not be representative of the broader range of applications where CBMs could be used. The lack of experiments on more diverse datasets and tasks raises concerns about the generalizability of the proposed method.

### Suggestions

The authors should more clearly articulate the specific limitations of existing CBMs that their approach aims to address, beyond simply stating that they are addressing limitations. A more detailed analysis of the shortcomings of current CBMs, such as their inability to capture complex concept interactions or their sensitivity to noisy concept labels, would provide a stronger motivation for the proposed method. Furthermore, the authors should provide a more rigorous justification for the use of energy-based models in this context, explaining why this particular framework is well-suited to overcome the identified limitations of CBMs. This should include a discussion of the potential advantages and disadvantages of using energy-based models compared to other possible approaches, such as probabilistic graphical models or transformer-based architectures.

To support their claim of human-intuitive interpretations, the authors should conduct a user study to evaluate the quality and usefulness of the concept-based interpretations provided by their ECBM. This study should involve human participants who are asked to assess the accuracy and clarity of the interpretations, as well as their usefulness for understanding the model's decision-making process. The study should also compare the interpretations provided by the ECBM with those of other CBM variants, to determine whether the proposed method offers any significant improvements in terms of interpretability. The results of this study should be presented in the paper, along with a detailed analysis of the findings.

The authors should also provide a more detailed analysis of the computational complexity and scalability of their approach. This analysis should include a discussion of the time and memory requirements for training and inference, as well as how these scale with the number of concepts, data points, and model parameters. The authors should also discuss any techniques they have used to improve the computational efficiency of their method, such as negative sampling or other approximations. Furthermore, they should provide a more thorough evaluation of their method on a wider range of datasets and tasks, to demonstrate its generalizability and robustness. This should include experiments on datasets with different characteristics, such as different numbers of concepts, different levels of noise, and different types of tasks.

### Questions

1. How does your approach compare to other possible solutions for addressing the limitations of CBMs, such as using transformer-based architectures or probabilistic graphical models?

2. Can you provide any empirical evidence or user studies to support your claim that your ECBMs provide concept-based interpretations that align well with human intuition?

3. How does your approach handle the computational complexity and scalability issues associated with energy-based models, especially when dealing with large datasets and complex models?

4. How does your approach ensure the robustness and reliability of the concept-based interpretations provided by your ECBMs, especially in the presence of noisy or ambiguous data?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
