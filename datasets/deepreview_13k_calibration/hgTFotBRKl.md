# SAFREE: Training-Free and Adaptive Guard for Safe Text-to-Image And Video Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Recent advances in diffusion models have significantly enhanced their ability to generate high-quality images and videos, but they have also increased the risk of producing unsafe content.
Existing unlearning/editing-based methods for safe generation remove harmful concepts from models but face several challenges: (1) They cannot instantly remove harmful or undesirable concepts (e.g., artist styles) without additional training. 
(2) Their safe generation capabilities depend on collected training data.
(3) They alter model weights, risking degradation in quality for content unrelated to the targeted toxic concepts.
To address these challenges, we propose \ours{}, a novel, training-free approach for safe text-to-image and video generation, that does not alter the model's weights. 
Specifically, we detect a subspace corresponding to a set of toxic concepts in the text embedding space and steer prompt token embeddings away from this subspace, thereby filtering out harmful content while preserving intended semantics. 
To balance the trade-off between filtering toxicity and preserving safe concepts, \ours{} incorporates a novel {\bf self-validating filtering} mechanism that dynamically adjusts the denoising steps when applying the filtered embeddings. 
Additionally, we incorporate adaptive re-attention mechanisms within the diffusion latent space to selectively diminish the influence of features related to toxic concepts at the pixel level. 
By integrating filtering across both textual embedding and visual latent spaces, \ours{} ensures coherent safety checking, preserving the fidelity, quality, and safety of the generated outputs.
Empirically, \ours{} achieves \textbf{state-of-the-art} performance in suppressing unsafe content in T2I generation (reducing it by \textbf{22\%} across 5 datasets) compared to other training-free methods and effectively filters targeted concepts, e.g., specific artist styles, while maintaining high-quality output. 
It also shows competitive results against training-based methods. 
We further extend \ours{} to various T2I backbones and T2V tasks, showcasing its flexibility and generalization. 
As generative AI rapidly evolves, \ours{} provides a robust and adaptable safeguard for ensuring safe visual generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method to remove user-defined toxic concepts from pre-trained text-to-image diffusion models by manipulating the text embeddings and intermediate latents. The intuition is to steer the text embeddings away from a subspace spanned by toxic tokens, while keeping them close to the learned manifold to avoid image quality degradation. The method does not modify pre-trained model weights, can be applied on various diffusion model architectures, and can be extended to support text-to-video models. The experiment results demonstrate that the model outperforms other training-free methods on several benchmarks while being more efficient and flexible.

### Strengths
- The method solves a meaningful task. It addresses toxic concept removal from generative models, a key step towards their safe and responsible deployment.
- The method is training-free, allowing easy integration into pre-trained models. Further, it generalizes well on different diffusion model architectures and can be extended to support text-to-video models.
- The experiment results look promising. It outperforms other training-free methods on adversarial prompt filtering and artistic style removal. It also demonstrates competitive performance in comparison to training-based methods while being more efficient and flexible.

### Weaknesses
 - The paper is very difficult to read, mainly because there are lengthy, distracting discussions all over the place. While the discussions help explain how ideas originated, they disrupt the flow of presentation and cover up the key ideas of the work. The authors are encouraged to sharpen the presentation of the paper by clearly separating background, their key innovations, and insights.

- Many key steps of the algorithm appear quite arbitrary to me. For example, I did not get the intuition behind the definitions of mask m and input space I, and thus got confused by what Eq. (5) means. The reasoning behind Eq. (6) (self-validating filtering) is also not clear. I am not sure I fully understand Eq. (7) either. In particular, why latents in the frequency domain has anything to do with toxic concepts?

- I am not an expert on concept removal from diffusion models, so I will not comment on the selection of baselines and benchmarks. In Table 2, what do LPIPS_e and LPIPS_u mean? Similarly, what do Acc_e and Acc_u mean? Why does the proposed method yield the worst LPIPS_u scores?

### Questions
- How is inference time compared to vanilla diffusion without filtering?
- How many diffusion steps are needed for filtering to work? Does the method support fast samplers that run <10 sampling steps?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SAFREE, a training-free and adaptive method designed to ensure safe content generation in text-to-image (T2I) and text-to-video (T2V) diffusion models without modifying the model’s weights. SAFREE works by identifying tokens in the input prompt that are related to undesirable concepts and projecting them into a space orthogonal to these concepts within the text embedding space. This approach maintains the coherence and intended meaning of the original prompt while filtering out unsafe content. Additionally, SAFREE adjusts the denoising steps in the diffusion process based on the input, enhancing the suppression of unwanted content when necessary. It also employs an adaptive re-attention mechanism in the visual latent space to reduce the influence of features tied to unsafe concepts at the pixel level. The method demonstrates strong performance across multiple benchmarks, effectively reducing the generation of unsafe content while preserving the quality and fidelity of the desired output.

### Strengths
- The method is training free and has no modification of model weights, which makes it efficient and perserve the generative ability.
- The method filters unsafe content in both textual embeddings and visual latent spaces, enhancing the robustness of the safeguard.
- The method shows strong performance on multiple benchmarks, reducing the attack success rate of adversarial prompts and maintaining high generation quality.

### Weaknesses
 - SAFREE may struggle with implicit or indirect triggers of unsafe content, especially when toxic prompts are subtle or crafted in a chain-of-thought style.
-  The effectiveness of the method relies on the accurate identification of the toxic concept subspace, which may not capture all forms of undesirable content.

### Questions
See weaknesses above

### Soundness
3

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
The paper presents SAFREE, an approach designed to enhance the safety of generative AI models in text-to-image and text-to-video applications. This training-free method effectively preserves the original model weights, offering a non-invasive solution to mitigate the risk of generating unsafe content. SAFREE improves safety by identifying and modifying the embeddings of toxic concepts within both textual and visual domains, ensuring the output is devoid of harmful elements. The framework utilizes adaptive token selection based on proximity to a toxic concept subspace, concept orthogonal token projection which repositions toxic tokens away from harmful subspace, and adaptive latent re-attention that diminishes the impact of low-frequency features often emphasized by the filtered prompt embedding.

### Strengths
- Addressing the critical challenge of safe content generation in AI, this paper tackles an increasingly important issue within the field.
- The method introduced in this paper for filtering toxic concepts operates without the need for retraining or modifying the underlying model weights, which is advantageous. 
- The method has been evaluated across an array of model architectures, including newer models like Stable Diffusion 3. Additionally, it has undergone benchmarking across various performance metrics and benchmarks. 
- The mathematical notations are clear and properly used, enhancing the understanding of the method.

### Weaknesses
 - The paper could benefit from a more thorough examination of scenarios where SAFREE may underperform, especially in instances where all toxic tokens are absent from the predefined space tokens. This would provide a clearer understanding of its limitations and potential areas for improvement.
- While Figures 3 and 4 demonstrate a correlation between toxic text and distance from subspace C, this might simply reflect that the words from the prompts are already included in subspace C, resembling a form of "dictionary lookup". For a more comprehensive analysis, it would be beneficial to provide metrics showing the extent to which words in the prompts overlap with those in subspace C.
- I have some reasonable guesses as to why the LPIPS_u metric is higher in Table 2, despite a lower score being preferable. However, this isn't addressed in the paper. Providing an explanation for this result would greatly aid readers in understanding the evaluation.
- Given that your method perturbs the text embedding fed into the model, discussing related works that utilize text embedding modifications for enhancing performance in various tasks would enrich the context. For instance, referencing works that apply text embedding modifications for continuous attribute control [1] or improving compositionally [2] would draw valuable parallels and situate your research within the broader field.
- Given that your method perturbs the text embeddings fed into the model, it would be insightful to discuss related works that have similarly applied text embedding modifications to enhance performance across various tasks. For instance, referring to studies like [1], which uses text embedding modifications for continuous attribute control, and [2], which applies them to improve compositionality, would provide valuable context and enhance the related work or background section of your paper.

### Questions
- In Equation 4, you calculate the mean of distances for masked tokens from subspace C to assess the impact of individual tokens on the distance. Why did you choose not to directly measure the distance of $p$ (without masking any tokens) from $C$? Specifically, I'm referring to using a metric like $\|\| d_{\backslash i} \|\|_2 > (1+\alpha) \times d_p$, where $d_p$ is the distance of the entire prompt $p$ (averaged across token embeddings) from the subspace $C$. 
- Regarding Equation 6, I'm curious about the choice to use the sigmoid function. Given that your input ($1-Sim(p, p')$) ranges from 0 to 2, the sigmoid function's output in this range is nearly linear. What motivated this choice? Additionally, with the values of $t'$ ranging from 5 to 9, this translates to $t$ values between 50 and 90. Could you specify how many time steps you have used in the backward process of the diffusion model?
- In Section 3.4, you discuss the flexibility enabled by *"... concept-orthogonal, selective token projection and self-validating adaptive filtering ..."* allowing SAFREE to be effective across various models and tasks. However, is the adaptive latent re-attention mechanism applied to models like Stable Diffusion 3, or is it utilized differently?

### Soundness
3

### Presentation
3

### Contribution
3
