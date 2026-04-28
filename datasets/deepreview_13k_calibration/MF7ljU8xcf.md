# Larger Language Models Provably Generalize Better

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 8, 6, 6

## Abstract
Why do larger language models generalize better? To explore this question, we develop generalization bounds on the pretraining objective of large language models (LLMs) in the compute-optimal regime, as described by the Chinchilla scaling laws. We introduce a novel, fully empirical Freedman-type martingale concentration inequality that tightens existing bounds by accounting for the variance of the loss function. The generalization bound can be broken into three contributions: the number of parameters per token, the loss variance, and the quantization error at a fixed bitrate. As language models are scaled up, the number of parameters per data point stays constant; however, both the loss variance and the quantization error decrease, implying that larger models should have \emph{smaller} generalization gaps. We examine why larger models tend to be more quantizable from an information theoretic perspective, showing that the rate at which they can integrate new information grows slower than their capacity on the compute optimal frontier. From these findings we produce a scaling law for the generalization gap, showing that our bounds decrease in a predictable way.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates why LLMs generalise better, using new theoretical bounds that quantify generalization in LLMs. Authors introduce an empirical Freedman-type martingale concentration inequality refining generalization sounds by considering the variance in the loss function, and influenced by 1) The parameters per token 2) The loss variance and 3) The quantisation error. They show that generalization gap decreases predictably as LLMs scale up. The bounds are empirically tested using Pythia model checkpoints on the Pile dataset, illustrating how loss variance and quantisation error decrease with scale. Last, they argue from an information theory perspective that information content in a model grows sublinearly with scale, allowing models to generalize better with fewer bits per parameters, hence improving quantizability.

### Strengths
The paper stands out for its ambition in taking down a complex question with originality, and its potential to inform future model scaling and generalisation research in LLMs. The use of a Freedman-type martingale concentration inequality, which incorporates the empirical variance of the loss function is both creative and original. The focus on optimal scaling through the chinchilla law, along with a brand new perspective (to my knowledge) on quantizability and information transfer, showcase originality. The authors well motivate the use of Freedman inequality by the need for higher bounds. The choice to base the empirical evaluation on the Pythia model also provides a reasonable foundation to explore the theoretical claims.

### Weaknesses
While the paper makes an ambitious attempt to understand generalization in LLMs, there are a few core weaknesses. The theoretical assumptions and methods could benefit from further grounding and justification. The empirical Freedman inequality and the notion of loss variance lack through derivation and validation across different settings, which may leave doubts about the generality of these bounds for LLMs in diverse applications. The empirical results, are limited to the single Pythia model architecture, constraining the scope of the findings (Paper would benefit expanding the evaluation to other widely-used LLMs eg. GPT, T5, BERT…). Moreover, some sections are overly technical without sufficient motivation, making presentation difficult to follow, especially for the proposed quantisation bound and its integration with the chinchilla scaling laws. Some of the notation is dense, and (if) introduced with minimal intuition. Examples:

— $\Sigma$: The term “loss variance” that is central is introduced without a clear mathematical definition or discussion. A clarification whether this variance refers to the empirical variance of the loss function over tokens or across model params would make it more understandable.
— $C$ The complexity term is introduced with very limited intuition and authors do not explain how this is derived, or what aspects of model size, dataset, or quantisation contribute to it.

### Questions
— Have you empirically tested the argument on quantizability from the Hessian spectrum and QuIP framework beyond GPTQ? 
— The information-theoretic argument using prequential coding is interesting but could benefit from further empirical support. Have you tested the information content predictions under varied trading or scaling setups? For instance, would be nice to understand how your complexity term $L(h)/D$ changes for models trained on different datasets or architectures
— Are there any specific factors that you believe yolk affect the generalization bound accuracy? Eg. Dataset size, architecture choice

### Soundness
2

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
2

### Summary
This paper explains the high generalization performance of large language models (LLMs) by introducing a new Freedman-type concentration inequality and constructing a generalization bound based on the Chinchilla scaling law. The generalization bound is decomposed into three factors: the number of parameters in the model, the token-wise loss variance, and the performance gap associated with quantization. This bound quantitatively shows how the generalization gap reduces as the size of the LLM scales. In particular, it shows that the amount of information grows sublinearly with the LLM size, indicating that the resources required for the model to efficiently integrate information are reduced. This finding provides an information-theoretic explanation for why LLMs can improve generalization ability with computationally optimal scaling and point out a new relationship between the model size and information.

### Strengths
The authors' approach to explaining LLM performance improvements by breaking down the generalization bound into three key components is particularly valuable. Furthermore, introducing a new inequality based on martingale concentration enables analysis specific to LLMs, where data is non-independent and identically distributed. It opens up a new path to theoretical understanding of generalization performance. This is a significant contribution to LLM research.

### Weaknesses
This paper contributes to the theoretical understanding of LLMs and confirms their validity using real LLM data. However, further verification is needed for practical applications. In particular, the merits of decomposing the generalization bound are unclear from the demonstrations in Fig.2(right) and Fig.3(center), for example. The specific scaling behavior of each term in the decomposition, and how they interact to produce the overall generalization performance, is not sufficiently clear from the presented figures. It is not obvious how the individual components of the bound contribute to the overall generalization performance, and the figures do not provide a clear visual explanation of this relationship. The analysis could benefit from a more detailed breakdown of how each term in the bound scales with model size and data, and how these scaling behaviors combine to produce the observed generalization performance.

### Questions
* As shown in Eq.(6), for example, it is explained that $K(h)$ is scaled by $\tilde{O}(D^{1-\beta})$, with this exponent $\beta$ coming from the Chinchilla scaling law. If this exponent $\beta$ can take a non-trivial value, is it possible to constrain its value using the authors' theory?

* The implications of the theoretical results are discussed in Sec.5.3, but I'm not entirely sure I understand the argument. I assume the authors focus on Pythia due to the availability of models with various parameter sizes; however, investigating other language models in the same way may be difficult. Given these limitations, how do the authors envision extending this type of analysis? Could they elaborate on potential insights or outcomes if similar analyses were feasible for other models?

* Minors
* The citation to the appendix on line 186 should be "Appendix" rather than "Section." There are several similar cases.
* Please check the ICLR format for citing equations.

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
This work provides a novel generalization bound for LLMs consisting of three components depending on the ratio of the number of parameters to tokens, loss variance, the performance gap from model quantization. The paper first provides a new martingale concentration inequality that can be evaluated empirically. The rest of the components of the bound come from loss variation, a smoothing constant, and quantization gap, all of which can be computed empirically. Experiments show that the obtained bounds are very close to evaluated loss functions in LLMs. The paper also provides an alternate bound based on information accumulation in LLMs using prequential coding, which is a less empirical bound. Nevertheless, gives insight on model complexity with changing model scale while keeping the ratio of dataset to parameters constant. Overall, the paper provides novel generalization bounds for LLMs with interesting insights to the working of LLMs and how they vary with scale.

### Strengths
- The paper presents two interesting generalization bounds for LLMs, one of them can be empirically calculated and shows results close to actual loss obtained in experiments. The other bounds gives insight on generalization bounds in LLMs with increase in model size with constant data to parameters ratio.
- For computing the first bound, the model derives a new concentration inequality based on the Freedman’s inequality that can be empirically computed and is likely to be of interest in future works.
- The empirical evidence provided in the paper showing that it is close to the obtained bounds in interesting.

### Weaknesses
 - It would be good to improve the readability of the paper a bit by distilling down the mathematics and giving an intuition for both the bounds in summary.
- It would be better to provide the empirical evidence after both the bounds instead of providing it in between. E.g., some plots are provided in Sec. 5, whereas the empirical evidence is given in Sec. 4.


### Questions
- A general question: Are the empirical bounds extendable to LLM performance with inference-compute scaling?, e.g. in [1]

[1] Sardana, Nikhil, et al. "Beyond chinchilla-optimal: Accounting for inference in language model scaling laws." arXiv preprint arXiv:2401.00448 (2023).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a new upper bound on the single-token generalisation error of language models. Evaluations of this bound are compared with selected empirical data from the training history of a language model.


EDIT: I have raised the score, on the understanding that the authors will amend the title as discussed and significantly clarify the exposition of the theorems, including to clearly state that the 'with probability 1- \delta' refers to the sampling of both the X_k and Y_k.

### Strengths
The authors' main result is interesting: an apparently novel generalisation bound which can be evaluated from data. The comparisons they make between their bound and empirical data is also of interest. Hopefully this bound will be useful in future for more efficiently guiding the development of AI models

### Weaknesses
 1. I am left wondering whether this is really an appropriate venue for this work. Proving the results stated in the actual paper requires 10 pages of dense technical appendices introducing a wealth of additional lemmas, theorems and corollaries which are not reviewable in the timeframe. The results themselves do not appear to be standard, and I feel would benefit from a proper presentation in a format, such as a journal, which gives sufficient space for a detailed investigation of the technical details.
2. The statement of several of the main results do not appear to be complete, and require extra clarification. In particular, the authors should take care to ensure that all notation is defined.
    - Does the 'with probability $1 - \delta$' in Theorems 3.1, 3.2, and 3.4 refer to the sampling of $X_k$, $Y_k$, or both? If both, the authors should clarify how their results on the *joint* probability of $X_k$ and the fictitious random variable $Y_k$ can be connected to standard generalisation bounds which look at the probability with respect to $X_k$. The random variables over which probabilities are being measured should be explicitly stated in all results.
    - The random variables $Y_k$ implicitly appear in the result of Theorem 3.4 (through $\Sigma$), but are not defined in the statement of the theorem.
    - In Theorem 3.1, what is $\mathcal{F}_k$? I expect this is some form of filtration, but it is undefined.
    - In Theorem 3.1, ${X_{k}}$ are ${\mathcal{F}{k}}$-measurable, while $Y_k$ are $\mathcal{F}_{k-1}$-measurable. Given the ambiguities of the notation, it is unclear what this distinction actually refers to. The authors should clarify the precise meaning of measurability in this context, and how it relates to the dependencies between the random variables.
    - The term 'NLL' is frequently used throughout, but is never defined. The authors should explicitly define the Negative Log-Likelihood and its specific form in the context of language models.
3. In Theorems 3.1, 3.2 and 3.4, the size of the finite set $K$ is a key component of the 'complexity' measure $\mathcal{C}$. Yet, $K$ itself seems to be just a technical construction in the proof, rather than something fundamental to the model. The authors should clarify what role this set plays, and why it should be considered as part of the complexity of the model, rather than simply an artefact of the proof. They should also indicate how this set can be chosen in practice (since the bounds are supposed to be computable). I see from Section 4 that they use 1000 points, but offer no indication of why this choice was made. The authors should justify this choice and explain how it impacts the tightness of the bound.
4. Additional random variables $Y_k$ are introduced and used in most of the main results. The authors state after Theorem 3.1 that they take this to be the mean of the model NLL, but I do not see what this can be guaranteed to satisfy the requirement that $Y_k - X_k > -\Delta$ (and how is the value of $\Delta$ chosen for this setup?). In fact, why not just take $Y_k = X_k - \Delta + \epsilon$ for some fixed value of $\Delta$ and a small value of $\epsilon > 0$? I do not see anything in the statement of the theorem preventing this, and it appears to optimise the bound. The authors need to clarify the constraints on the choice of $Y_k$ and justify why their specific choice is appropriate and satisfies the necessary conditions for their theorems.
5. The authors only compare their computable bound to empirical data for selected so-called 'compute-optimal' checkpoints. Why is this choice made? How does the bound compare for other checkpoints? This does not appear to be a requirement of the theorems, and so the rationale should be made explicitly clear. The authors should provide a more thorough empirical analysis, including results for non-compute-optimal checkpoints, to demonstrate the generality and practical relevance of their bound.
6. I am not convinced that the results presented by the authors justify the claim in the title. It seems to me that, in fact, their results show that increasing the size of the model will in general *increase* their generalisation bound, by increasing the complexity term. In fact, the authors themselves appear to advocate for compressing and quantising models. The authors should explicitly justify such a strong claim in the paper, or change the title to better reflect the results they present.

### Questions
Please see the questions in the Weaknesses box.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Building on an empirical version of Freedman's inequality - a concentration bound for martingales - the authors derive generic generalization bounds for large language models. These bounds are obtained in a PAC setting and do not take into account the training of the neural network considered or the model's precise architecture. They are empirical, meaning that they can be computed in practice with a limited computational budget, and are shown to hold for a single architecture and dataset. The authors then argue that these bounds get tighter as the number of parameters increases by analyzing information accumulation within the model.

### Strengths
**On the overall presentation of the paper.**

Overall, the paper is well written. The contributions are explained in great detail and are not overstated. Most of the mathematical and theoretical background needed to understand the article is provided in the main text. Figures are clear and well designed. 

**On the empirical version of Freedman's inequality.**

This theorem and its consequences for empirical loss minimization are the central contributions of this article. I believe this concentration bound to be valuable and interesting, mostly because of its empirical variance part which can be approximated as the solution of an optimization problem on a discrete real-valued grid. 

**On the derived generalisation bounds.**

The authors combine this bound with the smoothing technique of the model of Lotfi et al. (2024a), which in a nutshell convolutes the model with a uniform distribution to smoothen the prediction function, hence incurring an error but providing an interesting proxy of the empirical unsmoothed loss. Theorem 3.4 then combines this technique with the empirical Freedman's inequality to obtain a quite generic (i.e. model and training independant) generalization bound.

### Weaknesses
 **On the comparison with related work.**

While the authors cite some related work on generalization bounds for deep models, their literature review lacks in my opinion a precise comparison with previous approaches. In particular, I would enjoy both a theoretical, mathematical and empirical comparison of the derived bounds with other bounds present in the literature - see their section 6.  It is not clear how the presented bounds compare in tightness to existing bounds, and what specific advantages they offer beyond being empirical.

**On the tightness of the generalization bounds.**

From what I understand, the generalisation bounds display a strong linear dependency in the number of parameters - at least in the form presented in theorem 3.4. The authors later on argue that this bound can be improved, by improving on the inequality $L(h) \leq bN \log 2$. While interpretable and empirical, these bounds display an extreme dependence in the number of parameters, which is undesirable in the case of LLMs. The linear dependence on the number of parameters, even if mitigated by the information content argument, still raises concerns about the practical utility of the bound for very large models.

**On empirical evaluation.**

The validity of the author's claims is assessed on a single LLM on a given dataset. I am unsure whether this evaluation is sufficient. I have little experience in the evaluation and training of LLMs, hence my analysis of this part is limited. I will revise my judgement based on other reviews and discussions with the authors. The lack of diversity in the empirical evaluation limits the generalizability of the conclusions. It is unclear if the observed trends would hold for different model architectures or datasets.

**On Section 5.**

My principal concern lies in the arguments made in section 5. The authors argue that while their bound is linear in the number of parameters in the form presented in Theorem 3.4, one can refine this bound and obtain a bound which is independent of $N$ the number of parameters. This section is not clear and hard to understand --- I stress that I am not familiar with prequential coding and might hence not be the targeted audience here. In the end, I do not understand how the authors conclude from Equation $(6)$ that their generalization bound improves with the number of parameters. From what I understand, the authors claim that their bound improves as the number of parameters increases only if the size of the dataset increases as well. If this is the case, I believe that the significance of their results is overclaimed.  The connection between the scaling law and the prequential coding argument is not clearly established, and the assumptions behind the information content analysis are not fully transparent.

**Supplementary comment.**

I also raise to the other reviewers and chairs attention that this article relies on the smoothing technique designed by Lotfi et al. (2024a). The validity of the results of this paper has been questioned during review (see https://openreview.net/forum?id=GY1fKFXG5i&noteId=s9ciWh5QAI) leading to a rejection of this paper at another conference. While I am unable to assess whether this interrogations are justified, and if the possible errors in this paper might carry over to the results exposed here, I believe that this information should be shared among reviewers and chairs.

### Questions
* Could you please provide supplementary thorough explanations of section 5 ? I am puzzled by the arguments made here. 

* In regard of this last question, could you consider including a supplementary part which gives more background on these ideas ? 

* Could you give mathematical details on how your proof techniques rely on the results of Lotfi et al. (2024a) ? In the worst case, if these results were to be false, would your analysis still hold ?

### Soundness
3

### Presentation
3

### Contribution
3
