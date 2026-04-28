# LongHalQA: Long-Context Hallucination Evaluation for MultiModal Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Hallucination, a phenomenon where multimodal large language models~(MLLMs) tend to generate textual responses that are plausible but unaligned with the image, has become one major hurdle in various MLLM-related applications. Several benchmarks have been created to gauge the hallucination levels of MLLMs, by either raising discriminative questions about the existence of objects or introducing LLM evaluators to score the generated text from MLLMs. However, the discriminative data largely involve simple questions that are not aligned with real-world text, while the generative data involve LLM evaluators that are computationally intensive and unstable due to their inherent randomness. We propose LongHalQA, an LLM-free hallucination benchmark that comprises 6K long and complex hallucination text. LongHalQA is featured by GPT4V-generated hallucinatory data that are well aligned with real-world scenarios, including object/image descriptions and multi-round conversations with 14/130 words and 189 words, respectively, on average. It introduces two new tasks, hallucination discrimination and hallucination completion, unifying both discriminative and generative evaluations in a single multiple-choice-question form and leading to more reliable and efficient evaluations without the need for LLM evaluators. Further, we propose an advanced pipeline that greatly facilitates the construction of future hallucination benchmarks with long and complex questions and descriptions. Extensive experiments over multiple recent MLLMs reveal various new challenges when they are handling hallucinations with long and complex textual data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new benchmark for evaluating hallucinations in multi-modal large language models (MLLMs).
The paper makes use of GPT4V to generate image-level and object-level descriptions and conversation data for a set of images from VisualGenome. These wider range of generated data enables the proposed benchmark, LongHalQA, to evaluate various types of potential hallucination which go beyond the typical object level analysis (e.g. Is there a cat in the image?). The proposed method suggests two types of evaluation: (1) Hallucination Discrimination - the model must answer a MCQ about generated data (potentially containing hallucinations), to determine if the generated data contains hallucinations based on the image and the cause of the hallucination if present; (2) Hallucination Completion - the model must answer a MCQ, correctly selecting the answer which truthfully completes a partial conversation or description.
The authors conduct experiments on a range of open-source MLLMs and the closed-source GPT4o. They show that CoT prompting often has little or negative effect on results on LongHalQA. Finally they conduct a study in which hallucinations in free-form generations from their questions yield similar results to using their MCQ formulation.

### Strengths
This paper correctly identifies that many prior hallucination works focus on the narrow topic of object existence at an image level. To overcome they create questions which expand the evaluation to object level descriptions, object locations, attributes etc.

Their experimental results are numerous and allow the reader see the advantages/disadvantages of each model in the different types of question in LongHalQA (Table 2-5).

The authors make comparisons of their MCQ method to a free-form generation method in Section 6 and demonstrate the advantages of using MCQ over a free-form method in terms of efficiency of evaluation.

### Weaknesses
I have two main weaknesses with this paper, unfortunately both of which I consider pretty major.

### 1. The logic behind the creation of the benchmark itself.

As detailed in Section 4, all of the LongHalQA data comes from generations with GPT4V, this includes the descriptions, conversations etc. These generations are then analysed/modified with a number of checks. Furthermore, the question options themselves are generated with GPT4V. Therefore when evaluating a model X using LongHalQA, you are conditioning all reasoning/grounding/recognition of model X on the range of hallucinations GPT4V might make. This leaves a large range of potential hallucinations that are specific to model X which are left to be analysed, which may only be obtained by generating descriptions/conversations using model X rather than GPT4V. Taking Figure 1, GPT4V and the method used in Section 4 have created a hallucination regarding the number of people seated in the carriage. Now this is a hallucination of GPT4V + Section 4, _not_ of model X. Model X may have hallucinated the species of animal, the colour of the carriage etc, all of which is left potentially undiscovered because the hallucinations model X is asked to evaluate in LongHalQA are not its own, I therefore find the logic of this benchmark slightly confused. The free-form generations of methods like that of Kaul et al. and Jiang et al. referenced in the paper need the model being evaluated e.g. Model X to _actually generate_ its own text and therefore its own potential hallucinations.

### 2. Lack of details and clarity.

The crucial step in this work is the generation of the data for LongHalQA, detailed in Section 4. I find this section to be extremely thin on details and lack clarity.
1. L291 "...then analyze and filter them based on dataset annotations and GroundingDINO...", no information is given on how this process is done.
2. L297, "as illustrated in Appendix B." Appendix B contains a list of definitions of hallucinations used in this work.
3. L303, "Second, names of object present in the data are extracted, and certain image understanding tools such as GroundingDINO...", there are no details on how objects present in the data are extracted, which data? VG annotations or names in the GPT4V generated data or both? Which image understanding tools other than GroundingDINO are used?
3. L314-319, GPT4V is being used to generated hallucination explanation pairs, but there is no indication that manual checking is used here despite the authors accepting that GPT4V suffers from "sever hallucinations" (L298), the logic here seems confused on the ability of GPT4V to create such specific data which only contains one error which is also useful for evaluation.
4. L320-L346, same arguments as above with the ability of GPT4V to this accurately.
5. L344 "except the hallucination checking that involves optional human verification" does this mean human verification is used or not? What is the effect of using human verification in the data vs not?

Additionally as a more general point, the prompt templates used in Appendix C are extremely hard to follow without any examples, e.g. in Figure 6 what is "Possible Content"? The main text asks the reader to refer to Appendix C (L465) for details and then appears to simply paste the prompts used with no explanation of what goes where.

### Questions
### 1. Logic Behind the Benchmark Creation
1. Since all LongHalQA data is generated by GPT-4V, isn’t Model X limited to analysing GPT-4V’s specific hallucinations rather than its own?
2. Could Model X be missing its unique hallucinations because it doesn’t generate its own descriptions or conversations in LongHalQA?
3. Wouldn’t a model evaluation approach where Model X generates its own text reveal more relevant hallucinations, as done in Kaul et al. and Jiang et al.?

### 2. Lack of Details and Clarity
1. How are dataset annotations and GroundingDINO used to filter the LongHalQA data? Can details on this process be provided?
2. How are objects identified in the data? Are these from VG annotations, GPT-4V data, or both?
3. Other than GroundingDINO, which image understanding tools are used, and how?
4. If GPT-4V produces hallucination explanation pairs, is there manual verification, especially given its acknowledged hallucination issues (L298)?
5. In what cases is human verification used for hallucination checking, and how does it impact the dataset?

### Additional Clarity
1. Can examples be given to the prompt templates in Appendix C to clarify instructions like "Possible Content" etc. (Figure 6)?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a long-context hallucination benchmark. This benchmark aims to solve two problems in the existing evaluation pipeline: it is too easy for discriminative tasks and too time-consuming for open-ended generative tasks. To achieve this, the authors propose the LongHalQA, which unifies discriminative and generative tasks as multi-choice problems. Also, they formulate the construction of LongHalQA as a pipeline to construct future hallucination benchmarks with long and complex questions and descriptions.

### Strengths
1. The paper is well-written and easy to follow. 
2. The motivation is reasonable and practical. I think this benchmark will accelerate the development of MLLMs on hallucination. 
3. The analysis of the experiment is relatively comprehensive.

### Weaknesses
1. A little small number of evaluated models.
2. No comparison between the performance of existing methods towards solving the hallucination of MLLMs. I'm interested in whether existing methods have improved on LongHalQA.
3. Lack of related work about the method about how to decrease the hallucination of MLLMs

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new MLLM hallucination benchmark consisting of both hallucination discrimination and hallucination completion questions. The author unifies both discriminative and generative hallucination evaluation into the form of multiple-choice question where models only have to decode one token as response. The results show the proposed benchmark is challenging for both open-source MLLMs in varying sizes and strong GPT-4o.

### Strengths
1. The proposed benchmark can contribute the further development of this field tackling and analyzing the hallucination of MLLMs.
2. The proposed unification of discriminative question and generative question largely saves the evaluation cost via reducing the decoding sequence length.

### Weaknesses
1. Experimental results in Table 8 do not suggest a strong consistency between generation accuracy and mcq accuracy. For example, Fuyu-8b and LLaVA 1.5-7b exhibits score difference -12.41 in mcq while -41.0 in generation. It is necessary to include more methods into consideration, especially thous proposed to tackling hallucination of MLLMs such as LLaVA-RLHF, RLHF-V, Silkie and POVID.
2. Hallucination pairs are generated by GPT-4V, which are prone to generate hallucinated visual description. The author have to explain how #317 controls the generation quality.

### Questions
1. It is known that [LLMs are non-robust multiple-choice selectors](https://arxiv.org/abs/2309.03882). How do you tackle this problem during constructing this benchmark?
2. #419 mentions the 'ranking-based accuracy` of Fuyu-8B, while I could not find the corresponding results in Table 4. It is a writing issue?

### Soundness
2

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
5

### Summary
The paper addresses the issue of hallucination in multimodal large language models (MLLMs), where generated text doesn't match the input image. To solve problems with existing benchmarks, the authors propose LongHalQA, a new benchmark with 6,000 complex hallucinatory texts that mimic real-world scenarios. It introduces two tasks: hallucination discrimination and hallucination completion, which combine both discriminative and generative evaluations into a single multiple-choice format. This approach avoids the need for LLM evaluators, making the evaluation process more reliable and efficient. The paper also presents a new pipeline for creating complex hallucination benchmarks and provides experiments showing that recent MLLMs struggle with long, complex text.

### Strengths
1. LongHalQA addresses the limitations of previous benchmarks by creating a comprehensive dataset of hallucination text that mirrors real-world scenarios, providing a more accurate and complex testing environment for MLLMs.

2. By eliminating the need for LLM evaluators, the benchmark ensures more stable and reliable results, avoiding the randomness and computational intensity associated with LLM-based evaluations.

3. The combination of both discriminative and generative evaluation tasks in a multiple-choice format allows for a holistic assessment of MLLM performance in handling hallucinations, making the evaluation process more efficient.

### Weaknesses
1. How to evaluate model with the Hallucination Completion task?  What is the prefix text for evaluation? Is it the first word?
2. Why the Hallucination Completion can be seen as generative evaluation? The multi-choice question still is discriminative question.
3.  “then analyze and filter them based on dataset annotations and GroundingDINO”: how did authors analyze and filter?
4. Lack of comprehensive survey of hallucination on Large Vision-Language Models.
[1] Object hallucination in image captioning
[2] Halle-switch: Rethinking and controlling object existence hallucinations in large vision language models for detailed caption
[3] FaithScore: Fine-grained Evaluations of Hallucinations in Large Vision-Language Models
[4] Analyzing and mitigating object hallucination in large vision-language models
[5] FGAIF: Aligning Large Vision-Language Models with Fine-grained AI Feedback
5. The proposed LLM-free hallucination benchmark does not offer significant advantages, as the approach still requires various tools, LVLMs, and manual verification, leading to low efficiency.
6. The benchmark has not demonstrated greater reliability compared to existing ones, such as through experimental validation.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2
