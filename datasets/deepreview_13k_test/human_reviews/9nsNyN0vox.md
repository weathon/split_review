# Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
\vspace{-0.05cm}
Language models' (LMs) proficiency in handling deterministic symbolic reasoning and rule-based tasks remains limited due to their dependency implicit learning on textual data. To endow LMs with genuine rule comprehension abilities, we propose "Neural Comprehension" - a framework that synergistically integrates compiled neural networks (CoNNs) into the standard transformer architecture. CoNNs are neural modules designed to explicitly encode rules through artificially generated attention weights. By incorporating CoNN modules, the Neural Comprehension framework enables LMs to accurately and robustly execute rule-intensive symbolic tasks. Extensive experiments demonstrate the superiority of our approach over existing techniques in terms of length generalization, efficiency, and interpretability for symbolic operations. Furthermore, it can be applied to LMs across different model scales, outperforming tool-calling methods in arithmetic reasoning tasks while maintaining superior inference efficiency. Our work highlights the potential of seamlessly unifying explicit rule learning via CoNNs and implicit pattern learning in LMs, paving the way for true symbolic comprehension capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This paper proposes a new method called "Neural Comprehension" to enhance the symbolic reasoning capabilities of LLMs by integrating compiled neural networks (CoNNs), which are transformer-based networks with artificially designed attention weights to explicitly implement rules and transformations, thus can accurately perform symbolic computations.
- Neural Comprehension outperforms baselines like fine-tuning and few-shot learning on length generalization, and achieves near perfect accuracy on symbolic operations like parity, reverse, addition, and subtraction.

### Strengths
- The gating mechanism naturally incorporates CoNN into LLMs and allows gradient optimization for the whole network. This feature makes the proposed method different from the existing tool-use papers. 
- Near perfect accuracy on symbolic tasks, significant gains on arithmetic reasoning, compared to the regular LLMs like GPT-3/3.5, especially when the number of digits goes up.
- The proposed method results in less than 3% increase in the inference time, showing the potential to be applied to the existing models efficiently.

### Weaknesses
- Marginal performance improvement on real-world arithmetic reasoning tasks such as GSM8K. The result suggests that it may not be necessary for us to apply such neural compression into LLMs if the task is not related to strict symbolic operations.

### Questions
- In table 5 of appendix, it seems that you plug the neural comprehension into GPT-3. How did you achieve that when GPT-3 can only be accessed through APIs?
- Have you ever tried the [GSM-hard](https://huggingface.co/datasets/reasoning-machines/gsm-hard) dataset? [1] I think the proposed method is helpful for problems that have more digits. I expect that this method will be useful for GSM-hard as it is intended to includes more digits in the answers. Can you try experiments on it and compare the results with PAL?



[1] PAL: Program-aided Language Models. Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, Graham Neubig https://arxiv.org/abs/2211.10435

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the limitations of language models (LMs) in handling deterministic symbolic reasoning and rule-based tasks due to their implicit learning from textual data. To enhance their rule comprehension ability, the authors introduce "Neural Comprehension," which incorporates Compiled Neural Networks (CoNNs) into LMs. CoNNs are transformer-based neural networks that execute rules using artificially generated attention weights. This method enables LMs to effectively tackle rule-intensive challenges and improves their performance in symbolic reasoning tasks and real-world calculations.

### Strengths
1. The paper introduces a novel approach, "Neural Comprehension" by incorporating Compiled Neural Networks (CoNNs) into language models. This approach is highly original as it addresses the limitations of LMs in handling deterministic symbolic reasoning, offering an innovative solution that combines neural networks and explicitly coded, interpretable CoNNs;

2. The research methodology is well-founded, with empirical experiments showing superior performance compared to existing techniques. The study also includes a thorough analysis of combining multiple CoNNs, offering insights into model fusion. Besides, the AutoCoNN toolkit for automatic CoNN generation adds to the quality and scalability of the approach.

### Weaknesses
1. Even though the use of CoNNs to handle symbolic reasoning tasks is meticulously explained, the authors lack a well-structured explanation of "Neural Comprehension" and CoNNs, making it not very accessible to readers;

2. As I understand it, the authors need to generate a corresponding CoNN for each rule-based task (such as Parity, Reverse, Subtraction, and so on) and integrate it with the LM, is that correct? If so, this approach seems to lack generality.

### Questions
1. What does $I_{d_{L}}$ in Equation 1 mean? The author seems to have not provided an explanation. This seriously impedes my understanding of the crucial part of the proposed method;

2. What does "ICL" mean? Which term is the abbreviation for?

3. How are CoNNs compiled? How is the gradient $I_{d_{2}}$ for rule-based in Equation 2 obtained? Does it involve first training a specific task's CoNNs and then extracting the rule-based gradient, which is merged with the LM's gradient to influence the final gradient? If so, how are CoNNs trained? What is the training dataset like?

4. From all the equations, I haven't seen an explanation of how the LM-based gradient and Rule-based gradient are combined. I feel very confused about this and need a more detailed explanation from the authors.

Typos:

1. ’=’  ->  ‘=’，  ’Select’  ->  ‘Select’

2. “Neuralresulting”

3. As depicted in Figure 5.4  ->  As depicted in Figure 7

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces Neural Comprehension, a method for combining language models with compiled neural networks (CoNNs) which allow explicit rules to be encoded as transformers. CoNNs can generalize more effectively on symbolic problems, but do not have the linguistic flexibility of LMs. My understanding is that Neural Comprehension works "similar to MoE" (mixture of experts), in that the token at a given position is decoded either by the LM or by a CoNN, depending on whether explicit reasoning is needed. The authors demonstrate that Neural Comprehension indeed generalizes better than a pure LM, especially for problems that might have very long length (e.g Figure 4).

### Strengths
- LMs often do not generalize well in symbolic reasoning problems, so finding ways to improve this is very important
- experiments are quite extensive
- Neural Comprehension seems to work reasonably well on many of the tasks the authors look at

### Weaknesses
- Presentation is overall quite hard to follow. Authors should correct me if I misinterpret any parts of the method below
- It is not clear when aspects of CoNNs are learned or if they are just compiled as fully operational symbolic functions. Gradients are mentioned, but the authors do not elaborate on exactly what these apply to
- The combination of CoNNs and LMs seems quite simplistic here based on Figure 3 and section 4.1. For example, it seems that Neural Comprehension takes the output of the Addition CoNN when encountering '='. It is not clear whether there is a more sophisticated process used to decide when to apply CoNNs. If not, why is using CoNNs better than simply using external tools? 
- In a similar vein, it would strengthen the results to also compare to networks which use external tools. The authors frame the work in contrast to that, but it is not clear how those methods would compare

### Questions
See weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method called "Neural Comprehension" to augment language models with the ability to perform symbolic reasoning and operations more robustly. The key idea is to incorporate compiled neural networks (CoNNs) that encode rules explicitly into the language model architecture.

The authors argue that standard language models struggle with symbolic tasks like arithmetic due to relying on statistical patterns learned implicitly from data. In contrast, CoNNs directly compile rules like addition into neural network modules using specialized attention weights. By integrating CoNNs in a plug-and-play manner, language models can leverage both their natural language understanding and the symbolic reasoning of CoNNs.

The proposed Neural Comprehension framework uses a gating mechanism to determine when to invoke a CoNN module versus the original language model decoder. Experiments on symbolic operations and arithmetic tasks demonstrate substantially improved performance over baseline methods.

### Strengths
(1) Proposes a novel way to impart symbolic reasoning abilities in language models using CoNNs. Addresses a clear limitation of standard LMs.

(2) Achieves strong performance improvements on multiple symbolic and arithmetic datasets over baselines. Shows the benefit of combining statistical and symbolic knowledge.

(3) CoNN integration does not require tool APIs. Comparable to tool-based methods while being end-to-end differentiable and not needing code generation.

(4) Reasoning process is more interpretable compared to black-box LM predictions. Outputs show step-by-step reasoning.

### Weaknesses
(1) CoNN design and integration could be non-trivial for more complex reasoning tasks, e.g. compositional arithmetic reasoning tasks. Gating mechanism may work fine if we just want to add one skill. However, it will be hard to scale to thousands of skills for a specific language model and this exploration remains limited. Developing a specific model for a specific task involves significant human efforts and we want to build a model that can have multiple skills.

(2) Although this paper claims it does not require tool API, in my opinion, this is not free and has very large costs. If a calculator is there, I think we should use it instead of building neural networks mimicking these tools. API is also required for internet-based retrieval and data analysis (OpenAI Code Interpreter ), etc. I think adding a python api is simpler than adding a neural module.

(3) Experimental results shown in Table 5 on real-world reasoning tasks, e.g. GSM8K, are similar to baselines without significant improvements.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
