# Enhancing Audio--Language Models through Self--Supervised Post--Training with Text--Audio Pairs

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Research on multi-modal contrastive learning strategies for audio and text has rapidly gained interest. Contrastively trained Audio-Language Models (ALMs), such as CLAP, which establish a unified representation across audio and language modalities, have enhanced the efficacy in various subsequent tasks by providing good text aligned audio encoders and vice versa. These improvements are evident in areas like zero-shot audio classification and audio retrieval, among others. However, the ability of these models to understand natural language and temporal relations is still a largely unexplored and open field for research. In this paper, we propose to equip the multi-modal ALMs with temporal understanding without loosing their inherent prior capabilities of audio-language tasks with a temporal instillation method \textbf{TeminAL}. We implement a two-stage training scheme TeminAL A $\&$ B, where the model first learns to differentiate between multiple sounds in TeminAL A, followed by a phase that instills a sense of time, thereby enhancing its temporal understanding in TeminAL B. This approach results in an average performance gain of $5.28\%$ in temporal understanding on the ESC-50 dataset, while the model remains competitive in zero-shot retrieval and classification tasks on the AudioCap/Clotho datasets. We also note the lack of proper evaluation techniques for contrastive ALMs and propose a strategy for evaluating ALMs in zero-shot settings. The general-purpose zero-shot model evaluation strategy \textbf{ZSTE}, is used to evaluate various prior models. ZSTE demonstrates a general strategy to evaluate all ZS contrastive models. The model trained with TeminAL successfully outperforms current models on most downstream tasks.git}{link}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a post-training method to enhance CLAP's (Contrastive Language-Audio Pretraining) understanding of temporal relations in audio samples. This post-training method consists of two stages: (1) post-training on single and dual audio events, and (2) post-training on varying temporal sequences of the same event combinations. The paper also presents a detailed evaluation on zero-shot temporal evaluation (ZSTE) to demonstrate that CLAP, with the proposed two-stage training, achieves a better understanding of audio semantics in the temporal relations, especially on the understanding of both events in the overlapping cases.

### Strengths
The strengths of this paper lie in two main areas:

(1) **Two-Stage Post-Training**: The paper introduces a two-stage post-training method based on an assumption about the learning challenge in CLAP models, which is the difficulty gap related to the number of events versus their temporal order. By addressing these learning challenges progressively through distinct post-training stages, the paper demonstrates performance improvements. Additionally, it contributes by adapting the training objectives of CLAP to TNCE loss terms, though this is primarily referred by prior work in computer vision.

(2) **Zero-Shot Temporal Evaluation**: The introduction of ZSTE establishes a benchmark for audio understanding. The paper provides a range of tasks to thoroughly evaluate CLAP's performance in understanding temporal relations in audio samples.

### Weaknesses
However, the weaknesses of this paper are substantial and can be categorized into three main points:

(1) **Limited Novelty and Generalization**:  The primary contribution lies in the two-stage post-training approach and its experiments; however, the concept of using augmented captions (such as concatenation and overlay) to improve CLAP’s understanding of temporal audio relations has already been explored in prior works [1][2]. Moreover, the paper lacks sufficient evidence and explanation to justify the necessity of a two-stage post-training approach (see point (2) below). Generalization is also a critical concern, as the paper primarily focuses on two-event audio scenarios and restricts prompts to a narrow set of captions—[before, after, while]. Real-world audio scenarios are significantly more complex, involving a wider variety of events and more natural language descriptors. Scaling this method to accommodate more events and captions poses a significant challenge, as the size of the contrastive matrices would become prohibitively large for processing.

(2) **Inadequate Experimental Setup to Demonstrate Effectiveness**:

a. While the proposed post-training method could be applied to existing CLAP models (e.g., LAION-CLAP, Microsoft-CLAP, CompA-CLAP), the authors did not showcase this flexibility. As mentioned in Section 3.4, “the encoders need to be pretrained", it would have been more effective to apply the post-training method to 2-3 different CLAP models and compare their performance with and without the post-training. This approach would demonstrate the post-training method's effectiveness without the need to train the CLAP model from scratch (as it appears the authors did) to save time. It also strengthens the evidence supporting the proposed method.

b. Effectiveness of Two-Stage Training (i.e., TerminAL A and B): Table 2 presents a partial ablation study but omits the results for TerminAL A-only. Including this result would provide a clearer picture of how TerminAL A alone impacts ZSTE performance, offering more comprehensive evidence for the individual effectiveness of each training stage. Without this ablation, it's difficult to ascertain whether the performance gains are due to the two-stage approach or simply the addition of more training data in the second stage.

c. Overall Performance: According to Table 3, the proposed T-CLAP does not consistently outperform previous models or yield comparable results on non-temporal tasks. CompA-CLAP and T-CLAP each achieve the top-1 performance on approximately half of the tasks. While CompA-CLAP struggles with tasks 2A and 2C, which require predicting both events, T-CLAP sacrifices substantial accuracy on task 1A (dropping from 82% to 75%), which is the most fundamental audio understanding task. These results suggest two conclusions: first, the single-dual contrastive training (T-A) step is crucial, as it drives improvements in tasks 2A and 2C. Second, a trade-off remains between temporal enhancement and core audio classification accuracy, as the proposed method fails to preserve the performance on basic classification task, even falling below ML-ACT, (the baseline before CLAP).

(3) **Poor Presentation**:  This paper lacks several necessary introductions on its regular pages. The paper should emphasize more on explaining the T-A and T-B training paradigms (see further details in the question section) instead of reiterating TNCE details, which are largely sourced from [3]. Additionally, the experimental section is hard to follow due to minimal guidance on the five tasks and their A-B(-C-D) variations. The analysis of these experiments is too brief, making it difficult to validate the effectiveness of the two-stage training method and assess the overall performance. Furthermore, the title of the paper is vague and somewhat misleading; it would benefit from a clearer focus, such as emphasizing **temporal relation enhancement** in **contrastive language-audio pretraining** models.

Above all, I found this paper falls below the standard of ICLR, for its limited novelty and generalizability to enhance CLAP performance; insufficient experimental setup to effectively validate the method’s impact and stability in audio understanding through post-training; and a lack of writing organization that hinders clear communication of the essential training paradigms.

### Questions
1. In the TerminAL A training stage, the model is fed both single-event and dual-event samples. Do these samples also include overlay cases? For instance, will "Dog" and "Dog while Cat" be presented in the same batch?

2. In Table 2, T-AB appears to improve the 2A and 2C tasks compared to T-B. This suggests that T-A introduces a bias that enhances performance. However, I am unclear on how the T-A training stage leads to this bias. If "Dog" and "Dog while Cat" are presented in the same batch, the samples for "Dog while Cat" will still be penalized under the "Dog" label. Could you provide more insight into how the model effectively retrieves single-class captions when presented with dual-event (overlay) audio samples?

3. Were additional temporal-enhanced captions considered for training, or was the model exclusively trained with prompts like [after, before, while]? For instance, were alternatives such as [then, followed by, and then] also utilized? 

4. The use of prompts when combining two audio events in CompA-CLAP [1] differs from the proposed TerminAL approach. Do you believe this discrepancy will affect the performance results presented in Table 3 and whether the comparison remains fair? For example, it is possible that the keywords [before, after] were not employed in the training of CompA-CLAP.

[1] CompA: Addressing the Gap in Compositional Reasoning in Audio-Language Models

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces an essential gap in contrastively pre-trained Audio-Language Models (ALMs) by showing their failure to capture correct temporal relationships between audio and various acoustic events. To address this, the authors propose TeminAL—a two-step post-training framework for infusing temporal awareness in ALMs. Additionally, the paper introduces ZSTE, a Zero-Shot Temporal Evaluation scheme designed to evaluate temporal understanding in ALMs in a zero-shot fashion.

### Strengths
1. The paper shows a critical gap in current ALMs for lacking temporal reasoning and acting as a "bag of words" while mapping audio and textual information using cosine similarity. To address this, the paper proposes Temin AL, a post-hoc alignment approach focusing on injecting temporal ordering among diverse acoustic events in existing ALMs
2. To evaluate temporal understanding in current ALMs in a zero-shot fashion, the authors also propose a multistage zero-shot temporal evaluation scheme, called ZSTE

### Weaknesses
1. The curriculum learning approach introduced by the authors while showing decent performance in audio-text retrieval tasks, still remains very similar to the CompA's modular contrastive pre-training approach. I will request the authors to address this in the main paper. 
2. The authors have used ESC50 for synthesizing temporal-rich audio segments (e.g., dog after cat, etc.). Did the authors explore more diverse audio sources like AudioSet Strong, which contains time-aligned information and more than 500+ labels? I will request the authors to add a few lines in the paper to explain the rationale behind using ESC50 when compared to other audio data sources.
3. I find important ZS experiments on standard audio-classification tasks like AudioSet, FSD50K, USD8K, TUTUrban, etc. missing in the main paper.

### Questions
Additional Questions:
1. As shown in Figure 1, what is the advantage of 2-stage training vs 1stage training? Doing a comparative study will be useful in understanding which stage is contributing more towards temporal understanding.
2. The performance on standard order understanding benchmarks in audio like COMPA-Order and COMPA-attribute is missing in the main paper.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose to include both data curation and loss function design in helping the CLAP model to understand better the temporal relation. They also propose a zero shot temporal evaluation framework with a series of tasks in order to benchmark specific temporal modeling capability.

### Strengths
- Temporal modeling capability in audio is a fairly novel and under-explored research area. The proposed zero shot evaluation benchmark is reasonable and can be a good contribution to the community.

### Weaknesses
 - The use of equations in section 3 to explain the proposed loss function is not easy and straightforward to follow, and they do not connect well with figure 3. The variables and loss terms in the equations are not clearly mapped to the components in Figure 3, making it difficult to understand how the loss is computed in practice. For example, it is unclear which parts of the model correspond to the variables in the equations, and how the different loss terms interact within the model's architecture. Consider adding annotations or visual cues to Figure 3 to improve the connection for clearer explanation.
- TeminAL A can benefit from more detailed explanation. It is mentioned that TeminAL A is trained to distinguish between single and multiple sounds,  are they trained with similar contrastive loss? if so, how are the audio and text pairs curated? or are they trained with classification loss separately? The training procedure for TeminAL A is not sufficiently clear, particularly how the audio and text pairs are created and used in the loss function. It might worth adding a figure to explain the TeminAL A stage training, similar to figure 4 for TeminAL B, to clarify the data flow and loss computation.
- The more detailed explanation of ZSTE should be included in the main paper, current appendix B.4 contains most of the information for the reader to understand what proposed ZSTE is? Since these are one of the main contributions of this work, it is worth integrate into the main narratives. The current placement of ZSTE details in the appendix makes it difficult to assess its importance and how it contributes to the overall claims of the paper. Moving this to the main text would allow for a better understanding of the proposed evaluation framework.
- The explanation of the categories A, B, C, D used in Table 2 is buried in the caption of Table 3, these are also important information and might worth moving into the narrative in the sections explaining the evaluation and benchmarks. The current location of these definitions makes it difficult for the reader to understand the results in Table 2 without referring to another table's caption. This information should be presented in the main text to improve readability and understanding.
- Minor suggestion: consider making the fonts in the figures larger, there are still space in the figure that can be adjusted. The current font size in the figures makes it difficult to read the labels and annotations, impacting the overall clarity of the figures.
- For section 3.3, in the l_text, x_c and x_a are referred to the raw inputs, if the loss function takes embeddings as inputs, should these variables be z instead of x? The use of raw inputs 'x' in the loss function when embeddings 'z' are expected can cause confusion and should be clarified. It is important to ensure consistency in the notation and variable usage throughout the paper.

### Questions
- In table 1, are the results from different model in comparison trained by the authors? Or are they taking from publicly available models from each work?

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
5

### Summary
This paper presents a novel method for training audio-language contrastive models with sensitivity to temporal relations. This paper first constructed augmented data pairs that contain temporal relations, then trained with a novel 2-stage objective TeminAL AB. TeminAL AB first trains the model to distinguish single sounds and multiple sounds, then in the next stage it trains the model to distinguish between specific temporal relationships of the events. The objectives in TeminAL A and B consist of modified infoNCE loss which upweights the training of temporal relations. Last, this paper proposes a benchmark ZSTS to evaluate various audio-language zero-shot understanding tasks.

### Strengths
1. This paper proposes a novel 2-stage objective TeminAL AB for training audio-language contrastive models on temporal relationships.
2. This paper proposes a benchmark ZSTS to evaluate various audio-language zero-shot understanding tasks.

### Weaknesses
This paper lacks sufficient justification for its contributions, particularly due to limited comparison with prior works. Here are specific issues with the paper:

1. Comparison with Related Work: To my knowledge, the most relevant prior works are CompA [1] and T-CLAP [2]. The paper briefly introduces CompA in lines 90-104 but does not directly discuss how this work differs from or improves upon CompA. The related work section needs to more clearly articulate the current state of the field and how this work distinguishes itself from existing approaches, particularly those that also address temporal relationships in audio-language models.

2. Insufficient Comparative Analysis with CompA: CompA is only included for benchmarking performance. CompA generated and used a larger dataset with up to 110k samples, while this paper does not discuss the impact of dataset size or the types of datasets used in fine-tuning. CompA has its own method of defining tasks, such as using prompts like "before" and "after," while CompA uses "succeeded," "preceded," and "amidst." I am curious if the authors compared the effects of prompt design between these two models. Since CompA has a public benchmark, a fairer comparison would involve evaluating this model on CompA’s benchmark to highlight differences in approach. Perhaps the authors intend to show that their objective is superior to CompA’s, but there is no evidence provided to support this claim. The paper needs a more thorough comparison of the proposed method with CompA, including a discussion of the differences in approach, dataset size, and prompt design, and ideally, a direct comparison on a common benchmark.

3. Comparison with T-CLAP: T-CLAP is also highly relevant, as both papers use the ESC-50 dataset to generate data. Although it seems the model and dataset in T-CLAP are not yet public, this work should at least include a discussion of T-CLAP’s approach. The paper should include a more detailed discussion of T-CLAP’s methodology, even if a direct comparison is not feasible due to the lack of public resources.

4. Limitations in Contributions: Regarding the three contributions listed in this paper:
The first contribution has already been demonstrated in prior works [1-3].
The second requires more evidence and direct comparison with existing methods.
The third contribution lacks comparison with other benchmarks.
The paper needs to more clearly delineate its contributions relative to prior work, and provide more substantial evidence to support its claims.

5. Discussion on Objective Functions: Although the authors note in the appendix that training with only the Terminal B objective is ineffective, I believe they should discuss why both Objectives A and B cannot be trained together. The paper should include a discussion on why a joint training approach was not used, and at least provide ablation results to support the chosen sequential approach.

Issues with Paper Presentation:
1. The text in the middle of Figure 3 is too small to read. I suggest placing Figures 3 and 4 together or at least referring to Figure 4 within Figure 3.
2. Line 334 contains a repeated "equation."
3. In line 334, it seems the numbering of the equation is incorrect. Eq 3 does not contain C^{cr} and C^{co}.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
