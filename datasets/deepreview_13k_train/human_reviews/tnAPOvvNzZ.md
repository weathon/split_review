# JsonTuning: Towards Generalizable, Robust, and Controllable Instruction Tuning

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Instruction tuning has become an essential process for optimizing the performance of large language models (LLMs). However, current text-to-text instruction tuning methods, referred to as TextTuning, exhibit significant limitations in terms of generalization, robustness, and controllability, primarily due to the absence of explicit task structures. In this paper, we introduce JsonTuning, a novel structure-to-structure approach for instruction tuning. By utilizing the versatile and structured format of JSON to represent tasks, JsonTuning enhances generalization by enabling the model to comprehend essential task elements and their interrelations, improves robustness by reducing ambiguity, and increases controllability by providing explicit control over the output. We conduct a comprehensive comparative analysis between JsonTuning and TextTuning using various language models and evaluation benchmarks. Our experimental results demonstrate that JsonTuning consistently outperforms TextTuning across a range of applications, showing marked improvements in performance, robustness, and controllability. By addressing the inherent limitations of TextTuning, JsonTuning reveals significant potential for developing more effective and reliable LLMs capable of managing diverse scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes JsonTuning,  a novel structure-to-structure approach for instruction tuning. It leverages the widely used JSON format and uses the structured format to define tasks. Empirical results show JsonTuning improves TextTuning on generalization, robustness, and controllability. Ablation study shows the label space and control information are both curial for JsonTuning. The paper also analyzes the effects of data size and structured tasks.

### Strengths
- Originality: The paper proposes JsonTuning, which is a new format of instruction tuning. It reformats standard instruction tuning data into JSON format to reduce ambiguity and improve controllability. The proposed method is novel in that it leverages the LLM's understanding of structured data format - JSON and makes use of it in downstream instruction tuning.
- Clarity: The paper is well-written and easy to follow.
- Quality: The claims in this paper are well supported by citations or empirical results. The authors clearly demonstrate JsonTuning's advantages in generalization, robustness, and controllability.

### Weaknesses
 - Significance: the format of instruction tuning data is only one of the many system choices of the overall instruction tuning. Others include tasks, base model, domains, and languages. Since the paper only focuses on the data format on a selection of tasks, the significance is limited.
- Soundness: It is not clear if a TextTuning model with candidate answers and output control in plain text would also perform as good as JsonTuning. In other words, how much gain was from the structured format of JSON itself?

### Questions
- How did you construct training data for JsonTuning from plain text instruction tunning data? Did you use human annotator to do the conversion or use another language model?
- Why did you choose JSON format instead of other popular structured formats, such as XML and YAML?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper uses JSON as a formatting scheme to tune language models, and shows that this can help models learn and generalize better than formatting examples as plain text. JSONTuning also reduces prompt sensitivity.

### Strengths
- The paper is clear and easy to follow. 
 - The method is simple and works well.

### Weaknesses
 - In my opinion this paper needs some sort of analysis of the number of additional tokens introduced by the JSON format for training and inference. The additional training cost is probably negligible and unimportant, but the additional FLOPS and encoded/decoded tokens for the JSON format will add up for inference. Note: I am not saying that the fact that JSON-formatted examples have extra tokens is a weakness, but this extra cost should at least be quantified in my opinion. 
 - I generally don't think papers should be penalized harshly for a lack of novelty or for overly simple methods, but it must be acknowledged that the idea of "format exampels as JSON instead of plain text" can only be taken so far. Note: I am not saying this is grounds for rejection, just that this paper's impact and contribution is limited.

### Questions
- How do text-tuned models behave as a base for JSON-formatted examples? For example, I think some of the following questions should be answered or at least discussed: 
   * What if we text-tune the model and then JSONTune it on a small dataset? 
   * What if we text-tune the model and then use JSON-formatted examples in a few shot prompt? 
 - What is the decoding mechanism used for evaluating models? I assume it is just greedy sampling, but it would be nice for more evaluation details to be in the appnendix. 
 - How often was invalid JSON generated? What do the authors think about constrained decoding schemes like [Scholak et al](https://arxiv.org/abs/2109.05093), is there any point of using constrained decoding to improve JSONTuned models?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new approach called JsonTuning, which leverages the structured JSON format to represent tasks. JsonTuning improves generalization by helping the model understand task elements and their relationships, enhances robustness by reducing ambiguity, and offers greater control over the model's output. The paper presents a thorough comparative study with different language models and evaluation benchmarks, demonstrating that JsonTuning surpasses TextTuning in various applications, achieving better performance, adaptability, robustness, and control.

### Strengths
This paper provides a very simple method to convert the original instruction tuning into a unified Json format. The authors also conduct comprehensive comparison against baselines trained under text-to-text formulation, and show that JsonTuning can harvest better performance. The ablation studies help us to better understand the effect of the subparts such as label space and control information.

### Weaknesses
Despite the commendable performance exhibited by JsonTuning, there are still several notable weaknesses:

**Introduction of Additional Knowledge in Input**: The utilization of Json formatting can aid models in generating outputs that conform to the constraints specified in the Json input. However, it also introduces supplementary knowledge, such as information pertaining to input and output types, which is originally absent in the unstructured textual instructions. To facilitate a fair comparison, it becomes essential to incorporate the information present in the Json input but absent in the textual input into the original text instructions. This allows for a comprehensive assessment of whether the Json format indeed outperforms the text format.

**Potential Incompleteness of Generalization Experiments**: While the training dataset encompasses a diverse range of tasks, including Flan and P3++, there appears to be some overlap between the types of tasks assessed during testing and those encountered in training. It is pertinent to explore whether the model can adeptly generalize to entirely unseen task types, which may not have been covered by the training data. Furthermore, the evaluation tasks, primarily centered on structure prediction, demand output format constraints. However, for the field of instruction tuning, there exists a research interest in user-oriented instruction following evaluation, exemplified by AlpacaEval. In cases involving more open-ended instruction data, the Json format may not bring additional benefits since there are no specific constraints imposed on the output format. It also remains uncertain how the model performs on the Super-NI test set, a widely employed dataset assessing a model's ability to follow instructions.

**Challenges for Real-World Applications**: The practical applicability of Json-tuned models is constrained by the need to manually craft complex Json prompts that delineate output fields and their corresponding types. For users lacking expertise in computer science, utilizing such models proves challenging, as they may lack the proficiency required to construct a Json-formatted instruction. Unless a method for automatically generating Json instructions becomes available, the utility of this approach is notably limited in real-world scenarios.

### Questions
1. Will there be a significant improvement after fine-tuning code LLMs (e.g., CodeLLAMA) on the Json instruction data? It seems that code LLMs might be a better counterpart that learns the Json data more easily.

2. There might be several missing relevant references. The first one have studied Json-format instruction data. The second one is a resource that has the similar formulation with Super-NI and can be represented in well-structured Json format as well: 
- Did You Read the Instructions? Rethinking the Effectiveness of Task Definitions in Instruction Learning. Yin et al., 2023.
- Dynosaur: A Dynamic Growth Paradigm for Instruction-Tuning Data Curation. Yin et al., 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose JsonTuning which unifies different text-to-text tasks into a structured format, i.e. json format. Experiments and analyses are conducted on various popular benchmarks with models from the LLaMA family ranging from 7B to 13B.

### Strengths
* The motivation is simple and easy to understand.
* The paper is well-written and easy to follow.
* Comprehensive experiments and analyses are provided to support the authors' claims.

### Weaknesses
There are several key limitations of the proposed approach:
* Context window consumption: JsonTuning demands much more tokens than TextTuning and it poses a challenge both in the training and inference time. One key aspect of current LLMs is their context window, and how to use it efficiently. The authors should provide evidence relating to the extra overhead on training/inference of JsonTuning. Specifically, a detailed breakdown of the token usage for various tasks and input/output lengths would be beneficial to understand the practical implications of this overhead. Furthermore, the impact of this increased token usage on computational resources, such as memory and processing time, should be quantified and discussed.
*  It is not also obvious to transform the user's request into a structured format. Despite the authors' arguments on the generalization capability of JsonTuning, structured object like Json still lags far behind natural language in terms of expressivity. The tasks concerned in the work are relatively easy and can be transformed into json format with less effort. However, I am not convinced this generalizes to real industrial use cases where the user's request could be far more complex. For example, consider a scenario where a user needs to extract highly nuanced information from a complex document or engage in a multi-turn dialogue with the model. The mapping of such complex interactions into a rigid JSON structure might prove to be cumbersome and limit the model’s ability to capture the full range of user intent. The paper needs to address how it would handle such complex scenarios.
* A simple question: assume a user requests the model to produce output following json format at the first place. Then how the output control be defined on the input side? I suppose it would be a nested json and could be fragile for the model to take as input. This raises concerns about the practical usability of the method, particularly in cases where the desired output structure is itself complex and requires careful specification. The authors should clarify how the model can effectively handle nested JSON structures for both input and output, and what mechanisms are in place to ensure the model correctly interprets and generates these structures.

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
