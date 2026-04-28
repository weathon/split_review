# LLM Distillation for Efficient Few-Shot Multiple Choice Question Answering

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 6, 3

## Abstract
Multiple Choice Question Answering (MCQA) is an important problem with numerous real-world applications, such as medicine, law, and education. The high cost of building MCQA datasets makes few-shot learning pivotal in this domain. While Large Language Models (LLMs) can enable few-shot learning, their direct application in real-world scenarios is often hindered by their high computational cost. To address this challenge, we propose a simple yet effective approach that uses LLMs for data generation and scoring. Our approach utilizes LLMs to create MCQA data which contains questions and choices, and to assign probability scores to the generated choices. We then use the generated data and LLM-assigned scores to finetune a smaller and more efficient encoder-only model, DeBERTa-v3-base by leveraging distillation loss. Extensive experiments on the Massive Multitask Language Understanding (MMLU) benchmark demonstrate that our method improves accuracy from 28.9\% to 39.3\%, representing a gain of over 10\% compared to a baseline finetuned directly on 5-shot examples. This shows the effectiveness of LLM-driven data generation and knowledge distillation for few-shot MCQA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes the method of distillation of the large language model to the smaller one for efficient solving of Multiple Choice Question Answering task,  via data generation and distillation loss. Two methods of data generation are considered: generate the whole question-answer structure with answer options in json format (via 5-shot prompting); or generate question-answer pairs obtaining each option separately. Then, the smaller model is trained on the generated data by distillation loss, learning to predict the larger model's probability of the generated options. The evaluation is done on MMLU benchmark. For the ablation study, ARC dataset is used

### Strengths
- The paper is clearly written, and presents a practical method of LLM distillation to a smaller encoder-only model
- A nice ablation study is provided. There are several interesting observations, e.g. increasing the performance with the distill loss + temperature adjustment, or the usage of the format correctness as an implicit sign of the model's confidence.

### Weaknesses
 - The method is rather straightforward and does not contain a significant novelty, although the presented analysis is good
- The practical usefullness of the considered task is not so clear. Indeed, Multiple Choice Question Answering is the specific QA format convenient for LLM's evaluation, but the MCQA results are not necessarily directly connected to the general QA abilities of the model. For encoder-only LLMs, classification-based approach looks more appropriate (i.e. scoring the correctness of the QA pair)
- The model does not outperform Tasksource model which is obtained by the multi-task training of the same backbone: the improvement on MMLU is marginal (+0.5), and on ARC data the proposed approach works significantly worse.

### Questions
Q1. Do you have any idea, if the huge improvement of the performance of DeBerta after distillation is related to improving of the model's question answering ability, or just due to  learning of Multiple Choice QA format?

### Soundness
3

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
This paper aims to enhance the performance of low-computation-cost, only-encode models for few-shot multiple-choice question answering (MCQA) tasks. It leverages large language models (LLMs) to generate a high-quality, task-specific MCQA dataset for training and introduces a training approach that applies distillation loss based on LLM-assigned scores. Experimental results demonstrate the effectiveness of the proposed method: LLM-driven data generation and knowledge distillation for few-shot MCQA.

### Strengths
1. The method is relatively simple and clearly explained.
2. The paper explores the effectiveness of using LLMs to construct data for MCQA tasks, and the proposed distillation loss training method shows notable performance improvements.
3. The paper conducted a relatively comprehensive ablation experiment.

### Weaknesses
1. The method's performance improvement is limited and depends on the strength of the base model. While the gains are more pronounced with the weaker DeBERTa-base model, they are minimal with the stronger Tasksource model, and even slightly decreases in the case of Decompose. 
2. Additionally, when using DeBERTa-base, the best performance (JSON distill) achieved by using only the constructed dataset does not surpass that of a multi-task fine-tuned model (Tasksource).

### Questions
The experiments lack a more detailed analysis of the two data generation methods (e.g., example-based analysis): Why do the two methods (JSON and Decompose) lead to different outcomes in performance? Why does JSON outperform Decompose?

### Soundness
2

### Presentation
3

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
This paper studies the possibility of encoder model with LLM-generated dataset and knowledge distillation. To address current effortful MCQA benchmark making, this paper utilizes LLM’s ability in few shot prompting with two formatting strategies. Then, by distilling the loss of bigger LLM into small, encoder-only model, the paper shows the efficient way to achieve performance nearing that of bigger LLM.

### Strengths
* This paper sheds light again on the encoder-only model, which had been receiving less attention recently.
* The methodology's adaptability to existing domain-specific benchmarks suggests its potential for broad application across diverse fields.

### Weaknesses
**[Novelty is limited]**

The paper’s novelty appears limited, as it does not introduce a new dataset and relies primarily on formatting prompts either in full JSON format or as segmented parts, raising questions on whether these methods constitute a genuinely novel approach. Furthermore, the distillation technique applied here does not seem particularly innovative, as it essentially reduces to a form of fine-tuning. The use of JSON formatting and segmented prompts for data generation, while practical, does not represent a significant methodological advancement. The distillation process, lacking exploration of more advanced techniques, such as attention-based or feature-level distillation, further limits the perceived novelty.

**[Using Encoder-only Models - limited Experimental setups]**

Additionally, while the paper suggests the encoder-only model’s powerful capabilities, this claim is primarily based on improvements from distillation and model size reduction. These factors alone may not suffice to substantiate the model’s claimed "power" without more substantial baseline comparisons, particularly in tasks beyond fine-tuning. The focus on a single encoder model, DeBERTa, without exploring other encoder architectures, raises concerns about the generalizability of the findings. The lack of comparisons with other encoder-only models, such as RoBERTa, which was mentioned to perform poorly without further analysis, makes it difficult to assess whether the improvements are specific to DeBERTa or are broadly applicable to encoder models. Furthermore, the absence of evaluations on tasks beyond MCQA limits the conclusions about the model's overall capabilities.

**[Inadequate analysis of suggested method]**

There is inadequate validation of the quality of the LLM-generated dataset, which raises further concerns about the reliability and applicability of the findings. The analysis of the generated dataset relies solely on semantic similarity, neglecting other crucial aspects of data quality, such as question complexity, diversity, and the correctness of the generated answers. The lack of a thorough analysis of the generated data's characteristics makes it difficult to assess the true impact of the proposed method.

### Questions
* Has there been any comparison with recently released lightweight models, such as those with a 1B parameter size?
* Is there a specific reason why only the DeBERTa encoder model was tested?
* Was there a particular reason for employing few-shot learning in an encoder model instead of using a masked language model (MLM)?
* Does this paper really aligns to the ICLR conference is questionable. Any other natural language processing conference seems more suitable.

### Soundness
2

### Presentation
1

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
This paper presents a novel approach to address few-shot multiple choice question answering (MCQA) by leveraging large language models (LLMs) for data generation and knowledge distillation into a smaller, efficient encoder-only model, DeBERTa-v3-base. The study addresses the computational challenges associated with using LLMs directly in real-world applications and provides a three-step framework involving synthetic data generation, LLM-based scoring, and distillation training. Experimental results demonstrate significant improvements in accuracy over baseline models on the Massive Multitask Language Understanding (MMLU) benchmark, as well as competitive performance compared to larger models like LLaMA-7B and Flan-T5-250M. The paper also includes ablation studies on various generation methods, scoring techniques, and hyperparameters.

### Strengths
1. The approach addresses a relevant problem in natural language processing, providing a practical solution for scenarios where computational resources are limited.
2. The framework is straightforward, and the two methods of data generation (JSON and decomposed) are described in detail, with thoughtful consideration of their benefits and limitations.
3. The paper presents extensive experiments, including performance comparisons, ablation studies, and evaluations on the MMLU benchmark.

### Weaknesses
1. The method relies heavily on the availability of robust LLMs, which may not be readily accessible in languages other than English or for certain domain-specific tasks. This dependence introduces a significant practical limitation, as the quality of the generated data is directly tied to the performance of the LLM used. Furthermore, the computational cost of running these LLMs for data generation can be substantial, potentially negating the efficiency gains of distilling the knowledge into a smaller model. The lack of readily available high-performing LLMs in diverse languages and specialized domains restricts the applicability of this approach.

2. The decomposed generation method, while reducing parsing errors, often results in noisy data due to longer and less structured answers. The increased length and lack of structure can introduce irrelevant information and make it harder for the distilled model to learn effectively. This noise can degrade the overall performance of the model, potentially offsetting the benefits of reduced parsing errors. The trade-off between parsing accuracy and data quality needs to be carefully considered.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors use a few task-specific multiple choice questions as seed examples to get a LLM to generate task-specific, synthetic multiple choice data. They explore two ways of prompting the LLM to generate this data. They train a small, encoder-only model via knowledge distillation using soft labels assigned by the LLM. They show that training on synthetic data via distillation is better than just training on a few non-synthetic task-specific data points directly, and also compare to some other models. The authors also conduct ablation studies regarding the amount of synthetic data, synthetic data generation temperature, and choice of LLM.

### Strengths
(Originality) While synthetic data generation with LLMs and knowledge distillation into transformer based models are both widely used and studied, the authors consider the specific setting of MCQA and distilling a decoder-only model into an encoder-only model, which is a new setting.

(Quality) The authors report results across several random seeds. They also do some nice ablation studies. The limitations section was also of high quality.

(Clarity) The paper was generally clear and easy to follow.

(Significance) As mentioned in originality, this paper explores a setting that is slightly different from past work.

### Weaknesses
 * A couple typos (these didn’t affect my review at all, but just mentioning them)
  * Line 69/70 missing a space
  * Line 179 “a scalar values” -> “scalar values”
* When generating synthetic data, how can you be sure you’re not generating questions that are in the MMLU/ARC test sets (or that are quite close?). It would be nice to see something like nearest neighbors of generated questions, or something like overlap of answer options with answer option sets from the test sets.
* A note on the tasksource+decompose/JSON is I don’t think it can necessarily be concluded that tasksource+JSON is better than tasksource as 0.5 is quite a narrow margin.
* In my mind the main weakness of this paper would be lack of significance.
  * In practice, in the resource constrained setting there are already compelling alternatives to the approach described in this paper. For example, tasksource has the same amount of parameters, comparable performance, and faster inference as it only needs one forward pass. It also doesn't require synthetic data generation for each task. Furthermore, performance is less good than that of e.g., Gemma-2-2b-it and similar models which can be run quite cheaply on even a laptop (especially after quantization). I don’t see when “distillation into DeBERTa” would be used in practice because there are already very compelling alternatives. I'd be happy to hear the authors' take on this, though.
  * A paper definitely doesn't need to be the best "in practice" option to be useful, as it might provide surprising/intuitive insights compared to previous work. However, I don’t find the results of this paper particularly surprising in light of past work. Knowledge distillation is already widely used with LMs, and distillation from larger LLMs to smaller LLMs is done all the time with good results. Synthetic data generation with LLMs is also frequently done, and has been shown to work well. That more synthetic data works better is as expected.

*Strengths & Weaknesses tl;dr*: I think the authors’ study is well thought out and put together, and mostly easy to follow. However, I don’t think it provides substantial insight/methods beyond what already seems to be common knowledge in the research community. I’ve assigned a rating of 3, but I’d choose 4 if it were an option because I think the paper is overall well made but just doesn’t have the level of impact I typically associate with ICLR papers.

### Questions
* On line 245, why is it “approximately 4000 MCQA examples”? Shouldn’t this be exact?
* Why was number of negative examples set to 5 when MMLU and ARC only have 3?
* What temperature was used for the MMLU experiments?
* In Section 3.2, how is a sequence is being transformed into a scalar — [CLS] token? Pooling?
* From Section 3.2 it is my understanding that handling a MCQ with n options requires n forward passes. Is that correct?
* How was inference done for the baseline models?
* When JSON samples are not properly formatted, are they resampled, or are less than 1024 samples used?

### Soundness
3

### Presentation
3

### Contribution
2
