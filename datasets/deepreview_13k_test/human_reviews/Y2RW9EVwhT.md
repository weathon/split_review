# Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders

- Decision: Accept
- Scores: 8, 6, 8, 6, 8

## Abstract
The ability to accurately interpret complex visual information is a crucial topic of multimodal large language models (MLLMs). Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. A number of recent MLLMs achieve this goal using a mixture of vision encoders. Despite their success, there is a lack of systematic comparisons and detailed ablation studies addressing critical aspects, such as expert selection and the integration of multiple vision experts. This study provides an extensive exploration of the design space for MLLMs using a mixture of vision encoders and resolutions. Our findings reveal several underlying principles common to various existing strategies, leading to a streamlined yet effective design approach. We discover that simply concatenating visual tokens from a set of complementary vision encoders is as effective as more complex mixing architectures or strategies. We additionally introduce \textit{Pre-Alignment} to bridge the gap between vision-focused encoders and language tokens, enhancing model coherence. The resulting family of MLLMs, \textit{Eagle}, surpasses other leading open-source models on major MLLM benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper conducts a systematic study on the **mixture of vision encoders** in multimodal large language models (LLMs). Specifically, the paper thoroughly compares the performance differences between various combinations of vision encoders and fusion methods, ultimately finding that simply concatenating the tokens from different encoders outperforms more complex fusion strategies. To bridge the gap between different vision encoders, the authors propose a **pre-alignment** strategy, which enhances the subsequent collaboration between vision encoders by aligning them with a small LLM in advance. The proposed method demonstrates significant improvements across several metrics.

### Strengths
This paper provides a detailed and systematic study on the **mixture of vision encoders**, offering valuable insights to the research community.

### Weaknesses
1. **Limited novelty**:  
   While the primary contribution of this paper lies in the extensive comparisons and ablation studies, the method itself lacks significant innovation. Technically, it does not introduce any groundbreaking insights for the community.

2. **Flaws in Experimental Setup**:  
   There are some flaws in the experimental setup. In the comparison shown in **Table 5**, the configuration using pre-alignment includes an additional **stage 1** of training compared to the configuration without pre-alignment, leading to an imbalance in the amount of training. It is recommended that the authors add a setup where **stage 1** is removed and **stage 3** is trained for an additional epoch to eliminate the unfair advantage of extra training rounds. Furthermore, since the vision encoders are pre-aligned in **stage 1**, why is it necessary to retrain in **stage 3**? What would happen if the vision encoders were simply frozen?

3. **Computational and Memory Costs**:  
   Since the proposed method involves mixing multiple different vision encoders, the computational and memory costs during training and inference are important factors to consider. When comparing with other methods, these indicators should be included. Additionally, it would be helpful to provide the computational cost and memory usage for each combination in **Table 6** for a more comprehensive evaluation of different vision encoder combinations. **Table 6** shows that the performance difference between five encoders and three encoders is minimal. If the cost is significantly higher, is it necessary to use the combination of five encoders?

4. **Omission of a Key Model**:  
   **SigCLIP** is one of the widely used vision models for MLLMs. Why is it not included as an option in **Table 2**?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

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
The authors present an extensive study of mixture of encoders, providing ablations and experiments on various design choices. The authors recommend interpolating for higher resolutions, having a higher number of vision encoder experts, concatenating tokens in a channel-wise manner, and also compare training strategies. The method is compared against a lot of recent advances in this space, and has competitive performance on a variety of benchmarks.

### Strengths
- The paper is well articulated, with various steps properly backed up with experiments, and compared against significant number of baselines. The results indicate that the approach performs better than other mixture of vision encoders works. 
- The better performance of interpolation over tiling in the initial steps is an important contribution towards efficiency, and is much appreciated
- The paper addresses an important issue, with multiple strides in the space of multimodal LLMs, it is essential to incorporate the best set of changes that work well together, and this paper is a good step towards this goal.
- Well written paper, easy to read

### Weaknesses
I will combine weaknesses and questions here:

(1) My major primary concern is about the efficiency of the approach, and I will list it below as a two-part concern - 

- (**Most Imp Concern**) Fig 4 mentions the various combinations tried in the mixture of vision encoders. As compared to the 2 encoder setting (X2), the next mixture (X3) leads to a slight improvements at the expense of 50% reduction in throughput, and going further, X5 leads to more than 4x reductions in throughput. While the results in terms of accuracy improve, as also suggested by Table 6, it comes at a significant compute expense. It would be important to understand the author's perspective on this agenda. Additionally, in Table 6, it would be useful to mention the throughput of other baseline methods, wherever possible. In my humble opinion, if the proposed method has a severely lower throughput (high inference cost), it should also be compared against other methods having comparable throughput when comparing accuracy metrics.
- The paper suggests that unfreezing leads to better performance, however, it also increases the number of trainable parameters. The authors should provide details on the training overhead that this change leads to, so as to better understand the efficacy of the slight improvement.

(2) The motivation behind introducing the Deformable Attention baseline is unclear and the comparisons made with it are limited. Additionally, to motivate channel concatenation further over sequence concatenation, quantitative comparisons of the implications of handling longer sequence lengths would be helpful.

### Questions
Please see the weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper's findings reveal several underlying principles common to various existing strategies, leading to a streamlined yet effective design approach. The paper discovers that simply concatenating visual tokens from a set of complementary vision encoders is as effective as more complex mixing architectures or strategies. Additionally, the paper introduces Pre-Alignment to bridge the gap between vision-focused encoders and language tokens, enhancing model coherence. The resulting family of MLLMs, Eagle, surpasses other leading open-source models on major MLLM benchmarks.

### Strengths
1. This paper has confirmed through comprehensive and integrated experiments the necessity of turning on vision encoders during the SFT stage. At the same time, the paper has discovered and validated that straightforward channel concatenation stands out as a simple yet competitive fusion strategy, offering the best efficiency and performance.
2. This paper proposes a pre-alignment stage where non-text-aligned vision experts are individually fine-tuned with a frozen LLM before being trained together.
3. The illustrations in this paper are accurate and concise, and the language expression is very refined, making it easy for people to understand.

### Weaknesses
1. Some details of the methods are missing. How are the projectors of each expert in stage 1 of Figure 3 dealt with in stage 2?
2. Some corrections to details. In Table 4 at line 317 of the text, it looks like it should be referring to Figure 4. The same applies below.

### Questions
## Justification For Recommendation And Suggestions For Rebuttal：
- Justification For Recommendation：Reference to Paper Strengths.

## Additional Comments For Authors：
It would be better to add the results of some other models that also use many vision encoders for comparison in Table 6.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper conducts an empirical analysis study on the design space for integrating vision encoders for MLLMs. It optimizes the training recipes of individual vision encoders step by step, identify an extendable and efficient fusion method, and gradually combine vision encoders with different domain knowledge. Built upon these findings, this paper propose Eagle, the results somehow show the importance of basic design space.

### Strengths
Strength：

1. Extensive experiments demonstrate the importance of optimizing the design space of vision encoders.
2. The ablation studies are abundant.
3. This paper is well-organized and clearly-written.

### Weaknesses
Weakness:

1. The contribution is limited. PrismaticVLM[1] conducts similar empirical study on MLLMs, especially on the vision encoders. Although they only explored the combination of two encoders, they have achieved significant improvements while keeping a good efficiency. This paper extends the mixture of encoders up to six, but the performance only increases from 681.5 to 697 as shown in Fig.4, which is somehow trivial from my perspective. What's worse, it brings double parameters and slows down the inference by more than four times. 
2. Missing related discussion. It is really strange there is not any discussion with PrismaticVLM, considering these two paper focus so closely.

[1] Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models. ICML 2024

### Questions
Please see the comments above.
My main concern is weakness 1, for such reasons i don't think this paper's contribution can lead to an acceptance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores strategies to inject information (visual tokens) from a mixture of pretrained visual encoders (experts) into LLM’s (Vicuna-12B) for finetuning MMLM’s. Namely, they explore how to incorporate: 1) High Resolution inputs which are needed for text understanding. 2) A number of visual encoders. Based on their ablation strategies, they propose the following training recipe.

* Simple linear interpolation for adaptation to high resolution.
* Unfreezing the image encoder instead of just the projection layer
* Channel concatenation to incorporate multiple vision encoder outputs.
* Prealigning the visual encoders with a LLM.
* Simple greedy strategy to incorporate multiple vision experts.

### Strengths
The paper is well written. They start with a base clip image encoder model and build towards the final recipe using careful ablations. They show that a simple recipe without any fancy tricks can lead to strong performance on a number of benchmarks. The paper also achieves strong performance on VLM benchmarks and is likely to have an impact on multimodal LLMs.

### Weaknesses
The clarity over some of the details in the paper can be expanded upon. See below for detailed feedback.

### Questions
The clarity over some of the details in the paper can be expanded upon.

* It’s a bit worrisome that the benchmark used to arrive at the recipe (Table 2-5 and Fig.4) is the same benchmark used in the final results (Table 6.). This would be great if authors confirm that the validation set is used for Table 2-5 and Fig.4 and the test-set for Table 6 or provide some evidence that the recipe is not overfitting to this particular benchmark.
* There is a final finetuning stage where the entire model, i.e LLM + projector + vision encoder is finetuned. In Table 7, it is mentioned that this is done on Eagle 1.8M, however on L141-L142, it is mentioned that this is done on multi-model conversation data. Further clarification on this will be helpful.
* Similarly, in Table 7 the best model is pretrained on LLava-595K + Eagle 1.8M. However, it seems Table 2-5 and Fig 4, the recipe is arrived at by only pretraining on Eagle 1.8M. Can the authors confirm this and clarify this in the paper?
* What is the effect of unfreezing vs freezing the image encoder on training time? Table 2 shows the number of flops are the same for both freezing and unfreezing. But while unfreezing one has to backpropagate through the encoder , so the flops should be different.
* What is the difference between 5th row of Table 5 (Unfreeze yes + prealign no + clip + convnext) and 2nd row of Table 4? In both cases, clip + convnext is used with channel concatenation and pre-alignment switched off. So why are the numbers different?
* The empirical comparison of flops between tiling and interpolation is provided in Table 2. I assume there is a tradeoff in the sense that tiling requires more forward passes but the self-attention might be less expensive because of the lesser number of tokens . So It would also be nice if some theoretical comparisons are also provided between interpolation and tiling with respect to number of tokens and resolution.
* I may have missed it but was the size of the Clip encoder L? And what resolution was the pretraining done on?

### Soundness
3

### Presentation
4

### Contribution
3
