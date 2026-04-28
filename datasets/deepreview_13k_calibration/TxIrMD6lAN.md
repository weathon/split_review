# Incremental Learning with Task-Specific Adapters

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3, 3

## Abstract
Incremental learning aims to continuously acquire new knowledge while preserving previously learned information. Existing literature primarily focuses on improving model stability,  often at the cost of plasticity, to prevent the forgetting of earlier tasks. In this paper, we argue that inter-task differences are the primary driver of catastrophic forgetting. To address this challenge, we propose a novel network architecture compromising  two distinct components: one dedicated to learning invariant features shared across tasks and another for capturing task-specific details. Specifically, we repurpose adapters, originally introduced for parameter-efficient fine-tuning, as feature modifiers to capture task-specific details, while the backbone network focuses on learning invariant features. Unlike prior approaches that keep the backbone frozen and only fine-tune {adapters}, we co-train both the backbone network and adapters, employing an additional regularization term that encourages the backbone to learn shared features.   Our approach integrates seamlessly with established methods, such as Learning without Forgetting (LwF). Extensive experiments on CIFAR-100 and ImageNet datasets demonstrate that our adapter-based methods consistently outperform non-adapter counterparts across diverse learning scenarios, including various task orders and data scales. Our approach improves both plasticity and stability, effectively addressing the stability-plasticity dilemma.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper tries to access continual learning with the perspective on the 'plasticity' instead of 'stability', which is under explored perspective in the regularisation based methods. To increase the plasticity while minimising the memory consumption required by the proposed method, the authors incorporate the Parameter Efficient Finetuning (PEFT) modules into the incremental learning. The authors introduce the co-training for dividing the role of back bone and PEFT module. The authors validate the proposed methods on diverse datasets.

### Strengths
1. The paper is well organised and easy to follow.
2. The authors tried to visualise the results.

### Weaknesses
1. Lack of literature search/comparison with existing methods. The fields of continual learning is now gathering a lot of attention in ML community, which means there are plenty of literatures which deals with various perspective. While authors states that the role of plasticity is under-estimated, it is definitely not true. The community tried to increase the plasticity with various approach including architectural expansion or using PEFT modules. There are so many such papers so that I can not even cite them here. However, authors did not cite, discuss or compare them at all which makes me hard to evaluate the contribution of this paper. While I believe that regularisation approach is no more mainstream of continual learning research, the authors did not even compare with the current regularisation approaches. The methods they compare are EWC, LwF things which are far outdated. If the authors conducted some kinds of theoretical research, I might be convinced with these kind of experimental design. However, what authors are doing is proposing practical component for continual learning. In this case, the authors should compare with at least 'recent' (maybe not state of the art) methods.

2. Lack of novelty/Naive approach. As I mentioned in 1, there are plenty of methods that incorporates PEFT modules for Continual learning. Hence, naively integrating with small modification does not have contribution. Also the authors should clarify how the modules are used during inference. According to adapter regularisation, it seems that the authors retain all modules trained so far, however it is not clear how they use the modules for inference, e.g., how they select or integrate.

### Questions
See the weakness section

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a method for incremental learning by utilizing task-specific adapters in a neural network architecture. This approach is designed to mitigate catastrophic forgetting, a common issue in incremental learning, by combining invariant feature extraction with task-specific modifications introduced through adapters. The authors implement this adapter-based framework on mainly two incremental learning algorithms (i.e.  EWC and LwF), and report improved performance on CIFAR-100 and ImageNet datasets.

### Strengths
The paper aims to address a critical issue in incremental learning: the stability-plasticity dilemma. Task-specific adapters, in this context, are a promising approach to balancing stability and plasticity.

### Weaknesses
 - I am not convinced by the argument that "existing literature primarily focuses on enhancing model stability to prevent catastrophic forgetting of earlier tasks, often overlooking the challenges posed by inter-task differences." There are several methods in the literature that address the stability-plasticity dilemma using task-specific and task-agnostic components, such as [2-3]. I recommend revising the abstract to focus more specifically on the paper's unique contributions.
- Recent adapter-based methods, such as TAMiL [2], DualNet [3], L2P [4], DualPrompt [5], InfLoRA [6], which are tailored for similar continual learning scenarios, could provide a stronger and more relevant comparison.
- Some sections, such as the descriptions of evaluation metrics and adapter initialization, could be condensed or included in an appendix.
- Novelty is questionable, given the incremental contributions relative to existing approaches.
- Although simplicity can be valuable, a thorough analysis is essential to demonstrate whether this proposal performs on par with or better than competing methods.

- Related Works:
     - It is unclear how multi-task learning is directly relevant to this method.
     - Many of the cited works are from before 2020. Please consider referencing more recent studies to support your points and provide a stronger baseline comparison.
     - For parameter-efficient fine-tuning (PEFT) and adapter-based methods, please compare your work with approaches mentioned in [1] and methods applied to CNNs [2].
- The main problem outlined in Line 129 should be reiterated throughout the paper to maintain focus.
- The claim regarding LwF’s limited adaptability due to increased inter-task diversity (Line 158) is unclear. Please explain how this inference was made.
- Methods Section:
     - The explanation of how adapters are co-trained with the entire network is unclear. How is forgetting in the backbone managed, if at all?
     - If there is no such strategy, how does this differ from methods like [2] that also apply task-specific modules in CNNs?
     - Consider reducing emphasis on the adapter design, as it seems straightforward. Instead, provide more detail on how adapters are co-trained, their effect on overall training, and why they are expected to capture task-specific information.

- The choice of baselines, specifically EWC and LwF, may be insufficient, as these methods are now somewhat dated. The absence of recent incremental learning methods reduces the comparative strength of the paper.
     - The statement in line 328-330 regarding the choice of EWC and LwF as baselines "... owing to their superior performance among ..." is debatable and may not hold up with recent literature.
- The method uses two hyperparameters for regularization losses, but only one is reported in Table 3, with no specification for different datasets. This table also shows a high sensitivity of the methods to hyperparameter choices.
- The rank of the adapter, another hyperparameter, exhibits considerable sensitivity to the dataset (and possibly to the architecture, such as ResNet-18 vs ResNet-34), which should be addressed​.
- The authors use a higher-capacity CNN for CIFAR-100 and a smaller version for ImageNet. This is unusual, as recent literature typically applies the same model across datasets. This choice could impact the results and comparisons and should be justified.
- There is no explanation on how task IDs were inferred at inference when these IDs are not given.
- In Figures 5 and 8, the titles of the subplots are incorrect, as they refer to tasks instead of classes, which could mislead readers.
- In multiple instances, the adapter worsens the results, such as in Figure 6 (for EWC and MAS) and Table 1 (for LwF and LwM), with similar patterns in Table 4, Figure 7, and Figure 8 (middle plot). These results indicate that adapters may not consistently enhance performance and may even hinder it in certain cases.
- The results for Class-IL are generally less convincing, as performance is either very marginal in most cases or worsens when using an adaptor compared to Task-IL. This undermines the proposed method’s claim of broader applicability.

### Questions
in addition to the weaknesses mentioned above:

- Could you clarify what is meant by “feature extraction (Line 38)”? This could improve the overall clarity of the text.
- The claims made in Introduction (Line 58) are only applicable to regularization and distillation-based methods. Please specify this explicitly and make the scope clear in both the abstract and introduction.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the class incremental continual learning problem. To tackle the catastopic forgetting problem, the paper used adopters to add new knowledge to the model and keep the old knowledge without forgetting. The paper is well written and has good amount of experiments to show the benifits use of adoptors for the continual learning problem.

### Strengths
the paper is well written and the experiments are suffently done to show the benifits of the adopters for continual learning. 

It is nice that the paper evaulates the methods, on Imagenet and higher 224 resolution than 32x32 images on CIFAR100. 

figure 5, also shows that this approch works with different sizes for each tasks, such as 5,10 and 20.

### Weaknesses
please address the similarities and difference between the following works, they share similar flavors to this work and they are discussed. Specifically, side-tuning is very close to this approch would be nice to compare, if not it should be discussed.
Random path selection for continual learning, NurIPS 2019
Side-Tuning: Network Adaptation via Additive Side Networks, ECCV 2020

also would be nice to show that this approach can work for other architectures like vit. I believe it should work without any problems.

for figure 3, it would be nice to show the width on x axis, to show that there is a optimal middle point where the loss in performance is minimal on average.

this might be outside of this papers scope, but is it necessary to add the adopters for every task? is there any conditions that can be used to makes sure the adopters are initialized only if it is necessary.

### Questions
please look at my strengths and weakness sections, and if you can adress the weakness section, i am happy to change my ratings.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors address the challenge of incremental learning, where a model must continually learn new tasks without forgetting previously learned information. While much of the existing research emphasizes improving model stability to retain earlier task knowledge, this paper argues that inter-task differences are a key contributor to forgetting and proposes a novel network design to address this issue.

### Strengths
1. The approach includes two main components: a backbone network that captures invariant features shared across all tasks, and adapters—originally introduced for efficient fine-tuning—that serve as feature modifiers for task-specific information. This design allows the model to learn new tasks while preserving knowledge of prior ones. 

2. The authors also provide insights into compression with KD-based incremental learning, highlighting failures and disadvantages through demo experiments.

### Weaknesses
However, addressing the following concerns could strengthen the paper:

1. The paper's baselines, EWC and LwF, date back to 2017, which limits the study's relevance, given the advancements in incremental learning benchmarks and methods over recent years. Comparing the proposed method with more recent techniques would enhance its impact.

2. The overall approach is not entirely novel, as similar concepts have been extensively explored, especially in meta-learning-based class-incremental learning or dynamic expansion incremental learning approach, which also trains a generalized model and then adapts it to task-specific scenarios. The authors should discuss differences from this approach in depth, such as in [1] and [2].

3. The overall accuracy of the results needs to be more thoroughly addressed to support the paper's claims. For example, in the class incremental learning (CIL) setting, the proposed method reaches only about 68% accuracy on CIFAR-100 for each 10-class increment, while other methods in [1] achieve up to 78% (as shown in Figure 5). This performance gap limits the generalizability of the method. The authors should clarify whether this accuracy gap is due to the network architecture, network constraints, or training strategy.

### Questions
Experimental Clarity: The experimental setup for class-incremental learning (class-IL) is unclear. Task-incremental learning (task-IL) reveals task information, making it feasible for adapters to adjust to task-specific models. However, class-IL does not disclose this information, and the authors have not clearly described how they address this. Without correct task-specific information, adapting the model may not be feasible.

### Soundness
2

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
5

### Summary
Incremental learning is commonly studied problem in machine learning, seeking models that can learn sequentially arriving data without forgetting prior capabilities. Combatting catastrophic forgetting while maintaining plasticity for new tasks is a common challenge, and the authors propose doing so with task-specific adapters, which are used in conjunction with other continual learning methods like LwF or EWC. Several different formulations of adapters (primarily the number of layers) are introduced, as well as different methods of initialization.  Experiments are performed on CIFAR-100 and ImageNet in both task-incremental and class-incremental learning setups, using ResNet architectures and adding the proposed adapters to several different baseline incremental learning methods.

### Strengths
S1. Evaluation protocols: The authors included experiments on both task-incremental learning and class-incremental learning settings. The latter is widely considered to be much harder, with methods that work on task-incremental learning often not generalizing to class-incremental. With the current state of the field, having good results on class-incremental learning is a must for a top-tier conference.

S2. Task order: I also appreciate that the authors analyzed the impact of task order on their method, in particular coarse and iCaRL task ordering instead of the more common default alphabetical ordering. While this effect is not something new from this paper, task order does have a strong impact on results in incremental learning (as confirmed here), and more papers should examine this effect.

S3. Multiple seeds: The authors ran experiments with 10 random seeds, which provides a better sense of consistency. 

S4. Writing: The paper is generally clearly written and well-organized. The proposed method and experimental settings are fairly easy to grasp. However, there still remains a number of typos and mistakes. See non-exhaustive examples listed under “Miscellaneous” under Weaknesses. Also, the presentation of the methodology is a little inconsistent with the experiments, as the methodology primarily focuses on LwF, but the experiments present a variety of baselines, including regularization-base approaches; I recommend generalizing the methodology section.

### Weaknesses
W1. Novelty: The proposed methodology is lacking in novelty. The adapter strategy (within the larger context of expansion-based methods) for continual learning has been explored many times before (e.g. [a], [b]), and after the recent popularity of LoRA for LLMs, LoRA and similar adaptation techniques have been ported over to continual learning many times as well (e.g. [c], but a simple search will yield many more). [a] in particular is very similar to the proposed method, also using a low-rank parameterization inserted between layers of a network to adapt to each task. All of these highly related methods should be discussed and compared with empirically. Claiming to be “among the first to investigate the role of adapters in incremental learning” (line 085) is not appropriate.

W2. Soundness: From Figure 2, it appears that the main difference between the proposed adapters and the more traditional approach is the lack of freezing of main-body weights, allowing the model the plasticity to adapt to new tasks. However, this freezing is precisely what allows such methods to avoid catastrophic forgetting. Instead, it appears that this method is relying on the “base” continual learning method (e.g. LwF) to prevent most of the forgetting, while the adapters simply provide additional capacity. Also, with the importance given to this distinction, I would expect that this design choice of allowing the main network to be fine-tuned be ablated in the experiments section, but I did not see such a comparison. It is unclear how the base network's feature representations are prevented from drifting over time, which would lead to catastrophic forgetting of the base network's features, and thus the adapters' ability to maintain performance on previous tasks. The method seems to be relying on the regularization method to combat forgetting, and thus is not an incremental learning method on its own.

W3. Experiments:
- I have concerns about the chosen set of baselines, which are quite old at this point and not representative of the type of method proposed in this paper. There should be comparisons with other adaptation methods/techniques (see W1).
- While there are some gains when added to some baselines in certain settings, the improvements are not clear cut. The paper admits that its improvements are diminished with more classes, or with harder task orderings. For the ImageNet task-incremental learning results in Table 1, the results are even more uneven. While some form of adapter method does the best after every task i, there’s no consistent winner, which poses a problem in practice when a practitioner must choose a single method. Worse, there many instances in Table 1 where adding adapters actually hurts performance: this can be seen for example in EWC and MAS in Task 2, and LWF-A for every task after Task 6, which is especially concerning since LWF-A is highlighted in the paper as one of the main proposed variants.
- While I appreciate the additional class incremental learning results in the Appendix, the gains from adding the proposed adapters appear to be fairly marginal.

W4. Parameter count:
- Any continual learning method that adds parameters per task will raise concerns due to increasing model size + memory requirements as the number of tasks gets large. Experiments in this paper only go up to 10 tasks, which is quite small. Moreover, any sort of characterization of how many additional parameters are being added per task is sorely missing. It’s very important that the authors add the parameter scaling characteristics of the method to the paper.
- Line 226-227: “When applied to large networks, the number of parameters introduced by adapters becomes negligible” <= This is never demonstrated.

Minor:
- Page limit: The page limit for this year’s ICLR has a recommended cap of 9 pages of main text; exceeding this to use a tenth page should only be for including larger and more detailed figures. This paper leaks over to a tenth page, but I do not think it’s justified in doing so. With some judicious editing/rearrangement, this paper should easily fit in 9 pages (e.g. see white space on page 6).
- The paper’s figures tend to be in the middle of the page. While there isn’t anything inherently wrong with that, I’d recommend putting them at the top of pages (or occasionally the bottom); this should help with the space issues mentioned in the previous bullet, while also making the captions more easily distinguishable from the main body text.
- The experimental results section begins with a hyperparameter sweep for bottleneck dimension and number of layers in the adapter. While this perhaps may have been the first thing the authors did chronologically while conducting this study, I would recommend presenting this as an ablation study after the “main” results instead.
- Fig 4+5: I suggest using more distinct shades for differentiating the different methods in this plot. The chosen colors are little to close, which may be difficult for example for readers with color blindness.

Miscellaneous:
- “cosine similarities” => “cosine similarity”
- Equation 1: While fairly self-explanatory, $\ell_t$ and $\Theta$ are never defined.
- Line 292: “intput”
- Line 313: “Two evaluation protocols are available for incremental learning” => Domain incremental learning is also a common evaluation protocol. In the case of this paper, it’s probably fine choosing only to evaluate on task-incremental and class incremental learning, but the authors should instead say that these are the two chosen for this paper’s experiments.
- Line 318: “We focus on the task-IL where task-IDs remain unknown at inference time” => This is in fact class incremental learning setting, and backwards from the definition given over the past few sentences.
- Line 469: backwards double parentheses
- Table 1: This table would be more digestible if the differences between the baseline method and baseline-A were better highlighted, e.g. by showing the delta. I’d also recommend adding a column for the average across all tasks.
- Line 698: A $\lambda$ of 10K for EWC seems a bit excessive. Also, there should be a table number + label here.

### Questions
Q1: Eq 252: Is $model$ the same as $\phi$, as used in Section 3.2? Or is there another linear projection? Regardless, the notation could be improved to make the connection between the equations on line 258 and 252 (please include equation numbers) more explicit.

Q2: Why is adapter representation differentiation necessary? This isn’t explained well in the methodology. Is this more important when using previous-task alignment instead of random initialization (Section 3.3.2).

Q3: Why do the experiments use a deeper network (ResNet-34) for CIFAR-100, compared with the higher resolution and more complex ImageNet (ResNet-18). This feels a little backwards.

Q4: Figure 4: All methods with adapters noticeably outperform the baseline method (~10%) even after the first task. Why is this case? At 10 classes, there should be no catastrophic forgetting, as there’s only been one task.

Q5: Line 395-6: If it is indeed a capacity issue, then it would seem that using a larger size adapter should lead to improvements. Is this something you’ve tried?

### Soundness
3

### Presentation
3

### Contribution
1
