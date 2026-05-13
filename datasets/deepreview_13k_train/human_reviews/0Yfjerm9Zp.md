# Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference

- Decision: Reject
- Scores: 5, 1, 3, 5

## Abstract
As large language models (LLMs) are increasingly applied to complex reasoning tasks, achieving both accurate task performance and faithful explanations becomes crucial. However, LLMs often generate unfaithful explanations, partly because they do not consistently adhere closely to the provided context. Existing approaches address this problem either rely on superficial calibration, such as decomposed Chain-of-Thought prompting, or require costly retraining to improve model faithfulness. In this work, we propose a probabilistic inference paradigm that provides fine-grained and lookahead rewards to ensure that LLM-generated rationales are logically coherent and comprehensive. These rewards are derived from a domain-specific proposal distribution, allowing for optimised sequential Monte Carlo approximations. Our evaluations across three different reasoning tasks show that this method, which allows for controllable generation during inference, improves both accuracy and faithfulness of LLMs while keeping computational costs similar to those of existing decoding techniques. This method offers a promising path towards making LLMs more reliable for reasoning tasks without sacrificing performance or efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an approach to do faithful rationale generation in LLMs. It uses a steering-based approach to make the outputs more faithful to the reasoning of the llm in classification. The idea is to weight token logits using 2 kinds of reward models: A "local" one that tries to match tokens to those suggested by a domain-specific expert model and a "lookahead" one that does an MTCS type search and re-weights logits based on rewards from unrolled sequences.  

Experiments are performed on a couple of QA type datasets, demonstrating that each method makes improvements in classification accuracy and faithfulness of rationales. Some qualitative analyses are also presented.

### Strengths
1. MTCS type inference is a hot topic right now, and it is indeed an important frontier for LLMs to improve on.
2. At a surface level, experimental results seem to show large gains.

### Weaknesses
Section 3 is pretty badly written, it is pretty hard to get the details of the approach. Instead of invoking irrelevant sophisticated-sounding terminology like "Feynman-Kac" formulas it would be better to describe the method in more detail. The math especially is confusing, see below.  

The paper seems to show some positive experimental results, but I am concerned about whether we are looking at a meaningful comparison. The proposed methods rely on domain experts. Looking at table 8 in the appendix these are generally models that have been fine-tuned for the task in some way (and not just on the validation sets as the main section claims, some have access to external datasets). So it shouldn't be that surprising that a method that is given access to an expert which has more signal will do better than the backbone pre-trained model. A fair comparison would have to be with an approach that does vanilla fine-tuning of LLama or mixtral model. 

In terms of novelty: The authors have not really cited relevant work in the controlled decoding space:

https://arxiv.org/abs/2310.17022

https://sea-snell.github.io/ILQL_site/

These works already do something more sophisticated than just token reweighting by a reward score. So what is the novel contribution here? 2 possibities:
1. Focusing on the faithfulness problem.
2. The "lookahead" idea of the reward model. I dont recall having seen this before, but it feels like a simplification of a full-blown MCTS. I would also call this a poor man's version of ILQL.

So we are just left with #1 then, unless I missed something. And this is something I consider of limited novelty (more like an application for a particular problem, though one with interesting implications from the steering perspective).


1. what is "t \wedge T" ?
2. sec 3.3, what is P(s_t) a posterior over?
3. In what sense is \pi_t a "potential" function?
4. I cannot make any sense of eq 2. Is w \in V the same as w_t?  why cant you simply remove the indicator function and write it as \sum_w \in C ? why is the indicator function in the deminator as well? is the intent to have a logit distribution that only puts mass on the tokens in C?
5. are the rollouts done on the backbone model or the expert model? have we considered /measured the inference time cost? this is an important consideration in a paper about mtcs type methods.

6. Does q_\phi simply reward completions of the output that have tokens in C?

7. intro: "in contrast, an expert model....." : this is an interesting claim (does seem plausible). is there a citation for evidence?

8. line 140: tend to generate similar token....": what does this mean?

9. i am not up to date on the faithfulness literature, but the kind of interventations that the paper describe as standard ways of evaluation i.e. word inclusion and perturbation just seem to be likely to be noise-prone, leading to unreliable evals?

10. GenExpert =?  lookahead?

11. comment: the discussion between 329-342 helped understanding a bit and should be earlier in the paper.

12. sec 5.2.2: the NLI example is a bad one i think. Submergible only means it is something that can be submerged. which doesnt automatically mean it is submerged.

### Questions
1. what is "t \wedge T" ?
 2. sec 3.3, what is P(s_t) a posterior over?
 3. In what sense is \pi_t a "potential" function?
 4. I cannot make any sense of eq 2. Is w \in V the same as w_t?  why cant you simply remove the indicator function and write it as \sum_w \in C ? why is the indicator function in the deminator as well? is the intent to have a logit distribution that only puts mass on the tokens in C?
 5. are the rollouts done on the backbone model or the expert model? have we considered /measured the inference time cost? this is an important consideration in a paper about mtcs type methods.

6. Does q_\phi simply reward completions of the output that have tokens in C?

7. intro: "in contrast, an expert model....." : this is an interesting claim (does seem plausible). is there a citation for evidence?

8. line 140: tend to generate similar token....": what does this mean?

9. i am not up to date on the faithfulness literature, but the kind of interventations that the paper describe as standard ways of evaluation i.e. word inclusion and perturbation just seem to be likely to be noise-prone, leading to unreliable evals?

10. GenExpert =?  lookahead?

11. comment: the discussion between 329-342 helped understanding a bit and should be earlier in the paper.

12. sec 5.2.2: the NLI example is a bad one i think. Submergible only means it is something that can be submerged. which doesnt automatically mean it is submerged.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The work aims to improve the faithfulness of the LLM-generated rationales for reasoning tasks. They propose an inference-based method where an LLM is guided to generate more faithful rationales by both local and global rewards. Both rewards are provided by additional expert models which are trained on the downstream tasks. Experiments demonstrate the effectiveness of the method in achieving higher accuracy and faithfulness.

### Strengths
1. Faithful rationales are important for explainability and model control, which makes this work well-motivated.
2. The proposed method is training-free (although with reliance on trained expert models), making their method portable.
3. A comprehensive set of experiments is conducted to showcase the effectiveness of their proposed method.

### Weaknesses
1. The method requires the model to generate the answer prior to the rationale, which provides no guarantee that the decision is made based on the rationale. The model could still suffer from inherent biases. Specifically, the approach does not address the potential for the model to generate an answer based on spurious correlations in the input data, and then generate a rationale post-hoc to justify that answer. This could lead to rationales that appear faithful but are not actually the basis for the model's decision.
2. The method is limited to reasoning tasks with constrained answer space, limiting its generalization to more open-ended tasks. While the authors demonstrate results on tasks with discrete answer choices, the applicability to tasks requiring free-form text generation is unclear. The reliance on expert models that provide a probability distribution over a fixed set of labels limits the method's flexibility.
3. The method is poorly introduced. It would be very helpful if the authors could explain what exactly Eq.1-3 are doing in plain words. The current description lacks clarity on how the local and global rewards are computed and integrated into the generation process. The connection to the Feynman-Kac model is not clearly explained, making it difficult to understand the theoretical underpinnings of the approach.

### Questions
Could this method generalize to the setting where the rationale is generated before the answer?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes an inference-time method to improve the performance and faithfulness of general (instruction-tuned) large language models (LLMs). Specifically, the method uses expert models to provide fine-grained and lookahead rewards to search and reweight possible tokens or continuations proposed by the LLM. With the help of expert models trained on the target task or domain, the proposed method can improve both the accuracy and faithfulness of the zero-shot answers of two instruction-tuned models on three reasoning tasks.

### Strengths
The direction this paper explored has been receiving increasing interest recently: improving the quality of LLM answers at inference time without modifying the model weights directly. The proposed method improves the zero-shot accuracy and faithfulness of two strong general instruction-tuned models (Llama-3-8B and Mistral-7b-Instruct-v0.3) on three reasoning tasks. The experiment showing the benefits of going beyond local/token-level rewards and taking into account the global/lookahead reward is interesting.

### Weaknesses
- There needs to be more details explaining the proposed method, the motivation of each part, the equations and variables, the relation to related work, and the implementation details. Specifically:
  - Section 3.3: how does the Feynman-Kac Formulae model inspire the faithfulness-seaking search framework? The connection is not straightforward. The notation of eq 1 is ambiguous. What does posterior P_t(st) mean exactly? How is it used in the proposed method? Also, the equation itself needs more explanations on what it is computing and why in this way.
  - Section 3.4 (Local constraint): line 179 I find it hard to follow the motivation. How "certain attributes can be implicitly conveyed over longer spans rather than the individual token" is connected to "Instead, domain-specific experts tend to demonstrate better accuracy in knowledge-rich tasks." ? If the domain expert has better accuracy why not just use the expert to predict the scores? Why bother to use them to improve the backbone LLM? In lines 180-181, it says "we introduce a set of classification label words C from these expert models ...", how is C constructed? What is the motivation behind token masking?
  - Section 3.4 (Lookahead Reweight): Equation 3 is hard to understand without proper explanations. $m$ and $x_i$ are not explained in the texts. $s_{t+l}=s_{t-1}||w_t$ is more confusing: $s_{t+l}$ has $t+l$ tokens while $s_{t-1}||w_t$ has $t$ tokens. What does equality mean here?
- Many experimental details are missing, and important experiments are missing.
  - Missing baselines: the performance and faithfulness of the expert models alone. If the faithfulness or accuracy of the expert models are better than the backbone LLM, why do we even need to use the expert models to improve the backbone LLM?
  - Evaluation details: how is the original model evaluated? If it is a zero-shot evaluation. What is the exact prompt and task format used? How to extract answers from the outputs to calculate the accuracy? The backbone LLMs are state-of-the-art instruction-tuned models. However, the task performance as well as the faithfulness are quite low, so the authors need to provide more details on the evaluation.
  - What is the choice of hyperparameter n (number of rollouts) and how is it chosen?
- The writing of the paper could be improved for better readability. First, the paper is not properly scoped. For example, in lines 16-18, it says "... to ensure that LLM-generated rationales are logically coherent and comprehensive." However, there is no result discussing the logical coherence or comprehensiveness of answers in the paper. Another example is line 108: it says "We firstly introduce the faithfulness definition in our context,", but there is no clear definition in section 3.2.

### Questions
1. If the expert model is as big as the base model, how can the computational cost be similar to beam search?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
They tackle the rationale generation tasks in LLMs' reasoning process. Specifically, they propose a probabilistic inference paradigm that provides fine-grained and lookahead rewards to instruct LLMs to generate good rationale. The key problem addressed is that LLMs often produce unfaithful explanations, especially when they fail to incorporate essential contextual information. 

+ **Local Reward**:  this component ensures coherence with the immediate context, often by using a domain-specific expert model.
+ **Global reward**: This assesses the plausibility of the current token in relation to desirable future attributes

The search algorithm, especially for lookahead reweight seems interesting.

Please forgive me if I misunderstand something. I spent much time for reading the paper but to be honest, I am not an expert in this area. I will available on the rebuttal time for author's response and will read their response. I am also open to other reviewers' opinions.

### Strengths
1. The paper introduces a novel probabilistic inference method with a dual-reward mechanism, combining local and global reward. This is a very novel solution. 
2. The paper is well-written. I am not an expert in this domain but I can get their core contributions. 
3. The experiment design is clear: they design the ablation study in Section 5.1 to justify the local and global rewards for the final performance. Although I suggest authors could do better by choosing more LLMs in different model size to better support their experimental design.

### Weaknesses
1. There are several related works that are missing or less discussed:
        + Evaluating Human Alignment and Model Faithfulness of LLM Rationale
        +  On Measuring Faithfulness or Self-consistency of Natural Language Explanations
2. Figure 2 about the distribution of domain-specific words is unclear to me. "showing that our method can respond more actively to those domain-specific words" Why does this part matters to the experimental results.

### Questions
1. The overall experiments are conducted on LLaMA3. I think more backbone LLMs and other sizes of LLMs are needed to justify the proposed inference paradigm.
2. More experiments on more related datasets is needed.

### Soundness
2

### Presentation
2

### Contribution
2
