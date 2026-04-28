# Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Fine-tuning large pre-trained models has become the \textit{de facto} strategy for developing both task-specific and general-purpose machine learning systems, including developing models that are safe to deploy. 
Despite its clear importance, there has been minimal work that explains how fine-tuning alters the underlying capabilities learned by a model during pretraining: does fine-tuning yield entirely novel capabilities or does it just modulate existing ones?
We address this question empirically in \textit{synthetic, controlled} settings where we can use mechanistic interpretability tools (e.g., network pruning and probing) to understand how the model's underlying capabilities are changing. 
We perform an extensive analysis of the effects of fine-tuning in these settings, and show that: (i) fine-tuning rarely alters the underlying model capabilities; (ii) a minimal transformation, which we call a `wrapper', is typically learned on top of the underlying model capabilities, creating the illusion that they have been modified; and (iii) further fine-tuning on a task where such ``wrapped capabilities'' are relevant leads to sample-efficient revival of the capability, i.e., the model begins reusing these capabilities after only a few gradient steps. 
\textit{This indicates that practitioners can unintentionally remove a model's safety wrapper merely by fine-tuning it on a, e.g., superficially unrelated, downstream task.} 
We additionally perform analysis on language models trained on the TinyStories dataset to support our claims in a more realistic setup.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work applies mechanistic interpretability methods on finetuned language models as an attempt to understand how the finetuning process alters pretrained models. The authors conclude that finetuning with smaller learning rate allows the finetuned model to learn a "wrapper" on top of the existing pretrained model to perform specific finetuned tasks.

### Strengths
I appreciate how the experiment is setup: gradully stepping from a controllable but synthetic setting to a less controllable but realistic setting. The gradual stepping from controllable to uncontrollable settings and the meticulous linking of claim consistency between each experiment makes tracing the arguments and their evidence easy.  The conclusions drawn are well supported by the empirical results. 

I also appreciate how the notion of capability is defined in this work. An exact definition conveys what the authors consider as "capabilities" and their coarse dichotomy into strong and weak relevances.

### Weaknesses
The main (potential) weakness of this work is the conclusion drawn. I personally dislike the usage of "lack of novelty" as a justification to reject a paper. That being said, there is frankly not much to be learned about finetuning from this work. Yes, small finetuning rate would only change the model a little. Yes, the change would be potentially reverted if training on the original pretraining task. Yes, a larger finetuning rate would cause collateral damage, causing existing capabilities to be lost. These are all well-established knowledge about finetuning where plenty of papers have explored. Again, this is not to discredit this entire work. The authors should consider highlighting the newer findings that readers may not already know, perhaps how the distinction between strong and weak relevance would benefit the finetuning of a new capability.

The authors motivate the importance of understanding of the finetuning process by mentioning safety and jailbreaking attacks in the introduction and conclusion. Unfortunately no related experiments are shown.

Last but not least, the authors should include a paragraph in related works discussing on how semi-controllable language models (e.g. transformers training on PCFG and Tracr) have been utilized in model interpretability previously, to help contexualize the usage of mechanistic interpretability techniques (e.g. weight pruning). The authors should also include the baseline of finetuning with a portion of pretrained data mix in, since that would be the most common finetuning technique. Conclusions drawn on such finetuned procedures would be more applicable, compared to purely finetuning on the new domain.

### Questions
(see weaknesses)


Overall this is a good solid and interesting paper. I would like to see it being accepted.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores how fine-tuning impacts the capabilities of large pre-trained models. It uses mechanistic interpretability tools and the technique of reverse fine-tuning to study how fine-tuning affects these capabilities and finds that fine-tuning often adds a minimal transformation, called a "wrapper," on top of the existing capabilities when the learning rate is sufficiently small. They demonstrate this in a synthetic setting with PCFG's initialized with Tracr solutions and in a more realistic setting with the TinyStories dataset.

### Strengths
1. The authors address the critical problem of understanding how fine-tuning impacts models, and specifically try to offer mechanistic insight via a compelling section of techniques (probing, pruning, reverse fine-tuning).
2. I like the TinyStories experiment, where the authors find that the pretraining capability can be recovered via fine-tuning uniquely when the learning rate is small enough, as evidenced by the control model. Importantly, I find it really interesting how in the high learning rate deletion setting, the capability loss for fine-tuning the control and deleted model match each other. I best understood this from Figure 79 on page 53 in the Appendix, which might benefit from being in the main paper. 
3. The authors are incredibly comprehensive over hyperparameters, giving many alternatives in the appendix.

### Weaknesses
My overall analysis is that the authors haven't provided a clear definition of what it means for a capability to have been lost or recoverable

1.  [Experiment 2] I believe the wrapper formalization is inconsistently used throughout the paper. Starting at Definition 2, a wrapper $g$ is composed with $\mathcal{C}$ and is defined as a map acting on the output of a capability ($g$ is unquantified here, and I believe the range should be the domain here). This definition is independent of a model and how it is parameterized. However, in the experiments, the wrapper definition is always a subset of the weights to be pruned. I believe this is not captured as a function of the capability/model output, but rather the function parameterization. As such, probing can not be used as evidence that the model learns a wrapper over the capability.
    - This is not simply fixed by altering the definition to be a change over weights; there is always the wrapper of adding the optimal FT weights and subtracting the current PT weights, which would produce a strongly relevant capability but (I think) would go against the spirit of a wrapper. I believe it is non-trivial to find a definition of wrapper that is 1) covered by pruning and 2) captures the spirit of being a lightweight modification of the model.
    - Is there an example of a fine-tuning capability that can not be obtained by a wrapper under the current or a revised definition? Having this delineation is important to proving something that isn't true by construction.

2.  [Experiment 3] In the abstract and introduction, revival via reverse fine-tuning is discussed as being sample-efficient. Experiment 3 is intended to demonstrate this phenomenon experimentally. However, there is no discussion of sample efficiency here or later in the paper. Specifically, to show that the pretrained capability is actually forgotten, there would need to be a comparison to how much time it takes to learn the pretrained capability, which doesn't exist since the capabilities are directly compiled via Tracr. Even this experiment would be confounded by the fact that the fine-tuned model can be seen as simply a good initialization for learning the pretrained capability from scratch. This sample efficiency analysis is critical since in theory, any capability can be learnt by training for long enough.

3.  [Experiment 4] The linked Figure 8 for the probing analysis does not concern probing. Does this mean to refer to Figure 5? If so, what new information does this section provide that is not captured in Experiment 2, which refers to Figure 5? The analysis and takeaway in this section do not seem grounded in data in the current state.

4.  I found the results in this paper quite difficult to parse. None of these items individually changed my score, but it did make it much harder/time-consuming to parse the message of the results.
    - In Figure 4, (i) through (iv) do not agree on the figure vs the text.
    - Figure 5 does not have a legend and I do not know what it is measuring.
    - Figure 6 does not have an x-axis and I do not know what it is measuring.
    - The plots are out of order, for example, Fig 7 is referenced before Fig 5. This led to some confusion while reading experiments.
    - Plots such as Figures 6, 7, and 8 test for three controlled variables at once and take a lot of effort to parse.
    - Is there a reason the chosen $P(O_{PT})$ is changed from Figure 7b to Figure 8b?
    - The reader is required to parse and remember a lot of notation consistently across the paper. It would be helpful to be more verbose about the notation definitions, especially in plot titles and captions.

### Questions
All questions are addressed in weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzed the changes of a pretrained model during fine-tuning, especially how the capabilities are learned or lost during fine-tuning.

### Strengths
1. I am really interested in this topic as while fine-tuning is important for unleashing LLM's capabilities learned during pretraining, there is little literature on understanding the dynamics during this process. This is also important for how to mitigate forgetting during LLM fine-tuning.

2. The authors proposed some novel synthetic tasks to probe the evolving of capabilities  during LM fine-tuning.

### Weaknesses
1. The presentation of this paper is extremely unclear. I have tried my best to understand the first 5.5 pages with many unclear notations but cannot understand the remaining 2.5 pages. I list some (but not all) unclear points below:
*   $R_{FT, TR}$ and $R_{FT, TE}$ in Section 4 are not clearly defined. It is stated that they contain three elements, but the meaning of these elements is not explained. For instance, what is the precise probabilistic interpretation of each element, and how do they contribute to the overall model of spurious correlation?
*   The characters $L, M, H$ in $P_C^L$ are not defined. It is unclear what these notations represent in the context of the model. Are they related to low, medium, and high probabilities, or do they signify something else entirely? A clear definition is needed to understand their role in the experiments.
*   In Section 4, the relationship between $O_{pre}$ and $O_{ft}$ is confusing. If $O_{pre}$ already contains $b$, what is the specific rationale behind fine-tuning the model on counting $O_{ft}b$? This needs further clarification to understand the experimental design.
*   The sentence "The probability of embedding a spurious correlation in the train/test fine-tuning dataset," is unclear and grammatically incorrect. It should be revised to clearly state what is meant by the probability of embedding a spurious correlation.
*   In Figure 5, the meaning of the different lines is not explained. Without a legend or clear description, it is difficult to interpret the results presented in the figure. What do the different lines represent in terms of experimental parameters or outcomes?

Unclear presentations such as listed above largely downgraded the quality of this paper and I cannot fully understand some of the paper's main claims. I hope the author can thoroughly revise their paper on its presentations.

2. Some related works are missing such as [1][2].

[1] Two-stage LLM Fine-tuning with Less Specialization and More Generalization

[2] Data distributional properties drive emergent incontext learning in transformers

### Questions
Please see the first point in Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
