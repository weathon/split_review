# Drawing the Line: Enhancing  Trustworthiness of MLLMs Through the Power of Refusal

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Multimodal large language models (MLLMs) excel at multimodal perception and understanding, yet their tendency to generate hallucinated or inaccurate responses undermines their trustworthiness. Existing methods have largely overlooked the importance of refusal responses as a means of enhancing MLLMs reliability. To bridge this gap, we present the Information Boundary-aware Learning Framework (InBoL), a novel approach that empowers MLLMs to refuse to answer user queries when encountering insufficient information. To the best of our knowledge, InBoL is the first framework that systematically defines the conditions under which refusal is appropriate for MLLMs using the concept of information boundaries proposed in our paper. This framework introduces a comprehensive data generation pipeline and tailored training strategies to improve the model’s ability to deliver appropriate refusal responses. To evaluate the trustworthiness of MLLMs, we further propose a user-centric alignment goal along with corresponding metrics. Experimental results demonstrate a significant improvement in refusal accuracy without noticeably compromising the model’s helpfulness, establishing InBoL as a pivotal advancement in building more trustworthy MLLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents the Information Boundary-aware Learning Framework (InBoL) for enhancing the trustworthiness of multimodal large language models (MLLMs). MLLMs often produce hallucinated or inaccurate responses, especially when faced with ambiguous or unfamiliar inputs. InBoL addresses this by training models to recognize “information boundaries”—distinguishing between questions they can answer confidently and those they should refuse. The framework leverages two novel training techniques: “I Don’t Know” (IDK) Instruction Tuning (IDK-IT) and Confidence-aware Direct Preference Optimization (CA-DPO), both aimed at improving refusal responses for uncertain or ambiguous queries.

To evaluate trustworthiness, the authors introduce a user-centered metric that rewards accurate and helpful responses while penalizing misinformation. Experimental results indicate that InBoL improves refusal accuracy without compromising the helpfulness of responses, setting a new benchmark for trustworthiness training in MLLMs. This work proposes a robust approach to model alignment for safe and reliable AI responses, particularly in vision-language tasks.

### Strengths
The paper leverages a decrease in accuracy robustness of some VLLM’s responses to create a dataset that establishes clear boundaries for confident responses, incorporating refusal mechanisms for cases where the model might otherwise respond incorrectly. Through training, combined with experimentation, the study shoes the reduction of unreliable responses through the use of synthetic data in training.

### Weaknesses
 - Limited Scope: Experiments focus narrowly on Visual LLMs (with claim for MLLMs) and small models (e.g., LLaVA 1.5), lacking insights into broader MLLM applicability or resource requirements.

- Lack of Explanatory Rejection: The model is trained to learn outright refusals lack explanations. Adding explanations or visualizations of boundaries could enhance user trust.

- Conceptual and Metric Issues: The construction of the "unknown" dataset used for training lacks clear justification for how it genuinely promotes trustworthiness in LLMs. Furthermore, the trustworthiness score proposed in the paper is unnormalized, which can be different across different dataset with different theoretical max accuracy rate. Answered accuracy might be a more objective measure. There’s also a lack of motivation behind the metrics, authors say the old metric is bad because “unknown” questions domain is hard to know, but then create such domain in Fig 3)

- Boundary and Hallucination Exploration: The simplistic boundary approach doesn’t adequately address the cause of hallucination, or accounting for decrease accuracy of responses. This investigation of cause of not refusal is lacking.

- Methodology Novelty: Core techniques (PEFT, DPO) are standard, limiting innovation, and newer methods like inference-time corrections could improve boundary handling.

- Dependence on GPT-4o: Dependence on GPT-4o for data generation risks biases from its potential hallucinations. Limited discussion of pipeline generalizability weakens applicability.

- Missing Literature, Limitations and Ethics Review: A more complete literature review and ethical discussion are needed (not in the appendix), currently relegated to the appendix, to frame the work’s limitations and ethical impact fully. Also the cost of InBol is lacking, which can be heavy to generate such dataset with model responses of so many benchmark in practice.

### Questions
- How does InBoL innovate beyond existing methods like PEFT and DPO? While InBoL uses “I Don’t Know” (IDK) Instruction Tuning and Confidence-aware Direct Preference Optimization (CA-DPO), which build on established techniques, could you clarify any additional features that make InBoL uniquely suited to MLLMs? Consider highlighting or incorporating advanced techniques, such as inference-time adjustments, to distinguish InBoL further.
- Why did you choose an unnormalized trustworthiness score over a normalized or cross-comparable metric? The score is dataset-dependent, which could affect its generalizability across datasets. Could you discuss why this metric was prioritized over an alternative like answered accuracy? Introducing a normalized metric or justifying this choice could clarify how trustworthiness is assessed across various MLLMs and test sets.
- How does InBoL’s boundary creation address hallucination causes and refusal failures? Defining boundaries by confidence thresholds doesn’t appear to directly address why hallucinations or refusal failures might occur. Would expanding boundary classifications or including visual boundary explanations aid in understanding these limitations?
- How does the dependence on GPT-4o for data generation impact generalizability? Relying on GPT-4o to generate unanswerable questions may risk inheriting its biases. Could you describe any mitigations for GPT-4o-induced biases in the dataset and discuss InBoL’s performance if an alternative model or method is used to create unanswerable data?
- What are your expectations for InBoL’s generalizability to larger models and domains beyond visual tasks? The experiments focus on smaller models (e.g., LLaVA 1.5) and visual LLMs. Providing experimental insights on InBoL’s scalability to more complex or varied models would clarify its broader applicability.
- Would explanatory feedback enhance trust in refusal responses? InBoL’s refusal responses currently lack explanations, potentially limiting user trust. Have you considered integrating explanatory refusals to improve user understanding, particularly when refusals stem from visual limitations or knowledge boundaries?
- Could you expand on the ethical implications of refusal mechanisms? The ethical considerations section is limited, mainly relegated to the appendix. Given the potential for user reliance on refusal responses, would a more thorough discussion on the ethical impacts of this feature strengthen the paper’s contextual relevance?

### Soundness
3

### Presentation
2

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
This paper presents Information Boundary-aware Learning Framework (InBoL) to enhance the reliability of Multimodal Large Language Models (MLLMs) by systematically training them to recognize their knowledge and perception 'intrinsic' and 'extrinsic' boundaries and refuse to respond when they lack sufficient information. The InBoL framework includes a data generation pipeline to generate structured data (with refusal questions generated with gpt-4o prompting) for 'IDK' Instruction Tuning (IDK-IT) and Confidence-aware Direct Preference Optimization (CA-DPO) (built on top of https://github.com/opendatalab/HA-DPO) — the dataset is designed to improve the model’s accuracy in refusal responses without sacrificing helpfulness to some extent. The paper adopts a user-centric evaluation approach, emphasizing human preference as the core metric for assessing trustworthiness.

### Strengths
- the paper disentangles existing value alignment methods (as noted in section 2.1) to create a model-agnostic objective by using user preferences for DPO and generating structured datasets using confidence sampling and LLM judges for creating model fine-tuning recipes. 

-  the paper integrates refusal as an explicit mechanism for trustworthiness. This systematic refusal approach seems to be unique among MLLM alignment techniques.

- The paper’s combined approach for instruction tuning for cautious response handling and CA-DPO for adaptive preference optimization proves effective in experimental results, especially for out-of-domain (OOD) tasks.

### Weaknesses
 - While IDK-IT effectively reduces misinformation, it can limit model's helpfulness (contrary to what the authors claim). One can increase truthfulness by giving refusal responses along with some justification for why the model refused to answer. Authors have not addressed this aspect of refusal with reasoning in the paper. 

- For section 3.1, authors give an example for extrinsic information boundary - similarly, it will help to give an example for intrinsic information boundary. Also, Figure 1 examples ii and iii, how can we use the protocol mentioned in the paper to respond appropriately to the questions. The demarkation of intrinsic and extrinsic responses is still confusing.

- In Table 3, it's not clear if the CA-DPO results also include the IDK-IT step. 
- While the paper builds up on intrinsic and extrinsic knowledge sources and that knowledge can come from model's parameters or from the visual content, there are no experiments to dissect this aspect of knowledge grounding. This analysis can significantly improve the quality of the paper (given the framing of the method for increasing trustworthiness)
- There is no comparison with other methods mentioned in the paper for increasing trustworthiness of reducing hallucinations as well as response refusal.

### Questions
- In Table 3, it's not clear if the CA-DPO results also include the IDK-IT step. 
- While the paper builds up on intrinsic and extrinsic knowledge sources and that knowledge can come from model's parameters or from the visual content, there are no experiments to dissect this aspect of knowledge grounding. This analysis can significantly improve the quality of the paper (given the framing of the method for increasing trustworthiness)
- There is no comparison with other methods mentioned in the paper for increasing trustworthiness of reducing hallucinations as well as response refusal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors of this paper aim to address a key issue in multimodal large language models (MLLMs). While MLLMs are powerful and can handle various types of data, they often generate inaccurate or incorrect responses, which diminishes user trust. Many existing approaches overlook the importance of "refusal to answer." In fact, enabling models to refuse answering when information is insufficient can make them more reliable. To address this gap, the authors propose a new framework called InBoL, which trains models to refuse to answer when uncertain. This framework also defines clear criteria for when a refusal is appropriate and introduces a comprehensive data generation process and training strategy to enhance the model's ability to refuse when necessary.

They also present evaluation methods for assessing the model's trustworthiness, focusing on user experience and relevant scoring metrics. Experimental results show that InBoL significantly improves refusal accuracy without compromising the model's usefulness, making it more trustworthy overall.

### Strengths
This paper introduces a new data construction pipeline that systematically classifies questions based on model dependence, generates unanswerable questions and organizes them in a standardized format for further training. The confidence estimation method improves the accuracy of the answer by combining string matching and LLM evaluation, ensuring a more robust assessment of model knowledge. The generation of unanswered questions allows the model to learn not to provide incorrect responses when there is insufficient information, but to choose to refuse to answer, thereby improving the credibility of the model and reducing the risk of misleading users. The Advanced training strategies improve model reliability by balancing accuracy and rejection rates, further reducing false information while improving performance. Experiments on different datasets prove the generality and reliability of the method, making this method very valuable for future multimodal research.

### Weaknesses
The paper lacks a thorough explanation of how to balance between increasing the refusal rate and maintaining accuracy. The trade-off mechanism between these two aspects is not sufficiently discussed. Additionally, while the current setup may not consider user frustration as a major concern, I’m still curious whether this could become an issue. Would it be beneficial for the model to offer users some form of feedback when refusing to answer, such as providing partial information or clarifying why it cannot respond? This might help improve user experience and prevent frustration by giving more context to the refusal, rather than leaving users without any explanation.

The approach of generating unanswerable questions by randomly swapping images and questions may not effectively simulate real-world unanswerable scenarios. It raise a concern about whether this method accurately reflects realistic situations where a model cannot provide a correct answer.

The paper also falls short in providing examples of unanswerable questions with varying types and levels of difficulty, limiting the demonstration of question diversity. It is unclear whether different prompts or variations in prompt structure are used to encourage this diversity. Furthermore, the strategy for generating unanswerable questions might need to be dynamically adjusted based on the capabilities of different models, but this aspect is not explored.

### Questions
Could you elaborate on how you balance increasing the refusal rate with maintaining accuracy? It would be helpful to understand more about the trade-off mechanism between these two goals. Additionally, do you have any strategies in place to address potential user frustration if the model refuses too often?

Do you think the strategy for generating unanswerable questions should be adjusted dynamically depending on the model's capabilities?

### Soundness
3

### Presentation
2

### Contribution
3
