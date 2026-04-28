# Looking beyond the surface with Contrastive LEarning with Anti-contrastive Regularization (CLEAR)

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 5, 3, 3, 3

## Abstract
Learning representations that are robust to superficial sources of variability is important to ensure such variability does not impact downstream tasks. For instance, in healthcare applications, we might like to learn features that are useful for identifying pathology, yet have similar distributions across diverse demographic groups, leading to more accurate and equitable diagnoses regardless of background or surface characteristics. More broadly, this capability can improve the generalizability of our representations by mitigating unwanted effects of variability not seen during training. In this work, we suppose that data representations can be semantically separated into two components: $content$ and $style$. The $content$ consists of information needed for downstream tasks -- for example, it is predictive of the class label in a downstream classification problem -- whereas the $style$ consists of attributes that are superficial in the sense that they are irrelevant to downstream tasks, yet may compromise performance due to associations observed in training data that do not generalize. Here we propose a weakly supervised framework, Contrastive LEarning with Anti-contrastive Regularization (CLEAR), to effectively disentangle $content$ and $style$ in the latent space of a Variational Autoencoder (VAE). Our anti-contrastive penalty, which we call Pair Switching (PS), uses a novel label flipping approach to ensure content is recognized effectively and limited to the $content$ features. We perform experiments to quantitatively and qualitatively evaluate CLEAR-VAE across distinct data modalities. We then analyze the trade-off between disentanglement and ELBO, and the impact of various hyperparameters within our framework. Our results show that using disentangled representations from CLEAR-VAE, we can: (a) swap and interpolate $content$ and $style$ between any pair of samples, and (b) improve downstream classification performance in the presence of previously unseen combinations of $content$ and $style$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an amazing new framework named Contrastive Learning with Anti-contrastive Regularization (CLEAR-VAE). It's designed to take data representation disentanglement to the next level by separating essential "content" features from irrelevant "style" attributes. CLEAR-VAE takes the Variational Autoencoder (VAE) model to the next level by integrating a cutting-edge Pair Switching (PS) anti-contrastive regularization. This mechanism is a game-changer! It effectively disentangles content from style representations in a weakly supervised setting by penalizing style features with different content labels. This framework is a game-changer in representation learning. It allows data with similar labels to maintain similar content while style remains independent, enhancing model generalization on unseen data. CLEAR-VAE has been evaluated across image and text datasets, and it has shown incredible potential in enhancing classification performance by effectively managing content and style in latent representations. It has introduced PS regularization, content-style swapping experiments, and a novel metric to quantify disentanglement efficacy.

### Strengths
The use of Pair Switching (PS) as an anti-contrastive regularization method is new and directly addresses limitations in previous disentanglement approaches by encouraging independent style distributions across content labels.

By disentangling content and style, CLEAR-VAE enhances classification accuracy on previously unseen content-style combinations, which is valuable in applications sensitive to bias or style variance.

The framework's potential to mitigate biases in healthcare and other applications underscores its real-world impact, highlighting the model’s relevance to equitable decision support.

### Weaknesses
While the paper mentions the impact of temperature and similarity metrics in SNN loss, it could benefit from a deeper analysis of hyperparameters and their effects on performance, especially in complex datasets.

The paper could improve its impact by comparing CLEAR-VAE’s performance with other recent disentanglement methods.

Since CLEAR-VAE relies on content labels as the only form of weak supervision, the approach may be limited when label noise or ambiguities exist. This limitation is particularly relevant in real-world applications where ground-truth labels are less reliable.

### Questions
Please see the weaknesses section

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces CLEAR-VAE, a novel weakly supervised framework designed to learn semantically disentangled latent representations of content and style within VAEs. Unlike traditional methods, CLEAR-VAE leverages contrastive pairs rather than explicit ground truth labels, offering a more flexible approach to disentangling these features. Specifically, content encompasses information critical for downstream tasks, while style includes superficial and irrelevant attributes to those tasks.

CLEAR-VAE achieves disentanglement by extracting group-level content representations through groups organized by ground truth labels and by separating style from content representations without requiring labels for style attributes. To accomplish this, the framework enhances the standard $\beta$-VAE loss by introducing two additional penalties: (1) a contrastive regularization adapted from the SNN loss, which encourages similarity in $z^{(c)}$ (content) representations within the same downstream label, and (2) an anti-contrastive regularization that promotes ambiguity in $z^{(s)}$ (style) regarding the downstream label.

To evaluate its effectiveness, the paper provides both qualitative and quantitative experiments. The qualitative results confirm the successful disentanglement of content and style representations. At the same time, quantitative comparisons against ML-VAE and baseline models demonstrate CLEAR-VAE’s superior performance and generalizability to unseen combinations of style and content.

### Strengths
1. **Problem Significance**: This paper addresses a significant challenge—disentangling content and style representations in VAEs. This approach not only enhances interpretability but also increases the model's robustness against superficial sources of variability, making it better suited for downstream tasks.

2. **Elegance of Anti-Contrastive Regularization**: The design of the anti-contrastive regularization is both elegant and effective. By flipping the labels of positive and negative pairs in $L_{SNN}^{(s)}$, it achieves a similar effect as directly minimizing $-L_{SNN}^{(s)}$ while ensuring that the regularization term remains non-negative. This method simplifies model optimization, eliminating potential issues related to negative terms.

3. **Comprehensive Evaluation**:
   - **Qualitative**: The results of the swapping and interpolation operations are impressive, effectively showcasing the model's disentanglement capabilities (see Fig. 3, Fig. 4, Appx. A.6).
   - **Quantitative**: The setups for evaluating the model's generalizability are well-defined, offering clear insights into performance (e.g., Table 2).

### Weaknesses
1. **Core Innovations and Clarity**: The core contributions of this paper, according to the authors, are a weakly supervised framework and an anti-contrastive regularization for style representation.
   - **Weakly Supervised Framework**: For semantic disentanglement of style and content, the authors introduce a weakly supervised framework. However, they omit comparisons with recent similar works, which could lead to misunderstandings that this is the first use of a weakly supervised framework in this context. For instance, other papers have also adopted weakly supervised approaches, such as:
     - *["SW-VAE: Weakly Supervised Learning of Disentangled Representations via Latent Factor Swapping"](https://arxiv.org/abs/2209.10623)*
     - *["Weakly Supervised Disentangled Generative Causal Representation Learning"](https://jmlr.org/papers/v23/21-0080.html)*
   - **Anti-Contrastive Regularization**: The authors state that the benefit of anti-contrastive regularization over direct optimization of $-L_{SNN}^{(s)}$ is that it avoids complicating the minimization of final loss. However, this claim lacks further explanation or experiment validation, which weakens its persuasiveness regarding the ''complication'' mentioned.

2. **Some Mathematical Errors and Confusing Sentences**:
   - The VAE loss in Equation 1 should be the negative ELBO.
   - The two symbols $L_{SNN}^{(s)}$ and $L_{SNN^{(s)}}$ have been used interchangeably, confusing the reader.
   - In Equation 9, *z\** is supposed to represent the latent variable with the maximum normalized mutual information, but there is no annotation provided.
   - In line 358, it is unclear why contrastive regularization is applied specifically to the EOS token's latent representation, while KL regularization applies to the entire set of contextualized embeddings.

### Questions
1. In the quantitative experiments, the performance advantage of CLEAR-VAE over the baseline model exhibits differing trends across datasets as the value of $K$ increases(Fig. 6). Specifically, on the styled-MNIST dataset, this advantage diminishes, whereas on the CelebA dataset, it amplifies. Given that both datasets are image-based, it would be beneficial for the authors to provide an explanation for this discrepancy.
2. In line 233, the phrase *"we will encourage the representation to be ambiguous about the supervised label"* raises a question: does this imply minimizing $ I(z^{(s)}; y) $ or maximizing $gMIG(y)$?

### Soundness
3

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
This paper introduces CLEAR-VAE (Contrastive Learning with Anti-contrastive Regularization for Variational Autoencoders), a framework designed to disentangle content and style components in data representations. The authors propose a new Pair Switching (PS) technique to ensure style features remain independent of the content, enhancing model robustness against superficial variations. CLEAR-VAE’s performance is demonstrated across multiple datasets, including Styled-MNIST, CelebA, and Amazon Product Reviews, with both qualitative and quantitative evaluations of the learned disentangled representations.

### Strengths
- **Novelty and Contribution**:
    - The authors address the challenge of disentangling style and content without relying on explicit style labels. The proposed PS technique and weakly supervised contrastive framework represent a meaningful advance in disentangled representation learning.
    - The disentanglement method has potential applications in real-world scenarios where spurious correlations in training data (e.g., demographic biases) can affect model generalizability and fairness.
- **Thorough Experimental Analysis**:
    - The paper presents comprehensive experiments, including swapping and interpolation tasks, to visually illustrate CLEAR-VAE’s disentangling capabilities. Moreover, quantitative measures of generalizability on unseen style-content combinations reinforce the practical benefits of CLEAR-VAE.

### Weaknesses
- **Limitations of Experimental Setup**:
     - The study uses relatively simplified datasets, such as Styled-MNIST and CelebA, for experiments, which may limit the understanding of CLEAR-VAE’s performance on more complex data. Testing the model on more challenging real-world datasets, particularly those with higher-dimensional variations in style (e.g., medical imaging data), would better showcase its generalizability and robustness.
- **Limited Baselines**: There are limited comparisons to baseline approaches. In [1], more approaches working in the weakly-supervised setting are discussed that could also serve as VAE-baselines, e.g. Group VAE. [2] propose a method that can automatically infer the group size of shared factors during training, which might at least be worth discussing in the related work section. And what about comparisons to other contrastive learning approaches?
- **Motivation**: I am not sure the motivation for the approach is clear to me. Given that the content labels are available during training and the assumptions state that only content labels are necessary for downstream prediction tasks, why are we training a VAE and not a supervised classifier?


---
[1] Locatello et al., "Weakly-Supervised Disentanglement Without Compromises", ICML 2020
[2] Sutter et al., "Differentiable Random Partition Models", Neurips 2023

### Questions
- supervised contrastive learning: Would it make sense to include the paper "Supervised Contrastive Learning" by Khosla et al.? It is based on a similar idea to combine labels and contrastive learning.
- are the assumptions realistic? This question is related to the motivation of the paper. How likely is it that we will have access to all the content labels during training? It would be interesting to analyze what happens if it is not the case. What about an experiment where only a subset of content labels is available?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel framework called CLEAR (Contrastive Learning with Anti-contrastive Regularization), designed to effectively disentangle content and style in data representations. CLEAR utilizes a single set of content labels (information required to perform a downstream task of interest), while the style source of variability (consisting of attributes irrelevant to the downstream task) is not explicitly required for model training. CLEAR introduces Pair Switching, a Contrastive Learning-inspired regularization loss and a label-switching method that enables the content latent space to learn only the content information. This framework allows for the separation of relevant content features from superficial style attributes, ultimately enhancing the generalizability of models in downstream tasks. Experimental results demonstrate that CLEAR not only facilitates the interpolation and swapping of content and style between samples but also improves classification performance in scenarios with unseen combinations of content and style. Overall, the proposed method offers significant advancements in creating robust representations that mitigate the effects of unwanted variability, particularly in sensitive applications like healthcare.

### Strengths
This paper effectively motivates the subject of disregarding style information within the content latent space by using the example of a medical healthcare application. It soundly presents the theoretical foundations of the concepts it utilizes (ELBO loss and variational auto-encoder, Mutual Information Gap, a classifier-free disentanglement measurement method, etc.). The paper illustrates its results well, both quantitatively (showing generalization in a downstream imbalanced classification scenario and demonstrating that encouraging disentanglement promotes generalization) and qualitatively (with intuitive visual experiments using CelebA and Style MNIST).

### Weaknesses
Overall, it seems that Variational Autoencoders are not the latest state-of-the-art models in terms of both 1) generation and 2) representation learning, which dampens the practical use of this method compared to diffusion models and contrastive learning methods. Additionally, the comparison with existing methods appears to be relatively weak, and similar approaches could have been discussed or compared more thoroughly, particularly the Capturing Characteristics VAE (cc-VAE) [A].

Furthermore, the Pair-Switching loss could have been compared with standard Mutual Information minimization losses, such as Total Correlation [B] or kernel Joint Entropy Minimization loss [C].

Ultimately, the experimental section seems relatively weak, as it only involves three datasets. Experiments in healthcare applications with real-world impact would have been expected.

[A] Capturing Label Characteristics in VAEs, T. Joy et al. ICLR 2021, https://arxiv.org/abs/2006.10102.  
[B] Abubakar Abid and James Zou. Contrastive Variational Autoencoder Enhances Salient Features, 2019, https://arxiv.org/abs/1902.04601.  
[C] Separating Common from Salient Patterns with Contrastive Representation Learning, R. Louiset et al., ICLR 2024, https://arxiv.org/pdf/2402.11928.

### Questions
How can this method be applied in a healthcare scenario where unwanted style attributes are often partially observed (e.g., acquisition site, demographic attributes such as age and sex are generally available in practice)? Could this approach be adapted into a semi-supervised framework that accounts for partially observed style attributes?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes a weakly supervised method to disentangle content and style latent variables in variational autoencoders (VAEs), where content variables are those that have a (non-spurious) correlation with the downstream task to solve, and style variables are the rest of them (which should not affect the downstream task). To this end, the authors propose a combination of three losses: a $\beta$-ELBO to encourage disentangle representations, a contrastive loss to incentivize content features from the same downstream label to be equal, and another contrastive loss to incentivize the style features from different downstream labels to be equal. The authors demonstrate empirically the efficacy of the proposed method by: qualitatively generating samples that swap/traverse the content and style variables; and quantitatively by comparing the performance of their model with another VAE model (ML-VAE).

### Strengths
- **S1** The intuition of the method is quite clear.
- **S2** The problem of finding disentangled representations (content vs. style) in latent space is of interest to the community.
- **S3** The qualitative results are quite impressive, and the quantitative ones are clear as well.
- **S4** The setup for the quantitative experiments are clearly detailed.

### Weaknesses
The manuscript has many things to improve in its current state. While I will point some of the most critical ones below, this is no an exhaustive list and I did not dive as deep in other aspects (e.g. experiments) since they would require the list below to be addressed:

- **W1.** The paper's writing contains several typographical errors (L40, L147, L201, L218, L247), incoherent/unnecessary statements (L63,L149-L151), and many unexplained terms (L63, L155, L194, Eq. 9, L215, L253, contrastive learning is given as related work but not explained, etc), and dubious examples (e.g. the one describe for the medical domain is questionable at best, since differences _directly caused_ by the sensitive attributes should **not** be removed from the predictions).
- **W2.** The maths contain many typos (Eq 1 should negate the loss, Eqs 4,5,6 are missing a closing parenthesis, Eq. 8 writes $c$ instead of $s$, etc.) and questionable statements (L184: you cannot _reasonably_ assume the posterior factorizes, as they are _dependent_ given $x$; L204: what is the norm of two comma-separated terms?; why not using the definitions in Eq. 5 and 6 in the section before?; L236: Why would having a negative value complicate the minimization?; L248: why would the model reach an equilibrium at all?; etc.). This is on top of statements that find little explanations/intuitions (e.g. L219: why would the content get mixed with the style feratures, if they are predictive of the label?)
- **W3.** The most pressing issue is the literature review (and therefore the baselines in the experiments) which is really weak and misses a lot of relevant works. To name just a few, there are a number of works on identifying content from style variables (for example, [1,2]), which has also been applied to multimodal VAEs [3]. Moreover, contrastive learning has already been applied to successfully learn multimodal representations [3,4]. All these works (which form by no means an exhaustive list) are relevant and the authors should discuss and compare with them.

---

[1] [Self-Supervised Learning with Data Augmentations Provably Isolates Content from Style](http://arxiv.org/abs/2106.04619)

[2] [Multi-View Causal Representation Learning with Partial Observability](http://arxiv.org/abs/2311.04056)

[3] [Identifiability Results for Multimodal Contrastive Learning](https://openreview.net/forum?id=U_2kuqoTcB&s=09)

[3] [Relating by Contrasting: A Data-efficient Framework for Multimodal Generative Models](http://arxiv.org/abs/2007.01179)

### Questions
- **Q1.** What is the difference in the text between a group and a class? Are they the same?
- **Q2.** What is the Jeffrey divergence?
- **Q3.** Where is the naming "anti-contrastive" coming from?
- **Q4.** Why explaining a VAE as only having Gaussian-distributed posteriors/likelihoods? I know it is the common practice, but still.
- **Q5.** How do you decide the dimensionality of the content and style variables? And why did you decide to have an autoencoder (rather than just an encoder) if only the content is relevant for the downstream task?

### Soundness
2

### Presentation
1

### Contribution
2
