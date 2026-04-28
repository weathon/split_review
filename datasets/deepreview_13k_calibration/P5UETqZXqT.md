# Model Collapse in the Chain of Diffusion Finetuning: A Novel Perspective from Quantitative Trait Modeling

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The success of generative models has reached a unique threshold where their outputs are indistinguishable from real data, leading to the inevitable contamination of future data collection pipelines with synthetic data. While their potential to generate infinite samples initially offers promise for reducing data collection costs and addressing challenges in data-scarce fields, the severe degradation in performance has been observed when iterative loops of training and generation occur---known as ``model collapse.'' This paper explores a practical scenario in which a pretrained text-to-image diffusion model is finetuned using synthetic images generated from a previous iteration, a process we refer to as the ``Chain of Diffusion.'' We first demonstrate the significant degradation in image quality caused by this iterative process and identify the key factor driving this decline through rigorous empirical investigations. Drawing an analogy between the Chain of Diffusion and biological evolution, we then introduce a novel theoretical analysis based on quantitative trait modeling. Our theoretical analysis aligns with empirical observations of the generated images in the Chain of Diffusion. Finally, we propose Reusable Diffusion Finetuning (ReDiFine), a simple yet effective strategy inspired by genetic mutations. ReDiFine mitigates model collapse without requiring any hyperparameter tuning, making it a plug-and-play solution for reusable image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper identifies CFG as the major factor leading to model collapses on synthetic data, and analyses it through the perspective of quantitative trait modeling. Then, the paper proposes a novel mitigation strategy: conditional drops during finetuning, and decayed CFG scaling during sampling.

### Strengths
* The observations are interesting.
* The analysis of quantitative trait modeling is novel.
* The method is easy to implement and shows promising results.

### Weaknesses
 * No discussion on the potential tradeoff of the method: specifically, how would the generation quality be affected if using the proposed CFG scheduling?
* Unclear how the method behaves on other CFG scales and decay rates, especially a lower CFG scale, as I only found 5 to 10 in the paper. It's important to understand the sensitivity of the method to these parameters, as the optimal range might be narrow or dataset-dependent. The lack of exploration below CFG 5 is a significant gap.
* The paper summarizes prior arts as “focused on the reduction of diversity”. The paper could have shown if the proposed method maintains sampling diversity as well. It's not sufficient to claim that prior work focuses on diversity reduction; the paper needs to demonstrate its method's behavior in terms of diversity, using appropriate metrics like recall or precision.
* The connection between the proposed method and analysis is not convincing. How would a decaying CFG schedule correspond to smoothing truncations? The paper needs to provide a more mechanistic explanation of this connection, perhaps through mathematical analysis or detailed simulations. The current explanation is too high-level and lacks concrete evidence.

### Questions
* How would the generation quality be affected if using the proposed CFG scheduling?
* How does the method behave on other CFG scales and decay rates?
* Does the proposed method maintain sampling diversity?
* How would a decaying CFG schedule correspond to smoothing truncations?
* Another work [1] sheds light on how CFG increases quality but reduces variation. It would be interesting to see if using their method would alleviate model collapse.
* What if different synthetic images have different CFG scales?

[1] Tero Karras, Miika Aittala, Tuomas Kynk¨a¨anniemi, Jaakko Lehtinen, Timo Aila, and Samuli Laine. Guiding a diffusion model with a bad version of itself. arXiv preprint arXiv:2406.02507, 2024a.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates an emerging challenge in machine learning: the potential contamination of training data for future models by AI-generated content. The authors introduce and analyze the concept of "model collapse" - a degradation in model performance caused by training on self-generated data. Their key contributions are identifying classifier-free guidance as a primary factor in this degradation process, developing an analytical framework inspired by genetic biology to study this phenomenon, and proposing ReDiFine, a new inference method to mitigate model collapse.

### Strengths
- The paper addresses a timely and critical research question, particularly relevant given the rapid proliferation of foundation models and AI-generated content.
- The work demonstrates foresight in identifying and analyzing a challenge that could significantly impact future model development.
- The authors provide clear explanations supported by effective visual diagrams.
- The biological inspiration for the analytical framework offers a novel perspective on the problem.

### Weaknesses
 - The analysis of the observed phenomena lacks sufficient depth and causal investigation. For instance, the relationship between low CFG scales and low-frequency degradation could be explained by the absence of concept generation in subsequent iterations (those trained without real data), as a CFG scale of 1.0 effectively neutralizes the guidance. However, this hypothesis cannot be verified without samples of generated images used as dataset for successive training iterations. In this connection, not having the concept in the training images of successive iterations could lead to dilution of the concept getting trained.
- Conversely, the link between high CFG scales and high-frequency degradation could be seen as just concept overfitting. Due to high guidance, crude copies of the previous training images could compose the next the training dataset. This again cannot be verified since training sets for each iteration are not shown. The paper analysis would benefit from a more systematic investigation of these mechanisms, which should form the foundation for developing more robust solutions to the model collapse problem.

### Questions
How does the proposed framework extend to multi-domain training scenarios? While early work need not address all complexities, some preliminary insights into situations where multiple concepts are trained simultaneously would better align with the paper's broader motivation of understanding model training with aggregated domains.

Specifically:
- How do different concepts interact during the collapse process?
- Does the rate of degradation vary across different domains?
- How might ReDiFine's effectiveness vary across different concept types?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This  work simulates a recycled pipeline of synthetic images for the training of generative models, and named "self-consuming chain"。
And most importantly, image degradation will happen in such recycle chain. So authors design a metric to evaluate whether this model is collapse.
Authors check and conclude (among many factors) that  higher CFG scale will be the key factor to accelerate the model collapse.
And a new strategy named ReDiFine is proposed to mitigate model collapse, including dropping condition during finetuning and dynamically adjusting the CFG scale along the chain.

### Strengths
1. Clear clirify and writing. Good representation.

2. Systematically exploring the self-consuming chain, with designed metric and listed factors.

3. Successfully mitigates the issue proposed by their own.

### Weaknesses
1. The methods and the paper is well designed and very serious. And I admire this is a good paper.
But my main concern is the motivation, which seems to be an impractical and pseudo demands:

a. Data hungury now happens in LLM  and many AI models leverage the synthetic data to train. But this work choose the visual/image generation (visual signals are sufficient currently). It might be better to discuss such a topic in the scenario of language?

b. For the training of a large-scale vision model (such as SAM), we have the semi-supervised strategy like human-in-the-loop for SAM.  We can get a huge amounts of raw data with human annotated prompts, for the training of visual generation models.

Combing with the above two reasons, it seems that we do not need using the synthetic data with the same prompts to re-train a visual generation model.

### Questions
1. Could please provide the Recall score in the "self-consuming chain"? A common sense is that higher CFG fator (Within a reasonable range) can lead to better FID but the worse Recall. And recall means the generation diversity.  So I consider that the high CFG is the shallow reason but the worse  and worse generation diversity  brought by high CFG is the key factor in the "self-consuming chain" .

Besides, I recommend you the high-score work CADS[1] in the last ICLR, which is a more elegant CFG to improve both the FID and the Recall score. You can leverage such an idea to sovle the collapse problem in  ReDiFine.

[1] Sadat, Seyedmorteza, et al. "CADS: Unleashing the diversity of diffusion models through condition-annealed sampling." ICLR 2024

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the phenomenon of "model collapse" and identifies significant degradation in image quality caused by the iterative process of generation and training. The key factor contributing to this degradation is found to be the CFG. The paper introduces a novel theoretical analysis based on quantitative trait modeling to explain this phenomenon and proposes ReDiFine, a new method to mitigate model collapse without the need for hyperparameter tuning.

### Strengths
1. The observation that the direction of degradation changes with different CFG values is intriguing and provides new insights.
2. The proposed ReDeFine method effectively reduces the collapse rate without the need for meticulous tuning. Additionally, this mitigation strategy produces reusable images for future training.
3. The theoretical perspective offers a novel approach to explaining model collapse.

### Weaknesses
1. The statement in the abstract that "their outputs are indistinguishable from real data" is too absolute. As noted by [a], the distributions generated by diffusion models still differ significantly from real data from the perspective of classifiers. This overstatement undermines the credibility of the paper's claims. The authors should acknowledge the limitations of their generated images, especially in the context of adversarial attacks or other scenarios where subtle differences can be exploited.
2. The experimental setting in this paper differs from existing studies. Here, the authors fine-tune the base model with newly generated data in each iteration, whereas previous studies fine-tune the new model with newly generated data in each iteration. This discrepancy raises concerns about the generalizability of the findings. The authors' approach may not capture the dynamics of model collapse as observed in prior research, where the model is iteratively trained on its own outputs. This difference could lead to different conclusions about the causes and mitigation of model collapse.

### Questions
1. Different fine-tuning approach:
- Why does this paper fine-tune the base model with newly generated data in each iteration, while existing studies fine-tune the new model in each iteration? I believe this difference makes it distinct from the "model collapse" phenomenon discussed in prior research.
2. Clarification on ‘clip’ metric (line 208):
- What does the 'clip' metric refer to in this context? Could you provide more details?
3. Effectiveness of guidance interval:
- Could the guidance interval proposed by [b] effectively slow down the collapse rate?
4. Alternative fine-tuning strategy:
- Could you try fine-tuning the new model instead of the original model and show some example results?
5. Choice of k=6:
- Why was k=6 chosen for the experiments? Could you elaborate on the reasoning behind this selection?
6. Meaning of symbols in Fig. 2:
- What do the symbols C, W, S, L, and CLIP skip represent in Fig. 2?
7. Fine-tuning the text encoder (Fig. 2):
- Why is fine-tuning the text encoder considered an option in Fig. 2? In my view, the text encoder should not be fine-tuned. Could you explain the rationale for this choice?

[b] Kynkäänniemi T, Aittala M, Karras T, et al. Applying guidance in a limited interval improves sample and distribution quality in diffusion models[J]. arXiv preprint arXiv:2404.07724, 2024.

### Soundness
3

### Presentation
2

### Contribution
3
