# Controlling Language and Diffusion Models by Transporting Activations

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
The increasing capabilities of large generative models and their ever more widespread deployment have raised concerns about their reliability, safety, and potential misuse. To address these issues, recent works have proposed to control model generation by steering model activations in order to effectively induce or prevent the emergence of concepts or behaviors in the generated output.
In this paper we introduce Activation Transport (\method), a general framework to steer activations guided by optimal transport theory that generalizes many previous activation-steering works.
\method is modality-agnostic and provides fine-grained control over the model behavior with negligible computational overhead, while minimally impacting model abilities. 
We experimentally show the effectiveness and versatility of our approach by addressing key challenges in large language models (LLMs) and text-to-image diffusion models (T2Is). For LLMs, we show that \method can effectively mitigate toxicity, induce arbitrary concepts, and increase their truthfulness. In  T2Is, we show how \method enables fine-grained style control and concept negation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Activation Transport (ACT), a framework based on optimal transport theory to steer model activations and control generative model outputs. ACT is designed to modify activations from a source distribution (e.g., toxic language) to a target distribution (e.g., non-toxic language) while preserving the natural activation distributions within the model. The framework applies to both large language models (LLMs) and text-to-image diffusion models (T2Is), supporting tasks like toxicity mitigation, concept induction, style control, and concept negation. ACT outperforms other methods in robustness and interpretability by allowing fine-grained, interpretable control of generative behaviors with minimal computational overhead.

### Strengths
1. ACT is a simple and efficient transport function approach that seems to perform well on the experimental setups for both LLM and T2I without significant impact on performance.
2. The paper is well written with clear and easy to follow formulation and experimental results, The paper demonstrates ACT’s effectiveness in diverse tasks, including toxicity mitigation, concept induction, style control, and concept negation, showing superior or comparable performance to existing methods. The method’s flexibility and consistent results across both LLM and T2I applications underscore its potential as a general-purpose activation steering tool.
3. By basing the intervention on optimal transport theory, ACT provides a clear, interpretable parameter (λ) that adjusts the strength of control. This parameterisation allows for easy tuning and understanding of model adjustments, enhancing its usability for practitioners.

### Weaknesses
1. ACT currently relies on linear transport maps, which are computationally efficient but may not capture complex, non-linear relationships within activations, especially in large or multimodal generative models. This assumption could limit its effectiveness in applications requiring nuanced adjustments.

2. The quality of ACT’s transport maps depends on the representativeness of the source and target samples. If the samples do not fully capture the intended distribution (e.g., all aspects of toxic vs. non-toxic language), the intervention may be less accurate, impacting model behavior under real-world conditions with unseen data.

3.  Although ACT shows promising results in mitigating toxicity and inducing specific concepts, the paper provides less evidence of its effectiveness across a broader range of behavioral modifications, especially in challenging or ethically sensitive areas like misinformation suppression or bias control.

4. The performance of ACT can be influenced by which model layers are selected for intervention. While the paper provides some guidance, a more systematic approach to identifying optimal layers would improve robustness and reduce the need for manual tuning.

### Questions
1. A potential future work could be the focus on data selection to estimate the linear transport. This I would argue might produce better improvements than moving to non-linear estimations

2. although you show good evidence of the relatively minor degradation of model performance, more evidence is needed in a more quantifiable way, for example by showing limited impact on downstream tasks

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of activation steering for diffusion models and Transformer language models. The key idea is to view activation steering as optimal transport. Under this umbrella, most existing methods are equivalent to mean transport map, which might not be optimal and do not preserve the activation distribution. Instead, the proposed method, Linear-ACT, can avoid out-of-distribution activations after steering. 

Experiments on Transformer language models (Gemma and Llama) show that the proposed method outperform baselines that use constant vectors for activation steering, on tasks including toxicity mitigation, concept inducing, and truthfulness. Experiments on diffusion models (Stable Diffusion models) show the effectiveness of the proposed method for style control and concept negation.

### Strengths
- This paper studies an interesting problem in activation steering -- out-of-distribution activations. Many existing works require a very large coefficient before the steering vector, which can easily lead to OOD activations. The proposed method instead do not need this extrapolation.
- The experiments are extensive, covering a wide range of control tasks for language models and diffusion models. Many of them are important tasks such as truthfulness and style control.
- The paper proposes a unified framework to understand the connection between different activation steering methods.

### Weaknesses
- One of the exciting applications of activation steering or representation engineering is safety. It would be interesting to see how well the proposed method perform on safety risk mitigation.
- The baselines are mainly vector addition methods. I wonder how the proposed method compare with vector projection methods such as https://arxiv.org/abs/2303.02536

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Activation Transport (AcT) as a general approach to steer activations in generative models, to map activations from one source distribution to the target distribution, while minimizing limitations of current inference intervention approaches. The authors show that the optimal transport-based framework proposed here generalizes many of the previous activation steering work. More specifically, AcT accounts for difference in the amount of variance for each activation dimension in its map which previous approaches do not. The representation maps are iteratively derived updated layer by layer, starting from the earlier layers to the last layers. AcT is agnostic to the modalities; as shown in the experiments, AcT can steer generation in the text domain, in applications such as toxicity mitigation, concept induction and truthfulness, and in the image generation, in applications such as style control and concept negation.

### Strengths
The proposed approach is grounded, intuitive and is applicable to several modalities and domains in generative modeling.

The paper is well written and easy to follow.

Extensive experiments are conducted to compare AcT to baselines approaches in text and image generation.

### Weaknesses
Scope is limited to single modality within a model and linear (not non-linear) mapping.

Experiments and results supporting the claim of AcT better preventing representations from being OOD is lacking.

### Questions
Choice of pooling operation: Can the authors show data to support the choice of average pooling? Some discussion about why average pooling is ideal versus max pooling or last token would be insightful. Ablation disentangling the choice of pooling layers versus other approaches would better differentiate the contribution of AcT and the pooling operations.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel framework called Activation Transport (ACT) for controlling generative models by steering activations using optimal transport theory. It claims to offer fine-grained control over model behavior with minimal computational overhead. ACT is applied to tasks in both large language models (LLMs) and text-to-image diffusion models (T2Is), demonstrating effectiveness in mitigating toxicity, inducing concepts, and providing style control.

### Strengths
1. The use of optimal transport theory to steer activations is a novel idea that generalizes previous activation-steering methods.

2. ACT is shown to be effective across different types of models (LLMs and T2Is), which suggests broad applicability.

3. The method claims to add negligible computational cost, which is crucial for scalability in large models.

4. The paper provides experimental results demonstrating improvements in toxicity mitigation and style control, among other tasks.

### Weaknesses
1. The paper mentions that Linear-ACT assumes a linear transmission relationship between activations, which is a simplification made for computational and memory considerations. Is it possible for nonlinear mapping to allow more complex activation relationships and finer control?

2. Since the mapping estimate depends entirely on the samples used, its expressive power is limited by the diversity and coverage of the samples. How to improve the generalization ability of the mapping through more extensive data sampling or enhancement techniques.

3. The paper mainly focuses on the control of a single task, such as toxicity mitigation or style control. How to deal with multiple conflicting objectives or constraints simultaneously under a unified framework?

4. Although Linear-ACT has a certain robustness to the parameter λ, other methods such as ITI-C are very sensitive to the choice of model and layer, which may lead to a lot of parameter tuning in different situations.

5. Although the ACT method claims to have low computational overhead, there is a lack of detailed analysis of the specific computational costs and resource requirements of models of different sizes in practical applications.

### Questions
1. How does ACT perform in scenarios with highly multimodal distributions, where linear transport might be insufficient?

2. Can the authors provide more details on the computational costs associated with the implementation of ACT?

3. How sensitive is the method to the choice of the transport support $Q_o$ or $Q_∞$?

4. Are there any limitations observed in the diversity or creativity of outputs when using ACT for concept induction in LLMs?

5. How does the method handle potential biases introduced during the transport of activations?

### Soundness
3

### Presentation
2

### Contribution
3
