# Expressivity of ReLU-Networks under Convex Relaxations

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
\vspace{-2mm}
Convex relaxations are a key component of training and certifying provably safe neural networks. However, despite substantial progress, a wide and poorly understood accuracy gap to standard networks remains, raising the question of whether this is due to fundamental limitations of convex relaxations. Initial work investigating this question focused on the simple and widely used IBP relaxation. It revealed that some univariate, convex, continuous piecewise linear (CPWL) functions cannot be encoded by any ReLU network such that its IBP-analysis is precise.
To explore whether this limitation is shared by more advanced convex relaxations, we conduct the first in-depth study on the expressive power of ReLU networks across all commonly used convex relaxations. We show that: (i) more advanced relaxations allow a larger class of \emph{univariate} functions to be expressed as precisely analyzable ReLU networks, (ii) more precise relaxations can allow exponentially larger solution spaces of ReLU networks encoding the same functions, and (iii) even using the most precise single-neuron relaxations, it is impossible to construct precisely analyzable ReLU networks that express \emph{multivariate}, convex, monotone CPWL functions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors presented an analysis for special classes of convex relaxations of neural networks and their expressivity. Unfortunately, given that I am not an expert with the subject, and that the background in the paper is limited, I have trouble understanding the high level ideas of the paper. I would encourage the authors to engage with discussion, so that I can provide a proper review of this work.

### Strengths
I will re-evaluate the strengths after a discussion with the authors to understand the paper.

### Weaknesses
### weaknesses:

Similar to strengths, I will re-evaluate after discussion.

### questions:

As mentioned earlier, I have many basic questions about this work. Perhaps let me start from the basics about the background of this work.

1. Can the authors elaborate on how convex relaxations are helping with formal robustness guarantees? This was quickly glossed over, but I would hope to get a better explanation.

2. Can the authors explain exactly what is being relaxed into a convex function? Section 2.1 reads quite confusingly for me, as all I can discern are inequalities, and I do not see which parts are being relaxed.

3. When the authors write a vector is less than or equal to another vector, is this inequality entrywise?

4. There are a lot of definitions in section 2.2, can the authors provide a simpler explanation of these definitions and what they are trying to capture? In particular, why is it that we care about $D$-analysis in the definition of expressivity? I would have expected expressivity of a network architecture to be about function approximation.

5. At the end, it seems like the authors are investigating whether or not ReLU networks can express certain functions. I thought this was already an answered question with respect to universal approximation, but perhaps I am missing something. Can the authors explain why we need to analyze the expressivity results for these certain class of functions?

### Questions
As mentioned earlier, I have many basic questions about this work. Perhaps let me start from the basics about the background of this work. 

1. Can the authors elaborate on how convex relaxations are helping with formal robustness guarantees? This was quickly glossed over, but I would hope to get a better explanation. 

2. Can the authors explain exactly what is being relaxed into a convex function? Section 2.1 reads quite confusingly for me, as all I can discern are inequalities, and I do not see which parts are being relaxed. 

3. When the authors write a vector is less than or equal to another vector, is this inequality entrywise? 

4. There are a lot of definitions in section 2.2, can the authors provide a simpler explanation of these definitions and what they are trying to capture? In particular, why is it that we care about $D$-analysis in the definition of expressivity? I would have expected expressivity of a network architecture to be about function approximation. 

5. At the end, it seems like the authors are investigating whether or not ReLU networks can express certain functions. I thought this was already an answered question with respect to universal approximation, but perhaps I am missing something. Can the authors explain why we need to analyze the expressivity results for these certain class of functions? 

Perhaps let's start here. Once we go into discussion and have a better understanding, I can follow up with more questions regarding the actual technical contributions of this work.

### Soundness
2 fair

### Presentation
1 poor

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
This paper studies the expressive power of ReLU neural networks under different convex relaxations that are commonly used for neural network certification. The key findings are:

* For univariate functions, more precise convex relaxations like Δ and DeepPoly allow expressing larger classes of continuous piecewise linear (CPWL) functions precisely compared to the simple interval bound propagation (IBP).
* IBP can precisely express monotone CPWL functions, while Δ and DeepPoly can also express convex CPWL functions.
* Multi-neuron relaxations allow single-layer networks to express all univariate CPWL functions precisely.
* For multivariate functions, even the most precise single-neuron relaxation (Δ) cannot precisely express simple classes like multivariate monotone convex CPWL functions.
* This suggests single-neuron convex relaxations are fundamentally limited for multivariate functions, highlighting the need for more precise analysis methods like multi-neuron relaxations.
* The results have implications for certified training, suggesting more precise relaxations could yield larger effective hypothesis spaces and higher performance if optimization challenges can be overcome.

In summary, the paper provides an in-depth analysis of the expressive power of ReLU networks under different convex relaxations, showing more precise relaxations increase expressivity for univariate functions but are still fundamentally limited for multivariate functions. The results motivate developing more advanced analysis techniques and studying their potential benefits for certified training.

### Strengths
Here are some strengths of this paper:

* It provides the first in-depth, systematic study on the expressive power of ReLU networks under a wide range of convex relaxations commonly used in neural network certification.
* The analysis covers univariate and multivariate functions and simple as well as more complex function classes like (monotone) convex CPWL.
* It clearly differentiates the capabilities of different relaxations through precise mathematical results and constructive proofs.
* The paper relates the theoretical results back to certified training, drawing interesting hypotheses about the potential benefits of more advanced relaxations.
* The paper is clearly structured and provides detailed mathematical proofs for all results.

### Weaknesses
Some potential weaknesses of this paper:

* The focus is exclusively on ReLU networks, not covering other activation functions commonly used like sigmoid or tanh. This limits the scope of the analysis, as different activation functions may exhibit different expressive power under convex relaxations. For example, the saturation properties of sigmoids and tanh could lead to different behaviors in terms of the tightness of relaxations.
* Only fully-connected feedforward networks are considered, not convolutional or residual architectures widely used in practice. This is a significant limitation as the structure of convolutional and residual networks is known to affect their expressivity and robustness properties. The analysis should be extended to these architectures to assess the generalizability of the results.
* The analysis is limited to deterministic networks, not touching on stochastic networks. The behavior of stochastic networks under convex relaxations is not well understood, and this is a relevant direction for future work, especially considering the increasing interest in Bayesian neural networks and other probabilistic models.
* Only standardized datasets and perturbation sets are studied; results may not generalize to other domains. While the paper focuses on theoretical analysis, the practical implications of the results should be evaluated on a wider range of datasets and perturbation sets. The current analysis is limited to common $\ell_p$-norm bounded perturbations, but the results could be different for other types of perturbations.
* While hypotheses are provided for certified training, no experiments are conducted to validate the conjectured benefits. The lack of empirical validation is a significant weakness, as the theoretical results may not translate directly into practical improvements in certified training. Experiments are needed to determine if the theoretical benefits of more precise relaxations can be realized in practice.
* The writing is quite dense and mathematical, which could make it less accessible to a general AI audience. The paper could benefit from more intuitive explanations and examples to make the results more accessible to a broader audience.
* Aside from certified training, implications for other applications of neural network analysis are not discussed much. The paper could explore other potential applications of the results, such as neural network compression, pruning, or interpretability.

### Questions
Here are my questions:

* There is recent literature on the convex optimization of ReLU network, e.g., [1] and several other follow-up papers by the same authors extending this work to various neural network architectures. Can authors comment on their contributions over this work and explain how their paper supports/refutes the claim there? For example, the very first question to comment on would be: What is the point of having convex relaxations if the ReLU networks can already be trained using convex optimization?

* Can authors also briefly comment on the issues raised in the weaknesses part?

[1] Pilanci and Ergen, Neural Networks are Convex Regularizers: Exact Polynomial-time Convex Optimization Formulations for Two-layer Networks, ICML 2020

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the expressive power of ReLU neural networks under various convex relaxations, by measuring their ability to represent (certain subclass of) CPWL functions. On the positive side, for univariate CPWL functions, most convex relaxation methods are shown to be able to express monotone or convex CPWL functions, and Multi-Neuron can even represent all CPWL functions. However, it's shown that all these methods fail in the multivariate case: they can't even represent the simple $\max$ function in $\mathbb{R}^2$.

### Strengths
**Novel direction:** the expressive power of neural networks is an interesting and important topic. This work is the first to consider such expressive power in the precise representation setting.

**Wide coverage:** in the univariate setting, this work discusses a broad range of convex relaxation methods, which covers most popular ones in practice.

### Weaknesses
 **Univariate is restricted:** the main weakness I found is the restricted univariate assumption. All the positive results for the expressive power of convex relaxation methods hold for univariate functions, which is restricted in two ways: (1) in practice, almost all functions of interest are multivariate (2) in theory, the case of univariate functions is too special, which often times avoids the general difficulty in high dimensions and thereby hard to generalize. 

On the other hand, the negative multivariate result only holds for $\triangle$, and the precision gap can be arbitrarily small. It's not clear whether multivariate methods can express multivariate CPWL functions precisely.

### Questions
**Motivation for precise analysis:** it's mentioned in this work if we allow approximate analysis, for any approximation error $\epsilon>0$ and general multivariate continuous function on $\mathbb{R}^n$, IBP can express the function up to $\epsilon$ error (Baader et al 20). This seems a strong enough guarantee. What's the significance of considering precise analysis beyond pure theoretical interest?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
