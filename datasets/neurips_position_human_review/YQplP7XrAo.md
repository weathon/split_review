# Vision encoders should be image size agnostic and task driven

- Decision: Reject
- Scores: 3, 7, 6

## Abstract
This position paper argues that the next generation of vision encoders should be image size agnostic and task driven. The source of our inspiration is biological. Not a structural aspect of biological vision, but a behavioral trait – efficiency. We focus on a couple of ways in which vision in nature is efficient, but modern vision encoders not. We – humans and animals – deal with vast quantities of visual data, and need to be smart where we focus our limited energy – it depends on the task. It is our belief that vision encoders should be dynamic and the computational complexity should depend on the task at hand rather than the size of the image. We, also, provide concrete first steps towards our vision – a proof-of-concept solution for image classification. Despite classification being not very representative for what we are trying to achieve, it shows that our approach is feasible and promising.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript claims the form the vision encoder should be. The authors propose two properties, image-size agnostic and task-driven, which are motivated by their opinion with biological inspiration. Pilot experiments are performed as a proof-of-concept.

### Strengths
- The concept based on the biological motivation is worthy.

- I agree that the larger image size, such as 2000x2000, would become a critical issue when using ViT with standard patch partitioning.

### Weaknesses
- Evaluation of the idea - I agree with the "image size agnostic" part; patch partitioning fashion in the ViT is unnatural for larger image sizes. However, I think opinions in the research community will vary on the "task-driven" part. The current approach, where the foundation model is task agnostic and only the final head is task specific, would be thought of as sufficient.

- Although I understand that this manuscript is for the position paper track, I think that it needs more objective evidence for the two claims than just opinion based on verbal statements. In particular, the task-driven part lacks solid references or relevant data on biological motivation.

- Although the term encoder is used, it seems like the authors are tackling the tokenization step of an image, such as patch embedding, rather than the encoder itself. In other words, the topic is rather related to image representation, and the encoder itself is still ViT.

- The top-1 accuracy in Table 2 is too low. I think a reasonable baseline would be 0.7 to 0.8.

### Questions
See the weaknesses above. Overall, I understand that this is for the position paper track, but the two claims require more solid evidence rather than opinions.

### Presentation
2

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper advocates for vision encoders to be "image size agnostic" and "task-driven," drawing inspiration from the biological vision. The authors support this position by by introducing an iterative transformer system that processes images by selectively extracting "multi-zoom patches" in a top-down manner, guided by a learned policy. This system maintains an evolving internal state as a form of memory, allowing it to build an understanding of the image over several steps. They demonstrate the feasibility of their approach on the ImageNet-1K image classification task, with a two-stage training process. The position, ultimately aims to reignite interest in biologically-inspired vision models with the idea of making them more efficient and task-aware.

### Strengths
- The paper is well-written, logically structured, and easy to understand. It uses effective analogies and illustrations
- The overall idea is quite interesting. Also, it pinpoints a fundamental inefficiency in current vision encoders regarding their image size dependency.
- This work offers a specific, implementable proof-of-concept, rather than just a hypothesis. The results on ImageNet-1K are promising, and demonstrates feasibility of the idea

### Weaknesses
While the position effectively argues for image size agnosticism and task-driven encoders, the primary focus on these two aspects for designing/proposing a biologically-inspired vision encoder might be in a way, limiting, especially if we consider real-world visual complexities. Real-world environments present a multitude of other challenges beyond just image resolution, such as occlusions, lighting variations, background clutter, object poses, etc. Although the proposed method could implicitly benefit these scenarios by focusing on salient features, the paper doesn't explicitly discuss them. Expanding on this would further solidify the breadth of the proposed approach's potential impact.

### Questions
See weaknesses

### Presentation
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose that current vision architectures (e.g., ViTs, CNNs) process images inefficiently because computational complexity scales with image size rather than task difficulty. They advocate for a shift toward models whose computation depends on the task at hand, processing high-resolution information only where needed—similar to human foveal vision. They outline a proof-of-concept: a **top-down, multi-zoom patch extraction method**, an **iterative transformer with evolving internal state**, and a **policy module** (trained via GRPO) to decide where to "look" next. Experiments on ImageNet-1K validate feasibility, though image classification is acknowledged as a limited benchmark for task-driven capabilities. The paper positions this approach as both biologically inspired and more computationally efficient, reviving older attention-based vision ideas with modern architectures.

Position: Vision encoders should be image size agnostic and task driven.

### Strengths
1. The paper is well written, clear in communication and its stance
    
2. Biological inspiration put across is valid and the efficiency argument is well motivated.
    
3. The PoC further adds well in support of the argument.
    
4. The proposed proof of concept and he paper make it clear that biological inspiration may not imply copying of the biological system as we may be limited by hardware and engineering potential.  
    
5. The idea of learning the right patches does seem well motivated although may be expensive given we want to build task driven encoders.
    
6. good discussion about open questions

### Weaknesses
1. If we adopt separate task-driven vision encoders for different tasks, how do we scale their training efficiently? The potential efficiency gains at inference may be offset by the cost of training and maintaining multiple large parameter sets across tasks.
    
2. The paper does not provide concrete measurements of efficiency (e.g., FLOPs, latency, memory usage) for the representative task and pipeline, making it difficult to evaluate whether the proposed approach actually delivers computational savings.
    
3. In domains with limited labeled or unlabeled data, how would we train effective task-driven encoders? The paper does not address whether the policy and encoder could generalize to low-data settings or transfer from other domains.
    
4. The paper does not discuss how the proposed approach would extend to other learning paradigms, such as vision–language models (VLMs) or broader multimodal systems. In such settings, integrating a task-driven, size-agnostic encoder may require adapting the pipeline to work with text or other modalities, and it is unclear whether the two-stage process (policy training followed by model training) would remain feasible or become prohibitively complex and expensive.

### Questions
1. How would we scale training of different vision encoders for different tasks? 
2. In domains with limited labeled or unlabeled data, how would we train effective task-driven encoders?
3. How would the sample pipeline work in a VLM based setting?

### Presentation
3
