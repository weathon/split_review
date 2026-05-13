# ConceptPrune: Concept Editing in Diffusion Models via Skilled Neuron Pruning

- Decision: Accept
- Scores: 6, 8, 6, 3

## Abstract
While large-scale text-to-image diffusion models have demonstrated impressive image-generation capabilities, there are significant concerns about their potential misuse for generating unsafe content, violating copyright, and perpetuating societal biases. Recently, the text-to-image generation community has begun addressing these concerns by editing or unlearning undesired concepts from pre-trained models. However, these methods often involve data-intensive and inefficient fine-tuning or utilize various forms of token remapping, rendering them susceptible to adversarial jailbreaks. In this paper, we present a simple and effective training-free approach, \textbf{\textit{ConceptPrune}}, wherein we first identify critical regions within pre-trained models responsible for generating undesirable concepts, thereby facilitating straightforward concept unlearning via weight pruning. Experiments across a range of concepts including artistic styles, nudity, object erasure, and gender debiasing demonstrate that target concepts can be efficiently erased by pruning a tiny fraction, approximately 0.12\% of total weights, enabling multi-concept erasure and robustness against various white-box and black-box adversarial attacks.git}\blfootnote{Correspondence to: $\{$\texttt{ruchika.chavhan, t.hospedales}$\}$@ed.ac.uk}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces ConceptPrune, a training-free method for concept editing in pre-trained diffusion models, specifically latent diffusion models like Stable Diffusion. The core idea is to identify and prune "skilled neurons" within the feed-forward networks (FFNs) of the model's UNet architecture that are responsible for generating undesirable concepts. By calculating importance scores based on neuron activations for target (undesired) and reference (desired) prompts, the method isolates neurons that predominantly influence the generation of unwanted content. Pruning these neurons effectively erases the target concepts while preserving the model's ability to generate unrelated content. The authors demonstrate the efficacy of ConceptPrune across various concepts, including artistic styles, nudity, object erasure, and gender biases, showing that pruning approximately 0.12% of the model's weights suffices. Additionally, the method exhibits robustness against both white-box and black-box adversarial attacks aimed at circumventing concept removal.

### Strengths
1. The paper introduces an application of neuron pruning techniques to concept editing in diffusion models. Specifically, ConceptPrune utilizes the identification and pruning of skilled neurons, providing an alternative approach to mitigating undesired content generation.

2. The experimental results support the method's effectiveness in erasing various concepts while maintaining image generation quality. The authors compare ConceptPrune with several baselines, demonstrating its performance in concept removal and robustness against adversarial attacks.

3. The manuscript is well-written and well-structured, offering clear explanations of the methodology and detailed descriptions of the experiments. Mathematical formulations are provided to illustrate the approach, and visual examples enhance comprehension.

4. The work addresses significant ethical concerns related to the generation of unsafe or copyright-infringing content in diffusion models.

### Weaknesses
1. The method seems relatively straightforward and may be considered incremental in light of existing works [1,2] that also employ pruning techniques for unlearning in diffusion models. It would strengthen the contribution of the paper to clearly delineate the differences between the proposed approach and these related methods. Specifically, methods such as [1,3] have achieved state-of-the-art results in diffusion model unlearning tasks. Including these methods as baselines in the experimental comparisons would provide a more comprehensive evaluation and help illustrate the effectiveness of the proposed scheme.

2. The experimental validation is conducted solely on Stable Diffusion, which may limit the generalizability of the proposed method. To address this potential limitation, it is recommended that the effectiveness of the approach be demonstrated on additional diffusion models, such as [4,5]. This would provide evidence that the method is not tightly coupled to a specific architecture and can be broadly applied to other models in the domain.

3. The choice of focusing on the second layer of the feed-forward networks (FFN-2) for pruning appears to be based on empirical observations and may depend significantly on the architecture of Stable Diffusion. Is there theoretical justification or empirical evidence supporting this selection as the optimal pruning target? Providing analytical insights or additional experiments on different architectures would help ascertain whether this observation holds true universally or is specific to the model under consideration.

4. The decision to aggregate skilled neurons over the last 10 timesteps for pruning seems somewhat arbitrary. Could the authors elaborate on the reasoning behind selecting this particular range of timesteps? It may be beneficial to reference insights from related literature [6,7] that discuss the importance of different timesteps in the denoising process. A more thorough explanation or an exploration of how varying the number of timesteps affects the results would enhance the understanding of this methodological choice.

5. The evaluation of unlearning effectiveness in the context of artistic style erasure relies on CLIP-based similarity metrics. However, CLIP-based metrics consider redundant factors, not only the style but also the object content, arrangement, etc. It is potentially confounding the assessment of style erasure alone. This approach may not effectively isolate the stylistic elements from other irrelevant factors. It is recommended to employ a dedicated style classifier for evaluation (e.g., classifier in [8]) to more accurately measure the degree of style removal. This would provide a more reliable and focused assessment of the method's effectiveness in erasing artistic styles.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
To prevent the misuse of text-to-image diffusion models, this paper proposes a training-free approach using weight pruning for unlearning undesired concepts, such as artistic styles, nudity, and specific objects.

### Strengths
1. The experiments cover all diffusion model unlearning tasks, including artistic styles, nudity, and specific objects.
2. Consider ASR against different attacks while simultaneously evaluating FID and CLIP score to assess model utility.
3. The proposed method requires no additional training.

### Weaknesses
1. The chosen diffusion model baselines are weak and not state-of-the-art methods, so the comparison does not effectively demonstrate true superiority. To defend against adversarial prompt attacks, a stronger baseline, such as AdvUnlearn [1], should be considered. The lack of comparison against more robust unlearning methods makes it difficult to assess the practical effectiveness of the proposed approach in challenging scenarios. The current baselines do not adequately represent the spectrum of existing techniques, particularly those designed for adversarial robustness.
2. More visualization examples are needed, as the current version only includes visualizations for the style unlearning task. The absence of visualizations for nudity and object unlearning limits the qualitative assessment of the method's performance in these critical areas. Visualizations are essential for understanding the nuances of concept removal, and their omission hinders a comprehensive evaluation.


### Questions
In Table 5, the FID metric is missing, and the performance of the base model (SD) should be included for greater clarity.

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
4

### Summary
The paper introduces ConceptPrune, a method for editing concepts in pre-trained diffusion models by pruning neurons associated with undesired concepts, like specific artistic styles, nudity, and biases. This approach identifies "skilled neurons" within diffusion models, such as Stable Diffusion, that activate in response to specific target concepts. By selectively pruning these neurons, the method effectively removes the unwanted concepts without the need for extensive fine-tuning, maintaining the model's overall performance on unrelated tasks. ConceptPrune demonstrates significant resistance to both black-box and white-box adversarial attacks, showing promise as a scalable and robust approach to safer model deployment.

### Strengths
Strengths:
- The investigation into how specific weights influence certain abilities in text-to-image (T2I) models is intriguing and provides valuable insights into the inner workings of these models.
- The paper presents extensive experiments demonstrating the effectiveness of the proposed method across various editing targets, including nudity, artistic style, and specific objects.
- Additionally, the paper is well-structured with a clear logical flow, making it easy to follow and understand.

### Weaknesses
 - **Limited Comparison with Recent SOTA Methods**: The paper lacks sufficient discussion and comparison with recent state-of-the-art methods. For instance, [1] appears to be a strong baseline, demonstrating both high robustness in concept erasure and good utility preservation. While it’s acceptable if this paper does not outperform [1], it would be beneficial to include [1] as a baseline and discuss potential improvements for the current approach in light of their findings.

- **Insufficient Discussion on Related Concept Pruning Work**: The paper lacks sufficient background on concept pruning and similar work. Several studies ([2, 3, 4]) have explored the relationship between weight importance and model abilities during unlearning and editing tasks. Incorporating these works would help situate this paper within the broader landscape and highlight how ConceptPrune builds on or differs from these existing approaches.


### Questions
1. Could you please add discussions on the recent SOTA methods and relevant baselines as highlighted in the weaknesses section?

2. How did you determine the optimal pruning ratio for skilled neurons? Please describe the considerations or criteria used in selecting a suitable pruning ratio.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the risks of large-scale text-to-image diffusion models, including misuse for unsafe content, copyright violations, and bias perpetuation. Traditional methods for removing undesired concepts from these models often require intensive fine-tuning or token remapping, which remain vulnerable to adversarial jailbreaks. To tackle these issues, the authors propose ConceptPrune, a training-free approach that locates key regions in pre-trained models linked to unwanted concepts and applies weight pruning for efficient concept unlearning. Experiments show ConceptPrune effectively erases specific styles, nudity, and objects by pruning only 0.12% of weights, allowing multi-concept removal with resilience to adversarial attacks.

### Strengths
1. The paper is clearly written and well-structured. 
2. It offers an innovative approach to unlearning by employing model pruning techniques.

### Weaknesses
1. There is a lack of adequate baselines. The authors only compare their method to a few early baselines in machine unlearning within diffusion models. As far as I know, many more effective methods have emerged recently, but these were not included in the comparison.

2. The robustness of the method is insufficiently studied. According to recent research, machine unlearning can be vulnerable to adversarial prompts. Without a robust evaluation, it remains unclear whether pruning-based unlearning is indeed resilient against such attacks.

### Questions
1. Could the authors add more baselines by comparing their method with recently published machine unlearning methods in diffusion models?

2. Could the authors include experiments on the robustness of machine unlearning? Specifically, experiments involving adversarial prompts or similar robustness tests would be valuable.

### Soundness
3

### Presentation
2

### Contribution
2
