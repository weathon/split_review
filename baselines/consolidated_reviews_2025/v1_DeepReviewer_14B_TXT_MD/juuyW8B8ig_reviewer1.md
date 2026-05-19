### Summary

This paper proposes to learn language-informed visual concept representation so that the representation can extract disentangled concept embeddings from various concept axes, which can be used to generate novel concept compositions. The authors train a set of concept encoders to encode information pertaining to a set of language-informed concept axes, with an objective of reproducing the input image through a pre-trained Text-to-Image model. They also anchor the concept embeddings to a set of text embeddings obtained from a pre-trained Visual Question Answering model to encourage better disentanglement of different concept encoders. In inference time, the trained concept encoders extract concept embeddings from a test image, which can be remixed to generate images with novel compositions of concepts. With a lightweight test-time finetuning procedure, the encoders can also be quickly adapted to extract novel concepts unseen during training.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The idea of learning language-informed visual concept learning is interesting and promising.
2. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The training dataset is small and contains few domains. The generalization ability of the proposed method is not clear. Specifically, the paper does not provide sufficient detail on the diversity of the generated synthetic data used for training. The limited number of domains (5) raises concerns about the model's ability to generalize to unseen concepts and compositions outside of these specific categories. It is unclear how the model would perform on more complex or abstract concepts not represented in the training data.
2. The experiments are limited and the compared methods are old. The authors should compare with more recent works. The experimental evaluation lacks a thorough comparison with state-of-the-art methods. The chosen baselines appear to be relatively old, and the paper does not adequately justify why more recent and relevant methods were not included. This makes it difficult to assess the true performance and novelty of the proposed approach. The evaluation also lacks a comprehensive analysis of the disentanglement quality, relying primarily on qualitative examples rather than quantitative metrics.
3. The authors mention that the proposed method can generalize to unseen concepts via test-time finetuning, but there is no evidence to support this claim. The claim of generalizing to unseen concepts through test-time fine-tuning is not sufficiently supported by empirical evidence. The paper lacks a rigorous evaluation of this aspect, and it is unclear how the model adapts to truly novel concepts not encountered during training. The provided examples are insufficient to demonstrate the robustness and effectiveness of this fine-tuning process.
4. The authors do not provide any quantitative evaluation of the different concept axes being disentangled. The lack of quantitative evaluation for disentanglement is a significant weakness. The paper relies solely on qualitative examples to demonstrate the disentanglement of concept axes, which is not sufficient to validate the claim. There is no metric to measure the degree of disentanglement, making it difficult to assess the effectiveness of the proposed method in achieving this goal.

### Suggestions

The paper would benefit significantly from a more rigorous evaluation of its generalization capabilities. The authors should expand the training dataset to include a wider range of domains and more complex concepts. It would be beneficial to include a detailed analysis of the synthetic data generation process, including the diversity of the generated images and the range of concepts covered. Furthermore, the authors should conduct experiments on held-out datasets that contain concepts and compositions not seen during training. This would provide a more realistic assessment of the model's ability to generalize to new scenarios. The evaluation should also include a quantitative analysis of the model's performance on these held-out datasets, rather than relying solely on qualitative examples.

To address the issue of limited comparisons, the authors should include more recent and relevant methods in their experimental evaluation. This would provide a more accurate assessment of the proposed method's performance relative to the current state-of-the-art. The authors should also consider using more comprehensive metrics to evaluate the disentanglement quality, such as those used in the disentanglement learning literature. This would provide a more objective and quantitative measure of the model's ability to disentangle different concept axes. The paper should also include a more detailed analysis of the limitations of the proposed method, including scenarios where it may fail to generalize or disentangle concepts effectively. This would provide a more balanced and realistic assessment of the method's capabilities.

Finally, the authors need to provide more substantial evidence to support their claim of generalizing to unseen concepts via test-time fine-tuning. This should include a rigorous evaluation of the fine-tuning process, including the number of samples required for effective adaptation and the sensitivity of the process to the choice of fine-tuning data. The authors should also provide a quantitative analysis of the model's performance on unseen concepts after fine-tuning, comparing it to the performance without fine-tuning. This would provide a more convincing demonstration of the method's ability to adapt to new concepts. The paper should also include a discussion of the limitations of the fine-tuning process, including scenarios where it may fail to adapt effectively.

### Questions

1. How is the generalization ability of the proposed method? The training dataset is small and only contains 5 domains.  Have the authors evaluated the proposed method on held-out data that contains concepts and compositions unseen in the training set?
2. The authors should compare with more recent works. 
3. The authors mention that the proposed method can generalize to unseen concepts via test-time finetuning, but there is no evidence to support this claim. 
4. The authors only provide qualitative examples to show different concept axes are disentangled. Have the authors any quantitative evaluation?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
