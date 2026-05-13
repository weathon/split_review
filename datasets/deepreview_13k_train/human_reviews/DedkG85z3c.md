# Aligning to Constraints for Data-Efficient Language Model Customization

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
General-purpose language models (LMs) are aligned to diverse user intents, but fall short when it comes to specific applications. While finetuning is the default method for customized alignment, human annotations are often unavailable in various customization scenarios. Based on the observation that one of the main issues of LM customization is constraint adherence, we investigate the feasibility of using constraints as a bridge from general LMs to customized ones. We investigate common constraints in NLP tasks, categorize them into three classes based on the types of their arguments, and propose a unified framework, ACT (Aligning to ConsTraints), to automatically produce supervision signals for user alignment with constraints. Specifically, ACT uses constraint verifiers, which are typically easy to implement in practice, to compute constraint satisfaction rate (CSR) of each response. It samples multiple responses for each prompt and collect preference labels based on their CSR automatically. Subsequently, ACT adapts the LM to the target task through a ranking-based learning process. Experiments on fine-grained entity typing, abstractive summarization, and temporal question answering show that ACT is able to enhance LMs' capability to adhere to different classes of constraints, thereby improving task performance comparable to or approaching that of finetuning with labeled data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
# Goal an Method
This work looks at general problem of training LLMs to perform tasks where the output must fulfill some set of constraints. Their proposed training approach assumes access to some implemented constraint verification method for measuring how closely the LLM's output follows the task's constraints. Training is then done in a manner that is similar to rejection sampling: For a given, unlabeled input they first sample multiple outputs from the model before scoring and ranking outputs using their constraint verification method. The authors then update the LLM by training on two losses using these rankings: (1) the standard NLL loss of generating the best ranked sample and (2) ranking loss encouraging the model to assign greater likelihood to samples rank higher in constraint following than those that rank lower.

# Main Results
The authors experiment on a variety of tasks with different constraints: (1) Fine-Grained Entity Typing w/ Label Space and Label Hierarchy Constraints (2) Abstractive Summarization w/ Extractiveness Constraints and (3) TemporalQA w/ Event Ordering Logic Constraints.
The primary baselines used in this work are using the base LLM (w/ prompting for constraint following) and (2) finetuning on gold labels. The results demonstrate that their proposed method improves performance over simple prompting. They also demonstrate that in the first two settings, their proposed method can achieve comparable performance while reducing annotation cost. In the third setting, there is a still a significant gap between full finetuning and their proposed method.

# Additional Results
The authors demonstrate that the learned constraints can transfer across tasks (learning extractiveness constraint on table-to-text summarization transfers to text-to-text). The authors also experiment with using their constraint-following rankings to train reward models, and find it that it improves reward modeling performance on Fine-Grained Entity Typing, but still performs worse than training with gold, human-annotated labels.

### Strengths
The work is well written, clear, and technically sound. Results are generally positive, demonstrating that

### Weaknesses
 # Generalizability and Reliance on Constraint Verifier 
A significant limitation of the method proposed in this work is the reliance on the constraint verifier. This limits the utility of the proposed method, where constraint verifiers are applicable and implemented. This work also, for the most part, explores settings where constraint following is directly tied to the end task performance metric, which is often not the case. The only exception to this is the summarization setting, where the authors do find that some mixing between constraint following and standard finetuning performs best. 

# Missing Comparisons Against Existing Methods
The proposed training approach is very similar to standard training methods like rejection sampling and preference learning methods (e.g., DPO) , where the constraint verification evaluator is used in lieu of a reward model. The most significant differences are seem to be minor changes to the learning objective (Loss function in L218 and L222), and response sampling method (Section 3.3). Describing the differences between the proposed training approach and experiments comparing the proposed method against these standard approaches and ablations using different response sampling methods would help determine the differences and the impact of these changes in moving from a reward-maximizing to constraint-following setting.

### Questions
Could you clarify the necessity of only evaluating on LLMs following the Apache 2.0 license and whether there are any other public LLMs that could be used for additional experiments? The limited model settings would be listed as a weakness of this work, but this is understandable if there is no further options.

How is Inference w/ constraints implemented? Is it the sampling approach as is used during training for generating candidates? I'm particularly curious of in the improvement of ACT (100% setting ) and inference w/ constraints performance in Table 1. It's also surprising that inference w/ constraints significantly improves entity typing performance, over ACT, but not in summarization. Is there any explanation for this?

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
3

### Summary
The paper presents an approach to adapt LLM to focus on a particular task which comes with constraints. The task is assumed to have a set of constraints, each of which are easy to automatically verify (e.g., you can write a simple code that checks whether the model output satisfies the constraint or not). The paper propose a simple, reasonable approach to address this issue: they build automatic constraint verifiers manually, sample multiple responses from the base LMs, evaluates the responses with constant verifiers, and fine-tune LLM to prefer constant satisfying responses over non constant satisfying ones. 

 And I find the paper is well-written and easy to follow. The experiments are well explained, and I do not have major concerns with the validity of the proposed method. But I'm having an issue with the baselines and the gains from the proposed approach. Please see weaknesses for the details.

### Strengths
* They propose a simple and reasonable approach that can be applied to a wide range of applications. 
* The task is well motivated. 
* The experimental design is solid, though it misses baselines from prior work. 
* The paper is clearly written. 
* The discussion (Section 5) is quite thorough and interesting.

### Weaknesses
 * Weak results(?): 
 The gains from the proposed approach is pretty small or non-existent compared to reasonable baseline (e.g., fine-tuning approaches). For example, in fine-grained entity typing, fine-tuning outperforms (Figure 3&4). I'm not sure I'm understanding the Fine-tuning setup -- is ACT "unsupervised" (w/t access to human labels) and fine-tuning approach "supervised" with labeled data? Instaed, ACT has manually crafted constraint verifiers?  More elaboration on how much supervision is given to each setting would be helpful.

* Issues with baselines / task choice: It would be helpful if authors can provide justification for the choice of three benchmarks. There are other benchmarks that has been studied for constrained generations, for example, COMMONGEN corpus [1] which considers lexically constrained decoding (LLMs goal is to generate a coherent sentence containing all listed words). There are rich literature (which the paper cites e.g., COLD decoding paper) that handles such constraint adherence problems in this dataset, and they should be compared as a baseline. 

[1] B. Y. Lin, W. Zhou, M. Shen, P. Zhou, C. Bhagavatula, Y. Choi, and X. Ren. CommonGen: A constrained
text generation challenge for generative commonsense reasoning. In EMNLP - Findings, 2020. URL https://aclanthology.org/2020.findings-emnlp.165.pdf.

### Questions
(1) In your experiments, how many constraints (on average) exist for each task?
(2) There exist tasks where either (a) building a reliable verifier is difficult (e.g., long-form question answering) or (2) reliable verifier is computationally very expensive. Do you have any ideas how your approach could be modified/further improved to address such tasks? 



Comments:
* I am not sure identification of three downstream tasks where constraints apply is strong enough to be listed as a contribution in the introduction. 
* The verifier must be built manually, if I’m understanding correctly. It’d be good to make that clear in Figure 2.  
* Human evaluation result (for summarization) should be more carefully reported, with inter-annotator agreement and statistics on the annotators, payment for them, etc. 
* It would be helpful to have example task instance for each one in the appendix.

Minor comments/suggestions:
* For reproducibility, it’d be good to provide the exact prompt / in-context examples used (e.g., line 294).

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
In this paper, the authors proposed a methodology to customize an LLM to specific user needs by introducing task constraints.
The main contributions consist of, firstly, defining a categorization of constraints that covers scenarios where the constraints involve the response alone (as in restricting the label(s) of the prediction), context and response, and groups of prompts and responses. Secondly,
the framework allows for the implementation of automatic constraint verifiers, which are used to build preference data and customize the models using a ranking-based method.
Finally, experiments on tasks representative of each constraint scenario, including analysis on transfer task learning scenarios, and the potential impact of constraint verification as a reward signal for reward modeling.

### Strengths
-	The framework makes no assumptions about the constrain type, and can be easily categorized into the proposed hierarchy.
-	The collection strategy for the preference dataset is sound, maximizing the “constraint satisfaction score” gap between responses whilst making sure all of them are highly probable. This effectively leverages the sensitivity of the “constraint satisfaction score” given for each scenario and the well-trained knowledge in the base LLM.

### Weaknesses
 - Although the constraint hierarchy is sound, only one task was investigated per constraint category. The exploration of at least two more tasks per category would provide a more confident indicative that the proposed method is efficient and we are not just overfitting to a specific task. Perhaps peripheral experiments in section 5 can be reworked as main experiments in section 4.
- Critically, the paper is also missing more details and examples on the defined constraint categorization, as well as an analysis on distribution of the constraint satisfaction scores for each constraint scenario (see ORPO, https://arxiv.org/pdf/2403.07691)

## Section 3.5: Training
- Some details are missing (as well as numeration on the equations) from the loss functions, which make the section difficult to understand for someone who hasn’t seen the cited paper (RRHF). It is alright to add redundant details in order to make the sections more understandable. For instance, the margin (L228) does not appear in L_rank.

## Section 4.1. Implementation details
- From what I gather, the chosen (preferred) response is defined as one that satisfies all constraints, whereas a rejected response is one that does not satisfy ‘some’ constraints.  which kind of constraints are considered when selecting a rejected response?

## Section 4.2. 
- Details of the ‘enhanced loss function’ are missing in appendix C
- For the ‘inference with constraints’ baseline, how often are the constraints verified during inference? After each token or sentence, or at the end?

## Section 4.3
- Footnote 6, could you please elaborate in a more technical way what the ‘garbage in-garbage out’ problem is?
- When collecting feedback from the constraint verifier, two responses are sampled from all possible combinations. It is desirable for this response pair to have minimal conflict. How is this conflict defined, and how is it quantified?

## Section 5
- 5.1. The argumentation in this section would be better placed at the related work section, as it provides general motivation
- 5.2. In table 2 and 3, when source task = ‘-‘, does this mean that training was done on the target task or that inference was done over the base model (before ACT training)

### Questions
## Section 3.5: Training
-	Some details are missing (as well as numeration on the equations) from the loss functions, which make the section difficult to understand for someone who hasn’t seen the cited paper (RRHF). It is alright to add redundant details in order to make the sections more understandable. For instance, the margin (L228) does not appear in L_rank.

## Section 4.1. Implementation details
-	From what I gather, the chosen (preferred) response is defined as one that satisfies all constraints, whereas a rejected response is one that does not satisfy ‘some’ constraints.  which kind of constraints are considered when selecting a rejected response?

## Section 4.2. 
-	Details of the ‘enhanced loss function’ are missing in appendix C
-	For the ‘inference with constraints’ baseline, how often are the constraints verified during inference? After each token or sentence, or at the end?

## Section 4.3
-	Footnote 6, could you please elaborate in a more technical way what the ‘garbage in-garbage out’ problem is?
-	When collecting feedback from the constraint verifier, two responses are sampled from all possible combinations. It is desirable for this response pair to have minimal conflict. How is this conflict defined, and how is it quantified?

## Section 5
- 5.1. The argumentation in this section would be better placed at the related work section, as it provides general motivation
- 5.2. In table 2 and 3, when source task = ‘-‘, does this mean that training was done on the target task or that inference was done over the base model (before ACT training)

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
3

### Summary
This paper is about incoporating constraints in LLMs in order to improve them efficiently for NLP downstream tasks (in the paper: summarization, entity typing and temporal question answering). The approach to do so relies - as far as I understand - a rather standard process in this area where constraints are defined (manually), automatically verified and different responses of an LLM are then generated, each of which is assessed for constraints. The model is then trained with these constraint-verified outputs. The paper goes on to show that this approach can rival standard fine-tuning of LLMs on three selected NLP tasks.

### Strengths
S1) The paper's idea is interesting

S2) The evaluation is thorough

S3) The paper is well-written and easy to follow

S4) The paper conducts multiple interesting and thorough analyses

### Weaknesses
I generally like this paper, but list here a few potential weaknesses:

W1) Even though I am not an expert for this, I think the methodology is straightforward and standard

W2) The topic is arguably not one of the most fanciest, concurrently

W3) Could one have added more baselines, e.g., constrained decoding?

### Questions
Q1) Choosing relevance as a constraint in summarization seems a bit arbitrary. Why not other aspects such as coherence? Overall, however, I am not sure whether it makes sense to think of those dimensions as constraint. Should that not be more formal aspects such as the length of the summary?

Q2) Did I miss something: In Table 3, you show the results for summarization&table-to-text generation but where is extraction? (Table 2 shows only CSR)

Q3) see W3

Depending on author answers, I am prepared to raise my score.

### Soundness
4

### Presentation
4

### Contribution
3
