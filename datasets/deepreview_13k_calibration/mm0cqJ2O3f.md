# Ready-to-React: Online Reaction Policy for Two-Character Interaction Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
This paper addresses the task of generating two-character online interactions. Previously, two main settings existed for two-character interaction generation: (1) generating one's motions based on the counterpart's complete motion sequence, and (2) jointly generating two-character motions based on specific conditions. We argue that these settings fail to model the process of real-life two-character interactions, where humans will react to their counterparts in real time and act as independent individuals. In contrast, we propose an online reaction policy, called Ready-to-React, to generate the next character pose based on past observed motions. Each character has its own reaction policy as its ``brain'', enabling them to interact like real humans in a streaming manner. Our policy is implemented by incorporating a diffusion head into an auto-regressive model, which can dynamically respond to the counterpart's motions while effectively mitigating the error accumulation throughout the generation process. We conduct comprehensive experiments using the challenging boxing task. Experimental results demonstrate that our method outperforms existing baselines and can generate extended motion sequences. Additionally, we show that our approach can be controlled by sparse signals, making it well-suited for VR and other online interactive environments. Code and data will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a new two-person boxing dataset to support three tasks: (1) reactive motion generation, (2) two-character interaction generation, and (3) long-term two-character interaction generation. The authors demonstrate that their method can generate motions lasting over one minute and outperforms existing methods across various tasks. Interestingly, the authors verify that their approach can be used in VR scenarios.

### Strengths
1. The proposed DuoBox dataset is a strong dataset for two-person interaction, which is highly beneficial to the community. It provides a new test benchmark for three novel tasks.

2. The method proposed in the paper can generate impressive results, significantly outperforming GPT-based methods and capable of generating longer action sequences.

### Weaknesses
1. Given that there is not much actual contact between individuals in this scenario, with contact occurring only at specific moments, have the authors analyzed how the occurrence of such contact influences subsequent motion generation?

2. Since the visualizations provided by the authors seem to be based on some kind of simulation environment, have the authors quantified metrics such as penetration (clipping) or foot sliding to assess the physical plausibility of the generated results?

### Questions
This paper investigates a very interesting problem. However, the paper does not consider the modeling of contact information during two-person interactions, which seems to limit its application in real robots. Nevertheless, the authors demonstrate the potential of their approach in VR applications. Overall, I have given my current score based on these considerations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes an autoregressive diffusion model to generate motion for human boxing matches. The main innovation lies in an autoregressive policy that handles both the human actor's and opponent's policy concurrently, ensuring there is an "action" and "reaction" aspect for each player. To train the proposed method, a new dataset, DuoBox, is collected. Results show that the proposed method can generate long and realistic boxing motions.

### Strengths
- This work addresses an important problem in two-person interaction motion generation: handling interaction. The proposed autoregressive approach is sound and intuitive.
- The proposed online motion decoder is a well-thought-out solution for applying VQ-VAE styled motion representation in the autoregressive motion generation scheme.
- The special focus on root orientation prediction is crucial for the boxing task, based on the ablation.
- The generated motion is of high quality and visually pleasing. Quantitative results also show that the generated motion is of high quality and outperforms prior arts.
- The study on sparse VR input is a welcome addition, showcasing the method's applicability in animation.

### Weaknesses
 - At video 0:45 (of the gray box), it is clear that the reaction of the other character can contain large penetration and unrealistic interaction. These should be properly handled. In fact, from watching the video, I would say that while the motion quality of the two characters is high, the "reaction" part is not well-demonstrated. There are many cases where punches are thrown, but the opponent does not evade and has no discernible reaction.
- I feel that given the study's scope, the title should reflect the focus on "boxing". Many proposed techniques (such as root orientation) focus on boxing. Extending to two-person sports (fencing, dancing, etc.) could be an interesting direction, but the proposed method has not been shown to handle generic two-person interactions.

### Questions
Does the model generalize beyond boxing? There have been several two-person interaction datasets proposed (e.g., [1]).
[1] Xu, Liang, et al. "Inter-x: Towards versatile human-human interaction analysis." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2024.

### Soundness
3

### Presentation
3

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
The paper present a new method for human reactive motion generation. The method contains a history encoder to encode historic motion using VQ-VAE or MLP, a latent predictor using Transformer encoder and diffusion and a latent decoder using Transformer decoder. The proposed architecture can be use for reactive motion generation but also for two persons interaction generation and support long term generation (1800 frames). The proposed method outperforms the state of the art quantitatively and qualitatively on a new boxing dataset containing more than 1 hour of 3D motions.

### Strengths
- The method is relatively simple yet performs very well and is very versatile as it can be used for reactive motion generation but also for two persons interaction generation.

- The method is efficient even for long term generation.

- The paper presents extensive experiments and ablation.

- The authors propose a new interaction (boxing) dataset with long sequence. This is very welcome due the the scarcity of long interaction datasets.

- The authors provided qualitative results in video format.

### Weaknesses
 - The experiments are performed on only one dataset and this dataset is the new one proposed in the paper. It would have been better to also have experiment on another dataset e.g one of those used for Duolando or Interformer.

- The paper does not precise if the dataset will be released to the public.

- While I understood the reasoning behind using diffusion with MLP for the latent predictor, I am surprised that it works so well with only a single layer. What was the intuition behind the choice of this single layer MLP, did the authors try other configurations for the denoising network ? This would have been interesting to explore this more in details.

- A few things are still not clear to me in the methodology:

    - Line 176: what is the reasoning behind the exclusion of the y-axis when extracting r_off and r_dir?

    - Why does the opponent input doesn't contain r_off and r_dir when the agent input uses them?

    - Also on the subject of differences between agent and opponent, why use a VQ-VAE for the AGENT but a MLP for the opponent?

    - How does the two-character motion generation works exactly? Does this work in a auto-regressive manner? i.e. generate agent motion T -> generate opponent motion T+1 -> generate agent motion T+1->... . Does it need two separately trained networks (one for agent and one for opponent) or only one ? More details are necessary.

- For the two-character motion generation experiments the authors do not compare with Duolando. This is understandable since it was build to generate the motion of only one person in an interaction. However this seems to also be the case for Interformer yet the authors were able to compare against it. Were some modifications done to the network architecture or to the training/inference protocol to make it possible? this should be clarified.

- In figure 2 "Tranformer" is used in both the latent predictor and the motion decoder. from what I understood of the text there is only a Transformer encoder in the latent predictor and a transformer decoder in the motion predictor. If it is the case the authors should update the figure to reflect this. Using the term "Transformer" alone make it seems it contains both encoder and decoder.

- Notation error: "d" is used both for the down-sampling factor (line 198) and for the initial number of frame (line 248)

### Questions
- In figure 2 "Tranformer" is used in both the latent predictor and the motion decoder. from what I understood of the text there is only a Transformer encoder in the latent predictor and a transformer decoder in the motion predictor. If it is the case the authors should update the figure to reflect this. Using the term "Transformer" alone make it seems it contains both encoder and decoder.

- Notation error: "d" is used both for the down-sampling factor (line 198) and for the initial number of frame (line 248)

### Soundness
3

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
3

### Summary
This paper introduces a novel approach to generating real-time interactions between two characters. The proposed "Ready-to-React" method focuses on creating dynamic, continuous motions for each character based on their counterpart’s actions. The key innovation lies in incorporating a diffusion head into an auto-regressive model, which helps mitigate error accumulation and improves the naturalness of long-term interactions. The approach is demonstrated on a boxing task, where it outperforms existing methods in generating coherent and plausible interactions over extended sequences. This technique has potential applications in VR and online interactive environments.

### Strengths
1. Experimental adequacy: The experimental result is persuasive compared with existing baselines and ablation studies are sufficient to prove the effectiveness of the proposed method.
2. The insight into error accumulation mitigation in two-character motion generation is interesting.

### Weaknesses
1. Lack of significance: The background of this work is too narrow and I do not think it is important to study. Also, from my perspective, this method is for interaction generation. However, there has been much work studying video generation which seems to be a lot more complicated than this paper. 
2. Lack of novelty: The proposed method simply uses diffusion to generate representations instead of directly generating actions which is lack of novelty and contribution. 
3. This method is only tested in one dataset which is not sufficient although you mention this scene is a difficult one.

### Questions
1. You mention in the introduction that "incorporating a diffusion head into an auto-regressive model, which can respond to the counterpart’s motions in a streaming manner while ensuring the naturalness and diversity of the motions". How can this method help diversity?
2. Can you use a few baselines that are not deep learning, such as those executed by programmed programs? Because in this scene (such as ), I think pre-programmed is quite smooth.

### Soundness
3

### Presentation
3

### Contribution
3
