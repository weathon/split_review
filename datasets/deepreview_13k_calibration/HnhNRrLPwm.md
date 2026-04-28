# MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
Interleaved multimodal comprehension and generation, enabling models to produce and interpret both images and text in arbitrary sequences, have become a pivotal area in multimodal learning. Despite significant advancements, the evaluation of this capability remains insufficient. Existing benchmarks suffer from limitations in data scale, scope, and evaluation depth, while current evaluation metrics are often costly or biased, lacking in reliability for practical applications. To address these challenges, we introduce \ours, a large-scale knowledge-intensive benchmark for evaluating interleaved multimodal comprehension and generation in Large Vision-Language Models (LVLMs). \ours\ comprises 20K meticulously curated multimodal queries, spanning 3 categories, 12 fields, and 102 subfields, including mathematics, coding, physics, literature, health, and arts. It supports both interleaved inputs and outputs, offering a mix of multiple-choice and open-ended question formats to evaluate diverse competencies. Moreover, we propose a reliable automated evaluation metric, leveraging a scoring model fine-tuned with human-annotated data and systematic evaluation criteria, aimed at reducing bias and improving evaluation accuracy. Extensive experiments demonstrate the effectiveness of our benchmark and metrics in providing a comprehensive evaluation of interleaved LVLMs. Specifically, we evaluate eight LVLMs, revealing that even the best models show significant room for improvement, with most achieving only moderate results. We believe \ours\ will drive further advancements in the development of interleaved LVLMs. We publicly release our benchmark and code in \href{https://mmie-bench.io/}{https://mmie-bench.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents MMIE: a benchmark for evaluating interleaved multimodal comprehension and generation abilities of Multimodal LLMs. The evaluation dataset is also publicly released. Further, they propose an automated evaluation metric, using a finetuned LLM. They evaluate various interleaved and “integrated” (text-generation followed to text-to-image generation) LLMs on their proposed benchmark.

### Strengths
The MMIE benchmark presented in the paper offers a significant contribution in the interleaved comprehension and generation domain. The benchmark is of significant scale (~20k examples) and well categorised, specifically the project-based learning, situational analysis and multi-step reasoning categories. They also describe in good detail the process of the benchmark creation. 

Another significant strength is the automated evaluation metric based on a finetuned LLM. With open-ended evals for interleaved generation, the challenge lies in capturing the various facets including image-text alignment, image quality and text quality. Their proposed method captures these, making it a strong contribution.

The experiment section of the paper is quite detailed. Especially the creation of the integrated LLMs where they combine state-of-the-art LLMs with text-to-image generation models. Sec 5 “Error Analysis” where they identify the typical types of errors offers a great analysis of failure cases.

The MMIE benchmark along with the finetuned model for evaluation is publicly released.

### Weaknesses
While the proposed automated evaluation metric using a finetuned LLM is novel and promising, details on the construction of the dataset used for finetuning are missing in the paper.  

The claim L110 “The proposed scoring model ... has proven to be comparable to human evaluation.” is not well justified in its current form. For instance, while Table 5 shows that their proposed method has better similarity with human scoring, further details on how the human annotations were obtained are missing.

### Questions
1. The effectiveness of the proposed evaluation metric is a function of the evaluation model. Please provide further details on the finetuning method and dataset utilised for the evaluation model.
2. To better understand the role that the evaluation model plays in the pipeline, please provide qualitative examples of eval model responses corresponding to Fig 7,9,10,11,12 in the appendix.
3. Please provide details on how the human annotations were obtained for Table 5 to better support the claim in L110.

Edit: I have read the author response and revised my score.

### Soundness
3

### Presentation
3

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
The paper introduces MMIE (Massive Multimodal Interleaved Evaluation), a large-scale benchmark designed to evaluate interleaved multimodal comprehension and generation in Large Vision-Language Models (LVLMs). MMIE comprises 20K multimodal queries across 12 fields, including math, coding, physics, literature, health, and arts. The benchmark supports both interleaved text and image inputs and outputs, including image generation, offering a mix of multiple-choice and open-ended question formats. As evaluation metric, the authors propose an finetuned (multimodal) LLM as a scoring model. This metric aims to reduce bias and improve evaluation accuracy over existing LLMs as-a-judges. The results reveal that current LLMs have significant room for improvement when evaluated on MMIE.

### Strengths
* Originality: The paper introduces a novel and comprehensive benchmark for evaluating interleaved multimodal comprehension and generation, addressing an underexplored but increasingly important area.
* Quality: The benchmark is large-scale and diverse, covering a wide range of domains and task formats, which enhances its utility and applicability. The methodology for dataset curation and quality control is rigorous.
* Automated Evaluation Metric: The proposed scoring model provides a more reliable and unbiased evaluation compared to using a "raw" GPT model, strengthening the analysis beyond traditional metrics.
* Human Scoring Comparison: Comparison of different scoring model against human annotations is great in highlighting the strength.

### Weaknesses
 * Potential Biases in Scoring Model: The reliance on a LLM as a scoring model may introduce biases inherent in the base model. A more thorough analysis of these potential biases, and how they might affect evaluation outcomes across different domains or tasks, might be needed. Specifically, the paper should investigate whether the scoring model exhibits a preference for certain types of responses or formats, which could skew the results. For example, does the scoring model favor responses that are more verbose or those that use a particular writing style? Furthermore, the impact of the training data used for the scoring model should be examined, as this could introduce biases that are not immediately apparent. The paper should also consider the potential for the scoring model to be sensitive to minor variations in the responses, which may not reflect actual differences in quality.
* Content Warning Handling: The paper includes a content warning but does not elaborate on it, as Ethical Statement highlight strict guidelines and lack of bias in the dataset. The lack of detail regarding the specific types of content that triggered the warning raises concerns about the transparency of the dataset creation process. It is important to understand the nature of the potentially sensitive content and the measures taken to mitigate any associated risks. The paper should provide a more detailed explanation of the content warning, including examples of the types of content that were flagged and the specific steps taken to ensure the dataset is ethically sound.

### Questions
* Dataset Size: The 20K sample benchmark is substantial and statistically robust, enabling a comprehensive evaluation. However, validating the full dataset with 20K samples may be costly. Have the authors considered designating a "mini" subset for consistent yet quicker evaluation? For example, using 800 samples selected for scoring model training.
* Visual Component Importance: Is it feasible to analyze the impact of visual content within the benchmark? For instance, comparing text-only generation with generation that includes images. Some examples in Figure 1 do not rely on image content but rather use images solely for illustrative purposes.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces MMIE, a large-scale benchmark designed to evaluate interleaved multimodal comprehension and generation capabilities of Large Vision-Language Models (LVLMs). MMIE comprises 20K multimodal queries across 12 fields, supporting interleaved text and multi-image inputs and outputs in both multiple-choice and open-ended formats. It provides a comprehensive framework to assess LVLMs on complex, real-world tasks that demand high multimodal reasoning and synthesis skills.

### Strengths
1. MMIE provides a robust evaluation framework for Large Vision-Language Models (LVLMs) by supporting cross-modal, interleaved input and output of both text and multiple images. This flexibility in handling multi-image inputs and outputs, along with the inclusion of multiple-choice and open-ended question formats, broadens the range and depth of tasks LVLMs are tested on. Furthermore, the large data scale and comprehensive scope of MMIE allow it to evaluate LVLMs in a way that captures the complexities of real-world multimodal interactions, offering a thorough assessment of these models’ interleaved multimodal comprehension and generation capabilities.

2. MMIE introduces an automated scoring model fine-tuned with human-annotated data, developed using detailed evaluation criteria. This approach addresses the challenge of bias often seen in traditional metrics, enhancing the objectivity and precision of multimodal model evaluation.

### Weaknesses
1. Lack of fine-grained presentation of results across fields: Although the paper evaluates several models, it does not fully present results across different fields, making it challenging to analyze performance gaps in specific domains. This limitation may restrict insights into targeted improvements for specific models in particular fields.

2. Potential Overfitting to Specific Benchmark Tasks: Since the scoring model in MMIE is fine-tuned on data specific to the benchmark, it may overfit to the types of tasks and response styles within MMIE.   This could limit its generalizability to other multimodal datasets or tasks, potentially reducing its effectiveness when evaluated in new contexts outside of MMIE’s scope.

### Questions
Given that the scoring model is trained on data similar to MMIE (12 domains), I am curious about its generalizability to other benchmarks. Does the scoring model work on other benchmark data, such as MMLU, which includes 30 domains? This would provide insight into whether the model’s evaluation criteria are adaptable to a broader range of multimodal tasks.


Edit: I have read the author response and revised my review.

### Soundness
3

### Presentation
3

### Contribution
2
