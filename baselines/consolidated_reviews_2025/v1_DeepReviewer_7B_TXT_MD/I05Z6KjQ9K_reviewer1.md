### Summary

This paper proposes a gradient regularization method to improve the transferability of adversarial attacks on vision-language models. The authors observe that existing adversarial attacks on VLMs exhibit significant instability, with the optimization process for adversarial samples oscillating between success and failure. They attribute this instability to overfitting during the optimization process. To address this issue, they propose a gradient regularization method that clips the gradients of visual and textual features during error backpropagation, eliminating extreme gradients to prevent falling into local optima. The proposed method is evaluated on several VLMs, including Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP, and the results demonstrate the effectiveness of the proposed method in enhancing the transferability of adversarial attacks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors conduct extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Adversarial attacks on large language models via embedding space perturbation
[2] Adversarial examples for vision-language models
[3] On the effectiveness of adversarial attacks for cross-modal retrieval

#### comment

1. The novelty of the proposed method is limited. The idea of gradient regularization has been widely studied in the field of adversarial attacks [1, 2, 3]. The authors should provide a more detailed discussion on how the proposed method differs from existing gradient regularization techniques, particularly in the context of vision-language models. Specifically, the paper lacks a clear explanation of how the proposed method addresses the unique challenges posed by the cross-modal nature of VLMs, such as the interaction between visual and textual gradients, and how this differs from applying gradient regularization in a single modality.

2. The authors should provide more details about the experimental settings, such as the specific prompts used for each task and the evaluation metrics. The current description lacks sufficient detail to allow for reproducibility. For example, it is unclear how the prompts are constructed for the VQA tasks, and what specific metrics are used to evaluate the attack success rate. The paper should also clarify how the attack success rate is calculated, especially in the context of VLMs, and whether it is based on the model's ability to answer the question correctly or if it is based on other criteria.

3. The authors should provide more analysis on the transferability of the proposed method. The current analysis is limited to a few models and tasks. It is unclear how the proposed method performs on a wider range of VLMs and tasks, and whether it is robust to different model architectures and training datasets. The paper should also investigate the impact of different hyperparameter settings on the transferability of the proposed method, and provide a more detailed analysis of the factors that affect the transferability of the adversarial examples.

### Suggestions

The paper should provide a more detailed explanation of how the proposed gradient regularization method is adapted to the cross-modal nature of vision-language models. Specifically, the authors should discuss how the gradients from the visual and textual modalities are handled during the regularization process. It is not sufficient to simply state that the method is applied to both modalities; the paper should explain how the gradients are combined or processed to ensure effective transferability. For example, are the gradients from the two modalities treated equally, or is there a weighting mechanism? Furthermore, the paper should discuss how the proposed method addresses the potential for negative transfer, where the adversarial examples generated for one model may not be effective on another. A more detailed analysis of the gradient landscape and how the proposed regularization method affects it would be beneficial.

To improve the reproducibility of the experiments, the authors should provide a more detailed description of the experimental settings. This should include the specific prompts used for each task, the evaluation metrics, and the hyperparameter settings. The paper should also provide a clear explanation of how the attack success rate is calculated, including the criteria used to determine whether an adversarial example is successful. For example, if the attack is targeted, the paper should specify the target label and how it is used to evaluate the attack success. If the attack is untargeted, the paper should explain how the attack is measured in the absence of a specific target. The authors should also provide a more detailed explanation of the experimental setup, including the hardware and software used, and the specific versions of the libraries and frameworks.

Finally, the paper should provide a more comprehensive analysis of the transferability of the proposed method. This should include experiments on a wider range of VLMs and tasks, and an investigation of the impact of different hyperparameter settings on the transferability of the adversarial examples. The paper should also investigate the robustness of the proposed method to different model architectures and training datasets. For example, the authors could evaluate the method on models trained with different architectures or on datasets with different characteristics. The paper should also analyze the factors that affect the transferability of the adversarial examples, such as the similarity between the source and target models, and the size of the training datasets. A more detailed analysis of these factors would provide a better understanding of the strengths and limitations of the proposed method.

### Questions

Please refer to the weakness.

### Rating

5

### Confidence

4

**********
