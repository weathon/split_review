# Improving Multi-modal Representations via Binding Space in Scale

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Recently, human-computer interaction with various modalities has shown promising applications, like GPT-4o and Gemini. Meanwhile, multimodal representation models have emerged as the foundation for these versatile multimodal understanding and generation pipeline. Models like CLIP, CLAP and ImageBind can map their specialized modalities into respective joint spaces. To construct a high-quality omni representation space that can be shared and expert in any modality, we propose to merge these advanced models into a unified space in scale. With this insight, we present \textbf{OmniBind}, advanced multimodal joint representation models via fusing knowledge of 14 pre-trained spaces, which support 3D, audio, image, video and language inputs. To alleviate the interference between different knowledge sources in integrated space, we dynamically assign weights to different spaces by learning routers with two objectives: cross-modal overall alignment and language representation decoupling. Notably, since binding and routing spaces only require lightweight networks, OmniBind is extremely training-efficient. Extensive experiments demonstrate the versatility and superiority of OmniBind as an omni representation model, highlighting its great potential for diverse applications, such as any-query and composable multimodal understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes OmniBind, a framework that aims to merge multiple pre-trained multimodal models into a unified, large-scale representation space that can handle 3D, audio, image, video, and language inputs. This binding strategy employs weight routing to address knowledge interference from multiple sources and optimizes the integration of various models. OmniBind showcases impressive zero-shot generalization and cross-modal alignment across modality pairs.

### Strengths
1. This paper effectively addresses the challenge of binding multiple pre-trained multimodal spaces through dynamic weight routing. This approach moves beyond traditional fixed-weight methods by introducing a learnable routing mechanism, enhancing cross-modal alignment and reducing knowledge interference.
2. OmniBind's performance is thoroughly evaluated across diverse benchmarks, covering a wide range of modality combinations. This strengthens the claims of improved generalization and versatility.
3. The paper provides multiple examples of how OmniBind's representation space can be used in various applications, such as any-query object localization and audio separation, which demonstrate the practical benefits of the model.

### Weaknesses
1.  While the model uses pseudo-paired data due to a lack of real-world multimodal data pairs, this raises questions about the validity of the results in real-world applications. This reliance on pseudo-pairs could potentially limit the model's robustness in unexpected scenarios. Specifically, the method of generating pseudo-pairs, which relies on predictions from other models, introduces a potential for compounding errors and biases. The quality of the pseudo-pairs is directly tied to the performance of these models, and any inaccuracies or limitations in their predictions will propagate into the training of OmniBind. This could lead to a model that performs well on benchmarks derived from similar data but struggles with real-world data that deviates from the training distribution.
2. Although the dynamic routing approach is innovative, it may introduce complexity, particularly in practical implementations or deployment, where computational costs and latency might become prohibitive with increasing scale. The routing mechanism, while adaptive, adds overhead to the model's architecture. This overhead could manifest as increased memory usage and slower inference times, making it challenging to deploy on resource-constrained devices or in real-time applications. The computational cost of determining the optimal weights for each modality combination could also become a bottleneck, especially as the number of modalities and models increases.

### Questions
1. If future models introduce new modalities or more granular representations, how easily can OmniBind incorporate them without significant retraining or re-engineering?
2. Given that 3D, audio, image, video, and text often represent different levels of semantic information (e.g., higher ideographic density in text), how does OmniBind address potential biases in multimodal alignment? How did you ensure the reliability and consistency of the pseudo pairs generated across all modalities?
3. Can you provide more details or visualizations on how the routers assign weights in different tasks or datasets? How do these weights correlate with performance on cross-modal benchmarks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript presents OmniBind, a multimodal joint representation model designed to integrate and optimize the capabilities of 14 pre-trained modalities, including 3D, audio, image, video, and language inputs. By merging these specialized models into a unified representation space, the authors aim to enhance multimodal understanding and generation. The proposed framework employs a dynamic weight assignment mechanism, utilizing lightweight networks to facilitate the binding and routing of knowledge sources. The author claim that they not only improves the overall alignment across different modalities but also allows for effective language representation decoupling.

### Strengths
1.The manuscript presents a compelling approach to integrating various multimodal representation models into a unified framework, which is an advancement in the field of human-computer interaction.
2.The introduction of dynamic weight assignment and language representation decoupling may bring benefits.
3.The experimental validation provided in the study partially supports the authors’ claims regarding the versatility and effectiveness of the proposed model.

### Weaknesses
1. As for the proposed Language Representation Decoupling, statistics on the number of such cases can be added to support the need for such improvements.
2. Regarding the construction of the pseudo pair data for training, for audio, the authors use audio from AudioSet and then employ a state-of-the-art audio-text model to retrieve the most similar texts from AudioCaps and Clotho (they also retrieve texts from other datasets, but as the authors mention, there is a gap in the texts across different modalities, so the most similar texts are likely to come from the audio-text dataset). First, I think this is somewhat redundant, as they could have directly used the paired audio-text data from AudioCaps, since the audio in AudioCaps comes from AudioSet. Secondly, this means that the training set includes data from Audiocaps, so please confirm whether the methods in Table 2 also have similar situations; otherwise, I believe it would be an unfair comparison. Additionally, the annotations of AudioCaps are highly correlated with the category annotations of AudioSet, which raises concerns about the potential for label leakage. Therefore, I question whether it is appropriate to use AudioSet to validate zero-shot classification in Table 3.
3.The datasets used in the experiments are mostly quite old; it might be worth considering more updated ones.
4.In my opinion the methods used in this paper fall under multi-task learning. Please provide comparisons with multi-task methods to demonstrate the advantages of the approach presented in this paper.

### Questions
1. For a certain modality, when different modalities need to be aligned, will it itself require different angles of representation, and is it reasonable to do a universal representation?
2.For language representation decoupling, my understanding is that this involves separately aligning image encoders with text encoders from image-text pretraining, and audio encoders with text encoders from audio-text pretraining, etc. If the authors separate these alignments, does it contradict the goal of achieving a universal representation?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel method for fusing knowledge from mutiple pre-trained spaces across different modalities (including 3D, audio, image, video and language etc.) into a single shared "high-quality omni representation space". The core technique involves a dynamically adjusted weighting schema (achieved via a learnable router) to alleviate interference across knowledge sources/modalities. The lightweight router network that controls binding and routing enables the system to be trained efficiently. The authors performed extensive experiments and demonstrated the superior performance of the approach on multiple relevant benchmarks.

### Strengths
* Originality

This paper presents a novel approach for binding cross-modal pre-trained latent space into a different space. Although similar ideas have been published in several prior work, this paper has made some extensions to enable more efficient pseudo item-pair construction and to be able to scale up the target spaces. 

* Quality

The effectiveness of the proposed framework is validated by extensive experiments over multiple benchmarks, and the model has achieved even better performance than "individual best" (specialist source model on the target modality only).

* Clarity

The paper is in good shape with key ideas being clearly presented by text and figure illustrations. It is relatively easy to follow.

* Significance

The proposed idea can be easily adapted to new modalities and may lead to more exciting applications.

### Weaknesses
 * Arguably the idea presented in this paper is a natural extension thus incremental to previous work, e.g. the main change from FreeBind would be the pseudo-item generation (from pseudo-embedding pair aggregation to pseudo-item pair retrieval) and learnable weights routing.

* One missing ablation (correct me if I missed anything) would be a side-by-side comparison of pseudo item pair retrieval vs. pseudo embedding aggregation (e.g. FreeBind), as the authors claim the proposed approach is more efficient and robust. The ablation can be done by applying pseudo item pair retrieval to the same experimental setup as pseudo embedding aggregation if the latter doesn't support more datasets.



### Questions
* The foundational step behind the proposed approach is the quality of curated pseudo item-pair across all modalities. Is there any direct or indirect quality measurement of this step? Meanwhile as the results in Table 2 and Table 3 show, after binding the omni representation sometimes beat the original "individual best", suggesting the cross-modality binding can even improve representation capability. It would be interesting to see qualitative examples of such improvement if possible. 

* Related to previous question, when a new space needs to be added to the omni representation space, does it require re-computation of all existing spaces? According to equation (4) it seems all embedding spaces need to be adjusted but please provide more clarifications. Also curious if it's possible to iterative do the binding (iteratively do binding -> pseudo item-pair update -> binding etc.) to further boost the performance, if incremental binding (one space at a time) is possible?

* Some minor issues include citations wrong (L53, L60, L124, L155, etc.)

### Soundness
4

### Presentation
4

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
This paper presents OmniBind, a framework designed to integrate diverse multimodal models into a unified representation space. This paper introduces a learnable router that dynamically assigns weights to different input combinations, mitigating interference between knowledge sources and enhancing versatility. By binding various pre-trained models, OmniBind achieves notable performance across multiple benchmarks and demonstrates versatility in handling different modalities.

### Strengths
1. This paper presents an approach OmniBind leverages the strengths of specialized models.
2. This paper addresses the limitation of fixed-weight averaging and offers a flexible way to integrate multiple knowledge sources.
3. This paper shows the potential of OmniBind for practical applications such as 3D-audio retrieval, any-query object localization, and complex multimodal compositional understanding.

### Weaknesses
1. This paper is somehow hard to follow and not well-written. The motivation and method sections may not be sufficiently clear. This paper contains some inconsistencies in notation and symbols, which is confusing for readers. For instance, the term "item pair {p, a, v, t}" on line 211 is not clearly defined or explained when it first appears.
2. This paper does not address how the introduction of OmniBind affects training and inference speeds. Specifically, the computational overhead of the learnable router and the binding of multiple pre-trained models should be quantified. The paper lacks a discussion on the trade-offs between performance gains and increased computational costs.
3. This paper lacks detailed discussions on certain aspects of the method. For example, expert load balancing in the Mixture of Experts (MoE) has not been explored. The paper should discuss whether the router equally distributes the load across different experts or if some experts are consistently favored, and the implications of such behavior.
4. While the paper mentions that textual descriptions of different modalities exhibit significant biases (on line 258), it does not provide supporting evidence or references to illustrate these biases. The paper should include empirical evidence, such as visualizations of feature distributions or quantitative analysis, to support this claim.
5. The generalizability to new modalities is not presented in this paper. The paper should discuss the process of integrating new modalities, including the required modifications to the framework and the potential challenges.

### Questions
1. This paper mentions in the abstract that OmniBind is extremely training-efficient (line 041). How is this reflected?
2. Did the paper consider the issue of expert load, and if so, how was it addressed?
3. On line 199 of the paper, the authors mention the advantages compared to FreeBind. How is item-pair retrieval done here?
4. If one wants to support a new modality under this method, how should it be carried out?

### Soundness
2

### Presentation
2

### Contribution
2
