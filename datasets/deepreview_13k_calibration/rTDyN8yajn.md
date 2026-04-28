# Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 8, 6, 5, 5

## Abstract
Recent studies have demonstrated Large Language Models (LLMs) can extend their zero-shot generalization capabilities to multimodal learning through instruction tuning.
As more modalities and downstream tasks are introduced, negative conflicts and interference may have a worse impact on performance. 
While this phenomenon has been overlooked in previous work, we propose a novel and extensible framework, called \mname, for comprehensive studies and experimentation on multimodal learning with Multimodal Large Language Models (MLLMs).
Specifically, we combine the well-known Mixture-of-Experts (MoE) and one of the representative PEFT techniques, \emph{i.e.,} LoRA, designing a novel LLM-based decoder, called {\dec}, for multimodal learning.
To the best of our knowledge, we are one of the pioneering efforts to introduce MoE into MLLMs to address this problem.
The experimental results (about 20\% improvement) have shown the effectiveness and versatility of our design in various 2D and 3D downstream tasks.
Code and datasets are available at \href{https://openlamm.io/paper_list/Octavius}{\texttt{https://openlamm.io/paper\_list/Octavius}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use a combination of MoE with the LoRA technique to address the challenge of incorporating additional tasks in the MLLM. The MoE components are chosen using a sparsely gating network. The outcomes demonstrate the efficacy of this approach.

### Strengths
This method is straightforward but powerful, capable of integrating numerous vision tasks within this framework. Its adaptability is showcased as it seamlessly operates with both 2D images and 3D point clouds. Ultimately, the integration of LoRA with MoE for PEFT proves to be highly efficient.

### Weaknesses
Given our awareness of each example's task, an important baseline involves employing a dedicated LoRA for each task individually. Additionally, conducting an ablation study on the impact of top-k would be informative.

### Questions
How can you attain top-2 sparsity gates while ensuring compatibility with gradient flow?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper mainly introduced 1) LoRA-MoE (Mixture-of-Experts) decoder to mitigate tug-of-war (interference) problem between different tasks/modalities, and 2) point cloud encoder called Object-As-Scene to extract language-aligned scene-level 3D features. 
Experiments on both 2D and 3D tasks show LoRA-MoE improves performance by ~20% over strong baselines like LAMM and LLaVA-LoRA. The model is also verified on multimodal learning with both images and point clouds.

### Strengths
- The idea of MoE with sample routing to mitigate task interference for MLLMs is novel.
- The author conducted thorough experiments to validate the framework on a diverse set of 2D and 3D tasks. The gains are substantial.
- The framework is modular and extensible to incorporate more modalities and tasks.

### Weaknesses
 - There is no analysis on how the routing among experts actually works. It would be great if the authors can provide some qualitative study of the predictions from sample-based gating network as responses to the input task, to show how the routing mechanism work. I wonder whether the gating network will simply act like a task classifier, or it's not the case.
- The scaling behavior as more modalities and tasks are added is not studied. There may be limitations in very high multi-task settings.

### Questions
- Can you show some qualitative study of the predictions from the sample-based gating network as responses to the input task? It can help us understand how network routing works.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper contributes a method for mitigating task interference in instruction tuning by learning LoRA-based Mixture-of-Experts. By using a sparse gate routing scheme, different LoRA experts can learn task- and modality-specific knowledge. In experiments, they do instruction tuning for MLLMs on both 2D image tasks and 3D point cloud tasks, each having individual vision encoders.

### Strengths
- The paper is well-motivated -- MoEs have been shown to be useful for distributing the different types of knowledge that are required for multi-task learning, and VL instruction tuning is a good application of this insight.

- The experiments are performed on both 2D image and 3D point cloud tasks, both individually and with the two datasets combined.

### Weaknesses
 - I am primarily concerned by the analysis in Figure 5 -- it seems that all the 2D tasks are using only two experts! This makes me skeptical about the utility of MoE at all.  Could you run the ablation in Table 5 with 2 experts? so these two experts will get selected each time and there in routing involved, but the model has the capacity to learn with 2 LoRAs at once instead of one (which is what it seems to be doing in Fig5)

- An additional analysis that is needed is how the gate routing is distributed between 2D and 3D tasks, for the model that is trained on the combined LAMMv2+ScanNet instruction tuning dataset.

Given the result in Figure 5, I am not convinced about the utility of MoE with routing, when it doesn't seem that different experts are even used.

- I am not sure what the non-MoE baseline in Tables 2-3 is -- is it merely training the frozen model minus the LoRA parameters?

### Questions
- What is the actual LLM decoder that you use? it's never mentioned throughout the paper.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Observing the tug-of-war problem between 2D detection and VQA, this paper proposes a Mixture-of-Expert (MoE) style architecture with LoRA for efficient optimization of multi-modality and multi-task. To further support 3D instruction-following tasks, the authors propose a novel point cloud encoding architecture called Object-as-scene. The simple yet effective architecture demonstrate strong experimental performance.

### Strengths
- This paper constructs Octavius by collecting better detection annotation, combing multiple modality data and propose a novel MoE architecture.
- The authors provide a throughout discussion between related works.
- The proposed method is relatively simple but with strong performance.

### Weaknesses
 - About the tug-of-war problem:
  - The authors demonstrate the existence of this problem simply by optimization 2D detection and VQA simultaneously.
  - Considering the authors also include multi-modality, it would be better to include preliminary also in this direction (e.g., 2D & 3D captioning).
- About the router input:
  - As shown in Fig. 2, the input consists of the system prompt, modality embedding and the question embedding, which contradicts wit Tab. 5.  Would you mind clarifying how exactly to construct the router input?
  - Also how to get the question embedding? Do you utilize other embedding model or just do that on-the-fly?

- About the MoE deployment:
  - Do you adopt LoRA-MoE in each Transformer block?
  - Do you adopt LoRA only for the MLP, similarly with the original MoE?
- About zero-shot evaluation:
  - According to Sec. 4.1, the zero-shot evaluation conducted in this paper is only about zero-shot evaluation on novel datasets of the training tasks (e.g., ScienceQA for evaluation and VQA for training).
  - Therefore, I wonder how it works if you have not seen any QA tasks during training, since it is difficult to understand a specialized architecture like MoE can generalize well to totally unseen tasks during pre-training.
  - Moreover, if you still train with VQA, but change the prompt template of ScienceQA during testing, will the MoE router be robust to this kind of OoD generalization?
- Overall, I think this is an interesting paper, but still with some problems to convince me about the effectiveness of the proposed method. I would consider increasing the score if my questions are well addressed.

- Implementation details:
  - In Fig. 5, do you select a single layer to do the visualization or take an average of all layers?
  - In Tab. 6, the authors claim that loading balancing loss has negative effect. Do you use loading balancing afterwards? If not, how would we prevent the MoE architecture from collapsing to always using a single expert?
  - The 2D results in Tab. 4 have a significant performance gap with state-of-the-art VLLM like InstructBLIP (e.g., ScienceQA and Flickr30K captioning).
  - The authors should have utilized stronger baseline methods. There is a significant performance gap between LAMN and state-of-the-art methods including InstructBLIP and Shikra.

### Questions
- Implementation details:
  - In Fig. 5, do you select a single layer to do the visualization or take an average of all layers?
  - In Tab. 6, the authors claim that loading balancing loss has negative effect. Do you use loading balancing afterwards? If not, how would we prevent the MoE architecture from collapsing to always using a single expert?
  - The 2D results in Tab. 4 have a significant performance gap with state-of-the-art VLLM like InstructBLIP (e.g., ScienceQA and Flickr30K captioning).
  - The authors should have utilized stronger baseline methods. There is a significant performance gap between LAMN and state-of-the-art methods including InstructBLIP and Shikra.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The work proposes a multimodal LoRA-MoE decoder for task- and modality-specific learning. The experimental results (about 20% improvement) have shown the effectiveness and versatility of our design in various 2D and 3D downstream tasks.

### Strengths
1. The work adopts a simple but effective gate routing scheme allowing sparsely-activated LoRA modules to learn task- and modality-specific knowledge as an independent expert. 
2. The work can address various 2D/3D vision and language tasks, and conduct various experiments to validate the effectiveness and versatility with a few trainable parameters.

### Weaknesses
1. The work focuses on SFT, whether it can be generalized to pre-training on massive data.
2. Lack of evaluation on some of the latest MLLM Chat evaluation, such as MMBench, MME, SEED-Bench, etc.
3. Lack of comparison with some classic and latest methods, such as MiniGPT4, mPLUG-Owl, LLAVA-1.5, Qianwen-VL, etc.


### Questions
1. In Figure 5, Loras2 has a probability of 0 on 6 tasks. What could be the possible reasons for this phenomenon? Could you provide more visualizations of experts and provide some insightful analysis?
2. Can you analyze the impact of k in the top-k sparse gate?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
