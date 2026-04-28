# SciSafeEval: A Comprehensive Benchmark for Safety Alignment of Large Language Models in Scientific Tasks

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Large language models (LLMs) have had a transformative impact on a variety of scientific tasks across disciplines such as biology, chemistry, medicine, and physics. However, ensuring the safety alignment of these models in scientific research remains an underexplored area, with existing benchmarks primarily focus on textual content and overlooking key scientific representations such as molecular, protein, and genomic languages. Moreover, the safety mechanisms of LLMs in scientific tasks are insufficiently studied. To address these limitations, we introduce \textsc{SciSafeEval}, a comprehensive benchmark designed to evaluate the safety alignment of LLMs across a range of scientific tasks. \textsc{SciSafeEval} spans multiple scientific languages—including textual, molecular, protein, and genomic—and covers a wide range of scientific domains. We evaluate LLMs in zero-shot, few-shot and chain-of-thought settings, and introduce a 'jailbreak' enhancement feature that challenges LLMs equipped with safety guardrails, rigorously testing their defenses against malicious intention. Our benchmark surpasses existing safety datasets in both scale and scope, providing a robust platform for assessing the safety and performance of LLMs in scientific contexts. This work aims to facilitate the responsible development and deployment of LLMs, promoting alignment with safety and ethical standards in scientific research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SciSafeEval, a benchmark designed to evaluate the safety alignment of LLMs in scientific tasks across disciplines like biology, chemistry, medicine, and physics. SciSafeEval introduces a jailbreak feature to test LLMs’ responses to potentially malicious queries, particularly those that could be misused in scientific research. The benchmark includes 30k samples, vastly surpassing previous benchmarks in both scale and scope.

### Strengths
The dataset construction adheres closely to established regulations across multiple scientific domains.

The scale of the dataset surpasses previous safety benchmarks in scientific fields. The dataset's design and collection process are effective.

The paper is easy to follow.

### Weaknesses
Since the setting is binary (whether or not the LLM generates harmful content). The few-shot/CoT method will bring significant benefit because it gives an example of rejecting harmful content. Could the authors discuss why some tasks may benefit significantly more than other tasks from few-shot/CoT examples  

The interpretation of appendix F is not clear. How to interpret the “-” and 0s in the tables?

### Questions
Line 23, the quote in latex is ``''.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript proposes a benchmark to be used in assessing the ability of language models to avoid providing information when prompts include potentially harmful subjects in the science domains. Relative to existing benchmarks in this area, the proposed benchmark contains an order of magnitude more total examples and includes prompts related to the fields of physics and medicine.

Examples related to chemistry, biology, and medicine are constructed by mixing prompt templates sourced from previous scientific benchmarks with names of molecules sourced from toxicological screens, controlled substance ledgers, or similar. Examples related to physics are a subset selected from a previous publication. Examples using "jailbreak" prompting strategies are additionally constructed from the "standard" prompts.

An array of language models, both general purpose and specialist, are evaluated using the proposed benchmark and the results reported. A LLaMa-based model trained on a number of human-annotated example is used to determine whether the models engaged with a given prompt or successfully identified it the prompt as malicious and refused. Models are evaluated under three circumstances: zero-shot prompting, five-shot prompting, and a chain-of-thought prompting strategy. All models are found to perform poorly in the zero-shot scenario. The generalist models are found to outperform specialist models in general.

### Strengths
- The area of AI-safety in the sciences is of interest to both the public and regulators. It is good to see interest in expanding our ability to effectively quantify the safety of a given model.
- The proposed benchmark is larger in size and scope than the pre-existing benchmarks in this area.
- A substantial amount of work has been done in aggregating the test cases and benchmarking the existing language models.

### Weaknesses
 - The only considered safety scenario is that of the "evil scientist", an assumed malicious user attempting to access information for misuse. There are other scenarios that a comprehensive scientific safety of evaluation should consider. For example, the suggestion of a faulty synthesis protocol that may lead to injury in the laboratory in the chemistry domain or a confident misdiagnosis leading to incorrect treatment in the medical domain. The current benchmark focuses solely on the identification of known hazardous substances, neglecting other critical safety aspects such as procedural errors or incorrect conclusions.
- Many examples are produced for the proposed benchmark, but the vast majority appear to reduce to the same question: "Can the model identify the presence of a known toxic/controlled substance or infectious agent in the prompt?" This scope should be better documented to prevent potential users over-interpreting results from the proposed benchmark. The benchmark's reliance on simple keyword detection limits its ability to assess more nuanced safety issues, such as the generation of plausible but incorrect scientific information.
- The manuscript uses non-quantitative/non-scientific language in several places that would be helpful to replace with more specific language. For example:
  - (4, 210) "...using a large-scale, high-quality dataset."
  - (5, 254) "This multi-dimensional approach to data collection ensures comprehensive coverage... maximizing the... utility for further biological safety evaluation."
  - (6,303) "This holistic evaluation ensures a multi-faceted risk assessment under various conditions."

### Questions
- The manuscript states "we emphasize the comprehensive coverage of key tasks and safety considerations for each one." How were the included tasks determined to be comprehensive of the key tasks and safety considerations? Were any tasks considered but determined to be non-integral and excluded?
- The manuscript states "Continuous updates are implemented to keep the dataset aligned with evolving scientific knowledge and safety regulations". How are these updates implemented?
- The experimental results in Table 3/Figure 4 lack units. I think that these are the percentage of prompts successfully rejected by the model (i.e. the inverse of the attack success rate used in Table 5)? It would be helpful to explicitly state so.

### Soundness
2

### Presentation
2

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
The paper introduces a benchmark designed to evaluate the safety alignment of large language models (LLMs) when used in scientific domains like chemistry, biology, medicine, and physics. The authors highlight the critical risks LLMs pose in these fields, such as the generation of potentially harmful compounds, pathogenic sequences, or instructions for synthesizing such substances. The benchmark includes a robust and comprehensive dataset of over 31k examples and evaluates models under various prompting settings, including zero-shot, few-shot, and chain-of-thought.

### Strengths
1. The paper makes a substantial contribution by providing a large-scale, multidisciplinary benchmark tailored to the needs and risks of scientific language modeling. It addresses a timely and critical issue in the application of LLMs to scientific domains.
2. The introduction of multi-disciplinary safety evaluations and the jailbreak prompt feature seems valuable.

### Weaknesses
1.	The motivation for creating instruction-tuning datasets using *only harmful compounds* from hazard databases is not well justified in terms of real-world applicability. It seems the authors collected substances associated with hazard-related tags and created an instruction dataset using templates from prior work, followed by prompting experiments. However, the practical impact and real-life utility of these experiments remain unclear, especially since real-world hazard assessments are often multi-layered especially for chemistry. The paper lacks a clear explanation of how this isolated focus on hazardous substances translates to a realistic evaluation of LLM safety in scientific contexts. Specifically, it is unclear how the model's behavior on these artificially constructed examples would generalize to real-world scenarios where both safe and hazardous substances are encountered.
2.	The authors aim for the LLM to not respond at all when there is a risk of mentioning hazardous or toxic substances. If the LLM refuses to respond even to legitimate and safe queries simply because the query involves a topic or substance that can be hazardous in different contexts, it could hinder useful and informative interactions. An improved strategy could involve the LLM generating safe, context-aware responses that include warnings or safety instructions. Then it raises the question: how to evaluate such responses. The current approach of complete refusal is overly simplistic and does not account for the nuances of real-world scientific inquiry where discussions of potentially hazardous materials are often necessary and appropriate within a controlled context. The paper does not address how to differentiate between malicious and legitimate inquiries.
3.	The notion of hazard or toxicity in fields like chemistry or medicine is nuanced. For example, certain levels of toxicity might be acceptable under specific conditions: dose, exposure duration, specific patient contexts, etc. Thus, suggesting that a simple binary approach to harmful versus non-harmful substances might be insufficient. The paper fails to address the complexities of dose-response relationships and context-dependent toxicity, which are crucial in scientific risk assessment. A more sophisticated approach would consider these factors rather than relying on a simplistic binary classification.
4.	The evaluation framework appears to be incomplete -- it focuses solely on accuracy in cases where the model fails to refrain from responding to instructions involving hazardous substances. What about the cases where the model fails to respond to instructions related to non-hazardous substances? Such cases would equally impact the model's practical utility and should be accounted for in the evaluation. The current evaluation metric is biased towards penalizing false positives (responding to hazardous queries) while ignoring false negatives (failing to respond to safe queries). This imbalance makes it difficult to assess the overall usability of the model.
5.	While the paper successfully identifies vulnerabilities in current LLMs, there seems to be little contribution to actually address this issue. The identified issues are somewhat already familiar to researchers, hence limiting the major contribution of this work to the introduction of the dataset which is crowdsourced from existing work. The paper does not propose any novel techniques or strategies for mitigating the identified safety risks. The contribution is primarily limited to the creation of a benchmark, which, while valuable, does not advance the field in terms of practical solutions.
6.	Since the evaluation heavily relies on adversarial prompting (jailbreak prompts), there is a risk that the models may have been inadvertently tuned or overfitted to specific types of prompts used in the benchmark. What if the prompts do not adequately represent the full range of possible adversarial strategies? The paper does not provide sufficient evidence that the jailbreak prompts used are representative of the broader space of adversarial attacks, raising concerns about the generalizability of the findings.

### Questions
1. Could the authors provide insights into the underlying mechanisms that make certain models more vulnerable than others, such as differences in training data or tokenization strategies?
2. Could the authors provide more details on the diversity of jailbreak prompts?
3. For few-shot experiments, how exactly are the "3 representative examples demonstrating effective strategies for handling malicious prompts" selected? Any quantifier? The example in G.1 shows a case for DNA classification. What about the other tasks

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
4

### Summary
The paper introduces a benchmark dataset called SciSafeEval, to evaluate the safety alignment of LLMs across a range of scientific domans -  chemistry, biology, medicine and physics and language scope - textual, molecular, protein and genomic. It improvises over existing benchmarks on the following fronts - (1) a more comprehensive coverage of domains  (existing ones exclude medicine and physics). (2) larger in scope includes 10 times more examples than prior benchmarks.  and (3) incorporates jailbreak prompts that challenge existing safety guardrails.

### Strengths
The paper makes a sound contribution and address an important problem to ensure LLM  safety and alignment in scientific domains. The paper ensure comprehensiveness of the the entities considered benign versous hazorudous by referring to many existing sources. They also disucss how  imporve safety of the models and raise interesting discussion points regarding robustness and specialization.

### Weaknesses
The paper could benefit from clarifying and expanding upon its evaluation. Addressing the following questions may help enhance understanding:

What does the number 31K samples refer to? Does it represent 31K diverse instructions, such as those shown in Figure 3?

Could you provide a comparison of the diversity of instructions in this dataset versus those in existing, narrower scope benchmarking datasets? This would help in understanding the dataset’s unique scope.

Since the dataset includes samples from multiple domains, such as medicine, biology, physics and chemistry are all of these domains used to evaluate models specialized in for example say protein LLMs? Naturally, performance may be lower in textual or molecular genomic domains in this case if the model lacks domain-specific knowledge or cannot decline to answer unfamiliar questions. How is a "threat" defined in this context—does it mean responding to a malicious question, or providing a malicious or incorrect answer to an otherwise benign question?


Is the performance reported in the heatmap exclusively on malicious instructions? If so, does few-shot learning impact performance differently on benign questions versus safety-critical evaluations? The paper mentions using both benign and malicious prompts in few-shot settings—does the ratio of these prompt types influence performance? What would be the recommended mix for optimizing safety performance?

Could you elaborate on the quality assurance process? Specifically, how was malicious content identified—was a sample deemed malicious if any reviewer flagged it, or did all reviewers need to reach consensus?

### Questions
It would be helpful to receive a response from the authors on the questions described above.

### Soundness
2

### Presentation
3

### Contribution
3
