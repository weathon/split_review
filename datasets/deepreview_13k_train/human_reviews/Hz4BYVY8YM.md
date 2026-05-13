# SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Despite the significant advancements of Large Vision-Language Models (LVLMs) on established benchmarks, there remains a notable gap in suitable evaluation regarding their applicability in the emerging domain of long-context streaming video understanding. Current benchmarks for video understanding typically emphasize isolated single-instance text inputs and fail to evaluate the capacity to sustain temporal reasoning throughout the entire duration of video streams. To address these limitations, we introduce SVBench, a pioneering benchmark with temporal multi-turn question-answering chains specifically designed to thoroughly assess the capabilities of streaming video understanding of current LVLMs. We design a semi-automated annotation pipeline to obtain 49,979 Question-Answer (QA) pairs of 1,353 streaming videos, which includes generating QA chains that represent a series of consecutive multi-turn dialogues over video segments and constructing temporal linkages between successive QA chains. Our experimental results, obtained from 14 models in dialogue and streaming evaluations, reveal that while the closed-source GPT-4o outperforms others, most open-source LVLMs struggle with long-context streaming video understanding. We also construct a StreamingChat model, which significantly outperforms open-source LVLMs on our SVBench and achieves comparable performance on diverse vision-language benchmarks. We expect SVBench to advance the research of streaming video understanding by providing a comprehensive and in-depth analysis of current LVLMs. Our benchmark and model can be accessed at https://anonymous.4open.science/r/SVBench-356F.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SVBench, a benchmark designed to evaluate Large Vision-Language Models (LVLMs) on streaming video understanding. A single data point in SVBench consists of a video segment with its corresponding temporal dialogue chain. Each chain contains 4-5 question-answer pairs that are contextually connected, meaning each subsequent question builds upon previous answers. Additionally, each chain has "temporal linkages" to chains from adjacent video segments based on common elements (people, events, objects). 

The authors employed a semi-automated annotation pipeline where GPT-4 generates QA pairs for each video segment, identifies related QA pairs based on six relationship types, followed by human annotators who modify the result. The evaluation framework uses two modes - dialogue evaluation (testing multi-turn QA within the same video segment) and streaming evaluation (testing understanding across temporally linked segments with an 80% chance of jumping to questions linked with temporal linkages) - while scoring responses across five dimensions using LLMs. 

The authors also introduced StreamingChat, a LVLM built on InternVL2 that uses an InternViT vision encoder, MLP projector, and InternLM2 language model. Regarding the results, GPT-4o leads with the highest scores (66.29% in dialogue and 58.17% in streaming evaluation) while among open-source models, StreamingChat performs best (59.41% in dialogue and 53.90% in streaming), with all models scoring below 60%, indicating significant room for improvement in streaming video comprehension.

### Strengths
- Novel Technical Contribution: The paper introduces a semi-automated pipeline that combines LLM-assisted generation with human verification to create temporal multi-turn QA chains, representing a methodologically sound approach to dataset creation.

- Comprehensive Empirical Validation: The evaluation spans 14 different models (both open and closed-source), uses multiple metrics (METEOR, GPT4-Score, etc.), and includes detailed ablation studies comparing single-instance vs. multi-turn QA performance.

- The temporal linkage: The temporal linkage concept between QA chains is interesting and addresses a real gap in video understanding benchmark by forcing models to maintain context across time segments, mimicking real-world streaming scenarios.

### Weaknesses
The paper's heavy reliance on LLMs for evaluation is a significant methodological concern. While authors use GPT-4 to assess models’ performance across multiple dimensions (semantic accuracy, contextual coherence, etc.), there's no validation of whether these automated scores align with human judgments. The fact that LLMs are being used to both generate the annotations and evaluate the results creates a circular dependency that could mask real limitations or biases in the evaluation process. Without human validation studies, it's difficult to trust the reported performance gains or confidently compare different models using this benchmark.

### Questions
- How reliable are LLMs evaluations? 
- Did you try different LLMs to evaluate the models?
- How did evaluation depend on LLMs hyperparameters like temperature?
- Does it change if run several times?
- How does it change over different prompts?

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
In this paper, the authors introduce SVBench, a novel benchmark designed to evaluate the capabilities of LVLMs in long-context streaming video understanding. SVBench features temporal multi-turn question-answering chains comprising 49,979 QA pairs across 1,353 streaming videos. The study reveals that while the closed-source GPT-4o model outperforms others, most open-source LVLMs struggle with long-context streaming video understanding. 

The authors also develop StreamingChat, a model that outperforms existing open-source LVLMs on SVBench and achieves comparable performance on diverse vision-language benchmarks.

### Strengths
S1: The paper introduces SVBench, a benchmark explicitly designed for evaluating LVLMs in long-context streaming video understanding. I believe this fills a notable gap in existing benchmarks, which typically focus on isolated text inputs rather than sustained temporal reasoning across video streams. The comparison between the benchmarks also shows the advantages of SVBench.

S2: The QA pairs in this work are annotated semi-automatically, making it a large-scale dataset with high-quality annotations.

S3: The experiments and evaluation provide insights into open-source models' struggles with long-context video understanding.

S4: The paper is well-organized, with clear explanations of SVBench, the QA chain structure, and the temporal linkages created for sustained reasoning tasks.

### Weaknesses
W1: The paper does not include a comparison with human performance. Incorporating such a comparison would provide valuable insights into the gap between current models and human capabilities in long-context streaming video understanding.

W2: The paper does not analyze the impact of language model size on performance. Considering that models like InternVL2 have versions with 1B, 2B, 4B, 8B, 26B, 40B, and 72B parameters, and Video-LLaMA2 also have 72B versions, expanding experiments to include these variations and providing more detailed analysis would enhance the work. Additionally, exploring the number of frames the model can process would offer valuable insights. In addition to model size and the input length, analyzing the amount and diversity of training data used for each model would provide a more comprehensive understanding of their performance in long-context streaming video understanding. Training data quality and quantity are crucial factors influencing model capabilities.

W3: The evaluation overlooks several important models capable of long-video understanding, such as LLaVA-OneVision [1], Qwen2-VL [2], LongVILA [3], Long-LLaVA [4], and Oryx [5]. Including these models would enhance the comparison, providing a more comprehensive view of current capabilities in this area.

### Questions
Q1: The videos of the benchmark come from some publicly available datasets; how do you ensure that the models used for evaluation have not encountered this data during their training?

Q2: How do QA chains address the issue of information sparsity in videos? For lengthy videos with few key events, how does SVBench construct meaningful QA chains? Is there a mechanism to handle or generate question chains that effectively deal with scenarios where information is sparse or low-density?

Q3: In your benchmark, do the videos retain their audio tracks? Multimodal information significantly aids in understanding videos. If audio is included, does it genuinely assist in answering the questions?

### Soundness
3

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
To make up for the gap of lacking attention in streaming video understanding, this paper introduces an novel designed SVBench which try to assess how well large multi-modal language models handle temporal multi-turn question-answering dialogues over streaming videos. SVBench includes 49,979 QA pairs derived from 1,353 videos and all
annotations are interconnected through temporal linkages, ensuring that the model needs to consider previous and current video segments to answer questions correctly.
The authors developed StreamingChat, which significantly improved performance by incorporating long-context reasoning abilities specific to streaming videos. They also leveraged advanced training techniques like fine-tuning with LoRA (Low-Rank Adaptation) to handle long video contexts efficiently

### Strengths
1. The SVBench proposed fill the gap between video benchmarks and streaming video understanding. In the real world, streaming video is a more challenging data form, so this benchmark has very important practical significance.
2. The authors proposed a semi-automatic annotation process and integrated multiple types of video data, which not only maintained the diversity of the benchmark, but also the accuracy of the annotation information and prevented hallucinations from affecting the benchmark results.
3. In response to the observed limitations of current large multi-modal langeuage models, the authors introduce StreamingChat, which significantly improves performance on SVBench.
4. The paper conducts an extensive evaluation of 14 models, comparing both open-source and closed-source models,  provides valuable insights into the current state-of-the-art models in handling streaming video understanding.

### Weaknesses
 1. Although the authors provide an intuitive expression of the proposed SVBench in terms of video types and the diversity of annotation information through visualization results, the authors lack a description of the distribution of video lengths, which may be important for a benchmark. Specifically, the absence of detailed statistics regarding the average, median, and range of video durations makes it difficult to assess the benchmark's suitability for different model architectures and computational constraints. Furthermore, the distribution of video lengths could reveal potential biases in the dataset, such as a disproportionate number of short or long videos, which could skew the evaluation results.
 2. The training method of the StreamingChat architecture proposed by the author is similar to the recently proposed streaming video understanding model Video-online. I hope the author can explain the difference between them in more detail. The high-level description of using interleaved multi-image training is not sufficient to distinguish the two approaches. A more detailed comparison of the specific network architectures, training objectives, and loss functions is needed to clarify the novelty of the proposed method. It is also unclear how the proposed method handles temporal dependencies compared to Video-online.
 3. The author's experimens are rich, but lacks measurements of the overall system's latency and inference speed like FPS, which are also very important matrics for streaming video understanding. Without these metrics, it is difficult to assess the practical applicability of the proposed method in real-time scenarios. The evaluation should include a breakdown of the computational cost associated with different components of the system, such as feature extraction, language processing, and temporal reasoning.

### Questions
1. According to the paper, the length of video data used by SVBench is between 5 and 30 seconds. Has the author considered the maximum video processing time of StreamingChat?
2. Can the author provide the test results of the latest streaming video understanding model Flash-VStream and Video-online on SVBench? This will further highlight the advantages of the article.
3. Can the author provide some data on the model's inference speed and resource consumption? For example, the change curve of inference speed and current consumption under different video lengths, which may be what I am more interested in.

### Soundness
3

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
3

### Summary
This paper focus on evaluating LVLMs on streaming video understanding tasks. The authors claimed that existing benchmarks for video understanding merely emphasize isolated single-instance text inputs and fail to evaluate the capacity to sustain temporal reasoning throughout the entire duration of video streams. Therefore, they proposed SVBench, a comprehensive benchmark created from a semi-automated annotation pipeline to obtain QA chains that represent consecutive multi-turn dialogues. The new benchmark is closer to the real-world scenarios and the evaluation results reveal that most open-source LVLMs struggle with long-context streaming video understanding. The authors also developed StreamingChat, a novel model that could significantly outperform open-source LVLMs on SVBench and could be a good starting point to inspire future research.

### Strengths
1. Overall, the motivation is clear and reasonable, i.e., to develop a complete solution (benchmark + model) for streaming video understanding.
2. The paper is well-written and easy-to-follow.
3. The proposed benchmark seems to have good quality, and it's closer to real-world scenarios.

### Weaknesses
I only have minor concerns regarding the quality of the collected annotations and the evaluation metrics.

1. The proposed semi-automated (LLM + human) annotation pipeline is novel and reasonable. However, the authors did not provide sample data to demonstrate the high quality of the benchmark. Although they mentioned in the paper that GPT-4 was utilized to score and rank the QA chain annotations, it still cannot fully convince me that such an LLM-based check can ensure the quality of the benchmark.
2. SVBench leverages METEOR and GPT-4 Score to evaluate model outputs, which either cannot fully reveal the semantic consistency between prediction and ground truths (METEOR) or is costly to call APIs (GPT-4 Score). It would be better to explore the possibility of leveraging open-source language models (e.g., computing distances in semantic space like [1] or prompting open-source LLMs) to perform evaluation.

### Questions
1. Can the authors provide some data samples to demonstrate the significance of the proposed benchmark?
2. Is it possible to utilize open-source models (suggested in the weakness part) to perform evaluation in SVBench? If yes, how do the results align with the existing metrics (METEOR and GPT-4 Score) and human evaluations?

### Soundness
4

### Presentation
3

### Contribution
3
