# Does learning the right latent variables necessarily improve in-context learning?

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 3, 6, 8, 5

## Abstract
\looseness=-1
Large autoregressive models like Transformers can solve tasks through in-context learning (ICL) without learning new weights, suggesting avenues for efficiently solving new tasks. For many tasks, e.g., linear regression, the data factorizes: examples are independent given a task latent that generates the data, e.g., linear coefficients. While an optimal predictor leverages this factorization by inferring task latents, it is unclear if Transformers implicitly do so or if they instead exploit heuristics and statistical shortcuts enabled by attention layers. Both scenarios have inspired active ongoing work. In this paper, we systematically investigate the effect of explicitly inferring task latents. We minimally modify the Transformer architecture with a bottleneck designed to prevent shortcuts in favor of more structured solutions, and then compare performance against standard Transformers across various ICL tasks. Contrary to intuition and some recent works, we find little discernible difference between the two; biasing towards task-relevant latent variables does not lead to better out-of-distribution performance, in general. Curiously, we find that while the bottleneck effectively learns to extract latent task variables from context, downstream processing struggles to utilize them for robust prediction. Our study highlights the intrinsic limitations of Transformers in achieving structured ICL solutions that generalize, and shows that while inferring the right latents aids interpretability, it is not sufficient to alleviate this problem.\blfootnote{$^*$ Equal Contribution.}
\blfootnote{$^\dagger$ Equal Supervision.}
\blfootnote{Correspondence to \href{mailto:sarthmit@gmail.com}{sarthmit@gmail.com}, \href{mailto:eric.elmoznino@gmail.com}{eric.elmoznino@gmail.com} and \href{mailto:leogagnon@gmail.com}{leogagnon@gmail

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies an important problem of whether learning good latent representation improve in context learning. For that, the authors add a bottleneck to Transformers to encourage structured predictions. Experimental results are presented. Interestingly, the experiments show that learning good latent representation does not help with out of distribution predictions nor downstream tasks.

### Strengths
- It is important for the community to learn about such work.
- The problem studied is interesting.

### Weaknesses
The findings from the paper are interesting, but the experiments, while controlled, might not be sufficient to draw such strong conclusions about the general in-context learning (ICL) behavior. The paper's core argument hinges on the idea that good latent representations don't inherently improve ICL without an appropriate prediction function. However, the experimental setup, which uses a bottleneck in Transformers to encourage structured predictions, might be too constrained to generalize to more complex scenarios. The experiments seem to focus on a specific type of latent space and prediction function, and it is unclear how these results would translate to other types of latent spaces or prediction mechanisms. The paper does not explore the possibility of more flexible or adaptive prediction functions that could potentially leverage good latent representations more effectively. The claim that learning good latent representations does not help with out-of-distribution predictions or downstream tasks is a strong one, and the current experiments might not fully support such a broad conclusion. It would be beneficial to see experiments on a wider range of tasks and with different architectures to solidify the findings.

### Questions
The findings from the paper are interesting, do you think that the controlled experiments are enough to draw such a strong conclusions? Or will there be cases where learning good latent representation improves the prediction performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
A commonly believed hypothesis is that Transformers do ICL through brittle statistical shortcuts rather than by inferring the underlying generative latent variables of the task, and that this explains their inability to generalize outside of the training distribution.
This paper attempts to understand if it is true. They minimally modify the Transformer architecture with a bottleneck designed to prevent shortcuts in favor of more structured solutions, and then compare performance against standard Transformers across various ICL tasks. Their empirical simulations suggest that little discernible difference exist between the two different approaches, thus questioning the previous belief.

### Strengths
The strength of this paper is that they provide empirical simulations on their claim. Their plot looks very carefully drawn. The problem seems to be interesting.

### Weaknesses
The major weakness of this paper is its presentation, which is not very clear to the reviewer. In particular, the reviewer felt it very difficult to understand (1) The contributions of this work. (2) The structure and logic of this work. (3) The motivation of this work. Given these concerns, the reviewer believes that the current paper requires significant rewrite to make it publishable at ICLR.

In particular, the author has not highlighted their key contributions in this work at the abstract/introduction part. The motivations seem like a course project rather than a publishable work.

### Questions
Given the above weakness, the reviewer believes that the author needs to clarify (1) what is the contribution and novelty in this work. (2) how is the claim being rejected by the experiments. (3) whether the experiments are scalable to LLMs  (4) what is the motivations in this work and the impact of this work to the research communities.

And at the current stage, the reviewer believes a significant improvement and rewrite is needed to get it publishable.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main goal of this paper is to study the relationship between learning latent variables and in-context learning performance. To do so, the paper compares the in-context learning abilities of implicit and explicit models, where the explicit model has an architecture with a bottleneck designed to explicitly infer the task latents. Furthermore, the paper examines how performance changes in explicit models causally through various ablation studies.

### Strengths
1. The paper clearly describes the procedures and results of the experiments.
2. The paper incorporates various tasks, ranging from simple regression tasks to more realistic tasks such as gene targeting tasks.
3. The paper studies causal relationships between ICL performance and various factors, such as the presence of an auxiliary ground-truth task latent loss.

### Weaknesses
The paper addresses an interesting question, but the robustness of its implications remains unclear. The finding that explicitly learning latent variables does not enhance performance may be limited to the specific tasks chosen for evaluation, especially those where implicit models already perform well. Specifically, the explicit model's bottleneck architecture, which forces the model to compress task information into a low-dimensional latent space, might be a limiting factor. This design choice could prevent the explicit model from capturing the full complexity of certain tasks, particularly those where the relevant information is not easily compressed or represented in a low-dimensional space. Also, the paper lacks a discussion on how observations differ across tasks. For example, in Figures 3 and 4, the performance trends (accuracy gains) of the explicit model and other factors vary inconsistently across task types, yet the paper does not explore how or why these results differ by task. This lack of task-specific analysis makes it difficult to generalize the findings and understand the conditions under which explicit models might be more beneficial.

### Questions
Is it possible to study the task-specific relationships shown in Figures 3 and 4 in more depth? For example, could you provide a detailed analysis of why certain tasks benefit from the explicit model while others do not?
In Figure 4b, can you explain why MLP predictions are generally less effective than those from transformers?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors of this paper propose a hypothesis -- namely, that the in-context learning capabilities of transformers are limited by their tendency to be deceived by shortcuts (as demonstrated in [1]) -- and test it by benchmarking a transformer they introduce to prevent shortcut learning (explicit model) against a standard autoregressive transformer (implicit). The explicit model is a slightly modified architecture in which the parameters that are optimized to perform next-token prediction are not able to attend to specific hidden states, whereas the implicit model can do so. The benchmark is performed over a variety of tasks in in-domain (ID) and out-of-domain (OOD) settings. The results show that the explicit model is not superior to the implicit one on ID data. They show that the bottleneck of the explicit model encodes useful representations of the learned task but the next-token prediction parameters are suboptimal at exploiting it. Additional experiments to investigate the interpretability and scaling properties of the explicit and implicit models are performed.

[1] Large Language Models Can be Lazy Learners: Analyze Shortcuts in In-Context Learning, Tang et al, 2023

### Strengths
* **Originality** This paper brings a new perspective to recent work on the problem of shortcut learning. Designing a network to prevent shortcut learning and applying it in the way the authors have done is novel. Framing the investigation in a parametric vs. non-parametric setting is insightful and highlights the operation of attention mechanisms as a particular feature of interest.
* **Quality** This is a high-quality paper. The evaluation on at least five types of tasks is thorough. The authors' use of tasks with known latents indicates a high level of rigor. The authors state the general hypothesis under investigation and provide additional hypotheses (line 165) about which model -- implicit or explicit -- are best suited to the evaluation tasks. The additional experiments (starting line 294) are informative.
* **Clarity** This paper is clear and well written. The setup of the problem and the motivation for the work is communicated concisely.
* **Significance** The contribution of this paper is a novel perspective on a timely problem. Robustness of large transformers is an area of active investigation -- including, shortcut learning (see [1]) -- and this paper shows to an extent that when a network is constrained in a targeted way, generalization does not necessarily improve.

### Weaknesses
While the overall quality of the paper is quite good, much of the quality can be said to be tactical (i.e. the execution) rather than strategic (i.e. the motivation and contribution). In tactical terms, the paper is beautiful. Strategically, it can be improved.

While I acknowledge and appreciate the principled argument in favor of the explicit model in the context of parametric vs non-parametric learning (see p. on line 70, Section 3, and Figure 1), I believe the paper would be very much improved if it verified empirically that the explicit model is itself resistant to shortcut learning in the presence of **injected** shortcuts. Whereas [1] injects shortcuts ("triggers") into data in an ICL setting, the work presented here appears to use datasets without such injections. Creating, if necessary, a synthetic dataset for evaluating robustness to shortcuts, and empirically demonstrating that the explicit model is resistant to shortcuts would strengthen the paper by showing a method by which existing large-scale models might be made resistant to shortcuts. Further showing that the explicit model exhibited consistent resistance to shortcuts as the model size increases would be a substantial contribution. Finally, showing this would provide solid empirical ground on which the argument in p. on line 70 rests.

I would prefer that the authors removed "commonly" from their conclusion (line 512). It's non-controversial that shortcuts are a likely explanation for well-demonstrated non-robustness of transformers to incidental variations of their inputs. In the context of the sentence on line 512, however, the use of "commonly" can be taken to imply that most people believe that shortcut learning is the reason for poor OOD generalization. If that particular view w.r.t. OOD generalization is commonly held, I would expect there to be be some literature -- particularly since [1] was published in 2023 -- claiming exactly that. If it exists, it should be cited in the introduction.

Nit: The classification tasks in the first row of Figure 4 are missing the label on the Y axis.

### Questions
1. Do you have results comparing the explicit model's performance to the implicit model on a task in which triggers have been deliberately injected? If you do, please report them here. If they show that the explicit model is robust to shortcuts, I would find the result compelling.
2. Beyond what you argue in the paragraph starting on line 70, does your understanding of OOD generalization include robustness to variation of incidental features on ID data?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the role that learning ground-truth task vectors plays for out-of-domain generalization in the in-context learning framework. For this purpose, the authors compare a traditional transformer (referred to as the “implicit model”) and a similar model with a bottleneck in its architecture (the “explicit model”).
They empirically find that the implicit model does not perform better than the explicit model, on the OOD setup, even though the implicit model correctly learns a relatively good representation of the ground-truth task vector. They thus demonstrate that access to the task vector is not sufficient for OOD generalization in the ICL framework.

### Strengths
Writing: The paper is accessible and easy to read, which, however, is also facilitated due to the nature of the content. The overall structure is straightforward and easy to follow.
The extensive use of bar-plots makes it convenient to understand the experimental results.

Significance: The question whether ICL can be accurately described via task vectors is certainly interesting and important. Clearly stating this question is thus a central contribution of this paper. I also appreciate that the authors present a negative result. The paper also presents a new experimental setup, compared to for instante that in the paper “In-Context Learning Creates Task Vectors” by Hendel et al.

### Weaknesses
In summary, I mainly miss a theoretical framework or at least some mathematical justifications for the things you claim and investigate. Without them a lot of your arguments felt only heuristically motivated and shallow.

First, there are no theoretical results referenced or provided that support the premise that the constrained architecture should generalize better in the first place. The paper would benefit a lot from including mathematical reasoning in that direction. Given that the premise that learning an explicit representation of the task vector is necessary (not sufficient, that’s clear) for generalization is not well-supported in the first place, the results from Figure 2, which refute this premise, cannot be seen as an interesting contribution.

You should also be careful with the general statement that using parametric assumptions inevitably leads to better generalization than relying on non-parametric ones. It is, for instance, well-known that the posterior predictive of a Bayesian Linear Regression model is in fact equal to the posterior predictive of a Gaussian Process with an appropriate covariance function. The paper should thus state much more clearly, what is meant by “the model takes shortcuts”.

Furthermore, the results displayed in figure 4 do not provide as much evidence as claimed in the text for the hypothesis that the model accurately learns the task vector since the discrepancy compared to your trivial baseline is, except for the linear and sinusoidal case, not that large and, furthermore, using the ground-truth decoding function does not yield great benefits except for the linear and sinusoidal cases. 

There is further little evidence that the explicit model does not also utilize task vectors in some way or another as your counterfactual approach targets interpretability, which is, however, a different question. On the contrary, the results from “In-Context Learning Creates Task Vectors” are still very valid evidence that “implicit” transformers do in fact use task vectors. 

There are further several practical issues with the experiments: 
1.) The number of tasks you consider is quite small 
2.) The dimensionality of the data-points, which you set to 1 or 2  (see Appendix) is also very restricted
3.) You only consider a single and quite limited way of generating OOD samples for each task.

Finally, some sections of the paper are a bit lengthy or perhaps even unnecessary in the main body of the paper, such as the results displayed in figure 5, or the section on Meta-Learning in the related-works part. 

I also have a few issues with the reproducibility of your results:
1.) The code is not provided
2.) Please explicitly mention how many parameters your models have and on how many samples they are trained
3.) You should at least mention what the error bars in your plots represent, i.e. the standard error or the IQR or something else?

There are also a few typos, grammatical issues, and notational errors in the manuscript. For example when denoting functions or in the text on the axes of the plots. 

Finally, using a blogpost or a Wikipedia Article as a reference might be a possibility to give the reader a pointer to an accessible source of information, but it should clearly not be used as a sole reference.

As a small detail, I also find it a bit unusual that you neither use weight decay nor a learning rate schedule in your training.

### Questions
What is the evidence to believe in the first place that learning task vectors might improve generalization? And, especially, what is the evidence that not learning it leads to poor generalization? 

You should also be more careful with the claim that parametric models generalize better than non-parametric ones in OOD scenarios, or, alternatively, also support this claim.

The paper would clearly benefit from providing more empirical evidence for the fact that the task vectors are actually always learned well by the explicit model. 

Please also provide more evidence that the explicit model learns the task vector *better than* the implicit one.

The scale of the experiments could be improved in several dimensions (please refer to the "weakness" section)

I also think that the paper would benefit from carefully reading it again to fix typos and other small issues and from shortening it to the recommended length of nine pages. 

Please also take the reproducibility issues from above into consideration, with releasing the code being the most important point.

### Soundness
2

### Presentation
3

### Contribution
2
