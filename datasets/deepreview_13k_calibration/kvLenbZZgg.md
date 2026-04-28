# Transformer Block Coupling and its Correlation with Generalization in LLMs

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Large Language Models (LLMs) have made significant strides in natural language
processing, and a precise understanding of the internal mechanisms driving their
success is essential. In this work, we trace the trajectories of individual tokens as they pass through transformer blocks, and linearize the system along these trajectories through their Jacobian matrices. By examining the relationships between these Jacobians, we uncover a \textbf{transformer block coupling} phenomenon in a variety of LLMs, characterized by the coupling of their top singular vectors across tokens and depth. Our findings reveal that coupling \textit{positively correlates} with model performance, and that this relationship is stronger than with other hyperparameters, namely parameter budget, model depth, and embedding dimension. We further investigate the emergence of these properties through training, noting the development of coupling, as well as an increase in linearity and layer-wise exponential growth in the token trajectories. These collective insights provide a novel perspective on the interactions between token embeddings, and prompt further approaches to study training and generalization in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents an insightful exploration into the internal dynamics of Large Language Models (LLMs). The authors propose a novel framework to evaluate the coupling of transformer blocks through their Jacobian matrices, offering a structured perspective on their inter-token and cross-layer relationships. The study concludes that this coupling is positively correlated with model generalization performance and appears to be a more significant factor than other hyperparameters such as parameter budget and model depth.

### Strengths
- The concept of using Jacobians to study transformer block coupling provides a fresh perspective on understanding the internal mechanics of LLMs.

- The authors conduct an extensive empirical analysis across a variety of LLMs, lending credence to their hypothesis regarding the significance of transformer block coupling.

- The paper is well-organized, with clear definitions and logical flow, making it easy to follow the complex concepts and their implications.

### Weaknesses
 - The most concern lies in the strength of the generalization claims made by the authors. The paper presents empirical evidence suggesting a strong correlation between transformer block coupling and model performance on Open LLM LeaderBoard. However, it seems that some new models (e.g., LLaMA 3, Phi-2) which involve more pertaining steps (tokens) may have a more significant increase in performance than coupling. Revisiting the Figure 2, the coupling seems to emerge at certain training steps and then remain plain. So if the correlation only holds on a limited scope of pretraining steps?

- The model performance is evaluated on Open LLM LeaderBoard. However, for some reasoning tasks, there may be some emergent capabilities [1] that only larger models have. In such settings, is the correlation between coupling and model performance still holding?

### Questions
See weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
the paper analyzes and correlates jacobian singular value decompositions cross tokens and cross layer-depths. as a result, they define a 'coupling metric', and show that high coupling apparently correlates to high benchmark values.
as such some intel on the inner processings of llm's is generated but the interpretation is widely left to the user.

### Strengths
- the paper offers a new perspective on by coupling training dynamics with model performance. 
- the method demonstrates somewhat robust as shown with the regression fit
- potentially high impact on model architecture/ training and diagnosis (if better understood)

### Weaknesses
the interpretation of this metric is vastly unclear. it is kinda clear that model training dynamics converge over training steps, in particular with common decaying lr-schedulers applied. so i wonder rather if one can interpret the score as a 'model training convergence rate' rather then performance-metric. falcon-7b (the entire model cluster > -.7 in fig1) demonstrates that high-coupling does not necessarily correlate with openllm-benchmarks afterall, tracing the activations/ gradients already shows such a convergence as well. afterall, on a converged model, activations only nuanced shift between layers. 

similarly i'm unsure how to interpret fig 6 etc.
computational costs of the methods are also not discussed (?).

overall i appreciate the solid work and do think there is merit in this methodology per se. however more focus should be made to practical implications of this rather abstract metric, and rigorously discussed.

### Questions
1) what is the value of fig 6/9?
2) what are your computational costs?
3) anything surprisingly found in the jacobians?

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
2

### Summary
This paper studies the inference dynamics in LLMs, by looking at several properties of the "trajectories" that tokens representations form as they evolve through the network. It is found that the linearized approximations of different blocks in a trained transformer tend to align with each other (in the sense of their top singular vectors being aligned), and that the magnitude of this alignment correlates with overall model performance. Several other properties of the trajectories are also discussed.

### Strengths
The paper offers an intriguing observation, expanding on previous works that have reported similar phenomena in resnets. It makes a strong use of the large number of openly available LLMs to study hidden representations. The observation that the "coupling" performance correlates with model performance is of potential interest to the community and could encourage further research.

### Weaknesses
The paper offers an intriguing observation regarding the alignment of linearized approximations of different blocks in trained transformers and its correlation with model performance. However, the manuscript lacks a coherent organization and a clear, central message. Specifically, the motivation behind considering additional metrics like "Linearity" (Section 3.2) and "Layer-wise exponential growth" (Sec 3.3) remains unclear. The paper does not establish a clear theoretical or empirical relationship between these metrics and the "coupling" phenomenon, which is the main focus. The attempt to address this in Section 6.2 is not sufficiently convincing.

Furthermore, the coupling phenomenon is presented as an "interesting observation" without much further investigation or explanation, leaving the reader unsatisfied. A more in-depth "functional" study of this phenomenon would significantly improve the paper. For instance, investigating whether this behavior is uniform across different tasks/prompts or if there are variations could provide valuable insights. Additionally, exploring whether coupling is crucial for learning or inference or merely an epiphenomenon would strengthen the paper's contribution. Another avenue for enhancing the findings' significance could be a mechanistic understanding of the phenomenon, such as examining its occurrence in small models trained on synthetic data.

There are also several specific issues that need to be addressed:

Line 35: The explanation of a "discrete non-linear dynamical system" is confusing and inaccurate. The term "discrete" typically refers to discrete time, not finite depth. The dynamics would still be "discrete" even with infinite network depth. Conversely, a continuous-time system can be evaluated for finite time. The term "coupled" is also inaccurately used; even a simple MLP or a linear network can exhibit coupled dynamics. Lastly, the term "dynamical" usually refers to the state changing with time, not the presence of residual connections. If non-standard interpretations of standard terms are used, the authors should explicitly state and justify their choices.

Figure 2 and section 5.3: The rapid rise in "coupling" suggests that the correlation between coupling and performance (Fig 1) might be due to other variables or confounders. Performance likely doesn't plateau after 10-20K training steps like coupling. Therefore, the claim that "developing training methods to amplify coupling across transformer blocks may lead to favourable model performance" (Line 431) seems too strong without evidence of a causal relationship.

Section 6.2: The explanation is confusing. Linearizing $F^l$ doesn't imply that the entire dynamical system can be approximated as linear. The system is linearized *at* a particular input $x$, so we can't infer much about the dynamics of the same input without introducing a perturbation. The authors should study the evolution of this perturbation using the linearized dynamics. Rewriting Appendix A.4 in terms of discrete dynamics would also be more relatable to the paper's content.

Figure 3: The LSS is defined as a ratio of two positive numbers, yet Figure 3 shows negative LSS values. This contradicts the statement that "LSS \(\geq 1\)" (Line 216).

Figures 4 and 5: Readability would be greatly improved by adding indications of the relevant axes and a scale/colorbar. The choice to present absolute values is also not well-motivated.

### Questions
Figure 3: The LSS is defined as $\frac{L}{\lVert \tilde{x}^l_{i}-\tilde{x}^0_{i} \rVert}$ -- clearly a ratio of two positive numbers. How can it be that LSS values reported in Figure 3 are negative?. The authors themselves mention that "Note that $\text{LSS}\geq1$" (in Line 216) which is inconsistent with Fig. 3

Figures 4 and 5: Readability will be greatly improved if some indications of the relevant "axes" is added to the figure itself (Layer/Time in Fig 4/5; embedding dimension on one of the panels; ). Since the different models basically exhibit "identical" results (at least qualitatively), I will advise the authors to keep just one column (one model) for each Fig in the main text, and use the freed space to better visual explanation (other models can be moved to Supplementary).
Even more importantly: a scale/colorbar should be included. Currently it's not even clear if different sub-panels have the same scale or no. The choice to present absolute values is also a bit odd and not well-motivated.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Coupling, a metric of a Transformer model.
It computes the similarity of two Jacobians, followed by a normalization; each is the sum of non-residual terms by Attention and FFN.
The main claim of this paper is that the Couping metric of a model, among a set of public pre-trained LLMs, is correlated with the average performance of a set of downstream tasks from the HuggingFace Open LLM Leaderboard (R^2 value of 0.7214).
Additionally, the paper explores the properties of the Transformer models in terms of the line-shape score (LSS), defined by Gai & Zhang (2021), and the exponential spacing (expodistance) of the hidden trajectories.

### Strengths
To the best of my knowledge, this work is the first to explore the Coupling measures and indicate a correlation between them and the LLM performance on downstream tasks.
It also analyzes linearity in intermediate embeddings over the depth and exponential growth of the embedding norms.

### Weaknesses
The correlation between the Coupling metric and performance may not be a helpful or exciting finding. First of all, the paper does not provide any reasonable explanation or hypothesis about (1) why they investigated the Coupling, (2) why the Coupling could reflect performance, and (3) whether the correlation is from a causality (of a direction) or not.
Additionally, the paper does not perform intervention experiments, e.g., training a model with a regularization of increasing the Coupling and demonstrating the improvement. In total, it is difficult to conclude that this finding is helpful for the community so far. There are many experimental results, but they are not always well-organized and explained. I would like to know the real contributions of the results.

The correlation between the Coupling metric and performance might be very consistent. It may disappear in trends of recent high-performance models.

The contribution of the analysis of linearity and exponential growth is unclear. In my understanding, the analysis is conducted independently from the Coupling. Results are not specific to the models of interest and the Coupling. Many things might be obvious from Li & Papyan (2023). It would be great to add connections between them and Coupling (and the performance, if possible).

### Questions
In summary, what can we concretely learn from the result? If we don't consider the quality, it's not very difficult to develop metrics that show a correlation but are ultimately not useful. Playing devil's advocate for a moment, for example, one of the most boring metrics could be the performance of a single downstream task like GSM8K. It may be correlated with the performance on the LLM Leaderboard. But, of course, this finding is not helpful. Compared with this or other candidates with such correlations, how can we claim that the Coupling metric is more interesting, helpful, or convincing?

The main claim may be based on Figure 1. But, the result looks very consolidated. Can we believe the presence of the correlation over various models or a limited number of models? For example, what happens if you only examine models that score above 50? Is there still a strong correlation, or does the relationship break down at higher performance levels? For example, if one observes phi-1 and phi-2, the Coupling rule may be broken because they may have similar settings, similar Couplings, and very different performances.

I'm not sure why linearity and exponential growth are discussed and considered as a goodness metric. Playing devil's advocate for a moment again, if we make Transformer blocks, which just scale their inputs by large positive constants, it seems to satisfy the linearity and exponential growth but would fail to achieve the high performance as they the Transformer is just a scaler. Could you provide more discussion and reasons for choosing or designing the metrics for analysis?

Figure 3 (c). Does this show that Linearity disappears at the end of training?

Figure 6. MPT -> Mistral?

Can we see Figure 6-style results of untrained models?

Figure 8. Can we see the results of untrained models?

### Soundness
3

### Presentation
2

### Contribution
2
