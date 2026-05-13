# Markovian Transformers for Informative Language Modeling

- Decision: Reject
- Avg Score: 6.75
- Scores: 5, 6, 6, 10

## Abstract
Chain-of-Thought (CoT) reasoning holds great promise for explaining the outputs of language models, but recent studies have highlighted significant challenges in its practical application for interpretability. We propose to address this issue via two key components: a technique to factor next-token prediction through intermediate CoT text, ensuring the CoT is causally load-bearing, and a reinforcement learning approach to train CoT to predict future tokens independently of other context. This results in ``Markovian'' language models, where CoT serves as a fixed-size state for future token prediction. Our approach optimizes for ``informativeness'' – the improvement in next-token predictions using a trained CoT compared to a baseline. We demonstrate our method's effectiveness using Proximal Policy Optimization (PPO) on arithmetic problems and achieve an 11\% performance boost on the GSM8K benchmark using Mistral 7B Inst V2. The increased sensitivity of model performance to CoT perturbations provides strong evidence of CoT reliance. This work advances the development of more transparent and interpretable language models, potentially enabling their extension to arbitrarily long contexts and enhancing AI reasoning capabilities across various domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a framework where the reasoning steps are used as fixed-size states, which limits the model’s context (text bottleneck), and force the model to use the reasoning steps as input. This method design is inspired by the fact that past CoT literature find that the final answer might not be sensitive to the CoT trace. In the experiment, the authors show that the model trained with this method is indeed more fragile against CoT pertubations.

### Strengths
- The Markovian framework blocks the model from attending back to the original question and force it to use the CoT context for generation. This provides a new view and framework for analyzing CoT effects.
- The reinforcement learning-based approach demonstrates improved performance on tasks requiring multiple steps, 
- The CoT steps generated from this method seem to be more interpretable, from two dimensions: 1) pertubation of the CoT could lead to more model errors 2) the reasoning can be carried over to another model.

### Weaknesses
 - The main concern “it’s uncertain if this CoT is genuinely interpretable by humans” is not addressed after the rebuttal.

  - This manuscript motivates the method in both the abstract and introduction and argues that interpretability techniques are important. For example, the abstract highlight the problem of “interpretability”, and this paper is to “address this issue”. In the introduction, the author motivates with “high-stakes scenarios”. Given this motivation, it is not sufficient if how interpretability improves for human readers is studied. If the authors consider human interpretability and study should be another work, then major revision is needed for the motivation part of this paper. “Envisioned methods” are without results are not enough to prove the case, so they are not enough to serve as evidences.
  - I appreciate the authors trying to address the comments in the appendix, but a proposed method is not enough to support the claims. Further, like many has pointed out, the appendix will not be treated as important as the main body.
  - I further notice in the “steganography” appendix, L1011 and 1012 are undeleted comments of the authors, indicating the manuscript isn’t fully proofread.

- Baselines and insufficient analysis of section 5
  - The baselines designed for this paper should also be tie to the motivation (which is currently interpretability). A study needs to be setup to show how the method improves the interpretability. In my review I pointed out that 5.2 is lacking depth, the same applies to 5.3 (if not more), since if the key motivation of this paper is interpretability, I would expect a much richer version of the analysis section. 

- Not enough tasks/datasets to prove the generalizability and effectiveness.
  - CoT is a technique generally applicable to many tasks, and if we want to show an improved version of that, more tasks and datasets need to be tested. The “Wikipedia” experiment is not convincing enough as an alternative challenging reasoning task, and one more next token prediction task still cannot convince me the “generalizability” of this work.

### Questions
- Is there a way to combine the interpretability with actual human perception? Though informativeness here can be used to improve model quality, it is also very helpful from human level. This is probably mentioned in F. But it seems to me F is more about how to encode human interpretability in training.
- In F it is mentioned that "optimal CoT would be a compression of the question, which can potentially be difficult for humans ". Is this observed in your experiments?
- Were there more ablation study or comparison conducted?

### Soundness
3

### Presentation
2

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
This paper proposes a metric to measure the informativeness of CoT tokens, and then uses RL to train the model to generate highly informative CoT tokens, in order to improve the correctness of the final answer. Experiments in random addition problems and GSM8K math problems demonstrate the effectiveness of the proposed metric and RL methods. The paper also shows that more informative tokens will bring gains in interpretability.

### Strengths
The technical ideas, including the proposed metric and RL methods, are new, well-motivated, and technically reasonable.  

The experiments in random addition and GSM8K are positive.

### Weaknesses
The experiments are limited to a synthetic math problem setting and GSM8K, and the only trained model is Mistral 7B. 

The presentation needs a better organization. E.g., some major results are placed in the appendices, but training details are in the main paper.

### Questions
Have you tried other open-source models like llama? Not use CoT of Mistral in it, but use your method to finetune Llama.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces and explains the construction of a Markovian Language Model to study causality in chain-of-thought reasoning. With a limited state (the previous state and its observation) on which to condition, the model is trained (fine-tuned) to maximize an informativeness objective through PPO, and is empirically shown to improve performance on mathematics tasks such as GSM8K and toy addition problems.

### Strengths
* The setup of this causally-guided model is pretty novel, and the finding that this improves performance by optimizing on an “information” metric is an impactful finding. 
* The selection of the RL training technique (PPO) is supported by highlighting the limitations of other considered methods (expert iteration and policy gradient).
* The work is written in a way that was simple to follow, which I appreciated.
* The gains on GSM8K (24.64% --> 35.71%) are meaningful (although, a bit tucked away in the paper's text).

### Weaknesses
 * I understand the general intuition surrounding the design of the informativeness function, but it would be good to add some discussion on why the expected reward over the trajectory actually constitutes / addresses “informativeness” under your construction. 
* While math tasks have a more well-defined structure (the order in which their steps may be pursued), this is less clear for other tasks without such a clear structure in natural language, for instance. It would be good to examine this approach on at least one such task to further support the method’s general efficacy.
* Despite the intuition-based process of selection for the RL training strategy, there are recent works that advocate in favor of expert iteration and REINFORCE / vanilla policy gradient for LLM reasoning and RLHF [1, 2]. To this effect, including such approaches for comparison in the results section (or in the appendix) would strengthen the defense of the PPO method chosen. It would be helpful to include some evidence supporting the limitations posed.
* While I appreciate documenting the design choices in Section 4.3, some justification behind them would be beneficial, either through ablations (it’s fine for these to be in the appendix) or relevant references. 

### Questions
* Is the space of states task-conditional? This isn’t apparent based on the formulation in Section 3.1 (and is unclear by the wording in line 162). If not, then it would seem that the set of relevant “CoT states” would be very sparse relative to the complete space. 
* As posed in the weaknesses section, does this method extend to other reasoning tasks (e.g. in natural language or code) whose structure is less “linear”?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
__Post-rebuttal update__:

After the rebuttal has concluded, I feel the need to express my strong support for this paper. I believe the proposed method has the potential to become an industry-defining standard, which ICLR should be proud to be the publisher off. The authors have done a lot to further improve the paper from a decent submission to an excellent submission that should be highlighted at a conference. While one can always conduct more experiments to support one's claims even more strongly, I think the remaining requests made by other reviewers are unrealistic. The paper should be accepted as is.

---------

The paper addresses an issue of Chain-of-Thought (CoT) reasoning in LLMs where the LM's final answer does not always depend on the CoT. The paper's idea is to enforce informativeness by conditioning the answer model on the generated CoT only without other context. To this end, the paper formally defines Markovian Language Models and (informative) update functions, from which the policy gradient procedure is derived. Applying the framework to the specific use case of CoT reasoning, the paper experiments with several RL techniques such as expert iteration, policy gradient, and PPO. The model is applied to a simple arithmetic task of adding 15 numbers as well as GSM8K, and shows that the model a) improves performance on the task b) is sensitive to perturbation in the CoT reasoning and c) produces CoTs that are sensible to a different language model such that its performance on the task is improved.

### Strengths
* The paper addresses an important limitation in Chain-of-Thought reasoning, which is of relevance to the broader ICLR community.
* The core idea is intuitive and simple.
* The paper is well written.
* The results on the simple arithmetic task and the math task are promising.
* The claims that the proposed method improves the generated CoTs in terms of interpretability and informativeness are well supported.

### Weaknesses
The method is evaluated only on few tasks and models, limiting how sure we can be that this is a useful method. Especially an application to language modeling would be very insightful and potentially extremely impactfull. However, while more is always better when it comes to experimental results, I think that this initial set of experiments support the ideas presented well and should suffice for publication.

### Questions
Please use different line styles in your figures so colorblind people can make sense of them. Otherwise Figure 2 and 3 are really hard to parse!

### Soundness
4

### Presentation
4

### Contribution
4
