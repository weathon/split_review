# MOUCHI: Mitigating Over-forgetting in Unlearning Copyrighted Information

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Large language models are trained on massive internet datasets, which may inadvertently memorize illegal copyrighted content, making its inclusion unavoidable. Unlearning is a potential solution to remove such content. However, existing unlearning methods often suffer from **over-forgetting**, where the process unintentionally erases knowledge similar to the copyrighted content that falls under fair use and should be preserved. To address this issue, we propose **MOUCHI**, a novel unlearning framework that introduces the concept of **derivative knowledge**, a subset of information derived from copyrighted content that must be retained during unlearning. MOUCHI first generates derivative knowledge and then incorporates a derivative loss function into the unlearning process to mitigate over-forgetting in unlearning copyrighted content. Due to its plug-and-play nature, MOUCHI can be effortlessly integrated into existing unlearning methods. Experimental results show that MOUCHI reduces unintended knowledge loss, improving performance by **up to 145%** compared to baseline methods when evaluated on the derivative set.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the problem of over-forgetting during the unlearning process of LLMs, i.e., unintentionally removing similar content which should be preserved. The authors propose a concept of derivative knowledge, which is a subset of information derived from the copyrighted content and should be retained during unlearning. In particular, 1) the set derivative knowledge will be generated and 2) a derivative loss function is included. Different unlearning approaches can incorporate their proposed method and obtain various performance improvements in terms of model utility and forget quality.

### Strengths
* Propose an interesting and effective approach to tackle the over-forgetting issue of LLMs' unlearning process
* The approach can be integrated into existing unlearning methods to achieve various performance improvements
* Detailed analysis of the experiment results

### Weaknesses
 * Lack of manual analysis of the derivative knowledge: the authors also mention that experts/lawmakers need to be involved to check the boundary, otherwise it is difficult to judge how good (enough) the KL-based semantic similarity is in this context. I would suggest the authors to incorporate human judgements in this process.
* Experiments are restricted to one dataset, also one scenario/domain. Maybe the authors could comment on how easy/difficult for the approach to be adapted to other types of copyrighted information.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper titled "MOUCHI: Mitigating Over-Forgetting in Unlearning Copyrighted Information" addresses the critical issue of copyright infringement within large language models (LLMs). Due to the extensive and often indiscriminate data used in their training, LLMs can inadvertently memorize and reproduce copyrighted content, posing a significant legal and ethical challenge. The proposed MOUCHI framework introduces "derivative knowledge" as a subset of information derived from copyrighted content but intended for retention during unlearning to maintain fair-use knowledge. MOUCHI integrates a derivative loss function to differentiate and preserve derivative knowledge, allowing the model to continue answering general questions related to copyrighted material while removing infringing content. The framework is designed to work seamlessly with existing unlearning methods, providing a plug-and-play solution. Experimental results show that MOUCHI successfully reduces unintended knowledge loss by up to 145% over baseline methods.

### Strengths
The paper is well-written, with a clear explanation of the problem and the proposed solution. 

The concept of over-forgetting and derivative knowledge is effectively introduced and explained, making the paper accessible to a broad audience.

Copyright concerns in LLMs are increasingly pressing, particularly as these models become more widely deployed. The focus on balancing copyright compliance with preserving relevant knowledge is timely and important. MOUCHI attempts to address the complex need to avoid copyright infringement while retaining content that may fall under fair use.

### Weaknesses
The MOUCHI framework, while straightforward, maybe too simplistic to fully address the nuanced requirements of copyright compliance. 

MOUCHI may still risk indirect copyright violations by retaining derivative knowledge that could closely resemble the copyrighted content "CopyBench: Measuring Literal and Non-Literal Reproduction of Copyright-Protected Text in Language Model Generation"

Utility evaluation is limited, which weakens the claim of solving overforgetting problems. The authors may need to run common benchmarks such as MMLU to ensure the utility of LLM is not sabotaged. 

The paper does not compare MOUCHI with some recent and relevant unlearning baselines, such as Goldfish Loss "Be like a goldfish, don’t memorize!" and "Avoiding Copyright Infringement via Machine Unlearning"

Code is not given.

Although the authors reference several key studies, the paper could be strengthened by discussing additional recent works that are pertinent to the topic of copyright compliance in LLMs. Listed below:

- Foundation Models and Fair Use
- Rethinking LLM Memorization through the Lens of Adversarial Compression
- Llms and memorization: On quality and specificity of copyright compliance
- SHIELD: Evaluation and Defense Strategies for Copyright Compliance in LLM Text Generation
- Digger: Detecting copyright content misusage in large language model training
- Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4

KL Divergence value is constrained by ChatGPT? Is this possible without an iterative approach?

How to know whether the generated dataset is correct and does not include hallucinations?

### Questions
KL Divergence value is constrained by ChatGPT? Is this possible without an iterative approach?

How to know whether the generated dataset is correct and does not include hallucinations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the over-forgetting in LLM unlearning, this paper proposes MOUCHI, a new unlearning framework that generates a set of derivative knowledge to enrich the retain set. The derivative knowledge lies between the forget set and the retain set, which helps to better specify the boundaries of the knowledge to be removed. Experimental results demonstrate that MOUCHI can provide better control over over-forgetting.

### Strengths
1.This paper is well motivated as it focuses on the over-forgetting issue in unlearning.

2.This paper proposes a simple method to expand the retain set in the form of data synthesis.

### Weaknesses
1.The proposed method lacks novelty as it simply prompts the model to generate derivative knowledge and uses KL divergence for filtering. And there is no improvement in the loss function for the derivative set, which can be regarded as an expansion of the retain set. Is there a generation-free way to induce derivative knowledge?

2.This paper only conducts experiments on TOFU and needs to verify the effectiveness on more unlearning datasets, such as scenarios where the range of unlearning knowledge is particularly extensive.

3.Some implementation details are lacking. For example, the forget set in TOFU consists of 200 fictional authors and has no connection with real-world knowledge. Then what is the derivative knowledge of these fictional authors? Some generated results need to be provided.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Copyright concerns in large language models (LLMs) have become especially prominent due to the widespread use of these models, making them more vulnerable to misuse. Unlearning is a potential solution for removing such content. However, existing unlearning methods often suffer from over-forgetting, where the process unintentionally erases knowledge that is similar to copyrighted content falling under fair use and should be preserved. There is a trade-off between unlearning and over-forgetting.

This paper analyzes and identifies the over-forgetting problem in current LLM unlearning methods, then introduces the concept of derivative knowledge, and applies it to the MOUCHI framework by proposing the $L_{drv}$ loss. Experimental results show that this method achieves better performance than previous unlearning methods.

### Strengths
This paper investigates the issue of over-forgetting in unlearning methods. Its strengths include:

1. Analyzing and identifying the over-forgetting problem in current LLM unlearning methods.
2. Proposing the concept of derivative knowledge, which can be viewed as a buffer zone between the knowledge to be forgotten and the knowledge that needs to be retained.
3. Carefully designing a derivative generation module, with experimental results surpassing those of previous unlearning methods.

### Weaknesses
1. There are inconsistencies in the paper's wording. For example, in line 17, it states, "...the concept of derivative knowledge, a subset of information derived from copyrighted content that must be retained during unlearning." However, in line 76, it says, "the concept of derivative knowledge—a subset derived from the target copyrighted information that needs to be removed."

2. More experiments are needed to validate the effectiveness of the method. Currently, the paper is based on only one language model and a relatively small dataset (TOFU), where each author has only 20 QA questions. Such results may have certain limitations. There are many existing, more comprehensive unlearning datasets available, and broader testing is required to assess the method's generalizability. The TOFU dataset's limited size and specific structure may not fully capture the complexities of real-world copyright unlearning scenarios. The lack of diversity in the dataset, particularly with only 20 QA pairs per author, raises concerns about the robustness of the findings. The paper should also consider the impact of varying dataset sizes and the potential for overfitting on such a small dataset. Furthermore, the method's performance on datasets with more complex relationships between copyrighted and derivative content remains untested. [1,2,3]

### Questions
1. Since the TOFU dataset is relatively small, this paper divides it into four subsets (by augmenting part of the data). Could you provide a detailed distribution of these subsets?

2. Regarding the evaluation metric "Derivative," if MOUCHI is not included, will the model not be trained on $D_{drv}$ ? Or is $D_{drv}$ integrated into other subsets for training?

3. Given the diversity of ChatGPT's generated content, has the determination of δmin and δmax undergone multiple validations to ensure its accuracy?

4. In the example on the right side of Figure 6, is the given "A" the knowledge that the model needs to retain? If so, what specifically needs to be forgotten? For clarity, it would be helpful to include related Q&A from both the Forget set and the Derivative set for the same author in the presentation, illustrating what should be retained versus what should be forgotten.

### Soundness
2

### Presentation
3

### Contribution
3
