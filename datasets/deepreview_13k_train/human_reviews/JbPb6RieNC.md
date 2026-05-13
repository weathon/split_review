# Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge

- Decision: Accept
- Scores: 8, 6, 6, 6, 3

## Abstract
Recent advances in Large Language Models (LLMs) have enabled the development of Video-LLMs, advancing multimodal learning by bridging video data with language tasks. However, current video understanding models struggle with processing long video sequences, supporting multi-turn dialogues, and adapting to real-world dynamic scenarios. To address these issues, we propose StreamChat, a training-free framework for streaming video reasoning and conversational interaction. StreamChat leverages a novel hierarchical memory system to efficiently process and compress video features over extended sequences, enabling real-time, multi-turn dialogue. Our framework incorporates a parallel system scheduling strategy that enhances processing speed and reduces latency, ensuring robust performance in real-world applications. Furthermore, we introduce StreamBench, a versatile benchmark that evaluates streaming video understanding across diverse media types and interactive scenarios, including multi-turn interactions and complex reasoning tasks.  Extensive evaluations on StreamBench and other public benchmarks demonstrate that StreamChat significantly outperforms existing state-of-the-art models in terms of accuracy and response times, confirming its effectiveness for streaming video understanding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces StreamChat, a training-free framework for streaming video reasoning and conversational interaction, and StreamBench, a comprehensive benchmark for evaluating streaming video understanding across various media and interactive scenarios. Extensive evaluations on StreamBench and other public benchmarks show that StreamChat significantly outperforms existing state-of-the-art models in accuracy and response times, highlighting its effectiveness for streaming video understanding.

### Strengths
Nice paper. This work is comprehensive, provides significant contributions, and is well-written.

The biggest contribution is StreamBench. Previously, there was no suitable benchmark for streaming video understanding. StreamBench is a high-quality addition.

Furthermore, StreamChat is also very interesting, demonstrating that an agent-like system can also achieve state-of-the-art results in streaming video understanding.

### Weaknesses
Overall, the paper is satisfactory, but I have some concerns regarding StreamChat:

- What motivated the selection of LongVA as a foundation? What are the essential capabilities required for other Video-LLMs to serve as the base model?

- Would fine-tuning LongVA with some streaming vision-language data be better than the current system?

- Is it feasible to integrate the proposed hierarchical memory storage into a trainable framework?

### Questions
Please refer to the part of weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method for online interactions with videos through an LLM, and a benchmark suitable for evaluating streaming-style scenarios where the dialogue happens in real time with the video.

Contributions:
- Video-based LLM which processes high framerate video (typically LLMs need to subsample severely the video due to computational constraints). This method uses optical flow magnitude to assess whether to process any particular frame (w.r.t. previous), therefore saving considerable amount of computation needed. The LLM also has a "short/long" term memory system.
- New benchmark that should be useful since it's one of a kind, simulating multi-round interactions centered on the video content. 25h of content was used in the creation of this benchmarks, making it one of the larger ones available.

### Strengths
Strong empirical results. This is a systems pape which is tied to a particular benchmark which was designed for it, so it's unsurprising that the proposed method works best. With that said, given the engineering effort put into it, it still is impressive, particularly because of the fact that this system could be used in a realtime scenario. 

I am personally excited by the new benchmark that is proposed in this paper perhaps even more so than the method, because it captures a whole class of interactions which were under-represented before.

### Weaknesses
I am kind of baffled by the language of "our method can further improve our foundation model LongVA [20] by 5.1% in accuracy". Does this imply that you're the authors of this method? (Please don't answer this question, but please be mindful of the language which might accidentally de-anonimize you).

The hierarchical design seems a bit ad-hoc. It would have been nice to spend a bit more time to motivate the various design choices. Currently, it sounds like the paper is in the "this is what we did" style, without spending too much into the motivation which led to the various choices made. I could easily imagine many other ways in which the hierarchical memory could have been implemented. For example, the short-term memory could have been implemented as a sliding window over the video features, instead of the proposed mechanism. The long-term memory could have been implemented as a key-value store, with the keys being some sort of summary of the video content, instead of a tree structure. The paper should explore the design space more thoroughly.

The abstract claims "compression" of video features, but reading the paper reveals that this is actually not at all the case. I find the abstract to be misleading and should be updated to reflect the reality of the methods involved. The paper does not actually compress the video features, but rather selects a subset of the frames to process. This is not the same as compression, and the abstract should be updated to reflect this.

Minor comments:
- I am having a hard time reading figures. For example, in Figure 1 I had to use a color picker to figure out which method was which line. In the interest of color blind people, (or partially color blind people like me), please use symbols (*, triangle, diamond, etc) or line styles in addition to colors to make the figures more accessible (either to color-challenged people like me, or when printed out in grayscale).
- There's a typo "Gine-grained" in the appendix.

### Questions
- Do you plan to make this benchmark publicly available?
- Do you plan to open source your method so that others may benefit from the engineering effort you've put into your method? (I am of course talking about academic researchers)
- What the process of identifying the various categories STREAMBENCH encompasses? I am of course talking about the domains and classes of videos. 
- In the appendix, you very briefly mention that you're using a LLM to determine accuracy. The formula you present is unclear. (What's N, T?). What are you getting out of the LLaMA model? Also, do you use any particular prompt for the LLaMA model?
-

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
3

### Summary
This paper presents a benchmark, named StreamBench, and as well a model, named StreamChat, for real-time streaming video LLM answering. The StreamBench comprehensively evaluates assorted capabilities of video LLMs, including spatial search, long & short memory recall, common knowledge reasoning, etc. The size of StreamBench is also larger than previously-proposed benchmarks. The authors also paid a lot of efforts in building the training-free StreamChat model, which bases on current video LLM LongVA and consists of novel techniques including hierarchical memory storage, optimized system scheduling. Evaluations on various benchmarks show that StreamChat enjoys better performance with lower latency compared to previous streaming models.

### Strengths
1. The proposed benchmark, StreamBench, is a comprehensive benchmark testing various capabilities of real-time video LLMs. As far as I know, this is the first benchmark designed for online streaming video task evaluation.
2. The proposed method, StreamChat, integrates frame selection, memory building and retrieval, and several optimizations into a video LLM in a training-free manner. Though designed complicatedly, the latency of StreamChat is still under control (under one second). Several benchmarks, including online StreamBench and offline video understanding tasks, show the effectiveness of the proposed StreamChat. The authors also put a detailed inference example, every components illustrated, in Fig 6. Also, the detailed ablations on threshold and memory parameters should be appreciated.

### Weaknesses
My major concerns comes from two sides:
1. **The presentation**. The presentation of StreamBench is good but the part of StreamChat seems to need to be further improved. It is hard to tell what StreamBench is designed to do when understanding Fig 4 and Fig 5. Though there are both captions and texts written in the method section, it is still hard to relate text descriptions to components in the figures (especially for ones less familar with memory mechanism and RAG).
2. **The complexity**. StreamChat seems too complicated: there are selective frame stacking based on motion vectors, vision-based short-term memory, caption-based long-term memory (also a clustering mechanism in it), dialogue memory (whose language encoder is different from video LLM), and FAISS indexing library. Although being tuning-free, all these components make this 'system' super heavy. The authors should justify every components used in building the memory system in StreamChat. Moreover, this looks more like a RAG system specifically designed for online videos. The authors should compare with other basic RAG methods.

### Questions
See weaknesses. I am just at the borderline due to 1) the contribution of StreamBench and StreamChat, 2) the over-complicated design of StreamChat (being too engineering and RAG-like).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors propose a training-free framework, StreamChat, for streaming video understanding. StreamChat uses a hierarchical memory system to efficiently process long video sequences for real-time, multi-turn dialogue. With parallel scheduling, it improves speed and reduces latency. 

The authors also introduce a new benchmark, StreamBench, which tests video understanding across diverse scenarios, and results show StreamChat outperforms current models in accuracy and response time.

### Strengths
S1: The paper introduces a novel hierarchical memory mechanism that compresses video representations over long sequences, enabling efficient video feature retrieval in real-time multi-turn dialogue contexts.

S2: I believe the introduction of StreamBench as a benchmark for streaming video understanding is a significant contribution that can fill a critical gap in the field. By offering a standardized evaluation framework, StreamBench enables more rigorous comparisons across models, driving advancements in streaming video understanding.

S3: The proposed StreamChat achieves the best performance on StreamBench, surpassing other state-of-the-art methods, which is impressive.

### Weaknesses
W1: StreamChat was compared only with several open-source models. Including proprietary models like GPT-4o and Gemini-1.5 in the StreamBench evaluation would provide a more comprehensive comparison.

W2: Human performance is absent in the comparison, which would help illustrate the gap between current models and human capabilities if included.

W3: The authors compare their new benchmark only with older datasets or benchmarks, such as MSVD, MSRVTT, and ActivityNet. It would strengthen the evaluation to include comparisons with more recent benchmarks for video understanding, such as Seed-Bench [1], Video-Bench [2], MVBench [3], and LVBench [4].

W4: The paper lacks an analysis of factors that impact performance on StreamBench, such as the input frame sequence length or the language model size used by the models.

### Questions
Q1: Will the example in the prompt impact the models' prediction? For example, your example in the prompt is "{'pred': 'A'}". Does it increase the probability of predicting "A"?

Q2: The StreamBench benchmark supports only QA tasks now. Are there any plans to extend it to include additional streaming video understanding tasks, such as dense streaming video captioning or temporal/spatiotemporal grounding?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies streaming video understanding. The authors propose a new benchmark named StreamBench to evaluate streaming video understanding across diverse media types and interactive scenarios, including multi-turn interactions and complex reasoning tasks. They also propose StreamChat, a training-free framework for streaming video reasoning and conversational interaction, with a complex memory mechanism. Their method enhances processing speed and reduces latency, ensuring robust performance in real-world applications. Extensive evaluations on StreamBench and some public benchmarks demonstrate that StreamChat outperforms the selected
baselines.

### Strengths
1. The proposed StreamBench may be the first benchmark for streaming video understanding.
2. The proposed StreamChat outperforms the selected baselines on StreamBench.
3. The processing speed of StreamChat significantly outperforms those of baselines.

### Weaknesses
1. The proposed dataset is too small, only 306 videos and 1.8K  question-answer pairs are collected. The current video benchmark typically has at least thousands of videos and tens of thousands of QA pairs. This version of the benchmark is not ready for release.
2. State-of-the-art video LLMs are not included in the benchmark, such as MiniCPM-V 2.6 [1], InternLM-XComposer2.5 [2], VILA [3], and InternVL2 [4]. The effectiveness of the proposed method is unclear. Furthermore, the choice of LLaMA-3 for evaluation is questionable, as there are more powerful LLMs available, and the alignment of LLaMA-3's judgments with human evaluations is not sufficiently justified.
3. The Selective Frame Stacking seems may ignore small objects in the video and only focus on the global frame feature.
4. The proposed memory mechanism is very complicated and discards a large amount of information in the video. The motivation behind the hierarchical memory design is not clear, and the specific implementation details of how information is stored and retrieved are lacking.
5. The authors test the processing speed of models on two NVIDIA Tesla A800 80GB GPUs, which is not a typical scenario of model development in real-world applications. This experimental setup appears to be specifically tailored to favor the authors' model, making the efficiency comparison with other models potentially unfair.

### Questions
Please respond to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
