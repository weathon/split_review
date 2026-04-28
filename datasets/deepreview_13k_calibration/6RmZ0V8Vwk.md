# Language Guided Representation Learning

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 3, 5, 5

## Abstract
Deep neural networks have achieved notable success; however, they still encounter significant challenges compared to humans, particularly in areas such as shortcut learning, texture bias, susceptibility to noise, and catastrophic forgetting, all of which hinder their ability to generalize and adapt. Humans excel in learning high-level abstractions, attributed to various mechanisms in the brain, including reasoning, explanation, and the ability to share concepts verbally—largely facilitated by natural language as a tool for abstraction and systematic generalization. Inspired by this, we investigate how language can be leveraged to guide representation learning. To this end, we explore two approaches to language guidance: Explicit Language Guidance, which introduces direct and verbalizable insights into the model, and Implicit Language Guidance, which provides more intuitive and indirect cues. Our extensive empirical analysis shows that, despite being trained exclusively on text, these methods provide supervision to vision encoders, resulting in improvements in generalization, robustness, and task adaptability in continual learning. These findings underscore the potential of language-guided learning to develop AI systems that can benefit from abstract, high-level concepts, similar to human cognitive abilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on the impact of using language model's representation on vision tasks. The paper uses two ways to use language model to "guide" the vision model, one is by explicitly align the vision model embedding and language model embedding, another is by implicitly use and freeze (part of) pretrained language model parameters as part of the model pipeline to make prediction on images. The authors demonstrated the usefulness of the two methods by showing that with language guidance, the model is more robust to out of distribution examples, texture bias, and adversarial attack, and it can do better on continual learning.

### Strengths
The paper covers experiments in extensive aspects to illustrate the benefits of language model guidance. The setting of the experiment is comprehensive, and I believe it can be reproduced.

### Weaknesses
 - The idea behind this paper is not very novel. Starting from CLIP, it is well known that the alignment between language and vision can bring benefits (for example, [1] can do zero shot generalization to image classifications with new labels).
- The setting of the paper seems outdated. Nowadays, VLMs like LLaVA has been widely used, but the paper still focuses on ResNet and CIFAR-10. A good question here is what the implication of the results is, as the state-of-the-art models has already been using vision language alignment to achieve much more.
- The presentation of the paper can be improved. For example, eq (2) and (3). Seem like $f_v$ and $f_l$ are defined across a set of datapoints, $S_v(i, j)$ is the cosine similarity between image embeddings of two data points, indexed as $i$ and $j$. The current presentation is very misleading.
- Similarly, for Sec 4.2, the authors failed to clarify what is the input to classification head, and what is exactly the input to the language block. My concern here is that the paper uses ResNet-18, which is not natural to convert to input of language model block.
- Figure 3 is hard to read and interpret, thus the implication is unclear to me.

### Questions
- In Figure 1, I don't understand why CKA can be applied here. What is $X$ and $Y$ in eq (4)?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies language guided representation learning and its potential techniques for incorporating language guidance into vision representation learning. The paper considers two techniques for incorporating language guidance, one based on explicit guidance (ExLG) and the other based on implicit guidance (ImLG). The paper investigates the effect of language guidance on sample efficiency, OOD generalization, spurious feature learning, shortcut learning, and robustness. Generally, the paper finds ExLG improves on all aspects over traditional approaches for performing vision representation learning.

### Strengths
A thorough improvement from language guidance: I found the paper to do a reasonably good exploration of language guidance with strong results.

Consistent and large amount of experimentation: The paper has many experiments comparing its two proposed methods. 

Interesting analysis: Figures 3, 4, and 5 show some interesting analyses from language guidance, showing feature maps on the Skewed-CelebA dataset, the effects of stylization, etc. These were pretty useful for understanding language guidance more deeply.

### Weaknesses
My main concern in the paper is related to novelty and clarity on its positioning. Given the large number of related papers in the field, I’m finding it a bit difficult to describe the guiding question the paper aims to answer. This leads to the weaknesses I describe below.

•	Motivation of the methods: Overall, I found the approach for ExLG and ImLG a bit difficult to motivate fully since I don’t see how they map language guidance approaches for vision representation learning papers from the past. I don’t see how these findings are interesting or relevant to the way people design language guidance for visual representation learning if ExLG or ImLG aren’t well motivated methods themselves. In particular, with ImLG, could the authors give some methods that use something similar?

•	Distinction with related papers: First, I strongly recommend that the authors write a related work section. This is necessary for positioning the paper in relation to other work that incorporates language guidance for visual representation learning. Overall, I found myself puzzled over the novelty of this paper. The paper finds many benefits from language guidance that has been found in prior papers that use language guidance [1, 2, 3]. The paper tries to differentiate itself from CLIP, which uses a joint language encoder by arguing that the approach uses a frozen language encoder. However, there are plenty of other papers that use a frozen text encoder [1, 2, 3] for language guidance. These papers also report similar findings of improvements over robustness, generalization, etc., although not all features are covered in the search I did.

•	Focus on vision domain: For a paper that has the title on language guided representation learning, I would have expected a focus on more domains than just vision. Would this extend to the other modalities? I would prefer if the title just stated that this was focused on vision instead.

### Questions
•	Can the authors more clearly explain what ImLG is doing? I found myself confused about the approach. 
•	I found it interesting to see cases where ImLG was worse than the baseline. For example, T4 in Figure 6. Would the authors mind providing some discussion?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors investigate using natural language to enhance visual representations, and how this enhancement affects systematic generalization and catastrophic forgetting in neural networks. More specifically, inspired by human cognition, the authors propose that language, as a tool for abstraction and concept-sharing, can help guide DNNs to better, more abstract representation learning. The authors explore two main approaches: Explicit Language Guidance (ExLG), which aligns visual representations with high-level language descriptions, and Implicit Language Guidance (ImLG), where a pre-trained language model “indirectly” enhances the vision model. Both methods are tested extensively across diverse tasks such as generalization to new data (IID and OOD), among others. Perhaps unsurprisingly, the results show improvements over baseline models. ExLG performed better on generalization tasks, while ImLG showed advantages in robustness and shortcut learning. As seminal work in the past (e.g., CLIP), the study highlights language guidance as a powerful tool for creating models that generalize and retain knowledge more effectively.

### Strengths
1. The paper is well written and clearly explained
2. Figures are clear and informative. 
3. The topic is timely and of extensive interest and applicability.

### Weaknesses
The main, and crucial weakness of this work is its novelty and scope. Although, as the authors point out, their method slightly differs from other VLMs whose representation “fuse” vision and language embeddings, both the added theoretical and empirical value of this paper is poor:

1. Other papers already make the point that language can generate richer representations that have an impact on the issues highlighted by the authors.

2. I would compare the proposed methods with other VLM models, in order to show concrete empirical value of this paper.

### Questions
*If you mention the Global Workspace Theory, I think it’s only fair to cite at the very least Dehaene (1998) and I would also include Baars (1994).
*Line 123, CKA is first presented without spelling the acronym.
*I would define what a “conventional classification model” is.

Typo:
Line 036: “…is one of the aspects of human cognition is still a challenge for neural networks...” -> that is still
Line 049: “...context of continual learning (?)...”  issue with citation.
Line 099: “...System 2 (Explicit) processing (Daniel, 2017).” Citation should be Kahneman.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studied the effect of additional language information in image tasks training. The research found out that language guidance in the form of explicit representation alignment and implicit access to the language model improved ResNet's
- OOD generalization
- shortcut learning (reduction of spurious correlations)
- bias on textures
- robustness against adversarial attacks
- continual learning (reduction of catastrophic forgetting)

### Strengths
1. Thoroughly studied the role of representation learning in language models.
2. Identified that the guidance of language reduced many unwanted behaviors in image models training, such as catastrophic forgetting and the vulnerability against adversarial attacks.

### Weaknesses
1. The evaluation needs to be fair. For all the experiments, we should keep the total (frozen) parameter count the same, and (ideally) the tunable parameter count the same. Otherwise we may attribute the better performance of ExLG/ImLG comparing to the baseline models to the increase of the number of parameters, not language-guidance.
2. You should add more baselines/ablations. For example, in the "continual learning" experiment, it is unclear whether the reduction of catastrophic forgetting from ER to ExLG/ImLG is due to the language guidance or access to a large bank of information (be it language/image/...). Specifically, the continual learning setup needs more rigorous controls to isolate the impact of language guidance from other factors, such as the inherent capacity increase from the additional language model.
3. You should conduct a more thorough related work analysis. I haven't conducted a thorough literature review on the topic, but this paper should have a "related work" section that distinguishes it from other related concepts or frameworks, such as CLIP.
4. There is a lack of explanation or insight into how the language guidance improved the image's performance on these tasks. Consider how the alignment loss improved the representation alignment by offering some interpretability analysis, such as probing the learned resnet's inner representations, https://arxiv.org/pdf/2410.06940 applies on diffusion models, but did several layer-by-layer analyses, which I think is valuable at improving the insights of your work.

### Questions
1. Could you clarify again what is the core difference between your approach with other language/vision representation alignment approaches, such as CLIP? Especially for the explicit guidance.
2. In section 5.3 and figure 4, what is the "stylization alpha"? It seems that this is not explained.
3. In figure 7, how did you calculate the "plasticity" and "stability"? How are these precisely defined mathematically?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper asks whether non-visual language models provide advantages when used to create an image representation, over a traditional end-to-end image classifier alone. It compares a traditional classifier with a proposed “ExLG” vision encoder and an “ImLG” encoder, where ExLG adds a tung-mori student-teacher setup to align the image representation with a language representation, and ImLG incorporates a frozen pretrained language model as the final stage of the vision encoder.  With this setup, they train on several standard classification problems and compare performance on low-data regimes, OOD generalization, strongly biased data, and adversarial robustness, and continual learning. They conclude that the incorporation of pretrained language models is helpful in all these settings.

### Strengths
The community has a lot of interest in the language models’ capabilities to represent the visual world without ever having been exposed to an image during training. The paper poses natural questions, looking beyond basic classification performance to ask whether incorporating a language model improves the inductive biases for a model. The benchmark datasets used to investigate OOD and bias behavior are reasonable, and the robustness test is appropriate.

### Weaknesses
The paper as currently presented doesn’t have enough evidence to support its broad claims. The claim is that several types of robustness improve when language modeling is incorporated (implying that there are benefits from having the “knowledge” derived from lots of text training), but there are several possible confounders that aren’t investigated.

For example, the addition of extra loss terms (for ExLG) or extra layers (for ImLG) could have a regularizing effect regardless of the specific content of those extras, which could mean that there is nothing special about language knowledge.  The paper would be strengthened if it presented clearer evidence that the essential benefits come from the fact that the extra model involved is a language model trained on lots of text, as compared to e.g., a random neural network. Ablations are needed on: what type of text is used in ExG; how powerful the language model is; whether it matters if the language model is trained on natural text or some non-object related task, or left uninitialized. Ideally the hyperparameters can be held fixed while comparing the use of a language model to a baseline with the same computational form that doesn’t have the benefit of large-scale text training.

The paper’s investigations are related to the idea articulated in the recent paper “The Platonic representation hypothesis” by Huh, and it would be nice to cite+connect it.

In the ExG case, it is unclear what text is used for aligning the representation. Is it image-specific text, or class-generic text, or something else; how was it chosen, and how important is this choice? What would be the effect of some text-per-class that has nothing to do with the class?

As the language model becomes more powerful, does it improve OOD, resistance to bias, robustness, and CI behavior? Only one small model size comparison is done, and only on basic classification accuracy.

The claim is that incorporating a language model helps, but does it need to be a language model pretrained on real text?  Would performance benefits be obtained from a randomly-initialized language model? What about an early checkpoint of a language model with poor performance, or a model trained on non-visual-world-descriptive text such as a code LM?

### Questions
In the ExG case, it is unclear what text is used for aligning the representation. Is it image-specific text, or class-generic text, or something else; how was it chosen, and how important is this choice? What would be the effect of some text-per-class that has nothing to do with the class?

As the language model becomes more powerful, does it improve OOD, resistance to bias, robustness, and CI behavior? Only one small model size comparison is done, and only on basic classification accuracy.

The claim is that incorporating a language model helps, but does it need to be a language model pretrained on real text?  Would performance benefits be obtained from a randomly-initialized language model? What about an early checkpoint of a language model with poor performance, or a model trained on non-visual-world-descriptive text such as a code LM?

### Soundness
2

### Presentation
3

### Contribution
2
