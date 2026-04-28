# Towards Foundation Models for Learning on Tabular Data

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Learning on tabular data underpins numerous real-world applications. Despite considerable efforts in developing effective learning models for tabular data, current transferable tabular models remain in their infancy, limited by either the lack of support for direct instruction following in new tasks or the neglect of acquiring foundational knowledge and capabilities from diverse tabular datasets. In this paper, we propose Tabular Foundation Models (TabFMs) to overcome these limitations. TabFMs harness the potential of generative tabular learning, employing a pre-trained large language model (LLM) as the base model and fine-tuning it using purpose-designed objectives on an extensive range of tabular datasets. This approach endows TabFMs with a profound understanding and universal capabilities essential for learning on tabular data. Our evaluations underscore TabFM’s effectiveness: not only does it significantly excel in instruction-following tasks like zero-shot and in-context inference, but it also showcases performance that approaches, and in instances, even transcends, the renowned yet mysterious closedsource LLMs like GPT-4. Furthermore, when fine-tuning with scarce data, our model achieves remarkable efficiency and maintains competitive performance with abundant training data. Finally, while our results are promising, we also delve into TabFM’s limitations and potential opportunities, aiming to stimulate and expedite future research on developing more potent TabFMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to adapt pretrained large language models (LLMs) to tabular data problems. The proposed adaptation method uses generative modeling of table rows encoded as text with column and task descriptions, and additional loss for reconstructing continuous features. The proposed method applied to the LLaMA 2 7B is tested on the benchmark from prior work on LLMs for tabular data in zero-shot, few-shot and fine-tuning settings.

### Strengths
- The goal of creating tabular foundational models is noteworthy and interesting.
- Numerical loss during finetuning seems to help in adapting language models to numerical data.
- The idea of using next token prediction / generative modeling for adapting text models to tabular data is clear and interesting

### Weaknesses
 - There is a possibility that modern well-trained LLMs like LLaMA memorized the datasets being used as the benchmark in this paper. Almost all datasets were present on the internet (some plentifully) before the knowledge cutoff for those models. Additional experiments on newer datasets or explicit discussion and testing for memorization are necessary to claim remarkable zero-shot performance on tabular tasks.
- Looking at Table 1, the results vary significantly depending on the number of shots (for the same model: see GPT-4 on Diabetes for example), knowing that LLMs are very sensitive to prompting (even prompt formatting `[1]`). Some standard deviation over shot-selection or prompt formats is needed in this table to make conclusions.
- The baselines that propose foundation models for tabular data without LLMs are discussed in related work, but not compared against in the few-shot experiments, I believe this is an important comparison for a paper to claim a "comprehensive comparison".

### Questions
- Could you provide evidence for or against a hypothesis that LLMs (in this case) LLaMA 2 7B memorized popular datasets from the benchmark and the GTL procedure helps with extracting those memorized samples and not using "general knowledge"?
- How does prompt formatting influence zero/few-shot performance?
- How does GTL on top of LLaMA compare to baselines that do not use LLMs, and just use pretraining on multiple tables instead like `[1]` or `[2]`?

Other remarks:
- NODE was introduced in another paper `[3]`

**References**
- `[1]` Yang, Yazheng, et al. "UniTabE: Pretraining a Unified Tabular Encoder for Heterogeneous Tabular Data." arXiv preprint arXiv:2307.09249 (2023).
- `[2]` Zhu, Bingzhao, et al. "XTab: Cross-table Pretraining for Tabular Transformers." arXiv preprint arXiv:2305.06090 (2023).
- `[3]` Popov, Sergei, Stanislav Morozov, and Artem Babenko. "Neural oblivious decision ensembles for deep learning on tabular data." arXiv preprint arXiv:1909.06312 (2019).

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a method called Generative Tabular Learning (GTL) for transforming pretrained large language models (LLM) into foundational models for tabular data problems (TabFM). In other words: `TabFM = PretrainedLLM + GTL`. A given LLM trained with GTL can be applied to new unseen tabular tasks in two ways:
- immediately following instructions in zero-shot and in-context regimes
- or after additional finetuning on the task data

The main components of GTL:
- data: a collected set of 115 public datasets with (available or generated by GPT-4) task and column descriptions.
- the loss is based on:
    - traditional language modeling where tabular objects are represented as token sequences
    - feature reconstruction

The main claims:
- *"This approach endows TabFMs with a profound understanding and universal capabilities essential for learning on tabular data"*
- *"excel in instruction-following tasks like zero-shot and in-context inference"*
- *"achieves remarkable efficiency and maintains competitive performance with abundant training data"*

### Strengths
- The collected set of 115 datasets is a valuable contribution.
- Modulo the data collection, the method itself is simple (in a good way).
- (Table 1) Promising results in the zero-shot and few-shot regimes, where the proposed LLaMA-GTL is clearly better than the vanilla LLaMA.
- I greatly appreciate the appendix in general, and section A.4 in particular. This transparent analysis is a big plus to me.
- The story is mostly easy to follow.

### Weaknesses
 *I am ready to review the changes and raise my score even if the changes will be significant (though here I can speak only for myself). In a nutshell, my main recommendations are to narrow the scope and allocate significantly more space for detailed communication of limitations and missing analysis. Regarding the priorities, to me, the points 1, 2, 4, 5 (no experiments required) are more important than 3 (requires experiments). That said, in my opinion, the paper can significantly win from addressing 3.*

**(1. How to apply the proposed model to new tasks?)** *TL;DR: in my opinion, this is an important question that deserves more discussion (and, perhaps, it should be positioned as a limitation).*

From Section A.3 of the appendix, my impression is that if I, as a researcher or a practitioner, want to use the proposed method as a baseline, I need:
- *"use GPT-4"*
- do *"manual corrections"*
- *"specify the task background"*

The above list looks relatively demanding (compared to traditional models) and giving a lot of room for making performance significantly worse/better without any intentions of doing so. In that regard, TabLLM looks easier to use. I think this aspect deserves more discussion.

**(2. Positioning, story, claims)** *TL;DR: In my opinion, the proposed method and reported results are significantly more limited that can be expected from the title/abstract/claims/story. I suggest making the communication of the scope more precise starting from the title and abstract.*

My first impression was that the paper proposed something very general and powerful (*"Towards **Foundation** Models"*, *"we propose Tabular **Foundation** Models"*, *"TabFMs with a **profound understanding and universal capabilities**"*, *"our model achieves **remarkable efficiency** and maintains **competitive performance with abundant training data**"*, etc.). In particular, I expected that the proposed method was tested against things like gradient-boosted decision trees and modern tabular DL architectures without any significant limitations and according to the standards and datasets established in the corresponding field (e.g. see `[1]` for one of the latest examples where such models are compared against each other). However, in the "All" section of Table 2:
- The number of tasks: 9
- The number of regression tasks: 0
- The maximum dataset size: ~50K objects
- The number of trivial tasks (solvable with 100% accuracy): 2
- Among the remaining 7 tasks, the number of simple tasks (Logistic regression performs well): 3
- The proposed LLaMA-GTL vs. the vanilla LLaMA: 2-wins/6-ties/1-loss
- The number of tasks where the proposed method is the only best solution: 2
- (Less of an issue in the light of the above, but important for making strong claims about the non-few-shot regime) I recommend using more powerful DL baselines, e.g. see `[1]`.

Additionally, the proposed method implies running a large 7B model, annotating tasks and columns, and limiting the number of features to fit in the context size. Based on the above, in my opinion, it is too early to promote the new method in the non-small-data scope.

Personally, I would focus on the positive things: the promising results from Table 1 and the collected dataset. And, based on the reported results, I recommend changing the title, abstract and claims accordingly, so that the terms "few-shot" and "classification" are explicitly communicated starting from the title. To me, a great example of a transparent communication is the paper "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second" by Hollmann et al., where all important things are described in the title and the abstract.

**(3. Methodology)** *TL;DR: the paper introduces many significant changes compared to prior work (e.g. TabLLM): a new backbone, a non-trivial prompt template, language modeling loss, numerical loss. It may be hard to understand what are the important elements of the scheme.*

- Is it necessary for the proposed method to applied to a relatively powerful 7B LLM? Was the T0 model used by TabLLM a bottleneck?
- Prompts are known to have significant effect on the performance of language models `[2]`. In `[3]`, it was shown that the trivial "List" format is already good enough (perhaps, except for the zero-shot regime). Again, this work diverges from the prior work and uses rich prompts insteads. It is unclear whether this is important.
- Additionally, the benchmark from `[3]` may be enough to illustrate the idea of applying LLMs to tabular data for the first time, but overall, to me, it seems to be limited as I explained above. I believe that, in future, the benchmark should be extended. Works like `[1]` and `[4]` may be a source of additional datasets.

**(4. Conceptually important claims)**. In my opinion, the following claims may worth revisiting or clarifying.

*> "Besides, using a text representation enables the easy integration of **crucial** meta information that can hardly be utilized by traditional studies for learning on tabular data, such as feature meanings and background knowledge."*

The quote (implicitly) suggests that the inability of "traditional" models to process textual information is worth addressing. However:
- If a model requires task and feature descriptions to be presented, **it is a limitation** preventing from applying the model to non-annotated tasks. Traditional models are free from this limitation.
- This can be a problem on my side, but I am not aware of studies showing that an average tabular problem contains non-trivial amount of helpful (in terms of task metrics) information in its description. My guess is that it may be true for tiny tasks, but it becomes increasingly non-obvious for larger tasks.

*> "it also showcases performance that approaches, and in instances, even transcends, the renowned yet mysterious closed- source LLMs like GPT-4"*

I recommend providing a relevant citation to support positioning GPT-4 as a strong baseline for the considered scope. Another option is to remove this additional accent on GPT-4 (using it as a baseline is totally fine).

**(5. The "Limitations" paragraph)**. Currently, this paragraph rather discusses future work than limitations. I recommend adding limitations of the method and of the conducted analysis in this paragraph, and move the ideas for future work into a new "future work" paragraph.

### Questions
Please, see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of building tabular foundation models, or neural networks that can operate with high performance across several downstream tabular tasks. The particular approach is to fine tune pretrained LLMs to better handle tabular tasks. In a range of experiments the tactic is examined in the zero shot, in-context learning, and fine-tuning settings.

### Strengths
1. To my knowledge, this paper is original -- the idea of fine tuning LLMs like Llama for general purpose tabular tasks is novel.
2. The quality and clarity of the writing are good.

### Weaknesses
1. The central results in Table 1 are unclear. I think this is in part due to the massive multi-row table and in part due to the hazy conclusions.  
    1. For example, on the Bank data, the only method that ever achieves AUC of 85 is LLaMA-GTL but it does this with no examples (#contexts = 0). Suggesting that LLaMA-GTL is great for this task, but in-context learning doesn't help it.  
    2. On C. Hous. and Car datsets, LLaMA-GTL strictly underperforms baselines with 0 contexts.  
    3. On Diabetes, Heart, Income, and Jungle, LLaMA-GTL again shows no better performance than 0-context baselines

--> This tells a less-than compelling story about when LLaMA-GTL is the right tool. Seemingly for free (no context, no training) existing methods are more general. I do see that the GTL component provides LLaMA with a significant boost in almost all cases. 

2. The  results presented in Table 1 are a weakness of the paper also because the claims made following Table 1 include (i) in-context learning doesn't help; (ii) GTL helps in most zero-shot settings; (iii) GTL helps in few-shot in-context settings; Point (i) is made clearly by the table, but strikes me as a limitation -- foundation models tend to do better with in context examples, if TabFMs don't this needs to be investigated further. Points (ii) and (iii)  are funny comparisons since the number of in-context examples is presented as a control variable, but GTL models have a bunch more training. This may be a strength of GTL models over base models, but this is simply an example of where fine tuning base models makes them better at specific tasks and therefore feels like a less than novel finding.   

3. The results in Table 2 are similarly hard to interpret. See the questions below.

Minor issues not affecting my score:
1. The comparison of the proposed method to the baselines and in various settings are presented in massive and complicated tables. It took me a very long time and repeated readings to follow the rows and columns and draw conclusions. This is a relatively minor point, as I acknowledge that the data itself is there, but I suggest smaller tables or plots/figures for some of the experiments to help the reader draw conclusions and interpret the results faster.  
2. the indices in Section 3 are quite confusing and difficult to follow. I'm fairly certain I understand what goes into these models but these equations in their current form confused rather than clarified the details for me.
3. `We employ LLaMA-2-7B (Touvron et al., 2023) as our base LLM, which will be simply referred to as ’LLaMA’ in the following sections for brevity. Additionally, we denote the obtained TabFM after the GTL stage as LLaMA-GTL` looks like it's repeated on Page 6.

### Questions
1. How is AUC computed with language models? I see in Appendix Figure 4 that there are logits, but I don't follow exactly how they are computed. Can the authors elaborate?  
2. How does GTL work when paired with LLMs other than LLaMA? A little more breadth here could make the story more compelling. I'm sensitive to limited compute resources, but I also think that more than one model would help illuminate when/where GTL can be effective.
3. Can the authors add any intuition or explanation about when TabFM's might be succeeding/failing? For example, do the datasets on which it works well have anything in common (number of features, categorical/numerical features, number of classes, similarity to datasets in the GTL training sets, etc)? Without any discussion or hypotheses around this point, I think the results in this paper seem fragmented and difficult to parse.

I look forward to discussing these questions with the authors and the other reviewers.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to train an LLM-backbone foundation model for tabular data. The premise is that, by including examples from from tabular datasets serialized into text, they can train a model that generalizes well to new tabular datasets in the zero and few-shot setting. They find that their model trained in this way leads to improved generalization on a held out set of tabular tasks compared to tabllm and gpt* models. Additionally, they find their model performs comparably to classic tabular models like LR and xgboost when trained with more data points.

### Strengths
- Tabular data is a widely used data format. Improvements in this area are very important and high impact.
- The presentation of the paper is quite clear and easy to follow.
- The pre-training data set seems comprehensive and collects many relevant dataset for tabular pre-training.
- The results in Table 1 are quite promising -- in the few shot setting, the proposed methods either offers clear gains or is comporable to GPT-4 which is exciting

### Weaknesses
This paper offers promise in terms of performance gains on several tabular benchmarks but currently leaves quite a few questions unanswered about how LLMs like the trained foundation model might be used in place of current tabular models and what the tradeoffs are in leveraging these techniques. 

1. The foundation model is leveraging prior knowledge in the form of feature names + values. What role do these play in generalization to new tasks? If features are anonymous or have values scaled to an unexpected range (common occurances in practice) how much does this hurt generalization? Specifically, how does the model handle situations where feature names are not semantically meaningful or are simply IDs, and how does it perform when numerical features have drastically different scales or units than seen during pre-training? For example, if the model is pre-trained on datasets with heights in centimeters and then encounters a dataset with heights in inches, how does this impact performance? 
2. For tabular learning, the presence of (potentially many) noisy / useless features is quite common. Does this hurt generalization of this method, as the model might pay attention to noisy or useless features? For instance, if a dataset contains many irrelevant features alongside a few highly predictive ones, will the model be able to effectively filter out the noise and focus on the important signals, or will its performance be degraded by attending to the irrelevant features? Furthermore, how does the model's performance change as the number of noisy features increases? 
3. For table 2, I'm a bit concerned about the gap between logistic regression and xgboost on these tasks. It seems like these datasets are simple enough that logistic regression matches xgboost performance. In more complicated real world cases, this gap is often quite greater, as the ability of xgboost to fit complex patterns in the data is needed for good performance. So, I'm concerned the evaluation isn't reflective of many real world uses cases. To be fair, in certain domains, such as medical domains, I've seen results demonstrating logistic regression leads to sota performance, but in many other domains this is not the case, so am unsure how much I can expect the utility of this model to generalize.


Other considerations:
- It's a bit strange to fit the baselines (LR, lightgbm, and xgb) in table 2 with no (?) hyperparameter tuning -- I didn't see a description of this process here. E.g., even with only 64 data points, its often possible to get considerably better results by tuning on LOO or k-fold CV on the training set for instance and considering a couple different hyperparameter combinations. Without this, I'm a somewhat suspicious the true performance of these baslines is a point or two higher than currently presented. 

There's also an additional related work here which could be a useful benchmark: https://arxiv.org/abs/2304.13188

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
