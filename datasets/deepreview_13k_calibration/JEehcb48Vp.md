# Critic-CoT: Boosting the reasoning abilities of large language model via Chain-of-Thought Critic

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Self-critic has become a crucial mechanism for enhancing the reasoning performance of LLMs. 
However, current approaches mainly involve basic prompts for intuitive instance-level feedback, which resembles System-1 processes and limits the reasoning capabilities. Moreover, there is a lack of in-depth investigations into the relationship between LLM's ability to criticize and its task-solving performance. 
To address these issues, we propose Critic-CoT, a novel framework that pushes LLMs toward System-2-like critic capability.
Through a step-wise CoT reasoning paradigm and the automatic construction of distant-supervision data without human annotation, Critic-CoT enables LLMs to engage in slow, analytic self-critique and refinement, thereby improving their reasoning abilities.
Experiments on GSM8K and MATH demonstrate that our enhanced model significantly boosts task-solving performance by filtering out invalid solutions or iterative refinement. Furthermore, we investigate the intrinsic correlation between critique and task-solving abilities within LLMs, discovering that these abilities can mutually reinforce each other rather than conflict.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a CoT-based critic framework, including training data collections and two different inference methods (reflection or filter).

### Strengths
The paper is clear, the method is well motivated.

### Weaknesses
At least for me, the novelty of the proposed method is limited, as it is pretty similar to existing self-reflection-based approaches.
In particular, the proposed method does not guarantee that the generated critic is reasonable, as long as the refined output (taking the generated critic as additional inputs) contains the correct answer.

Besides, I expect more experiments on broad reasoning tasks beside math, and the improvements are limited for both GSM8K and MATH.

### Questions
No

### Soundness
3

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
3

### Summary
This paper proposes a simple procedure to construct NL critic and refinement data, with those data, this paper tests two ways of using those data: iterative refine (run NL critic on a system output, and then perform refinement to produce a new output) and critic as filter (only use NL critic as re-ranking). Experiments on GSM8k and MATH test sets show some improvements when run with Iterative Refine and Critic As Filter.

### Strengths
1.	The data construction for NL critique at step level looks interesting.
2.	The approach of Critic As Filter shows consistent gains over majority voting.

### Weaknesses
1. 	“Self-critique” ability used in this paper is distilled from a stronger model (e.g. GPT4-Turbo).
2. 	The basic data construction in Section 3.1 is built on sampling of LLMs, this procedure will inevitably introduce some noise, the overall quality of those data must be evaluated by human and reported in this paper. 
3. 	It’s not clear to me where the main improvements in Table 1-3 come from, it probability comes from GPT4-Turbo annotations (supervision).


### Questions
1.	The quality of critique data is crucial to train a valid NL critique at step-level. A) the assumption that the final answer is correct, then all intermediate steps are correct. Please evaluate some of those data and report the accuracy. B) All Att and Cri are from sampling, that randomness will also introduce some errors, those generated data should be also evaluated and reported in paper.
2.	The Iterative Refine improvements on MATH task without re-ranking are not significant, thus, I’m not convinced self-critique refinement with single pass is a valid approach. 
3.	It looks like self-critique iterative refine works in the re-ranking setting, this suggests that the self-critique accuracy is not high, we need some analysis in detail.

### Soundness
3

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
This paper introduces a new method to train a CoT-style critic model. For a multi-step solution, the proposed Critic-CoT is can be used to refine the multi-step solution with step-level explanations and can also be used to filter response samples. The experiments are conducted on math and reasoning tasks such as GSM8K and StrategyQA.

### Strengths
+ The performance of the critic model is evaluated using F1, which was usually indirectly evaluated by the downstream tasks.
+ The critic-cot model may be used as an additional critic model for filtering purposes.

### Weaknesses
 + Based on the description, it seems that CoT for the critique (e.g., those in Figure 1) is not well used. Also, the formulation is a little bit confusing (e.g., l_i is +1 or -1, however, the cot part is not included in this representation). The refinement ability of the CoT-critic seems to be weak on challenging math tasks such as MATH and MATH500, as the improvements in these tasks are marginal. Though the authors claim the main difference is the CoT ability of the critic model compared with other types of critic models, the advantage of using CoT is not well justified.
+ The role of distillation: the revised step also can be regarded as re-writing answers (the quality may be better than the original human annotation due to factors such as consistency), it is somehow unclear the gains from in-domain data augmentation or from the critic-cot.
Considering the fact that 10 samples are leveraged to form the data per instance, labeled by the gpt-3.5, the process can be regarded as that best-of-10 responses are used for SFT. Using 16 retry gpt-4-Turbo to obtain the refinement data also brings the same issue.
+ The evaluation lacks strong baselines that also use NL critic models or other types of reward models (e.g., deterministic), PRM or ORM.
+ Some details are missing. Please see the question part.

### Questions
+ How to define one step?
+ How to identify pred from the attempt? I can understand for GSM8K and MATH, there may exist answer patterns. Then how can we adapt the proposed method to other tasks, in which the answers cannot be easily extracted? To use the critic-cot for filtering, majority vote is also leveraged, which also assumes that the answers can be easily extracted (or only numbers). 
+ For the 2nd assumption (if the final answer is correct, then all the intermediate steps are correct), could the authors manually check tens of examples and provide the percentage of instances with perfect CoT reasoning? Also for the 1st assumption, it may also depend on the ability of the LLM.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the limitations of existing self-critique methods for LLMs, which primarily use simple feedback mechanisms that resemble intuitive (System-1) processing. In fact, many works have explored this issue, such as whether large language models (LLMs) can accurately reflect and how to inspire LLMs to reflect. Most works are designed based on prompt engineering.

To bridge this gap, the authors propose Critic-CoT, a framework designed to elevate LLMs' reasoning by developing a stepwise, chain-of-thought (CoT) critique process. The motivation is to enable LLMs to critique and refine their solutions autonomously, thus enhancing task-solving abilities without human annotation costs.  The author generates step-wise feedback by extensive sampling and using a strong LLM. Then based on this self-generated feedback dataset, it trains the model to have the ability of self-criticism.

### Strengths
First, the motivation of this paper is very interesting. How can we endow LLMs with the ability to self-reflect and self-evaluate? Regarding this point, many works have explored whether LLM can have spontaneous internal reflection ability. The author generates a large amount of step-wise feedback data through a strong LLM model, e.g., GPT4-Turbo. This is very practical.

Besides, this step-wise self-evaluate design is very practical. This type of  dataset is even more valuable than the MATH SFT data itself.

Finally, the author not only provides the main experimental results but also evaluates the self-evaluate ability of the trained model, considering indicators in dimensions such as P, R, F, and Acc. This is also relatively novel.

### Weaknesses
The main problems of this paper are as follows: 
1. The experimental results seem not very satisfactory. In Table 1 and 2, it seems that the sampling + voting mechanism (self-consistency) is more effective. For example, in Table 1, Critic-CoT + Llama-3-70B-Instruct achieved an accuracy of 91.7, which seems not very advantageous. However, after adding Maj1@96, it is increased to 94.8, surpassing the method Iterative Refine proposed by the author. If the native Llama-3-70B-Instruct + Maj1@96 is used, an effect of 94.1 can also be achieved. Can the author explain this phenomenon?

2. The ability of LLMs for self-reflection and self-evaluation, as well as step-wise feedback, is interesting. However, the paper lacks a more in-depth analysis. For example, does LLM really possess this ability? Does the model trained through CRITIC-COT have this ability? From my perspective, I think LLM is unable to achieve self-reflection by completely relying on oneself. The author's carefully crafted step-wise feedback dataset can improve the mathematical performance of the model. But can it really achieve self-reflection? It seems that the experimental results provided by the author cannot effectively prove this point. I hope the author can provide a more solid analysis.

3. Although the author provides the code, it seems that I don't see the generated feedback dataset.

4. I don't quite understand what specific relationship the term "distant supervision" has with this paper. In the field of information extraction, the meaning of this term is clear. However, in "LLM for math reasoning", I don't quite understand the relationship between this term and this paper. It is recommended that the author modify the corresponding expression.


Miss References:  

Many works have explored whether LLMs really have the ability of self-reflection:   

Huang J, Chen X, Mishra S, et al. Large language models cannot self-correct reasoning yet.  ICLR24   

Zhang W, Shen Y, Wu L, et al. Self-contrast: Better reflection through inconsistent solving perspectives.  ACL24

### Questions
As I mentioned above. 
The question studied in the paper is very interesting, but some key experiments and analyses need to be further strengthened.

### Soundness
3

### Presentation
2

### Contribution
3
