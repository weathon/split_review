## Human Reviewer 1

### Summary
This work combines ANN-SNN Conversion framework with a Dynamic Sparse Training (DST) scheme named Cannistraci-Hebb Training (CHT) to achieve low-power SNNs.

### Strengths
1. This work explores the feasibility of obtaining low-power SNNs from the perspective of conversion learning rather than SNN direct training (or referred to as STBP training).

### Weaknesses
1. This work only shows the energy-saving ratio in Table 2, but does not simultaneously display the inference accuracy under the corresponding sparsity level. In addition, this work only presents two small-scale static datasets (CIFAR-10/100) and convolutional network structures.

2. The so-called energy saving in this work are compared to vanilla pretrained ANN models. This work did not compare the inference accuracy and energy consumption with a series of important works based on STBP sparse training.

3. The sparse SNN obtained based on ANN-SNN Conversion requires a significant amount of time-steps in the inference phase, as evidenced by the time-steps listed in Table 2. In comparison, the SNN obtained from STBP sparse training usually only requires no more than 8 time-steps, which is also a limitation of this work.

4. The sparse training in this work was conducted during the ANN stage and is not directly related to SNN, which raises concerns about the contribution of this work to the SNN community.

5. It is obvious that the layout of the figures, tables and formulas in this work needs further optimization.

### Questions
See Weaknesses Section.

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper investigates whether dynamically sparse artificial neural networks (ANNs), trained using the Cannistraci-Hebb Training (CHT) algorithm, can improve the performance and energy efficiency of spiking neural networks (SNNs) when converted through existing ANN-to-SNN conversion methods. The authors report that converting dynamically sparse ANNs to sparse SNNs maintains comparable accuracy to dense baselines while achieving substantial theoretical energy reductions (up to 99%)

### Strengths
Originality.
Poses a concrete and timely question at the intersection of dynamic sparsity and ANN to SNN conversion: do topology-sparse ANNs yield accuracy/energy benefits after conversion when topology is preserved?

Quality.
Provides a clear experimental pipeline: train sparse ANNs via CHT, freeze topology, convert with three representative methods, then evaluate accuracy vs. time steps and theorized energy. 

Clarity.
The paper is structured and readable (method figures, tables, and definitions are straightforward).

Significance.
If validated on hardware and broader settings, the claim that sparse-topology conversion preserves accuracy while dramatically reducing energy would matter for energy-aware neuromorphic deployment.

### Weaknesses
1. Novelty appears incremental: The study combines two well-established components, namely dynamically sparse training (DST)-based sparsity and standard ANN-to-SNN conversion techniques, and focuses mainly on evaluating their combined effect rather than introducing a new methodological contribution.

2. Energy claims are theoretical and hinge on strong assumptions; no hardware validation. The headline “up to 99% energy reduction” is derived from a spike-count/FLOP model plus constants (EMAC/EAC) and the assumption that sparse hardware gives linear speed/energy benefits w.r.t. link sparsity. There is no measurement on neuromorphic or sparse-compute hardware. Consequently, the core claim remains speculative without device-level latency/energy evidence or even cycle-accurate simulators.

### Questions
1. Hardware validation: Can you provide on-device latency and energy results for one platform to substantiate the 99% savings, and report how close real savings are to the theoretical model?
2. Scope expansion: Do results persist on larger datasets (e.g., Tiny-ImageNet/ImageNet-subset) and deeper/backbone variants (e.g., ResNet/transformers) to support broad claims?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper explores a novel angle for ANN-to-SNN conversion: using dynamically sparsely trained ANNs as the source models. The authors employ Cannistraci-Hebb Training (CHT), a brain-inspired sparse training algorithm, to introduce sparsity into the ANN before conversion. The central claim is that this approach can produce sparse SNNs that achieve high energy efficiency (up to 99% savings compared to dense SNNs) while maintaining accuracy, representing a step towards more brain-like efficient computing.

### Strengths
The core idea of investigating dynamically sparse ANNs for conversion is innovative and represents a fresh contribution to the ANN2SNN field.

The focus on sparsity is well-aligned with the fundamental advantages of SNNs for energy-efficient, event-driven computation.

The method demonstrates good performance and significant energy savings on MLP (Multi-Layer Perceptron) architectures, validating the potential of the approach on simpler networks.

### Weaknesses
The title, "CONVERSION OF SPARSE ARTIFICIAL NEURAL NETWORK TO SPARSE SPIKING NEURAL NETWORK CAN SAVE UP TO 99% OF ENERGY," is potentially misleading. It suggests a 99% saving over a baseline that is not clearly specified, likely leading readers to assume it's compared to a sparse ANN. The abstract clarifies it's versus a dense SNN, but the title remains overly broad and risks overstating the finding.

The experiments are conducted on small datasets. The paper's impact would be significantly greater with validation on larger, more complex datasets (e.g., ImageNet or its subsets).

Table 2 reports sparsity and energy but crucially ​​omits the accuracy/performance​​ of the converted models. This makes it impossible to evaluate the true trade-off between efficiency and accuracy, which is the central claim of the work.

A key component of the method, CHT, is based on a preprint that has not undergone peer review. This reliance weakens the methodological foundation of the paper, as the core algorithm's efficacy and claims are not yet independently verified.

The discussion and conclusion frame the work as a significant step towards brain-like architecture. However, simply converting a sparsely trained ANN to an SNN is a relatively indirect contribution to neuromorphic computing. The narrative should be tempered to more accurately reflect the specific contribution: an efficient conversion pipeline leveraging sparse training, rather than a fundamental advance in brain-like computing.

### Questions
What are the accuracy results corresponding to the models in Table 2? Without these, the claim of high efficiency is incomplete. How much accuracy is sacrificed for the gained sparsity and energy savings?

Can the demonstrated benefits of this conversion approach scale to larger, modern datasets and architectures (e.g., deep convolutional networks)? What are the potential challenges?

Given that CHT itself is not a contribution of this paper and is not yet peer-reviewed, to what extent are the observed benefits specific to CHT versus being a general property of any high-quality sparse training method? Could similar results be achieved with other established sparse training techniques?

The 99% energy saving is compared to a dense SNN. What is the energy saving compared to a sparse SNN converted from a standard (non-CHT) pruned ANN? This would better isolate the contribution of the dynamic sparse training method.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a novel and promising approach that combines Dynamic Sparse Training with ANN-to-SNN conversion. The authors employ Cannistraci-Hebb Training to train highly sparse ANNs and successfully convert them into sparse SNNs. The results demonstrate that these sparse SNNs can achieve accuracy comparable to or even surpassing their dense counterparts, while achieving a remarkable theoretical energy reduction of up to 99%. Furthermore, the paper is the first to reveal the phenomenon of a time lag between the saturation of firing rate and accuracy in SNNs, and finds a significant difference in this lag between sparse and dense networks, providing new insights into the underlying mechanisms of SNNs. Overall, this is an important work that synergizes the advantages of structural sparsity and temporal sparsity.

### Strengths
1.This is a study on converting dynamically sparsely trained ANNs into SNNs, while prior work has mostly focused on converting dense networks.

2.The authors validate their findings across two different network architectures (MLP and VGG-16), two datasets (CIFAR-10/100), and three representative conversion methods.

### Weaknesses
1.The experiments are conducted solely on traditional CNNs like MLP and VGG-16. Currently, Transformer architectures have become mainstream in fields such as computer vision. To demonstrate the generalizability and state-of-the-art relevance of the proposed method, the authors should include experimental results on converting sparsely trained Transformer models from ANN to SNN.

2.All experiments are performed on the relatively small CIFAR-10 and CIFAR-100 datasets. The absence of validation on large-scale, more challenging real-world datasets like ImageNet raises concerns about the generalization capability of the conclusions in complex scenarios and diminishes the practical value of the method.

### Questions
1.Regarding the relatively small energy improvement (only 19%) for VGG-16 under the AEC method, the paper attributes it to the sparse SNN requiring a longer inference time T. Could the authors analyze why, under the AEC method, the 50%-sparse VGG-16 requires a longer T to reach peak accuracy? Does this suggest a potential incompatibility between certain conversion methods and sparse topologies?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5