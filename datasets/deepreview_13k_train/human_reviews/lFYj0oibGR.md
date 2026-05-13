# Vision-Language Foundation Models as Effective Robot Imitators

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation.
We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data.
To this end, we derive a simple and novel vision-language manipulation framework, dubbed \our, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, \our{} utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets.
Such a decomposition provides \our{} the flexibility for open-loop control and deployment on low-performance platforms.
By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show that \our{} can be an effective and competitive alternative to adapt VLMs to robot control.
Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks.
\our{} can be trained or evaluated on a single GPU server, and we believe it has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy. 
Codes and models will be public.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- Proposes RoboFlamingo, a framework for adapting large vision-language models (VLMs) like OpenFlamingo to robot manipulation policies.
- Achieves state-of-the-art performance on the CALVIN benchmark by fine-tuning VLMs with only a small amount of robotic demonstration data.
- Shows VLMs can enable effective vision-language comprehension and long-horizon planning for robot control when combined with a simple policy head, while demonstrating strong generalization ability to unseen tasks and environments. Comprehensive analysis and ablation studies on using VLMs for robotic manipulation are conducted.

### Strengths
- RoboFlamingo outperforms considerably prior methods on CALVIN
- Requires much less data and compute than methods like RT-2 that co-train on extensive internet-scal data.
- Decouples perception and policy to enable flexibility like open-loop control, while maintaining relatively strong zero-shot generalization ability.

### Weaknesses
 - Relies on simulated robot environment, may be challenging to transfer to real world.
- The evaluation is limited to a single simulated benchmark environment (CALVIN). Testing on more diverse robotic platforms and tasks in simulation could help validate the generalizability of the method. The CALVIN benchmark, while useful, may not fully capture the complexities of real-world robotic manipulation scenarios, particularly in terms of variations in object properties, lighting conditions, and sensor noise.
- Less sample efficient than methods leveraging offline robot data like MCIL.

### Questions
- What steps would be needed to transfer RoboFlamingo to real robotic systems? How realistic are the CALVIN simulations?
- Is there scope to incorporate offline robotic data to improve sample efficiency?
- Experiments are with visual and language modalities. Robotic manipulation often relies on additional sensing (e.g. force, tactile). How can RoboFlamingo incorporate other modalities?
- How flexible is the decoupled design? Will it be possible to incorporating RoboFlamingo into hierarchical frameworks like in PaLM-E?
- How does the computational overhead of RoboFlamingo compare to other VLM-based methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces RoboFlamingo, a language-conditioned manipulation method that finetunes an open-source VLM OpenFlamingo to output low-level robot control actions. The method builds upon the pre-trained and frozen OpenFlamingo Transformer backbone: 1) adds an LSTM policy head after the pooled visual-language embedding output from the OpenFlamingo backbone, 2) adds first-person and third-person camera image tokens to the ViT for the Resampler. Following the OpenFlamingo finetuning procedure, the ViT, Tokenizer, and Self-Attention Layers of the backbone are frozen during training; only the resampler, cross-attention, and policy head parameters are updated during finetuning on robot imitation learning datasets. In evaluations, RoboFlamingo is evaluated on: 1) in-distribution training performance and out-of-distribution generalization on the CALVIN benchmark where it achieves SOTA over HULC and RT-1, 2) ablations that show history based policy heads (GPT and LSTM) outperform MLPs, vision-language pretraining is critical for good performance, and 3) larger models and instruction finetuned base models performing better. The authors commit to releasing code upon acceptance.

### Strengths
- The motivation is clear for a low-cost alternative solution to large closed Vision Language Action models (VLAs) like RT-2, which motivate this work. The study which incorporates open-source design components like the different LLMs of various architectures and sizes in OpenFlamingo is a great contribution to the open-sourced community as well.
- The results on CALVIN, a well established and difficult robot control and generalization benchmark, are very compelling
- Open loop results are intriguing for pragmatic on-robot deployment
- The presentation is largely very easy to follow and a pleasure to read

### Weaknesses
 - Other ways of incorporating VL pre-training are not considered, such as utilizing VL representations like R3M or VOLTRON or MVP. These baselines are relevant given the frozen-backbone + robot finetuning setup in RoboFlamingo. Essentially, a baseline should study different ways of incorporating "web data", which the current baselines do not study.
- A core claim of RT-2 was the benefit of co-fine-tuning on robotics data in addition to the original VL data. This core claim is not studied in RoboFlamingo.
- Another claim of RT-2 was measuring the transfer of internet knowledge to robotics, in addition to in-domain performance. This seems like a major benefit of utilizing VLMs for robotics generalization. However, this is not studied in this work; the setting in the ABC => D CALVIN environment seems insufficient to measure how much transfer is occuring from internet-scale VL pre-training to robotics. 
- Another claim of RT-2 was the benefit of mixing robot action tokens explicitly with VL tokens. In contrast, RoboFlamingo introduces a new policy head that directly only predicts action tokens. It would be interesting to compare an explicit action-only policy head with the multi-modal output token prediction setting in RT-2.
- The presentation can be improved a bit in Section 4.2.1 and 4.2.2, where the notation is unwieldy. For example, the notation of $K$ is overloaded.
- Writing nits:
    - Section 2: "models to encoder" => "models to encode", "train the policy" => "training the policy", "utilizing robot manipulation data both the web data" => "utilizing both robot manipulation data and web data", "We hope RoboFlamingo provide" => "We hope RoboFlamingo provides"
    - Section 4: "Particularlly" => "Particularly", "look into one" => "looks into one", "and take its" => "and takes its"
    - Section 5: "We wonder" => "We study", "24 thousand trajectories" => weird ~ added
    - Section 5.4.1: "single-frame observation" => "single-frame observations"

### Questions
- Clarifications to my concerns above would be appreciated.
- Will checkpoints be released as well?
- How does performance on pre-training tasks change during finetuning? That is, is there catastrophic forgetting occurring, where the base foundation capabilities are lost?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the RoboFlamingo architecture for effective language-conditioned robot manipulation task learning through behavior cloning. Specifically, the paper shows that by initiating model weights from pretrained VLMs and finetuning them in the OpenFlamingo-style using a minimal amount of downstream robot manipulation data, the policy can achieve good performance on the CALVIN benchmark for both seen task and unseen task variations. Such performance also outperforms previous baselines like RT-1. The authors further provide ablations on the effect of different backbone scales, different architectures, and training paradigms on agent performance.

### Strengths
- The authors agree to open-source their code and implementations, which I really appreciate. This will greatly facilitate efforts to scale up foundation model training for robotic manipulation tasks.
- The ablation section is very helpful for readers to understand the critical components of the proposed RoboFlamingo architecture.
- RoboFlamingo significantly outperforms prior baselines like RT-1 on the CALVIN benchmark.

### Weaknesses
Firstly, the presentation of the paper can be improved, and some parts of the method are unclear, which hinders reader's understanding.
- According to Section 4.2.2, the finetuned language model backbone will output a fused vision-language representation $X_t^L=\{x_{t,1}^L,\dots, x_{t,M}^L\}$ for *each* time step $t \in [1...T]$, where $M$ is the length of the input language instruction $l$. To produce such outputs, it seems necessary that the same language instruction needs to be tiled $T$ times and fed into the language model for a sequence of $T$ images. However, such detail is not illustrated in Figure 2, and Figure 2 only illustrates the model behavior when $T=1$. It would be a lot more helpful if Figure 2 illustrates model behavior when $T>1$. Specifically, how are the temporal dynamics of the input sequence handled when generating these fused representations across multiple timesteps? A more detailed diagram illustrating the information flow across timesteps would greatly enhance clarity.
- Sec. 5.4.2 of the ablation study shows that "loading the pre-trained parameters of the cross-attention layers" is crucial for model performance. However, it is unclear from which model these cross-attention layer weights are being loaded. The source of these pretrained weights should be explicitly stated. Additionally, the rationale for not loading the perceiver resampler weights from a pretrained model is not provided. Given the importance of the cross-attention layers, it seems reasonable to assume that the perceiver resampler might also benefit from pretrained weights. A justification for this design choice should be included. Furthermore, the methodology section lacks a description of the design to load pretrained cross-attention weights. This design decision should be clearly outlined in the methodology section to ensure reproducibility.
- In Section 5.4.3, the setup for the "instruction fine-tuning" experiment is not clearly defined. What specific instructions and datasets were used for this fine-tuning process? Additionally, the methodology section does not describe the instruction finetuning designs. A detailed description of the instruction finetuning procedure, including the datasets and instructions used, should be provided in the methodology section.

Secondly, authors choose to only train RoboFlamingo on the CALVIN benchmark throughout the paper. Even though authors claim that they want to showcase RoboFlamingo's ability to produce good language-conditioned manipulation policies given a small amount of finetune data, I'm afraid that by only finetuning on the CALVIN benchmark, the model overfits to the dataset and loses some crucial abilities like spatial reasoning and object relation understanding (which may be crucial for other robot manipulation tasks that are not present in the CALVIN benchmark). By training RoboFlamingo on a mixture of downstream robot datasets and large-scale datasets used to pretrain e.g., OpenFlamingo, InstructBLIP, IDEFICS, LLaVA, authors might alleviate such phenomenon, and even improve upon the CALVIN benchmark performance they achieved in this paper. Therefore, I do not quite agree with the author's claim that "only a minimal amount of data is required to adapt the model to downstream manipulation tasks". The claim that "only a minimal amount of data is required" seems premature without exploring the impact of training on a more diverse dataset.

### Questions
Page 3: `Compared to other works, the controlling policies do not require any ability to understand instructions, but rely on the pre-trained frozen LLM to select necessary skills.`. This sentence is inaccurate. The author's proposed approach still need to understand language instructions as the LLM backbone still needs to fuse language representations with visual input representations. I believe the authors' actual meaning is that the policy head does not explicitly take language instructions as input.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper uses a VLM as a backbone for visual imitation learning of language-conditioned policies. In contrast to prior work, it builds on open-source VLMs and limits the number of finetuned parameters to make VLM-policy training feasible for conventional compute budgets. They demonstrate that the VLM backbone leads to superior imitation performance on the CALVIN simulated robotic manipulation benchmark and compare a few different design choices.

### Strengths
Using VLM backbones for policy learning is a promising direction for robot learning, but prior work was confined to proprietary models and required large compute for policy training. This work's focus on open-source models and parameter-efficient finetuning brings those models within the reach of academic compute budgets and thus is very valuable. The demonstrated results on the CALVIN benchmark are strong and support the claim that pre-trained VLM backbones are good features for imitation learning.

I appreciate that the authors analyzed several of the design decisions experimentally and showed which choices have a larger influence on final performance. Particularly the results in Table 3 are interesting in that they show that larger VLM backbones are particularly beneficial in a low-data regime. I also appreciated the separate investigation of generalizability in the visual domain and to diverse language instructions.

The paper is easy to follow and most of the experiments are easily understandable.

### Weaknesses
A main selling point of the paper is that it claims the introduced method can forego expensive co-finetuning by restricting the number of finetuned weights and freezing most of the VLM weights. However, if I understand correctly, the paper finetunes all weights that were also finetuned in the Flamingo VLM grounding stage, i.e. like Flamingo they froze the vision and language model features, but finetuned all cross-attention features that perform the vision-to-language grounding (and Fig 3b shows that this is crucial). This however suggest that the model may still forget most of the knowledge obtained in the VLM pretraining stage, ie the OpenFlamingo training. The experimental section of the paper lacks comparison to (A) co-training with the current parameter-freezing scheme, (B) full model finetuning w/ and w/o co-training to support the claim that their partial finetuning scheme is actually key to enable good performance without co-finetuning.

Another comparison that would be good to add is to a simpler, pre-trained visual representation, like VC-1, Voltron etc. These models also use internet data to train good representations for imitation learning, but are arguably easier to use than the billion-parameter scale models introduced here, so it would be good to experimentally show the benefits.

One notable difference to prior work is that instead of predicting actions as tokens in the VLM's output vocabulary, the proposed method trains a separate action head. It would be good to analyze this choice and compare to directly outputting actions as "text tokens".

Since the paper is mainly an empirical study, it would be good to evaluate the policy on more than one environment, e.g. the IKEA Furniture assembly environment could be a nice and challenging testbed with ~ photorealistic rendering.

The paper also lacks details on the computational requirements for training policies with the VLM backbones (required GPU + training time), which seems crucial given the focus on making VLM policies more accessible.

Finally, Section 5.5 on open-loop execution lacks some detail on what exactly was tried, so I was a bit confused about these experimental results (see questions below).

### Questions
- for the enriched language evaluations, the authors mention that they sample language instruction synonyms randomly from the GPT-4 generations -- did you ensure that all methods are evaluated on the same randomly sampled set of instructions to make the comparison fair?

- can you explain in more detail the experiment on open-loop execution in Section 5.5? How can you open-loop execute the policy without re-training?


## Review Summary

Overall I think this paper is an interesting contribution to democratizing the access to large vision language models for policy learning. I believe that many in the community will be interested in this and thus recommend acceptance. However, the empirical analysis in the paper could be significantly improved by addressing the points raised above. Concretely, the authors can:
- add details about the required compute
- add comparison to co-finetuning and full model finetuning
- add comparison to other pre-trained representations
- add evaluations on at least one additional environment

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
