# ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Retrieval-Augmented Generation (RAG) models are designed to incorporate external knowledge, reducing hallucinations caused by insufficient parametric (internal) knowledge. However, even with accurate and relevant retrieved content, RAG models can still produce hallucinations by generating outputs that conflict with the retrieved information. Detecting such hallucinations requires disentangling how Large Language Models (LLMs) utilize external and parametric knowledge. Current detection methods often focus on one of these mechanisms or without decoupling their intertwined effects, making accurate detection difficult. In this paper, we investigate the internal mechanisms behind hallucinations in RAG scenarios. We discover hallucinations occur when the \textit{Knowledge FFNs} in LLMs overemphasize parametric knowledge in the residual stream, while \textit{Copying Heads} fail to effectively retain or integrate external knowledge from retrieved content. Based on these findings, we propose \textbf{ReDeEP}, a novel method that detects hallucinations by decoupling LLM’s utilization of external context and parametric knowledge. Our experiments show that ReDeEP significantly improves RAG hallucination detection accuracy. Additionally, we introduce AARF, which mitigates hallucinations by modulating the contributions of Knowledge FFNs and Copying Heads. %These methods demonstrate notable improvements in both hallucination detection and mitigation in RAG models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method for detecting hallucinations of Retrieval Augmented Generation (RAG) models in the scenario when retrieved context is accurate and relevant. 

The authors hypothesize that hallucinations are caused by models ignoring the retrieved context and overemphasizing their parametric knowledge. To capture these concepts they introduce two auxilary scores: External Context Score (ECS) that reflects utilization of the retrieved context by the model, and Parametric Knowledge Score (PKS) that reflects utilization of the parametric knowledge. Hallucinations are then predicted by thresholding a hallucination score H which is computed as a weighted sum of ECS and PKS.

In addition to that, the authors propose a method to reduce hallucinations by suppressing outputs of attention heads that contribute to low ECS and outputs of fully-connected layers that contribute to high PKS.

### Strengths
- Authors provide a straightforward method to detect hallucinations in RAGs that does not require model fine-tuning.
- Empirical results provided by the authors look good.

### Weaknesses
## Lack of justification for PKS and ECS

### No PKS justification
Although PKS is correlated with a hallucination label (line 319) there is still no guarantee that it is adding parametric knowledge. Since you do not provide any theoretical justification for this score, at least an empirical justification is needed. You can run a simple experiment: use LogitLensed outputs before FFN as final outputs and check whether it removes the parametric knowledge bias using some of the setups for that, for example, the one from [1] (they study it through the prism of the phenomenon you encounter in RQ3 and Appendix E).

### Questionable ECS justification
Contrary to the PKS the authors provided empirical justification for the ECS measuring model reliance on context, however, I find it not very convincing so far.

First of all, I do not see how the ratio of attention head attending vs mis-attending justifies ECS. It would make more sense to me if you provided such a ratio for mulitple different values of ECS and observed that the higher the ECS the more often a model attends.

Secondly, I am not sure that ratio of attending is computed correctly. As far as I understood for LLama-7B you take hallucinated response (which means that it contradicts external context) and the most attended span in external context. Then you ask gpt-4o to evaluate whether this span supports existence of a conflict in response or not. If that is the case, I do not understand why this experiment shows whether the model attends (the attention span contains part of the context needed for the correct answer) or mis-attends. If attention span supports the existence of a conflict in response it might still not be relevant for the correct response itself, which means a conflict exists but we can not call it a hallucination according to your definition (hallucination = response is contradicting the context or is not supported by it - line 72).

Please correct me if I misunderstood the experiment setting, what is meant by attending, or the way attending and mis-attending is computed.

## Too many hyperparameters
I am afraid that the proposed hallucination detection method is not applicable in practice as it requires a lot of manual hyperparameter tuning. According to the provided values, they all are different per dataset and model (see Appendix I). They include:

- top k % for ECS 
- top k % for PKS
- tau threshold for H - page 8 bottom
- alpha and beta for reweighting page 9 top
- chunk size for the chunked version of REDEEP

I suggest that the authors discuss strategies for automating hyperparameter selection or provide guidelines for choosing these parameters in real-world applications.

## Insufficient experiments

### Hallucination detection experiment
- For RagTruth dataset there exist baselines provided by the original paper [2] which perform better than all the baselines considered by you, could you please include them? E.g. Baseline LLama2-13B results fine-tuned on RagTruth have 78.7 F1, see Table 5 in [2] vs yours 78.3 in Table 1. I think the comparison makes a lot of sense since you tune many hyperparams using RagTruth validation dataset while you could simply fine-tune that baseline on the same data instead.
- Same comes for Dolly dataset, please include results for AlignScore and RepC-LE-nn-n2000-e2000 that have 84 and 86 accuracy correspondigly, while the best method provided by you scored 73.73 (LLama2-7B).
- Please also provide results for the Noisy Context split from Dolly [3] dataset because it better approximates realistic RAG application scenario. 

### Causal experiment

- First of all, I don’t see how a higher NLL difference for the experimental group than for the control group shows a causal relation between hallucinations occurrence and copying heads neglecting necessary knowledge, could you please elaborate?
- The experiment results are very noisy and it is hard to draw any conclusions from them, for example, boxplot of the experimental group is fully contained within the boxplot of the control group in Figure 5 (b). 
- It is not clear how many heads are within experimental and control groups, it can be the case that loss changes are bigger for the experimental group simply because it intervenes in more heads.

### Hallucination generation experiment

Prompt for truthfulness (Appendix L) creates bias, since GPT-4o knows which answer belongs to the baseline and which to AARF. It can influence its answers since usually in scientific papers named methods outperform baselines, which must have been the case on chatgpt training data as well and possibly created such a bias. 

Instead, it would be nice to see the results for prompts that contain anonymous names (e.g. model 1 and model 2 instead of baseline and AARF) to avoid the mentioned naming bias and have a randomly shuffled order of AARF and Baseline inputs before showing to GPT-4o to avoid positional bias.

### Lack of sensitivity experiments
Please provide sensitivity experiments to the numerous hyperparameters you introduced (see the section "Too many hyperparameters" for the hyperparameters)

## Unclear writing
- While being core concepts of the paper, Copying Heads (set A) Knowledge FFNs (set F) are not formally defined (line 381). I guess set A is built by taking top-k attention heads after sorting them by ECS while set B is built by taking top-k FFNs after sorting them by PKS, but I could not find it in text.
- Strange ordering equations, for example, Eq. 2 that defines an important part of ECS has an undefined value “a” which is only introduced in Appendix Eq. 8.

## Typos
455: REDEPE

### Questions
- Why LLama2-7B (smaller and older version than others) has better results on Dolly in terms of F1 or Accuracy in Table 1?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Retrieval-Augmented Generation (RAG) models are still prone to hallucinations. This paper explores the internal mechanisms behind hallucinations in RAG settings. Building on these insights, the authors propose a hallucination detection method, ReDeEP, and a RAG truthfulness improvement method, AARF.

### Strengths
Each step is thoughtfully motivated, with both conceptual reasoning and empirical validations in §3. The detection method shows effective results in Table 1, and the RAG truthfulness improves using AARF, as shown in Figure 6.

### Weaknesses
Figure 3 is problematic. The starting point and flow of the diagram are unclear, with too many arrows, making it hard to identify the main computational paths. An effective graphic would show one main data processing pipeline, which is missing here. Additionally, the quantities computed are not well-defined. Panels (b) and (c) add no extra information and could be removed without loss.

Otherwise, rather minor points:
- l.281: Please describe the number of hallucinations and non-hallucinations (h = 0 and h = 1) in the evaluation set.
- Pearson's Correlation in §3: Why measure Pearson’s correlation between ECS and hallucination labels (binary)? It would be more informative to report accuracy at a fixed threshold or detection metrics such as AUROC. Similarly, for PKS and hallucination, detection metrics like AUROC would be preferable.
- l.465: Could you clarify the criteria for selecting thresholds for accuracy, recall, and F1?

Even more nits:
- Use full names for FFN, ReDeEP, and AARF, at least in the abstract.
- In Figure 4(c), clarify what the colour bar values represent.
- Overall, font sizes in the figures are too small.
- Structure in §3.2 is difficult to follow. Stick to a standard structure using \section, \subsection, \subsubsection, \paragraph, etc., rather than introducing new hierarchies (boldface, underline, italics, numbering (1), (2), …).

### Questions
The paper offers valuable insights into how RAG-based LLMs produce hallucinated outputs. Building on these findings, it proposes a detection method and mitigation strategy grounded in this understanding. Presentation issues remain, particularly in the main figure explaining the method, yet the contribution is significant.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes ReDeEP - a method to detect hallucinations by LLMs in retrieval augmented generation settings by using mechanistic interpretability. The authors introduce two novel metrics - (1) the External Context Score (ECS) and (2) Parametric Knowledge Score (PKS) to identify when hallucinations happen because of over reliance on internal knowledge or from the underuse of external information. The authors also introduce AARF (Add Attention Reduce FFN), which aims to adjust the weights of the attention heads, and feed forward layers to reduce hallucinations.  Their approach is empirically validated on standard benchmarks, demonstrating superior performance to existing methods.

### Strengths
1. The development of the ECS and PKS metrics to understand the contributions external and internal knowledge have on the LLM's generation is a compelling and novel way to understand LLM outputs. 

2. They demonstrated great empirical validation by running extensive experiments across two datasets, three LLMs, and many baseline methods. 

3. They also introduce a method to curb hallucinations called AARF - which relates back to the introduced metrics nicely.

### Weaknesses
1. Performing this analysis at the token/chunk level might limit its practicality in real time or large scale settings - it would be nice to have a richer discussion of the trade-offs and real world feasibility. 

2. The experiments are extensive - however they are all with the LLama family of models - testing (even a much smaller set) on a different model would be informative. 

3. While the performance of AARF seems good (Figure 6) - it would be good to see some example outputs - its unclear how this could effect the model’s output in terms of coherence/writing in general.

### Questions
1. Could you discuss more the trade-offs of your method? In particular thinking about real time settings? 

2. Have you tested your method on non-LLama models? Do you anticipate any challenges for different models? 

3. Could you provide some example outputs pre and post using AARF? Or can you speak to the effect AARF has on the coherence of the model’s output after AARF?

### Soundness
3

### Presentation
3

### Contribution
3
