### Summary

This paper proposes a zero-shot image classification method that leverages image-text multimodal LLMs. The proposed method uses a simple and universal set of prompts to elicit rich textual representations from input images, which are then fused with visual features to perform zero-shot classification. The proposed method outperforms existing methods on a variety of benchmark datasets.

### Soundness

2

### Presentation

2

### Contribution

1

### Strengths

- The idea of leveraging multimodal LLMs to enhance zero-shot image classification is novel and interesting. 
- The experimental results demonstrate the effectiveness of the proposed method, which outperforms existing methods on a variety of benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the proposed method is limited. The proposed method is a straightforward application of multimodal LLMs for zero-shot image classification, and does not offer any new insights or techniques that could be useful for future research. Specifically, the method simply uses the LLM to generate text descriptions of images, which are then used as input to a text-based classifier. This approach lacks any novel architectural components or training strategies that would advance the field.
- The proposed method relies on the availability of powerful multimodal LLMs, which may not be feasible in all settings. Specifically, the proposed method requires a large amount of computational resources and memory to run, which may not be available in all research environments. The reliance on cloud-based APIs for LLM access also introduces potential latency and cost issues that are not fully addressed.
- The paper does not provide a thorough analysis of the proposed method, and does not explore the limitations or potential drawbacks of the approach. For example, the paper does not analyze the impact of different prompt designs on the performance of the method, nor does it explore the sensitivity of the method to the quality of the generated text descriptions. Furthermore, the paper lacks a detailed analysis of failure cases, which would be useful for understanding the limitations of the approach.
- The proposed method is not well-motivated. The paper does not provide a clear explanation of why the proposed method is expected to work, and does not discuss the potential limitations or drawbacks of the approach. The motivation seems to be solely based on the empirical success of the method, rather than a deeper understanding of the underlying mechanisms.

### Suggestions

The paper would benefit from a more detailed exploration of the method's limitations and potential failure modes. Specifically, the authors should investigate the impact of different prompt designs on the quality of the generated text descriptions and the overall classification performance. A sensitivity analysis of the method to the quality of the generated text would also be valuable. For example, the authors could introduce noise or errors into the generated text descriptions to see how robust the method is to such perturbations. Furthermore, a more detailed analysis of failure cases, including examples of images where the method performs poorly, would provide valuable insights into the limitations of the approach. This analysis should go beyond simply stating that the method fails when the generated text is incorrect, but should delve into the specific reasons why the generated text is incorrect and how this leads to misclassification.

To address the lack of motivation, the authors should provide a more detailed explanation of why the proposed method is expected to work. This explanation should go beyond simply stating that the method leverages the power of multimodal LLMs. The authors should discuss the specific mechanisms by which the generated text descriptions enhance the classification performance. For example, do the text descriptions provide additional contextual information that is not captured by the visual features alone? Or do the text descriptions help to disambiguate between similar-looking classes? A deeper understanding of these mechanisms would provide a stronger motivation for the proposed method. Additionally, the authors should discuss the potential limitations of the approach, such as the reliance on the availability of powerful multimodal LLMs and the potential for bias in the generated text descriptions.

Finally, the paper should include a more thorough comparison with existing zero-shot image classification methods. While the authors compare their method to several baselines, they should provide a more detailed analysis of the strengths and weaknesses of each method. For example, how does the proposed method compare to other methods in terms of computational cost, memory requirements, and robustness to different types of images? A more comprehensive comparison would help to better position the proposed method within the existing literature and highlight its unique contributions. The authors should also consider including ablation studies to evaluate the impact of different components of the proposed method, such as the choice of LLM and the specific fusion strategy used.

### Questions

1. What are the potential limitations or drawbacks of the proposed method? 
2. How does the proposed method compare to other zero-shot image classification methods in terms of computational cost, memory requirements, and robustness to different types of images? 
3. What are the potential future research directions for zero-shot image classification?

### Rating

3

### Confidence

5

**********
