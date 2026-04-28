# OmniBench: Towards The Future of  Universal Omni-Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 8, 3, 6

## Abstract
Recent advancements in multimodal large language models (MLLMs) have aimed to integrate and interpret data across diverse modalities. However, the capacity of these models to concurrently process and reason about multiple modalities remains underexplored, partly due to the lack of comprehensive modality-wise benchmarks.  
We introduce \textbf{OmniBench}, a novel benchmark designed to rigorously evaluate models' ability to recognize, interpret, and reason across \textbf{visual}, \textbf{acoustic}, and \textbf{textual} inputs simultaneously. We define language models capable of such tri-modal processing as the omni-language models (OLMs).
OmniBench is distinguished by high-quality human annotations, ensuring that accurate responses require integrated understanding and reasoning across all three modalities. Our main findings reveal that: 
\emph{i)} open-source OLMs exhibit critical limitations in instruction-following and reasoning capabilities within tri-modal contexts; and \emph{ii)} most baselines models perform poorly (below 50\% accuracy) even when provided with alternative textual representations of images or/and audio.
These results suggest that the ability to construct a consistent context from text, image, and audio is often overlooked in existing MLLM training paradigms. 
To address this gap, we curate an instruction tuning dataset of 84.5K training samples, \textbf{OmniInstruct}, for training OLMs to adapt to multimodal contexts.
We advocate for future research to focus on developing more robust tri-modal integration techniques and training strategies to enhance OLM performance across diverse scenarios.
Codes, data and live leaderboard could be found at \href{https://m-a-p.ai/OmniBench}{the project page}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents OmniBench, a multi-modal benchmark developed to evaluate the capacity of large multimodal language models (MLLMs) to process and reason across visual, auditory, and textual modalities. In this framework, the authors classify these systems as `omni`-language models (OLMs) and set a unique requirement for accurate responses that reflect an integrated understanding across all three data types.

Additionally, the paper introduces OmniInstruct, an instruction-tuning dataset containing 84.5K multimodal samples, specifically designed to strengthen OLMs' tri-modal reasoning abilities. Experimental findings indicate limitations in existing open-source LLMs, which demonstrate notable challenges with tri-modal integration, especially in complex reasoning tasks.

The study highlights an ongoing need for advancements in model architectures and training methods to address these limitations effectively. Personally, I find the paper’s focus on addressing the tri-modal gap quite compelling, as it addresses an increasingly relevant challenge in multimodal AI research. 

- The insights from this benchmark could indeed motivate the development of more robust models capable of cohesive multimodal understanding, though it’s clear the field has substantial work ahead.

### Strengths
1. OmniInstruct is a valuable resource, contributing not only to benchmarking but also to supervised fine-tuning efforts to improve multimodal reasoning.

2. The multi-stage annotation protocol ensures the data integrity of OmniBench, with stringent criteria enforced by both human and machine inspections. This includes a requirement for all tasks to depend on information from all three modalities.

### Weaknesses
1. While OmniBench has potential in research contexts, the immediate applicability of such stringent multi-modal dependency requirements in industrial applications, such as autonomous systems or assistive technologies, is less clear. This could impact the dataset’s adoption.

2. Although the paper provides extensive evaluations, most open-source baselines underperform significantly (under 50% accuracy). This limits the immediate insights on how more advanced architectures might interact with the benchmark.

3. The design focuses on strict dependency on three modalities, which, while rigorous, may not align with more flexible, real-world tasks where certain modalities may contribute only supplementary information. i.e, the attention of each modality during human understanding.

4. While the benchmark focuses on the three primary modalities (visual, audio, text), the term "omni-language" could extend to other modalities. How feasible would it be to adapt OmniBench for future modalities like haptics or environmental sensors, in short, time series?

### Questions
1. The paper’s inclusion of textual approximations for images and audio is intriguing. Could the authors further discuss the impact of substituting text on model generalization? How do they plan to mitigate the potential information loss in future tri-modal datasets?

2. The paper notes that model scaling impacts performance, particularly on certain task types. Would the authors consider expanding the benchmark or the OmniInstruct dataset with larger, more complex task sets to investigate scaling effects systematically?

3. Given the benchmark's high reliance on human annotations across multiple modalities, is there any plan for further bias analysis, particularly regarding the cultural context of audio and visual content?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a new benchmark to evaluate omni-language models, i.e LLM accepting multiple modalities. In the context of this work, the authors restricts those modalities to three: text, vision and audio. Questions asked in the OmniBench are human-curated multiple-choices questions (MCQ) that require to understand/reason across all the modalities simultaneously, totaling 1142 test questions across multiple categories (causal inference, temporal/spatial identity, abstract concept). Along OmniBench, authors introduce OmniInstruct; a dataset for omni-language instruction-following fine-tuning, totaling 97k data samples. OmniBench annotation protocol, and OmniInstruct building are described.

### Strengths
- Authors make clear that common benchmarks generally focus on single or dual-modality. This highlight the need to have 'omni' benchmarks as proposed by this work. 
- The state of the art of multimodal benchmarks is extensive and well documented, making clear the approaches in use in the literature. 
- The paper is really well written, with clear figures and statements. The biggest weakness is to me the lack of clarity about the sources and license of OmniBench.

### Weaknesses
 - The source of OmniBench is not clearly stated. Or did I miss it? I went over the papers a couple times, and I couldn't find a clear statement about the source and the license of the benchmark. A manual inspection of the examples seems to show film clips, but nothing seems to be clearly stated anywhere in the text. 
- Related to the above point, if indeed sources are film clips, one could potentially see biases in that dataset. I would expect a strong multimodal image-text LLM to be able to answer some of those questions just by recognizing the clips. Figure 1 shows for instance a famous scene of the TV show Friends. This scene is extensively mentioned on the Internet across many fan websites.
- The OmniBench is not a free-form answer benchmark, but a MCQ, hence potentially overestimating the reasoning/understanding capabilities of the model evaluated. With 4 choices, there is always the possibility that the model being evaluated picks randomly 25% of the time the right answer. Having a one confusing wrong option as proposed in this work is a decent mitigation, but that doesn't remove that design flaw completely.

### Questions
- What are the sources used for OmniBench? Can you specify them in the paper? Related to this question, what is the license associated with those source? If OmniBench becomes a standard in the community, having a CC-NC might be a deal breaker for many users.
- Why using InternVL-2-76B for OmniInstruct but Llava-1.6-34B for the quality control of OmniBench? Can you explain that choice in the paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a multiple choice question answering (QA) benchmark, OmniBench, for multimodal LLMs that simultaneously take image, audio, and text input. It uses a human annotation pipeline to construct 1142 questions that are verified to require all input modalities to answer (instead of being answerable by just one). The paper also proposes OmniInstruct, an instruction tuning QA dataset that is constructed by merging 3 existing multimodal QA datasets (MSRVTT-QA, AVQA, and Music-AVQA2.0) and then filtering out the questions that can be answered by only the visual or only the audio modalities. Finally, the paper benchmarks a large number of existing multimodal LLMs on OmniBench, finding that most of them perform marginally above chance accuracy on the benchmark.

### Strengths
The paper poses a well-motivated benchmark, ensuring that questions must be answerable by leveraging all modalities together. This ensures that the results on the benchmark reflect a model's ability to jointly reason over all of its inputs.

### Weaknesses
- The proposed OmniBench evaluation set is quite small at barely over 1100 questions. Because these questions are broken down across audio type (speech, sound event, music) and within each of these span a large number of categories ("Object Identification", "Plot Inference", "Count and Quantity"), the number of questions belonging to each category is even smaller. According to the statistics in Table 1, only 15 total questions deal with "Count and Quantity", only 28 deal with "Object Identification and Description" for the "sound event" category, and so forth. I am skeptical that 15 "Count and Quantity" questions is sufficient to produce statistically significant differences between models when attempting to assess their ability to count (this concern is not limited only the "Count and Quantity" questions, I'm just using it as an example). I think OmniBench is simply too small to serve as a useful benchmark; at this scale the experimental comparisons between models on the benchmark really need to have statistical significance testing done, but none was presented in the paper.

- The OmniInstruct dataset, as far as I can tell, was not used in any of the experiments. Therefore, it's not clear why it is included in the paper at all.

- I have doubts about the quality of the dataset. There are barely any example questions provided (the appendix would have been a great place to include these), and the categories are never defined so it's very unclear to me e.g. what a "Plot Inference" question regarding the "Music" or "Sound Event" modality even would entail. What's worse, the only example OmniBench question provided in the main body of the paper (in Figure 3) doesn't make any sense. The question asks "What is this black box" and the answer is "a red pill" but no black box is visible in the image or mentioned in the content of the audio.

- Also related to the OmniBench quality, no human performance on the dataset is given. I understand the questions were crafted by human annotators, but to know whether these questions are actually answerable by humans (especially in light of the confusing example given in Figure 3, which I certainly wouldn't have been able to answer correctly) they should have been presented to an independent set of annotators.

### Questions
- Can you show that there are statistically significant differences between the performances of the models evaluated on the benchmark?

- Can you prove that the OmniBench questions are indeed answerable by humans?

- What is the purpose of OmniInstruct, and can you show that using it improves performance on OmniBench?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Inspired by the recent multimodal large language models (MLLMs) benchmarks, this paper proposes OmniBench, which can cover three modality (visual, acoustic and textual). By examining the existing Omni language models (OLMs), this paper reveals that the existing open-source OLMs show limited instruction following and reasoning capabilities on the proposed OmniBench. Furthermore, this paper introduces an 84.5k training corpus, OmniInstruct for training OLMs.

### Strengths
1. This paper leverages the existing resources to curate an OmniBench, which can cover three modalities, to evaluate the MLLMs or OLMs.

2. This paper also introduces an 84.5k training corpus for the research community.

### Weaknesses
1. This paper is more like an empirical analysis for the existing MLLMs or OLMs on the proposed OmniBench. It proposed an 84.5k training corpus for OLMs, which is to improve the model capability of tri-modal reasoning, but did not verify the quality and effectiveness of the proposed corpus. It looks an missing piece, which may not convince people the usefulness of the corpus, whether this training corpus can actually help to improve the models' capability from the findings from the OmniBench results.

2. This paper lacks a detailed description of the evaluation protocols and metrics used for the proposed OmniBench. The absence of this information makes it difficult to assess the validity and reliability of the experimental results. Specifically, it is unclear how the multiple-choice questions are structured, how the models' responses are evaluated, and what statistical measures are used to compare the performance of different models. Without these details, it is hard to interpret the significance of the reported results.

3. The evaluation in Section 5 only covers Image and Audio modalities, with no specific evaluation for Text. While the authors acknowledge the existence of many benchmarks for LLMs, it is still crucial to evaluate the OLMs' capability on text-specific tasks within the context of the proposed OmniBench. The omission of text-based evaluation raises concerns about the comprehensiveness of the benchmark and its ability to fully assess the tri-modal reasoning capabilities of the models.

### Questions
1. It may miss a section/paragraph to illustrate the evaluation protocols and metrics of the proposed OmniBench.

2. As discussed above, it looks the model training part is a missing piece, to verify the introduced OmniInstruct is useful and effective. 

3. One feeling after reading the paper is - the paper proposed OmniBench to cover three modalities (visual, audio, and text), while, the evaluation in Section 5 only covers Image and Audio, no Text specific evaluation. (though we know there is a lot of benchmarks for LLMs.). Do you think whether it is necessary to evaluate their (OLMs) capability on Text?

### Soundness
3

### Presentation
3

### Contribution
3
