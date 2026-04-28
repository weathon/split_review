# Text as parameter: interactive prompt optimisation for large language models

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 3, 5, 3

## Abstract
Large language models (LLMs) can handle a variety of tasks conditioned on natural language instructions. While fine-tuning improves task-specific performance, adjusting the model weights of LLMs requires a huge amount of computational resources, and it is impractical for real-time updates. Alternatively, prompting allows LLMs to adapt to a broad range of tasks without the need for computationally intensive gradient-based optimisation. 
However, crafting effective prompts remains a challenge, to the extent that it is even unclear if expert in-domain knowledge is what is needed or experience in writing prompts or something else. 
Approaches like meta-prompting and self-feedback seek to alleviate this burden, but they rely primarily on a numerical feedback signal, leaving the potential of textual feedback unexplored. 
These methods also typically require numerous interactions with the environment to gather sufficient context, leading to significant computational overhead.

In this work, we propose a novel framework that takes a prompted large language model as an optimiser and treats the text-based prompt itself as a parameter. 
By interacting with the environment to collect feedback, our proposed method constructs the updated textual prompt. 
Our experimental results demonstrate that this method not only achieves superior performance but also automatically incorporates domain-specific knowledge, establishing a scientifically motivated, practical and efficient approach to prompting for future research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Text-as-Parameter (TaP) to optimize prompts. This method involves interacting the model with the environment and using another model to provide detailed textual feedback that discusses the strengths and limitations of the prompt. The prompt is then rewritten based on this feedback. Experiments demonstrate that this approach achieves good performance in task-oriented dialogue and medical question-answering domains.

### Strengths
1. The paper proposes Text-as-Parameter (TaP), a method that leverages textual signals as feedback to iteratively optimize prompts.  
2. Experiments on task-oriented dialogue and medical question-answering demonstrate the effectiveness of the method.

### Weaknesses
1. The novelty of this work lies primarily in replacing the score-based evaluation with a text-based evaluation to measure the prompt quality. But this is just one aspect of various kinds of feedback in previous works[1][2][3]. I believe the authors have overstated the contribution of the paper.  

2. The authors only verify their methods on closed LLMs and do not evaluate open-source LLMs, such as Llama-3 and Qwen-2. They also miss to compare their approach with some recent baselines, such as [1][2]. Additionally, they fail to assess their methods on general benchmarks, such as BBH and MMLU, which are commonly used by other baselines. 

3.The authors do not provide a detailed analysis of some important characteristics of the method, such as convergence, generalization, and the impact of the initial prompt in prompt optimization.

### Questions
See the weaknesses part.

### Soundness
3

### Presentation
2

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
In this paper, the authors propose a prompt optimization method called Text-as-Parameter. In this framework, the initial prompt is used to generate some samples which consist of interaction between LLM and users. Then, the interactions are sent to feedback LLM to generate a review and then sent to rewrite to rewrite the prompt. The results on two datasets show that the proposed TaP outperforms numerical feedback.

### Strengths
1. Prompt optimization is an important and urgent topic for LLMs as prompt influences the performance significantly and it is still unknown how to find the best or robust prompt. 

2. The idea of self-improvement or refinement is popular and seems promising.

3. The experimental results on MultiWOZ improve the numerical baseline by a large margin.

### Weaknesses
1. The experiments are not solid. Although the introduction and related work mention a number of works such as APO, OPPO, and GPO. The experiments only compare with one GPO baseline, weakening the conclusions. Besides, more ablation studies are needed to understand how the proposed framework works. Also, it is unclear how the GPT-simulated user performs. At least some human annotations are needed to confirm the simulation quality. Overall, it is difficult to judge the performance of the entire system.

2. The novelty of the proposed work is limited. If I understand correctly, the biggest novelty is the external text feedback rather than the numerical ones. However, there are some studies generating text-based feedback for optimizing prompts, such as TextGrad [1]. Also, textual feedback and rewriting are well-established, such as self-refine [2,3]. This further weakens the novelty of the proposed work.

3. Writing and presentation need to improve. For instance, the introduction does not introduce the experimental results.  And more explaination is needed for trajectories and other designs rather than proposing a name alone.

### Questions
See above weakness.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel framework for optimizing prompts in large language models (LLMs) by treating text-based prompts as parameters that can be iteratively improved through feedback interactions. The proposed method leverages textual feedback, refining prompts based on interactions with the environment, which integrates domain-specific knowledge. Experimental results show that the method is effective across various LLMs, such as GPT-4o mini and Gemini-1.5-flash, and works well with multiple prompting styles, including standard and ReAct.

### Strengths
(1) The framework proposed in this paper is effective. Without additional training or fine-tuning, TaP improves performance across prompting styles under the GPT4-o and Gemini.

(2) The framework diagram in the paper is well-crafted.

### Weaknesses
(1) The evaluation dataset is small and lacks benchmark comparisons on popular datasets. The experiments in this paper are conducted on 100 MultiWoZ instances, 30 pairs of interactions in general medicine, and 30 in traditional Chinese medicine. In contrast, the baseline method GPO [1] provides comparison results across multiple datasets (BBH, GSM8K, MMLU, WSC, WebNLG). Extending this method to more widely used evaluation datasets would enhance its reliability and effectiveness.

(2) The evaluated models are limited and are all closed-source, namely GPT-4o and Gemini. It remains to be seen whether this approach applies to different sizes of open-source models. I suggested extending the method to the Llama-2 series, as GPO does, to enable a direct performance comparison between your method and GPO.

(3) The method lacks novelty; the instruction-feedback-refine framework is familiar in NLP.

### Questions
1. Why did you choose to evaluate Task-oriented dialogue and medical question-answering tasks rather than using popular benchmark datasets? 

2. Why was the evaluation conducted on small-scale samples (e.g., 30 samples) from three datasets instead of using the entire test set? Evaluating just a few selected samples seems like cherry-picking, which may lead readers to question the model's effectiveness.

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
This paper introduces a novel framework called Text-as-Parameter (TaP) for optimizing prompts in LLMs based on the way humans learn new things. Instead of relying on fine-tuning or simple numeric feedback, TaP treats the prompt text itself as a parameter, iteratively refining it based on textual feedback from interactions. The process involves initializing a prompt, then continually updating it through a feedback loop where a ``rewriter'' component incorporates the feedback to generate an improved prompt for the next interaction. Experimental results indicate that TaP outperforms existing numerical-feedback methods in diverse applications, including task-oriented dialogue and medical question answering.

### Strengths
* Using detailed textual feedback instead of simple numerical scores is intuitively beneficial, as it provides richer, more nuanced guidance for prompt adjustments.

* The paper presents a comprehensive set of experiments demonstrating the benefits of TaP across simulated and real-world settings, thus validating the approach’s effectiveness compared to traditional numerical feedback methods.

* The TaP method demonstrates steady improvement in complete rates over multiple epochs, indicating its robustness and potential for long-term usability.

### Weaknesses
 * While the shift from numerical scores to textual feedback enhances prompt refinement, this alone may not constitute a sufficient contribution.

* The claim of treating text as a “parameter” feels overstated. While the method refines prompts iteratively, it primarily mirrors traditional prompt optimization techniques and doesn’t fully leverage text as an integrated parameter of the model.

* Table 2 presents a comparison by aligning TaP optimization closely with gradient-based methods. However, unlike gradient-based methods which iteratively refine continuous parameters towards optimal values, TaP relies on discrete prompt rewriting. This could lead to inconsistent improvements, as prompt optimization depends heavily on the quality of feedback and may not consistently yield better outcomes.

### Questions
* When both the user, rewriter, and system are built using LLMs, the framework essentially functions as an LLM-based multi-agent system. Given this structure, it would be valuable for the authors to explore comparisons with existing multi-agent collaboration methods. Have the authors considered benchmarking TaP against multi-agent collaboration methods?

[1] Kim D K, Sohn S, Logeswaran L, et al. MultiPrompter: Cooperative Prompt Optimization with Multi-Agent Reinforcement Learning[J]. arXiv preprint arXiv:2310.16730, 2023.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method for prompt optimization that utilizes text feedback from an optimizer large language model (LLM). The proposed method is compared with GPO, a method that optimizes prompts with numerical feedback (such as accuracy score). The proposed TaP method significantly outperforms the GPO baseline by a notable margin on 1000 MultiWOZ and on two Chinese medicine datasets.

### Strengths
- This paper presents an excellent comparison between prompt optimization and other methods like prompt tuning and inference-time self-refinement.
- Experiments on two challenging human-machine interaction tasks demonstrate that this method not only achieves superior performance but also automatically incorporates domain-specific knowledge

### Weaknesses
 - The paper is lacking in comprehensive comparisons with recent baselines. For example, the related work introduced between lines 120 to 135, like APO and OPRO. However, the experiment only compares with GPO, which makes the empirical result rather weak.
- The novelty of the paper is also lacking. As the author pointed out in line 120, the APO method also uses "textual feedback which gives suggestions on how to edit the old prompt". Having read the APO paper, it is unclear to me how the proposed method differs from APO, except for the difference in meta prompts.

### Questions
- How is your method differnt from APO?

### Soundness
2

### Presentation
2

### Contribution
1
