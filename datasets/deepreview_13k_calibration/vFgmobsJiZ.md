# Verbalized Machine Learning: Revisiting Machine Learning with Language Models

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 5, 3, 6

## Abstract
\vspace{-.5mm}
Motivated by the progress made by large language models (LLMs), we introduce the framework of verbalized machine learning (VML). In contrast to conventional machine learning (ML) models that are typically optimized over a continuous parameter space, VML constrains the parameter space to be human-interpretable natural language. Such a constraint leads to a new perspective of function approximation, where an LLM with a text prompt can be viewed as a function parameterized by the text prompt. Guided by this perspective, we revisit classical ML problems, such as regression and classification, and find that these problems can be solved by an LLM-parameterized learner and optimizer. The major advantages of VML include (1) easy encoding of inductive bias: prior knowledge about the problem and hypothesis class can be encoded in natural language and fed into the LLM-parameterized learner; (2) automatic model class selection: the optimizer can automatically select a model class based on data and verbalized prior knowledge, and it can update the model class during training; and (3) interpretable learner updates: the LLM-parameterized optimizer can provide explanations for why an update is performed. We empirically verify the effectiveness of VML, and hope that VML can serve as a stepping stone to stronger interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework called Verbalized Machine Learning (VML), which constrains the parameter space to human-interpretable natural language. In this framework, the input prompt of a large language model (LLM) is optimized within the discrete natural language space, and an optimizer LLM iteratively updates the parameters of the learner LLM. VML is more interpretable and adjustable than traditional machine learning as all components are characterized by human-understandable natural language.

### Strengths
The idea of parameterizing a machine-learning model with natural language is niche. The new framework, Verbalized Machine Learning (VML), may be used to explain and distinguish between traditional machine learning and LLM-based learning schemas.

### Weaknesses
- The novelty and contribution seem marginal. While applying LLMs to classical machine learning problems is an interesting exploration, the core concept of VML, which relies on using two LLMs in a role-playing manner as a learner and an optimizer and updating LLMs through prompt engineering, does not appear to offer fundamentally new scientific insights into the nature of learning or optimization. The approach seems more like an application of existing techniques (LLMs and prompt engineering) to a new domain rather than a novel method in itself.
- I find it unclear how the millions and billions of parameters of a language model are represented by natural language. The claim that optimizing model parameters is effectively a prompt optimization problem (Line 161) seems inaccurate. In Figure 2, the prompt functions as an additional input providing contextual information, rather than directly representing or modifying the underlying model parameters. This raises questions about the true relationship between the prompt and the model's internal learned parameters.
- This framework only functions with LLMs that are adept at following instructions, which limits its applicability to smaller or non-instruction-based models. This dependency restricts the generalizability of the VML framework and raises concerns about its practicality for a wider range of machine learning tasks and models.
- The framework has been tested on regression and classification tasks, which traditional machine learning models can handle quite well. It is unclear to me why it is worth applying this LLM-based VML framework, especially considering the potential costs and computational expense associated with running large language models. A more compelling justification is needed to demonstrate the practical advantages of VML over traditional approaches in these well-established domains.

### Questions
My main question lies in the motivation behind proposing the VLM framework for classical machine learning tasks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the author propose to frame conventional machine learning with LLM as Verbalized Machine Learning: casting the "model parameters" to be the input language to the modeling LLM; and "parameter update" as language feedback from an optimizer LLM. This allows major advantages of VML include (1) easy encoding of inductive bias; (2) automatic model class selection; and (3) interpretable learner updates.

### Strengths
* illustration and mathematical formulation are very clear.

### Weaknesses
 * I do not understand the additional benefit (beyond iterative prompting methods e.g. [3] or retrieval-augmented generator model) provided by this general framework. For example,

1. Using LLM to solve basic numerical computation has been shown to be hard by previous work [1]. Therefore, LLM doesn't seem to be a fit for more advanced calculation like regression. Also, the "classical ML problems" in the paper like regression models are very simple cases, but I do not believe such observation could be extrapolated to more advanced ML setting.

2. Figure 6: couldn't a conventional decision tree achieve the same level of predictive power and interpretability? In VML framework, if the LLM is not good at instruction following anywhere during reading the "model parameter".

3. The author claim VML brings the benefit of encoding human interpretable prior, but the examples given are a bit simple, like "Prior: The input is X-ray image for identifying pneumonia." (Figure 9). And the benefit of such prior seems to be unstable (Figure 9a). Have the author tried to experiment with more complicated prior? or shows more stable benefit over "without prior"?

* Such framework seems to make so strong assumptions --- optimizer LLM are essentially treated as an oracle machine; and the LLM needs to be very strong and faithful (to input) LLM. However, LLM has been shown to be brittle for explanation [2]. If such strong assumption is put on the backbone model, the same level of efforts (to get such a strong LLM) could be spent on alternative framework (a framework to unify various approaches from like a better decision tree, or other interpretable classifier) to achieve the same desiderate claimed by VML; and the "conventional ML" models from such alternative framework could run with much higher efficiency than serving an LLM.

### Questions
Interpretability is claimed as a benefit of VML framework, but I am uncertain about the actual benefit. For example, Line 515-516 "validated by medical professional". My confusion is: what does it take for a professional to inspect the "model parameter"? If the model parameter is like a document-long, the practitioner might be better off by not using the system right?

### Soundness
2

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
4

### Summary
This paper proposed a new framework of using LLMs as the backbones of machine learning tasks. The authors illustrated and verified the ideas using several simple ML tasks, and demonstrated that the approach is feasible. Furthermore, the authors also conducted ablations to show that the method is more effective than merely prompt optimization.

### Strengths
- This paper explores the potential of using LLMs in optimization and learning. The perspective and ideas are novel.
- Overall the paper is well written and conveys the key ideas clearly with a good amount of details.
- The experiments that support the claims are thorough and well designed.

### Weaknesses
 - To make a strong argument of the generality of this new framework, the paper would need more results to show how practical it is, such as including empirical results measuring the efficiency of this approach. I'd also expect the paper to discuss the scalability of this approach, e.g. how it scales with amount of training data and size of the LLM being used. Given that this approach is not suitable for all or most machine learning tasks, the paper should carve out a concrete area of tasks which the proposed approach shines.
- Since the major differentiator with prior work, e.g. Yang et al. is the function approximation view of LLM, the paper should provide some theoretical analysis of what functions could and could not be approximated, and which properties of the LLMs architecture pose constraints, etc.

### Questions
For the training dynamics plots across model scales, i.e. Fig 10 a), it'd be more clear if the authors can change the x-axis to be the FLOPs instead of step size.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Verbalized Machine Learning (VML), a framework that uses natural language (text prompts) as the parameter space for machine learning models. VLM represents model parameters as text prompts, and uses an optimizer LLM to improve the prompts of the learner LLM. The paper mainly tests the proposed on a series of classical ML problems  such as linear regression, polynomial regression, and shows the proposed framework can enable learning textual prompts for these problems.

### Strengths
The paper studies a general and timely problem.

The main experiments cover multiple classical ML problems. The paper also presents some pilot results on image classification problems beyonds language tasks.

### Weaknesses
Overall, regarding technical contributions, the paper does not sufficiently differentiate the proposed technique from existing prompt optimization approaches and prior work using LLMs as optimizers. At the same time, the paper does not provide enough comparison against these baseline approaches. Specifically:

The proposed approach is essentially optimizing textual prompts for a learner LLM using an optimizer LLM (as acknowledged in line 160 of the paper). This has been explored in previous prompt optimization work (Pryzant, et al., 2023; Yang et al., 2023; Yuksekgonul et al., 2024; Zhang et al., 2024). The paper states the difference as  "prompt optimization seeks a generic instruction tuning without changing the original meaning." (line 233),
I am not sure if I can buy this claim, modern prompt optimization techniques do have more specific edits in the prompts (e.g., see the examples in appendices of Yang et al., 23 and Zhang et al., 2024).

Moreover, the paper lacks experimental comparisons against these related approaches. The evaluation mainly focuses on regression tasks. The only comparison with prior prompt optimization work is in Section 4.6, which provides a qualitative comparison against APE on text classification. (It's also worth noting that APE is primarily a search-based approach without LLM optimizers, making it a less relevant baseline). In order to clearly show the difference of VLM against prior approaches, it is necessary to compare to up-to-date prompt optimization approaches (Pryzant, et al., 2023; Yang et al., 2023; Yuksekgonul et al., 2024; Zhang et al., 2024) across a broader range of tasks under a controlled computational budget setting.

### Questions
See weakness

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Verbalized Machine Learning (VML), a framework that leverages large language models (LLMs) to address machine learning problems by constraining the parameter space to human-interpretable natural language. VML treats the LLM's text prompt as model parameters, enabling the model to be optimized over a discrete, sequential, and interpretable space. The framework offers advantages such as easy encoding of inductive bias, automatic model class selection, and interpretable learner updates. The paper empirically evaluates VML's effectiveness on various tasks, including regression, classification, and medical image classification, demonstrating its potential for enhancing interpretability and trustworthiness in machine learning.

### Strengths
* Good presentation
* VLM is interesting and provides a new perspective on machine learning.
* This paper investigates two important problems in machine learning: classification and regression.

### Weaknesses
 * Lack of dicussion and comparison with [1]. [1] introduce agent symbolic learning, a systematic framework that enables language agents to optimize themselves on their own in a data-centric way using symbolic optimizers.
* I found that training loss is not stable in Figure 10. Is common in VML?

### Questions
Please see weakness

### Soundness
4

### Presentation
4

### Contribution
4
