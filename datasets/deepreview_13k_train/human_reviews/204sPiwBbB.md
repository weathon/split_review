# Learning from others' mistakes: Finetuning machine translation models with span-level error annotations

- Decision: Reject
- Scores: 8, 5, 3, 5

## Abstract
Despite growing interest in incorporating feedback to improve language models, most efforts focus only on sequence-level annotations. 
In this work, we explore the potential of utilizing fine-grained span-level annotations from offline datasets to improve model quality.
We develop a simple finetuning algorithm, called Training with Annotations (TWA), to directly train machine translation models on such annotated data.
TWA utilizes targeted span-level error information while also flexibly learning what to penalize within a span.
Moreover, TWA considers the overall trajectory of a sequence when deciding which non-error spans to utilize as positive signals.
Experiments on English-German and Chinese-English machine translation show that TWA outperforms baselines such as Supervised FineTuning on sequences filtered for quality and Direct Preference Optimization on pairs constructed from the same data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a new method called Training with Annotations (TWA) that leverages the MT evaluation annotation data to improve the quality of machine translation systems. High quality MT evaluation consists of annotation of errors at span-level per example. TWA essentially uses these to annotations to create an additional span level loss while trying to keep 
The baselines consist of supervised fine-tuning approaches and DPO based models. The experiments are carried on two language pairs and sufficient ablation studies are conducted.

### Strengths
The proposed method is indeed novel - use of MQM annotations to train better MT systems is quite understudied and this work improves on that. 

The method looks fairly extensible to other tasks where span level annotations are already available.

The design of the span based loss function carefully considers the potential pitfalls of its inclusion and incorporates additional loss terms to mitigate the same.

### Weaknesses
Proposed experiments have been evaluated on high-resource languages. MQM based data is available for Indic languages (https://aclanthology.org/2023.acl-long.795/), African languages (https://aclanthology.org/2024.naacl-long.334/) as well as previous editions of the Quality Estimation Shared Tasks. Evaluation on a mix of different resourced languages can strengthen the contribution of this work.

Not a serious concern with this regards to the content of this work but proposed method is extensible to language pairs/tasks where such annotated data is already available. Future work could indicate potential ways of including synthetic data/alternatives when such high quality annotations are not available.

### Questions
Questions: 
1. What was the motivation to include a DPO baseline? 
2. [Clarification] in the SFT baseline, does the finetuning of the base model involve training with MT triples from the MQM data (without annotations)?
3. Were there any discussions about evaluation on span-based MT metrics like XCOMET (https://arxiv.org/abs/2310.10482) or GEMBA MQM (https://arxiv.org/abs/2310.13988)?



Suggestions:
1. Please include a few more qualitative examples in the Appendix.
2. Please release the code/path to corresponding data after the process.
3. While there is still no consensus about the quality of translations produced by LLMs, it would be useful to add a comment about the extension of this work to LLMs in the discussion section.
4. To get an idea of the effectiveness of this work with contemporary works, it may be useful to report the performance of a few MT models submitted to the WMT'23 shared tasks (where the outputs are already available)

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work investigates improving machine translation performance through fine-grained, span-level human-crafted annotations. It introduces a hybrid training loss that treats error spans as negative partial samples, ignores tokens after the first error, and considers tokens before the first error as positive samples. This fine-tuning approach is termed TWA. TWA is then compared against a set of newly proposed baselines, demonstrating outstanding performance.

### Strengths
* The paper is easy to follow.
* It motivates exploration of learning from detailed, fine-grained signals.
* The discussion on the importance of allowing the model to learn which tokens in an error span should be penalized is clear and well-motivated. The experiment supporting this claim is appropriately designed.

### Weaknesses
 * Training Data Overlap: MetricX-23 is fine-tuned on MQM WMT’20-’21, and TWA is also trained on this dataset. This overlap suggests that evaluation might leak into training, disqualifying MetricX-23 as an evaluation metric in this setup. Furthermore, while the authors present MetricX-23 as a source-text-ignorant metric, its training on MQM data makes it sensitive to MQM-specific information, thus not a suitable representative of source-text-ignorant metrics. A more appropriate source-text-ignorant metric, not trained on the same data, should be included.
* Motivation for Task: The task is not well-motivated. Obtaining fine-grained annotations is costly, and it’s unclear why methods are needed to utilize this type of supervision. Although this is discussed in the third paragraph of the conclusion, it comes too late (it is better to be addressed in the Introduction), and the motivation largely pertains to other tasks that might benefit from TWA techniques. This raises the question: why focus on machine translation instead of these other tasks?
* Choice of Offline Learning: It’s not well-explained why offline learning is favored over RL-based models. Efficiency might be one reason, which could benefit from further discussion and experimental analysis. Specifically, the memory cost of RL-based methods should be experimentally compared with the proposed approach, controlling for model size and other relevant factors. Furthermore, the possibility of using offline RL to initialize an agent, which is then fine-tuned with online samples, should be discussed.
* Design Choice Clarity: The design choice mentioned in footnote 1 on page 4 lacks adequate explanation. It is unclear why a fixed weight of -5 is used for major errors instead of the actual score of -25. The motivation for this simplification should be clarified.
* Evaluation Choices: The choices of evaluation metrics and experimental designs are not well-justified. The use of Metric-X, which is trained on the same data as the proposed method, is questionable. The lack of justification for not comparing against RL methods is also a concern.
* Statistical Analysis in Section 6.1: The statistical test mentioned in Section 6.1 lacks detail. It’s unclear what test is used or how it’s conducted. More clarity here would improve the reader's understanding, especially when there is only one instance of each model.
* Baseline Selection: The baselines are loosely defined. While there are efforts to select the best variant of DPO, the approaches cited as baselines remain relatively simple and open to criticism. For example, why not consider weighted sampling instead of TWA-seq, or use erroneous samples as negative samples instead of Filter + SFT? Similarly, why not adopt a weighted contrastive learning approach rather than DPO? Additionally, it raises questions as to why RL-based methods are excluded as baselines. Moreover, for baselines that do not require fine-grained supervision, other larger and less costly datasets could be leveraged. Restricting models with fewer training data limitations to the same dataset may be unfair.
* Impact of Ignoring Off-Trajectory Tokens: The observation that ignoring off-trajectory tokens benefits one translation path while impairing another needs further exploration, even though it’s noted as a topic for future work. Given that ignoring these tokens is presented as a critical step—likely essential for En->De to outperform baselines—it would be beneficial to discuss this more thoroughly. Experiments across more translation paths might shed light on this factor’s impact. Additional analysis to identify the underlying reasons is necessary.
* Further Elaboration on Observation in Sec. 6.3: Observation mentioned in Sec. 6.3 would benefit from additional elaboration.
* Experiment in Figure 2: The experiment illustrated in Figure 2 highlights the importance of allowing the model to learn which tokens within an error span should be penalized. While the presentation is intuitive, including more statistical evidence and quantitative analysis would strengthen this point.
* Expansion of Translation Paths and Metrics: It’s suggested to test additional translation paths and incorporate more evaluation metrics, as the two currently provided are not strongly correlated. The inclusion of a source-text-ignorant metric, not trained on MQM data, is crucial.
* Marginal Performance Gap with References: In the setup that utilizes References, the performance gap between TWA and other baselines is minimal. A stability test could help substantiate the claims more effectively.
* Minor Weaknesses:
    * Line 064: “Training with Annotations (TWA)” is repeated (the abbreviation alone suffices) and is incorrectly linked.
    * Lines 124-126: Missing a verb, rendering the sentence incomplete.
    * Unaddressed Observations on TWA: TWA’s performance lagging behind DPO in one experiment is not addressed in the analysis.

### Questions
I would appreciate clarification on the questions raised in the weaknesses section. Additionally, please let me know if there are any other aspects I may have overlooked that could address areas of confusion.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose to train machine learning systems with error annotations, where both the reference translation and a poor translation are given. Here, the poor translation is annotated by humans, indicating which spans of the text are wrong (and how wrong it is). The authors propose to use an unlikelihood loss to discourage the model to generate tokens in the error spans.

### Strengths
1. The authors utilize existing data annotations and show it’s helpful to train machine learning systems.
2. The authors compare their method with DPO.

### Weaknesses
1. Novelty. The main novelty of this work is utilizing additional annotations to improve translation systems, which is not surprising. Otherwise, the proposed unlikelihood training is straightforward.
2. Getting annotations is costly. The authors propose to utilize existing annotations, which is scarce. Although in the limited data setting, the proposed method is better than DPO, it’s likely that DPO is still much better in terms of annotation cost.
3. Relatively weak experimentation. The authors only evaluated two translation directions in one dataset, which may be below standard practice of translation papers.

### Questions
How efficient is TWA training compared with SFT?

### Soundness
2

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
5

### Summary
This paper proposes a fine-grain loss to penalty error during supervised fine-tuning (SFT) for machine translation. The main contribution is to take the annotation of the MQM dataset (fine-grained, human-label translation errors) as both positive and negative supervision during SFT at the token level. The main results of this paper are compared with those of using DPO and SFT in two language directions, EN-DE and ZH-EN, showing some improvements in their setting. Also, ablation studies clearly show the difference among multiple variants of their methods. 

The writing is clear and easy to follow. The method, to some extent, might inspire some developments in nowadays optimization toward human preference. However, I hold some concerns with their motivation and evaluation, see the weakness part.

### Strengths
1. The writing is clear and easy to follow.
2. MQM shows fine-grained error annotation. Exploring and leveraging MQM data for MT training is interesting. Also, it might inspire some research in optimizing translation towards human preferences.
3. Positive results in two language directions under their settings.

### Weaknesses
1. MQM data is hard to largely achieve: Compared to other MT-eval annotation data at the sentence level, like DA, MQM data shows more detailed human evaluation. However, it is also hard to largely achieve (even for the DA dataset, it only covers 10+ languages and hundreds k samples through years of work done by WMT).

2. Feasibility aside, if we only focus on the generality of this technique, this method is hard to generalize to other domains, like QA, as it is hard to say that span annotation also applies to QA data collection.

3. The baseline is not strong: 1) The baseline model leg behind the average performance of WMT submission quite a lot. 2) In Table 3, the SFT setting improves results a lot. This gain from SFT is weird if their base model is strong. It would be much better if they could simply increase the model size and clean data for base model training. 

### Questions
1. In Table 3, the main baseline I wanna see is applying SFT on reference data, while it is missing. I am speculating that the gain of this method is mainly from removing noise (which might even exist in the filtered submission data) based on human annotation. If so, the mechanism of success is far away from guiding translation based on negative signals. To resolve this concern, could you show some results of SFT on reference?

2. As mentioned in Weakness-3, could you show some results of Table-3 when using a stronger model? E.g., apply TWA on M2M100 or NLLB. 

3. In lines 201-202, does it simply indicate truncating loss to the first error token? If so, some loss truncation methods could be compared, like https://arxiv.org/pdf/2407.02208

4. In Table 1 and Table 3, the scores for the base model are not aligned? Could you explain a little bit about my misunderstanding?

### Soundness
2

### Presentation
3

### Contribution
2
