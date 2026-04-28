# Adaptive Inference: Theoretical Limits and Opportunities for Efficient AI

- Decision: Reject
- Avg Score: 4.20
- Scores: 6, 6, 3, 5, 1

## Abstract
With the commercial deployment of increasingly larger and more complex neural networks at the cloud and the edge in recent years, inference has become too costly in terms of compute workload worldwide. Adaptive inference methods, which dynamically adjust a neural network's size or structure during inference, offer a means to enhance efficiency of neural networks beyond what static network compression and optimization methods can fundamentally achieve.

This paper introduces the first theoretical framework for quantifying the efficiency and performance gain opportunity size of adaptive inference algorithms. We provide new approximate and exact bounds for the achievable efficiency and performance gains, supported by empirical evidence demonstrating the potential for 10-100x efficiency improvements in both Computer Vision and Natural Language Processing tasks without incurring any performance penalties. Additionally, we offer insights on improving achievable efficiency gains through the optimal selection and design of adaptive inference state spaces.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work provides a theoretical framework for quantifying the adaptive inference opportunity space. The authors introduce a notion of adaptive agents which select between multiple classifiers of varying accuracies and resource costs given data to classify. They introduce the notion of an oracle agent which alway selects the classifier with the lowest resource costs without hampering accuracy. Using the oracle agent, they derive expressions for its resource cost and accuracy as a function of the probability that smaller classifiers overcome errors made by larger models. These expressions form conservative and empirically grounded upper bounds on the resource-accuracy frontier achievable for agents on various datasets.

### Strengths
- The goal of the paper—theoretically quantifying adaptive inference opportunities—is both timely and relevant for current industrial applications of ML.
- The authors theoretical framework is explained concisely and written well.
- The bounds appear to match empirical adaptive inference results.
- The theory provides guidance for choosing the number of "states" or classifiers considered by an adaptive agent.

### Weaknesses
Theoretical bounds are most useful when they provide a prescription for how to empirically close the gap, but the bounds provided in this work are too generic to provide such insight. Suppose I have an agent with the optimal number of states as defined in Section 4.1.1, but it is not achieving the accuracy-resource trade-off predicted by the theory. How can I relate quantities of interest in my adaptive inference algorithm to terms in Eq. 10?
- See Question 1 and 2 for actionable suggestions

The model provided assumes all costs are part of a single ordered resource value and all objectives are part of a single ordered accuracy value. This oversimplifies the search space and does not allow an agent to balance multiple resource optimizations or consider multiple objectives.
- For example, sparse MoE also facilitates domain adaptation in LLMs (GLaM https://proceedings.mlr.press/v162/du22c/du22c.pdf, Meta-DMoE https://proceedings.neurips.cc/paper_files/paper/2022/file/8bd4f1dbc7a70c6b80ce81b8b4fdc0b2-Paper-Conference.pdf). In these cases, a single accuracy metric seems insufficient to capture the goals of the agent.
- A simpler case is when resources are split across memory and compute. There could be several states in the $(R_i, A_i)$ space that are equivalent on a single resource axis but different when split across two resources axes.
- See Question 3 for actionable suggestions

### Questions
1. How could someone map these results to improve an agent? For example, taking a standard sparse MoE agent, how would I identify why my agent fails to achieve better trade-offs as predicted by the theory? Perhaps you can work through an example case-study in the text.
2. If the current theory does not provide prescriptive guidelines for improving an agent, are there changes (e.g. to $\alpha_i$) that could facilitate this? Perhaps expressing $A_i$ and $R_i$ in terms of the specific adaptive inference algorithms' parameters will help. Similar to Question 1, you could either include a case study on this or expand on the discussion in Section 4.2. I recommend referring to a specific adaptive inference technique.
3. Have you considered how this theory would extend to multiple resource or accuracy axes? Are there suggestions you can make for future work (e.g. changes to Eq. 4-7) to facilitate multiple axes?

### Soundness
4

### Presentation
4

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
This paper explores theoretical efficiency and introduces performance bounds for adaptive inference methods, which dynamically adjust network's complexity based on input difficulty. The authors derive these bounds by introducing the concept of an Oracle Agent that optimally selects the least resource-intensive model configuration for each input. To simplify the analysis, the authors further adopt a constant “error correlation", which they justify with empirical evidence.

The paper presents both conservative and optimistic adaptation bounds for various SOTA classifiers on ImageNet and language models on HellaSwag, which highlight the potential accuracy and efficiency improvements achievable through adaptive inference. The authors further discuss optimal design choices for the adaptation state space, and provide insights on the number of states required to maximize efficiency gains.

### Strengths
The theoretical framework introduced is novel, and sets the foundation for further theoretical and empirical exploration of adaptive inference methods, which is valuable to the community. The simplifying assumptions adopted in the paper and supported by empirical evidence, ensure that its theoretical findings are practically applicable. Additionally, the conservative and optimistic bounds provided offer insights and guidelines for implementing adaptive inference in real-world models.

### Weaknesses
While the theoretical analysis is comprehensive, the paper would benefit from additional experimental validation to further support its claims. Specifically, testing a concrete adaptive inference method, such as AR-Net or early exiting approaches on LLMs, cited in the paper, and verifying whether the observed efficiency-performance trade-off curves satisfy the theoretical bounds, would strengthen the theoretical and empirical foundation. If such experiments are infeasible, providing an explanation would be helpful.

Additionally, in such concrete experiments, it would be beneficial to incorporate adaptation overheads as well, which are currently discussed only theoretically. This would illustrate how they impact the efficiency and performance of adaptive inference methods in more concrete examples.

- How are the dashed curves (conservative or optimistic bounds) in Figures 3 and 4 produced? Do I understand correctly that they result from applying Equation 9 to different subsets of the state space? Further elaboration on this would enhance the clarity of the paper.
- Could you please clarify more precisely how the shaded regions in Figure 4 are obtained?
- Minor typo: the paragraph in lines 393-397 appears to be repeated.

### Questions
- How are the dashed curves (conservative or optimistic bounds) in Figures 3 and 4 produced? Do I understand correctly that they result from applying Equation 9 to different subsets of the state space? Further elaboration on this would enhance the clarity of the paper.
- Could you please clarify more precisely how the shaded regions in Figure 4 are obtained?
- Minor typo: the paragraph in lines 393-397 appears to be repeated.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a theoretical framework to quantify the efficiency and performance gain opportunity size of adaptive inference methods. In this framework, an Oracle Agent is introduced, which is capable of oracle access to the predictions of an ensemble of classifiers. This agent can then estimate the expected resource consumption and accuracy of the adaptive inference agent using the ensemble. Exact and approximate bounds are provided and evaluated in empirical evidence using computer vision and natural language processing tasks.

### Strengths
The authors seem to be the first to tackle the task of adaptive inference from a theoretical perspective, deriving bounds to estimate an achievable resource consumption and accuracy using an Oracle Agent. The paper is well structured, going from the theoretical section to the experimental section.

### Weaknesses
 **General**
- Since the paper is proposing a *theoretical* framework, it could benefit from more rigorous mathematical definitions and a less convoluted style of expressing, explaining, and reasoning about these. See *Specific* part below.
- There is no related work section.
- Paragraph structures could be improved greatly. There are many paragraphs which consist of a single one or two line sentence.

**Specific**
> However, such efficiency advancements have reached a plateau, necessitating fundamentally new techniques that extend beyond the design space of conventional static neural network optimization methods.

Have they? I'm no expert in that particular field, but I was under the impression that, especially with the rise of *large* language models we saw over the last two years, these fields (compression, pruning, quantization) were thriving. It would be great if the authors would provide relevant sources to these claims.

> Let $A_i$ represent the test accuracy of classifier $i$ represented with $S_i$.

Is this with respect to a specific dataset that the classifier $i$ was trained on (the test set from the same distribution), is this the hypothetical dataset the classifier is being tested/evaluated on when the oracle agent as applied, or what exactly does this accuracy relate to?

> Given the definition of the adaptation state space, an adaptive agent aims to identify an optimal strategy that maximizes average performance ($A$) and minimizes the average resource consumption ($R$) by selecting the optimal adaptation state ($S_i$) for each given input $x$.
>
> [...]
>
> 2.2 The Oracle Agent
>
> An Oracle Agent is defined as an agent equipped with simultaneous knowledge of both resource consumption and the accuracy (i.e. correctness) of all models for each instance $x$. As a result, it can choose the adaptation state with the lowest resource consumption while still achieving the highest accuracy possible (within the constraints of the adaptation state space) for every classified instance.

How is "the optimal adaptation state ($S_i$)" defined? What does it mean to be optimal? Let's say we have $S_1 = (R_1=10, A_1=95\%)$ and $S_2 = (R_2=20, A_2=97\%)$, which state should be preferred? Doesn't this require a scoring function $f$ that depends on $R_i$ and $A_i$, such that we can actually define an "optimal" state, w.r.t. $f$?


Definition 2.1 states the Oracle Agent strategy ($R_{oracle}(x) = \min_i(R_i) \text{ s.t. } Y_i(x) = Y_{GT}(x)$ and $R_1$ else) which seems to be independent of the classifier accuracy $A_i$? According to Section 2.2, the Oracle Agent strategy is supposed to find "the optimal adaption state" based on the resources $R_i$ **and** the accuracies $A_i$?

Section 2.2.1 goes on and states the *expected* resource consumption $R_{oracle}$ and accuracy $A_{oracle}$ achieved by such an Oracle. This part could greatly benefit from more rigorous mathematical definitions to be able to follow why the authors decide on certain formulations. If we are looking at expectations, why not express the expected resource consumption and accuracy as $\mathbb{E}[R_{oracle}] = \sum_i R_i \cdot P(R_i)$ with $P(R_i)$ being the probability, that the agent chose state $S_i$, which only happens, when all classifiers $< i$ made an error ($E_i := Y_i \neq Y_{GT}$), leading to $P(R_i) = P(E_1, \dots, E_{i-1}, \overline{E_i})$. This is exactly the quantity that the authors define in Appendix A.2 as $P(x_i) = P(e_{i-1}) - P(e_i)$ with $x_i := \{Y_1 \neq Y_{GT} \cap \dots \cap Y_1 = Y_{GT}\}$ (which is an odd naming choice since $x$ is already defined as the datapoint) and $e_i := \{Y_1 \neq Y_{GT} \cap \dots \cap Y_1 \neq Y_{GT}\}$.

Secondly, the authors state the expected accuracy $A_{oracle} = 1 - P(e_N)$ without any derivation or explanation. Since $P(e_N)$ is the probability, that *all* models fail, $1 - P(e_N)$ is the probability, that at least one (or more) model is correct. I cannot follow the reasoning of why this holds, looking at the formulation of the expected value of $A_{oracle}$, we get $\mathbb{E}[A_{oracle}] = \sum_i A_i \cdot P(A_i)$, where $P(A_i) = P(E_1, \dots, E_{i-1}, \overline{E_i})$ which is the probability, that we pick state $S_i$ (same as $P(R_i)$) -- why should this "collapse" to $1 - P(e_i) = 1 - P(E_1, \dots, E_i)$? Appendix A.2 "Proof of Eq. (5)" also does not derive this quantity and simply states the same equation again in Eq. (12).

The authors then go on to rewrite $P(e_i)$ as $\alpha_i (1 - A_i)$ (for $i>1$) with $\alpha_i = P(Y_1 \neq Y_{GT} \cap \dots \cap Y_{i-1} \neq Y_{GT} | Y_i \neq Y_{GT})$ and then rewrite $R_{oracle}$ and $A_{oracle}$ using $\alpha_i$ in Eq. (7). Why are we interested in the quantity $\alpha_i$? Looking at the events, this is the probability, that all classifiers $<i$ fail, given that classifier $i$ failed. The authors state in L202, that larger $\alpha_i$ implies that it is unlikely, that a smaller model can correctly classify what a larger model misclassified and smaller $\alpha_i$ implies that it is likely, that a smaller model can correctly classify what a larger model misclassified -- okay, this is simply how $\alpha_i$ was defined, but why do we need this for the Oracle Agent?

Afterward, the authors claim

> The resource consumption and accuracy of an Oracle Agent calculated using this equation can serve as an upper bound on the performance and efficiency achievable by any adaptive agent

Why exactly is the *expected* resource consumption and accuracy an upper bound on the performance (accuracy?) and efficiency (resource consumption?)

> On the other hand, $\alpha_i$ captures the cross-dependencies among the entire set of backbone models, a detail often not reported for static off-the-shelf models

Without the authors having defined what they imply by "cross-dependencies among the entire set of backbone models", I assume, that it means that $(Y_j \neq Y_{GT}) \perp\!\!\!\!\perp (Y_k \neq Y_{GT})$ (independence) does not hold. I think this is wrong, since $\alpha_i$ is a conditional probability (conditioned on the event $Y_i \neq Y_{GT}$) which then only covers the conditional independence $(Y_j \neq Y_{GT}) \perp\!\!\!\!\perp (Y_k \neq Y_{GT}) | Y_i \neq Y_{GT}$ with $j < i$ and $k < i$.

> Figure 2: Empirical Measurements of $\alpha_i$ for different tasks and models. $\alpha_i$ remains relatively constant for models with similar architecture.

The figure shows a graph with four plot lines. *All* of them decrease in value $\alpha_i$ with increasing $i$. Saying $\alpha_i$ remains *relatively constant* sounds hand wavy and not scientific at all to me, simply to justify a constant $\alpha$, which is being used in the rest of the body.

> As previously discussed, $\alpha_i$ serves as a measure of the probability that a large model making a classification error leads to errors in all of the smaller models

How does "a large model making a classification error lead to errors in all of the smaller models"? It is simply a probability distribution over events happening (classifiers being correct/wrong), capturing correlation and **not causation**.

I've continued reading the rest of the paper (Section 3 to 6) in detail. Unfortunately, since, as explained above, I'm lost on the reasoning of the choice for most of the definitions in the essential Section 2, I wasn't able to appreciate and follow the results in the later sections.

I hope that I didn't severely misunderstand something which left me confused for the rest of the paper, but as it is written now, the essential Section 2 needs to be greatly improved to clarify most of what I've said above. I'm happy to discuss the details with the authors, and I'm interested to see if other reviewers were able to make sense of Section 2.

### Questions
See **Weaknesses**.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper, titled "Adaptive Inference: Theoretical Limits and Opportunities for Efficient AI," addresses the challenge of reducing the computational cost of neural network inference by employing adaptive inference techniques. The authors propose a novel theoretical framework for quantifying the efficiency gains achievable through adaptive inference, contrasting it with traditional static methods such as pruning and quantization. Key contributions include (1) a framework that utilises "Oracle Agents" to establish efficiency and performance bounds, (2) theoretical bounds for efficiency gains, and (3) empirical results showing that adaptive inference can yield significant improvements on tasks such as ImageNet classification and HellaSwag-based natural language inference. The work also provides guidelines for optimizing the "adaptation state space," demonstrating the potential efficiency gains of up to 121x for some models.

### Strengths
Below is the list of the strength points identified in this work:

- This paper stands out for its novel approach to quantifying efficiency in adaptive inference. Unlike traditional static techniques, such as pruning and quantization, which primarily focus on model compression, this research introduces a theoretical framework to understand and measure the potential of adaptive inference. The concept of an "Oracle Agent" is particularly interesting, as it provides theoretical bounds for the maximum efficiency achievable through adaptation, making this methodology both original and promising for optimising computational resources.
- The authors back up their theoretical framework with experiments on real-world tasks, such as ImageNet image classification and HellaSwag language inference, showing potential efficiency gains of up to 121x without sacrificing accuracy. These results make the proposed approach more credible and demonstrate that adaptive inference has practical benefits beyond theory. 
- The authors provide practical advice for designing adaptive systems, which could be applied across various AI domains, from computer vision to natural language processing.
- By providing both conservative and optimistic estimates of the gains from adaptive inference, the authors make it easier to understand the potential impact of their approach.

### Weaknesses
Below is the list of weaknesses that I would like to see refuted or clarified by the authors:

- The framework is based on the idea that the difficulty of an input can be identified quickly, allowing the model to adjust accordingly. However, the paper doesn’t explain how this input complexity could be estimated in a practical setting or what costs this might involve. Furthermore, the paper does not address the potential overhead of the adaptive policy itself. The cost of determining the appropriate adaptation strategy for each input could negate the benefits of adaptive inference, especially if this decision-making process is computationally expensive or requires significant memory. The framework needs to account for this overhead, which could vary significantly depending on the complexity of the adaptation policy.
- Moreover, the concept of complexity per input sample is central to the adaptive approach but is not clearly defined. How is complexity determined at inference without a priori knowledge? The paper lacks a concrete definition of input complexity beyond its intuitive notion. Is it based on the entropy of the input, the number of features activated, or some other measure? The absence of a clear, measurable definition makes it difficult to validate the framework's assumptions and apply it in practice. It also raises questions about how this complexity measure would generalize across different data modalities and tasks.
- The paper often relies on the constant-α approximation, which may oversimplify model dependency in adaptive systems. This assumption may not hold for heterogeneous architectures or diverse datasets. The constant-α assumption, while simplifying the analysis, disregards the fact that different layers or modules within a neural network may have varying sensitivities to input complexity. This simplification could lead to inaccurate predictions of efficiency gains, particularly in complex models where different components contribute unequally to the overall computational cost and accuracy. The framework needs to address this heterogeneity.
- The framework implicitly assumes the adaptive gains would generalise across different tasks and data distributions without rigorous testing. Given that models might perform inconsistently across various domains, the generalisation of adaptive efficiency gains seems optimistic. The paper does not adequately discuss how the proposed framework would handle domain shift or variations in data distributions. The assumption that adaptive gains observed on ImageNet and HellaSwag would translate to other datasets or tasks is not sufficiently justified, and the framework needs to address the potential for performance degradation in different scenarios.
- The framework is tested on only two datasets (ImageNet for CV and HellaSwag for NLP), which limits the demonstration of its general adaptability across tasks and different dataset dimensions. The selection of only two datasets, while providing initial validation, does not adequately demonstrate the framework's broad applicability. The framework needs to be tested on a more diverse set of tasks and datasets to establish its robustness and generalizability. This includes datasets with different characteristics, such as varying input sizes, class distributions, and noise levels.
- Theoretical derivations and equations, especially around the Oracle Agent, lack intuitive explanations, which might make it difficult for readers to understand the assumptions and implications of key equations. The theoretical derivations, particularly those related to the Oracle Agent, are presented without sufficient intuitive explanation, making it challenging for readers to grasp the underlying assumptions and implications. The paper should provide more accessible explanations of the key equations, possibly through illustrative examples or analogies, to enhance clarity and understanding.

### Questions
Authors are requested to clarify or make changes, as appropriate, based on what is discussed in the ‘Weaknesses’ section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper presents a theoretical framework aimed at quantifying the efficiency and performance gains of adaptive inference in neural networks. The authors propose that adaptive inference, where model complexity adjusts based on input instance difficulty, can yield significant efficiency improvements compared to static inference methods. By introducing an adaptation state-space model using Oracle Agents, the authors derive approximate and exact bounds on the achievable efficiency gains of adaptive methods. The study includes empirical demonstrations on models for computer vision and natural language processing, suggesting up to 10-100x efficiency improvements without compromising accuracy. Additionally, the paper offers insights on designing efficient adaptive inference pipelines.

### Strengths
1.Theoretical Novelty: The paper makes an original attempt to introduce a theoretical framework for assessing adaptive inference efficiency bounds, potentially contributing to foundational understanding in this area.

2.Potential Impact on Resource Efficiency: If successful, the framework could lead to substantial improvements in resource efficiency, with claimed gains of up to 100x, which is highly relevant for cloud and edge AI deployments.

### Weaknesses
1.Writing Clarity Needs Improvement: The paper would benefit from a more polished writing style to improve clarity. For instance, the first sentence of the abstract, "With the commercial deployment of increasingly larger and more complex neural networks at the cloud and the edge in recent years, inference has become too costly in terms of compute workload worldwide," is grammatically awkward and challenging to follow. Enhancing the readability of the text would help convey the contributions more effectively.

2.Unclear Structure and Presentation: The structure is poorly organized, with important theoretical results scattered throughout the text rather than being clearly highlighted as Lemmas or Theorems. This makes it difficult to identify the core theoretical contributions and understand how these results were derived. Additionally, there is no "Related Works" section, and the "Limitations and Future Works" section is brief and lacks organization, which detracts from the paper's overall clarity and coherence.

3.Lack of Clear Experimental Validation: Although the paper theoretically discusses efficiency bounds and includes some empirical comparisons between models (e.g., Llama-2 and Pythia), it is unclear how an Oracle model would achieve the proposed efficiency bounds. The experimental setup lacks clear alignment with the theoretical claims, leaving it ambiguous what specific hypothesis or theoretical results are being validated. This weakens the support for the authors’ claims and raises questions about the practical feasibility of achieving the claimed efficiency improvements.

### Questions
My questions are listed in weaknesses part, I hope the authors can give some feedback. Yet, this paper is not easy to follow, which make me hard to get the real point of this work.

### Soundness
1

### Presentation
1

### Contribution
2
