# Capturing substructure interactions by invariant Information Bottle Theory for Generalizable Property Prediction

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Molecular interactions are a common phenomenon in physical chemistry, often resulting in unexpected biochemical properties harmful to humans, such as drug-drug interactions. Machine learning has shown great potential for predicting these interactions rapidly and accurately. However, the complexity of molecular structures and the diversity of interactions often reduce prediction accuracy and hinder generalizability. Identifying core invariant substructures (i.e., rationales) has become essential to improving the model's interpretability and generalization. Despite significant progress, existing models frequently overlook the pairwise molecular interaction, leading to insufficient capture of interaction dynamics. To address these limitations, we propose I2Mole (Interaction-aware Invariant Molecular learning), a novel framework for generalizable property prediction. I2Mole meticulously models atomic interactions, such as hydrogen bonds and Van der Waals forces, by first establishing indiscriminate connections between intermolecular atoms, which are then refined using an improved graph information bottleneck theory tailored for merged graphs. To further enhance model generalization, we construct an environment codebook by environment subgraph of the merged graph. This approach not only could provide noise source for optimizing mutual information but also preserve the integrity of chemical semantic information. By comprehensively leveraging the information inherent in the merged graph, our model accurately captures core substructures and significantly enhances generalization capabilities. Extensive experimental validation demonstrates I2Mole's efficacy and generalizability. The implementation code is available at https://anonymous.4open/r/I2Mol-C616.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The motivation for this paper stems from limitations in molecular interaction modeling and a lack of focus on out-of-distribution (OOD) generalization capability. To address these challenges, the authors introduce I2Mole, a method designed to enhance both molecular interaction modeling and OOD generalization. 

To capture emergent properties in molecular interactions—characteristics that do not appear in independent molecules—the approach constructs a merged graph that connects the interacting molecule pair, leveraging the Graph Information Bottleneck (GIB) to extract the rational.

Subsequently, the model utilizes a codebook to enhance OOD capabilities, ensuring consistency across various environments. This codebook enables the model to adapt more effectively to diverse conditions, thereby improving generalization performance in unfamiliar scenarios.

### Strengths
* The paper clearly explains its key claims, including limitations in molecular interaction modeling and the lack of focus on out-of-distribution (OOD) generalization.

* The proposed method is technically sound. Constructing a merged graph that combines two molecules to model molecular interactions and using the Graph Information Bottleneck (GIB) to identify important substructures is an intuitive and effective approach. Additionally, the introduction of a VQ codebook to account for diverse environments is a simple yet effective strategy to enhance OOD generalization.

* The authors conducted comprehensive experiments across multiple datasets, demonstrating improved performance compared to baseline methods.

### Weaknesses
 * More detailed explanations are needed regarding the necessity of each component. For instance, it would be helpful to clarify: 1) why intra-molecular and inter-molecular message passing need to be separated after constructing the merged graph, and 2) while the limitations of simulating diverse environmental distributions through noise injection are well discussed, further elaboration on the role and benefits of vector quantization in this context would enhance understanding.

* There is insufficient consideration of environmental factors. The environment is defined based on portions of the merged graph outside of the core substructure, yet the physical and chemical environment where interactions occur, as well as other external conditions, are not considered.

* Although quantitative metrics demonstrate the model’s superiority, it is disappointing that the paper does not provide evidence that the model captures emergent structures specific to interactions, as suggested in the introduction. Showing such examples would better highlight the effectiveness of the model in learning interaction-specific substructures.

* Numerous formatting, notation, and equation issues need correction:
    * Inconsistent usage of "I2Mol" and "I2Mole."
    * In Equation (5), the definition of $k$ is missing
    * Redundant wording in "$u$ is is updated into $u_i^{'}$."
    * Misaligned square brackets in Equation (6).
    * In Equation (10), $s$ is defined by the top $s$%, but the equation appears to represent a threshold.
    * In Equation (24), the definition of $||$ is missing.
    * The following sentence in Section 4.2 seems to belong in Section 4.3: "Type 1 aims to predict potential interaction properties between known and unseen drugs, while Type 2 aims to predict potential interaction properties between unseen and unseen drugs."

### Questions
* Could you provide more detailed explanations on why each component is necessary? For example, why do intra-molecular and inter-molecular message passing need to be separated after constructing the merged graph? Also, what are the role and benefits of vector quantization in simulating diverse environmental distributions? (Related to W1)
* Can you provide examples showing that the model captures emergent structures specific to interactions, as mentioned in the introduction? (Related to W3)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a framework, I2Mole (Interaction-aware Invariant Molecular Learning), that captures atomic interactions by establishing broad connections between intermolecular atoms and refining them through an improved graph information bottleneck theory. This approach can capture core substructures critical to interactions and, in addition, create an environment codebook of the merged graph, which enhances the generalizability and preserves chemical semantics. Extensive experiments were carried out to validate the proposed approach.

### Strengths
* Combines Graph Information Bottleneck and Invariant Learning to tackle molecular interaction issues. 
* Extensive experiments that yield interesting findings.

### Weaknesses
 * Some of the math notations are confusing. For example, but not limited to the following. In equation (1), G_IB on the left side should be different from that on the right side. Similar confusion appears in equation (12). Equation (2) has a typo (it seems that the expectation term is put in the subscript), and "env" and "E" are not clearly defined.

* The construction of core reaction substructure candidate in the merged graph can be better explained. Section 3.2.2 explains see some of the components such as zi (updated node representation with injection of noise) and h_i^r (irrelevant substructure node). More clarification is needed to explain how to combine these components to construct $g^ ̃_IB$ in details.

* Regarding code embedding of environment, it is unclear how to decide M. For example, what criteria and/or method(s) can be used to justify a choice of M.

### Questions
See the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript proposes a novel framework for generalizable molecular property prediction by enhancing generalizability using graph information bottleneck theory and an environment codebook. Experimental results show that the proposed method outperforms baseline methods on three benchmark datasets.

### Strengths
1. The method is presented clearly.

2. The proposed approach demonstrates superior performance and generalizability on benchmark datasets.

### Weaknesses
1. The method has not been evaluated on common DDI benchmarks, such as those referenced in "Comprehensive Evaluation of Deep and Graph Learning on Drug–Drug Interaction Prediction".

2. It is unclear why the information bottleneck (IB) approach improves performance. As shown in Table 5, IB significantly boosts model performance, raising AUROC from 87 to 94. Providing insights or explanations about the underlying mechanism for this improvement would help readers better understand its impact.

### Questions
1. What does “environment” represent chemicallly?

2. Could you provide examples illustrating how IB enhances model performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method, I2Mole (Interaction-aware Invariant Molecular learning), for predicting molecular interactions, such as drug-drug interactions. This method is based on two main ideas: (1) identifying subgraph pairs (core substructures) that contribute most to prediction accuracy, based on Graph Information Bottleneck (GIB) theory (Yu et al, 2020; 2022b), and (2) implementing out-of-distribution generalization through invariant learning (Wu et al, 2022a) to mitigate environmental factors that may disrupt estimation. 

In (1), intramolecular message passing is first conducted for each molecule of a molecular pair, followed by intermolecular message passing, defining a merged graph from non-zero coefficients of intermolecular connections. Core substructure identification is then performed on this graph applying GIB, in particular, "compression via noise injection (Yu et al., 2022b)." In (2), several latent environmental factors in the training data are represented as learnable embedding vectors, and prediction robustness is enhanced by clustering non-core substructure variations through learning vector quantization (LVQ). The method demonstrates superior predictive accuracy over established approaches in drug-drug interaction (DDI) prediction benchmarks.

### Strengths
- In molecular interactions, explicitly considering subgraph-level interactions is crucial for both predictive accuracy and interpretability. This study leverages GIB (Yu et al., 2022b) and invariant learning (Wu et al., 2022a) as highly relevant prior knowledge to achieve more precise molecular interaction modeling and predictions that are robust to environmental factors.
- In the presentation of the paper, the motivations and intentions are clearly introduced through examples, followed by technical details, making it easier to grasp the design principles despite the complex methodology.
- Compared to many existing methods, this approach demonstrates outstanding results in DDI prediction benchmarks.

### Weaknesses
 - Overall, the paper is intriguing, but the description in Section 3.3, one of the two main ideas, is highly unclear and falls short of publication standards. For example, at the start of Section 3.3, it states that \tilde{G}_{IB} is obtained from Equation (19), but in its definition, it is derived via optimization in Equation (12), which is contradictory. Additionally, mutual information is represented as I(Y; \tilde{G}_{IB}) in Equation (12) but as MI(\tilde{G}_{IB}, Y) in Equation (19), showing inconsistency in notation. In Section 3.1, \tilde{G}_{IB} is defined as a graph, yet in Equations (20)–(22), it is treated as a multivariate vector apparently, with no explanation of this difference within the paper. Furthermore, the description of q(\tilde{G}_{IB}) in Equation (20) as “the distribution of data under environment \tilde{G}_{IB}” is too vague to understand, and defining \tilde{G}_{IB} as a subgraph of \tilde{G} while expressing (\tilde{G}_{IB}, Y) \sim q(\tilde{G}_{IB}) is unclear.

- Numerous simple typos are found throughout the draft. For instance, in the title “Bottle” should be “Bottleneck”; in Section 2.1, “a molecular” should be “a molecule”; “is is” on line 187 should be “is”; parentheses in Equation (6) do not match; “Equation equation” on line 219 should be “equation”; in Equation (19), MI(\tilde{G}_{IB}, Y) should be I(Y; \tilde{G}_{IB}); there is inconsistency on whether \tilde{G}_{IB} is a graph or a vector; and “vertor” on line 479 should be “vector.”

- Regarding Sections 3.2.1 and 3.2.2 on GIB applications, the approach primarily applies Yu et al. (2022b)’s method to a merged graph, which lacks technical originality. It would be better to clarify this point, as the sections present ideas from Yu et al. (2022b) as if they were original derivations, which is misleading. If these points are self-evident, emphasizing the proofs is unnecessary.

- The term “out-of-distribution generalization” requires discussion. Since this paper primarily addresses adaptations to environmental changes within the training data by modeling environment patterns through clustering, it focuses on robustness within the training data rather than an out-of-distribution approach. Typically, “out-of-distribution” refers to data outside the training distribution, so calling this an OOD method could be quite misleading. The original idea in Section 2.3 would be assuming that the external environments can be represented by latent factors, therefore the adjustment of Eq(2) would make sense to achieve unbiased predictions to mitigate any potential OOD biases.

### Questions
- What does the first sentence in Section 3.3 mean? Since $\tilde{G}_{GIB}$ is obtained through the optimization in Equation (12), shouldn’t it be referring to that equation rather than Equation (19)? Also, why is the notation for mutual information inconsistent? Any special meaning here?

- In Section 3.3, it seems that \tilde{G}_{GIB} is treated as a vector. How is this derived? If it’s obtained through some form of global pooling, the procedure should be clearly specified and reflected in the notation. The paper defines \tilde{G}_{GIB} as a graph, so Equations (20) and (21)–(22) doesn't make any sense.

- The probability distribution $q$ assumed in $(\tilde{G}, Y) \sim q(\tilde{G}_{GIB})$ and the sampling process from it are unclear. With respect to what variable is the expectation $\mathbb{E}$ taken?

- Also, $\tilde{G}_{GIB}$ is a subgraph of a graph from the training data, so it seems it would not contain information beyond the training set. Is it appropriate to refer to this as “out-of-distribution generalization”? If there’s any additional information on this point, please clarify.

### Soundness
3

### Presentation
2

### Contribution
4
