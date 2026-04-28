# Collective Model Intelligence Requires Compatible Specialization

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 5, 3, 3

## Abstract
In this work, we explore the limitations of combining models by averaging intermediate features, referred to as \textit{model merging}, and propose a new direction for achieving collective model intelligence through what we call \textit{compatible specialization}. Current methods for model merging, such as parameter and feature averaging, struggle to effectively combine specialized models due to representational divergence during fine-tuning. As models specialize to their individual domains, their internal feature representations become increasingly incompatible, leading to poor performance when attempting to merge them for new tasks. We analyze this phenomenon using centered kernel alignment (CKA) and show that as models specialize, the similarity in their feature space structure diminishes, hindering their capacity for collective use. To address these challenges, we investigate routing-based merging strategies, which offer more flexible methods for combining specialized models by dynamically routing across different layers. This allows us to improve on existing methods by combining features from multiple layers rather than relying on fixed, layer-wise combinations. However, we find that these approaches still face limitations when layers within models are representationally incompatible. Our findings highlight the importance of designing new approaches for model merging that operate on well-defined input and output spaces, similar to how humans communicate
through language rather than intermediate neural activations.io/compatible_specialization}{jyopari.io/compatible\_specialization}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the central argument arises as the authors highlight how fine-tuning models may hinder their parameter-wise combinations (i.e., model merging). The authors present empirical evidence (via a CKA similarity measurement) on how specializing models, via transfer learning, cause their representation to diverge; hence, feature averaging algorithms will tend to be suboptimal, for merging models in this setting.

The authors claim that it is crucial for models to communicate their (layer-wise) learned knowledge; they go on to state that feature averaging and representational alignment methods do not address this problem. As an alternative, they propose a _mixture of experts_ (MoE) mechanism, focusing entirely on adequate routing. Overall, given two (pretrained) models, their method proposes to treat certain layers as experts and route them, instead of combining them with any interpolation coefficient. This method is, allegedly, flexible to support merging different architectures.

Experiments show that while the proposed routing-based merging approach does improve upon basic feature averaging methods, it still faces substantial limitations. Specifically, the authors observe that as models become more specialized through fine-tuning on distinct tasks (e.g., math vs. coding), the merged model’s performance on a cross-domain adaptation task initially improves but subsequently declines as representational divergence increases. The experiments also demonstrate that routing methods with more degrees of freedom—such as multi-layer and cross-layer routing—yield better performance than single-layer static interpolation, particularly when the models share similar internal structures. However, even these sophisticated routing techniques struggle when the internal layer representations of the models are highly dissimilar, ultimately reaching a performance plateau.

### Strengths
- Insightful Identification of Compatibility Issues: The paper highlights that representational divergence during fine-tuning can hinder model merging efforts, which is a fundamental issue when merging any kind of machine learning models; hence the paper is well motivated.
- The paper is generally well-written and offers useful analogies for the reader to ground his or her intuitions correctly.
    - The reader can smoothly go over the paper, as academic language develops every concept with eloquence.
- Experiments are conducted on both, in-domain and out-of-distribution settings, which are typical scenarios to assess knowledge transferability between models.
- There is no discussion on time and space complexity caveats.

### Weaknesses
 - Arguing that models require **compatible specialization** is central to the purposes of this paper. Yet the concept remains ill-defined after the methodology section, which brings certain issues such as:
    - no direct/intuitive connection between routing mechanisms and a neural model's _ability to communicate its knowledge_;
    - lack of literature review on past methods that could, at least, somehow contribute to enhancing compatible specialization;
- While Figure 6 showcases how layer incompatibility increases between more distant layers, no concrete actions were taken to improve the experimental decisions; in particular, only conjectures were made to handle similar relative positions between models, without explicitly modifying their method.
- There are no experimental ablations against past model merging techniques, rather than just comparing the routing with feature averaging.

### Questions
- The issue of merging task-specialized pretrained models has been explored before; therefore, it will be interesting to compare and contrast the presented _compatible specialization_ with:
    - $$L^2-SP$$: this method represents a preliminary fine-tuning-based approach, where regularization is added to retain pretrained knowledge: https://arxiv.org/abs/1802.01483;
    - The question of whether two models are compatible, with each other, has already been studied exhaustively, through the lens of _linear mode connectivity_ (LMC). For instance, see: https://arxiv.org/abs/2110.06296.
-  Section 2.4 introduces CKA, yet it seems that a bunch of equations were just thrown to the reader without the needed context. I suggest revising this section by somewhat explaining step-by-step what CKA is doing.
- What is the difference between _activation interpolation_ (see Section 2.2) and averaging weights with varying coefficients?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates the challenges of merging specialized neural models, focusing on issues of representational similarity and compatibility. It highlights that common merging techniques, such as feature averaging, often struggle to produce effective merged models as the individual models become more specialized. This specialization leads to divergent feature representations, which limit the models' ability to combine effectively. The authors propose exploring dynamic routing-based strategies, where features are merged across multiple layers instead of using static, layer-by-layer averaging. Their empirical analysis, including the use of centered kernel alignment (CKA) metrics, underscores the limitations of current merging methods and emphasizes the need for new approaches that prioritize compatible specialization. This work signals the importance of inter-model compatibility in the development of effective model merging techniques.

### Strengths
- **Originality**: This paper introduces a fresh perspective on model merging by emphasizing the importance of compatible specialization rather than direct feature merging. The application of centered kernel alignment (CKA) in this context is a novel approach that strengthens the paper’s analysis and arguments.
  
- **Clarity**: The paper is well-organized, with clear sections and helpful diagrams (e.g., Figures 1 and 4) that effectively illustrate the merging processes and highlight the limitations of current methods.

- **Significance**: By addressing the challenges of model merging and outlining future directions, this work provides valuable insights for advancing collective model intelligence. This is increasingly significant as fine-tuned, domain-specific models continue to proliferate. The paper’s emphasis on both computational efficiency and compatibility offers a meaningful contribution to the field.

### Weaknesses
 - **Quality**: The paper’s experimental scope is limited, and expanding it to include a wider range of tasks, such as those in SuperGLUE [1], would strengthen its findings. Additionally, comparisons with other benchmark model merging of Mixture of Experts (MoE) methods, such as those presented in recent works [2,3,4,5], would help contextualize the contributions and insights of this paper within the broader field.

- **Experimental Validation of CKA Insights**: The paper uses CKA analysis to examine representational similarity (e.g., in Figures 2 and 6). However, recent works have raised concerns about the reliability of CKA in drawing conclusions based on its similarity values, suggesting that it can sometimes produce misleading results in neural network similarity analyses [6,7,8]. Given that CKA’s benefits depend on observing specific conditions (discussed in aforementioned works), further investigation into its validity in this context, or the inclusion of additional similarity metrics, would lend greater robustness to the findings. Furthermore, the CKA analysis is performed pre-merging, which limits its utility in explaining the performance dynamics observed post-merging. The observation that adjacent layers exhibit high CKA similarity is well-documented [9,10], and the current analysis does not leverage this to advance understanding or propose innovative strategies. Observing how representational similarity changes *post-merging* could have provided more actionable insights, as it would directly relate to the performance dynamics observed in the routing methods.

- **Findings of Section 4.3**: Section 4.3 begins with the statement:
  > “When the performance in Figure 5 plateaus, we find that this is correlated with representational similarity between layers within a model and across models.”

  However, the analysis in Figure 6 does not conclusively support a correlation between the performance plateaus observed in Figure 5 and representational similarity among adjacent layers. As Figure 6 shows only a single snapshot (likely for the "Routing with 3 Layers" setting, please clarify if it is not the case as it is not mentioned in the text), observing CKA changes from "Standard Routing" to "Routing with 2 Layers" to "Routing with 3 Layers" would be necessary to conclude a correlation. If CKA values indeed increase between nearby layers across these configurations, then a correlation might be established. The current results as it stands only reconfirm previous observations that adjacent layers exhibit high CKA similarity, as shown in earlier studies [9,10]. Moreover, the authors' explanation that CKA values do not change across different merging methods because they are measured pre-merging further highlights the limitations of this analysis. If the CKA metric remains constant regardless of the merging method, it undermines its utility in correlating representational similarity with the performance plateaus observed in Figure 5. This calls into question the strength of the conclusions drawn in Section 4.3. Without additional evidence, such as tracking representational dynamics post-merging, the claimed correlation remains speculative.

- **Scope of the Vision for Collective Intelligence**: Although the paper’s proposal for collective intelligence in Section 5.2 (Routing Models in Input and Output Spaces) is intriguing, its practical impact is limited by a lack of concrete steps or preliminary experiments to advance this vision.

### Questions
1. **Practical Implications of Compatible Specialization**: Beyond the discussions provided in the paper, how do the authors envision compatible specialization being achieved in practice? Are there potential architectures or training methods that might enhance inter-model compatibility?
2. **Routing Complexity Trade-offs**: The results in Figure 5 suggest diminishing returns as routing complexity increases. Could the authors elaborate on potential architectural modifications or efficiency improvements to manage the trade-offs of increased routing complexity?
### Minor Suggestions
- **Line 343 (Figure 4 caption)**: The caption appears incomplete. Consider rephrasing to finish the sentence describing the complexity of routing to different layers.
- **Lin 411**: It is written " we find that is is correlated". There is one too many "is" here.
- **Consider Additional Citations**: Adding citations to studies that critique the use of CKA in representational analysis would provide a balanced view and strengthen the experimental conclusions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Previous works use parameter interpolation for merging models from two domains, which may fail if the CKA (Centered Kernel Alignment) between the two models is too large. This paper proposes using a Mixture of Experts (MoE) approach that routes between two models as a new model merging strategy.

### Strengths
The proposed MoE-based approach introduces a fresh perspective to the challenge of model merging by routing between domain-specific models. This strategy could address issues with prior methods that rely on simple parameter interpolation, particularly when models are poorly aligned in terms of CKA.

### Weaknesses
1. The paper only uses cross-entropy (CE) loss to evaluate the merged model, which may be insufficient to capture the model’s true performance, particularly in language modeling tasks. CE loss alone may not fully reflect the merged model’s language modeling and generation quality. Following guidelines from prior work ([1]), it would be beneficial to include additional metrics that measure both the intrinsic quality of the model (e.g., perplexity and accuracy) and the quality of generated text (e.g., diversity and coherence).

2. Since the MoE approach increases the model’s parameter count (potentially doubling it compared to individual models), the observed reduction in loss may be due in part to this increase in model size rather than the efficacy of the MoE merging itself. Interpolation of parameters, by contrast, maintains the original model size, which could lead to an uneven comparison. It would be more informative to compare models of similar sizes to isolate the effectiveness of the MoE merging strategy.

3. While the paper claims that a larger CKA divergence between models degrades the performance of interpolation-based merging, it lacks experimental results to support this claim. Testing model pairs with varying CKA levels (e.g., comparing interpolation results between a GPT-math and GPT-code model versus two similar GPT-code models) would strengthen the case for MoE merging as a preferable alternative. For example, additional experiments can be conduct to verify that when $CKA(GPT_{math}, GPT_{code}) > CKA(GPT_{code1}, GPT_{code2})$, then $Loss(\alpha GPT_{math} + (1 - \alpha)GPT_{code}) > Loss(\alpha GPT_{code1} + (1 - \alpha)GPT_{code2})$.

### Questions
I'm curious that what would the CKA pattern look like for an MoE-merged model compared to an interpolation-based merged model? 

Specifically:
How do CKA values between the MoE model and the original models (A or B) differ from those seen in interpolation-based merging?
Further analysis on these patterns could reveal additional insights into the advantages of MoE merging over parameter interpolation, especially in cross-domain contexts.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies model merging focusing on compatible specialization. The paper points out that as models specialise, the similarity of their internal representations, as measured by centered kernel alignment (CKA), diminishes, and therefore, make it harder to merge with other specialised models. The paper investigates model merging via dynamic routing across different layers but reports limitations to such methods as well.

### Strengths
- The analyses conducted in the paper involving multiple tasks and representation similarity is insightful, motivates future work.

### Weaknesses
 - The experimental design of the study is somewhat weak:
-- The only routing function R studied in this work is a linear transformation which may explain the plateau reported in Fig.5.
-- The paper reports a plateau in Fig. 5 using only 3 points (standard, 2 layers, and 3 layers) but it is unconvincing to report a plateau using only 3 points.
-- Results are reported in validation cross-entropy loss, which is a disadvantage, as that may not necessarily translate to merging of expertise; one or more well defined benchmarks should be chosen that require multiple specializations, to allow more meaningful and comparable results.

### Questions
- Why are results reported in validation cross-entropy loss?
- In response to "Hence, having models directly being representationally compatible both internally and across models appears critical if we want feature space merging. There have been works to improve layer wise compatibility within models (Jiang et al., 2024b), yet we still have no clear way to ensure representations are compatible across models as they specialize during the finetuning process.", what are the trade-offs? Would this compatibility perhaps be at the cost of individual specialisation performance?
- Why are math and coding chosen? One may argue that both tasks have more in common than other tasks.
- Can you list the number of parameters in addition to performance in Table 1? Am I correct in stating that fine-tuning method has less than half of the parameters of the merging method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores certain phenomena related to feature merging within the MoE (Mixture of Experts) architecture. The authors have conducted validation experiments on the GPT-2 model using mathematical and code datasets, arriving at two primary conclusions: 1) As the expert models are trained, the decreasing similarity among expert models affects the performance of merging in MoE architecture. 2) Granting the router more freedom (enabling it to route more MLPs) within the MoE architecture improves the performance of the MoE model.

### Strengths
Pros:
1. Investigating the impact of similarity among expert models in MoE on merging performance is a valuable direction.
2. The concept of cross-layer routing is intriguing and holds potential for developing new methodologies.

### Weaknesses
1. Novelty: The conclusions drawn are not particularly surprising, as similar and more in-depth discussions in MoE research [1,2,3] already exist, especially concerning the form of the router. Additionally, their discussions often relate to practical models or applications, whereas this paper merely performs validation, leaving the content somewhat lacking. I strongly encourage the authors to advance their research further, particularly with the cross-layer router.
2. Scope of the paper: The experiments conducted by the authors are based solely on the MoE architecture for GPT, focusing on feature merging. There is a significant gap between this and another major area of model merging: parameter merging. Moreover, feature merging encompasses many methods not related to MoE. Whether the conclusions drawn from MoE can be generalized to methods across the entire field of model merging is debatable. I suggest the authors clearly specify their focus on MoE in the abstract and introduction to avoid potential misunderstandings.
3. Experimental settings: The use of a relatively small GPT-2 model trained on mathematical and code tasks with SFT, and using validation loss as a metric, is not a common setting. Given the small scale, code and mathematical tasks are particularly challenging for the GPT-2 model, especially with SFT training, which raises concerns about potentially adverse effects on the experimental results. I recommend the authors consider using more traditional, simpler tasks or a larger-scale model.
Typos:
There is a conspicuous error in Figure 3.

### Questions
1. CKA(Centered Kernel Alignment) does not appear to be a commonly used metric for measuring feature distance.  How does it differ from the more commonly used metrics, such as cosine similarity and PCA-based methods?
2. As training progresses, the disparities between expert models become more pronounced. However, this not only poses the drawback of increasingly difficult communication among experts but also offers the benefit of further enhancing the experts' specialized capabilities. How does the author perceive this balance?

### Soundness
2

### Presentation
3

### Contribution
2
