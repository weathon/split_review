### Summary

This paper proposes a framework to learn language-informed visual concepts by distilling pre-trained vision-language models. The proposed method can extract visual concepts along a number of concept axes specified by language, and can be remix to generate images with novel concept compositions. Experiments show that the proposed method can disentangle and compose visual concepts, and outperforms prior work.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

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

The paper would benefit from a more thorough comparison to existing methods, particularly those that combine textual inversion and VQA. The authors should clearly articulate the novel aspects of their approach and how it differs from simply applying these techniques sequentially. For example, a detailed analysis of how the proposed method's concept encoders differ from the concept embeddings used in textual inversion, and how the VQA model is integrated to guide the concept extraction process, would be beneficial. This should include a discussion of the specific advantages of the proposed method over a naive combination of these techniques, highlighting the technical contributions that go beyond a straightforward application of existing ideas. Furthermore, the authors should provide a more detailed explanation of the training process, including the specific loss functions used and the optimization strategy. This would help to clarify the technical details of the method and make it easier for others to reproduce the results.

To address the limited number of visual results, the authors should include a more comprehensive set of examples that demonstrate the method's ability to generalize to unseen concepts and compositions. This should include a wider range of concepts, as well as more complex compositions of these concepts. For example, the authors could show results for combinations of multiple concepts, or for concepts that are not present in the training data. The visual results should also include a variety of different image styles and contexts to demonstrate the method's robustness. Additionally, the authors should provide a more detailed analysis of the failure cases, identifying the limitations of the method and suggesting potential avenues for future research. This would help to provide a more complete picture of the method's capabilities and limitations.

Finally, the authors should provide more quantitative results to support their claims, especially regarding the method's ability to generalize to unseen concepts. This should include a more rigorous evaluation using a wider range of metrics and datasets. For example, the authors could use metrics that measure the similarity between the generated images and the target concepts, as well as metrics that measure the diversity of the generated images. The authors should also consider using a more diverse set of evaluation datasets, including datasets that are not used for training. This would help to provide a more robust evaluation of the method's performance and demonstrate its generalizability. Furthermore, the authors should provide a more detailed analysis of the quantitative results, discussing the strengths and weaknesses of the method based on the numerical data.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
