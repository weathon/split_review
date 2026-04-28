# BAT: Backbone Augmented Training for Adaptations

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Adaptations have enabled efficient training for large backbone models such as
diffusion models for image generation and transformer-based language models.
While various adaptation techniques aim to maximize performance with minimal
computational resources, limited data often leads to challenges like overfitting,
mode collapse, or hallucinations. Recently, a promising solution has emerged in
the form of augmenting adapter datasets using data originally employed to train
backbone models. While this approach has shown potential as a breakthrough, it
often lacks a solid theoretical foundation or well-defined standards for control-
lability. To address these limitations, we establish a comprehensive theoretical
framework for Backbone Augmented Training (BAT). Furthermore, we provide
both theoretical and experimental evidence demonstrating that BAT achieves a
faster convergence rate to optimal adaptation parameters compared to conven-
tional adaptation methods. Our results underscore the potential of backbone aug-
mentation to significantly improve performance, especially when coupled with an
effective and well-designed data selection schema.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Being able to efficiently adapt a pretrained large model for a specific task is extremely useful. The authors propose "Backbone Augmented Training," which selects training data from the original pretraining dataset to add to the finetuning dataset. Authors theoretically motivate using "backbone" training data and show that it approaches the optimal adaptation weights more quickly than naively ignoring the pretraining dataset or randomly selecting pretraining data to use.

### Strengths
- Authors connect their theory to existing methods, like Dreambooth and LoRA. 
- Authors attempt to show results on both image (diffusion model) and language (Llama 2-7B) adaptation settings.

### Weaknesses
 - The paper is very difficult to understand. There is a lot of unnecessary mathematical notation introduced, which obfuscates what is actually happening. Variables should be more descriptive (e.g. $\mathcal D_\text{pretrain}, \mathcal{D}_\text{finetune}$ instead of $\mathcal C, \mathcal G$). The main contributions of this work, Propositions 1 and 2, should have their full statements and assumptions in the main text. Each definition and theorem should have their meaning and importance explained intuitively in words. 
- Evaluations are not convincing. 
  - Why is normalized weight difference a good metric to show in the plots instead of test loss?
  - How much tuning has been done for the method vs the baselines?
  - Even if the proposed method converges slightly faster than the baseline, can't we take additional steps with the baseline to compensate, especially since we don't have to spend compute on data selection?



### Questions
- Fig 1: Why does random augmented training start high? Where is the comparison of loss, which is what we actually care about instead of "normalized weight difference"? Figure caption should be more descriptive, especially as it comes far before any explanation of the method or what the metrics mean. 
- Eq. 1: none of these variables have been defined. Why is this necessary?
- L163: "We do not utilize these schemes or scores in the selection of backbone regularization data, but we follow a similar method in the experiments." Can you explain the specific differences between your method and previously proposed methods?
- L202: "$\theta^A := g(\theta^B)$: what is the intuitive meaning of $g$?
- L217: "compositional approaches between two risks are not valid for some cases." What does this mean?
- L263: what does "epoch error of $\mathcal C$" mean?
- What is an intuitive explanation for Proposition 2?
- Fig. 3: I'm confused by the schematic here. If the optimal $\theta^{A*}$ and $\theta^{bat | A*}$ do not coincide, how is this objective valid? Furthermore, can't we take larger steps with the original adaptation objective since it's flatter, and make the same amount of progress on the loss?
- Why do we care about normalized weight difference, especially since these problems are nonconvex and there are many good solutions?
- How does the proposed method compare against adding a regularization term on the model output, to encourage it to stay close to its pretrained outputs?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores the subject of training adapters for Diffusion models and Language models from limited data, and proposes a data mixing strategy called Backbone Augmented Training that mixes data from the set used in training the original model backbone, into the dataset used for learning adapters. The paper provided a theoretical justification for Backbone Augmented Training, proving that, for Dreambooth-based fine-tuning, and LoRA-based fine-tuning, the proposed method finds a set of weights that converges to an optimal solution on the adaptation tasks (if such a solution can exist).

The paper then explores the viability of the proposed method on learning tasks from the Dreambooth dataset, and a set of language tasks, including MedQuad, WinoGrande, and XSum. The experimental analysis focuses primarily on showing that the proposed method converges faster, according to a normalized weight difference comparing the training weights to those of an optimally trained model.

Experiments appear to show that BAT leads to consistently faster convergence across tasks.

### Strengths
Overall, results in the paper, while showing a promising initial signal for the method---the faster rate of convergence is indeed impressive---can be improved in a few key ways. For example, the selected set of datasets and tasks is a great start towards showing the viability of the method, but while measuring a normalized weight difference to a known good solution is helpful to see faster convergence, it is not by itself the most convincing method to showcase the quality of the found solution.

Recent works have found a surprising behavior for adapters, that the location in weight space of the adapter is unreliable at determining the quality of the adapter at a particular task:

[1] Prompt Waywardness: The Curious Case of Discretized Interpretation of Continuous Prompts, Khashabi et al. 2022.

[2] Understanding Visual Concepts Across Models, Trabucco et al. 2024.

For this reason, I am not convinced that a normalized weight difference is a sufficient evaluation metric to showcase the quality of the solutions found by Backbone Augmented Training, because there are very likely many near-optimal solutions dispersed throughout the weight space at different distances from the initialization of the adapter [2] that have comparable performance. To strengthen the evaluation, the authors could also report domain evaluation metrics, such as FID, and CLIP Scores for the diffusion-based tasks, and relevant NLP metrics for the language tasks.

---

## Originality:

The proposed method is to leverage samples from the pre-training dataset of the foundation model used to initialize the adapter, and mix this data with the target dataset for adaptation. The method is relatively simple as a result, but simplicity alone is not a weakness, and should be considered a strength in cases where the proposed method results in significant improvements in convergence speed and quality.

Adaptation of foundation models is becoming a well-studied problem, with LoRA being the de-facto in most cases, including the diffusion-based and language tasks explored in this paper. The problem statement explored in this paper is not particularly original, but the idea of leveraging the model’s original pre training data rather than generating samples from the model is original.

One important limitation of such an approach (and its theoretical analysis), is the reliance on accessing the model’s pre training data, which is becoming less true as many recent large-scale models are trained on closed-source datasets, including: Flux, SDXL, SD3+, Llama3+. How does the theoretical analysis extend to these cases, where researchers may not know what data the model observed in training?

---

## Quality:

Datasets and baseline in the paper are well selected.

The analysis appears to be of high quality, and the bridge from theory to empirical results by measuring the actual weight difference is a great start to showcase the faster convergence suggested by theory. However, the empirical results can be improved in a few key ways. First, reporting standard evaluation metrics, and showcasing faster convergence in these metrics during optimization is crucial to support the claim being made in this paper that BAT results faster convergence rates.

In addition to understanding the rate of convergence, an important experiment to understand the quality of the solutions found by BAT is to explore the FID vs CLIP Score pareto curve, and the FID vs Inception Score pareto curve, which showcase the tradeoff of image quality vs prompt adherence, and the tradeoff of image quality vs image diversity respectively. The strongest version of this paper would show that BAT systematically improves these pareto curves given fixed adaptation data, and compute budget.

As a final comment on quality, the results of base Dreambooth in Figure 2 are not convincing. The figure shows that Dreambooth-based adaptation is unable to learn to generate the corgi (left) which differs from results previously reported for Dreambooth on the corgi from [3], can this difference be explained?

[3] DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation

---

## Clarity:

The paper is generally organized well, and clearly communicates its ideas in most cases, excluding a few minor locations, where better phrasing would improve clarity. 

Locations where clarity could be improved:

Line 152 (Equation 1) - variables are used without first being introduced.
Line 149-150 - shift and inject are used to describe optimizing the adapter weights for Dreambooth and Textual inversion methods, and I did not catch this on my first pass reading this section.

Line 206 - “parameters that are updated during adaptation” my understanding of this is that this set subtraction is the set of newly added parameters (and doesn’t include parameters from the original model updated as optimization progresses). This is an important distinction, because Dreambooth in its original formulation does not introduce new parameters per se, the entire model is fine-tuned, so this set is empty.

Line 223 - I’m not sure what is meant by `\hat{\theta}^{A}_{n + 1} = …` as my understanding is that the sets of parameters given by \hat{\theta}^{A} and \hat{\theta}^{A} \ \hat{\theta}^{B} are different.

Line 250 - I’m not sure what point is being made in this section that adaptation trainers “have to create the data in most cases” does this refer to Dreambooth-style prior preservation using synthetic examples?

Authors, please follow-up and clarify these sections.

---

## Significance:

Adaptation of foundation models is perhaps one of the most important tasks in modern deep learning, and faster optimization methods that require less data are an important research task. The problem statement is of great importance, and the goal of this paper to analyze and improve convergence rates is well timed. However, limited evaluation and lack of standard metrics, and results showing faster convergence of target metrics, rather than convergence of weight difference, limits the overall significance of the results.

### Weaknesses
Overall, results in the paper, while showing a promising initial signal for the method---the faster rate of convergence is indeed impressive---can be improved in a few key ways. For example, the selected set of datasets and tasks is a great start towards showing the viability of the method, but while measuring a normalized weight difference to a known good solution is helpful to see faster convergence, it is not by itself the most convincing method to showcase the quality of the found solution.

Recent works have found a surprising behavior for adapters, that the location in weight space of the adapter is unreliable at determining the quality of the adapter at a particular task:

[1] Prompt Waywardness: The Curious Case of Discretized Interpretation of Continuous Prompts, Khashabi et al. 2022.

[2] Understanding Visual Concepts Across Models, Trabucco et al. 2024.

For this reason, I am not convinced that a normalized weight difference is a sufficient evaluation metric to showcase the quality of the solutions found by Backbone Augmented Training, because there are very likely many near-optimal solutions dispersed throughout the weight space at different distances from the initialization of the adapter [2] that have comparable performance. To strengthen the evaluation, the authors could also report domain evaluation metrics, such as FID, and CLIP Scores for the diffusion-based tasks, and relevant NLP metrics for the language tasks.

The proposed method is to leverage samples from the pre-training dataset of the foundation model used to initialize the adapter, and mix this data with the target dataset for adaptation. The method is relatively simple as a result, but simplicity alone is not a weakness, and should be considered a strength in cases where the proposed method results in significant improvements in convergence speed and quality.

Adaptation of foundation models is becoming a well-studied problem, with LoRA being the de-facto in most cases, including the diffusion-based and language tasks explored in this paper. The problem statement explored in this paper is not particularly original, but the idea of leveraging the model’s original pre training data rather than generating samples from the model is original.

One important limitation of such an approach (and its theoretical analysis), is the reliance on accessing the model’s pre training data, which is becoming less true as many recent large-scale models are trained on closed-source datasets, including: Flux, SDXL, SD3+, Llama3+. How does the theoretical analysis extend to these cases, where researchers may not know what data the model observed in training?

Datasets and baseline in the paper are well selected.

The analysis appears to be of high quality, and the bridge from theory to empirical results by measuring the actual weight difference is a great start to showcase the faster convergence suggested by theory. However, the empirical results can be improved in a few key ways. First, reporting standard evaluation metrics, and showcasing faster convergence in these metrics during optimization is crucial to support the claim being made in this paper that BAT results faster convergence rates.

In addition to understanding the rate of convergence, an important experiment to understand the quality of the solutions found by BAT is to explore the FID vs CLIP Score pareto curve, and the FID vs Inception Score pareto curve, which showcase the tradeoff of image quality vs prompt adherence, and the tradeoff of image quality vs image diversity respectively. The strongest version of this paper would show that BAT systematically improves these pareto curves given fixed adaptation data, and compute budget.

As a final comment on quality, the results of base Dreambooth in Figure 2 are not convincing. The figure shows that Dreambooth-based adaptation is unable to learn to generate the corgi (left) which differs from results previously reported for Dreambooth on the corgi from [3], can this difference be explained?

[3] DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation

The paper is generally organized well, and clearly communicates its ideas in most cases, excluding a few minor locations, where better phrasing would improve clarity.

Locations where clarity could be improved:

Line 152 (Equation 1) - variables are used without first being introduced.
Line 149-150 - shift and inject are used to describe optimizing the adapter weights for Dreambooth and Textual inversion methods, and I did not catch this on my first pass reading this section.

Line 206 - “parameters that are updated during adaptation” my understanding of this is that this set subtraction is the set of newly added parameters (and doesn’t include parameters from the original model updated as optimization progresses). This is an important distinction, because Dreambooth in its original formulation does not introduce new parameters per se, the entire model is fine-tuned, so this set is empty.

Line 223 - I’m not sure what is meant by `\hat{\theta}^{A}_{n + 1} = …` as my understanding is that the sets of parameters given by \hat{\theta}^{A} and \hat{\theta}^{A} \ \hat{\theta}^{B} are different.

Line 250 - I’m not sure what point is being made in this section that adaptation trainers “have to create the data in most cases” does this refer to Dreambooth-style prior preservation using synthetic examples?

Authors, please follow-up and clarify these sections.

Adaptation of foundation models is perhaps one of the most important tasks in modern deep learning, and faster optimization methods that require less data are an important research task. The problem statement is of great importance, and the goal of this paper to analyze and improve convergence rates is well timed. However, limited evaluation and lack of standard metrics, and results showing faster convergence of target metrics, rather than convergence of weight difference, limits the overall significance of the results.

### Questions
Questions have been woven into the strengths section, see above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper tackles the problem of adapting foundation model training using backbone adapted training data. It introduces the BAT (backbone adapted training) method that selects training data for adaptation. It conducts some experiments with the weight difference metric to showcase results compared to a random selection baseline.

### Strengths
- The paper tackles an important problem surrounding adaptations in current foundation models, both unimodal and multimodal.

- The theoretical backing seems to be quite strong and well presented.

### Weaknesses
 - Writing and Presentation: The overall presentation and story of the paper seem all over the place. It is not easy to follow any of the higher level points made in the theory section and how they connect with the empirical evidence. I would urge the authors to substantially rewrite parts of the results section to ease readability. For example, it is unclear how different parts presented in the theory section have been useful for the main empirical results presented.

- Lack of practically useful experiments / results: Most of the plots look at normalised weight differences, this isn’t particularly useful or exciting, are there results with the y-axis being some performance metric that is known to be a good measure of performance. For example, most adaptation methods test on tasks like MNLI, SST-2, MRPC, CoLA, QNLI etc for language and classification tasks like OxfordPets, ImageNet, DTD, Flowers etc for vision.

- Lack of appropriate baselines: All the results in the paper only compare adding BAT training to methods like LoRA and DoRA, however the improvements yielded by BAT are not compared to other standard adaptation baselines like VeRA, ETHER etc. Further, even the experiments conducted with LoRA and DoRA only measure the normalized weight differences which does not provide any signal on the effectiveness of the method in terms of downstream performance.

- Doesn’t the BAT method effectively use more unique samples for the adaptation data mixture? Wouldn’t that be a major confounder in the paper experiments — don’t we expect performance to get better as we include more relevant training data for the adaptation method? A more appropriate comparison would be to include a baseline that uses the same total number of training samples as BAT, but without selecting from the backbone data. This would help isolate the effect of the BAT selection method versus simply having more training data.

### Questions
- In some cases, the training data of the backbone is not known, for example GPT-4o, Llama-3.2, Gemini etc. In this case, we cannot explicitly do BAT since it relies on the training data of the backbone model right? Could the authors please discuss potential ways to approximate or estimate suitable backbone data when the original training data is not available? For example, are there ways to synthesize or curate proxy data that could still enable BAT-like approaches, while ensuring the overall data distribution remains preserved?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Context and Problem: The paper addresses the challenges faced during the adaptation of large generative models like GPT-3 and diffusion models, where adaptation techniques struggle with issues like mode collapse, knowledge shift, and high computational demands. Existing adaptation strategies either update the backbone model's parameters partially or modify them slightly, often leading to suboptimal performance and inefficiencies.

Solution Proposed: The core contribution is the Backbone Augmented Training (BAT), which integrates additional backbone training data into the adaptation process. BAT is designed to enhance the efficiency and effectiveness of adaptations by improving convergence rates towards optimal adaptation parameters. The paper provides theoretical support for BAT, demonstrating through mathematical proofs that BAT can achieve faster convergence than traditional methods. Empirical validation is also presented, comparing BAT to existing adaptation methods using metrics like cosine similarity and centroid distance on benchmark datasets.

### Strengths
Innovative Approach: BAT introduces a creative solution to the long-standing problem of inefficiency in model adaptations, providing a fresh perspective that leverages existing backbone data effectively.

Solid Theoretical Underpinning: The paper not only proposes a new method but also backs it with rigorous theoretical analysis.

Comprehensive Testing: Extensive empirical tests across different types of models (language and image) and datasets underline the method's versatility and robustness.

### Weaknesses
Potential Overfitting: There is a concern about the potential for overfitting, as BAT integrates more data from the backbone model, which might not always generalize well across diverse tasks.


BAT method require the existence of the backbone model data which might not be the case in some backbone models.


Quality of Backbone Data: The success of BAT heavily relies on the relevance and quality of the backbone data integrated during adaptation. Poor selection or low-quality backbone data could lead to ineffective learning or exacerbate existing issues like mode collapse and overfitting.

### Questions
How do you ensure that the backbone data integrated into BAT is of high quality and relevance to the specific adaptation task? Could you elaborate on any preprocessing or data selection criteria used?


In Figure 1, does a lower weight difference means better convergence rate?   In some tasks it would be better to deviate from the backbone data to solve the task at hand, relying on weight difference for the convergence rate feels like in continual learning where we try to limit weight updates to avoid catastrophic forgetting.

### Soundness
3

### Presentation
3

### Contribution
3
