# AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Generating bitmap graphics from text has gained considerable attention, yet
  for scientific figures, vector graphics are often preferred. Given that
  vector graphics are typically encoded using low-level graphics primitives,
  generating them directly is difficult.
  To address this, we propose the use of \tikzname, a well-known abstract
  graphics language that can be compiled to vector graphics, as an intermediate
  representation of scientific figures.\ \tikzname offers human-oriented,
  high-level commands, thereby facilitating conditional language modeling with
  any large language model.
  To this end, we introduce \dataset, the first large-scale \tikzname dataset
  consisting of 120k \tikzname drawings aligned with captions. We fine-tune
  \llama on \dataset, as well as our new model \clima, which augments \llama
  with multimodal \clip embeddings. In both human and automatic evaluation,
  \clima and \llama outperform commercial \gpt and \claude in terms of
  similarity to human-created figures, with \clima additionally improving
  text-image alignment.
  Our detailed analysis shows that all models generalize well and are not
  susceptible to memorization.\ \gpt and \claude, however, tend to generate
  more simplistic figures compared to both humans and our models.
  We make our framework, \projectname, along with model weights and datasets,
  publicly
  available

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, authors collect 119k TiKz datat to fine-tune LLaMa, and achieve better performance compared to GPT4 and Claude2 in TiKz generation. 
Also, authors propose a method to prevent the TiKz code from not compiling.

### Strengths
1. Good approach error handling method. Quite interesting study: on a specific domain, with relatively small data scale (119k) and LoRA, the author's approach can actually perform pretty well.
2. Evaluation metrics are extensive and conving.
3. Presentation is clear.

### Weaknesses
1. Seems like author didn't show any conversation example where users can edit or optimize the code while in the chat. 
2. Recently, [1] propose to leverage SVG, a similar format to TiKz, to conduct image understanding, generation and editing. How do authors judge on this?
3. The error handling strategy seems quite standard and wildly used in programming languages. 

### Questions
1. Any code error rate comparsion? (compiling success rate)

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
The paper proposes an approach to generating scientific images, by generating their TiKZ code, and open-sources the training dataset for this task. The paper investigates two solutions, namely LLaMa and LLaMa combined with CLIP-based image adapter. Both models are LoRA-tuned. The comparison with promping GPT-4 and Claude-2 is performed.

### Strengths
Originality: While this is not the first paper to do vector graphics generation with language models, the specific focus on TikZ is novel, and the published dataset is first of its' kind.

Quality & Clarity: The paper is of high quality, with good related work section, clear metrics,and detailed analysis of the performance, including a human study. It provides the code accompanying the submission, and suggests the availability of the models (link removed for anonymity). The writing is mostly clear, doesn't have typos, the dataset composition is clearly outlined, as are many of the choices made by the authors (such as the choice of LLaMa vs LLaMa-2, the specific prompts used for the models, etc.).

Signficance: The main point of signficance is the release of the dataset, fostering future work in this direction, and I believe it will be useful for the community.

### Weaknesses
The main weakness of the paper is the limited ablation study: The authors compare and contrast the two versions of the model, LLaMa and CLiMA (LLaMa + CLIP adapter) but don't highlight other important choices made, ex.
* The effect of the aritifical samples. 50% of the proposed dataset is the artificial samples, but the evaluation is done on real samples. The effect of augmentation with artificial samples is not measured.
* The effect of re-sampling the generation. The authors re-generate the output multiple times until the result is compilable, and the average number of re-generations is > 1.5, but the performance without regeneration is not reported.
* The effect of data augmentation for CLiMa. As specified in section 5, during training CLIP is given either the input caption or the reference image (50-50%) and during inference it is given the input caption. The effect of this data augmentation is not reported.
* The performance of vanilla LLaMa or prompt-tuned LLaMa is not reported, making the comparison between fine-tuned versions and prompted GPT-4 / Claude-2 not exactly fair.

The second issue is the limited model output results reported in the paper - the authors only show 6 examples in the appendix, and out of 3 labeled "good", the first one shows the image that, in my perception, doesn't really match the label ("some dots are clustered together" in the prompt, but shows just rows of points in the image)

### Questions
How did the authors arrive at the specific prompt that was used for GPT-4 / Claude-2 and how do they know if that is the one that indeed yields a reasonably high performance from the models?
Given the iterative re-generation, the models could have also made use of the TikZ compiler error / stack trace, what was the rationale for not using this information?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents AutomaTikZ, a project aimed at automatically generating TikZ drawings from natural language descriptions. The authors introduce a novel dataset, DaTikZ, which consists of aligned TikZ drawings and captions, and a new model architecture named CLiMA that integrates multimodal CLIP embeddings into LLaMA. The results show that CLiMA outperforms both LLaMA and other proprietary models like GPT-4 and Claude 2 in various metrics. CLiMA's capability to process images opens potential applications in vectorization and sketch conditioning.

### Strengths
- The paper is well-written and easy to follow.
- The paper introduces a pioneering dataset and a novel model architecture, which is a significant contribution to the field of automatic drawing generation from textual descriptions.
- The proposed model, CLiMA, demonstrates superior performance over existing models, including well-known ones like GPT-4 and Claude 2, across several evaluation metrics.

### Weaknesses
 - Since the main contribution of the study is introducing DatikZ, it would be better to add a couple of simple captions to the code/image examples in the main draft

### Questions
- Can you please provide a couple of examples of different models' behavior to typographic attacks?
- Have others considered comparing with ChatGPT? Maybe fine-tuned on a very small subset of the dataset.

### Soundness
2 fair

### Presentation
3 good

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
This paper focuses on TikZ, a language for vector graphics, and provides a dataset, DaTikZ, consisting of 120,000 pairs of TikZ and their captions. The authors are also evaluating the application of LLaMA and CLIP on the dataset. Experimental results show that models trained on DaTikZ can generate more complex vector graphics compared to those synthesized by closed-source LLMs such as GPT-4 and Claude 2.

### Strengths
- It is the largest scientific vector image and caption dataset to the best of the reviewer's knowledge.
- Benchmarking with multiple baseline models is reported.
- While automatic evaluation of generative models often encounters difficulties regarding their quality, this paper uses multiple scores for automatic evaluation to make the comparison meaningful. Multiple human subjective evaluations have also been considered and performed, as described in Sections 5.2 and D.

### Weaknesses
 - As shown in Table 1, DaTikZ consists of multiple data sources. If DaTikZ consists of multiple data sources, the authors should evaluate which data sources contribute to the accuracy of the generation on the test data and to what extent. This would not only justify the use of each data source, but may also suggest what further data should be collected in the future. Specifically, it is important to understand if certain data sources introduce biases or noise that negatively impact the model's ability to generalize. For example, are the curated examples significantly better than the data scraped from TEX Stack Exchange, and if so, what are the key differences that contribute to this disparity? A detailed analysis of the data sources is needed to understand their individual contributions and potential drawbacks.
- The contribution of data augmentation should also be evaluated. It is not clear how much the data augmentation techniques contribute to the performance of the model. A thorough ablation study is needed to determine the effectiveness of each augmentation method. For example, if geometric transformations are used, it is important to understand if these transformations improve the model's robustness or if they introduce artifacts that hinder performance. Similarly, if color augmentations are applied, it is important to understand if they help the model generalize to different color schemes or if they simply add noise. Without this analysis, it is difficult to assess the true value of the data augmentation pipeline.
- Since this paper is also about a novel dataset for scientific vector graphics and their benchmarking, the technical contribution of the baseline method is modest. While the authors present a method that combines LLMs with vision encoders, the novelty of this approach is not clearly established. The paper would benefit from a more detailed comparison with existing methods and a more thorough analysis of the advantages and disadvantages of the proposed approach. It is important to understand if the proposed method offers a significant improvement over existing techniques or if it is simply a combination of existing methods.

### Questions
- The reviewer expects the authors to respond to the points listed in Weaknesses.
- Figure 2 shows two radar charts. Although the main purpose of the radar charts is to make relative comparisons within the same chart, it would be possible to make some comparisons among the method in the left and right charts if the ranges of each score were adjusted.
- When the authors conduct a human annotation campaign, they could also evaluate how well the automatic evaluation metrics used in section 5.1 correlate with subjective evaluation; are there any plans to do so?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
