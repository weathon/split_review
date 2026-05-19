### Summary

The paper proposes a gradient regularization method to improve the transferability of visual adversarial examples for vision-language models. The proposed method regularizes the gradients of both visual and textual features during backpropagation to prevent overfitting. The authors demonstrate the effectiveness of their method through experiments on multiple vision-language models, showing improved attack success rates and enhanced transferability of adversarial examples.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, as demonstrated by the experimental results.
3. The authors provide a comprehensive evaluation of their method on multiple vision-language models, showing its effectiveness in enhancing the transferability of adversarial examples.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The idea of gradient regularization has been widely studied in the field of adversarial attacks. The authors should provide a more detailed discussion on how their method differs from existing gradient regularization techniques, particularly in the context of vision-language models. Specifically, the paper lacks a clear explanation of how the proposed method addresses the unique challenges posed by the cross-modal nature of VLMs, such as the interaction between visual and textual gradients, and how this differs from applying gradient regularization in a single modality. The paper should also clarify the specific mechanisms by which the proposed method achieves improved transferability compared to existing methods.
2. The authors should provide more details about the experimental settings, such as the specific prompts used for each task and the evaluation metrics. The current description lacks sufficient detail to allow for reproducibility. For example, it is unclear how the prompts are constructed for the VQA tasks, and what specific metrics are used to evaluate the attack success rate. The paper should also clarify how the attack success rate is calculated, especially in the context of VLMs, and whether it is based on the model's ability to answer the question correctly or if it is based on other criteria. The paper should also provide a more detailed explanation of the experimental setup, including the hardware and software used, and the specific versions of the libraries and frameworks.
3. The authors should provide more analysis on the transferability of the proposed method. The current analysis is limited to a few models and tasks. It is unclear how the proposed method performs on a wider range of VLMs and tasks, and whether it is robust to different model architectures and training datasets. The paper should also investigate the impact of different hyperparameter settings on the transferability of the proposed method, and provide a more detailed analysis of the factors that affect the transferability of the adversarial examples. The paper should also analyze the computational cost of the proposed method compared to existing methods.

### Suggestions

The paper would benefit from a more thorough comparison with existing gradient regularization techniques, particularly those applied in the context of multimodal models. The authors should clearly articulate the specific challenges in applying gradient regularization to vision-language models, such as the complex interactions between visual and textual gradients, and how their method addresses these challenges. A detailed analysis of the gradient landscape and how the proposed regularization method affects it would be beneficial. Furthermore, the authors should provide a more in-depth explanation of the mechanisms by which their method achieves improved transferability compared to existing methods. This should include a discussion of how the regularization of gradients in both visual and textual modalities contributes to the transferability of adversarial examples. The paper should also include a more detailed analysis of the computational cost of the proposed method compared to existing methods, including the time and memory requirements.

To enhance the reproducibility of the experiments, the authors should provide a more detailed description of the experimental settings. This should include the specific prompts used for each task, the evaluation metrics, and the hyperparameter settings. The paper should also provide a clear explanation of how the attack success rate is calculated, including the criteria used to determine whether an adversarial example is successful. For example, if the attack is targeted, the paper should specify the target label and how it is used to evaluate the attack success. If the attack is untargeted, the paper should explain how the attack is measured in the absence of a specific target. The authors should also provide a more detailed explanation of the experimental setup, including the hardware and software used, and the specific versions of the libraries and frameworks. This level of detail is crucial for other researchers to replicate the results and build upon the proposed method.

Finally, the authors should provide a more comprehensive analysis of the transferability of the proposed method. This should include experiments on a wider range of vision-language models and tasks, and an investigation of the impact of different model architectures and training datasets. The paper should also analyze the sensitivity of the proposed method to different hyperparameter settings and provide a more detailed analysis of the factors that affect the transferability of the adversarial examples. The authors should also consider evaluating the transferability of the adversarial examples to models trained with different objectives or architectures. This would provide a more robust assessment of the generalizability of the proposed method and its potential for practical applications.

### Questions

1. How does the proposed method compare to other gradient regularization techniques in the context of vision-language models?
2. How sensitive is the proposed method to different hyperparameter settings?
3. How does the proposed method perform on a wider range of vision-language models and tasks?

### Rating

5

### Confidence

4

**********
