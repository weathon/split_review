# StreamingBench: Assessing the Gap for MLLMs to Achieve Streaming Video Understanding

- Decision: Reject
- Scores: 3, 6, 6, 8

## Abstract
The rapid development of Multimodal Large Language Models (MLLMs) has expanded their capabilities from image comprehension to video understanding. However, most of these MLLMs focus primarily on offline video comprehension, necessitating extensive processing of all video frames before any queries can be made. This presents a significant gap compared to the human ability to watch, listen, think, and respond to streaming inputs in real time, highlighting the limitations of current MLLMs. In this paper, we introduce \textbf{StreamingBench}, the first comprehensive benchmark designed to evaluate the streaming video understanding capabilities of MLLMs. 
StreamingBench assesses three core aspects of streaming video understanding: (1)~\textbf{real-time visual understanding}, (2)~\textbf{omni-source understanding}, and (3)~\textbf{contextual understanding}. The benchmark consists of 18 tasks, featuring 900 videos and 4,500 human-curated QA pairs. Each video features five questions presented at different time points to simulate a continuous streaming scenario. We conduct experiments on StreamingBench with 13 open-source and proprietary MLLMs and find that even the most advanced proprietary MLLMs like Gemini 1.5 Pro and GPT-4o perform significantly below human-level streaming video understanding capabilities. We hope our work can facilitate further advancements for MLLMs, empowering them to approach human-level video comprehension and interaction in more realistic scenarios

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a benchmark called StreamingBench to evaluate video LLM capabilities in streaming settings. StreamingBench introduces several tasks tailored to streaming scenarios, including real-time visual understanding, omni-source understanding, and contextual understanding.

### Strengths
- This work introduces a new benchmark designed to evaluate video models in streaming scenarios.
- It conducts insightful experiments, such as "Does Redundant Information Affect Contextual Understanding?", which provide valuable perspectives in this area.

### Weaknesses
 - Although this benchmark focuses on streaming scenarios, a standard video LLM can handle it effectively with simple preprocessing. For instance, whenever a question arises, the model can process all frames up to that timestamp. With this approach, the benchmark may not differ significantly from traditional video benchmarks. Therefore, it is essential for this benchmark to identify scenarios that cannot be simplified to an offline setting.

- While handling redundant information is indeed critical for video LLMs, this challenge is not exclusive to streaming scenarios; it is a general issue for any long-video task. As a result, the insights from this paper may be overshadowed by findings from benchmarks specifically focused on long-video understanding.

- The annotation process lacks clarity. Specifically, how do human annotators manually label QA pairs for omni-source understanding and other contextual understanding tasks? What measures are in place to ensure the quality of each question, and what specific strategies were employed?

- If this paper aims to evaluate the capabilities of streaming models, the tasks it designs should specifically target streaming scenarios and emphasize the distinct advantages of streaming models. However, many of the tasks listed in the paper are not exclusive to streaming models. For instance, tasks like object perception and attribute perception can also be effectively handled by offline models with minimal pre-process. This is also reflected in Table 2 of the paper.

- Moreover, if many of these tasks can be reformulated for offline models to handle, it implies that the capabilities measured by these tasks can already be well-assessed by existing offline benchmarks. This raises the question: why do we need another benchmark to evaluate such tasks? For example, tasks like object recognition and attribute perception are already thoroughly evaluated by existing offline benchmarks, making it unnecessary to introduce a new one for the same purpose.

- That said, I do appreciate the design of the “Proactive Output” task, as it effectively demonstrates the unique strengths of streaming models. Compared to offline models, streaming models indeed excel in real-time reasoning and prediction. However, this task includes only 50 examples, which I believe is insufficient to establish a robust benchmark.

### Questions
As mentioned in the weakness

### Soundness
2

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
5

### Summary
This paper introduces StreamingBench, a benchmark designed to evaluate the capabilities of MLLMs in understanding online streaming videos. Key features of StreamingBench include the ability to pose questions at any point during the video, rather than requiring the full video to be viewed first. The benchmark also considers both visual and audio inputs, and it takes into account the influence of historical interactions in multi-turn dialogues.

### Strengths
- StreamingBench addresses a relatively unexplored area in MLLM research—real-time video understanding. By allowing questions to be asked at any moment and incorporating both audio and visual data, it expands the scope of existing benchmarks.

### Weaknesses
 - The methodology for collecting 900 videos from YouTube lacks sufficient detail.
- Given that the study focuses on a model's capability that is seldom addressed—real-time video understanding—it would be beneficial to create or curate a specific supervised fine-tuning (SFT) dataset. This would allow for an evaluation of model performance post-SFT.
- There is a lack of exploration into the model’s ability to generate proactive outputs. Designing a corresponding SFT dataset to assess whether the model performs better with prior exposure to similar outputs would provide valuable insights.
- Clarification is needed on how open-source models like Qwen2-VL tackle omni-source understanding problems, particularly in the absence of audio inputs. This comparison could shed light on the robustness of the proposed benchmark.

### Questions
See Weaknesses

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
5

### Summary
The paper introduces StreamingBench, a benchmark designed to evaluate the streaming video understanding abilities of Multimodal Large Language Models (MLLMs). Traditional MLLMs are effective in offline video comprehension but struggle with real-time, streaming scenarios that require instant processing, synchronizing visual and audio inputs, and understanding context over time. StreamingBench addresses this by presenting 900 videos across diverse real-world scenarios, structured into 18 tasks and 4,300 human-curated question-answer pairs. These tasks test MLLMs on real-time visual, omni-source, and contextual understanding, aiming to bridge the gap between MLLMs and human-level comprehension in streaming contexts. Testing 13 MLLMs, including state-of-the-art proprietary models, revealed significant limitations in current models, especially in omni-source and contextual tasks, suggesting that MLLMs need further development to match human performance in real-time understanding. In general, it is a solid paper and I would recommend acceptance to it.

### Strengths
1. It is the first valid benchmark on streaming long videos. The questions are designed properly to reflect the information gained in a streaming long video, and highly resembles what human will ask when continuously watching a video.
2. The evaluation and discussion are both very solid.
3. Human performance is another plus.

### Weaknesses
1. The real-time understanding part is nice, but seems a little bit trivial. From all kinds of NIAH evaluations, all models can best answer questions near the ending part of the input, and questions related to "current moments" (which is actually the ending part of input as implemented) might not be so important. Would love to see the understanding on "remembering earlier moments" and the discrepancy from "current moments" for LMMs.

2. The omni-source (visual+audio) part is good. However, how are LMMs without audio abilities evaluated? As these `audio'-related questions seem to be mostly about speeches, do authors plan to interleave text ASR into the model for evaluation? At present, sadly we only see a black-box Gemini-1.5-Pro (for which we do not know how they integrate audio and video) being evaluated with audio.

3. A minor suggestion: the omnisource part of the benchmark is related to "referring reasoning" part of LongVideoBench, an interleaved benchmark for frames and ASR texts, which also needs to judge between concurrent video and audio information in a video. As some other long video benchmarks discussed in Tab 1, please also try to discuss it in the revised paper.

### Questions
Please see the weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new benchmark, StreamingBench, for evaluating MLLMs in streaming video understanding. It assesses three aspects of streaming video understanding: real-time visual understanding, omni-source understanding, and contextual understanding. There are 18 tasks in total. They evaluate 13 open-source Video MLLMs and 3 proprietary MLLMs on this benchmark and analyze the results.

### Strengths
S1: In this paper, the authors propose a benchmark to evaluate the MLLMs' capabilities of streaming video understanding, which is novel and unexplored previously. I believe this will facilitate the advancement of Video MLLMs.

S2: The benchmark considers both video and audio modalities, which have been absent in most previous benchmarks.

S3: The experiments and analysis are comprehensive and detailed, effectively highlighting the limitations of current Video MLLMs in understanding streaming video.

S4: The writing is clear and well-structured.

### Weaknesses
W1: The impact of language model size on performance has not been analyzed. For instance, models like InternVL-V2 come in 1B, 2B, 4B, 8B, 26B, 40B, and 72B parameter versions, while Video-LLaMA2, LLaVA-OneVision, and Qwen2-VL also have 72B versions. Expanding your experiments to include these variations and providing a more detailed analysis would enhance your work. Additionally, exploring the number of frames the model can process would offer valuable insights. It's crucial to understand how performance scales with model size, especially given the computational demands of streaming video. The current analysis lacks a systematic investigation into this aspect, making it difficult to draw conclusions about the optimal model size for different streaming video tasks. Furthermore, the analysis should consider not only the number of parameters but also the architectural differences that might influence performance at different scales.

W2: Several significant models are missing from the evaluation, such as LongVILA [1], Long-LLaVA [2], and Oryx [3]. Including these would provide a more comprehensive comparison. The absence of these models, which are specifically designed for long-context understanding, limits the generalizability of the findings. These models have demonstrated strong performance in other video understanding tasks, and their inclusion would provide a more complete picture of the current state-of-the-art in streaming video MLLMs. Specifically, LongVILA and Long-LLaVA are designed to handle longer video sequences, which is highly relevant to streaming video understanding.

### Questions
Q1: Do you plan to extend your benchmark to support additional streaming video understanding tasks, such as dense streaming video captioning or grounding? Currently, it only supports QA.

Q2: Could you provide more details on how audio is utilized in the MLLMs? I am aware that Video-LLaMA2 supports audio input, but what about the other models?

Q3: Have you considered memory constraints?  I believe this is a crucial factor in streaming video understanding. It would be more consistent and fair to have a fixed memory limit applied across all models, as retaining all input frames throughout a task—particularly in real-world applications—may not be feasible. If some models retain all frames, it could lead to an unfair advantage.

### Soundness
4

### Presentation
4

### Contribution
3
