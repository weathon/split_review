# Shot2Story: A New Benchmark for Comprehensive Understanding of Multi-shot Videos

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
A short clip of video may contain progression of multiple events and an interesting story line. A human need to capture both the event in every shot and associate them together to understand the story behind it. In this work, we present a new multi-shot video understanding benchmark \dataset  with detailed shot-level captions and comprehensive video summaries. To facilitate better semantic understanding of videos, we provide captions for both visual signals and human narrations. We design several distinct tasks including single-shot video and narration captioning, multi-shot video summarization, and video retrieval with shot descriptions. Preliminary experiments show some challenges to generate a long and comprehensive video summary. Nevertheless, the generated imperfect summaries can already significantly boost the performance of existing video understanding tasks such as video question-answering, promoting an under-explored setting of video understanding with detailed summaries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Shot2Story, a benchmark aimed at improving multi-shot video understanding through a rich set of annotations, including shot-level captions, detailed video summaries, and question-answer pairs. The benchmark focuses on tasks such as single-shot captioning, multi-shot summarization, and multi-shot question-answering, each designed to leverage both visual and auditory cues in video data. The authors provide a comprehensive dataset of nearly 43,000 videos, annotated with visual and audio information at each shot level, as well as summaries and QA pairs to facilitate high-level semantic understanding of video content.

### Strengths
Shot2Story addresses the limitations of existing benchmarks by providing fine-grained shot-level annotations, narration captions, and comprehensive video summaries. This detailed annotation setup allows for a more nuanced understanding of multi-shot videos.

The dataset's scale and quality are commendable, with 42,958 videos annotated both visually and auditorily. The authors employ advanced techniques, including GPT-4 for generating initial summaries, followed by human verification, ensuring data reliability.

The authors present solid baseline models across tasks, demonstrating the benchmark's challenges and providing insights into areas where current models struggle, particularly in complex video summarization.

### Weaknesses
The reliance on automated generation may introduce inaccuracies or biases, despite human verification. Clarifying any common pitfalls in the generated summaries would strengthen the paper.

The baseline models appear to struggle with integrating visual and auditory information effectively, as noted in the single-shot captioning task. It may be beneficial to explore more advanced audio-visual fusion models as baselines.

A deeper analysis comparing Shot2Story with related benchmarks would contextualize its contributions, especially in terms of unique challenges posed by shot transitions and multi-event progression.

### Questions
The paper mentions that models sometimes produce hallucinated details in the video summaries. Did you explore any methods to mitigate these issues during model training or fine-tuning? Additionally, were there specific patterns observed in these hallucinations (e.g., adding non-existent objects, exaggerating actions)?

The distinction between single-shot captioning and multi-shot summarization is well-explained. However, were there cases where summarizing at the shot level led to information redundancy or fragmentation when compiling multi-shot summaries? If so, what strategies did you use to address this issue?

### Soundness
3

### Presentation
3

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
- This paper presents Shot2Story, a large-scale benchmark for comprehensive multi-shot video understanding. 

- The dataset contains detailed shot-level captions for both visual signals and human narrations, and comprehensive video summaries based on shot-level captions.

- The authors further design a challenging video question-answering benchmark for multi-shot video understanding.

### Strengths
- The paper presents a new multi-shot video understanding benchmark (Shot2Story), with detailed shot-level captions, comprehensive video summaries and question-answering pairs. This will benefit the community, as a benchmark for multi-modal, multi-shot video understanding benchmark.

- The paper has made significant efforts for curating the datasets, to maintain high quality standard, getting the data from 2.1M video clips to 42,958 video clips. The descriptions of the filtering stages are clear and reasonable.

- For baseline establishment, the authors have extensively evaluated a series of open-source models.

### Weaknesses
 - My main concern is on its scientific novelty, as the paper does not include new designs on tackling the multi-shot video evaluation problem, only providing a benchmark, it seems to be more suitable for a benchmark track.

- For baseline evaluation, the focus has been mainly on open-source models, what about models, for example, gpt4v, claude3.5 ?

- In Table 1, \hline is incorrect ?

### Questions
I think the main concern is on its contribution of methodology, as it doesn't involve any architecture/method design for tackling the multi-shot video understanding problem.

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
For multi-shot videos, current video benchmarks tend to annotate captions in a coarse-grained manner, either by providing a holistic caption for the entire video or by allowing annotators to subjectively define the boundaries of each event. But multi-shot videos often include rich narrations that correspond to distinct events occurring within the video. Given this context, this work introduces a new benchmark, *Shot2Story*, aimed at enhancing audio-visual understanding of multi-shot videos through the detailed textual annotation of each individual shot. The authors conduct extensive experiments from three perspectives: single-shot video captioning, multi-shot video summarization, and video question-answering with video summaries. These experiments demonstrate significant limitations in current models’ abilities to understand multi-shot content. Additionally, the authors design two baseline models based on MiniGPT-4 and Video-Chat2. Experimental results reveal that the multi-shot instruction data constructed by the authors substantially improves the performance of multi-shot video understanding.

### Strengths
This paper addressed here underscores a critical issue in current Video LLM work, where shot-level temporal understanding in video instruction data has largely been neglected. Most existing video instruction datasets lack the fine-grained, shot-level annotations necessary to capture nuanced transitions between events within videos.

To address and evaluate this issue, this work introduces a challenging multi-shot video understanding instruction dataset and benchmark. The dataset construction process involves substantial human oversight, which significantly reduces the likelihood of inaccuracies and biases often introduced by external models (e.g., GPT).

In the experiments, the authors analyze and compare several existing Video LLM approaches, highlighting the benchmark’s applicability and challenges. Additionally, they propose two suitalbe baseline models ,which achieve considerable improvements in the understanding of multi-shot video content.

### Weaknesses
The methods compared across the three tasks—video shot captioning, video summarization, and multi-shot video question answering—lack consistency, making it difficult to observe a clear, uniform improvement in performance across these tasks with the proposed dataset. To improve consistency, I suggest that the authors consider using the same set of baseline models across all tasks. 

The constructed multi-shot dataset appears to resemble a series of single-shot descriptions loosely connected by simple transition words, such as "begin with," "then," and "next." The annotation process seems more akin to first splitting multi-shot videos into individual shots, generating isolated descriptions for each, and then using an external tool (e.g., GPT-4) to concatenate these descriptions. This method does not accurately represent the interconnections between shots, which may pose challenges in teaching large language models (LLMs) multi-shot temporal reasoning skills using the constructed instructional data. Although the actual content contained in different shots is inconsistent, there is an obvious time sequence and event relationship between them. I suggest that the authors improve the annotation process by having annotators explicitly describe relationships or continuity between shots, rather than relying on simple transition words. This approach would better capture the temporal flow and coherence between shots, which is essential for developing multi-shot temporal reasoning capability in LLMs.

Moreover, it raises the question of whether multi-shot understanding is at odds with simple video understanding and long-video comprehension. I noticed that the average length of videos in the dataset is only 17.1 seconds, and shots with minimal variation between them were deliberately excluded during construction. Although the videos are relatively short, they contain numerous individual shots with significant differences between them. This could lead models to develop a bias toward segmenting any input video into multiple shots for interpretation, which may pose challenges for understanding both simpler and longer videos. I recommend that the authors conduct additional experiments to evaluate whether models trained on this dataset struggle with simple single-shot videos or longer videos, as this could help clarify any potential biases introduced by the dataset construction.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a new benchmark for understanding multi-shot videos, named Shot2Story. The benchmark provides a dataset of 42,958 short videos, each consisting of an average of 4.4 shots, with detailed textual descriptions, video summaries, and question-answering pairs for multi-modal understanding. It aims to enhance the understanding of videos by providing shot-level captions, human narrations, and generated summaries. Several distinct tasks are defined using this dataset: single-shot video captioning, multi-shot video summarization, and multi-shot video question answering. The paper also presents baseline models and demonstrates the challenges of long, comprehensive video summaries.

### Strengths
1. The paper is well-written, providing clear explanations of the benchmark, tasks, and dataset construction, making complex ideas accessible.
2. Shot2Story sets a new standard for multi-shot video understanding, with detailed shot-level captions, audio narrations, and summaries that advance research in video analysis and multi-modal understanding.
3. The benchmark's unique focus on multi-shot videos with rich shot-level annotations differentiates it from previous benchmarks, contributing to a better understanding of event transitions in multi-shot videos.
4. The authors conduct thorough experiments using baseline models like MiniGPT-4 and VideoChat2, providing valuable insights into current models' strengths and limitations, and establishing a solid foundation for benchmarking future models.

### Weaknesses
1. There is a format issue in Table 1 that affects its readability. Consistent formatting is essential for clarity and for the accurate presentation of comparative data.
2. The motivation for annotating audio text descriptions is not clearly articulated. Understanding audio alongside video is crucial for comprehensive multimedia understanding, especially in tasks involving multi-modal large language models (MLLMs). Merely using textual descriptions without integrating auditory context reduces the potential for deep reasoning capabilities across modalities, which limits the advancement of MLLM applications.
3. The experimental section lacks baselines from well-regarded models such as the Qwen-VL series. Including such comparisons would provide a stronger benchmark and enable a more effective evaluation of the proposed model’s performance.
4. The paper does not propose any self-developed model tailored specifically for the Shot2Story benchmark, which would demonstrate the specific advantages and limitations of the benchmark through a purpose-built approach.

### Questions
1. Is it an optimal approach to use large language models (LLMs) to annotate datasets and then use those annotations for reasoning tasks by the LLMs themselves? This self-referential process might introduce biases or limitations in understanding. Is there a better approach to improving the depth of reasoning and multi-modal alignment, perhaps involving a more collaborative method of training distinct specialized models (e.g., one focused on annotation and another on reasoning)?

### Soundness
3

### Presentation
3

### Contribution
3
