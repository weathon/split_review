### Summary

This paper proposes a framework for learning visual concept representation from images, by distilling large pre-trained vision-language models. The learned concept encoders can extract disentangled concept embeddings from images, which can be used to generate images with novel concept compositions. The authors demonstrate that this approach achieves better disentanglement and compositionality compared to text-based prompting baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel framework for learning language-informed visual concepts by distilling pretrained vision-language models. The idea of using concept encoders to extract disentangled concept embeddings from images is innovative and has the potential to enable more flexible and controllable image generation.

2. The paper is well-written and easy to follow. The authors provide a clear explanation of their method and the underlying concepts.

### Weaknesses

#### Some Related Works


#### comment

1. The authors use BLIP to obtain the text anchors. However, BLIP is not perfect and may make mistakes in some cases. How does this affect the performance of the proposed method? It is unclear how sensitive the method is to the quality of these text anchors, and whether errors in BLIP's predictions lead to significant degradation in the disentanglement or compositionality of the learned concept embeddings. For example, if BLIP incorrectly identifies the color of an object, how does this impact the learned color embedding and its ability to be composed with other concepts?

2. The proposed method is only evaluated on a few datasets. It would be better to see how it performs on a wider range of datasets and tasks. The current evaluation is limited in scope, and it is unclear whether the method generalizes well to different types of visual concepts or datasets with different characteristics. For instance, the method's performance on datasets with more complex scenes or finer-grained concepts is not explored.

3. The authors only compare their method with text-based prompting baselines. It would be useful to see how it compares with other methods for learning visual concept representations. The lack of comparison with other relevant methods makes it difficult to assess the relative strengths and weaknesses of the proposed approach. For example, how does this method compare to other techniques that learn disentangled representations, such as those based on variational autoencoders or generative adversarial networks?

### Suggestions

The paper introduces an interesting approach for learning visual concept representations, but there are several areas where the evaluation and analysis could be strengthened. First, a more thorough investigation into the impact of BLIP's accuracy on the overall performance is needed. The authors should conduct experiments where they systematically introduce errors into the text anchors, either by manually perturbing the labels or by using a weaker VQA model, and then analyze how these errors affect the quality of the learned concept embeddings. This analysis should include both quantitative metrics, such as the disentanglement score, and qualitative examples, showing how errors in the text anchors manifest in the generated images. Furthermore, it would be beneficial to explore methods for making the framework more robust to errors in the text anchors, such as using an ensemble of VQA models or incorporating uncertainty estimates into the training process.

Second, the evaluation should be expanded to include a wider range of datasets and tasks. The authors should consider evaluating their method on datasets with more complex scenes, such as those containing multiple objects or intricate backgrounds, and on datasets with finer-grained concepts, such as those involving subtle variations in style or material. This would provide a more comprehensive assessment of the method's generalization capabilities. Additionally, the authors should explore the method's performance on tasks beyond image generation, such as image editing or concept manipulation. This would demonstrate the versatility of the learned concept representations and their potential for various downstream applications. For example, the authors could evaluate how well the learned embeddings can be used to modify specific attributes of an image while preserving other aspects.

Finally, the authors should compare their method with other relevant approaches for learning visual concept representations. This comparison should include methods that learn disentangled representations, such as those based on variational autoencoders or generative adversarial networks, as well as other methods that leverage pre-trained vision-language models. This would provide a more comprehensive understanding of the relative strengths and weaknesses of the proposed approach and help to contextualize its contributions within the broader field of visual representation learning. The comparison should include both quantitative metrics and qualitative examples, highlighting the differences in the quality of the learned representations and their ability to generate novel concept compositions.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
