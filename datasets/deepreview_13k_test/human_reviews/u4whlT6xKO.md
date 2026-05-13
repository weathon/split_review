# Fine-Tuning with Divergent Chains of Thought Boosts Reasoning Through Self-Correction in Language Models

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Requiring a Large Language Model to generate intermediary reasoning steps has been shown to be an effective way of boosting performance. In fact, it has been found that instruction tuning on these intermediary reasoning steps improves model performance. In this work, we present a novel method of further improving performance by requiring models to compare multiple reasoning chains before generating a solution in a single inference step. We call this method \textit{Divergent CoT} (DCoT).
We find that instruction tuning on DCoT datasets boosts the performance of even smaller, and therefore more accessible, LLMs. Through a rigorous set of experiments spanning a wide range of tasks that require various reasoning types, we show that fine-tuning on DCoT consistently improves performance over the CoT baseline across model families and scales (1.3B to 70B). 
Through a combination of empirical and manual evaluation, we additionally show that these performance gains stem from models generating multiple \textit{divergent} reasoning chains in a single inference step, indicative of the enabling of \emph{self-correction} in language models.
Our code and data are publicly available

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Divergent Chain of Thought (DCoT), which generating multiple reasoning chains in a single inference step in order to improve model reasoning. Given a reasoning problem, the approach fine-tunes models on data that includes multiple chains of thought for that problem. The approach is evaluated across different model sizes (1.3B to 70B parameters) and various reasoning tasks. The paper claims that DCoT consistently outperforms CoT baselines, works well on different model sizes, generalizes to unseen tasks, and enables models to self-correct their reasoning.

### Strengths
-The method is evaluated on models of varying size as well as diverse reasoning tasks.

-The approach is natural and (to the best of my knowledge) novel.

-It would be relatively straightforward to implement the method with new tasks or at a larger scale.

-The hint of self-correction in the results would be very interesting if it is real. 

-The paper is well-written, and clear about experimental details.

### Weaknesses
I am generally concerned about the inferences drawn from the experimental results. There are a number of cases where the experimental results do not, as presented, support the authors' claims.

-The out of domain generalization results are weak. The hyperparameter k which controls the number of sampled CoTs is not estimated on a separate validation set. Performance only improves when k is post-selected for maximizing test set performance. This is not a fair way to evaluate the method. In addition, the paper does not report the performance of Llama2 70B on the out of domain tasks.

-Table 12 suggests that there is at most a very small benefit (and in most cases no statistically reliable benefit) from using DCoT@1 compared to DCoT@k for k>1. This suggests that diversity at inference-time is not reliably improving results.

-The results do not currently include 95% confidence intervals. From tables 10 and 11, many of the test sets have sample size of 1500 or less. For these datasets, the confidence intervals will be at least as wide as +/- 0.03. This means that many of the measured effects of DCoT will be non-significant.

-The DCoT@1 vs DCoT@2 comparison reported in Table 6, which is used to support the argument that DCoT models are self-correcting, does not appear to be significant. 62% of tasks (25 out of 40) show an improvement with DCoT@2, but the confidence interval includes 50%.

-The manual evaluation of self-correction only evaluates cases where DCoT@1 is incorrect while DCoT@2 is correct. It concludes from this evaluation that DCoT induces self-correction behavior. However, this ignores cases where the second reasoning chain in DCoT@2 introduces an error that was not present in the first reasoning chain. The results may not indicate true self-correction, but rather random variation in the reasoning chains. Table 7 may address this issue, but it is not clear how many of the responses have been filtered by the requirement that the first CoT in DCoT@3 matches DCoT@1.

### Questions
Why is self-correction only manually evaluated for Llama2 7B? It seems more likely that this ability would emerge for a larger model like Llama2 70B.

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
The paper investigates the impact of training LLMs with multiple chain-of-through traces.
Alternative chain-of-thought traces are generated for the training data, then filtered to only contain those that produce the correct answer.
A fine-tuned model is trained to generate multiple CoT in one sequence, given a parameter k that determines the number of CoT.
At inference time, k > 1 is given to slightly improve performance on some tasks.

### Strengths
The idea of the paper is potentially interesting.
The paper reports on several different base models and a number of different benchmarks, which is good to see.
There is also an attempt to investigate the underlying impact to the model, which is commendable, although there are some issues (see below).

### Weaknesses
It is unfortunate that only Llama2 is reported, given that Llama3 and 3.1 are available and achieve much better performance on these benchmarks. 
It is unclear whether the findings generalise to the current generation of models.

In Section 3.5 it is claimed that using instruction-tuned base models would be unfair, therefore non-instruction-tuned versions are used. 
It is entirely unclear why that would be unfair, if both COT and DCOT started training with an instruction-tuned base model.
In fact, the overall performance would probably be higher on the benchmarks and the results would be more realistic.
Showing improvements on an intentionally weak baseline makes the conclusions less convincing.

It seems a bit unfair to tune the k for each dataset separately, given that the COT baseline doesn't receive such tuning.

If I understand correctly, one model is trained on all the training sets at the same time. 
Which is different from the normal setup of training with a particular training set, making the results uncomparable to other published work.

"The best performance of our model is achieved with more than one CoT in 25 cases out of 32 dataset × LLM combinations"
There are 4 possible values of k and at 22% of them k=1 was the best - that result isn't much better than random.

Section 5 tries to prove that the model is performing self-correction but the methodology is not convincing.
First, it is assumed that there are only two possible sources for the performance difference - self-ensembling or self-correcting - but there could be many other reasons. For example, the DCOT model could be benefitting just from having a larger number of in-domain tokens in the context at inference time. Eliminating self-ensembling does not prove that self-correcting is the reason.
Furthermore, self-ensembling also cannot be ruled out like this. Two models can still be ensembled, there doesn't need to be a majority vote, as long as there is information sharing.

In line 419 it is presented that k=2 is better than k=1 in 62% of the cases. But given that 50% would be random chance, that isn't a particularly convincing result.

Most of the performance improvements are not very large, particularly considering that they are using previous-generation base models and therefore have much room for improvement.
There really should be significance testing to actually show that the improvements are not just due to randomness.

In Section 5.2:
"Of these instances where the first reasoning chain is shared, we observe that in 45% of the cases, the second CoT of DCoT@2 exhibits a different reasoning pattern from the first."
This result isn't really showing much. If the model has 50% probability of generating a correct or incorrect CoT, then this result would be consistent with that.
These examples where specifically chosen based on the first CoT being incorrect. How does the second CoT affect cases where the first CoT is correct? If it is still 45% likely to be correct then that would imply a disadvantage instead.

### Questions
The prompt in Section 3.2 has an "Options" field. What are the options? This doesn't seem to be mentioned anywhere.

It is said that Llama2 70B is reported only on the dev set due to "the costs for hyperparameter tuning".
In fact, the appendix mentions that the results are not even on the full dev set but only a small subset (this should be made clear in the main paper).
Surely the training of the 70B model takes much more resources than inference? If you were able to train the model, why would you not be able to test it on the test set (without doing hyperparameter tuning, sure)?

"We then randomly sample five instances per dataset, resulting in a total of 33 samples."
33 does not divide by 5. What happened there?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Divergent Chain of Thought (DCoT), a  method for enhancing the reasoning capabilities of large language models (LLMs). DCoT prompts LLMs to generate multiple reasoning chains, fostering a divergent exploration of potential solutions. Subsequently, the model analyzes these diverse chains to identify the most accurate answer through a convergent process.

Empirical validation of DCoT's efficacy is provided through extensive experimentation across various reasoning tasks, model families, and scales. Results demonstrate consistent performance improvements compared to conventional Chain-of-Thought (CoT) techniques. 

This study offers valuable insights into augmenting LLM reasoning abilities by promoting internal self-evaluation and correction mechanisms, thereby contributing to the development of more reliable and robust reasoning capabilities in future language models.

### Strengths
The main contributions of the paper are as follows:

(a)  This method augments the traditional Chain of Thought (CoT) prompting technique by generating multiple, divergent reasoning chains before converging on a final answer.

(b)  Through rigorous experiments, the authors demonstrate that fine-tuning LLMs on DCoT datasets significantly improves their performance compared to the traditional CoT baseline across various model families and sizes (from 1.3B to 70B parameters). The improvement is consistent across a range of tasks requiring different reasoning types, including math, logic, symbolic reasoning, and multi-hop reasoning.

(c) Notably, DCoT exhibits a beneficial side effect - it enables LLMs to self-correct without external feedback or prompt optimization

### Weaknesses
If the authors could provide the following details it would make the paper even stronger:

(a) Diversity of CoTs Generated by Different Prompt Suffixes --  they do not directly evaluate or discuss the diversity of the CoTs generated by these different suffixes. It would be good to understand how different the CoTs are 

(b) While the authors described how multiple CoTs are generated in DCoT, the provide limited information on the exact convergence mechanism used to arrive at a final answer based on these diverse reasoning chains. 

(c) The results in Table 3 demonstrate that while increasing the number of generated CoTs (k) generally improves performance, there are cases where increasing k leads to a performance drop, the author should provide some explanation to that.

DCoT's performance gains are not uniform across all tasks. For instance, on StrategyQA, the only boolean question-answering dataset used, CoT sometimes outperforms DCoT. This is attributed to the limited range of possible answers in boolean tasks, where the need for divergent reasoning might be less pronounced. Similarly, the results on LLaMA-2 13B for unseen tasks are mixed, with significant gains observed only in non-math domains. These findings suggest that DCoT's effectiveness might be influenced by the nature of the task and the complexity of the reasoning required. 

Increased Computational Cost Compared to CoT: Generating multiple CoTs in a single inference step inherently requires more computational resources than generating just one, as in the traditional CoT method.

Added Complexity in Training Data Generation: Creating training data for DCoT involves generating multiple correct CoTs for each question, which is a more complex and potentially time-consuming process than generating single CoTs.

### Questions
Please refer the previous section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces *Divergent Chain of Thought* (DCoT), a method for inducing multiple chains of thought in a single inference call from LLMs. Specifically, the paper focuses on *DCoT fine-tuning*, where LLMs are instruction-tuned using *DCoT data*, which includes instances where a question is paired with multiple valid reasoning chains. The paper evaluates DCoT across various reasoning benchmarks, comparing its performance with LLMs instruction-tuned on standard CoT data, where each instance represents a question paired with a single valid reasoning chain. Additionally, the paper provides an analysis of the individual reasoning chains produced in a single DCoT inference, examining the soundness of subsequent chains. Finally, it discusses the implications of this analysis, arguing that DCoT promotes a self-correcting mechanism within the model.

### Strengths
Positive aspects include the following:
- The paper is clearly written and easy to follow.
- The paper uses open-access LLMs and reports both training parameters and hyperparameters for DCoT. Furthermore, a link to an anonymized GitHub repository is provided, thereby facilitating reproducibility.
- Experiments have been conducted across various benchmark datasets, with some models evaluated using multiple random seeds.
- The observation that DCoT@1 approximates the performance achieved by fine-tuning on CoT data, suggesting that DCoT@k could be effectively viewed as a natural extension of CoT fine-tuning.

### Weaknesses
The paper’s main weaknesses are:
- DCoT promotes the generation of multiple reasoning chains before arriving at a conclusion, which significantly increases token generation relative to the standard CoT approach considered. This increased computational cost is not sufficiently discussed in the paper.
- The comparison between DCoT and CoT in Tables 2, 4 and 5 seems to be based on unfair grounds. Given that DCoT involves generating multiple reasoning chains, a more appropriate, fairer comparison would be between DCoT and CoT combined with Self-Consistency (CoT + SC). While Table 2 includes this comparison, Tables 4 and 5 omit the corresponding results. The authors themselves acknowledge in lines 233-234 that the selected out-of-domain evaluation tasks benefit from self-consistency, making a DCoT vs. CoT + SC comparison much more fair. Notably, Table 2 indicates that DCoT only outperforms CoT + SC for Phi models, whereas CoT + SC generally yields better performance than DCoT with Llama-2. This is not sufficiently discussed in the paper.
- Several claims are too strong and do not seem to be sufficiently supported by the experimental evidence provided. For instance:
  - The "in-domain effectiveness of DCoT" (ll. 249-250) is overstated as "consistent and significant." (ll. 261-262). While DCoT may offer performance gains over CoT, these improvements are not “consistent” across different dataset-model pairs (e.g., Llama-2-7B on StrQA). Moreover, for several datasets, the gains are marginal, calling into question the “effectiveness” of DCoT, especially given its higher computational cost relative to CoT.
  - The statement that “DCoT is effective for any k > 1” (lines 308-309) does not align with the experimental evidence, particularly in Table 3. For instance, increasing k degrades performance for Phi 1.5, and results such as DCoT@2 outperforming DCoT@4 on Llama-2-13B indicate that performance does not always increase with k. No evidence suggests that higher values, such as k = 10, would not decrease performance compared to DCoT@1.
  - The claim that “DCoT has the ability to self-correct” (line 500) is not supported by Section 5’s analysis. For example, while Table 6 shows that generating two reasoning chains improves outcomes in 62% of cases, the remaining 38% of cases do not benefit (potentially introducing rather than correcting an error). Additionally, the experiments in Section 5.3 reveal that when a second CoT generation produces an error, a subsequent attempt does not necessarily self-correct it (A, B, B pattern). Consequently, the notion of DCoT’s self-correction ability lacks adequate empirical support. Instead, the model seems to sometimes produce a second correct CoT, while other times it produces an incorrect one.
- There exist newer, updated versions of the models evaluated in this work (e.g. Llama-3.1). Furthermore, only one model family of size > 3B and one model family of size < 3B have been considered.

### Questions
Suggestions for the authors:
- In several instances, the paper employs language that anthropomorphizes LLMs. For example, the expressions “a second thought can be beneficial to find the answer” (lines 199-200) and “an overthinking effect” (line 313) imply cognitive functions. While these terms may lend an intuitive appeal to describing the LLM's reasoning process, they risk creating a misleading perception of the model's actual internal workings.
- The term “significant” should be used with care. For instance, in lines 261-262, the authors state, “DCoT achieves consistent and significant performance gains compared to CoT.” However, without a statistical significance test, this terminology may be misleading and should not be used in this context.

Questions for the authors:
- How many CoTs were sampled for the self-consistency (SC) experiments, such as for CoT + SC in Table 2?
- Have the authors conducted CoT + SC experiments for models on unseen tasks (Table 4) and Big Bench Hard (Table 5)?
- How do the authors respond to the view that the model does not engage in self-correction but rather generates additional reasoning chains, which independently vary in accuracy from the preceding reasoning chain (sometimes correct, sometimes incorrect)?

### Soundness
2

### Presentation
2

### Contribution
2
