# A Theory of Unimodal Bias in Multimodal Learning

- Decision: Reject
- Scores: 8, 5, 5, 3

## Abstract
Using multiple input streams simultaneously in training multimodal neural networks is intuitively advantageous, but practically challenging. A key challenge is unimodal bias, where a network overly relies on one modality and ignores others during joint training. While unimodal bias is well-documented empirically, our theoretical understanding of how architecture and data statistics influence this bias remains incomplete. Here we develop a theory of unimodal bias with deep multimodal linear networks. We calculate the duration of the unimodal phase in learning, as a function of the depth at which modalities are fused within the network, dataset statistics, and initialization. We find that the deeper the layer at which fusion occurs, the longer the unimodal phase. In addition, our theory reveals the modality learned first is not necessarily the modality that contributes more to the output. Our results, derived for multimodal linear networks, extend to ReLU networks in certain settings. Taken together, this work illuminates pathologies of multimodal learning under joint training, showing that late and intermediate fusion architectures can give rise to long unimodal phases and even prioritize learning a less helpful modality.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies how deep linear networks with multiple pathways learn from data to produce a scalar output  when starting from small weights. The paper studies how the learning dynamics depend on layer in the network architechture when the modalities is fused in an additive manner, and find that with early fusion both modalities are learned (approx) simultaenously, whereas with late fusion the modality more correlated with the output is learned earlier in training.

### Strengths
The paper is well-written, the figures are clear, and the mathematical results appear to be sound. I did not carefully check the derivation of the time ratios for learning from the different modalities in the Appendix.

### Weaknesses
The motivating phenomonom (unimodal bias) that one modality dominates at convergence is not addressed in the deep linear multimodal settings, as the manuscript studies the transient dynamics for when these modalities get learned (which the authors directly acknowledge in the intro). While the motivating phenomenon is well motivated, developing an improved understanding of the transient dynamics was not well-motivated. It would be helpful if the manuscript could comment/discuss how the analysis of the transient in the deep linear network setting could inform the phenomemon of unimodal bias at convergence in practice. I also feel that the paper title could better reflect the contents of the paper.

Do the results extend to the multitask case where output y is a vector?

The authors considered architectures of equivalent depth between pathways. How do the result change if these depths differ?

How do the weights evolve in the pre and post fusion layers?

When the paper says: "In essence, an early fusion point allows the weaker modality to benefit from the stronger modality's learning in the post-fusion layers:" Are there settings where this can be harmful as well, or would the larger scale of the weights always help learning?

Minor: 

What matrix norm is being used throughout the paper? It should be clarified (For example in Eq 7, Eq 9 etc). Apologies if I missed it.
Do the results apply to more complicated covariance matrices? It seems like diagonal input covarainces were studied, and 2x2 matrices.

Define the product notation used for a product over weight matrices (for example in Eq 2)

It was unclear the experimental details used. For example, were there a finite amount of inputs used, or were inputs drawn according to the covariance structure every batch (In Fig 2,3; for example). The paper mentioned full-batch SGD but the details were not provided (and could not find in appendix.)

In sect. 3.2.3 unclear why it is ideal for modality learned first to lead to larger decrease in loss.

Wording " a smaller initialization scale exacerbates the impediment to learning modality A compared to modality
B, yielding a larger time ratio" is unclear.

It was a bit strange to add in new results in the discussion section.

Why do the results require a small initialization?

### Questions
The authors considered architectures of equivalent depth between pathways. How do the result change if these depths differ? 

How do the weights evolve in the pre and post fusion layers?

When the paper says: "In essence, an early fusion point allows the weaker modality to benefit from the stronger modality's learning in the post-fusion layers:" Are there settings where this can be harmful as well, or would the larger scale of the weights always help learning?

Minor: 

What matrix norm is being used throughout the paper? It should be clarified (For example in Eq 7, Eq 9 etc). Apologies if I missed it.
Do the results apply to more complicated covariance matrices? It seems like diagonal input covarainces were studied, and 2x2 matrices.

Define the product notation used for a product over weight matrices (for example in Eq 2)

It was unclear the experimental details used. For example, were there a finite amount of inputs used, or were inputs drawn according to the covariance structure every batch (In Fig 2,3; for example). The paper mentioned full-batch SGD but the details were not provided (and could not find in appendix.)

In sect. 3.2.3 unclear why it is ideal for modality learned first to lead to larger decrease in loss.

Wording " a smaller initialization scale exacerbates the impediment to learning modality A compared to modality
B, yielding a larger time ratio" is unclear.

It was a bit strange to add in new results in the discussion section.

Why do the results require a small initialization?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on a theoretical understanding of unimodal bia and  examines the effect of network architecture, dataset characteristics, and initialization factors. It reveals that while early fusion networks do not exhibit unimodal bias, this bias is noticeable in networks with intermediate and late fusion. Additionally, the paper quantifies the duration of the unimodal phase in these settings. To support these findings, the paper presents experimental data using numerical simulations conducted on two-layer ReLU networks and deep linear networks.

### Strengths
- The paper tackles an important problem of unimodal bias by investigating the unimodal bias theoretically and understanding the impact of various components such as network configuration, dataset statistics and initialization, which would be of interest to the community.
- The paper was clear and well-written.
- The supporting experimental evidence provides interesting insights into intermediate and late fusion for multimodal learning.

### Weaknesses
 - The paper presents an interesting study of unimodal bias in intermediate and late fusion contexts, yet the evidence supporting the absence of unimodal bias in early fusion remains unconvincing. The reliance on the Frobenius norm of weights as a metric for understanding unimodal bias seems reasonable, but the experiments regarding early fusion are limited to simplistic scenarios. These toy settings, specifically the use of linearly separable data, are insufficient to assert the absence of unimodal bias in early fusion. The experiments do not explore the full range of potential interactions between modalities in early fusion, particularly in cases where the modalities might compete or interfere with each other.
- All experiments are conducted with linearly separable data. The inclusion of experiments with XOR data, where early fusion fails to perform effectively, further casts doubt on the claims for early fusion. Considering that the main focus of the paper was to investigate the interplay between unimodal bias, network configuration, and dataset statistics, the scope and depth of the study become critical. When this research is contrasted with prior studies that have identified unimodal bias across a diverse range of datasets, the robustness of the current findings for complex, real-world scenarios appears uncertain. The study does not adequately address the potential for unimodal bias to manifest in more complex, non-linear early fusion architectures, which limits the generalizability of the conclusions.

- Minor suggestions
   - In equation 2, did you intend to use W^{tot} alongside y?.
   - The latter part of the caption for figure 2, particularly the description following parts a-c, is somewhat confusing and could benefit from a more straightforward explanation.

### Questions
Apart from the review, I have some additional questions:
- Can the authors provide more details with respect to Fig 3e) 
- “Two-layer early fusion ReLU networks do not learn XOR features and can even fail to learn this task” – can the authors comment and provide more reasoning about this observation wirth respect to the XoR experiment?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper theoretically study the unimodal bias in deep multimodal linear networks. They also derived the duration of the unimodal phase in terms of network configuration, and dataset statistics. The theoretical findings are supported by numerical simulations.

### Strengths
1. The paper is clear and well-written 
2. The results for early fusion and intermediate fusion are novel
3.  This paper explicitly characterizes an analytical relationship between unimodal bias, network configuration, and dataset statistics under simplified linear settings, and the implication from theory, fast-to-learn modality, is interesting.
4.  The results are validated by numerical simulations.

### Weaknesses
1. The author claims "there is a scarce theoretical understanding of how unimodal bias arises and how it is affected by the network configuration, dataset statistics, and initialization". However,  the work [1] mentioned in this paper already theoretically explored the rise of unimodal bias in a more realistic neural network setting, and their results somewhat reveal the relationship between the inferior performance of late-fusion networks with initialization and modality correlations. 

2. Moreover, there is another work [2] that has provided some analysis about insufficient learning of uni-modal features and proposed some methods to overcome the limitations of late-fusion networks.  In their study, they also discuss the effect of easy-to-learn features.

Therefore, the novelty and contribution of this paper compared to the previous analysis is not clear to me, considering they studied more complex and realistic settings.

3. The theoretical analysis is limited by the assumption of linear networks, which is a significant simplification compared to the non-linear activation functions commonly used in deep learning. This raises concerns about the applicability of the theoretical findings to real-world scenarios where non-linearities play a crucial role in feature learning and representation. The insights gained from linear networks may not fully capture the complex dynamics of unimodal bias in non-linear deep multimodal networks.

4. The frequent use of the approximation symbol ($\approx$) in the appendix when deriving mean results raises questions about the rigor and precision of the theoretical justifications provided. The lack of explicit error bounds or analysis of the approximation's impact on the final results makes it difficult to assess the validity and reliability of the theoretical claims. It is crucial to understand the magnitude of the approximation errors and their potential influence on the derived relationships between unimodal bias, network configuration, and dataset statistics.

### Questions
See weakness.

1. For the data generation process,  it appears that only the correlation matrices are required. Are there specific assumptions made regarding $y$ that need to be clarified?
2. The author claims "we develop a theory of unimodal bias with deep multimodal linear networks." However, the frequent use of the approximation symbol ($\approx$) in the appendix when deriving mean results raises questions about the rigor and precision of the theoretical justifications provided.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work initiates a theoretical study on the unimodal bias in multimodal learning, by analyzing the training dynamics. In particular, for linear networks, factors including a deeper fusion layer, stronger correlations between modalities and disparities in input-output correlations are identified as the causes of the unimodal bias.

### Strengths
The problem of building up a theoretical understanding of multimodal learning is urgent and significant.

Analyzing the training dynamic is an interesting and promising avenue for understanding unimodal bias. Such direction is intuitive due to relevant works on the implicit bias of neural networks, particularly on the training dynamics after zero training loss.

### Weaknesses
 **Unfocused writing:** the writing of this work is unfocused. From the title and the contents, I presume this work is theoretical paper. However, there is no formal presentation of the theoretical results (propositions/lemmas/theorems). It greatly obstructs a smooth understanding of the results for readers. After I read the main-text, I still can't tell which part is prioritized. There should be rigorous summaries of the theoretical results. Even a heuristic-level summary can be useful.

**Restricted results:** the dynamic analysis only concerns linear networks, which is not popular in practice. Tools from the study of implicit bias of neural networks (for example, [1]) might be useful to deal with nonlinear networks.

### Questions
Though the contents might be interesting, the current writing style is certainly non-standard and disadvantageous to readability. In my opinion, the work needs a thorough rewriting for a clear summary and presentation of the theoretical results.

Still, I'm curious the reason of the current writing. There seems to be plenty rigorous mathematical arguments in the appendix. Is there any difficulty preventing you from summarizing them as theorems?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
