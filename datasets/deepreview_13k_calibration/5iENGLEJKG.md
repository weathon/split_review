# INViTE: INterpret and Control Vision-Language Models with Text Explanations

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Large-scale pre-trained vision foundation models, such as CLIP, have become de facto backbones for various vision tasks. However, due to their black-box nature, understanding the underlying rules behind these models’ predictions and controlling model behaviors have remained open challenges. We present INViTE: a framework for INterpreting Vision Transformer’s latent tokens with Text Explanations. Given a latent token, INViTE retains its semantic information to the final layer using transformer’s local operations and retrieves the closest text for explanation. INViTE enables understanding of model visual reasoning procedure without needing additional model training or data collection. Based on the obtained interpretations, INViTE allows for model editing that controls model reasoning behaviors and improves model robustness against biases and spurious correlations. Our code is available at https://github.com/tonychenxyz/vit-interpret.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to interpret the “latent” representations of vision transformers. To interpret a visual token representation of layer K, the paper proposes to disable the self-attention for layers higher than layer K, and then use the final layer representation to calculate text-token similarity. The ability to find such latent tokens enables several applications: fixing typographical attacks, intervening in the reasoning procedure, and reducing spurious correlations.

### Strengths
Such an interpretation approach is definitely new; it is a novel observation that one could simply disable the self-attention from above a certain layer (K) and then use the representation as a representation for latent token at layer K. The paper uses causal intervention and saliency map overlap to verify the effectiveness of the approach.

### Weaknesses
My main concern is that I do not quite see the method’s advantage compared to gradient-based methods that find important input regions (e.g., Grad-CAM) given a text description.

(1). The first question is why we want to find latent tokens but not salient regions?

Conceptually, the biggest advantage is that there might exist “high-level” and “abstract” latent tokens. For example, in Figure 3, using Grad-CAM to find regions corresponding to “overpass” might result in a lot of matched image patches while using the proposed method can find one single latent token corresponding to the concept.

However, this is not reflected in the quantitative experiments. For the fixing typographical attacks and reducing spurious correlations experiments, ideally a gradient-based baseline could be included, where we seek to use grad-cam to find and zero-out a few important image patches. Then one could compare whether the proposed method can achieve the same performance but zeroing out less tokens. Otherwise, it is hard to claim that the method can find “high-level” latent tokens.


(2). Suppose we wish to find latent tokens corresponding to a text description, why should we resort to the proposed method but not a gradient-based method where we calculate the gradient with respect to each latent tokens of every layer? This seems like a more principled way to obtain important latent tokens.


### Questions
I am not sure I get the motivation behind the Intervening in the Reasoning Procedure experiment. Under what settings would this be useful?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a method to interpret intermediate representations (referred to as *latent tokens*) in vision-language Transformer models (e.g. CLIP) by retrieving relevant natural language descriptions for individual latent tokens. The authors do so by removing the self-attention operations after a latent token, and using the last layer token representation to retrieve a text description. The authors posit that the retrieved text for a latent token provides an interpretation for it. They further posit that manipulating these latent tokens can be used to edit and control model behavior.

### Strengths
- The experiments are very convincing. The author use their methodology to not only do model interpretation (which would have been sufficient imo), but also for model controllability. The results for interpretability (causality and saliency map overlap) are very convincing. 

- The controllability experiments are also very well designed, and demonstrate consistent results across three different kinds of model editing -- typography attacks, entity editing and gender debiasing.

- The paper is well-written overall. Some of the experiment setups are a little hard to understand, because the setting is slightly artificial,

### Weaknesses
 - I am skeptical of the motivation behind the methodology. Specifically, typically the CLS representation from the vision encoder is used as the query to do text retrieval in CLIP, but do we know that latent tokens corresponding to other image patches from the final layer retrieve meaningful text concepts? There is no theoretical motivation -- which isn't strictly needed, but I would be much likelier to trust the method beyond just the empirical results.

- It's unclear what the benefit of these natural language descriptions for latent tokens is, or how these descriptions should be leveraged. The examples in Section 4.3 ("Our Interpretations Reveal Visual Reasoning") do not seem very convincing, and are more about how one chooses to interpret the tokens' NL descriptions (e.g. I would not think "motor vehicle" + "valley" = "overpass" is necessarily a correct reasoning, let alone whether that's actually how the model went about the reasoning process).

### Questions
- What is the benefit of the proposed method over the saliency maps that are presented in Figure 3?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to interpret the semantic meaning of vision foundation models by retrieving the closest text description. Specifically, the method turns off the inter-token cross attentions in the latter layers and only keeps the self-attention, in order to get the final CLS representation that corresponds to only the target token. Saliency attention visualizations and quantitative results are provided to show the correctness of the interpretations. To demonstrate the application of the proposed method in terms of controlling and intervening the model behaviors, the paper runs experiments on three tasks: fixing topographical attacks, intervening object entities, and removing gender bias.

### Strengths
1. The paper runs experiments on three practical tasks to showcase the applications of the derived interpretations. It is exciting to see that the interpretations can improve the model’s robustness towards text/topographical attacks and gender bias, as well as intervening the model’s decision in object classification in satellite images.

2. Abundant visualizations and numbers are reported to show the advantage of the proposed method over random intervention.

### Weaknesses
1. The major limitation is that the method can only be applied on the CLIP model (at least only CLIP is shown in the paper). Since CLIP aligns the visual embeddings (CLS) with the texts, the method can retrieve texts based on the CLS embedding after turning off the cross-attentions. Otherwise, if the model’s token embeddings are not trained to be aligned with the texts, it is doubtful whether the method can still work or not. It would be best if the authors can show that the method can workin on other non-text trained models like MAE, DINOv2, etc.

2. Most of the comparisons are against the “random baseline”, which is not a very strong baseline. For example, additional stronger baselines should be compared with, like the ones listed in the “model interpretation” in the related works sections. Moreover, it’s better to include related work [1].

3. The method is based on text-retrieval, which assumes a finite set of candidate texts (closed world). In related work, the authors criticize that Koh et al (2020) (concept bottleneck network) is limited to a closed vocabulary, but isn’t this work also closed vocabulary?

4. The method is training free. As an extension, can the method be extended for improving model training?

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel method to interpret the latent tokens in pretrained vision-language models like CLIP using natural language descriptions. The key idea is to map the latent token embeddings to the final output space by disabling self-attention and propagating through the feedforward layers. This allows retrieving the closest text description for each token from the model's vocabulary. The authors demonstrate how these interpretations can provide insights into the model's reasoning and enable controlling model behaviors like fixing adversarial attacks, reducing biases, and replacing entities.

### Strengths
1. Novel method to interpret transformer tokens with language; doesn't require retraining or new data.

2. Solid motivation,clear methodology, extensive experiments across multiple datasets.

3. Well-written paper with clear explanation of the approach and results.

4. Interpretability is valuable for ML model transparency and trust. Controlling models via token editing has useful applications.

### Weaknesses
1. More analysis could be provided on how distribution shifts from removing attention affect interpretation quality. Specifically, the method disables self-attention, which fundamentally alters the information flow within the transformer. This could lead to the latent token embeddings being mapped to the output space in a way that is not representative of their original function within the model. The paper should include a more rigorous analysis of how this manipulation impacts the quality and reliability of the interpretations.

2. More comparisons to related interpretation methods would further validate advantages. While the paper presents a novel approach, it lacks a thorough comparison with existing techniques for interpreting vision-language models. For instance, methods based on gradient-based saliency maps or concept activation vectors could provide alternative interpretations. The paper should include a quantitative and qualitative comparison to these methods to better highlight the unique benefits and limitations of the proposed approach.

3. Significance could be boosted by showing applications beyond the demonstrated tasks. The paper demonstrates the method's utility in fixing adversarial attacks, reducing biases, and replacing entities. However, the broader applicability of the method is not fully explored. The authors should consider demonstrating how the method could be used in other tasks, such as model debugging, knowledge transfer, or few-shot learning, to further establish its significance.

### Questions
Can you provide more details on how the distribution shift introduced by disabling attention affects interpretation quality? Is performance very sensitive to this?

What processes did you use to create the vocabularies for retrieving token interpretations? How important is vocabulary size and coverage?

How do your interpretation results compare qualitatively to other methods like saliency maps or concept activation vectors?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
