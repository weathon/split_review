# TypedThinker: Typed Thinking Improves Large Language Model Reasoning

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Despite significant advancements in the reasoning capabilities of Large Language Models (LLMs), the lack of diverse reasoning solutions often makes them trapped in a limited solution search area. 
In this paper, we propose \method, a reasoning framework that diversifies LLMs' reasoning solutions by incorporating multiple reasoning types (deductive, inductive, abductive, and analogical). Our analysis across four benchmarks reveals that different reasoning types uniquely solve distinct sets of problems, highlighting the importance of diverse thinking approaches. \method addresses two key challenges: selecting appropriate reasoning types for given problems and effectively implementing specific reasoning types. 
Through self-training on successful experiences, \method learns an implicit policy for reasoning type selection and application. Experimental results demonstrate significant improvements over baseline models, with accuracy increases of 3.4\% for Mistral 7B and 16.7\% for LLaMA3 8B across four reasoning benchmarks. Notably, \method shows effective generalization to new benchmarks and can further enhance the reasoning capability of powerful models like GPT-4o.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a novel framework, *TypedThinker*, designed to improve the problem-solving abilities of LLMsimplementing that reasoning type effectively. by integrating multiple types of reasoning, including deductive, inductive, abductive, and analogical. It addresses two core challenges: 1) choosing the best reasoning type for a given problem and 2) implementing that reasoning type effectively. Using a meta-thinker to select the reasoning type and a reasoner to execute it, TypedThinker can improve accuracy from baseline: by 3.4% for Mistral 7B and 16.7% for LLaMA3 8B on logical and mathematical tasks.

### Strengths
- S1. The approach to incorporate multiple reasoning types (deductive, inductive, abductive, and analogical) into consideration for a meta-thinker for LLM reasoning is novel and seems like a generalizable approach for most LLMs.
- S2. There were clear quantitative gains for this approach.
- S3. TypedThinker’s ability to generalize to unseen benchmarks is a strength particularly in regards to generalization.
- S4. The experiments on the two models were very thorough, with various components of the framework ablated (e.g. w/o meta-thinker, w/o finetuning, w/o memory on 4 benchmarks)

### Weaknesses
 - W1. Accuracy improvement of 3.4% on Mistral 7B seems rather minimal, though improvements on LLaMA3 was quite notable. Since there were such varied performance improvements, it would have been more beneficial to have more models to convincingly validate the findings on this paper.
- W2. The individual methods in this paper does not seem novel enough, as strategies for the individual types of reasoning were studied in numerous work (e.g. https://arxiv.org/pdf/2309.05660 for inductive reasoning). However, I do believe that the overall framework has strong potential and is novel by ensembling these existing strategies and methods for prediction. Since there are existing methods for each of these types, it would have been very effective to compare these existing methods with this framework. This could be possibly used to measure effectiveness for/against existing methodologies, and would have made this work a lot more relevant and connected with existing work.
- W3. While overall performance gain with a unified meta-thinker is a gain, I wonder you could have compared this with a baseline, e.g. if there is a significant difference with simply prompting the model to simultaneously state and explore all these reasoning type for final prediction. If there is not a significant performance gain with respect to this baseline, this seems like an overly contrived framework for marginal gains. If there is a significant performance gain, this work would certainly be more convincing, particularly with regards to needing to differentiate reasoning type for precise prediction rather than having inappropriate mixtures.
- W4. While it is encouraging to see that there were improvements on a rather new dataset probably outside pretraining, I do not think an experiment on a single dataset on 1 task is evidence enough to claim generalization.

### Questions
- Q1. Figure 1 shows the percentage distribution of each reasoning types. How was this annotated? Did the dataset come with these groundtruth labels for type of reasoning required?
- Q2. Have you considered other models? Especially since there are new models that explore reasoning in-depth, e.g. GPT-o1, it would be interesting to see if this results hold for those reasoning optimized models.
- Q3. This was primarily done with logical reasoning and math. Is there a particular reason for picking those domains? I wonder if this strategy would be more effective with reasoning domains with more ambiguity e.g. natural language reasoning. Though, I can also understand that those domains may be difficult to experiment with/validate due to the nature of NL.

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
The paper proposes to solve reasoning by a two-step process. First, select a reasoning type from deductive, inductive, abductive and analogical reasoning. This selector is finetuned. Then historical success cases of the selected reasoning type are retrieved from the memory. These retrieved examples along with the selected reasoning type are used to solve the reasoning problem. The paper conducted experiments on Mistral 7B, LLaMDA 3 8B, GPT-4o and MetaMath, on benchmarks such as BBH, GSM8K, MATH etc.

### Strengths
1. The paper is well written and easy to follow.
2. The experiments conducted are very thorough to get a whole picture of the impact of each component.
3. It is clearly motivated that diversity is important for superior reasoning performance in LLMs.

### Weaknesses
1. The paper lacks novelty: the idea of introducing different thinking types is not new at all. For example, Meta-Prompting [1] introduced the concept of applying different experts to solve different tasks. Self-Discover [2] proposed to select and compose different reasoning modules to customize the solving of each reasoning task.
2. The fundamental assumption of matching each task into one of the 4 reasoning types is flawed. There are many ways of solving reasoning beyond the 4 reasoning types. In addition, each task could involve several different reasoning types at different steps.
3. The proposed method is unnecessarily complex with a fine-tuned reasoner, a meta thinker and a memory.
4. Despite the cost of fine tuning a reasoner, the gain compared to Few-shot methods is not impressive at all and doesn’t seem to justify the complexity of the pipeline. For example, on Mistral 8B, the average gain on 4 tasks from Few-shot SC@5 is only 3.4% (Table 1). There is almost no gain at all when TypedThinker is applied to GPT-4o (Table 5) and MetaMath (Table 6).
5. It is not fair to compare TypedThinker against few-shot methods, since TypedThinker involves fine tuning. Instead, it should be compared against methods such as OPRO [3].

### Questions
Overall, the basic assumption of choosing one reasoning type from 4 is flawed. The fact that there is almost no gain at all for strong models such as GPT-4o reflects the method is not touching the core of how to improve LLM's reasoning ability.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents TypedThinker, a framework that improves LLMs problem-solving ability by integrating multiple reasoning types—deductive, inductive, abductive, and analogical. The authors do this by using a meta-thinker for selecting appropriate reasoning types and a reasoner for execution. Several experimental results demonstrate accuracy improvements over baseline models across various logical and mathematical benchmarks.

### Strengths
- The framework is clearly explained and the paper is easy to follow
- Improved accuracy by leveraging different and multiple types of reasoning allowing the models to approach the problem with a better suited strategy and different cognitive point of view
- The novelty of the proposed method is a good contribution of the paper which may significantly improve LM's reasoning ability for some tasks.

### Weaknesses
 - Scalability and resource requirement due to the maintenance of the memory buffer could increase computational cost.
- TypedThinker depends on self-training and experience retrieval. How generalizable is the learned experience to other different domains? In sect. 4.5 the authors discuss applicability of typedThinker to ContextHub however this remains a collection of problems for logical reasoning. There is no issue with the proposed framework to be suited only for mathematical and logical reasoning, but then this needs to be specified.

### Questions
- Can this method be applied to other types of reasoning (symbolic, commonsense etc)?
- How quickly can this approach adapt to an unseen task? Would one or two examples from new task be enough to achieve reasonable accuracy? It would be great to give some analysis to the adaptability and continual learning ability of the proposed approach.

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
4

### Summary
This paper proposed a novel TypedThinker to incorporate four diverse reasoning types and enhance LLMs' problem-solving abilities. The proposed framework first selected appropriate reasoning types for given problems with a fine-tuned meta-thinker module, and then conducted the selected type of reasoning with a fine-tuned reasoner module and retrieved experiences as few-shot examples. The authors conducted extensive experiments and demonstrated the effectiveness and generalization of the proposed method.

### Strengths
1. The idea of different reasoning types in problem-solving is novel and inspiring.
2. The authors conducted sufficient data analysis to support the necessity of applying different reasoning types.
3. The authors conducted extensive experiments and in-depth analysis of the proposed method to demonstrate its effectiveness.

### Weaknesses
1. Although the idea of the paper is novel, the technical contribution seems to be limited. The authors seem to simply fine-tune a model to select the reasoning type and use it to search the examples and specify the prompt.
2. Some technical details may be misleading. For example, the memory usually refers to data buffers frequently updated in inference, but in this paper it is updated during training and fixed in inference. It would be better to clarify more clearly. Besides, some details used in training and inference are mixed such as the accuracy measurement and memory storage, which makes it somewhat confusing. It would be better to clarify the framework from the input to the output for training and inference.

### Questions
See the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
