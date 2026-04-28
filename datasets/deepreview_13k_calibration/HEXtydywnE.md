# LASER: A Neuro-Symbolic Framework for Learning Spatio-Temporal Scene Graphs with Weak Supervision

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
We propose \ours, a neuro-symbolic approach to learn semantic video representations that capture rich spatial and temporal properties in video data by leveraging high-level logic specifications. 
In particular, we formulate the problem in terms of alignment between raw videos and spatio-temporal logic specifications. 
The alignment algorithm leverages a differentiable symbolic reasoner and a combination of contrastive, temporal, and semantics losses.
It effectively and efficiently trains low-level perception models to extract a fine-grained video representation in the form of a spatio-temporal scene graph that conforms to the desired high-level specification.
To practically reduce the manual effort of obtaining ground truth labels, we derive logic specifications from captions by employing a large language model with a generic prompting template.
In doing so, we explore a novel methodology that weakly supervises the learning of spatio-temporal scene graphs with widely accessible video-caption data.
We evaluate our method on three datasets with rich spatial and temporal specifications: OpenPVSG, 20BN-Something-Something, and MUGEN. 
We demonstrate that our method learns better fine-grained video semantics than existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a neural-symbolic framework to learn spatio-temporal scene graph generation from the weak supervisory signals provided by video captions. It is achieved by utilizing an LLM to convert a video caption into a programmatic specification and then compute the alignment scores by a pretrained vision-language embedding model. Experiments are conducted to show the effectiveness of the proposed weakly-supervised method in performance.

### Strengths
1.This paper is well-written and the organization is reasonable and easy to follow.

2.Experimental results show that the proposed method achieves state-of-the-art performance that can even outperform fully-supervised methods.

3.The introduction of neural-symbolic representations and reasoning sounds interesting and could be a promising direction to explore.

### Weaknesses
1.Although the authors claimed that they proposes the first framework to learn weakly-supervised scene graph generation from video caption data, the utilization of image caption data in weakly-supervised scene graph generation has been widely explored [1, 2], and I think this work falls into a straightforward adaptation to the video domain, so this contribution is not that appealing.

2.The idea to incorporate LLMs into scene graph generation has also been investigated by several previous works [3, 4]. This makes the novelty of this framework less significant.

3.For using neural-symbolic techniques, as have been mentioned in the manuscript, it could be hard to accurately transform a video caption into a structured representation like formal program. However, the proposed method heavily relies on the extracted programmatic specification for making predictions and this would possibly become a weakness that reduces the robustness of the method. Moreover, if the video captions become even more complex and longer, I am wondering whether the method will simply fail since the programmatic representations can be very inaccurate in such scenario. It is suggested to add experimental results on the model's sensitivity to the LLM's capability.

4.In terms of performance comparison, the authors claimed that their weakly-supervised framework outperforms fully-supervised frameworks, but I think this is kind of unfair since the complexity and external models like LLMs adopted in this work are much more expensive and stronger than many fully-supervised method. So what would be the comparative result if no LLMs are used in this work? If LLMs are necessary for this method to work, then how much complexity and resources will it cost to use the LLMs?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces LASER, a framework that leverages video captions as weak supervision to train spatio-temporal scene graph (STSG) generators, addressing the challenge of costly manual STSG annotations. LASER utilizes large language models to derive spatio-temporal semantic specifications from video captions, then aligns STSG predictions with these specifications using a differentiable symbolic reasoner and specialized loss functions. This approach enables efficient training of STSG models without annotated data, achieving notable improvements over fully-supervised baselines on datasets such as OpenPVSG, 20BN, and MUGEN.

### Strengths
1. This paper proposes a new framework the uses specification language, for specifying fine-grained video semantics.
2. The experimental results show good performance compared with fully-supervised one.

### Weaknesses
1.  The design of this approach seems puzzling. If the STSG can be generated based on a series of advanced models such as CLIP and LLM, why need to train an additional model to make predictions based on the generated data? What are the problems with directly using the generated data as the results, and what is its performance?
2. The description of the experimental section is also quite unclear. For instance, it is not specified which state-of-the-art (SOTA) methods are used for comparison or whether they represent the most advanced approaches. Additionally, there are no specific references provided, making it difficult to assess the relative effectiveness of the proposed method.
3. The motivation behind STSL is not very clear. Its relationship with STSG is also unclear, as well as why this step is necessary.

### Questions
Lines 428-430 describe the baseline; however, it seems that no state-of-the-art (SOTA) methods for relation extraction are mentioned. Does this paper surpass the SOTA methods for image or video relation extraction?

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
The paper proposes LASER, a framework for training spatio-temporal scene graph (STSG) generators using video captions as weak supervision. LASER uses large language models to extract logical specifications from captions and aligns these with predicted STSGs through a differentiable symbolic reasoner and a mix of contrastive, temporal, and semantic losses. This approach enables training STSG generators without manually annotated STSG data. LASER is evaluated on OpenPVSG, 20BN, and MUGEN datasets, showing notable improvements over supervised baselines.

### Strengths
The paper introduces a novel approach for training spatio-temporal scene graph (STSG) models using video captions as weak supervision, which removes the need for labor-intensive STSG annotations. It leverages large language models to extract logical specifications, which is innovative in combining neuro-symbolic learning with weakly supervised STSG generation.

This work has high significance as it opens a new path for STSG learning, making it accessible without costly annotation processes. Its performance gains on OpenPVSG, 20BN, and MUGEN suggest practical implications for scalable STSG generation in video understanding.

### Weaknesses
The reliance on large language models to extract logical specifications may introduce noise and inaccuracies, especially if the captions lack detailed descriptions. Enhancing this extraction process or adding error-handling mechanisms could improve overall model performance.

The evaluation covers three datasets but could be strengthened by testing on additional complex datasets for scene graph generation to validate generalizability, such as Action Genome, VidVRD, and VIdOR.

The paper does not include strong works on scene-graph generation, such as STTran, TRACE. It is hard to evaluate the robustness of the proposed framework without the comparison with such methods.

STTran: https://openaccess.thecvf.com/content/ICCV2021/papers/Cong_Spatial-Temporal_Transformer_for_Dynamic_Scene_Graph_Generation_ICCV_2021_paper.pdf

TRACE: https://openaccess.thecvf.com/content/ICCV2021/papers/Teng_Target_Adaptive_Context_Aggregation_for_Video_Scene_Graph_Generation_ICCV_2021_paper.pdf

### Questions
Could you clarify the specific criteria or methods used by the language model to extract logical specifications? Additional details on handling ambiguous or underspecified captions would be helpful.

Have you considered using additional forms of weak supervision, such as visual cues or scene descriptions, to compensate for the limitations of captions alone?

How well does the approach generalize to more complex, real-world videos beyond the tested datasets? Testing on diverse, large-scale datasets could provide valuable insights.

### Soundness
2

### Presentation
2

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
This paper uses large language models to generate pseudo-labels for spatiotemporal scene graph generation models without intensive human annotations. It generally contains a probabilistic relational database construction section, a spatiotemporal specification language description section, a natural language parsing section, and a spatiotemporal alignment checking section. A loss function that combines contrastive, temporal, and semantic components is exploited. The authors conduct extensive experiments on three popular datasets: OpenPVSG, 20BN, and MUGEN.

### Strengths
1. Exploring large language models to generate pseudo labels for vision-language learning tasks is intuitive nowadays. The proposed method designs an elegant pipeline to generate pseudo labels for the spatio-temporal scene graph generation task.

### Weaknesses
1. The significance of the target task spatiotemporal scene graphs needs to be discussed further. Since the large language models generate the pseudo label, they should be able to create scene graphs with appropriate prompts. So, the problem formulation and significance do not seem solid enough. It would be better to compare the proposed approach more explicitly to directly using LLMs to generate scene graphs. If the experiments are too expensive, the authors can discuss the potential advantages of the proposed method over state-of-the-art MLLMs. The authors can also explain why training a separate STSG model is beneficial.
2. Some technical details are not clear enough. The symbols in equation (1) are not explained well.

 $~~~~~~~~~~~~~~~~~\mathcal{L}\left ( Pr\left ( M_{\theta} \left ( X \right ) |= \psi  \right ) ,1 \right )  $

I am unclear about what the $\psi$ stands for and why $ M_{\theta} \left ( X \right )$ needs to condition on 1. What does the "1" stand for?

3. There are many key concepts and methodologies that are not explained in the method section. For example, in line 181, what does "0.05::unary_atom("deformed", 3, e)" stand for, especially the number "0.05"? The same problem appears in line 182.

   In lines 213-215, the logic component set is not given. It's an essential point for readers unfamiliar with the spatiotemporal scene graph to understand the paper.

4. The spatio-temporal scene graph part in the right-up corner of Figure 1 is unclear. The same problem appears in Figure 6.

In Figure 1, in the third row, there are "$\neg $touching (B, H)" both on the left and the right side. What this means seems to be ambiguous.

5. The paper does not present state-of-the-art MLLM results. To demonstrate the advantage of the proposed method, authors should consider some multimodal large language models, such as BLIP-2, InstructBLIP, MiniGPT-4, and LLaVA-1.5.

6. The title uses the keyword "neuro-symbolic," but it seems that the proposed method doesn't emphasize this point. It deserves further discussion.

### Questions
I have no further questions. See the weakness part please.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents LASER, a model-agnostic neuro-symbolic framework designed to learn Spatio-Temporal Scene Graphs from videos using weak supervision derived from video captions. Traditional supervised methods for training STSGs are hindered due to reliance on labor-intensive annotated datasets, while LASER addresses this challenge by employing LLMs to extract logical specifications and then training the underlying generator to align the STSG with the specification.

### Strengths
1. The overall presentation is clear and the figures are well-illustrated.
2. The introduction of the STSL provides a flexible and expressive way to capture the nuances of video semantics, and the alignment checking ensures the relations between STSL and STSG.
3. Extensive experiments and ablation studies demonstrate the effectiveness of LASER in learning STSG.

### Weaknesses
1. The performance of LASER heavily relies on the quality of video captions. If captions are sparse or inaccurate, the resulting generated STSGs may also suffer in quality.
2. The model seems to have a problem building scene graphs with longer videos and more instances. 
3.  While the framework is promising, the scalability of the approach to very large datasets or real-time applications may pose challenges to the model.

### Questions
1. In Table 3, setup 1 & 2 have the same F1 score, while the full setting of losses is higher than setup 3. Can you explain this phenomenon? 
2. See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
