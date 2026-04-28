# Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Recent popularity of Large Language Models (LLMs) has opened countless possibilities in automating numerous AI tasks by connecting LLMs to various domain-specific models or APIs, where LLMs serve as dispatchers while domain-specific models or APIs are action executors. Despite the vast numbers of domain-specific models/APIs, they still struggle to comprehensively cover super diverse automation demands in the interaction between human and User Interfaces (UIs). In this work, we build a multimodal model to ground natural language instructions in given UI screenshots as a generic UI task automation executor. This metadata-free grounding model, consisting of a visual encoder and a language decoder, is first pretrained on well studied document understanding tasks and then learns to decode spatial information from UI screenshots in a promptable way. To facilitate the exploitation of image-to-text pretrained knowledge, we follow the \textit{pixel-to-sequence} paradigm to predict geometric coordinates in a sequence of tokens using a language decoder. We further propose an innovative Reinforcement Learning (RL) based algorithm to supervise the tokens in such sequence jointly with visually semantic metrics, which effectively strengthens the spatial decoding capability of the \textit{pixel-to-sequence} paradigm. Extensive experiments demonstrate our proposed reinforced UI instruction grounding model outperforms the state-of-the-art methods by a clear margin and shows the potential as a generic UI task automation API.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel Reinforced Instruction Visual Grounding (RIVG) model for automating UI tasks using LLMs. Following Pix2Seq, the RIVG model is built upon a multimodal architecture consisting of a visual encoder and a language decoder, which is pretrained on document understanding tasks and then fine-tuned for decoding spatial information from UI screenshots. The authors argue the limitation of the pixel-to-sequence paradigm, where the loss is not optimized towards the "combinational semantics", e.g. a bounding box prediction of <bbox><x1><x2><y1><y2></bbox>, the current loss implementation is treating each token separately instead of the bounding box coordinates as a whole. The authors propose a reinforcement learning-based algorithm that jointly supervises tokens in the sequence with visually semantic metrics, effectively enhancing the spatial decoding capability. Extensive experiments demonstrate that the RIVG model outperforms state-of-the-art methods and has the potential to serve as a generic UI task automation API.

### Strengths
- The use of reinforcement learning and policy gradients for optimizing directly towards the IoU metric is an interesting and novel approach.
- The motivation for the awareness of the combinational semantics is intriguing and addresses a limitation in the pixel-to-sequence paradigm.

### Weaknesses
 - It is unclear if the benefit of the reward loss is due to the lack of model capacity in the LLM or if it would scale with the model size (e.g. LLaMA-2) and the model knowledge (e.g. more training data). It is nice that the authors conduct the scaling experiments in Table 6, but it is not necessarily at the scale of the recent large language models and has not undergone large-scale pretraining. Despite LLMs use the same loss at token level, which also has the "combinational semantics" issue, they are able to achieve complex reasoning capabilities as they scale up. This raises a concern that the proposed method might not be as impactful when applied to larger, more capable models. The experiments should have included a more thorough analysis of the model's performance with varying model sizes and pretraining regimes, especially given the current trend of scaling up LLMs. The current experiments do not sufficiently isolate the effect of the proposed reward loss from the effect of model capacity and pretraining data.


### Questions
- How do you compare the original Pix2Seq model, and the recent instruction-tuned multimodal models like LLaVA [1]? Can we think of them as Pix(image)2Seq(language)? -- bounding box outputs is a special case. If LLaVA is finetuned to (1) understand the text; (2) predict the bounding box for objects using datasets like COCO, would the proposed approach still be beneficial compared with SFT on these datasets? Given that this is a concurrent work, I am putting this in the questions section instead of a weakness.

[1] Liu et al. Visual instruction tuning. NeurIPS 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of automating User Interface (UI) tasks through natural language instructions. The authors introduce a multimodal grounding model without the need of metadata information. This model, consisting of a visual encoder and a language decoder, is pretrained on document understanding tasks and subsequently trained to decode spatial information from UI screenshots. By adopting a "pixel-to-sequence" approach, it predicts geometric coordinates as a sequence of tokens. Furthermore, the authors propose a novel Reinforcement Learning-based algorithm using policy gradients. This algorithm supervises tokens jointly in a sequence, thereby enhancing spatial decoding capabilities. Through extensive experiments, it's shown that this Reinforced UI instruction Grounding (RUIG) model outperforms existing methods and holds promise as a comprehensive UI task automation API.

### Strengths
- The proposed model requires only text instructions and screenshot images as inputs, without the need of UI metadata or additional information.
- A policy gradients-based approach is introduced to augment the pixel-to-sequence paradigm to be aware of combinational semantics.
- Various experiments have showcased the superior of the proposed method to surpass existing methods, even those that rely on UI metadata.

### Weaknesses
 - It is not very clear what is the key difference between the UI task and general object grounding tasks [1][2][3]? A follow-up question is that is the proposed reinforced learning method similar to [4] ?
- In my understanding, introducing Reinforcement Learning is the main contribution of this paper, instead of multimodal large language model, since a lot of papers have been proposed to use multimodal large language model to solve tasks during the past months. However, the authors only use half of the page to illustrate the reinforced pixel-to-sequence model. Is there no detailed introduction or well-curated design?
- In Section 4.3, when comparing with traditional grounding approaches, it is not surprising the traditional grounding approaches and UI-tailored grounding approaches are not good at understanding UI data, since their language models have less capacity than Large Language Models. Have the recently-proposed LLM-based multimodal models [5][6][7] been tested on UI data ?

### Questions
I really appreciate the analysis on the limitation of vanilla pixel-to-sequence and the insight on combinational semantics of (xmin, ymin, xmax, ymax). Although the authors propose a new training objective to improve it, I wonder whether it is enough. In other words, do we need to change the mechanism of decoded process, for example, from autoregressive to parallel decoding?
(I assume this is an open problem, and should not be considered as a weakness of this paper)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a UI instruction grounding model which is purely vision-based and requires no additional user-provided information about the UI. The task aims at locating an area in the UI screenshot (eg. a button) given a natural language instruction. To that end, the proposed model takes the UI screenshot and instruction as inputs to predict the geometric coordinates of the bounding box (coordinates of the top-left and bottom-right corners) as a sequence of tokens. To encourage the model’s optimisation by prediction accuracy of the complete bounding box rather than each independent coordinate value, the authors introduce the concept of “combinational semantics” to scale the loss of different coordinate tokens corresponding to the same bounding box according to its IoU with the ground-truth and update the model according to coordinates only instead of the whole sequence to be completed. Experiments were carried out on both mobile and desktop data, which demonstrates impressive improvements over existing UI instruction grounding models and verifies the effectiveness of the two proposed designs.

### Strengths
This paper is well-organised and well-motivated to build a purely vision-based UI instructing grounding model. The formulated algorithm is fairly original with a novel “combinational concept” introduced, which integrated coexisting relationships between tokens in addition to sequential relationships that are commonly adopted in causal language modelling. Experiments are somewhat sufficient to demonstrate the overall performance of the proposed method and the effectiveness of independent components.

### Weaknesses
I'm generally fine with this paper with just a few minor concerns:

The two learning objectives in Eq.2 and Eq.3 are used in parallel, but another straightforward idea is to combine the two and scale the losses for coordinate tokens by rewards. Will this work better?

Although the Monte Carlo sampling is commonly adopted in the RL community for computing the expectation value of rewards, I’d suggest the authors briefly describe its formulation or core ideas for the paper’s completeness.

Whilst the presentation of the overall ideas and model designs are clear, the paper still have some formatting issues that need to be addressed carefully:
+ broken references. In the second paragraph of the introduction “AI model (…) and APIs (…; ?)”
+ typos. At the paragraph above the experiments section “We estimation the expectation…”; “We evaluate the effectiveness  … on UI UI instruction grounding…”
+ In the paragraph at the end of Page 7, “As shown in Table 3, RUIG (all tokens)…” should it be Table 4?
+ In the first paragraph in Sec4.3, “As shown in Table 6…”, I found Table 6 in the appendix but it has nothing to do with the traditional baselines


### Questions
In Sec 3.1, the authors claim that some of the existing grounding methods require the bounding boxes of all UI elements as priors and that limits their generic use in practice. However, the proposed methods also need the coordinates of the bounding boxes as the labels for computing the rewards. In this case, what are the advantages of the proposed methods in terms of practice using? 

In the comparisons to existing methods in Table 5, why not use web data?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a reinforcement learning (RL) framework that utilizes the visual metric (such as IOUs) as the reward function to optimize an encoder-decoder policy network that generates token represented element bounding boxes for visual grounding, specifically in the web-UI domain. The framework is proposed to alleviate the issues of existing pixel-to-sequence works that cannot associate stronger and coherent geometrical information to their token optimization process.
The method is tested on mobile and desktop web UI datasets and performance gains were shown to justify their proposed method’s effectiveness.

### Strengths
- The proposed RL framework marries the benefits from both vision and language (token generation).
- The paper is easy to follow, and the method is well-motivated against existing works.
- The ablation studies on tokens to optimize is justifying for the proposed method.
- The tackled UI instruction grounding problem is an important task for modern generation AI agents.

### Weaknesses
 - The work is a bit over-claimed by stating that the framework does not require any additional information, while it indeed still requires the ground truth bounding boxes of the elements. This is misleading, as the standard expectation for a grounding task is to use ground truth bounding boxes during training and predict them during inference. The claim of 'no additional information' is only true during inference, which is not a novel aspect of the proposed method, but rather a standard practice in grounding tasks.
- More details on the baselines of existing grounding modules, such as GroundingDINO [1] and GLIP [2], are needed. I.e., how the inputs are handled, how the tasks are adapted for their settings, training details, etc. I’m a bit skeptical about the results being that much lower than the proposed module where after all they are all using the same amount of output supervisions for training. (Afterall, the author proposed method is also not benefiting much from non-provided metadata, such as OCRs, so that explanation is not convincing.) These grounding models may have been simply under-tuned. The core issue is that the baselines are not evaluated under the same conditions, specifically regarding pre-training. The performance gap may be due to the baselines not being optimized for the specific characteristics of UI data, rather than an inherent limitation of the models themselves. The lack of a fair comparison makes it difficult to assess the true contribution of the proposed method.
- Following up on the previous point, the proposed method adopts pre-trained weights from document understanding tasks that the conventional grounding modules do not have access to. A more fair comparison is to pre-train these grounding modules at least with these document understanding data (perhaps only regressing the boxes of texts and/or contents, the actual text recognition is not so important), as their pre-training domains are far from these structural textual contents. The current experimental setup introduces a significant confounding variable, as the proposed method benefits from a pre-training regime that is not available to the baselines. This makes it impossible to isolate the impact of the proposed RL framework from the impact of the pre-training data.
- Since the framework does not fully utilize the benefits of web UI browsing tasks (see “Questions” below), the framework is supposed to be generic enough to also tackle conventional grounding problems on images from, e.g., COCO. (Since the GT boxes are nevertheless still needed.) I would like to see how this method compares with existing grounding modules (even if just compared with pixel-to-sequence ones) on these more generic tasks. The lack of evaluation on standard grounding benchmarks limits the generalizability of the findings and prevents a thorough assessment of the method's effectiveness compared to existing approaches.

### Questions
- At a first glance, I thought the model can really omit any metadata for supervisions, including even the ground truth boxes. That is to say, this may be the advantage of web UI problems as the predicted boxes may not need to be 100% correct but at least “touch” the ground truth ones (and then in reality it should be clickable). In this sense, one can really design an RL framework that relies solely on “successfully clicked” the right place in the UI as the reward function, and this should be much easier to collect from the data curation point of view. Why not consider this setting as an upgraded version of the framework, and really showcase the power of RL here?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
