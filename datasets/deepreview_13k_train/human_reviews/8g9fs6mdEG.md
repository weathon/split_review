# Streaming Video Question-Answering with In-context Video KV-Cache Retrieval

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We propose ReKV, a novel, training-free approach that integrates seamlessly with existing Video Large Language Models (Video-LLMs) to enable efficient streaming video question-answering (StreamingVQA). Traditional VideoQA systems struggle with long videos, as they must process the entire video before responding to queries, and repeat this process for each new question. In contrast, our approach analyzes long videos in a streaming fashion, allowing for prompt responses as soon as user queries are received. Building on a common Video-LLM, we first incorporate a sliding-window attention mechanism, ensuring that input frames attend to a limited number of preceding frames, thereby reducing computational overhead. To prevent information loss, we store processed video key-value caches (KV-Caches) in RAM and disk, reloading them into GPU memory as needed. Additionally, we introduce a retrieval method that leverages an external retriever or the parameters within Video-LLMs to retrieve only query-relevant KV-Caches, ensuring both efficiency and accuracy in question answering. ReKV enables the separation of video analyzing and question-answering across different processes and GPUs, significantly enhancing the efficiency of StreamingVQA. Through comprehensive experimentation, we validate the efficacy and practicality of our approach, which significantly boosts efficiency and enhances applicability over existing VideoQA models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents video KV caches to make a streaming video question and answering video-LLMs in a training-free approach.
While it uses a sliding-attention mechanism to aggregate short-term temporal context, video KV caches and the proposed retrieval method are introduced to long-term temporal context.
This method shows efficiency with LLaVA-OV in several benchmarks.

### Strengths
- This paper outperforms existing video-LLMs on long-form benchmarks.
- This paper is easy to follow.
- Ablation study shows the validity and impact of the retrieval methods.

### Weaknesses
 - My major concern is the novelty. Already, many LLM systems reduce the context-processing delay by using the KV cache of the context. This paper is also built on LLMs, while it is coupled with a video encoder. It's hard to find the specialty for the video streaming system. The causal attention and retrieval system with cosine similarity are also not new.

- Implementation with only one design (LLaVA-OV) with different sizes is limited to prove the generality of the proposed method.

- There are many recent methods to reduce the memory of KV caches such as adaptive KV cache (ICLR'24) and Keyformer (Muhammad Adnan et al., arxiv'24), compared to these methods, is the proposed attention and search method more effective?

### Questions
- How about GFLOPs on streaming VQA?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ReKV, a novel, training-free approach designed to enhance existing Video-LLMs for StreamingVQA. Traditional VideoQA systems struggle with long videos due to the need to process entire videos before responding and repeating this process for each new question. ReKV addresses these challenges by storing processed video key-value caches (KV-Caches) in RAM or disk to prevent information loss. ReKV introduces retrieval methods—both external (using models like CLIP) and internal (leveraging the Video-LLM's parameters)—to fetch only query-relevant KV-Caches, enhancing efficiency and accuracy in question-answering.
Experiments conducted on various benchmarks, including MLVU, QAEGO4DMC, EgoSchema, ActivityNet-QA, and StreamingVQA (RSV-Ego and RSV-Movie) datasets, demonstrate that ReKV improves VideoQA accuracy while maintaining stable inference latency and memory usage as the number of frames increases. The method enables real-time interaction and long-term context for StreamingVQA tasks.

### Strengths
- The paper presents a novel and simple, training-free method that extends the capabilities of existing Video-LLMs for StreamingVQA. By integrating a sliding-window attention mechanism and efficient KV-Cache retrieval, ReKV addresses the challenges of processing long video streams in real-time.

- The methodology is well-motivated and thoroughly explained. The paper clearly defines the StreamingVQA task, differentiates it from traditional OfflineVQA, and outlines the specific challenges involved. The proposed solutions are detailed and logically sound.

-  The paper is well-organized and clearly written with figures to support the method explanation.

- ReKV significantly improves efficiency and accuracy over existing VideoQA models on multiple benchmarks. The ability to handle long video streams in a streaming fashion has practical importance for real-world applications. The training-free nature of ReKV can potentially enhance its applicability across different Video-LLMs.

### Weaknesses
Currently, a major limitation of the method is that the method is that it is only evaluated on LLaVA-OV models (0.5B and 7B). Although these models are strong baselines, the applicability of ReKV to other Video-LLMs is not demonstrated. Evaluating ReKV on a broader set of models would strengthen the claim of its versatility and general applicability.
I’ll be happy to increase my score if that limitation is addressed.

### Questions
- Have the authors tested ReKV with other Video-LLMs besides LLaVA-OV? Demonstrating the integration and performance of ReKV with different architectures (e.g., VideoChatGPT…) would confirm its general applicability and ease of integration.
- Table 5 shows that the internal KV-Cache retrieval reduces computational overhead compared to external retrieval. However the “internal retrieval” retrieves KV-Caches for each attention layer independently while it is only done once for the “external retrieval”. How do you explain that the internal is faster?


Minor: 
In practice, how does ReKV manage KV-Cache storage for extremely long video streams, such as surveillance footage that can run continuously for many hours or days? Are there mechanisms in place to prevent unsustainable increases in cache size, and how does this impact performance and resource requirements?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present ReKV (Retrieve In-context Video KV-Cache) for streaming video question-answering. The authors incorporate a sliding-window attention mechanism on existing VideoLLMs, introduce a retrieval method that leverages an external retriever or the parameters within Video-LLMs to retrieve only queryrelevant KV-Caches. The authors evaluates the model on both long video QA and streaming videoqa.

### Strengths
1. The number of evaluation benchmark for the proposed method is adequate. 

2. The improvements against standard VideoLLMs are substantial.

### Weaknesses
1. Lack of fair comparison against existing memory-based models (including VideoStreaming and Flash-VStream). It would be better if the author could provide results for ReKV and previous memory-based models under the same VideoLLM backbone to show the effectiveness of the proposed method, for both long video benchmarks and streaming video benchmarks. Specifically, the comparison should control for factors such as the visual encoder, projector, LLM, training data, and training/evaluation pipelines. The absence of such a controlled comparison makes it difficult to isolate the true impact of the proposed retrieval mechanism.

2. Missing related works. The authors should discuss the novel contribution compared to the paper VideoLLM-online[1], MC-ViT[2]. The discussion should clarify how the proposed method differs in terms of training methodology (training-free vs. fine-tuning), the amount of visual information retained (single token vs. full visual features), and the specific mechanisms for handling long videos (e.g., token pruning, merging, or memory-based approaches).

3. The “External Video KV-Cache Retrieval” is confusing, do the authors mean selecting the keyframes using the query information via the CLIP-based models (like a cross-modal matching)? This is already investigated by a number of works, including ATP [3], SeViLA[4] and so on.  It would be if for the authors to clarify how "External Video KV-Cache Retrieval" differs from or improves upon the keyframe selection methods. The authors should also clarify whether this retrieval mechanism is a core contribution or merely a baseline for comparison, and if it is a baseline, why it was chosen over other existing methods.

### Questions
All weakness, and:

1. The citation format is inconsistent over the paper, the authors should unify this format. 

2. Since the model is claimed to integrate seamlessly with existing Video-LLMs, is it possible to apply to a bigger VideoLLM backbone, like around 70B scale? 

3. In Table 4,  for offline video question-answering, could the authors elaborate more on the baseline setting of the LLaVA-ov model, like frame numbers? Also, could the authors compare the efficiency of the proposed ReKV compared to the original LLaVA-ov model in the table?

### Soundness
3

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
4

### Summary
The paper introduces ReKV, a novel, training-free approach designed to enhance the efficiency of Video Large Language Models (Video-LLMs) for streaming video question-answering (StreamingVQA). Unlike traditional VideoQA systems that process entire videos before answering queries, ReKV processes video streams in real-time, allowing for prompt responses. The method employs a sliding-window attention mechanism to reduce computational overhead and uses a KV-Cache system to store and retrieve relevant video information efficiently. The approach separates video encoding and question-answering into distinct processes, enhancing efficiency. The paper demonstrates the efficacy of ReKV through comprehensive experiments, showing improvements in accuracy, latency, and memory usage over existing models.

### Strengths
1.	Efficiency: The sliding-window attention mechanism and KV-Cache retrieval significantly reduce computational overhead and memory usage.
2.	Real-Time Processing: The method allows for real-time responses to queries, making it highly practical for applications like surveillance and live broadcasts.
3.	Comprehensive Evaluation: The paper provides extensive experimental results, demonstrating the effectiveness of ReKV across multiple benchmarks.
4.	Seamless Integration: ReKV integrates seamlessly with existing Video-LLMs without requiring additional training, making it easy to adopt.

### Weaknesses
1.	Writing Quality: The organization of this paper could be improved. It is not appropriate to place ablation study before main experiments. Sec 2.1 Task definition and discussion should not be a part of Method. This part is too repetitive of the discussion in the introduction.
2.	Citation format: In Table 4 Line 391 there may be a misleading citation of Video-LLaVA-7B, pointing to the same reference of Video-ChatGPT-7B.
3.	Lack explanation: The term "oracle retrieval" from Table 2 and Line 305 is difficult for readers to understand. How is the “recall” metric calculated? How can it be 100?

### Questions
1.	Generalizability of method: Since ReKV is a training-free method, can it be integrated with models other than LLaVA-OV? Are there any experimental results?
2.	Scalability: How does ReKV scale with increasing video length and complexity? Are there any observed limitations when dealing with very high-resolution videos or videos with a high frame rate?
3.	Implementation details: What is the hyperparameters of external retrieval?

### Soundness
4

### Presentation
2

### Contribution
3
