# Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization

- Decision: Reject
- Scores: 5, 5, 3, 8

## Abstract
Methods for knowledge editing and unlearning in large language models seek to edit or remove undesirable knowledge or capabilities without compromising general language modeling performance. This work investigates how mechanistic interpretability---which, in part, aims to identify model components (circuits) associated to specific interpretable mechanisms that make up a model capability---can improve the precision and effectiveness of editing and unlearning. 
We find a stark difference in unlearning and edit robustness when training components localized by different methods. We highlight an important distinction between methods that localize components based primarily on preserving outputs, and those finding high level mechanisms with predictable intermediate states.
In particular, localizing edits/unlearning to components associated with the \textit{lookup-table mechanism} for factual recall 1) leads to more robust edits/unlearning across different input/output formats, and 2) resists attempts to relearn the unwanted information, while also reducing unintended side effects compared to baselines, on both a sports facts dataset and the CounterFact dataset across multiple models.
We also find that certain localized edits disrupt the latent knowledge in the model more than any other baselines, making unlearning more robust to various attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work explores methods for knowledge editing and unlearning in large language models, focusing on how mechanistic interpretability can enhance the precision and effectiveness of these processes. The study reveals that localizing edits to components associated with lookup-table mechanisms for factual recall leads to more robust unlearning, resisting unwanted information relearning and minimizing side effects. Additionally, certain localized edits disrupt latent knowledge more effectively than other methods, resulting in increased resilience against various attacks.

### Strengths
* Studying unlearning methods from the perspective of knowledge storage and mechanistic interpretability is indeed a very important and promising direction.

* This paper further confirms that causal tracing-based localization methods are not suitable for editing and unlearning tasks.

* The paper is well presented and the literature review is thorough.

* The experimental design is generally comprehensive.

### Weaknesses
1. The test dataset appears to be limited to this triplet format; is it constrained by the knowledge format, and could it be applied to more broadly and flexibly expressed knowledge sentences, such as continuous text, etc.?

2. Manually analyzing and then selecting layers for operations seems to lack convenience and flexibility in the context of large-scale data editing/unlearning.

3. The proposed new unlearning method lacks sufficient originality. There are already some works that attempt unlearning directly from the perspective of mechanistic interpretability, including [2].

4. Knowledge is not necessarily stored entirely in the MLP; there are certain cases where it exists in the attention mechanism [1], yet the method described in the paper only considers knowledge stored in the MLP.

5. There is a lack of discussion on unlearning methods in Representation Engineering [3, 4].

6. Can the proposed method achieve performance advantages on other representative series of transformers, such as LLaMA?

### Questions
Please see the Weaknesses section above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates the effectiveness of mechanistic interpretability techniques in improving the precision and robustness of knowledge editing and unlearning in LLMs. The authors mainly discuss two types of localization methods, i.e., OT techniques that focus on preserving outputs, and mechanistic localization, which identifies high-level mechanisms with predictable intermediate states. They claim in the paper that localizing edits to components associated with the FLU mechanism leads to more robust unlearning across different input/output formats and resists attempts to relearn unwanted information. They conduct experiments on the Sports Facts and CounterFact dataset using Gemma-7B and Gemma-2-9B models.

### Strengths
This paper contains the following several strengths:
+ The paper addresses an important topic by attempting to improve the robustness of knowledge unlearning in LLMs through  localizing edits to components associated with the FLU.
+ The authors provide a in-depth analysis and comparison between mechanistic unlearning and previous OT methods.

### Weaknesses
 + The paper would benefit from a more in-depth theoretical analysis to explain why FLU could inherently lead to more robust unlearning. While the authors claim that targeting the fact lookup components is more effective, they do not provide analysis or proof to support this. The claim that FLU components are the primary locus of factual knowledge requires more rigorous justification, especially considering the distributed nature of knowledge representation in large language models. It would be beneficial to explore potential mechanisms by which edits to FLU components propagate through the network and affect downstream behavior, and how this differs from edits to other components.
+ The experiments are limited, especially limiting itself to Gemma-7B and Gemma-2-9B models and two datasets. The authors could provide a larger variety of models and unlearning tasks in order to better demonstrate the consistency of their findings. The current experimental setup does not fully explore the generalizability of the proposed method across different model architectures, sizes, and training regimes. The choice of datasets also limits the scope of the study, as both Sports Facts and CounterFact are relatively narrow in terms of the types of knowledge they cover. Expanding the experimental scope to include more diverse datasets and tasks would strengthen the claims made in the paper.
+ Can the author provide more ablation study, for example on the loss weights parameter being used in 2.3, so that we could better understand the contribution of each loss in the finetuning process. The lack of a thorough ablation study on the loss function parameters makes it difficult to assess the sensitivity of the method to these hyperparameters. Specifically, the relative weighting of the forget and inject losses could significantly impact the effectiveness of the unlearning process. It is crucial to understand how these parameters interact and how they should be tuned for optimal performance.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This article investigates the performance of various localization methods in unlearning/editing tasks, particularly focusing on their limitations in adapting to shifts in prompting/output distributions and adversarial relearning scenarios. It compares three main approaches: output tracing, attribution patching, and FLU. Through experiments conducted on two models and two datasets, the findings reveal that the component set identified by FLU localization is more closely tied to the factual query process, demonstrating greater robustness and generalization when fine-tuned. Additionally, the authors achieve more efficient parameter editing by controlling model modifications through weight masking.

### Strengths
1. The motivation and approach of this article are interesting, as it breaks down factual recall into more granular steps to enhance the accuracy and generalization of editing methods. 

2. The extensive experiments demonstrate the effectiveness of the proposed approach. The findings indicate that fine-tuning the FLU-related components identified through manual localization effectively eliminates specific knowledge from the model and makes it less susceptible to re-learning.

3. Using multiple-choice questions (MCQs) can help eliminate the influence of input patterns while allowing for a more effective exploration of knowledge deletion. This approach can provide clearer insights into how specific knowledge is affected by unlearning processes.

### Weaknesses
1. Regarding the editing task, only the decline in the original answers is reported, which aligns with the unlearning aspect. However, results seem to lack a demonstration of improvement in the correctness of the new answers. This is significantly related to the performance of the editing task. Specifically, the paper should report the accuracy of the model on the edited facts after the editing process, not just the decrease in accuracy on the original facts. This is crucial to demonstrate that the model is actually learning the new information and not just forgetting the old.

2. Additionally, for the analysis of intermediate representations using probing, this concept is derived from existing work and does not represent a novel contribution to this research. The use of probing techniques to understand model behavior is well-established, and the paper does not present any novel probing methodologies or findings that significantly advance the field. The paper should clarify how the specific probing techniques used here offer unique insights beyond what is already known.

3. [Critical] In the unlearning task, there is no theoretical proof or guarantee that the knowledge is fully forgotten. Since approximate unlearning can be easily exploited, this method is vulnerable. I believe that a theoretical guarantee is crucial for the unlearning task because the security issue is fundamentally a "to be or not to be" problem. The lack of theoretical guarantees makes the method unreliable for applications where complete knowledge removal is required, and the paper should acknowledge this limitation more explicitly.

4. [Critical] No adaptive attack experiments were conducted. The authors performed only standard unlearning/editing experiments, without testing for membership inference or adaptive attacks, despite the fact that approximate unlearning methods are particularly susceptible to adaptive attacks. The absence of adaptive attack evaluations leaves a significant gap in the assessment of the method's robustness. The paper should include evaluations against attacks that are specifically designed to exploit the weaknesses of approximate unlearning methods.

5. [Critical] There is a lack of experiments on adaptive unlearning, which would involve sequentially unlearning specific types of knowledge—for instance, first basketball, then football, and finally table tennis. Would adaptive unlearning impact the efficiency of the unlearning methods? The paper should investigate how the method performs when unlearning is applied sequentially to different types of knowledge, as this is a more realistic scenario in many practical applications.

### Questions
1. In the section defining the method, it mentions, "In practice, we fix τ such that Cτ contains the same number of parameters in OT, FLU, and random localizations." How should this statement be understood? For example, in the counterfact dataset, what are the MLP results using OT and EAP, given that our analysis highlights layers 3-5, 7-10, and 14-17 as the critical MLPs?

2. Could you explain in more detail the process of direct path patching on the counterfact dataset? For example, after obtaining the set of components related to the fact extraction mechanism, how do we replace all edges from each MLP to all components in the set?

3. In the manual localization process, why is only the MLP considered as the localization component, while other methods like EAP and OT do not also set the form to only consider MLP? Instead, they assess both attention heads and MLP components simultaneously?

4. [Critical] Can the authors provide theoretical proof or guarantee to show that the knowledge is forgotten?

5. [Critical] Can the authors provide the experiments of adaptive attack (attackers that easily conquer approximate unlearning )?

6. [Critical] Can the authors provide the experiments of sequential unlearning?

### Soundness
2

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
The authors study whether insights from mechanistic interpretability can improve our ability to perform unlearning or make targeted model edits. More specifically, using a collection of factual recall tasks, the authors study different ways of selecting a subset of the model's parameters to finetune for unlearning or editing certain facts. Building on prior work identifying a subset of model parameters involved in factual recall, the authors show that finetuning only these parameters results in more effective unlearning/model editing than finetuning parameters selected via other techniques. These claims are supported by a variety of analyses, such as robustness to different ways of eliciting the model's factual knowledge and robustness to retraining the model to relearn the facts.

### Strengths
Overall, the results in this paper are very strong, and the suite of evaluations is impressively thorough.
1. The authors do a good job of establishing that finetuning on the "manual interp" subset of parameters results in qualitatively different unlearning dynamics and quantitatively stronger results. The field of interpretability has struggled recently to demonstrate that their insights are useful for downstream tasks in general—and for unlearning/model editing in particular as demonstrated by Hase et al. (2023)—so I expect these results will be a breath of fresh air for the interpretability community.
2. The authors perform a very thorough suite of evaluations showing that mechanistic unlearning more effectively changes knowledge stored in the model weights (see (3) and (4) for more detail). This is another place where the authors set themselves apart from the field: the unlearning literature has often struggled with thoroughly evaluating the efficacy of their methods.
3. I was especially impressed by the relearning evaluations, showing that—when training the model to relearn the unlearned facts—the mechanistically unlearned model relearns the facts much more slowly (figure 2).
4. Also impressive were the results that sweep over the number of masked parameters, revealing qualitative differences in the various unlearning techniques. Figure 5, right, which shows that mechanistic unlearning generalizes to MCQ rephrasing substantially better than any other unlearning technique, was especially striking.

### Weaknesses
Overall, this work's presentation was very poor.
1. Many important details are missing from the main body of the text. (a) The "fact loookup localization" (which is also called "manual interpetability"—why not use one term?) method is entirely explained in an appendix. While it's reasonable to put most of the FLU details in the appendix (since this is a replication of prior work) understanding at a high level what FLU is and how it assigns importance scores to various model components is essential for understanding the rest of the work. Specifically, the method relies on identifying specific layers where the model's internal representations are enriched with factual information, but the exact mechanism for identifying these layers through probing or other techniques is not sufficiently explained in the main text. (b) The definition of the unlearning loss is described only as "the log(1 - p) measure from Mazeika et al."—this is an important part of the method and should be explained. The specific form of 'p' and how it relates to the model's output probabilities needs to be clarified, as this choice can significantly impact the unlearning process.
2. It is very difficult to follow discussions of the tasks. There are two tasks related to sports facts, one related to unlearning facts about basketball athletes (how many athletes? I think this is mentioned later, but it should be included in section 2.1) and one related to editing 16 (random?) athletes to change their sport to "golf." The authors later refer to these tasks with vague phrases like "For editing the subset of athletes..." The authors should instead give distinct names to these two tasks (e.g. "Sports-unlearning" and "Sports-editing") which they use to refer to the tasks throughout the rest of the text. The lack of clear task definitions and consistent naming makes it hard to track the experimental setup and results.
3. Although the results are strong, the authors do not make it easy to tell this from reading the work. For example, the tables of numbers in the first results section are not a reasonable way to present these results. Tables like these are good for when we want to inspect small numerical differences; in contrast here we don't care about small differences (e.g. between forget scores of 0.002 and 0.000) but about large differences (e.g. between MCQ scores of 0.110 and scores >0.5). The authors should choose a different way of presenting these results, perhaps as a bar chart. The current tabular format obscures the key findings and makes it difficult to quickly grasp the magnitude of the differences between methods.
4. Similarly, the authors present results for all three tasks for each of their evaluations, resulting in a large number of figures which are left to the reader to synthesize. This work would be much stronger if the authors found ways of presenting their work that summarized and emphasized the key takeaways. The sheer volume of figures, without clear summarization, makes it challenging to identify the most important results and the overall trends.
5. The main takeaway from the counterfact retraining experiment should have been that this experiment isn't informative, since relearning on some facts doesn't generalize to other facts for *any* of the unlearning techniques. This experiment should therefore be moved into an appendix. The fact that no method shows generalization in the relearning phase suggests that the experiment is not providing useful insights into the unlearning process itself, and thus it distracts from the main findings.

### Questions
(All of my questions were asked in the "weaknesses" section.)

### Soundness
4

### Presentation
2

### Contribution
4
