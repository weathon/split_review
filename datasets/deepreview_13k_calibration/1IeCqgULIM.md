# Abstracting and Refining Provably Sufficient Explanations of Neural Network Predictions

- Decision: Reject
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
Despite significant advancements in post-hoc explainability techniques for neural networks, many current methods rely on approximations and heuristics and do not provide formally provable guarantees over the explanations provided.  Recent work has shown that it is possible to obtain explanations with formal guarantees by identifying subsets of input features that are sufficient to determine that predictions remain unchanged by incorporating neural network verification techniques. Despite the appeal of these explanations, their computation faces significant scalability challenges. In this work, we address this gap by proposing a novel abstraction-refinement technique for efficiently computing provably sufficient explanations of neural network predictions. Our method *abstracts* the original large neural network by constructing a substantially reduced network, where a sufficient explanation of the reduced network is also *provably sufficient* for the original network, hence significantly speeding up the verification process. If the explanation is insufficient on the reduced network, we iteratively *refine* the network size (by gradually increasing it) until convergence. Our experimental results demonstrate that our approach substantially enhances the efficiency of obtaining provably sufficient explanations for neural network predictions while additionally providing a fine-grained interpretation of the network's decisions across different abstraction levels. We thus regard this work as a substantial step forward in improving the feasibility of computing explanations with formal guarantees for neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work introduces an approach to provide "provably minimally sufficient
explanations", based on "abstraction refinement". Provably minimally
sufficient explanations are defined as the minimal set of features required to
under which the model produces the same prediction. Abstraction
refinement is a method from model checking and verification, which reduces the
complexity of the model while keeping the prediction (winning class) constant,
somewhat similar to model pruning. The work includes a formal proof motivating
its approach, and some empirical experiments analyzing the runtime and
identified number of minimal features, as well as a comparison to two similar
approaches with respect to sufficiency and runtime.

### Strengths
- The work is clearly written.

- The proposed approach is well-motivated.

- The work makes the limitations of its approach clear.

- The application of abstraction-refinement from the area of model verification
  to feature explanation in an occlusion-based context is original.

### Weaknesses
 - Significance: The practicality of the approach is severely limited by is long
  runtime (up to 3 hours for a single attribution mask). This issue could be
  alleviated by discussing trade-offs, especially considering the approaches in
  Table 2. Comparing with these methods, SIS and Anchors, there is likely some
  optimal trade-off between sufficiency and runtime that would be valuable to
  analyze. Specifically, the current work does not explore how the size of the epsilon ball used in the verification process impacts runtime and the size of the minimal sufficient set. A smaller epsilon ball would likely reduce the computational cost of verification, but at the expense of a less robust explanation.

- Contribution: The identified explanations may not necessarily be unique. A purely additive
  model with some threshold could have any combination of inputs, as long as
  the threshold is passed (i.e., the prediction does not change). Due to this,
  the identified feature attributions might not necessarily present all
  features relevant for the prediction, but rather only a subset thereof.
  A discussion of the uniqueness, and the issue of the order of removing the
  features, would be very valuable. The method's reliance on a specific feature removal order, such as prioritizing features based on their sensitivity values, could lead to different minimal sufficient sets. The paper should discuss how this ordering impacts the resulting explanation and whether alternative orderings could lead to different, but equally valid, explanations.

- Novelty: There is a plethora of approaches (see, e.g., Ancona et al., 2019 for
  approximations of Shapley values) that assign relevance to features (somewhat
  different to choosing feature subsets) with this issue without constraining
  the sufficiency (i.e., the fidelity) of the model directly. These mostly
  avoid computing the Occlusion (see Zeiler 2014), which observes the
  prediction under removal of individual features, due to its infeasible
  runtime. The approach presented is very similar to occlusion-based
  approaches, as the model is reduced in order to occlude parts of the input.
  This is an important body of related work to discuss. The paper should explicitly discuss the computational cost of the abstraction refinement process compared to simpler occlusion-based methods. While the proposed method offers formal guarantees, it is important to understand the practical trade-offs in terms of runtime and scalability compared to these alternatives.

### Questions
- Did you consider some trade-off of sufficiency versus runtime?

- How do you solve the issue of uniqueness of the relevant feature set?

- How does this work compare to "brute-force" occlusion?

- How did you verify the sufficiency for the heuristics-based approaches?

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
3

### Summary
The paper proposes an abstraction-refinement technique to create provably sufficient and minimal explanations for neural network predictions. The method works by initially generating a smaller, abstract network through a neuron-merging technique. Neurons with similar behavior are combined, controlled by a reduction rate, which specifies the extent of abstraction. This smaller network allows faster computation of explanations, but if the explanation is insufficient, the network is iteratively refined by gradually adding neurons back until a satisfactory explanation is found.

The evaluation on datasets like MNIST, CIFAR-10, and GTSRB shows that this approach is more efficient in both computation time and explanation size than traditional verification-based methods. However, the method’s reliance on neural network verification may limit scalability, and its testing on only standard benchmarks raises questions about real-world applicability. Nonetheless, the paper’s contribution lies in using formal verification to ensure that the explanations are very sound and reliable, which is critical for safety-sensitive domains.

### Strengths
1. Introduces a novel abstraction-refinement framework integrated with neural network verification for generating provable explanations, a unique combination in the field.
2. Empirical results are robust, with detailed comparisons to baseline methods.
3. The paper is well-written with precise definitions and a logical flow that enhances its readability and understanding.
4. Addresses a critical challenge in XAI, making it possible to deploy more reliable AI systems in regulated environments.

### Weaknesses
1. The method’s reliance on neural network verification queries limits its scalability to real-world applications. The verification tools required here may not support the level of scalability needed for larger, state-of-the-art networks. Specifically, the computational complexity of verification, which often scales exponentially with network size and depth, poses a significant barrier. This is particularly concerning for models with complex architectures, such as those employing attention mechanisms or residual connections, which are common in modern deep learning.

2. The paper primarily tests on MNIST, CIFAR-10, and GTSRB, standard benchmarks that do not adequately test the scalability and generalizability of the method. This narrow evaluation undermines claims of efficiency and limits insights into practical, diverse applications (such as regression problem). Including a challenging regression problem, such as the aircraft taxiing task evaluated by Wu et al., would provide stronger evidence of the method's scalability and applicability in high-stakes, continuous-output domains. Furthermore, these datasets are relatively low-dimensional and may not capture the complexities present in real-world data, such as high-resolution images or natural language text.

3. The abstraction process risks oversimplifying the neural network to a degree that explanations may lose meaningful detail, leading to explanations that are formally sufficient but practically uninformative. The neuron merging technique, while efficient, could potentially obscure critical interactions between neurons, resulting in explanations that are too coarse to be useful for debugging or understanding model behavior. This is especially problematic if the merged neurons represent distinct functionalities within the network.

4. The paper’s current evaluation lacks a comprehensive set of baselines, particularly from perturbation-based and gradient-based explainability methods. Including comparisons with these widely used XAI techniques would better contextualize the capabilities of the proposed abstraction-refinement approach. For example, methods like LIME or SHAP, which provide local explanations, could offer a different perspective on feature importance that is not captured by the proposed method. A comparison with these methods would help to understand the trade-offs between formal guarantees and practical interpretability.

### Questions
1. Could the authors provide further insights or potential solutions on how to extend the applicability of their method to more complex, state-of-the-art neural network architectures?
2. In the experimental setup, was the computational overhead of the abstraction-refinement process compared to traditional methods quantified beyond explanation size and time? A breakdown of this could enhance the paper's impact.
3. How does the method perform across different domains, such as vision versus text? Are there domain-specific challenges that might affect the sufficiency of explanations?
4. Have the authors considered evaluating their method on a complex regression problem, such as the aircraft taxiing task used in Wu et al.'s work?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an abstraction-refinement approach to efficiently generate provably sufficient explanations for neural network predictions. Traditional formal explainability methods are computationally intensive and struggle with scalability on larger models. This method simplifies the neural network by creating a smaller, abstract version, which speeds up the computation of explanations. If the explanation is insufficient, the network is gradually refined until a minimal, sufficient subset of features is identified.

### Strengths
1. The paper presents a unique abstraction-refinement technique, effectively bridging the gap between interpretability and scalability in neural network explanations. This approach is innovative in the realm of provable explanations.
2. Unlike many heuristic-based explainability methods, this technique provides formal guarantees for explanation sufficiency, which is highly valuable in safety-critical applications requiring reliability in interpretability.

### Weaknesses
1. The paper primarily demonstrates results on relatively simple models and standard datasets. Testing on more complex architectures (e.g., deep CNNs or Transformer-based models) would strengthen the claims regarding scalability and broader applicability. The current experiments do not sufficiently demonstrate the method's ability to handle the computational demands of modern, large-scale neural networks, particularly those with complex, non-linear activation functions and intricate architectures.
2. While the abstraction-refinement approach reduces computational load, it is still constrained by the scalability limits of neural network verification. The authors could address this limitation by discussing ongoing advancements in verification techniques and how they might enhance this method. The paper lacks a detailed discussion on the specific types of verification algorithms used and their inherent limitations, which are crucial for understanding the practical scalability of the proposed approach.
3. The comparison focuses primarily on heuristic-based methods (e.g., Anchors and SIS) but lacks depth regarding alternative formal explanation methods. Adding comparisons with other provable techniques would provide a more comprehensive evaluation. The paper should include a more thorough comparison with other formal methods, such as those based on symbolic reasoning or constraint satisfaction, to better position the proposed approach within the landscape of provable explainability.
4. The abstraction process may lead to information loss, which could affect the explanation's precision or fidelity. The paper could benefit from a more in-depth analysis of the trade-offs between explanation minimality and information retention across abstraction levels. The paper needs to quantify the potential loss of information during abstraction, possibly by measuring the difference in the explanation's fidelity or the change in the model's behavior after abstraction.

### Questions
1. How well does the abstraction-refinement approach scale to more complex architectures, such as Transformers or deeper CNNs, beyond the datasets tested? Can the authors provide insights or preliminary results on its performance with larger models?
2. The paper mentions that abstraction reduces the network size, potentially losing information. How does this information loss impact the quality or trustworthiness of the explanations? Could the authors quantify or analyze this trade-off?
3. The experiments focus on image datasets. How does the approach generalize to other types of data, such as time-series, tabular data, or text? Are any modifications to the method necessary for non-image data?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
The paper proposes to adopt an abstraction-refinement approach similar to distillation techniques for scaling up the extraction of provably sufficient explanations.
This is a relevant research direction, as traditional methods have scalability issues.
Results confirm that the extracted explanations are indeed sufficient and also minimal, and the runtime shows great improvements compared to baselines.

### Strengths
- Providing provably sufficient explanations is a relevant problem, and developing methods to compute them efficiently is certainly of great interest. The results confirm the effectiveness of the proposed methodology
- The overall quality of the writing and presentation is very good
- The authors provided the source code with a good description of how to use it

### Weaknesses
 - Corollary 1 is essential for the overall message of the paper, but the proof is not self-contained and seems more like a straightforward application of the result of [1]. The authors should make the proof more self-contained, also clarifying how it builds on top of [1].

-  The title suggests that the main contribution is a method providing provably sufficient explanations for neural networks. To my understanding, however, providing a provably sufficient explanation of an abstract model as per [1] is *fairly easy*, given that a sufficient explanation for any abstract model will also be sufficient for the original one. Nonetheless, this does not guarantee the minimality of the explanation, requiring the iterative refinement method proposed in Algorithm 2. I wonder, therefore, whether the main contribution lies in providing provably sufficient explanations, or in making a provably sufficient explanation also provably minimal.

### Questions
- How hard is it to extend these results to arbitrary modifications of the complement, therefore not limiting to an epsilon-ball perturbation?

### Soundness
3

### Presentation
4

### Contribution
3
