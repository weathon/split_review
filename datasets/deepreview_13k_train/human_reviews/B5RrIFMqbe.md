# FormalAlign: Automated Alignment Evaluation for Autoformalization

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Autoformalization aims to convert informal mathematical proofs into machine-verifiable formats, bridging the gap between natural and formal languages. However, ensuring semantic alignment between the informal and formalized statements remains challenging. Existing approaches heavily rely on manual verification, hindering scalability. 
To address this, we introduce \method, the first automated framework designed for evaluating the alignment between natural and formal languages in autoformalization. \method trains on both the autoformalization sequence generation task and the representational alignment between input and output, employing a dual loss that combines a pair of mutually enhancing autoformalization and alignment tasks. Evaluated across four benchmarks augmented by our proposed misalignment strategies, \method demonstrates superior performance. In our experiments, \method outperforms GPT-4, achieving an Alignment-Selection Score 11.58\% higher on \forml-Basic (99.21\% vs. 88.91\%) and 3.19\% higher on MiniF2F-Valid (66.39\% vs. 64.34\%). 
This effective alignment evaluation significantly reduces the need for manual verification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FormalAlign, an automated alignment evaluation framework designed for autoformalization tasks. FormalAlign addresses the challenge of ensuring semantic alignment between informal and formal mathematical statements, a critical issue given the limitations of traditional manual verification methods. By employing a dual loss framework that combines cross-entropy loss and contrastive loss, FormalAlign enhances its alignment detection ability in a comprehensive way. Evaluations on FormL4 and MiniF2F demonstrate FormalAlign’s superior performance over GPT-4, with notable improvements in precision scores.

### Strengths
- FormalAlign demonstrates high precision across two major datasets, maintaining robust recall scores. 
- In the LLM-as-judge setting detailed in Appendix G, FormalAlign notably outperforms GPT-4o in identifying nuanced misalignments and step further to human experts' level.
- FormalAlign's approach shows strong potential for enhancing the quality of autoformalized statement datasets in Lean, providing a valuable contribution to training more effective automatic theorem-proving models.

### Weaknesses
 - The misalignment strategy "Change of Variable Type" in Table 2 may create examples that should be considered aligned rather than misaligned. Specifically, the example provided, where the variable type is changed from real numbers (R) to rational numbers (Q), does not necessarily create a misaligned example. The original natural statement does not explicitly require the variable to be real numbers. The proposition with the variable in Q still accurately reflects the original question. 
- The misalignment strategies discussed in the paper appear to be primarily applicable to high-school-level mathematics or below. When dealing with more advanced mathematical statements, such as those only involving logic, quantifiers, or set theory, half of the proposed misalignment methods, including constant modification, exponent modification, and modification of equality, become less relevant or inapplicable. This limitation suggests that the strategies may not generalize well to more complex mathematical domains.
- A more extensive ablation study to determine the optimal balance between the two components of the loss function, $ L_{CE} $ and $ L_{CL} $, is recommended. Specifically, the study could explore how different balancings affect the model's performance on the pure autoformalization task. Understanding this balance could provide insights into the trade-offs between the two loss components and potentially enhance the model's ability to accurately formalize mathematical statements.
- The ablation experiment in Section 5.2 may not effectively demonstrate the benefits of combining cross-entropy and contrastive loss, as these two loss functions have distinct objectives and may steer the training process in different directions. This discrepancy is particularly pronounced when using the hidden state of a decoder-only model, which is not inherently optimized for capturing semantic information. Since the alignment-selection metric (the average of certainty and similarity scores) naturally favors models trained with the combined loss, the improvement in scores may reflect a metric bias rather than a genuine enhancement from the augmented loss.

### Questions
Have you considered splitting the alignment-checking baseline for GPT-4 into two steps: back-translation followed by a natural language alignment check? This approach could encourage GPT-4 to capture more details during the back-translation phase and minimize any impact from its limited familiarity with Lean during the alignment-checking stage.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose to check the alignment between informal and formal mathematical statements using a model trained both on the autoformalisation and alignment tasks. This approach is automatic, avoiding the scaling issues of manually checking, while enhancing previous approaches that relied either on BLEU relative to a ground-truth statement or checking for logical consistency, since statements can be logically consistent but misaligned. To validate their approach, the authors create a dataset by mutating knowing correct informal-formal pairs using one of the following operators: modify constant, modify exponent, introduce variable, change variable type, and modify equality. Further, they also introduce misalignments by shuffling the formal/informal data for random pairings. The authors demonstrate improvements in alignment score and precision across FormL4 and MiniF2F.

### Strengths
+ Solving the autoformalisation as an autoformalisation and alignment joint task which should enable better inner representations.
+ Ablation study to empirically show the value of both tasks (hence the value of cross-ent and contrastive loss and the value of considering both sequence probability and similarity for the alignment score).
+ Empirical justification of the foundation model that is used/fine-tuned for FormalAlign.
+ "Mutation" based construction of a known ground-truth dataset.

### Weaknesses
 - Results are presented at a fixed alignment score threshold instead of P-R curves. (I suspect this is due to a lack of access to create such curves for GPT models).
- The misaligned types generated are not uniform (Figure 3)
- Model performance by misalignment type is not reported, the case study is only vs BLEU and BERTScore, which is welcomed, but a comparison with GPT-4 would also be welcomed. (A similar breakdown for the LLM-as-judge study would also be welcomed)

### Questions
1. Looking at the Table 3 results, and considering that you have an alignment threshold, would it be possible to obtain P-R curves for FormalAlign? If so, I would like to know the performance of the approach when matching GPT-4 recall (So P@(R=0.9)). Further, presenting the P-R curves would allow people to have a better understanding of the performance, while providing such curves to users of the approach for evaluation could make a more informed choice of the threshold value depending on the expected manual load afterwards.

2. Is there a reason why the strategies were applied non-uniformly to generate negative examples? (The strategies are in Table 2, while Figure 3 presents the distribution of misalignments generated.)

3. For the case study and LLM-as-judge results, do you have per-misalignment-type data? Would it be possible to report that, as it would be interesting if any category is especially difficult/easy to spot?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel framework, FormalAlign, which trains a Large Language Model (LLM) to evaluate autoformalization alignment. Beyond the standard cross-entropy loss derived from viewing autoformalization as a sequence generation task, FormalAlign incoperates a new loss term as a dual objective. This new loss measures alignment between the informal and formal versions by leveraging the cosine similarity between their representations. Experiments on the FormL4 and MiniF2F datasets demonstrate the effectiveness and robustness of FormalAlign.

### Strengths
- The paper addresses an important and relatively unexplored problem—improving the autoformalization of mathematical statements.

- The proposed framework is intuitive and easy to understand, achieving promising empirical performance on challenging evaluation datasets.

### Weaknesses
 - The discussion on the broader significance of autoformalization is lacking, which limits the accessibility of this problem to researchers in other fields (e.g., software verification). Furthermore, providing a clear formal definition of autoformalization alignment would enhance the reader’s understanding of the paper’s objectives.
-  The running example is somewhat unconvincing to me. First, in this example, the alignment issue can be detected easily by verifying whether the statement is provable. Using the lean-set tool, a counterexample [b := 7/8, a := 1/2, c := 63/160] can be found. Second, the low certainty score suggests that LLMs may only generate this example with low probability (correct me if not).  
- The construction of datasets is a bit unnatural. The authors generate negative examples by mutating correct input-output pairs, but these synthetic examples may not realistically reflect the types of errors typically produced by LLMs during autoformalization.
- The reference section contains a duplicated citation for Deepseekmath, and some related works are missing, such as [1, 2, 3].

### Questions
- FormalAlign appears to focus exclusively on statement autoformalization. Could this framework be extended to proof autoformalization as well?
- The certainty score and similarity score operate on different scales ([0,1] and [-1,1] respectively). Why are these combined using a simple average?
- The authors claim that FormalAlign can significantly reduce the need for manual verification, but only limited evidence is presented in the experiments. Could the authors provide more quantitative results on this claim? For instance, by deploying FormalAlign in a complete autoformalization pipeline, how many formalizations can be automatically verified?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a technique for automatically evaluating the semantic alignment between a natural language description and its corresponding formal representation that may be produced by an AutoFormalization system (Autoformalization aims to convert informal mathematical proofs to formal proofs that can be automatically checked by existing theorem provers). The technique is based on fine-tuning a base LLM with respect to a dual loss function that combines cross-entropy loss in the sequence generation with a contrastive loss based on cosine similarity of the informal/formal pairs. The technique is evaluated on existing datasets for autoformalization that are augmented with misalignment strategies proposed by the authors to test negative examples of incorrect formalizations. It is shown to have superior performance in many cases against GPT models prompted with a similar alignment evaluation task.

### Strengths
1. Innovative focus on the alignment problem in Autoformalization. Translating informal mathematical proofs into formal, machine-verifiable formats is an important problem in fields like theorem proving and formal verification, since formal systems (e.g. Lean, Isabelle) are highly precise but difficult for humans to use. This work brings an explicit focus on a key issue that plagues autoformalization: to ensure semantic alignment between the informal input and formal output. This is an important problem to address, since formal provers can check for syntactic but not semantic correctness with respect to the original intent, and other metrics such as BLEU scores are very imprecise. Addressing this alignment problem explicitly seems a novel angle taken by this work, and such focus could help further progress in the field of autoformalization.  

2. Dual-Task Training Approach. The technique of simultaneously training to generate formal statements and check alignment is interesting. While multi-task learning and contrastive learning have been used in other areas (e.g., machine translation, image-text alignment), the combination of sequence generation with contrastive alignment seems to be a novel application in the context of autoformalization. 

3. Clarity and presentation. Though some parts unclear (see below), in general the paper clearly explains and motivates the problem, and explains the technique well, including definitions of the combination of cross-entropy loss (for sequence generation) and contrastive loss (for semantic alignment). The evaluation covers some important aspects to show that on the synthetically augmented datasets the technique performs well in general, and also better or comparable to alignment inference based on prompting GPT models. This demonstrates the core value of the technique. The authors also  include ablation studies that provide insight into the contribution of both kinds of loss functions, as well as comparison with human evaluation.

### Weaknesses
1. Use of synthetic data for evaluation. To evaluate alignment, the authors create a synthetic dataset of negative example formalizations based on explicit misalignment strategies that they propose. I do not have a sense of how realistic those misalignments are in practical terms. I think addressing this issue is important,  especially since the whole purpose of the task is to detect the errors made by existing AF systems: we should be testing the ability to detect those kinds of variations, which could be very much smaller and more subtle than the ones produced by the explicit misalignment strategies here - would the contrastive loss be able to help distinguish between those kinds of variations (for which the task is actually intended)? While I understand such data is not readily available, I think it should be possible to obtain some real data perhaps in the following way: since you already have access to human judges (which you used for a similar task), perhaps you can run a SoTA AutoFormalization system on the standard datasets you use here, get the outputs and ask the human judges to label correct/incorrect for the formalizations produced and also provide corrected formalizations. Then just check the alignment evaluation against this data (which would provide one positive and one negative example for each case where the AF system had failed). The dataset need not be very big as it is only to be used for evaluation. Such an approach would also show the actual improvement you can make to a SoTA AF system. 

2. Lack of compelling baselines in comparison. The prompt used for GPT models Appendix C.1 seems to ask GPT to assign an "alignment score" from 1 - 5. This seems a pretty vague and not well-defined task that may be difficult for the model (or even a human) to interpret. A more well-defined question is to simply ask if the formalization correctly represents the informal NL or not - since that is the main (only) problem we are trying to solve? Scoring seems to make it a subjective/continuous domain problem - e.g. it may be possible that a given formalization correctly represents the problem, but perhaps the model may still assign it a score 4 rather than 5 due to some stylistic differences with the informal input it detects. Having a true/false binary judgement would make a more well-defined task for the model to address. Also, this seems a very obvious case of where Chain of thought (CoT) reasoning should be tried as another baseline - the evaluation task is very reasoning based and the GPT models can be expected to do much better with CoT reasoning to infer any discrepancies between the informal and formal representations - rather than just predicting some number score from 1 to 5. Especially since you do not have other baseline or SoTA methods to compare against (do there exist such methods?), using a CoT baseline is easy to implement and would be very relevant here. You also provide all the candidate formalizations in the same prompt - perhaps evaluating each one of them separately will be a better approach so not to confound the model with too many tasks at the same time. 

3. Some problems with positioning/presentation. You state in the abstract: "FORMALALIGN trains on both the autoformalization sequence generation task and the representational alignment between input and output, employing a dual loss that combines a pair of mutually enhancing autoformalization and alignment tasks." and make similar statements in the introduction. That sounds like you are addressing both the autoformalization task as well as the alignment evaluation task - but you have not shown any evaluation of the autoformalization task - if that is not an intended contribution of the work then such statements are a bit misleading or confusing in the intro and abstract. It should be clarified that you are only providing an evaluation method to test alignment of given candidate informal-formal pairs. Also, if the AF task itself is not a contribution - why not? If the combination of cross-entropy and contrastive loss accurately infers alignment, why can't the fine-tuned model based on that dual loss function be better at the autoformalization task overall? Could you have compared it to prior auto-formalization approaches? 

Typos: 
- "The challenges of automated evaluating natural language"
- "to train an FORMALALIGN"
- "Eq. equation 5. Table 6"

### Questions
1. I am confused  about the Metrics description in section 4.2. I thought this should describe the metric itself independently of the system being evaluated (whether is your system or any other baseline system). But the AS and detection metrics are defined with respect to the V_align function which seems specific to your model only and used in its inference. Is that specific for the FormalAlign model only or otherwise how are these metrics computed for the other models like GPT4? (I hope that is not the case as they would then be really problematic metrics to be using that are specific to your model). And if that is not the case then please move this discussion to the inference section - since they look like modes of inference in which your model can be used: it can either select the best formalization from a given set (selection), or return a true/false label for a given informal/formal pair (detection). The metrics are then just to measure the quality of these two selection and detection modes of inference using standard precision/recall. 


2. Similarly, can you clarify exactly how you compute AS, precision and recall numbers for the GPT models? (As above, I hope you are not computing the alignment scores for them in the exact way you describe in section 4.2). I am assuming it is based on you prompting the models to predict an "alignment score" from 1-5 as in the prompt in Appendix C2? Please confirm this is correct and it should be explained clearly in the evaluation section. Also please explain the details - how is AS inferred from 1-5 score generated by GPT model? How is precision measured? What if there are ties on the top score between multiple candidate formalizations? 


3. I dont understand the second prompt in Appendix C.2 - it is just doing a translation task? How is it used in your evaluations? Or is it just the prompt used to run your final fine-tuned model for the sake of generating and extracting the alignment scores?

4. Just to confirm - you do not use the synthetically generated misalignment data for training at all right? 

5. What is SIM() function in Figure 2? - is it the same as Cos()? If so please fix for consistency.

### Soundness
2

### Presentation
3

### Contribution
3
