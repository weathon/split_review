# Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3

## Abstract
As an effective alternative to the direct fine-tuning on target tasks in specific languages, cross-lingual transfer addresses the challenges of limited training data by decoupling ``task ability'' and ``language ability'' by fine-tuning on the target task in the source language and another selected task in the target language, respectively. However, they fail to fully separate the task ability from the source language or the language ability from the chosen task. In this paper, we acknowledge the mutual reliance between task ability and language ability and direct our attention toward the gap between the target language and the source language on tasks. As the gap removes the impact of tasks, we assume that it remains consistent across tasks. Based on this assumption, we propose a new cross-lingual transfer method called \texttt{AdaMergeX} that utilizes adaptive adapter merging. By introducing a reference task, we can determine that the divergence of adapters fine-tuned on the reference task in both languages follows the same distribution as the divergence of adapters fine-tuned on the target task in both languages. Hence, we can obtain target adapters by combining the other three adapters. Furthermore, we propose a structure-adaptive adapter merging method. Our empirical results demonstrate that our approach yields new and effective cross-lingual transfer, outperforming existing methods across all settings

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces AdaMergeX, a new cross lingual transfer learning approach. The main idea is to realize that regular fine-tuning on a task consists of two aspects: “task ability”, the ability to train the actual task, and “language ability” the ability to understand the language in which the task was trained. With that assumption authors define a way to train a model on a specific task task and specific language by using another task as pivot to provide the language ability, to provide the task on a different language, and remove the undesired pair pivot task and languages.
This idea is adapted into two existing parameter efficient fine tuning methods, LoRA and (IA)3 and tested in a variety of tasks such as multilingual arithmetic reasoning, multilingual common-sense reasoning, multilingual natural language inference, question-answering and multilingual summarization. The method is compared against five cross-lingual transfer competing techniques, which are beaten by AdaMergeX.
A few ablation studies are presented, showing the generalizability of the approach regardless of the pivot language, using Spanish and Vietnamese instead, and generalizability  in terms of pivot task, comparing the performance using XNLI and XCOPA as reference tasks.
Finally an experiment using T5 instead of LlaMa model is performed, showing the generalizability  in terms of architecture.

### Strengths
The paper is sound and strong.
The idea is cleverly defined, implemented and tested.
The experimentation seems appropriate, it shows that the new approach is effective to perform cross lingual and cross task training.

### Weaknesses
Experimentation on this approach is difficult. All the experiments provide good evidence that support the author's claims, but given the generalizability nature of the approach, more experiments are needed.

The ablation study on adaptive merging method is a bit confusing? What do the authors were expecting? Cross adaptive merging methods is probably a bad idea and your experiments support that.

The experiments on source language generalizability ? Why choose only 2 languages? Do the authors consider that the experiments on Spanish and Vietnamese make the point?

Similar question for XNLI and XCOPA for task generalizability

And for T5.

Do this approach work on Encoder models as well such as XLM or mBERT?

### Questions
The ablation study on adaptive merging method is a bit confusing? What do the authors were expecting? Cross adaptive merging methods is probably a bad idea and your experiments support that.

The experiments on source language generalizability ? Why choose only 2 languages? Do the authors consider that the experiments on Spanish and Vietnamese make the point?

Similar question for XNLI and XCOPA for task generalizability

And for T5.

Do this approach work on Encoder models as well such as XLM or mBERT?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work presents an approach to cross-lingual transfer where the idea is to merge adapters that can deal with 'general processing' of a source language and a target language (eliciting language abilities) further with the task adapter trained on the desired task in the source language (therefore eliciting 'task abilities'). The term 'structure-adaptive' adapter merging from the title and the abstract actually denotes the need to perform merging via different operations, which depends on the nature of the chosen adapter architecture: e.g., LoRA relies on elementwise addition, so the same operation should be used for adapter merging, while IA3 requires elementwise multiplication. As the ablations studies show, doing 'blind' merging that doesn't align with the actual underlying adapter structure yields large task performance drops.

The proposed merging strategy is then applied on several LLMs and mostly compared against other recent (and less sophisticated) merging strategies on several standard cross-lingual transfer tasks, spanning a total of 12 languages. The results show consistent gains over the chosen baselines.

### Strengths
While the paper is generally well written and easy to follow, for each of its strength there is a mirrored weakness. For each strength (S_i), I suggest to check the related weakness (labeled W_i later).

S1. The work connects the ideas of modular and PEFT learning (via adapters such as LoRA and IA3) on LLMs and cross-lingual transfer learning. 

S2. One of the main conceptuals novelties, as claimed by the authors, is the division of information and abilities into 'language abilities' (captured through language adapters via causal language modeling) and 'task abilities' (captured through task-specific tuning). However, while it's interesting to revisit this idea in the context of LLMs, the idea is definitely not novel (see W2).

S3. The main results seem to suggest the gains of the proposed approach over the chosen baselines.

### Weaknesses
W1. The idea of connecting modular and PEFT learning with cross-lingual transfer has been explored before with encoder-only models (a body of work on bottleneck adapters, sparse subnetworks, etc.) as well as encoder-decoder models (e.g., check the work on mmT5). Moreover, even the idea of (simple) adapter merging is not novel and has been proposed, e.g., by Zhang+.

W2. There has been a large body of work that decomposed language and task abilities into dedicated language and task adapters and then performed various operations on such decomposed modules with well defined abilities. Cross-lingual transfer is basically one of the primary applications demonstrating how modularisation helps with postiive transfer. I suggest the readers to check a recent survey paper on modular deep learning of Pfeiffer+ for an overview (e.g., MAD-X work performed exactly this but stacking instead of merging language and task adapters). Overall, the paper doesn't perform a good job in contextualising their work within the wider area where the idea of modularisation for cross-lingual transfer has been extensively researched with encoder-only and encoder-decoder models. This diminishes the novelty of the work substantially.

W3. The gains are reported only over the chosen baselines (which seem most relevant at first), but there's a large body of work on cross-lingual transfer (i.e., with adapters as well as without adapters) that the paper simply ignores. For instance, combining language and task masks as done in the work of Ansell+ (ACL-22) can be seen as a form of direct adapter merging for cross-lingual transfer, and is therefore directly relevant as a baseline. Comparing performance to adapter-based transfer with encoder-only models is also a must, as previous work typically reported much higher absolute scores in general.

W4. The results in absolute terms are quite low - for instance, many XNLI results actually underperform the random baseline (or a majority baseline) in a 3-way classification task such as NLI. The same goes for XCOPA results. There are much higher scores reported on those benchmarks in prior work on cross-lingual transfer learning. Given the reduced novelty and other methods that are very relevant and perform some sort of adapter merging, I fail to see how exactly this approach advances the field.

W5. It is quite intuitive to see that merging adapters via the same technique that merges their parameters with the parameters of the original model will yield the highest performance. While it's nice to see this confirmed empirically, I feel that the paper overclaims this as a contribution (similar to overclaiming the novelty of decoupling learning into language and task adapters). Also, the work only explores adapters that get their parameters merged/composed with the original parameters of the large model, but it doesn't explore other techniques such as bottleneck and serial adapters, or a combination of different architectures (e.g., UniPELT or AutoPEFT).

W6 (Minor). The paper doesn't really evaluate on low-resource languages, but this mostly stems from the limitations of the underlying LLMs that simply cover less languages than models such as mT5, XLM-R, mDeBERTa, etc.

### Questions
Can the authors comment on low performance of LLMs on tasks such as XNLI and XCOPA that often go below the random/majority baseline?

Why haven't the authors compared the results also with encoder-based XLT approaches (e.g., MAD-X is one very relevant approach and there are also improved approaches that build on top of it)?

Have the authors also considered comparing to other adapter aggregation strategies in the context of XLT (e.g., adapting AdapterFusion for XLT)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an adaptive adapter merging method, termed AdaMergeX, for cross-lingual transfer of large language models (LLMs). The authors decompose the abilities of multilingual LLMs into "task ability" and "language ability". AdaMergeX introduces three types of adapters to LLMs, and models the task ability and language ability by different adapter merging strategies of the three adapters. They conduct experiments on five multilingual tasks, and observe improvement over several baselines.

### Strengths
- The idea of adapter merging and ability composite is nice, and it could be useful for efficient cross-lingual transfer for LLMs, which are expensive to fine-tune.
- The structured-adaptive merging methods consider the structure of adapters, and consistently outperforms a strong adapter merging baseline, AriMerge.
- The authors conduct experiments on five multilingual datasets, covering reasoning, natural language understanding, and natural language generation tasks.

### Weaknesses
 - The experimental setup is unclear and confusing. (1) Training data: Since the proposed methods learn task adapters, I would guess it learns on some training data of the downstream tasks. However, Table 1 only provides the details of test data, and it is unclear why the evaluation is conducted on small subsets of the test sets. Specifically, the paper should clarify the size of the training sets used for adapter training for each task. The paper also needs to justify why only subsets of the test data are used for evaluation, especially given that the total test set sizes are not exceptionally large for tasks like XNLI. (2) Baseline setup:  MAD-X[1] adopts a similar idea, and introduces task and language adapters to cross-lingual transfer, which should be the most important baseline. Besides, fine-tune-based cross-lingual transfer methods such as xTune[2], and translate-test[3] should be considered. The setup of the XLT baseline is not clear. If the proposed method uses training data, is XLT evaluated in a few-shot setup as well?
- The results are insufficient to support the claim "AdaMergeX consistently outperforms other state-of-the-art methods". First, the XNLI accuracy scores in Table 2 are too low to compete with random guess, which has 33.3% accuracy. For reference, mT5[4] achieves 85.0 accuracy on zero-shot cross-lingual transfer on XNLI. Besides, regarding XLT as a SOTA cross-lingual transfer method is misleading because a lot of cross-lingual transfer methods achieve better performance. The low XNLI scores raise concerns about the overall effectiveness of the proposed approach, and the comparison to XLT is not convincing given the existence of much stronger baselines. The paper should demonstrate performance on par with or better than established methods on XNLI before claiming state-of-the-art results. Additionally, the paper should include results for more challenging cross-lingual tasks to demonstrate robustness.
- "AdaMerge outperforms cross-lingual transfer methods" is misleading. I would guess the paper focuses on some efficient-training setup, but the results in Table 1 cannot support this claim. The paper needs to clearly define the scope of the work, and if it is indeed focused on efficient training, this should be stated explicitly. The current presentation is misleading because it implies a general superiority over all cross-lingual transfer methods, which is not supported by the experiments.

### Questions
- In Eq.3 and 4, how the symbol "~" is converted to "="?
- What is the relation between AdaMergeX and MAD-X?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies model merging in cross-lingual transfer. The authors propose learning adapters that capture 'task ability' and 'language ability' separately and introduce a novel adaptive adapter merging method called AdaMergeX, which is applied to LoRA adapters and IA3 adapters. The core idea of the paper is to achieve cross-lingual *task* transfer with merging of 3 adapters, namely 2 reference task adapters (1 in source language, 1 in target language), 1 task adapter (in source language for the target task). Element-wise addition/subtraction is applied to LoRA type adapters and element-wise multiplication is applied to IA3 adapters.
The paper examines the proposed method in several cross-lingual transfer tasks and demonstrates that it achieves improved performance.

### Strengths
The paper conducted experiments on a range of cross-lingual transfer tasks for LoRA and IA3. Additionally, the paper proposed an interesting distinction: merging different types of adapters may require different operations.

### Weaknesses
There are several drawbacks in the proposed work:
- Inadequate benchmark / baselines, for example:
    * The paper argues that the lack of enough training data to study standard adapters (Houlsby) merging is unconvincing. (See MAD-X as an example, which is not fundamentally different in terms of training data requirements compared to Houlsby nor this work).
     * The test results are sub-sampled (in paper, "while for XNLI, XLSum, and XQuAD we randomly sample 1000, 500,
and 1000 data points from the whole test set respectively") without convincing justifications.

- Ablations:
    * Even though differences in results between the same task across two languages approximate 'language ability,' such a claim was not carefully examined or discussed. Are the domains of training data the same for two languages (for the same task)? Was any of the cross-lingual data for the reference task machine-translated?
    * Why is the ablation of backbone models (Table 6) evaluated on only a single task with two languages? Given that XNLI contains 15 languages, it's unconvincing that the results generalize across languages, especially when prior tables (e.g., Table 2 or 4) show results across multiple languages.
    * The same question applies to Table 3, where results are only shown for 2 languages (es, fr), and they are not even the same languages as in Table 6 (es, vi). No justifications are provided.

- Inadequate discussions about the proposed work and its relationship to prior work. For example:
    * the training of adapters capturing language ability skills using 'LM objectives' (equivalent to the reference task in the paper) lacks a clear connection to existing literature in cross-lingual transfer, such as MAD-X and LT-SFT.
    * insufficient exploration of its relationship and differences with methods like AdaMerge and Task Arithmetics. The LoRA merging in the proposed work involves element-wise addition/subtraction, which is the same as in Task Arithmetics.
    * imho, one of the core interesting point proposed by the author is different types of adapters requires different merging operation, yet this aspect is not sufficiently studied in the paper.

- Writing:
    * Details of the experiments, such as the backbone model used for the experiments, are scattered throughout the paper, making it very difficult to follow the experiments.
    * Definition of AdaMergeX (adaptive) vs AdaMergeX (cross), Eng-Tune vs Eng-FT etc.
    * There are unclear descriptions of experimental settings, such as of what has been used as reference tasks for specific experiments, including details on the amount of data used and the training process etc.

### Questions
* Why do you randomly sub sample test set for evaluation for  XNLI, XLSum, and XQuAD? What's wrong with evaluating on all test data?
* What hyper-parameters do you use for training?
* What's the reason behind using Llama-2 or T5 as the backbone, where other backbones, especially multilingual backbones are available?


-------------------

Dear authors,
Thank you very much for the additional information. I acknowledged that I've reviewed the rebuttal and updated information.
Best,

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
