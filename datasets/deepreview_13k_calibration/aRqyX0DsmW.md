# Benchmarking LLMs on Safety Issues in Scientific Labs

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3, 5, 3

## Abstract
Laboratory accidents pose significant risks to human life and property, underscoring the importance of robust safety protocols. Despite advancements in safety training, laboratory personnel may still unknowingly engage in unsafe practices. With the increasing reliance on large language models (LLMs) for guidance in various fields, including laboratory settings, there is a growing concern about their reliability in critical safety-related decision-making. Unlike trained human researchers, LLMs lack formal lab safety education, raising questions about their ability to provide safe and accurate guidance. Existing research on LLM trustworthiness primarily focuses on issues such as ethical compliance, truthfulness, and fairness but fails to fully cover safety-critical real-world applications, like lab safety. To address this gap, we propose the Laboratory Safety Benchmark (LabSafety Bench), a comprehensive evaluation framework based on a new taxonomy aligned with Occupational Safety and Health Administration (OSHA) protocols. This benchmark includes 765 multiple-choice questions verified by human experts, assessing LLMs and large vision models (LVMs) performance in lab safety contexts. Our evaluations demonstrate that while GPT-4o outperforms human participants, it is still prone to critical errors, highlighting the risks of relying on LLMs in safety-critical environments. Our findings emphasize the need for specialized benchmarks to accurately assess the trustworthiness of LLMs in real-world safety applications. The code and data are available at https://anonymous.4open.science/r/LabSafetyBench-6363

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Laboratory accidents pose significant risks to human life and property, and despite safety training, unknowingly unsafe practices may occur. LLMs are increasingly relying on for guidance, raising concerns about their reliability in safety-related decision-making. The Laboratory Safety Benchmark (LabSafety Bench) is proposed to address this gap, assessing LLM and large vision models' performance in lab safety contexts. The benchmark includes 765 multiple-choice questions verified by human experts.

### Strengths
+ By focusing on laboratory safety, the paper tackles a highly specific yet essential aspect of LLM application. Unlike general benchmarks, the LabSafety Bench targets a field where errors can have severe, real-world consequences, filling a critical gap in LLM evaluation.
+ The creation of the Laboratory Safety Benchmark (LabSafety Bench) tailored to lab safety demonstrates a novel and practical contribution.

### Weaknesses
 -  While multiple-choice questions allow for standardized assessment, they may not fully capture complex decision-making required in lab safety.
- How the human experts are selected and the examination procedure should be described in details. 
- Some related works are missing, e.g.,

	- Xie, Tinghao, Xiangyu Qi, Yi Zeng, Yangsibo Huang, Udari Madhushani Sehwag, Kaixuan Huang, Luxi He et al. "Sorry-bench: Systematically evaluating large language model safety refusal behaviors." arXiv preprint arXiv:2406.14598 (2024).
	- Li, Kenneth, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg. "Inference-time intervention: Eliciting truthful answers from a language model." Advances in Neural Information Processing Systems 36 (2024).
	- Xie, Xuan, Jiayang Song, Zhehua Zhou, Yuheng Huang, Da Song, and Lei Ma. "Online Safety Analysis for LLMs: a Benchmark, an Assessment, and a Path Forward." arXiv preprint arXiv:2404.08517 (2024).

### Questions
1. What are the tasks and roles LLMs play in Lab environment? Why is it important to benchmark the safety? It should be highlighted in the intro.

2. The selection of human experts and the manual processing procedure is not so clear. It should be illustrated for readers' understanding the soundeness of your benchmark.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers the problem of an LLM being queried on laboratory protocols and inadvertently generating responses which cause users to take unsafe actions that cause laboratory accidents. To measure this risk, the paper introduces a benchmark of multiple-choice lab safety questions, similar to tests given in formal lab safety trainings, and compares the results to human baseline performance. The paper also compares a variety of commercial models including open-weight models and proprietary access models, exploring the nature of the observed differences in performance.

### Strengths
+ Benchmarks have a difficult epistemic relationship with risk of unwanted behavior. The validation study performed here is welcome and useful.
+ There is substantial engagement with the performance evaluation results, including (informal) qualitative review of errors and of lower-performing models to understand approaches for enhancing support.

### Weaknesses
 - The paper's core material is substantially disconnected from its motivation, to the point of being potentially misleading. These claims need to be tempered. In specific, there is no offered model of how users reach unsafe actions. The model of "a user queries an LLM and then takes an action which might be unsafe" is naive to the point of straining credulity, and this is not even proposed except in a latent way. The motivating accidents offered between 036 and 040 are, in general, not lab accidents of the sort that improved LLM function would avoid. How does the LLM query fit into a process for operating things like chemical fabrication pipelines safely? Why would a human lab scientist with safety training unquestioningly follow guidance from an LLM? Why would a lab user without safety training be in the position to access materials that could lead to the kinds of issues motivating this work? Yes, personnel benefit from automated guidance and may act counter to safety protocols for a variety of reasons, but what is the threat model justifying this work (without which the value of the work is hard to establish or evaluate)? Relatedly, the approach of focusing on all manner of labs should be justified more cleanly from the beginning - it took me to almost the end of the paper to understand that the goal was to evaluate the performance of current models against these risks (again, because the risk model is not made explicit) rather than try to develop a benchmark which would aid the development of domain-specific models or of model tuning. At a systems level, it is unlikely that actions taken on the equivalent of the honor system can, on their own, cause an accident. It's possible, but the model needs to be clearer or the motivation and top level claims tempered accordingly.
- As the validation moves forward, the paper concludes that having certain structured knowledge could benefit the generation of safe advice, but there is surprisingly little study in the paper of methods for integrating symbolic representation or knowledge bases into generation. I am interested to know how much this can help, if at all.
- Tests against benchmarks do not define much if any knowledge about the avoidance of risk. The paper should caveat the measurement of safety against some notion of the claim that's actually required, which is that the model under test is fit for purpose for some defined purpose. It would be valuable, I think, to link not only to workflow tasks but to some kind of ontology of safety practices vs. lab tasks, which is essentially what the standards used for question generation provide. Why not maintain this structured representation? What is gained/lost by transitioning to this approach?
- I am somewhat concerned about the approach of using LLMs to (re)generate benchmark questions. In specific, if LLM text is detectable, can this rewriting of questions bias the selection of multiple-choice answers by models during benchmark evaluation? Why or why not?
- Although part of the evaluation used human subjects, I cannot find an ethics statement or other mention of human subjects research review.

Minor nit:
- Reference (OSHA, 2011l) is somewhat challenging to read due to the orthographic similarity of the 1 and the l. I'm not sure what to do about this, but perhaps there are ways to find alternative keys?

### Questions
* What is the model of safety risk against which this benchmark is meant to measure model performance? How can I turn the performance evaluation against the benchmark into a claim about whether certain actions or workflows will be safe? Should there be a process model for integrating LLM-driven actions into lab activities?
* What are the tasks against which models are being measured by this benchmark?

### Soundness
2

### Presentation
4

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
This paper introduces LabSafety Bench, a benchmark for evaluating LLM capabilities in understanding and providing guidance on laboratory safety protocols. The benchmark contains 765 multiple-choice questions covering various aspects of lab safety, including hazardous materials handling, emergency responses, and equipment usage. The authors evaluate 17 models on this benchmark and compare their performance against human experts.

### Strengths
- The work addresses an important topic as LLMs are increasingly being integrated into scientific workflows
- The benchmark is comprehensive, covering multiple aspects of lab safety and aligned with established OSHA protocols
- The evaluation is thorough, including both text-only and multimodal questions, and comparing against human performance

### Weaknesses
 - My main concern is with the practical significance of the benchmark. The primary use case presented - students asking LLMs about lab safety - is itself problematic, as students should be consulting official protocols and trained personnel rather than LLMs. In practice, I doubt students will solely consult LLMs on safety-related questions. Is this the main use case?
- The benchmark may not effectively capture real-world safety risks, as actual laboratory environments have multiple safeguards and verification processes beyond just knowledge of safety protocols. Real-world failures like the ones listed in the introduction involve many overlapping systems, and it is unclear how this benchmark will help prevent them.
- Human evaluation does not allow participants to consult external materials. This is problematic as if in practice humans can get 100% on this benchmark they wouldn't need LLMs to help with lab safety questions

### Questions
Are there any potential biases to using GPT-4 as part of the benchmark curation process?

### Soundness
3

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
3

### Summary
This paper explores the performance of LLMs when they are applied to safety issues in scientific labs. The author(s) identifies a new taxonomy aligned with Occupational Safety and Health Administration protocols and based on it, they develop a benchmark for LLM-based lab safety. The benchmark includes 765 multiple-choice questions that human experts manually verify. A systematic evaluation approach is defined to evaluate the performance of several SOTA LLMs such as GTP-4o. Several findings are drawn from the evaluation, such as that LLMs can outperform human beings in lab safety but are still prone to critical errors or safety crises.

### Strengths
1. A sound study with carefully designed experiments and evaluations. I must acknowledge the authors' efforts to build corpora in this specific domain. I understand that it needs a huge amount of human effort to compose and examine the data for a high-quality corpus. Particularly, lab safety in different domains is very domain-specific and requires a lot of domain knowledge. A benchmark is highly valuable in developing useful LLMs for the purpose of safety guidance. 

2. Good and clear presentation. The paper has a clear motivation, methodology, and evaluation results. The findings from the study are convincing. It is interesting to see that CoT and few-shot learning have minimal impact on LLM performance. From the evaluation, the authors also identify that most LLMs have difficulties in Radiation Hazards, Physical Hazards, Equipment Usage, and Electricity Safety.

### Weaknesses
 1. Lack of insights. The findings from the work are not surprising. For instance, the authors find that LLMs are not fully reliable in the application of lab safety. This result is apparent. At present, in any safety-critical domain, a big concern with LLMs is their safety or reliability. Compared with such findings, potential solutions would be more valuable, even in this specific domain. 

 2. The authors spend several pages discussing the comparison of several mainstream LLMs when they are applied to lab safety. I couldn't see the meaning of the comparison results. I understand that the comparison can reflect which LLM performs better than the other. But what does that imply? LLM competition develops fast. The results might be obsolete quickly. I do not think the comparison is necessary or important. 

 3. Lack of evaluation of benchmarks. The authors claim their contribution is the benchmark for lab safety applications. If so, the benchmark shall be carefully evaluated to convince the followers the benchmark is good enough to train LLMs or investigate new approaches to achieve more accurate lab safety guidance using LLMs or other LLM-assisted approaches.

### Questions
1. Could you explain the necessity of comparing LLM performance for the benchmark? 
2. How could we assess the quality of the benchmark? 
3. Besides data, what are the real challenges when LLMs are applied to the lab safety problem?

### Soundness
3

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
This paper argues that although there is much previous work on safety, trustworthiness, truthfulness, fairness and privacy for LLMs, no previous work has investigated lab safety specifically, which involves a different aspect of trustworthiness. The paper develops a benchmark to evaluate LLMs in terms of lab safety where they develop a taxonomy based on OSHA protocols, curate a set of questions based on the taxonomy, and then evaluate a set of foundation models and humans for their accuracy in selecting the correct answer to the questions.

### Strengths
The problem is well motivated and justified, and seems important considering the use of LLMs in many safety-critical areas. The lab safety taxonomy based on various OSHA requirements seems helpful and useful for benchmarking. The evaluation has good diversity of LLM models, with 17 foundation models, including both open source, proprietary and scientific models and different prompting techniques. Finally, I appreciate that the code is released open source.

### Weaknesses
I have some issues with the evaluation. Starting with the human evaluation (see question 1): the paper mentions they used individuals who had undergone lab safety training but what exactly does that entail? I am wondering if this was a sufficiently fair comparison-- it may be the case that the humans were being tested on very specific lab safety questions that they had not encountered or been trained for (e.g., lab safety training was for a broad range of biology wet lab safety questions when an individual only works in or is only trained in a specific sub field of biology safety or vice versa). Moreover, I would argue the LLM in this scenario should be considered an expert, and therefore should be compared to only human "experts" (i.e., not junior scientists like undergraduates).

In addition, the authors mention the goal is to determine whether or not LLMs can be trusted to be more reliable than humans in decision making and planning for lab safety. Can the authors comment on the applicability of using the benchmark multiple-choice question & answer as a proxy for evaluating this (see question 2)? In practice, the way a user engages with the LLM for these types of decisions is very different (i.e., they are probably not going to ask it a multiple choice question with the answers listed.) I am wondering if this is really a fair methodology in order to evaluate how well LLMs follow lab safety protocols.

### Questions
(1a) For the human evaluation, how were the human participants selected and to what extent did they have direct experience or training related to the specific questions being asked in the evaluation? 
(1b) Why did you include junior scientists in the comparison?

(2a) Why were multiple choice questions chosen as the evaluation technique?
(2b) Can the authors comment on the applicability of using the benchmark multiple-choice question & answer as a proxy for evaluating this?

### Soundness
1

### Presentation
2

### Contribution
2
