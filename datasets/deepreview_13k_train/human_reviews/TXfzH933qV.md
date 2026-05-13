# Reliable and Diverse Evaluation of LLM Medical Knowledge Mastery

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Mastering medical knowledge is crucial for medical-specific LLMs. However, despite the existence of medical benchmarks like MedQA, a unified framework that fully leverages existing knowledge bases to evaluate LLMs' mastery of medical knowledge is still lacking. In the study, we propose a novel framework PretexEval that dynamically generates reliable and diverse test samples to evaluate LLMs for any given medical knowledge base. We notice that test samples produced directly from knowledge bases by templates or LLMs may introduce factual errors and also lack diversity. To address these issues, we introduce a novel schema into our proposed evaluation framework that employs predicate equivalence transformations to produce a series of variants for any given medical knowledge point. Finally, these produced predicate variants are converted into textual language, resulting in a series of reliable and diverse test samples to evaluate whether LLMs fully master the given medical factual knowledge point. Here, we use our proposed framework to systematically investigate the mastery of medical factual knowledge of 12 well-known LLMs, based on two knowledge bases that are crucial for clinical diagnosis and treatment. The evaluation results illustrate that current LLMs still exhibit significant deficiencies in fully mastering medical knowledge, despite achieving considerable success on some famous public benchmarks. These new findings provide valuable insights for developing medical-specific LLMs, highlighting that current LLMs urgently need to strengthen their comprehensive and in-depth mastery of medical knowledge before being applied to real-world medical scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents PretexEval, an innovative evaluation framework designed to assess medical LLMs' knowledge mastery with a focus on generating reliable, diverse test samples. By transforming medical knowledge points through predicate equivalence transformations, PretexEval produces varied yet accurate textual representations, allowing for a richer evaluation compared to traditional benchmarks like MedQA. The framework not only highlights areas where LLMs are deficient but also introduces joint accuracy as a critical metric to measure the consistency of LLMs’ responses—an important yet often overlooked requirement in healthcare settings.

### Strengths
- Novel Evaluation Method: PretexEval introduces a fresh approach by transforming knowledge points into diverse predicates, effectively improving both the reliability and comprehensiveness of LLM evaluation. This is particularly relevant in fields like healthcare, where factual consistency is crucial.
- Focus on Consistency: The framework’s use of joint accuracy to measure consistency across expressions of the same knowledge point is a valuable contribution. In healthcare, where consistency is key, this metric allows for a deeper look at whether a model can reliably interpret nuanced variations of medical knowledge.
- Broad Evaluation Scope: The study evaluates 12 leading LLMs across both general and medical-specific models, demonstrating PretexEval’s versatility and highlighting critical insights into current LLM limitations.

### Weaknesses
 - Scope of Evaluation Tasks: The framework is limited to true/false verification tasks, which could constrain its applicability in complex medical scenarios where contextual understanding and reasoning are required. The true/false format, while straightforward, may not fully capture the nuances of medical knowledge, such as differential diagnoses or treatment planning, where more elaborate reasoning is needed.
- Prototype Dependence: Manually crafted prototypes, while improving reliability, may limit scalability and introduce potential subjectivity. Refining this step or automating parts of it could enhance PretexEval’s flexibility. Reliability here is measured by two annotators on a 50-sample subset, introducing a skewed potential for bias. Expanding this evaluation to at least three annotators and including an inter-annotator agreement measure would add robustness. The small sample size for reliability assessment also raises concerns about the generalizability of the reliability scores.
- Applicability for Model Training: While it’s a promising evaluation tool, exploring the potential of PretexEval-generated samples for training might add another layer of impact, possibly making it a resource for enhancing models’ medical knowledge consistency. The current focus is solely on evaluation, and the potential for using the generated data to improve model performance is not explored.

### Questions
- How do you plan to extend PretexEval beyond true/false verification tasks? Adding context-sensitive or reasoning-based tasks could expand its applicability to more complex clinical scenarios.

- Prototype Automation: Are there plans to automate prototype creation to reduce potential subjectivity and improve scalability? If not, what criteria ensure prototype reliability and consistency across varied medical contexts?

- Reliability Validation: Given the small sample size and limited number of annotators for reliability measurement, how would expanding the annotation set or incorporating inter-annotator agreement metrics influence reliability scores? Would this improve the robustness of results?

- Could PretexEval-generated samples serve a role in training, not just evaluation? If incorporated into training, would these samples likely boost LLMs’ consistency on diverse medical knowledge?

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
PretexEval is a new way to assess how well large language models (LLMs) understand medical knowledge by creating dynamic test samples from medical databases. The framework uses simple logic transformations (like flipping statements, modifying them, and using double negatives) to produce a variety of reliable test questions, going beyond traditional fixed tests. The authors evaluate 12 well-known LLMs, including some designed specifically for medicine, using two databases focused on clinical diagnosis and treatment. They show that while these models perform well on existing medical benchmarks, they still struggle to consistently grasp medical knowledge when it’s presented in different ways. The main contribution is a flexible method for testing LLMs’ understanding of medical knowledge, backed by detailed results that reveal significant gaps between their performance on tests and their genuine understanding of medical concepts. This research offers further insights into methods for setting up a systematic way to scale the evaluation of LLM readiness for use in clinical settings.

### Strengths
- PretexEval introduces a new approach to testing medical knowledge in language models. Rather than using fixed test questions, it dynamically generates diverse test cases that probe deeper understanding. This represents a significant methodological advancement in AI evaluation.
- The authors create a reliable yet flexible testing framework by combining predicate transformations with natural language generation. The method is both principled and practical, with clear steps for reproduction.
- The empirical results reveal important insights about current AI capabilities in medicine. The authors demonstrate that even state-of-the-art models struggle with consistent understanding by testing 12 different models with varying forms of the same medical knowledge. This finding has direct implications for clinical applications.
- The framework's generalizability is a key strength. While demonstrated on two medical knowledge bases, the approach can extend to other medical domains and potentially beyond medicine. This broad applicability makes the contribution particularly valuable for the field.
- LLMs across sizes and even API based models were evaluated and compared against simple LLM rephrasing

### Weaknesses
The study's methodology, while strong, has a few areas that could be strengthened. 
- Though clearly explained for simple relationships, the predicate transformation concept lacks a formal specification for handling complex medical relationships that don't cleanly map to simple predicates. Specifically, the method does not detail how multi-hop relationships or those involving multiple interacting entities would be represented and transformed. For example, a relationship like 'Drug A inhibits Enzyme B, which is necessary for the activation of Compound C, which treats Disease D' would be difficult to represent with simple predicates and transformations. 
- Further, the evaluation is limited to one relationship test in a multiple-choice setting, which may not fully capture the complexity of medical knowledge application. Exploring the handling of multiple variations, such as incorporating distractors or relationship swapping similar to GSM symbolic approaches, could provide a more comprehensive assessment of LLM capabilities in medical contexts. The current evaluation focuses on verifying a single transformed statement, but does not assess the models' ability to synthesize information from multiple related statements or to reason about complex scenarios involving multiple medical concepts. 
- Currently, the framework is only tested for binary settings; it would be useful to know how this setting can be applied to even a simple 4-class mcq or, ideally, an open-ended setting.

### Questions
In the case study shown in Figure 6, the PretexEval method includes a rewording that shifts from "may treat" to "is recommended." This raises concerns about whether this transformation validly rephrases the original medical relationship. In medical contexts, "may treat" and "is recommended" carry different implications:
"May treat" suggests a possibility or potential for treatment, leaving room for other options or uncertainties.
"Is recommended" implies a stronger clinical endorsement, suggesting that the treatment is advised or endorsed by clinical guidelines or experts.
Given this distinction, the shift from "may treat" to "is recommended" could be problematic if it alters the strength of the claim. This transformation might lead to incorrect evaluations, as LLMs could be unfairly penalized for failing to recognize a relationship that has been shifted beyond its original meaning.
Therefore an important question arises:
- Clarification on Predicate Transformation Boundaries: Could you clarify how you ensure that predicate transformations do not alter the underlying meaning of medical relationships? Specifically, how do you prevent shifts in meaning from "may treat" (a possibility) to "is recommended" (a stronger clinical assertion)? I understand some validation in the initial setting was completed, but this may be lost during rephrasing- so I just want to clarify what of the final questions were validated and by what grade physicians.
- Handling Ambiguities in Medical Relationships: How does PretexEval handle nuanced medical relationships where different levels of certainty or recommendation are involved? For example, how do you ensure that transformations like "may treat" vs. "is recommended" retain their original intent without introducing stronger or weaker claims?
- Validation of Rephrased Statements: Could you describe any validation steps taken by medical experts to confirm that reworded statements retain their original intent and do not introduce factual inaccuracies or misleading implications? 
- Addressing these concerns would help ensure that the transformations generated by PretexEval maintain clinical accuracy and do not inadvertently alter the meaning of medical knowledge points during evaluation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents PretexEval, a novel evaluation framework designed to assess the mastery of medical knowledge by large language models (LLMs). Recognizing the limitations of existing evaluation methods, which often produce test samples with factual errors and insufficient diversity, PretexEval introduces a new schema based on predicate equivalence transformations. This approach generates a series of variant samples from a given medical knowledge point, ensuring both reliability and diversity in the test samples created. This framework was applied to evaluate 12 well-known LLMs using two medical knowledge bases. The findings reveal that, despite notable successes on standard QA benchmarks, current LLMs exhibit significant deficiencies in thoroughly understanding medical knowledge.

### Strengths
Originality: The concept of dynamically generating test samples from medical knowledge bases using predicate equivalence transformations is innovative.

Quality: The experimental design is robust, involving a comprehensive evaluation of 12 well-known LLMs across two distinct medical knowledge bases. The methodology for transforming predicates into diverse textual samples ensures that the evaluations are rigorous. The detailed ablation study and the use of two evaluation metrics (average accuracy and joint accuracy) further substantiate the quality of the research.

Clarity: The paper is well-organized and articulates ideas clearly and logically.

Significance: The findings highlight significant deficiencies in the current LLMs' ability to fully master medical knowledge, which is critical for their deployment in real-world medical scenarios.

### Weaknesses
1) The limitations of the proposed approach should be discussed in the paper:
- The PretexEval framework heavily relies on predicate transformations to generate test samples. While this approach contributes to sample diversity, it may not adequately capture the complexity or the nuances of medical reasoning that goes beyond simple factual recall.
- The current evaluation metrics, while useful, focus predominantly on binary true/false assessments of knowledge mastery. This binary approach might oversimplify the evaluation of medical knowledge, where a more nuanced understanding might be necessary.

2) The code and datasets should be made publicly available for reproducibility purposes.

### Questions
- In comparison with the previous subsections, section 3.2.2 is harder to follow. To facilitate understanding, this section would greatly benefit from including examples (particularly lines 211-213).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces PretexEval, a framework for generating test samples from medical knowledge bases by generating variants of predicate expressions. This is done in three steps: 

(1) A knowledge point is converted to a predicate expression. 

(2) A predicate expression is converted to multiple predicate variants. 

(3) Predicate variants are converted back to a textual format.  

Authors prompt a number of current LLMs to verify the correctness of each statement (True/False), and find that current LLMs display subpar performance on these newly generated test samples, leading to the conclusion that they have not yet mastered medical knowledge.

### Strengths
- The motivation of generating reliable test samples without factual errors, which is especially important in the medical domain, is clear and concise.
- The proposed framework can be applied to any medical knowledge base.

### Weaknesses
 - Opposed to the overall impression that the proposed framework enables diverse evaluation of LLMs’ medical knowledge, the paper only utilizes a single metric (true/false verification) for evaluation. A reviewer think that addressing multiple choice question answering or generating through (subject, relation, object) triplet makes more beneficial to elicit LLMs' medical knowledge. Although the authors do involve joint accuracy as a measure to account for all related samples that stem from a specific knowledge point, defining the knowledge span of current LLMs without diverse evaluation metrics (e.g. Single/Multiple Choice QA, Extractive/Abstractive QA) seems insufficient.
- Further consideration on baseline selection seems necessary to support the efficacy of the proposed framework. Based on the initial problem statement that prompting LLMs to “directly generate test samples based on specific knowledge points” may lead to insufficient factuality, the LLMEval baseline from Table 1 seems to be unreliable. Could you provide more justification details why you added the LLMEval baseline?
- In the Related Work section, authors point out that existing benchmarks crafted from medical experts may “become outdated or leaked to LLMs, affecting the comprehensiveness of evaluation”. How is the dataset created from the suggested framework any different? Further clarification regarding the authors’ intentions would be helpful.
- How are the test samples for the “Direct” baseline constructed? More clarification on the template paraphrasing process would be helpful, as readers may not be familiar with related works that adopt template paraphrasing. Please provide the example of a template and how it is used to create a test sample for the "Direct" baseline.
- Can you elaborate more on the qualifications of the “two experienced doctors” that have manually evaluated the test samples? Such as providing the years of experience or the doctors' specialities, or any relevant certifications that qualify them to evaluate these medical knowledge samples.
- When analyzing the “Effect of Predicate Transformation Types”, have the authors conducted the “Direct + Double Negation” setting as well? Experiments in this setting seems to be important for the claim that “current LLMs exhibit relatively less proficiency in understanding negated expressions”.

### Questions
- In the Related Work section, authors point out that existing benchmarks crafted from medical experts may “become outdated or leaked to LLMs, affecting the comprehensiveness of evaluation”. How is the dataset created from the suggested framework any different? Further clarification regarding the authors’ intentions would be helpful.
- How are the test samples for the “Direct” baseline constructed? More clarification on the template paraphrasing process would be helpful, as readers may not be familiar with related works that adopt template paraphrasing. Please provide the example of a template and how it is used to create a test sample for the "Direct" baseline.
- Can you elaborate more on the qualifications of the “two experienced doctors” that have manually evaluated the test samples? Such as providing the years of experience or the doctors' specialities, or any relevant certifications that qualify them to evaluate these medical knowledge samples.
- When analyzing the “Effect of Predicate Transformation Types”, have the authors conducted the “Direct + Double Negation” setting as well? Experiments in this setting seems to be important for the claim that “current LLMs exhibit relatively less proficiency in understanding negated expressions”.

### Soundness
3

### Presentation
3

### Contribution
3
