# Understanding Long Videos with Multimodal Language Models

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Large Language Models (LLMs) have allowed recent LLM-based approaches to achieve excellent performance on long-video understanding benchmarks. We investigate how extensive \textit{world knowledge} and strong \textit{reasoning skills} of underlying LLMs influence this strong performance. Surprisingly, we discover that LLM-based approaches can yield surprisingly good accuracy on long-video tasks with limited video information, sometimes even with no \textit{video specific} information. 
Building on this, we exploring injecting video-specific information into an LLM-based framework. We utilize off-the-shelf vision tools to extract three object-centric information modalities from videos and then leverage natural language as a medium for fusing this information. Our resulting Multimodal Video Understanding (MVU) framework demonstrates state-of-the-art performance across multiple video understanding benchmarks. Strong performance also on robotics domain tasks establish its strong generality. Our code will be released publicly.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces two baselines and a novel approach called the Multimodal Video Understanding (MVU) framework for video understanding tasks. The baselines explore using either a single frame or no visual input at all. In contrast, MVU aggregates multimodal information relevant to the video to enhance understanding.

### Strengths
+ It is interesting that this work introduces three key attributes essential for video understanding: Global Object Information, Object Spatial Location, and Object Motion Trajectory. These attributes contribute significantly to a more comprehensive analysis of video content.

### Weaknesses
 - Although this paper focuses on long-video understanding, it lacks specific design elements to address long-video scenarios. Challenges such as context length limiting input frames and modeling long-range temporal information are not directly addressed. The attributes introduced—Global Object Information (GOI), Object Spatial Location (OSL), and Object Motion Trajectory (MOT)—are not tailored to tackle these issues in long-video understanding.

- In Table 1, the comparisons may be weaker due to the differing training setups and base models used across experiments. As such, the superior performance of SF-LLM over the state-of-the-art does not necessarily imply that the number of frames is irrelevant for video understanding.

- Since the model is based on LLaVA-v1.5-13B, an important baseline is missing: the use of multiple frames as input for LLaVA-v1.5-13B.

- Certain details are lacking, such as the method for using LLaVA-v1.5-13B for frame sampling, as mentioned in Figure 3.

- Likelihood Selection is widely used in the MCQ benchmark as an additional track. For a fairer comparison, other methods should also incorporate this strategy for comparison results.

- The benchmark in this paper only includes mid-length videos, roughly under three minutes. To more competitively demonstrate MVU's capabilities in long-video understanding, it would be beneficial to evaluate on benchmarks like VideoMME and LongVideoBench.

### Questions
As mentioned in the weakness.

### Soundness
3

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
3

### Summary
This paper proposes a training-free approach to understanding long-form videos by extracting explicit image-/object-level information. The extracted information is translated into natural language descriptions to make LLM ‘see’ the visual input. Experimental results on several videoQA benchmarks demonstrate the superiority.

### Strengths
1. The proposed likelihood selection approach offers a good way to speed up the inference in autoregressive LLMs. 
2. Going beyond existing video datasets, this paper further evaluates the generalization ability on Open-X-Embodiedment.
3. The paper is well written and easy to follow.

### Weaknesses
1. It seems that using likelihood as a selection criterion still focuses on the exact match between the generated text and the answer candidates in a per-logit manner, without considering the semantic meaning. For example, ‘C is washing plates’ vs ‘C is cleaning dishes’. 
2. Unlike prior approaches where all answer candidates are fed together to the language model, the proposed likelihood selection method organizes the Q-A pairs in a batch dimension. In this way, it seems that LLM fails to analyze the relationship between answer candidates, increasing the difficulty of QA.
3. If the frames are uniformly sampled across the entire long video, how can you ensure the consistent occurrence of objects? In certain cases, the appeared objects in each frame are completely different. Another related question is whether using X_{OSL} and X_{OMT} extracted from densely sampled frames (i.e. with better object/trajectory consistency) would lead to performance gain. 
4. The authors are encouraged to evaluate the model on more long-video QA benchmarks, especially those designed to mitigate the language bias of existing long-video QA benchmarks (e.g., EgoSchema). 
5. In Tables 2 and 3, a series of recent state-of-the-art approaches are not compared. [1][2]

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes to inject video-specific information into an LLM based framework for video understanding. Specifically, the authors utilize off-the-shelf vision tools to extract three object-centric information modalities from videos and then leverage natural language as a medium to fuse the information. I think the proposed method seems novel and interesting. But I think this paper leaks a comparison with recent papers and the performance is not good enough.

### Strengths
The proposed method seems novel and I think that makes sense for video understanding. But I think the key frame selection plays the most important role for video understanding -- it seems the authors do not propose new method on this.

### Weaknesses
1.Figure 1 caption: “(left-right)” -> “(left-bottom)”;
2.I think the authors used both \cite{} and \citep{} in their writing;
3.Missing comparison with recent methods, for examples the publish papers in 2024. I think that is necessary to better your paper;
4.The performance seems not so good, only a marginly superiority compared to the counterparts even without comparing the recent methods. I think the performance is not good;
5.How to select the frames for most relevant frames? Is there any novelty to do that -- I think this is the most important part for video understanding.

### Questions
See the fifth point of weakneses.

### Soundness
3

### Presentation
2

### Contribution
2
