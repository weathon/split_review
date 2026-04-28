# Holmex: Human-Guided Spurious Correlation Detection and Black-box Model Fixing

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
We propose Holmex, a method for human-guided spurious correlation detection and black-box model fixing. \ours{} provides a way for humans to be easily involved in the deep model debugging process, which includes 1) detecting conceptual spurious correlation in training data and 2) fixing biased black-box models by white-box models. In the first step, we leverage pre-trained vision-language model to construct separable vectors for some high-level and meaningful concepts, and we further propose a novel algorithm based on concept vectors that is more stable than previous methods. In the second step, unlike previous works, we do not constrain the original biased model to be interpretable and editable. Instead, \ours{} is compatible with arbitrary black-box models. To this end, we propose transfer editing, a novel technique that can transfer the revision in interpretable models to the black-box models to correct their spurious correlations. Extensive experiments on multiple real-world datasets demonstrate the effectiveness of \ours{} in detecting and fixing spurious correlations. The source code and datasets can be found in https://anonymous.4open.science/r/Holmex-15DF.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents HOLMEX, a method to identify a model's reliance on spurious correlations, and fix it. The general idea is to construct concept vectors using a large pre-trained model like CLIP, and then surface the correlation between a concept vector and a label to a human. The human can then use their inductive bias/domain knowledge to trim correlations that happen to be spurious. Once the spurious concept and label tuple is detected, the authors then propose a transfer technique to edit the model. In the transfer editing technique, you train two 'white-box' models: 1) where the spurious concept has been removed, and 2) where the spurious concept is present. These whitebox concepts are basically softmax linear layers on top on the clip representations for the input samples. The hope here is that the weights of these two whitebox models capture the spurious direction. To perform transfer editing, you take a difference between the logits of the two whitebox models, and add that to the logits of the blackbox model. They couple this approach with ensembling and show that such an approach leads to improved model performance.

### Strengths
Overall, this papers sets out an important problem and presents a scheme for addressing that problem. I list below some nice aspects of this work: 

- **Modular Approach**: The paper separates detecting spurious correlation from fixing it.
- **Clear scheme**: The paper describes its scheme very clearly, and tries to justify each step of the scheme.
- **Demonstrates performance improvement**: The paper also shows that the transfer editing schemes and ensembling leads to improved performance across the board across all the tasks tested.
- **Control experiment**: I liked that the authors included a control experiment for a model with no spurious signals. The approach shows the kind of null behavior you would want in that setting.

### Weaknesses
Below I discuss some of the weaknesses of the scheme presented here. 

- **Too many moving parts**: While the scheme presented is modular. As it stands, there are several decisions that need to be gotten right for the overall scheme to work. Here is what I mean: 1) it looks like the traditional concept vectors (derived from model embeddings) are ineffective, so we need a modified version, 2) One needs a background word, 3) One needs to train a linear classifier to estimate correlations, 4) One needs to train two separate linear classifiers again to do editing for each spurious concept that you want to remove. This means that if you have 20 concepts to remove, then you would be training 40 linear classifiers to remove the effect of these 20 spurious concepts for that label alone. If any of the steps that I have listed does not work, then the entire scheme does not work. The reliance on multiple independently trained components introduces significant fragility to the overall approach. For instance, the choice of background word is not rigorously justified and could significantly impact the quality of the concept vectors. Furthermore, the training of multiple linear classifiers introduces a computational overhead and potential for overfitting, especially if the number of spurious concepts is large. The paper does not provide any analysis on the sensitivity of the method to the choice of background word or the robustness of the trained linear classifiers. 

- **Over reliance on CLIP**: I think the dependence on CLIP in this work is quite worrisome. I think the CLIP embeddings are effective probably because the CLIP dataset is quite large, so those embeddings don't suffer from the issues the authors noticed. For example, imagine that you wanted to now fix a model that solely relies on CLIP embeddings as its classifier, then I assume the approach here would be ineffective? The paper does not address the scenario where the model to be fixed is itself based on CLIP embeddings, which is a significant limitation. If the spurious correlations are present within the CLIP embeddings themselves, then the proposed approach may not be able to disentangle them. This raises questions about the generalizability of the method to models that do not rely on CLIP or other large pre-trained models. The authors should discuss the limitations of the approach in settings where CLIP is not applicable or when the model to be fixed is based on CLIP itself. 

- **Logit Correction in Transfer Editing**: I am surprised that the editing scheme here works since we can simply think of this as shifting the distribution of the logits. However, it requires that the output space for the black-box models be the same size as that of the model you want to edit. The paper does not provide a theoretical justification for why a simple logit shift would effectively remove spurious correlations. It is unclear why adding a difference in logits from two white-box models would lead to the desired disentanglement. The authors should provide a more detailed analysis of the effects of this logit correction on the model's decision boundaries and its ability to generalize to unseen data. It is also unclear how this approach would handle cases where the spurious correlation is not a simple linear shift in the logit space.

### Questions
Here are some questions for the authors:
- How do you think the transfer editing approach here relates to the task vectors approach? See: Editing models with Task Arithmetic, and Task Arithmetic in the Tangent Space. It seems like you could avoid training two white-box models by adopting the task arithmetic editing approaches in the above papers.

- What is the justification for why the concept vectors from raw embeddings does not work? What if I have a model that just uses the clip embedding itself for classification, but the clip embedding has spurious correlations too? Is this approach just inheriting the limitations of clip representations? What about if I have satellite images or a setting where CLIP is not useful?

- Ensembling: Did you test ensembling alone in Table 3? It would be interesting to see whether simply ensembling recovers the performance gains that you see in that table. I ask this because ensembling has been shown to give OOD benefits.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Holmex, a method designed for human-guided spurious correlation detection and black-box model fixing. It enables humans in the deep model debugging process by addressing two main tasks:

Detecting Spurious Correlations: Holmex uses pre-trained vision-language models to create separable vectors representing high-level and meaningful concepts. It proposes a novel algorithm based on these concept vectors to detect conceptual spurious correlations in training data, and this algorithm is more stable than previous methods.

Fixing Biased Black-Box Models: Unlike prior approaches that focus on making biased models interpretable and editable, Holmex is compatible with arbitrary black-box models. It introduces a novel technique called "transfer editing" to transfer revisions made in interpretable models to correct spurious correlations in black-box models.

### Strengths
The strengths of the paper are as follows:

1. Improved Concept Embeddings: The paper enhances the quality of concept embeddings by reducing the entanglement of raw text embeddings. It achieves this by subtracting a vector of the background word, which is a useful contribution. This improvement is crucial for accurate detection of spurious correlations.

2. Novel Detecting Algorithm: The paper introduces a novel detecting algorithm that is specifically designed to reveal correlations between concepts and labels in a stable manner. This algorithm enhances the reliability and stability of the spurious correlation detection process.

3. Transfer Editing Technique: The paper proposes a transfer editing technique, which is a novel method for transferring revisions made by humans in white-box models to black-box models. This approach enables the fixing of spurious correlations in black-box models, making it a versatile and impactful contribution.

The paper conducts extensive experiments on multiple datasets with different types of biases, including co-occurrence bias, picture style bias, and class attribute bias. This demonstrates the effectiveness and applicability of the Holmex method across a range of real-world scenarios, which is a significant strength in showcasing its practical utility.

### Weaknesses
The paper does not cite several works in this domain. Some of the missing citations are:

1. Salient ImageNet: How to detect spurious correlations in deep learning? ICLR 2022.
2. Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations. ICLR 2023.
3. Wilds: A benchmark of in-the-wild distribution shifts. PMLR, 2021.

Salient ImageNet provides a scalable methodology for identifying spurious correlations at scale. The paper does not include any comparison with that method, rather no citation is provided. Similarly, the latter paper provides a method for robustifying against spurious correlations. Again, no citation provided.

This provides a strong evidence that the paper is written without a thorough research of the prior work.

### Questions
There is no comparison against several of the group robustness methods presented in the prior works. Given the extent of the literature on robustness against spurious correlations, results comparing the accuracy of the proposed method against the baseline are not acceptable.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Holmex for detecting and mitigating spurious correlations based on concept vectors. In spurious correlation detection, the method is based on CLIP and makes two contributions: (1) subtracting a background concept vector (Section 4.1.2) and (2) proposing a new algorithm for stable detection of spurious correlation. In spurious correlation mitigation, the paper proposes transfer editing to mitigate spurious correlations in a black box model. The experiments are conducted on multiple datasets and tasks to show Holmex’s performance on spurious correlation detection and mitigation.

### Strengths
* The paper studies an important problem.
* The code is released for better reproducibility.

### Weaknesses
## Concerns about the method

### Subtracting background concept vector (Section 4.1.2) 
First, I am confused by the motivation of this part of the method. I understand the argument that irrelevant concepts (e.g., cat and airplane) have high cosine similarities. However, I am completely lost for the “model editing experiment” where “a linear layer after the concept activation layer” was trained. Such as the model editing experiment was not introduced before and the details are completely left to Appendix A.1, which was not clear to me either. Second, I wonder why not a simple alternative solution would not suffice. Following the equation on the bottom of Page 4, we can compute 
$P(y = c \mid z) = \frac{\exp(t_c^\top z / T) }{\sum_{c' \in C} \exp(t^\top_{c'} z / T )}$
, where $T$ is temperature in softmax, $c$ is one concept, and $\mathcal{C}$ is the set of all concepts. You can choose a low temperature to reduce the similarity among different concepts. While the authors use cosine similarity, the core issue is that the raw concept embeddings are not discriminative enough, leading to high similarity scores between unrelated concepts. Applying a temperature scaling to the cosine similarity before the softmax could potentially sharpen the probability distribution over concepts, making the concept scores more discriminative without requiring the complex background subtraction and model editing steps.

### Transfer difference of logits (step 2 in Section 5.1, page 7)
Different models (i.e., white-box and black-box) can have different scales in logits. Although the paper has a discussion of “The scale of logits” on page 7, my question is still not answered. The paper assumes that the logits of the white-box and black-box models are on comparable scales, which is a strong assumption. Logit scales are influenced by various factors, such as model architecture, training data, and optimization procedures. Without proper normalization or calibration, directly transferring logit differences can lead to suboptimal results. The method lacks a mechanism to account for potential scale differences, which could limit its generalizability across diverse models.

## Concerns about the experiments

### Datasets and Metrics
I appreciate the authors' efforts in doing experiments for three types of biases. However, I don’t think the paper explains the motivation for creating new evaluation settings and metrics. There are many previous benchmarks and evaluation settings for both (1) spurious correlation detection ([1,2] and (Wu et al., 2023)) and (2) bias mitigation benchmarks ([3-6]). The paper introduces new metrics and evaluation settings without a clear justification for why existing benchmarks are insufficient. This makes it difficult to compare the proposed method with existing approaches and to assess its true performance. The lack of a clear motivation for these new settings raises concerns about the generalizability and relevance of the experimental results.

### Comparison Methods
The proposed method is only compared with a limited number of methods. For spurious correlation detection, the paper is only compared with the PCBM method and its variants. Why not compare with DISC (Wu et al., 2023), which is also a concept-based method? For spurious correlation mitigation, many methods, especially methods that do not rely on concept vectors [1,2,7-9], are not compared. The paper's comparison is limited, especially in the bias mitigation area. The absence of comparisons with methods that do not rely on concept vectors makes it difficult to assess the proposed method's relative strengths and weaknesses. A more comprehensive comparison is needed to establish the method's effectiveness and novelty.

### Questions
I expect the authors to address my concerns in the response:

1. Why not use software with temperature to address the problem of irrelevant concepts with high similarity?
2. Do you assume that white-box and black-box models share a similar logit scale? If so, this approach is not generalizable enough to claim the “black-box model fixing.”
3. Why create new evaluation settings with new metrics?
4. Add experiments to compare with a broader range of methods.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach for detected spurious correlations in datasets and transfer editing to transfer the interpretable knowledge to a black box model and improve model accuracy on various tasks. The paper discussed how to detect spurious correlations between concepts in the images and class labels using vision language models such as CLIP. It proposes to train 2 white box models based on frozen CLIP model’s autoencoder backbone and trainable MLP layer the weights of which represent the interpretable importance scores of the concepts (similar to TCAV). One of the white-box models contains the spurious concepts and the other one doesn’t. The differences between 2 white box models are then transferred to the black-box model.
The authors conduct multiple experiments to show the effectiveness of their approach.

### Strengths
1) The paper addresses an important problem of identifying and fixing spurious correlations in vision models.
2) It discusses the challenge of entangled concepts and proposes a technique to improve disentanglement using a baseline/neutral concept such as the concept of others.
3) The paper performs through experimentation for different types of spurious correlations (Co-occurrence, Picture style and class attribute).

### Weaknesses
1) The paper has multiple important contributions but they are a bit intertwined. In some cases it sounds that the authors use the term bias when they refer to spurious correlations. It would be good to make the terminology consistent and clear.
2) Overall I think that it is a bit hard to follow the paper in terms of understanding the full picture. There are multiple models involved and figure 1 attempts to explain it but it is unclear what bias is and what `compare weights with concept vectors` really means. The description of how the concept vectors are derived and compared to the weights of the white-box models is not sufficiently detailed, making it difficult to grasp the core mechanism of spurious correlation detection.
3) It is unclear how the human is involved in the guiding of spurious correlation detection and model fixing. It seems that according to the algorithm listing 1, the output of the algorithm is presented to humans but it is unclear how humans guide the process as the title of the paper suggests. The paper lacks a clear explanation of the human-in-the-loop interaction, specifically how human feedback is incorporated to refine the spurious correlation detection and model fixing process.
4) In Figure 4 it is unclear how we decide to incorporate the spurious example C_cat into the white-box. How is human involved in that process ? The criteria for selecting and incorporating specific spurious examples into the white-box model are not well-defined, and the role of human intervention in this selection process is ambiguous.

Minor

eep learning models -> deep learning models

### Questions
1) How scalable is the proposed method  ?
2) Is accuracy the main metric used in evaluation experiments ?
3) Why are the experimental results mainly focused on showing the advantage for ensemble models ?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
