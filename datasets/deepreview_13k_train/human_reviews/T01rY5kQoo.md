# JoPA: Explaining Large Language Model's Generation via Joint Prompt Attribution

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Large Language Models (LLMs) have demonstrated impressive performances in complex text generation tasks. However, the contribution of the input prompt to the generated content still remains obscure to humans, underscoring the necessity of elucidating and explaining the causality between input and output pairs. Existing works for providing prompt-specific explanation often confine model output to be classification or next-word prediction. Few initial attempts aiming to explain the entire language generation often treat input prompt texts independently, ignoring their combinatorial effects on the follow-up generation. 
In this study, we introduce a counterfactual explanation framework based on joint prompt attribution, XPrompt, which aims to explain how a few prompt texts collaboratively influences the LLM's complete generation. Particularly, we formulate the task of prompt attribution for generation interpretation as a combinatorial optimization problem, and introduce a probabilistic algorithm to search for the casual input combination in the discrete space. We define and utilize multiple metrics to evaluate the produced explanations, demonstrating both faithfulness and efficiency of our framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper pays attention to the contribution of input prompts on generated content. By using counterfactual explanation, this paper proposes JoPA, a framework to highlight which components of input prompts have the fundamental  effect on the generated context via solving a combinatorial optimization problem. JoPA uses the gradient information and the probabilistic search-space strategy to find the more important tokens and improve efficiency.

### Strengths
1. This paper focuses on an important area, the impact of prompt on generated outputs.

2. The time cost of JoPA is quite less than baselines.

### Weaknesses
1. The counterfactual explanation is emphasized as the important part in JoPA, but its concept and logic are not fully explained. And there are not enough case studies to support this argument.

2. The practical usage scene of JoPA is under discussion. How would a user perform JoPA when using LLM via web service or APIs like chatgpt? Can more general advices are given for users?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the problem of prompt attribution, i.e., identifying the most important tokens in the prompt that influence the language model generation. This is formulated as a search / discrete optimization problem where the objective is to optimize a binary mask over the prompt tokens that would induce the most significant probability drop in generating the original target output. 

The proposed optimization method JoPA is (on a high-level) an improved version of MCMC, with two tricks:

1. Gradient guided masking: with the initial masking m_0, sample generations, use the gradient of the loss function to decide m_1 (leveraging the intuition that higher gradient magnitudes indicate more important t tokens). 

2. Probabilistic search update: at every iteration, perturb the current masking by swapping a non-zero entry with a sampling zero entry,  where this sampling is also guided by the gradient. Evaluate with this new perturbed masking, accept it if it improves the optimization objective.

### Strengths
- The paper is clearly organized and easy to read. The proposed algorithm is described clearly. 
- The experiment setup is very reasonable, with comprehensive evaluation metrics. 
- The empirical experiment results are positive.

### Weaknesses
 - I would love to see a couple more baselines to be compared. For example, I think leave-on-out is a classic baseline not included here. You could also compare with attention-based methods (e.g., selecting most important tokens with highest attention weights). I know there are flaws with these methods but there are all well-known baselines for token-level attribution that I think would be good to include.

 - I would love for the authors to further highlight the novelty of the proposed method. Right now it feels like a pretty standard discrete optimization method. Gradient-guided search is nothing new and it's been widely used in prior adversarial attack / attribution literature (e.g., "Universal and Transferable Adversarial Attacks on Aligned Language Models"; "HotFlip: White-Box Adversarial Examples for Text Classification"). And the idea of sampling a perturbation and updating the current masking with some acceptance criteria is also standard discrete optimization style (e.g., MCMC). 

 - This is pretty minor but the case study in Sec 5.5 isn't super informative to me. Maybe you could consider using some downstream applications to illustrate the usefulness of the proposed method, like the experiments done in a recent (concurrent) paper: "CONTEXTCITE: Attributing Model Generation to Context".

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors identify a weakness of current prompt attribution methods : The interaction effects of tokens within the prompt are usually disregarded because of the combinatorial cost of evaluation.  To enable a search for the 'most important' tokens, they test a mask optimisation procedure where a fixed number $k$ mask positions are chosen for evaluation, and then local moves (one masked position is moved for each new evaluation) are made to search for the best set of mask positions overall.  A number of experiments are performed and the results show that the method produces better sets of attributions than previous methods.

### Strengths
The problem that has been identified (i.e. others not looking at the joint effects from prompts) seems real.  There also seems to be a genuine advantage in searching for a better optimum point using the local search method proposed.

### Weaknesses
L288 : The "Theoretical Guarantee" proof that the procedure "theoretically converge to the local optima given enough iterations" (L288) seems tautological, since the definition of local implies accessibility by 1-step swaps.  Clearly a global convergence proof would be much nicer to have, but the local version does not seem like it provides any real 'power' in the necessary direction.

L434 : "our algorithm solves the combinatorial optimization problem efficiently" seems like it is claiming global optimisation.  Perhaps "aims to solve"?

Minor tweaks:
* L014 : "elucidating and explaining" ... are these technically different?  Would "understanding" work instead?
* L024 : "both faithfulness and efficiency" -> "both the faithfulness and efficiency"
* L032 : "limited understanding on" -> "limited understanding of"
* L073 : "probabilistic updaten for" -> "probabilistic updates for"
* L139 : "notions depicting the LLM" -> "notation for the LLM"
* L142 : "Notions on LLM Generation" -> "LLM Generation Notation"

### Questions
How was the value of $k$ chosen?  And (to get an idea of the scale of the combinatorial problem) how many tokens are generally within a prompt?  

In the initialisation of L266 - how often are the final $k$ mask positions chosen from the initial (say) top-$2k$?  Could we safely reject all but the top-$2k$ tokens from consideration?

Suppose we start with two different mask patterns (for a given $k$, say : 0..01.....1 and 1.....10..0).  What percentage of the time would Algorithm 1 arrive at the same final mask for both?  Figure 4 suggests that even a sequence of gradient-proposed local moves moves towards a global minimum slowly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper primarily addresses the task of prompt attribution, which involves identifying the input tokens that have the greatest impact on model output, and proposes an iterative computation method, JoPA, that can simultaneously identify multiple important tokens. Specifically, JoPA begins with an all-ones mask matrix and calculates the gradient produced on the mask matrix by the results with $p(y|m \odot x)$ (using the mask matrix $m$) and $p(y|x)$ (without the mask matrix). Based on the gradient values at different indices of the mask matrix, JoPA selects the Top-k indices with highest values to fill with zero (where k is a hyperparameter of the algorithm). However, the mask matrix generated by this step alone is not sufficiently effective, thus JoPA requires further iterative optimization. More specifically, during an iteration, JoPA samples from the sets of indices where the values are 0 and 1, according to the previously calculated gradient values, swaps the values of these two indices, and then performs model inference. If the result generated by the model deviates more from the original model output than in the previous iteration, the mask matrix from this iteration is retained; otherwise, it is not. Experimentally, the paper uses multiple metrics such as BLEU, ROUGE, and SentenceBert to measure the disparity between texts generated from the masked input versus the original generation across three datasets on two large language models (LLMs).

### Strengths
The proposed method has the following advantages in the task of prompt attribution: JoPA can search for combinations of multiple tokens, rather than one by one; benefiting from the guidance of gradient information, JoPA's search efficiency is relatively high.

Experimentally, the paper uses a robust evaluation system with multiple metrics and dimensions to measure the differences in output before and after input masking.

The writing is logical, comprehensive, and considerate of the problem.

### Weaknesses
 * **Insufficient contribution to the field.** This work may be a commendable improvement for readers focused on this niche area, but for the broader audience of ICLR, which mainly consists of machine learning and deep learning researchers, the gains from reading this paper might not be significant if they do not engage in prompt attribution tasks. A deeper, impactful work in a niche would fully demonstrate the method's significance in specific applications, but this paper only uses a brief text in the main body and two examples in the appendix to describe this, lacking statistical significance and persuasive power. Additionally, while the paper seeks tokens with the greatest impact on output, it does not consider whether the output contains unsafe or toxic content, as these are aspects of the model's behavior, not simply reducible to output differences. For example, the model might generate two outputs with significant differences, both containing some form of toxicity. However, is the method only limited to the prompt attribution task? I think not. Essentially, the paper identifies the most impactful tokens from the current model input, which could directly apply to detecting important tokens, but conversely, another potentially more interesting application could be in prompt compression (retaining words with significant output impact while removing less impactful ones) or prompt optimization (trying to replace impactful words to improve performance). These are directions worth considering by the authors. If effective in more areas, this paper would undoubtedly be more impressive.

* **Theoretical proofs lack persuasiveness.** In the last part of Section 4, the paper uses reductio ad absurdum to theoretically prove that the method will eventually find a local optimum after infinite searches. However, this lacks persuasiveness. First, it does not prove that a local optimum can be found within a limited number of iterations. It merely states that if a better local point is sampled, it will be accepted by the algorithm, which is obvious; second, the mask is sampled based on gradients, and gradients play a very important role in guiding the mask generation process, yet this factor is not considered in the theoretical proof stage, as there is no explicit evidence that gradient information is correct in performing the prompt attribution task. Thus, the proof may have flaws.

* **Some explanations of concepts are unclear.** For example, the author states in the discussion of related work that some studies are only applicable to next-word prediction, yet the scenario applied by this paper, large language models, also involves next-word prediction, without clearly distinguishing the differences between related work and this paper. Additionally, the paper mentions prompt attribution at the beginning without any explanation, which could be quite unfamiliar to readers not from this field.

* **Experiments to demonstrate method effectiveness are still lacking.** Only extracting 110 data samples per dataset seems too few. Additionally, are there simpler, more direct methods, such as writing some rules and then prompting LLMs to determine the most important words in input sentences? How effective is ChatGPT in this task? Lastly, the paper compares random methods and related works from 2017 and 2023, and an early 2024 study (ReAGent) introduced in the paper, but does not perform experimental comparisons.

* The paper's narrative sometimes uses excessive verbiage; consideration should be given to appropriately simplifying the description of the method.

* **Some typos and format errors.** 
1. The headers of Tables 1 and 2 are above the tables, which does not comply with the ICLR template.
2. Tables 1, 2, 3, 5, 6, 7, and 8 lack punctuation in their descriptions.
3. The terms Llama2(7B-Chat) and LLaMA-2(7B-Chat) are used inconsistently.
4. Figures 3 and 4 are not aligned properly.
5. Line 743 should replace a punctuation error; there are many such errors throughout the text.
6. In line 118, "in the the generated output" -> "in the generated output".
7. In line 195, "the pipline of" -> "the pipeline of".

### Questions
* The first computational step of Algorithm 1 involves calculating the gradient produced on the mask matrix by the results with $p(y|m \odot x)$ and without the mask matrix $p(y|x)$, but at this point, the mask matrix is initialized as an all-ones matrix, meaning it does not change any model input. In this case, $x$ and $m \odot x$ should be the same, so $p(y|x)$ and $p(y|m \odot x)$ should be the same, and if so, how would a loss of 0 produce a gradient?
* The paper uses Figure 1 to explain its method, but the right side of this figure, which uses gradients to guide mask generation, is too vague and needs revision. Additionally, why would gradients occur on the mask? Was the mask implemented as a learnable parameter?
* The K in the paper's method is a hyperparameter, but in real scenarios, we do not know how many K should be set. Could an optimization algorithm consider this parameter? Intuitively, K would have a significant relationship with the length of the input sentence.

### Soundness
2

### Presentation
3

### Contribution
2
