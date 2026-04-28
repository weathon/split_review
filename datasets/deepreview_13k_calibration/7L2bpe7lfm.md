# Large Scale Video Continual Learning with Bootstrapped Compression

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
Continual learning (CL) promises to allow neural networks to learn from continuous streams of inputs, instead of IID (independent and identically distributed) sampling, which requires random access to a full dataset. This would allow for much smaller storage requirements and self-sufficiency of deployed systems that cope with natural distribution shifts, similarly to biological learning. We focus on video CL employing a rehearsal-based approach, which reinforces past samples from a memory buffer. We posit that part of the reason why practical video CL is challenging is the high memory requirements of video, further exacerbated by long-videos and continual streams, which are at odds with the common rehearsal-buffer size constraints. To address this, we propose to use compressed vision, i.e. store video codes (embeddings) instead of raw inputs, and train a video classifier by IID sampling from this rolling buffer. Training a video compressor online (so not depending on any pre-trained networks) means that it is also subject to catastrophic forgetting. We propose a scheme to deal with this forgetting by refreshing video codes, which requires careful decompression with a previous version of the network and recompression with a new one. We expand current video CL benchmarks to large-scale settings, namely EpicKitchens-100 and Kinetics-700, with thousands of relatively long videos, and demonstrate empirically that our video CL method outperforms prior art with a significantly reduced memory footprint.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose a method for large-scale long video continual learning to learn from continuous streams without access to the entire dataset. They employ a rehearsal-based approach which reinforces past samples in a memory buffer. To deal with long-videos and continuous streams, they propose to use video codes (video embeddings) instead of raw inputs, and train a video classifier by IID sampling from this buffer. 

A video compressor is used to generate the video codes. To deal with the video compressor's catastrophic forgetting, the authors propose continuous compression and decompression technique over the neural-code rehearsal buffer (past video codes). They also train a classifer in the compressed space. 

The authors show results on EpicKitchens-100 and Kinetics-700 datasets in two settings -- 
- (i) incremental learning from scratch, and 
- (ii) pretraining.

### Strengths
The problem statement is interesting -- continual learning of large-scale long videos from continous video streams. 

The proposed technique is reasonable, paper is well-written, and nicely motivated. 

The design of the experiments is clearly explained and exhaustive-- 
- (i) default IID sampling, 
- (ii) incremental learning, and 
- (iii) CL with pretraining. 

For both the incremental learning and CL with pretraining settings, evaluations are done on two large-scale long-video benchmarks -- Kinetics-700 and EpicKitchen-100. The proposed method outperforms the baselines.

### Weaknesses
 - During the incremental learning stage, the codes in the buffer are decoded using the decoder from the previous task. Can the authors quantify the additional memory required to store decoder weights from the previous task, and compare it with the memory savings from using compressed codes instead of the raw video frames. This would give a clear picture of the overall memory trade-offs in the proposed method. 

- Is a single latent code enough to compress/represent a temporally-long and possibly diverse video? Can the authors provide analysis or ablations showing how the performance varies with varying video lengths or video diversity? For instance, can you compare the performance on short vs long videos, or videos with varying amount of scene/action changes.

### Questions
What was the number of frames in the videos that were used for training/evaluation? Could you clarify how the performance varies with video length, and whether there's a maximum video length beyond which the method's performance degrades significantly? This would help the readers understand the practical limitations of this approach?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a memory-efficient approach for video continual learning (CL) using compressed embeddings stored in a neural-code rehearsal buffer. The main idea is to reduce the high memory demands of video CL by compressing video frames into compact neural codes instead of storing raw data. The method also includes a code-refreshing mechanism to mitigate representational drift, which may happen as the model continues the incremental learning process. The method is evaluated on Epic-Kitchens-100 and Kinetics-700, across both pre-trained and completely incremental learning settings. Empirical results indicate that the method achieves promising performance with significantly reduced memory usage.

### Strengths
1. **Reasonable Approach to Memory Efficiency**: The paper introduces a novel memory-efficient method for video continual learning by storing compressed neural codes rather than raw frames. This approach, combined with a code-refreshing mechanism, is a reasonable way to adapt continual learning to video data’s storage constraints and combat representational drift and catastrophic forgetting.

2. **Clear Experimental Setup**: The experiments are well-structured, covering both pre-training and incremental learning settings on widely-used large-scale video datasets (Epic-Kitchens-100 and Kinetics-700). Memory constraints and compression rates are clearly defined.

3. **Potential Significance for Real-World Applications**: By focusing on reducing memory demands in video CL, the paper tackles a central obstacle in scaling continual learning to real-world applications. This approach could be impactful for memory-limited devices and applications requiring continual processing of video data, such as surveillance or autonomous systems.

### Weaknesses
1. **Limited Novelty in Memory Efficiency Solutions**
   While the paper proposes a new method to address memory efficiency in video CL, this problem has already been identified and approached by prior works. From a benchmarking perspective, **vCLIMB** [1] redefined the memory metric specifically for video CL, proposing **Memory Frame Capacity** to measure memory usage in terms of frames rather than full video instances. This framework allows for evaluating frame selection strategies in video CL. From a method perspective, Furthermore, vCLIMB implemented a regularization term to reduce representation drift between original videos and stored frames, improving memory efficiency in rehearsal-based CL. Additionally, **FrameMaker** [2] further addresses memory efficiency by introducing **Frame Condensing**, where a single condensed frame per video is stored along with instance-specific prompts to retain temporal details. By not comparing against these methods, the paper’s memory efficiency claim is weakened, as the approach lacks context relative to prior works. Specifically, the paper does not address how its method compares to the frame selection strategies used by vCLIMB, or the frame condensing approach of FrameMaker, both of which are designed to reduce memory footprint while preserving temporal information. The lack of comparison makes it difficult to assess the true novelty and contribution of the proposed method in the context of existing memory-efficient video CL techniques.

2. **Lack of Comparison to Rehearsal-Free Methods**
   If memory efficiency is a primary goal, comparisons with **rehearsal-free video CL methods** are essential, as these approaches inherently avoid memory constraints. For instance, **ST-Prompt** [3] achieves continual learning without rehearsal by using vision-language models and temporal prompts to encode sequential information, thus sidestepping the need for a memory buffer. More recently, **DPAT (Decoupled Prompt-Adapter Tuning)** [4] combines adapters for capturing spatio-temporal information with learnable prompts, employing a decoupled training strategy to mitigate forgetting without rehearsal. While DPAT may be too recent for comprehensive testing, at minimum, a comparison to ST-Prompt or a discussion on why rehearsal-free methods were not included would provide a more complete assessment of memory efficiency in CL. The paper should clarify why it focuses on rehearsal-based methods when rehearsal-free approaches offer a more direct solution to memory constraints.

3. **Inadequate Baselines for Modern CL Standards**
   The paper’s use of **GDumb** [5] as a baseline is insufficient for evaluating the performance of a modern CL method. GDumb, introduced in 2020, was meant to highlight flaws in existing CL evaluation metrics and methods, demonstrating that a simple random-sampling rehearsal method could outperform many complex algorithms of that time. However, it is not representative of state-of-the-art continual learning. Since its release, more advanced rehearsal-based methods, such as **ER-ACE** [6] and **L2P** [7] have been developed, each addressing the limitations GDumb originally exposed. GDumb’s rudimentary approach lacks the complexity needed to benchmark against a method claiming novel contributions in memory-efficient CL, and thus relying on GDumb alone creates an unconvincing evaluation framework for the proposed method. Including state-of-the-art baselines from both image and video CL (see previous point for video baselines) would strengthen the paper’s claims of memory efficiency and performance. The choice of GDumb as a primary baseline does not adequately demonstrate the proposed method's superiority over more recent and sophisticated continual learning techniques.

4. **Insufficient Justification of Benchmark Superiority**
   The paper introduces a new benchmark with a pre-training phase on a subset of classes, followed by incremental learning. However, **Park et al. (2021)** [8] has already explored a similar pre-training and incremental learning setup for video CL. The paper does not provide sufficient justification for why its benchmark is necessary or superior to existing benchmarks (such as [1] and [8]). A new benchmark should ideally improve upon current setups in aspects such as realism, task granularity, or sequence transitions. Without a clear rationale, the proposed benchmark appears redundant rather than an improvement. The paper needs to explicitly state the limitations of existing benchmarks and how the proposed benchmark addresses these limitations, especially given the existence of similar setups in prior work.

5. **Unsubstantiated Novelty Claim in Large-Scale, Long-Video Testing**
   The paper claims to be the first to extend CL to “large-scale naturally-collected long videos.” This claim is inaccurate, as several previous studies have conducted video CL on large, untrimmed datasets. For example, **vCLIMB** and other works used **ActivityNet** [1] for CL, which includes long, untrimmed videos from natural events and provides extensive temporal context. Similarly, the **Kinetics** and **Something-Something** datasets have been widely used for video CL research, with recent methods like **DPAT** [4] even leveraging Epic-Kitchens for long, naturally collected video scenarios. Without clear evidence that the benchmark adds unique value, such as in video length or task diversity, the claim of novelty is misleading and diminishes the contribution’s significance. The paper needs to provide a more rigorous comparison of its benchmark to existing datasets, demonstrating a clear advantage in terms of video length, diversity, or task complexity to justify its novelty claim.

### Questions
1. **Comparison to Advanced Video CL Methods**: How does the proposed method compare with other recent memory-efficient video CL approaches like vCLIMB and FrameMaker, which use selective frame retention with temporal consistency regularization and condensed frames? These comparisons could contextualize the memory benefits claimed in the paper.

2. **Evaluation Against Rehearsal-Free Methods**: Since memory efficiency is a key focus, why were rehearsal-free methods like ST-Prompt not included as baselines? Including or discussing these could provide a clearer assessment of the method’s memory advantages.

3. **Justification of Benchmark Novelty**: The paper introduces a new benchmark setup with pre-training followed by incremental learning. Could the authors elaborate on why this setup is preferable or unique compared to existing video CL benchmarks? Quantifying the differences and summarizing them in a table might be useful here. 

4. **Rationale behind Baselines**: Could the authors explain why the baselines were chosen, including GDumb?

5. **Clarification of “Large-Scale, Naturally-Collected, Long Videos” Claim**: The paper claims to be the first to use “large-scale, naturally-collected long videos” in CL, but prior works have used datasets like ActivityNet, Kinetics, and Something-Something. Could the authors clarify what sets this benchmark apart from these established datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work implements continual learning for action and object classification in relatively long video clips. This is an important setting for many applications such as robotics, and is quite challenging due to the high information density and temporal correlations inherent in video data. The authors employ a VQ-VAE-based video compression approach to enable large-scale storage of encoded video information in a buffer, enabling replay of previously encountered examples to mitigate catastrophic forgetting in incremental learning settings from scratch and with pretraining. The compression strategy is designed to balance stability and plasticity, using a frozen decoder for each task to minimize representational drift. The proposed algorithm outperforms several relevant baselines by large margins under memory-constrained conditions.

### Strengths
1. The described setting (continual learning of classification tasks involving long videos as input) is relevant to many practical applications in robotics, security camera systems, and other areas – it is also quite challenging due to the size of video data and the inherent temporal correlations, and as such has been explored by existing work to only a limited extent. 

2. Replay-based continual learning methods in image processing applications can have a large memory storage footprint – this is exacerbated with video data, making approaches like this one especially practically useful in this setting. 

3. Combining a stored set of frozen “decompressors” to manage representational drift with a “compressor” trained on-the-fly is an interesting and novel approach to this continual learning problem. Figure 2 is well-designed and quite helpful for understanding the approach. 

4. The proposed approach outperforms the baselines on all benchmarks, and often by large margins. The selected baselines are appropriate and are compared with the proposed method in reasonable ways. 

5. The paper is well-written, and for the most part is clear and easy to follow. For example, the methods section is written in a way that makes the proposed approach easy to understand, by first presenting the simplified IID case and then moving to the incremental learning case. There is an insightful and balanced account of biological inspiration and plausibility of the proposed algorithm in the introduction.

### Weaknesses
This paper appears to present strong state-of-the-art results on an important and challenging continual learning problem, but the review score is limited primarily due to insufficient detail in describing and justifying the proposed algorithm and in describing the setting/datasets. Performance comparisons are also not presented in a sufficiently rigorous way (no estimates of uncertainty, no clear definition of the accuracy metric being used). However, the weaknesses of the paper appear relatively addressable in ways that could improve this reader’s review score. 

1.	The proposed method uses an existing video compression algorithm to allow a large portion of compressed video data to be stored in a buffer for replay, with novelty mainly arising from the specific configuration of encoders and decoders and how they are trained or kept frozen at different stages of continual learning in different settings (e.g., keeping a separate decompressor for stored codes from each task) – however, this configuration is not strongly justified either theoretically or empirically (see also items 1 and 2 in the “questions” section).

2.	In the related works section under “Continual Learning with Images and Videos”, there is only one reference to an existing work on continual learning with videos. To make the claim that this is the first practical CL algorithm in a large-scale long video setting would seem to require a more thorough review of prior approaches (even if they do not fully meet this criterion) to distinguish the current work from them – for example, the authors could consider the following:
a.	Verwimp, Eli, Kuo Yang, Sarah Parisot, Lanqing Hong, Steven McDonagh, Eduardo Pérez-Pellitero, Matthias De Lange, and Tinne Tuytelaars. "Clad: A realistic continual learning benchmark for autonomous driving." Neural Networks 161 (2023): 659-669.
b.	Wu, Jay Zhangjie, David Junhao Zhang, Wynne Hsu, Mengmi Zhang, and Mike Zheng Shou. "Label-efficient online continual object detection in streaming video." In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 19246-19255. 2023.

3.	There is little to orient the unfamiliar reader with the overall setting, specifically the EpicKitchens and Kinetics-700 datasets.  It would be useful to include some additional details, such as basic statistics on how long the videos are, examples of the kinds of actions/objects that are depicted in the datasets, how the labeling works (e.g., does each frame of the video have one label and one label only? How do the models and the labeling schemes manage smooth transitions between classes?) and visualizations of a few examples (there are a few examples from Epic-Kitchen in Figure 1, but none from Kinetics-700 and there is no in-text reference to Figure 1).  

4.	Although the proposed method appears to outperform the baselines by large margins, there is no way to assess the statistical reliability of these results. I think it is important to include results from multiple training runs and assess variability among runs (e.g., reporting standard error or confidence intervals) in addition to the mean performance numbers, and to add error bars to Figure 3.

### Questions
1.	Additional ablation studies could further justify aspects of the proposed approach. In particular, it would be interesting to explore the benefits and drawbacks of the specific way in which the autoencoder is trained. For the incremental setting, is it necessary to keep a separate decoder for each task to limit representational drift, or does the method perform well using only one decoder that is trained continuously? Does it improve performance to maintain a separate encoder for each task in addition to a separate decoder? Any performance tradeoffs here should be described alongside the drawbacks of maintaining more encoders/decoders – what is the size in memory of the autoencoder parameters relative to the replay buffer? For example, if it so happens that it is very cheap to store lots of different encoders/decoders for each task, this approach might be well-justified if it also improves performance. 

2.	Related to the above, it does not seem entirely clear what is meant by the compressor being trained “continuously” in the incremental setting. Is it that there is just one compressor that continues to be updated with each task? Or is a separate compressor trained from a random initialization for each task? Or, at the conclusion of each task, is the compressor for that task frozen and a copy made of it to form the initial condition of the compressor to be trained for the next task? 

3.	There are some prior works that have explored continual learning in video-formatted datasets. One claim that underscores the novelty/significance of the work is that these video clips are much longer – can you provide a measure of quantification for this? How much longer, and is this a practically meaningful increase in duration of videos that can be processed? 

4.	In section 5.1 where does the 224x224x14 dimension of each video clip come from? Are these grayscale videos with 14 frames? (this would seem inconsistent with the statement that the method operates on long videos)

5.	In the “baselines” section, a limit on the number of samples in the buffer per task is described. However, it is not described how these samples were selected – e.g., perhaps they were randomly (IID) selected from each task, in which case this should be made explicit. There is a statement in section 6.1 that “One interesting finding from our work is that we do not need to apply any frame selection or sampling strategy, even for very large videos,” however it is not clear what this means – is it that the compression is so efficient that you can store every single frame? Or is it that random selection is sufficient? (this strategy is commonly used in replay-based continual learning approaches). For the sampling selection strategies of the baselines, I see that some are explained in the appendix, although it is not clear how the sampling worked for REMIND.

6.	Are the incremental and pretraining settings here best characterized as class-incremental learning or task-incremental learning? (i.e., when the trained model is evaluating a new, unknown sample, does it also need to be told which task the sample belongs to?)

7.	What is meant by “average accuracy” in tables such as table 1? This can be measured in different ways – for example, it could be average accuracy on all tasks measured at the conclusion of the task sequence, or it could also be averaged across accuracy measured after each task increment. 

Minor comments: 

8.	Some of the references appear to be incorrectly formatted – e.g. [1], [3], [6], and many more do not have a journal or conference listed. A few also have incomplete author information (e.g., [1] does not list an author, only the title and year). It is also my understanding that in-text citations should be author-date formatted instead of just numbers for each reference (specifically for ICLR). 

9.	There are a few typos - e.g., in section 3.2 “a concatenation of m samples from each of the task” and near the end of section 5.3 “we store the resulting the codes.” Additional proofreading would be helpful to refine the paper. 

10.	The average forgetting (AvgF) metric should be briefly defined in the paper – currently, there is just a citation to the Avalanche GitHub repository. 

11.	The method seems to be referred to as “BootstrapCL” in some of the tables, but this name is not introduced anywhere else in the text. Why is it called “BootstrapCL”? It should be made more clear that this is the name of the new algorithm – e.g., in the tables it could be called “BoostrapCL (Ours)”. It can also be helpful to bold the best performance numbers on each metric in the tables. 

12.	Equation 10 seems to imply that the same encoder is used for both new samples and samples reconstructed from the buffer. Why is it that the decoder from previous tasks needs to be retained to decode those older examples, but the same encoder can be used for all tasks?  It is seemingly contradictory that, in equations 6 and 7, there appear to be different versions of the encoder for each task ($ϕ_1$, $ϕ_2$, etc.) when it is also stated that the encoder is trained continuously in the incremental setting. 

13.	I suggest combining the ablation study tables 3-5 in the appendix into a single table, so it is easier to compare the performance under each ablation with the baseline performance and also compare among the different ablations. 

14.	If I understand correctly, “compressor” is used interchangeably with “encoder” and “decompressor” with “decoder.” I suggest choosing one set of terms and using them throughout the paper consistently. 

15.	The CL acronym for continual learning should also be used consistently.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a continual learning (CL) framework for video. The proposed method (pre)trains a compressor for video frames with an encoder and decoder. Additionally it maintains a buffer of past codes which are used when changing task. The system uses these buffers to do, in the case of experiments in the paper, noun and action classification. Catastrophic forgetting is minimized by maintaining the previous task buffer and making sure the compressor doesn't drift too much when changing tasks.

### Strengths
Originality:
While most of the work is based on existing literature, the use of compressed representations in this context is novel.

Quality:
It's nice to see some "real world" datasets being used in this context so there is a beginning of good experimental validation here (but see below). The ablations in the appendix should have been in the main paper, but are nice.

Clarity:
The paper is nicely structure but see below.

### Weaknesses
Unfortunately the paper suffers from several weaknesses;

Experimental validation - while I appreciate the use of real world video the experimental validation is lacking. There are only two tasks used and if a method is aiming to show improvement in continual learning then I would really expect more. For example including more datasets (Ego4D, SSv2 for example) and more tasks (dense tasks, pixel prediction) would have made the case of the paper stronger. The current experimental setup, focusing solely on noun and action classification, does not fully demonstrate the method's generalizability to other video understanding tasks. The lack of evaluation on dense prediction tasks, such as segmentation or optical flow estimation, leaves a gap in the assessment of the method's capabilities. Furthermore, the limited number of datasets used restricts the evaluation to specific video characteristics, potentially overlooking challenges posed by other types of video content.

Analysis - there is very little analysis as to what the model learns and how - the main ablation is the previous task buffer size, the rest is in the appendix but not a lot of analysis of the significance of the results is given. I would have loved to see how the compressed representation evolve as more tasks are introduced - do they stay the same? do they change abruptly to fit the new task (while still being meaningful for the old ones)? some visualization of the learned representation would be nice as well. The paper lacks a thorough investigation into the learned representations. The analysis is primarily focused on the impact of buffer size, while neglecting the evolution of the compressed representations over the course of continual learning. Understanding how these representations adapt to new tasks, whether they undergo gradual changes or abrupt shifts, is crucial for evaluating the effectiveness of the proposed method. Visualizing the learned representation space would provide valuable insights into the model's behavior and its ability to retain knowledge from previous tasks.

Clarity - I found the paper hard to follow. The model and problem set up are not well explained and the figure captions do little to help. Specifically, the method section (4) needs more context with clear definition of what tasks are and how they evolve over time. Figure 2 caption should be extended - the model is quite simple (I think) and should be completely understandable from that figure alone. The method section lacks a clear and concise explanation of the problem setup. The definition of tasks and how they evolve over time is not well-defined, making it difficult to understand the continual learning scenario. The figure captions, particularly for Figure 2, do not provide sufficient information to fully grasp the model architecture and its functionality. A more detailed description of the model and its components is needed to improve the clarity of the paper.

### Questions
-

### Soundness
2

### Presentation
2

### Contribution
2
