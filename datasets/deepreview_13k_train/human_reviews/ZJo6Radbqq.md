# Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Video understanding is a crucial next step for multimodal large language models (MLLMs).
Various benchmarks are introduced for better evaluating the MLLMs.
Nevertheless, current video benchmarks are still inefficient for evaluating video models during iterative development due to the high cost of constructing datasets and the difficulty in isolating specific skills.
In this paper, we propose \textbf{VideoNIAH} (\textbf{Video} \textbf{N}eedle \textbf{I}n \textbf{A} \textbf{H}aystack), a benchmark construction framework through synthetic video generation. 
VideoNIAH decouples video content from their query-responses by inserting unrelated visual 'needles' into original videos. 
The framework automates the generation of query-response pairs using predefined rules, minimizing manual labor.  The queries focus on specific aspects of video understanding, enabling more skill-specific evaluations. The separation between video content and the queries also allow for increased video variety and evaluations across different lengths.
Utilizing VideoNIAH, we compile a video benchmark, \textbf{VNBench}, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. We conduct a comprehensive evaluation of both proprietary and open-source models, uncovering significant differences in their video understanding capabilities across various tasks. Additionally, we perform an in-depth analysis of the test results and model configurations. Based on these findings, we provide some advice for improving video MLLM training, offering valuable insights to guide future research and model development.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a scalable synthetic framework for benchmarking video MLLMs. It decouples video content from query-response pairs and separates different aspects of video understanding skills. The authors construct a synthetic video benchmark with tasks like retrieval, ordering, and counting to evaluate video models' temporal perception, chronological order, and spatio-temporal coherence. The experiment on VNBench reveals performance gaps and weaknesses in current video models.

### Strengths
1. VideoNIAH offers a novel approach to evaluating video models by decoupling video content and query-response pairs.

2. VNBench provides a scalable and flexible way to evaluate video understanding across different dimensions and video lengths, overcoming some limitations of traditional benchmarks.

3. The paper conducts a thorough evaluation of multiple models, analyzing various factors such as haystack length, needle number, and model settings, providing valuable insights for model improvement.

### Weaknesses
1. While VNBench assesses important aspects of video understanding, it may not cover all possible video-related tasks and scenarios.

2. Despite the relatively low cost of the evaluation method proposed in this paper, it is vulnerable to being gamed by models. Models may develop strategies to perform well on the tasks without truly understanding the video content, thus compromising the reliability of the evaluation.

3. The overall tasks in the proposed evaluation framework are relatively simplistic. After targeted training, models can achieve high scores with relative ease, which may not accurately reflect their ability to handle more complex and diverse real-world video understanding scenarios. This simplicity could lead to an overestimation of the models' capabilities and may not provide a comprehensive assessment of their true understanding and generalization ability in practical applications.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Video Needle-In-a-Haystack (VideoNIAH), a framework for synthetic video generation that utilizes intra-frame and inter-frame edits to create specific modifications within video segments. These modifications, referred to as "needles," are used to assess the capabilities of video MLLMs in handling challenging video content. Additionally, the authors present VNBench, a benchmark compiled from these synthetic videos, which evaluates video MLLMs across three video understanding tasks: retrieval, ordering, and counting. The benchmark is tested on 12 MLLMs, both proprietary and open-source.

### Strengths
- The paper presents a framework to create a synthetic (i.e.: edited video) video that can be automated based on certain predetermined rules and tasks. These edits are posed as “needles” in a “haystack” (the original video segment), and the query for the MLLM is based on the inserted needles. The proposed method is easily scalable given the minimal labeling/definition process that needs to be set manually.
- The curated VNBench benchmark can be used for evaluation of MLLM in video understanding, primarily spatial and temporal understanding. This is presented through tasks of retrieval, counting and ordering based queries from the curated video benchmark.
- The paper evaluates 12 MLLMs on the proposed benchmark with extensive evaluation on the “needle” placements and difficulty.

### Weaknesses
 - The rule-based automation process for dataset curation is unclear. For example, Figure 1(b) lacks clarity in illustrating this process, which is essential to understanding the scalability benefits of this approach, which can be improved.
- While the method is scalable and captures the temporal dependency well, the scope of video understanding through this framework seems limited. For instance, the ability of the model in understanding actions, fine-grained action recognition cannot be ascertained, especially since MLLMs are used in this context extensively.
- Given the nature of the benchmark, the sampling strategy of the video MLLM I believe plays a significant role in its performance. For instance, if any of the frames with a “needle” is not sampled, the model fails to correctly answer that query. Clarification on how this issue is addressed, or suggested solutions, would strengthen the framework’s reliability.
- Can the authors explain if each cell in Figure 8 corresponds to a single test sample? It would be better to enhance this image with a heat map to better understand how the depth of the needle impacts the MLLMs performance. In addition, is there a reason that a depth higher than 10% was not considered?
- Section 6: The mention of the "training recipe" lacks context on what is being trained, creating some confusion. A clearer introduction to this section would aid comprehension.

### Questions
- **Counting E2 Task:** What factors might explain the poor performance of Gemini and GPT-4 on the counting E2 task (Figure 5)?
- **Consistency Check:** Could the authors verify the data in Figure 5 and Table 2? For instance, Video-LLaVa and VideoChat2 seem to perform better than Gemini on the counting E2 task in Figure 5, but Table 2 suggests otherwise.
- **Haystack Length Variation:** In Section 5, where the "Effect of Needle Position" is discussed, the authors mention that the haystack is fixed. Could the authors clarify how the length of the haystack is adjusted in this scenario?

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
This paper proposed a synthetic framework called VideoNIAH to construct the benchmark for evaluating video MLLMs. This framework aims to decouple video content from query-response pairs by corrupting the original videos with "needles" that are irrelevant to the videos.  Based on this frame, a video benchmark named VNBench is further built to evaluate different capabilities of proprietary and open-source video MLLMs, such as temporal perception, chronological ordering, and spatio-temporal coherence.

### Strengths
1. The proposed VideoNIAH is a simple and flexible framework for constructing the video benchmark by avoiding expensive human annotation and leveraging existing video datasets. 
2. The VNBench seems to be the first synthetic video benchmark for evaluating video MLLMs through three skills including retrieval,
ordering and counting. 
3. Comprehensive evaluation experiments are conducted to evaluate close- and open-source MLLMs, further giving some insights for improving the model development and training.

### Weaknesses
1. Although the authors mentioned the proposed framework is inspired by language model evaluation. It is still not very clear about the motivation for proposing such a synthetic framework for video benchmarking and why the proposed one is necessary or important. Specifically, the paper does not adequately articulate the limitations of existing video benchmarks that VideoNIAH aims to overcome, nor does it clearly define the specific evaluation needs that are not currently met. A more detailed discussion of the shortcomings of current methods and how this framework addresses them is needed to establish its significance.
2. The proposed framework mainly adopts subtitles and unrelated images as the "needle", it is better to discuss whether there are other types of "needle" that can be used. The current choice of needles may limit the evaluation to a narrow set of visual and textual distractors. Exploring other modalities, such as audio or short video clips, could provide a more comprehensive assessment of video MLLMs' robustness. The paper should also discuss the potential impact of different types of needles on the benchmark's difficulty and the insights they can provide.
3. A small number of video samples and the types of selected video datasets are used to build the benchmark. In addition, only three tasks are adopted to evaluate the video MLLMs. It is better to make the benchmark more scalable and diverse with comprehensive evaluation capabilities. The limited scale and diversity of the benchmark may not fully capture the complexities of real-world video understanding. Expanding the dataset with more diverse video sources and incorporating a wider range of tasks would enhance the benchmark's ability to evaluate the full spectrum of video MLLM capabilities.

### Questions
1. The paper mentioned the used 'needles' are not related to the original videos. Did you conduct the similarity calculation between each video frame and the candidate "needle" before inserting them? 
2. Inserting the unrelated visual "needle" may not make the benchmark very challenging. Did you try the "needles" that are similar to the original video frame to a certain extent but are from a different category or situation? Maybe it will make the benchmark more challenging.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces VideoNIAH, a novel framework for constructing scalable synthetic benchmarks for evaluating video multimodal large language models (MLLMs).  The core idea is to inject unrelated visual or textual "needles" into existing videos ("haystacks") and then pose questions designed to test specific video understanding skills, such as temporal perception, chronological ordering, and spatio-temporal coherence.  The authors create VNBench, a benchmark based on VideoNIAH, and evaluate 12 proprietary and open-source video MLLMs, revealing significant performance gaps, particularly in long-dependency tasks.  They also conduct a detailed analysis of model performance across various factors like video length, needle number, and position.

### Strengths
1. In VideoNIAH, the decoupling of video content from query-response pairs addresses a limitation of existing real-world video benchmarks, namely the high cost of data creation and the difficulty in isolating specific skills.  The synthetic approach mitigates data leakage concerns. The framework's design allows for easy generation of diverse and large-scale benchmarks, adaptable to various video lengths and complexities.  
2. The authors evaluate a wide range of models (both proprietary and open-source), providing a comprehensive comparison of their performance on different tasks and under varying conditions. The analysis goes beyond simple performance metrics, exploring the impact of various factors (video length, needle number, position, etc.) on model accuracy.  This provides valuable insights into the strengths and weaknesses of current video MLLMs.

### Weaknesses
1. While the synthetic nature is a strength in terms of scalability and avoiding data leakage, it also limits the ecological validity of the benchmark.  Performance on VNBench doesn't guarantee real-world performance. The authors acknowledge this, but a correlation computation between the given benchmark and other real-world ones is needed.
2. The reliance on CLIP for filtering needle images introduces a potential bias.  The performance of the CLIP model itself could influence the results, especially on synthetic videos.  A sensitivity analysis or exploration of alternative filtering methods would be valuable.
3. Minor issues
- Wrong single quotation marks in L18, P1.

### Questions
1. How does the performance on VNBench correlate with performance on established real-world video understanding benchmarks?  Can you provide a comparative analysis?
2. Have you explored the sensitivity of the results to the CLIP similarity threshold used for needle filtering?
3. How robust are the results to variations in the types and complexities of the "needles"?
4. Could the VideoNIAH framework be adapted to evaluate other multimodal tasks beyond video understanding?

### Soundness
2

### Presentation
2

### Contribution
3
