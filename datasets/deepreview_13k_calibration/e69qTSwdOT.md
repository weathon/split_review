# Exploring the Discriminative Capability of LLMs in In-context Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
_In-context learning_ (ICL), as an emergent behavior of large language models (LLMs), has exhibited impressive capability in solving previously unseen tasks based on the observations of the given samples without extra training. However, recent works find that LLMs irregularly obtain unexpected fragmented decision boundaries in simple discriminative tasks, such as binary linear classification. Our observations on the output of Llama-3-8B for the reasoning process of label predictions reveal that LLMs tend to leverage the existing machine learning algorithms to perform discriminative tasks. Specifically, LLMs tend first to select a strategy for the given task and then predict the labels of query data by executing the selected strategy. Based on the observation, in this paper, we propose to dive into such a behavior of LLMs for a deeper understanding of the discriminative capability of LLMs. We conduct a series of analyses on Llama-3-8B to determine the behaviors adopted by LLMs in the discriminative tasks, including probing the label predictions of query data and the corresponding confidence of LLMs under different prompt settings. Moreover, we also probe the preference of LLMs for strategy selection and then simulate the behavior of LLMs performing classification based on obtained preference. The analysis and simulation results provide some important observations and insights into the properties of LLMs in performing discriminative tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores how Llama-3-8B performs in a linear classification task, suggesting that the model employs a two-step paradigm involving the selection and application of various machine learning and statistical methods. The authors attempt to investigate this aspect by prompting the model either to just write the answer or to base the answer on “the running results of [some machine learning] algorithm/model”. Furthermore, they study the decision boundaries obtained from the classification by Llama-3-8B as well as classic ML algorithms and assess self-reported confidence of Llama-3-8B in prediction of labels. Lastly, the authors seek to simulate the model’s classification behavior by randomly sampling a machine learning method for each query.

### Strengths
The underlying topic of the presented work – how LLMs perform some algorithmic computations – is indeed interesting and worth of further investigations.

The presentation is rather good.

### Weaknesses
The paper is based on a strong hypothesis (which is also the first claimed contribution) that “LLMs tend to perform discriminative tasks in a two-step paradigm, where LLMs first randomly sample a strategy for the query data point and then predict the label based on the execution of the selected strategy on the given in-context samples”. This claim is unclear, misleading, and not well-grounded.

(1) The claim is unclear because LLM have no will or aspiration (as something which is not a subject) and thus cannot “tent” to do something. They either do or not. I would not use term “tend” as not technical enough.

(2) If the claim means that live calculations in the layers of LLM somehow simulate the two-stage process, this claim is not grounded. In fact, all arguments in Section 3 and Section D are based on what Llama-3-8B says itself on this question in several answers to some prompt, which is not given in the paper (!). Obviously, unvalidated answers of LLMs cannot be directly treated as scientific findings. Still, I can provide my own experiment on what LLMs can reason about their own abilities. Unlike the authors, I will share my prompt in the following dialog with ChatGPT 4o mini:  

Me:
“It is known that you, ChatGPT, while process my queries, cannot communicate with Internet, cannot query different applications and resources, cannot receive additional information and results of calculations from outsource tools such as python libraries. Does it limit you? Do you suffer from the absence of such opportunities that humans have? For example, imagine you are given a set of pairs of numbers and their labels, and was asked to predict the label for a new input pair of numbers based on the provided data. This is a standard machine learning problem. How can you solve it without access to external tools, which human data scientists successfully apply?”

ChatGPT:
“You're absolutely right in pointing out that I don't have access to the internet or external tools such as Python libraries for tasks like running machine learning models or doing live computations. While this limits my ability to directly execute code or retrieve real-time information, I can still provide insights and walk through the steps of how a human data scientist might approach solving a problem — including tasks like building a predictive model — by drawing on the knowledge I've been trained on.
So, to your question, do I "suffer" from not having access to these tools? In a way, yes, in the sense that I'm unable to perform live calculations, make real-time predictions, or validate models dynamically. But I’m not “suffering” in a conventional sense — my role is more about guiding you through the process, explaining concepts, and helping you understand how to solve problems, which is an essential part of data science itself.
Let me break this down further in the context of your example:
…”

As we can see, ChatGPT “thinks” that (1) it is unable to directly run ML tools, (2) its role is different: to provide guidance to humans rather than to solve ML tasks itself.

There are other unsubstantiated claims about LLM’s decision behavior. For instance, in line 234, the authors state:
>"Moreover, our further quantitative results indicate that the decision behavior of the LLM, where the learning strategies are specialized in prompts, resembles that of MLP"
Yet, the authors do not cite specific results to support this claim. Although they may be referring to Table 1, I do not think that the differences in predictions that are shown there can tell us anything about the actual decision behavior as the authors suggest; instead, these results simply indicate a superficial similarity between the output values of the LLM and an MLP

Lines 179-182:
>”The example reasoning output above implies two important aspects of how LLMs perform classification tasks. On the one hand, LLMs tend to resort to existing mathematical methods (e.g., machine learning algorithms) to infer the labels of query data. On the other hand, LLMs tend to generate the predictions of labels based on the execution of the selected algorithm."
I do not concur that the model's reasoning output provided in the paper is sufficient to jump to such conclusions.

As authors acknowledge themselves, “Hallucination also takes place" (when discussing the model's incorrect reference to class imbalance in Appendix D). These “hallucinations” suggests that the model can merely rephrasing some texts about machine learning instead of truly executing the computational steps of ML algorithms.

Keeping the above comments in mind, the investigations into the quantitative differences in decision boundaries do not provide a strong enough basis for the claims about the LLM's actual implementation of ML algorithms.

There are also some minor oversights:
- Line 50: "LLMs *irregularly* obtain unexpected fragmented decision boundaries”. Meaning of 'irregularly' is unclear in this context. One might assume it means that some runs with LLMs produce fragmented boundaries, and some runs don't, but this would contradict the data presented in the paper.
- What motivated authors to uniformly divide each dimension into $N_g$ coordinates? (Line 124). The workshop paper that authors refer to, Zhao et. al (2024), does not seem to provide any motivation behind this as well. An explanation of this choice would add clarity.
- In the main-text Section 6 that describes the related work, the references to (Shi et al., 2023; Xiao et al., 2024) appear out of context. Although these works are elaborated on in Appendix A, it would be better to address them directly in the main text, including a brief explanation of how the ideas they explore differ from the authors' work.

### Questions
Questions:

1. Could you clarify what you mean by the LLM “using” or “leveraging” machine learning methods? Specifically, what criteria are you using to identify when the LLM is actively implementing these algorithms versus merely describing them?
2. Could you elaborate on the “two-step paradigm” hypothesis? What evidence or examples in the paper directly support this framework as applied to LLMs in a classification setting?
3. What specific evidence supports the claim that the LLM’s decision behavior resembles that of an MLP (Line 234)? Is this comparison based solely on the output values shown in Table 1, or do you have additional insights into the decision processes?
4. Could you clarify the rationale behind the model's self-reported confidence in Sections 4.1 and 4.2? Why is this measure considered valid in evaluating the LLM’s decision process?
5. What motivated the choice to uniformly divide each dimension into $N_g$ coordinates (Line 124)?
6. Why randomly sampling ML algorithms is justified as a means of simulating LLM classification behavior?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to explore the operational mechanisms behind the in-context learning (ICL) capabilities of large language models (LLMs) in discriminative and classification tasks. Specifically, the core components of ICL consist of demonstration inputs and test inputs. The authors decompose the ICL process into two sub-processes for detailed examination. The first stage involves selecting a classification strategy from among multiple options (referred to by the authors as “hybrid” selection). Using sampling to establish a fixed distribution for strategy selection, the paper investigates the underlying causes of the discontinuous decision boundaries observed in ICL for discriminative tasks. The second stage is the execution of the chosen classification strategy. Here, the authors use prompts to direct the LLM to apply specific strategies, evaluating the effectiveness of execution through analysis of the LLM's output, confidence levels, and squared error metrics. Overall, this research introduces an interesting perspective for examining the decision boundaries formed by LLMs during in-context learning.

### Strengths
1. This paper builds upon the previous work by providing an in-depth exploration of the mechanisms of in-context learning (ICL) in discriminative tasks for LLMs, with concrete examples for support. Given the black-box nature of LLMs, as well as challenges like emergent hallucinations and instability, I believe this is a crucial yet underexplored topic within the field of ICL.
2. The authors propose an innovative hypothesis for the computational process of ICL, framing it as a two-stage process. This approach is intuitive and mathematically sound, and each stage is explained in detail to elucidate its underlying mechanisms.
3. The paper includes extensive visualizations that clarify the empirical findings, providing strong support for the analysis and enabling both readers and reviewers to understand the authors’ intent clearly.
4. The paper connects LLMs with traditional machine learning models, a critical perspective given that traditional models excel in some classification tasks where LLMs may struggle—even to the point of failing to recognize simple patterns, like the correct number of 'r's in "strawberry."

### Weaknesses
 1. **The empirical results are influenced by uncontrolled variables, undermining the hypothesis**: The authors arrive at a preliminary conclusion that LLMs resort to existing mathematical methods in a two-step classification process based on an analysis of the reasoning process output by the LLMs. However, prompting the LLM to output reasoning itself alters its classification behavior. As prompt design and demonstration selection are known to significantly impact ICL performance [A survey on in-context learning], the prompts here should have been treated as control variables. The authors do not control for these prompts, and due to the black-box nature of LLMs, it may not even be feasible to fully control these influences. Therefore, conclusions drawn from LLM output may be confounded by the influence of the reasoning-prompt itself.

2. **Flaws in research logic**:
   - 2.1 **Mismatch with the origin of ICL in few-shot learning**: The concept of ICL originated from the GPT-3 paper "Language Models are Few-Shot Learners," which is grounded in deep learning. In deep learning, the model’s few-shot capability arises from its ability to discern differences across limited samples, unlike ML classification models that rely on feature calculations. Applying conventional assumptions from ML classification models to LLMs may be inappropriate, though differences could stem from LLMs being trained on extensive, diverse corpora. Perhaps using ML to measure the resolution ability of ICL is not appropriate, and perhaps adding such an argumentation process as well as a discussion on the formation process of the ICL decision boundary would be more helpful.
   - 2.2 **Insufficient support for hybrid strategy hypothesis**: In examining whether “LLMs fully leverage existing ML algorithms for classification,” the authors hypothesize that hybrid strategies contribute to poor decision boundaries (as outlined in Appendix C). However, this hypothesis is not thoroughly substantiated. Additionally, when assessing confidence between standard and specific prompts, the authors do not account for the influence of unrelated variables (as mentioned in point 1), which may lead to differences due to the LLM’s intrinsic capabilities rather than prompt content. Furthermore, when discussing confidence, the authors suggest the LLM’s use of an "anchor" class. However, in the case of two distinct categories with strong clustering and nearly linear regression, this anchor assumption seems inappropriate. It may be more helpful to add analysis on hybrid strategies, response to point 1, and visualization of decision boundaries for multiple data types with different distributions.
   - 2.3 **Lack of discussion on CoT capabilities and calculation weaknesses**: The paper mentions that CoT capabilities and mathematical limitations contribute to discontinuous decision boundaries but does not adequately link these points to the core arguments or clarify the rationale for this conclusion. If the author could explain the reason for the abrupt appearance of Cot and computational ability in the paper, it might be more helpful.
   - 2.4 **Unclear rationale for discontinuous boundaries with specific strategies**: If fragmented boundaries result from random selection, it is unclear why boundaries remain discontinuous even when specific strategies are applied. Please explain this phenomenon.

3. **Limitations in understanding of LLMs**: In this study, the authors attempt to explore the discrimination capabilities of ICL through machine learning classification models, therefore, the following comments may not be very important, but there are still some basic points about LLM that need to be discussed:
   - 3.1 **Tool (ML and other methods in this paper) usage in LLMs**: In practice, ML or other discriminative methods serve as tools within the LLM ecosystem. When tasked with classification, an LLM would typically apply 'Tool Learning' [Tool Learning with Foundation Models] rather than using tools as an intrinsic reasoning method.
   - 3.2 **Unclear conclusions in Section 4.3**: The quantitative analysis in Section 4.3 is somewhat unclear, and its significance is difficult to interpret. For instance, the finding of the lowest SD in the MLP setting is not particularly innovative. Since LLMs are composed of multiple Transformer, other studies [In-Context Learning Creates Task Vectors], [Iterative Forward Tuning Boosts In-Context Learning in Language Models] have demonstrated that vector representations (akin to MLPs) are fundamental to effective ICL. Hence, it is unsurprising that MLP yields the lowest SD.

### Questions
1. **What is the prompt design for outputting the reasoning process?** How might this prompt affect the original performance of LLMs on discriminative tasks? (Does the LLM approach the task in the same way for the same input when prompted to output its reasoning process versus when it is not prompted to do so?)
2. **How is the hybrid strategy hypothesis in Appendix C introduced to explain overconfidence?** In Figure 3, could the confidence distribution be influenced by unrelated variables in the prompt (e.g., specifying a classification strategy within the prompt might actually impact the inherent capabilities of the LLM)?
3. **How does the LLM execute MLP?** Is it manually calculating gradient backpropagation over a long-text response?
4. (This part is the most important.) **Other questions raised in the Weaknesses section.** I have a generally positive attitude towards this research, but due to some parts of this article that are not effectively explained in a chain-like, interconnected manner, there are many questions that need to be answered.

### Soundness
3

### Presentation
4

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
The paper investigates the behavior of large language models (LLMs), specifically Llama-3-8B, in performing discriminative tasks such as binary classification. It highlights that LLMs often exhibit fragmented decision boundaries when tackling simple classification problems, which contrasts with the smooth decision boundaries typically achieved by conventional machine learning methods.

The authors observe that LLMs tend to select strategies based on existing machine learning algorithms to predict labels for query data. However, they find that LLMs struggle to effectively leverage these algorithms, often leading to overconfidence in their predictions. The study conducts a series of analysis to understand the reasons behind these behaviors, including probing the label predictions and the confidence levels of the models under different prompt settings.

### Strengths
The paper provides valuable insights into the decision-making processes of LLMs, highlighting how they select and execute strategies based on in-context data.

The research includes quantitative evaluations of the frequency of different machine learning methods used by Llama-3-8B, offering a clear understanding of its preferences in strategy selection.

### Weaknesses
This paper provides understanding of the LLM for decision-making, however, it lacks in-depth by providing insights to address the current issues.

It is not clear to me how LLM chooses different ML algorithms.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the ICL behavior of Llama-3-8B in classification tasks. It demonstrates that LLMs exhibit fragmented decision boundaries during simple discriminative tasks, revealing a two-step approach where they first select a strategy and then predict labels. Despite attempts to leverage existing machine learning algorithms, LLMs struggle to do so effectively and often display overconfidence in their predictions.
Through analyses of label predictions and simulations based on strategy preferences, the authors find that LLMs tend to mimic Decision Tree mechanisms, which contributes to the fragmented decision boundaries due to randomness in feature selection. The paper offers insights into the discriminative capabilities of LLMs and the challenges they face in applying traditional machine learning techniques.

### Strengths
1. The paper demonstrates that LLMs, particularly Llama-3-8B, approach discriminative tasks through a two-step process: sampling a strategy and predicting labels based on in-context examples.
2. It analyzes decision boundaries formed by Llama-3-8B with various specialized prompts, revealing that LLMs struggle to leverage machine learning algorithms effectively due to overconfidence and limitations in mathematical reasoning, leading to less smooth decision boundaries.
3. The research also explores Llama-3-8B's preference for classification strategies, demonstrating that it relies on feature observation. The findings suggest that fragmented decision boundaries may arise from the randomness in feature selection during classification tasks.

### Weaknesses
1. The primary weakness of this paper is its reliance on experiments conducted solely with Llama3-8B. The observations and insights derived may not be applicable to other families of LLMs. Therefore, it would be prudent for the authors to narrow the scope of their discussion specifically to Llama3-8B.

2. Another significant weakness is the conclusion that 'LLMs tend to perform discriminative tasks in a two-step paradigm.' This conclusion arises from either the conditional probability (Eq. 2) or from prompting Llama3 with a reasoning requirement. I believe that responses based on additional requirements like reasoning requirements do not accurately reflect Llama3's behavior with standard prompts. For instance, we can add 'think step by step' to standard prompts for better LLM performance compared with standard prompts and demonstrate the use of CoT. Therefore, the results only support the effectiveness of the 'two-step paradigm' when prompted with 'provide the answer with reasoning,' which does not represent LLMs' true functionality under standard prompts

3. The choice of an 8B parameter model raises concerns about its representativeness among the larger LLMs, such as Llama 3.1 with 405B parameters. This model size may not sufficiently capture the characteristics and capabilities of larger LLMs.

4. The authors repeatedly assert that Llama3-8B employs random sampling strategies (lines 92 and 417). However, it is unclear which specific experiments substantiate this claim. Clarification and supporting evidence are needed.

### Questions
1. The authors frequently mention that 8B models exhibit CoT-like reasoning. However, existing literature suggests that CoT reasoning is primarily associated with larger LMs. Are there references or empirical evidence to support that 8B models can also benefit from this reasoning technique?

2. Instead of stating that LLMs 'do not effectively leverage machine learning algorithms,' does the similarity in decision boundaries shown in Fig. 2 imply that LLMs are not applying any machine learning algorithms at all? Are there any statistically significant results that demonstrate that the boundaries in Fig. 2 differ?

3. The template mentioned in line 295 lacks specificity regarding specialized learning strategies (e.g., Decision Trees). What exactly is the template for Fig. 3, and how does it relate to the template described in line 295?

4. In Table 1, the behavior of LLMs with different learning strategies shows the smallest squared difference compared to MLP. How can we conclude that 'the behavior of LLMs, when learning strategies are specialized, resembles that of KNN, SVM, and MLP algorithms'?

### Soundness
2

### Presentation
3

### Contribution
2
