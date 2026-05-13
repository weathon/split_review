# MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for Text-to-Image Generation?

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
While text-to-image models like DALLE-3 and Stable Diffusion are rapidly proliferating, they often encounter challenges such as hallucination, bias, and the production of unsafe, low-quality output. To effectively address these issues, it is crucial to align these models with desired behaviors based on feedback from a \textit{multimodal judge}. Despite their significance, current multimodal judges frequently undergo inadequate evaluation of their capabilities and limitations, potentially leading to misalignment and unsafe fine-tuning outcomes.
    To address this issue, we introduce \algname, a novel benchmark which incorporates a comprehensive preference dataset to evaluate multimodal judges in providing feedback for image generation models across four 
    key perspectives: alignment, safety, image quality, and bias. Specifically, we evaluate a large variety of multimodal judges including smaller-sized CLIP-based scoring models, open-source VLMs (e.g. LLaVA family), and close-source VLMs (e.g. GPT-4o, Claude 3) on each decomposed subcategory of our preference dataset. Experiments reveal that close-source VLMs generally provide better feedback, with GPT-4o outperforming other judges in average. Compared with open-source VLMs, smaller-sized scoring models can provide better feedback regarding text-image alignment and image quality, while VLMs provide more accurate feedback regarding safety and generation bias due to their stronger reasoning capabilities.
    Further studies in feedback scale reveal that VLM judges can generally provide more accurate and stable feedback in natural language (Likert-scale) than numerical scales.
    Notably, human evaluations on end-to-end fine-tuned models using separate feedback from these multimodal judges provide similar conclusions, further confirming the effectiveness of \algname.
    All data, code, models are available at 
\url{https://huggingface.co/MJ-Bench}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MJ-BENCH, a novel benchmark that includes a comprehensive preference dataset to evaluate multimodal judges in providing feedback for image generation models across four key perspectives: alignment, safety, image quality, and bias. Detailed experimental analyses were conducted on CLIP-based scoring models, open-source VLMs, and close-source VLMs.

### Strengths
The paper is well-written and logically coherent. The proposed benchmark is comprehensive, covering aspects such as alignment, safety, image quality, and bias.

### Weaknesses
I would consider increasing my score if these concerns are addressed or resolved.

**1. Comprehensiveness and fairness of the evaluation**: The paper evaluates models like CLIP, LLaVA and GPT-4, but lacks some popular alternative alignment evaluation models such as the Decompose method ([Davidsonian Scene Graph](https://arxiv.org/pdf/2310.18235)) and the Answer Probability Method ([VQAScore](https://arxiv.org/pdf/2404.01291)). Additionally, the paper claims that the alignment dataset was collected from Pick-a-pic, HPDv2, and ImageRewardDB, so evaluating PickScore-v1, HPS-v2.1, and ImageReward in the experiments is unfair because these models have already been trained on similar data or dataset formats.

### Questions
1. Could you please explain how quality control is conducted in the construction of data across different evaluation dimensions? For example, how is a human verification process conducted, and what is the proportion of data that gets filtered?

2. Given the criticisms of CLIP-based methods as 'bag-of-words' and the lack of interpretability and reproducibility when directly asking VLMs to output scores, evaluating and comparing alternative evaluation methods is crucial. It's important to include popular alignment approaches that avoid these weaknesses, such as decomposition methods from [T2i-compbench](https://proceedings.neurips.cc/paper_files/paper/2023/file/f8ad010cdd9143dbb0e9308c093aff24-Paper-Datasets_and_Benchmarks.pdf)  and [Davidsonian Scene Graph](https://arxiv.org/pdf/2310.18235), as well as answer probability methods like [VQAScore](https://arxiv.org/pdf/2404.01291).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
* The paper introduces MJ-BENCH, a benchmark to improve feedback for text-to-image models on alignment, safety, image quality, and bias. 
* Some interesting points are found: e.g., Closed-source VLMs like GPT-4o outperform others overall, while smaller models excel in alignment and quality, and VLMs perform better on safety and bias. Human evaluations confirm MJ-BENCH’s effectiveness for model fine-tuning.

### Strengths
* The writing and presentation of the entire paper are good.
* A comprehensive benchmark is provided, which can further advance research in the related field.
* It further promotes research on RLAIF (Reinforcement Learning from AI Feedbacks) and provides solid evidence for its effectiveness.

### Weaknesses
 * Please provide a comprehensive discussion that covers the related work. For example, some studies have also made efforts in aligning text-to-image models with feedback from MLLMs, such as VisionPrefe r[1], which also discusses the varying effectiveness of different MLLMs as annotators for alignment data in text-to-image tasks.

* It would be beneficial to discuss further the situations in which human judges and MLLM judges disagree, as this could provide valuable insights for future work.

* Besides, to better demonstrate the effectiveness of MJ-BENCH,  the authors are recommended to present some visualization cases of MJ-BENCH to help to offer a clearer and more comprehensive understanding of how well the dataset.

### Questions
Please see in Weaknesses

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
4

### Summary
This paper proposes a benchmark for evaluating LMMs about the judgement capability for T2I generation. The proposed benchmark set contains a few thousands (win, lose, prompt) triplets covering T2I evaluation aspects: alignment, safety, quality, and bias. To show that the proposed benchmark set can provide a fair platform to compare LMMs, this paper uses LMMs as the reward model and use DPO/DDPO to finetune SD1.5. The results show that the model finetuned with a better LMM (evaluated with the proposed benchmark) is preferred by human.

### Strengths
- Evaluating and benchmarking the capability of LMMs is an important research direction of the community nowadays. This paper proposes a comparably comprehensive benchmark set and provides the comparison of a large amount of LMMs, which is valuable to the community.
- I like the design of the benchmark questions based on (win, lose, prompt) triplets, which, in my opinion, can make the human annotation easier compared with direct quality rating.

### Weaknesses
 - In terms of the presentation, I am unsure whether claiming evaluating "reward models" is a better idea than claiming evaluating "LMMs". Close-sourced LMMs such as GPT-4o/4v/Claude are not widely adopted T2I reward models due to their high cost and low throughput. In addition, Table 10 summarizes the number of evaluation questions for each category of the benchmark, which is of the pivotal importance and should be put in the main paper.
- In Table 10, how the number of evaluation questions for each category is determined? I found that most categories, scenarios, and subsets have random numbers of evaluation questions. If so, does this evaluation benchmark introduce bias by itself? For example, the questions for object (250) is more than 4 times of counting questions (55). Since all LMMs are evaluated by the averaged metrics, does the proposed benchmark biased towards LMMs that are better at object questions?
- Table 2 and 3 show the results of SD1.5 finetuned with DPO and DDPO, which, according to my understanding, is the "evaluation" to the proposed benchmark. However, I found that the LMM that work best as the reward (Table 2) is not aligned with the LMM having the highest evaluation scores based on the benchmark (Table 1). Does it mean the proposed benchmark is not good to evaluate T2I reward models? In addition, in Table 3, GPT-4o and GPT-4v achieve the best results with DPO and DDPO, respectively. I think this result suggest that the evaluation of reward model should be performed for certain RLHF methods. I suggest the authors to provide more discussion about this.

### Questions
- I found that very limited details about how to use GPT-4o/4v/Gemini/Claude as the reward model for DPO/DDPO is provided in the paper. Do you use online or offline RL? If online, how to make use of these APIs and obtain the reward for DPO/DDPO fast? What if the API calls fail? If offline, what is the dataset used to finetune the model with DPO/DDPO?

### Soundness
2

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
The paper organizes a new preference dataset called MJ-Bench, which captures four different aspects of text-to-image generation: text-image alignment, safety, image quality, and bias. 

The authors propose two methods to obtain feedback from multi-modal judges: single-input and multi-input judge. The paper also conducts detailed analysis, such as the consistency of the preference of the judges w.r.t different image modes.

### Strengths
1. The paper tackles a crucial issue in evaluating text-to-image models. 
2. The paper includes detailed ablation studies with some insightful findings. For instance,  the analysis of the consistency of the preference of the judges w.r.t different image modes. 
3. The proposed dataset offers many formats (e.g., ranking and voting), which can enable a wider variety of preference modeling.

### Weaknesses
1. The paper's novelty seems limited, as the whole pipeline has been proposed in the previous method. Besides, The selection of these four aspects lacks in-depth analysis.
2. The paper employs human evaluators for experimental evaluation multiple times, yet it fails to report the number of human evaluators involved. Since human evaluators may introduce bias, it is recommended to report this metric. If the number is small, it is advised to increase the scale of human evaluators.
3. The scale of the dataset was not compared with other existing datasets. As a result, the application scope of the dataset may be limited.
4. Since this work is a benchmark study, the quality of the samples within the benchmark was not evaluated. It is recommended to supplement the study with an experiment to assess the quality of the samples in the dataset.
5. The dataset only involved feedback from six judges to train a model (as indicated on page 7). It is suggested to supplement the study with an experiment where feedback is directly constructed from the benchmark data to train a model, in order to observe the outcomes.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
