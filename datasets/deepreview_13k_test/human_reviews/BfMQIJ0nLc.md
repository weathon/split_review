# MMBench: Is Your Multi-modal Model an All-around Player?

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
\label{sec:abstract}
Large vision-language models (VLMs) have recently achieved remarkable progress, 
exhibiting impressive multimodal perception and reasoning abilities. 
However, effectively evaluating these large VLMs remains a major challenge,
hindering future development in this domain.
Traditional benchmarks like VQAv2 or COCO Caption provide quantitative performance measurements but lack fine-grained ability assessment and robust evaluation metrics.
Meanwhile, subjective benchmarks, such as OwlEval, offer comprehensive evaluations of a model's abilities by incorporating human labor, 
which is not scalable and may display significant bias.
In response to these challenges, we propose MMBench, a bilingual benchmark for assessing the multi-modal capabilities of VLMs.
MMBench methodically develops a comprehensive evaluation pipeline, primarily comprised of the following key features:
1. MMBench is meticulously curated with well-designed quality control schemes, surpassing existing similar benchmarks in terms of the number and variety of evaluation questions and abilities;
2. MMBench introduces a rigorous CircularEval strategy and incorporates large language models to convert free-form predictions into pre-defined choices,
which helps to yield accurate evaluation results for models with limited instruction-following capabilities.
3. MMBench incorporates multiple-choice questions in both English and Chinese versions, enabling an apples-to-apples comparison of VLMs' performance under a bilingual context.
To summarize, MMBench is a systematically designed \textbf{objective} benchmark for a \textbf{robust} and \textbf{holistic} evaluation of vision-language models. 
We hope MMBench will assist the research community in better evaluating their models and facilitate future progress in this area.
\footnote{This is a revised version released in April 2024. It describes MMBench v1.1, a refined version of the MMBench (with better data quality). Please refer to \url{https://arxiv.org/pdf/2307.06281v3} for the previous version, which is released in August 2023. }

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to establish a new benchmark, known as MMBench, for evaluating the multi-modal capabilities of VLMs. In comparison to previous benchmarks, MMBench offers a fine-grained assessment of abilities and employs more robust evaluation metrics. This is achieved by incorporating a wider range of evaluation questions. Additionally, MMBench introduces a rigorous CircularEval strategy that ensures models comprehend the questions and provide answers based on understanding rather than guessing. Moreover, MMBench leverages ChatGPT to convert open-form predictions into pre-defined options, mitigating the impact of varying instruction-following capabilities of VLMs. The proposed benchmark evaluates various MLLMs, revealing their capabilities and limitations.

### Strengths
The current MLLMs greatly require a fair and reasonable benchmark to assess the strengths and weaknesses of different methods, making the problem addressed in this paper highly significant. The proposed CircularEVAL strategy effectively enhances the robustness of the evaluations.

### Weaknesses
The authors should provide results for GPT4 to establish the upper bound of performance within the proposed benchmark.

For tasks that perform poorly within the current benchmark, the authors should explain why the models exhibit such poor performance. Is it due to inherent issues with the tasks themselves? Additionally, a comparison with the results of GPT4 can be made to analyze the performance shortcomings of the current open-source MLLMs.

### Questions
No other questions.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes an evaluation-only benchmark, named MMBench, for multimodal (vision-and-language) models. The benchmark contains 3k single-choice questions for images that come from existing datasets or newly collected sources, covering 20 different ability dimensions. To evaluate vision-language models on the benchmark, the paper proposes an evaluation pipeline featuring the CircularEval strategy, which tests the VLM for multiple times and requires consistent correct answers, and chatGPT-involved choice extraction, which extracts single-choice answers for the VLM responses that do not follow the instruction format well. Multiple models are evaluated on the benchmark, where Qwen-VL-Chat shows the best performance.

### Strengths
1. The paper comes with a relatively big (3k) and well-designed benchmark for VLM evaluation, which is an important contribution.
2. Evaluation strategies are designed to test the VLMs that cannot generate single-choice answers. ChatGPT is used in this case, with an analysis compared to human evaluation to show that the introduction of ChatGPT does lead to evaluation bias.
3. The paper is well-written and easy to follow.

### Weaknesses
1. More discussions of the 20 different ability dimensions would be favored. How these dimensions are selected can be discussed further. Moreover, in many cases, multiple abilities are entangled with each other in order to correctly answer a question. For example, “How many apples are there in the image?” as shown in Fig-3 requires both numerical (counting) reasoning and perception (detect apples), which category does this example belong to? 
2. The results are usually “winner takes all”. As shown in the results in Tab-3, more powerful models are usually stronger in every evaluation dimension. It would be interesting to see more fine-grained analysis, e.g. some models are stronger in dimension A, while another is stronger in dimension B, etc.
3. Bias analysis. Shortcut/bias has long been a problem in VQA, where language bias and visual context bias are entangled with each other, leading the models to take shortcuts to answer the questions without real understanding. Does this benchmark suffer from similar problems? Some analysis on how the dataset is balanced, as well as visualizations of the distribution for different concepts and how they co-occur with each other would be helpful.
4. It would be good to have the results for Bard and GPT-4V.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new multiple-choice VQA evaluation benchmark for assessing recent multimodal language large models without subjective human evaluation. The benchmark is set up to evaluate the perception and reasoning abilities of these models, such as attribute prediction, OCR, action recognition, social relation, and so on. It currently consists of 2948 single choice questions covering over 20 abilities. It comprehensively reports the performance of recent 18 models including LLaVA, InstructBLIP, Shikra, and etc.

### Strengths
There are several strengths about this work:
- The vision-language community certainly needs more objective benchmarks for evaluating recent multimodal models.
- The proposed VQA benchmark covers a wide array of abilities (over 20).
- The paper comprehensively tests most recent multimodal models (18 of them).

### Weaknesses
I have several major concerns about dataset collection and evaluation strategies.

> **Dataset Collection and Quality**

As the major contribution of this paper is the new VQA benchmark, I find the paper did a **poor job in explaining how the samples are generated, collected, and verified**. For example, how did you select images from existing sources? How did the annotator come up with QA pairs based on the images? How did you verify the correctness/relevance of these samples? From the current paper it is really hard to gauge the data quality of the benchmark.

After I downloaded the public dev set, I can easily find a lot of VQA samples across categories that can be **solved without looking at the images**. Here are some examples:  

>**Example 1**

Image: a photo of an African elephant. 

Question: The African elephant is the () land animal in the world. 

Options: (A) smallest, (B) largest. 

Category: attribute_recognition.

> **Example 2**

Image: a photo of a snow rabbit. 

Question: Which animal’s skin is also adapted for survival in cold places? 

Options: (A) fantastic leaf-tailed gecko, (B) polar bear. 

Category: physical_property_reasoning.  

> **Example 3**

Image: a photo of the world map centered on Australia.

Question: What direction is Indonesia in Australia?

Options: (A) northwest, (B) northeast, (C) southwest, (D) southeast.

Category: spatial_relationship

Even though I cannot attach images to my review, it is clear that these questions can be answered by a human without looking at the images. This makes MMBench more like a QA instead of a VQA benchmark. The authors should discuss how MMBench is collected and why such problematic samples can leak into your dev set. Did you use crowd-sourced or expert annotators? This is an important question to answer especially if MMBench continues to expand -- how do you plan to ensure the quality of collected samples?

Finally, the paper did not discuss the **licensing for collected Internet images**. I also find some images of MMBench containing **watermarks** from existing website such as zhihu.com.

> **Evaluation Strategy**

I am also concerned with the CircularEval strategy. In section 3.1, the paper says *“CircularEval doesn’t necessarily require N x inference cost”* because if the VLM makes a wrong prediction in one pass, the following passes can be dropped. As such, the paper claims this strategy has *“an affordable cost“* (Section 3). I find this to be a very misleading statement because the computation cost is indeed O(N) and a “perfect” model will still require N passes. 

Could you explain why not doing N passes then report the average accuracy? 

Human performance on MMBench is currently missing. This is important to gauge the overall difficulty of this benchmark.

Finally, answer extraction using LLMs is a standard practice in NLP [1], and thus it is hardly a novel contribution.

> **References**

[1] Large Language Models are Zero-Shot Reasoners. Kojima et al. 2022.

### Questions
In addition to my questions listed above in weakness section, I have one extra question regarding **related work**:

Could you explain why MME has *"a non-rigorous evaluation setting"* that makes it harder to reveal the real performance gap between VLMs? (Appendix A.1)

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new benchmark MMBench for multimodal models. Unlike previous benchmarks suffering from scalable or bias problems, MMBench provides a comprehensive evaluation in an automatic ways. This benchmark reveals several drawbacks of current multimodal models, such as limited instruction-following and logic reasoning capabilities.

### Strengths
This work proposes a comprehensive benchmark and conducts extensive experiments on current multi-modal models. Additionally, this paper shows the bias of model's answer of singlechoice questions and proposes circular evaluation to improve the robustness.

### Weaknesses
The analysis and observations in this study align with prior research. Additionally, MME[1] highlights issues such as not following instructions, lack of reasoning and limited physical relation perception. Personally I encourage the presentation of novel insights regarding the shortcomings of existing MLLMs or suggestions for improvements.

While employing ChatGPT as the choice extractor can eliminate the need for manual ratings, it does introduce reliability concerns. Recent research[2] has revealed successful attacks to GPT by other LLMs, raising safety issues incorporating ChatGPT in evaluations.

[1] https://arxiv.org/pdf/2306.13394.pdf
[2] https://arxiv.org/pdf/2310.08419.pdf

### Questions
I am curious about the efficiency of this benchmark. As it uses CircularEval and incorporates chatGPT in the evaluation process, will it become much slower than other benchmarks?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
