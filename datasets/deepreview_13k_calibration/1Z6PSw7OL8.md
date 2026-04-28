# BiGR: Harnessing Binary Latent Codes for Image Generation and Improved Visual Representation Capabilities

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We introduce BiGR, a novel conditional image generation model using compact binary latent codes for generative training, focusing on enhancing both generative and representation capabilities. 
BiGR is the first conditional generative model that unifies generation and discrimination within the same framework. 
BiGR features a binary tokenizer, a masking modeling mechanism, and a binary transcoder for binary code prediction. 
Additionally, we introduce a novel entropy-ordered sampling method to enable efficient image generation. 
Extensive experiments validate BiGR's superior performance in generation quality, as measured by FID-50k, and representation capabilities, as evidenced by linear-probe accuracy. 
Moreover, BiGR showcases zero-shot generalization across various vision tasks, enabling applications such as image inpainting, outpainting, editing, interpolation, and enrichment, without the need for structural modifications. Our findings suggest that BiGR unifies generative and discriminative tasks effectively, paving the way for further advancements in the field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
BiGR is a novel conditional image generation model that uses compact binary latent codes to enhance both generative and representation capabilities.​ It unifies generative and discriminative tasks within the same framework, featuring a binary tokenizer, a masked modeling mechanism, and a binary transcoder for binary code prediction. BiGR introduces an entropy-ordered sampling method for efficient image generation and demonstrates superior performance in generation quality and representation capabilities.

### Strengths
1. Paper is clear and well-written.
2. The binary latent idea is new regarding Image Generation through LLMs.

### Weaknesses
- While the idea introduced is novel, it is hard for me to reason why the design choices used in the paper are leading to improving representation capabilities. It would be great if authors shed light on this much more.

- The idea of the diffusion process in Binary seems interesting, however the motivation of why it should improve the overall results could be clearer.

- The authors claim that they have replaced causal attention with bi-directional attention. I need help understanding how this can be done at the inference stage and what fine-tuning was done to make it work.

- The LlamaGen paper reports better results for the ImageNet (256x256). So could the authors please clarify the discrepancy in the results reported?

### Questions
- The SiT architecture reports improved results [1]; could authors clarify more about the SotA claim? 

- Could the authors please fix the citation format at L196 by using \citet{}?

[1] Ma et al. ECCV 2024, SiT: Exploring Flow and Diffusion-based Generative Models with Scalable Interpolant Transformers

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces BiGR, a conditional image generation model that leverages compact binary latent codes to achieve both high-quality image generation and strong visual representation capabilities. BiGR integrates a binary tokenizer, a masked modeling mechanism, and a binary transcoder to generate binary codes, to achieve efficient generation through an entropy-ordered sampling strategy. The model's design allows it to perform favorably in both generative and discriminative tasks. BiGR demonstrates strong performance on generation metrics, e.g., FID-50k and representation tasks evaluated via linear-probe accuracy. Additionally, the proposed method demonstrates its versatility in applications including image editing and zero-shot generalization on several tasks.

### Strengths
- Unified Framework for Generation and Representation. The proposed method effectively combines generative and discriminative capabilities within a single model, demonstrating strong performance in both areas.
- Strong Experimental Validation. The model's performance is validated through extensive experiments, showing improvements over previous methods in generation quality and discriminative accuracy.
- Fast Inference Speed. The model’s entropy-ordered sampling strategy accelerates the generation process by iteratively unmasking tokens in a confidence-guided manner. This is significantly faster compared to autoregressive models.
- Various Applications. BiGR's ability to perform tasks such as inpainting, outpainting, and image enrichment in a zero-shot setting validates its flexibility and generalization capabilities.
- Extensive Ablations. The paper provides thorough ablation studies that detail the impact of various components and settings on the model's performance.
- Well written. The paper's motivation is clear and well-connected to the approach. Although some technical parts can be improved with more detail, the paper is well-written overall.
- The limitations are discussed in the paper.

### Weaknesses
 - Hyperparameter Complexity. The proposed method relies on several hyperparameters for both training and inference, such as the CFG scale, Gumbel temperature, number of sampling iterations, and number of diffusion steps. This complexity increases the time and resources required for tuning. This is discussed in the limitation section of the paper.

- Fixed Sequence Length: The model’s architecture enforces a fixed sequence length during training, which restricts its flexibility to handle inputs of varying sizes. Generating images at different resolutions requires retraining the model with the new sequence length configuration. This is also discussed in the limitation section of the paper.

- The diffusion and denoising process is a bit confusing. It took me a while to figure out where the noise and denoising process is applied. Clarifying that the binary transcoder is the component responsible for denoising the noise introduced in the "Bernoulli diffusion" section would make the flow more understandable and easier to follow.

### Questions
1.	How does BiGR handle scenarios where binary latent codes introduce quantization artifacts? 
2.	Does entropy order sampling prioritize representative features (attribute) of an object or class? Is there any relation in order of sampling and semantic characteristics?
3.	It would be insightful to include examples of failure cases.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces BiGR, a novel conditional image generation model that unifies generative and discriminative tasks within a single framework. This model is notable for several key advantages:

Uniformity: BiGR is the first model to integrate both generative and discriminative tasks, leveraging compact binary latent codes to achieve strong performance in both areas. This unification allows BiGR to handle tasks that typically require separate models.

Efficiency: The model is designed to generate images quickly, making it more efficient than existing models. This efficiency is achieved without compromising the quality of the generated images.

Flexibility and Scalability: BiGR is adaptable to various tasks, including zero-shot generalized tasks, showcasing its potential for a wide range of applications. The model's scalability is demonstrated through its performance across different model sizes and configurations.

Performance: Extensive experiments show that BiGR delivers decent performance in terms of generation quality and linear separability. The model's performance is evaluated using metrics like FID (Fréchet Inception Distance), and it is shown to perform well compared to other models like LlamaGen.

Inference Hyperparameters: The paper discusses the impact of hyperparameters such as the number of sampling iterations and diffusion timesteps on the model's performance. It is noted that larger models tend to achieve lower FID values, but with increased sample time, and that optimal performance varies with model size.

Comparison with Other Models: BiGR is compared against other models, including LlamaGen, across different settings involving tokenizers, training objectives, and modeling types. The paper highlights that while the unconditional version of the model shows better representation capabilities, the conditional version excels in generative tasks.

Overall, BiGR represents a significant advancement in the field of image generation by combining generative and discriminative capabilities in a single, efficient model, with promising applications for future research and development.

### Strengths
Please refer to the summary.

### Weaknesses
Lack of Comprehensive Benchmarking: While the paper compares its model against LlamaGen and a few other settings, the scope of comparison is limited. The paper could benefit from a more extensive benchmarking against a wider range of state-of-the-art models to better establish its relative performance. Specifically, the evaluation lacks comparisons with models that utilize different architectural backbones or training methodologies, making it difficult to assess the true novelty and effectiveness of the proposed approach. A more rigorous comparison should include models that are known to perform well on similar tasks, and should also explore a broader range of datasets beyond ImageNet to demonstrate generalization capabilities.

Sampling Strategy Issues: The paper mentions a "nan" issue in the sampling strategy due to logarithmic operations. Although a workaround is provided, this indicates potential instability in the model's implementation. A more robust solution to this problem would enhance the reliability of the model. The reliance on an alternative method, while functional, raises concerns about the fundamental stability of the original formulation and whether the workaround introduces any unintended biases or limitations in the sampling process. A deeper investigation into the root cause of the NaN issue and a more principled solution would be beneficial.

Limited Exploration of Model Configurations: The paper primarily focuses on a few configurations (S0, S1, S2, S3) and does not explore a broader range of hyperparameters or architectural variations. This limits the understanding of the model's capabilities and its adaptability to different tasks or datasets. The lack of exploration of different network depths, widths, or attention mechanisms, for example, makes it difficult to understand the sensitivity of the model to these parameters and limits the potential for optimization. A more thorough exploration of the design space would provide a more complete picture of the model's capabilities.

Evaluation Metrics: The paper emphasizes generative performance but does not provide a detailed analysis of other important aspects such as scalability, robustness, or efficiency. Including these metrics would provide a more holistic view of the model's strengths and weaknesses. While FID is a common metric for generative models, it does not capture all aspects of performance. A more comprehensive evaluation should include metrics such as computational cost, memory usage, and sensitivity to adversarial attacks. Furthermore, the evaluation should include a more detailed analysis of the model's performance on different types of images and under varying conditions.

Assumptions and Limitations: The paper acknowledges that surpassing state-of-the-art models across all metrics is not the goal, but it does not clearly outline the specific scenarios or applications where the proposed model excels. A clearer articulation of the model's intended use cases and limitations would help in understanding its practical applicability. The paper should clearly define the specific tasks and datasets where the model is expected to perform well, and also acknowledge the limitations of the approach. This would provide a more realistic assessment of the model's potential impact.

Theoretical Justification: While empirical results are presented, the paper could strengthen its theoretical foundation by providing more in-depth explanations or proofs of why certain design choices, such as the non-deterministic binary transcoder, lead to better performance. The paper would benefit from a more rigorous analysis of the theoretical properties of the proposed model, including convergence properties, generalization bounds, and the impact of different design choices on the model's performance. A more solid theoretical foundation would increase the credibility of the work.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a language model based image generation/discrimination model. Using binary latent code autoencoder, the model can learn binary codes from the image representation. Llama is originally a decoder-only model but this method use it as encoder-only model. The generation of an image is conducted by sampling from the Bernoulli distribution of outputs of the model.

### Strengths
- The method is easy to follow and the paper is easy to read
- The architecture of this model seems to work very well on specific tasks such as inpainting, outpainting.

### Weaknesses
 - The biggest problem of this approach is that it is unable to conduct text-to-image generation. Early stage of diffusion models were constrained to class-conditional generation but now it is hard to find models that is unable to do t2i generation. Even LlamaGen can receive various types of condition (especially text condition) since it is a decoder-only model.
- I think that's why binary latent code has been enough to encode image representation. Even VQ-VAE inevitably suffers from loss of information because the latent variable is not continuous. But as the problem setting of this paper is limited to class conditional image generation, the amount of information is not large enough to see the malfunction of the binary code.
- Also, I think it is not fair to directly compare with LlamaGen since it is designed to handle multiple modalities, not focusing on image generation. And also with an appropriate prompt, LlamaGen is able to conduct image discrimination task as well.
- In conclusion, limiting the scope of the problem enabled the binary code to work well.

### Questions
- Comments in Weaknesses should be resolved.

### Soundness
2

### Presentation
2

### Contribution
2
