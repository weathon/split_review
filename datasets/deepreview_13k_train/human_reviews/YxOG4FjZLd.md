# 🤔Emoji2Idiom: Benchmarking Cryptic Symbol Understanding of Multimodal Large Language Models

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Vision and Language are two major modalities in Artificial Intelligence research.
Bridging the gap between these modalities has long been a key focus in the multimodal community.
Inspired by human cognition, we believe that if a model can see an image and directly associate it with its linguistic meaning, the model possesses high-level intelligence that spans vision and language.
In our work, we focus on emojis in images, a widely-used "cryptic symbol", with a data form of both visual and linguistic features, i.e. emojis have the specific textual semantics while human understand the meaning from their visual information.
Specifically, we first propose the novel task of translating emojis in images to corresponding idioms, thereby challenging Multimodal Large Language Models (MLLMs) to (1) understand the semantic correlation between language and emojis, and (2) reason the intricate linguistic meaning from the emojis in images.
To facilitate the advancement of this task, we construct a high-quality benchmark (emoji2idiom) following the process of automatic model generation and human manual filtering. 
Based on our constructed emoji2idiom, we employ multiple advanced MLLMs to conduct extensive experiments and detailed analyses, demonstrating that existing MLLMs do not yet have enough capability to understand and reason the linguistic information from visual data.
We believe our proposed benchmark and interesting discoveries will encourage the community to attach importance to the intelligence of MLLMs directly associating language from vision, to give MLLMs more comprehensive vision-language understanding ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Emoji2Idiom, a novel benchmark designed to evaluate the ability of Multimodal Large Language Models (MLLMs) to interpret emojis within images and map them to corresponding idioms in English and Chinese. The authors argue that this task necessitates complex reasoning skills across visual and linguistic modalities and highlight the challenges of harmonic mappings, fine-grained emoji understanding, and multi-emoji to one-word mapping. They propose a high-quality dataset comprising emoji-to-idiom mappings and present experimental results with several advanced MLLMs, providing insights into the models' current limitations and potential areas for improvement.

### Strengths
1. The paper introduces a creative and challenging task that requires MLLMs to interpret emojis within images and map them to complex idiomatic expressions. This task highlights a unique aspect of visual-language understanding that goes beyond traditional multimodal benchmarks, pushing models to engage in symbolic and cultural reasoning, which is closely aligned with human cognitive processing.

2. By including both English and Chinese idioms, the benchmark accommodates linguistic diversity and cultural depth, which is often underrepresented in multimodal tasks.  This cross-linguistic approach makes the dataset a valuable resource for exploring the generalization capabilities of MLLMs across different languages and idiomatic expressions, thus broadening its applicability and relevance for global AI applications.

### Weaknesses
1. Limited applicability to real-world scenarios: In practical applications, emojis are often input as text rather than images. The restriction of setting emojis as image input limits the benchmark's applicability to real-world contexts. Testing the performance with emojis as text input would more closely align with actual user behavior, thereby enhancing the benchmark's practical value. Furthermore, the current setup does not account for the variability in how emojis are rendered across different platforms and devices, which could impact the robustness of models trained on this data. A more comprehensive evaluation should include testing with diverse emoji renderings to ensure real-world applicability.

2. Reliance on Harmonic Mapping for Semantics: The task design relies heavily on harmonic mappings, where emojis represent words or idioms based on similar sounds rather than direct meanings (e.g., phonetic similarities in Chinese). This reliance could constrain the model's understanding and may lead to brittle performance if deployed in real-world scenarios where direct meanings and context are more important than phonetic resemblance. This approach might also introduce a bias towards models that are good at phonetic matching rather than true semantic understanding, potentially misrepresenting the model's actual capabilities in real-world scenarios where semantic context is crucial.

### Questions
Is the visual input in the form of a single combined image of emojis, or is each emoji treated as an individual image? 


Edit: I have read the author response and revised my score.

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
5

### Summary
This paper introduces a novel benchmark focused on translating emojis in images into corresponding idioms or phrases using multimodal large language models (MLLMs). The concept is innovative and intriguing, with experiments conducted to evaluate the performance of several MLLMs on this benchmark.

### Strengths
1. The paper presents a new perspective on evaluating MLLMs' understanding capabilities, with a creative and interesting approach.

### Weaknesses
1. The primary data source was the internet, but it seems the authors did not consider potential data leakage during filtering;
2. Some evaluation settings are vague and need further explanation. For example, why is there a difference in templates used across models? Does the metric calculation consider language structure, and if not, why exclude semantics? How are model responses processed?
3. The authors claim that Emoji2Idiom is a fine-grained visual understanding task, but the task design does not reflect this. There is no granular categorization of tasks from a broader perspective; perhaps describing it as an abstract understanding capability would be more appropriate;
4. The range of evaluated models is limited, and neither open-source nor closed-source models specify which versions were used, with open-source models not even providing parameter sizes.

### Questions
1. Many tasks in Emoji2Idiom seem inclined toward a matching task. Did the authors consider testing the performance of CLIP models or using them as a data filtering method?
2. Since emojis have multiple visual representations, how did the authors address this factor? Were there any ablation studies conducted?
3. Did the authors consider annotating the dataset with difficulty, domain, etc., to provide more analytical insights?
4. The authors mention using GPT-4 to review images during data filtering. This might be a typo error; it may be necessary to clarify which specific model was used (GPT-4V, GPT-4o, or ChatGPT web).

### Soundness
1

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
3

### Summary
This paper introduces Emoji2Idiom, a benchmark for evaluating multimodal large language models' ability to translate emoji sequences into meaningful text (Chinese idioms, English words, and English idioms). 

 The benchmark challenges models in three key aspects: harmonized word reasoning, fine-grained visual understanding, and complex mapping relationships. Through extensive evaluation of commercial and open-source MLLMs, the authors demonstrate current limitations in models' ability to bridge visual and linguistic understanding. The work's main contributions are proposing a novel emoji-to-text translation task and providing insights for improving MLLMs' symbolic understanding capabilities.

### Strengths
Using emoji-to-text translation as a proxy for testing abstract symbolic understanding is both original and insightful, especially given emojis' unique position as symbols with both visual and linguistic meaning. 

The work meaningfully addresses a gap in current MLLM evaluation benchmarks - while most focus on natural image understanding, this paper tackles the understudied area of abstract symbol comprehension, providing a reusable benchmark and practical insights for improving model performance.

### Weaknesses
The paper's primary weakness lies in its artificial data construction approach. The extensive use of homophonic relationships to create emoji sequences, feels contrived and deviates significantly from how emojis are naturally used in real-world communication. In reality, people use emojis to express emotions, enhance communication efficiency, or circumvent content restrictions - not to create puzzles through sound-alike words. This artificial construction, especially in the text-to-emoji generated portion of the dataset, makes many examples challenging even for humans to understand and raises questions about the benchmark's real-world applicability. A more meaningful evaluation would focus on how MLLMs understand emoji usage in authentic social media contexts, where emoji sequences naturally emerge from genuine communication needs rather than being reverse-engineered from predetermined phrases.

### Questions
Is there overlap between the human experts in data construction and the human experts in model evaluation?

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
The paper presents the Emoji2Idiom benchmark aimed at evaluating the cryptic symbol understanding capabilities of Multimodal Large Language Models (MLLMs). It introduces a novel task where MLLMs must translate emojis in images to corresponding idioms, challenging models to understand semantic correlations and reason linguistic meanings from visual data. The authors construct a high-quality benchmark with tasks spanning language, text format, and semantic diversity. Experiments with advanced MLLMs demonstrate current models' limitations in understanding visual data's linguistic information, suggesting areas for future research.

### Strengths
* The paper introduces a unique benchmark task that bridges vision and language modalities, providing a new perspective on MLLM evaluation.
* The proposed Emoji2Idiom benchmark covers diverse language tasks, enhancing the generality of the evaluation.
* The whole work is complete, with detailed annotations and filtering, and diverse evaluation settings such as zero-shot, few-shot, COT, and human evaluation.

### Weaknesses
 * Why is it necessary for emoji as image task compared to emoji as text task? There needs a more in-depth discussion about the relationship between emoji as image task and high-level vision-language understanding.
* For some emojis in Emoji2Idiom benchmark, there may not be a standard answer (the same emoji can mean different things and emotions in different situations, where everyone has their own perspective). How do the authors ensure that the ground truth answer is unique? 
* The authors need to provide more latest MLLMs to support experimental conclusions, such as Claude-3.5-Sonnet,  LLaVA-1.6, Qwen2-VL, and InternVL2.
* Table 3 has a format error about "Deepseek-VL".

### Questions
* Have the authors considered designing multiple-choice questions where the model selects the correct answer from given options rather than generating the answer? It is worth exploring whether there is a significant gap compared to the generation task.
* The paper could improve by including tests on model performance after fine-tuning with data highly relevant to the task of emoji understanding. This would provide a clearer picture of how adaptable and improvable the models are with targeted training.
* The dataset's reliance on manual annotation makes it difficult to expand, which could limit its long-term applicability as models improve.

I look forward to an active discussion with the authors during the rebuttal phase and will revise my score accordingly.

### Soundness
3

### Presentation
3

### Contribution
2
