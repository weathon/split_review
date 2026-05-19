### Summary

The paper proposes a method to learn language-informed visual concepts by distilling pre-trained vision-language models. The proposed method can extract visual concepts along a number of concept axes specified by language, and can be remix to generate images with novel concept compositions. Experiments show that the proposed method can disentangle and compose visual concepts, and outperforms prior work.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is technically sound and the motivation is clear.
3. Experiments show that the proposed method can disentangle and compose visual concepts, and outperforms prior work.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be a simple combination of textual inversion and VQA. The authors are suggested to clarify the difference between the proposed method and these two methods.
2. The authors are suggested to provide more visual results, especially for generalization to unseen concepts. The current results are limited to a few examples, and it is unclear how well the method would perform on a broader range of concepts and compositions.
3. The authors are suggested to provide more quantitative results, especially for generalization to unseen concepts. The current quantitative results are limited, and it is unclear how the method performs on a more rigorous evaluation.

### Suggestions

The authors should provide a more detailed explanation of how their method differs from a naive combination of textual inversion and VQA. Specifically, they should clarify the architectural differences and training procedures that enable their approach to achieve better disentanglement and composition of visual concepts. A more thorough analysis of the loss functions used, and how they contribute to the desired properties of the learned representations, would also be beneficial. For example, it would be helpful to understand how the concept encoders are trained to capture specific visual concepts, and how the VQA model is used to guide this process. The authors should also discuss the limitations of their approach, such as potential failure cases or scenarios where the method might not perform well. This would provide a more balanced and comprehensive view of their work.

To address the limited number of visual results, the authors should include a more diverse set of examples that demonstrate the method's ability to generalize to unseen concepts and compositions. This should include examples with more complex and nuanced concepts, as well as combinations of multiple concepts. The authors should also consider including examples that showcase the method's ability to handle variations in image style and context. Furthermore, the authors should provide a more detailed analysis of the failure cases, identifying the limitations of the method and suggesting potential avenues for future research. This would help to provide a more complete picture of the method's capabilities and limitations. It would also be beneficial to include a quantitative analysis of the generated images, such as metrics that measure the similarity between the generated images and the target concepts, as well as metrics that measure the diversity of the generated images.

Finally, the authors should provide more quantitative results to support their claims, especially regarding the method's ability to generalize to unseen concepts. This should include a more rigorous evaluation using a wider range of metrics and datasets. For example, the authors could use metrics that measure the semantic similarity between the generated images and the target concepts, as well as metrics that measure the diversity of the generated images. The authors should also consider using a more diverse set of evaluation datasets, including datasets that are not used for training. This would help to provide a more robust evaluation of the method's performance and demonstrate its generalizability. Furthermore, the authors should provide a more detailed analysis of the quantitative results, discussing the strengths and weaknesses of the method based on the numerical data.

### Questions

See weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
