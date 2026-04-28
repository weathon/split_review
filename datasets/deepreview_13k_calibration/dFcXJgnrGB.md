# PlaSma: Procedural Knowledge Models for Language-based Planning and Re-Planning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Procedural planning, which entails decomposing a high-level goal into a sequence of temporally ordered steps, is an important yet intricate task for machines. It involves integrating common-sense knowledge to reason about complex and often contextualized situations, e.g. ``scheduling a doctor's appointment without a phone''. While current approaches show encouraging results using large language models (LLMs), they are hindered by drawbacks such as costly API calls and reproducibility issues. In this paper, we advocate planning using smaller language models. We present PlaSma, a novel two-pronged approach to endow small language models with procedural knowledge and (constrained) language-based planning capabilities. More concretely, we develop *symbolic procedural knowledge distillation* to enhance the commonsense knowledge in small language models and an *inference-time algorithm* to facilitate more structured and accurate reasoning. In addition, we introduce a new related task, *Replanning*, that requires a revision of a plan to cope with a constrained situation. In both the planning and replanning settings, we show that orders-of-magnitude smaller models (770M-11B parameters) can compete and often surpass their larger teacher models' capabilities. Finally, we showcase successful application of PlaSma in an embodied environment, VirtualHome.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a distillation procedure and an inference-time decoding algorithm to enable relative small language models for planning and replanning with performance close or surpassing its larger language teacher models.

### Strengths
• Proposed a paradigm to distill procedural planning knowledge from large language models to enable smaller languages to do planning, and it seems to be working. 
	• Within the paradigm, a cost-effective human-in-loop LLM generated data curation procedure is also proposed to create the COPLAN dataset.
	• Proposed a  guided decoding procedure with a LLM-based (RoBERTa) step verifier to  guide the beam-search during planning steps decoding generation. The guidance help to further regulate the validity of the steps.

### Weaknesses
• The LLM-to-Planning-Model teacher-student paradigm for planning is not well motivated. Cost, performance (from specialization), controllable procedure, better-integration with downstream tasks (e.g. decoding/execution) and so on? It is more about better understanding of the key capabilities of existing techniques and combining them to solve the critical problems. For example, if it is more about specializing common knowledge embedded in LLMs to do planning, then smaller LLM might not be the right solution --- the same proposed paradigm can be combined with LLM of the same size or even larger LLMs for superior planning capabilities. What are the real problems and the corresponding means could be better sorted out? 
	• The truth contribution and their relevancy might be hidden in the paper title and the current way of writing.  The proposal is composed of three parts (1) planning data generation from LLMs with human-in-loop curation, (2) teacher-student distillation training, (3)  language model decoding with step verifier.  There are less texts regarding teacher-student distillation. This might indicate that the teacher-distillation importance is over-estimated. With the planning data generation and verifier-guided decoding generation, there might other ways to enhance planning abilities, e.g. finetuning the original LLMs to specializing into planning domains. If the distillation step is an importance component in the ingredients, please detail it and discuss more.

### Questions
1. There are good ideas within the paper. The writing could be improved to make these good idea clear and stand-out. For example, how to train the step-verifier from human-written plans along with more formal analysis of impact of the step-verifier. 
	2. Please define the loss functions formally with teacher-student distillation and verifier-training.
	3. For the step verifier, "we design perturbations … ordering, semantic completeness, topicality and fluency", please provide detailed analysis of these data-side steps regarding their intuition and formal properties if possible. How does a single verifier score reflect all these criteria? Any special design to achieve them with a simple RoBERTa based classifier?
	4. Regarding the evaluation metrics, please provide more details of the AMT human steps. Are coverage, order, over quality complete to evaluate a plan? Any comparison or correlation on the human evaluation metrics and the bleu numbers and the Emobided Environment's metrics? If not well-correlated, any proposal on automatic evaluating plans? Also how to relate and align human evaluation, bleu-style sequence matching metrics, embodied environment testable metrics and real-world execution measurable metrics?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a framework designed to improve the procedural knowledge and planning capabilities of small language models. This is achieved through symbolic procedural knowledge distillation and a verifier-guided step-wise beam search algorithm. The authors have conducted experiments to compare student models of varying sizes with their teacher model, and have utilized human evaluations to assess the generated plans in terms of sequence, completeness, and overall quality. The findings indicate that smaller models can reach or even surpass the performance of larger models by employing the PLASMA framework.

### Strengths
- The paper is well-written and well-structured.
- Equipping small language models to come up with procedural knowledge at the same level as large language models is an important direction from an engineering perspective given the accessibility, carbon footprint, and cost of large language models.

### Weaknesses
 - Although human evaluations were conducted, the executability conditions for the plans in the domains used in these experiments seem to be loose. It would be beneficial to evaluate the models in domains which have hard executability conditions (like the domains used in International Planning Competitions), where the correctness can be objectively determined, to more accurately gauge the language planning abilities of the proposed method.
- A comparison with GPT-4, in addition to GPT-3, could provide additional insights into the effectiveness of the method.
- The potential for increased bias due to the distillation from larger language models is mentioned in the limitations section but remains a concern.

### Questions
- If smaller language models can be effectively paired with human input or external verifiers for improved planning, why is distillation from a larger model necessary? This question is particularly relevant given that the domains discussed in the paper appear to be amenable to human verification.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the use LLMs for generating NL instructions for a given task, called procedural plans. The paper proposes that smaller LLMs trained specifically for generation of such plans can outperform the models used as teacher, and be on par of larger models.

Algorithmically, the contributions are three:
- PlaSma: small model specialized in generating NL instructions.
- PlaSma+: uses PlaSma and an additional model for biasing the output towards higher validity. The paper refers to this bias as a “constraint”.
- CoPlan dataset

The key transversal issues are both data generation and evaluation.

The dataset (CoPlan) is generated using a combination of seed prompts, large models, and human validation.

The experimental setup is reasonable these days: use proprietary GPT as teacher and for generating data; use T5 variants as small models; BERT-variations for classification tasks.

The evaluation is more complicated. The paper reports good human evaluation results in one dataset as the plans cannot be tested. (The  appendix reports usual BLEU and ROUGE scores, perhaps for pacifying some reviewers, but for natural situations there are so many possible wordings that that might very misleading). For VirtualHome, they report an interesting success rate.

The key question is whether the smaller model is just mimicking the teacher’s behaviour. However, the paper reports that the student might outperform the teacher significantly, especially if it has enough capacity. The bias-towards verification model has a higher impact in models with lower capacity.

### Strengths
- Interesting problem as instructions are a key possible application of LLM. Sensible to scale and cost.
- Good description of the methodology in all aspects.
	- In particular the data generation vs curation.
- Sensible complexity of the tasks: goal, conditions, verification.
- A secondary model specialized in higher correctness is a good idea while focusing at lower capacity.

### Weaknesses
 - The dataset ProScript is not well explained
	- It is hard to qualify the complexity of the instructions.
	- So, the results in Table 2 are hard to understand because we don’t know about the relative complexity of the task and the diversity of tasks.
 - I suggest reducing the tone of the phrase “we introduce the task of counterfactual planning”. A quick search in google scholar for “plan revision” reported, for instance, these papers: 
	- Ow, P. S., Smith, S. F., & Thiriez, A. Reactive plan revision. AAAI 1998.
	- Williams, K., & Burdick, J. Multi-robot boundary coverage with plan revision. In Proceedings 2006 IEEE International Conference on Robotics and Automation.
- Abuse of some terms
	- The “step verifier” is **not** verifying, but adding a bias. For instance, the paper mentions that in the case of embodied agents, that verification can be taken over by a safety module. In that scenario, with reasonable \alpha that follows the LLM when the so-called verification is not saying anything relevant, the aggregation of Eq (3) cannot prevent cathastrophic errors that are considered very attractive by the LLM. Perhaps a better name would be “quality bias” or anything saying bias.
	- Same applies to the notion of “symbolic knowledge destilation”, but we are probably too late for this one. I find it problematic that in AI we associate NL with symbolic, as the word is overloaded with a huge body of work in AI ranging from logic to graphical models. It should be more clear to call it something like “instruction distillation”.
- The claim that human-written data is better for evaluation is not justified. Human-written data might lack diversity depending on the protocol, as human annotators have incentive to write as soon as possible. The key issue is not the human-writing but how the situations are generated. The contribution of using smaller models might be tainted if that’s exploiting an artifact of the datasets. So, the dataset description and analysis is crucial to prove the point. Otherwise, the results are not convincing.

### Questions
- Except for PlaSma-Mul, what does PlaSma mean when measured in different tasks. Can you elaborate on how that manifests in the experiments?
	- For instance, in Table 1, the PlaSma model is trained in the planning task, so there are precisely 6 models there. Right?
	- Those models are completely different from the ones reported in Fig 4, correct?
- Please describe the ProScript in-depth and discuss why this is a good dataset for studying this problem.
- Please discuss what other datasets could have been used, and explain why some possibilities are inconvenient. 
	- This should be added to the related work section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to leverage knowledge distillation to train smaller LMs to replicate the procedural plan generation abilities of LLMs.This serves as a cost-effective alternative to achieve the same performance as LLMs using smaller LMs. The authors generate a novel dataset, called CoPlan which includes goal-based and constrained planning tasks, as well as counterfactual replanning tasks. When trained on the CoPlan dataset, the smaller (distilled) models showcased comparable performance to their LLM counterparts. Empirical and ablation experiments further demonstrate the same.

### Strengths
1. Overall, the paper is well-written and has a smooth flow, which makes it easy to follow.

2. The data collection process used to generate CoPlan is novel and would be useful for researchers to collect high-quality data with minimal human involvement.

3. Some of the results shown in the paper were interesting, although not entirely surprising.

### Weaknesses
1. Novelty: The main contribution of this work -- to train a small LM to imitate an LLM by using the LLM as a teacher to train the small LM, is not novel. It has already been demonstrated in [A] (and has not been cited here) for a variety of tasks including complex reasoning If considered in the context of [A], the novelty here is limited to its extension to planning. The use of beam search-based planning is also very similar to [B], however, given its recency, I have discounted it in my evaluation.

2. Missing Key Experiments: While the authors motivate the use of knowledge distillation and compare their distilled models with that of the teacher model, the comparisons with the original (undistilled) model seem to be missing. Without this, it is hard to gauge the performance enhancement from distillation.

### Questions
1. How is CoPlan different from ProScript? Barring the size factor, is it the counterfactual and replanning subset that is novel? Or is there a difference in the diversity of data too?

2. Can you explain the use of the term "symbolic" in "symbolic procedural knowledge distillation"? What is "symbolic" here?

3. It would be interesting to see when distillation leads to overfitting. What factors (model size of small LM, amount of training data) does it depend on? This would help motivate the generation of a larger dataset (compared to existing ones like ProScript).

4. Minor Comment: The use of the term "task" in Sec 2.2 is ambiguous. The authors should clarify upfront that the three tasks are the three different settings that they investigate.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
