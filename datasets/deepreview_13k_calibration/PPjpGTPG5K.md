# PERFT: Parameter-Efficient Routed Fine-Tuning for Mixture-of-Expert Model

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 3, 8

## Abstract
The Mixture-of-Experts (MoE) paradigm has emerged as a promising approach for scaling transformer-based large language models (LLMs) with improved resource utilization. 
However, efficiently fine-tuning MoE LLMs remains largely underexplored.
Inspired by recent works on Parameter-Efficient Fine-Tuning (PEFT), we present a unified framework for integrating PEFT modules into MoE LLMs.
Our framework, aligned with the core mechanisms of MoE, encompasses a comprehensive set of design dimensions including various functional and composition strategies.
By combining the key design choices within our framework, we introduce Parameter-Efficient Routed Fine-Tuning (PERFT) as a flexible and scalable family of PEFT strategies tailored for MoE LLMs.
Extensive experiments adapting OLMoE-1B-7B and Mixtral-8×7B for commonsense and arithmetic reasoning tasks demonstrate the effectiveness, scalability, and intriguing dynamics of PERFT. 
Additionally, we provide empirical findings for each specific design choice to facilitate better application of MoE and PEFT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors proposed Parameter-Efficient Routed Fine-Tuning (PERFT), a framework of Parameter-Efficient Fine-Tuning (PEFT) strategies for MoE models. Multiple experiments on different datasets and models showed improved performance over baseline methods.

### Strengths
1. The proposed framework makes sense and is technically sound to me.
2. The authors conducted several experiments on multiple tasks to show improved performance.
3. Writing is good and easy to follow.

### Weaknesses
1. The proposed framework is more of a combination of straightforward implementations of different PEFT strategies. I did not find much insight in the current draft. Even though there are several design choices provided in the current draft, these are more of a permutation of different ways adding PEFT to MoE architecture. Both PEFT and MoE have been validated to help and there is no surprise or insight by simply combining them together.  
2. The experimental results are rather inconclusive and task dependent. I am not sure how beneficial it would be to the research community. For example, for PERFT-E  and PERFT-R in Table 1, I am not sure which one is better than the other. What's more, as the authors mentioned in line 418, "These divergent patterns reveal that the optimal configuration appears to be
task-dependent". Without a conclusive design choice or rule of thumb design principal, I am not sure how applicable it would be.
3. Figure 4 is very difficult to interpret. A better design and legend is needed. There are over 10 different color and lines in the figure and without a legend, it is very difficult to keep track of them.

### Questions
Overall, I think the proposed framework is more of a vanilla combination of different strategies without much insight. Please refer to the weakness section for details and prepare rebuttal accordingly.

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
4

### Summary
The paper introduces "Parameter-Efficient Routed Fine-Tuning" (PERFT), a framework for efficiently finetuning Mixture-of-Experts models. PERFT offers a set of strategies tailored to MoE, and claims to reduce the resource intensity traditionally required for finetuning such large models.

### Strengths
The work tries to be one of the first methods to introduces Parameter-Efficient Fine-Tuning (PEFT) methods which are applicable directly and only to Mixture-of-Experts models.

### Weaknesses
Line 31 Mixture of Experts models do not significantly or necessarily reduce computation costs since routing methods may be complex and may not optimize and generalize trivially, and also significantly increase memory costs for both training and inference. This assertion is not entirely correct and forms an inadequate motivation for this work.

Line 38 "Motivation is unclear"
The usage of terms 'dense models' is not explained at the outset but is used all the time. Additionally, the term 'Peft strategies .. tailored for MoE models' remains ambiguous and unmotivated. Does it refer to making specific peft models for mixture of experts models? Why do we need this separation from normal peft models?

Line 47 "...our framework focuses on the core principles and unique
challenges of MoE architecture." - This statement is not followed by any explanation of what these principles and challenges are

The application shown is quite limited (to reasoning tasks). It remains unclear to see if the current methodology is applicable to other tasks and domains as well (Even in simpler tasks like image segmentation or classification), especially in harder tasks like text to image generation and complex vision-language architectures.

MoE models often suffer with training instability[3] and load balancing issues[1, 2] (i.e. uneven load distribution among experts), therefore diverse testing (even on smaller models) is necessary. The paper doesn't provide any analysis of whether this peft methodology acerbates or ameliorates these problems and if it does not improves on these issues, then why not simply apply normal peft methods to individual experts?

"Novelty" I had some difficulty in understanding the novelty of the method introduced. The adapters and the routing mechanisms seem conventional and its unclear what in terms of novelty has been presented in this work (method, theoretical proofs and novel empirical results).

"Increased Complexity" Since, a new routing methodology is to be learnt between the peft modules in addition to the routing between the original experts, the motivation to do so is not explained in the work. Routing mechanism can be infamously hard to optimize and may lack ability to generalize to different tasks. It remains unclear why have this increased complexity in the methodology when a peft model can be learnt for an individual expert and these modified experts be combined in a new mixture. Also, is there any computational and memory advantage (both during training and inference) for using this work's method over learning individual peft for each expert model?

"Readability" The paper is a bit hard to read given often the method and assertions are not well motivated and explained. Terms which may be common to this subfield are not explained initially or in the appendix and are used throughout the paper. For e.g. line 201 - the paragraph "Routing among PEFT Experts" does not explain whether it is important or necessary or not and neither provides any theoretical insight or empirical evidence and just says "This aspect highlights the profound dynamics between routers and experts in MoE and PEFT modules". This does not make much sense for a reader.

### Questions
Please refer to the questions in the weakness section. Improving the readability by stressing on the motivation, novelty and intuition of the method would make this work much better.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a PEFT framework tailored for Mixture-of-Experts (MoE) models.  Within the realm of functional strategies, the paper delves into the internal workings of PEFT modules, encompassing the architecture of individual PEFT experts, the multiplicity of these experts, and the routing mechanisms among them.  On the other hand, the compositional strategies dimension elucidates how PEFT modules interact with the original MoE architecture, exploring configurations such as shared or embedded PEFT experts. The empirical validation through diverse experiments showcases substantial performance enhancements across tasks like commonsense reasoning and arithmetic word problems, underscoring the framework's efficacy in enhancing model training efficiency and scalability.

### Strengths
1. This paper makes some efforts to design some strategies for MoE's PEFT. It  can serve as a benchmark or an empirical report to the community.

2. The authors detailed experiments with many settings on two MoE LLMs, and the figures are well drawn.

### Weaknesses
1. Not well motivated: the authors did not state well or give some experimental evidence about the motivation, objective, and benefits of designing a customized PEFT method for MoE. For example, does the proposed method perform better or computationally cheaper on MoE LLMs compared to the widely adopted vanilla LoRA fine-tuning?


2. Lack of Novelty. Actually, this paper is (A+B) type work. It combines some existing designs in MoE, multiple LoRA, MoE-LoRA approaches.

3. Potentially limited generalizability: Considering that there are many different designs for MoE LLMs such as fine-grained grouped experts, shared experts, and for both the single and multi- task scenarios, I am worried about the scalability of the proposed complex designs to different MoE LLMs. The authors need to add experiments in these different scenarios that I mentioned to address this concern.

4. Not Important and Necessary Research Track: Similar to that mentioned in 1, is it necessary and important to design a customized PETF method for MoE LLMs? Why not use a generalized LoRA setting? Are MoE LLMs so widespread that they can be become a new track out of the common LLMs? Similarly, is a customized PEFT needed for some other architectures like SSM LLMs like Mamba, or in case some incremental new architectures like MoE-SSM come up later on, is a new PEFT needed to be designed?

5. Lack of comparisons and experiments under more scenarios: This paper only compares with different of its own designs, and lacks comparisons with more LoRA variants, multi-LoRA, and MoE-LoRA methods. This makes it difficult to show the superiority of this work. In addition, this paper only experiments on two MoE LLMs, and more types and sizes of MoE LLMs need to be considered, such as Deepseek-MoE, Mixtral 8 × 22B, Qwen1.5-MoE-A2.7B, Qwen 2-57B-A14B, DBRX, and Grok-1.


6. Lack of theory. The paper is all empirical analysis lacking theoretical analysis and support, which is not appropriate to appear in machine learning conferences. In fact, the experimental results and analysis are potentially problematic, and it is unconvincing without theoretical support and analysis.


7. The design of the sub-modules is very confusing, complex and unintuitive. It makes it difficult to understand the connections between the modules, not to mention for other community researchers to use them.

### Questions
See weaknesses. In fact, I don't think this work meets ICLR's acceptance standards at all, and I'm giving br a preliminary score out of kindness.  I think the authors need to devote lots or even rewrite their paper all over again to completely address my concerns.

### Soundness
3

### Presentation
3

### Contribution
3
