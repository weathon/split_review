# Large Language Models are Interpretable Learners

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
The trade-off between expressiveness and interpretability remains a core challenge when building human-centric predictive models for classification and decision-making. While symbolic rules offer interpretability, they often lack expressiveness, whereas neural networks excel in performance but are known for being black boxes. In this paper, we show a combination of Large Language Models (LLMs) and symbolic programs can bridge this gap. In the proposed LLM-based Symbolic Programs (LSPs), the pretrained LLM with natural language prompts provides a massive set of interpretable modules that can transform raw input into natural language concepts. Symbolic programs then integrate these modules into an interpretable decision rule. To train LSPs, we develop a divide-and-conquer approach to incrementally build the program from scratch, where the learning process of each step is guided by LLMs. To evaluate the effectiveness of LSPs in extracting interpretable and accurate knowledge from data, we introduce IL-Bench, a collection of diverse tasks, including both synthetic and real-world scenarios across different modalities. Empirical results demonstrate LSP's superior performance compared to traditional neurosymbolic programs and vanilla automatic prompt tuning methods. Moreover, as the knowledge learned by LSP is a combination of natural language descriptions and symbolic rules, it is easily transferable to humans (interpretable), and other LLMs, and generalizes well to out-of-distribution samples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new framwork, named LSP, for LLM-Symbolic Program combining LLMs with Neurosymbolic programs (NSPs). The main idea of the paper is to consider a prompted LLM as an interpretable unit, enabling the use of NSPs with a minimal domain specific language and thus narrowing this important bottleneck of NSPs. The approach is demonstrated on a proposed Interpretable-Learning benchmark. It includes a comparison with SOTA NSPs as well as some ablation study on the components of the approach. It also include an human evaluation protocol to access the interpretability of the approach.

### Strengths
The main strengths of the paper are :
+ **Clarity** : the paper is well written with a clear and well motivated idea. The paper provides nice illustration that enable a clear understanding of the proposed approach. The addressed research question are also very clear.  Moreover, a thorough description of the proposed framework, including ablation studies and code for reproducibility is provided.
+ **Originality** : the main originality of the paper is to use prompting and the ability of summarization of LLMs, a method named RuleSum, to obtain concrete rules and to prevent from manually designing operators, one of the bottleneck of NSPs. It is a simple approach but opening the way for LLM-based symbolic programs. The IL-bench is also an interesting contribution of the paper.
+ **Quality** : The paper is of sufficient quality for the ICLR conference standard.
+ **Significance** : the paper propose a new approach for interpretable learning, i.e. interpretable and comprehensible decision making process which an important area for XAI and trust in AI.

### Weaknesses
While the core idea is interesting, the paper has several limitations:
+ a first small concerns is about the title of the paper which is for me not really aligned on the content. The authors use LLMs as learnable building blocks for NSPs but are not interpretable as their own. The title of the paper should be slightly changed to better reflect the true claims of the paper.
+ **lack of clear definition of the notion of interpretability and of the underlying assumptions** : as the authors tackle the trade-off between expressiveness and interpretability, a clear definition of them should be given. For instance for me, using a minimalist DSL means less expressivity since there are only two operators. The assumption that relying on natural language brings interpretability should also be discussed. The interpretability seems to be linked to the interpretability of the prompts.
+ a better positioning to recent approach on XAI, in particular concept-based XAI, mentioned in appendix A.1 and Mechanistic Interpretability.
+ **Generality of the findings**  : the IL-Bench should be more motivated. It is not clear for me what a symbolic task is exactly. Moreover, a large part of the task are classification tasks. What about other tasks regarding the proposed approach ?
+ What is $Dist$ in equation 1 ?

### Questions
Some questions are in the Weaknesses section.
Other questions :
+ Could the following claim could be discussed : the resulting model is inherently interpretable as the prompt s is expressed in natural language ? 
+ How this idea of using LLMs to transforms signals into high-level concepts, how the approach compared to concept induction approach ? To  Concept-based Explanations for LLMs ? 
+ In the following approach, is the decision making process limited to conditional branching and tree-based models ? Is it a strong limitation ? 
+ Can hallucinations can occur for RuleSum ?

### Soundness
3

### Presentation
3

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
The authors in this paper introduce LLM-based Symbolic Programs (LSPs), combining Large Language Models with symbolic programming to create predictive models that balance expressiveness and interpretability. LSPs use LLMs to generate interpretable modules from raw data. With a step-by-step program generation algorithm, the proposed method could generate the symbolic programs. Besides, the authors propose a new benchmark, called IL-Bench, for evaluating interpretable learning tasks. In their evaluation, LSPs outperform traditional methods, offering interpretable, transferable, and generalizable results.

### Strengths
1. A new benchmark for interpretable learning tasks, for both vision and text scenarios.
2. Design a LLM-symbolic program generation algorithm (called LSP by authors) by a program structure search procedure.
3. Evaluation shows that the LSP significantly outperforms the baselines in the authors' evaluation settings.

### Weaknesses
1. As the authors say, LLM's responsibility is to make decisions in each LLM module in their llm-symbolic programs. Thus, generating a correct LSP relies on the LLM's ability. I am curious whether the proposed method could correspond with other open-source LLMs that could be deployed locally.


### Questions
Referring to W1, the author may run an additional evaluation of the proposed method with specific open-source LLMs (e.g. LlaMA3.1-8B, LlaMA3.2) that can be run locally. No matter the results, the authors could discuss some potential limitations to making LSP work with locally deployed LLMs.

The authors claim that the existing LLM benchmark could measure (M)LLM’s IL ability: "all these tasks are all zero-shot solvable, allowing LLMs to make predictions without additional rule learning. Therefore, these benchmarks are unsuitable for evaluating IL tasks."
My other questions are:

1. Are datasets from AIPS or/and AlphaGeometry, which contains IMO level mathematical problems, able to be IL benchmark? 
The authors may discuss the difference between the proposed dataset and the datasets like AIPS or AlphaGeometry in terms of measuring interpretable learning ability.

FYI, AIPS aims to address inequality math problems, and AlphaGeometry aims to address geometrical math problems. Both papers propose a dataset and a problem-solving algorithm. From my point of view, the algorithm is a neural-symbolic method and is similar to LSP, which uses LLM as a module to generate a one-step decision, add a construct for geometry problems, and transform an inequality. Then, designing a high-level search problem to solve the complex problem.

2. Instead of constructing LSP, does SFT or some RL could be applied to LLM to improve the LLM's IL ability?

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
2

### Summary
This paper tackles the challenge of balancing expressiveness and interpretability in predictive models for classification and decision-making. The authors propose LLM-based Symbolic Programs (LSPs) that combine Large Language Models with symbolic programs to bridge this gap. LLMs generate interpretable modules that transform raw inputs into natural language concepts, which are then integrated into decision rules by symbolic programs.
Moreover, the paper proposes IL-Bench, a new benchmark for the interpretable learning capabilities of LLMs. In experiments, it is demonstrated that LSPs outperform traditional neurosymbolic programs and prompt tuning methods on the proposed benchmark.

### Strengths
The approach to integrating LLMs into DSL-based neuro-symbolic programming approaches is interesting, although the idea itself may be straightforward. 
By combining Large Language Models (LLMs) with symbolic programs, the authors effectively leverage the strengths of both methods: LLMs for creating interpretable natural language concepts and symbolic programs for incorporating these into decision rules. This hybrid approach not only enhances model interpretability without sacrificing performance but also makes the knowledge easily transferable to humans and adaptable for other LLMs.
Limitations are discussed in an explicit section.
In experiments, the proposed approach outperformed established baselines in multiple aspects, e.g., on OOD examples, expressiveness, and interpretability (transferability).

### Weaknesses
I found the manuscript somewhat challenging to follow due to the absence of consistent examples within the main text. Currently, major examples are relegated to the supplementary materials. To enhance clarity, I recommend incorporating one or two examples directly into the main manuscript and referencing them throughout.

Moreover, a clear problem statement would significantly improve comprehension. Specifically, outlining the input and output parameters before discussing the methodology would be beneficial.

Apart from these presentation issues, the experiments appear to demonstrate the efficacy of the proposed approach. However, as I feel I lack sufficient expertise in the baselines, I will defer to other reviewers for a critical assessment of the significance of these results.

Minor Points:

The structure of the document feels somewhat convoluted. There is an overuse of emphasized text formats (bold, italic, etc.), particularly noticeable on Page 3, which detracts from the core ideas being presented. I recommend retaining emphasis only on the most critical sections and reducing the use of bold and italic text.

Equation 3 could be better explained with a figure that includes a concrete example and details like $\alpha$ and $y_i$.

The text size in Figure 8 (f) makes it difficult to interpret. Consider increasing the text size for better readability.

Furthermore, the code is not submitted, making it challenging to assess reproducibility.

### Questions
I was not fully following the reasoning in line 268 -- 286.
Could you elaborate the following two arguments?
> Therefore, with a fixed LLM, the set of natural language prompts, ... provides a massive set of interpretable neural network modules for the task.

Why the prompts can be trivially seen as interpretable neural modules?

> ... the resulting model is inherently interpretable, as the prompt s is expressed in natural language.

Why the resulting model can be seen inherently interpretable?

### Soundness
3

### Presentation
2

### Contribution
3
