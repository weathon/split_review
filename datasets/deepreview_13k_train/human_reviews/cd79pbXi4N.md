# Certified Robustness Under Bounded Levenshtein Distance

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Text classifiers suffer from small perturbations, that if chosen adversarially, can dramatically change the output of the model. Verification methods can provide robustness certificates against such adversarial perturbations, by computing a sound lower bound on the robust accuracy. Nevertheless, existing verification methods incur in prohibitive costs and cannot practically handle Levenshtein distance constraints. We propose the first method for computing the Lipschitz constant of convolutional classifiers with respect to the Levenshtein distance. We use these Lipschitz constant estimates for training 1-Lipschitz classifiers. This enables computing the certified radius of a classifier in a single forward pass. Our method, LipsLev, is able to obtain $38.80$% and $13.93$% verified accuracy at distance $1$ and $2$ respectively in the AG-News dataset, while being $4$ orders of magnitude faster than existing approaches. We believe our work can open the door to more efficient verification in the text domain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a technique to verify the robustness of a neural network for text classification tasks in a natural language processing setting (NLP).
In NLP, the Levenshtein distance is a natural way to measure the distance between two strings.
Existing verification approaches, that often rely on interval bound propagation (IBP), are however prohibitively expensive when using the Levenshtein distance to measure robustness radia.
To address this, the authors present a Lipschitz constant-based verification technique that allows to compute a certified robustness radius for convolutional models, once the Lipschitz constant of the classifier is known.
For their verification procedure, the authors consider a real-valued extension of the Levenshtein distance and a specific convolutional architecture, for which they derive robustness radius bounds that can be computed with a single forward pass.
Compared to existing IBP and brute force approaches, the proposed method is significantly faster and provides comparable clean/verified accuracy ratio for a Levenshtein distance of 1.
Remarkably, the proposed method is the only one which can provide robustness guarantees for a Levenshtein distance of 2.

### Strengths
The authors address an interesting problem in NLP, which is of great relevance given the prevalence, and related risks, of large language models.
From a wider perspective, it is important to devise techniques to provide robustness certifications which are practically computable.
The paper has thus a strong motivation.
With respect to the approach, the paper clearly presents the limitations of existing techniques and orderly discusses the proposed solution.
The paper is well structured, and it seems sound and of potential practical relevance to me.

### Weaknesses
 **Relevance of ReLU-activated convolutional networks**

While the paper is generally well motivated and an architecture similar to the one discussed has been previously investigated, I think that further details on the relevance of the method presented would be helpful.
Specifically, it is not clear how practically useful ReLU-activated, fully-connected convolutional networks are in text classification. The paper would benefit from a more thorough discussion of the limitations of the proposed method, particularly in the context of modern NLP architectures, which often employ attention mechanisms and recurrent layers, rather than simple convolutional networks. This discussion should include an analysis of how the proposed method might be extended or adapted to handle these more complex architectures, or at least a clear explanation of why such extensions are not straightforward.


**Definition of terms**

Some notions and terminology used require more explicit definition.
Firstly, Lipschitz continuity, as well as related concepts such as the "local Lipschitz constant", is never explicitly introduced. A formal definition of Lipschitz continuity, including the global and local variants, should be provided, along with an explanation of why this property is crucial for the proposed verification technique. The paper should also clarify how the Lipschitz constant is estimated or bounded for the specific network architecture used. Similarly, the notions of "clean accuracy" and "verified accuracy" are not clearly defined. As these are used as the main performance metrics, they should be properly described as well, including a precise mathematical definition of what constitutes a verified prediction within a given Levenshtein distance.



**Empirical evaluation**

Related to my previous comment, further explanations on the behaviour of the clean accuracy for networks with more than one layer is necessary.
In figure S4, the clean accuracy drops significantly as more than 2 layers are used: why is this behaviour observed? The paper should provide a more in-depth analysis of this phenomenon, possibly including a discussion of the optimization challenges associated with training deeper Lipschitz-constrained networks. It would be beneficial to investigate whether this drop in accuracy is due to vanishing gradients, or other training-related issues, and to explore potential mitigation strategies.


**Minor comments**

* line 52, of with -> with
* (several places) Related works -> related work

### Questions
* What is the relevance of methods that combine several algorithms such as alpha-beta-CROWN in your investigation? Can such approaches be adapted to the NLP setting?

* The approach you propose is sound, can you discuss completeness too?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the certified robustness of convolutional neural networks for text classification under Levenshtein distance. The major challenge of this setting compared with standard certified robustness is twofold: one is the non-fixed length of text under perturbation, and the other is the discrete nature of tokens. The authors define the concept the Lipschitzness in this setting in terms of Levenshtein distance, and derived a relxation method for compute the Lipschitzness. The approach can be readily used to train certifiably robust models. Results show that the method is efficient and can achieve a performance on par with previous IBP-based certification and extend to larger perturbation scenarios.

### Strengths
1. The problem is significant and challenging. The original problem of certified robustness typically focuses on continuous, fixed-demension inputs, which is different from real-world NLP setting. The authors instead considered Levenshtein distance, which is a reasonable metric.
2. The proposed solution is interesting, efficient, and simple. This is a major advantage of this paper compared with prior approaches.
3. The writing is quite clear and readable. I enjoy reading this paper a lot.

### Weaknesses
1. One major problem is the Lipschitzness constraint is so strong and perhaps harms the expressive power of resulting model, thus hampering the clean accuracy. In the standard certified robustness community in CV, constraining the Lipschitz constant does not show performance comparable to IBP. This problem is also theoretically studied in [Zhang et al. 2022]. Do you think your models in experiment suffers from this problem in clean accuracy compared with other approaches in small perturbation scenario?

Reference: [Zhang et al. 2022] Rethinking lipschitz neural networks and certified robustness: A boolean function perspective.

2. Regarding the experimental results, the performance where Levenshtein distance is 1 does not show the advantage of the proposed method. Although the training and verification is quite efficient, the performance on SST-2 and IMDB is not comparable with the simplest IBP.

### Questions
1. Why on FakeNews dataset LipsLev has exactly the same performance as IBP when the Levenshtein distance is 1?

Miscellaneous:
1. Line 108: $s_i$ should be $S_i$?
2. Line 240: $\mathbb R^{m+(q-1)\times d}$ should be $\mathbb R^{m+2(q-1)\times d}$?

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
3

### Summary
This work presents a convolutional text classifier which is certifiably robust to Levenshtein-distance perturbations.

### Strengths
Overall, this work is a solid academic contribution, albeit with limited prospects for scalability.

1. I like that this approach provides closed-form, deterministic certificates. It is the first paper that I have seen tackling the challenging Levenstein-distance setting without resorting to randomized approaches.
2. The paper writing is clean and structurally sensible. The problem setting is well-motivated and the necessary prior work is precisely and clearly introduced.
3. Figure and table presentation is thoughtful -- I appreciate the coordinated highlighting between Table 2 and Table 3.
4. Method runtime is orders of magnitude faster than baselines; this is expected as the Lipschitzness constant is enforced by construction.
5. The theory is carefully presented and a quick scan of the proof strategy in appendix B makes sense, although I haven't checked the proofs in detail.

### Weaknesses
1. My main concern with this approach is that a) the certified edit distances are very small (one or two characters), b) the models are tiny (only one convolutional layer), and c) I think possibility for future improvement is minimal. Layer-level Lipschitz constants have been more or less discarded by the image classification robustness community for several years now, as exponential signal attenuation makes it difficult to construct verifiable deep networks. This problem setting is arguably much more difficult, and since layer-wise Lipschitz approaches have proven intractable for images, I don't expect that this approach will be scalable to any reasonable network size. The core issue is that bounding the Lipschitz constant of each layer independently leads to a rapidly diminishing robustness radius as the network depth increases. This is because the overall Lipschitz constant is the product of the individual layer constants, and even with constants close to 1, the product quickly becomes very small, severely limiting the achievable robustness guarantees. This is especially problematic for text, where small perturbations can lead to large semantic changes.
2. Section 6 discusses extensions to transformers, which is too far removed from what is presented in the paper. I understand the author's desire to connect their approach with SOTA language models, but a one-layer convolutional classifier is nowhere close to the complexity of a transformer. The leap from a single convolutional layer to the complex architecture of a transformer is substantial, and the challenges in extending the proposed approach to transformers are not adequately addressed. The discussion feels speculative without concrete evidence or a clear path forward.
3. The literature review should be a little more comprehensive, and do a better job of grouping related works. For example, a quick google search for "certifiable robustness text classifier" yields [1], which is certainly related work. The current literature review lacks a thorough analysis of existing methods for certifiable robustness in text classification, and fails to adequately contextualize the proposed approach within the broader landscape of related research. A more detailed discussion of the strengths and weaknesses of existing methods would be beneficial.
4. The authors don't evaluate against randomized methods. While I understand that deterministic methods are a more apples-to-apples comparison, some readers might appreciate fully comprehensive baselines (perhaps in the appendix). The absence of comparisons with randomized methods leaves a gap in the evaluation, as these methods represent a significant portion of the existing work in robustness verification. Including such comparisons, even if they are not the primary focus, would provide a more complete picture of the proposed method's performance relative to the state-of-the-art.

### Questions
1. To confirm: Theorem 4.3 holds for any choice of $p$ and $r$ which satisfy $1/p + 1/r = 1$?
2. A suggestion for Figure 1: I think this would be better presented a line graph with the y axis as "percent of sentences verified." That's what you're actually trying to communicate: that as the sentence length goes up, a high fraction are verified. Right now, readers have to mentally "divide the columns" to  back out what you're trying to say. Another alternative is a stacked bar chart based on proportions, e.g. something like [this](https://community.tableau.com/sfc/servlet.shepherd/version/renditionDownload?rendition=THUMB720BY480&versionId=0684T000002JELx&operationContext=CHATTER&contentId=05T4T000008xZ3u&page=0).
3. Have the authors empirically verified their certificates by running inference on random string modifications within the Levenstein distance of the certificate? Just to check that there's no mistake in the proofs that is slipping through.
4. Related to the previous point, I'd be curious to see the gap between the empirical and theoretical certificates, perhaps adapting a greedy coordinate-wise attacking strategy as in [1]. But I understand that this is orthogonal to the certified robustness focus of the paper, so this is just a suggestion to the authors if they are independently compelled to investigate.

Minor notes:
1. "English" on line 92 should be capitalized.
2. In Definition 4.1, it seems that the notation of $d_{ERP}$ should also be dependent on $p$? I.e. $d_{ERP}^p(A,B)$.

[1] Zou, Andy, et al. "Universal and transferable adversarial attacks on aligned language models." arXiv preprint arXiv:2307.15043 (2023).

### Soundness
4

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
This paper derives the Lipschitz constant of convolutional networks with respect to the Levenschtein distance on its textual inputs. As a result, certified radii (in the Levenschtein distance) for robustness are provided. It is shown how to use the derived Lipschitz bound in order to train a 1-Lipschitz model (with respect to the Levenschtein distance). Furthermore, experiments are conducted to validate the effectiveness of the proposed robustness certificates.

### Strengths
The topic is certainly of interest to the ICLR community. The mathematical derivations appear correct. The proposed ideas are novel and well-motivated.

### Weaknesses
I have concerns regarding the presentation and performance limitations of the proposed method. See my Questions below for more details.

1. Line 161: How is $d_\text{edit}$ defined? It would be good to explicitly define this for readers that are from outside the NLP community. It would also be good to clarify exactly what the embedding matrix $\mathbf{E}$ is.
2. Line 163: In the introduction, you said that you would denote the elements of a matrix by $x_{ij}$ (no comma in the subscript). However, you're now using commas in the subscripts (e.g., $z_{i,j}$ and $e_{k,i}$). It would be good to fix things to use consistent notation throughout the paper.
3. Line 173: "tenths". It looks like you probably meant "tens of thousands."
4. In Section 4.1, you are concerned with local Lipschitz constants, but then in Section 4.2 you begin to discuss global Lipschitz continuity. Why the discrepancy?
5. Line 253: The footnote 1 should be put after the punctuation. Otherwise, as it is now, it looks like it is part of the mathematical expression (i.e., it looks like "one to the power of one").
6. Remark 4.5: Could you explain how this is a local Lipschitz constant? This seems like a global bound if it indeed holds for all $\mathbf{P}$ and $\mathbf{Q}$.
7. Table 2 makes your method look quite loose, with IBP and BruteF attaining higher verified accuracies than yours in most of the $k=1$ settings. I understand that the other methods are more computationally expensive/are not applicable to $k=2$, but the results being displayed here are not very convincing.
8. "Our method, LipsLev, is able to provide the best performance in AG-News" Isn't BruteF providing the best performance for AG-News?

### Questions
1. Line 161: How is $d_\text{edit}$ defined? It would be good to explicitly define this for readers that are from outside the NLP community. It would also be good to clarify exactly what the embedding matrix $\mathbf{E}$ is.
2. Line 163: In the introduction, you said that you would denote the elements of a matrix by $x_{ij}$ (no comma in the subscript). However, you're now using commas in the subscripts (e.g., $z_{i,j}$ and $e_{k,i}$). It would be good to fix things to use consistent notation throughout the paper.
3. Line 173: "tenths". It looks like you probably meant "tens of thousands."
4. In Section 4.1, you are concerned with local Lipschitz constants, but then in Section 4.2 you begin to discuss global Lipschitz continuity. Why the discrepancy?
5. Line 253: The footnote 1 should be put after the punctuation. Otherwise, as it is now, it looks like it is part of the mathematical expression (i.e., it looks like "one to the power of one").
6. Remark 4.5: Could you explain how this is a local Lipschitz constant? This seems like a global bound if it indeed holds for all $\mathbf{P}$ and $\mathbf{Q}$.
7. Table 2 makes your method look quite loose, with IBP and BruteF attaining higher verified accuracies than yours in most of the $k=1$ settings. I understand that the other methods are more computationally expensive/are not applicable to $k=2$, but the results being displayed here are not very convincing.
8. "Our method, LipsLev, is able to provide the best performance in AG-News" Isn't BruteF providing the best performance for AG-News?

### Soundness
3

### Presentation
2

### Contribution
2
