# Just How Flexible are Neural Networks in Practice?

- Decision: Reject
- Scores: 5, 6, 5, 5, 3

## Abstract
It is widely believed that a neural network can fit a training set containing at least as many samples as it has parameters, underpinning notions of \emph{overparameterized} and \emph{underparameterized} models.  In practice, however, we only find solutions accessible via our training procedure, including the optimizer and regularizers, limiting flexibility.  Moreover, the exact parameterization of the function class, built into an architecture, shapes its loss surface and impacts the minima we find. In this work, we examine the ability of neural networks to fit data in practice.  Our findings indicate that: (1) standard optimizers find minima where the model can only fit training sets with significantly fewer samples than it has parameters; (2) convolutional networks are more parameter-efficient than MLPs and ViTs, even on randomly labeled data; (3) while stochastic training is thought to have a regularizing effect, SGD actually finds minima that fit more training data than full-batch gradient descent; (4) the difference in capacity to fit correctly labeled and incorrectly labeled samples can be predictive of generalization; (5) ReLU activation functions result in finding minima that fit more data despite being designed to avoid vanishing and exploding gradients in deep architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper empirically investigates the practical flexibility and capacity of neural networks to fit data, introducing several key findings:

1. Practical Capacity vs Theory: While theory suggests neural networks can fit as many samples as they have parameters, in practice, they often fit significantly fewer samples under standard training procedures.

2. Architectural Efficiency: The study finds that CNNs are more parameter-efficient than MLPs and Vision Transformers (ViTs), even when trained on randomly labeled data, highlighting the importance of architectural inductive biases.

3. Optimization Effects: Stochastic training methods like SGD enable networks to fit more data than full-batch gradient descent, suggesting that stochasticity enhances flexibility beyond regularization effects.

4. Generalization Predictor: The difference between a network's ability to fit correctly labeled versus incorrectly labeled data strongly correlates with generalization performance, providing a novel metric for predicting generalization.

5. Activation Function Impact: ReLU activation functions improve data-fitting capability beyond their traditional role in addressing gradient issues.

The paper measures these effects using the Effective Model Complexity (EMC) metric, which quantifies the largest sample size a model can perfectly fit under realistic training conditions. To support their findings, the authors conduct extensive experiments across various datasets (including ImageNet-20MS), model architectures, and training procedures.

This research bridges theoretical understanding with practical observations about neural network capacity, providing insights into model design, training procedures, and the relationship between flexibility and generalization.

-------- 
Update: After reviewing the responses, I hold my original score.

### Strengths
**Originality:**
The paper's primary innovation lies in systematically quantifying the gap between theoretical and practical neural network capacity. While building on Nakkiran's EMC metric, it makes three notable advances: (1) demonstrating that SGD solutions enable fitting more samples than full-batch gradient descent, challenging the conventional wisdom about SGD's purely regularizing role, (2) showing that CNNs maintain parameter efficiency advantages even on random data, suggesting fundamental architectural benefits beyond inductive biases, and (3) establishing EMC differences between correct and random labels as a strong generalization predictor. However, the core methodology remains largely derivative of existing capacity measures, and the theoretical framing draws heavily from prior work on overparameterization.

**Quality:**
The experimental methodology exhibits both strengths and concerning limitations. The convergence criteria combining gradient norms, loss plateaus, and Hessian eigenvalue verification provides robust guarantees for capacity measurement. The systematic ablation across architectures (MLPs, CNNs, ViTs), optimizers (SGD, Adam, Shampoo), and data conditions enables clean isolation of individual factors. However, two critical weaknesses undermine the work: (1) the lack of theoretical analysis explaining why SGD enables fitting more samples or why CNNs maintain efficiency on random data, and (2) insufficient statistical rigor - while error bars are provided, formal hypothesis testing and effect size calculations are notably absent. The computational feasibility of EMC calculation for large architectures also raises scalability concerns.

**Clarity:**
The paper's structure effectively builds from motivation through methodology to results, with particularly strong visualization of key findings. The experimental section clearly delineates controls and confounding factors. However, several crucial elements lack sufficient detail: the precise criteria for EMC convergence, the hyperparameter optimization methodology, and most importantly, the theoretical connections between EMC and generalization. The appendices provide thorough implementation details but omit key derivations and proofs. The paper would benefit from explicit formalization of its hypotheses and clearer specification of where empirical results extend versus contradict prior theoretical work.

**Significance:**
While the paper's empirical findings are interesting, their impact is constrained by three factors: (1) domain specificity - results are primarily limited to image classification tasks, leaving questions about generalization to other domains like language models or reinforcement learning, (2) lack of theoretical grounding - without mechanistic explanations for the observed phenomena, it's unclear how to extend these insights to new architectures or training regimes, and (3) practical limitations - the computational cost of measuring EMC may restrict its applicability. That said, the demonstration of CNN architectural advantages persisting even on random data provides valuable guidance for architecture design, and the EMC-based generalization predictor outperforming existing metrics offers immediate practical utility. The work opens important questions about the relationship between optimization algorithms and model capacity.

### Weaknesses
 **Key Technical Limitations and Suggested Improvements:**

1. **Theoretical Foundation for SGD Findings**
The paper's most striking result - that SGD enables fitting more samples than full-batch GD (Figure 3b) - lacks theoretical analysis. While empirically robust, understanding why this occurs is crucial (please let me know if I'm missing something). The authors should investigate whether this results from:
    - Loss landscape exploration properties (could analyze loss surface geometry using recent techniques from Li et al. 2018, "Visualizing the Loss Landscape of Neural Nets")
     - Implicit regularization effects (connect to Gunasekar et al. 2021 work on implicit biases)
    - Different minima characteristics (analyze Hessian properties of solutions found by each optimizer)

2. **Limited Domain Validation**
While image classification results are thorough, claims about general network capacity require broader validation:
- Test on sequence modeling tasks to verify if CNN parameter efficiency persists in different domains
- Include language learning experiments to examine capacity effects with sequential, non-iid data
- Current conclusions may not generalize beyond vision - a critical limitation for a paper about fundamental network properties

3. **EMC Practicality Concerns**
The EMC metric, while insightful, has serious computational limitations:
- Computing EMC for large models (>100M parameters) requires prohibitive compute
- No discussion of approximation methods or scaling strategies
- Need comparison with cheaper alternatives (gradient noise scale, NTK condition numbers)
Suggesting efficient estimation methods would make EMC more practically relevant.

4. **Statistical Rigor**
The empirical analysis needs stronger statistical validation:
- Add formal hypothesis tests for architecture comparisons
- Include effect size calculations to quantify the strength of observed differences
- Provide confidence intervals for EMC measurements
This would help distinguish robust findings from potential noise in the experiments.

### Questions
1. **Theoretical Connection to SGD Dynamics**
Could you explain or analyze why SGD enables fitting more samples than full-batch GD (Figure 3b)? Your empirical results show this consistently, but understanding the mechanism (implicit regularization, loss landscape exploration, or other factors) would significantly strengthen the paper. Have you considered analyzing the loss landscape properties or gradient noise characteristics of these solutions?

2. **EMC Scalability**
For a network with 100M parameters, computing EMC appears to require dozens of full training runs. Have you explored efficient approximation methods or upper/lower bounds that could make EMC practical for modern architectures? What is the largest model size where EMC remains computationally feasible?

3. **Architecture Generalization**
The superior parameter efficiency of CNNs persists even on random data - does this hold for other domains? Specifically, have you tested whether similar architectural advantages appear when comparing Transformers vs. MLPs on sequence tasks? This would help validate whether your findings about architectural benefits generalize beyond vision.

4. **EMC Failure Modes**
Under what conditions does the correlation between EMC gap (real vs. random labels) and generalization break down? Have you tested this with different optimization settings, architectures, or dataset properties? Understanding the limitations of EMC as a generalization predictor would clarify its applicability.

5. **Statistical Significance**
Could you provide formal hypothesis tests and effect size calculations for the architecture comparisons, particularly for the EMC differences between CNNs, MLPs, and ViTs? This would help quantify the strength and reliability of your findings about architectural advantages.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper empirically investigates the practical capacity and flexibility of deep neural networks compared to theoretical capacity. This paper reveals that parameter counting is not sufficient to understand a neural network's capacity to fit data. Effective Model Capacity (EMC), which captures the practical training dynamics, is a better measure of understanding model capacity and flexibility. It reveals dependence on other factors, such as stochasticity in optimization, activation functions, etc. The authors also observe inefficiency in parameter utilization neural networks and proposed parametrization strategies to increase parameter efficiency, such as subspace training and quantization.

### Strengths
1. The paper is written clearly and easy to understand. 

2. The influence of architectures, optimizers, and activation functions on model capacity is interesting.

### Weaknesses
1. The reasoning behind why SGD converges to solutions that fit fewer samples than parameter count is not clear. Authors should provide a step-by-step explanation of the mechanism by which SGD leads to solutions that fit fewer samples. It will be better to include a comparison with full-batch gradient descent to highlight the specific role of stochasticity in this phenomenon.

2. In Figure 1, CIFAR-10 CNN and CIFAR-10 MLP have EMC values approximately close to each other for higher values of parameter count. Thus, the observation that CNN is a more parameter-efficient MLP is not verified. This is true for MNISt-MLP and MNIST-CNN.  Authors should discuss potential reasons for the convergence of EMC values at higher parameter counts and how this affects their conclusions about parameter efficiency of CNN as compared to MLP.

3. The author should include Kendall's ranking correlation as a metric to show performance improvements in the generalization gap [https://arxiv.org/pdf/2012.07976].

### Questions
Please respond to the questions above.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the flexibility of neural networks from a new aspect with a metric called "Empirical Model Complexity". The paper considers factors such as optimizers, neural network architectures, activation functions, and regularization techniques that influence EMC. According to the experimental results, the paper finds the relation between EMC and all the factors considered.

### Strengths
The paper is well-written and easy to follow. The results involve lots of experimental observations. This topic may be an interesting direction.

### Weaknesses
1. When investigating the relation between architectures and EMC, it is hard to compare the different architectures. The shape of the architecture may have a large impact on the ability of networks, so the paper needs to explain more about the comparison among different architectures.
2. It seems like the paper summarizes and explains the results obtained by experiments without the underlying reasons. For instance, the paper states that only ReLU improves the network's ability among all the activation functions selected, but we can not know the reason why ReLU is the special one.
3. The process of computing EMC may not be so rigid. There may be some settings that cause EMC to stop growing. And, the paper does not provide any figures about training accuracies when increasing the sample size.

### Questions
Can you provide more details about why EMC can be regarded as a predictor of generalization performance?

### Soundness
3

### Presentation
3

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
This paper aims to study the capacity and flexibility of neural networks in practical settings. The authors suggest that unlike theoretical expectations, neural networks cannot in practice memorize the same number of training samples as their number of parameters and the number of neural network parameters is not the only underlying factor. In addition, they study the effect of neural network architecture, optimization approaches, and activation functions on the memorization capacity. They further show the capability of the Effective Model Capacity (EMC) (particularly its difference in fitting randomly labeled samples vs correctly labeled samples) to predict generalization.

### Strengths
- The paper is overall well-written and well-structured. Some sections (for example Sections 3 and 4) could be more concise. While certain mentioned details might be helpful for broader audiences, experienced readers might find them overly detailed as the details are mostly conventional practices in the literature.
- The empirical results are comprehensive and well-presented. The flow logically guides the reader through the findings, which are both intuitive and interesting to the research community.

### Weaknesses
 - While the paper provides a valuable exploration of the EMC metric [Nakkiran et al, 2021] and its implications, it lacks novelty. The paper's core findings, while interesting, appear to primarily confirm existing understandings about neural network memorization. The main adaptation that is done on EMC is based on an assumption that neural networks memorize/fit correctly and incorrectly labeled samples differently. This has been previously studied both theoretically and empirically for example in [Garg et al, 2021] and [Forouzesh et al, 2023], respectively.
- The paper could benefit from a deeper analysis and interpretation of the findings. Most of the provided discussions are conventionally known in the literature, and the findings that go a bit beyond existing knowledge are not provided with potential new explanations. More particular examples are given in the questions section below.
- While Figure 1.a may suggest a relationship between generalization and data-fitting capability, it's crucial to acknowledge the limitations of this observation.  The figure alone cannot directly support the claim that  "generalization is related to data-fitting capability." The key issue is when comparing models trained on different datasets, like MNIST and ImageNet. Such a comparison might be misleading, and it is like comparing apples and oranges.  The observed relationship in Figure 1.a could result from an underlying hypothesis: models achieving a specific training accuracy on MNIST might exhibit lower generalization capability than models with the same training accuracy on ImageNet. However, this is a separate assumption requiring further validation.  Concluding a direct relationship between generalization and data-fitting based solely on Figure 1.a, without exploring this underlying assumption, would be premature.

### Questions
1. Figure 2 suggests that MLPs fit random inputs more easily than semantic labels, while the opposite is true for CNNs. This contradicts the intuition that semantic labels, being more structured, should be easier to fit than random data. This would mean that the following statement from section 5.2.1 is not generalizable/valid for random inputs “We see here that the networks fit significantly fewer samples when assigned random labels compared to the original labels, indicating that neural networks are less parameter efficient than linear models in this setting. “ Why is that and what are the possible hypotheses or possible explanations for this behavior?

2. While it's expected that CNNs would have higher EMC than MLPs due to their architectural differences, it's less intuitive why CNNs exhibit higher EMC than ViTs.  ViTs generally demonstrate better generalization capabilities compared to CNNs. This raises questions about the assumed correlation between EMC and generalization, particularly when comparing CNNs and ViTs.  Does Figure 4.b show an **EMC improvement** for CNNs over ViTs? If so, how does this relate to their respective generalization gaps? Maybe the link between EMC and generalization isn't so straightforward, and it could change depending on the type of model. What are the authors thoughts on this?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors investigate the practical flexibility of neural networks through extensive experiments.
The authors make the following contributions:
- Standard training procedures often result in neural networks fitting datasets that contain significantly fewer samples than there are model parameters.
- CNN-based architectures are more parameter-efficient than MLPs and ViTs.
- Stochastic Gradient Descent (SGD) is more flexible than GD.
- EMC can serve as a generalization prediction metric.
- ReLU activation functions improve a model’s ability to fit data.

### Strengths
- The paper is well written and easy to follow.
- The experimental section is thorough, covering a variety of datasets, architectures, and design choices.

### Weaknesses
 - The novelty and core contributions of this work are not immediately evident, making it challenging to discern what differentiates it from previous research in the field. Additionally, the authors have not clearly conveyed a concrete takeaway message that highlights its practical applications or potential benefits for real-world usage. As a result, readers may struggle to understand the findings of this paper.
- Besides the correlation between EMC and the model's generalization, I find the insights presented in this work to be rather trivial. For example, the claim of "SGD is more flexible than GD" - this phenomenon was already empirically investigated in [1] where they showed that using large batches results in sharper minima in the loss landscape. Therefore the optimized model lacks generalization capabilities. In addition, the claim "ReLU activation functions improve a model’s ability to fit data" is demonstrated in [2,3].
- There are some missing details regarding how the EMC is calculated. I suspect that the score heavily depends on the size of the data partitions. Specifically, how many samples are used in the first iteration? How many are added in each subsequent iteration? Additionally, how many epochs (update steps) do you run during each iteration? These details are crucial for readers' understanding and for the reproducibility of this work.
- Calculating the EMC is computationally intensive, particularly with today’s larger models, which have a greater number of parameters, and datasets, which involve larger input sizes and more samples. This complexity makes using EMC as a metric for generalization impractical. How long did it take to compute the EMC for the ImageNet-20MS dataset? Can we approximate EMC to reduce the computational burden, or how can we make this process more efficient?

### Questions
- The authors focused on discriminative tasks (classification), do the findings present in this paper also map to generative tasks?
- Given the point above it would be interesting to see the effect on LLMs which are overparameterized.

### Soundness
2

### Presentation
2

### Contribution
2
