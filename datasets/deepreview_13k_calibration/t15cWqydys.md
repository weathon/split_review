# Inferring from Logits: Exploring Best Practices for Decoding-Free Generative Candidate Selection

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Generative Language Models rely on autoregressive decoding to produce the output sequence token by token. Some tasks, such as preference optimization, require the model to produce task-level output consisting of multiple tokens directly by selecting candidates from a pool as predictions. Determining a task-level prediction from candidates using the ordinary token-level decoding mechanism is constrained by time-consuming decoding and interrupted gradients by discrete token selection. Existing works have been using decoding-free candidate selection methods to obtain candidate probability from initial output logits over vocabulary. Though these estimation methods are widely used, they are not systematically evaluated, especially on end tasks. We introduce an evaluation of a comprehensive collection of decoding-free candidate selection approaches on a comprehensive set of tasks, including five multiple-choice QA tasks with a small candidate pool and four clinical decision tasks with a massive amount of candidates, some with 10k+ options. We evaluate the estimation methods paired with a wide spectrum of foundation LMs covering different architectures, sizes and training paradigms. The results and insights from our analysis could inform the future model design.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method for selecting an answer among candidates from a language model without explicitly decoding the answer. Given a question and candidates, a typical scheme would use them as prompt and generate an answer from the LM. In case of extreme classification in which the number of candidates is numerous, the candidates might be omitted from the prompt. The generated answer is then compared against the candidates for selection. However, this process is expensive as it requires a full decoding pass. This paper proposes to use the logits produced directly after encoding the question (and candidates) to induce a distribution over the candidates and pick the highest scoring candidates. This approach doesn't need to generate the full output sequence which could be faster in the scenario when the candidates are long and numerous. Various approaches for using the logits produced after encoding are tested. The experiments are carried out on multiple choice selection tasks and extreme classification tasks with a very large number of lengthy candidates.

### Strengths
-- The proposed problem is well motivated. Not having to decode the answer in mutiple choice QA has potential to imporve runtimes significantly.

-- The proposed approach is simple to implement and is faster tham retrieval and full-decoding based approaches.

-- The experiments on base-versions of language models seem to be promising for short candidate answers.

### Weaknesses
 -- My biggest concern is that the proposed approach shows very poor results in general. For the case in which candidates are not numerous and can be incorprated into the prompt (Table 3), the proposed approach singificantly degrades the performance over nearly all the datasets and LMs. While it shows improvements over the base LMs, it is handily outperformed by instuction-tuned versions of these models.

-- Similar concerns are observed on tasks in which candidates are numerous and long (Table 4). Based on these numbers, I am not convinced that logits produced after encoding contain enough information to help with classification effectively. In table 4, the approach does imporve over Flan-T5. But this model is a very poor baseline to begin with compared to the instruct-LMs.

-- Moreover the performance of the proposed approach degrades with longer candidate lengths. This is precisely the setting in which one would want to use a decoding-free candidate selection approach to save on potentially large decoding costs.

-- The writing could be made mroe concise and direct to describe the ideas in the paper.

### Questions
Please address the concerns above

### Soundness
3

### Presentation
2

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
The paper explores how to use standard autoregressive language models for tasks that require, for a given query, selection from a candidate from predefined candidate pool (making this a form of classification problem). Instead of doing autoregressive decoding and then mapping the output sequence to a candidate, the authors explore “decoding-free” approaches directly select a candidate.

They evaluate several decoding-free methods, including using the logits from the first, last and all tokens from each candidate: multiple-choice QA with limited candidate pools and clinical decision-making with extensive candidate options. Their analysis spans various large language models, from non-instruction-tuned to instruction-tuned, and considers different architectures and model sizes.

The study finds that decoding-free methods *sometimes* are effective alternatives to full-decoding, especially when the model has relatively low performance with decoding-based selection. However, for most cases, it seems decoding an output sequence and matching it to a candidate seems to yield the best results.

### Strengths
- The problem explored is practically relevant: doing classification with decoded outputs from LLMs is always troublesome, requiring dealing with edge cases when they don’t decode one of the possible candidates, marginalization of different lexical forms for candidates, etc… Alternatives methods that perform as well or better would be very valuable.
- Some positive results for classification tasks with very large number of labels/candidates

### Weaknesses
 - My main concern is the practical usefulness of the results: the methods explored seem to quite lacklustre in terms of performance compared normal decoding-based selection. This, coupled with the lack of novelty in proposed methodology (as this is mostly a comparison paper) leads me to not see much actionable insight to take away from this paper. I suggest the clarify and specify practical insights for readers to take away (which methods to use, in which case, etc…)
- The paper also doesn’t touch/compare a fundamental capability that decoding-based approaches allow: chain-of-though. How would the final performance and speed of decoding-based approaches change when chain-of-though is considered, and how does that change the picture of the comparison to decoding-free approaches?
- Overall the paper also has some presentation issues, with a somewhat confusing terminology in section 2 and some typos over the paper.

### Questions
- What are the speeds for the large candidate pool tasks? It seems that it is the case where decoding-free approaches could be more beneficial compared to decoding-based, but it’s unclear what the speed difference is here (as I expected in this case that decoding-free approaches are actually slower)

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
Various methods exist to parse task predictions from large language model (LLM) outputs, yet they lack systematic definition, evaluation, and comparison. Addressing this gap, the authors systematically evaluate decoding-free generative candidate selection methods for LLMs, focusing on scenarios where task-level predictions are made from a set of candidates. The evaluation covers five decoding-free methods alongside the other approaches, such as classification, retrieval, and full decoding, tested across five multiple-choice question (MCQ) datasets, like CommonsenseQA and MMLU, as well as four additional clinical decision-making tasks. From the experimental results, the authors conclude nine key insights to guide future development and application of LLMs.

### Strengths
1. The focus on decoding-free methods shows their potential to reduce computational costs, an increasingly important factor in deploying LLMs in real-time, resource-intensive environments.
2. The paper offers a systematic evaluation of existing candidate selection methods for LLMs, serving as a useful reference given the rapid development and expanding applications of LLMs.
3. The experiments include multiple MCQ datasets and model types, providing actionable insights into the strengths and limitations of each method and thus the practical utility of the findings.

### Weaknesses
1. Technically speaking, the paper functions more as an analysis, evaluating existing methods rather than proposing new approaches. While insights are drawn from the experiments, unfortunately, no new methods are proposed given the concluded insights. Thus, the lack of novel methodology may limit its contribution for a top-tier conference.
2. Although multiple datasets are included, the types of tasks remain limited. Standard classification tasks, such as those in the GLUE benchmark for evaluating natural language understanding, are missing. Instead, the choice of clinical decision tasks is not well-motivated or explained, which may lead to results that are biased toward a specific domain.
3. Although the paper provides insights from experimental results, it lacks a clear recommendation on the best technique to use in general settings. The insights largely focus on numerical comparisons without deeper investigation, leaving it unclear which method is generally preferable or in what contexts specific methods may excel, and the according reason.

### Questions
1. What is the definition of "decoding" in the context of "full decoding" in this paper? Are not the logits considered part of the decoding process? If so, what specifically makes logits-based methods "decoding-free"?
2. The table summarizing differences across various methods is helpful. Since the mapping function is task-dependent, it would be useful to this in the table.
3. The experimental setup and results are not organized in a standard format. It would improve clarity to separate different task groups into individual sections rather than combining all setups in one section and all results in another.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper evaluates different approaches for candidate selection using large language models (LLMs). Specifically, it compares two categories of methods: (i) decoding, where the model generates a candidate based on an instruction and query, followed by post-processing, and (ii) estimation, where candidate selection is based on examining the logits of the model in response to the instruction and query. The authors benchmark models of various sizes, both with and without instruction fine-tuning, across candidate selection tasks of varying difficulty. They find that estimation methods generally improve the performance of models without instruction fine-tuning but reduce the performance of instruction-fine-tuned models. Additionally, they observe that the effectiveness of estimation methods varies by task.

### Strengths
When considering how to perform candidate selection with generative models, there are several design choices to make: for example, should we generate candidates by decoding, or infer them directly from the model’s logits? Evaluating how these decisions affect downstream performance could be helpful for practitioners in making informed choices. For this reason, I find the premise of this paper quite valuable.

### Weaknesses
**Framing:** The framing in this paper, especially in the abstract, is unclear and could be improved. For instance, the abstract begins by discussing the limitations of decoding candidates from LLMs, which gives the impression that the paper will propose more efficient methods for candidate selection. To address this, I suggest introducing the evaluation focus right from the start to set clearer expectations.

**Presentation:** The paper’s presentation could be significantly improved in a few areas:

1. Consistency: Each category of methods should have a consistent label. Currently, terms like “decoding-free methods,” “estimation methods,” and “candidate selection without decoding” are all used to describe the same category, which can confuse readers.

2. Avoid vague terms: Certain terms and descriptions lack clarity. For example, the authors mention that “decoding-based methods cut off the gradient flow and prevent optimization,” without specifying what kind of gradient flow or optimization issue they’re referring to. In another instance (line 390), they state that “decoding-free methods are not influenced by trajectory biases,” but it’s unclear what “trajectory” means or what types of biases are involved. Similarly, in line 395, they write, “estimation methods rely solely on the logits without capturing the token dependencies within the output,” which could benefit from a more precise explanation.

**Method:** In an evaluation paper, one of the main objectives is to provide insights that practitioners can use. However, this paper lacks interpretations of the results, often leaving the reader with more questions than answers. For instance, in Table 4, it appears that estimation methods consistently reduce the performance of instruction-tuned models. One might expect that, since instruction-tuned models are more calibrated for task performance, their logits would align better with the reference candidates. However, there’s a large performance gap between estimation and decoding methods, with estimation methods performing notably worse. Additionally, the table shows variations in the performance of different estimation techniques across tasks, but the authors do not analyze or interpret these differences, only noting that certain techniques work better for some tasks than others. Finally, an essential aspect missing from the evaluation is the best practice of performing calibration [1] during decoding, which is not addressed in the paper.

[1] [Calibrate Before Use: Improving Few-Shot Performance of Language Models, Zhao et al.](https://arxiv.org/pdf/2102.09690)

### Questions
Most questions are in the weakness section. 

Line 462: why isn't that phrase part of the prompt? usually, the first token refers to the first token in the answer, right?

### Soundness
2

### Presentation
2

### Contribution
2
