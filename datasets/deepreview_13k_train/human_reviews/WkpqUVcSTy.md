# SlowFast-LLaVA: A strong training-free baseline for video large language models

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
We propose \textbf{S}low\textbf{F}ast-LLaVA (or SF-LLaVA for short), a training-free video large language model (LLM) that can jointly capture detailed spatial semantics and long-range temporal context without exceeding the token budget of commonly used LLMs. This is realized by using a two-stream SlowFast design of inputs for Video LLMs to aggregate features from sampled frames in an effective way. Specifically, the Slow pathway extracts features at a low frame rate while keeping as much spatial detail as possible (\textit{e.g.,} with $12\times24$ tokens), and the Fast pathway operates on a high frame rate but uses a larger spatial pooling stride (\textit{e.g.,} downsampling $6\times$) to focus on the motion cues. As a result, this design allows us to adequately capture both spatial and temporal features that are beneficial for detailed video understanding. Experimental results show that SF-LLaVA outperforms existing training-free methods on a wide range of video tasks. On some benchmarks, it achieves comparable or even better performance compared to state-of-the-art Video LLMs that are fine-tuned on video datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a training free method that converts an image MLLM into a video MLLM. This was achieved by simply concatenating features or frames in previous works. This paper proposes to concatenate features in a slow fast manner that combines a few high resolution feature maps with a large number of low resolution feature maps, which enabled LLM to see both local details and temporal context. The method SF-LLAVA achieves improved results on video MLLM benchmarks.

### Strengths
1. The proposed method is simple, intuitive, and efficient. It involves no training but obtains a video MLLM for free.
2. Ablations are performed extensively on multiple datasets and benchmarks, focusing on the optimal selection of the slow and fast resolutions.

### Weaknesses
1. Limited novelty compared with existing methods such as IG-VLM, or PLLaVA. It has been shown that simply concatenating frames (or frame features) gives a good MLLM without or with only a little training. On top of these existing works, it is straightforward to see or expect that a cleverer selection of feature such as adopting the SlowFast idea can work a little bit better.
2. Limited performance gain on top of the baselines such as IG-VLM, as shown in Table 2 (e.g. +1.1% on NextQA), as well as in the ablation, line 413, where adding the fast path improves marginally on top of the 12 frame slow only model.
3. It is less well justified to keep “training free” as a requirement. It is true that training free is a nice property but existing training-based methods such as pllava and VILA involve only a lightweight fine-tuning stage that initializes mostly from image (LLaVA) model and learns only a projector or arguably simply concept selection/merging layers.
4. Limited comparison with strong training based methods, such as VILA, and more comprehensive benchmarks such as MVBench or VideoMME. The benchmarks that are currently studied are either spatial biased (i.e. a 1-frame model can do quite well) or temporal-biased (EgoSchema that is based on high level semantics), rather than those that require both spatial and temporal reasoning.
5. It may be interesting to see the difference in the order of input tokens. The current model looks like a bag of words model with the LLM doing most of the heavy lifting. Does the order of the tokens really matter? Does the model really learn motion? Do the datasets require/measure motion? This may give more insights to the community, if the goal is not to push the best results on video benchmarks.

### Questions
1. Since SF-LLAVA does not require training, is it possible to compute features offline to save some memory and thus use a lot more tokens than those methods that compute vision features during inference? In this case, is it possible to show that SF-LLAVA can work as a general add-on to any model that improves inference for any model? e.g. trained on 4 frames but can infer on many more frames with SF-Model?
2. Does SF-LLaVA achieve good results on zero-shot generalization cases, compared with video trained methods such as pllava and vila? e.g. these methods are trained on specific datasets and therefore work well on those datasets that are similar to the training distribution, while SF-LLAVA works out of box and better on some datasets that are more different than the training sets of these existing papers.
3. Following the discussion on weakness #3, is it possible to apply SF-LLaVA on larger scale models where video training is less feasible such as a 70B/90B llama3 model? This may be a real advantage of training-free vs. training-based methods.

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
The paper proposes SlowFast-LLaVA (SF-LLaVA), a training-free video large language model (LLM) that can jointly capture detailed spatial semantics and long-range temporal context without exceeding the token budget of commonly used LLMs. This is achieved by using a two-stream SlowFast design of inputs, where the Slow pathway extracts features at a low frame rate while keeping spatial detail, and the Fast pathway operates on a high frame rate but uses a larger spatial pooling stride to focus on motion cues. Experimental results show that SF-LLaVA outperforms existing training-free methods on a wide range of video tasks, and achieves comparable or even better performance compared to state-of-the-art video LLMs that are fine-tuned on video datasets.

### Strengths
1. the proposed method to build video-llm is simple, novel, and the slowfast design to aggregate spatial and temportal information is reasonable.
2.the paper is in good writing for understanding, and ablation experiments to provide detailed results for the influential factors of the provided method.

### Weaknesses
1. video-mllms could not only do recgnition and captioning of a video, but also exploite the knowledge of LLM to do further recognition reseasoning. In order to comprehensively evaluate the proposed training-free method to build a video-mllm.

a. I suggest authors provide evaluations not only on captioning benchmarks, such as MSVD, MSR-VTT and so on, but also on benchmarks specifically for video-mllm, such as video-mme, mvbench, videovista, MLVU and so on, which could provide more comprehensive video-llm performance comparation, the evaluation resutls could provide important new insights about the model's performance.

2. the two-stream method is only applied on llava-next image-llm, if authors could give proof that this idea could be generalized to other image-llm models, the two-stream token aggregation design is more persuasive and thought-provoking for futher video-llm research. Here, I list some recent  image-llm models with structure different from llava, blip2(with q-former structure), internvl(with pixel shuffle structure), Ovis(Ovis: Structural Embedding Alignment for
 Multimodal Large Language Model, with visual embedding table), Aria（An Open Multimodal Native Mixture-of-Experts Model， with MoE structure）and suggest authors give test or theoretical analysis on these models.

3.Althogh training-free is a good feature for the method, a training-based model could gain a more powerful performance, just as  LLaVA-NeXT-Video-DPO is better than SF-LLaVA(Both built on LLaVA-NeXT-Image ).

a. I suggest authors discuss specific use cases or scenarios where a training-free approach might be preferable despite potentially lower performance. 

b. I also suggest authors elaborate on potential trade-offs between training-free and fine-tuned approaches in terms of factors like deployment flexibility, computational requirements, or ability to handle novel domains.

### Questions
questions are listed above

### Soundness
3

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
4

### Summary
This paper presents SF-LLaVA, a training-free video LLM that requires no additional fine-tuning to work for various video tasks.  Technically, the authors propose a SlowFast design of inputs for Video LLMs to capture both detailed spatial semantics and long-range temporal context, which is a simple and effective approach. The experiments on 3 video tasks with 8 benchmarks demonstrate the effectiveness and superiority of SF-LLaVA compared to training-free and SFT methods. Comprehensive ablation studies provide valuable insights for future research.

### Strengths
+ The motivation for enabling LLMs to understand video inputs through a training-free approach is reasonable. 

+ The paper is easy to read and well-structured.

+ Experiments on a diverse set of 8 video benchmarks demonstrate the effectiveness of SF-LLaVA.

### Weaknesses
 - Experiments were conducted only on LLaVA-NeXT (despite including 7B and 34B models), with no additional results from other open-source LLMs provided.


- The quantitative results in Figure 5 lack the results without the SlowFast design.

### Questions
-  Can the proposed method work for particularly long video understanding, such as LVBench[1]?

-  The paper indicates that it lacks the capability to detect the precise start and end times. Can fine-grained frame-level textual descriptions be introduced to enhance the spatio-temporal understanding of videos?

### Soundness
2

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
4

### Summary
Inspired by the idea of two stream networks in action recognition, this paper introduces a really simple sampling scheme of the frames and spatial pooling for training free evaluation of image LLM on videos. They show consistent improvements over the baseline on many tasks.

### Strengths
The idea is extremely simple (which is a good thing) and battle tested in action recognition.

The evaluations and ablations seem comprehensive and fair.

### Weaknesses
The paper suffers from excessive repetition. Given the simplicity of the core idea, it seems unnecessarily stretched to fill 10 pages and could be more concise. Additionally, table captions, such as in Table 1, lack added value; they simply reiterate the table content without providing further insights. Similarly, the experiment descriptions merely repeat the accuracy values from the tables, without offering additional intuition or interpretation.

Furthermore, the prompt aspect could be explored in greater depth, as it represents an additional axis to consider in zero-shot adaptation of vision-based large language models (LLMs) for videos.

### Questions
It seems that the prompt aspect in zero-shot adaptation could add substantial value if further explored. Have you considered additional prompt engineering or variations in the prompts to evaluate their impact on the model’s performance?

### Soundness
3

### Presentation
2

### Contribution
3
