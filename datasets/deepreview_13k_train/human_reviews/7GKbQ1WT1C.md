# Prompting Fairness: Integrating Causality to Debias Large Language Models

- Decision: Accept
- Scores: 6, 3, 6, 6

## Abstract
Large language models (LLMs), despite their remarkable capabilities, are susceptible to generating biased and discriminatory responses. As LLMs increasingly influence high-stakes decision-making (e.g., hiring and healthcare), mitigating these biases becomes critical. In this work, we propose a causality-guided debiasing framework to tackle social biases, aiming to reduce the harmful dependence between LLMs' decisions and the social information in the input. Our framework introduces a novel perspective to identify how social information can affect an LLM's decision through different causal pathways. Leveraging these causal insights, we outline principled prompting strategies that regulate these pathways through selection mechanisms. This framework not only unifies existing prompting-based debiasing techniques but also opens up new directions for reducing bias by encouraging the model to prioritize fact-based reasoning over reliance on biased social cues. We validate our framework through extensive experiments on real-world datasets across multiple domains, demonstrating its effectiveness in debiasing LLM decisions, even with only black-box access to the model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a prompt-based method to remove biases in a language model's output. It motivates the prompts using the idea of selection bias from causal inference literature. Experiments show a significant reduction in measured bias on two datasets.

### Strengths
* Theoretical justification of prompting strategies using a stylized selection bias argument
* Significant reduction of bias in demonstrated experiments.

### Weaknesses
 * The connection of selection bias, causal graph and the proposed prompt is weak. In one dataset, strategy I and II is used. In the other dataset, strategy I and III. So it is not clear that the set of selection biases listed are exhaustive. Rather, it appears that the list of such selection biases may increase as the datasets increase, and so the current selection biases presented are the union of those that were useful for prompts for these two data sets.
* Ablations are not provided. What happens when all strategies are used for first dataset, and what happens when strategy I and II is used for second dataset?
* Other methods of removing bias are not compared. Since the final solution is just a prompting change, there can be other ways of prompting the LLM that are simple to implement. For example, the text "avoid any gender bias while answering the question" can be added to the prompt.  
* Strategy I seems the most useful. However, I have two concerns. First, it may be computationally intensive. Can the authors clarify how many calls would it need to answer a single question? If I understand correctly, there will be one call to create the two possible scenarios for the base question, and then there will be one call to decide which of them is more plausible, and then a final call to actually answer the question? So there are going to be three calls per question? If that's the case, I can think of other methods, for example, the React multi-agent framework, where the LLM is asked to respond to the question first, then there is a critique agent that checks whether there is any bias in the answer, and if yes, it asks the LLM to regenerate the answer giving the feedback from the critique as a part of the prompt. Second concern is that the creation of the base question, while could be templated for simple examples like the one shown in the paper, but eventually will also become a task that an LLM will need to do so, are there ways to use a smaller model or something more efficient for this?

### Questions
I have mixed opinions about this paper. On the one hand, I appreciate the selection bias analogy and the abstraction of the problem to a causal graph and the conclusions that come from it. On the other hand, the final solution proposed is just an ensemble of intuitive prompts, and it is not clear to me that these prompts are meaningfully guided by the selection bias theory. And it is not clear to me that other better prompts could not have been obtained without any selection bias theorization. So my questions to the authors are :
1. Can you show that avoiding bias based on selection bias is better than simply asking the LLM to avoid bias? See one suggestion of a modified prompt in the weaknesses above. I guess the literature on debiasing LLMs may have more simple prompt additions or system prompts that can be added.  In your comparison, also consider the computational cost of your proposed method.
2. How does the selection bias theory help in choosing the correct strategy, and later, the prompt? What was the justification for using strategy II in one case and strategy III in another? 
3. How would Strategy I generalize to more complex bias scenarios? Do you need an LLM for creating the base prompt in that case? Many cases of biases may not be simple template pronoun substitutions.
4. Strategy I seems closest to a variant of in-context-learning where the closest example is chosen so to help the LLM answer the question correctly. Can you compare to a baseline that selects the K nearest in context examples to add to the prompt, rather than a fixed set of in context examples?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses responsive bias in both open-source and proprietary LLMs by formulating a theoretical debiasing framework that analyzes the impact of social information on an LLM's decisions from a novel causal perspective. The framework identifies causal pathways through which social information influences model outputs and develops the integrated inference-time prompting strategies to accordingly regulate information flow across different pathways, thereby suppressing potential social bias. Extensive experiments on real-world datasets across multiple domains validate the framework, demonstrating its effectiveness in debiasing LLM decisions.

### Strengths
1. This paper provides a detailed analysis of the internal mechanisms behind biased decision-making in LLMs from a causal perspective, offering a theoretical understanding for the proposed prompting-based debiasing methods.
2. The Introduction section is well-written and effectively conveys the existing challenges.
3. Extensive experiments demonstrate that the proposed DDP significantly outperforms other baseline methods.

### Weaknesses
1. The proposed DDP suffers from poor applicability for general-purpose generation: DDP is a prompting-based technique that relies on adding extra textual guidance into  the prompt context to achieve debiasing. For evaluation, DDP needs dataset-specific design to obtain its corresponding textual guidance, thereby adapting to different evaluation datasets. So DDP can not be applied to free-form generation, especially when social attributes of interest are not directly given in input prompt but emerge as the intermediate generated results of LLMs, limiting its further applicability in more critical scenarios.
2. The paper organization is unclear and redundant: the pre-trained data generating process is not necessary for understanding the main contributions of this paper. The theoretical insights (strategies) are coupled together with the technical details, making it hard to fully and clearly assess the technical contributions after reading Section 3.
3. Prompting-based debiasing approaches have limitations and may not be particularly meaningful. Traditionally, the responsibility for model alignment and debiasing lies with model deployers. Implementing prompting-based debiasing can be unsafe and inevitably introduces additional time costs.
4. The textual guidance introduced by DDP may introduce noise that hinders the reasoning abilities of LLMs. As shown in Table 1-Type II, while DDP reduces the bias gap, it significantly degrades performance in terms of Anti and Pro (on GPT-3/3.5 and Claude 2). Therefore, their robustness remains an unsolved problem.

### Questions
1. Does the 'default' in Table 2 refer to the same meaning as the 'default' in Table 1, which solely receives the original question as input? If so, why does this method also include the metrics (TT, TF, FT, FF)?
2. See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a causality-guided framework for debiasing large language models through prompting strategies. The authors introduce a novel perspective to identify how social information influences LLM decisions through different causal pathways and develop principled prompting strategies to regulate these pathways through selection mechanisms. The framework encompasses two main approaches: encouraging fact-based reasoning and discouraging biased reasoning. The authors validate their framework through extensive experiments on multiple benchmark datasets (WinoBias, BBQ, and Discrim-Eval) across various social dimensions, demonstrating its effectiveness in debiasing LLM decisions while maintaining strong performance.

### Strengths
This work presents a novel theoretical framework that bridges causality and LLM debiasing, providing clear intuitions and principled strategies for addressing bias. The causal modeling of both training data generation and LLM reasoning processes offers valuable insights into bias sources and mitigation approaches.

### Weaknesses
Although the authors demonstrate improved performance across multiple models, there's limited discussion of how the effectiveness of their approach might vary with model scale or architecture. Additionally, while the authors show reduced bias metrics, there could be more analysis of potential trade-offs between bias reduction and task performance.

### Questions
How does the effectiveness of the proposed debiasing strategies vary with model size and architecture?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This article conducted a causality analysis for bias in LLM's decision and provided a prompting-based solution for bias mitigation. The solution included three strategy pathways and demonstrated that the combining strategy can achieve comprehensive debiasing.

### Strengths
The given causality-analysis clarified the origins of bias in well-trained LLMs, making the proposed bias mitigation strategies more explainable. 

In addition to examining the influence of training data corpus and prompts, the authors also considered bias caused by data selection, offering a more systematic and comprehensive bias-mitigation solution.

### Weaknesses
1. The assumption in A.3 CAUSALITY AND LLMS, 
"We adopt a rather mild assumption that a well-trained and well-aligned LLM captures the dependence pattern in the training data and that such a pattern is internalized and utilized during reasoning" 
needs to be put in the main text. If LLMs are not well-trained and well-aligned, then the author's prompting-based de-dependency method will no longer be so effective, so I think this is an assumption worth stating in the main text.

2. There is a lack of discussion related to other prompting-based debiasing methods in LLMs, such as those in [1][2][3].


### Questions
1. When the three strategies are combined, both social-salient text representation and social-agnostic fact
representation are independent of social category
representation. Does this mean that it is equivalent to using only prompts Q:{Base Question}, a prompt that is completely unrelated to sensitive features, to let LLM complete the answer to Original Question? If not, when both social-salient text representation and social-agnostic fact
representation are independent of social category
representation, what is the performance difference of LLM decision brought by prompts Q:{Base Question} and Q:{Given that your answer to {Base Question} is {Answer to Base Question}, Assume male and female are equally represented in drivers and in teachers. Do not answer the question using gender information. {Original Question}}? Can the author give experimental results on this point?
2. Should there be a solid line in Figure 3 connecting prompt to LLM potential decision?
3. In addition to the fact that prompting-based techniques are suitable for dealing with black-box scenarios, can the authors add a discussion on the advantages and limitations of prompting-based techniques compared to direct fine-tuning of model parameters and prompting-based techniques, for example, a limitation of  prompting-based technique ——the need for human users to be proactive and knowledgeable to complete debiasing?
4. Can the authors provide a comparison of this work with other prompting-based debiasing methods mentioned in weakness, either experimentally or analytically?
5. In the Table 2, why the sum of the true-rate (42.33%, 32.02%) and false-rate (8.68%, 8.82%) of the base question under GPT-3.5/Counteract Only/Anti case is not 1?

### Soundness
3

### Presentation
3

### Contribution
3
