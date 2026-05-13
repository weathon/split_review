# SPARC: Continual learning beyond experience rehearsal and model surrogates

- Decision: Reject
- Scores: 5, 6, 6, 5, 5

## Abstract
Continual learning (CL) has become increasingly important as deep neural networks
(DNNs) are required to adapt to the continuous influx of data without retraining
from scratch. However, a significant challenge in CL is catastrophic forgetting (CF),
where learning new tasks erases previously acquired knowledge, either partially
or completely. Existing solutions often rely on experience rehearsal or full model
surrogates to mitigate CF. While effective, these approaches introduce substantial
memory and computational overhead, limiting their scalability and applicability in
real-world scenarios. To address this, we propose SPARC, a scalable CL approach
that eliminates the need for experience rehearsal and full-model surrogates. By
effectively combining task-specific working memories and task-agnostic semantic
memory for cross-task knowledge consolidation, SPARC results in a remarkable
parameter efficiency, using only 6% of the parameters required by full-model
surrogates. Despite its lightweight design, SPARC achieves superior performance
on Seq-TinyImageNet and matches rehearsal-based methods on various CL benchmarks. Additionally, weight re-normalization in the classification layer mitigates
task-specific biases, establishing SPARC as a practical and scalable solution for
CL under stringent efficiency constraints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents SPARC, a continual learning (CL) approach designed to mitigate catastrophic forgetting without relying on experience rehearsal or model surrogates. SPARC proposes task-specific "working memories" and a task-agnostic "semantic memory" to allocate parameters for each task while sharing common knowledge across tasks. Additionally, it introduces a weight re-normalization technique to reduce recency bias towards newly learned tasks. The approach is validated on computer vision benchmarks, where it achieves comparable or superior performance to rehearsal-based methods with a significantly lower parameter count.

### Strengths
- SPARC introduces a rehearsal-free CL approach with a parameter isolation strategy that does not rely on model surrogates, contributing to an efficient model for task-based CL.

- The model achieves competitive results on Seq-TinyImageNet and similar benchmarks with only 6% of the parameters used by comparable full-model surrogates, making it computationally lightweight.

- By incorporating a weight re-normalization technique, the model mitigates recency bias, an issue that often hinders performance in continual learning.

- Although SPARC grows in size as new tasks are added, its growth rate is slower compared to other parameter isolation techniques, which may offer better scalability in extended task sequences.

### Weaknesses
- Task Boundary Knowledge: SPARC requires explicit task boundary information to switch between task-specific sub-networks. This reliance limits its applicability, as task boundaries may not always be available in real-world scenarios, particularly in task-free CL.

- Task-Specificity and Lack of Generalization: The proposed parameter isolation approach is tailored specifically to computer vision tasks and convolutional layers, limiting its generalizability and making it less model-agnostic. This reduces the impact of the approach outside of well-defined task separations in vision applications.

- Batch Normalization and Inference Concerns: Similarly to the previous point, also model’s task-specific batch normalization is handled in an isolated manner, and it is unclear how SPARC addresses batch normalization in a class-incremental scenario. Additionally, the paper lacks clarity on how task-specific parameters managed during inference in class-incremental tasks.

- Misleading Terminology: The term "working memories" suggests dynamic memory allocation; however, SPARC merely allocates parameters to tasks without true memory management. This terminology may create confusion.

- Parameter Comparisons and Experimental Justification: While SPARC's reduced parameter count is a notable advantage, the paper would benefit from greater emphasis and description of this feature. Also, the choice of replay buffer sizes (200 and 500 exemplars) for comparison appears arbitrary, with limited justification. The comparison could be more robust if different buffer sizes were evaluated to understand competitor performance across a wider range.

### Questions
1. How does SPARC manage parameter selection during inference in a class-incremental scenario, particularly when task-specific batch normalization is used?

2. Could you clarify the choice of replay buffer sizes for baseline comparisons? How does SPARC's performance compare when different buffer sizes for ER baselines are tested?

3. While SPARC's reduced parameter count is a notable advantage, the paper would benefit from greater emphasis and description of this feature. From Table 1 it seems that SPARC has 10 times less parameters than a standard Resnet 18, exploited by competitors. I would like  a more detailed comment by the authors on this, which I believe is a central advantage by the model. 

4. What is the computational cost of the  weight re-normalization presented in Section 3.2, and is this something that could have been applied also to competitors?

### Soundness
2

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
3

### Summary
This paper adapts a ResNet architecture for image classification continual learning in a novel way: by maintaining separate weights for each of some number of tasks but sharing a portion of the pointwise convolution filters in depthwise-separable 2D convolutions, which replace standard convolutions in the main blocks of the network. Both the switch to depth-wise separable convolutions and the sharing of some parameters among tasks greatly reduces the overall parameter count, allowing this parameter isolation approach to be relatively scalable even though more parameters are added for each additional task.  Recency bias is also identified as a factor that can limit performance in continual learning, and a weight re-normalization approach is proposed to counteract this. The authors compare their model’s performance with a wide array of baseline algorithms on several benchmarks derived from three datasets, showing that it typically achieves competitive or superior performance with a dramatically reduced parameter count.

### Strengths
1.	Continual learning in resource-constrained settings is an important problem in a number of applications, such as robotics. 

2.	The approach of partial parameter sharing among tasks with depthwise-separable convolutions appears to be novel. This is an interesting strategy because it can reduce total parameter count (thus improving scalability) while striking a tradeoff between general, shared representations and task-specific representations that are less vulnerable to catastrophic forgetting.

3.	Performance comparisons are provided with a comprehensive array of relatively recent baseline algorithms, and the proposed algorithm appears to generally attain competitive or superior performance in both task-incremental and class-incremental settings.

4.	An ablation study is included, which provides insights into the relationship between performance and convolutional layer dimensions, normalization to mitigate recency bias, and parameter sharing among tasks.

5.	The paper is generally well written and easy to follow.

6.	The related work section (parts in the Introduction and "Model Surrogate Bottleneck" sections) is thorough and nuanced, and includes many recent papers.

### Weaknesses
**UPDATE 12/3/2024**: 

Most of the weaknesses below have been addressed. Notable exceptions are: 

(1) A continued lack of error bars/uncertainty estimates (these are present in some of the tables, but are not defined)

(2) Figure 3, which in my view has an inappropriate selection of baselines. It appears to show a clean relationship between model size and performance, but is potentially very misleading because a subset of baselines was seemingly arbitrarily selected to make this point, and none of them are parameter isolation approaches that make sense for comparison with SPARC in this context except for PackNet in the right-hand panel only. There are 4 parameter isolation approaches that the authors tested (see Table 1) that would be more appropriate choices here. 

(3) Poor framing of SPARC in comparison to existing works. The focus on "full-model surrogates" has caused some confusion amongst reviewers and is not particularly helpful in explaining SPARC's contribution - in my view the authors would be better served by focusing on more direct comparisons to existing parameter isolation approaches. 

(4) Terms "working memory" and "semantic memory" are a misleading way to name two of the major components of SPARC, which do not resemble/are not analogous to these concepts as they are defined and commonly used in the behavioral sciences. This was unfortunately not addressed during rebuttal although it was noted in initial reviews by two reviewers. 

To summarize, SPARC is an interesting and novel approach that could make a useful contribution, but the paper is limited primarily by concerns around presentation that were not adequately addressed during the rebuttal phase - in my view, all four of the above weaknesses must be addressed before final publication. To reflect this, my finalized overall score is ``marginally above the acceptance threshold'' but my finalized score for "presentation" is "poor."

**Original weaknesses section**:

The paper has a number of score-limiting weaknesses, particularly regarding the justification and framing for the proposed approach and in the ways certain results are presented. It is not clear the extent to which the performance and scalability of SPARC is related to the novel aspects of its design, and several key conclusions are poorly supported by the results – of particular concern are both panels of figure 3 (details below).  

1.	The authors seek to differentiate their approach from those requiring “full model surrogates” for each task, and one of their central claims is that SPARC is parameter efficient and scalable. SPARC appears to have fewer parameters than competing approaches primarily because of the switch from full convolutional layers to depthwise-separable convolutional layers, which is not in itself novel. Parameters are reduced further (to a more modest degree) by having a task-agnostic portion of the pointwise convolutions (which carries only a small performance penalty based on table 5), but the number of parameters still grows linearly with the number of tasks. From one perspective, SPARC could be characterized as requiring an almost full model surrogate for each task except for a shared portion of the pointwise convolutions. 

2.	There is a claim that SPARC works for class-incremental learning (i.e., without access to task information), and the requirement of knowing task identity during inference is cited as a disadvantage of existing parameter isolation approaches. However, it is not clear how SPARC can do inference across multiple tasks without knowing task identity – how does it know which set of task-specific parameters to use for each input?  This applies to depth-wise convolution parameters, the task-specific portion of the point-wise convolution parameters, and the batch norm layers. It is not clear to this reader that the method is strictly capable of class-incremental learning. 

3.	The re-normalization approach to mitigate recency bias (as described in equation 5) does not seem fully explained/justified. Why this new approach instead of the many existing methods to mitigate recency bias? For example, the authors could consider citing papers such as the following and distinguishing their approach from them: 
a.	Wu, Yue, Yinpeng Chen, Lijuan Wang, Yuancheng Ye, Zicheng Liu, Yandong Guo, and Yun Fu. "Large scale incremental learning." In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 374-382. 2019.
b.	Zhao, Bowen, Xi Xiao, Guojun Gan, Bin Zhang, and Shu-Tao Xia. "Maintaining discrimination and fairness in class incremental learning." In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 13208-13217. 2020.
c.	Mai, Zheda, Ruiwen Li, Hyunwoo Kim, and Scott Sanner. "Supervised contrastive replay: Revisiting the nearest class mean classifier in online class-incremental continual learning." In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 3589-3599. 2021.

4.	Related to the preceding point, the right-hand panel of Figure 3 does not convincingly show that weight re-normalization offers any advantage in terms of performance. This plot seems ambiguous – what do the error bars mean, and why is the violin plot seemingly truncated at the error bars? This is supposed to show distributions of final task accuracies, but what is the distribution over – different training runs, different batches, different tasks? There are also no statistical tests to verify whether there is a significant difference with vs without normalization. In the “Impact of weight re-normalization” section, it is stated that “As shown, weight re-normalization reduces the IQR for all three task sets, leading to a more balanced distribution of accuracies and lower task recency bias” – however, this is not consistent with what is shown in the figure (the IQR appears identical with vs without normalization for the 5-task set, and there is nothing to indicate quantitatively that performance on earlier tasks is specifically boosted in this figure). Figure 6 in supplementary partially addresses this, but only by comparing with other methods rather than in an ablation study of SPARC. 

5.	The left-hand panel of figure 3 appears, at least superficially, to compellingly show that the relative model size is related to the relative class-incremental learning performance, except that SPARC bucks this trend by having high performance and low model size. But why were these specific continual learning approaches selected for inclusion in this plot?  Included in this plot are some, but not all, of the models from the “rehearsal-based with 200 buffer size” section of Table 1 (starting with “ER”) – this seems to be an odd set of choices, as I would think that relative model size is much less relevant for rehearsal-based approaches than for parameter isolation or “model surrogate” approaches.  Unless there is a strong justification for the choice of models used in the current version of the figure, I think including a wider range of baselines in this figure is necessary, and/or with a more appropriate selection of baselines. 

6.	There are some additional issues with error bars/estimates. For Tables 1, 2, 5, 6, and 7, it is not stated what the +- error measurements are (standard deviation, standard error, confidence interval?). Figure 2, Figure 3 (left), Figure 4 (left), and appendix figure 6 all lack error bars, and in the figures where error bars are shown, they are not defined. 

7.	SPARC is specifically designed for ResNet18, and thus is only evaluated using one CNN architecture (although it would seem possible to implement SPARC for other CNNs). However, ResNets are among the most widely used CNNs so this is not necessarily a major issue. 

Minor comments: 

8.	There is a statement that, according to complementary learning systems (CLS) theory, slow-learning neocortex and fast-learning hippocampus work together to allow continual learning without explicit experience rehearsal. However, it should be noted that hippocampal replay is frequently invoked in discussions of CLS theory as a possible mechanism for transfer of learned information from the hippocampus to the cortex. 

9.	“Working memories” might be an unintentionally misleading term for the disjoint sets of parameters. In the context of human cognition, the term "working memory" means something very different in that it is an extremely short-term form of storage of very limited amounts of information. Similarly, “semantic memory” typically refers to a type of declarative memory involved in the ability of humans to recall facts, words, numbers, concepts, etc. – while what is stored in the task-agnostic parameters of SPARC is closer to a form of procedural memory (“how to distinguish class 1 from class 2”). Overall, the way that the design of SPARC is analogized to human memory systems should probably be reconceptualized. 

10.	There is a statement in section 2 that “maintaining a buffer raises privacy concerns and resource overhead.” It would seem that privacy is only an issue in some but not all continual learning applications (although it can be quite important, e.g. in clinical applications)

11.	typo “connection disbled” in legend of Figure 1

12.	There are some duplicate citations including both the preprint and the journal/conference version of the same paper, it is not necessary to include both (e.g., Chollet et al. “Deep learning with depthwise separable convolutions”, Guo et al. “Depthwise convolution is all you need for learning multiple visual domains”).

13.	In Table 1, ideally there would be citations for each baseline method in the table itself so it’s easy to figure out which one is which (especially given the abbreviated names, not all of which seem to be stated in the main text). All baselines should be cited in the main text – for example, ER-ACE is cited in the appendix but I can't find it anywhere in the main text except table 1.

### Questions
1.	At the end of section 3.1, referring to the final fully-connected layer: “Cross-task connections are discarded to avoid interference” – what does "cross-task connections" mean for a single FC layer?

2.	Some of the equations in the paper are not fully explained:
a.	In equations 1 and 2, F, O, and the two Ks are explained, but not h, l, m, n, I, and j. Does t refer to the task? Similar issues with later equations. 
b.	In equation 5 (sec 3.3), what is the dimensionality of $A^t$, the number of training examples? Or is it number of batches (where each batch provides one “iteration”)? 
c.	Also in equation 5, what is the reasoning behind adding $A^t_{0.75}$ and $A^t_{IQR}$? Assuming this calculation makes sense, why not just take $A^t_{0.75} + A^t_{IQR}$ instead of finding a value “a” in $A^t$ that is close to this value? 

3.	In the right-hand panel of figure 4, what is S? (this should be more clearly indicated)

4.	In the section “Effect of semantic information consolidation”, it is stated that “The difference in terms of the number of parameters will be even more pronounced in longer task sequences”. This appears to be speculative, with no theoretical or empirical justification. Wouldn’t the difference between shared parameters and separate parameters actually be smaller with more tasks, as task-specific parameters take up a greater proportion of the overall number of parameters while shared parameters stay the same in number? Why would we expect the performance gap to be smaller with more tasks (compared to fully separate point-wise convolutions)?

5.	The design of Table 2 is challenging to understand – why do versions with a width factor of ¼ appear in the top and bottom sections of the table but not the middle one? There is also a duplicate row (the highlighted row in the bottom section is identical to the last row of the middle section). Explaining the notation would be helpful – what exactly does # filters per task mean – does it refer to the dimension of the point-wise convolutions, or the spatial ones? 

6.	There are separate depth-wise convolutional filters for each task, while only the point-wise convolutional filters have some shared parameters among tasks. It is not clear how much of the claimed parameter efficiency gains are because of SPARC’s unique approach and how much is just from the switch to depth-wise separable convolutions instead of standard convolutions. 
a.	It might be helpful to explain how many of the parameters overall are in the depth-wise filters vs the point-wise filters – for example, if it so happens that many of the parameters are in the point-wise filters and the depth-wise filters have few, this helps justify the parameter sharing approach. How does the growth in parameters with the number of tasks compare to other methods in a quantitative sense? 
b.	It seems like the number of parameters grows with the number of tasks in a similar way to how approaches involving “surrogate models” would grow, but then this is counteracted by the greatly-reduced amount of parameters from switching to depth-wise separable convolutions. One way to think about it: is this approach more parameter-efficient than just switching to depth-wise separable convolutions and then using something like EWC on that architecture?  

7.	Related to the preceding point, Table 4 does not appear to make a compelling case for SPARC’s scalability. SPARC does have many fewer parameters overall, but this seems to be mostly attributable to using depth-wise separable convolutions rather than parameter sharing across tasks – indeed, according to table 5, the number of parameters is still only 1.65M even if point-wise and depth-wise filters are completely separate for each task. Taking this into account, the growth in parameters with the number of tasks in SPARC (e.g., relative to baseline with 5 tasks) appears large compared with other methods. 

8.	Related to the preceding point and to weakness #5 – what is the justification for the chosen set of baselines in Table 4 and left panel of Figure 4?

9.	From the start of section 3.1: “We assume prior knowledge of the number of tasks and task boundaries to evenly distribute learnable parameters across tasks.” Does this limit scalability in a practical sense, because you have to begin the training process already knowing how many tasks there will be?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel framework called SPARC to address exemplar-free continual learning. They employ depth-wise separable convolutional layers to reduce the number of learnable parameters, enabling the allocation of distinct subparts of the model to different tasks, thereby mitigating interference issues. Additionally, task consolidation is encouraged through partial weight sharing and normalization techniques applied to the classification head. Experimental results demonstrate that SPARC’s approach to network expansion is highly efficient and scalable -- employing only 1.04 million parameters compared to 11.23 million for ER and 33.6 million for PackNet. In terms of accuracy, SPARC achieves promising performance, although it is not consistently optimal.

### Strengths
- The paper is well-written, with only a few minor clarity issues (detailed below).
- The approach is technically sound and, to the best of my knowledge, fairly novel.
- The underlying problem of continual efficient learning is significant and warrants attention.
- The paper includes extensive ablation studies that highlight the advantages of this scalable approach, particularly in reducing the number of learnable parameters.

### Weaknesses
**Limited applicability**. I believe the range of possible applications for SPARC may be significantly restricted due to several assumptions that could limit its practicality.
- The approach is specifically designed for CNNs and lacks support for ViTs.
- SPARC requires training the backbone from scratch; unlike other methods, it cannot leverage pre-trained backbones (e.g., those pre-trained on ImageNet or visual-language tasks like CLIP).
- The authors acknowledge that SPARC requires prior knowledge of the number of tasks. In my experience, this is an uncommon and impractical requirement, as most existing methods avoid this constraint. From a technical standpoint, could the authors explain why this prior knowledge is necessary? Additionally, could they consider developing an alternative that removes this requirement?
- SPARC also requires identifying task boundaries, which, while a limitation, is a common issue across most existing methods. Therefore, I view it as the least impactful limitation among those mentioned above.

**Accuracy and comparison with state-of-the-art methods** My second main concern pertains to SPARC’s performance in terms of final classification accuracy. While its efficiency and scalability are noteworthy, its accuracy appears suboptimal. For example, on Seq-CIFAR-10, SPARC's performance lags 12 points behind OCDNet. Additionally, I question whether the competitors employed by the authors truly represent the current state of the art in non-exemplar class-incremental learning (NECIL). Several recent publications (from 2023 and 2024) report considerably higher accuracy on CIFAR-100 and TinyImageNet:

- SOPE (CVPR22, 154 citations):
Zhu, K., Zhai, W., Cao, Y., Luo, J., & Zha, Z. J. (2022). Self-sustaining representation expansion for non-exemplar class-incremental learning. CVPR, pp. 9296-9305.
- Fetril (WACV23, 112 citations):
Petit, G., Popescu, A., Schindler, H., Picard, D., & Delezoide, B. (2023). Feature translation for exemplar-free class-incremental learning. WACV, pp. 3911-3920.
- PRAKA (ICCV23, 16 citations):
Shi, W., & Ye, M. (2023). Prototype reminiscence and augmented asymmetric knowledge aggregation for non-exemplar class-incremental learning. ICCV, pp. 1772-1781.
- PKSPR (AAAI24, 5 citations):
Zhai, J. T., Liu, X., Yu, L., & Cheng, M. M. (2024). Fine-Grained Knowledge Selection and Restoration for Non-exemplar Class Incremental Learning. AAAI, Vol. 38, No. 7, pp. 6971-6978.

**Clarity issues**
- Regarding weight re-normalization, the explanation for the normalization applied in Eq. 5 is unclear. The authors’ comment (lines 264–267) merely summarizes the procedure, leaving the rationale and benefits unexplained.
- SPARC allocates specific filters to each task. However, in Class-IL settings, the task ID is not provided during evaluation. How did the authors address it? How did they select filters? The solution is not clearly explained.
- (Minor) Fig. 3 is difficult to interpret when printed in black and white (whereas Fig. 4 remains readable).

**Minor suggestions**
- It would be interesting to see also the results of JOINT with the SPARC’s backbone ( Table 1). Currently, the JOINT upper bound in Table 1 appears to use the standard ResNet-18 architecture.

**Justification of rating** While the technical contributions of this work are notable and address an important problem -- enhancing efficiency in continual learning -- the limitations affecting SPARC’s applicability are substantial. Furthermore, the experimental comparison does not seem fully aligned with recent advancements in the NECIL field. These factors raise concerns about the potential impact of this work within the community.

### Questions
No questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to mitigate catastrophic forgetting in continual learning. It proposed a new method called SPARC that (1) modifies the model architecture (2) maintains working memories and (3) normalizes classification layer's weight. The experiment results show that SPARC outperforms baselines in standard benchmark while maintain parameter efficiency.

### Strengths
1. The proposed method does not require an additional memory buffer, which is efficient.
2. The experiment results show that the proposed method outperforms baselines in standard benchmarks.
3. Detailed ablation studies and additional experiments to analyze and support the proposed method.
4. Honest and sufficient Limitation section that states the shortcomings of the proposed method.

### Weaknesses
1. The proposed method is only discussed for ResNet-18, and seems to be customized for ResNet structure. It limits the usage of the proposed method for other models like transformers, and other fields like natural language processing.
2. In Section 3.1, it describes why uses DSC to replace traditional convolutions for several reasons. However, it is not clear why the replacement is necessary for continual learning. Meanwhile, it's unclear whether the performance improvement comes from the DSC or the proposed algorithm.
3. In Table 1, it shows that SPARC's number of parameters is smaller than baselines. However, I believe this is because it replaces normal ResNet-18's convolutional layers by DSC, not because of the efficiency of the algorithm.  
4. As described in the Limitation section, model parameters increasing linearly when learning more tasks, which put the scalability of the proposed method in question.

I am willing to increase my score if questions are answered.

### Questions
1. The definition of "model surrogate" is missing and unclear. From the description of Section 2 and Introduction section, I guess it's parameters of the old tasks or something related. 
2. Weight renormalization is proposed before [1]. While it's only a preprint, the paper is still useful and it would be nice if authors can discuss the difference between their proposed normalization method and the previous work.
3. I recommend to adjust the color and improve the presentation of Figure 1, since the current version is hard to understand.

### Reference
[1] Continual Learning in Deep Networks: an Analysis of the Last Layer, arXiv preprint arXiv:2106.01834 (2021).

=====
After discussion, the authors propose to improve some unclear part and give clearer explanations, so I increase the score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on continual learning, leveraging task-specific information as memory for cross-task knowledge consolidation. The proposed method eliminates the need for memory-intensive experience rehearsal and model surrogates, while minimizing forgetting. Empirical evaluations on various continual learning tasks demonstrate the method's superior performance in terms of accuracy and parameter efficiency.

### Strengths
The discussion on rehearsal memory is well-supported with sufficient related work and analysis. The study of rehearsal-free continual learning methods is important.

### Weaknesses
The method still relies on task boundary information for task-specific model learning, and further investigation into this aspect and relevant work is not provided.

### Questions
1. The complementary learning systems theory has been implemented in many recent continual learning studies such as Remembering Transformer. On Line 66, only distant studies were mentioned and the most recent ones are missing.

2. Parameter isolation has been studied extensively. Could you provide further clarification on how the trade-off between performance, model size, and the model's accessibility to task boundaries evolves in your approach?

3. The evaluation lacks key metrics such as forgetting rates, which are essential for assessing continual learning performance.

4. It is unclear whether task similarity-based weight reuse is applicable within the proposed framework, given the delicate nature of the proposed method such as using the task-agnostic pointwise filters. Could you clarify what regulations or conditions would be needed to enable this?

5. In Table 1, the performance on class-IL appears to be lower than some previous methods, both those included in this work and others that are not. For instance, accuracy scores of 61.22 and 49.03 are relatively low even for the class-IL tasks. Could you provide further clarification on this point, along with additional comparisons to more recent and stronger baselines?

### Soundness
2

### Presentation
3

### Contribution
2
