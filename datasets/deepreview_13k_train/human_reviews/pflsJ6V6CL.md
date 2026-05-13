# Listening to Formulas: Pioneering Models and Datasets for Converting Speech to LaTeX Equations

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Recognizing spoken mathematical expressions is a challenging task that involves transcribing speech into a strictly structured symbolic representation while addressing the ambiguity inherent in the pronunciation of equations. Although significant progress has been achieved in both automatic speech recognition (ASR) and language models (LM), the specific problem of translating spoken formulas into LaTeX has received relatively little attention. This task is particularly important in educational and research domains, for example, for lecture transcription. To address this issue, in this paper, we present a pioneering study on Speech-to-LaTeX conversion, introducing a novel, diverse human-uttered dataset in English and Russian comprising 16000 (10000 in English and 6000 in Russian) distinct spoken equations uttered by 3 different speakers. Our approaches, which incorporate ASR post-correction and multi-modal language models, demonstrate a notable performance with up to a 25% character error rate (CER).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The title is a good summary: the authors describe the process of creating an annotated audio-based dataset to help building and evaluating models for automatic conversion of spoken formulas to latex code. The submission adds performance evaluations using different LLM pipelines on this dataset.

### Strengths
The idea and motivation is good. Comparing multiple LLM pipelines and NLU-centric metrics is in general good as well.

### Weaknesses
The biggest weakness of the submission is that it doesn't help to continue research on this topic as the dataset is not made publicly available. The submission explains some details of the process to create it, but given the complexity of that process and the very brief, vague and unclear description of it between lines 283 and 297, I doubt that any researcher can reproduce these results. The brief description does not even allow to reverse engineer which TTS voices and parameters have been used. In addition, the reader is being left in the dark what XTTSv2 means or why only two/one voices have been used despite possibly more being available?

Another weakness is the description of the used evaluation metrics (lines 320-348). A citation to chrF and chrF++ is missing as well as a definition. Furthermore it is unclear wether chrF or chrF++ has been used. A definition of CER is repeated, but a citation would last there as the definition is simple and well known *plus* it has been widely used over the last 3 decades at least. The unbalanced care in defining the different metrics being used is puzzling.

The analysis of results is limited and in my view not formulated well (lines 392-412). SALMONN-13B consistently shines on all metrics and languages except CER, while Qwen2.5-* has a slight edge over SLAMONN-13B wrt CER.

A few text passages lack clarity:
- line 024: the abstract seems shortened and ends with a performance metric (25%) of unknown unit.
- missing targets of in-text references to sections and tables: line 242, lines 422-423, line 479 (I also check the whole supplementary data)

### Questions
I suggest to substantially add clarity, make the dataset publicly available and resubmit as the motivation of the work is good and certainly of interest to a subset of the community.

### Soundness
2

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
4

### Summary
This paper introduces a new Speech to Latex dataset. The dataset comprises spoken equations in English and Russian as well as synthetic data. Various systems (ASR + difference LLMs) are evaluated on the dataset and provide initial benchmarks.

### Strengths
* the tasks is reasonably well motivated (transcribe some part of a lecture to latex)
* several LLM models are tested

### Weaknesses
 * The main issue is in the presentation. The paper appears to still be in draft form (missing references, e.g. 214 and 479, Figure 1 is not referenced; results and discussion section seems to be still be in draft form) and does not provide enough details on the methodology.
* The impact of the dataset is unclear for now given that the baseline models that are benchmarked are simply using ASR as a frontend and the main task becomes converting text to latex formula.

### Questions
No questions but presentation comments:
214: “in the Appendix in Table ??.” missing reference
416-420: this paragraph seems somewhat out of place and may be a better fit for the introduction
422-423: missing references
479: missing reference

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of converting speech to LaTeX. 

It introduces a 3-way dataset containing speech, text, and LaTeX formulas in two languages: English and Russian. 

The study explores various model architectures, including hybrid ASR post-correction and multimodal audio-LLMs, achieving promising results across several metrics (CER, ROUGE-1, sBLEU, and chrF).

### Strengths
1. The paper is well-written and easy to read,  making it straightforward for readers to follow the authors' methods and findings.

2. A good contribution of the paper is the introduction of a new dataset for the speech-to-LaTeX task. This dataset, which includes speech, text, and LaTeX formulas in both English and Russian, is a valuable resource for the field. The authors also provide the introduction of the data collection process. This can be beneficial not only for replicating their work but also for other researchers looking to develop similar resources or expand on this dataset in future studies.

3. The paper includes a good introduction to related work, it provides readers with sufficient background knowledge.

4. The experimental section of the paper is thorough, comparing the performance of various models across multiple evaluation metrics, including CER, ROUGE-1, sBLEU, and chrF. By evaluating different model architectures, such as hybrid ASR post-correction and multimodal audio-LLMs, the authors demonstrate the robustness and effectiveness of their approach as well as making the findings more convincing and reliable.

### Weaknesses
Main weaknesses:
1. Lack of novelty: Apart from the newly introduced dataset, the paper’s contributions are fairly limited. Both hybrid ASR post-correction and audio-LLM adaptation are quite standard and are well-explored areas, and the paper does not present any particularly novel or innovative ideas from a model/pipeline perspective. Additionally, the results align with what might be expected. The use of hybrid ASR post-correction, while effective, does not introduce any new techniques in how ASR outputs are refined for LaTeX generation. Similarly, the adaptation of audio-LLMs, although showing promise, follows a typical fine-tuning approach without significant methodological advancements. The paper does not delve into novel loss functions, architectural modifications, or training strategies that would distinguish it from existing work in these areas.

2. The scope of this paper is somewhat narrow, as the speech-to-LaTeX task is a very specific subtask of Speech Translation. The practical relevance of this task is also unclear, as it’s difficult to find real-world scenarios where people speak only in formulas, even in math classes. A more practical approach might involve developing a model capable of distinguishing between natural speech and mathematical formulas within the same input. So that it can handle both seamlessly. The paper does not address the challenge of integrating formula transcription within a broader context of natural language. This limits the applicability of the proposed approach in real-world scenarios where mathematical expressions are typically embedded within sentences.

Minor weakness:

3. It would be better to include more analysis of the cases that failed to compile. In this paper, it was simply described as "The models reached up to 95-99% compilation success rate."

### Questions
1. Does Qwen-Audio support Russian?

2. There are missing table numbers in the following locations:
 - Line 242
 - Lines 422 and 423
 - Line 479

### Soundness
3

### Presentation
4

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
In this work, the authors focus on the speech to latex (S2L) task, which is not well explored. The first challenge is little relevant data available and authors created datasets in both English and Russian to address this issue. They also explore different modeling methods to tackle with the S2T based on the proposed datasets.  However, there are many information missing or not addressed well.

### Strengths
- A dedicated dataset is created for the S2L task. The dataset is from three sources: 1) GPT-4 generated latex samples based on prompt 2) MathBridge subset after filtering 3) OleehyO/latex-formulas dataset and generated with GPT-4

- Propose several methods to tackle with the S2L task

### Weaknesses
1.  It is great to create dataset for the new tasks. My main concern for the dataset is the coverage or representativeness of the dataset.  
- Part of the data is generated by GPT-4 with prompt. The data is highly dependent on the model and prompts used.  There is no analysis conducted how representative the data is
- Part of the data is based on MathBridge, which is created based on arXiv papers. However, only 15,000 samples are selected from 23 million samples and 3000 of them are used after filtering. The selection rules and filtering methods could introduce bias too. There is no analysis conducted how representative the data is for the arXiv papers.
2. The paper lacks information for model fine-tuning, which is critical to compare different methods.

### Questions
- For the evaluation, do we evaluate the results based on the spoken form as displayed in Table 1? Why not use the written form (latex equation)?
- Do we use the data to fine-tune the acoustic models, such as Whisper, Canary, WavLM and wav2vec2? How about Qwen-Audio, which is built for speech and why it performs worse than other LLM only model?

### Soundness
2

### Presentation
2

### Contribution
2
